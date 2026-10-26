# fd4 + fd5: merge proposal (one volume for the shared preliminaries)

**Status.** 提案，尚未核准（2026-10-26）。在作者核准、並回答 §6 的問題之前，`fd4/src`、`fd5/src`、任何 config、ledger、sidecar 與 math-atlas registry 都不動。fd3 目前有另一個 workflow 在改，本提案對 fd3 的修補（§5.4）一律排在那個 workflow 收尾之後。

**Conventions.**（沿用 fd2、fd3 re-cut）
- 章號按位置計；atlas id 與章號脫鉤（F4.1 早就不是 fd4 的第 1 章了）。
- **標籤一律不改名。** 已核對：fd4 的 71 個標籤與 fd5 的 381 個標籤沒有任何重名（兩冊 `_build/crossref_labels.json` 的交集為空），合併後同一個 label 命名空間不必改名。
- 時數取各章 index.md 的 Time 行（已成稿）或 blueprint 的估計（S1）；沒有 blueprint 的章（F4.6、F4.10）為本提案的估計，標 *est*。「core／full」= 核心路線／全部。
- 字數為 `wc -w`（含習題與摺疊，非主線字數）。

---

## 1. 為什麼要合併

作者的話（2026-10-26，verbatim）：

> 「fd4 與 fd5 可以合併成一本嗎，我覺得裡面講的東西兩邊都會用到」

盤點下來，作者的判斷有具體根據：

1. **F4.1 複數兩邊都用。** fd5 已成稿的四章引用 `@fd4:` 共 130 次（F5.2 37、F5.3 17、F5.4 10、F5.5 66），全部指向 F4.1；線代各冊另引 F4.1 109 次。F4.1 實際上是代數那一半的地基，卻放在「分析」那一冊。
2. **兩冊的計畫章彼此重教。** spec/08 為了讓 fd4 不依賴 fd5，在 F4 的計畫裡刻意重做了代數冊已有的東西：
   - F4.7 §05「Polynomial Functions and Their Roots」直接在 ℝ → ℝ 的函數上證因式定理與「至多 d 個根」（blueprint：「without fd5」），F5.4 §04、F5.5 §04 已經證過一般版本。
   - F4.6 計畫的二項式定理與有限和，F5.2 §06 已經在交換環上用 Pascal 規則證過（不用除法）。
   - F4.6 計畫的有限形式 Cauchy–Schwarz（Lagrange 恆等式）與 F4.8 §05 的 `thm-cauchy-schwarz-rn` 是同一個定理。
   - F4.10 的單位根、極式與 F4.1 §05–§06 重疊；F4.10 的「ℂ 的等距是 az+b 或 a z̄+b」與 F4.9 §06「Isometries of the Line and the Plane」重疊。
   合成一冊後，每個結果只證一次，其餘一律引用，符合 house aim「不重教」。
3. **代數那一半分析也用。** AN2.12（Euler 乘積）引用 `@fd5:thm-fundamental-arithmetic`；PMA 的考試目標把 F5.5 的代數基本定理列為 PMA 8 的覆蓋章。分析讀者並非完全不碰 fd5。
4. **系列讀序本來就是線性的。** spec/08 的圖是 F3 → F4 → F5，F5 只依賴 F4.1；兩冊之間沒有反向依賴，合併不會產生環。

---

## 2. Inventory

### 2.1 已成稿的章

