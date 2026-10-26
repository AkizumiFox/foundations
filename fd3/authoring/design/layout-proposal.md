# fd3 *Number Systems*: re-cut layout proposal (The Natural Numbers, The Integers, The Rationals, Ordered Fields and Sequences, The Real Numbers from Cauchy Sequences, The Complete Ordered Field)

**Status.** **已核准（approved 2026-10-26）**。作者在 2026-10-26 回答了 §7 的四個問題（見 §0），本檔是 fd3 re-cut 結構提交的依據，地位等同 fd2 的 `layout-six-chapters.md`。結構提交已完成（§9）；之後依 §8 逐章 deepen。原提案的狀態行：「提案，尚未核准（2026-10-26）。在作者核准、並回答 §7 的問題之前，`fd3/src`、其他書、atlas 一律不動。」

**Conventions.**（沿用 fd2 的 re-cut）
- 節號按位置計。
- **標籤一律不改名**，包括 `omega` 系列（正文說 ℕ，標籤仍是 `thm-omega-*`）與 slug 不再對應檔名的練習標籤。
- 「Now」為目前主線字數（到 `## Exercises` 為止，`tools/check_structure.py --book fd3 --words`）；「Target」依 5,000 字上限。
- 鷹架等級依 STYLE §11.4：**full** = `[Scratch work]` + method box + Givens/Goal + 兩個 worked example；**Idea** = 短 Idea 加回指；**terse** = 只有證明。
- 新 method box 的標籤在 S1 命名；下文寫的是暫定名。

---

## 0. 作者的決定（2026-10-26，verbatim）

| 問題 | 作者的回答（verbatim） | 執行 |
|---|---|---|
| Q1 ℕ 的立足點 | 「多留一小節」 | ℕ 取為 Peano 系統；ZF 公理、von Neumann ω、Kuratowski 序對、遞移集、tuple 的集合編碼移到 ST.1（停放於 `fd3/authoring/parked/st/`）。**但 Chapter 1 保留一小節 1.5 "Where ℕ Comes From"**：不證明，只講想法（集合是原料、ω 是最小的歸納集、序對也是集合），全部指向 ST。這是 §7 Q1 的 (b) 案，取代原建議的 (a)。 |
| Q2 第 3 章 | 「整章移到 fd5 (Recommended)」 | 方案 A：舊 3.2–3.5 成為 fd5 Chapter 1（F3.5 → F5.1），fd5 原有各章順延一章；只有帶餘除法（舊 3.1）留在 fd3，成為 2.5。 |
| Q3 ℤ 與 ℚ | 「分兩章 (Recommended)」 | Chapter 2 The Integers、Chapter 3 The Rationals；新 atlas id F3.11 給 The Rationals。 |
| Q4 Dedekind 分割 | 「整章移到 ST (Recommended)」 | 舊 Chapter 7 整章停放到 ST（`fd3/authoring/parked/st/ch07-reals-dedekind-cuts/`），atlas F3.3 → ST.1。 |

**調整後的 Chapter 1**（取代 §3 的 Chapter 1 表，其餘各章照 §3）：

| § | Title | 內容 | Pipeline |
|---|---|---|---|
| 1.1 | Peano's Axioms and Induction | 同 §3 | F |
| 1.2 | Recursion; Addition and Multiplication | 同 §3 | F |
| 1.3 | Order and Well-Ordering | 同 §3 | F |
| 1.4 | All Peano Systems Are Alike | 同 §3 | F |
| 1.5 | Where ℕ Comes From | **新的一小節，不含證明、不含帶標籤的結果**：集合是原料（公理說哪些集合存在）；ω 是最小的歸納集（0 = ∅、S(x) = x ∪ {x}），所以 (ω, 0, S) 是一個 Peano 系統，而 1.4 說它是唯一的（同構意義下）；序對也是集合（Kuratowski）。每個證明都在 ST.1；舊文逐字停放在 `fd3/authoring/parked/st/`（from-1.1 … from-1.6）。約 2,000–3,000 字。Time 約加 2 h core / 3 h full。 | F（新寫） |

ZF 的證明一律停放（`parked/st/`），不放進 1.5。

---

## 1. 為什麼要重切

**作者的話（verbatim）。** fd2 因為「我覺得 fd2 好像有太多不必要的太難的知識了」而重切成六章、難度適中的書；現在作者說「fd3 也照這樣開始做」。和 fd2 一樣，第一步是這份版面提案。

**fd3 的定位不變**：從 ℕ 建出 ℤ、ℚ、ℝ，證明 ℝ 是完備有序體且唯一。要拿掉的是偏離這條主線、或對讀完 fd1、fd2 的讀者太重的部分。

**量測（2026-10-26）。**
- 7 章、37 節，主線約 **191,000 字**：Ch1 34,751、Ch2 31,316、Ch3 24,740、Ch4 26,540、Ch5 26,715、Ch6 23,483、Ch7 23,781。
- 各章 Time 合計：主線 **150 h core / 210 h full**；加上選讀的 Ch7，是 175 / 240。
- 三份稽核都發現同一件事：**37 節沒有任何 `[Scratch work]`、Givens/Goal 或 `exm-method-*`**（grep 為 0；fd2 有 174 處 method 引用）。證明方法只出現在章首的「Named moves」條列裡。每一步推理都掛一個 `@prp-ordered-ring-rules (x)` 之類的引用（Ch5 平均約每 34 字一個）。這些都不符合 fd2 的寫法。

## 2. 各章診斷（摘要）

