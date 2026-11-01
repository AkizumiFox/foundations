# fd1–fd3 初學者可讀性診斷

日期：2026-11-01。作者的問題：「整個 fd 系列的措辭好像不太適合初學者，要怎麼改進呢？」，以及「好，先開診斷」。
這份診斷是唯讀的：沒有改動 `src/`、`verify/`、config 或 ledger。fd4/fd5 正在合併，所以不在範圍內。配套的試寫在 `beginner-pilot-rewrite.md`。

---

## §1 方法

**讀者設定。** 新手讀者是剛高中畢業、第一次讀證明式數學、自學、沒有老師可問的人（STYLE §1 的讀者）。六份新手讀者報告各讀一段範圍，對每個抽樣 section 給出總評和 1–5 難度，再逐條列問題。每條問題記錄：檔案與行號、原句引文、類別、嚴重度、原因、較白話的改寫。

**抽樣。** 每章的 `index.md` 加上 1–3 個 section，共 60 個檔案（20 個章首頁、40 個 section）：

| 報告 | 範圍 | 抽樣檔案 |
|---|---|---|
| 1 | fd1 Ch1–4 | 4 個 index，1.1、1.5、2.1、2.5、3.1、3.2、4.1、4.8 |
| 2 | fd1 Ch5–8 | 4 個 index，5.1、5.6、6.1、6.4、7.1、7.3、8.1、8.3 |
| 3 | fd2 Ch1–3 | 3 個 index，1.1、1.3、2.1、2.4、3.1、3.3 |
| 4 | fd2 Ch4–6 | 3 個 index，4.1、4.4、5.1、5.2、6.1、6.2 |
| 5 | fd3 Ch1–3 | 3 個 index，1.1、1.4、2.1、2.2、3.1、3.3 |
| 6 | fd3 Ch4–6 | 3 個 index，4.1、4.5、5.1、5.5、6.1、6.3 |

抽樣偏向每章最難的 section，所以問題數不能直接外推到整冊。但類別的比例和成因都和抽到哪一節無關（見 §3），所以據此改規則是站得住的。

**類別**（報告用的固定標籤）：`process-jargon`（作者或製作流程用語上版面）、`undefined-term`（用到尚未定義的詞）、`citation-clutter`（引用堆疊）、`step-size`（步子太大，或反過來，對顯然的事過度論證）、`long-sentence`、`tone`、`meta-talk`（談文本自身結構）、`notation-load`、`abstract-before-example`、`nominal-style`。
**嚴重度**：`stuck`（讀不下去）、`slowed`（要重讀）、`annoyed`（讀得懂但被打擾）。

計數是逐條手工清點報告得到的，總數 510 條。

---

## §2 計數與重點類別

### 2.1 類別 × 冊

| 類別 | fd1 | fd2 | fd3 | 合計 | 其中 stuck |
|---|---:|---:|---:|---:|---:|
| process-jargon（作者用語） | 27 | 24 | 30 | **81** | 11 |
| undefined-term（未定義詞） | 28 | 19 | 30 | **77** | 17 |
| citation-clutter（引用堆疊） | 15 | 19 | 25 | **59** | 8 |
| step-size（步距：太大或過度論證） | 19 | 18 | 19 | **56** | 12 |
| long-sentence（長句） | 22 | 18 | 14 | **54** | 18 |
| tone（語氣、繞圈、對其他書說話） | 13 | 24 | 16 | **53** | 7 |
| meta-talk（談文本自身） | 21 | 11 | 14 | **46** | 2 |
| notation-load（記號負擔） | 12 | 16 | 15 | **43** | 9 |
| abstract-before-example（抽象先行） | 10 | 14 | 8 | **32** | 9 |
| nominal-style（名詞化） | 3 | 1 | 5 | **9** | 3 |
| **合計** | **170** | **164** | **28** | **176** | **510** | **96** |

### 2.2 嚴重度 × 冊

| 嚴重度 | fd1 | fd2 | fd3 | 合計 |
|---|---:|---:|---:|---:|
| stuck | 32 | 33 | 31 | 96（19%） |
| slowed | 93 | 92 | 98 | 283（55%） |
| annoyed | 45 | 39 | 47 | 131（26%） |

