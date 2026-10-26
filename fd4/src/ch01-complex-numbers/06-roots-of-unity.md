# Higher Roots, Roots of Unity, and a Look Ahead

Section 1.4 solved \( z^2 = c \) with real square roots alone. Polar form turns the general equation \( z^n = c \) into a question about lengths and angles: by De Moivre's formula (@thm-de-moivre), raising to the \( n \)-th power raises the modulus to the \( n \)-th power and multiplies the argument by \( n \). The angle part is a linear equation for a real number, with the ambiguity \( 2\pi\nZ \) of @prp-polar-form attached. The length part is the real equation \( r^n = \rho \) with \( \rho > 0 \), and before anything else we must know that it has exactly one positive solution. This section proves that, solves \( z^n = c \), counts the solutions, studies the case \( c = 1 \), and ends with a look ahead at polynomial equations in general.

## Real n-th roots

For \( n = 2 \), *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 6 built the square root by the move **construct a point as a supremum** (@fd3:prp-cof-square-roots), and an exercise there ran the same move for cube roots (@fd3:exr-measuring-by-rationals-b2). For a general exponent the move is the same; only the estimate for \( (s + h)^n \) needs a new tool, and @lem-difference-of-powers supplies it. Here \( n \cdot 1_{\nR} \) is written \( n \), and powers in \( \nR \) are those of @prp-power-laws-commutative-ring with \( R = \nR \), the same recursion as @fd3:def-naturals-in-ordered-field (b).

