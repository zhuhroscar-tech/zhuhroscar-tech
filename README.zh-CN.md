[![English](https://img.shields.io/badge/English-555555?style=flat)](README.md) [![简体中文](https://img.shields.io/badge/简体中文-555555?style=flat)](README.zh-CN.md)

# Oscar Zhu

我开发位于**机器学习可靠性、量化决策和原生 Apple/Linux 工具交叉点**的软件。目前在圣路易斯华盛顿大学学习数学科学与金融工程。

[个人网站](https://zhuhroscar-tech.github.io) · [LinkedIn](https://www.linkedin.com/in/huairuizhu/) · [发布历史](CHANGELOG.md) · [许可证](LICENSE)

下面每个项目都有完整的 README——安装方法、示例、验证状态、已知限制，没有一个是没有测试支撑的空壳。

## 推荐从这里开始

- [**ItoCanvas**](https://github.com/zhuhroscar-tech/ItoCanvas) — 离线 macOS 期权分析工具，支持 Black–Scholes–Merton 定价、Greeks、隐含波动率、策略和情景分析。
- [**token-telescope**](https://github.com/zhuhroscar-tech/token-telescope) — 非常轻量（34MB）的 macOS 菜单栏小工具，实时显示 ChatGPT + Claude 订阅用量，无需 API Key、无需终端。
- [**numguard**](https://github.com/zhuhroscar-tech/numguard) — 使用高精度独立参考计算和对抗性测试数据检查机器学习数值计算内核。
- [**recallwatch**](https://github.com/zhuhroscar-tech/recallwatch) — 检测近似最近邻索引中的尾部查询召回率下降。

## 📈 量化金融

定价、组合跟踪、决策支持工具——这里没有任何工具会替你下单或提供投资建议。

| 项目 | 功能 |
|---|---|
| [ItoCanvas](https://github.com/zhuhroscar-tech/ItoCanvas) | 原生离线 macOS 期权分析工具：Black–Scholes–Merton 定价、Greeks、隐含波动率、策略盈亏、情景热力图。 |
| [portfolio-performance](https://github.com/zhuhroscar-tech/portfolio-performance) | 仅显示百分比的组合表现页面，从券商交易记录生成——可以放心链接到简历里，绝不展示美元金额或账号。 |

## 🍎 macOS 应用

体积小、原生（Swift/Python + AppKit）、以菜单栏为主的工具——没有 Electron，占用极小。

| 项目 | 功能 |
|---|---|
| [token-telescope](https://github.com/zhuhroscar-tech/token-telescope) | 实时显示 ChatGPT + Claude 订阅用量的菜单栏小工具，用真实账号登录，无需 API Key。 |
| [stashbar](https://github.com/zhuhroscar-tech/stashbar) | 给菜单栏加一个"抽屉"——把状态图标收进一个托盘图标里，不用退出背后的 App，专为刘海屏 MacBook 设计。 |
| [ScreenDimmer](https://github.com/zhuhroscar-tech/ScreenDimmer) | 用一个滑块同时调暗折叠屏/多显示器组合的亮度，并根据折叠屏连接状态自动切换 Safari 缩放比例。 |
| [dualTyper](https://github.com/zhuhroscar-tech/dualTyper) | 隐私优先的菜单栏翻译工具，只翻译你明确选中的文字，使用 Apple 端侧 Translation framework。 |
| [sleepguard](https://github.com/zhuhroscar-tech/sleepguard) | 只读检查工具，找出到底是哪个进程在阻止你的 Mac 进入睡眠。*（开发预览版）* |

## 🩺 系统诊断 — macOS

用真实证据（而非猜测）回答"这个卷为什么弹不出来 / 卸载不了 / 备份不了"的 CLI 工具。

| 项目 | 功能 |
|---|---|
| [mac-volume-doctor](https://github.com/zhuhroscar-tech/mac-volume-doctor) | 统一的 macOS 卷诊断工具，覆盖 Time Machine 目标盘、本地快照、Spotlight 索引、DMG/稀疏映像繁忙挂载点。 |

## 🐧 系统诊断 — Linux

用内核/systemd/设备的真实证据，一条命令解释某个具体故障的单一用途 CLI 工具。

| 项目 | 功能 |
|---|---|
| [systemd-crashloop](https://github.com/zhuhroscar-tech/systemd-crashloop) | 用 unit 状态和最近的日志证据解释 systemd 服务失败原因。 |
| [oom-postmortem](https://github.com/zhuhroscar-tech/oom-postmortem) | 从内核证据、cgroup 状态和进程上下文解释 OOM 被杀的原因。 |
| [trim-doctor](https://github.com/zhuhroscar-tech/trim-doctor) | 验证完整的 SSD TRIM/discard 传递链路：设备、LUKS、LVM、挂载选项。 |
| [zram-doctor](https://github.com/zhuhroscar-tech/zram-doctor) | 检测 `zram-generator.conf` 配置和实际运行中 zram 设备之间的偏差。 |
| [enospc-doctor](https://github.com/zhuhroscar-tech/enospc-doctor) | 从块、inode、已删除文件、预留空间等角度诊断"设备空间不足"错误。 |
| [unmount-doctor](https://github.com/zhuhroscar-tech/unmount-doctor) | 解释是哪个进程占用了某个挂载点/路径，以及为什么。 |
| [usbsmart-doctor](https://github.com/zhuhroscar-tech/usbsmart-doctor) | 找到 USB 桥接芯片需要的 `smartctl -d` 设备类型，输出干净的 SMART 健康报告。 |
| [nft-splitbrain](https://github.com/zhuhroscar-tech/nft-splitbrain) | 找出 iptables-legacy、iptables-nft、nftables 防火墙状态之间的不一致。 |
| [nm-portable](https://github.com/zhuhroscar-tech/nm-portable) | 迁移到另一台机器前，检查 NetworkManager 连接配置文件。 |
| [locale-doctor](https://github.com/zhuhroscar-tech/locale-doctor) | 诊断 shell 和 SSH 会话里的 locale 警告和编码不匹配问题。 |
| [reboot-safety-check](https://github.com/zhuhroscar-tech/reboot-safety-check) | 在你重启进入一个刚安装但还没启动过的内核之前，提前警告 DKMS/内核模块问题。 |
| [resume-timer-audit](https://github.com/zhuhroscar-tech/resume-timer-audit) | 检查挂起/恢复后一起触发的 systemd 定时器。 |
| [privaudit](https://github.com/zhuhroscar-tech/privaudit) | 基于 PipeWire 在本地记录 Linux 麦克风和摄像头访问历史——Linux 上缺失的 OverSight 等价工具。 |

## 🔬 机器学习与数值正确性研究

针对 NumPy/PyTorch/tokenizers 中真实、可复现 bug 的独立验证工具和防护——每一个都引用上游 issue，并用从零实现的参考计算来验证，而不是让库自己给自己的作业打分。

| 项目 | 功能 |
|---|---|
| [numguard](https://github.com/zhuhroscar-tech/numguard) | 用高精度参考实现检查朴素 vs 数值稳定的机器学习内核（softmax、log-sum-exp、交叉熵、方差）。 |
| [numpy-correctness-guards](https://github.com/zhuhroscar-tech/numpy-correctness-guards) | 整合的 NumPy 正确性防护工具集，共享 CLI 和测试套件。 |
| [torch-correctness-guards](https://github.com/zhuhroscar-tech/torch-correctness-guards) | 整合的 PyTorch 正确性诊断和调用点防护工具集。 |
| [einsum-oracle](https://github.com/zhuhroscar-tech/einsum-oracle) | 精确动态规划 oracle，验证 `numpy.einsum_path` 的张量收缩顺序是否真正最优。 |
| [qdrift](https://github.com/zhuhroscar-tech/qdrift) | affine INT8 量化运算的精确 oracle 正确性检查工具。 |
| [blasdrift](https://github.com/zhuhroscar-tech/blasdrift) | 检测 NumPy 基于 BLAS 的运算与独立精确参考之间、跨 BLAS 后端的浮点数漂移。 |
| [recallwatch](https://github.com/zhuhroscar-tech/recallwatch) | ANN 索引的分段召回率漂移监控——在用户发现之前捕捉尾部查询召回率下降。 |
| [rng-leak-audit](https://github.com/zhuhroscar-tech/rng-leak-audit) | 检测并中和 PyTorch DataLoader 静默泄漏全局 RNG 状态的问题。 |
| [bytelevel-guard](https://github.com/zhuhroscar-tech/bytelevel-guard) | 在上线前检测 ByteLevel-BPE 新增 token 的解码损坏风险。 |
| [causality-audit](https://github.com/zhuhroscar-tech/causality-audit) | 针对序列模型层的双次前向传播前缀不变性（因果泄漏）审计。 |
| [starveguard](https://github.com/zhuhroscar-tech/starveguard) | 模拟并审计优先队列调度器的饥饿问题（对应一个真实的 vLLM bug）。 |

## 🛠 开发者与 Agent 工具

| 项目 | 功能 |
|---|---|
| [safari-mcp](https://github.com/zhuhroscar-tech/safari-mcp) | 通过 JXA 驱动 macOS 上的 Safari.app——CLI、Python 库、MCP server，使用你真实的已登录会话。 |
| [llm-quota-mcp](https://github.com/zhuhroscar-tech/llm-quota-mcp) | 以 CLI、Python 库、MCP server 的形式跟踪 LLM API 速率限制剩余额度和重置时间。 |

## 🌐 网站

| 项目 | 功能 |
|---|---|
| [pace-website](https://github.com/zhuhroscar-tech/pace-website) | Pace——面向大学生的隐私优先自适应学习伴侣。 |

## 我关注的方向

- 数值正确性、静默错误检测和可复现的机器学习实验。
- 支持离线运行、明确说明限制并安全失败的工具。
- 在目标操作系统上验证 macOS 和 Linux 的实际行为。
- 用真实测试支撑的小型专注软件，而不是夸大的完整性声明。

欢迎交流软件工程、量化金融、机器学习基础设施和分析型产品方向的机会。