三冊的分布幾乎一樣。這說明問題出在共用的寫作規則，而不是某一冊、某位起草者。

**章首頁特別集中。** 抽到的 20 個 `index.md` 累計 78 條（15%）。fd3 Ch4 的 index 一頁就有 10 條，讀者的評語是：初學者應該跳過第一段以後的內容，但頁面上沒有任何地方告訴他可以跳過。

**最難的 section**（讀者評 5 分，並依 stuck 數排序）：fd3 §2.2 well-defined operations（5 個 stuck）、fd3 §1.4 categoricity（4）、fd1 §2.5 reductio（3）、fd1 §4.8 completeness、fd1 §7.3 first-order soundness、fd3 §5.5 LUB（各 2）、fd2 §6.2 Zorn、fd3 §6.3 uniqueness（各 1）、fd1 §6.4 uniform continuity（0 個 stuck，但讀者說「the densest so far」）。

### 2.3 最重要的四組

#### A. 書在講自己（process-jargon + meta-talk = 127 條，25%）

讀者讀到的是編書的工具：core track、exit checks、named moves、method box、fold、second reading、Givens/Goal、the prompt、self-explain、hook、payoff、citing rule、"clause 3"、"step (2) of the box"。這是最大的一組，而且大部分句子是規則直接規定的（§3）。

- fd1 Ch1 index L27：「About 40 hours on the core track (all of A, one B and one C per section, the exit checks)」
  → 「Plan on about 40 hours if you do every A exercise and one B and one C exercise per section; about 65 hours to do everything.」
  （這句是 STYLE §2 第 4 項規定的原文模板，三冊 20 個 index 都有。）
- fd3 §2.2 L137（stuck）：「multiply the given by \( c \), and, read from right to left, by \( d \)」
  → 「So multiply the hypothesis a + b' = b + a' by c, and its mirror form b + a' = a + b' by d, then add the results.」
- fd2 §4.1 L406（stuck）：「The claim is a negation, "no bijection", so this is face (i), chosen by @exm-method-choosing-the-form; but the clash is between results, not between two lines.」
  → 「The statement says 'there is no bijection', so we prove it by contradiction: assume a bijection exists and show that two earlier theorems then give different numbers of elements for B.」
- fd3 §1.4 L252（stuck）：「…fall into three groups, which later chapters refer to by number: … citable only in review exercises; (iii) templates used later over an ordered field. The fold lists each group in full.」
  → 移到給講師的附錄；正文只留：「Every arithmetic fact the earlier books used has now been proved for our ℕ, so those results may be used freely.」

#### B. 引用堆疊與過度論證（citation-clutter 59 + step-size 中屬於「過度論證」的約 25 條）

這一組讓人覺得書不信任讀者：連 7 ∤ 8、(k+1)+1 = k+2、"2 + 2 in ℚ" 都附上引用。另一種形式是 "What you need" 列出 25–60 個 label 的牆。

- fd2 Ch2 index L9（stuck）：「From *Logic and Proof*, Chapters 1 and 2: the contrapositive and its converse (@fd1:prp-contrapositive, @fd1:prp-contrapositive-converse), proof by contradiction (@fd1:def-rule-raa), …」（全段約 40 個引用）
  → 「You need Logic and Proof, Chapters 1–8, and Chapter 1 of this volume (sets, unions, pairs, products, relations).」
- fd3 §3.3 L34：「Since p, q ≥ 0, @prp-ordered-ring-rules (g) gives p² < q² if p < q, and p² = q² if p = q; so p² ≤ q², that is, q² + q² ≤ q², and adding −q² (O3) gives q² ≤ 0.」
  → 「If p ≤ q, then p² ≤ q², so 2q² ≤ q², so q² ≤ 0, which is impossible since q > 0. Hence q < p.」
- fd2 §5.1 L122：「8 = 7k fails for every integer k: if k ≤ 1, then 7k ≤ 7; if k > 1, then k ≥ 2 by @prp-integers-closed (c), and 7k ≥ 14.」
  → 「Not reflexive: 1 S 1 would need 7 | 8, which is false.」