| 章 | 判斷 | 理由 |
|---|---|---|
| Ch1 The ZF Fragment and the von Neumann Natural Numbers (F3.1) | **砍半**：ZF 與 von Neumann 的部分移到 ST.1；保留 Peano 系統、遞迴、算術、序、範疇性 | 1.1–1.3 的形式公理、Kuratowski 序對、遞移集對「建出 ℝ」都不是必要的；ST.1 本來就寫著「revisits F3.1」。真正被下游大量引用的是 1.5–1.7 的結果（`cor-omega-identification` (b) 約 52 次） |
| Ch2 Building ℤ and ℚ (F3.2) | **保留，全章修剪**；2.3 一分為二；ℤ 與 ℚ 分成兩章 | 這是全系列的樞紐（`prp-ring-algebra` ≈168、`prp-ordered-ring-rules` ≈166 次引用），不能動內容，只能修剪 |
| Ch3 Divisibility and Congruences (F3.5) | **移出到 fd5**，只把 3.1（帶餘除法）留在 ℤ 那一章 | fd3 主線只用到它四次（5.2 一步、6.4、6.5 一個例子、4.6 R1），真正的使用者是 fd5（286 次引用）。3.4 的抽象理想對這個階段太難，到了 fd5 才有第二個實例 F[x]/(f) |
| Ch4 Ordered Fields and Sequences (F3.9) | **整章保留，輕度修剪** | Ch5–6、AN1.2、AN1.11、fd4、fd5 都引用它。4.3 是 fd2 寫法的好範例 |
| Ch5 Reals from Cauchy (F3.10) | **6 → 5 節**：舊 5.5（ℝ 的 Cauchy 完備性）移到 AN1；改寫 LUB，直接用有理端點二分法證明 | `thm-constructed-reals-cauchy-complete` 沒有任何下游引用，AN1.2 從 LUB 自己證 Cauchy 判準。5.2 改用逐項證環律，拿掉對 F3.5 理想的依賴 |
| Ch6 The Complete Ordered Field Is Unique (F3.4) | **5 → 3 節**：ℚ(√2) 移到 fd5、ℝ(x) 移到 AN1.11；6.5 壓縮併入 6.3 | 6.4 是系列裡第三次出現的 ℝ(x)/ℚ(t)；6.5 講模型與一致性，太抽象，又沒有問題驅動 |
| Ch7 Dedekind Cuts (F3.3, optional) | **整章停放到 ST** | fd3 之外沒有任何 `@fd3:` 引用它；它是同一個物件的第二種建構，乘法的符號分案又冗長 |

## 3. 建議目錄

**共 6 章、22 節，主線約 107,000 字，約 100 h core / 146 h full。** Ch4–6 保留原章號，所以下游「Chapter 4/5/6」的指標都不必改（§4.6）。

### Chapter 1. The Natural Numbers (F3.1), `ch01-natural-numbers/`（原 `ch01-zf-and-natural-numbers/`）

Time：約 **18 h core / 25 h full**（原 30/40）。ℕ 取為一個**假設的 Peano 系統**，它從 (Z1)–(Z7) 的存在證明延到 ST.1（§7 Q1）。這樣一來，「用 fd2 的 ℕ ⊆ ℝ 去建 ℝ」的循環疑慮不靠 ZF 也能消除。

| § | Title | 內容（一行） | 主要來源與標籤 | Method box／鷹架 | Now → Target | Pipeline |
|---|---|---|---|---|---|---|
| 1.1 | Peano's Axioms and Induction | 為什麼現在需要 ℕ 的公理（要建 ℝ，就不能拿 ℝ 裡的 ℕ 當起點）；Peano 系統、各公理互相獨立、性質形式的歸納、唯一前驅 | 舊 1.4 的 `def-peano-system`、`exm-peano-axioms-independent`；舊 1.3 的 `thm-omega-induction`（重述為 Peano 系統上的定理）；唯一前驅（標籤 S1 決定） | `exm-method-induction-step` 回指 fd2（Idea）；full | ≈ 2,500 移入 → 4,500 | F |
| 1.2 | Recursion; Addition and Multiplication | 遞迴定理、+ 與 ·、消去律、算術律 | 舊 1.5：`thm-omega-recursion`（證明縮短，或改用「對步驟封閉的最小關係」）、`def-omega-arithmetic`、`cor-omega-successor-cancellation`、`thm-omega-arithmetic-laws`（2–3 條完整鷹架，其餘改為練習） | 新 box「固定其他變數，對遞迴變數歸納」（暫名 `exm-method-induct-on-recursion-variable`）；full | 5,475 → 5,000 | F |
| 1.3 | Order and Well-Ordering | 定義 m ≤ n ⟺ ∃j n = m + j；全序、良序、序與算術、冪與奇偶 | 舊 1.6 換基礎重寫：`thm-omega-order` 只留 (a)(b)(d)（**字母不重排**，下游引用的就是這三條；(c)(e) 移到 ST.1）、`thm-omega-well-ordering`、`prp-omega-order-arithmetic`、`prp-omega-powers-parity` | 回指 fd2 `exm-method-least-element`（Idea） | 6,807 → 5,000 | F |
| 1.4 | All Peano Systems Are Alike | 範疇性、算術的轉移；fd2 的 ℕ 就是這個 ℕ；引用規則一段話講完 | 舊 1.7 大幅修剪：`thm-peano-categoricity`、`prp-isomorphism-preserves-arithmetic`、`cor-omega-identification` (a)–(c)（重述，(b) 仍是「歸納與遞迴在 ℕ 上成立」，(c) 仍涵蓋 `@fd2:lem-naturals-arithmetic`）；刪去三組 meta 對照表、選擇公理稽核、「兩幅圖像」 | 新 box「用遞迴建、用歸納比」（暫名 `exm-method-build-by-recursion`）；full | 5,696 → 4,500 | F |

### Chapter 2. The Integers (F3.2), `ch02-integers/`（原 `ch02-integers-and-rationals/` 的前半）

Time：約 **18 h core / 25 h full**。

| § | Title | 內容（一行） | 主要來源與標籤 | Method box／鷹架 | Now → Target | Pipeline |
|---|---|---|---|---|---|---|
| 2.1 | The Integers as Classes of Pairs | 先試「符號加大小」並看它失敗，再用 ℕ × ℕ 的類 | 舊 2.1：`def-integers-as-classes`、`prp-integer-pairs-equivalence`、`exm-integer-pair-classes`、`prp-integer-normal-form`；刪去 `prp-pair-not-natural` 的評註與 integer 字源；ℕ 的例行算術不再逐步掛標籤 | Idea | 4,472 → 3,800 | S |
| 2.2 | Well-Definedness and the Arithmetic of ℤ | 在代表元上檢查，一次一個變數；ℤ 的 + 與 ·；ℕ 嵌入 ℤ | 舊 2.2：`thm-well-defined-on-classes`（(a) 回指 fd2 5.2 的 induced map，(b)(c) 配 box）、`def-integer-operations`、`exm-ill-defined-first-coordinate`、`prp-naturals-embed-integers` | 回指 `@fd2:exm-method-well-definedness`；新 box「一次一個變數」（暫名 `exm-method-one-argument-at-a-time`）；full | 4,678 → 4,000 | S |
| 2.3 | Commutative Rings; ℤ Is One | 交換環與體的公理；ℤ 是交換環；環裡的代數規則 | 舊 2.3 前半：`def-commutative-ring-and-field`、`thm-integers-commutative-ring`、`prp-ring-algebra` | 新 box「化約到下一層」（暫名 `exm-method-reduce-to-level-below`）；full | ≈ 3,800 → 4,000 | S（拆節） |
| 2.4 | Ordered Rings and the Rules for Inequalities | 由正元集定序；ℤ 是有序環；不等式規則 (a)–(i)；ℤ 的離散性 | 舊 2.3 後半：`def-ordered-ring-and-field`、`prp-order-from-positives`、`def-integer-order`、`thm-integers-ordered-ring`、倍數 n·a、`prp-ordered-ring-rules`（3–4 條完整鷹架，其餘 Idea）、`prp-integer-least-element`、`exm-finite-ring-not-orderable` | 新 box「把比較化成一個正元」（暫名 `exm-method-one-positive-element`）；full | ≈ 4,500 → 5,000 | S（拆節） |
| 2.5 | Division with Remainder | 用問題開頭（在建構出來的 ℤ 上，每個整數仍是偶數或奇數嗎？），回指 fd2 的證明；整除規則、帶餘除法、奇偶 | 舊 3.1 修剪：`prp-divisibility-rules-integers`（只留 Idea 與 (e)(g) 的證明）、`thm-integers-division-remainder`、`cor-integers-even-odd`；刪 small-primes 評註與 C1；本章的 R 組新寫在這一節 | 回指 `@fd2:exm-method-least-element`（Idea） | 3,601 → 2,500 | F |

