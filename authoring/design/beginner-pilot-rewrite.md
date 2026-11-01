# 初學者措辭試寫：fd3 §2.2 Well-Definedness, and the Arithmetic of the Integers

日期：2026-11-01。配套文件：`beginner-readability-audit.md`（§4 的規則草案 B1–B13）。
**原檔 `fd3/src/ch02-integers/02-well-defined-operations.md` 未改動。** 下面的 After 只是提案文字。

## 為什麼選這一節

新手讀者報告裡，fd1–fd3 共有 10 個 section 被評為難度 5。本節除了難度 5，還有 **5 個 stuck**，是所有 section 中最多的（第二名 fd3 §1.4 有 4 個，fd1 §2.5 有 3 個）。報告的總評是：「the general lemma comes before any concrete case on ℤ and introduces ∼, ≈, X, Y, f, F, g, G, S and S̄ all at once … Moving those [the heuristic and the failure examples] before the lemma would help a lot.」這幾個毛病（抽象先行、引用堆疊、作者用語、長句）正好是審計裡最主要的四類，所以拿它來試新規則最有代表性。

## 範圍

本節主線約 4,278 字。試寫範圍是第 1–183 行：開場、「Definitions through representatives」、「The lemma」、「Sum, product and negative of integers」，到命題證明後的那段為止，約 3,250 字（含數學），比任務建議的 ~1,500 字長。這樣取是因為 5 個 stuck 都在這一段（L20、L39、L57、L97、L137），從中間截斷就看不出規則的效果。「Rules that fail」和「The natural numbers inside the integers」兩小節不在範圍內。

**保持不變的部分**：所有 label（`thm-well-defined-on-classes`、`def-integer-operations`、`exm-method-one-argument-at-a-time`、`prp-integer-operations-well-defined`、`eq-integer-rep-change`、`eq-integer-product-target`），定理與命題的敘述（逐字），證明的每一步（順序與內容），Quick check，remark，以及摺疊區塊（逐字保留，見註 7）。原本所有 `@ref` 都還在檔內，只是部分移到證明末尾的 `*Uses:*` 行，所以依賴圖、`check_forward_deps.py` 和 dependency ledger 都不受影響（ledger 一行都不用改）。

## 改了什麼、為什麼（對應 §4 的規則）

1. **先例子，後引理（B5）。** 原文第 20 行直接給出帶十個符號的一般引理（讀者 stuck：「comes before a single concrete case on ℤ」）。新版在「Definitions through representatives」先算兩條具體規則：取第一座標（在 (0, 2) ∼ (1, 3) 失敗）和逐座標相加（成立）。引理敘述之後再加一段，把這兩個例子對回 (a) 和 (b) 的假設。§2.2 後面的 `exm-ill-defined-first-coordinate` 照樣存在，這裡只是預覽（不加 label，不引用它，避免前向引用）。
2. **一句最多一個引用，其餘放進 Uses 行（B1）。** 原 L57 一句 70 字、三個引用、兩層括號（stuck）。新版拆成五句，每句一步，來源集中到證明末尾的 `*Uses:*` 行。(a) 的證明也一樣處理。
3. **刪掉談文本結構的句子（B3）。** 原 L39「steps (1)–(3) of that method are its hypothesis, and step (4) is the graph built below」（stuck：引用另一冊方法框的步驟編號）改成直接講想法，最後一句才說它和 *Sets and Functions* 那個方法的關係。原 L102「the move this chapter is built on」改成平白敘述。
4. **作者用語不上版面（B4）。** `Givens | Goal` 改成 `We know | We want`；方法框的 `Template / The usual failure` 改成 `How it goes / Common mistakes`，失誤清單由名詞片語改成完整句子；「heuristic」改成「only a guide」。
5. **定義裡的長名詞句（B6）。** 原 L97 主詞和動詞之間隔著一串參數（stuck）。新版拆成三句，每句最多一個引用，內容不變：sum/product 是引理 (b) 從 g₊、g· 誘導出的函數，negative 是 (a) 從 (a, b) ↦ (b, a) 誘導出的函數。
6. **「read from right to left」（B11/B4）。** 原 L137、L162 用這個說法表示「把等式左右對調」（L137 stuck）。新版直接寫出對調後的等式 \( b + a' = a + b' \)，證明步驟不變。
7. **代號說成文字（B7）。** (Eq3) 寫成「transitivity, (Eq3)」，(Eq2) 寫成「symmetry, (Eq2)」，(Fn1)/(Fn2) 第一次出現時說明意思。摺疊區塊「The graph of G, checked as in (a)」逐字保留，這次只示範主線；正式改寫時摺疊區塊也要套用 B1。
8. **證明後的評論（原 L183）。** 原文「four equations in eight unknowns」讀者看不懂（實際只有兩條假設），改成「both hypotheses enter one computation」，意思一樣但不會誤導。