#### C. 詞先於意思（undefined-term 77 + abstract-before-example 32 = 109 條，stuck 26）

主要出現在兩個地方。一是章首頁：開場故事、Named moves、Summary、Terms 都放在章首，用的是本章才定義的詞。二是 §3 的定義模板：先給定義或一般定理，例子排在後面。

- fd1 Ch1 index L20（stuck）：第一頁的小測驗答案就用了「It holds only inside the supposition's box.」，而 box 要到 1.4 節才出現。
  → 「No. The line x² > 4 was reached only under the assumption x > 2, so it may be used only while that assumption is in force.」
- fd3 §2.2 L20（stuck）：一般引理一次帶進 ∼, ≈, X, Y, f, F, g, G, S, S̄，之前沒有任何 ℤ 上的例子。
  → 先在 ℤ 上示範一條失敗的規則（取第一座標）和一條成立的規則（逐座標相加），再敘述引理（見試寫）。
- fd2 §6.2 L125（stuck）：「(1) **partial objects:** let P be the set of partial objects, of which the complete ones are the finished case, ordered by ⊆ (extension)」
  → 先放代表元素集的例子，再用它說明模板：「let P be the sets that meet each class at most once ('partial' solutions) …」

#### D. 長句與記號代號（long-sentence 54 + notation-load 43 + nominal-style 9 = 106 條，stuck 30）

長句是 stuck 最多的類別（18 條）。常見的樣子是一句話塞進多層括號、多個引用和分號。另一個毛病是代號 (Eq3)、(Fn1)、(O3)、(S1)、(W3)、(N4)、(F9) 從不用文字重述。

- fd1 §1.5 L301（stuck）：「A **whole box**, cited by →I, has its own condition: the citing line must stand in exactly the boxes that the cited box stands in, other than the cited box itself.」
  → 「When you close a box and cite it as a whole, the citing line must sit at the same nesting level as the box, just after it.」
- fd1 §5.6 L47（stuck）：∃E 規則的一句話裡同時有 line h、flagged box、名字、代換、末行 j、「a line of that box itself」和兩個交叉引用。
  → 「The rule uses two things: a line h saying ∃x φ, and a box. The box starts with a new name x₀ and the assumption φ[x₀/x]. It ends with some line χ. After the box you may write χ again.」
- fd3 §3.1 L192（stuck）：「As there, (F4) gives pairs that are related rather than equal; here (F9) does too, and the scaling observation is what relates them.」
  → 「For the inverse law x + (−x) = 0 and for distributivity, the two sides come out as different pairs in the same class …」

（第五組 tone 53 條，大多是對其他書、其他邏輯、構造主義讀者說話，例如「a fact this book does not prove」「classical step」「as far as we know」。成因和處理方式併入 §3–§4 的 B9、B11。）

---

## §3 成因：寫作與審稿規則本身

這些措辭大多是照規則寫出來的，不是起草者自己的習慣。下表列出規則條文，以及它造成的類別。

