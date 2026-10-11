# Finite Fields from Modular Arithmetic

Every field of Section 2.1 is infinite. *Number Systems: From \( \nN \) to \( \nR \)* has already met finite ones: it proved that the integers modulo a prime \( p \) form a field (@fd3:thm-integers-mod-prime-field). This section restates that result in the language of @def-field, gives these fields a name of their own, \( \nF_p \), and computes in them: inverses, linear equations, and the elimination of Section 2.1, now run modulo \( 5 \). Finite fields are not a curiosity; coding theory and computer algebra do linear algebra over them every day.

## Arithmetic modulo n, recalled

Fix an integer \( n \ge 1 \). The ring \( \nZ/n\nZ \) of @fd3:def-integers-mod-n-ring consists of the classes \( [a] \) of integers \( a \) under congruence modulo \( n \), and two classes are equal exactly when their representatives differ by a multiple of \( n \):
\[
[a] = [b] \iff n \mid a - b .
\]
This is the class test of *Number Systems* (@fd3:thm-quotient-ring-by-ideal (a), read with @fd3:def-integers-mod-n-ring). Sums and products are computed on representatives. The first example collects what is known about this arithmetic, in the language of @def-field.

::: {#exm-finite-fields}
[Arithmetic on \( \nZ/n\nZ \) and the Field \( \nF_2 \)]

Let \( n \ge 1 \), and define \( [a] + [b] \coloneqq [a + b] \) and \( [a][b] \coloneqq [ab] \) for \( a, b \in \nZ \). Show that these operations are well defined, that they satisfy every clause of @def-field except possibly (F8) and the condition \( 1 \ne 0 \) in (F7), and that \( [1] \ne [0] \) holds exactly when \( n \ge 2 \). Then write out the addition and multiplication tables for \( n = 2 \).
:::

::: {.solution}
All of this was proved in *Number Systems*, and we collect it.

*Well-definedness.* The formulas use representatives, so the answer must not depend on which representatives are chosen. For the ideal \( n\nZ \) of \( \nZ \) this is @fd3:thm-quotient-ring-by-ideal (b), and \( \nZ/n\nZ \) is defined as that quotient (@fd3:def-integers-mod-n-ring).

*The clauses.* By @fd3:thm-integers-mod-n-ring (a), \( \nZ/n\nZ \) is a commutative ring with zero \( [0] \) and one \( [1] \): clauses (F1)–(F6) and (F9) hold, and so does (F7) without the condition \( 1 \ne 0 \). The negative of \( [a] \) is \( [-a] \), since \( [a] + [-a] = [a + (-a)] = [0] \).

*The condition \( 1 \ne 0 \).* By @fd3:thm-integers-mod-n-ring (c), \( [1] \ne [0] \) if and only if \( n \ge 2 \). For \( n = 1 \) every class equals \( [0] \), and \( \nZ/1\nZ \) is the zero ring.

*Size.* By @fd3:thm-integers-mod-n-ring (b), each class is \( [r] \) for exactly one \( r \in \{0, 1, \dots, n - 1\} \), the remainder of any representative on division by \( n \). So \( \nZ/n\nZ \) has exactly \( n \) elements.

*The tables for \( n = 2 \).* Write \( 0 \) and \( 1 \) for \( [0] \) and \( [1] \). Since \( 1 + 1 = 2 \) and \( 2 - 0 = 2 \cdot 1 \), the class test gives \( [1] + [1] = [2] = [0] \); the other entries are read off directly:
\[
\begin{array}{c|cc}
{+} & 0 & 1 \\ \hline
0 & 0 & 1 \\
1 & 1 & 0
\end{array}
\qquad\qquad
\begin{array}{c|cc}
\cdot & 0 & 1 \\ \hline
0 & 0 & 0 \\
1 & 0 & 1
\end{array}
\]
Here (F8) holds as well: the only non-zero element is \( 1 \), and \( 1 \cdot 1 = 1 \). So \( \nF_2 \coloneqq \nZ/2\nZ \) is a field. In it \( 1 + 1 = 0 \), and therefore \( -1 = 1 \).
:::

The tables of \( \nF_2 \) are those of the two-element field of @fd3:exm-finite-ring-not-orderable, with \( 0 \) and \( 1 \) read as classes. The one surprise is \( 1 + 1 = 0 \): it says that \( 2 \) is even, and nothing more. It is also the field promised by the warning on order in Section 2.1, where "\( 1 + 1 \ne 0 \)" fails.

## Which moduli give fields

For \( n \ge 2 \), whether \( \nZ/n\nZ \) is a field now comes down to one clause, (F8): does every non-zero class have an inverse? An inverse of \( [a] \) is a class \( [x] \) with \( [ax] = [1] \), that is, an integer \( x \) with \( n \mid ax - 1 \), that is, integers \( x, y \) with \( ax + ny = 1 \). Such a combination is what Bézout's theorem produces. The linear-algebra volumes cite it in the following special form.

::: {#lem-bezout-integers}
[Bézout's Lemma for Integers]

Let \( a, n \in \nZ \) with \( n \ge 1 \), and suppose that the only positive integer dividing both \( a \) and \( n \) is \( 1 \). Then there are \( x, y \in \nZ \) with
\[
ax + ny = 1 .
\]
:::

::: {.proof}
Since \( n \ge 1 \), \( (a, n) \ne (0, 0) \), so \( g \coloneqq \gcd(a, n) \) is a common divisor of \( a \) and \( n \) with \( g \ge 1 \) (@fd3:def-integer-gcd and the well-definedness paragraph after it). By hypothesis, \( g = 1 \). So \( a \) and \( n \) are coprime, and @fd3:cor-coprime-iff-combination gives \( x, y \in \nZ \) with \( ax + ny = 1 \).
:::

The general statement, for any pair of integers not both zero and with \( \gcd(a, n) \) in place of \( 1 \), is @fd3:thm-integers-bezout; the Euclidean algorithm computes the \( x \) and \( y \). We keep the special case under its own name because the linear-algebra volumes cite it in this form.

::: {#thm-zp-field-iff-prime}
[\( \nZ/n\nZ \) Is a Field Exactly for Prime \( n \)]

Let \( n \ge 2 \) be an integer. Then \( \nZ/n\nZ \) is a field (@def-field) if and only if \( n \) is prime.
:::

::: {.idea}
By @exm-finite-fields, only (F8) is in question. If \( n = p \) is prime and \( [a] \ne [0] \), then \( p \nmid a \), so the only positive common divisor of \( a \) and \( p \) is \( 1 \), and @lem-bezout-integers hands over \( ax + py = 1 \), that is, \( [a][x] = [1] \). If instead \( n = rs \) with \( 1 < r, s < n \), then \( [r][s] = [n] = [0] \) with both factors non-zero, which @thm-field-basic-properties (f) forbids in a field. *Number Systems* ran this argument, with @fd3:thm-units-mod-n in the role of the lemma.
:::

::: {.proof}
By @fd3:thm-integers-mod-prime-field, \( \nZ/n\nZ \) is a field in the sense of @fd3:def-commutative-ring-and-field if and only if \( n \) is prime. By the remark after @def-field, a field in that sense is the same as a field in the sense of @def-field. This proves the theorem.
:::

So for each prime \( p \) there is a field with exactly \( p \) elements, and for each composite \( n \ge 4 \) the ring \( \nZ/n\nZ \) is not a field. The fields deserve a short name.

## The fields with p elements

::: {#def-field-fp}
[The Field \( \nF_p \)]

Let \( p \) be a prime. The field \( \nF_p \) is \( \nZ/p\nZ \), with the operations of @exm-finite-fields. It has exactly \( p \) elements (@fd3:thm-integers-mod-n-ring (b)), which we write \( 0, 1, \dots, p - 1 \), without brackets: the number \( r \in \{0, \dots, p - 1\} \) stands for the class \( [r] \). For integers \( a, b \), "\( a = b \) in \( \nF_p \)" means \( [a] = [b] \), that is, \( p \mid a - b \).
:::

So \( \nF_2 \), \( \nF_3 \), \( \nF_5 \), \( \nF_7 \), \( \nF_{11} \), … are fields, by @thm-zp-field-iff-prime, while \( \nZ/4\nZ \), \( \nZ/6\nZ \) and \( \nZ/9\nZ \) are not. To decide that a given \( p \) is prime, the remark after @fd3:lem-least-divisor-prime says it is enough to check that no \( d \ge 2 \) with \( d \cdot d \le p \) divides \( p \).

Computing in \( \nF_p \) is computing with integers and replacing the answer by its remainder on division by \( p \). The words "in \( \nF_p \)" must be said whenever an equation would be false in \( \nZ \): "\( 3 \cdot 5 = 1 \) in \( \nF_7 \)" is true, because \( 15 - 1 = 2 \cdot 7 \); "\( 3 \cdot 5 = 1 \)" alone is false. Every result of Section 2.1 now holds in \( \nF_p \). For instance, by @cor-field-squares-equal the only elements of \( \nF_p \) whose square is \( 1 \) are \( 1 \) and \( -1 = p - 1 \).

::: {.check}
Find the inverse of \( 3 \) in \( \nF_7 \).
:::

::: {.solution}
The inverse is the \( x \in \{1, \dots, 6\} \) with \( 7 \mid 3x - 1 \). Testing the candidates in turn, the products \( 3, 6, 9, 12, 15 \) leave remainders \( 3, 6, 2, 5, 1 \), and \( 3 \cdot 5 = 15 = 2 \cdot 7 + 1 \). So \( 3^{-1} = 5 \) in \( \nF_7 \), and by @thm-field-basic-properties (c) it is the only inverse.
:::

For small \( p \), trial is fast. For larger \( p \) the Euclidean algorithm of *Number Systems* finds the inverse directly, through @fd3:thm-units-mod-n: if \( ax + py = 1 \), then \( [a]^{-1} = [x] \).

::: {#exm-inverses-in-fp}
[Inverses in \( \nF_7 \) and in \( \nF_{101} \)]

(i) List the inverses of the non-zero elements of \( \nF_7 \). (ii) Find the inverse of \( 17 \) in \( \nF_{101} \).
:::

::: {.solution}
(i) In \( \nF_7 \):
\[
1 \cdot 1 = 1, \quad 2 \cdot 4 = 8 = 1, \quad 3 \cdot 5 = 15 = 1, \quad 6 \cdot 6 = 36 = 1,
\]
since \( 8 - 1 = 7 \), \( 15 - 1 = 2 \cdot 7 \) and \( 36 - 1 = 5 \cdot 7 \). So \( 1^{-1} = 1 \), \( 2^{-1} = 4 \), \( 4^{-1} = 2 \), \( 3^{-1} = 5 \), \( 5^{-1} = 3 \), \( 6^{-1} = 6 \), using (F6) for the reversed pairs. Each element of \( \nF_7^{\times} \coloneqq \nF_7 \setminus \{0\} \) appears exactly once as an inverse, as it must: the inverse of \( a^{-1} \) is \( a \) (@thm-field-basic-properties (g)), so two elements with the same inverse are equal. The elements \( 1 \) and \( 6 = -1 \) are their own inverses, and by @cor-field-squares-equal no others are.

(ii) First, \( 101 \) is prime: no \( d \) with \( 2 \le d \le 10 \) divides it (the remainders of \( 101 \) on division by \( 2, 3, \dots, 10 \) are \( 1, 2, 1, 1, 5, 3, 5, 2, 1 \)), and \( 11 \cdot 11 = 121 > 101 \). Run the Euclidean algorithm on \( (101, 17) \):
\[
101 = 5 \cdot 17 + 16, \qquad 17 = 1 \cdot 16 + 1 .
\]
Back-substitute from the last line:
\[
1 = 17 - 16 = 17 - (101 - 5 \cdot 17) = 6 \cdot 17 - 101 .
\]
So \( 17 \cdot 6 + 101 \cdot (-1) = 1 \), and @fd3:thm-units-mod-n gives \( 17^{-1} = 6 \) in \( \nF_{101} \). Check: \( 17 \cdot 6 = 102 = 101 + 1 \).
:::

Since \( \nF_p \) is a field, each result of Section 2.1 about equations holds there word for word; what changes is how the numbers are computed. The opening elimination, done over \( \nF_5 \), looks like this.

::: {#exm-elimination-f5}
[Elimination over \( \nF_5 \)]

Solve the system \( 2x + y = 3 \), \( 3x + 2y = 4 \) over \( \nF_5 \).
:::

::: {.solution}
In \( \nF_5 \) the inverses are \( 1^{-1} = 1 \), \( 2^{-1} = 3 \), \( 3^{-1} = 2 \) and \( 4^{-1} = 4 \), since \( 2 \cdot 3 = 6 = 5 + 1 \) and \( 4 \cdot 4 = 16 = 3 \cdot 5 + 1 \).

*By elimination.* Scale the first equation by \( 2^{-1} = 3 \). In \( \nF_5 \), \( 3 \cdot 2 = 1 \), \( 3 \cdot 1 = 3 \) and \( 3 \cdot 3 = 9 = 4 \), so the scaled equation reads \( x + 3y = 4 \). Taking \( 3 \) times it away from the second equation removes \( x \) and leaves
\[
(2 - 9) y = 4 - 12, \quad \text{that is,} \quad 3y = 2 \ \text{ in } \nF_5,
\]
since \( -7 = -10 + 3 \) and \( -8 = -10 + 2 \). Multiply by \( 3^{-1} = 2 \): \( y = 4 \). Then \( x = 4 - 3y = 4 - 12 = -8 = 2 \) in \( \nF_5 \).

*By the formula.* With \( a = 2 \), \( b = 1 \), \( c = 3 \), \( d = 2 \), \( e = 3 \), \( f = 4 \), the coefficient \( ad - bc = 4 - 3 = 1 \) is non-zero, so @prp-field-linear-equation (b) applies:
\[
x = \frac{3 \cdot 2 - 1 \cdot 4}{1} = 2, \qquad y = \frac{2 \cdot 4 - 3 \cdot 3}{1} = -1 = 4 \ \text{ in } \nF_5 .
\]
The two methods agree. Check: \( 2 \cdot 2 + 4 = 8 = 3 \) and \( 3 \cdot 2 + 2 \cdot 4 = 14 = 4 \) in \( \nF_5 \). By @prp-field-linear-equation (b), \( (x, y) = (2, 4) \) is the only solution.
:::

::: {.check}
Which elements \( x \in \nF_{11} \) satisfy \( x^2 = 1 \)?
:::

::: {.solution}
Exactly \( 1 \) and \( 10 \). By @cor-field-squares-equal, \( x^2 = 1 \) if and only if \( x = 1 \) or \( x = -1 \), and \( -1 = 10 \) in \( \nF_{11} \), since \( 10 - (-1) = 11 \). Check: \( 10^2 = 100 = 9 \cdot 11 + 1 \).
:::

::: {.warning}
A non-zero class of \( \nZ/n\nZ \) need not have an inverse. In \( \nZ/6\nZ \) the equation \( [2]x = [1] \) has **no** solution, since \( [2]x \) is always one of \( [0], [2], [4] \); and \( [2]x = [4] \) has **two** solutions, \( x = [2] \) and \( x = [5] \) (as \( 10 - 4 = 6 \)). So division by \( [a] \) modulo \( n \) is allowed when \( n \) is prime, or more generally when \( \gcd(a, n) = 1 \) (@fd3:thm-units-mod-n), and not otherwise.
:::

::: {.remark}
[No order on \( \nF_p \)]

For \( n \ge 2 \), no relation \( < \) makes \( \nZ/n\nZ \) an ordered commutative ring (@fd3:thm-integers-mod-n-ring (e)). So the inequalities of *Number Systems* have no meaning in \( \nF_p \), as the warning on order in Section 2.1 said. The representatives \( 0, 1, \dots, p - 1 \) are ordered as integers, but that order is not compatible with the arithmetic: \( 0 < p - 1 \) as integers, and adding \( 1 \) to both sides would give \( 1 < 0 \), since \( (p - 1) + 1 = 0 \) in \( \nF_p \).
:::

## Exercises

### A. Check your understanding

::: {#exr-finite-fields-from-modular-arithmetic-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. True or false: \( \nZ/8\nZ \) is a field. Justify your answer.
2. List the inverses of \( 1, 2, 3, 4 \) in \( \nF_5 \).
3. Compute \( 4 \cdot 4 + 3 \) in \( \nF_5 \).
4. True or false: \( x^2 = x \) for every \( x \in \nF_2 \).
5. How many elements does \( \nF_{13} \) have, and is \( 13 = 0 \) in \( \nF_{13} \)?
:::
:::

::: {.solution}
(a) False. \( 8 = 2 \cdot 4 \) is not prime, so @thm-zp-field-iff-prime applies; concretely \( [2][4] = [8] = [0] \) with \( [2] \ne [0] \) and \( [4] \ne [0] \), which @thm-field-basic-properties (f) forbids in a field.

(b) \( 1^{-1} = 1 \), \( 2^{-1} = 3 \), \( 3^{-1} = 2 \), \( 4^{-1} = 4 \), as in @exm-elimination-f5.

(c) \( 4 \cdot 4 + 3 = 19 = 3 \cdot 5 + 4 \), so the answer is \( 4 \).

(d) True: \( 0 \cdot 0 = 0 \) and \( 1 \cdot 1 = 1 \) in \( \nF_2 \). (This agrees with @exr-field-axioms-b1 (c): the solutions of \( x^2 = x \) in any field are \( 0 \) and \( 1 \), and \( \nF_2 \) has no other elements.)

(e) \( 13 \) is prime (neither \( 2 \) nor \( 3 \) divides it, and \( 4 \cdot 4 = 16 > 13 \)), so \( \nF_{13} \) is defined and has \( 13 \) elements. And \( 13 = 0 \) in \( \nF_{13} \), since \( 13 \mid 13 - 0 \).
:::

### B. Practice

::: {#exr-finite-fields-from-modular-arithmetic-b1}
[B1]

::: {.enumerate options="label=(\alph*)"}
1. Solve \( 3x + 5 = 2 \) in \( \nF_7 \).
2. Solve the system \( x + 2y = 3 \), \( 3x + y = 1 \) over \( \nF_7 \).
:::
:::

::: {.solution}
(a) Adding \( -5 \) to both sides gives \( 3x = 2 - 5 = -3 = 4 \) in \( \nF_7 \). Since \( 3 \cdot 5 = 15 = 1 \) in \( \nF_7 \), \( 3^{-1} = 5 \), and @prp-field-linear-equation (a) gives \( x = 5 \cdot 4 = 20 = 6 \). Check: \( 3 \cdot 6 + 5 = 23 = 3 \cdot 7 + 2 \).

(b) Here \( a = 1 \), \( b = 2 \), \( c = 3 \), \( d = 1 \), \( e = 3 \), \( f = 1 \), and \( ad - bc = 1 - 6 = -5 = 2 \ne 0 \) in \( \nF_7 \). Since \( 2 \cdot 4 = 8 = 1 \), \( 2^{-1} = 4 \). By @prp-field-linear-equation (b),
\[
x = (3 \cdot 1 - 2 \cdot 1) \cdot 4 = 4, \qquad y = (1 \cdot 1 - 3 \cdot 3) \cdot 4 = -32 = 3,
\]
since \( -32 = -5 \cdot 7 + 3 \). Check: \( 4 + 2 \cdot 3 = 10 = 3 \) and \( 3 \cdot 4 + 3 = 15 = 1 \) in \( \nF_7 \). Hence \( (x, y) = (4, 3) \), and it is the only solution.
:::

::: {#exr-finite-fields-from-modular-arithmetic-b2}
[B2: Which Are Fields?]

Determine which of \( \nZ/9\nZ \), \( \nF_5 \), \( \nZ/1\nZ \) and \( \nZ/91\nZ \) are fields. Justify your answer.
:::

::: {.solution}
\( \nZ/9\nZ \): **not a field**, since \( [3][3] = [9] = [0] \) with \( [3] \ne [0] \), against @thm-field-basic-properties (f). \( \nF_5 \): **a field**, by @thm-zp-field-iff-prime, since \( 5 \) is prime. \( \nZ/1\nZ \): **not a field**, since \( [1] = [0] \) there (@exm-finite-fields), against the condition \( 1 \ne 0 \) of (F7). \( \nZ/91\nZ \): **not a field**, since \( 91 = 7 \cdot 13 \) is not prime (@thm-zp-field-iff-prime); concretely \( [7][13] = [91] = [0] \).
:::

::: {#exr-finite-fields-from-modular-arithmetic-b3}
[B3]

Find all solutions of \( x^2 = 2 \) in \( \nF_7 \), and all solutions of \( x^2 = 2 \) in \( \nF_5 \).
:::

::: {.solution}
In \( \nF_7 \), \( 3^2 = 9 = 2 \). By @cor-field-squares-equal, \( x^2 = 2 = 3^2 \) holds exactly for \( x = 3 \) and \( x = -3 = 4 \). Check: \( 4^2 = 16 = 2 \cdot 7 + 2 \).

In \( \nF_5 \) the squares of \( 0, 1, 2, 3, 4 \) are \( 0, 1, 4, 9 = 4, 16 = 1 \). None is \( 2 \), so \( x^2 = 2 \) has no solution in \( \nF_5 \).
:::

### C. Going deeper

::: {#exr-finite-fields-from-modular-arithmetic-c1}
[C1: A Field with Four Elements]

Let \( F \) be the set of formal expressions \( a + b\alpha \) with \( a, b \in \nF_2 \): four symbols \( 0 \), \( 1 \), \( \alpha \) and \( \beta \coloneqq 1 + \alpha \), where \( a + b\alpha = c + d\alpha \) means \( a = c \) and \( b = d \). Define
\[
\begin{aligned}
(a + b\alpha) + (c + d\alpha) &\coloneqq (a + c) + (b + d)\alpha, \\
(a + b\alpha)(c + d\alpha) &\coloneqq (ac + bd) + (ad + bc + bd)\alpha,
\end{aligned}
\]
with all arithmetic of coefficients in \( \nF_2 \). (The product is what multiplying out gives if \( \alpha^2 \) is replaced by \( 1 + \alpha \).)

::: {.enumerate options="label=(\alph*)"}
1. Write out the addition and multiplication tables of \( F \).
2. Prove that \( F \) is a field.
3. Show that there is no bijection \( \varphi \colon F \to \nZ/4\nZ \) with \( \varphi(x + y) = \varphi(x) + \varphi(y) \) and \( \varphi(xy) = \varphi(x)\varphi(y) \) for all \( x, y \in F \). So this four-element field is not \( \nZ/4\nZ \) in disguise.
:::
:::

::: {.solution}
[Hint 1]

For (c): where must \( \varphi \) send \( 0 \)?
:::

::: {.solution}
[Hint 2]

For (c): look for a non-zero element of \( \nZ/4\nZ \) whose square is zero, and ask which element of \( F \) is sent to it.
:::

::: {.solution}
(a) Using the formulas, with \( 1 + 1 = 0 \) in \( \nF_2 \):
\[
\begin{array}{c|cccc}
{+} & 0 & 1 & \alpha & \beta \\ \hline
0 & 0 & 1 & \alpha & \beta \\
1 & 1 & 0 & \beta & \alpha \\
\alpha & \alpha & \beta & 0 & 1 \\
\beta & \beta & \alpha & 1 & 0
\end{array}
\qquad\qquad
\begin{array}{c|cccc}
\cdot & 0 & 1 & \alpha & \beta \\ \hline
0 & 0 & 0 & 0 & 0 \\
1 & 0 & 1 & \alpha & \beta \\
\alpha & 0 & \alpha & \beta & 1 \\
\beta & 0 & \beta & 1 & \alpha
\end{array}
\]
For instance, \( \alpha \alpha = (0 + 1\alpha)(0 + 1\alpha) = (0 + 1) + (0 + 0 + 1)\alpha = 1 + \alpha = \beta \), and \( \alpha \beta = (0 + 1\alpha)(1 + 1\alpha) = (0 + 1) + (0 + 1 + 1)\alpha = 1 \).

(b) Let \( x = a + b\alpha \), \( y = c + d\alpha \), \( z = e + g\alpha \) with \( a, b, c, d, e, g \in \nF_2 \). Since \( \nF_2 \) is a field (@exm-finite-fields), the coefficients obey every rule of Section 2.1, and in addition \( u + u = (1 + 1)u = 0 \) for every \( u \in \nF_2 \).

*Addition* works on each coefficient separately, so (F1) and (F2) for \( F \) are (F1) and (F2) for \( \nF_2 \), applied twice; the element \( 0 = 0 + 0\alpha \) satisfies (F3); and \( -x = x \) satisfies (F4), since \( a + a = 0 \) and \( b + b = 0 \).

*(F6).* Exchanging \( (a, b) \) with \( (c, d) \) leaves the product formula as it was: \( ac + bd = ca + db \) and \( ad + bc + bd = cb + da + db \), by (F1) and (F6) in \( \nF_2 \).

*(F7).* With \( 1 = 1 + 0\alpha \), \( x \cdot 1 = (a \cdot 1 + b \cdot 0) + (a \cdot 0 + b \cdot 1 + b \cdot 0)\alpha = a + b\alpha = x \). And \( 1 \ne 0 \), because the first coefficients \( 1 \) and \( 0 \) of \( \nF_2 \) differ.

*(F9).* Since \( y + z = (c + e) + (d + g)\alpha \),
\[
\begin{aligned}
x(y + z) = {} & \big(a(c + e) + b(d + g)\big) \\
& + \big(a(d + g) + b(c + e) + b(d + g)\big)\alpha ,
\end{aligned}
\]
and multiplying out the coefficients regroups this as \( \big((ac + bd) + (ae + bg)\big) + \big((ad + bc + bd) + (ag + be + bg)\big)\alpha = xy + xz \).

*(F5).* Write \( xy = h + k\alpha \) with \( h = ac + bd \) and \( k = ad + bc + bd \). Then \( (xy)z = (he + kg) + (hg + ke + kg)\alpha \), and multiplying out,
\[
\begin{aligned}
he + kg &= ace + adg + bcg + bde + bdg, \\
hg + ke + kg &= acg + ade + adg + bce + bcg + bde,
\end{aligned}
\]
where the second line uses \( bdg + bdg = 0 \). On the other side, \( yz = l + m\alpha \) with \( l = ce + dg \) and \( m = cg + de + dg \), and \( x(yz) = (al + bm) + (am + bl + bm)\alpha \). Multiplying out gives \( al + bm = ace + adg + bcg + bde + bdg \) and \( am + bl + bm = acg + ade + adg + bce + bcg + bde \), again using \( bdg + bdg = 0 \). The coefficients agree, so \( (xy)z = x(yz) \).

*(F8).* From the table, \( 1 \cdot 1 = 1 \) and \( \alpha \beta = \beta \alpha = 1 \). So every non-zero element has an inverse: \( 1^{-1} = 1 \), \( \alpha^{-1} = \beta \), \( \beta^{-1} = \alpha \).

This proves that \( F \) is a field.

(c) Assume, for a contradiction, that \( \varphi \) is such a bijection. To begin, \( \varphi(0) = \varphi(0 + 0) = \varphi(0) + \varphi(0) \) in \( \nZ/4\nZ \). Adding \( -\varphi(0) \) to both sides gives \( \varphi(0) = [0] \); this is additive cancellation, whose proof (@thm-field-basic-properties (b), first half) uses only (F1)–(F4), which hold in the commutative ring \( \nZ/4\nZ \) (@fd3:thm-integers-mod-n-ring (a)). Surjectivity provides \( x \in F \) with \( \varphi(x) = [2] \); this \( x \) is not \( 0 \), because \( \varphi(0) = [0] \ne [2] \). But
\[
\varphi(x x) = \varphi(x) \varphi(x) = [2][2] = [4] = [0] = \varphi(0),
\]
and injectivity turns this into \( x x = 0 \). By (b), \( F \) is a field, so @thm-field-basic-properties (f) gives \( x = 0 \), a contradiction. Hence no such \( \varphi \) exists.

**Marking scheme.** (10 points)

- 2: (a) both tables correct, with at least one product computed from the formula.
- 1: (b) addition clauses (F1)–(F4), coefficientwise, with \( -x = x \).
- 1: (b) (F6) and (F7), including \( 1 \ne 0 \).
- 2: (b) (F5) and (F9) by expanding coefficients, with \( u + u = 0 \) in \( \nF_2 \) used and named.
- 1: (b) (F8) from the table.
- 1: (c) \( \varphi(0) = [0] \), with the cancellation justified in \( \nZ/4\nZ \).
- 2: (c) an \( x \ne 0 \) with \( \varphi(x) = [2] \) by surjectivity, then \( x x = 0 \) by injectivity, contradicting the absence of zero divisors in \( F \).

Fatal errors (0 for the step): "\( F \) is \( \nZ/4\nZ \) because both have four elements"; using in (c) that \( \nZ/4\nZ \) is a field. A solution of (b) that checks (F5) and (F9) by listing all \( 64 \) triples from the tables earns the same points.
:::

By @thm-zp-field-iff-prime, \( \nZ/4\nZ \) is not a field, so a field with four elements cannot be found among the rings \( \nZ/n\nZ \); part (c) shows that \( F \) is not even a disguised copy of \( \nZ/4\nZ \). Chapter 5 builds this field again, from polynomials over \( \nF_2 \), and explains where the rule \( \alpha^2 = 1 + \alpha \) comes from.

::: {#exr-finite-fields-from-modular-arithmetic-c2}
[C2: Find the error]

Here is a claim with a proof.

> **Claim.** Let \( p \) be a prime. Then \( \nZ/p\nZ \) is a field.
>
> **Proof.** (1) By @exm-finite-fields, only (F8) needs checking. (2) Let \( [a] \ne [0] \); then \( a \ne 0 \). (3) Put \( [a]^{-1} \coloneqq [1/a] \). (4) Then \( [a][1/a] = [a \cdot (1/a)] = [1] \). (5) So every non-zero class has an inverse, and \( \nZ/p\nZ \) is a field.

Is the claim true? Does the proof prove it? If not, name the line that fails, the error, and give a counterexample to the step.
:::

::: {.solution}
The **claim is true**: it is @thm-zp-field-iff-prime, direction \( (\Leftarrow) \).

The **proof is wrong**, at line (3), and line (4) inherits the fault. The classes of \( \nZ/p\nZ \) are classes of **integers**, and "\( [1/a] \)" names a class only when \( 1/a \) is an integer, that is, when \( a = 1 \) or \( a = -1 \). The rule \( [x][y] = [xy] \) of @fd3:def-integers-mod-n-ring is stated for integers \( x, y \) only; line (4) applies it to the non-integer \( 1/a \), a general "fact" that no result supplies. This is entry (N9) of @fd1:exm-not-allowed-catalogue: citing a line that is not available. The proof also never uses that \( p \) is prime, a sign that something is wrong: the same lines would "prove" that \( \nZ/6\nZ \) is a field.

A counterexample to the step: \( p = 5 \), \( a = 2 \). Then \( 1/2 \notin \nZ \), so \( [1/2] \) is not an element of \( \nZ/5\nZ \). (The inverse of \( [2] \) exists, but it is \( [3] \), which line (3) does not produce.)

A repair: since \( p \) is prime and \( p \nmid a \), the only positive common divisor of \( a \) and \( p \) is \( 1 \); @lem-bezout-integers gives \( ax + py = 1 \), and then \( [a][x] = [ax] = [1] \), because \( p \mid ax - 1 \).
:::

::: {#exr-finite-fields-from-modular-arithmetic-c3}
[C3]

Find all solutions of \( x^2 + x + 1 = 0 \) in \( \nF_2 \), in \( \nF_3 \) and in \( \nF_7 \).
:::

::: {.solution}
Each field is finite, so we can test every element; this finds all solutions.

In \( \nF_2 \): the values at \( x = 0, 1 \) are \( 1 \) and \( 3 = 1 \). **No solution.**

In \( \nF_3 \): the values at \( x = 0, 1, 2 \) are \( 1 \), \( 3 = 0 \) and \( 7 = 1 \). The **only solution is \( x = 1 \)**.

In \( \nF_7 \): the values at \( x = 0, 1, \dots, 6 \) are the remainders of \( 1, 3, 7, 13, 21, 31, 43 \) on division by \( 7 \), namely \( 1, 3, 0, 6, 0, 3, 1 \). The **solutions are \( x = 2 \) and \( x = 4 \)**, since \( 7 = 1 \cdot 7 \) and \( 21 = 3 \cdot 7 \).

The three answers differ in number (none, one, two), although the equation looks the same. Section 2.5 returns to this equation with completing the square, which needs \( 1 + 1 \) to be invertible: it is in \( \nF_3 \) and \( \nF_7 \), and it is not in \( \nF_2 \).
:::

<!-- dependency ledger
exm-finite-fields (claim): (paragraph before it) the class test [a] = [b] iff n | a - b | fd3:thm-quotient-ring-by-ideal (a) with fd3:def-integers-mod-n-ring, cited
exm-finite-fields (solution): well-defined operations, commutative ring, [1] != [0] iff n >= 2, n elements | fd3:thm-quotient-ring-by-ideal (b), fd3:def-integers-mod-n-ring, fd3:thm-integers-mod-n-ring (a)-(c), cited
exm-finite-fields (solution): tables of Z/2Z | inline, class test; verify/ch02/exm-finite-fields.py
exm-finite-fields (claim): (aftermath) same tables as fd3:exm-finite-ring-not-orderable | inline comparison of tables
lem-bezout-integers (proof): gcd(a, n) >= 1 is a common divisor when (a, n) != (0, 0) | fd3:def-integer-gcd and its well-definedness paragraph, cited; coprime means gcd = 1 (fd3 def-coprime-integers, named in fd3:cor-coprime-iff-combination)
thm-zp-field-iff-prime (proof): Z/nZ is a field iff n prime, fd3's sense | fd3:thm-integers-mod-prime-field, cited; translated by the remark after def-field
thm-zp-field-iff-prime (idea): p does not divide a gives gcd(a, p) = 1; n = rs with 1 < r, s < n | fd3:cor-prime-divides-product (a) (as in fd3's proof), named in the idea only; the proof cites fd3
def-field-fp (claim): primality by trial divisors d with d * d <= p | the remark after fd3:lem-least-divisor-prime (F3.5 §03; not in the blueprint's allowed list; reported)
def-field-fp (claim): 3 * 5 = 1 in F_7; squares equal to 1 in F_p; (quick check after it) remainders of 3x mod 7; (remark on order) 1 + (p - 1) = 0 | inline; cor-field-squares-equal; verify/ch02/def-field-fp.py
exm-inverses-in-fp (solution): inverses in F_7; 101 prime (remainders on division by 2..10); Euclid on (101, 17); 17 * 6 = 102 | inline arithmetic; fd3:thm-units-mod-n, cited; verify/ch02/exm-inverses-in-fp.py
exm-elimination-f5 (solution): inverses in F_5, elimination, formula values | prp-field-linear-equation (b); verify/ch02/exm-elimination-f5.py
exm-elimination-f5 (claim): (quick check after it) x^2 = 1 in F_11 iff x in {1, 10}; 100 = 9 * 11 + 1 | cor-field-squares-equal; verify/ch02/exm-elimination-f5.py
exm-elimination-f5 (claim): (warning after it) [2]x in {[0], [2], [4]} in Z/6Z; [2]x = [4] iff x in {[2], [5]} | inline, all six classes; verify/ch02/exm-elimination-f5.py
exm-elimination-f5 (claim): (remark after it) no order on Z/nZ | fd3:thm-integers-mod-n-ring (e), cited
exr-finite-fields-from-modular-arithmetic-a1 (solution): 4 * 4 + 3 = 4 in F_5; 13 prime; [2][4] = [0] in Z/8Z | inline; remark after fd3:lem-least-divisor-prime; verify/ch02/exr-finite-fields-from-modular-arithmetic-a1.py
exr-finite-fields-from-modular-arithmetic-b1 (solution): x = 6; (x, y) = (4, 3), ad - bc = 2 | prp-field-linear-equation; verify/ch02/exr-finite-fields-from-modular-arithmetic-b1.py
exr-finite-fields-from-modular-arithmetic-b2 (solution): [3][3] = [0] mod 9; 91 = 7 * 13 | verify/ch02/exr-finite-fields-from-modular-arithmetic-b2.py
exr-finite-fields-from-modular-arithmetic-b3 (solution): squares in F_7 and F_5 | cor-field-squares-equal; verify/ch02/exr-finite-fields-from-modular-arithmetic-b3.py
exr-finite-fields-from-modular-arithmetic-c1 (solution): tables; (F5), (F9) coefficient identities; u + u = 0 in F_2 | inline; verify/ch02/exr-finite-fields-from-modular-arithmetic-c1.py (all axioms by exhaustion, and no additive-multiplicative bijection to Z/4Z among the 24 bijections)
exr-finite-fields-from-modular-arithmetic-c1 (solution): additive cancellation in the ring Z/4Z | first half of the proof of thm-field-basic-properties (b), which uses (F1)-(F4) only; fd3:thm-integers-mod-n-ring (a)
exr-finite-fields-from-modular-arithmetic-c1 (claim): (after the solution) Chapter 5 builds the field from polynomials over F_2 | F4.5 prose pointer (exm-polynomial-quotient-four-elements); nothing rests on it
exr-finite-fields-from-modular-arithmetic-c2 (solution): (N9) | fd1:exm-not-allowed-catalogue, cited
exr-finite-fields-from-modular-arithmetic-c3 (solution): values of x^2 + x + 1 in F_2, F_3, F_7 | verify/ch02/exr-finite-fields-from-modular-arithmetic-c3.py
exr-finite-fields-from-modular-arithmetic-c3 (solution): Section 2.5 explains completing the square | prose pointer within the chapter (exr-characteristic-and-prime-subfield-b2); nothing rests on it
-->