| atlas id | 現址 | 章名 | 狀態 | 字數 | 時數 core／full | 前置（plan-edges `s`） | 誰引用它 |
|---|---|---|---|---|---|---|---|
| F4.1 | `fd4/src/ch01-complex-numbers/`（7 檔） | Complex Numbers | approved pending S9 | 45,213 | 25／35 | F2.1、F2.5、F3.10、F3.4、F3.2；b AN1.10（`ax-cosine-sine`） | fd5 src 130 次（ch02 37、ch03 17、ch04 10、ch05 66）；LA split 109 次（la1–la4、ma、nla、geo）；an1 blueprints 17 次（ch04、ch08、ch09）；plan：F4.10、CA.1、MA、exam targets apostol-ma／pma |
| F5.1 | `fd5/src/ch01-divisibility-and-congruences/`（5 檔） | Divisibility and Congruences | fd3 re-cut 剛搬入（b401a06），deepen pending | 37,509 | 25／30 | F3.2、F3.11 | fd3 src 21 次（ch04 5、ch05 16：`thm-quotient-ring-by-ideal`、`def-ideal-commutative-ring`、`def-integers-mod-n-ring`）；an2 blueprint ch05 與 coordinator notes 3 次（`thm-fundamental-arithmetic`）；F5.2、F5.3、F5.5 |
| F5.2 | `fd5/src/ch02-fields/`（7 檔） | Fields | approved pending S9（2026-10-25 從 fd4 原樣搬來） | 51,980 | 25／40 | F5.1；see F4.1、F3.10、F3.4、F3.9 | LA split 大量（`thm-field-basic-properties` 35、`def-characteristic` 32、`def-field` 21 …）；F5.4、LA1 |
| F5.3 | `fd5/src/ch03-groups-and-permutations/`（6 檔） | Groups, Subgroups, and Homomorphisms | 同上 | 47,413 | 25／35 | F2.1、F5.1；see F1.6、F2.6 | LA2.7（sign）、AL1；LA split（`exm-groups`、`thm-homomorphism-basic-properties` …） |
| F5.4 | `fd5/src/ch04-formal-polynomials/`（6 檔） | Formal Polynomials | 同上 | 49,542 | 25／35 | F5.2；see F4.1、F5.3 | LA split（`thm-evaluation-respects-operations` 56、`thm-degree-of-product` 45 …）；F5.5、LA1、AL2.2 |
| F5.5 | `fd5/src/ch05-polynomials-over-a-field/`（7 檔） | Polynomials over a Field | 同上 | 68,828 | 30／45 | F5.4、F5.1、F4.1、F3.10、F3.4 | LA2.6（revisits）、LA2.10、CA.2（revisits）、exam target pma |
| 小計 | | | | 300,485 | **155／220** | | |

LA split 對 fd5 的引用合計 409 次（120 個 src 檔），對 fd4 的 109 次；`linear-algebra-split` 目前停在 WIP（7a79e59 "stopped mid-run"）。

`fd5/authoring/parked/`：`from-fd2/03-binary-operations.md`、`from-fd2/04-permutations-and-iteration.md`（F5.3 的素材）、`from-fd3/from-6.4-q-sqrt2.md` 與 `ledger-parked.yaml`（F5.2 的 ℚ(√2) 素材）。合併時整個目錄搬到 `fd4/authoring/parked/`，用途不變。

### 2.2 計畫中的章（fd4，spec/08 §A2）

| atlas id | 章名 | blueprint | 時數 core／full | 前置 | 下游 |
|---|---|---|---|---|---|
| F4.6 | Inequalities, Finite Sums, and Real Powers | **無**（f4-6.md 尚未寫） | *est* 30／40 | F3.9、F3.4、F2.2 | AN1.1（revisits）、AN1.2、AN2.12、F4.7、F4.8、F4.11 |
| F4.7 | Real Functions and Their Graphs | `f4-7.md`（S1，7 節） | 35／50 | F4.6、F2.1；see AN1.10 | AN1.5、AN1.10（revisits）、AN2.12、F4.11；病態函數表起點（spec/08 §C5） |
| F4.8 | Coordinates and Vectors in ℝⁿ | `f4-8.md`（S1，6 節，約 23,000 主線字） | 25／40 | F4.6、F2.1 | AN1.4、AN1.7、AN2.3、F4.9、F4.11；LA1.1、LA3.11 see |
| F4.9 | Lines, Convexity, and Isometries of ℝⁿ | `f4-9.md`（S1，6 節） | 30／42 | F4.8 | F4.10 s；F4.11 see；chapter-constraints 規定等距分類不用線代 |
| F4.10 | Rotations, Angles, and the Complex Plane | **無** | *est* 25／35 | F4.1、F4.9 | CA.1 s；AN1.10 revisits；exam target apostol-ma（Apostol 1） |
| F4.11 | Metrics and Norms | `f4-11.md`（S1，6 節） | 30／40 | F4.8、F4.7、F4.6；see F4.9 | AN2.1 s（AN2.1 已搬進 AN1 當第 3 章） |
| 小計 | | | **175／247** | | |

照原計畫各自成冊：fd4 七章約 200／282 h，fd5 五章 130／185 h，合計 **330／467 h**。

---

## 3. 合併後的單一冊

### 3.1 Slot：保留 fd4，退役 fd5（建議）

理由：

