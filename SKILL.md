---
name: paper-polishing-chinese
description: >
  中文学术论文语言润色技能，专为经济学等社会科学领域的中文学位论文和期刊投稿设计。用于中文学术润色、Introduction 结构重组、研究谜题与文献缺口提炼、逻辑衔接、标点数字规范、学术表达习惯修正，以及核心概念定义、术语边界和机制句去空转检查。主干只保留原则、流程与导航，细则通过 references 懒加载。
---

# 中文学术论文语言润色

处理语言、概念边界、论证结构和表达层面的优化，不改研究立场、事实口径或论证结论。

## 常驻主干

1. **准确第一**：不改变原意，不替作者偷换概念。
2. **硬规则先行**：先查硬规则，再做风格与句法润色。
3. **概念先于句子**：核心概念、变量口径或机制含义不清时，先澄清再润色。
4. **叙事优先**：输出可直接入文的连续学术叙述，避免流程图口吻。
5. **问而不猜**：事实边界、术语角色或比较口径不清时，提示用户确认。
6. **懒加载优先**：`SKILL.md` 只保留导航；细则一律按任务读取 `references/`。
7. **结构先于润句**：涉及 Introduction 重写或压缩时，先对齐研究对象、决策节点、文献缺口、识别设计、主要结果与贡献，再处理局部句法。

## 默认执行顺序

1. 识别任务类型：全文润色、局部润色、Introduction 结构重组、英译中母语化、格式规范化、概念界定检查。
2. 先执行硬规则：
   - 读取 `references/hard-rules-chinese-academic.md`
   - 必要时同时读取 `references/prohibited-wording.md`
3. 涉及文献综述、Introduction、理论机制或任何带引文的学术改写时：
   - 必须读取 `references/citation-claim-density.md`
   - 逐项核对研究主体或比较对象、结论方向、具体结果与证据边界
4. 涉及 Introduction 撰写、重写、压缩、段落重组、研究问题提炼或贡献定位时：
   - 必须读取 `references/introduction-argument-architecture.md`
   - 必须同时读取 `references/word-precision.md`，检查指标简称、比较方向、因果动词、机制词、比喻和强调词
   - 先核对开篇现象、研究谜题、文献缺口、制度或冲击、识别设计、主要结果与贡献是否沿同一决策节点和传导链展开
5. 再检查概念边界与反模板化：
   - 读取 `references/concept-boundary-academic.md`
   - 需要风格去模板化时读取 `references/anti-template-academic.md`
6. 再做语言层润色：
   - 按需读取 `references/word-precision.md`
   - 按需读取 `references/sentence-structure.md`
   - 按需读取 `references/colloquial-to-formal.md`
   - 按需读取 `references/academic-conventions.md`
   - 格式任务再读取 `references/punctuation-rules.md`
7. 默认只输出可直接入文版本；仅在用户要求时输出逐条台账。
8. 如需 `.docx` 修订稿，直接转交 `docx` 技能原生流程，不在本技能重复展开。

## 默认扫描重点

- **硬规则重点**：`assumption / hypothesis` 区分、空泛强化词禁用、比较句量化、程序性免责句删除、政策脚注正式来源、实证模型符号与脚标解释。
- **文献引用重点**：研究主体或比较对象、结论方向、具体结果、证据边界，以及引文与紧邻主张的一致性。
- **Introduction 架构重点**：开篇结果范围、可识别决策节点、文献缺口、传导链、识别设计、主要结果和贡献之间的一致性。
- **用词精度重点**：指标简称保留比较方向，因果动词匹配识别强度，机制词保持具体，修辞性动词不替代可观察结果。
- **概念边界重点**：核心概念先定义、术语角色不滑动、大词空转检测、机制句必须落地。
- **反模板化重点**：连接词密度、翻译腔介词链、升维词谨慎使用、论证边界显化。

## 懒加载索引

- `references/hard-rules-chinese-academic.md`：硬规则细化与可执行判定。
- `references/prohibited-wording.md`：禁忌用语 A/B 分级及替换策略。
- `references/citation-claim-density.md`：文献结论的最小信息单元、引文分组规则和交付前逐句核查；文献综述、Introduction、理论机制及带引文改写时必读。
- `references/introduction-argument-architecture.md`：Introduction 的结果范围、研究谜题、文献缺口、传导链、识别设计、主要结果和贡献对齐规则；Introduction 撰写、重写、压缩或段落重组时必读。
- `references/concept-boundary-academic.md`：概念边界检查最小集。
- `references/anti-template-academic.md`：学术版反模板化最小集。
- `references/word-precision.md`：指标简称、比较方向、证据强度、因果动词、机制概念、修辞性动词与术语口径；Introduction 任务必读，其他用词任务按需读取。
- `references/sentence-structure.md`：句式与段落衔接。
- `references/colloquial-to-formal.md`：去口语化与去营销化。
- `references/academic-conventions.md`：学术表达规范。
- `references/punctuation-rules.md`：标点与数字规范。
- `references/high-frequency-lexicon.md`：候选表达词库，仅在需要备选措辞时读取。

## 关键提醒

- 润色只改语言与表达，不替作者扩写新论点。
- Introduction 结构调整只重组已有且有证据支持的主张；缺少结果、识别或文献依据时，标记缺口并提示作者确认。
- 发现概念冲突或事实口径风险时，先提示，不强行润句子。
- 标题公式、内容运营模板和非学术文案技巧不属于本技能范围。
