# The Unit Circle and Polar Form

Addition in \( \nC \) is addition of arrows in the plane: \( (a, b) + (c, d) = (a + c, b + d) \) puts the second arrow at the tip of the first. Multiplication has a picture too, and Section 1.2 already holds half of it: the modulus of a product is the product of the moduli (@thm-conjugate-properties (d)). The other half is about angles, and angles need the functions cosine and sine, which this volume does not construct. This section first proves everything about directions that needs no angle at all, then states exactly five facts about cosine and sine that it borrows, and from those five builds the polar form of a complex number and the rule "multiply the lengths, add the angles".

## Length and direction

Every non-zero complex number should be a length times a direction. The length is the modulus. The directions are the complex numbers of length \( 1 \), and they deserve a name.

*The unit circle is the set of complex numbers at distance \( 1 \) from \( 0 \).*

We write
\[
\nT \coloneqq \{ u \in \nC : \abs{u} = 1 \}
\]
for the **unit circle**. For \( u = x + yi \) with \( x, y \in \nR \), the condition \( \abs{u} = 1 \) says \( \sqrt{x^2 + y^2} = 1 \), that is, \( x^2 + y^2 = 1 \): both sides of the first equation are non-negative, so it holds exactly when the squares agree (@fd3:prp-ordered-ring-rules (g)). So \( \nT \) is the circle of radius \( 1 \) about \( 0 \) in the plane. It contains \( 1 \), \( -1 \), \( i \) and \( -i \), and also \( \tfrac35 + \tfrac45 i \), since \( \tfrac{9}{25} + \tfrac{16}{25} = 1 \). It does not contain \( 1 + i \), whose modulus is \( \sqrt 2 \ne 1 \).

The next proposition collects what the multiplication of \( \nC \) does on \( \nT \). None of it uses an angle.

