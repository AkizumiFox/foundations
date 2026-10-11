# Polynomials as Coefficient Sequences

At school a polynomial is an expression such as \( 3x^2 - x + 2 \), and \( x \) is a number that has not been chosen yet. This chapter replaces that picture by a definition that works over every commutative ring of *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 2 (@fd3:def-commutative-ring-and-field): over \( \nQ \), over the fields \( \nF_p \) of Chapter 2, and over rings such as \( \nZ/6\nZ \), where a product of two non-zero elements can be zero. This section makes the one decision the whole chapter rests on: a polynomial **is** its list of coefficients. It then collects the finite sums, powers and multiples that the next sections compute with.

Throughout, \( R \) is a commutative ring, with \( a - b \coloneqq a + (-b) \).

## What goes wrong with "an expression in x"

Take the field \( \nF_2 = \{0, 1\} \) of @def-field-fp, in which \( 1 + 1 = 0 \). Read \( x^2 + x \) the school way, as a rule: replace \( x \) by an element \( c \) and compute \( cc + c \). The tables of @exm-finite-fields give
\[
0 \cdot 0 + 0 = 0 , \qquad 1 \cdot 1 + 1 = 1 + 1 = 0 .
\]
So the rule \( c \mapsto cc + c \) and the rule \( c \mapsto 0 \) give the same output at both elements of \( \nF_2 \). As functions \( \nF_2 \to \nF_2 \) they are equal, by @fd2:prp-function-equality: same domain, same codomain, same values.

If a polynomial were the function it defines, then \( x^2 + x \) would be the zero polynomial over \( \nF_2 \). So would \( x^3 + x \) and \( x^4 + x^2 \), which also give \( 0 \) at \( 0 \) and \( 1 + 1 = 0 \) at \( 1 \). None of them would have a highest power of \( x \), and the rule "the degree of a product is the sum of the degrees", which we want over every field, would fail for \( x \cdot (x + 1) = x^2 + x \): degrees \( 1 \) and \( 1 \), product "zero". Over \( \nQ \) the problem never shows (Section 5.4 proves that over an infinite field a non-zero polynomial never gives the zero function), which is why school algebra can afford the picture. Over a finite ring with \( 1 \ne 0 \) it cannot.

So we decide the other way. Two polynomials are the same when their coefficients are the same, and the letter \( x \) is not a number at all.

*A polynomial is its list of coefficients; the letter \( x \) only marks the positions.*

## Polynomials over a commutative ring

A list of coefficients that goes on forever is a sequence, that is, a function on \( \nN \). We keep only the sequences that stop being non-zero.