| 規則（檔案 §） | 條文要點 | 造成的類別 |
|---|---|---|
| STYLE §2 item 4、§11.9 | Time 行的**原文模板**：「About N hours on the core track (all of A, one B and one C per section, the exit checks)」 | process-jargon（三冊 20 個 index 每個都有） |
| STYLE §2 item 3；PIPELINE S8 | "What you need" 要「with links」；Seam referee 要核對它對交付文本為真 → 起草者列出全部引用 | citation-clutter（25–60 個 label 的牆） |
| STYLE §2 item 6、§12.13.5 | Named moves、Summary、Terms 都放在 `index.md`，也就是章首 | undefined-term（章首頁 78 條） |
| STYLE §1 "Recall before use" | 「recall it in a clause, name it, and link it with `@label`」 | long-sentence（插入語）、citation-clutter |
| STYLE §4 item 4 | 「**Every step names its reason**: … a cited result (`@label`, not restated)」，以及「Always justify each clause …」 | citation-clutter、step-size（過度論證） |
| STYLE §9 ledger；PIPELINE S5 Referee B | 不帶 `@ref` 的事實都要記進 ledger，漏記算 finding；多一個行內 `@ref` 卻從不算 finding | 不對稱的誘因：最安全的寫法就是行內引用一切。fd3 從 Peano 重建 ℕ、ℤ、ℚ，連 5+x=3 也要四個引用 |
| PIPELINE S5 Referee A | 「name the reason for each step … check the cited label」 | 審稿修正又加更多行內理由 |
| STYLE §5、§9 Meta-claims | 「point at the line, the table row or the label」 | meta-talk：「the answer to the prompt」「clause 3」「step (2) of the box」「the eighth and ninth items」 |
| STYLE §7 Promises、§12.1 | 前向承諾要記入 STATUS；允許 Looking ahead | meta-talk：「Section 4.3 shows …」「the promise of Section 1.2」 |
| STYLE §3 step 8、step 11；§10、§11.1；§11.6；§12.5；§12.13.3；§12.14、§2 item 6；§8 | 模板的名稱直接印上版面：「Non-example by minimal change」「Payoff」「*Self-explain lines 3–5.*」「**Marking scheme** … Fatal errors (0 for the step)」「Givens / Goal」「Not allowed … tagged with the clause it breaks」「(N3)」「Template / When to use / The usual failure」「fold」 | process-jargon |
| STYLE §3 順序 | Situate → Hook → Slogan → **Definition** → Paraphrase → … → **Examples**（第 7 步）；Hook 允許「a goal theorem stated first」；§4 是敘述先、Idea 後 | abstract-before-example |
| STYLE §7 Voice | 只規定中位句長 12–18，沒有上限，也沒限制括號、分號 | long-sentence |
| STYLE §4「Say what each constant depends on」、「where the second equality uses …」 | 鼓勵在句尾補子句 | long-sentence |
| （缺規則） | 沒有規定代號 (Eq3)、(Fn1)、(O3)、(S1)、(W3)、(N4) 要用文字重述；同一冊重用 (T1)–(T5)、∼ | notation-load |
| STYLE §12.0「Instructor notes: comparisons with other calculi, remarks on conventions」；§10「Choice and non-constructive steps are flagged in prose」；DRAFTING「plainly marked as not proved here」 | 這些內容本該放進 fold，卻常寫在主線；excluded-middle、other logics、Lean 欄位的旁白 | tone |
| fd3 Ch1 identification 決定（citing rule） | 跨冊引用政策寫進了正文 | process-jargon、meta-talk（fd3 §1.4 最難的部分） |
| PIPELINE 全流程 | S2–S8 沒有任何一個審稿人以新手身分讀稿；可讀性只有 Referee B 的一句「effort proportional to difficulty」。每一輪修正都增加精確度子句，沒有東西把它們減回去 | 所有類別都會隨審稿輪次累積 |

**總結。** 規則是為了讓「每句話都可查核」而寫的，而它也確實做到了：pilot 沒有發現錯誤的證明步驟。但查核用的工具，也就是來源、label、步驟編號、版面指標，全部印在讀者面前。下一節的提案不減少可查核性，只是把查核用的資料從句子裡移出去：移到證明末尾的 Uses 行、ledger 和工具裡。

---

## §4 提案：STYLE.md 新增一節

以下英文是準備插入 STYLE.md 的文字，建議作為 §13，放在 §12 之後。