::: {#lem-reals-nth-root}
[Real n-th Roots]

Let \( n \in \nN \) with \( n \ge 1 \).

::: {.enumerate options="label=(\alph*)"}
1. If \( s, t \in \nR \) and \( 0 \le s < t \), then \( s^n < t^n \).
2. For every \( a \in \nR \) with \( a \ge 0 \) there is **exactly one** \( b \in \nR \) with \( b \ge 0 \) and \( b^n = a \). We write \( \sqrt[n]{a} \coloneqq b \). For \( n = 2 \) it is the square root \( \sqrt a \) of @fd3:prp-cof-square-roots.
:::
:::

::: {.idea}
Part (a) is the factorization \( t^n - s^n = (t - s)(t^{n-1} + t^{n-2}s + \dots + s^{n-1}) \): both factors are positive. For (b), let \( s \) be the supremum of the set \( S \) of non-negative \( y \) with \( y^n \le a \), and rule out \( s^n < a \) and \( s^n > a \).

If \( s^n < a \), we want \( h > 0 \) with \( (s + h)^n \le a \). Working backwards: for \( 0 < h \le 1 \), the same factorization writes \( (s + h)^n - s^n \) as \( h \) times a sum of \( n \) terms, each at most \( (s + 1)^{n-1} \). So \( (s + h)^n - s^n \le h \cdot n(s + 1)^{n-1} \), and it is enough that this be at most half the room \( a - s^n \). That gives \( h \coloneqq \min\{1, (a - s^n)/(2n(s + 1)^{n-1})\} \).

If \( s^n > a \), we want \( h > 0 \) with \( (s - h)^n \ge a \) still, which makes \( s - h \) a smaller upper bound. Now \( s^n - (s - h)^n \le h \cdot n s^{n-1} \), and it is enough that this equal the excess \( s^n - a \). That gives \( h \coloneqq (s^n - a)/(n s^{n-1}) \).
:::

::: {.proof}
Three facts are used throughout: a power of a non-negative real number is non-negative and a power of a positive one is positive (induction on the exponent with @fd3:prp-ordered-ring-rules (c)); if \( 0 \le y \le 1 \) then \( y^k \le y \) for every \( k \ge 1 \), while if \( y \ge 1 \) then \( y^k \ge y \) (induction: \( y^{k+1} = y^k y \), and @fd3:prp-ordered-ring-rules (c) or equality); and if \( 0 \le x \le x' \) and \( 0 \le y \le y' \), then \( xy \le x'y \le x'y' \) (@fd3:prp-ordered-ring-rules (c) twice, or equality).

(a) By @lem-difference-of-powers in the commutative ring \( \nR \),
\[
t^n - s^n = (t - s) \sum_{k=0}^{n-1} t^k s^{n-1-k} .
\]
Every term of the sum is \( \ge 0 \), and the term with \( k = n - 1 \) is \( t^{n-1} > 0 \), since \( t > s \ge 0 \). So the sum is \( \ge t^{n-1} > 0 \). Also \( t - s > 0 \). Hence \( t^n - s^n > 0 \) (@fd3:prp-ordered-ring-rules (c)).

(b) *Uniqueness.* If \( b, c \ge 0 \) and \( b \ne c \), say \( b < c \), then \( b^n < c^n \) by (a); so at most one non-negative \( b \) has \( b^n = a \).

*Existence.* If \( a = 0 \), then \( b \coloneqq 0 \) works, since \( 0^n = 0^{n-1} \cdot 0 = 0 \). Let \( a > 0 \), and let
\[
S \coloneqq \{ y \in \nR : y \ge 0 \text{ and } y^n \le a \} .
\]
Put \( m \coloneqq \min\{1, a\} > 0 \). Since \( 0 < m \le 1 \), \( m^n \le m \le a \), so \( m \in S \). Put \( M \coloneqq \max\{1, a\} \). If \( y > M \), then \( y > 1 \), so \( y^n \ge y > M \ge a \) and \( y \notin S \); hence \( M \) is an upper bound of \( S \). Since \( \nR \) is a complete ordered field (@fd3:thm-reals-complete-ordered-field, @fd3:def-complete-ordered-field), \( S \) has a supremum; let \( s \coloneqq \sup S \). Then \( s \ge m > 0 \).

*Case \( s^n < a \).* Let
\[
h \coloneqq \min\Bigl\{ 1, \frac{a - s^n}{2n(s + 1)^{n-1}} \Bigr\} .
\]
It depends only on \( a \), \( n \) and \( s \), and \( h > 0 \), since \( a - s^n > 0 \) and \( 2n(s + 1)^{n-1} > 0 \). By @lem-difference-of-powers,
\[
(s + h)^n - s^n = h \sum_{k=0}^{n-1} (s + h)^k s^{n-1-k} .
\]
Since \( 0 \le s < s + h \le s + 1 \), each term satisfies \( (s + h)^k s^{n-1-k} \le (s + 1)^k (s + 1)^{n-1-k} = (s + 1)^{n-1} \), by (a) (or equality), the third fact, and @prp-power-laws-commutative-ring (a). A sum of \( n \) terms, each at most \( (s + 1)^{n-1} \), is at most \( n (s + 1)^{n-1} \). Hence
\[
(s + h)^n \le s^n + h \cdot n(s + 1)^{n-1} \le s^n + \frac{a - s^n}{2} < a .
\]
So \( s + h \in S \), and \( s + h > s \), against \( s \) being an upper bound of \( S \).

*Case \( s^n > a \).* Let
\[
h \coloneqq \frac{s^n - a}{n s^{n-1}} ,
\]
which depends only on \( a \), \( n \) and \( s \), and is positive. Since \( a > 0 \), we have \( s^n - a < s^n \le n s^n \), so \( h < s^n/(n s^{n-1}) = s/n \le s \); thus \( 0 < s - h < s \). By @lem-difference-of-powers and the same bound, with \( 0 < s - h < s \), each of the \( n \) terms of \( \sum_{k=0}^{n-1} s^k (s - h)^{n-1-k} \) is at most \( s^{n-1} \), so
\[
s^n - (s - h)^n \le h \cdot n s^{n-1} = s^n - a ,
\]
that is, \( (s - h)^n \ge a \). Now let \( y \in S \). If \( y > s - h \), then (a) gives \( y^n > (s - h)^n \ge a \), against \( y \in S \). So \( y \le s - h \), and \( s - h \) is an upper bound of \( S \) smaller than \( s \), against \( s \) being the **least** upper bound.

Both cases are impossible, so \( s^n = a \) by trichotomy, and \( b \coloneqq s \ge 0 \) works.

For \( n = 2 \), the number \( \sqrt[2]{a} \) is non-negative and squares to \( a \), so it is \( \sqrt a \), by the uniqueness in @fd3:prp-cof-square-roots.
:::

The constants were found backwards in the Idea and placed first in the proof, and each depends on \( a \), \( n \) and \( s \) only. Completeness was used once, to produce \( s \). For \( a > 0 \) the root is positive, since \( 0^n = 0 \ne a \). For instance \( \sqrt[3]{8} = 2 \) and \( \sqrt[4]{4} = \sqrt 2 \), since \( 2^3 = 8 \) and \( (\sqrt 2)^4 = \bigl((\sqrt 2)^2\bigr)^2 = 4 \), and both are non-negative. The symbol \( \sqrt[n]{a} \) is used only for **non-negative real** \( a \); the next theorem shows why it could not mean "the" \( n \)-th root of a complex number.

## Solving the equation z to the n equals c

Now the main result. Every non-zero complex number has exactly \( n \) different \( n \)-th roots, and polar form lists them.

::: {#thm-complex-nth-roots}
[n-th Roots of a Complex Number]

Let \( n \in \nN \) with \( n \ge 1 \), and let \( c \in \nC \) with \( c \ne 0 \). Let \( c = \rho e^{i\alpha} \) be a polar form of \( c \) (@prp-polar-form), and for \( k \in \nZ \) put
\[
z_k \coloneqq \sqrt[n]{\rho} \; e^{i(\alpha + 2\pi k)/n} .
\]

::: {.enumerate options="label=(\alph*)"}
1. For \( z \in \nC \): \( z^n = c \) if and only if \( z = z_k \) for some \( k \in \nZ \).
2. For \( k, l \in \nZ \): \( z_k = z_l \) if and only if \( n \mid k - l \) (@fd2:def-divides).
3. The map \( \{0, 1, \dots, n - 1\} \to \{ z \in \nC : z^n = c \} \), \( k \mapsto z_k \), is a bijection. So \( c \) has exactly \( n \) \( n \)-th roots (@fd2:def-finite).
:::

In particular every non-zero complex number has an \( n \)-th root, and every \( u \in \nT \) has one in \( \nT \).
:::

::: {.idea}
Write the unknown in polar form, \( z = r e^{i\theta} \). De Moivre turns \( z^n = c \) into \( r^n e^{in\theta} = \rho e^{i\alpha} \), and the uniqueness half of polar form splits that into a real equation for the length, \( r^n = \rho \), and an equation for the angle, \( n\theta \in \alpha + 2\pi\nZ \). The first has one solution, \( r = \sqrt[n]{\rho} \). The second has the solutions \( \theta = (\alpha + 2\pi k)/n \), one for each integer \( k \). Different \( k \) can give the same point, and they do exactly when the angles differ by a whole number of turns, that is, when \( n \mid k - l \). So the \( k \) that matter are the remainders \( 0, \dots, n - 1 \).

*Before reading on: where is the uniqueness half of the polar form used, and where the uniqueness of the real \( n \)-th root?*
:::

::: {.proof}
Here \( \rho = \abs{c} > 0 \) by @prp-polar-form (a), so \( \sqrt[n]{\rho} > 0 \) exists by @lem-reals-nth-root (b).

(a) Let \( z \in \nC \). If \( z = 0 \), then \( z^n = 0^{n-1} \cdot 0 = 0 \ne c \) (@fd3:prp-ring-algebra (b)), and \( z \) is no \( z_k \), since every \( z_k \) has modulus \( \sqrt[n]{\rho} > 0 \). So let \( z \ne 0 \), and fix a polar form \( z = r e^{i\theta} \) (@prp-polar-form (a)). By @thm-de-moivre, \( z^n = r^n e^{in\theta} \), a polar form with \( r^n > 0 \). By @prp-polar-form (b),
\[
z^n = c \iff r^n = \rho \ \text{ and } \ n\theta - \alpha \in 2\pi\nZ .
\]
Since \( r > 0 \), the uniqueness in @lem-reals-nth-root (b) gives \( r^n = \rho \iff r = \sqrt[n]{\rho} \). And \( n\theta - \alpha = 2\pi k \) holds for a given \( k \in \nZ \) exactly when \( \theta = (\alpha + 2\pi k)/n \).

\( (\Rightarrow) \) If \( z^n = c \), then \( r = \sqrt[n]{\rho} \) and \( \theta = (\alpha + 2\pi k)/n \) for some \( k \in \nZ \), so \( z = z_k \).

\( (\Leftarrow) \) If \( z = z_k \), use the polar form \( r \coloneqq \sqrt[n]{\rho} \), \( \theta \coloneqq (\alpha + 2\pi k)/n \) of \( z \) in the equivalence above. Both conditions on the right hold, so \( z^n = c \).

(b) The numbers \( z_k \) and \( z_l \) are given in polar form with the same modulus. By @prp-polar-form (b), \( z_k = z_l \) if and only if
\[
\frac{\alpha + 2\pi k}{n} - \frac{\alpha + 2\pi l}{n} = \frac{2\pi (k - l)}{n} \in 2\pi\nZ ,
\]
that is, if and only if \( 2\pi(k - l)/n = 2\pi m \) for some \( m \in \nZ \). Multiplying by \( n/(2\pi) \), and back, this says \( k - l = mn \), an equation between integers. So \( z_k = z_l \) if and only if \( n \mid k - l \).

(c) By (a), each \( z_k \) is a solution, so the map is into the set of solutions. *Injective:* let \( 0 \le l < k \le n - 1 \). Then \( 0 < k - l < n \). If \( z_k = z_l \), then \( n \mid k - l \) by (b), and since \( n > 0 \) and \( k - l > 0 \), @fd3:prp-divisibility-rules-integers (e) gives \( n \le k - l \), a contradiction. So \( z_k \ne z_l \). *Surjective:* let \( z^n = c \). By (a), \( z = z_k \) for some \( k \in \nZ \). Division with remainder (@fd3:thm-integers-division-remainder (a)) gives \( k = qn + j \) with \( q \in \nZ \) and \( 0 \le j \le n - 1 \). Then \( n \mid k - j \), so \( z = z_k = z_j \) by (b). Hence the map is a bijection. Composing it with the bijection \( \{1, \dots, n\} \to \{0, \dots, n - 1\} \), \( j \mapsto j - 1 \), shows that the set of solutions has \( n \) elements (@fd2:def-finite).

Finally, \( z_0 \) is an \( n \)-th root of \( c \). If \( \abs{c} = 1 \), then \( \rho = 1 \) and \( \sqrt[n]{1} = 1 \), since \( 1 \ge 0 \) and \( 1^n = 1 \); so every \( z_k \) has modulus \( 1 \) and lies in \( \nT \).
:::

The answer to the prompt: the uniqueness half of the polar form, @prp-polar-form (b), turns the one complex equation \( z^n = c \) into the two real conditions, and is used again in (b) to decide when two of the \( z_k \) coincide. The uniqueness of the real root forces the modulus, \( r = \sqrt[n]{\rho} \). The ambiguity \( 2\pi\nZ \) in the angle is what produces \( n \) roots instead of one.

::: {.warning}
Dividing the angle equation by \( n \) too early loses roots. From \( z^3 = 1 \), \( z = e^{i\theta} \), one might write \( e^{3i\theta} = e^{i0} \), "so \( 3\theta = 0 \) and \( z = 1 \)". But \( e^{3i\theta} = e^{i0} \) only gives \( 3\theta \in 2\pi\nZ \) (@prp-polar-form (b)), and the angles \( 2\pi/3 \) and \( 4\pi/3 \) give two more cube roots of \( 1 \). Only the remainders \( 0, \dots, n - 1 \) of \( k \) matter, but all of them do.
:::

## Roots of unity

The most important case is \( c = 1 \).

::: {#exm-roots-of-unity}
[Roots of Unity]

Let \( n \ge 1 \) be an integer. Find all \( z \in \nC \) with \( z^n = 1 \), and draw them for \( n = 6 \).
:::

::: {.solution}
Apply @thm-complex-nth-roots with \( c = 1 = 1 \cdot e^{i0} \) (@thm-polar-multiplication (b)): \( \rho = 1 \), \( \alpha = 0 \), and \( \sqrt[n]{1} = 1 \). The solutions are
\[
z_k = e^{2\pi i k / n} , \qquad k \in \nZ .
\]
Put \( \omega \coloneqq e^{2\pi i/n} \). By @thm-de-moivre, \( z_k = (e^{2\pi i/n})^k = \omega^k \) for \( k \in \nN \). By @thm-complex-nth-roots (c), there are exactly \( n \) solutions,
\[
1, \; \omega, \; \omega^2, \; \dots, \; \omega^{n-1} ,
\]
the **\( n \)-th roots of unity**. They lie on \( \nT \), at the arguments \( 2\pi k/n \), equally spaced around the circle: multiplying by \( \omega \) turns each one into the next (@thm-polar-multiplication (a)), and \( \omega^{n-1} \) back into \( \omega^n = z_n = z_0 = 1 \) (@thm-complex-nth-roots (b)). For \( n \ge 3 \) they are the corners of a regular polygon with \( n \) corners, one of them at \( 1 \); for \( n = 2 \) they are \( 1 \) and \( \omega = e^{i\pi} = -1 \) (@exm-special-angles (i)); for \( n = 1 \) only \( 1 \).

For \( n = 6 \), \( \omega = e^{i\pi/3} = \tfrac12 + \tfrac{\sqrt 3}{2} i \) (@exm-special-angles (iii)), and \( \omega^3 = e^{i\pi} = -1 \). Hence \( \omega^2 = \bigl(\tfrac12 + \tfrac{\sqrt 3}{2} i\bigr)^2 = \tfrac14 - \tfrac34 + \tfrac{\sqrt 3}{2} i = -\tfrac12 + \tfrac{\sqrt 3}{2} i \), \( \omega^4 = -\omega \) and \( \omega^5 = -\omega^2 \). The six roots are
\[
1, \quad \tfrac12 + \tfrac{\sqrt3}{2}i, \quad -\tfrac12 + \tfrac{\sqrt3}{2}i, \quad -1, \quad -\tfrac12 - \tfrac{\sqrt3}{2}i, \quad \tfrac12 - \tfrac{\sqrt3}{2}i .
\]

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.6]
    \draw[->] (-1.5,0) -- (1.6,0) node[right] {$\operatorname{Re}$};
    \draw[->] (0,-1.4) -- (0,1.5) node[above] {$\operatorname{Im}$};
    \draw[dashed] (0,0) circle (1);
    \draw[thick] (0:1) -- (60:1) -- (120:1) -- (180:1) -- (240:1) -- (300:1) -- cycle;
    \foreach \k in {0,...,5} { \fill (\k*60:1) circle (1.2pt); }
    \node[below right] at (0:1) {$1$};
    \node[above right] at (60:1) {$\omega$};
    \node[above left] at (120:1) {$\omega^2$};
    \node[below left] at (180:1) {$\omega^3 = -1$};
    \node[below left] at (240:1) {$\omega^4$};
    \node[below right] at (300:1) {$\omega^5$};
\end{tikzpicture}
\end{center}
```

The six roots sum to \( 0 \): since \( \omega^3 = -1 \), we have \( \omega^{k+3} = -\omega^k \), so the roots cancel in the opposite pairs \( \{1, \omega^3\} \), \( \{\omega, \omega^4\} \), \( \{\omega^2, \omega^5\} \). In the picture, the hexagon is symmetric about its center \( 0 \). In general the sum is @prp-roots-of-unity-sum below.
:::

We write \( \mu_n \coloneqq \{ z \in \nC : z^n = 1 \} = \{ 1, \omega, \dots, \omega^{n-1} \} \) for the set of \( n \)-th roots of unity. It is a subset of \( \nT \), since each element is some \( z_k = e^{2\pi i k/n} \) (@thm-complex-nth-roots (a)). It contains \( 1 \), and it is closed under products, since \( (\zeta\eta)^n = \zeta^n \eta^n = 1 \) for \( \zeta, \eta \in \mu_n \) (@prp-power-laws-commutative-ring (c)). It is closed under inverses, since \( \zeta \cdot \zeta^{n-1} = \zeta^n = 1 \) gives \( \zeta^{-1} = \zeta^{n-1} \), a product of elements of \( \mu_n \) (for \( n = 1 \), \( \zeta^{0} = 1 \)). *Algebraic Preliminaries*, Chapter 3 treats \( \mu_n \), like \( \nT \), as an example of a group.

The roots of unity also describe the roots of any \( c \ne 0 \): the root \( z_0 = \sqrt[n]{\rho}\, e^{i\alpha/n} \) of @thm-complex-nth-roots satisfies \( z_k = z_0 \, \omega^k \) for \( k \in \nN \), by @thm-polar-multiplication (a) and @thm-de-moivre, since \( (\alpha + 2\pi k)/n = \alpha/n + 2\pi k/n \). So by @thm-complex-nth-roots (c) the \( n \)-th roots of \( c \) are \( z_0, z_0\omega, \dots, z_0\omega^{n-1} \): one of them times the \( n \)-th roots of unity.

The six roots canceled in pairs. The same pairing works for every even \( n \), since \( \omega^{n/2} = e^{i\pi} = -1 \) (@thm-de-moivre, @exm-special-angles (i)) gives \( \omega^{k + n/2} = -\omega^k \); but for odd \( n \) there are no opposite pairs: if \( \zeta \) and \( -\zeta \) were both \( n \)-th roots of unity, then \( 1 = (-\zeta)^n = (-1)^n \zeta^n = -1 \). A different argument is needed. It is @lem-difference-of-powers once more.

::: {#prp-roots-of-unity-sum}
[Sums of Roots of Unity]

Let \( n \in \nN \) with \( n \ge 2 \), and let \( \omega \coloneqq e^{2\pi i/n} \).

::: {.enumerate options="label=(\alph*)"}
1. For \( m \in \nN \): \( \omega^m = 1 \) if and only if \( n \mid m \). In particular \( \omega \ne 1 \).
2. \( \displaystyle\sum_{k=0}^{n-1} \omega^k = 0 \).
3. For \( m \in \nN \),
\[
\sum_{k=0}^{n-1} \omega^{mk} =
\begin{cases}
n & \text{if } n \mid m , \\
0 & \text{otherwise.}
\end{cases}
\]
:::
:::

::: {.idea}
Put \( \zeta \coloneqq \omega^m \). The sum in (c) is \( 1 + \zeta + \dots + \zeta^{n-1} \), and @lem-difference-of-powers multiplies it by \( \zeta - 1 \) to give \( \zeta^n - 1 = 0 \). If \( \zeta \ne 1 \) we may cancel, and the sum is \( 0 \); if \( \zeta = 1 \) it is \( n \). Part (a) decides which case occurs.
:::

::: {.proof}
We use the notation of @exm-roots-of-unity: \( z_k = e^{2\pi i k/n} \) are the roots of \( c = 1 \) in @thm-complex-nth-roots, and \( \omega^m = z_m \) for \( m \in \nN \) (@thm-de-moivre).

(a) Since \( 1 = z_0 \), @thm-complex-nth-roots (b) gives \( \omega^m = 1 \iff z_m = z_0 \iff n \mid m \). For \( m = 1 \): if \( n \mid 1 \), then \( n \le 1 \) by @fd3:prp-divisibility-rules-integers (e), against \( n \ge 2 \). So \( \omega \ne 1 \).

(c) Let \( \zeta \coloneqq \omega^m \). By @prp-power-laws-commutative-ring (b), \( \omega^{mk} = \zeta^k \) for each \( k \), and \( \zeta^n = \omega^{mn} = (\omega^n)^m = 1^m = 1 \), since \( \omega^n = z_n = z_0 = 1 \) by @thm-complex-nth-roots (b).

*Case \( n \mid m \).* Then \( \zeta = 1 \) by (a), and the sum is \( \sum_{k=0}^{n-1} 1 = n \).

*Case \( n \nmid m \).* Then \( \zeta \ne 1 \) by (a). By @lem-difference-of-powers with \( w = 1 \),
\[
0 = \zeta^n - 1 = (\zeta - 1) \sum_{k=0}^{n-1} \zeta^k .
\]
Since \( \zeta - 1 \ne 0 \) and \( \nC \) has no zero divisors (@thm-complex-numbers-field, @fd3:lem-field-fraction-rules (d)), the sum is \( 0 \).

(b) This is (c) with \( m = 1 \), since \( n \nmid 1 \) by (a).
:::

Comparing real and imaginary parts in (b), with \( \omega^k = \cos(2\pi k/n) + i \sin(2\pi k/n) \) (@thm-de-moivre), gives two real identities that are awkward to prove any other way: for \( n \ge 2 \),
\[
\sum_{k=0}^{n-1} \cos\frac{2\pi k}{n} = 0 \qquad \text{and} \qquad \sum_{k=0}^{n-1} \sin\frac{2\pi k}{n} = 0 .
\]
Part (c) says more: the sum of the \( m \)-th powers of the roots of unity detects whether \( n \) divides \( m \).

::: {.check}
Write the three cube roots of unity in the form \( a + bi \).
:::

::: {.solution}
By @exm-roots-of-unity with \( n = 3 \), they are \( 1 \), \( \omega \), \( \omega^2 \) with \( \omega = e^{2\pi i/3} = (e^{i\pi/3})^2 = -\tfrac12 + \tfrac{\sqrt 3}{2} i \) (@thm-de-moivre, and the square computed for \( n = 6 \) above). Since \( \omega \in \nT \) and \( \omega \cdot \omega^2 = \omega^3 = 1 \), \( \omega^2 = \omega^{-1} = \conj{\omega} = -\tfrac12 - \tfrac{\sqrt 3}{2} i \) (@prp-unit-circle (a)). So the cube roots of unity are \( 1 \) and \( -\tfrac12 \pm \tfrac{\sqrt 3}{2} i \). Without angles: \( z^3 - 1 = (z - 1)(z^2 + z + 1) \), and @cor-complex-quadratic-formula applied to \( z^2 + z + 1 = 0 \), with \( d = \sqrt 3\, i \) a square root of \( 1 - 4 = -3 \), gives \( z = (-1 \pm \sqrt 3\, i)/2 \).
:::

## Polynomial equations, and a look ahead

An \( n \)-th root of \( c \) solves \( z^n - c = 0 \), a polynomial equation of degree \( n \) with only two non-zero coefficients. The general question is whether every equation
\[
a_n z^n + a_{n-1} z^{n-1} + \dots + a_1 z + a_0 = 0 , \qquad a_0, \dots, a_n \in \nC , \ a_n \ne 0 , \ n \ge 1 ,
\]
has a solution in \( \nC \). Here the left side is a **polynomial expression** \( \sum_{k=0}^{n} a_k z^k \), a finite sum; *Algebraic Preliminaries*, Chapter 4 makes polynomials objects in their own right. We built \( \nC \) so that one such equation, \( z^2 + 1 = 0 \), has a solution, and Section 1.4 solved every equation of degree \( 2 \). It turns out that nothing more ever needs to be added.

::: {.remark}
[Looking ahead]

*Algebraic Preliminaries*, Section 5.6 proves that every such equation has a solution in \( \nC \): the Fundamental Theorem of Algebra. Its proof uses only the square roots of Section 1.4 and the completeness of \( \nR \), not polar form and not the borrowed facts about cosine and sine. With division of polynomials, *Algebraic Preliminaries*, Chapter 5 deduces that every complex polynomial of degree \( n \ge 1 \) is a non-zero constant times a product of \( n \) factors of the form \( z - z_j \). Nothing in this chapter or in *Algebraic Preliminaries*, Chapters 2–4 uses the theorem.
:::

One companion fact needs no heavy machinery: when the coefficients are real, the solutions that are not real come in conjugate pairs.

::: {#prp-real-coefficients-conjugate-roots}
[Real Coefficients and Conjugate Roots]

Let \( n \in \nN \), let \( a_0, \dots, a_n \in \nR \), and let \( z \in \nC \). Then
\[
\conj{\sum_{k=0}^{n} a_k z^k} = \sum_{k=0}^{n} a_k \, \conj{z}^{\,k} .
\]
Hence, if \( \sum_{k=0}^{n} a_k z_0^k = 0 \) for some \( z_0 \in \nC \), then also \( \sum_{k=0}^{n} a_k \conj{z_0}^{\,k} = 0 \).
:::

::: {.proof}
First, \( \conj{z^k} = \conj{z}^{\,k} \) for every \( k \in \nN \), by @fd1:ax-induction on \( k \): \( \conj{z^0} = \conj{1} = 1 = \conj{z}^{\,0} \), since \( 1 \) is real (@prp-modulus-of-real); and if \( \conj{z^k} = \conj{z}^{\,k} \), then \( \conj{z^{k+1}} = \conj{z^k z} = \conj{z^k}\, \conj{z} = \conj{z}^{\,k} \conj{z} = \conj{z}^{\,k+1} \), by @thm-conjugate-properties (b). Next, \( \conj{a_k} = a_k \) since \( a_k \) is real (@prp-modulus-of-real), so \( \conj{a_k z^k} = a_k \conj{z}^{\,k} \), again by @thm-conjugate-properties (b). Finally, the conjugate of a finite sum is the sum of the conjugates, by induction on the number of terms along the recursion for finite sums, with @thm-conjugate-properties (a) in the step. This proves the identity. If \( \sum a_k z_0^k = 0 \), then \( \sum a_k \conj{z_0}^{\,k} = \conj{0} = 0 \).
:::

A solution \( z_0 \) that is not real gives a **second** solution: \( \conj{z_0} \ne z_0 \), since \( z_0 = x + yi \) with \( y \ne 0 \) has \( \conj{z_0} = x - yi \), and \( -y \ne y \). For example, \( z^2 - 2z + 5 = 0 \) has the solution \( 1 + 2i \), since \( (1 + 2i)^2 - 2(1 + 2i) + 5 = (-3 + 4i) - (2 + 4i) + 5 = 0 \); so it also has the solution \( 1 - 2i \). *Algebraic Preliminaries*, Chapter 5 uses this to factor real polynomials into real factors of degree \( 1 \) and \( 2 \).

## Exercises

### A. Check your understanding

::: {#exr-roots-of-unity-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Find all \( z \in \nC \) with \( z^4 = 1 \).
2. In the proof of @thm-complex-nth-roots, where is the uniqueness half of @prp-polar-form used?
3. In the same proof, why is the modulus \( r \) of a solution forced to be \( \sqrt[n]{\rho} \)?
4. True or false: \( z^3 = 1 \) has exactly three solutions in \( \nC \), and exactly one of them is real. Justify your answer.
5. State the idea of the proof of @thm-complex-nth-roots in two sentences.
:::
:::

::: {.solution}
(a) By @exm-roots-of-unity with \( n = 4 \), the solutions are \( \omega^k \) for \( k = 0, 1, 2, 3 \), where \( \omega = e^{2\pi i/4} = e^{i\pi/2} = i \) (@exm-special-angles (ii)): \( 1 \), \( i \), \( -1 \), \( -i \).

(b) Twice. In (a), to turn \( r^n e^{in\theta} = \rho e^{i\alpha} \) into the two conditions \( r^n = \rho \) and \( n\theta - \alpha \in 2\pi\nZ \). In (b), to decide when \( z_k = z_l \).

(c) Because \( r > 0 \) and \( r^n = \rho \), and @lem-reals-nth-root (b) says that \( \sqrt[n]{\rho} \) is the **only** non-negative real number with \( n \)-th power \( \rho \).

(d) True. By @thm-complex-nth-roots (c) there are exactly three. By the Check above they are \( 1 \) and \( -\tfrac12 \pm \tfrac{\sqrt 3}{2} i \); the last two have imaginary part \( \pm \tfrac{\sqrt 3}{2} \ne 0 \), so only \( 1 \) is real.

(e) Polar form and De Moivre split \( z^n = c \) into a real equation for the modulus, which has exactly one positive solution, and an equation for the argument, which is solved up to the ambiguity \( 2\pi\nZ \). That ambiguity, divided by \( n \), produces \( n \) different roots, one for each remainder modulo \( n \).
:::

### B. Practice

::: {#exr-roots-of-unity-b1}
[B1]

Find all \( z \in \nC \) with \( z^3 = -8i \), in the form \( a + bi \).
:::

::: {.solution}
By @exm-special-angles (ii) and @thm-polar-multiplication (b), \( e^{-i\pi/2} = \conj{e^{i\pi/2}} = \conj{i} = -i \), so \( -8i = 8 e^{-i\pi/2} \) is a polar form, with \( \rho = 8 \) and \( \alpha = -\pi/2 \). Also \( \sqrt[3]{8} = 2 \). By @thm-complex-nth-roots, the solutions are \( z_k = 2 e^{i(-\pi/2 + 2\pi k)/3} = 2 e^{i(-\pi/6 + 2\pi k/3)} \) for \( k = 0, 1, 2 \), with arguments \( -\pi/6 \), \( \pi/2 \) and \( 7\pi/6 \):
\[
\begin{aligned}
z_0 &= 2 e^{-i\pi/6} = 2\, \conj{e^{i\pi/6}} = \sqrt 3 - i , \qquad z_1 = 2 e^{i\pi/2} = 2i , \\
z_2 &= 2 e^{i\pi} e^{i\pi/6} = -2 \Bigl( \frac{\sqrt 3}{2} + \frac12 i \Bigr) = -\sqrt 3 - i ,
\end{aligned}
\]
by @exm-special-angles (i), (ii), (iv) and @thm-polar-multiplication. Check: \( (2i)^3 = 8 i^3 = -8i \), and \( (\sqrt 3 - i)^2 = 2 - 2\sqrt 3\, i \), so \( (\sqrt 3 - i)^3 = (2 - 2\sqrt 3\, i)(\sqrt 3 - i) = 2\sqrt 3 - 2i - 6i - 2\sqrt 3 = -8i \).
:::

::: {#exr-roots-of-unity-b2}
[B2]

Find all \( z \in \nC \) with \( z^4 = -4 \), in the form \( a + bi \), and check one of them directly.
:::

::: {.solution}
A polar form is \( -4 = 4 e^{i\pi} \) (@exm-special-angles (i)), and \( \sqrt[4]{4} = \sqrt 2 \), since \( \sqrt 2 \ge 0 \) and \( (\sqrt 2)^4 = 4 \). By @thm-complex-nth-roots, the solutions are \( z_k = \sqrt 2 \, e^{i(\pi + 2\pi k)/4} \) for \( k = 0, 1, 2, 3 \). First, \( z_0 = \sqrt 2 \, e^{i\pi/4} = 1 + i \) (@exm-special-angles (v)). Next, \( (\pi + 2\pi(k + 1))/4 = (\pi + 2\pi k)/4 + \pi/2 \), so \( z_{k+1} = z_k e^{i\pi/2} = i z_k \) (@thm-polar-multiplication (a), @exm-special-angles (ii)). Hence
\[
z_0 = 1 + i , \quad z_1 = -1 + i , \quad z_2 = -1 - i , \quad z_3 = 1 - i ,
\]
that is, \( z = \pm 1 \pm i \) with all four choices of signs. Check: \( (1 + i)^2 = 2i \), so \( (1 + i)^4 = (2i)^2 = -4 \).
:::

::: {#exr-roots-of-unity-b3}
[B3]

Let \( n \ge 1 \) and \( \omega \coloneqq e^{2\pi i/n} \). Show that \( 1 \in \mu_n \), that \( \mu_n \) is closed under multiplication, that for \( k = 1, \dots, n - 1 \) the inverse of \( \omega^k \) is \( \omega^{n-k} \), and that \( \mu_n \subseteq \nT \).
:::

::: {.solution}
\( 1^n = 1 \), so \( 1 \in \mu_n \). If \( \zeta^n = \eta^n = 1 \), then \( (\zeta\eta)^n = \zeta^n \eta^n = 1 \) by @prp-power-laws-commutative-ring (c). For \( 1 \le k \le n - 1 \), \( \omega^k \omega^{n-k} = \omega^n = 1 \) by @prp-power-laws-commutative-ring (a) and @prp-roots-of-unity-sum (a) (or @exm-roots-of-unity), so \( \omega^{n-k} \) is the inverse of \( \omega^k \), and it lies in \( \mu_n \). Finally let \( \zeta \in \mu_n \). Then \( \abs{\zeta}^n = \abs{\zeta^n} = \abs{1} = 1 \), where the first equality is @thm-conjugate-properties (d) applied \( n \) times (induction on \( n \)). Since \( \abs{\zeta} \ge 0 \) and also \( 1 \ge 0 \) with \( 1^n = 1 \), the uniqueness in @lem-reals-nth-root (b) gives \( \abs{\zeta} = 1 \). So \( \zeta \in \nT \). (This last argument uses no borrowed fact.)
:::

### C. Going deeper

::: {#exr-roots-of-unity-c1}
[C1: Exit check: n-th roots]

Let \( n \ge 1 \) and \( c \in \nC \) with \( c \ne 0 \), and let \( c = \rho e^{i\alpha} \) be a polar form. Prove parts (a) and (b) of @thm-complex-nth-roots: the solutions of \( z^n = c \) are exactly the numbers \( z_k = \sqrt[n]{\rho}\, e^{i(\alpha + 2\pi k)/n} \), \( k \in \nZ \), and \( z_k = z_l \) if and only if \( n \mid k - l \). Cite the polar form, De Moivre's formula and the real \( n \)-th root where you use them.
:::

::: {.solution}
Here \( \rho = \abs{c} > 0 \) (@prp-polar-form (a)). The number \( 0 \) is not a solution, since \( 0^n = 0 \ne c \), and is no \( z_k \), since \( \abs{z_k} = \sqrt[n]{\rho} > 0 \) (@lem-reals-nth-root (b)). For \( z \ne 0 \), fix a polar form \( z = r e^{i\theta} \) with \( r > 0 \) (@prp-polar-form (a)); then \( z^n = r^n e^{in\theta} \) (@thm-de-moivre), a polar form with \( r^n > 0 \), and by the uniqueness of polar form (@prp-polar-form (b)), \( z^n = \rho e^{i\alpha} \) if and only if \( r^n = \rho \) and \( n\theta - \alpha \in 2\pi\nZ \). The first condition is \( r = \sqrt[n]{\rho} \), by existence and uniqueness of the real \( n \)-th root (@lem-reals-nth-root (b)); the second is \( \theta = (\alpha + 2\pi k)/n \) for some \( k \in \nZ \). So \( z^n = c \) implies \( z = z_k \); conversely, applied to the polar form \( r \coloneqq \sqrt[n]{\rho} \), \( \theta \coloneqq (\alpha + 2\pi k)/n \) of \( z = z_k \), the equivalence gives \( z^n = c \). For (b), \( z_k \) and \( z_l \) are given in polar form with the same modulus, so the same uniqueness gives \( z_k = z_l \) if and only if \( 2\pi(k - l)/n \in 2\pi\nZ \), if and only if \( k - l = mn \) for some \( m \in \nZ \), that is, \( n \mid k - l \).

**Marking scheme.** (10 points)
- 1: rules out \( z = 0 \), with the reason \( 0^n = 0 \ne c \).
- 2: writes \( z \) (and \( c \)) in polar form and applies De Moivre's formula to get \( z^n = r^n e^{in\theta} \).
- 3: splits \( z^n = c \) into \( r^n = \rho \) and \( n\theta - \alpha \in 2\pi\nZ \), citing the uniqueness of polar form, and states both directions (every \( z_k \) is a solution, every solution is some \( z_k \)).
- 1: \( r = \sqrt[n]{\rho} \), with both existence and uniqueness of the real \( n \)-th root cited (the point is lost if either is assumed without citation).
- 3: (b), \( z_k = z_l \iff n \mid k - l \), both directions.
Fatal errors (0 for the step): concluding \( n\theta = \alpha \), or \( \theta = \alpha/n \), from \( e^{in\theta} = e^{i\alpha} \) (dropping \( 2\pi\nZ \)); writing \( \sqrt[n]{c} \) for a complex \( c \). Second route: find one root \( z_0 \) and show that \( z^n = c \) if and only if \( (z/z_0)^n = 1 \), then solve \( w^n = 1 \) by polar form. The same points apply, with the 3 points of the third line awarded for the roots of unity, and (b) replaced by the distinctness of \( 1, \omega, \dots, \omega^{n-1} \) and the periodicity \( \omega^{k+n} = \omega^k \).
:::

::: {#exr-roots-of-unity-c2}
[C2: Find the error]

Here is an argument.

> **Claim.** For \( n \ge 2 \), the \( n \)-th roots of unity sum to \( 0 \).
>
> (1) Let \( \omega \coloneqq e^{2\pi i/n} \) and \( S \coloneqq 1 + \omega + \dots + \omega^{n-1} \). (2) Then \( \omega S = \omega + \omega^2 + \dots + \omega^n = S \), since \( \omega^n = 1 \). (3) So \( (\omega - 1) S = 0 \). (4) Since \( \omega \) is an \( n \)-th root of unity, \( \omega^n = 1 \), so \( \omega \ne 1 \). (5) Hence \( \omega - 1 \ne 0 \), and \( S = 0 \).

Is the claim true? Does the argument prove it? If not, name the first line that fails, say what is wrong with it, give a counterexample to the step, and repair the argument.
:::

::: {.solution}
The claim is true: it is @prp-roots-of-unity-sum (b).

The argument does not prove it. Lines (1)–(3) are correct: \( \omega^n = 1 \) by @exm-roots-of-unity, and (3) is (2) rearranged. Line (5) is correct **given** (4), since \( \nC \) has no zero divisors. Line (4) fails. "\( \omega^n = 1 \), so \( \omega \ne 1 \)" cites a general "fact", that an \( n \)-th root of unity is not \( 1 \), which is false: this is the error (N9) of @fd1:exm-not-allowed-catalogue. *Counterexample to the step:* \( 1 \) itself satisfies \( 1^n = 1 \), and \( 1 = 1 \). Being an \( n \)-th root of unity gives no information that separates \( \omega \) from \( 1 \); the information is in the particular choice \( \omega = e^{2\pi i/n} \) with \( n \ge 2 \).

*Repair.* If \( \omega = e^{2\pi i/n} = 1 = e^{i0} \), then \( 2\pi/n \in 2\pi\nZ \) by @prp-polar-form (b), so \( 1/n = m \) for some \( m \in \nZ \), that is, \( 1 = mn \) and \( n \mid 1 \). Since \( n \ge 2 > 0 \), @fd3:prp-divisibility-rules-integers (e) gives \( n \le 1 \), a contradiction. So \( \omega \ne 1 \), and lines (5) and the conclusion stand. (This repair uses (T1)–(T3) of @ax-cosine-sine, through @prp-polar-form (b), and no value of the cosine.)
:::

### R. Review

::: {#exr-roots-of-unity-r1}
[R1]

Let \( \sigma \colon \nC \to \nC \) satisfy \( \sigma(z + w) = \sigma(z) + \sigma(w) \) and \( \sigma(zw) = \sigma(z)\sigma(w) \) for all \( z, w \in \nC \), \( \sigma(1) = 1 \), and \( \sigma(a) \in \nR \) for every \( a \in \nR \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that either \( \sigma(z) = z \) for every \( z \in \nC \), or \( \sigma(z) = \conj{z} \) for every \( z \in \nC \).
2. Show that conjugation \( z \mapsto \conj{z} \) satisfies all the hypotheses on \( \sigma \).
:::
:::

::: {.solution}
(a) Since \( \sigma \) maps \( \nR \) into \( \nR \), it restricts to a map \( \tau \colon \nR \to \nR \), \( \tau(a) \coloneqq \sigma(a) \), which preserves sums and products and sends \( 1 \) to \( 1 \). Since \( \nR \) is a complete ordered field (@fd3:thm-reals-complete-ordered-field), @fd3:thm-cof-field-automorphism-identity gives \( \tau = \id_{\nR} \): \( \sigma(a) = a \) for every real \( a \). In particular \( \sigma(-1) = -1 \), so
\[
\sigma(i)^2 = \sigma(i \cdot i) = \sigma(-1) = -1 = i^2 .
\]
So \( \bigl(\sigma(i) - i\bigr)\bigl(\sigma(i) + i\bigr) = 0 \), and \( \sigma(i) = i \) or \( \sigma(i) = -i \) (no zero divisors in \( \nC \); or @prp-complex-square-roots (b)). For \( z = a + bi \) with \( a, b \in \nR \),
\[
\sigma(z) = \sigma(a) + \sigma(b)\sigma(i) = a + b\,\sigma(i) .
\]
If \( \sigma(i) = i \), then \( \sigma(z) = z \) for every \( z \); if \( \sigma(i) = -i \), then \( \sigma(z) = a - bi = \conj{z} \) for every \( z \).

(b) Conjugation preserves sums and products by @thm-conjugate-properties (a), (b), and \( \conj{a} = a \) for every real \( a \) (@prp-modulus-of-real), so in particular \( \conj{1} = 1 \) and real numbers go to real numbers.

The comparison with *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 6 (@fd3:thm-cof-field-automorphism-identity) is the point: \( \nR \) has only the identity, while \( \nC \) has exactly two such maps. In \( \nR \) the order can be read off from the field operations (the non-negative numbers are exactly the squares, @fd3:prp-cof-square-roots), and a map preserving \( + \) and \( \cdot \) must preserve it. In \( \nC \) there is no order (@prp-complex-not-orderable), and nothing written with \( + \), \( \cdot \) and real numbers alone tells \( i \) from \( -i \).
:::

::: {#exr-roots-of-unity-r2}
[R2]

Let \( n \ge 1 \). Show that \( [k] \mapsto e^{2\pi i k/n} \) is a well-defined bijection \( f \colon \nZ/n\nZ \to \mu_n \), and that \( f([k] + [l]) = f([k]) \, f([l]) \) for all \( k, l \in \nZ \).
:::

::: {.solution}
Write \( z_k \coloneqq e^{2\pi i k/n} \), the roots of \( c = 1 \) in @thm-complex-nth-roots (with \( \rho = 1 \), \( \alpha = 0 \), as in @exm-roots-of-unity). The classes of \( \nZ/n\nZ \) are the congruence classes of @fd2:def-congruence: \( [k] = [l] \) if and only if \( n \mid k - l \). By @thm-complex-nth-roots (b), \( n \mid k - l \) if and only if \( z_k = z_l \). Reading this equivalence from left to right, \( f([k]) \coloneqq z_k \) does not depend on the representative \( k \) of the class, so \( f \) is well defined; reading it from right to left, \( f \) is injective. Each \( z_k \) lies in \( \mu_n \) by @thm-complex-nth-roots (a), and every element of \( \mu_n \) is some \( z_k \), again by (a); so \( f \) is surjective. Finally, \( [k] + [l] = [k + l] \), and by @thm-polar-multiplication (a),
\[
f([k] + [l]) = z_{k+l} = e^{2\pi i k/n} e^{2\pi i l/n} = f([k]) \, f([l]) .
\]
As a check on the count, both sets have \( n \) elements (@fd2:prp-integers-mod-n and @thm-complex-nth-roots (c)). In the language of *Algebraic Preliminaries*, Chapter 3, \( f \) is an isomorphism from the additive structure of \( \nZ/n\nZ \) to the multiplicative structure of \( \mu_n \).
:::

::: {#exr-roots-of-unity-r3}
[R3]

Let \( F \) be an ordered field and \( x, y \in F \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \abs{x + y} \le \abs{x} + \abs{y} \) by comparing the squares of the two sides.
2. The proof of the same inequality by "trapping" \( x \) between \( -\abs{x} \) and \( \abs{x} \), and adding the traps for \( x \) and \( y \), works in every ordered field. Which step of it cannot be carried out for complex \( x, y \), and what replaces it in the complex triangle inequality?
:::
:::

::: {.solution}
(a) Both sides are non-negative. By @fd3:prp-absolute-value-ordered-field (b), \( \abs{x}^2 = x^2 \), \( \abs{y}^2 = y^2 \), \( \abs{x + y}^2 = (x + y)^2 \) and \( \abs{x}\abs{y} = \abs{xy} \). Hence
\[
(\abs{x} + \abs{y})^2 - \abs{x + y}^2 = \abs{x}^2 + 2\abs{x}\abs{y} + \abs{y}^2 - x^2 - 2xy - y^2 = 2\bigl(\abs{xy} - xy\bigr) \ge 0 ,
\]
since \( xy \le \abs{xy} \) (@fd3:prp-absolute-value-ordered-field (c)). So \( \abs{x + y}^2 \le (\abs{x} + \abs{y})^2 \). If \( \abs{x + y} > \abs{x} + \abs{y} \), then @fd3:prp-ordered-ring-rules (g), applied to these non-negative elements, would give \( \abs{x + y}^2 > (\abs{x} + \abs{y})^2 \); so \( \abs{x + y} \le \abs{x} + \abs{y} \).

(b) The trapping proof (@fd3:prp-absolute-value-ordered-field (e), proved from (c)) uses \( -\abs{x} \le x \le \abs{x} \): it compares \( x \) itself with real numbers. For a complex \( x \) that is not real such a comparison means nothing, since no order on \( \nC \) is compatible with its arithmetic (@prp-complex-not-orderable). The squaring proof of (a) is the one that survives: in the complex triangle inequality (@thm-complex-triangle-inequality) the cross term \( 2\operatorname{Re}(z\conj{w}) \) is bounded by a comparison between **real** numbers, \( \operatorname{Re} u \le \abs{u} \) (@lem-real-part-at-most-modulus), which replaces \( xy \le \abs{xy} \) here.
:::

::: {#exr-roots-of-unity-r4}
[R4]

Find all \( z \in \nC \) with \( \conj{z} = z^2 \).
:::

::: {.solution}
*The tool:* take moduli first. If \( \conj{z} = z^2 \), then \( \abs{z} = \abs{\conj{z}} = \abs{z^2} = \abs{z}^2 \) (@thm-conjugate-properties (d)), so \( \abs{z}\bigl(\abs{z} - 1\bigr) = 0 \) and \( \abs{z} = 0 \) or \( \abs{z} = 1 \).

If \( \abs{z} = 0 \), then \( z = 0 \) (@thm-conjugate-properties (e)), and \( z = 0 \) is a solution.

If \( \abs{z} = 1 \), multiply \( \conj{z} = z^2 \) by \( z \): \( 1 = z\conj{z} = z^3 \) (@thm-conjugate-properties (c)). So \( z \) is a cube root of unity: \( z = 1 \) or \( z = -\tfrac12 \pm \tfrac{\sqrt 3}{2} i \) (the Check above). Conversely, each cube root of unity \( \zeta \) lies in \( \nT \) (Exercise B3), so \( \conj{\zeta} = \zeta^{-1} \) (@prp-unit-circle (a)), and \( \zeta^{-1} = \zeta^2 \) because \( \zeta \cdot \zeta^2 = \zeta^3 = 1 \). So each is a solution.

The solutions are \( 0 \), \( 1 \), \( -\tfrac12 + \tfrac{\sqrt 3}{2} i \) and \( -\tfrac12 - \tfrac{\sqrt 3}{2} i \).

*Why the look-alike tools are worse.* Comparing real and imaginary parts, with \( z = x + yi \), gives \( x^2 - y^2 = x \) and \( 2xy = -y \), which can be solved, but only with a case split by hand (\( y = 0 \) or \( x = -\tfrac12 \)). "Divide \( \conj{z} = z^2 \) by \( z \)" silently loses the solution \( z = 0 \). Polar form works, but it is not needed: the moduli settle \( \abs{z} \), and the cube roots of unity can be found without angles, as in the Check.
:::

<!-- dependency ledger
lem-reals-nth-root (proof): powers of non-negative (positive) reals are non-negative (positive); 0 <= y <= 1 gives y^k <= y, y >= 1 gives y^k >= y, for k >= 1; 0 <= x <= x', 0 <= y <= y' gives xy <= x'y' | inline (induction, fd1:ax-induction via fd3:cor-omega-identification (b), with fd3:prp-ordered-ring-rules (c))
lem-reals-nth-root (proof): finite sums in R; a sum of non-negative terms is >= any one term; a sum of n terms each <= M is <= nM | template: fd2:def-sum-product recursion used as a pattern in R; inline induction on n (fd1:ax-induction)
lem-reals-nth-root (proof): 0^n = 0 for n >= 1; min{1, a}, max{1, a} exist (two-element sets in a total order) | fd3:prp-ring-algebra (b); fd3:prp-ordered-ring-rules (i)
lem-reals-nth-root (proof): h < s from s^n - a < s^n <= n s^n and s/n <= s | arithmetic in the ordered field R (n >= 1: fd3:prp-naturals-in-ordered-field (b)); verify/ch01/lem-reals-nth-root.py
lem-reals-nth-root (proof): constants h and the two inequalities (s + h)^n <= s^n + h n (s + 1)^{n-1}, s^n - (s - h)^n <= h n s^{n-1} | verify/ch01/lem-reals-nth-root.py (numeric, sample a, n)
lem-reals-nth-root (claim): cube root of 8 is 2, fourth root of 4 is sqrt 2 | inline (uniqueness); verify/ch01/lem-reals-nth-root.py
thm-complex-nth-roots (proof): 2 pi (k - l)/n = 2 pi m iff k - l = mn, an equation in Z | arithmetic in R; Z inside R via F3.10's kappa (fd3:thm-reals-complete-ordered-field: injective, preserves + and *)
thm-complex-nth-roots (proof): {1..n} -> {0..n-1}, j -> j - 1, is a bijection; composite of bijections is a bijection | inline; fd2 composition of bijections (fd2:def-bijective)
thm-complex-nth-roots (proof): sqrt[n]{1} = 1 | inline (1^n = 1, lem-reals-nth-root (b) uniqueness)
exm-roots-of-unity (solution): regular polygon picture | prose (picture); nothing depends on it
exm-roots-of-unity (solution): omega^2 for n = 6; omega^4 = -omega, omega^5 = -omega^2 | inline; verify/ch01/exm-roots-of-unity.py
sec-roots-of-unity (claim): z_k = z_0 omega^k for k in N, z_0 the theorem's root | thm-polar-multiplication (a), thm-de-moivre, thm-complex-nth-roots (c) (cited)
sec-roots-of-unity (claim): even-n pairing, omega^{n/2} = -1 and omega^{k+n/2} = -omega^k (prp-power-laws-commutative-ring (a)) | thm-de-moivre, exm-special-angles (i) (cited); inline; nothing depends on it
sec-roots-of-unity (claim): for odd n, (-1)^n = -1 | inline (induction); nothing depends on it
prp-roots-of-unity-sum (proof): sum_{k=0}^{n-1} 1 = n (as n * 1 in C); omega^{mn} = (omega^n)^m with mn = nm; 1^m = 1 | template: fd2:def-sum-product; prp-power-laws-commutative-ring (b); inline induction
prp-roots-of-unity-sum (claim): sum of cos(2 pi k/n) = sum of sin(2 pi k/n) = 0: real part of a finite sum is the sum of real parts | inline (addition in C is coordinatewise, def-complex-numbers; induction on the number of terms); verify/ch01/prp-roots-of-unity-sum.py
prp-real-coefficients-conjugate-roots (proof): conjugate of a finite sum is the sum of conjugates | inline (induction along fd2:def-sum-product recursion, template, with thm-conjugate-properties (a))
sec-roots-of-unity (example): (1 + 2i)^2 - 2(1 + 2i) + 5 = 0 | verify/ch01/prp-real-coefficients-conjugate-roots.py
sec-roots-of-unity (claim): Looking ahead: *Algebraic Preliminaries*, Section 5.6 proves the FTA using only square roots and completeness; *Algebraic Preliminaries*, Chapter 5 deduces splitting into linear factors; nothing in this chapter or in Algebraic Preliminaries Chapters 2-4 uses it | F5.5 (prose pointer; blueprint ch05.md thm-fundamental-theorem-algebra, cor-complex-polynomials-linear-factors); nothing here depends on it
sec-roots-of-unity (claim): *Algebraic Preliminaries*, Chapter 4 makes polynomials objects; *Algebraic Preliminaries*, Chapter 5 factors real polynomials into real factors of degrees 1 and 2; *Algebraic Preliminaries*, Chapter 3 treats T and mu_n as groups | F5.4, F5.5 (prp-real-polynomial-conjugate-roots), F5.3 (exm-subgroups (f)) (prose pointers; blueprints); nothing here depends on them
sec-roots-of-unity (solution): Check, cube roots of unity; z^3 - 1 = (z - 1)(z^2 + z + 1) | inline; verify/ch01/exm-roots-of-unity.py
exr-roots-of-unity-b1 (solution): z^3 = -8i values | verify/ch01/exr-roots-of-unity-b1.py
exr-roots-of-unity-b2 (solution): z^4 = -4 values; (pi + 2 pi (k + 1))/4 = (pi + 2 pi k)/4 + pi/2 | verify/ch01/exr-roots-of-unity-b2.py
exr-roots-of-unity-b3 (solution): |zeta^n| = |zeta|^n | inline (induction with thm-conjugate-properties (d))
exr-roots-of-unity-c2 (solution): 1/n = m gives 1 = mn | arithmetic in R; Z inside R via kappa
exr-roots-of-unity-r1 (solution): sigma restricted to R is a map R -> R preserving +, *, 1 | inline
exr-roots-of-unity-r1 (solution): the non-negative reals are exactly the squares, so the order of R is definable | fd3:prp-cof-square-roots (cited); fd3:prp-ordered-ring-rules (e)
exr-roots-of-unity-r2 (claim): "isomorphism" in the language of *Algebraic Preliminaries*, Chapter 3 | F5.3 (prose pointer); nothing depends on it
exr-roots-of-unity-r3 (solution): (|x| + |y|)^2 - |x + y|^2 = 2(|xy| - xy) | inline (fd3:prp-ring-algebra (d), fd3:prp-absolute-value-ordered-field (b))
exr-roots-of-unity-r4 (solution): solutions 0, 1, -1/2 +- (sqrt 3/2) i | verify/ch01/exr-roots-of-unity-r4.py
sec-roots-of-unity (claim): ax-cosine-sine (T1)-(T5) through def-polar-form, thm-polar-multiplication, prp-polar-form, thm-de-moivre, exm-special-angles: used by thm-complex-nth-roots, exm-roots-of-unity, prp-roots-of-unity-sum, the prose claims on mu_n = {1, omega, ..., omega^(n-1)} and mu_n subset T (after exm-roots-of-unity), z_k = z_0 omega^k, the even-n pairing and the cos/sin sums, the Check (first route), A1, B1, B2, B3 (the inverse clause, through prp-roots-of-unity-sum (a); its 1 in mu_n, closure and mu_n subset T steps use none), C1, C2, R2; lem-reals-nth-root, prp-real-coefficients-conjugate-roots, R1, R3, R4 (via the Check's angle-free route, cor-complex-quadratic-formula, and B3's angle-free mu_n subset T step) use none | AN1.10 (borrow)
-->
