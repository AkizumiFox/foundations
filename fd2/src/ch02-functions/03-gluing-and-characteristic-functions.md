# Gluing and Characteristic Functions

Section 2.1 made a function a graph with a codomain, and Section 2.2 asked what a function does to its inputs and to its codomain. This section builds new functions out of old ones by the three simplest constructions: cutting a function down to a smaller domain, enlarging its domain, and assembling one function from pieces defined on parts of the domain. The last is behind every definition "by cases". The section ends with the functions that take only the values \( 0 \) and \( 1 \), with which an equation between sets becomes a computation with numbers, and with the theorem that the subsets of \( X \) and the 0–1 functions on \( X \) correspond one to one.

## A function in two pieces

School mathematics defines many functions in pieces. The sign function is
\[
\sgn x = \begin{cases} 1 & \text{if } x > 0, \\ 0 & \text{if } x = 0, \\ -1 & \text{if } x < 0 . \end{cases}
\]
Each real number falls under exactly one case, and in each case the value exists and is unique, so \( \sgn \) is a function \( \nR \to \nR \). That sentence carries the whole definition. It is worth asking what it really needed.

Here is a familiar definition by cases:
\[
\abs{x} = \begin{cases} x & \text{if } x \ge 0, \\ -x & \text{if } x \le 0 . \end{cases}
\]
This time a point falls under **both** cases: \( 0 \ge 0 \) and \( 0 \le 0 \). So the sentence about \( \sgn \) does not apply. Is \( \abs{\cdot} \) still a function? Most readers would say yes at once, because both formulas give \( 0 \) at \( 0 \). Now try
\[
r(x) = \begin{cases} x & \text{if } x \ge 0, \\ x + 1 & \text{if } x \le 0 . \end{cases}
\]
At \( 0 \) the first line gives \( 0 \) and the second gives \( 1 \). The "rule" offers two values at one input, and by (Fn2) of @def-function it is not a function.

So whether "one formula on this piece, another on that piece" defines a function depends on two things: whether the pieces leave any point out, and what the formulas do where the pieces meet. *Before reading on: write down the condition on two formulas, on two pieces, that makes the definition a function.* The gluing theorem below answers this, for any number of pieces.

## Restriction and extension

Section 2.1 cut a function down: the restriction of \( f \colon X \to Y \) to a subset \( A \subseteq X \) keeps the pairs of \( f \) whose input lies in \( A \). The reverse question is just as natural. A function is known on part of a set, say \( g(x) = 1/x \) on \( (0, 1] \); can it be **extended** to a larger set, and in how many ways?

*A restriction forgets part of the domain; an extension fills in the part that was missing.*