```markdown
## 13. Writing for a beginner (fd1–fd3 and every introductory volume; binding)

The reader of §1 has just left school. Every sentence they read should be about mathematics,
in words they have already been given. The checking apparatus of §9 stays complete; it moves
out of the sentence and into the Uses line, the ledger and the tools. `tools/check_beginner.py`
checks B1, B4, B6 and B7 mechanically; Referee C (PIPELINE S5) checks the rest.

**B1. One reference per sentence.** A sentence of main-line prose, proof, idea or solution
carries at most one inline `@ref` (two only when the sentence compares the two results).
Every other source goes into a **Uses line**, the last paragraph of the proof, solution or
idea: `*Uses:* @fd2:def-quotient-set (every class is some [x]); @fd2:prp-function-equality.`
A Uses entry names what the source gives in at most five words. The Uses line is inside the
block, so `check_forward_deps.py`, the dependency graph and Referee B read it as a citation.

**B2. Justify inline only the step that matters.** Give the reason inside the sentence only
for (i) the step that uses a hypothesis or the result just proved, (ii) a step a reader could
doubt: dividing, a sign, the direction of an inequality, a swap of quantifiers, a choice,
excluded middle, and (iii) the clause of a definition being verified, named in words.
Arithmetic and algebra whose laws the volume has already proved get no inline citation. One
sentence per proof ("All rearrangements use @thm-…") or the Uses line covers them. The ledger
still lists every such fact (§9); B2 changes where the reason is printed, not whether it exists.

**B3. No sentences about the text.** Main-line prose never describes the page's own devices:
"the fold below", "the box", "the prompt", "this subsection", "clause 3 of the list", "the
eighth item", "now with a label", "we state it as a proposition because later sections cite
it", "placed here for that reason", labelling or citation policy. Allowed: the opening frame's
one sentence on what the section does; the one Looking ahead box (§12.1); "the table above",
"the derivation above" when it is on the same screen. A meta-claim (§9) names the mathematics
("the step that uses x > 0"), not the device ("step (2) of the box").

**B4. Authoring vocabulary is never printed.** These words do not appear in reader-facing text
(headings and box titles included): core track, exit check, named move(s), method box, move
(for a proof technique), fold, hook, payoff, prompt, self-explain, template, the usual failure,
non-example by minimal change, degenerate, Givens/Goal, citing rule, ledger, legal
source/target, fatal error. Replacements: the Time line of §2 reads "About N hours if you read
the main text and do every A exercise and one B and one C exercise per section; about M hours
for everything."; "Named moves" becomes "Proof methods in this chapter"; a method box's parts
are "How it goes / When to use it / Common mistakes"; the Givens/Goal table's columns are
"We know | We want"; a marking scheme is headed "What a complete answer needs" and ends with
"Slips that lose the step"; a self-explanation prompt reads "*Before reading on: explain to
yourself why lines 3–5 follow.*"

**B5. A concrete case before the general statement.** A definition or theorem that
introduces two or more new symbols, or is stated over a general X, is preceded on the page by
a worked instance with small numbers or a small finite set (school level first, §12.9). §3's
order becomes Situate, Hook, **Instance**, Slogan, Definition, …; a theorem's lead-in may be
the instance. A worked instance placed before its theorem carries no label and cites nothing
later.

**B6. Sentence shape.** Main-line sentences have at most 35 words (displays excluded), at
most one parenthesis and no parenthesis inside a parenthesis, and at most two semicolons. The
median stays 12–18 (§7). A list of three or more results, cases or conditions is a displayed
list, not a run-on sentence. A sentence whose subject and verb are more than 15 words apart is
rewritten.

**B7. Codes in words.** A clause or rule code — (Eq3), (Fn1), (O3), (F9), (S1), (W3), (P5),
(N4), (I2) — is never used alone. At its first use in each section it comes with its meaning
("transitivity, (Eq3)"; "every upper bound is at least s, (S2)"). An entry of the "not
allowed" catalogue is always cited with the error in words ("using one letter for two
witnesses, (N4)"). No code is reused within a volume for a different list.

**B8. Chapter openings are for someone who has not read the chapter.** The story uses only
words from earlier chapters or words explained in the same sentence. "What you need" has at
most five items, in words, with at most five links; the full list of cited results is a
generated "Results used from earlier volumes" list at the end of the chapter. Proof methods,
Summary and Terms move to the end of the chapter (a "Chapter review" page), not the opening.

**B9. Talk to this reader only.** Remarks addressed to readers of other books (terminology
elsewhere, other logics, constructive concerns, Lean, which direction of a law is classical,
what "some books call sound") go into a fold titled "For instructors", or are cut. §10's
flag on choice stays, as one clause in words ("this step makes infinitely many choices at
once"), and never before choice has been named.

**B10. Other volumes by name.** A cross-volume pointer names the volume and the result in
words with one link ("*Sets and Functions* proved that every class is some [x]
(@fd2:def-quotient-set)"), never a chain ("the remark after X, by Y").

**B11. No planted doubts or private metaphors.** Do not hedge a settled point ("as far as we
know", "need not have been built at all", "with no choice made" before choice exists), and
do not use figurative verbs in proofs ("spends (I1)", "earns its keep", "holds it in", "read
from right to left"). State the fact and, if needed, where it is proved.

**B12. Line bookkeeping.** An example spends at most one sentence mapping line numbers
between two derivations or two levels; otherwise name the step ("the line that applies δ₀ at
x₀").

**B13. Slogans are followed by plain words.** An italic slogan or aphorism is immediately
followed (or preceded) by an ordinary sentence that says the same thing literally.
```

