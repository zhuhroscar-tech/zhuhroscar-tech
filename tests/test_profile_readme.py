from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README_FILES = (ROOT / "README.md", ROOT / "README.zh-CN.md")

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


if __name__ == "__main__":
    unittest.main()