1. **系列序號連續。** F1 → F2 → F3 → F4，退役 fd5 之後基礎系列是 fd1–fd4 四冊，沒有空號；反過來保留 fd5 會留下 fd4 的空洞，books.json、series.py、preview 的排序都要特例。
2. **F4.1 是全冊的中樞**，而且是全冊被引用最多的章；保留它所在的 slot，它的 `@fd4:` 引用（LA 109 次、an1 blueprints 17 次）一處都不用改。
3. **改寫量差距小，而且可以延後。** 退役 fd5 要改 `@fd5:` → `@fd4:` 約 433 處（LA 409、fd3 21、an2 3）；退役 fd4 要改約 126 處（LA 109、an1 17）。差距看似大，但全部是機械替換，而且因為兩冊標籤不重名，各書的 `external-books.fd5` 可以先改指 `../fd4/_build/crossref_labels.json`，**所有 `@fd5:` 引用當天就能照常解析**，替換留到各書自己的下一個 commit（fd3 等現行 workflow 收尾、LA split 恢復時）。兩個方向下，fd5 src 內的 130 處 `@fd4:` 都會變成同冊引用，要改成裸 `@label`，這部分不分方向。
4. **atlas 前例。** spec/08 決策 1 已核准「F4 是分析與後續的 prelim」；保留 F4 不需要重開那個決策。

### 3.2 書名（選項）

| 選項 | 書名 | subdir | 評語 |
|---|---|---|---|
| (a)（建議） | *Preliminaries for Analysis and Algebra* | `preliminaries` | 直接說出「兩邊都用」；subdir 短 |
| (b) | *Analytic and Algebraic Preliminaries* | `analytic-and-algebraic-preliminaries` | 最貼近兩個舊名，讀者一看就知道是合併；稍長 |
| (c) | *Numbers, Polynomials, and Space* | `numbers-polynomials-and-space` | 依內容命名，和 *Number Systems*、*Sets and Functions* 同一風格；不提「預備」 |

中文名建議「分析與代數預備」。

### 3.3 章序

依賴關係決定的形狀是「共同地基 → 兩條各自獨立的支線」：

- 兩邊都要的：F4.6（有限和、二項式、不等式、實數冪）、F5.1（ℤ 的算術；F5.2 s、AN2.12 s）、F4.1（F5.2–F5.5 與 AN、CA、LA 都用）。
- 只有代數／線代要的：F5.2–F5.5。
- 只有分析要的：F4.7、F4.8、F4.9（F4.8 對 LA1 只是 see）。
- 兩條支線之間沒有任何 s 邊（核對：F5.2–F5.5 不用 F4.7–F4.9；F4.7 刪掉 §05 之後不用 F5；F4.9 吸收 F4.10 後只要 F4.1、F4.8）。

把已成稿的代數支線排在計畫中的分析支線**之前**，是為了機械上的穩定：已成稿章的章號只改一次，之後分析支線怎麼增減（例如 F4.11 去留）都不會再動到已審過的正文。

| Ch | atlas id | 章名 | 目錄 | 來源 | 時數 core／full |
|---|---|---|---|---|---|
| | | **Part I. Common Ground** | | | |
| 1 | F4.6 | Inequalities, Finite Sums, and Real Powers | `ch01-sums-inequalities-and-powers/` | 新寫；二項式定理在交換環上陳述，有限 Cauchy–Schwarz 讓給 Ch 9 | *est* 30／40 |
| 2 | F5.1 | Divisibility and Congruences | `ch02-divisibility-and-congruences/` | fd5 ch01（deepen 照原計畫，改寫開頭的 What you need） | 25／30 |
| 3 | F4.1 | Complex Numbers | `ch03-complex-numbers/` | fd4 ch01，正文不動，只改指標 | 25／35 |
| | | **Part II. Algebraic Structures** | | | |
| 4 | F5.2 | Fields | `ch04-fields/` | fd5 ch02；§06 的二項式定理改引 Ch 1，只留 Frobenius 與 Fermat | 24／38 |
| 5 | F5.3 | Groups, Subgroups, and Homomorphisms | `ch05-groups-and-permutations/` | fd5 ch03 | 25／35 |
| 6 | F5.4 | Formal Polynomials | `ch06-formal-polynomials/` | fd5 ch04；§04 接收 F4.7 §05 原本要講的「多項式函數 vs 形式多項式」 | 25／35 |
| 7 | F5.5 | Polynomials over a Field | `ch07-polynomials-over-a-field/` | fd5 ch05 | 30／45 |
| | | **Part III. Functions and Space** | | | |
| 8 | F4.7 | Real Functions and Their Graphs | `ch08-real-functions/` | 新寫；**刪 §05**（因式定理與根數改引 Ch 6–7），6 節 | 30／43 |
| 9 | F4.8 | Coordinates and Vectors in ℝⁿ | `ch09-coordinates-and-vectors/` | 新寫；Cauchy–Schwarz 唯一的家 | 25／40 |
| 10 | F4.9 | Lines, Convexity, and Isometries of ℝⁿ | `ch10-lines-convexity-isometries/` | 新寫；§06 吸收 F4.10：平面的等距用 ℂ 寫成 az+b、a z̄+b，旋轉 = 乘單位複數，arg 不唯一（CA 分支的伏筆） | 32／45 |
| (11) | F4.11 | Metrics and Norms | — | **建議移到 AN1**（§6 Q3）；若留下則為 `ch11-metrics-and-norms/` | （30／40） |