### Chapter 3. The Rationals (F3.11, new id), `ch03-rationals/`（原 `ch02-integers-and-rationals/` 的後半）

Time：約 **12 h core / 18 h full**。

| § | Title | 內容（一行） | 主要來源與標籤 | Method box／鷹架 | Now → Target | Pipeline |
|---|---|---|---|---|---|---|
| 3.1 | The Rationals as Classes of Fractions | 同一招的第二輪：分數的類、運算、ℚ 是體 | 舊 2.4：`prp-rational-pairs-equivalence`、`def-rationals-as-classes`、`def-rational-operations`、`exm-ill-defined-fraction-sum`、`thm-rationals-field`、`prp-integers-embed-rationals`；`exm-fractions-nonzero-denominators` 改為 B/C 練習（無下游引用） | 回指 2.2、2.3 的 box（Idea） | 5,162 → 4,000 | S |
| 3.2 | ℚ as an Ordered Field; the Archimedean Property | ℚ 的序、倒數與序、中點稠密、Archimedes、整數部分 | 舊 2.5：`def-rational-order`、`thm-rationals-ordered-field`、`prp-reciprocal-order`、`thm-rationals-archimedean`、`cor-rationals-archimedean-epsilon`、`prp-rational-integer-part` | Idea | 4,523 → 4,000 | S |
| 3.3 | The Gaps in the Rationals | 沒有有理數的平方是 2（對最小分母下降）；√2 的缺口；Newton 數列 | 舊 2.6：`thm-no-rational-square-two`、`thm-rationals-gap-sqrt2`、`exm-newton-rationals-sqrt2`、`eq-newton-identities`；練習區由 5.8k 字修剪，`exr-gaps-in-the-rationals-r2` 必留；R 組留在這裡 | 回指 `@fd2:exm-method-smallest-counterexample`（Idea） | 4,139 → 4,000 | S |

### Chapter 4. Ordered Fields and Sequences (F3.9), `ch04-ordered-field-sequences/`（不變）

Time：約 **22 h core / 35 h full**（原 25/40）。

| § | Title | 內容（一行） | 修改 | Method box／鷹架 | Now → Target | Pipeline |
|---|---|---|---|---|---|---|
| 4.1 | Working in an Ordered Field | 分式規則、一半、絕對值與三角不等式 | 刪 B2；規則字母引用每個概念只引一次 | Idea | 3,449 → 3,000 | S |
| 4.2 | ℚ inside an Ordered Field; Archimedes | ι_F、Archimedes、整數部分、稠密、ℚ(t) | `thm-rationals-embed-ordered-field` 的 Steps 1–3 收進 second-reading fold，正文留陳述、Idea 與唯一性那一步；C3（ℚ 的序唯一）移到 Ch6 或刪除 | Idea | 5,074 → 4,000 | S |
| 4.3 | Sequences and Limits | 第一次 ε–N | 加 scratch work：由 \|aₙ − a\| 倒推 N（以 B1 為 worked example） | 新 box「由定義證極限」（暫名 `exm-method-limit-from-definition`）；ε/2 唯一性用 Idea；full | 4,594 → 4,800 | S |
| 4.4 | Limit Laws | 極限律、保序、夾擠 | 引用減量 | Idea | 3,804 → 3,800 | S |
| 4.5 | Cauchy Sequences | Cauchy 數列、代數、符號定理 | 否定量詞定義用 Idea 回指 fd1 Ch6；修剪 | Idea | 5,237 → 5,000 | S |
| 4.6 | A Cauchy Sequence with No Rational Limit | √2 的 Newton 數列在 ℚ 中無極限 | R1 改寫為「零數列對 + 封閉、對乘上 Cauchy 數列封閉」，不用理想的字彙；「What you need」拿掉 3.4 | Idea | 4,382 → 4,400 | S |

### Chapter 5. The Real Numbers from Cauchy Sequences (F3.10), `ch05-reals-from-cauchy/`

Time：約 **18 h core / 25 h full**（原 25/35）。

| § | Title | 內容（一行） | 修改 | Method box／鷹架 | Now → Target | Pipeline |
|---|---|---|---|---|---|---|
| 5.1 | Sequences That Should Converge | 有理 Cauchy 數列、等價、有限改動 | 截斷的構造縮成草圖或練習 | Idea | 4,412 → 3,500 | S |
| 5.2 | The Field of Reals | 類上的運算、良定義、ℝ 是體 | **拿掉商環路線**：環律逐項證（`thm-well-defined-on-classes` 加上「𝒞 的律在類上讀出」）；刪重複的良定義證明；C2 不再提 ℤ/4ℤ；ℝ = 𝒞/𝒩 留一句前瞻，指向 *Algebraic Preliminaries* | Idea | 4,288 → 4,000 | F |
| 5.3 | Positive Classes and the Order | 正類、正錐、序體 | 修剪；`prp-reals-absolute-value-termwise` 改為練習 | 新 box「先取 margin，再取 index」（暫名 `exm-method-margin-before-index`）；full | 5,008 → 4,500 | S |
| 5.4 | The Rationals Inside the Reals | 嵌入、Archimedes、稠密、√2 的類 | 稠密改為一行（`@thm-rationals-dense-ordered-field` 加上 Archimedes），直接證明改為練習；`cor-rational-epsilon-suffices`、`thm-terms-converge-to-class` 改為練習 | Idea | 4,320 → 3,000 | F |
| 5.5 | Least Upper Bounds | 二分法：以有理端點逐次對分，上端點 (u_k) 是有理 Cauchy 數列，s = [(u_k)] 就是上確界；ℝ 是完備有序體 | 舊 5.6 改寫：`def-complete-ordered-field`、`lem-power-two-bound`、`thm-reals-complete-ordered-field`（**陳述不變**）；`exm-representatives-need-choice` 縮成一段評註，標籤保留；刪 History fold；Laurent 評註只在 AN1.11 保留其回收時才留 | 新 box「二分並維持不變式」（暫名 `exm-method-bisect-invariant`）；full | 5,084 → 4,000 | F |