### 4.1 必須修改的現有規則

| 現有規則 | 修改 |
|---|---|
| STYLE §1「Recall before use … link it with `@label`」 | 改為「recall it in words; link it inline only when it is the step's point (B2), otherwise in the Uses line (B1)」。 |
| STYLE §2 item 3、4、6；§11.9；§12.13.5 | 依 B4、B8 改 Time 行的模板、What you need 的上限、Named moves 的名稱，並把 Summary、Terms 移到章末（需作者決定，見 §6 Q2）。 |
| STYLE §3 順序；step 8、step 11 | 插入 Instance（B5）；step 8、step 11 的名稱只供作者使用，不印上版面。 |
| STYLE §4 item 4「Every step names its reason」 | 改為「Every step has a reason the reader can find: inline for the steps listed in B2, otherwise in the Uses line」。「Always justify」清單保留，但改成用文字寫出。 |
| STYLE §5、§9 Meta-claims | 「point at the line, the table row or the label」改成「name the mathematical step or object」，並加上 B3 的禁用清單。 |
| STYLE §6、§11.6 Marking scheme | 標題與「Fatal errors」改為 B4 的寫法；評分內容不變。 |
| STYLE §10、§11.1 self-explanation | fd1 Ch8 照樣教一次「self-explanation」這個概念，但之後的提示用 B4 的白話句。 |
| STYLE §12.5 Givens/Goal | 欄名改成「We know | We want」，每列寫成完整句子。 |
| STYLE §12.13.3「tagged with the clause it breaks」 | 改成用文字標出被違反的條件（例如「cites a box that is already closed」），條款編號放進括號（B7）。 |
| STYLE §12.0 Instructor notes | 明訂放進「For instructors」fold（B9），不放主線。 |
| STYLE §1「fd1 is unchanged」 | §13 適用於 fd1–fd3 全部。 |
| DRAFTING Rules | 加一行：「Writing for a beginner (STYLE §13): B1–B13; run `tools/check_beginner.py`.」並在回覆格式加上它的結果。 |
| PIPELINE S4 | 加入 `tools/check_beginner.py`（B1 每句引用數、B4 禁用詞、B6 句長與括號、B7 單獨出現的代號）。 |
| PIPELINE S5 | 加 **Referee C（新手讀者）**：拿六份報告用的同一份 brief 與類別，只讀主線，不看 ledger；`stuck` 算 `gap`，`slowed` 算 `minor`。 |

### 4.2 來源查核如何保留

- **Ledger 不變。** §9 的 ledger 仍列出每個沒有 `@ref` 的事實。B2 只改「理由印在哪裡」，Referee B 照樣把「證明用到的事實」和「行內 ref ∪ Uses ref ∪ ledger」做差集，一個事實都不會漏。
- **工具不變。** Uses 行在 proof/solution 區塊內，`check_forward_deps.py`、`check_optional.py`、依賴圖和 reading paths 讀到的 `@ref` 集合跟現在一樣。試寫驗證了這一點：一個引用目標都沒有遺失。
- **Meta-claim 仍可查核。** 改成指向數學內容後（「the step that uses x > 0」），Referee B 照樣能在頁面上找到它。

---

## §5 成本與計畫