### 3.4 計畫章的去留

| id | 處置 | 說明 |
|---|---|---|
| F4.6 | **留**，Ch 1 | 去重：二項式定理只在這裡證（交換環版本，F5.2 §06 改引）；有限 Cauchy–Schwarz 與 Lagrange 恆等式移給 F4.8（Lagrange 恆等式可留作 F4.8 的 C 題）。n 次方根與有理冪照 spec/08 用 sup 構造。blueprint 尚未寫，S1 時依本表定稿。 |
| F4.7 | **留**，Ch 8，刪 §05 | §05 是「為了不依賴 fd5」才存在的重教；合冊後直接引 F5.4 `thm-evaluation-respects-operations` 與 F5.5 的根數定理。病態函數表（§07）照舊是起點。 |
| F4.8 | **留**，Ch 9 | 不變；F4.1 的 see F4.8 反過來寫成 F4.8 指回 F4.1（ℝ² 即 ℂ 的平面）。 |
| F4.9 | **留並吸收 F4.10**，Ch 10 | §06 改名 *Isometries of the Line and the Plane; Rotations as Complex Multiplication*；s 邊加 F4.1。等距分類（§04–§05）不用線代的約束照舊。 |
| F4.10 | **合併進 F4.9 §06 與 F4.1**，id 退役 | 單位根、極式已在 F4.1 §05–§06；剩下的旋轉、arg、ℂ 的等距放進 F4.9 §06。renames `F4.10 → F4.9`；CA.1 s、AN1.10 revisits、exam target apostol-ma 的 F4.10 改為 F4.9。 |
| F4.11 | **建議移到 AN1**，併入 AN2.1 | 見 §6 Q3。AN2.1 *Metric Spaces and Their Topology* 已在 AN1 第 3 章，Apostol 3.13–3.15 本來就把度量公理、範數與開集放在一起；拆在兩冊只是為了「F4 鋪路」，結果是 F4.11 被迫「不碰收斂與開集」。`f4-11.md` 原樣轉成 AN2.1 S1 的前半素材。 |

### 3.5 篇幅與時數（**超過 ~250 h full，已標記**）

| 版本 | core | full |
|---|---|---|
| 原計畫：fd4（7 章）+ fd5（5 章）分冊 | 330 | 467 |
| 合冊，照 §3.3 建議（去重、F4.10 併入、F4.11 移出） | **271** | **386** |
| 合冊，F4.11 留下 | 301 | 426 |
| 讀者路線：代數／線代（Part I + II） | 184 | 258 |
| 讀者路線：分析（Part I + III） | 167 | 233 |

**警示。** 整冊 full 386 h，遠超 ~250 h。但已成稿的六章本身就是 220 h full，再加上兩條線都要的 F4.6，任何合併方案的整冊 full 都不可能壓到 250 h 以下，除非把已成稿的章移出去。因此本提案改用**讀者路線**當篇幅尺度：在 config 的 `reading-paths` 宣告兩條路線（Analysis：Ch 1–3、8–10；Algebra and linear algebra：Ch 1–7），兩條都落在 ~230–260 h full。合併比分冊省下約 60 h core、80 h full，全部來自去重。

