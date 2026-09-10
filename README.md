# Oscar Zhu

I study Mathematical Sciences and Financial Engineering at Washington University in St. Louis. I build tools that work locally, explain their assumptions, and fail safely — native Mac apps, quantitative software, and a growing set of small Linux system-diagnostic CLIs.

[Portfolio](https://zhuhroscar-tech.github.io) · [LinkedIn](https://www.linkedin.com/in/huairuizhu/)

## Linux diagnostic CLIs

Small, focused, read-only-by-default command-line tools that walk a real
multi-layer diagnostic chain in one command instead of by hand. Each one:
targets a documented, recurring pain point; ships tested (CI on real Linux
runners); and is installable via `pip` or a standalone zipapp.

### [privaudit](https://github.com/zhuhroscar-tech/privaudit)
Local mic/camera access history for Linux, built on PipeWire — the missing OverSight/Android-privacy-dashboard equivalent.

### [reboot-safety-check](https://github.com/zhuhroscar-tech/reboot-safety-check)
Warns about DKMS/kernel-module problems for an installed-but-not-yet-booted kernel, before you reboot into it.

### [trim-doctor](https://github.com/zhuhroscar-tech/trim-doctor)
Verifies the full SSD TRIM/discard passthrough chain — device support, LUKS, LVM, and mount options — in one command.

### [unmount-doctor](https://github.com/zhuhroscar-tech/unmount-doctor)
Explains which process is holding a Linux mount point busy, and why, in plain language (`fuser`/`lsof` translated).

### [zram-doctor](https://github.com/zhuhroscar-tech/zram-doctor)
Detects drift between `zram-generator.conf` and the actually-running zram device(s).

### [usbsmart-doctor](https://github.com/zhuhroscar-tech/usbsmart-doctor)
Finds the `smartctl -d` device type a USB drive's bridge chip needs and prints a clean SMART health report.

`Python` `Linux` `CLI` `Read-only diagnostics` — source, tests, CI, and a downloadable release/checksum on every repo above.

## macOS & quantitative software

### [ItoCanvas](https://github.com/zhuhroscar-tech/ItoCanvas)
A native, offline options laboratory for macOS. Prices European options with Black–Scholes–Merton, calculates Greeks and implied volatility, builds multi-leg strategies, and maps spot/volatility scenarios.

`Swift` `SwiftUI` `Quantitative finance` `Local-first`

[Source](https://github.com/zhuhroscar-tech/ItoCanvas) · [Latest release](https://github.com/zhuhroscar-tech/ItoCanvas/releases/latest)

### [DualTyper](https://github.com/zhuhroscar-tech/dualTyper)
A macOS menu-bar translator for explicit text selections. Uses Apple's on-device Translation framework, rechecks the selected text before editing, and avoids secure fields.

`Swift` `SwiftUI` `Accessibility` `Apple Translation`

[Source](https://github.com/zhuhroscar-tech/dualTyper) · [Free prerelease](https://github.com/zhuhroscar-tech/dualTyper/releases/tag/v0.3.0)

## How I like to build

- Keep user data on the device when the product allows it.
- Test the numerical and failure-prone parts, not only the happy path.
- Publish real limitations alongside releases.
- Prefer focused tools over crowded feature lists.

## Currently

I'm improving small macOS products and a set of Linux system tools, and exploring the overlap between software, markets, and decision-making. I'm open to internship conversations in software engineering, quantitative finance, and analytical product work.