::: {#def-polynomial}
[Polynomial]

Let \( R \) be a commutative ring. A **polynomial over \( R \)** (in the indeterminate \( x \)) is a function \( p \colon \nN \to R \), written \( p = (p_0, p_1, p_2, \dots) \), such that **only finitely many** \( p_k \) are non-zero: **there exists** \( N \in \nN \) with \( p_k = 0 \) **for every** \( k > N \). Such an \( N \) is called **admissible** for \( p \). The element \( p_k \) is the **coefficient of \( x^k \)** in \( p \).

For \( a \in R \) and \( n \in \nN \), the **monomial** \( a \, x^n \) is the polynomial with \( a \) in position \( n \) and \( 0 \) in every other position. We set \( x \coloneqq 1 \, x^1 \), and for \( a \in R \) the **constant** \( a \) is the monomial \( a \, x^0 \). The **zero polynomial** is \( 0 \coloneqq (0, 0, 0, \dots) \). The set of all polynomials over \( R \) is written \( R[x] \).
:::

In words: the first clause says that a polynomial is an infinite list of elements of \( R \), indexed from \( 0 \); the second says that from some position on, every entry is \( 0 \). The quantifiers are in the order "there is one \( N \) that works for every later \( k \)": a sequence with infinitely many non-zero entries, however sparse, is excluded. A monomial has at most one non-zero entry, so \( n \) is admissible for it, and it is a polynomial. The symbol \( x \) is the particular sequence \( (0, 1, 0, 0, \dots) \): an element of \( R[x] \), never an element of \( R \), and never a variable that takes values.

**Equality.** Two polynomials \( p, q \in R[x] \) are functions with the same domain \( \nN \) and the same codomain \( R \). By @fd2:prp-function-equality,
\[
p = q \quad \Longleftrightarrow \quad p_k = q_k \ \text{ for every } k \in \nN .
\]
To prove an identity between polynomials we therefore compute the \( k \)-th coefficient of both sides, for an arbitrary \( k \). We call this move **compare coefficients**. It is *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 2's "reduce to the level below" once more: a statement about polynomials becomes a statement about elements of \( R \), one position at a time.

**The display.** If \( N \) is admissible for \( p \), we write
\[
p = \sum_{k=0}^{N} p_k x^k = p_0 + p_1 x + p_2 x^2 + \dots + p_N x^N .
\]
For now this is **notation only**. No addition of polynomials has been defined yet, so the plus signs are not an operation: the display names the sequence by listing its entries, each with a marker \( x^k \) for its position. We drop terms whose coefficient is \( 0 \), write \( a x \) for \( a x^1 \), \( a \) for \( a x^0 \), \( x^k \) for \( 1 x^k \), and \( - a x^k \) for \( (-a) x^k \). So \( 3x^2 - x + 2 \) over \( \nQ \) names the sequence with \( p_0 = 2 \), \( p_1 = -1 \), \( p_2 = 3 \) and \( p_k = 0 \) for \( k \ge 3 \). Section 4.2 defines the sum of two polynomials and proves that the display is then an honest sum of monomials.

There is one thing to check about the display. The admissible \( N \) is not unique: if \( N \) is admissible, so is every \( M \ge N \), since \( k > M \) implies \( k > N \). Passing from \( N \) to \( M \) only adds the terms \( 0 x^k \) for \( N < k \le M \), which the convention drops. So every admissible \( N \) names the same sequence, and the display is well defined.

**Why "only finitely many".** Two later uses need it. In Section 4.4 we put an element \( c \in R \) in place of \( x \) and form \( \sum_k p_k c^k \); in a ring only finite sums are defined, and finiteness is what makes the sum finite. In Section 4.3 every non-zero polynomial gets a degree, the highest position holding a non-zero coefficient; without finiteness there may be no highest position.

**The degenerate cases.** The zero polynomial has every \( N \) admissible, including \( N = 0 \), and it is the monomial \( 0 \, x^n \) for every \( n \). It is the one polynomial with no non-zero coefficient at all, and Section 4.3 will need a convention for its degree. At the other extreme, let \( R \) be the zero ring \( \{0\} \) of the examples after @fd3:def-commutative-ring-and-field, where \( 1 = 0 \). There is exactly one function \( \nN \to \{0\} \), so \( R[x] \) has exactly one element, the zero polynomial, and \( x = 1 \, x^1 = 0 \, x^1 = 0 \). This is why some results below assume \( 1 \ne 0 \) in \( R \).

::: {#exm-elements-of-rx}
[Reading off coefficient sequences]

Write the coefficient sequence of each polynomial, and check it against @def-polynomial. In a ring \( \nZ/n\nZ \), a natural number \( m \) written as an element stands for \( m \cdot [1] = [m] \) (@fd3:thm-integers-mod-n-ring (d)), just as @def-field-fp does for \( \nF_p \).

::: {.enumerate options="label=(\alph*)"}
1. \( 3x^2 - x + 2 \in \nQ[x] \).
2. \( x^2 + x \in \nF_2[x] \).
3. \( [3]x + [4] \in (\nZ/6\nZ)[x] \).
4. The constant \( 7 \), over \( \nZ \), over \( \nZ/5\nZ \) and over \( \nF_2 \).
5. \( 0 \in R[x] \), for any \( R \).
:::
:::

::: {.solution}
(a) \( (2, -1, 3, 0, 0, \dots) \). The entries lie in \( \nQ \), and \( N = 2 \) is admissible, so it is a polynomial over \( \nQ \).

(b) \( (0, 1, 1, 0, 0, \dots) \), with entries in \( \nF_2 \) and \( N = 2 \) admissible. It is **not** the zero sequence, since its entry in position \( 1 \) is \( 1 \ne 0 \). So \( x^2 + x \ne 0 \) in \( \nF_2[x] \), although the rule \( c \mapsto cc + c \) is the zero function on \( \nF_2 \), as computed above.

(c) \( ([4], [3], [0], [0], \dots) \): the constant term comes first. The entries lie in \( \nZ/6\nZ \) (@fd3:def-integers-mod-n-ring) and \( N = 1 \) is admissible.

(d) Over \( \nZ \): \( (7, 0, 0, \dots) \). Over \( \nZ/5\nZ \): \( ([7], [0], [0], \dots) \), and \( [7] = [2] \) because \( 7 - 2 = 5 \) is a multiple of \( 5 \); so this is the constant \( [2] \). Over \( \nF_2 \): \( (1, 0, 0, \dots) \), because \( 7 = 1 \) in \( \nF_2 \) (\( 7 - 1 = 6 = 3 \cdot 2 \)). The same symbol \( 7 \) names three different polynomials, one in each ring, and in each ring \( N = 0 \) is admissible.

(e) \( (0, 0, 0, \dots) \), with every \( N \) admissible: the degenerate case.
:::

Now a non-example, by a minimal change. Start from \( 1 + x + x^2 \in \nQ[x] \), the sequence \( (1, 1, 1, 0, 0, \dots) \), and change every later \( 0 \) to \( 1 \). The result \( (1, 1, 1, 1, \dots) \), informally "\( 1 + x + x^2 + \cdots \)", is still a function \( \nN \to \nQ \). The one clause that fails is **only finitely many**: for every \( N \), the entry in position \( N + 1 \) is \( 1 \ne 0 \), so no \( N \) is admissible. It is a *formal power series*, met again in the exercises of Section 4.2, but not a polynomial. An expression such as \( x^{-1} + 1 \) fails for a more basic reason: it would need an entry in position \( -1 \), and a polynomial is a function on \( \nN \).

\( \nR \) and \( \nC \) are commutative rings too (for \( \nR \), *Number Systems: From \( \nN \) to \( \nR \)*, Chapter 5; for \( \nC \), Chapter 1), so \( \nR[x] \) and \( \nC[x] \) are defined, and they are the main examples of the linear-algebra companion. No proof in this chapter needs them; our examples come from \( \nZ \), \( \nQ \), \( \nZ/n\nZ \) and \( \nF_p \), the rings this series has built.

**Where \( R \) matters.** Nothing in @def-polynomial mentions inverses, an order, or size. It makes sense word for word over \( \nZ/6\nZ \), where \( [2][3] = [0] \) (@fd3:exm-integers-mod-six), and over the zero ring. The price is that school rules about polynomials cannot be assumed: each one that survives is proved, here or (division with remainder, counting roots) in Chapter 5, and each result says what it needs from \( R \) (nothing at all, no zero divisors, a unit leading coefficient, finiteness with \( 1 \ne 0 \), or, for the derivative, the characteristic of a field).

::: {.warning}
**\( p_2 \) is a coefficient; \( p(2) \) will be a value.** Section 4.4 writes \( p(c) \) for the result of putting \( c \in R \) in place of \( x \). For \( p = x^2 + 1 \in \nZ[x] \), the coefficient \( p_2 \) is \( 1 \), while the value at \( 2 \) will be \( 2 \cdot 2 + 1 = 5 \). Both are integers, so a reader who writes \( p(k) \) for "the \( k \)-th coefficient" gets \( 1 = 5 \). This book never writes \( p(k) \) for a coefficient: the coefficient of \( x^k \) is \( p_k \), always with a subscript.
:::

::: {.check}
Is \( 6x^2 \) equal to the zero polynomial in \( (\nZ/6\nZ)[x] \)? In \( \nZ[x] \)?
:::

::: {.solution}
In \( (\nZ/6\nZ)[x] \), yes: \( 6x^2 \) is the monomial \( [6] \, x^2 \), and \( [6] = [0] \), so every entry is \( [0] \) and the two sequences agree in every position. In \( \nZ[x] \), no: the entry in position \( 2 \) is \( 6 \ne 0 \), while the zero polynomial has \( 0 \) there. Same display, two rings, two answers.
:::

## Sums, powers and multiples

The next section defines the product of two polynomials by a formula whose \( k \)-th coefficient is a finite sum \( \sum_{i=0}^{k} p_i q_{k-i} \) of products in \( R \). Later sections raise elements of \( R \), and polynomials, to powers, and use multiples \( k \cdot a \). This subsection collects what we use about all three. Most of it is already proved: finite sums and multiples in a commutative ring are Chapter 2's (@lem-ring-finite-sums, @lem-integer-multiples), and the recursions follow the patterns that *Sets, Relations, and Cardinality*, Section 2.3 set up for real numbers (@fd2:def-sum-product, @fd2:def-power). The patterns are reused; no fact about \( \nR \) is.

One point deserves care before we start. The sums of polynomials in Section 4.2 must be formed **before** we know that \( R[x] \) is a commutative ring, because they are used to prove it. So part (a) below asks for an addition and a left-neutral element \( 0 \), and nothing more.

::: {#lem-finite-sums-and-powers}
[Finite Sums, Powers and Multiples]

Let \( R \) be a commutative ring.

::: {.enumerate options="label=(\alph*)"}
1. *(Sums.)* Let \( T \) be a set with a function \( + \colon T \times T \to T \) and an element \( 0 \in T \) with \( 0 + u = u \) for every \( u \in T \). For a sequence \( (u_i)_{i \in \nN} \) in \( T \) there is exactly one way to define \( \sum_{i=0}^{k} u_i \in T \), for \( k \in \nN \), such that
\[
\sum_{i=0}^{0} u_i = u_0 , \qquad \sum_{i=0}^{k+1} u_i = \sum_{i=0}^{k} u_i + u_{k+1} ,
\]
starting from the empty sum \( 0 \). The sum \( \sum_{i=0}^{k} u_i \) depends only on \( u_0, \dots, u_k \); so a finite list \( u_0, \dots, u_k \) has a sum, computed from any extension of the list to a sequence. Likewise, a finite list \( s_1, \dots, s_r \) in \( R \) has a **product** \( \prod_{j=1}^{r} s_j \), with \( \prod_{j=1}^{0} s_j = 1 \) and \( \prod_{j=1}^{r+1} s_j = \bigl( \prod_{j=1}^{r} s_j \bigr) s_{r+1} \).
2. *(Rules for sums in \( R \).)* For \( k \in \nN \), \( c \in R \) and elements \( u_i, v_i \in R \):

   (Σ1) \( \sum_{i=0}^{k} (u_i + v_i) = \sum_{i=0}^{k} u_i + \sum_{i=0}^{k} v_i \);

   (Σ2) \( c \sum_{i=0}^{k} u_i = \sum_{i=0}^{k} c \, u_i \);

   (Σ3) for \( j \in \nN \): if \( u_i = 0 \) for every \( i \le k \) with \( i \ne j \), then \( \sum_{i=0}^{k} u_i = u_j \) when \( j \le k \), and \( \sum_{i=0}^{k} u_i = 0 \) when \( j > k \);

   (Σ4) \( -\sum_{i=0}^{k} u_i = \sum_{i=0}^{k} (-u_i) \).
3. *(Powers.)* For \( s \in R \) and \( n \in \nN \), \( s^0 \coloneqq 1 \) and \( s^{n+1} \coloneqq s^n s \) define \( s^n \) for every \( n \), and for all \( s, t \in R \) and \( m, n \in \nN \),
\[
s^{m+n} = s^m s^n , \qquad (s^m)^n = s^{mn} , \qquad (st)^n = s^n t^n .
\]
4. *(Multiples.)* For all \( a, b \in R \) and \( m, n \in \nZ \),
\[
\begin{aligned}
(m + n) \cdot a &= m \cdot a + n \cdot a , & m \cdot (a + b) &= m \cdot a + m \cdot b , \\
(m \cdot a) b &= m \cdot (ab) , & (m \cdot 1) a &= m \cdot a , \\
(mn) \cdot a &= m \cdot (n \cdot a) .
\end{aligned}
\]
:::
:::

In words: (a) says that a finite list in a set with an addition has a sum, built one term at a time, and that terms beyond the list do not matter; it needs no law of addition beyond \( 0 + u = u \). (b) says that a finite sum of ring elements can be split into two sums, multiplied through by a constant, collapsed to its one non-zero term, or negated term by term. (c) is the three laws of exponents in a commutative ring. (d) is the arithmetic of the multiples \( m \cdot a \) of *Number Systems: From \( \nN \) to \( \nR \)*, Section 2.3 ("Multiples"), extended to \( m \in \nZ \) in Chapter 2: a dot with an integer on its left is always a multiple, and the product of two ring elements is written by juxtaposition.

Parts (b) and (d) are cited from Chapter 2: (Σ1)–(Σ4) are @lem-ring-finite-sums (a), (b), (d), (e) (for (Σ3), apply @lem-ring-finite-sums (d) to the sequence that agrees with \( u_0, \dots, u_k \) and is \( 0 \) beyond \( k \); by the finite-lists clause of part (a) above it has the same sum), and the five rules of part (d) above are @lem-integer-multiples (c), (d). Parts (a) and (c) are the recursions of *Sets, Relations, and Cardinality*, Section 2.3, read in \( T \) and in \( R \); each is built by @fd2:thm-recursion, and each of its laws is one short induction. Chapter 1 proves the same three power laws for every commutative ring (@prp-power-laws-commutative-ring); we only compare with it, and prove (c) again from the template, so that this chapter's main line rests on Chapter 2 and not on Chapter 1.

::: {.second-reading title="Proofs of (a) and (c)"}
::: {.idea}
Each statement comes from @fd2:thm-recursion, and each law is one induction on one index, following the clauses of the recursion: the base case uses the starting value, and the step peels off the last term or factor. Only the laws of \( R \) named at each step are used.
:::

::: {.proof}
*(a)* Apply @fd2:thm-recursion (read on \( \nN = \omega \) through @fd3:cor-omega-identification (b)) with \( X = T \), starting value \( 0 \) and step \( (j, y) \mapsto y + u_j \), a function \( \nN \times T \to T \) because \( + \) maps \( T \times T \) into \( T \). It gives exactly one sequence \( (S_j)_{j \in \nN} \) in \( T \) with \( S_0 = 0 \) and \( S_{j+1} = S_j + u_j \). Set \( \sum_{i=0}^{k} u_i \coloneqq S_{k+1} \). Then \( \sum_{i=0}^{0} u_i = 0 + u_0 = u_0 \) by the hypothesis on \( 0 \), and \( \sum_{i=0}^{k+1} u_i = S_{k+1} + u_{k+1} = \sum_{i=0}^{k} u_i + u_{k+1} \). Any assignment obeying the two displayed equations agrees with this one at every \( k \), by @fd1:ax-induction on \( k \).

For the dependence on \( u_0, \dots, u_k \), let \( (v_i) \) be a second sequence with \( v_i = u_i \) for \( i \le k \), and let \( (S'_j) \) be its sequence of partial sums. We prove by @fd1:ax-induction on \( j \) the statement "if \( j \le k + 1 \), then \( S_j = S'_j \)". For \( j = 0 \) both are \( 0 \). If \( j + 1 \le k + 1 \), then \( j \le k + 1 \) and \( j \le k \), so \( S_j = S'_j \) by the hypothesis and \( u_j = v_j \); hence \( S_{j+1} = S_j + u_j = S'_j + v_j = S'_{j+1} \). At \( j = k + 1 \) this gives \( \sum_{i=0}^{k} u_i = \sum_{i=0}^{k} v_i \). The argument used only that \( + \) is a function on \( T \). The product of a list is @fd2:thm-recursion with \( X = R \), starting value \( 1 \) and step \( (j, y) \mapsto y \, s_{j+1} \) (with \( s_j \coloneqq 1 \), say, for \( j > r \)), the pattern of the product in @fd2:def-sum-product; its dependence on \( s_1, \dots, s_r \) only is the same induction.

*(c)* The powers are @fd2:thm-recursion with \( X = R \), starting value \( 1 \) and step \( (n, y) \mapsto y s \), the pattern of @fd2:def-power. For the first law fix \( m \) and induct on \( n \) (@fd1:ax-induction). For \( n = 0 \): \( s^{m+0} = s^m = s^m \cdot 1 = s^m s^0 \), by (F7). If \( s^{m+n} = s^m s^n \), then
\[
s^{m+(n+1)} = s^{(m+n)+1} = s^{m+n} s = (s^m s^n) s = s^m (s^n s) = s^m s^{n+1} ,
\]
using \( m + (n + 1) = (m + n) + 1 \) (@fd3:thm-omega-arithmetic-laws (c)), the recursion, the hypothesis and (F5). For the second law fix \( m \): \( (s^m)^0 = 1 = s^0 = s^{m \cdot 0} \) (@fd3:def-omega-arithmetic (b)), and if \( (s^m)^n = s^{mn} \), then \( (s^m)^{n+1} = (s^m)^n s^m = s^{mn} s^m = s^{mn + m} = s^{m(n+1)} \), by the first law and \( m(n + 1) = mn + m \) (@fd3:thm-omega-arithmetic-laws (d), (e)). For the third: \( (st)^0 = 1 = 1 \cdot 1 = s^0 t^0 \), by (F7), and if \( (st)^n = s^n t^n \), then \( (st)^{n+1} = (st)^n (st) = (s^n t^n)(st) = (s^n s)(t^n t) = s^{n+1} t^{n+1} \), regrouping by (F5) and (F6). This proves (a) and (c).
:::
:::

We will use (a) twice over: for sums of ring elements, as in the product formula of Section 4.2, and for sums in \( R[x] \) of finitely many monomials, which Section 4.2 forms with its coefficientwise addition before any ring law of \( R[x] \) is known. In both cases \( 0 + u = u \) holds, in \( R \) by (F1) and (F3), and in \( R[x] \) position by position.

## Exercises

### A. Check your understanding

::: {#exr-polynomials-as-sequences-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the coefficient sequences of \( x^3 - 2x \in \nZ[x] \) and of \( [2]x^2 + [4]x \in (\nZ/4\nZ)[x] \). Is the second one a monomial?
2. Is "\( 1 + x + x^2 + \cdots \)", the sequence \( (1, 1, 1, \dots) \) of rationals, a polynomial over \( \nQ \)? Name the clause of @def-polynomial that decides it.
3. True or false: two polynomials \( p, q \) over \( \nF_2 \) whose rules \( c \mapsto \sum_{k=0}^{N} p_k c^k \) and \( c \mapsto \sum_{k=0}^{N} q_k c^k \), for an \( N \) admissible for both, agree at \( 0 \) and at \( 1 \) are equal. Justify your answer.
4. Which \( N \) are admissible for \( 3x^2 - x + 2 \in \nQ[x] \)?
:::
:::

::: {.solution}
(a) \( x^3 - 2x \) is \( (0, -2, 0, 1, 0, 0, \dots) \): the constant term is \( 0 \), the coefficient of \( x \) is \( -2 \), and that of \( x^3 \) is \( 1 \). The second is \( ([0], [4], [2], [0], \dots) \), and \( [4] = [0] \) in \( \nZ/4\nZ \), since \( 4 - 0 = 4 \). So it is \( ([0], [0], [2], [0], \dots) \), the monomial \( [2] x^2 \).

(b) No. The clause **only finitely many** fails: for every \( N \in \nN \) the entry in position \( N + 1 \) is \( 1 \ne 0 \), so no \( N \) is admissible.

(c) False. The polynomials \( x^2 + x \) and \( 0 \) over \( \nF_2 \) give the rules \( c \mapsto cc + c \) and \( c \mapsto 0 \), which agree at \( 0 \) and at \( 1 \) (the computation at the start of the section). But \( x^2 + x = (0, 1, 1, 0, \dots) \) differs from \( 0 \) in position \( 1 \), so the polynomials are not equal.

(d) Every \( N \ge 2 \). The coefficient of \( x^2 \) is \( 3 \ne 0 \), so \( N = 0 \) and \( N = 1 \) fail (position \( 2 > N \) holds a non-zero entry); and every \( N \ge 2 \) works, since all positions \( k \ge 3 \) hold \( 0 \).
:::

### B. Practice

::: {#exr-polynomials-as-sequences-b1}
[B1: Polynomials of bounded length as tuples]

Let \( N \in \nN \) and \( P_N \coloneqq \{ p \in R[x] : p_k = 0 \text{ for every } k > N \} \). Prove that
\[
\Theta \colon P_N \to R^{N+1}, \qquad p \mapsto (p_0, p_1, \dots, p_N) ,
\]
is a bijection (@fd2:def-bijective), where \( R^{N+1} \) is the set of \( (N + 1) \)-tuples of elements of \( R \), indexed here from \( 0 \) (@fd2:def-cartesian-product; for \( N = 0 \), where the book has no \( 1 \)-tuples, we read \( R^1 \) as \( R \), with \( (a_0) \) standing for \( a_0 \), and \( \Theta \) as \( p \mapsto p_0 \)). Hence list the elements of \( P_2 \) for \( R = \nF_2 \).
:::

::: {.solution}
*Injective.* Let \( p, q \in P_N \) with \( \Theta(p) = \Theta(q) \). Then \( p_k = q_k \) for \( k \le N \), and \( p_k = 0 = q_k \) for \( k > N \) by the definition of \( P_N \). So \( p_k = q_k \) for every \( k \), and \( p = q \) by @fd2:prp-function-equality.

*Surjective.* Let \( (a_0, \dots, a_N) \in R^{N+1} \). Define \( p \colon \nN \to R \) by \( p_k \coloneqq a_k \) for \( k \le N \) and \( p_k \coloneqq 0 \) for \( k > N \): extend by zeros. Then \( N \) is admissible for \( p \), so \( p \in R[x] \) and \( p \in P_N \), and \( \Theta(p) = (a_0, \dots, a_N) \).

So \( \Theta \) is a bijection; its inverse is "extend by zeros". For \( R = \nF_2 \) and \( N = 2 \), each \( a_i \) is \( 0 \) or \( 1 \), and the eight triples \( (a_0, a_1, a_2) \) give the eight polynomials
\[
0, \quad 1, \quad x, \quad x + 1, \quad x^2, \quad x^2 + 1, \quad x^2 + x, \quad x^2 + x + 1 .
\]
Section 4.4 returns to this list and asks which functions \( \nF_2 \to \nF_2 \) they define.
:::

::: {#exr-polynomials-as-sequences-b2}
[B2: Determine which]

Each formula below defines a sequence \( \nN \to \nZ/4\nZ \). Determine which of them are polynomials over \( \nZ/4\nZ \). Justify your answer, and for each polynomial give the least admissible \( N \) and the polynomial in the notation of the display.

::: {.enumerate options="label=(\alph*)"}
1. \( p_k \coloneqq [2^k] \).
2. \( p_k \coloneqq [k^2] \).
3. \( p_k \coloneqq [k(k - 1)(k - 2)(k - 3)] \).
4. \( p_k \coloneqq [2k] \).
:::
:::

::: {.solution}
By @fd3:thm-integers-mod-n-ring (b), \( [0], [1], [2], [3] \) are four different classes; in particular \( [1] \ne [0] \) and \( [2] \ne [0] \).

(a) A polynomial. The first entries are \( [1], [2], [4], [8], \dots \), and for \( k \ge 2 \), \( 2^k = 4 \cdot 2^{k-2} \) (@lem-finite-sums-and-powers (c)), so \( [2^k] = [0] \). The least admissible \( N \) is \( 1 \): \( N = 1 \) works, and \( N = 0 \) does not, since \( p_1 = [2] \ne [0] \). The polynomial is \( 1 + [2]x \).

(b) Not a polynomial. For odd \( k = 2j + 1 \), \( k^2 = 4(j^2 + j) + 1 \), so \( p_k = [1] \ne [0] \). Given any \( N \), the odd number \( k = 2N + 1 > N \) has \( p_k \ne [0] \), so no \( N \) is admissible.

(c) A polynomial: the zero polynomial. Let \( k \in \nN \). By @fd3:thm-integers-division-remainder (a), \( k = 4q + r \) with \( 0 \le r \le 3 \), so \( k - r = 4q \) is one of the four factors \( k, k - 1, k - 2, k - 3 \). Hence the product is a multiple of \( 4 \), and \( p_k = [0] \) for every \( k \) (for \( k \le 3 \) the multiple is \( 0 \), since then \( q = 0 \)). Every \( N \) is admissible; the least is \( 0 \), and the display is \( 0 \).

(d) Not a polynomial. For odd \( k = 2j + 1 \), \( 2k = 4j + 2 \), so \( p_k = [2] \ne [0] \), and as in (b) no \( N \) is admissible.

The sequences in (b) and (d) have infinitely many non-zero entries even though their values repeat; (c) shows that a formula in \( k \) can describe the zero polynomial.
:::

### C. Going deeper

::: {#exr-polynomials-as-sequences-c1}
[C1: Finitely many, in the sense of finite sets]

For a sequence \( p \colon \nN \to R \), let \( S \coloneqq \{ k \in \nN : p_k \ne 0 \} \), the set of positions that hold a non-zero entry. Prove that some \( N \in \nN \) is admissible for \( p \) if and only if \( S \) is finite (@fd2:def-finite). So "only finitely many \( p_k \) are non-zero" in @def-polynomial means exactly what it says.
:::

::: {.solution}
\( (\Rightarrow) \) Let \( N \) be admissible. If \( k \in S \), then \( p_k \ne 0 \), so \( k \le N \); hence \( S \subseteq \{0, \dots, N\} \). The set \( \{0, \dots, N\} \) has \( N + 1 \) elements (the third example after @fd2:def-finite), so its subset \( S \) is finite by @fd2:prp-subset-finite.

\( (\Leftarrow) \) We prove by @fd1:ax-induction on \( n \in \nN \): *every subset \( A \subseteq \nN \) with \( n \) elements has an upper bound \( b \in \nN \)*, that is, \( a \le b \) for every \( a \in A \). For \( n = 0 \), \( A = \emptyset \) (the first example after @fd2:def-finite), and \( b = 0 \) works vacuously. Suppose the statement holds for \( n \), and let \( \varphi \colon \{1, \dots, n + 1\} \to A \) be a bijection. Put \( z \coloneqq \varphi(n + 1) \) and \( A' \coloneqq A \setminus \{z\} \). The restriction of \( \varphi \) to \( \{1, \dots, n\} \) maps into \( A' \) (if \( \varphi(j) = z \) then \( j = n + 1 \), by injectivity), is injective, and is onto \( A' \) (an element of \( A' \) is \( \varphi(j) \) with \( j \ne n + 1 \), so \( j \le n \)). So \( A' \) has \( n \) elements and an upper bound \( b' \). By trichotomy (@fd3:thm-omega-order (a)), the larger \( b \) of \( b' \) and \( z \) is defined, and it bounds every element of \( A = A' \cup \{z\} \).

Now let \( S \) be finite, with an upper bound \( N \). If \( k > N \), then \( k \notin S \), that is, \( p_k = 0 \). So \( N \) is admissible.

The proof of \( (\Leftarrow) \) never needed a greatest element of \( S \), only an upper bound. The greatest element exists when \( S \) is non-empty and finite (an upper bound in \( \nN \subseteq \nZ \) gives one by @fd3:prp-integer-least-element), and Section 4.3 calls it the degree.

**Marking scheme.** (10 points)
- 3: \( (\Rightarrow) \) shows \( S \subseteq \{0, \dots, N\} \) and concludes that \( S \) is finite, citing that \( \{0, \dots, N\} \) is finite and that a subset of a finite set is finite (@fd2:prp-subset-finite).
- 2: \( (\Leftarrow) \) sets up an induction on the number of elements of a finite \( A \subseteq \nN \), with the claim that \( A \) has an upper bound, and handles \( A = \emptyset \).
- 2: in the step, removes one element \( z \) and shows that the rest \( A' \) has \( n \) elements (by restricting the bijection, or by @fd2:cor-remove-point).
- 1: takes the larger of \( b' \) and \( z \), by trichotomy, as a bound for \( A = A' \cup \{z\} \).
- 2: concludes that an upper bound \( N \) of \( S \) is admissible: \( k > N \) implies \( k \notin S \), so \( p_k = 0 \).

Fatal errors (0 for the step): using a greatest element of \( S \) without justification; overlooking \( S = \emptyset \) in \( (\Leftarrow) \).
:::

<!-- dependency ledger
def-polynomial (claim): (opening) F_p from Chapter 2; Z/6Z has [2][3] = [0] | def-field-fp (cited); fd3:exm-integers-mod-six (cited)
def-polynomial (claim): (hook) 0*0 + 0 = 0 and 1*1 + 1 = 0 in F_2; also x^3 + x and x^4 + x^2 vanish at 0 and 1 | exm-finite-fields (cited, tables of F_2); verify/ch04/def-polynomial.py
def-polynomial (claim): (hook) the two rules are equal functions | fd2:prp-function-equality (cited)
def-polynomial (claim): (hook) over Q a non-zero polynomial is not the zero function | F4.5 (forward prose pointer, Section 5.4; thm-polynomial-identity-from-values (b)); motivation only, nothing depends on it
def-polynomial (claim): (hook) over a finite ring with 1 != 0 the function picture fails | prp-polynomial-function-map (d), Section 4.4 (within the chapter); motivation only, nothing depends on it
def-polynomial (claim): (hook) deg(pq) = deg p + deg q wanted over every field; x(x + 1) = x^2 + x | motivation only; the product is computed in Section 4.2 (exm-polynomial-product method), degree in Section 4.3; nothing depends on it
def-polynomial (claim): equality of polynomials is equality of coefficients | fd2:prp-function-equality (cited)
def-polynomial (claim): "reduce to the level below" is Number Systems Chapter 2's move | fd3 F3.2 §03 paragraph before thm-integers-commutative-ring (named move, by position)
def-polynomial (claim): if N is admissible so is every M >= N | order on N: k > M >= N gives k > N (fd3:thm-omega-order (a), transitivity), used silently
def-polynomial (claim): Section 4.2 proves the display is an honest sum; Section 4.4 evaluates; Section 4.3 degree; Section 4.2 exercises on formal power series | ch04 blueprint (within the chapter: prp-polynomial-sum-of-monomials, def-polynomial-evaluation, def-degree, exr-polynomial-ring-c2); nothing here depends on them
def-polynomial (claim): the zero ring {0} with 1 = 0; exactly one function N -> {0} | fd3 examples after def-commutative-ring-and-field (cited by position); fd2:def-function (one graph N x {0}), used silently
def-polynomial (claim): R and C are commutative rings; R[x], C[x] are the companion's main examples | fd3 F3.10 (thm-reals-field) and Chapter 1 (thm-complex-numbers-field), prose only, not cited; nothing depends on it
exm-elements-of-rx (claim): a natural number m in Z/nZ stands for m*[1] = [m] | fd3:thm-integers-mod-n-ring (d) (cited); def-field-fp (cited)
exm-elements-of-rx (solution): [7] = [2] in Z/5Z (7 - 2 = 5); 7 = 1 in F_2 (7 - 1 = 6 = 3*2) | def-field-fp, fd3:def-integers-mod-n-ring (definition of the classes); verify/ch04/exm-elements-of-rx.py
def-polynomial (claim): (warning) value of x^2 + 1 at 2 is 5 | arithmetic in Z; evaluation is defined in Section 4.4 (prose pointer); verify/ch04/def-polynomial.py
def-polynomial (claim): (check) [6] = [0] in Z/6Z; 6 != 0 in Z | fd3:thm-quotient-ring-by-ideal (d) with 6 in 6Z, used silently; fd3:thm-integers-commutative-ring (1 != 0 and 6 = 6*1 > 0), used silently
lem-finite-sums-and-powers (proof): induction on k, j, n | fd1:ax-induction read on omega through fd3:cor-omega-identification (b)
lem-finite-sums-and-powers (proof): m + (n + 1) = (m + n) + 1; m(n + 1) = mn + m | fd3:thm-omega-arithmetic-laws (c), (d), (e) (cited)
lem-finite-sums-and-powers (proof): m*0 = 0 | fd3:def-omega-arithmetic (b) (cited)
lem-finite-sums-and-powers (proof): j + 1 <= k + 1 gives j <= k + 1 and j <= k | j < j + 1 <= k + 1 and transitivity give j < k + 1, hence j <= k (fd3:thm-omega-order (a), (b)), used silently
lem-finite-sums-and-powers (claim): (b) and (d) cited from Chapter 2 | lem-ring-finite-sums (a), (b), (d), (e) (cited; for (Σ3) the list is extended by zeros, as part (a) allows); lem-integer-multiples (c), (d) (cited)
lem-finite-sums-and-powers (claim): Chapter 1 proves the same power laws | prp-power-laws-commutative-ring (F4.1, see edge; prose comparison, not cited in the proof of (c))
lem-finite-sums-and-powers (claim): 0 + u = u in R and in R[x] | (F1), (F3) of R; in R[x] position by position (the addition of def-polynomial-ring, Section 4.2)
exr-polynomials-as-sequences-a1 (solution): [4] = [0] in Z/4Z | definition of the classes; verify/ch04/exr-polynomials-as-sequences-a1.py
exr-polynomials-as-sequences-b1 (solution): the eight triples over F_2 | listing; verify/ch04/exr-polynomials-as-sequences-b1.py
exr-polynomials-as-sequences-b2 (solution): 2^k = 4 * 2^(k - 2) for k >= 2; k^2 = 4(j^2 + j) + 1; 2k = 4j + 2 | lem-finite-sums-and-powers (c) in Z; ring algebra in Z; verify/ch04/exr-polynomials-as-sequences-b2.py
exr-polynomials-as-sequences-b2 (solution): one of k, k - 1, k - 2, k - 3 equals 4q | fd3:thm-integers-division-remainder (a) (cited); r <= 3 from 0 <= r < 4 by discreteness (fd3:thm-integers-ordered-ring (c)), used silently
exr-polynomials-as-sequences-c1 (solution): {0, ..., N} has N + 1 elements; empty set has 0 elements | fd2 examples after def-finite (cited by position); fd2:prp-subset-finite (cited)
exr-polynomials-as-sequences-c1 (solution): restriction of a bijection; max of two naturals | inline (marking scheme also accepts fd2:cor-remove-point, cited); fd3:thm-omega-order (a) (cited)
exr-polynomials-as-sequences-b1 (claim): R^(N+1) as (N+1)-tuples indexed from 0; R^1 read as R | fd2:def-cartesian-product (cited, n >= 2); N = 0 by stated convention
exr-polynomials-as-sequences-c1 (solution): greatest element; Section 4.3's degree | fd3:prp-integer-least-element (cited) with fd3:prp-naturals-embed-integers, used silently; prose pointer within the chapter
-->