### Chapter 6. The Complete Ordered Field Is Unique (F3.4), `ch06-complete-ordered-field/`

Time：約 **12 h core / 18 h full**（原 20/30）。

| § | Title | 內容（一行） | 修改 | Method box／鷹架 | Now → Target | Pipeline |
|---|---|---|---|---|---|---|
| 6.1 | What Completeness Gives at Once | 保序映射固定 ℚ、完備蘊含 Archimedes、下方有理數、平方根 | 平方根的證明（倒推 h）配完整 scratch work | 新 box「把點建成上確界」（暫名 `exm-method-point-as-supremum`）；full | 4,137 → 4,100 | S |
| 6.2 | Building the Map from the Rationals Below | 嵌入到任一完備有序體（7 步） | 第二個評註只留 ℚ(t)；修剪 | Idea | 3,903 → 3,800 | S |
| 6.3 | Two Complete Ordered Fields, One Isomorphism | 唯一性、自同構只有恆等；結尾「假設公理還是建模型」 | `exm-cof-two-models` 改寫成不依賴 Ch7（「x 下方的有理數滿足四條性質；滿足它們的集合叫 Dedekind 分割（ST）」）；舊 6.5 壓成約 1,500 字：AN1 的對照表、零 = ∅ 的例子、「極限隨同構搬過去」，轉移論證改引 `@fd1:thm-isomorphism-invariance`；ℚ(√2) 共軛只留一句指向 fd5；比較表縮成評註 | Idea | 4,555 + ≈ 1,500 → 5,000 | F |

### 合計

| 章 | 主線字數（Target） | core/full h | 原（章） | 原 core/full h |
|---|---|---|---|---|
| 1 The Natural Numbers | ≈ 19,000 | 18/25 | 1 ZF Fragment … | 30/40 |
| 2 The Integers | ≈ 19,300 | 18/25 | 2 ℤ and ℚ | 25/35 |
| 3 The Rationals | ≈ 12,000 | 12/18 | （同上） | — |
| — | — | — | 3 Divisibility（→ fd5） | 25/30 |
| 4 Ordered Fields and Sequences | ≈ 24,800 | 22/35 | 4 | 25/40 |
| 5 Reals from Cauchy Sequences | ≈ 19,000 | 18/25 | 5 | 25/35 |
| 6 The Complete Ordered Field | ≈ 12,900 | 12/18 | 6 | 20/30 |
| — | — | — | 7 Dedekind Cuts（→ ST） | 25/30 |
| **Total** | **≈ 107,000**（原 ≈ 191,000，−44%） | **≈ 100/146** | | 主線 150/210（含 Ch7：175/240） |

字數去向：約 24,700 字隨 F3.5 移到 fd5（其中 3.1 的約 2,500 字留下）；約 23,800（Ch7）＋約 20,000（Ch1 的 ZF 部分）停放到 ST；約 9,000（舊 5.5、ℝ(x)、`thm-cauchy-archimedean-lub`）停放給 AN1；ℚ(√2) 約 2,500 字併入 fd5；其餘來自修剪。Time 是依 STYLE §2 公式估的，每章做完 deepen 後用 `check_structure.py --words` 重算。

`fd3/src/index.md`（Preface）重寫成六章：章表、「How to read」、Time。

## 4. 移出 fd3 的內容、去處與下游修補

停放的材料留在所有 `src/` 之外，以原始文字保存。每個檔頭寫明舊節、所含標籤、預定去處；連同依賴 ledger 的行與 verify sidecar 一起移動（fd2 的作法）。

### 4.1 到 ST（停放於 `fd3/authoring/parked/st/`）

| 舊 | 內容 | 標籤 | ST 章 |
|---|---|---|---|
| 1.1 | (Z1)–(Z6) 的形式 schema | `ax-zf-fragment`、`prp-zf-basic-sets` | ST.1 |
| 1.2 | Kuratowski 序對、A×B、(W1)–(W5) | `def-kuratowski-pair`、`thm-kuratowski-pair`、`prp-working-rules-from-axioms` 等整節 | ST.1 |
| 1.3（大半） | S(x) = x ∪ {x}、歸納集、(Z7)、ω | `def-set-successor`、`exm-von-neumann-numerals`、`def-zf-inductive-set`、`ax-infinity`、`def-omega`、`thm-omega-least-inductive` | ST.1 |
| 1.4（一部分） | 遞移集、ω 滿足 Peano、序對不是自然數 | `def-transitive-set`、`lem-omega-transitive`、`thm-omega-peano`、`prp-pair-not-natural` | ST.1 |
| 1.6（一部分） | m < n 定為 m ∈ n 的條款、tuple 的集合編碼 | `thm-omega-order` (c)(e) 的文字、`prp-tuples-as-sets` | ST.1 |
| Ch7 全章 | Dedekind 分割的建構、算術、與 Cauchy 實數的比較 | 全部 `ch07` 標籤（`def-dedekind-cut` … `thm-dedekind-same-reals`） | ST.1（從 P(ℚ) 用 (Z5)/(Z6) 切出；與 Dedekind–MacNeille 評註相鄰） |

### 4.2 到 fd5 *Algebraic Preliminaries*

- **舊 3.2–3.5 整章搬家**，成為 fd5 的新 Chapter 1 *Divisibility and Congruences*（atlas id F3.5 → F5.1，§6）。這是活的章，不是停放：`git mv` 到 `fd5/src/ch01-divisibility-and-congruences/`，sidecar 從 `fd3/verify/ch03/` 移到 `fd5/verify/ch01/`。fd5 現有的 ch01–ch04 改為 ch02–ch05。
  - 3.2 的 `thm-euclidean-algorithm-integers` 不再用遞迴定理對映射 G 建數列，改為「一串除法，用最小元保證終止」。這件事留給 fd5 自己的下一輪，不在本次結構提交。
  - 3.5 的體那一半（`thm-integers-mod-prime-field`）與 fd5 現有的 1.2 *Finite Fields from Modular Arithmetic* 重疊；CRT 與 fd5 4.5 重疊。合併留給 fd5 的下一輪，暫時兩份並存。
- **ℚ(√2) 那一組**（舊 6.4）：`def-cof-sqrt2-field`、`prp-cof-sqrt2-field-archimedean`、`prp-cof-sqrt2-field-incomplete`、`exm-cof-sqrt2-conjugation` 原文插入 fd5 的 fields 章 §1.3–1.4（新編號 2.3–2.4），標籤不改。fd5 那裡原本「proved the same facts」的重述，在 fd5 下一輪合併。

