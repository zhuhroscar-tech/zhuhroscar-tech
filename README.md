[![English](https://img.shields.io/badge/English-555555?style=flat)](README.md) [![简体中文](https://img.shields.io/badge/简体中文-555555?style=flat)](README.zh-CN.md)

# Oscar Zhu

I build software at the boundary of **machine learning reliability, quantitative decision-making, and native Apple/Linux tools**. I study Mathematical Sciences and Financial Engineering at Washington University in St. Louis.

[Portfolio](https://zhuhroscar-tech.github.io) · [LinkedIn](https://www.linkedin.com/in/huairuizhu/) · [Release history](CHANGELOG.md) · [License](LICENSE)

Every project below has a real README with installation instructions, examples, verification status, and known limitations — no project here is a stub or a claim without a test suite behind it.

## Start here

- [**ItoCanvas**](https://github.com/zhuhroscar-tech/ItoCanvas) — offline macOS options laboratory for Black–Scholes–Merton pricing, Greeks, implied volatility, strategies, and scenario analysis.
- [**token-telescope**](https://github.com/zhuhroscar-tech/token-telescope) — tiny (34MB) macOS menu bar widget for live ChatGPT + Claude subscription usage, no API keys or terminal required.
- [**numguard**](https://github.com/zhuhroscar-tech/numguard) — high-precision checks for numerical ML kernels, with independent reference calculations and adversarial fixtures.
- [**recallwatch**](https://github.com/zhuhroscar-tech/recallwatch) — detects tail-query recall collapse in approximate-nearest-neighbor indexes.

## 📈 Quantitative finance

Pricing, portfolio tracking, and decision-support tools — nothing here trades for you or gives investment advice.

| Project | What it does |
|---|---|
| [ItoCanvas](https://github.com/zhuhroscar-tech/ItoCanvas) | Native offline macOS options lab: Black–Scholes–Merton pricing, Greeks, implied volatility, strategy payoffs, scenario heatmaps. |
| [portfolio-performance](https://github.com/zhuhroscar-tech/portfolio-performance) | Percentage-only portfolio performance page generated from brokerage transaction history — safe to link from a resume, never shows dollar amounts or account numbers. |

## 🍎 macOS apps

Small, native (Swift/Python + AppKit), menu-bar-first utilities — no Electron, minimal footprint.

| Project | What it does |
|---|---|
| [token-telescope](https://github.com/zhuhroscar-tech/token-telescope) | Menu bar widget for live ChatGPT + Claude subscription usage. Sign in with your real account, no API keys. |
| [stashbar](https://github.com/zhuhroscar-tech/stashbar) | A "drawer" for your menu bar — stash status icons behind one tray icon on notched MacBooks without quitting the apps behind them. |
| [ScreenDimmer](https://github.com/zhuhroscar-tech/ScreenDimmer) | Dims foldable/multi-display setups together with one slider; syncs Safari's zoom level to the foldable connection state. |
| [dualTyper](https://github.com/zhuhroscar-tech/dualTyper) | Privacy-first menu-bar translator using Apple's on-device Translation framework, only on text you explicitly select. |
| [sleepguard](https://github.com/zhuhroscar-tech/sleepguard) | Read-only inspector that names the process actually preventing your Mac from sleeping. *(development preview)* |

## 🩺 System diagnostics — macOS

CLI tools that answer "why won't this unmount / eject / back up" with real evidence, not guesses.

| Project | What it does |
|---|---|
| [mac-volume-doctor](https://github.com/zhuhroscar-tech/mac-volume-doctor) | Unified macOS volume diagnostics for Time Machine destinations, local snapshots, Spotlight indexing, and busy DMG/sparse-image mountpoints. |

## 🐧 System diagnostics — Linux

Single-purpose CLIs that explain a specific failure mode from real kernel/systemd/device evidence, in one command.

| Project | What it does |
|---|---|
| [systemd-crashloop](https://github.com/zhuhroscar-tech/systemd-crashloop) | Explains failed systemd services using unit state and recent journal evidence. |
| [oom-postmortem](https://github.com/zhuhroscar-tech/oom-postmortem) | Explains OOM kills from kernel evidence, cgroup state, and process context. |
| [trim-doctor](https://github.com/zhuhroscar-tech/trim-doctor) | Verifies the full SSD TRIM/discard passthrough chain: device, LUKS, LVM, mount options. |
| [zram-doctor](https://github.com/zhuhroscar-tech/zram-doctor) | Detects drift between `zram-generator.conf` and the actually-running zram device(s). |
| [enospc-doctor](https://github.com/zhuhroscar-tech/enospc-doctor) | Diagnoses "No space left on device" across blocks, inodes, deleted files, reserved space. |
| [unmount-doctor](https://github.com/zhuhroscar-tech/unmount-doctor) | Explains which process is holding a mount point/path busy, and why. |
| [usbsmart-doctor](https://github.com/zhuhroscar-tech/usbsmart-doctor) | Finds the right `smartctl -d` device type for a USB bridge chip and prints a clean SMART report. |
| [nft-splitbrain](https://github.com/zhuhroscar-tech/nft-splitbrain) | Finds mismatches between iptables-legacy, iptables-nft, and nftables firewall state. |
| [nm-portable](https://github.com/zhuhroscar-tech/nm-portable) | Audits NetworkManager connection files before migrating them to another machine. |
| [locale-doctor](https://github.com/zhuhroscar-tech/locale-doctor) | Diagnoses locale warnings and encoding mismatches in shells and SSH sessions. |
| [reboot-safety-check](https://github.com/zhuhroscar-tech/reboot-safety-check) | Warns about DKMS/kernel-module problems for an installed-but-not-yet-booted kernel, before you reboot into it. |
| [resume-timer-audit](https://github.com/zhuhroscar-tech/resume-timer-audit) | Audits systemd timers that all fire together right after suspend/resume. |
| [privaudit](https://github.com/zhuhroscar-tech/privaudit) | Local microphone/camera access history built on PipeWire — the missing OverSight equivalent for Linux. |

## 🔬 ML & numerical correctness research

Independent oracles and guards for real, reproducible bugs in NumPy/PyTorch/tokenizers — each one cites the upstream issue and verifies against a from-scratch reference calculation rather than trusting the library to grade its own homework.

| Project | What it does |
|---|---|
| [numguard](https://github.com/zhuhroscar-tech/numguard) | Audits naive vs. numerically-stable ML kernels (softmax, log-sum-exp, cross-entropy, variance) against a high-precision reference. |
| [numpy-correctness-guards](https://github.com/zhuhroscar-tech/numpy-correctness-guards) | Consolidated NumPy correctness guards with a shared CLI and test suite. |
| [torch-correctness-guards](https://github.com/zhuhroscar-tech/torch-correctness-guards) | Consolidated PyTorch correctness diagnostics and call-site guards. |
| [einsum-oracle](https://github.com/zhuhroscar-tech/einsum-oracle) | Exact dynamic-programming oracle verifying `numpy.einsum_path`'s contraction-order optimality. |
| [qdrift](https://github.com/zhuhroscar-tech/qdrift) | Exact-oracle correctness checker for affine INT8 quantization arithmetic. |
| [blasdrift](https://github.com/zhuhroscar-tech/blasdrift) | Detects floating-point drift between NumPy's BLAS-backed ops and an independent exact reference, across backends. |
| [recallwatch](https://github.com/zhuhroscar-tech/recallwatch) | Segmented recall-drift monitor for ANN indexes — catches tail-query recall collapse before users do. |
| [rng-leak-audit](https://github.com/zhuhroscar-tech/rng-leak-audit) | Detects and neutralizes PyTorch DataLoader's silent global-RNG-state leak. |
| [bytelevel-guard](https://github.com/zhuhroscar-tech/bytelevel-guard) | Detects ByteLevel-BPE added-token decode corruption before it ships. |
| [causality-audit](https://github.com/zhuhroscar-tech/causality-audit) | Two-forward-pass prefix-invariance (causal-leakage) audit for sequence-model layers. |
| [starveguard](https://github.com/zhuhroscar-tech/starveguard) | Simulates and audits priority-queue scheduler starvation (models a real vLLM bug). |

## 🛠 Developer & agent tooling

| Project | What it does |
|---|---|
| [safari-mcp](https://github.com/zhuhroscar-tech/safari-mcp) | Drives Safari.app on macOS via JXA — CLI, Python library, and MCP server, using your real logged-in session. |
| [llm-quota-mcp](https://github.com/zhuhroscar-tech/llm-quota-mcp) | Tracks remaining LLM API rate-limit quota and reset times as a CLI, Python library, and MCP server. |

## 🌐 Websites

| Project | What it does |
|---|---|
| [pace-website](https://github.com/zhuhroscar-tech/pace-website) | Pace — a privacy-first adaptive study companion for college students. |

## What I care about

- Numerical correctness, silent failure detection, and reproducible ML experiments.
- Tools that work offline, explain their limits, and fail safely.
- macOS and Linux behavior verified on the operating system where it matters.
- Small, focused software with real tests rather than claims of completeness.

I'm open to conversations about software engineering, quantitative finance, ML infrastructure, and analytical product work.