若作者仍要壓整冊，可再刪的（依建議順序）：
1. **F4.11 → AN1**（已計入建議版）：−30／−40。
2. **F4.9 的等距分類（§04–§06）移到 GEO 或 LA3**，F4.9 只留直線、超平面、最近點與凸集：約 −14／−20。代價：F4.10 吸收的旋轉內容要另找地方（CA.1 開頭），而且 chapter-constraints 的「不用線代」規則要撤。
3. **全冊 C 題減量**：只影響 full，每章約 −3，合計約 −30 full。
三項全做：約 257 core／326 full，仍高於 250 full。

---

## 4. Atlas ids

### 4.1 保留 F5.x id，不重編（建議）

- **保留 F5.1–F5.5，章號與 id 脫鉤**，在 `registry/renames.yaml` 的 `moves` 各加一列 `{id: F5.k, from: F5, to: F4, decided: <date>, spec: fd4/authoring/design/merge-proposal.md}`。這與 AN2.1–AN2.3 搬進 AN1 的處理完全相同，atlas.py check 已支援「id 前綴與所在冊不同」。
- 不建議重編回 F4.2–F4.5：那四個 id 在 renames 裡已經是 `F4.2 → F5.2` 的舊名，再寫 `F5.2 → F4.2` 會讓重導鏈成環，`atlas.py check` 的 ids 規則會拒絕；改編成 F4.12–F4.16 則要動所有 plan-edges（AL1.2、AL2.2、AL2.5、AL2.6、LA2.6、LA2.7、CA.2 …）、exam targets、STATUS、LA split 的 la-edges，換來的只是前綴好看。
- **F4.10**：`ids` 加 `{old: F4.10, new: F4.9}`（併入）；chapters.yaml 刪 F4.10 列。
- **F4.11（若移到 AN1）**：`ids` 加 `{old: F4.11, new: AN2.1}`；AN2.1 的 s 邊刪 F4.11、加 F4.6、F4.7、F4.8。

### 4.2 registry 的其他修改

- `volumes.yaml`：F4 的 title 改為新書名、`title_zh: 分析與代數預備`；F5 列刪除（chapters 已全數 move 到 F4）。
- `renames.yaml` `volumes`：加 `{id: F4, old: "Analytic Preliminaries", new: "<新書名>", alias: analytic-preliminaries, …}` 與 `{id: F5, old: "Algebraic Preliminaries", new: "(merged into F4)", alias: algebraic-preliminaries, note: fd5 退役，子目錄與 fd5/ 路徑改指 F4}`（check 不讀 volumes，只是紀錄）。
- `plan-edges.yaml`：F4 段落的章序註解改為新序；F4.1 刪 `see: F4.8`；F4.8 加 `see: [F4.1]`；F4.9 `s: [F4.8, F4.1]`；F5.2 `s` 加 F4.6；F4.7 加 `see: [F5.5]`；CA.1、AN1.10 的 F4.10 → F4.9；F4.11 依 Q3 處理。
- `chapter-constraints.yaml`：F4.7 的「不依賴 F5」改為「因式定理與根數引用 F5.4、F5.5，不重證」；F4.9 加上旋轉與 ℂ 的等距。
- `exam-targets.yaml`：apostol-ma 的 F4.10 → F4.9（第 103、108、110 行）。
- spec/08：在 §A2、§A3 文末加 2026-10-26 更新註記（與 F5.1 那條同格式），不改原文。

### 4.3 `math-atlas/site/books.json`

- fd4 條目：`subdir` 改新 slug（建議 `preliminaries`），`blurb` 重寫，`planned` 改為 10（F4.11 留下則 11），`aliases: ["fd4", "fd5", "analytic-preliminaries", "algebraic-preliminaries"]`。
- fd5 條目刪除。舊路徑 `fd5/`、`algebraic-preliminaries/`、`analytic-preliminaries/` 都由 alias 產生 redirect stub。
- 章級重導：short-urls 下舊網址 `algebraic-preliminaries/ch1`–`ch5` 分別對應新 `ch2`、`ch4`–`ch7`，`analytic-preliminaries/ch1` 對應 `ch3`；寫進 fd4 config 的 `redirects`（目前是空物件），若 engine 的 alias 只做冊級重導，需要 book-engine 補一個章級對照（§6 不列為問題，屬實作細節，S 階段確認）。

---

## 5. Mechanics（結構提交，作者核准後一次做完）

### 5.1 搬檔（`git mv`，保留歷史）