### 4.3 到 AN1（停放於 `fd3/authoring/parked/an1/`）

| 舊 | 內容 | 標籤 | 去處 |
|---|---|---|---|
| 5.5 | ℝ 的 Cauchy 完備性（對角線、ε/3） | `thm-constructed-reals-cauchy-complete` | AN1.2／AN1.11 的原料（AN1.2 從 LUB 證 Cauchy 判準） |
| 5.6（一部分） | (CC) + (A) ⇒ (LUB) | `thm-cauchy-archimedean-lub` | AN1.11 `thm-completeness-equiv` 的 Step 5 |
| 6.4（ℝ(x) 那一組） | 有理函數體、非 Archimedes、無窮小、平移自同構 | `lem-cof-leading-term-sign`、`lem-cof-polynomial-closure`、`def-cof-rational-functions`、`prp-cof-rational-functions-ordered`、`prp-cof-rational-functions-not-archimedean`、`exm-cof-infinitesimal`、`exm-cof-x-not-square`、`exm-cof-shift-automorphism` | AN1.11 的反例（它本來就計畫寫 ℝ(x)、ℝ((t))） |

另外改為練習、不移出的：舊 5.4 的 `cor-rational-epsilon-suffices`、`thm-terms-converge-to-class`。舊 6.5 的 R1、R2、R3、R4 與實閉體評註直接刪除，因為它們分別與 `exm-truncations-equivalent`、`exm-finite-ring-not-orderable`、ℝ(x)、`exm-cof-sup-one-minus-reciprocals` 重複。

### 4.4 會斷的引用與修補

| 離開的標籤 | 引用處 | 修補 |
|---|---|---|
| `ax-zf-fragment` | fd5 `ch02-fields/03-subfields.md` L178、fd5 Ch1 `index.md` L14、fd5 ch01 blueprint | 改引 `@fd2:def-power-set`、`@fd2:def-set-builder`（或 `@fd2:prp-smallest-closed-set`）；一句話的改動，做 changed-only review；blueprint 加 deviation 註記 |
| `def-kuratowski-pair`、`thm-kuratowski-pair` | fd3 `ch06…/05-axioms-or-model.md` L130（練習答案：√2 字面上是不是集合） | 這段併入 6.3 時改引 `@fd2:def-ordered-pair`，再加一句散文指向 ST.1 |
| `prp-tuples-as-sets` | fd4 blueprint f4-11 L77、L373（尚未起草） | 改用 fd2 的 n-tuple 慣例（`@fd2:def-cartesian-product`），或刪掉該評註 |
| `prp-pair-not-natural` | fd3 2.1、Ch2 index | 刪掉那句話 |
| 舊 Ch3 的全部標籤（F3.5 → F5.1） | fd5 約 33 個檔案（src 25 個，另含 authoring） | `@fd3:<label>` 機械式改成 `@<label>`；fd5 Ch1 index 的「What you need」（L7、L12）重寫 |
| `thm-quotient-ring-by-ideal`、`def-integers-mod-n-ring` | fd3 5.2 及其 C2 | 5.2 改寫時處理（§3） |
| `thm-integers-mod-prime-field`、`thm-integers-mod-n-ring` (d) | fd3 6.5 R2 | R2 刪除；6.5 併入 6.3 時改用 `exm-finite-ring-not-orderable` |
| `def-ideal-commutative-ring`、`thm-quotient-ring-by-ideal` | fd3 4.6 R1 | R1 改寫（§3） |
| `def-integers-mod-n-ring`、`thm-integers-mod-n-ring` | fd4 1.6（約 L420）、1.4 C2（L157、L322）、F4.1 index L7 | 改引 `@fd2:def-congruence`、`@fd2:prp-congruence-arithmetic`；ℤ/3ℤ 不能定序就地寫出（1 + 1 + 1 = 0）。帶餘除法與奇偶留在 fd3 2.5，fd4 的那些引用不受影響 |
| `prp-rationals-lowest-terms`、`def-integers-mod-n-ring` | F4.7 blueprint | 改為 `@fd5:` 或 `@fd2:` |
| `thm-fundamental-arithmetic` | AN2 Ch5 blueprint 與 coordinator 筆記 | 改為 `@fd5:` |
| 舊 Ch3 的標籤 | fd2 blueprint `ch01-deepen` | blueprint 紀錄加註，沒有工具讀它 |
| ℚ(√2) 那一組 | fd5 `index.md:13`、`03-subfields.md:90, 122, 279, 283, 287`、`04-field-homomorphisms.md:3, 27, 129`、`06-frobenius-and-fermat.md:478` | 改為本書內的 `@` |
| `lem-cof-polynomial-closure` | F4.7 blueprint L163、L273；F5.3 blueprint L230、L311 | F4.7 的開場改指 `@fd3:exm-rational-function-field`；F5.3 刪掉「same-statement」那幾列 |
| `thm-cauchy-archimedean-lub` | AN1.11 blueprint `ch10.md` L155、L210 | 改成 AN1.11 自己的 Step 5；L183 的二分法回指保留（新 5.5 仍然二分）；L32 的 Laurent 回收視 5.5 是否保留而定；L11 改為「Rudin appendix covered by F3.10; cuts in ST」 |
| `exm-representatives-need-choice`、`lem-power-two-bound`、`thm-constructed-reals-archimedean`、`thm-reals-complete-ordered-field` | fd5 Ch4（新 Ch5）`index.md:31`、`06-the-fundamental-theorem.md:150, :608` | 標籤留在 fd3，不必改；只有 `index.md:31` 散文裡的節號要改 |
| Ch7 的標籤 | fd3 以外沒有引用 | 只修散文：fd3 Preface、Ch5 index、舊 5.6 的結尾段、Ch6 index、6.1 開頭、`exm-cof-two-models`、4.2 L78 的指標 |

**留在 fd3 但改了編號或章的標籤**（例如 2.3–2.6 → 2.3、2.4、3.1–3.3，3.1 → 2.5，5.6 → 5.5，6.5 → 6.3）照舊能解析，不必修補。

### 4.5 要改指向的上游承諾（`authoring/STATUS.md`）