字數：After 的主線比 Before 多約 180 字，主要是開頭兩個具體例子和例子對回引理的那段。沒有刪去任何數學內容。

---

## Before（原文摘錄，第 1–183 行中的 stuck/slowed 處）

> **L3** Every operation on classes will be defined by a formula on representatives, and *Sets and Functions*, Section 5.2 showed what can go wrong: a formula that gives two answers for one class (@fd2:exm-ill-defined-class-map). This section proves, once and for all, the lemma that says when such a formula defines a function.

> **L9** Rather than repeat the argument of @fd2:prp-congruence-arithmetic for every formula, we separate it into two parts: a general lemma, proved here once, which turns a **check on representatives** into a function on classes; and the check itself, which is different for each formula and is all that remains to do each time.

> **L20（stuck：抽象先行）** Let \( \sim \) be an equivalence relation on a set \( X \), and \( \approx \) an equivalence relation on a set \( Y \). …（引理是本節第一個實質內容，之前沒有任何 ℤ 上的例子。）

> **L39（stuck：引用另一冊方法框的步驟編號）** Clause (a) is @fd2:exm-method-well-definedness turned into a theorem: steps (1)–(3) of that method are its hypothesis, and step (4) is the graph built below.

> **L57（stuck：長句）** The rest is the proof of (a) with pairs of classes in place of classes: the graph of all \( (([x], [y]), [g(x, y)]) \) has an output for each pair of classes, since each pair of classes is \( ([x], [y]) \) for some \( x, y \) (@fd2:def-cartesian-product, @fd2:def-quotient-set), and only one, by the paragraph above, @fd2:def-ordered-pair (equal pairs of classes have equal entries) and @fd2:thm-classes-partition (b); so it defines a function \( G \), and \( G \) is unique as in (a) (@fd2:prp-function-equality).

> **L97（stuck：名詞化長句）** The **sum** \( + \colon \nZ \times \nZ \to \nZ \) and **product** \( \cdot \colon \nZ \times \nZ \to \nZ \) are the functions that @thm-well-defined-on-classes (b), with \( X = \nN \times \nN \) and the equivalence relation \( \sim \) of @prp-integer-pairs-equivalence, induces from the maps \( g_+ \), \( g_\cdot \colon (\nN \times \nN) \times (\nN \times \nN) \to \nN \times \nN \) given by the pairs on the right; …

> **L102（作者用語）** The proof below uses the move this chapter is built on, after @fd2:exm-method-well-definedness:

> **L107–L111（記號、片語）** **Template.** … (2) fix \( x' \), take \( y \sim y' \), … **The usual failure.** Checking one numerical instance; using a law of \( \nZ \) to check an operation of \( \nZ \) (the computation stays in \( \nN \)); claiming symmetry for a formula that lacks it, such as \( [(a + d, \ b + c)] \).

> **L133–L137（stuck：作者用語）**
> `| Givens | Goal |` …
> `| every term of the goal contains \( c \) or \( d \); the given contains neither | multiply the given by \( c \), and, read from right to left, by \( d \) |`

> **L183（slowed）** Changing both at once is also possible, but the computation then mixes four equations in eight unknowns; one argument at a time keeps each computation to a single hypothesis.

---

## After（第 1–183 行的改寫全文）

````markdown
# Well-Definedness, and the Arithmetic of the Integers

Section 2.1 built \( \nZ \) as the set of classes of \( \sim \) on \( \nN \times \nN \), and gave each integer a normal form (@prp-integer-normal-form). The integers cannot yet be added. To add two classes, we will pick a pair from each and compute with the pairs. That is safe only if the answer does not depend on which pairs we picked. This section proves one lemma that says when it is safe, and then uses it to define the sum, product and negative of integers.

## Definitions through representatives