| 來源 | 目的 |
|---|---|
| `fd4/src/ch01-complex-numbers/` | `fd4/src/ch03-complex-numbers/` |
| `fd5/src/ch01-divisibility-and-congruences/` | `fd4/src/ch02-divisibility-and-congruences/` |
| `fd5/src/ch02-fields/` … `ch05-polynomials-over-a-field/` | `fd4/src/ch04-fields/` … `ch07-polynomials-over-a-field/` |
| `fd4/verify/ch01/`；`fd5/verify/ch01–ch05/`（共 47 + 243 個 sidecar） | `fd4/verify/ch03/`；`fd4/verify/ch02/`、`ch04–ch07/` |
| `fd4/authoring/ledger/ch01.yaml`；`fd5/authoring/ledger/ch0k.yaml`、`archive/` | `fd4/authoring/ledger/ch03.yaml`；`ch02.yaml`、`ch04–ch07.yaml`、`archive/` |
| `fd4/authoring/blueprints/ch01.md`；`fd5/authoring/blueprints/ch0k.md` | `fd4/authoring/blueprints/ch03.md`；`ch02.md`、`ch04–ch07.md`（frozen 檔只改檔名，文首加一行搬家註記） |
| `fd4/authoring/blueprints/f4-7.md`、`f4-8.md`、`f4-9.md` | 原地保留，S1 修訂時依 §3.4 改（f4-7 刪 §05；f4-9 §06 加 F4.10 內容） |
| `fd4/authoring/blueprints/f4-11.md` | Q3 選 (a)：`analysis-series/an1/authoring/blueprints/` 作為 AN2.1 素材（另一個 repo 的 commit） |
| `fd5/authoring/parked/` | `fd4/authoring/parked/` |
| `fd5/build.py`、`fd5/tests/`、`fd5/latex/`、`fd5/_build/` | 刪除（與 fd4 的同名檔相同；先 diff 確認）；`fd5/spelling.txt` 併入 `fd4/spelling.txt`；`fd5/config/known-unresolved.json` 的條目併入 fd4 config（目前 fd4 沒有此檔） |

`fd5/` 整個目錄在結構提交後消失；不留錨點目錄（網址層的重導由 books.json alias 與 `redirects` 負責）。

### 5.2 Config

- `fd4/config/config.json`：`title`、`chapters`（七章，Part 標題若 engine 支援則加）、`reading-paths`（Analysis、Algebra and linear algebra 兩條）、`external-books` 刪 `fd5`、`redirects` 填 §4.3 的章級對照。
- fd1、fd2、fd3 的 `external-books.fd5`：先改成 `labels: ../fd4/_build/crossref_labels.json`、`url` 改新 subdir、title 改新書名（過渡 alias，讓 `@fd5:` 照常解析）；`external-books.fd4` 的 title 同步改。
- LA split 各冊（la1、la2、la4、nla、geo；la3、ma 只有 fd4）同樣處理 `fd4`、`fd5` 兩個 key；an1、an2 的 config 同。這些都在別的 repo，各自一個小 commit，不必與 foundations 同步。

### 5.3 引用改寫（foundations 內，結構提交當下）

1. 搬入的 F5 四章內 130 處 `@fd4:<label>` → `@<label>`（同冊引用）。
2. 散文指標用 `tools/renumber.py` 兩輪（沿用 fd2、fd3 的做法）：
   - 舊 fd5 章內的「Chapter k／Section k.j」→ 新章號（1→2、2→4、3→5、4→6、5→7）；
   - 舊 fd4 F4.1 內的「Chapter 1／Section 1.j」→ 3／3.j；
   - fd5 內 14 個檔提到的「*Analytic Preliminaries*, Section 1.4」之類 → 「Section 3.4」（同冊，去掉書名）；
   - F4.1 內提到「*Algebraic Preliminaries*, Chapter k」（8 個檔）→ 同冊章號。
3. `authoring/STATUS.md`：F4.1、F5.1–F5.5 各列加一句合冊註記與新章號；上游承諾表（paid 欄）裡的 `F4.1 §0k`、`F5.k §0j` 不動（以 id 記，不受章號影響）。
4. `authoring/NOTATION.md` 的「fd4 and fd5」段改為單冊；兩條相衝的列（`\omega`、`e` 的用法）重新核對。
5. 兩冊 index.md 合成一個新 preface：fd5 現有 preface 的「What it covers」表與 fd4 的合併，Time 行改為兩條路線的時數，「No borrowed fact」段保留 `ax-cosine-sine` 的說明。

### 5.4 延後的跨 repo 掃描（各自 commit，不擋結構提交）