- 第 82 列 F1.6 §02（「(Z1) is the first axiom of *Number Systems* Ch1」，fd1 `ch07…/02-counter-models.md` L388 與 ledger L900）→ ST.1；fd1 那句散文改成指向 ST。
- 第 139 列 F1.3 §02（從集合公理導出歸納）→ ST.1。F3.1 現在把歸納當成 Peano 公理 (P5)。
- 第 164 列 F2.1 §02/§04：公理、序對由集合建構 → ST.1；ℤ、ℚ 仍指 F3.2（ℚ 改指 F3.11）；ℝ 仍指 F3.10。fd2 散文在 `ch01-sets/02-sets-and-subsets.md` L33、`04-products-and-relations.md` L24。
- 第 183 列 F2.2 §01：「ℕ 由集合建出」那一半 → ST.1；「Peano 公理」那一半留在 F3.1。
- 第 121、157、167、189、211 列（gcd、Euclid 引理、最簡分數、ℤ/nℤ、理想）：F3.5 改為 F5.1，所付的標籤不變；第 211 列「ℤ/nℤ 回訪 `exm-finite-ring-not-orderable`」改由 F5.1 付。
- 第 206–209 列（F3.1 自己的承諾）依新 Ch1 重寫：「ℕ means ω」改成「ℕ 是 Peano 系統」。
- 第 86、89 列（範疇性、完備有序體唯一）不變。
- F3.x 各列重寫成新的章節表；F3.3 那一列改寫為「已停放到 ST」。

### 4.6 指標掃描（沿用 fd2 的 `tools/renumber.py` 兩輪）

**第一輪（機械式）：**

| old | 2.3 | 2.4 | 2.5 | 2.6 | 3.1 | 5.6 | 6.5 |
|---|---|---|---|---|---|---|---|
| new | 2.3 / 2.4 | 3.1 | 3.2 | 3.3 | 2.5 | 5.5 | 6.3 |

另外，1.5、1.6、1.7 → 1.2、1.3、1.4（舊 1.1–1.3 與 1.4 被停放的部分刪掉指標，或改指 ST）。

**第二輪（人工）：**
- 「Chapter 2」依意思改成 2（ℤ）或 3（ℚ）。
- 「Chapter 3」「Section 3.2–3.5」改成 *Algebraic Preliminaries*, Chapter 2。
- 「Chapter 7」刪除，或在散文裡寫 ST。
- 「Section 6.4」：ℚ(√2) 改指 fd5，ℝ(x) 刪除。
- Ch4–6 的章號不變，所以 an1、fd4 裡的「*Number Systems*, Chapter 4/5/6」幾乎都不必改。

**fd5 重新編號**（只在 Q2 選 A 時）：fd5 內部的 Chapter 1–4 → 2–5，以及 fd4、an1、an2 blueprint 指向 fd5 的章號。

## 5. 新寫或改寫的部分（要寫 blueprint、要起草）

**整節重寫（pipeline F，S1–S4）：**
1. **1.1 Peano's Axioms and Induction**：新的開場動機，說明為什麼這位讀者現在需要 ℕ 的公理；把 `thm-omega-induction` 重述成 Peano 系統上的定理；唯一前驅（新標籤）。
2. **1.2 Recursion**：縮短遞迴定理的證明（S1 二選一：「對步驟封閉的最小關係」，或保留黏合部分解但寫短）；`thm-omega-arithmetic-laws` 改為 2–3 條完整鷹架的證明，其餘改為練習。
3. **1.3 Order**：以「∃j n = m + j」為定義，重證 `thm-omega-order` (a)(b)(d)、良序與 `prp-omega-order-arithmetic`。條款字母保持不動。
4. **1.4 Categoricity**：`cor-omega-identification` 重述，加一段引用規則；刪去 meta 對照表與選擇公理稽核。
5. **2.5 Division with Remainder**：由舊 3.1 修剪，新的開場問題，新 R 組。
6. **5.2 The Field of Reals**：逐項證環律，取代商環路線。
7. **5.4 The Rationals Inside the Reals**：稠密改為一行，兩個輔助結果改為練習。
8. **5.5 Least Upper Bounds**：用有理端點二分法的新證明，只用 `lem-termwise-order`、稠密與 (l_k) ~ (u_k)；陳述不變。
9. **6.3 One Isomorphism**：吸收壓縮後的舊 6.5；`exm-cof-two-models` 改寫。

**風格補課（pipeline S；其餘各節）。** 每節都要補 fd2 的寫法：
- 在 §3 指定的位置加 method box 與 `[Scratch work]`；
- 每個概念只引一次規則，不再每行掛字母（Ch7 7.4 的「rules of ℚ used without comment」就是範本）；
- 證明裡不再寫 ¬I、RAA、=E、∨E 之類的規則名；
- 刪 History fold（5.6、7.6）與「Not proved here」中書裡永遠不會建的物件（6.3 的非 Archimedes 全平方體、6.5 的實閉體）；
- 「What you need」縮到 fd2 re-cut 的長度（目前 25–40 個標籤）；
- 解答裡冗長的評分細則縮短。

每章寫一份精簡的 S1 blueprint，列出逐節的改動。

**新 method box 一覽（暫名，S1 定名）：** `exm-method-induct-on-recursion-variable`（1.2）、`exm-method-build-by-recursion`（1.4）、`exm-method-one-argument-at-a-time`（2.2）、`exm-method-reduce-to-level-below`（2.3）、`exm-method-one-positive-element`（2.4）、`exm-method-limit-from-definition`（4.3）、`exm-method-margin-before-index`（5.3）、`exm-method-bisect-invariant`（5.5）、`exm-method-point-as-supremum`（6.1）。fd2 已有的（well-definedness、least element、smallest counterexample、induction step）只用 Idea 回指，不重複開 box。

## 6. Atlas 變更（math-atlas，與結構提交同一個 commit）

- **`registry/chapters.yaml`**：
  - F3 依序為 F3.1、F3.2、F3.11、F3.9、F3.10、F3.4。
    - F3.1 "The Natural Numbers"／自然數：Peano 公理、遞迴與算術。
    - F3.2 "The Integers"／整數的建構。
    - **F3.11 "The Rationals"／有理數的建構（新 id；F3.6–F3.8 已退役，不重用）**。
    - F3.9、F3.10、F3.4 標題不變（F3.10 可改為 "The Real Numbers from Cauchy Sequences"）。
  - F3.5 移到 F5 區塊，id 改為 **F5.1**，標題 "Divisibility and Congruences"／整除與同餘。`chapters.yaml` L51 的註解「不設 F5.1」改寫。
  - F3.3 併入 ST.1。
- **`registry/renames.yaml`**：
  - `ids`：`{old: F3.5, new: F5.1}`、`{old: F3.3, new: ST.1}`，`decided:` 填核准日，`spec: fd3/authoring/design/layout-proposal.md`。
  - `titles`：F3.1、F3.2，以及 F3.10（若改名）。