Start with a rule that goes wrong. Try to send each integer \( [(a, b)] \) to its first coordinate \( a \). The pairs \( (0, 2) \) and \( (1, 3) \) lie in the same class, since \( 0 + 3 = 2 + 1 \). Read with \( (0, 2) \), the rule gives \( 0 \); read with \( (1, 3) \), it gives \( 1 \). One integer gets two values, so the rule defines no function.

Now a rule that works. Add two classes by adding coordinates, \( [(a, b)] + [(c, d)] \coloneqq [(a + c, \ b + d)] \). Replace \( (a, b) \) by another pair \( (a', b') \) of its class, so that \( a + b' = b + a' \). Then
\[
(a + c) + (b' + d) = (a + b') + (c + d) = (b + a') + (c + d) = (b + d) + (a' + c) ,
\]
so the new answer \( (a' + c, \ b' + d) \) lies in the same class as the old answer \( (a + c, \ b + d) \). Changing the pair did not change the class of the result.

*Sets and Functions* met the same problem for \( \nZ/n \). There, the sum \( [a] + [b] \coloneqq [a + b] \) was checked to depend only on the classes (@fd2:prp-congruence-arithmetic). The rule \( [a]_6 \mapsto [a]_4 \), by contrast, gave one class two values (@fd2:exm-ill-defined-class-map).

The problem comes back for \( \nQ \) in Section 3.1 and for \( \nR \) later in this volume. Each time, a set is a quotient \( X/{\sim} \), and something is defined on it by a formula on elements of \( X \). So we split the work in two. A lemma, proved once, says: if equivalent inputs always give equivalent outputs, the formula defines a function on classes. Then, for each new formula, only that condition is left to check.

A rule "\( [x] \mapsto \) something computed from \( x \)" is called **well defined** when representatives of the same class always give the same result. The lemma covers three kinds of rule: a map from one quotient to another, a binary operation on a quotient, and a property of classes.

## The lemma

*A rule on classes is a function as soon as equivalent inputs give equivalent outputs.*