::: {#def-restriction-extension}
[Restriction, Extension, Inclusion]

Let \( X \) and \( Y \) be sets and \( A \subseteq X \).

::: {.enumerate options="label=(\alph*)"}
1. For \( f \colon X \to Y \), the **restriction** of \( f \) to \( A \) is the function \( f|_A \colon A \to Y \), \( f|_A(a) \coloneqq f(a) \), as in Section 2.1.
2. For \( g \colon A \to Y \), an **extension** of \( g \) to \( X \) is **a** function \( f \colon X \to Y \) with \( f|_A = g \).
3. The **inclusion map** of \( A \) into \( X \) is \( \iota_A \colon A \to X \), \( \iota_A(a) \coloneqq a \).
:::
:::

In words: the restriction keeps the codomain and forgets the inputs outside \( A \). An extension is any function on the larger set that agrees with \( g \) at every point of \( A \); by @prp-function-equality, \( f|_A = g \) says exactly that \( f(a) = g(a) \) for every \( a \in A \), since both functions have domain \( A \) and codomain \( Y \). The inclusion map is the map of @exm-structure-maps (a), now given the name \( \iota_A \): the identity of \( A \) with its codomain enlarged to \( X \); it is not \( \id_A \) unless \( A = X \), because the codomains differ.

The article in (b) is "**a**", not "the", and the naive expectation that an extension is determined by \( g \) fails at once. The function \( g \colon (0, 1] \to \nR \), \( g(x) = 1/x \), has an extension to \( [0, 1] \) for every choice of a value at \( 0 \): sending \( 0 \) to \( 0 \) and sending \( 0 \) to \( 5 \) give two different extensions, since they differ at \( 0 \). The formula \( 1/x \) suggests no value at all there. Nor need an extension keep a property that \( g \) has. Let \( a \ne b \), and let \( g \colon \{1, 2\} \to \{a, b\} \) send \( 1 \mapsto a \) and \( 2 \mapsto b \), a bijection. An extension \( f \) to \( \{1, 2, 3\} \) with codomain \( \{a, b\} \) has \( f(3) = a = f(1) \) or \( f(3) = b = f(2) \), so it is not injective. So the bijection \( g \) has extensions, but no injective one.

Restriction, by contrast, is predictable. The next proposition lists what it does.

::: {#prp-restriction-properties}
[Restrictions]

Let \( f \colon X \to Y \) be a function and \( B \subseteq A \subseteq X \).

::: {.enumerate options="label=(\alph*)"}
1. \( f|_A = f \circ \iota_A \).
2. \( (f|_A)|_B = f|_B \).
3. For every function \( g \colon Y \to Z \), \( (g \circ f)|_A = g \circ (f|_A) \).
4. If \( f \) is injective, then so is \( f|_A \).
:::
:::

::: {.idea}
Parts (a)–(c) are equations between functions, so we compare domains, codomains and values. Part (d) only unwinds @def-injective, using \( f|_A(a) = f(a) \).
:::

::: {.proof}
For (a)–(c) we use @prp-function-equality: in each part both sides have the same domain and codomain, and we compare values.

(a) Both sides are functions \( A \to Y \) (@def-composition). For \( a \in A \), \( (f \circ \iota_A)(a) = f(\iota_A(a)) = f(a) = f|_A(a) \).

(b) Both sides are functions \( B \to Y \). For \( b \in B \), \( (f|_A)|_B(b) = f|_A(b) = f(b) = f|_B(b) \), where the middle step uses \( b \in A \).

(c) Both sides are functions \( A \to Z \). For \( a \in A \), \( (g \circ f)|_A(a) = g(f(a)) = g(f|_A(a)) = (g \circ (f|_A))(a) \).

(d) Let \( a, a' \in A \) with \( f|_A(a) = f|_A(a') \). Then \( f(a) = f(a') \), so \( a = a' \) because \( f \) is injective (@def-injective).
:::

Part (d) has no partner for surjectivity, and the next check asks why.

::: {.check}
Is a restriction of a surjection always surjective?
:::

::: {.solution}
No. The function \( f \colon \nR \to [0, \infty) \), \( f(x) = x^2 \), is surjective (every \( t \ge 0 \) is \( (\sqrt{t})^2 \)). Its restriction \( f|_{[1, 2]} \colon [1, 2] \to [0, \infty) \) takes only values \( x^2 \ge 1 \), so \( 0 \) is not a value. The restriction keeps the codomain while the domain shrinks, so it can lose surjectivity. It can also gain injectivity: \( f|_{[0, \infty)} \) is injective, by @exm-square-three-ways (b), although \( f \) is not, since \( f(-1) = 1 = f(1) \).
:::

## Gluing

Restriction takes a function apart: it hands us the pieces \( f|_{A_i} \) on the parts \( A_i \) of the domain. Gluing is the reverse. We are given functions on the parts and want one function on the whole set. The hook named the two ways this can go wrong: a point may lie in no part, and a point may lie in two parts whose formulas disagree there. Only the second failure appeared there; the first is easy to picture.

::: {#thm-gluing}
[Gluing Functions]

Let \( (A_i)_{i \in I} \) be a family of subsets of a set \( X \) with \( \bigcup_{i \in I} A_i = X \), and let \( (f_i)_{i \in I} \) be a family of functions \( f_i \colon A_i \to Y \). Suppose the \( f_i \) **agree on overlaps**:
\[
f_i(x) = f_j(x) \quad \text{for all } i, j \in I \text{ and every } x \in A_i \cap A_j .
\]
Then there is **exactly one** function \( f \colon X \to Y \) with \( f|_{A_i} = f_i \) for every \( i \in I \).
:::

::: {.idea}
[Scratch work]

A function is a graph satisfying (Fn1) and (Fn2), together with a codomain (@def-function). We must produce a graph, and the only graphs in sight are the graphs \( G_i \) of the \( f_i \). The obvious candidate is their union. The plan, as givens and goal:

| Givens | Goal |
|---|---|
| graphs \( G_i \subseteq A_i \times Y \), each with (Fn1) and (Fn2) on \( A_i \); \( \bigcup_i A_i = X \); agreement on overlaps | a function \( f \colon X \to Y \) whose restriction to each \( A_i \) is \( f_i \), and only one |
| \( G \coloneqq \bigcup_{i} G_i \subseteq X \times Y \) | (Fn1) and (Fn2) for \( G \) on \( X \) |
| \( x \in X \), so \( x \in A_i \) for some \( i \) (the cover) | (Fn1): \( (x, f_i(x)) \in G_i \subseteq G \) |
| \( (x, y) \in G_i \), \( (x, y') \in G_j \); so \( y = f_i(x) \), \( y' = f_j(x) \) and \( x \in A_i \cap A_j \) | (Fn2): \( y = y' \); this is the gap, and agreement on overlaps closes it |

In the existence part each hypothesis has one job: the cover gives (Fn1), agreement gives (Fn2). Uniqueness is easier: two functions with the right restrictions both take the value \( f_i(x) \) at a point \( x \in A_i \).
:::

::: {.proof}
For each \( i \in I \), let \( G_i \subseteq A_i \times Y \) be the graph of \( f_i \), and let \( G \coloneqq \bigcup_{i \in I} G_i \) (@def-family-union-intersection). Since \( A_i \subseteq X \), each \( G_i \subseteq X \times Y \), so \( G \subseteq X \times Y \).

*(Fn1).* Let \( x \in X \). Since \( \bigcup_{i \in I} A_i = X \), there is \( i \in I \) with \( x \in A_i \). Then \( (x, f_i(x)) \in G_i \subseteq G \).

*(Fn2).* Let \( (x, y) \in G \) and \( (x, y') \in G \). Then \( (x, y) \in G_i \) and \( (x, y') \in G_j \) for some \( i, j \in I \). Since \( G_i \subseteq A_i \times Y \) and \( G_j \subseteq A_j \times Y \), we have \( x \in A_i \cap A_j \), and by \( (\ast\ast) \) of Section 2.1, \( y = f_i(x) \) and \( y' = f_j(x) \). Agreement on overlaps gives \( y = y' \).

So \( f \coloneqq (G, Y) \) is a function \( X \to Y \). Let \( i \in I \). Both \( f|_{A_i} \) and \( f_i \) are functions \( A_i \to Y \), and for \( x \in A_i \) we have \( (x, f_i(x)) \in G \), so \( f(x) = f_i(x) \) by \( (\ast\ast) \); that is, \( f|_{A_i}(x) = f_i(x) \). By @prp-function-equality, \( f|_{A_i} = f_i \).

*Uniqueness.* Let \( g \colon X \to Y \) also satisfy \( g|_{A_i} = f_i \) for every \( i \in I \). Let \( x \in X \), and choose \( i \) with \( x \in A_i \). Then \( g(x) = g|_{A_i}(x) = f_i(x) = f|_{A_i}(x) = f(x) \). By @prp-function-equality, \( g = f \). This proves the theorem.
:::

In the existence part, the proof used the cover only for (Fn1) and agreement only for (Fn2). Each hypothesis is needed. If a point \( x \) lies in no \( A_i \), the union graph has no pair with first coordinate \( x \), and (Fn1) fails; the theorem fails too: for \( X = Y = \{0, 1\} \), \( A_1 = \{0\} \) and \( f_1(0) = 0 \), both ways of choosing the value at \( 1 \) give a function \( f \) with \( f|_{A_1} = f_1 \), so "exactly one" fails. The rule \( r \) of the hook shows two pieces that cover \( \nR \) and disagree at \( 0 \), where (Fn2) fails.

The theorem is used so often that its use deserves a template. Step (4) is the step that Example (c) below turns on.

::: {#exm-method-gluing}
[Method: define a function by gluing]

**Template.** (1) Name the pieces and check that they cover the domain. (2) For each two pieces, find the overlap and check that the formulas agree on it; disjoint pieces need nothing. (3) Conclude by @thm-gluing. (4) Prove further properties piece by piece **and across pieces**: for injectivity, compare a value from one piece with a value from another.

**When to use it.** Definitions by cases, piecewise formulas, a default value off a subset, a function given by different formulas on a subset and its complement.

**The usual failure.** Checking the cover and forgetting the overlaps (a boundary point lies in two pieces); checking injectivity inside each piece only.
:::

::: {#exm-piecewise-as-gluing}
[Piecewise definitions are gluings]

Decide whether each definition glues to a function \( \nR \to \nR \).

::: {.enumerate options="label=(\alph*)"}
1. \( x \) on \( [0, \infty) \) and \( -x \) on \( (-\infty, 0] \).
2. \( x \) on \( [0, \infty) \) and \( x + 1 \) on \( (-\infty, 0] \).
3. \( x \) on \( [0, \infty) \) and \( x + 1 \) on \( (-\infty, 0) \). If it glues, is the result injective?
:::
:::

::: {.solution}
(a) Step (1): the pieces cover \( \nR \), since every real number is \( \ge 0 \) or \( \le 0 \). Step (2): the overlap is \( \{0\} \), where the formulas give \( 0 \) and \( -0 = 0 \). They agree, so by @thm-gluing there is exactly one function with these restrictions: the absolute value \( \abs{\cdot} \).

(b) The pieces cover \( \nR \) and overlap in \( \{0\} \), where the values are \( 0 \) and \( 1 \). Agreement fails, so the hypothesis of @thm-gluing fails; and no function can have both restrictions, since its value at \( 0 \) would be \( 0 \) and \( 1 \). This is the rule \( r \) of the hook, which is not a function.

(c) A minimal change to (b): the second piece loses the point \( 0 \). Now the pieces are disjoint and still cover \( \nR \), so step (2) has nothing to check, and they glue to a function \( k \colon \nR \to \nR \). Inside each piece \( k \) is injective (\( x = x' \) and \( x + 1 = x' + 1 \) each force \( x = x' \)). Across the pieces, step (4) finds a collision: \( k(\tfrac12) = \tfrac12 \) and \( k(-\tfrac12) = -\tfrac12 + 1 = \tfrac12 \). So \( k \) is not injective.
:::

Part (c) found its collision across the pieces. Step (4) of the method box, for injectivity, is a proposition:

::: {#prp-injective-across-pieces}
[Injectivity Across Pieces]

Let \( f \colon X \to Y \) and \( X = A \cup B \). Then \( f \) is injective if and only if \( f|_A \) and \( f|_B \) are injective and \( f(a) \ne f(b) \) for all \( a \in A \setminus B \) and \( b \in B \setminus A \).
:::

::: {.idea}
Two different points either share a piece, where the restriction decides, or lie one in each piece outside the overlap, where the last condition decides. This is step (4) of @exm-method-gluing, and we prove injectivity in the contrapositive form given after @def-injective (justified by @fd1:prp-contrapositive-converse).
:::

::: {.proof}
\( (\Rightarrow) \) The restrictions are injective by @prp-restriction-properties (d). For \( a \in A \setminus B \) and \( b \in B \setminus A \) we have \( a \ne b \), since \( b \in B \) and \( a \notin B \); so \( f(a) \ne f(b) \) because \( f \) is injective.

\( (\Leftarrow) \) Let \( x, x' \in X \) with \( x \ne x' \). If both lie in \( A \), then \( f(x) = f|_A(x) \ne f|_A(x') = f(x') \), since \( f|_A \) is injective; likewise if both lie in \( B \). Otherwise they do not both lie in \( A \), so one of them is outside \( A \); renaming the two points if necessary, \( x \notin A \). Since \( X = A \cup B \), \( x \in B \setminus A \). Then \( x' \notin B \), for otherwise both points lie in \( B \), a case already done; so \( x' \in A \setminus B \), and \( f(x') \ne f(x) \) by hypothesis. In every case \( f(x) \ne f(x') \), so \( f \) is injective.
:::

The condition across the pieces mentions only points outside the overlap. A point of \( A \cap B \) lies in both pieces, so a collision involving it is already caught by one of the two restrictions.

**Default values.** Let \( A \subseteq X \), \( g \colon A \to Y \) and \( y_0 \in Y \). "Take \( g \) on \( A \) and the value \( y_0 \) on \( X \setminus A \)" glues \( g \) with the constant function \( X \setminus A \to Y \) with value \( y_0 \): the pieces \( A \) and \( X \setminus A \) are disjoint and cover \( X \). The indicator functions of the next subsection are default-value definitions too.

::: {.warning}
A boundary point usually lies in two pieces. "\( x^2 \) on \( (-\infty, 1] \), \( 3x \) on \( [1, \infty) \)" covers \( \nR \), and each formula is a function on its piece, but at \( 1 \) the values are \( 1 \) and \( 3 \), so nothing glues. Check every overlap, not just the cover.
:::

::: {.check}
Glue \( x^2 \) on \( (-\infty, 1] \) and \( 2x - 1 \) on \( [1, \infty) \). Does it glue? Is the result injective?
:::

::: {.solution}
The pieces cover \( \nR \) and overlap in \( \{1\} \), where \( 1^2 = 1 = 2 \cdot 1 - 1 \); so the definitions glue to a function \( f \colon \nR \to \nR \). It is not injective, and the failure is inside the first piece: \( f(-1) = 1 = f(1) \).
:::

## Indicator functions

A subset \( A \) of \( X \) can be described by a function that answers, for each \( x \in X \), the question "is \( x \) in \( A \)?" with \( 1 \) for yes and \( 0 \) for no. Section 2.1 met this function in @exm-first-functions (d). It now gets its own label, because it turns statements about sets into arithmetic.

::: {#def-indicator}
[Indicator Function]

Let \( X \) be a set and \( A \subseteq X \). The **indicator function** of \( A \) is \( \ind_A \colon X \to \{0, 1\} \),
\[
\ind_A(x) \coloneqq \begin{cases} 1 & \text{if } x \in A, \\ 0 & \text{if } x \in X \setminus A . \end{cases}
\]
:::

It is a default-value definition: the constant \( 1 \) on \( A \) glued with the constant \( 0 \) on \( X \setminus A \), over a disjoint cover of \( X \). The function depends on \( X \) as well as on \( A \), since \( X \) is its domain; throughout this subsection one set \( X \) is fixed and every set named is a subset of it. Two small cases: \( \ind_X \) is the constant function \( 1 \), and \( \ind_{\emptyset} \) is the constant function \( 0 \).

The last subsection of this section proves that \( A \mapsto \ind_A \) is a bijection \( \powerset{X} \to \{0, 1\}^X \), and \( f \mapsto \{ x \in X : f(x) = 1 \} \) undoes it on both sides (@thm-power-set-two-power). Only one consequence is needed here, and it can be read off directly: \( A \) is recovered from its indicator as the set of points where the value is \( 1 \). So
\[
\ind_A = \ind_B \quad \text{implies} \quad A = B .
\]
This is what lets a computation with indicators prove an equation between sets: show that the two sides have the same indicator, and they are equal.

To compute, we need to know what the set operations do to indicators. Besides the operations of @def-set-operations we use one more. The **symmetric difference** of \( A \) and \( B \) is
\[
A \triangle B \coloneqq (A \setminus B) \cup (B \setminus A) ,
\]
the set of points that lie in exactly one of \( A \) and \( B \).

::: {#prp-indicator-arithmetic}
[Set Operations as Arithmetic of Indicators]

Let \( A, B \subseteq X \). For every \( x \in X \), write \( u \coloneqq \ind_A(x) \) and \( v \coloneqq \ind_B(x) \). Then:

::: {.enumerate options="label=(\alph*)"}
1. \( \ind_{A \cap B}(x) = uv \);
2. \( \ind_{X \setminus A}(x) = 1 - u \);
3. \( \ind_{A \cup B}(x) = u + v - uv \);
4. \( \ind_{A \triangle B}(x) = u + v - 2uv \);
5. \( A \subseteq B \) if and only if \( \ind_A(x) \le \ind_B(x) \) for **every** \( x \in X \).
:::
:::

::: {.idea}
For (a), (b) and (d), membership of \( x \) in the left-hand set is decided by which of \( x \in A \), \( x \in B \) hold: four cases, one table. Part (c) need not be tabled at all: De Morgan turns a union into a complement of an intersection, and (a), (b) compute that.
:::

::: {.proof}
Fix \( x \in X \). By @def-indicator, \( u = 1 \) if \( x \in A \) and \( u = 0 \) otherwise, and likewise for \( v \) and \( B \).

(a), (b), (d). There are four cases, and in each we read membership from @def-set-operations and the definition of \( \triangle \):

| \( x \in A \)? | \( x \in B \)? | \( u \) | \( v \) | \( x \in A \cap B \)? | \( uv \) | \( x \in X \setminus A \)? | \( 1 - u \) | \( x \in A \triangle B \)? | \( u + v - 2uv \) |
|---|---|---|---|---|---|---|---|---|---|
| yes | yes | 1 | 1 | yes | 1 | no | 0 | no | 0 |
| yes | no | 1 | 0 | no | 0 | no | 0 | yes | 1 |
| no | yes | 0 | 1 | no | 0 | yes | 1 | yes | 1 |
| no | no | 0 | 0 | no | 0 | yes | 1 | no | 0 |

In every row, the number in each formula column is \( 1 \) exactly when the membership column before it says yes, and \( 0 \) otherwise. That is (a), (b) and (d).

(c) By @thm-set-algebra (d) with \( X \) in the place of \( A \), \( X \setminus (A \cup B) = (X \setminus A) \cap (X \setminus B) \). Applying (a) to the sets \( X \setminus A \) and \( X \setminus B \), whose indicators at \( x \) are \( 1 - u \) and \( 1 - v \) by (b), gives \( \ind_{X \setminus (A \cup B)}(x) = (1 - u)(1 - v) \). Applying (b) to the set \( A \cup B \subseteq X \),
\[
\ind_{A \cup B}(x) = 1 - \ind_{X \setminus (A \cup B)}(x) = 1 - (1 - u)(1 - v) = u + v - uv .
\]

(e) \( (\Rightarrow) \) Suppose \( A \subseteq B \) and let \( x \in X \). If \( \ind_A(x) = 1 \), then \( x \in A \), so \( x \in B \) and \( \ind_B(x) = 1 \). If \( \ind_A(x) = 0 \), then \( \ind_A(x) \le \ind_B(x) \) since \( \ind_B(x) \in \{0, 1\} \). \( (\Leftarrow) \) Suppose the inequality holds at every point, and let \( x \in A \). Then \( 1 = \ind_A(x) \le \ind_B(x) \le 1 \), so \( \ind_B(x) = 1 \) and \( x \in B \). By @def-subset, \( A \subseteq B \).
:::

Part (e) says the only pattern of values that \( A \subseteq B \) forbids is \( u = 1 \), \( v = 0 \): a point of \( A \) outside \( B \).

::: {.check}
Express \( \ind_{A \setminus B}(x) \) in terms of \( u = \ind_A(x) \) and \( v = \ind_B(x) \).
:::

::: {.solution}
By @def-set-operations, \( A \setminus B = A \cap (X \setminus B) \), since both consist of the points of \( A \) not in \( B \). By (a) and (b), \( \ind_{A \setminus B}(x) = u(1 - v) = u - uv \). Check on the row \( u = 1 \), \( v = 0 \): the value is \( 1 \), and indeed such an \( x \) lies in \( A \setminus B \).
:::

**Compute with indicators.** To prove an equation \( L = R \) between sets built from subsets \( A, B, C \) of \( X \), fix \( x \in X \), write \( u, v, w \) for the values of \( \ind_A, \ind_B, \ind_C \) at \( x \), and translate each side into a polynomial in \( u, v, w \) by @prp-indicator-arithmetic. Simplify both, using \( u^2 = u \), \( v^2 = v \), \( w^2 = w \), which hold because \( 0^2 = 0 \) and \( 1^2 = 1 \). If the two polynomials agree for all values in \( \{0, 1\} \), then \( \ind_L = \ind_R \), and \( L = R \) because a set is recovered from its indicator. The method replaces a case analysis on memberships by algebra, and it pays most when the case analysis is long.

::: {#exm-symmetric-difference-associative}
[Symmetric difference is associative]

Show that \( (A \triangle B) \triangle C = A \triangle (B \triangle C) \) for all \( A, B, C \subseteq X \).
:::

::: {.solution}
Fix \( x \in X \) and let \( u, v, w \) be the values of \( \ind_A, \ind_B, \ind_C \) at \( x \). By @prp-indicator-arithmetic (d), \( \ind_{A \triangle B}(x) = u + v - 2uv \). Applying (d) again, to the sets \( A \triangle B \) and \( C \),
\[
\begin{aligned}
\ind_{(A \triangle B) \triangle C}(x) &= (u + v - 2uv) + w - 2(u + v - 2uv)w \\
&= u + v + w - 2uv - 2uw - 2vw + 4uvw .
\end{aligned}
\]
The final expression does not change when \( u, v, w \) are permuted. The right-hand side gives \( u + (v + w - 2vw) - 2u(v + w - 2vw) \), which expands to the same expression. So the two sets have the same indicator, and they are equal.
:::

The common value is \( 1 \) exactly when an odd number of \( u, v, w \) equal \( 1 \): with one of them equal to \( 1 \) it is \( 1 \), with two it is \( 2 - 2 = 0 \), with three \( 3 - 6 + 4 = 1 \). So both sides are the set of points lying in an odd number of \( A, B, C \). An element chase would split into eight cases, one for each pattern of memberships; the indicator computation did all eight at once.

::: {.check}
Let \( X = \{1, 2, 3, 4\} \), \( A = \{1, 2\} \) and \( B = \{2, 3\} \). List the values \( \ind_{A \triangle B}(1), \dots, \ind_{A \triangle B}(4) \), first from the formula \( u + v - 2uv \) and then from the definition of \( \triangle \).
:::

::: {.solution}
The values of \( \ind_A \) are \( (1, 1, 0, 0) \) and those of \( \ind_B \) are \( (0, 1, 1, 0) \). The formula gives \( 1 + 0 - 0 = 1 \), \( 1 + 1 - 2 = 0 \), \( 0 + 1 - 0 = 1 \), \( 0 \): the list \( (1, 0, 1, 0) \). From the definition, \( A \triangle B = \{1\} \cup \{3\} = \{1, 3\} \), whose indicator is the same list.
:::

## Subsets are 0–1 functions

Section 2.1 stated, for every set, that subsets and 0–1 functions match, and gave both maps: send \( f \) to \( \{ x : f(x) = 1 \} \) and \( A \) to \( \ind_A \). Here are the two round trips, which make \( 2 \) a base like any other.

::: {#thm-power-set-two-power}
[Subsets and 0–1 Functions]

For every set \( X \), the map \( A \mapsto \ind_A \) is a bijection \( \powerset{X} \to \{0, 1\}^X \), and \( f \mapsto \{ x \in X : f(x) = 1 \} \) undoes it on both sides: each round trip is the identity.
:::

::: {.proof}
For \( A \subseteq X \), \( \ind_A \in \{0, 1\}^X \) (@exm-first-functions (d)), and \( \{ x \in X : \ind_A(x) = 1 \} = A \) by the definition of \( \ind_A \). For \( f \in \{0, 1\}^X \), let \( S \coloneqq \{ x \in X : f(x) = 1 \} \). For \( x \in S \), \( \ind_S(x) = 1 = f(x) \). For \( x \in X \setminus S \), \( f(x) \ne 1 \), so \( f(x) = 0 = \ind_S(x) \). So \( \ind_S = f \) (@prp-function-equality). The first round trip makes \( A \mapsto \ind_A \) injective, since \( \ind_A = \ind_B \) gives \( A = \{ x \in X : \ind_A(x) = 1 \} = B \); the second makes it surjective. So it is a bijection (@def-bijective).
:::

::: {.remark}
[Looking ahead]

Chapter 4 counts the subsets of a finite set and, through this bijection, the 0–1 functions on it; with Cantor's theorem it also shows that \( \{0, 1\}^X \) is larger than \( X \).
:::

## Exercises

### A. Check your understanding

::: {#exr-restriction-extension-and-gluing-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Let \( f \colon \nR \to \nR \), \( f(x) = x^2 \). Is \( f|_{(-\infty, 0]} \) injective? Is \( f|_{[-1, 2]} \)?
2. Let \( a, b, c \) be distinct and let \( g \colon \{1, 2\} \to \{a, b, c\} \) send \( 1 \mapsto a \), \( 2 \mapsto b \). How many extensions of \( g \) to \( \{1, 2, 3\} \) with codomain \( \{a, b, c\} \) are there, and how many of them are injective?
3. Let \( A \subseteq X \) and \( g \colon A \to Y \). Show that \( g \) has an extension to \( X \) if and only if \( A = X \) or \( Y \ne \emptyset \).
4. For \( X = \{1, 2, 3, 4\} \), write \( \ind_{\{1, 3\}} \) as the list of its values at \( 1, 2, 3, 4 \), and name the subset of \( X \) whose indicator has the values \( (0, 1, 1, 0) \).
:::
:::

::: {.solution}
(a) Yes. Let \( x_1, x_2 \le 0 \) with \( x_1^2 = x_2^2 \). Then \( -x_1, -x_2 \ge 0 \) and \( (-x_1)^2 = x_1^2 = x_2^2 = (-x_2)^2 \), so \( -x_1 = -x_2 \) as in @exm-square-three-ways (b), and \( x_1 = x_2 \). No: \( -1 \) and \( 1 \) lie in \( [-1, 2] \), and \( f(-1) = 1 = f(1) \).

(b) Three. An extension agrees with \( g \) on \( \{1, 2\} \), so by @prp-function-equality it is determined by its value at \( 3 \); and each of \( a, b, c \) gives one, by gluing \( g \) with a constant function on \( \{3\} \) (@thm-gluing; the pieces are disjoint). Only \( 3 \mapsto c \) gives an injective extension, since its three values \( a, b, c \) are distinct; \( 3 \mapsto a \) collides with \( 1 \), and \( 3 \mapsto b \) with \( 2 \).

(c) \( (\Leftarrow) \) If \( A = X \), then \( g \) is an extension of itself, since \( g|_X = g \). If \( Y \ne \emptyset \), choose \( y_0 \in Y \) and glue \( g \) with the constant function \( X \setminus A \to Y \) with value \( y_0 \): the pieces \( A \) and \( X \setminus A \) are disjoint and cover \( X \), so @thm-gluing gives \( f \colon X \to Y \) with \( f|_A = g \). \( (\Rightarrow) \) Suppose \( A \ne X \) and \( Y = \emptyset \). Since \( A \subseteq X \) and \( A \ne X \), some \( x_0 \in X \) is not in \( A \); so \( X \) is non-empty, and by @prp-empty-function (b) there is no function \( X \to \emptyset \), let alone an extension of \( g \). By contraposition, an extension forces \( A = X \) or \( Y \ne \emptyset \).

(d) \( (1, 0, 1, 0) \); the subset \( \{2, 3\} \), the set of points where the value is \( 1 \).
:::

### B. Practice

::: {#exr-restriction-extension-and-gluing-b1}
[B1: Three pieces]

Let \( f_1(x) = -x \) on \( (-\infty, -1] \), \( f_2(x) = x^2 \) on \( [-1, 1] \) and \( f_3(x) = x \) on \( [1, \infty) \), each with codomain \( \nR \). Show that they glue to a function \( f \colon \nR \to \nR \). Find the range of \( f \) and every \( x \) with \( f(x) = \tfrac14 \), and decide whether \( f \) is injective.
:::

::: {.solution}
The three intervals cover \( \nR \). The overlaps are \( (-\infty, -1] \cap [-1, 1] = \{-1\} \), where \( f_1(-1) = 1 = f_2(-1) \); \( [-1, 1] \cap [1, \infty) = \{1\} \), where \( f_2(1) = 1 = f_3(1) \); and \( (-\infty, -1] \cap [1, \infty) = \emptyset \). So the pieces agree on overlaps and glue, by @thm-gluing.

Every \( x \in \nR \) lies in a piece, where \( f(x) = f_i(x) \); so the range of \( f \) is the union of the ranges of the \( f_i \). On \( (-\infty, -1] \), \( -x \) takes every value \( t \ge 1 \) (at \( x = -t \)) and no other; on \( [-1, 1] \), \( x^2 \) takes every value \( t \in [0, 1] \) (at \( x = \sqrt{t} \)) and no other; on \( [1, \infty) \), \( x \) takes every value \( t \ge 1 \) (at \( x = t \)) and no other. Hence the range is \( [0, \infty) \).

On the first and third pieces every value is \( \ge 1 \), so a solution of \( f(x) = \tfrac14 \) lies in \( [-1, 1] \), where it solves \( x^2 = \tfrac14 \). Hence the solutions are \( -\tfrac12 \) and \( \tfrac12 \). Two different points have the same value, so \( f \) is not injective.
:::

::: {#exr-restriction-extension-and-gluing-b5}
[B2: A bijection in two pieces]

Let \( g_1(x) = x \) on \( (-\infty, 0] \) and \( g_2(x) = x^2 \) on \( [0, \infty) \), each with codomain \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( g_1 \) and \( g_2 \) glue to a function \( f \colon \nR \to \nR \).
2. Prove that \( f \) is injective, using @prp-injective-across-pieces.
3. Prove that \( f \) is surjective.
:::
:::

::: {.solution}
(a) The pieces cover \( \nR \), since every real number is \( \le 0 \) or \( \ge 0 \). They overlap in \( \{0\} \), where \( g_1(0) = 0 = 0^2 = g_2(0) \). By @thm-gluing they glue to a function \( f \colon \nR \to \nR \).

(b) Let \( A = (-\infty, 0] \) and \( B = [0, \infty) \). Then \( f|_A = g_1 \) is injective, since \( g_1(x_1) = g_1(x_2) \) says \( x_1 = x_2 \). And \( f|_B = g_2 \) is injective: \( x_1^2 = x_2^2 \) with \( x_1, x_2 \ge 0 \) gives \( x_1 = x_2 \), as in @exm-square-three-ways (b). Across the pieces, let \( a \in A \setminus B \) and \( b \in B \setminus A \), that is \( a < 0 < b \). Then \( f(a) = a < 0 < b^2 = f(b) \), so \( f(a) \ne f(b) \). By @prp-injective-across-pieces, \( f \) is injective.

(c) Let \( y \in \nR \). We argue by cases (@exm-method-cases). If \( y < 0 \), then \( y \in A \) and \( f(y) = y \). If \( y \ge 0 \), then \( \sqrt{y} \in B \) and \( f(\sqrt{y}) = (\sqrt{y})^2 = y \). So every real number is a value of \( f \), and \( f \) is a bijection.
:::

::: {#exr-restriction-extension-and-gluing-b3}
[B3: By indicators]

Let \( A, B, C \subseteq X \). Prove by computing with indicators:

::: {.enumerate options="label=(\alph*)"}
1. \( A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C) \);
2. \( A \cap (B \triangle C) = (A \cap B) \triangle (A \cap C) \).
:::
:::

::: {.solution}
Fix \( x \in X \) and write \( u, v, w \) for the values of \( \ind_A, \ind_B, \ind_C \) at \( x \). For any \( S \subseteq X \), \( A \setminus S = A \cap (X \setminus S) \), so @prp-indicator-arithmetic (a), (b) give \( \ind_{A \setminus S}(x) = u(1 - \ind_S(x)) \).

(a) By @prp-indicator-arithmetic (c), \( \ind_{B \cup C}(x) = v + w - vw \), so the left side has indicator value \( u(1 - v - w + vw) = u(1 - v)(1 - w) \). The right side has, by @prp-indicator-arithmetic (a), \( u(1 - v) \cdot u(1 - w) = u^2 (1 - v)(1 - w) = u(1 - v)(1 - w) \), using \( u^2 = u \). The indicators agree at every \( x \), so the sets are equal.

(b) By @prp-indicator-arithmetic (a) and (d), the left side has \( u(v + w - 2vw) = uv + uw - 2uvw \). The sets \( A \cap B \) and \( A \cap C \) have indicator values \( uv \) and \( uw \), so by @prp-indicator-arithmetic (d) the right side has \( uv + uw - 2(uv)(uw) = uv + uw - 2u^2 vw = uv + uw - 2uvw \). The indicators agree, so the sets are equal.
:::

::: {#exr-restriction-extension-and-gluing-b4}
[B4: Prove or disprove]

Prove each true statement and refute each false one with a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. If \( X = A \cup B \) with \( A \cap B = \emptyset \), and \( f \colon A \to Y \), \( g \colon B \to Y \) are functions, then there is exactly one \( h \colon X \to Y \) with \( h|_A = f \) and \( h|_B = g \).
2. If \( f \colon X \to Y \), \( X = A \cup B \), and \( f|_A \) and \( f|_B \) are injective, then \( f \) is injective.
3. If \( f \colon X \to Y \) and \( f|_A \colon A \to Y \) is surjective for some \( A \subseteq X \), then \( f \) is surjective.
4. The definition \( h(x) = x \) for \( x \in \nQ \), \( h(x) = 2x \) for \( x \in \nR \setminus \nQ \) gives a bijection \( h \colon \nR \to \nR \).
5. Gluing \( x \) on \( [0, 1] \) and \( 2 - x \) on \( [1, 2] \) gives an injective function \( [0, 2] \to \nR \).
:::
:::

::: {.solution}
(a) True. The family \( A, B \) covers \( X \), and the only overlap \( A \cap B \) is empty, so agreement holds vacuously. By @thm-gluing there is exactly one such \( h \).

(b) False. Let \( f \colon \nR \to \nR \), \( f(x) = x^2 \), \( A = [0, \infty) \) and \( B = (-\infty, 0] \). Then \( X = A \cup B \), and both restrictions are injective (on each piece, \( x^2 = x'^2 \) with \( x, x' \) of the same sign gives \( x = x' \)), but \( f(1) = 1 = f(-1) \). The collision is across the pieces.

(c) True. Let \( y \in Y \). Since \( f|_A \) is surjective, \( y = f|_A(a) = f(a) \) for some \( a \in A \subseteq X \). So \( y \) is a value of \( f \).

(d) True. The pieces \( \nQ \) and \( \nR \setminus \nQ \) are disjoint and cover \( \nR \), so \( h \) is a function by @thm-gluing. *Injective.* Inside the pieces: \( x = x' \) and \( 2x = 2x' \) each give \( x = x' \). Across the pieces: if \( x \in \nQ \), \( x' \notin \nQ \) and \( h(x) = h(x') \), then \( x = 2x' \), so \( x' = x/2 \in \nQ \), a contradiction. *Surjective.* A rational \( y \) is \( h(y) \). An irrational \( y \) is \( h(y/2) \): here \( y/2 \notin \nQ \), since otherwise \( y = 2 \cdot (y/2) \in \nQ \).

(e) False. The pieces agree at the overlap \( \{1\} \) (both give \( 1 \)), so they glue to a function \( f \); but \( f(\tfrac12) = \tfrac12 = 2 - \tfrac32 = f(\tfrac32) \).
:::

### C. Going deeper

::: {#exr-restriction-extension-and-gluing-c4}
[C1: The complement map, transported]

Let \( \Phi \colon \powerset{X} \to \{0, 1\}^X \), \( \Phi(A) = \ind_A \), a bijection by @thm-power-set-two-power, and let \( c \colon \powerset{X} \to \powerset{X} \), \( c(A) = X \setminus A \).

::: {.enumerate options="label=(\alph*)"}
1. Prove \( X \setminus (A \cap B) = (X \setminus A) \cup (X \setminus B) \) for \( A, B \subseteq X \) by computing with indicators.
2. Show that \( \Phi(c(A)) = 1 - \Phi(A) \) for every \( A \subseteq X \), where \( 1 - f \in \{0, 1\}^X \) denotes the function \( x \mapsto 1 - f(x) \) (its values are \( 1 - 0 = 1 \) and \( 1 - 1 = 0 \)).
3. Use (b) to show that \( c \circ c = \id_{\powerset{X}} \) without chasing elements.
:::
:::

::: {.solution}
(a) Fix \( x \in X \) and write \( u, v \) for the values of \( \ind_A, \ind_B \) at \( x \). By @prp-indicator-arithmetic (a) and (b), the left side has indicator value \( 1 - uv \). By @prp-indicator-arithmetic (b), the sets \( X \setminus A \) and \( X \setminus B \) have indicator values \( 1 - u \) and \( 1 - v \), so by @prp-indicator-arithmetic (c) the right side has
\[
(1 - u) + (1 - v) - (1 - u)(1 - v) = 2 - u - v - (1 - u - v + uv) = 1 - uv .
\]
The two sides have the same indicator, and \( \Phi \) is injective, so they are equal.

(b) Both sides are functions \( X \to \{0, 1\} \). At \( x \in X \), \( \Phi(c(A))(x) = \ind_{X \setminus A}(x) = 1 - \ind_A(x) \) by @prp-indicator-arithmetic (b), which is the value of \( 1 - \Phi(A) \) at \( x \). By @prp-function-equality, \( \Phi(c(A)) = 1 - \Phi(A) \).

(c) Let \( A \subseteq X \). Applying (b) to \( c(A) \) and then to \( A \),
\[
\Phi(c(c(A))) = 1 - \Phi(c(A)) = 1 - (1 - \Phi(A)) = \Phi(A) ,
\]
where the last step holds at every point because \( 1 - (1 - t) = t \) for every number \( t \). Since \( \Phi \) is injective, \( c(c(A)) = A \). Both \( c \circ c \) and \( \id_{\powerset{X}} \) are functions \( \powerset{X} \to \powerset{X} \) that agree at every \( A \), so \( c \circ c = \id_{\powerset{X}} \) (@prp-function-equality). This is the identity of @exm-structure-maps (d), recovered by a computation with numbers.
:::

::: {#exr-restriction-extension-and-gluing-c5}
[C2: Infinitely many pieces]

For each \( n \in \nZ \), let \( f_n \colon [n, n + 1) \to \nR \), \( f_n(x) = x - n \).

::: {.enumerate options="label=(\alph*)"}
1. Show that the intervals \( [n, n + 1) \) cover \( \nR \) and are pairwise disjoint, so that the \( f_n \) glue to a function \( f \colon \nR \to \nR \).
2. Find the range of \( f \), show that \( f(x + 1) = f(x) \) for every \( x \in \nR \), and decide whether \( f \) is injective.
3. Do the functions \( x \mapsto x - n \) on the closed intervals \( [n, n + 1] \), \( n \in \nZ \), glue to a function \( \nR \to \nR \)?
:::
:::

::: {.solution}
(a) *Cover.* Every \( x \in \nR \) lies in \( [\floor{x}, \floor{x} + 1) \), where \( \floor{x} \) is the integer of @exm-maps-from-calculus (b). *Disjoint.* Suppose \( x \in [n, n + 1) \cap [m, m + 1) \) with integers \( n \ne m \); since the situation is symmetric in \( n \) and \( m \), we may assume \( n < m \). Then \( n + 1 \le m \), because \( n \) and \( m \) are integers, and so \( m \le x < n + 1 \le m \), which is impossible. So no two pieces overlap, step (2) of @exm-method-gluing has nothing to check, and @thm-gluing gives \( f \).

(b) The range is \( [0, 1) \). If \( x \in [n, n + 1) \), then \( 0 \le x - n < 1 \), so every value lies in \( [0, 1) \); and each \( t \in [0, 1) \) lies in the piece with \( n = 0 \), so \( f(t) = t - 0 = t \). For the shift, let \( x \in [n, n + 1) \). Then \( x + 1 \in [n + 1, n + 2) \), the piece of \( n + 1 \), so \( f(x + 1) = (x + 1) - (n + 1) = x - n = f(x) \). Hence \( f \) is not injective: \( f(0) = 0 = f(1) \).

(c) No. The point \( 1 \) lies in \( [0, 1] \cap [1, 2] \), where the first formula gives \( 1 - 0 = 1 \) and the second gives \( 1 - 1 = 0 \). The functions disagree on an overlap, and no function can restrict to both, since its value at \( 1 \) would be \( 1 \) and \( 0 \).
:::

<!-- dependency ledger
def-restriction-extension (claim): (paragraph after it) the inclusion map iota_A is the inclusion map of exm-structure-maps (a) | exm-structure-maps (F2.6 §02, cited); same rule a -> a, same domain and codomain
thm-power-set-two-power (proof): f(x) is 0 or 1, so f(x) != 1 gives f(x) = 0 | the codomain {0, 1}
def-restriction-extension (claim): (hook before it) every real is > 0, = 0 or < 0, and exactly one of these | R order (trichotomy), school fact
def-restriction-extension (claim): 1/x on (0, 1] with value 0 or 5 at 0 gives two different extensions to [0, 1] | each is a function by excluded middle on x = 0, as in exm-first-functions (d); different by prp-function-equality (cited)
def-restriction-extension (claim): an extension f of g : {1, 2} -> {a, b} to {1, 2, 3} has f(3) = a = f(1) or f(3) = b = f(2) | f(3) is in the codomain {a, b} (def-function); f(1) = g(1) = a, f(2) = g(2) = b by f|_{1,2} = g
thm-gluing (proof): the graph of a function f_i : A_i -> Y lies in A_i x Y; (x, y) in f iff y = f(x) | def-function, (**) of Section 2.1 (named in the proof)
thm-gluing (proof): A_i subset X gives A_i x Y subset X x Y | def-cartesian-product, used silently
prp-restriction-properties (claim): (quick check) f|_{[0, inf)} injective by exm-square-three-ways (b); f(-1) = 1 = f(1) | cited, arithmetic
prp-restriction-properties (claim): (quick check) x^2 >= 1 for x in [1, 2]; every t >= 0 is (sqrt t)^2 | school fact (square roots, AN1.1)
exm-piecewise-as-gluing (solution): every real is >= 0 or <= 0; -0 = 0; -1/2 + 1 = 1/2 | R order (trichotomy) and arithmetic, school fact; verify/ch02/exm-piecewise-as-gluing.py
prp-injective-across-pieces (proof): two points both lie in A or not; renaming x, x' (the claim is symmetric); x not in A and X = A cup B give x in B \ A | excluded middle (classical), as in exm-method-cases; def-set-operations
exm-method-gluing (claim): (warning after it) 1^2 = 1 != 3 = 3 * 1 | arithmetic
prp-indicator-arithmetic (proof): four-row table of memberships and values | def-set-operations, def-indicator; verify/ch02/prp-indicator-arithmetic.py
prp-indicator-arithmetic (proof): 1 - (1 - u)(1 - v) = u + v - uv; 1 <= v <= 1 gives v = 1 | R arithmetic and order, school fact
def-indicator (claim): A = {x : ind_A(x) = 1}, so ind_A = ind_B gives A = B | def-indicator and def-set-equality, read off directly; also thm-power-set-two-power (cited)
prp-indicator-arithmetic (claim): (quick check) A \ B = A cap (X \ B) | def-set-operations, unwound in the solution
exm-symmetric-difference-associative (solution): the polynomial expansions; odd-count reading | R arithmetic; verify/ch02/exm-symmetric-difference-associative.py
exm-symmetric-difference-associative (claim): u^2 = u for u in {0, 1} | arithmetic (0^2 = 0, 1^2 = 1)
exm-symmetric-difference-associative (claim): (quick check after it) values (1, 0, 1, 0) of ind_{A triangle B} on {1, 2, 3, 4} | verify/ch02/prp-indicator-arithmetic.py
exr-restriction-extension-and-gluing-a1 (solution): x1, x2 <= 0 give -x1, -x2 >= 0 and (-x)^2 = x^2; -1, 1 in [-1, 2] | R arithmetic and order, school fact; verify/ch02/exr-restriction-extension-and-gluing-a1.py
exr-restriction-extension-and-gluing-a1 (solution): an extension to {1, 2, 3} is determined by its value at 3, each of a, b, c gives one; contraposition in (c) | prp-function-equality, thm-gluing (cited); fd1 prp-contrapositive, used silently
exr-restriction-extension-and-gluing-a1 (solution): A subseteq X and A != X give x_0 in X \ A | def-set-equality, def-subset; fd1 prp-quantifier-negation, used silently
exr-restriction-extension-and-gluing-b1 (solution): the ranges of -x on (-inf, -1], x^2 on [-1, 1], x on [1, inf); x^2 = 1/4 iff x = +-1/2 | school fact (square roots, AN1.1; x^2 <= 1 on [-1, 1]); verify/ch02/exr-restriction-extension-and-gluing-b1.py
exr-restriction-extension-and-gluing-b5 (solution): every real is <= 0 or >= 0, and a < 0 < b for a in A \ B, b in B \ A; b^2 > 0 for b > 0; (sqrt y)^2 = y for y >= 0 | R order (trichotomy) and arithmetic, school fact; square roots, AN1.1; verify/ch02/exr-restriction-extension-and-gluing-b5.py
exr-restriction-extension-and-gluing-b3 (solution): polynomial identities with u^2 = u | R arithmetic; verify/ch02/exr-restriction-extension-and-gluing-b3.py
exr-restriction-extension-and-gluing-b4 (solution): x^2 = x'^2 with x, x' of the same sign gives x = x'; Q closed under multiplication and halving | R arithmetic and order, school fact; verify/ch02/exr-restriction-extension-and-gluing-b4.py
exr-restriction-extension-and-gluing-c4 (solution): (1 - u) + (1 - v) - (1 - u)(1 - v) = 1 - uv; 1 - (1 - t) = t | R arithmetic; verify/ch02/exr-restriction-extension-and-gluing-c4.py
exr-restriction-extension-and-gluing-c5 (solution): every real x lies in [floor x, floor x + 1) | school fact (floor of a real, AN1.1; F3.2 prp-rational-integer-part for Q), as in exm-maps-from-calculus (b)
exr-restriction-extension-and-gluing-c5 (solution): integers n < m give n + 1 <= m; 0 <= x - n < 1 on [n, n + 1) | Z and R order, school fact; verify/ch02/exr-restriction-extension-and-gluing-c5.py
-->