- **`registry/plan-edges.yaml`**（暫定，以 `atlas.py check` 為準）：
  - `F3.1: {s: [F2.2, F2.6]}`：拿掉 `see: [F2.4]`（`ax-choice` 的「沒用到」評註刪掉了）；F2.3 只被舊 R1 用到，重算。
  - `F3.2: {s: [F3.1]}`。
  - `F3.11: {s: [F3.2]}`。
  - `F3.9: {s: [F3.11, F3.2]}`：拿掉 `see: [F3.5]`。
  - `F3.10: {s: [F3.9, F3.11], see: [F2.4]}`：拿掉 F3.5。
  - `F3.4: {s: [F3.10, F3.9], see: [F1.6]}`：拿掉 F3.5、F3.3。
  - `F5.1: {s: [F3.2]}`（原 F3.5）。
  - F5.2、F5.3、F5.5、AL1.2、AL2.5：F3.5 → F5.1。F5.2 的 `see` 拿掉 F3.4（ℚ(√2) 已在 F5.2 本章）。
  - F4.1：F3.5 → F3.2（帶餘除法在 2.5）；若引用 `prp-reciprocal-order`，加 F3.11。
  - AN1.11：`see: [F3.10]`，拿掉 F3.3。
  - `ST.1: {s: [F2.4], revisits: [F3.1]}`：註解改為「F3.1 以 Peano 系統為起點；ZF、ω、Kuratowski 序對、Dedekind 分割在這裡」。
- **`registry/statements.yaml`**：
  - `def-peano` 留在 F3.1，`def-integers` 留在 F3.2，`thm-r-unique` 留在 F3.4。
  - `thm-division`：F3.5 → **F3.2**。
  - `thm-bezout`、`thm-fta-arith`、`def-zn`：→ F5.1。
  - `def-dedekind`、`thm-dedekind-lub`：→ ST.1。
  - 新增 `def-rationals`，F3.11，「ℚ := ℤ×ℤ_{>0}/∼」（可選）。
- **`registry/terms.yaml`**：整除與同餘的術語改為 `ch: F5.1`；有理數的術語改為 F3.11。
- **來源對照**：spec/08 的 `pma`、`pugh` 列裡的 F3.3 改為 ST.1；spec/08 的 Foundations 表加註本次變更。
- **`site/books.json`**：fd3 `planned: 6`，blurb 重寫；fd5 的 planned 加 1。
- **`authoring/series.json`**（foundations、analysis-series）：執行 `tools/series.py refresh`。

## 7. 給作者的問題（每題附建議）

1. **ℕ 的立足點。**
   - **建議 (a)**：ℕ 取為假設的 Peano 系統，ZF 與 von Neumann ω 全部移到 ST.1。
   - (b)：另外保留一小節「ℕ 從哪裡來」，只描述 von Neumann ω、不證明，指向 ST。代價是多 2,000–3,000 字，而 fd3 沒有任何地方會用到它。
2. **第 3 章 Divisibility and Congruences。**
   - **建議 A**：整章移到 fd5，成為它的第一章（F3.5 → F5.1），帶餘除法（3.1）修剪後留在 fd3 的 2.5。fd3 省下約 22 h，主線變乾淨，理想在 fd5 有第二個實例。代價是 fd5 章號加 1，以及 fd5 約 33 個檔的機械式改前綴。
   - B：留在 fd3，3.1–3.4 修剪，只把 3.5（單位、ℤ/pℤ、CRT）移到 fd5 1.2。fd5 不必重編號，但 3.4 的抽象理想仍留在 fd3。
3. **ℤ 與 ℚ 分成兩章，還是一章？**
   - **建議分兩章**（Chapter 2 The Integers、Chapter 3 The Rationals）：一章建一個數系，正好讓 Ch4–6 保留原章號，下游指標幾乎不必改。代價是一個新 atlas id（F3.11）。
   - 另一案：維持一章，8 節（加上 2.3 拆節與帶餘除法），約 31,000 字，不需要新 id，但 Ch4 以後的章號都要減 1。
4. **Dedekind 分割。**
   - **建議整章停放到 ST**，因為 fd3 外沒有任何引用。
   - 另一案：在 Ch6 末保留一節選讀「6.4 Dedekind Cuts, Briefly」（約 3,500 字：`def-dedekind-cut`、`lem-cut-separation`、`thm-cut-order-total`、`thm-dedekind-lub`、`thm-dedekind-same-reals` 只給陳述），算術部分移到 ST。

## 8. 流程（與 fd2 相同）

**結構提交只有一次**，作者核准後才做，內容包括：
- 依 §3、§4 的所有 `git mv`、拆節與停放，舊文逐字搬移，待改處標 `<!-- S3: rewrite per blueprint (...) -->`；
- 停放檔的檔頭，`fd3/authoring/parked/ledger-parked.yaml`，sidecar 隨標籤移動；
- 依新章重新產生 `fd3/authoring/ledger/chNN.yaml`，保留既有的 item evidence；
- 指標掃描第一、二輪；
- 若 Q2 選 A：fd5 重新編號，並插入 F5.1 與 ℚ(√2)；
- §4.4 中的一句話修補（fd5 1.3 L178、fd4 1.4/1.6）；
- §6 的 atlas 編輯；
- `config/config.json` 列出新的六個目錄。

提交前必須通過 `check_structure`（0 fatal）、`atlas.py check` 與 forward-dependency ledger 檢查。

之後依 lean 規則逐章 deepen，一次只跑一個 workflow：changed-only blind review、S7 re-referee = S7r、round 2 手動、minor reviser 用 Sonnet。

| 類別 | 節 | 執行內容 |
|---|---|---|
| **F**：S1/S2 → 起草 → S4 → changed-only blind review → S7 → round 2 | 1.1–1.4、2.5、5.2、5.4、5.5、6.3 | 每章一份 blueprint：`ch01-peano.md`、`ch02-division.md`、`ch05-recut.md`、`ch06-recut.md` |
| **S**：風格補課（method box、scratch work、引用減量、修剪）→ S4 → 改動段落的 changed-only blind review → S7 | 2.1–2.4、3.1–3.3、4.1–4.6、5.1、5.3、6.1、6.2 | 每章一份精簡 S1 改動清單（`ch02-03-style.md`、`ch04-style.md` 等） |
| **fd5 / fd4 外部修補** | fd5 1.3 L178、F5.1 前綴機械改、fd4 1.4 C2 與 1.6、各 blueprint 註記 | changed-only review |

**建議順序：** Ch1 → Ch2/Ch3 → Ch5 → Ch6 → Ch4 → 外部修補。每章做完後重算 Time，S8 build check，再 `update_preview.sh` 更新預覽站。S9 抽樣仍由作者做。

## 9. 結構提交紀錄（2026-10-26）

照 §0、§3、§4 執行，標籤一律未改名。以下是與 §3–§8 不同或 §3–§8 沒寫的地方。

**目錄（`fd3/config/config.json`）。** `ch01-natural-numbers`、`ch02-integers`、`ch03-rationals`、`ch04-ordered-field-sequences`、`ch05-reals-from-cauchy`、`ch06-complete-ordered-field`。fd3 的 `external-books` 加上 fd5（4.6 R1、5.2、Ch4–6 index 引用已移到 fd5 的理想與商環標籤，改寫成 `@fd5:`，隨 S3 改寫消失）。