**規模。** fd1 有 50 個 section、8 個 index，fd2 有 24 個 section、6 個 index，fd3 有 27 個 section、6 個 index，共 **101 個 section、20 個章首頁**。主線字數（含習題）：fd1 366k、fd2 159k、fd3 121k，合計約 646k 字（`check_structure.py --words`）。

**審稿會失效。** PIPELINE 規則 4：verdict 綁定內容 hash，所以措辭一改，被改到的區塊 verdict 全部 stale。數學內容不變，所以不需要重跑完整的 S5/S6。建議用輕量的**等價複審**，比照現在的 S7r：fresh referee 拿到 diff，檢查四件事：(1) label、敘述、證明步驟逐一對應；(2) 原來所有 `@ref` 都還在（行內或 Uses）；(3) 沒有新的前向引用；(4) 數值不變，sidecar 照跑。另外每冊抽 5–6 節給 Referee C 重讀，確認可讀性確實改善。

**分階段順序**（一次只跑一個 workflow，照記憶中的 lean workflows 規則）：

| 階段 | 內容 | 規模 | 風險 |
|---|---|---|---|
| 0 | 作者核准 §13 與試寫；寫 `tools/check_beginner.py`；改 STYLE、DRAFTING、PIPELINE | 1 個 workflow | 無內容風險 |
| 1 | 機械替換，三冊一起：Time 行、Named moves 標題、Marking scheme 標題、Givens/Goal 欄名、method box 小標、「fold」一詞 | 腳本加人工抽查 | 低（不碰數學） |
| 2 | 20 個章首頁（B8），三冊 | 約 20 個改寫加等價複審 | 低；這一步就消掉 15% 的問題 |
| 3 | **fd1**，按章，從 Ch1–4 開始 | 50 節 | 中：fd1 最大，但它是入門冊，讀者最多 |
| 4 | fd2 | 24 節 | 中 |
| 5 | fd3（fd4/fd5 合併收尾後再做，避免同時動 fd3 的 label 文字） | 27 節 | 中 |
| 6 | fd4（合併後的新冊）在起草階段就直接套用 §13 | — | — |

**粗估。** 每節一個改寫 agent（措辭品質需要強模型，不建議用 Sonnet）加一個等價複審，約 0.15–0.25M tokens，101 節合計約 15–25M tokens。階段 1–2 另計約 2–3M。若每個 workflow 處理一章，約 22 個 workflow。

**本診斷不處理的事。** 有幾條建議是結構調整，不只是措辭，需要另外決定。例如 fd2 §1.3 把集合代數的主證明換成逐元素追蹤、把後設邏輯的證明移進 fold；fd3 §1.4 的跨冊引用政策移到附錄；fd3 §3.3 把四個代數恆等式從 fold 搬回主線；fd1 §4.8 的十五個標籤改成標註的真值表。這些應該在各冊改寫時逐條列給作者決定。

---

## §6 給作者的問題

1. **Uses 行要不要給讀者看到？** 選項：(a) 證明末尾一行小字，讀者看得到；(b) 只放在 HTML 註解或 ledger 裡。
   **建議 (a)。** 自學的讀者偶爾還是想知道「這一步憑什麼」。小字放在證明末尾，不打斷句子，引擎只要加一個樣式即可。

2. **章首頁的 Proof methods、Summary、Terms 要搬到哪裡？** 選項：(a) 每章章末加一頁「Chapter review」；(b) 留在 `index.md`，但放到「Read after the chapter」標題之下。
   **建議 (a)。** 章首只留故事、What you need（≤5 項）和 Time。這樣一次解決 78 條章首問題中的大半，glossary 的組裝方式也不受影響。

3. **範圍和順序是否照 §5：先機械替換和章首頁，再 fd1 → fd2 → fd3（fd3 等合併收尾），並用等價複審取代完整 S5？**
   **建議照做，從 fd1 Ch1–4 開始。** fd1 是入門冊，stuck 數和 fd2、fd3 一樣多，而且它的用語（box、fold、clause、Givens/Goal）一路被後兩冊沿用，先改 fd1 的收益最大。

---

## §7 `check_beginner.py` 基準線（2026-11-01）