::: {#thm-well-defined-on-classes}
[Functions on Classes]

Let \( \sim \) be an equivalence relation on a set \( X \), and \( \approx \) an equivalence relation on a set \( Y \). Classes are taken for \( \sim \) in \( X \) and for \( \approx \) in \( Y \).

::: {.enumerate options="label=(\alph*)"}
1. Let \( f \colon X \to Y \) be a function such that, **for all** \( x, x' \in X \), \( x \sim x' \) implies \( f(x) \approx f(x') \). Then there is **exactly one** function \( F \colon X/{\sim} \to Y/{\approx} \) with \( F([x]) = [f(x)] \) for every \( x \in X \).
2. Let \( g \colon X \times X \to X \) be a function such that, **for all** \( x, x', y, y' \in X \),
\[
\begin{aligned}
x \sim x' &\implies g(x, y) \sim g(x', y) , \\
y \sim y' &\implies g(x, y) \sim g(x, y') .
\end{aligned}
\]
Then there is **exactly one** function \( G \colon (X/{\sim}) \times (X/{\sim}) \to X/{\sim} \) with \( G([x], [y]) = [g(x, y)] \) for all \( x, y \in X \).
3. Let \( S \subseteq X \) be such that, for all \( x, x' \in X \), \( x \sim x' \) and \( x \in S \) imply \( x' \in S \). Let \( \bar S \coloneqq \{ [x] : x \in S \} \subseteq X/{\sim} \). Then, **for every** \( x \in X \), \( [x] \in \bar S \) if and only if \( x \in S \).
:::
:::

In words: (a) says that a map on elements that respects the two relations passes to a map on classes; (b) says that a binary operation that respects \( \sim \) **in each argument separately** passes to an operation on classes; (c) says that a property that respects \( \sim \) can be asked of a class, and the answer is the answer for any of its representatives. Clause (a) will give the negative of an integer, (b) its sum and product, and (c) the positive integers in Section 2.4.

The two rules at the start of the section are cases of the lemma. For the first coordinate, \( X = \nN \times \nN \), \( Y = \nN \) with equality as \( \approx \), and \( f(a, b) = a \); the hypothesis of (a) fails at \( x = (0, 2) \), \( x' = (1, 3) \). For the sum, \( g \) adds coordinates, and the computation with \( (a', b') \) is the first hypothesis of (b).

::: {.idea}
A function is a graph with **exactly one** output for each input (@fd2:def-function). The obvious graph is the set of all pairs \( ([x], [f(x)]) \). Every class is some \( [x] \), so each class has at least one output. The only danger is two outputs for one class, coming from two representatives \( x \) and \( x' \) of it. Three steps rule this out. "Same class" means \( x \sim x' \) (@fd2:thm-classes-partition (b)). The hypothesis turns this into \( f(x) \approx f(x') \). The same theorem turns that back into "same output". For (b) the plan is the same, once the two one-argument hypotheses are chained into one statement about both arguments by transitivity. This is the check-on-representatives method of *Sets and Functions* (@fd2:exm-method-well-definedness), made into a theorem.
:::

::: {.proof}
*(a)* Let
\[
G_F \coloneqq \{ (C, D) \in (X/{\sim}) \times (Y/{\approx}) : C = [x] \text{ and } D = [f(x)] \text{ for some } x \in X \} ,
\]
a set by specification. A graph is a function when every input has an output (Fn1) and no input has two (Fn2); we check both.

(Fn1): every \( C \in X/{\sim} \) is \( [x] \) for some \( x \in X \), and then \( (C, [f(x)]) \in G_F \).

(Fn2): suppose \( (C, D) \in G_F \) and \( (C, D') \in G_F \), say \( C = [x] \), \( D = [f(x)] \), and \( C = [x'] \), \( D' = [f(x')] \). Then \( [x] = [x'] \), so \( x \sim x' \) by @fd2:thm-classes-partition (b). By the hypothesis, \( f(x) \approx f(x') \). By the same theorem, \( [f(x)] = [f(x')] \), that is, \( D = D' \).

So \( F \), the function with graph \( G_F \) and codomain \( Y/{\approx} \), is a function \( X/{\sim} \to Y/{\approx} \), and \( F([x]) = [f(x)] \) because \( ([x], [f(x)]) \in G_F \).

For uniqueness, let \( F' \colon X/{\sim} \to Y/{\approx} \) also satisfy \( F'([x]) = [f(x)] \) for every \( x \). Every \( C \in X/{\sim} \) is some \( [x] \), and then \( F'(C) = [f(x)] = F(C) \). The two functions have the same domain and codomain, so \( F' = F \).

*Uses:* @fd2:def-set-builder (\( G_F \) is a set); @fd2:def-function (Fn1), (Fn2); @fd2:def-quotient-set (every class is some \( [x] \)); @fd2:prp-function-equality (equal functions).

*(b)* First, let \( x, x', y, y' \in X \) with \( x \sim x' \) and \( y \sim y' \). Then
\[
g(x, y) \sim g(x', y) \quad \text{and} \quad g(x', y) \sim g(x', y') ,
\]
by the first hypothesis (with \( y \) fixed) and the second (with \( x' \) fixed). By transitivity, (Eq3), \( g(x, y) \sim g(x', y') \).

The rest is the proof of (a), with pairs of classes in place of classes. Take as graph the set of all \( (([x], [y]), [g(x, y)]) \). Each pair of classes is \( ([x], [y]) \) for some \( x, y \in X \), so every input has an output. If \( ([x], [y]) = ([x'], [y']) \), then \( [x] = [x'] \) and \( [y] = [y'] \), since equal pairs have equal entries; so \( x \sim x' \) and \( y \sim y' \). By the paragraph above, \( g(x, y) \sim g(x', y') \), so the two outputs are the same class. Hence the graph defines a function \( G \), and \( G \) is unique, as in (a).

*Uses:* @fd2:def-equivalence-relation (transitivity, (Eq3)); @fd2:def-cartesian-product; @fd2:def-quotient-set; @fd2:def-ordered-pair (equal pairs have equal entries); @fd2:thm-classes-partition (b); @fd2:prp-function-equality.

::: {.second-reading title="The graph of G, checked as in (a)"}
Now let \( G_G \) be the set of \( (P, E) \in \bigl((X/{\sim}) \times (X/{\sim})\bigr) \times (X/{\sim}) \) such that \( P = ([x], [y]) \) and \( E = [g(x, y)] \) for some \( x, y \in X \), a set by specification. (Fn1): an element of \( (X/{\sim}) \times (X/{\sim}) \) is a pair \( (C, D) \) of classes (@fd2:def-cartesian-product), and \( C = [x] \), \( D = [y] \) for some \( x, y \in X \) (@fd2:def-quotient-set); then \( ((C, D), [g(x, y)]) \in G_G \). (Fn2): suppose \( (P, E) \) and \( (P, E') \) lie in \( G_G \), with \( P = ([x], [y]) \), \( E = [g(x, y)] \), and \( P = ([x'], [y']) \), \( E' = [g(x', y')] \). From \( ([x], [y]) = ([x'], [y']) \) the characteristic property of pairs (@fd2:def-ordered-pair) gives \( [x] = [x'] \) and \( [y] = [y'] \), so \( x \sim x' \) and \( y \sim y' \) by @fd2:thm-classes-partition (b). By the first paragraph, \( g(x, y) \sim g(x', y') \), so \( E = E' \) by @fd2:thm-classes-partition (b). So \( G_G \), with codomain \( X/{\sim} \), defines a function \( G \) with \( G([x], [y]) = [g(x, y)] \). Uniqueness is as in (a), by @fd2:prp-function-equality.
:::

*(c)* \( (\Leftarrow) \) If \( x \in S \), then \( [x] \in \bar S \) by the definition of \( \bar S \). \( (\Rightarrow) \) If \( [x] \in \bar S \), then \( [x] = [x'] \) for some \( x' \in S \). By @fd2:thm-classes-partition (b), \( x \sim x' \), so \( x' \sim x \) by symmetry, (Eq2). The hypothesis, applied to \( x' \sim x \) and \( x' \in S \), gives \( x \in S \).

This proves the theorem.
:::

The functions \( F \) and \( G \) are said to be **induced** by \( f \) and \( g \). In practice we write the conclusion of (a) as "the rule \( [x] \mapsto [f(x)] \) is well defined", and of (b) as "the operation \( [x] \ast [y] \coloneqq [g(x, y)] \) is well defined". The work is always the check of the hypotheses.

::: {.remark}
**Each hypothesis has a job.** Without the hypothesis of (c) the conclusion fails. On \( \nN \times \nN \) with the relation \( \sim \) of @def-integers-as-classes, let \( S \coloneqq \{ (a, b) : 0 < a \} \). Then \( (1, 1) \in S \), so \( [(1, 1)] \in \bar S \); and \( [(0, 0)] = [(1, 1)] \), so \( [(0, 0)] \in \bar S \), while \( (0, 0) \notin S \). Membership in \( \bar S \) does not tell us whether a particular representative lies in \( S \). The hypotheses of (a) and (b) are needed in the same way, and the examples below show them failing.
:::

## Sum, product and negative of integers

To guess the formulas, borrow the school picture once more. If \( (a, b) \) records "\( a - b \)" and \( (c, d) \) records "\( c - d \)", then school algebra gives
\[
\begin{aligned}
(a - b) + (c - d) &= (a + c) - (b + d) , \\
(a - b)(c - d) &= (ac + bd) - (ad + bc) , \\
-(a - b) &= b - a .
\end{aligned}
\]
These identities are only a guide. They come from the school integers, which this chapter does not assume, and we use them only to find the definition. Each right side is again a difference of two natural numbers, so it can be recorded as a pair.

::: {#def-integer-operations}
[Sum, Product and Negative of Integers]

For all \( (a, b), (c, d) \in \nN \times \nN \), let
\[
\begin{aligned}
[(a, b)] + [(c, d)] &\coloneqq [(a + c, \ b + d)] , \\
[(a, b)] \cdot [(c, d)] &\coloneqq [(ac + bd, \ ad + bc)] , \\
-[(a, b)] &\coloneqq [(b, a)] .
\end{aligned}
\]
Let \( g_+ \), \( g_\cdot \colon (\nN \times \nN) \times (\nN \times \nN) \to \nN \times \nN \) be the maps given by the pairs on the right of the first two lines. Take \( X = \nN \times \nN \) with the equivalence relation \( \sim \) of @prp-integer-pairs-equivalence. The **sum** \( + \colon \nZ \times \nZ \to \nZ \) and **product** \( \cdot \colon \nZ \times \nZ \to \nZ \) are the functions that clause (b) of @thm-well-defined-on-classes induces from \( g_+ \) and \( g_\cdot \). The **negative** \( - \colon \nZ \to \nZ \) is the function that clause (a) induces from \( (a, b) \mapsto (b, a) \). We also write \( xy \) for \( x \cdot y \).
:::

In words: to add integers, add representatives coordinatewise; to multiply, use the cross formula; to negate, swap the coordinates. All the arithmetic on the right happens in \( \nN \), where it is always possible. The definition makes sense only if the three maps on pairs satisfy the hypotheses of the lemma. Until that is checked, the three formulas are rules, not yet functions; the check is the next proposition.

Every operation on a quotient in this volume is checked in the same way, one argument at a time. It refines the method of *Sets and Functions* (@fd2:exm-method-well-definedness).

::: {#exm-method-one-argument-at-a-time}
[Method: check on representatives, one argument at a time]

**How it goes.** To show that \( [x] \ast [y] \coloneqq [g(x, y)] \) is well defined:

1. Change the first input. Fix \( y \), take \( x \sim x' \), and show \( g(x, y) \sim g(x', y) \), using the one equation that \( x \sim x' \) stands for.
2. Change the second input, keeping the new first input \( x' \). Take \( y \sim y' \), and show \( g(x', y) \sim g(x', y') \). If \( g(x, y) = g(y, x) \) always, this is step 1 with the roles exchanged.
3. Conclude by @thm-well-defined-on-classes (b).

Steps 1 and 2 together take \( g(x, y) \) to \( g(x', y') \) in two moves. A rule on single classes needs only step 1, and then clause (a).

**When to use it.** Every operation on a quotient given by a formula on representatives: the sum and product of \( \nZ \), and every later quotient built the same way.

**Common mistakes.** Checking one numerical instance instead of all representatives. Using a law of \( \nZ \) to check an operation of \( \nZ \): the computation must stay in \( \nN \). Claiming that a formula is symmetric when it is not, as for \( [(a + d, \ b + c)] \).
:::

::: {.check}
Does \( [(a, b)] \mapsto [(a + a, \ b)] \) define a function \( \nZ \to \nZ \)?
:::

::: {.solution}
No. \( (0, 0) \sim (1, 1) \), since \( 0 + 1 = 0 + 1 \), but the outputs are \( (0 + 0, 0) = (0, 0) \) and \( (1 + 1, 1) = (2, 1) \), and \( (0, 0) \not\sim (2, 1) \), since \( 0 + 1 \ne 0 + 2 \). In school terms the rule computes \( 2a - b \), which is not a function of \( a - b \).
:::

::: {#prp-integer-operations-well-defined}
[The Operations on Integers Are Well Defined]

The maps \( g_+ \) and \( g_\cdot \) of @def-integer-operations satisfy the hypotheses of @thm-well-defined-on-classes (b), and the map \( (a, b) \mapsto (b, a) \) satisfies those of @thm-well-defined-on-classes (a), with \( \sim \) on both sides. Hence the sum, product and negative of @def-integer-operations are well-defined functions.
:::

::: {.idea}
[Scratch work]

The sum takes one line; the product is the real check. Change the first argument, as in step 1 of the method:

| We know | We want |
|---|---|
| \( (a, b) \sim (a', b') \), and \( (c, d) \) is fixed | \( g_\cdot((a, b), (c, d)) \sim g_\cdot((a', b'), (c, d)) \) |
| \( a + b' = b + a' \) | \( (ac + bd) + (a'd + b'c) = (ad + bc) + (a'c + b'd) \) |
| The known equation has no \( c \) or \( d \), but every term we want has one. | Multiply \( a + b' = b + a' \) by \( c \), and its mirror form \( b + a' = a + b' \) by \( d \). |
| \( ac + b'c = bc + a'c \) and \( bd + a'd = ad + b'd \) | Add the two and regroup: this is what we want. |

Both formulas are unchanged when the two input pairs are exchanged, so step 2 comes free.

*Before reading on: which hypothesis of @thm-well-defined-on-classes (b) does this table check?*
:::

::: {.proof}
Let \( (a, b), (a', b'), (c, d) \in \nN \times \nN \) with \( (a, b) \sim (a', b') \), that is,
\[
a + b' = b + a' .
\]{#eq-integer-rep-change}
All rearrangements below use @thm-omega-arithmetic-laws: commutativity and associativity of \( + \), commutativity of \( \cdot \), and distributivity.

*Sum, first argument.* We need \( (a + c, b + d) \sim (a' + c, b' + d) \), that is, \( (a + c) + (b' + d) = (b + d) + (a' + c) \). The left side is \( (a + b') + (c + d) \), which by @eq-integer-rep-change equals \( (b + a') + (c + d) \), and that is the right side rearranged.

*Product, first argument.* We need
\[
(ac + bd, \ ad + bc) \sim (a'c + b'd, \ a'd + b'c) ,
\]
that is, the cross-sum equation
\[
(ac + bd) + (a'd + b'c) = (ad + bc) + (a'c + b'd) .
\]{#eq-integer-product-target}
Multiply both sides of @eq-integer-rep-change by \( c \) and use distributivity: \( ac + b'c = bc + a'c \). Write @eq-integer-rep-change with its sides exchanged, \( b + a' = a + b' \), and multiply by \( d \): \( bd + a'd = ad + b'd \). Adding these two equations,
\[
(ac + b'c) + (bd + a'd) = (bc + a'c) + (ad + b'd) .
\]
The left side rearranges to the left side of @eq-integer-product-target, and the right side to its right side. This proves @eq-integer-product-target.

*Second arguments.* By commutativity in \( \nN \), \( g_+((a, b), (c, d)) = (a + c, b + d) = (c + a, d + b) = g_+((c, d), (a, b)) \), and likewise
\[
g_\cdot((a, b), (c, d)) = (ac + bd, \ ad + bc) = (ca + db, \ cb + da) = g_\cdot((c, d), (a, b)) .
\]
So if \( (c, d) \sim (c', d') \), then, by the first-argument case applied with the roles of the two pairs exchanged,
\[
g((a, b), (c, d)) = g((c, d), (a, b)) \sim g((c', d'), (a, b)) = g((a, b), (c', d'))
\]
for \( g = g_+ \) and \( g = g_\cdot \). This is the second hypothesis of @thm-well-defined-on-classes (b).

*Negative.* The pair \( (b, a) \) is related to \( (b', a') \) when \( b + a' = a + b' \), and that is @eq-integer-rep-change with its sides exchanged. This is the hypothesis of @thm-well-defined-on-classes (a).

By clauses (b) and (a) of @thm-well-defined-on-classes, the three rules define functions \( \nZ \times \nZ \to \nZ \), \( \nZ \times \nZ \to \nZ \) and \( \nZ \to \nZ \), as claimed.
:::

The table checks the first hypothesis of @thm-well-defined-on-classes (b), \( g(x, y) \sim g(x', y) \), for the product. Symmetry gives the second, and the first paragraph of that proof joins the two by transitivity of \( \sim \). You could change both pairs at once, but then both hypotheses enter one computation. Changing one argument at a time uses one hypothesis per step.
````

## 試寫後的檢查（手工）

- Label：6 個全在，拼法未變。原文 `@ref` 的目標全部保留：(a) 的 `@fd2:def-set-builder`、`@fd2:def-quotient-set`、`@fd2:prp-function-equality`，(b) 的 `@fd2:def-cartesian-product`、`@fd2:def-ordered-pair`，都移到了 `*Uses:*` 行，還在 proof 區塊內，所以 `check_forward_deps.py` 和依賴圖照讀得到。
- 沒有新增引用目標：`@fd2:def-equivalence-relation` 在原文以「(Eq3) of @fd2:def-equivalence-relation」出現，現在移到 Uses 行。沒有新增前向引用。
- 新增的數學：開頭兩個具體例子 (0, 2) ∼ (1, 3)（同 `exm-ill-defined-first-coordinate` (a)）和加法的一行計算（同命題證明的「Sum, first argument」）。它們不加 label、不被引用，所以不必加 sidecar 或 ledger；若作者要正式採用，第一個數值可沿用 `verify/ch02/exm-ill-defined-first-coordinate.py`。
- 句長：主線最長句約 34 字（定義後的 "In words" 第一句，與原文相同）；每句最多一個行內 `@ref`，例外是原文的命題敘述（逐字保留，含兩個 `@thm-well-defined-on-classes`，指同一個結果）。
- 未做：`check_structure.py`、建置、重新審稿。原檔沒有改動，所以這些都要等作者核准、正式改寫時再跑。