| 對象 | 內容 | 時機 |
|---|---|---|
| fd3 src | 21 處 `@fd5:` → `@fd4:`；8 個檔的「*Algebraic Preliminaries*, Section 1.3／Chapter 1」→ 新書名與 Section 2.3／Chapter 2；3 個檔的 *Analytic Preliminaries* | fd3 現行 workflow 收尾之後 |
| fd1、fd2 src | 1＋3 個檔的 *Algebraic Preliminaries* 書名與章號 | 結構提交後的 downstream sweep |
| LA split src | 409 處 `@fd5:` → `@fd4:`；約 16 個檔的 *Algebraic Preliminaries*、11 個檔的 *Analytic Preliminaries* 書名與章號 | LA split 恢復時，在它自己的 WIP 之上 |
| an1、an2 blueprints | 17 處 `@fd4:` 不動；3 處 `@fd5:thm-fundamental-arithmetic` → `@fd4:`；10 個檔的 *Analytic Preliminaries* 書名與章號 | an1／an2 下一次 blueprint 修訂 |
| 過渡 alias 撤除 | 各 config 的 `external-books.fd5` 刪除 | 上面四列都做完、`grep -r '@fd5:'` 為空之後 |

### 5.5 Preview

- books.json 依 §4.3；`bin2/update_preview.sh` 照常跑一次（背景），CNAME 由腳本保留。
- 驗收：`fd5/`、`algebraic-preliminaries/`、`analytic-preliminaries/` 與其 `chN/` 都重導到新位置；新書 `ch1`–`ch7` 可讀；fd3 與 LA 各冊的 `@fd5:` 連結落在新網址。

### 5.6 驗收清單

`build.py` fd4 全書建置無 unresolved；`tools/check_structure.py --book fd4`；`check_numbers`（sidecar 路徑換章後全數找得到）；`tests/` 的 `test_built_book.py`；math-atlas `atlas.py check`（renames 鏈、moves 前綴、plan-edges 無環）；fd1–fd3 與 LA 各冊在過渡 alias 下重建無新增 unresolved。

---

## 6. 給作者的問題（每題附建議）

**Q1. 保留哪個 slot、id 怎麼處理？**
(a) 保留 fd4、退役 fd5，F5.1–F5.5 的 atlas id 不改，只在 renames 記 move；(b) 保留 fd4、退役 fd5，F5.x 重編為 F4.x 新號；(c) 保留 fd5、退役 fd4。
**建議 (a)**：序號連續、F4.1 的 126 處跨冊引用不動、`@fd5:` 靠過渡 alias 當天照常解析；重編 id 只換來前綴整齊，卻要改遍 plan-edges 與 LA 的對照，而且退回 F4.2–F4.5 會讓 renames 成環。

**Q2. 書名？**
(a) *Preliminaries for Analysis and Algebra*（分析與代數預備，subdir `preliminaries`）；(b) *Analytic and Algebraic Preliminaries*；(c) *Numbers, Polynomials, and Space*。
**建議 (a)**：直接說出合冊的理由，網址最短。

**Q3. F4.11 Metrics and Norms 留在本冊還是移到 AN1？**
(a) 移到 AN1，併進 AN2.1 *Metric Spaces and Their Topology* 的前半；(b) 留在本冊當 Ch 11（Part III 最後一章，章號不影響其他章）。
**建議 (a)**：Apostol 3.13–3.15 本來就把度量、範數、開集放在一起，拆兩冊才逼得 F4.11「不碰收斂與開集」；本冊省 30／40 h，分析路線降到 233 h full。代價是 AN1 變大，且 spec/08 決策 17 的理由（「F4.11 已鋪好度量」）要改寫。

**Q4. 篇幅超過 ~250 h full，接受哪一種？**
(a) 接受整冊約 271 core／386 full，以兩條讀者路線（代數 258、分析 233 full）為篇幅尺度，F4.10 併入 F4.9 與 F4.1；(b) 再把 F4.9 的等距分類移到 GEO／LA3，並減 C 題，整冊約 257／326；(c) 不合併，維持兩冊（330／467，重教的部分照 spec/08 寫）。
**建議 (a)**：已成稿六章就有 220 h full，整冊壓不到 250；合併已經靠去重省下 80 h full，每位讀者實際走的路線都在 250 h 上下。(b) 會拿掉作者在 spec/08 要的「不用線代證等距分類」。
