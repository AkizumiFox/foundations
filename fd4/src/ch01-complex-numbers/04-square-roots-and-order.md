# Square Roots, Quadratic Equations, and the Missing Order

*Logic and Proof*, Section 4.11 needed, in one of its checks, the fact that every complex number has a complex square root, and took it there as a school fact about polar form. This section proves it, with no angles at all: a square root of a complex number is built from two square roots of non-negative reals, which *Number Systems*, Chapter 6 provides (@fd3:prp-cof-square-roots). The quadratic formula follows, for complex coefficients. Then we see what \( \nC \) has lost on the way from \( \nR \): it has no order compatible with its arithmetic, and the rule \( \sqrt{x}\sqrt{y} = \sqrt{xy} \) has no complex version.

## Square roots from real square roots

The question is: given \( z = a + bi \), find \( w = x + yi \) with \( w^2 = z \). Since \( w^2 = (x^2 - y^2) + 2xyi \), comparing real and imaginary parts turns the question into two real equations,
\[
x^2 - y^2 = a , \qquad 2xy = b .
\]
The answer is an explicit formula in \( a \), \( b \) and \( \abs{z} \).

::: {#prp-complex-square-roots}
[Square Roots of Complex Numbers]

Let \( z = a + bi \in \nC \) with \( a, b \in \nR \) and \( z \ne 0 \), and let \( r \coloneqq \abs{z} \). Put \( s \coloneqq 1 \) if \( b \ge 0 \) and \( s \coloneqq -1 \) if \( b < 0 \), and
\[
x \coloneqq \sqrt{\frac{r + a}{2}} , \qquad y \coloneqq s \sqrt{\frac{r - a}{2}} , \qquad w \coloneqq x + yi .
\]
Then:

::: {.enumerate options="label=(\alph*)"}
1. \( w^2 = z \);
2. for \( u \in \nC \), \( u^2 = z \) if and only if \( u = w \) or \( u = -w \);
3. \( w \ne -w \).
:::

For \( z = 0 \): \( u^2 = 0 \) if and only if \( u = 0 \).
:::

*In words: every non-zero complex number has **exactly two** square roots, \( w \) and \( -w \), and the formula finds one of them; \( 0 \) has exactly one.*

*Try it first (ten minutes): find \( w \) with \( w^2 = 3 + 4i \) by writing \( w = x + yi \). What do you do with the two equations you get?*

::: {.idea}
For \( 3 + 4i \) the two equations are \( x^2 - y^2 = 3 \) and \( 2xy = 4 \). The natural attempt eliminates \( y = 2/x \) and arrives at \( x^4 - 3x^2 - 4 = 0 \), a quartic; it can be solved, but it hides what is going on, and in general it needs the quadratic formula before we have it. The missing piece is a **third** equation, and it comes from the modulus. If \( w^2 = z \), then \( \abs{w}^2 = \abs{w^2} = \abs{z} \) by @thm-conjugate-properties (d), that is, \( x^2 + y^2 = r \). Now the first equation and the third give \( x^2 \) and \( y^2 \) by adding and subtracting: \( x^2 = (r + a)/2 \), \( y^2 = (r - a)/2 \). That fixes \( x \) and \( y \) up to sign, and the second equation \( 2xy = b \) says which signs go together: \( xy \) has the sign of \( b \). For \( 3 + 4i \): \( r = 5 \), \( x^2 = 4 \), \( y^2 = 1 \), \( xy > 0 \), so \( w = \pm(2 + i) \).

The proof runs this forward: define \( x \) and \( y \) by the formulas, check \( w^2 = z \), and get "only \( \pm w \)" from the field axioms.

*Before reading on: why does the sign of \( b \) decide whether \( x \) and \( y \) have the same sign?*
:::

The proof uses one small rule about real square roots: for \( p, q \in \nR \) with \( p, q \ge 0 \),
\[
\sqrt{p}\,\sqrt{q} = \sqrt{pq} .
\]
Both sides are non-negative (a product of non-negative reals is non-negative), and the square of the left side is \( (\sqrt p)^2 (\sqrt q)^2 = pq \), by commutativity; so the left side is the non-negative number whose square is \( pq \), which is the right side by the uniqueness in @fd3:prp-cof-square-roots. The rule is about non-negative **reals** only; the last part of this section shows that it has no complex version.

::: {.proof}
*The roots exist.* By @lem-real-part-at-most-modulus, \( \abs{a} = \abs{\operatorname{Re} z} \le r \), so \( -r \le a \le r \) (@fd3:prp-absolute-value-ordered-field (d)). Hence \( r + a \ge 0 \) and \( r - a \ge 0 \) (@fd3:prp-ordered-ring-rules (a), (b)), and since \( 1/2 > 0 \), also \( (r + a)/2 \ge 0 \) and \( (r - a)/2 \ge 0 \) (@fd3:prp-ordered-ring-rules (c)). So the two square roots in the definition of \( x \) and \( y \) exist (@fd3:prp-cof-square-roots).

(a) Since \( s^2 = 1 \),
\[
x^2 - y^2 = \frac{r + a}{2} - s^2 \, \frac{r - a}{2} = \frac{r + a}{2} - \frac{r - a}{2} = a .
\]
For the imaginary part, the rule for real square roots gives
\[
\begin{aligned}
2xy &= 2s\sqrt{\frac{r + a}{2}}\sqrt{\frac{r - a}{2}} = 2s\sqrt{\frac{r^2 - a^2}{4}} \\
&= s\sqrt{r^2 - a^2} = s\sqrt{b^2} = s\abs{b} = b .
\end{aligned}
\]
Here the third equality is \( 2\sqrt{t/4} = \sqrt{4}\sqrt{t/4} = \sqrt{t} \), by the same rule and \( \sqrt 4 = 2 \); the fourth uses \( r^2 = a^2 + b^2 \) (@def-conjugate-modulus); the fifth holds because \( \abs{b} \ge 0 \) and \( \abs{b}^2 = b^2 \) (@fd3:prp-absolute-value-ordered-field (a), (b)), with uniqueness in @fd3:prp-cof-square-roots; and the last because \( s\abs{b} = b \) by the definitions of \( s \) and of \( \abs{b} \) (@fd3:def-absolute-value-ordered-field), in each of the two cases \( b \ge 0 \) and \( b < 0 \). Hence \( w^2 = (x^2 - y^2) + 2xyi = a + bi = z \), by the multiplication rule of @def-complex-numbers.

(b) Let \( u \in \nC \). Since \( \nC \) is a commutative ring, \( (u - w)(u + w) = u^2 - w^2 \) (@prp-complex-arithmetic-laws, @fd3:prp-ring-algebra (c)). If \( u^2 = z \), then \( u^2 - w^2 = z - z = 0 \) by (a), so \( (u - w)(u + w) = 0 \). Since \( \nC \) is a field (@thm-complex-numbers-field), it has no zero divisors (@fd3:lem-field-fraction-rules (d)), so \( u - w = 0 \) or \( u + w = 0 \), that is, \( u = w \) or \( u = -w \). Conversely \( w^2 = z \) by (a), and \( (-w)^2 = w^2 = z \) by @fd3:prp-ring-algebra (c).

(c) First \( w \ne 0 \), since \( w^2 = z \ne 0 \) and \( 0^2 = 0 \). Suppose \( w = -w \). Then \( 2w = w + w = 0 \). But \( 2 = 1 + 1 \ne 0 \) in \( \nC \): it is the real number \( 2 \), which is positive in \( \nR \) (@fd3:prp-ordered-ring-rules (h)), and \( \nR \subseteq \nC \) by the injective embedding of @prp-reals-embed-complex. So \( 2w = 0 \) with \( 2 \ne 0 \) and \( w \ne 0 \) contradicts the absence of zero divisors. Hence \( w \ne -w \).

Finally, for \( z = 0 \): \( 0^2 = 0 \), and if \( u^2 = u \cdot u = 0 \), then \( u = 0 \) by @fd3:lem-field-fraction-rules (d). This proves the proposition.
:::

The answer to the prompt: \( x \) is non-negative by construction, and \( y \) is \( s \) times a non-negative number, so \( xy \) is \( s \) times a non-negative number, and \( 2xy \) must equal \( b \). If \( b > 0 \), then \( x \) and \( y \) must both be non-zero with the same sign; if \( b < 0 \), opposite signs. When \( b = 0 \) the choice of \( s \) does not matter, because then one of \( x, y \) is \( 0 \).

The proposition proves what *Logic and Proof*, Section 4.11 assumed, and it is stronger: it counts the roots. It uses only the field \( \nC \), its modulus, and square roots of non-negative reals; no angle, cosine or sine appears. That matters later: Chapter 5 proves the Fundamental Theorem of Algebra using square roots in exactly this form.

::: {#exm-complex-square-root}
[Square Roots of \( 5 - 12i \)]

Find all \( w \in \nC \) with \( w^2 = 5 - 12i \).
:::

::: {.solution}
Write \( w = x + yi \) with \( x, y \in \nR \). Comparing real and imaginary parts in \( (x^2 - y^2) + 2xyi = 5 - 12i \) gives
\[
x^2 - y^2 = 5 \qquad \text{and} \qquad xy = -6 .
\]
Taking moduli, by @thm-conjugate-properties (d), \( x^2 + y^2 = \abs{w}^2 = \abs{5 - 12i} = \sqrt{25 + 144} = 13 \). Adding and subtracting, \( x^2 = 9 \) and \( y^2 = 4 \), so \( x = \pm 3 \) and \( y = \pm 2 \). Since \( xy = -6 < 0 \), \( x \) and \( y \) have opposite signs. Hence \( w = 3 - 2i \) or \( w = -3 + 2i \). Check: \( (3 - 2i)^2 = 9 - 12i + 4i^2 = 5 - 12i \), and \( (-3 + 2i)^2 = (3 - 2i)^2 \).

The formula of @prp-complex-square-roots gives the same root: \( a = 5 \), \( b = -12 < 0 \), so \( s = -1 \); \( r = 13 \), \( x = \sqrt{18/2} = 3 \) and \( y = -\sqrt{8/2} = -2 \). By part (b) there are no other roots.
:::

::: {.check}
Find the square roots of \( -4 \) and of \( 2i \).
:::

::: {.solution}
For \( -4 \): \( a = -4 \), \( b = 0 \), \( r = 4 \), so \( x = \sqrt{0} = 0 \) and \( y = \sqrt{8/2} = 2 \); the roots are \( \pm 2i \), and indeed \( (2i)^2 = -4 \). For \( 2i \): \( a = 0 \), \( b = 2 \), \( r = 2 \), so \( x = \sqrt{1} = 1 \) and \( y = 1 \); the roots are \( \pm(1 + i) \), and \( (1 + i)^2 = 1 + 2i - 1 = 2i \).
:::

## The quadratic formula

With square roots in hand, a quadratic equation with complex coefficients is solved exactly as in school: complete the square. The only difference is that we never need to ask whether the discriminant is negative.

::: {#cor-complex-quadratic-formula}
[Quadratic Formula over the Complex Numbers]

Let \( a, b, c \in \nC \) with \( a \ne 0 \), and let \( d \in \nC \) be a square root of \( b^2 - 4ac \) (one exists by @prp-complex-square-roots). Then for \( z \in \nC \),
\[
az^2 + bz + c = 0 \iff z = \frac{-b + d}{2a} \ \text{ or } \ z = \frac{-b - d}{2a} .
\]
The two solutions coincide if and only if \( b^2 - 4ac = 0 \).
:::

Here \( a, b, c \) are complex numbers, in a departure from the chapter's habit of reserving these letters for reals; the statement is the school formula, and keeps its letters. The choice of \( d \) does not matter: the other square root is \( -d \) (@prp-complex-square-roots (b)), which swaps the two solutions.

::: {.idea}
Complete the square, as in school: after multiplying by \( 4a \), the equation says that \( 2az + b \) is a square root of \( b^2 - 4ac \). The square roots of \( b^2 - 4ac \) are exactly \( d \) and \( -d \), and solving the two linear equations \( 2az + b = \pm d \) gives the formula.
:::

::: {.proof}
Multiply by \( 4a \) and complete the square. By the ring laws (@prp-complex-arithmetic-laws) and @fd3:prp-ring-algebra (d),
\[
4a(az^2 + bz + c) = 4a^2z^2 + 4abz + 4ac = (2az + b)^2 - (b^2 - 4ac) .
\]
Now \( 4a \ne 0 \), since \( 4 \ne 0 \) in \( \nC \) (as for \( 2 \) in the proof of @prp-complex-square-roots (c)) and \( a \ne 0 \), and \( \nC \) has no zero divisors (@thm-complex-numbers-field, @fd3:lem-field-fraction-rules (d)). So \( az^2 + bz + c = 0 \) if and only if \( (2az + b)^2 = d^2 \), that is, \( (2az + b - d)(2az + b + d) = 0 \), as in the proof of @prp-complex-square-roots (b). By the absence of zero divisors again, this holds if and only if \( 2az + b = d \) or \( 2az + b = -d \). Since \( 2a \ne 0 \), these say \( z = (-b + d)/(2a) \) or \( z = (-b - d)/(2a) \).

The two solutions coincide if and only if \( d = -d \), that is, \( 2d = 0 \), that is, \( d = 0 \) (as \( 2 \ne 0 \)). And \( d = 0 \) if and only if \( d^2 = 0 \) (no zero divisors), that is, \( b^2 - 4ac = 0 \). This proves the corollary.
:::

**Example.** Solve \( z^2 - (3 + i)z + (2 + 2i) = 0 \). Here \( a = 1 \), and the discriminant is
\[
(3 + i)^2 - 4(2 + 2i) = (8 + 6i) - (8 + 8i) = -2i .
\]
The formula of @prp-complex-square-roots, applied to \( -2i \) (real part \( 0 \), imaginary part \( -2 < 0 \), modulus \( 2 \)), gives \( x = \sqrt{2/2} = 1 \) and \( y = -\sqrt{2/2} = -1 \), so \( d = 1 - i \); indeed \( (1 - i)^2 = 1 - 2i - 1 = -2i \). The solutions are
\[
z = \frac{(3 + i) + (1 - i)}{2} = 2 \qquad \text{and} \qquad z = \frac{(3 + i) - (1 - i)}{2} = 1 + i .
\]
Check: their sum is \( 3 + i \) and their product is \( 2 + 2i \), the negative of the middle coefficient and the constant term, as they should be for \( (z - 2)(z - (1 + i)) \).

## No order on the complex numbers

In \( \nR \), and in every ordered field, a non-zero square is positive (@fd3:prp-ordered-ring-rules (e)). In \( \nC \), \( i \) is non-zero and its square is \( -1 \). If \( \nC \) carried an order of the kind \( \nR \) has, \( -1 \) would have to be positive, and so would \( 1 \). That is already the proof.

::: {#prp-complex-not-orderable}
[The Complex Numbers Cannot Be Ordered]

There is **no** relation \( < \) on \( \nC \) with which \( (\nC, +, \cdot, <) \) is an ordered field in the sense of @fd3:def-ordered-ring-and-field.
:::

::: {.proof}
Suppose \( < \) is a relation on \( \nC \) with which \( \nC \) is an ordered field. Since \( i = (0, 1) \ne (0, 0) = 0 \), @fd3:prp-ordered-ring-rules (e) gives \( i^2 > 0 \), that is, \( -1 > 0 \) (@prp-reals-embed-complex: \( i \cdot i = -1 \)). Since \( 1 \ne 0 \) in the field \( \nC \), the same part (e) gives \( 1 > 0 \). Adding, by @fd3:prp-ordered-ring-rules (b), \( 0 = 1 + (-1) > 0 + 0 = 0 \). But \( 0 < 0 \) is impossible: (O1), with both elements equal to \( 0 \), says that exactly one of \( 0 < 0 \) and \( 0 = 0 \) holds, and \( 0 = 0 \) does. So no such relation exists.
:::

The proof never asks whether \( i > 0 \) or \( i < 0 \): part (e) covers both at once. It also never assumes that the hypothetical order agrees with the order of \( \nR \) on real numbers. It concludes \( 1 > 0 \) and \( -1 > 0 \) in whatever order is supposed, and that is the contradiction.

::: {.remark}
*Number Systems*, Chapter 4 showed, in an exercise (@fd3:exr-rules-and-absolute-value-c1), that a field containing a square root of \( -1 \) cannot be ordered, and named the complex numbers as such a field; the proposition proves that fact for \( \nC \) on its own. Compare @fd3:exm-finite-ring-not-orderable and @fd3:thm-integers-mod-n-ring (e): there the obstacle to an order is \( n \cdot 1 = 0 \) for some \( n \ge 1 \). That obstacle is absent here, since \( n \cdot 1 \) in \( \nC \) is the real number \( n \cdot 1 > 0 \) of \( \nR \) (@fd3:prp-ordered-ring-rules (h)), which is non-zero; the obstacle in \( \nC \) is \( i^2 = -1 \) instead.
:::

::: {.warning}
An inequality \( z < w \) between complex numbers means nothing: by @prp-complex-not-orderable no order on \( \nC \) is compatible with its arithmetic. Every inequality in this chapter compares **real** numbers: moduli, real parts, imaginary parts, or quantities proved to be real, as \( 2\operatorname{Re}(z\conj{w}) \) was in Section 1.3. Writing \( i > 0 \) leads, by the proof above, to \( 0 > 0 \); so does writing \( i < 0 \).
:::

::: {.check}
Is the following a proof that \( \nC \) cannot be ordered? "Every real square is \( \ge 0 \), and \( i^2 = -1 < 0 \). So \( i \) is not a square of anything, a contradiction."
:::

::: {.solution}
No. The argument proves nothing about orders on \( \nC \). "\( -1 < 0 \)" is a statement in \( \nR \)'s order, and a hypothetical order on \( \nC \) need not agree with it on the reals; the argument never even introduces the hypothetical order. And "\( i \) is not a square" is false: \( i = (\pm(1 + i)/\sqrt 2)^2 \) by @prp-complex-square-roots. The correct proof works inside the supposed order, where \( i^2 > 0 \) because \( i \ne 0 \).
:::

## The square-root rule does not survive

In \( \nR \), \( \sqrt{x}\sqrt{y} = \sqrt{xy} \) for \( x, y \ge 0 \): that is the rule for real square roots used above. A non-zero complex number has two square roots and no preferred one, and no way of preferring one keeps the rule alive.

::: {.warning}
No choice of "the" square root \( \sqrt{z} \) of each complex \( z \) can satisfy \( \sqrt{z}\sqrt{w} = \sqrt{zw} \) for all \( z, w \in \nC \). Whatever is chosen for \( \sqrt{-1} \), it is \( i \) or \( -i \) (@prp-complex-square-roots (b)), and in both cases \( \sqrt{-1} \cdot \sqrt{-1} = (\pm i)^2 = -1 \). But \( \sqrt{(-1)(-1)} = \sqrt{1} \), which must be \( 1 \) if the rule is to extend the real square root. So in this volume the symbol \( \sqrt{\phantom{x}} \) is applied only to non-negative reals; for any other \( z \), say "a square root of \( z \)" and solve \( w^2 = z \).
:::

## Exercises

### A. Check your understanding

::: {#exr-square-roots-and-order-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. True or false: if \( z, w \in \nC \) and \( z^2 = w^2 \), then \( z = w \). Justify your answer, and state what **is** true.
2. Run the formula of @prp-complex-square-roots on \( z = -4 \): compute \( a, b, r, s, x, y \) and both square roots.
3. Where in the proof of @prp-complex-square-roots is \( r \ge \abs{a} \) used?
4. State the idea of the proof of @prp-complex-square-roots in two sentences.
:::
:::

::: {.solution}
(a) False: \( z = 1 \), \( w = -1 \) have \( z^2 = w^2 = 1 \) and \( z \ne w \). What is true: \( z^2 = w^2 \) implies \( z = w \) or \( z = -w \), since \( (z - w)(z + w) = z^2 - w^2 = 0 \) and \( \nC \) has no zero divisors (this is the argument of @prp-complex-square-roots (b)).

(b) \( a = -4 \), \( b = 0 \), \( r = \abs{-4} = 4 \), \( s = 1 \) (as \( b \ge 0 \)), \( x = \sqrt{(4 - 4)/2} = 0 \), \( y = \sqrt{(4 + 4)/2} = 2 \). So \( w = 2i \), and the square roots are \( \pm 2i \).

(c) To take the square roots at all: \( r \ge \abs{a} \) gives \( r + a \ge 0 \) and \( r - a \ge 0 \), so \( \sqrt{(r + a)/2} \) and \( \sqrt{(r - a)/2} \) exist.

(d) Comparing parts gives \( x^2 - y^2 = a \) and \( 2xy = b \); taking moduli gives a third equation \( x^2 + y^2 = r \), and the first and third give \( x^2 \) and \( y^2 \) by adding and subtracting. The signs are then fixed by \( 2xy = b \), and the absence of zero divisors shows that \( \pm w \) are the only roots.
:::

### B. Practice

::: {#exr-square-roots-and-order-b1}
[B1]

::: {.enumerate options="label=(\alph*)"}
1. Find all \( w \in \nC \) with \( w^2 = -3 + 4i \).
2. Hence solve \( z^2 + 2z + 4 - 4i = 0 \).
:::
:::

::: {.solution}
(a) Write \( w = x + yi \). Comparing parts, \( x^2 - y^2 = -3 \) and \( xy = 2 \). Taking moduli (@thm-conjugate-properties (d)), \( x^2 + y^2 = \abs{-3 + 4i} = \sqrt{9 + 16} = 5 \). Adding and subtracting, \( x^2 = 1 \) and \( y^2 = 4 \). Since \( xy = 2 > 0 \), \( x \) and \( y \) have the same sign, so \( w = 1 + 2i \) or \( w = -1 - 2i \), and by @prp-complex-square-roots (b) there are no others. Check: \( (1 + 2i)^2 = 1 + 4i - 4 = -3 + 4i \).

(b) By @cor-complex-quadratic-formula with \( a = 1 \), \( b = 2 \), \( c = 4 - 4i \): the discriminant is \( 4 - 4(4 - 4i) = -12 + 16i = 4(-3 + 4i) \), with square root \( d = 2(1 + 2i) = 2 + 4i \) by (a), since \( (2(1 + 2i))^2 = 4(1 + 2i)^2 \). So
\[
z = \frac{-2 + (2 + 4i)}{2} = 2i \qquad \text{or} \qquad z = \frac{-2 - (2 + 4i)}{2} = -2 - 2i .
\]
Equivalently, completing the square, \( z^2 + 2z + 4 - 4i = (z + 1)^2 - (-3 + 4i) \), so \( z + 1 = \pm(1 + 2i) \). Check: \( (2i)^2 + 2(2i) + 4 - 4i = -4 + 4i + 4 - 4i = 0 \).
:::

::: {#exr-square-roots-and-order-b2}
[B2: Put the proof in order]

The nine lines below include the seven lines of a proof of @prp-complex-not-orderable, shuffled, and two lines that do not belong. Write the seven lines in an order that makes a proof, and say what is wrong with each of the other two.

::: {.enumerate options="label=(\roman*)"}
1. \( i^2 = -1 \), so \( -1 > 0 \).
2. Since \( i \ne 0 \), we have \( i > 0 \).
3. Suppose \( < \) is a relation on \( \nC \) that makes \( \nC \) an ordered field.
4. \( 0 < 0 \) is impossible by (O1), so no such relation exists.
5. So \( i^2 > 0 \), because non-zero squares are positive in an ordered field.
6. \( 1 \ne 0 \), so \( 1 = 1^2 > 0 \).
7. \( i^2 = -1 < 0 \), because \( -1 < 0 \) in \( \nR \).
8. \( i \ne 0 \), since \( i = (0, 1) \ne (0, 0) \).
9. Adding, \( 0 = 1 + (-1) > 0 + 0 = 0 \).
:::
:::

::: {.solution}
An admissible order is (iii), (viii), (v), (i), (vi), (ix), (iv). The constraints are what each line uses: (iii) comes first, since every later line works in the supposed order; (v) uses (viii); (i) uses (v); (ix) uses (i) and (vi); (iv) uses (ix). Line (vi) uses only (iii), so it may stand anywhere after (iii) and before (ix): for instance (iii), (vi), (viii), (v), (i), (ix), (iv) is also admissible. No other changes are possible.

Line (ii) drops a case: from \( i \ne 0 \), trichotomy (O1) gives \( i > 0 \) **or** \( i < 0 \), and the line keeps only the first. That is (N7) of @fd1:exm-not-allowed-catalogue, a missing case. Line (v) needs neither case, which is why the proof does not split.

Line (vii) cites a reason that is not available: the supposed order on \( \nC \) is arbitrary, and nothing says that it agrees with the order of \( \nR \) on the real numbers. The proposition is about **every** relation on \( \nC \), and (vii) quietly replaces "every" by "one that extends \( \nR \)'s order". (The inequality \( -1 < 0 \) does hold in any ordered field, by @fd3:prp-ordered-ring-rules (a) applied to \( 1 > 0 \), so the line could be repaired by citing that; as written its reason is (N9) of @fd1:exm-not-allowed-catalogue, a fact that is not available.)
:::

::: {#exr-square-roots-and-order-b3}
[B3]

Let \( a, b, c \in \nR \) with \( a \ne 0 \) and \( b^2 - 4ac < 0 \). Prove that the equation \( az^2 + bz + c = 0 \) has exactly the two solutions
\[
z = \frac{-b + i\sqrt{4ac - b^2}}{2a} \qquad \text{and} \qquad z = \frac{-b - i\sqrt{4ac - b^2}}{2a}
\]
in \( \nC \), and that they are conjugate to each other.
:::

::: {.solution}
Since \( 4ac - b^2 > 0 \) (@fd3:prp-ordered-ring-rules (a)), \( q \coloneqq \sqrt{4ac - b^2} \) exists, \( q > 0 \), and \( d \coloneqq iq \) satisfies \( d^2 = i^2 q^2 = -(4ac - b^2) = b^2 - 4ac \). So @cor-complex-quadratic-formula with this \( d \) gives exactly the two solutions displayed, and they are distinct since \( b^2 - 4ac \ne 0 \). Since \( a, b, q \) are real and \( 2a \ne 0 \), the two solutions are
\[
-\frac{b}{2a} + \frac{q}{2a}\, i \qquad \text{and} \qquad -\frac{b}{2a} - \frac{q}{2a}\, i ,
\]
with the same real part and opposite imaginary parts: each is the conjugate of the other (@def-conjugate-modulus). For instance \( z^2 - 2z + 5 = 0 \) has \( b^2 - 4ac = -16 \), \( q = 4 \), and the solutions \( 1 \pm 2i \).
:::

### C. Going deeper

::: {#exr-square-roots-and-order-c1}
[C1: Find the error]

Here is an argument.

> **Claim.** For \( z, w \in \nC \), if \( z^2 = w^2 \), then \( z = w \) or \( z = -w \).
>
> **Proof.** If \( w = 0 \), then \( z^2 = 0 \), so \( z = 0 = w \), since \( \nC \) has no zero divisors. If \( w \ne 0 \), put \( u \coloneqq z/w \), which exists because \( \nC \) is a field; then \( u^2 = z^2/w^2 = 1 \). Taking square roots, \( u = \sqrt{u^2} = \sqrt{1} = 1 \). Since the sign is lost when taking square roots, \( u = 1 \) or \( u = -1 \). Multiplying by \( w \), \( z = w \) or \( z = -w \).

Is the claim true? Does the argument prove it? If not, name the line that fails and the reason, give a counterexample to that line, and repair the argument.
:::

::: {.solution}
The claim is true: it is the argument of @prp-complex-square-roots (b), and it also follows directly from \( (z - w)(z + w) = z^2 - w^2 = 0 \) and the absence of zero divisors in \( \nC \).

The argument does not prove it. The failing line is "\( u = \sqrt{u^2} = \sqrt{1} = 1 \)". It uses the rule "\( u = \sqrt{u^2} \) whenever \( u^2 \) is a non-negative real", which is neither proved nor true: it is a general "fact" of the kind (N9) of @fd1:exm-not-allowed-catalogue forbids. The symbol \( \sqrt{\phantom{x}} \) is defined only on non-negative reals, and \( u \) is a complex number; even for real \( u \), \( \sqrt{u^2} = \abs{u} \), not \( u \). Counterexample to the step: \( u = -1 \) has \( u^2 = 1 \), but \( \sqrt{u^2} = \sqrt{1} = 1 \ne u \).

The next line, "\( u = 1 \) or \( u = -1 \)", is a valid weakening of \( u = 1 \) (a disjunction follows from either part), so it is not itself an error; it only papers over the loss of the root \( -1 \) one line earlier. The rest of the argument (the case \( w = 0 \), the division, and multiplying back by \( w \)) is correct.

Repair: replace the two middle lines by "Then \( (u - 1)(u + 1) = u^2 - 1 = 0 \), and \( \nC \) has no zero divisors, so \( u = 1 \) or \( u = -1 \)."

**Marking scheme.** (10 points)
- 2: says the claim is true, with a reason.
- 3: names the line \( u = \sqrt{u^2} = \sqrt{1} = 1 \) as the failing one, and its illegal rule \( u = \sqrt{u^2} \).
- 2: a counterexample **to that step** (\( u = -1 \), or any \( u \) with \( u^2 = 1 \), \( u \ne 1 \)).
- 3: a correct repair, by factoring \( u^2 - 1 \) and using no zero divisors (or by @prp-complex-square-roots (b) applied to \( z = 1 \)).
Fatal errors (0 for the step): declaring the claim false; naming the "sign is lost" line as the error, since it is a valid weakening.
:::

::: {#exr-square-roots-and-order-c2}
[C2: A second proof that there is no order]

::: {.enumerate options="label=(\alph*)"}
1. Use @prp-complex-square-roots to give a second proof of @prp-complex-not-orderable in which the element \( i \) is never mentioned.
2. Say why the argument in (a) does not need the special element \( i \).
3. Is the converse of the principle behind (a) true? That is: if a commutative ring with \( 1 \ne 0 \) admits no order, must \( -1 \) be a square in it? Test the ring \( \nZ/3\nZ \).
:::
:::

::: {.solution}
[Hint 1]

In an ordered field, which elements can be squares? For (c), list the squares of the three classes.
:::

::: {.solution}
(a) Suppose \( < \) makes \( \nC \) an ordered field. Every square is then \( \ge 0 \): a non-zero square is positive by @fd3:prp-ordered-ring-rules (e), and \( 0^2 = 0 \). By @prp-complex-square-roots (a), applied to the non-zero number \( -1 \), some \( d \in \nC \) has \( d^2 = -1 \). So \( -1 = d^2 \ge 0 \). Also \( -1 \ne 0 \), since otherwise \( 1 = -(-1) = -0 = 0 \) (@fd3:prp-ring-algebra (a)), against \( 1 \ne 0 \) in the field \( \nC \) (@thm-complex-numbers-field). Hence \( -1 > 0 \). By part (e) again, \( 1 > 0 \). Adding (@fd3:prp-ordered-ring-rules (b)), \( 0 = 1 + (-1) > 0 \), which (O1) forbids. This is the argument of @fd3:exr-rules-and-absolute-value-c1, with the square root of \( -1 \) supplied by a formula.

(b) The argument uses only that \( -1 \) is a square in \( \nC \), and that is a property of the field, not of any named element. It does not matter that the formula of @prp-complex-square-roots, applied to \( -1 \), happens to produce \( i \) (\( a = -1 \), \( b = 0 \), \( r = 1 \): \( x = 0 \), \( y = 1 \)). The same argument shows that no field in which \( -1 \) is a square can be ordered; in particular no field in which **every** element is a square.

(c) No. The ring \( \nZ/3\nZ \) is a commutative ring with \( [1] \ne [0] \) (@fd3:thm-integers-mod-n-ring (a), (c)), and no relation makes it an ordered commutative ring (@fd3:thm-integers-mod-n-ring (e)). Its three elements are \( [0], [1], [2] \) (part (b) there), with squares \( [0]^2 = [0] \), \( [1]^2 = [1] \), \( [2]^2 = [4] = [1] \). So the squares are \( [0] \) and \( [1] \), while \( -[1] = [2] \). Hence \( -1 \) is not a square in \( \nZ/3\nZ \), and yet the ring cannot be ordered: the obstacle there is \( 3 \cdot [1] = [0] \), not a square root of \( -1 \).
:::

<!-- dependency ledger
prp-complex-square-roots (claim): Logic and Proof, Section 4.11 took "every complex number has a complex square root" as a school fact | backward pointer; prp-complex-square-roots pays it (fd1 11-models.md ledger line 698)
prp-complex-square-roots (proof): sqrt(p) sqrt(q) = sqrt(pq) for p, q >= 0; sqrt 4 = 2 | inline from fd3:prp-cof-square-roots (uniqueness) and (O4) / fd3:prp-ring-algebra (b)
prp-complex-square-roots (proof): s^2 = 1; s|b| = b by cases on the sign of b; 1/2 > 0 in R; (r + a)/2 - (r - a)/2 = a | inline; fd3:def-absolute-value-ordered-field; 1/2 > 0 since 2 > 0 and 2 * (1/2) = 1 > 0 (fd3:prp-ordered-ring-rules (c), (d), (e))
prp-complex-square-roots (proof): (u - w)(u + w) = u^2 - w^2 in a commutative ring | prp-complex-arithmetic-laws with fd3:prp-ring-algebra (c); inline
prp-complex-square-roots (proof): 2 = 1 + 1 is non-zero in C | fd3:prp-ordered-ring-rules (h) in R, prp-reals-embed-complex (injective, preserves sums), cited
prp-complex-square-roots (claim): Chapter 5 proves the FTA from square roots in this form | prose pointer (F4.5, lem-complex-direction-negative-real-part); nothing depends on it
exm-complex-square-root (solution): |5 - 12i| = 13; x = 3, y = -2 | inline; verify/ch01/exm-complex-square-root.py
prp-complex-square-roots (example): quick check, square roots of -4 and 2i | inline; verify/ch01/prp-complex-square-roots.py
cor-complex-quadratic-formula (proof): 4a(az^2 + bz + c) = (2az + b)^2 - (b^2 - 4ac); 4 != 0 in C | prp-complex-arithmetic-laws, fd3:prp-ring-algebra (d); 4 = 4 * 1 > 0 in R by fd3:prp-ordered-ring-rules (h) and prp-reals-embed-complex
cor-complex-quadratic-formula (example): z^2 - (3 + i)z + (2 + 2i) = 0 has the solutions 2 and 1 + i; discriminant -2i; (1 - i)^2 = -2i | inline; verify/ch01/cor-complex-quadratic-formula.py
prp-complex-not-orderable (proof): i * i = -1 | prp-reals-embed-complex, cited
prp-complex-not-orderable (claim): n * 1 in C is the real n * 1 > 0 | prp-reals-embed-complex (iota preserves sums, so iota(n * 1) = n * 1), fd3:prp-ordered-ring-rules (h); inline
prp-complex-not-orderable (claim): pays fd3 F3.9 Section 4.1 Exercise C1's prose pointer | backward pointer
prp-complex-not-orderable (solution): quick check, i = ((1 + i)/sqrt 2)^2 | prp-complex-square-roots; verify/ch01/prp-complex-square-roots.py
exr-square-roots-and-order-a1 (solution): run of the formula on -4 | verify/ch01/exr-square-roots-and-order-a1.py
exr-square-roots-and-order-b1 (solution): roots +-(1 + 2i); solutions 2i, -2 - 2i | verify/ch01/exr-square-roots-and-order-b1.py
exr-square-roots-and-order-b3 (solution): d = i sqrt(4ac - b^2), d^2 = b^2 - 4ac; example z^2 - 2z + 5 | inline; verify/ch01/exr-square-roots-and-order-b3.py
exr-square-roots-and-order-c2 (solution): -1 != 0 in a field | fd3:prp-ring-algebra (a); inline
exr-square-roots-and-order-c2 (solution): squares in Z/3Z are [0], [1]; -[1] = [2] | fd3:def-integers-mod-n-ring (class arithmetic, [4] = [1]); inline; verify/ch01/exr-square-roots-and-order-c2.py
-->