**為了讓 section contract（`check_structure.py`）在 S3 之前仍然通過而做的調整：**
- **2.3／2.4 暫不拆**：舊 2.3 整節逐字留在 `ch02-integers/03-commutative-rings.md`（標題暫用舊的 The Integers as an Ordered Ring），`04-ordered-rings.md` 是只有標題的 stub。原因：前半（交換環）單獨沒有 Quick check、沒有 A/B/C 練習。S3 在 `## Ordered rings` 處拆開（檔首 S3 註記寫明）。
- **1.1 帶進舊 1.3 的一個 warning**（「An inductive set is the set of natural numbers is false」），因為 1.1 保留的部分沒有任何 warning；它緊鄰 `thm-omega-induction`，與之一起移動，S3 改寫成 Peano 系統的版本。
- **2.5 的 `thm-integers-division-remainder` (b)**（q = ⌊a/n⌋）的陳述與證明停放到 `fd3/authoring/parked/from-3.1-division-part-b.md`：它的證明用到 ℚ，而 ℚ 現在在 Chapter 3 之後（forward-dependency 檢查會擋）。(a) 的字母保留（下游有 31 處引用 (a)，沒有人引用 (b)）。S3 決定 (b) 的去處（例如 3.2 `prp-rational-integer-part` 之後的練習）。
- **只有標題的 stub**：`ch01-natural-numbers/index.md`、`ch02-integers/index.md`、`ch03-rationals/index.md`、`ch01-natural-numbers/05-where-n-comes-from.md`、`ch02-integers/04-ordered-rings.md`（check_structure 只認「只有 `# Title` 一行」為 stub，所以這些檔不能帶 S3 註記；註記寫在這裡）。舊 Ch1、Ch2 index 原文停放在 `fd3/authoring/parked/old-indexes/`，供 S3 寫新 index。1.5 的內容見 §0。

**引用。** Chapter 1（1.1–1.4，F）與 5.5（F）保留的舊文仍引用已停放的 ZF 標籤與 `thm-cauchy-archimedean-lub`、`thm-constructed-reals-cauchy-complete`，共 29 處，列在 `fd3/config/known-unresolved.json`（引擎的 baseline 機制），隨改寫消失。S 類節裡的引用都已修好（2.1 刪掉 `prp-pair-not-natural` 那句；6.1 與 Ch6 index 不再提 `thm-cauchy-archimedean-lub`；Ch4–6 的散文指標改指 Chapter 3、*Algebraic Preliminaries*、*Axiomatic Set Theory*）。Ch5、Ch6 的 index 開頭加了 S3 註記：Roadmap 與 Named moves 仍描述舊章。

**ℚ(√2) 那一組**依協調者指示停放到 `fd5/authoring/parked/from-fd3/from-6.4-q-sqrt2.md`（§4.2 原本寫「插入 fd5 的 fields 章」）。fd5 對它們的引用已改成本書內的 `@`（§4.4 的修補），在 fd5 下一輪把這組併入 2.3–2.4 之前，列在 `fd5/config/known-unresolved.json`。

**fd5。** 舊 3.2–3.5 `git mv` 到 `fd5/src/ch01-divisibility-and-congruences/01–04`（index 一併移動，標題改為 Divisibility and Congruences，「What you need」與章內指標重新指向，加 S3 註記）；fd5 原 ch01–ch04 的 src、verify、ledger、blueprint 改為 ch02–ch05（`tools/renumber.py` 處理 fd5 自己的章節指標，之後人工改回誤改的指標：接在別書書名後面、其實指向別書的 "Chapter N"、"Section N.M"）。fd5 序言加 Chapter 1 一列。移入的檔案裡，仍在 fd3 的標籤改為 `@fd3:`；fd5 其他章對移入標籤的 `@fd3:` 改為本書內的 `@`。

**fd4。** ℤ/nℤ 的引用依 §4.4 改引 `@fd2:def-congruence`、`@fd2:prp-congruence-arithmetic`、`@fd2:prp-integers-mod-n`，ℤ/3ℤ 不能定序就地寫出（1 + 1 + 1 = 0）；C2 (c) 的解答與 R2 因此變動，`exr-square-roots-and-order-c2` 的 verdict 變 stale，需 changed-only review。

**其他下游。** fd1 7.2 的 (Z1) 指向 *Axiomatic Set Theory*；fd2 1.2、1.4 關於「由集合建出 ℕ、序對」的散文改指 *Axiomatic Set Theory*，ℚ 的指標改為 Chapter 3，ℤ/n 商環改為 *Algebraic Preliminaries*, Section 1.3；an1 1.3 與 Ch1 index 的 Dedekind 指標改為 *Axiomatic Set Theory*；各書 dependency ledger 的 atlas 指標（F3.1 §0x、F3.2 §04–06、F3.5、F3.3、F3.10 §06、F3.4 §05）依新編號重寫；blueprint 加註（fd4 f4-7、f4-11，fd5 ch02、ch04，an1 ch10，an2 ch05，fd2 ch01-deepen）。

**Ledger。** `fd3/authoring/ledger/ch01–ch06.yaml` 與 `fd5/authoring/ledger/ch01–ch05.yaml` 由腳本重建：每個 item 隨標籤移動並保留 verdict 歷史；check item 的 key 隨檔名改變，以內容 hash 對應（`moved_from` 記舊 key）。停放的 item 在 `fd3/authoring/parked/ledger-parked.yaml`（187 項）與 `fd5/authoring/parked/from-fd3/ledger-parked.yaml`（9 項），附 `parked_file` 與 `old_dir`。Stale：fd3 ch02 2 項（`thm-integers-division-remainder` 與其證明，因 (b) 停放）、ch04 1 項（4.6 R1 的指標改寫）；fd5 ch02 1 項（`prp-subfield-intersection` 的證明，ZF 改引 fd2）、ch04 1 項（`exr-formal-derivative-r3`）；fd4 ch01 1 項（`exr-roots-of-unity-r2`；`exr-square-roots-and-order-c2` 的解答 (c) 也改了，但 ledger 只雜湊第一個 hint，所以沒有顯示 stale）；fd2 ch01 1 項（`exr-products-and-relations-a1`，指標改指 *Axiomatic Set Theory*）。都要 changed-only review。

**Sidecar** 隨標籤移動：fd3/verify/ch01–ch06；fd5/verify/ch01（36 個，來自舊 fd3 ch03）；`fd3/authoring/parked/st/verify`、`parked/an1/verify`、`parked/verify`、`fd5/authoring/parked/from-fd3/verify`。
