# Real Functions and Their Graphs

Part II ended with polynomials as formal objects and with what their values can and cannot do. Part III turns to functions of a real variable, the objects that analysis adds, composes, inverts and bounds. This section fixes what a real function is, how two of them combine, how a graph moves when the formula changes, and how a function splits into an even and an odd part. Everything is proved from *Sets and Functions* and the complete ordered field \( \nR \); no limit appears.

## A formula is not yet a function

Let \( f(x) = x^2/x \). What is \( f(0) \)?

The tempting answer cancels: \( x^2/x = x \), so \( f(0) = 0 \). But the formula \( x^2/x \) asks us to divide by \( 0 \) at \( 0 \), and no field rule allows that. Another reader says \( f(0) \) is undefined. Both readers have a function in mind, and they have different ones. A function, by @fd2:def-function, consists of a graph **and** a domain on which every input has exactly one value; a formula supplies the values but not the domain. Until the domain is named the question has no answer.

*A real function is a set of inputs together with one real value for each of them.*

::: {#def-real-function}
[Real Function, Graph]

Let \( D \subseteq \nR \). A **real function on \( D \)** is a function \( f \colon D \to \nR \) (@fd2:def-function). Its **graph** is
\[
\operatorname{graph} f \coloneqq \{ (x, f(x)) : x \in D \} \subseteq \nR^2 ,
\]
where \( \nR^2 \coloneqq \nR \times \nR \) (@fd2:def-cartesian-product). The set \( D \) is always stated; there is no "natural domain" convention.
:::

The graph is exactly the relation \( G \) of @fd2:def-function, since each element of \( G \) is the pair \( (x, f(x)) \). The codomain of a real function is always \( \nR \), so @fd2:prp-function-equality reads: **two real functions are equal if and only if they have the same domain and the same value at every point of it.** With \( D = \nR \setminus \{0\} \), the hook's function is \( x \mapsto x^2/x \) on \( \nR \setminus \{0\} \), and \( 0 \) is not an input.

::: {#exm-first-real-functions}
[First Real Functions]

Each of the following is a real function; check that each input has exactly one value.

::: {.enumerate options="label=(\alph*)"}
1. A constant \( x \mapsto c \) on \( \nR \), and the identity \( x \mapsto x \) on \( \nR \).
2. The absolute value \( x \mapsto \abs{x} \) on \( \nR \) (@fd3:def-absolute-value-ordered-field).
3. \( x \mapsto 1/x \) on \( \nR \setminus \{0\} \).
4. \( x \mapsto \sqrt{x} \) on \( [0, \infty) \).
5. A restriction \( f|_A \) (@fd2:def-restriction-extension), for instance \( x \mapsto x^2 \) on \( [0, \infty) \).
6. An indicator \( \ind_A \) for \( A \subseteq \nR \) (@fd2:def-indicator), with codomain \( \nR \) in place of \( \{0, 1\} \).
7. The function equal to \( x \) on \( (-\infty, 0) \) and to \( x^2 \) on \( [0, \infty) \).
:::
:::

::: {.solution}
(a), (b) One formula, defined everywhere; \( \abs{x} \) is given by two cases that cover \( \nR \) and do not overlap. (c) \( 1/x \) exists exactly when \( x \ne 0 \). (d) For \( x \ge 0 \), \( \sqrt{x} \) is the unique \( b \ge 0 \) with \( b^2 = x \), which exists because \( \nR \) is a complete ordered field (@fd3:thm-reals-complete-ordered-field, @fd3:prp-cof-square-roots). (e) A restriction keeps the old values on the smaller domain. (f) Enlarging the codomain changes no value. (g) The two pieces are disjoint and cover \( \nR \), so they glue to one function, as in @fd2:exm-piecewise-as-gluing.
:::

The figure shows, from left to right, the graphs of \( \abs{x} \), \( 1/x \), \( \sqrt{x} \) and \( \ind_{[0, \infty)} \); an open dot marks a point that is not on the graph.

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.75]
  \begin{scope}
    \draw[->] (-1.6,0) -- (1.7,0); \draw[->] (0,-0.4) -- (0,1.8);
    \draw[thick] (-1.5,1.5) -- (0,0) -- (1.5,1.5);
    \node at (0,-0.9) {$|x|$ on $\mathbb{R}$};
  \end{scope}
  \begin{scope}[xshift=4cm]
    \draw[->] (-1.7,0) -- (1.7,0); \draw[->] (0,-1.8) -- (0,1.8);
    \draw[thick, domain=0.6:1.6, samples=30] plot (\x, {1/\x});
    \draw[thick, domain=-1.6:-0.6, samples=30] plot (\x, {1/\x});
    \node at (0,-2.2) {$1/x$ on $\mathbb{R} \setminus \{0\}$};
  \end{scope}
  \begin{scope}[xshift=8cm]
    \draw[->] (-0.4,0) -- (1.8,0); \draw[->] (0,-0.4) -- (0,1.8);
    \draw[thick, domain=0:1.6, samples=40] plot (\x, {sqrt(\x)});
    \node at (0.7,-0.9) {$\sqrt{x}$ on $[0, \infty)$};
  \end{scope}
  \begin{scope}[xshift=12cm]
    \draw[->] (-1.6,0) -- (1.7,0); \draw[->] (0,-0.4) -- (0,1.8);
    \draw[thick] (-1.5,0) -- (-0.06,0);
    \draw (0,0) circle (2pt);
    \fill (0,1) circle (2pt);
    \draw[thick] (0,1) -- (1.5,1);
    \node at (0,-0.9) {$\mathbf{1}_{[0,\infty)}$ on $\mathbb{R}$};
  \end{scope}
\end{tikzpicture}
\end{center}
```

Which subsets of the plane are graphs? Reading @fd2:def-function as a statement about vertical lines answers this.

::: {#prp-graph-vertical-line}
[Vertical Line Test]

Let \( D \subseteq \nR \) and \( G \subseteq \nR^2 \). Then \( G \) is the graph of a real function on \( D \) if and only if

::: {.enumerate options="label=(\roman*)"}
1. for every \( a \in D \) there is **exactly one** \( y \in \nR \) with \( (a, y) \in G \), and
2. every \( (a, y) \in G \) has \( a \in D \).
:::
:::

::: {.proof}
If \( G = \operatorname{graph} f \) for \( f \colon D \to \nR \), then (i) is the condition of @fd2:def-function, and (ii) holds because every element of \( G \) is a pair \( (x, f(x)) \) with \( x \in D \). Conversely, (ii) gives \( G \subseteq D \times \nR \), and with (i) the pair \( f \coloneqq (G, \nR) \) is a function \( D \to \nR \) by @fd2:def-function. Each \( (a, y) \in G \) has \( y = f(a) \) by the definition of the value, so \( G = \operatorname{graph} f \).
:::

In words: the vertical line through \( a \) meets \( G \) exactly once when \( a \in D \), and not at all when \( a \notin D \).

::: {.warning}
**No natural domain.** The function \( x \mapsto x^2/x \) on \( \nR \setminus \{0\} \) is the restriction of the identity of \( \nR \) to \( \nR \setminus \{0\} \); it is not the identity, because the domains differ. And not every curve is a graph: the circle \( \{ (x, y) \in \nR^2 : x^2 + y^2 = 1 \} \) contains \( (0, 1) \) and \( (0, -1) \), so (ii) forces \( 0 \in D \) and then (i) fails at \( 0 \), whatever \( D \) is.
:::

::: {.check}
Is each set a graph, and over which \( D \)? (1) \( \{ (x, y) : y = x^2 \} \); (2) \( \{ (x, y) : x = y^2 \} \); (3) \( \{ (x, y) : y \ge 0, \ x = y^2 \} \).
:::

::: {.solution}
(1) Yes, over \( \nR \). (2) No: \( (1, 1) \) and \( (1, -1) \) both lie in it, so (i) fails at \( 1 \), which (ii) puts in \( D \). (3) Yes, over \( [0, \infty) \): every element has \( x = y^2 \ge 0 \), and for \( a \ge 0 \) the only \( y \ge 0 \) with \( y^2 = a \) is \( \sqrt{a} \). It is the graph of \( \sqrt{\cdot} \).
:::

## Combining real functions

Two real functions with different domains can still be added; the sum lives where both are defined. Composition needs more care, because \( g(f(x)) \) needs \( f(x) \) to be an input of \( g \).

::: {#def-function-algebra}
[Operations on Real Functions]

Let \( f \colon D_f \to \nR \) and \( g \colon D_g \to \nR \) be real functions and \( c \in \nR \). On \( D_f \cap D_g \) define, for each \( x \),
\[
(f + g)(x) \coloneqq f(x) + g(x), \quad (fg)(x) \coloneqq f(x) g(x),
\]
and \( \max(f, g)(x) \coloneqq \max(f(x), g(x)) \), likewise \( \min(f, g) \). On \( D_f \) define \( (cf)(x) \coloneqq c f(x) \) and \( \abs{f}(x) \coloneqq \abs{f(x)} \). The quotient \( f/g \), \( x \mapsto f(x)/g(x) \), has domain \( \{ x \in D_f \cap D_g : g(x) \ne 0 \} \). The **composite** \( g \circ f \), \( x \mapsto g(f(x)) \), has domain
\[
\{ x \in D_f : f(x) \in D_g \} .
\]
:::

The composite is the composite of @fd2:def-composition in disguise. Write \( E \) for its domain. Every value of \( f|_E \) lies in \( D_g \), so \( f|_E \) may be regarded as a function \( E \to D_g \), and \( g \) after it is a composite in that sense, with values \( g(f(x)) \). Composition stays associative: \( h \circ (g \circ f) \) and \( (h \circ g) \circ f \) have the same domain and the same values \( h(g(f(x))) \), so they are equal, which is @fd2:prp-composition-associative for the restricted maps.

::: {.second-reading title="The two domains of a triple composite"}
Let \( h \colon D_h \to \nR \) as well. The domain of \( h \circ (g \circ f) \) is the set of \( x \) in the domain of \( g \circ f \) with \( g(f(x)) \in D_h \), that is, \( \{ x \in D_f : f(x) \in D_g, \ g(f(x)) \in D_h \} \). The domain of \( h \circ g \) is \( \{ y \in D_g : g(y) \in D_h \} \), so the domain of \( (h \circ g) \circ f \) is the set of \( x \in D_f \) with \( f(x) \) in it, which is the same set. On it both sides take the value \( h(g(f(x))) \), and @fd2:prp-function-equality gives equality.
:::

The domain of a composite can be empty. The square root after \( x \mapsto -x^2 - 1 \) has domain \( \{ x : -x^2 - 1 \ge 0 \} = \emptyset \): the composite is the empty function of @fd2:prp-empty-function, legal and useless.

::: {.check}
What is the domain of \( \sqrt{x} + 1/x \)? Of the composite of \( \sqrt{\cdot} \) after \( x \mapsto x - 1 \)?
:::

::: {.solution}
\( [0, \infty) \cap (\nR \setminus \{0\}) = (0, \infty) \). The composite has domain \( \{ x \in \nR : x - 1 \in [0, \infty) \} = [1, \infty) \).
:::

## Polynomial and rational functions

Chapter 6 defined, for a polynomial \( p \in \nR[x] \), its polynomial function \( c \mapsto p(c) \) on \( \nR \) (@def-polynomial-evaluation). In this chapter the letter \( x \) usually names a real number, so we write this function as \( x \mapsto p(x) \); the polynomial \( x \in \nR[x] \) has the identity as its function.

::: {#def-polynomial-rational-function}
[Polynomial Function, Rational Function]

Let \( D \subseteq \nR \). A **polynomial function on \( D \)** is the restriction to \( D \) of the polynomial function \( x \mapsto p(x) \) of some \( p \in \nR[x] \). For \( p, q \in \nR[x] \) with \( q \ne 0 \), the **rational function** \( p/q \) is \( x \mapsto p(x)/q(x) \) on \( \{ x \in \nR : q(x) \ne 0 \} \).
:::

Three facts about these functions were proved in Chapters 6 and 7 for every field, and \( \nR \) is a field; we cite them and prove nothing new.

- **Operations match.** The polynomial function of \( p + q \) is the sum of those of \( p \) and \( q \), and likewise for \( pq \): this is @prp-polynomial-function-map (b), and restricting to \( D \) keeps it.
- **The function determines the polynomial on an infinite set.** If \( D \) is infinite and \( p(x) = q(x) \) for every \( x \in D \), then \( p = q \): with \( n \coloneqq \max(\deg p, \deg q, 0) \), choose \( n + 1 \) distinct points of \( D \) (an infinite set has them, by the claim in the proof of @thm-polynomial-identity-from-values) and apply @thm-polynomial-identity-from-values (a). So on an interval with more than one point, the **degree** and **leading coefficient** of a polynomial function are well defined.
- **Few roots.** A non-zero \( q \) has at most \( \deg q \) roots (@thm-polynomial-root-count), so a rational function is defined at every real number except at most \( \deg q \) of them.

On a finite set the second fact fails: on \( D = \{0, 1\} \), the polynomials \( x^2 \) and \( x \) have the same function.

::: {.check}
Is \( \abs{x} \) on \( [0, \infty) \) a polynomial function? Are the rational function \( (x^2 - 1)/(x - 1) \) and the polynomial function \( x + 1 \) on \( \nR \) the same function?
:::

::: {.solution}
Yes: on \( [0, \infty) \), \( \abs{x} = x \), so it is the restriction of the identity, the function of the polynomial \( x \). No: their domains are \( \nR \setminus \{1\} \) and \( \nR \), although they agree at every point of \( \nR \setminus \{1\} \).
:::

## Moving a graph

Replacing \( f(x) \) by \( f(x - 1) \) moves a graph; the question is which way. Guessing from the sign gets it wrong half the time. A graph is a set of pairs, so the safe way is to test membership of a pair.

::: {#exm-method-graph-pairs}
[Method: reading a graph as a set of pairs]

**Template.** To prove that \( \operatorname{graph} g \) is \( \operatorname{graph} f \) moved by a bijection \( M \colon \nR^2 \to \nR^2 \), fix \( (x, y) \in \nR^2 \) and prove
\[
(x, y) \in \operatorname{graph} g \iff M^{-1}(x, y) \in \operatorname{graph} f ,
\]
by unwinding "\( (x, y) \in \operatorname{graph} g \)" into "\( x \in D_g \) and \( y = g(x) \)". Since \( M \) is a bijection, the right side says exactly that \( (x, y) \in M(\operatorname{graph} f) \).

**When to use it.** Shifts, reflections and stretches of graphs; symmetry of a graph; the graph of an inverse function in the next section.

**The usual failure.** Moving the wrong way: the formula for \( g \) contains \( M^{-1} \), while the picture moves by \( M \).
:::

For a set \( S \subseteq \nR^2 \) and \( (a, b) \in \nR^2 \), write \( S + (a, b) \coloneqq \{ (u + a, v + b) : (u, v) \in S \} \); for \( D \subseteq \nR \), write \( D + a \coloneqq \{ u + a : u \in D \} \), and \( -D \), \( cD \) as in @fd2:exm-sets-of-numbers-as-images.

::: {#prp-graph-transformations}
[Moving a Graph]

Let \( f \colon D \to \nR \), \( a, b \in \nR \) and \( c > 0 \).

::: {.enumerate options="label=(\alph*)"}
1. The function \( x \mapsto f(x - a) + b \) on \( D + a \) has graph \( \operatorname{graph} f + (a, b) \).
2. The function \( x \mapsto f(-x) \) on \( -D \) has graph \( \{ (-u, v) : (u, v) \in \operatorname{graph} f \} \), the reflection in the \( y \)-axis.
3. The function \( -f \) on \( D \) has graph \( \{ (u, -v) : (u, v) \in \operatorname{graph} f \} \), the reflection in the \( x \)-axis.
4. The function \( cf \) on \( D \) has graph \( \{ (u, cv) : (u, v) \in \operatorname{graph} f \} \), and \( x \mapsto f(x/c) \) on \( cD \) has graph \( \{ (cu, v) : (u, v) \in \operatorname{graph} f \} \).
:::
:::

::: {.idea}
[Scratch work]

We plan (a). Write \( g(x) \coloneqq f(x - a) + b \) on \( D + a \).

| Givens | Goal |
|---|---|
| \( f \colon D \to \nR \); \( g(x) = f(x - a) + b \) on \( D + a \) | \( (x, y) \in \operatorname{graph} g \iff (x - a, y - b) \in \operatorname{graph} f \) |
| \( (x, y) \in \operatorname{graph} g \): \( x \in D + a \), \( y = f(x - a) + b \) | \( x - a \in D \) and \( y - b = f(x - a) \) |

A naive guess first: "\( f(x - a) \) has a minus sign, so the graph moves left by \( a \)". Test it at \( f = \abs{\cdot} \), \( a = 1 \), \( b = 0 \). The vertex of \( \abs{x - 1} \) is where \( x - 1 = 0 \), at \( x = 1 \): the graph moved **right**. The table shows why. The move is \( M(u, v) = (u + a, v + b) \), and the formula evaluates \( f \) at the first coordinate of \( M^{-1}(x, y) = (x - a, y - b) \). The only gap left is \( x \in D + a \iff x - a \in D \), which is the definition of \( D + a \) read both ways.
:::

::: {.proof}
(a) Let \( g \) be the function in (a) and \( (x, y) \in \nR^2 \). By the definition of \( D + a \), \( x \in D + a \) if and only if \( x - a \in D \). So \( (x, y) \in \operatorname{graph} g \) if and only if \( x - a \in D \) and \( y - b = f(x - a) \), that is, \( (x - a, y - b) \in \operatorname{graph} f \). By the characteristic property of pairs (@fd2:def-ordered-pair), \( (x, y) = (u + a, v + b) \) holds exactly when \( (u, v) = (x - a, y - b) \); so the last condition says \( (x, y) \in \operatorname{graph} f + (a, b) \). This proves (a).

(b) \( (x, y) \) is on the graph if and only if \( -x \in D \) and \( y = f(-x) \), that is, \( (-x, y) \in \operatorname{graph} f \).

(c) \( (x, y) \in \operatorname{graph}(-f) \) if and only if \( x \in D \) and \( -y = f(x) \), that is, \( (x, -y) \in \operatorname{graph} f \).

(d) Since \( c \ne 0 \): \( (x, y) \in \operatorname{graph}(cf) \) if and only if \( (x, y/c) \in \operatorname{graph} f \); and \( (x, y) \) is on the graph of \( x \mapsto f(x/c) \) if and only if \( x/c \in D \) and \( y = f(x/c) \), that is, \( (x/c, y) \in \operatorname{graph} f \).
:::

The figure shows \( \abs{x} \) (dashed) and \( \abs{x - 1} - 2 \) on \( \nR \): by (a) with \( a = 1 \), \( b = -2 \), the vertex moves from \( (0, 0) \) to \( (1, -2) \), and the zeros are at \( -1 \) and \( 3 \).

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=0.8]
  \draw[->] (-2.6,0) -- (4.4,0) node[right] {$x$};
  \draw[->] (0,-2.6) -- (0,2.6) node[above] {$y$};
  \draw[dashed] (-2.4,2.4) -- (0,0) -- (2.4,2.4);
  \draw[thick] (-2.4,1.4) -- (1,-2) -- (4.2,1.2);
  \fill (1,-2) circle (2pt) node[below right] {$(1,-2)$};
  \node[below] at (-1,-0.05) {$-1$};
  \node[below] at (3,-0.05) {$3$};
\end{tikzpicture}
\end{center}
```

::: {.check}
Which function on \( \nR \) has graph \( (\operatorname{graph} \abs{\cdot}) + (-1, 2) \)?
:::

::: {.solution}
By (a) with \( a = -1 \) and \( b = 2 \), it is \( x \mapsto \abs{x + 1} + 2 \) on \( \nR + (-1) = \nR \). Its vertex is \( (-1, 2) \).
:::

## Even and odd functions

Two symmetries of a graph are common enough to have names. A set \( D \subseteq \nR \) is **symmetric** if \( -x \in D \) for every \( x \in D \); then \( -D = D \).

::: {#def-even-odd-function}
[Even and Odd Functions]

Let \( D \subseteq \nR \) be symmetric and \( f \colon D \to \nR \). Then \( f \) is **even** if \( f(-x) = f(x) \) for **every** \( x \in D \), and **odd** if \( f(-x) = -f(x) \) for **every** \( x \in D \).
:::

By @prp-graph-transformations (b), \( f \) is even exactly when its graph equals its reflection in the \( y \)-axis: both \( f \) and \( x \mapsto f(-x) \) have domain \( -D = D \), so they are equal exactly when their graphs are. The odd case is the method of @exm-method-graph-pairs once more, with \( M(u, v) = (-u, -v) \), which is its own inverse. For \( (x, y) \in \nR^2 \), the pair \( M(x, y) = (-x, -y) \) lies on the graph if and only if \( -x \in D \) and \( -y = f(-x) \). If \( f \) is odd, this says \( x \in D \) and \( y = f(x) \), so the graph is unchanged by \( M \). Conversely, if the graph is unchanged by \( M \), then for \( x \in D \) the point \( (-x, -f(x)) \) lies on it, so \( f(-x) = -f(x) \). The functions \( x^2 \), \( \abs{x} \) and the constants are even; \( x \), \( x^3 \) and \( 1/x \) on \( \nR \setminus \{0\} \) are odd; \( x + 1 \) on \( \nR \) is neither, since \( 0 \) at \( -1 \) is neither \( 2 \) nor \( -2 \). The zero function is both. An odd \( f \) with \( 0 \in D \) has \( f(0) = -f(0) \), so \( f(0) = 0 \).

Every function on a symmetric set splits into an even and an odd part, and only one way.

::: {#prp-even-odd-decomposition}
[Even and Odd Parts]

Let \( D \subseteq \nR \) be symmetric and \( f \colon D \to \nR \). There is **exactly one** pair of functions \( e, o \colon D \to \nR \) with \( e \) even, \( o \) odd and \( f = e + o \), namely
\[
e(x) = \frac{f(x) + f(-x)}{2}, \qquad o(x) = \frac{f(x) - f(-x)}{2} .
\]
:::

::: {.proof}
*Existence.* Replacing \( x \) by \( -x \) swaps \( f(x) \) and \( f(-x) \), so \( e(-x) = e(x) \) and \( o(-x) = -o(x) \); and \( e(x) + o(x) = f(x) \).

*Uniqueness.* Let \( f = e + o = e' + o' \) with \( e, e' \) even and \( o, o' \) odd, and put \( h \coloneqq e - e' = o' - o \). As a difference of even functions \( h \) is even, and as a difference of odd functions it is odd. So \( h(x) = h(-x) = -h(x) \), hence \( 2h(x) = 0 \) and \( h(x) = 0 \) for every \( x \in D \). Thus \( e = e' \) and \( o = o' \).
:::

For a polynomial function on \( \nR \) the even part keeps the even powers: \( (x + 1)^2 = x^2 + 2x + 1 \) has even part \( x^2 + 1 \) and odd part \( 2x \).

## Exercises

### A. Check your understanding

::: {#exr-real-functions-and-graphs-a1}
[A1]

Is each set a graph of a real function, and if so over which \( D \)?

::: {.enumerate options="label=(\alph*)"}
1. \( \{ (x, y) \in \nR^2 : x + y^2 = 0 \} \).
2. \( \{ (x, y) \in \nR^2 : y = \abs{x} \} \).
3. \( \{ (x, y) \in \nR^2 : x = 2 \} \).
4. \( \{ (x, y) \in \nR^2 : xy = 1 \} \).
:::
:::

::: {.solution}
We use @prp-graph-vertical-line. (a) No: \( (-1, 1) \) and \( (-1, -1) \) lie in the set, so \( -1 \in D \) by (ii), and (i) fails at \( -1 \). (b) Yes, over \( \nR \): it is \( \operatorname{graph} \abs{\cdot} \). (c) No: \( (2, 0) \) and \( (2, 1) \) lie in it. (d) Yes, over \( \nR \setminus \{0\} \): no pair has first coordinate \( 0 \), since \( 0 \cdot y = 0 \ne 1 \), and for \( a \ne 0 \) the only \( y \) with \( ay = 1 \) is \( 1/a \). It is the graph of \( 1/x \).
:::

::: {#exr-real-functions-and-graphs-a2}
[A2: Is this legal? Is it useful?]

Let \( f(x) = x - 1 \) on \( \nR \) and \( g(y) = 1/y \) on \( \nR \setminus \{0\} \).

::: {.enumerate options="label=(\alph*)"}
1. Find the domains of \( g \circ f \) and \( f \circ g \). Are the two composites equal?
2. Is the composite of \( g \) after the constant function \( 0 \) on \( \nR \) legal? Is it useful?
:::
:::

::: {.solution}
(a) By @def-function-algebra, \( g \circ f \) has domain \( \{ x \in \nR : x - 1 \ne 0 \} = \nR \setminus \{1\} \) and \( f \circ g \) has domain \( \{ y \in \nR \setminus \{0\} : 1/y \in \nR \} = \nR \setminus \{0\} \). They are not equal: the domains differ, and the values differ too, since \( g(f(2)) = 1 \) while \( f(g(2)) = -\tfrac12 \).

(b) Legal: its domain is \( \{ x \in \nR : 0 \in \nR \setminus \{0\} \} = \emptyset \), so it is the empty function (@fd2:prp-empty-function). It is useless: it has no values.
:::

### B. Practice

::: {#exr-real-functions-and-graphs-b1}
[B1]

Let \( f, g \colon D \to \nR \). Prove that \( \max(f, g) = \tfrac12 (f + g + \abs{f - g}) \) and \( \min(f, g) = \tfrac12 (f + g - \abs{f - g}) \).
:::

::: {.solution}
Both sides have domain \( D \); fix \( x \in D \). If \( f(x) \ge g(x) \), then \( \abs{f(x) - g(x)} = f(x) - g(x) \) by @fd3:def-absolute-value-ordered-field, so the right sides are \( \tfrac12 \cdot 2f(x) = f(x) = \max(f(x), g(x)) \) and \( \tfrac12 \cdot 2g(x) = g(x) = \min(f(x), g(x)) \). If \( f(x) < g(x) \), then \( \abs{f(x) - g(x)} = g(x) - f(x) \), and the right sides are \( g(x) \) and \( f(x) \), again the max and the min. The values agree at every \( x \), so the functions are equal.
:::

::: {#exr-real-functions-and-graphs-b2}
[B2]

Obtain the graph of \( x \mapsto 2\abs{x - 1} - 3 \) on \( \nR \) from that of \( \abs{\cdot} \) by @prp-graph-transformations, and find its vertex and its zeros.
:::

::: {.solution}
By (d) with \( c = 2 \), \( 2\abs{x} \) has graph \( \{ (u, 2v) \} \): stretch vertically by \( 2 \). By (a) with \( a = 1 \), \( b = -3 \), applied to \( 2\abs{\cdot} \), the function \( 2\abs{x - 1} - 3 \) has that graph moved right by \( 1 \) and down by \( 3 \). The vertex \( (0, 0) \) goes to \( (0, 0) \) and then to \( (1, -3) \). The zeros solve \( \abs{x - 1} = \tfrac32 \), so \( x = -\tfrac12 \) or \( x = \tfrac52 \).
:::

::: {#exr-real-functions-and-graphs-b3}
[B3]

Find the even and odd parts of \( f(x) = 1/(1 - x) \) on \( D = \nR \setminus \{-1, 1\} \). Why is \( -1 \) removed from \( D \)?
:::

::: {.solution}
For \( x \in D \), by @prp-even-odd-decomposition,
\[
\begin{aligned}
e(x) &= \tfrac12 \Bigl( \frac{1}{1 - x} + \frac{1}{1 + x} \Bigr) = \tfrac12 \cdot \frac{2}{1 - x^2} = \frac{1}{1 - x^2} , \\
o(x) &= \tfrac12 \Bigl( \frac{1}{1 - x} - \frac{1}{1 + x} \Bigr) = \tfrac12 \cdot \frac{2x}{1 - x^2} = \frac{x}{1 - x^2} .
\end{aligned}
\]
The formula \( 1/(1 - x) \) makes sense at \( -1 \), but @def-even-odd-function needs a symmetric domain: with \( 1 \) removed, \( -1 \) must go too.
:::

::: {#exr-real-functions-and-graphs-b4}
[B4: Prove or disprove]

Prove each true statement and refute each false one with a counterexample.

::: {.enumerate options="label=(\alph*)"}
1. The product of two odd functions on a symmetric \( D \) is even.
2. A function on a symmetric \( D \) that is both even and odd is the zero function.
3. The composite of two odd functions \( \nR \to \nR \) is odd.
4. The sum of an even and an odd function on \( \nR \) is never even.
:::
:::

::: {.solution}
(a) True: \( (fg)(-x) = (-f(x))(-g(x)) = f(x) g(x) \).

(b) True: \( f(x) = f(-x) = -f(x) \), so \( 2f(x) = 0 \), as in the uniqueness part of @prp-even-odd-decomposition.

(c) True: \( f(g(-x)) = f(-g(x)) = -f(g(x)) \).

(d) False: \( x^2 \) is even, the zero function is odd, and their sum \( x^2 \) is even.
:::

### C. Going deeper

::: {#exr-real-functions-and-graphs-c1}
[C1: Additive functions, used later]

Let \( f \colon \nR \to \nR \) satisfy \( f(x + y) = f(x) + f(y) \) for all \( x, y \in \nR \), and let \( c \coloneqq f(1) \). Prove:

::: {.enumerate options="label=(\alph*)"}
1. \( f(0) = 0 \), and \( f \) is odd;
2. \( f(nx) = n f(x) \) for every \( n \in \nZ \) and \( x \in \nR \);
3. \( f(q) = cq \) for every \( q \in \nQ \).
:::
:::

::: {.solution}
[Hint 1]

Choose \( x \) and \( y \) so that the equation speaks about \( f(0) \) alone.
:::

::: {.solution}
[Hint 2]

For (c), write \( q = m/n \) with \( m \in \nZ \), \( n \in \nZ_{>0} \), and compute \( n f(q) \) in two ways.
:::

::: {.solution}
(a) With \( x = y = 0 \), \( f(0) = 2f(0) \), so \( f(0) = 0 \). With \( y = -x \), \( f(x) + f(-x) = f(0) = 0 \), so \( f(-x) = -f(x) \).

(b) For \( n \in \nN \) we use induction (@fd1:ax-induction). For \( n = 0 \), \( f(0) = 0 = 0 \cdot f(x) \) by (a). If \( f(nx) = n f(x) \), then \( f((n + 1)x) = f(nx) + f(x) = (n + 1) f(x) \). For \( n < 0 \), \( -n \in \nN \), and by (a), \( f(nx) = -f((-n)x) = -(-n) f(x) = n f(x) \).

(c) Let \( q = m/n \) with \( m \in \nZ \) and \( n \in \nZ_{>0} \). By (b), applied twice, \( n f(q) = f(nq) = f(m \cdot 1) = m f(1) = mc \). Dividing by \( n \ne 0 \) gives \( f(q) = (m/n)c = cq \).

**Marking scheme.** (10 points)
- 2: obtains \( f(0) = 0 \) and oddness from suitable substitutions.
- 3: proves (b) for \( n \ge 0 \) by induction, with the step from the equation.
- 2: extends (b) to negative \( n \) by oddness.
- 3: computes \( n f(q) \) two ways and divides by \( n \ne 0 \).
Fatal errors (0 for the step): using \( f(qx) = q f(x) \) for rational \( q \) before proving it; assuming \( f \) is a polynomial or monotone.
:::

<!-- dependency ledger
def-real-function (claim): graph f equals the relation G of fd2's definition | fd2:def-function, the value f(x) being the unique y with (x, y) in G, recalled in prose
exm-first-real-functions (example): x != 0 is exactly when 1/x exists; the two cases of |x| cover R without overlap | field axioms of R (fd3:thm-reals-complete-ordered-field), trichotomy (fd3:prp-ordered-field-halves (a)), used silently
prp-graph-vertical-line (proof): the value f(a) is the unique y with (a, y) in G | fd2:def-function, recalled in the proof
prp-graph-transformations (proof): x in D + a iff x - a in D; x in cD iff x/c in D | definitions of D + a and cD, inline; c != 0 from c > 0
prp-graph-transformations (proof): (x, y) = (u + a, v + b) iff (u, v) = (x - a, y - b) | fd2:def-ordered-pair (cited) and arithmetic in R
prp-graph-transformations (example): vertex (1, -2) and zeros -1, 3 of |x - 1| - 2; check: |x + 1| + 2 | arithmetic; verify/ch08/prp-graph-transformations.py
def-function-algebra (claim): associativity of the extended composite: equal domains and values | second-reading fold, inline; fd2:prp-function-equality (cited)
def-polynomial-rational-function (claim): an infinite set contains n + 1 distinct elements | the claim in the proof of thm-polynomial-identity-from-values (b), cited by name
def-polynomial-rational-function (claim): R is a field, so Chapters 6-7 apply | fd3:thm-reals-complete-ordered-field (a complete ordered field is a field), used silently
def-polynomial-rational-function (claim): an interval with more than one point is infinite | between a < b lie the distinct points a + (b - a)/k, k in Z_{>0}; used silently
def-polynomial-rational-function (claim): on {0, 1}, x^2 and x have the same values | 0^2 = 0, 1^2 = 1, used silently
def-even-odd-function (claim): D symmetric implies -D = D; x + 1 at -1 is 0 | inline: -D is in D, and D = -(-D) is in -D
prp-even-odd-decomposition (proof): differences of even (odd) functions are even (odd); 2 != 0 in R | inline; 2 = 1 + 1 > 0 (fd3:prp-ordered-ring-rules), used silently
prp-even-odd-decomposition (example): (x + 1)^2 = x^2 + 2x + 1 | arithmetic; verify/ch08/prp-even-odd-decomposition.py
exr-real-functions-and-graphs-a1 (solution): 0 * y = 0 in R | fd3:prp-ring-algebra (b), used silently
exr-real-functions-and-graphs-a2 (solution): g(f(2)) = 1, f(g(2)) = -1/2 | arithmetic; verify/ch08/exr-real-functions-and-graphs-a2.py
exr-real-functions-and-graphs-b1 (solution): the two cases of the identity | fd3:def-absolute-value-ordered-field (cited); verify/ch08/exr-real-functions-and-graphs-b1.py
exr-real-functions-and-graphs-b2 (solution): vertex (1, -3), zeros -1/2 and 5/2 | arithmetic; verify/ch08/exr-real-functions-and-graphs-b2.py
exr-real-functions-and-graphs-b3 (solution): the even and odd parts of 1/(1 - x) | field arithmetic; verify/ch08/exr-real-functions-and-graphs-b3.py
exr-real-functions-and-graphs-c1 (solution): every rational is m/n with m in Z, n in Z_{>0}; Q inside R; Z = N together with the negatives of N | fd3 construction of Q (fd3:thm-rationals-embed-ordered-field) and of Z, used silently
-->