::: {#prp-unit-circle}
[The Unit Circle]

::: {.enumerate options="label=(\alph*)"}
1. \( 1 \in \nT \). If \( u, v \in \nT \), then \( uv \in \nT \). If \( u \in \nT \), then \( u \ne 0 \) and \( u^{-1} = \conj{u} \in \nT \).
2. For every \( z \in \nC \) with \( z \ne 0 \) there is **exactly one** pair \( (r, u) \) with \( r \in \nR \), \( r > 0 \), \( u \in \nT \) and \( z = ru \), namely \( r = \abs{z} \) and \( u = z / \abs{z} \).
3. For \( z \in \nC \) with \( z \ne 0 \): \( 1/z = \conj{z} \) if and only if \( \abs{z} = 1 \).
:::
:::

::: {.idea}
Every part is a statement about moduli, so each follows from the rules of Section 1.2: moduli multiply, \( u\conj{u} = \abs{u}^2 \), and only \( 0 \) has modulus \( 0 \). For (b), divide \( z \) by its length; for the uniqueness, take moduli of \( z = ru \).
:::

::: {.proof}
(a) By @prp-modulus-of-real, the modulus of the real number \( 1 \) is its absolute value, which is \( 1 \); so \( 1 \in \nT \). If \( \abs{u} = \abs{v} = 1 \), then \( \abs{uv} = \abs{u}\abs{v} = 1 \) by @thm-conjugate-properties (d). Let \( u \in \nT \). Then \( u \ne 0 \), since \( \abs{0} = 0 \ne 1 \) (@thm-conjugate-properties (e)). By @thm-conjugate-properties (c), \( u \conj{u} = \abs{u}^2 = 1 \), so \( \conj{u} \) satisfies the defining equation of \( u^{-1} \). Since \( \nC \) is a field (@thm-complex-numbers-field), inverses are unique (@fd3:lem-field-fraction-rules (a)), and \( u^{-1} = \conj{u} \). Finally \( \abs{\conj{u}} = \abs{u} = 1 \) by @thm-conjugate-properties (d).

(b) *Existence.* Let \( r \coloneqq \abs{z} \). Then \( r \ge 0 \), and \( r \ne 0 \) because \( z \ne 0 \) (@thm-conjugate-properties (e)); so \( r > 0 \), and its inverse \( r^{-1} \) is a positive real number (@fd3:prp-reciprocal-order (a)). By @thm-complex-numbers-field the inverse of \( r \) in \( \nC \) is this real number, so \( u \coloneqq z / \abs{z} = r^{-1} z \) is defined, and \( z = r u \). By @thm-conjugate-properties (d) and @prp-modulus-of-real, \( \abs{u} = \abs{r^{-1}} \abs{z} = r^{-1} r = 1 \), where \( \abs{r^{-1}} = r^{-1} \) because the absolute value of a positive real number is the number itself (@fd3:def-absolute-value-ordered-field). So \( u \in \nT \).

*Uniqueness.* Let \( z = r u \) with \( r > 0 \) and \( u \in \nT \). Taking moduli, \( \abs{z} = \abs{r} \abs{u} = r \cdot 1 = r \), again by @thm-conjugate-properties (d) and @prp-modulus-of-real. Then \( u = r^{-1} z = z / \abs{z} \). So the pair is the one named in the statement.

(c) Since inverses are unique, \( 1/z = \conj{z} \) holds if and only if \( z \conj{z} = 1 \), that is, by @thm-conjugate-properties (c), if and only if \( \abs{z}^2 = 1 = 1^2 \). Both \( \abs{z} \) and \( 1 \) are non-negative, so by @fd3:prp-ordered-ring-rules (g) neither can be strictly smaller than the other, and \( \abs{z}^2 = 1 \) holds if and only if \( \abs{z} = 1 \).
:::

Part (b) is the picture we wanted: \( z = \abs{z} \cdot u \), a length times a direction, and both factors are forced. Part (a) says that the directions are closed under multiplication and inversion and contain \( 1 \); Chapter 3 calls a set with these properties, under an associative product, a group, and \( \nT \) is one of its first examples. Part (c) is a practical test: on the unit circle, and only there, dividing by \( z \) is the same as conjugating.

::: {.check}
Write \( z = 3 + 4i \) as \( r u \) with \( r > 0 \) and \( u \in \nT \). What is \( 1/u \)?
:::

::: {.solution}
By @prp-unit-circle (b), \( r = \abs{3 + 4i} = 5 \) and \( u = \tfrac35 + \tfrac45 i \). By (a), \( 1/u = \conj{u} = \tfrac35 - \tfrac45 i \). Check: \( \big(\tfrac35 + \tfrac45 i\big)\big(\tfrac35 - \tfrac45 i\big) = \tfrac{9}{25} + \tfrac{16}{25} = 1 \).
:::

So far a direction is a point \( u \) of \( \nT \), and multiplying two directions gives a third. What we cannot yet say is **how much** a direction turns the plane. For that we need to measure positions on the circle by a real number, an angle, so that multiplying directions adds angles. That is a job for cosine and sine.

## What this volume borrows about cosine and sine

An angle should be a real number \( \theta \) that walks around the circle: a point \( (\cos\theta, \sin\theta) \) on \( \nT \), moving as \( \theta \) moves, returning to its start after a full turn of length \( 2\pi \). Defining such functions needs limits of functions, by power series or by integrals. This volume develops no limits of functions, so it does not define cosine and sine. *Analysis on the Real Line*, Chapter 10 does: there \( \cos \) and \( \sin \) are defined by power series, \( \pi \) is defined as twice the least positive zero of \( \cos \), and the facts below are proved. Its \( \nR \) is a complete ordered field, so by @fd3:thm-cof-uniqueness it is our \( \nR \), up to the one order-preserving field isomorphism; the functions and the number carry over along it.

We write \( 2\pi\nZ \coloneqq \{ 2\pi k : k \in \nZ \} \), the integer multiples of \( 2\pi \) in \( \nR \).

::: {#ax-cosine-sine}
[What This Volume Borrows about Cosine and Sine]

There are functions \( \cos, \sin \colon \nR \to \nR \) and a real number \( \pi > 0 \) with the following properties. They are **assumed here and proved in *Analysis on the Real Line*, Chapter 10**.

::: {.enumerate options="label=(T\arabic*)"}
1. \( \cos^2\theta + \sin^2\theta = 1 \) for every \( \theta \in \nR \).
2. For all \( \theta, \varphi \in \nR \),
\[
\begin{aligned}
\cos(\theta + \varphi) &= \cos\theta \cos\varphi - \sin\theta \sin\varphi , \\
\sin(\theta + \varphi) &= \sin\theta \cos\varphi + \cos\theta \sin\varphi .
\end{aligned}
\]
3. For \( \theta \in \nR \): \( \cos\theta = 1 \) if and only if \( \theta \in 2\pi\nZ \).
4. For every \( (x, y) \in \nR^2 \) with \( x^2 + y^2 = 1 \) there is \( \theta \in \nR \) with \( \cos\theta = x \) and \( \sin\theta = y \).
5. \( \sin\theta > 0 \) whenever \( 0 < \theta < \pi \).
:::
:::

In words: (T1) puts the point \( (\cos\theta, \sin\theta) \) on the unit circle; (T2) is the pair of addition formulas; (T3) says that the cosine reaches \( 1 \) exactly at the multiples of a full turn; (T4) says that every point of the circle is reached; (T5) says that during the first half turn the point stays in the upper half plane.

This box is where the chapter borrows. Like @fd1:ax-induction, which *Logic and Proof* assumed and *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 1 proved, it is a statement assumed in one volume and proved in another. Nothing in Sections 1.1–1.4, and nothing in this section above the box, uses it. From here on we use these five facts about \( \cos \), \( \sin \) and \( \pi \) and **no others**: no value such as \( \cos(\pi/3) = \tfrac12 \), no periodicity, no picture of a graph. Whatever else we need, we derive, and each proof that uses one of the facts names it by its number. Two consequences come at once.

- \( \cos 0 = 1 \), by (T3), since \( 0 = 2\pi \cdot 0 \in 2\pi\nZ \). Then (T1) gives \( \sin^2 0 = 1 - 1 = 0 \), so \( \sin 0 = 0 \), because a non-zero real number has a positive square (@fd3:prp-ordered-ring-rules (e)).
- \( \cos(2\pi k) = 1 \) and \( \sin(2\pi k) = 0 \) for every \( k \in \nZ \), by (T3) and then (T1) in the same way.

::: {.warning}
The five facts are about \( \cos \), \( \sin \) and \( \pi \) only. A school fact such as \( \sin(\pi/6) = \tfrac12 \) is not among them, and a proof in this volume may not quote it: @exm-special-angles below derives the few values we use. Nor do the facts say that \( \cos \) and \( \sin \) are "periodic with period \( 2\pi \)" as functions; that is true, and derivable from (T2) and (T3), but no proof here needs it.
:::

## Polar form

With angles available, we can name the point of \( \nT \) at angle \( \theta \).

*\( e^{i\theta} \) is the point of the unit circle at angle \( \theta \).*

::: {#def-polar-form}
[Polar Form]

For \( \theta \in \nR \) we write
\[
e^{i\theta} \coloneqq \cos\theta + i \sin\theta .
\]
Let \( z \in \nC \) with \( z \ne 0 \). A **polar form** of \( z \) is an expression \( z = r e^{i\theta} \) with \( r \in \nR \), \( r > 0 \), and \( \theta \in \nR \). Then \( \theta \) is **an** argument of \( z \).
:::

In words: the first line is an abbreviation, not an exponential. This volume has no exponential function, the letter \( e \) on its own means nothing here, and the only rule of exponents we will use for \( e^{i\theta} \) is the one proved below (@thm-polar-multiplication (a)). *Analysis on the Real Line*, Chapter 10 shows that \( e^{i\theta} \) is indeed the value of the complex exponential function at \( i\theta \); the notation anticipates that, and the linear algebra volumes write their roots of unity with it. The exponent may be written in any form equal to \( i\theta \) with \( \theta \) real, and the symbol then means \( e^{i\theta} \): for example \( e^{-i\theta} = e^{i(-\theta)} \), \( e^{2\pi i} = e^{i \cdot 2\pi} \), \( e^{in\theta} = e^{i(n\theta)} \) and \( e^{-2\pi i} = e^{i(-2\pi)} \). This is unambiguous, because the real number \( \theta \) is determined by \( i\theta \) (it is its imaginary part). The second part asks for a **positive** real \( r \) and allows **any** real \( \theta \).

The point \( e^{i\theta} \) lies on \( \nT \). Indeed \( \abs{e^{i\theta}} = \sqrt{\cos^2\theta + \sin^2\theta} = \sqrt 1 = 1 \), by @def-conjugate-modulus and (T1). So \( r e^{i\theta} \) is a length \( r \) times a direction, as in @prp-unit-circle (b), and that proposition gives \( r = \abs{z} \) for every polar form of \( z \).

**Examples.**

- \( e^{i0} = \cos 0 + i \sin 0 = 1 \), by the consequences of the box. So \( 1 = 1 \cdot e^{i0} \) and \( 5 = 5 e^{i0} \) are polar forms.
- \( e^{2\pi i} = \cos 2\pi + i \sin 2\pi = 1 \), by the second consequence with \( k = 1 \). So \( 1 = 1 \cdot e^{2\pi i} \) as well: \( 0 \) and \( 2\pi \) are both arguments of \( 1 \), and they differ, since \( \pi > 0 \).
- The number \( 0 \) has no polar form, since \( \abs{r e^{i\theta}} = r > 0 \).

**A non-example by minimal change.** Allow \( r < 0 \): then \( -1 = (-1) \cdot e^{i0} \) looks like a polar form of \( -1 \) with argument \( 0 \). The clause that fails is \( r > 0 \), and it matters: with negative \( r \) allowed, the length could no longer be read off as \( \abs{z} \), and \( 1 = 1 \cdot e^{i0} \) and \( -1 = (-1) e^{i0} \) would share the argument \( 0 \). We will see in @exm-special-angles that \( -1 = 1 \cdot e^{i\pi} \) is a genuine polar form.

The examples already show why the definition says **an** argument: \( 1 = e^{i0} = e^{2\pi i} \). How much freedom there is, exactly, is part (b) of @prp-polar-form below. First, the reason for the notation: these numbers multiply the way exponentials do.

::: {#thm-polar-multiplication}
[Multiplication in Polar Form]

::: {.enumerate options="label=(\alph*)"}
1. \( e^{i\theta} e^{i\varphi} = e^{i(\theta + \varphi)} \) for all \( \theta, \varphi \in \nR \).
2. \( e^{i0} = 1 \), and \( (e^{i\theta})^{-1} = e^{-i\theta} = \conj{e^{i\theta}} \) for every \( \theta \in \nR \).
3. If \( r, s \in \nR \) with \( r, s > 0 \) and \( \theta, \varphi \in \nR \), then \( (r e^{i\theta})(s e^{i\varphi}) = rs \, e^{i(\theta + \varphi)} \), and this is a polar form of the product.
:::
:::

::: {.idea}
Multiply out \( (\cos\theta + i\sin\theta)(\cos\varphi + i\sin\varphi) \) with the rule of @def-complex-numbers: the real and imaginary parts that appear are exactly the right-hand sides of the addition formulas (T2). The rest is bookkeeping with inverses and moduli.
:::

::: {.proof}
(a) By the multiplication rule of @def-complex-numbers,
\[
\begin{aligned}
e^{i\theta} e^{i\varphi}
&= (\cos\theta\cos\varphi - \sin\theta\sin\varphi) + (\cos\theta\sin\varphi + \sin\theta\cos\varphi) i \\
&= \cos(\theta + \varphi) + i \sin(\theta + \varphi) ,
\end{aligned}
\]
where the second equality is (T2), with the two products in the imaginary part reordered by commutativity in \( \nR \). The right-hand side is \( e^{i(\theta + \varphi)} \).

(b) \( e^{i0} = 1 \) was shown in the first example above. By (a) with \( \varphi = -\theta \), \( e^{i\theta} e^{-i\theta} = e^{i0} = 1 \), so \( e^{-i\theta} \) is the inverse of \( e^{i\theta} \), by uniqueness of inverses in the field \( \nC \) (@thm-complex-numbers-field, @fd3:lem-field-fraction-rules (a)). Since \( e^{i\theta} \in \nT \), its inverse is also its conjugate (@prp-unit-circle (a)).

(c) By @prp-complex-arithmetic-laws (commutativity and associativity of \( \cdot \)), \( (r e^{i\theta})(s e^{i\varphi}) = (rs)(e^{i\theta} e^{i\varphi}) \), and (a) turns this into \( rs \, e^{i(\theta + \varphi)} \). Here \( rs > 0 \) by @fd3:prp-ordered-ring-rules (c) (multiply \( 0 < r \) by \( s > 0 \)), so this is a polar form.
:::

In words: **to multiply two complex numbers, multiply their moduli and add their arguments**. This is the chapter's third named move, **multiply moduli, add angles**. Multiplying by a fixed \( w = s e^{i\varphi} \) therefore turns the plane about \( 0 \) by the angle \( \varphi \) and stretches it by the factor \( s \). The picture shows \( z \), \( w \) and \( zw \) for \( \abs{z} = 1.5 \), \( \abs{w} = 1.2 \), and arguments of \( 20^\circ \) and \( 50^\circ \) (a full turn being \( 360^\circ \), that is, \( 2\pi \)).

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=2]
    \draw[->] (-0.3,0) -- (2.2,0) node[right] {$\operatorname{Re}$};
    \draw[->] (0,-0.3) -- (0,2.1) node[above] {$\operatorname{Im}$};
    \draw[dashed] (1,0) arc (0:90:1);
    \draw[thick,->] (0,0) -- (20:1.5) node[right] {$z$};
    \draw[thick,->] (0,0) -- (50:1.2) node[below right] {$w$};
    \draw[very thick,->] (0,0) -- (70:1.8) node[above] {$zw$};
    \draw (0.55,0) arc (0:20:0.55);
    \node at (10:0.8) {\small $20^\circ$};
    \draw (20:1.3) arc (20:70:1.3);
    \node at (45:1.5) {\small $50^\circ$};
    \node[below] at (1,0) {\small $1$};
\end{tikzpicture}
\end{center}
```

The arrow for \( zw \) has length \( 1.5 \times 1.2 = 1.8 \) and makes the angle \( 20^\circ + 50^\circ = 70^\circ \) with the positive real axis: it is the arrow for \( z \), turned by the argument of \( w \) and stretched by the modulus of \( w \). The small arc marks the argument of \( z \), the large arc the extra turn by the argument of \( w \), and the dashed arc is part of the unit circle, where the numbers \( e^{i\theta} \) live.

Now the freedom in the argument. Every non-zero number has a polar form, and its arguments are determined up to a whole number of full turns.

::: {#prp-polar-form}
[Existence and Uniqueness of Polar Form]

::: {.enumerate options="label=(\alph*)"}
1. Every \( z \in \nC \) with \( z \ne 0 \) has a polar form, and every polar form \( z = r e^{i\theta} \) has \( r = \abs{z} \).
2. For \( r, s \in \nR \) with \( r, s > 0 \) and \( \theta, \varphi \in \nR \),
\[
r e^{i\theta} = s e^{i\varphi} \iff r = s \text{ and } \theta - \varphi \in 2\pi\nZ .
\]
:::
:::

::: {.proof}
(a) By @prp-unit-circle (b), \( z = \abs{z} \cdot u \) with \( u = x + yi \in \nT \), so \( x^2 + y^2 = 1 \). By (T4) there is \( \theta \in \nR \) with \( \cos\theta = x \) and \( \sin\theta = y \), that is, \( u = e^{i\theta} \). Hence \( z = \abs{z} e^{i\theta} \), with \( \abs{z} > 0 \). Conversely, if \( z = r e^{i\theta} \) is a polar form, then \( e^{i\theta} \in \nT \), and the uniqueness in @prp-unit-circle (b) gives \( r = \abs{z} \).

(b) Suppose first that \( r e^{i\theta} = s e^{i\varphi} \). The number \( r e^{i\theta} \) is non-zero: \( r \ne 0 \), \( e^{i\theta} \in \nT \) is non-zero (@prp-unit-circle (a)), and a product of non-zero elements of the field \( \nC \) is non-zero (@thm-complex-numbers-field, @fd3:lem-field-fraction-rules (d)). So both sides are polar forms of the same non-zero number, and \( r = s \) by (a). Multiplying by \( r^{-1} \) gives \( e^{i\theta} = e^{i\varphi} \). In the other direction, if \( r = s \), the two sides are equal exactly when \( e^{i\theta} = e^{i\varphi} \). So it remains to show that \( e^{i\theta} = e^{i\varphi} \) if and only if \( \theta - \varphi \in 2\pi\nZ \).

Multiplying by \( e^{-i\varphi} \), and back by \( e^{i\varphi} \), shows that \( e^{i\theta} = e^{i\varphi} \) holds if and only if \( e^{i\theta} e^{-i\varphi} = e^{i\varphi} e^{-i\varphi} \), that is, by @thm-polar-multiplication (a) and (b), if and only if \( e^{i(\theta - \varphi)} = 1 \). Comparing real and imaginary parts, this says \( \cos(\theta - \varphi) = 1 \) and \( \sin(\theta - \varphi) = 0 \). The second condition follows from the first: by (T1), \( \cos(\theta - \varphi) = 1 \) gives \( \sin^2(\theta - \varphi) = 0 \), hence \( \sin(\theta - \varphi) = 0 \) (@fd3:prp-ordered-ring-rules (e)). So \( e^{i\theta} = e^{i\varphi} \) if and only if \( \cos(\theta - \varphi) = 1 \), and by (T3) that holds if and only if \( \theta - \varphi \in 2\pi\nZ \).
:::

Existence came from (T4), and uniqueness from (T3), with (T1) helping and (T2) entering through @thm-polar-multiplication. "Comparing arguments" therefore always means comparing them up to a multiple of \( 2\pi \), and the next warning is the trap this sets.

::: {.warning}
From \( e^{i\theta} = e^{i\varphi} \) one may **not** conclude \( \theta = \varphi \): \( e^{i0} = e^{2\pi i} = 1 \), and \( 0 \ne 2\pi \). Only \( \theta - \varphi \in 2\pi\nZ \) follows (@prp-polar-form (b)). Forgetting this loses solutions as soon as an equation is solved for an angle; Section 1.6 meets an equation where it would lose all but one of them.
:::

## Powers

Repeating @thm-polar-multiplication gives powers. The powers \( z^n \) are those of the recursion \( z^0 = 1 \), \( z^{n+1} = z^n z \) (@prp-power-laws-commutative-ring).

::: {#thm-de-moivre}
[De Moivre's Formula]

For every \( \theta \in \nR \) and every \( n \in \nN \),
\[
\bigl(e^{i\theta}\bigr)^n = e^{in\theta} , \quad \text{that is,} \quad (\cos\theta + i\sin\theta)^n = \cos n\theta + i \sin n\theta .
\]
Consequently \( (r e^{i\theta})^n = r^n e^{in\theta} \) for every real \( r > 0 \), and this is a polar form.
:::

::: {.idea}
A power is a repeated product, and each new factor \( e^{i\theta} \) adds \( \theta \) to the argument, by @thm-polar-multiplication (a). So induction on \( n \), along the recursion \( z^{n+1} = z^n z \).
:::

::: {.proof}
We use @fd1:ax-induction on \( n \), read on \( \nN = \omega \) through @fd3:cor-omega-identification (b); here \( n\theta \) is the product in \( \nR \) of \( n \cdot 1_{\nR} \) and \( \theta \) (@fd3:def-naturals-in-ordered-field (a)). For \( n = 0 \), the left side is \( (e^{i\theta})^0 = 1 \) by the recursion, and the right side is \( e^{i0} = 1 \) by @thm-polar-multiplication (b). Suppose \( (e^{i\theta})^n = e^{in\theta} \) for some \( n \in \nN \). Then
\[
\bigl(e^{i\theta}\bigr)^{n+1} = \bigl(e^{i\theta}\bigr)^n e^{i\theta} = e^{in\theta} e^{i\theta} = e^{i(n\theta + \theta)} = e^{i(n+1)\theta} ,
\]
by the recursion, the induction hypothesis, @thm-polar-multiplication (a), and \( (n + 1) \cdot 1_{\nR} = n \cdot 1_{\nR} + 1_{\nR} \) (@fd3:def-naturals-in-ordered-field (a)) with distributivity in \( \nR \). This proves the formula for every \( n \in \nN \).

For the consequence, @prp-power-laws-commutative-ring (c) gives \( (r e^{i\theta})^n = r^n (e^{i\theta})^n = r^n e^{in\theta} \). The power \( r^n \) is the same whether it is computed in \( \nR \) or in \( \nC \), by the remark after @prp-power-laws-commutative-ring in Section 1.1, and \( r^n > 0 \) because a product of positive reals is positive (@fd3:prp-ordered-ring-rules (c); induction on \( n \), with \( r^0 = 1 > 0 \)).
:::

For a negative exponent, Exercise C1 below defines \( z^{-n} \) locally and proves the matching formula; nothing in the text uses it.

The five borrowed facts give no particular value of \( \cos \) or \( \sin \) except at multiples of \( 2\pi \). Every other value this chapter uses is derived next, from (T1)–(T5) and the algebra of Sections 1.1–1.4.

::: {#exm-special-angles}
[Special Angles]

Show, using only (T1)–(T5) and the results proved so far, that
\[
\begin{aligned}
&e^{i\pi} = -1, \qquad e^{i\pi/2} = i, \qquad e^{i\pi/3} = \tfrac12 + \tfrac{\sqrt 3}{2} i, \\
&e^{i\pi/6} = \tfrac{\sqrt 3}{2} + \tfrac12 i, \qquad e^{i\pi/4} = \tfrac{1}{\sqrt 2} + \tfrac{1}{\sqrt 2} i .
\end{aligned}
\]
:::

::: {.solution}
Each value is found the same way: a power of the unknown point is a point we already know, and (T5) chooses between the candidates. Since \( \pi > 0 \), each of \( \pi/2 \), \( \pi/3 \), \( \pi/4 \), \( \pi/6 \) lies strictly between \( 0 \) and \( \pi \), so (T5) gives \( \operatorname{Im} e^{i\theta} = \sin\theta > 0 \) for each of them.

(i) *\( e^{i\pi} = -1 \).* Let \( u \coloneqq e^{i\pi} \). By @thm-de-moivre, \( u^2 = e^{2\pi i} = 1 \), so \( (u - 1)(u + 1) = u^2 - 1 = 0 \), and since \( \nC \) has no zero divisors (@thm-complex-numbers-field, @fd3:lem-field-fraction-rules (d)), \( u = 1 \) or \( u = -1 \). Suppose \( u = 1 \). Then \( \cos\pi = 1 \), so \( \pi = 2\pi k \) for some \( k \in \nZ \) by (T3); dividing by \( \pi \ne 0 \) gives \( 1 = 2k \) in \( \nR \), an equation between images of integers. The embedding of \( \nZ \) into \( \nR \), through \( \nQ \) (@fd3:prp-integers-embed-rationals) and \( \kappa \) (@fd3:thm-reals-complete-ordered-field), is injective and preserves \( + \) and \( \cdot \), so \( 1 = 2k \) holds in \( \nZ \). But \( 1 = 2 \cdot 0 + 1 \) is odd, and an odd integer is not of the form \( 2k \) (@fd3:cor-integers-even-odd (a)). So \( u \ne 1 \), and \( e^{i\pi} = -1 \).

(ii) *\( e^{i\pi/2} = i \).* Let \( u \coloneqq e^{i\pi/2} \). By @thm-polar-multiplication (a), \( u^2 = e^{i\pi} = -1 = i^2 \), so \( (u - i)(u + i) = 0 \) and \( u = \pm i \). Since \( \operatorname{Im} u > 0 \) and \( \operatorname{Im}(-i) = -1 < 0 \), \( u = i \).

(iii) *\( e^{i\pi/3} = \tfrac12 + \tfrac{\sqrt 3}{2} i \).* Let \( u \coloneqq e^{i\pi/3} \). By @thm-de-moivre, \( u^3 = e^{i\pi} = -1 \). Multiplying out shows \( (u + 1)(u^2 - u + 1) = u^3 + 1 = 0 \). Now \( u \ne -1 \), since \( \operatorname{Im} u > 0 \); so \( u^2 - u + 1 = 0 \). By @cor-complex-quadratic-formula with \( a = 1 \), \( b = -1 \), \( c = 1 \), and \( d \coloneqq \sqrt 3\, i \), a square root of \( b^2 - 4ac = -3 \) (indeed \( (\sqrt 3\, i)^2 = 3 i^2 = -3 \)),
\[
u = \frac{1 + \sqrt 3\, i}{2} \quad \text{or} \quad u = \frac{1 - \sqrt 3\, i}{2} .
\]
Since \( \operatorname{Im} u > 0 \), \( u = \tfrac12 + \tfrac{\sqrt 3}{2} i \).

(iv) *\( e^{i\pi/6} = \tfrac{\sqrt 3}{2} + \tfrac12 i \).* Since \( \pi/6 = \pi/2 + (-\pi/3) \), @thm-polar-multiplication (a) and (b) give
\[
e^{i\pi/6} = e^{i\pi/2} e^{-i\pi/3} = i \cdot \conj{e^{i\pi/3}} = i \Bigl( \frac12 - \frac{\sqrt 3}{2} i \Bigr) = \frac{\sqrt 3}{2} + \frac12 i ,
\]
by (ii) and (iii).

(v) *\( e^{i\pi/4} = \tfrac{1}{\sqrt 2} + \tfrac{1}{\sqrt 2} i \).* Let \( u \coloneqq e^{i\pi/4} \). By @thm-polar-multiplication (a) and (ii), \( u^2 = e^{i\pi/2} = i \). The formula of @prp-complex-square-roots for \( z = i \) (so \( a = 0 \), \( b = 1 \), \( r = \abs{i} = 1 \)) gives the square root \( w = \sqrt{1/2} + \sqrt{1/2}\, i \), and \( \sqrt{1/2} = 1/\sqrt 2 \), since both are non-negative and square to \( \tfrac12 \). By @prp-complex-square-roots (b), \( u = w \) or \( u = -w \), and \( \operatorname{Im} u > 0 \) rules out \( -w \). So \( u = w \).

Comparing real and imaginary parts turns these into values of \( \cos \) and \( \sin \):

| \( \theta \) | \( 0 \) | \( \pi/6 \) | \( \pi/4 \) | \( \pi/3 \) | \( \pi/2 \) | \( \pi \) |
|---|---|---|---|---|---|---|
| \( \cos\theta \) | \( 1 \) | \( \sqrt 3/2 \) | \( 1/\sqrt 2 \) | \( 1/2 \) | \( 0 \) | \( -1 \) |
| \( \sin\theta \) | \( 0 \) | \( 1/2 \) | \( 1/\sqrt 2 \) | \( \sqrt 3/2 \) | \( 1 \) | \( 0 \) |

These are the familiar values, now proved from the five facts.
:::

Two special cases of the rotation picture are worth isolating. Multiplying by \( i = e^{i\pi/2} \) turns the plane by a quarter turn, counterclockwise; two quarter turns make a half turn, and this is the picture behind \( i^2 = -1 = e^{i\pi} \). And multiplying by \( e^{-i\theta} = \conj{e^{i\theta}} \) undoes the turn by \( \theta \) (@thm-polar-multiplication (b)).

Powers that are tedious to expand become one line in polar form.

::: {#exm-polar-power}
[A Power via Polar Form]

Compute \( (\sqrt 3 + i)^6 \).
:::

::: {.solution}
We have \( \sqrt 3 + i = 2 \bigl( \tfrac{\sqrt 3}{2} + \tfrac12 i \bigr) = 2 e^{i\pi/6} \), by @exm-special-angles (iv). By @thm-de-moivre and @exm-special-angles (i),
\[
(\sqrt 3 + i)^6 = 2^6 e^{i \cdot 6\pi/6} = 64 \, e^{i\pi} = -64 .
\]
By hand: \( (\sqrt 3 + i)^2 = 3 + 2\sqrt 3\, i - 1 = 2 + 2\sqrt 3\, i = 2(1 + \sqrt 3\, i) \), and \( (1 + \sqrt 3\, i)^3 = (1 + \sqrt 3\, i)(-2 + 2\sqrt 3\, i) = -2 - 6 = -8 \), so \( (\sqrt 3 + i)^6 = \bigl(2(1 + \sqrt 3\, i)\bigr)^3 = 8 \cdot (-8) = -64 \) (@prp-power-laws-commutative-ring (b), (c)), the same answer.
:::

::: {.check}
Use polar form to compute \( (1 + i)^8 \), and check the answer with \( (1 + i)^2 = 2i \).
:::

::: {.solution}
By @exm-special-angles (v), \( 1 + i = \sqrt 2 \bigl( \tfrac{1}{\sqrt 2} + \tfrac{1}{\sqrt 2} i \bigr) = \sqrt 2 \, e^{i\pi/4} \). By @thm-de-moivre, \( (1 + i)^8 = (\sqrt 2)^8 e^{i \cdot 8\pi/4} = 16 \, e^{2\pi i} = 16 \), since \( (\sqrt 2)^8 = \bigl((\sqrt 2)^2\bigr)^4 = 2^4 = 16 \) and \( e^{2\pi i} = 1 \). Check: \( (1 + i)^8 = \bigl((1 + i)^2\bigr)^4 = (2i)^4 = 16 i^4 = 16 \), by @prp-power-laws-commutative-ring (b), (c).
:::

## Exercises

### A. Check your understanding

::: {#exr-polar-form-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Give a polar form of \( -2 \) and of \( 3i \).
2. True or false: if \( e^{i\theta} = e^{i\varphi} \), then \( \theta = \varphi \). Justify your answer.
3. In @prp-polar-form, which of the borrowed facts (T1)–(T5) gives the existence of a polar form, and which gives the uniqueness of the argument up to \( 2\pi\nZ \)?
4. Which results of Sections 1.1–1.5 use none of the borrowed facts? Is @prp-unit-circle among them?
:::
:::

::: {.solution}
(a) \( -2 = 2 e^{i\pi} \) and \( 3i = 3 e^{i\pi/2} \), by @exm-special-angles (i) and (ii); the moduli \( 2 \) and \( 3 \) are positive, as a polar form requires. (Any \( \pi + 2\pi k \), respectively \( \pi/2 + 2\pi k \), with \( k \in \nZ \), is also an argument, by @prp-polar-form (b).)

(b) False. \( e^{i0} = 1 = e^{2\pi i} \), but \( 0 \ne 2\pi \) since \( \pi > 0 \). What is true is \( \theta - \varphi \in 2\pi\nZ \) (@prp-polar-form (b)).

(c) Existence: (T4), which provides an angle for the point \( z/\abs{z} \) of \( \nT \). Uniqueness: (T3), which turns \( \cos(\theta - \varphi) = 1 \) into \( \theta - \varphi \in 2\pi\nZ \); (T1) is used alongside it, to see that \( \sin(\theta - \varphi) = 0 \) follows from \( \cos(\theta - \varphi) = 1 \), and (T2) enters through @thm-polar-multiplication, which turns \( e^{i\theta} = e^{i\varphi} \) into \( e^{i(\theta - \varphi)} = 1 \).

(d) Everything in Sections 1.1–1.4, and the part of this section before @ax-cosine-sine; after the box, only Exercise C2, which is set up to avoid them. In particular @prp-unit-circle uses none of them: its proof uses only the modulus rules of Section 1.2, the field properties of \( \nC \), and order facts about \( \nR \) from *Number Systems: From \(\nN\) to \(\nR\)*.
:::

### B. Practice

::: {#exr-polar-form-b1}
[B1]

Compute \( (1 - \sqrt 3\, i)^6 \).
:::

::: {.solution}
We have \( 1 - \sqrt 3\, i = 2 \bigl( \tfrac12 - \tfrac{\sqrt 3}{2} i \bigr) = 2 \, \conj{e^{i\pi/3}} = 2 e^{-i\pi/3} \), by @exm-special-angles (iii) and @thm-polar-multiplication (b). By @thm-de-moivre,
\[
(1 - \sqrt 3\, i)^6 = 2^6 e^{-6i\pi/3} = 64 \, e^{-2\pi i} = 64 ,
\]
since \( -2\pi = 2\pi \cdot (-1) \in 2\pi\nZ \), so \( \cos(-2\pi) = 1 \) and \( \sin(-2\pi) = 0 \) by (T3) and (T1), and \( e^{-2\pi i} = 1 \).
:::

::: {#exr-polar-form-b2}
[B2: Symmetries of Cosine and Sine]

Prove that for every \( \theta \in \nR \):
\[
\begin{aligned}
&\cos(-\theta) = \cos\theta, \quad \sin(-\theta) = -\sin\theta, \quad \cos(\theta + \pi) = -\cos\theta, \\
&\sin(\theta + \pi) = -\sin\theta, \quad \cos\theta = \sin(\theta + \pi/2) .
\end{aligned}
\]

*Hint: write each left side as a part of some \( e^{i\psi} \), and compute that \( e^{i\psi} \) with @thm-polar-multiplication.*
:::

::: {.solution}
By @thm-polar-multiplication (b), \( e^{-i\theta} = \conj{e^{i\theta}} \), that is, \( \cos(-\theta) + i \sin(-\theta) = \cos\theta - i \sin\theta \). Comparing real and imaginary parts gives \( \cos(-\theta) = \cos\theta \) and \( \sin(-\theta) = -\sin\theta \).

By @thm-polar-multiplication (a) and @exm-special-angles (i), \( e^{i(\theta + \pi)} = e^{i\theta} e^{i\pi} = -e^{i\theta} \), that is, \( \cos(\theta + \pi) + i \sin(\theta + \pi) = -\cos\theta - i \sin\theta \). Comparing parts gives the next two identities.

By @thm-polar-multiplication (a) and @exm-special-angles (ii), \( e^{i(\theta + \pi/2)} = i e^{i\theta} = i\cos\theta - \sin\theta \). Comparing imaginary parts gives \( \sin(\theta + \pi/2) = \cos\theta \). (Comparing real parts gives, in addition, \( \cos(\theta + \pi/2) = -\sin\theta \).)
:::

::: {#exr-polar-form-b3}
[B3]

Let \( \theta \in \nR \). Show that \( \abs{e^{i\theta} - 1}^2 = 2 - 2\cos\theta \). Hence show again that \( e^{i\theta} = 1 \) if and only if \( \cos\theta = 1 \).
:::

::: {.solution}
Let \( u \coloneqq e^{i\theta} \), so \( u \conj{u} = \abs{u}^2 = 1 \). Squaring the modulus, by @thm-conjugate-properties (a)–(c),
\[
\abs{u - 1}^2 = (u - 1)\conj{(u - 1)} = (u - 1)(\conj{u} - 1) = u\conj{u} - (u + \conj{u}) + 1 = 2 - 2 \operatorname{Re} u ,
\]
and \( \operatorname{Re} u = \cos\theta \). Hence \( \abs{u - 1}^2 = 2 - 2\cos\theta \).

Now \( u = 1 \) if and only if \( \abs{u - 1} = 0 \) (@thm-conjugate-properties (e)), if and only if \( \abs{u - 1}^2 = 0 \) (a real number is \( 0 \) exactly when its square is: \( 0^2 = 0 \) by @fd3:prp-ring-algebra (b), and a non-zero square is positive by @fd3:prp-ordered-ring-rules (e)), if and only if \( 2 - 2\cos\theta = 0 \), that is, \( \cos\theta = 1 \).
:::

### C. Going deeper

::: {#exr-polar-form-c1}
[C1: Triple Angles and Negative Powers]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \cos 3\theta = 4\cos^3\theta - 3\cos\theta \) and \( \sin 3\theta = 3\sin\theta - 4\sin^3\theta \) for every \( \theta \in \nR \).
2. For \( z \in \nC \) with \( z \ne 0 \) and \( n \in \nN \), put \( z^{-n} \coloneqq (z^{-1})^n \) (a definition local to this exercise). Show that \( (e^{i\theta})^{-n} = e^{-in\theta} \).
:::
:::

::: {.solution}
(a) Write \( c \coloneqq \cos\theta \) and \( s \coloneqq \sin\theta \). By @thm-de-moivre, \( \cos 3\theta + i \sin 3\theta = (c + is)^3 \). Now \( (c + is)^2 = (c^2 - s^2) + 2cs\, i \), and
\[
\begin{aligned}
(c + is)^3 &= \bigl((c^2 - s^2) + 2cs\, i\bigr)(c + is) \\
&= (c^3 - 3cs^2) + (3c^2 s - s^3) i .
\end{aligned}
\]
Comparing real parts and using \( s^2 = 1 - c^2 \) (T1), \( \cos 3\theta = c^3 - 3c(1 - c^2) = 4c^3 - 3c \). Comparing imaginary parts and using \( c^2 = 1 - s^2 \), \( \sin 3\theta = 3(1 - s^2)s - s^3 = 3s - 4s^3 \).

(b) By @thm-polar-multiplication (b), \( (e^{i\theta})^{-1} = e^{-i\theta} = e^{i(-\theta)} \). By @thm-de-moivre applied to \( -\theta \), \( (e^{i\theta})^{-n} = (e^{i(-\theta)})^n = e^{in(-\theta)} = e^{-in\theta} \).

Nothing in this chapter uses negative powers of complex numbers; the definition in (b) is for practice only.
:::

::: {#exr-polar-form-c2}
[C2: Points on the Circle without Angles]

For \( t \in \nR \) put
\[
u_t \coloneqq \frac{1 + it}{1 - it} .
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( u_t \) is defined, that \( u_t \in \nT \), and that \( u_t \ne -1 \).
2. Show that every \( u \in \nT \) with \( u \ne -1 \) equals \( u_t \) for **exactly one** \( t \in \nR \), namely \( t = \operatorname{Im} u / (1 + \operatorname{Re} u) \).
3. Compute \( u_{1/2} \) in the form \( a + bi \).
:::

Use none of the borrowed facts (T1)–(T5).
:::

::: {.solution}
[Hint 1]

For (b), on the unit circle the conjugate is the inverse: \( \conj{u} = 1/u \).
:::

::: {.solution}
[Hint 2]

Clearing the denominator, \( u = u_t \) is equivalent to \( u - 1 = it(u + 1) \), and \( u + 1 \ne 0 \), so \( t \) is determined; it remains to show that \( (u - 1)/\bigl(i(u + 1)\bigr) \) is real.
:::

::: {.solution}
(a) The real part of \( 1 - it \) is \( 1 \), so \( 1 - it \ne 0 \) and the quotient is defined. The numbers \( 1 + it \) and \( 1 - it \) are conjugate, so they have the same modulus (@thm-conjugate-properties (d)), which is non-zero. From \( u_t (1 - it) = 1 + it \) and @thm-conjugate-properties (d), \( \abs{u_t} \abs{1 - it} = \abs{1 + it} = \abs{1 - it} \), and canceling the non-zero real number \( \abs{1 - it} \) gives \( \abs{u_t} = 1 \). If \( u_t = -1 \), then \( 1 + it = -(1 - it) = -1 + it \), so \( 1 = -1 \), which is false. So \( u_t \ne -1 \).

(b) Let \( u \in \nT \) with \( u \ne -1 \), and let \( t \in \nR \). Since \( 1 - it \ne 0 \), the equation \( u = u_t \) is equivalent to \( u(1 - it) = 1 + it \), that is, to
\[
u - 1 = it(u + 1) .
\]
Since \( i(u + 1) \ne 0 \), this holds if and only if \( t = t_0 \), where \( t_0 \coloneqq (u - 1)/\bigl(i(u + 1)\bigr) \in \nC \). So at most one real \( t \) has \( u_t = u \), and one does exactly when \( t_0 \) is real. Using \( u\conj{u} = 1 \),
\[
(u - 1)(\conj{u} + 1) = u\conj{u} + u - \conj{u} - 1 = u - \conj{u} = 2i \operatorname{Im} u ,
\]
where \( u - \conj{u} = 2i \operatorname{Im} u \) by @def-conjugate-modulus (with \( u = a + bi \), \( (a + bi) - (a - bi) = 2bi \)); and \( (u + 1)(\conj{u} + 1) = \abs{u + 1}^2 = 2 + 2\operatorname{Re} u \), by @thm-conjugate-properties (a), (c). This is a positive real number, since \( u + 1 \ne 0 \). Multiplying numerator and denominator of \( (u - 1)/(u + 1) \) by \( \conj{u} + 1 = \conj{u + 1} \ne 0 \),
\[
t_0 = \frac{1}{i} \cdot \frac{2i \operatorname{Im} u}{2 + 2\operatorname{Re} u} = \frac{\operatorname{Im} u}{1 + \operatorname{Re} u} ,
\]
a real number. So exactly one \( t \in \nR \) has \( u_t = u \), namely \( t_0 \).

(c) Multiplying numerator and denominator by the conjugate \( 1 + \tfrac12 i \) of the denominator,
\[
u_{1/2} = \frac{(1 + \tfrac12 i)^2}{1 + \tfrac14} = \frac{\tfrac34 + i}{\tfrac54} = \frac35 + \frac45 i .
\]
Check against (b): \( \operatorname{Im} u / (1 + \operatorname{Re} u) = \tfrac45 / \tfrac85 = \tfrac12 \).

So the map \( t \mapsto u_t \) is a bijection from \( \nR \) onto \( \nT \setminus \{-1\} \), and it was found with no angle. For rational \( t \), the point \( u_t \) has rational coordinates: the computation in (c) with \( t \) in place of \( \tfrac12 \) gives \( u_t = \bigl((1 - t^2) + 2t\, i\bigr)/(1 + t^2) \), and \( t = 1/2 \) gives the point \( (3/5, 4/5) \) behind the right triangle with sides \( 3 \), \( 4 \), \( 5 \).

**Marking scheme.** (10 points)
- 2: \( 1 - it \ne 0 \) with a reason, and \( \abs{u_t} = 1 \) from the equal moduli of conjugates.
- 1: \( u_t \ne -1 \).
- 2: \( u = u_t \) rewritten as a linear equation in \( t \), with \( u + 1 \ne 0 \) used to solve it uniquely.
- 3: shows that the unique solution is real and equals \( \operatorname{Im} u / (1 + \operatorname{Re} u) \), with \( 1 + \operatorname{Re} u \ne 0 \) justified (for example by multiplying by \( \conj{u + 1} \) and using \( u\conj{u} = 1 \), with \( 2 + 2 \operatorname{Re} u > 0 \)).
- Second route (coordinates \( u = x + yi \), \( x^2 + y^2 = 1 \)): the two lines above (5 points) become 2 for splitting \( u - 1 = it(u + 1) \) into \( x - 1 = -ty \) and \( y = t(1 + x) \), showing \( x \ne -1 \) (otherwise \( u = -1 \)) and so \( t = y/(1 + x) \) is forced; and 3 for checking that this \( t \) satisfies \( x - 1 = -ty \), using \( x^2 + y^2 = 1 \).
- 2: (c) computed and checked.
Fatal errors (0 for the step): writing \( u = e^{i\theta} \) and using a half-angle formula (borrowed facts, and values not derived here); dividing by \( 1 + \operatorname{Re} u \) without showing it is non-zero.
:::

<!-- dependency ledger
sec-polar-form (claim): the analysis volume (AN1.10) defines cos, sin by power series and pi as twice the least positive zero of cos, and proves (T1)-(T5) and e^{i theta} = exp(i theta) | AN1.10 (borrow, recorded in plan-edges b: [AN1.10]; prose pointer "Analysis on the Real Line, Chapter 10"); used only through ax-cosine-sine
sec-polar-form (claim): AN1.10's R is a complete ordered field, so cos, sin, pi transfer to F3.10's R along the unique order-preserving field isomorphism | fd3:thm-cof-uniqueness (cited); an1's axioms (prose)
sec-polar-form (claim): fd1's ax-induction is proved in Number Systems Chapter 1 | fd3:cor-omega-identification (b), fd3 thm-omega-induction (prose comparison; nothing depends on it)
sec-polar-form (claim): periodicity of cos and sin is derivable from (T2), (T3) | not proved here; marked so in the warning; nothing depends on it
ax-cosine-sine (claim): (T1)-(T5) assumed | AN1.10 (borrowed; proved there); users listed in the sec-polar-form borrow line at the end of this ledger
ax-cosine-sine (claim): cos 0 = 1, sin 0 = 0, cos(2 pi k) = 1, sin(2 pi k) = 0 | inline from (T3), (T1), fd3:prp-ordered-ring-rules (e)
prp-unit-circle (proof): the inverse of a positive real r in C is the real r^{-1} | thm-complex-numbers-field (cited: R closed under inverses)
prp-unit-circle (proof): |a| = a for a real a > 0 | fd3:def-absolute-value-ordered-field (cited)
prp-unit-circle (proof): r > 0 in R gives r^{-1} > 0 | fd3:prp-reciprocal-order (a) (cited)
def-polar-form (claim): e^{i theta} in T, via sqrt(cos^2 + sin^2) = sqrt 1 = 1 | (T1), def-conjugate-modulus (cited); sqrt 1 = 1 by uniqueness in fd3:prp-cof-square-roots
prp-polar-form (proof): r e^{i theta} is non-zero | prp-unit-circle (a), thm-complex-numbers-field, fd3:lem-field-fraction-rules (d) (cited)
exr-polar-form-c2 (solution): u - conj(u) = 2i Im u | def-conjugate-modulus (cited)
thm-polar-multiplication (proof): reordering sin theta cos phi + cos theta sin phi | commutativity of + and * in R (field axioms, fd3:thm-reals-complete-ordered-field)
thm-de-moivre (proof): r^n computed in R equals r^n computed in C | Section 1.1 remark after prp-power-laws-commutative-ring (cited)
thm-de-moivre (proof): r^n > 0 for r > 0 | inline (induction on n; fd3:prp-ordered-ring-rules (c))
thm-de-moivre (proof): n theta + theta = (n + 1) theta | fd3:def-naturals-in-ordered-field (a) and distributivity in R
exm-special-angles (solution): pi/2, pi/3, pi/4, pi/6 lie in (0, pi) since pi > 0; pi/6 = pi/2 - pi/3 | arithmetic in the ordered field R; verify/ch01/exm-special-angles.py
exm-special-angles (solution): pi = 2 pi k gives 1 = 2k in R, hence in Z | Z inside R via fd3:prp-integers-embed-rationals and F3.10's kappa (fd3:thm-reals-complete-ordered-field: injective, preserves + and *) (both cited)
exm-special-angles (solution): (u + 1)(u^2 - u + 1) = u^3 + 1; sqrt(1/2) = 1/sqrt 2; (sqrt 3 i)^2 = -3 | inline (ring algebra; uniqueness in fd3:prp-cof-square-roots); verify/ch01/exm-special-angles.py
exm-polar-power (solution): (sqrt 3 + i)^6 = -64 both ways | verify/ch01/exm-polar-power.py
sec-polar-form (solution): Check, (1 + i)^8 = 16, (sqrt 2)^8 = 16 | verify/ch01/exm-polar-power.py
exr-polar-form-a1 (solution): values | exm-special-angles (cited)
exr-polar-form-b1 (solution): (1 - sqrt 3 i)^6 = 64 | verify/ch01/exr-polar-form-b1.py
exr-polar-form-b3 (solution): a real is 0 iff its square is 0 | fd3:prp-ring-algebra (b) for 0^2 = 0, fd3:prp-ordered-ring-rules (e) for x != 0 (both cited)
exr-polar-form-c1 (solution): (c + is)^3 expansion, triple-angle formulas | inline; verify/ch01/exr-polar-form-c1.py
exr-polar-form-c2 (solution): u_t in T, t = Im u/(1 + Re u), u_{1/2} = 3/5 + 4/5 i | inline; verify/ch01/exr-polar-form-c2.py
sec-polar-form (claim): ax-cosine-sine (T1)-(T5) used by def-polar-form (T1), thm-polar-multiplication (T2; (b) also T1, T3 via e^{i0} = 1 and def-polar-form), prp-polar-form (T1, T3, T4; T2 through thm-polar-multiplication), thm-de-moivre (through thm-polar-multiplication), exm-special-angles (T3, T5, T1), exm-polar-power, exr-polar-form-a1, -b1 (T1, T3), -b2, -b3 (through def-polar-form), -c1 (T1); prp-unit-circle and exr-polar-form-c2 use none | AN1.10 (borrow)
-->
