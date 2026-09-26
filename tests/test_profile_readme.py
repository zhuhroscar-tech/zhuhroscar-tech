from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_FILES = (ROOT / "README.md", ROOT / "README.zh-CN.md")
LICENSE_FILE = ROOT / "LICENSE"
CHANGELOG_FILE = ROOT / "CHANGELOG.md"
WORKFLOW_FILE = ROOT / ".github" / "workflows" / "validate.yml"

ARCHIVED_CONSOLIDATION_MEMBERS = {
    "mac-dmg-doctor",
    "mac-spotlight-doctor",
    "mac-tm-doctor",
    "mac-tm-snapshot-doctor",
    "torch-optim-introspection-guard",
    "torch-take-along-dim-oob-guard",
    "torch-numpy-stream-shuffle-guard",
}

REQUIRED_UMBRELLAS = {
    "mac-volume-doctor",
    "torch-correctness-guards",
    "numpy-correctness-guards",
}


def _readmes() -> dict[str, str]:
    return {path.name: path.read_text(encoding="utf-8") for path in README_FILES}


def _repo_links(markdown: str) -> set[str]:
    return set(re.findall(r"https://github\.com/zhuhroscar-tech/([A-Za-z0-9_.-]+)", markdown))


class ProfileReadmeContractTests(unittest.TestCase):
    def test_profile_does_not_promote_archived_consolidation_members(self) -> None:
        for name, markdown in _readmes().items():
            with self.subTest(readme=name):
                links = _repo_links(markdown)
                stale = sorted(links & ARCHIVED_CONSOLIDATION_MEMBERS)
                self.assertEqual(stale, [], f"{name} still links archived repos: {stale}")

    def test_profile_points_to_consolidated_umbrella_repositories(self) -> None:
        for name, markdown in _readmes().items():
            with self.subTest(readme=name):
                links = _repo_links(markdown)
                missing = sorted(REQUIRED_UMBRELLAS - links)
                self.assertEqual(missing, [], f"{name} is missing umbrella repo links: {missing}")

    def test_bilingual_readmes_link_each_other(self) -> None:
        for name, markdown in _readmes().items():
            with self.subTest(readme=name):
                self.assertIn("README.md", markdown, f"{name} should link the English README")
                self.assertIn("README.zh-CN.md", markdown, f"{name} should link the Simplified Chinese README")

    def test_repository_has_clear_mit_license(self) -> None:
        self.assertTrue(LICENSE_FILE.exists(), "profile repo should include a LICENSE file")
        license_text = LICENSE_FILE.read_text(encoding="utf-8")
        self.assertIn("MIT License", license_text)
        self.assertIn("Copyright (c) 2026 Oscar Zhu", license_text)

    def test_readmes_link_release_history_and_license(self) -> None:
        for name, markdown in _readmes().items():
            with self.subTest(readme=name):
                self.assertIn("CHANGELOG.md", markdown, f"{name} should link release history")
                self.assertIn("LICENSE", markdown, f"{name} should link the license")

    def test_profile_uses_current_academic_program_copy(self) -> None:
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        chinese = (ROOT / "README.zh-CN.md").read_text(encoding="utf-8")

        self.assertIn("Mathematics and Financial Engineering", english)
        self.assertNotIn("Mathematical Sciences", english)
        self.assertIn("数学与金融工程", chinese)
        self.assertNotIn("数学科学与金融工程", chinese)

    def test_changelog_documents_current_release(self) -> None:
        self.assertTrue(CHANGELOG_FILE.exists(), "profile repo should include a CHANGELOG")
        changelog = CHANGELOG_FILE.read_text(encoding="utf-8")
        self.assertIn("## v0.1.3", changelog)
        self.assertIn("## v0.1.2", changelog)
        self.assertIn("## v0.1.1", changelog)
        self.assertIn("## v0.1.0", changelog)

    def test_validation_workflow_runs_for_release_tags(self) -> None:
        workflow = WORKFLOW_FILE.read_text(encoding="utf-8")
        self.assertIn("branches: [main]", workflow)
        self.assertIn("tags:", workflow)
        self.assertIn("'v*'", workflow)


if __name__ == "__main__":
    unittest.main()