作者採納 §4 之後（「對，照這個方向做」；Uses 行以小字顯示在證明末尾；章首的 Proof methods、Summary、Terms 移到章末的 Chapter review 頁），規則寫進 STYLE §13，機械可查的部分做成 `tools/check_beginner.py`（唯讀，預設只提示，`--strict` 才會失敗）。下表是改寫前 fd1–fd3 的基準，量的是 `f6d7a62` 的原文（`python3 tools/check_beginner.py --book fdN --summary`）。改寫各冊時，用同一個指令比較前後數字。

| 類別 | 規則 | fd1 | fd1 改寫後 | fd2 | fd3 | 合計 |
|---|---|---:|---:|---:|---:|---:|
| `refs`：一句有兩個以上行內 `@ref`（Uses 行不算） | B1 | 252 | 7 | 376 | 587 | 1,215 |
| `long`：一句超過 35 字 | B6 | 938 | 11 | 348 | 296 | 1,582 |
| `nested`：括號裡又有括號（`@ref (a)` 的條款標記不算） | B6 | 103 | 0 | 46 | 68 | 217 |
| `semicolons`：一句超過兩個分號 | B6 | 143 | 6 | 23 | 20 | 186 |
| `term`：作者用語上版面（含標題、框標題） | B4 | 394 | 0 | 241 | 183 | 818 |
| `code`：代號單獨出現（「by (Eq3)」） | B7 | 198 | 4 | 107 | 323 | 628 |
| `time-line`：舊的 Time 行模板 | B4 | 8 | 0 | 6 | 6 | 20 |
| `index-part`：章首頁有 Named moves、Summary 或 Terms | B8 | 24 | 0 | 18 | 16 | 58 |
| `need`：What you need 超過五個連結 | B8 | 3 | 0 | 6 | 6 | 15 |
| **合計** | | **2,063** | **28** | **1,171** | **1,505** | **4,739** |
| 每萬字（主線字數見 §5） | | 56 | 0.7 | 74 | 124 | 73 |

**fd1 改寫後（2026-11-01）。** 「fd1 改寫後」一欄量的是 fd1 第 1–8 章 STYLE §13 措辭改寫（S3e/S5e，commit 50099e0、088a23e、9f59a6e、524607b、7867d46、a83ec04、8f8a974、afb722c，加上收尾 commit）之後的原文，指令相同（`python3 tools/check_beginner.py --book fd1 --summary`）。2,063 條降到 28 條，每萬字從 56 降到 0.7（主線字數 366k → 377k，`check_structure.py --words`）。剩下的 28 條還沒逐條判斷（工具只是提示）：`refs` 7（第 8 章 6、第 6 章 1）、`long` 11（第 4 章 5、第 8 章 4、第 7 章 2）、`semicolons` 6（第 2 章 3、第 4 章 2、第 7 章 1）、`code` 4（第 7 章 3、第 4 章 1）。`term`、`time-line`、`index-part`、`need`、`nested` 全部歸零。「合計」欄仍是三冊改寫前的合計。

**怎麼讀這張表。**

- 這是提示，不是錯誤數。`refs` 會把「比較兩個結果」的句子也算進去（B1 允許兩個）；`code` 是啟發式，「transitivity, (Eq3)」不算，「by (Eq3)」算。工具只看得到形式，判斷交給起草者和 Referee C。
- 三冊的形狀不同，和 §2 的讀者報告一致。fd1 主要是長句（每萬字 26 句）和作者用語（`term` 394，其中 fatal error(s) 167、fold 83、Givens 35、degenerate 33、exit check(s) 28），fd3 主要是引用堆疊（每萬字 49 句）和代號（323）。fd3 從 Peano 重建數系，每一步都引用，正是 §3 指出的不對稱誘因。
- `time-line`、`index-part`、`need` 三類（共 93 條）全部集中在 20 個章首頁，§5 的階段 1–2 可以一次清掉。
- 這個工具只量 B1、B4、B6、B7、B8 的形式部分。B2（該不該在句中給理由）、B3（談文本自身）、B5（先例子）、B9–B13 要靠 Referee C（PIPELINE S5）閱讀判斷。
