# Injections and Surjections

Section 2.1 defined functions and composed them. This section asks the two basic questions about a function, and gives each its method of proof and its way of failing. We then ask what composition does to the two properties, and find the half of each converse that survives. After the maps that every subset, product and power set carries, and a set of examples from arithmetic and calculus, we read injectivity and surjectivity in a second way: as permission to cancel \( f \) from an equation between composites.

## Injective, surjective, bijective

Two questions can be asked of any function \( f \colon X \to Y \), and much of mathematics turns on them. First: can we recover the input from the output, or can two different inputs give the same output? Second: is every point of the codomain an output? The first question is about how \( f \) treats \( X \); the second is about how it covers \( Y \).

### Injective functions

*An injective function never sends two different inputs to the same output.*

::: {#def-injective}
[Injective]

A function \( f \colon X \to Y \) is **injective** (an **injection**, or **one-to-one**) if, **for all** \( x_1, x_2 \in X \), \( f(x_1) = f(x_2) \) implies \( x_1 = x_2 \). In symbols:
\[
\forall x_1 \in X \ \ \forall x_2 \in X \ \ \bigl( f(x_1) = f(x_2) \to x_1 = x_2 \bigr) .
\]
:::

In words: if two inputs give the same output, they were the same input. By @fd1:prp-contrapositive, the definition gives the **contrapositive form**
\[
\forall x_1 \in X \ \ \forall x_2 \in X \ \ \bigl( x_1 \ne x_2 \to f(x_1) \ne f(x_2) \bigr) :
\]
different inputs give different outputs. The two forms are equivalent; the way back, from the contrapositive form to the definition, is @fd1:prp-contrapositive-converse, which uses \( \rulename{RAA} \). A proof of injectivity usually uses the form of the definition, because an equation \( f(x_1) = f(x_2) \) is something to compute with, while an inequation \( x_1 \ne x_2 \) is not.

The negation is found by the laws of *Logic and Proof*, Chapter 6 for negating bounded quantifiers and implications: "\( f \) is **not** injective" is
\[
\exists x_1 \in X \ \ \exists x_2 \in X \ \ \bigl( f(x_1) = f(x_2) \wedge x_1 \ne x_2 \bigr) .
\]
So a failure of injectivity is shown by **two witnesses**: two different inputs with the same output.

### Surjective functions

*A surjective function reaches every point of its codomain.*

::: {#def-surjective}
[Surjective]

A function \( f \colon X \to Y \) is **surjective** (a **surjection**, or **onto**) if, **for every** \( y \in Y \), **there exists** \( x \in X \) with \( f(x) = y \). In symbols:
\[
\forall y \in Y \ \ \exists x \in X \ \ f(x) = y .
\]
:::

In words: every point of the codomain is an output; equivalently, the range of \( f \) is all of \( Y \). An \( x \) with \( f(x) = y \) is called a **preimage** of \( y \). The definition does not ask for the preimage to be unique. Negating as before, "\( f \) is **not** surjective" is
\[
\exists y \in Y \ \ \forall x \in X \ \ f(x) \ne y ,
\]
so a failure of surjectivity is shown by **one witness**: a point of the codomain that no input reaches.

Surjectivity depends on the codomain, which is why @def-function records it: \( s_1 \) and \( s_2 \) of @exm-equal-functions have the same graph, and we shall see that \( s_2 \) is surjective and \( s_1 \) is not.

::: {.warning}
Surjectivity cannot be checked by trying some \( y \). The function \( f \colon \nR \to \nR \), \( f(x) = x^2 + x \), reaches \( 0 = f(0) \), \( 2 = f(1) \), \( 6 = f(2) \), and \( 12 = f(3) \), and a reader who tries these may believe it reaches everything. It does not reach \( -1 \): \( x^2 + x = -1 \) would mean \( x^2 + x + 1 = 0 \), but \( x^2 + x + 1 = (x + \tfrac12)^2 + \tfrac34 > 0 \) for every real \( x \). Concluding "for every \( y \)" from a few instances is entry (N1) of the catalogue in *Logic and Proof*, Chapter 8.
:::

### Bijective functions

::: {#def-bijective}
[Bijective]

A function is **bijective** (a **bijection**) if it is both injective and surjective.
:::

A bijection is a function in which every point of the codomain is reached **exactly once**: for every \( y \in Y \) there is exactly one \( x \in X \) with \( f(x) = y \). This is the \( \exists! \) of @def-function again, now read from the codomain side, and its two halves are the two properties.

::: {.second-reading title="Why a bijection reaches each point once"}
In the terms of @exm-method-uniqueness, the two halves are these. Existence of such an \( x \), for every \( y \), is surjectivity. Uniqueness is injectivity: if \( f(x_1) = y = f(x_2) \), injectivity gives \( x_1 = x_2 \); and conversely, if every \( y \) has at most one preimage, then \( f(x_1) = f(x_2) \) makes \( x_1 \) and \( x_2 \) two preimages of the same point \( y \coloneqq f(x_1) \), so \( x_1 = x_2 \).
:::

### Worked examples

::: {#exm-method-injectivity}
[Method: proving injectivity]

**Template.** "Let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \)." Compute until \( x_1 = x_2 \). To refute injectivity, name two different inputs with one output.

**When to use it.** Any claim that \( f \) is injective. The equation form of @def-injective is the one to compute with, as the paragraph after the definition explains.

**The usual failure.** Starting from \( x_1 = x_2 \) and reaching \( f(x_1) = f(x_2) \), which proves the wrong implication (entry (N5) of @fd1:exm-not-allowed-catalogue; a warning below shows it on squaring); or assuming \( x_1 \ne x_2 \) and never using it.
:::

::: {#exm-method-surjectivity}
[Method: proving surjectivity]

**Template.** On scrap paper, solve \( f(x) = y \) for \( x \), working **backwards**, and note what the solving needed. The proof runs **forwards**: "Let \( y \in Y \). Put \( x \coloneqq \dots \)", check \( x \in X \), check \( f(x) = y \). To refute surjectivity, name one \( y \in Y \) and show that \( f(x) = y \) has no solution in \( X \).

**When to use it.** Any claim that \( f \) is surjective.

**The usual failure.** Writing the scratch work as the proof, so that the proof assumes \( y = f(x) \) and never checks that the \( x \) it found lies in \( X \); and testing a few \( y \) (entry (N1), the warning after @def-surjective).
:::

The two methods meet in one function whose surjectivity has to be found, not guessed.

::: {#exm-fraction-map}
[Solving backwards, proving forwards]

Let \( f \colon \nR \to (-1, 1) \), \( f(x) = x/(1 + \abs{x}) \). Show that \( f \) is a function, and that it is injective and surjective.
:::

::: {.idea}
[Scratch work]

*A function into \( (-1, 1) \).* The denominator is safe, since \( 1 + \abs{x} \ge 1 > 0 \), and \( \abs{f(x)} = \abs{x}/(1 + \abs{x}) < 1 \). Note also that \( f(x) \) has the sign of \( x \), and \( f(0) = 0 \).

*Injectivity.* If \( f(x_1) = f(x_2) \), then \( x_1 \) and \( x_2 \) have the same sign. In each case \( \abs{x} \) is \( x \) or \( -x \) for both, and clearing denominators should finish it.

*Surjectivity, backwards.* The absolute value suggests cases on the sign of \( y \) (@exm-method-cases). For \( y \ge 0 \), look for \( x \ge 0 \):
\[
y = \frac{x}{1 + x} \iff y + yx = x \iff x = \frac{y}{1 - y} .
\]
For \( y < 0 \), look for \( x < 0 \):
\[
y = \frac{x}{1 - x} \iff y - yx = x \iff x = \frac{y}{1 + y} .
\]
Both answers are \( x = y/(1 - \abs{y}) \), one formula, and it needs \( \abs{y} \ne 1 \). That is why the codomain is the open interval. As givens and goal:

| Givens | Goal |
|---|---|
| \( y \in (-1, 1) \) | some \( x \in \nR \) with \( x/(1 + \abs{x}) = y \) |
| \( x \coloneqq y/(1 - \abs{y}) \), defined since \( \abs{y} < 1 \) | \( f(x) = y \): the one check left |
:::

::: {.solution}
*Function.* For every real \( x \), \( 1 + \abs{x} > 0 \), and \( \abs{f(x)} = \abs{x}/(1 + \abs{x}) < 1 \), so \( f(x) \in (-1, 1) \).

*Injective.* Let \( f(x_1) = f(x_2) \). Since \( f(x) \) has the sign of \( x \), \( x_1 \) and \( x_2 \) are both \( \ge 0 \) or both \( < 0 \). In the first case \( x_1/(1 + x_1) = x_2/(1 + x_2) \) gives \( x_1 + x_1 x_2 = x_2 + x_1 x_2 \), so \( x_1 = x_2 \). In the second, \( x_1/(1 - x_1) = x_2/(1 - x_2) \) gives \( x_1 - x_1 x_2 = x_2 - x_1 x_2 \), so \( x_1 = x_2 \) in the same way.

*Surjective.* Let \( y \in (-1, 1) \) and put \( x \coloneqq y/(1 - \abs{y}) \), a real number since \( 1 - \abs{y} > 0 \). Then \( \abs{x} = \abs{y}/(1 - \abs{y}) \), so \( 1 + \abs{x} = 1/(1 - \abs{y}) \), and
\[
f(x) = \frac{x}{1 + \abs{x}} = x\,(1 - \abs{y}) = y .
\]
:::

The order is the one the box prescribes. The solving went backwards and needed two cases; the proof goes forwards, states one formula for \( x \), and checks it once.

::: {.check}
Show that \( n \mapsto 5n - 2 \), as a function \( \nZ \to \nZ \), is injective and not surjective.
:::

::: {.solution}
*Injective:* \( 5n_1 - 2 = 5n_2 - 2 \) gives \( 5n_1 = 5n_2 \), so \( n_1 = n_2 \). *Not surjective:* the witness is \( 0 \). The equation \( 5n - 2 = 0 \) means \( 5n = 2 \), and no integer solves it: if \( n \ge 1 \), then \( 5n \ge 5 \); if \( n \le 0 \), then \( 5n \le 0 \).
:::

::: {#exm-injective-surjective-first}
[Deciding injective and surjective]

For each function below, decide with proof whether it is injective and whether it is surjective.

(a) \( f \colon \nR \to \nR \), \( f(x) = 3x - 5 \).

(b) \( g \colon \nZ \to \nZ \), \( g(n) = 3n \).

(c) \( h \colon \{1, 2, 3\} \to \{a, b\} \), with \( h(1) = a \), \( h(2) = b \), \( h(3) = a \).

(d) \( k \colon \{1, 2\} \to \{a, b, c\} \), with \( k(1) = a \), \( k(2) = c \).
:::

::: {.solution}
(a) *Injective.* Let \( x_1, x_2 \in \nR \) with \( 3x_1 - 5 = 3x_2 - 5 \). Adding \( 5 \) and dividing by \( 3 \) gives \( x_1 = x_2 \).

*Surjective.* On scrap paper, \( 3x - 5 = y \) gives \( x = (y + 5)/3 \). Now the proof: let \( y \in \nR \), and put \( x \coloneqq (y + 5)/3 \). Then \( x \in \nR \), and \( f(x) = 3 \cdot \frac{y + 5}{3} - 5 = y \). So \( f \) is bijective.

(b) *Injective.* Let \( n_1, n_2 \in \nZ \) with \( 3n_1 = 3n_2 \). Dividing by \( 3 \) gives \( n_1 = n_2 \).

*Not surjective.* The witness is \( 1 \in \nZ \). If \( n \ge 1 \), then \( 3n \ge 3 \); if \( n \le 0 \), then \( 3n \le 0 \). So \( 3n \ne 1 \) for every integer \( n \), and \( 1 \) has no preimage. (Solving \( 3n = 1 \) gives \( n = \tfrac13 \), which is not in the domain \( \nZ \): the same formula on \( \nQ \) would be surjective.)

(c) *Not injective:* \( h(1) = a = h(3) \) and \( 1 \ne 3 \). *Surjective:* the codomain has two points, and \( a = h(1) \), \( b = h(2) \). For a finite codomain, checking every point **is** a proof: the instances are all the cases.

(d) *Injective:* the two inputs have the different outputs \( a \ne c \), and there are no other pairs of different inputs to check. *Not surjective:* \( b \) is not an output, since the only outputs are \( k(1) = a \) and \( k(2) = c \).
:::

Parts (c) and (d) show two more things. A function from a three-element set to a two-element set cannot be injective, and one from a two-element set to a three-element set cannot be surjective: there are too many inputs in the first case and too few in the second.

::: {.second-reading title="Drawing finite pictures"}
And the finite pictures are worth drawing: two columns of dots, with an arrow from each input to its output. Injective means no dot on the right receives two arrows; surjective means every dot on the right receives at least one.
:::

The key example of the section is one formula read as three different functions.

::: {#exm-square-three-ways}
[Squaring, three ways]

For each of the three functions, settle both questions: injective or not, surjective or not.

(a) \( q_1 \colon \nR \to \nR \), \( q_1(x) = x^2 \).

(b) \( q_2 \colon [0, \infty) \to \nR \), \( q_2(x) = x^2 \).

(c) \( q_3 \colon [0, \infty) \to [0, \infty) \), \( q_3(x) = x^2 \).
:::

::: {.solution}
(a) *Not injective:* \( q_1(1) = 1 = q_1(-1) \) and \( 1 \ne -1 \). *Not surjective:* the witness is \( -1 \in \nR \), since \( x^2 \ge 0 > -1 \) for every real \( x \). So \( q_1 \) is neither.

(b) *Injective.* Let \( x_1, x_2 \ge 0 \) with \( x_1^2 = x_2^2 \). Then \( x_1^2 \le x_2^2 \), so \( x_1 \le x_2 \) by @fd1:thm-squares-order, which applies since both numbers are nonnegative; and likewise \( x_2 \le x_1 \). Hence \( x_1 = x_2 \). *Not surjective:* the witness \( -1 \) still works, for the same reason.

(c) *Injective*, by the same proof as in (b): injectivity concerns only the domain and the values, and these are the same as for \( q_2 \). *Surjective.* Let \( y \in [0, \infty) \). A nonnegative real number has a nonnegative square root, so put \( x \coloneqq \sqrt{y} \). Then \( x \in [0, \infty) \) and \( q_3(x) = (\sqrt{y})^2 = y \). So \( q_3 \) is bijective.

The same rule gives three different functions. Shrinking the domain from \( \nR \) to \( [0, \infty) \) removed the two witnesses \( \pm 1 \) against injectivity. Shrinking the codomain to \( [0, \infty) \) removed the witness \( -1 \) against surjectivity. The graphs of \( q_2 \) and \( q_3 \) are the same set; only the declared codomain differs, and surjectivity changes with it.
:::

::: {.warning}
Injectivity is not the defining property of a function read backwards. Every function satisfies "if \( x_1 = x_2 \), then \( f(x_1) = f(x_2) \)": equal inputs give equal outputs, which is part of \( f(x) \) being well defined. Injectivity is the **converse**, "if \( f(x_1) = f(x_2) \), then \( x_1 = x_2 \)". A "proof" of injectivity that starts from \( x_1 = x_2 \) and reaches \( f(x_1) = f(x_2) \) has proved the wrong implication, entry (N5) of *Logic and Proof*, Chapter 8's catalogue, and it "proves" \( q_1 \) injective, which is false.
:::

::: {.check}
Is \( n \mapsto n + 1 \) surjective as a function \( \nN \to \nN \)? As a function \( \nZ \to \nZ \)?
:::

::: {.solution}
On \( \nN \): no. The witness is \( 0 \), since \( n + 1 \ge 1 \) for every \( n \in \nN \), so \( n + 1 = 0 \) has no solution in \( \nN \). On \( \nZ \): yes. For \( m \in \nZ \), the integer \( m - 1 \) satisfies \( (m - 1) + 1 = m \). Both functions are injective, since \( n_1 + 1 = n_2 + 1 \) gives \( n_1 = n_2 \).
:::

## Composites of injections and surjections

Both properties survive composition. This is the first theorem about functions whose proof uses the definitions and nothing else, and it shows the two proof shapes of the last subsection working together.

::: {#thm-composition-injective-surjective}
[Composites of Injections and Surjections]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

(a) If \( f \) and \( g \) are injective, then \( g \circ f \) is injective.

(b) If \( f \) and \( g \) are surjective, then \( g \circ f \) is surjective.

(c) If \( f \) and \( g \) are bijective, then \( g \circ f \) is bijective.
:::

::: {.idea}
For (a), start from equal outputs of \( g \circ f \). They are equal outputs of \( g \), at the points \( f(x_1) \) and \( f(x_2) \); peel off \( g \) by its injectivity, then \( f \) by its. For (b), work backwards along the chain \( X \to Y \to Z \): to reach \( z \in Z \), first find a point of \( Y \) that \( g \) sends to \( z \), then a point of \( X \) that \( f \) sends there. Part (c) is (a) and (b) together.
:::

::: {.proof}
(a) Let \( x_1, x_2 \in X \) with \( (g \circ f)(x_1) = (g \circ f)(x_2) \), that is, \( g(f(x_1)) = g(f(x_2)) \) by @def-composition. The points \( f(x_1) \) and \( f(x_2) \) lie in \( Y \), and \( g \) is injective, so \( f(x_1) = f(x_2) \) [\( \rulename{\forall E} \), \( \rulename{{\to}E} \): injectivity of \( g \) at \( f(x_1), f(x_2) \)]. Since \( f \) is injective, \( x_1 = x_2 \) [\( \rulename{\forall E} \), \( \rulename{{\to}E} \): injectivity of \( f \) at \( x_1, x_2 \)]. So \( g \circ f \) is injective.

(b) Let \( z \in Z \). Since \( g \) is surjective, there is \( y \in Y \) with \( g(y) = z \) [\( \rulename{\exists E} \): the name \( y \) is fresh]. Since \( f \) is surjective, there is \( x \in X \) with \( f(x) = y \) [\( \rulename{\exists E} \): \( x \) is fresh]. Then
\[
(g \circ f)(x) = g(f(x)) = g(y) = z ,
\]
so \( z \) has the preimage \( x \) under \( g \circ f \) [\( \rulename{\exists I} \), witness \( x \)]. Since \( z \in Z \) was arbitrary, \( g \circ f \) is surjective.

(c) If \( f \) and \( g \) are bijective, they are injective and surjective, so \( g \circ f \) is injective by (a) and surjective by (b), that is, bijective.
:::

::: {.second-reading title="Part (a) as a derivation"}
Part (a) is short enough to see whole at level 0 of *Logic and Proof*, Section 8.3, a full derivation. Here is its derivation, with the quantifiers bounded and handled by the bounded rules (@fd1:prp-bounded-quantifier-rules), and \( (g \circ f)(u) \) already unwound to \( g(f(u)) \) by @def-composition. Premises 1 and 2 are the injectivity of \( f \) and of \( g \); premise 3 says that \( f \) maps \( X \) into \( Y \), which the prose used in the clause "the points \( f(x_1) \) and \( f(x_2) \) lie in \( Y \)".

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall u \in X\, \forall v \in X\, (f(u) = f(v) \to u = v)}
  \hypo {2} {\forall u \in Y\, \forall v \in Y\, (g(u) = g(v) \to u = v)}
  \hypo {3} {\forall u \in X\, f(u) \in Y}
  \open[x_1]
  \hypo {4} {x_1 \in X}
  \open[x_2]
  \hypo {5} {x_2 \in X}
  \open
  \hypo {6} {g(f(x_1)) = g(f(x_2))}
  \have {7} {f(x_1) \in Y} \Ae{3,4}
  \have {8} {f(x_2) \in Y} \Ae{3,5}
  \have {9} {\forall v \in Y\, (g(f(x_1)) = g(v) \to f(x_1) = v)} \Ae{2,7}
  \have {10} {g(f(x_1)) = g(f(x_2)) \to f(x_1) = f(x_2)} \Ae{9,8}
  \have {11} {f(x_1) = f(x_2)} \ie{10,6}
  \have {12} {\forall v \in X\, (f(x_1) = f(v) \to x_1 = v)} \Ae{1,4}
  \have {13} {f(x_1) = f(x_2) \to x_1 = x_2} \Ae{12,5}
  \have {14} {x_1 = x_2} \ie{13,11}
  \close
  \have {15} {g(f(x_1)) = g(f(x_2)) \to x_1 = x_2} \ii{6-14}
  \close
  \have {16} {\forall v \in X\, (g(f(x_1)) = g(f(v)) \to x_1 = v)} \Ai{5-15}
  \close
  \have {17} {\forall u \in X\, \forall v \in X\, (g(f(u)) = g(f(v)) \to u = v)} \Ai{4-16}
\end{nd}$
\end{center}
```

Compare it with the prose of (a). "Let \( x_1, x_2 \in X \)" opens the two flagged boxes of lines 4 and 5, and "with \( g(f(x_1)) = g(f(x_2)) \)" is the assumption of line 6. The first tagged sentence is lines 7–11, and the second is lines 12–14. The closing "so \( g \circ f \) is injective" stands for lines 15–17, the closing lines of \( \rulename{{\to}I} \) and of the two \( \rulename{\forall I} \)'s; by the convention of *Logic and Proof*, Chapter 8 on silent steps, the prose may state their result without naming them. The two tags in the prose mark the only steps where a hypothesis is used, and that is what the proof is about.
:::

::: {.second-reading title="Each hypothesis is needed"}
**Each hypothesis is needed.** In (a), dropping the injectivity of \( g \) breaks the conclusion: with \( f = \id_{\nR} \) and \( g = q_1 \), squaring on \( \nR \), the composite \( g \circ f = q_1 \) is not injective, although \( f \) is. Dropping the injectivity of \( f \) instead, with \( f = q_1 \) and \( g = \id_{\nR} \), gives the same composite. In (b), with \( f = \id_{\nR} \) and \( g = q_1 \), the composite \( q_1 \) is not surjective, although \( f \) is; with \( f = q_1 \) and \( g = \id_{\nR} \), again \( g \circ f = q_1 \) is not surjective, although \( g \) is.
:::

The converses fail. If \( g \circ f \) is injective, \( g \) need not be: take \( f \colon \{1\} \to \{1, 2\} \), \( f(1) = 1 \), and the constant function \( g \colon \{1, 2\} \to \{1\} \). Then \( g \circ f = \id_{\{1\}} \), a bijection, while \( g \) is not injective, since \( g(1) = g(2) \), and \( f \) is not surjective, since \( 2 \) is not a value. Half of each converse survives.

::: {#prp-composite-partial-converse}
[Partial Converses for Composites]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

(a) If \( g \circ f \) is injective, then \( f \) is injective.

(b) If \( g \circ f \) is surjective, then \( g \) is surjective.
:::

::: {.idea}
For (a), equal values of \( f \) stay equal after \( g \) is applied, and then the injectivity of \( g \circ f \) takes over. For (b), a preimage of \( z \) under \( g \circ f \) gives one under \( g \), by passing through \( f \). The example above shows that neither half can be swapped: there \( g \circ f \) is bijective, \( g \) is not injective, and \( f \) is not surjective.
:::

::: {.proof}
(a) Suppose \( g \circ f \) is injective. Let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \); we must show \( x_1 = x_2 \). Applying \( g \) to both sides gives \( g(f(x_1)) = g(f(x_2)) \), because a function gives equal outputs at equal inputs. By @def-composition, this says \( (g \circ f)(x_1) = (g \circ f)(x_2) \). Since \( g \circ f \) is injective, \( x_1 = x_2 \). So \( f \) is injective.

(b) Let \( z \in Z \). Since \( g \circ f \) is surjective, there is \( x \in X \) with \( (g \circ f)(x) = z \). Let \( y \coloneqq f(x) \), an element of \( Y \). Then \( g(y) = g(f(x)) = (g \circ f)(x) = z \), by @def-composition. So \( z \) has a preimage under \( g \), namely \( y \). Since \( z \) was arbitrary, \( g \) is surjective.
:::

Section 2.4 builds on this: a function \( f \) with a function \( g \) such that \( g \circ f = \id_X \) is forced to be injective.

## Structure maps

Every subset, product and power set comes with maps of its own. They are the first test cases for the two questions, and the answers depend on the sets involved, sometimes only on whether a set is empty.

::: {#exm-structure-maps}
[The maps that come with sets]

Let \( X \) and \( Y \) be sets, and \( A \subseteq X \). Decide whether each of the following maps is injective and whether it is surjective.

(a) The **inclusion map** \( A \to X \), \( a \mapsto a \).

(b) The **projection** \( p_1 \colon X \times Y \to X \), \( p_1(x, y) = x \).

(c) The **diagonal map** \( \delta_X \colon X \to X \times X \), \( \delta_X(x) = (x, x) \).

(d) The **complement map** \( c \colon \powerset{X} \to \powerset{X} \), \( c(S) = X \setminus S \).
:::

::: {.solution}
(a) *Injective:* the value at a point of \( A \) is the point itself, so equal values come from equal points. *Surjective exactly when \( A = X \).* The values are the points of \( A \), so every \( x \in X \) is a value if and only if \( X \subseteq A \), that is, since \( A \subseteq X \), if and only if \( A = X \).

(b) *Surjective exactly when \( Y \) has an element or \( X = \emptyset \).* If \( y_0 \in Y \), then each \( x \in X \) is the value \( p_1(x, y_0) \). If \( X = \emptyset \), there is no point of \( X \) to reach, and \( p_1 \) is surjective vacuously. If \( Y = \emptyset \) and \( X \) has an element \( x_0 \), then \( X \times Y = \emptyset \) (@prp-product-set-laws), so \( p_1 \) has no values at all, and it misses \( x_0 \). Injectivity of \( p_1 \) is the Quick check below. The second projection \( p_2 \colon X \times Y \to Y \), \( p_2(x, y) = y \), behaves in the same way, with the roles of \( X \) and \( Y \) exchanged.

(c) *Injective:* if \( (x, x) = (x', x') \), then \( x = x' \) by @def-ordered-pair. *Not surjective as soon as \( X \) has two points* \( x \ne x' \): the pair \( (x, x') \) is not a value, since \( (z, z) = (x, x') \) would give \( x = z = x' \). If \( X \) has at most one element, \( \delta_X \) is surjective, and so bijective: \( X \times X \) is \( \emptyset \) or \( \{ (x, x) \} \), and each of its pairs is a value.

(d) *Bijective.* We write \( S \), \( T \) for subsets of \( X \), to keep them apart from the fixed \( A \). First, \( c(c(S)) = S \) for every \( S \subseteq X \). Let \( x \) be arbitrary. By a chain of equivalences (@exm-method-chain-of-iff),
\[
\begin{aligned}
&x \in X \setminus (X \setminus S) \\
&\quad\iff x \in X \wedge \neg(x \in X \wedge x \notin S) && \text{[definition of } \setminus \text{, twice]} \\
&\quad\iff x \in X \wedge (x \notin X \vee x \in S) && \text{[De Morgan; double negation]} \\
&\quad\iff x \in X \wedge x \in S && \text{[drop the disjunct } x \notin X \text{]} \\
&\quad\iff x \in S && \text{[} S \subseteq X \text{]}
\end{aligned}
\]
The second line is De Morgan (d), (c) (@fd1:prp-de-morgan) applied to the second conjunct, together with \( \neg\neg(x \in S) \dashv\vdash x \in S \) (@fd1:prp-double-negation); from left to right both steps use \( \rulename{RAA} \). In the third line, from left to right, the disjunct \( x \notin X \) clashes with the conjunct \( x \in X \), so disjunctive syllogism (@fd1:prp-disjunctive-syllogism) leaves \( x \in S \); from right to left, \( \rulename{\vee I} \) puts the disjunct back. In the last line, from right to left, \( x \in S \) gives \( x \in X \) because \( S \subseteq X \). By @def-set-equality, \( X \setminus (X \setminus S) = S \).

Now \( c \) is injective: if \( c(S) = c(T) \), then \( S = c(c(S)) = c(c(T)) = T \). And \( c \) is surjective: each \( T \subseteq X \) is the value of \( c \) at \( c(T) \), since \( c(c(T)) = T \).

So \( c \circ c = \id_{\powerset{X}} \) (@prp-function-equality): applying \( c \) twice changes nothing.
:::

::: {.check}
When is the projection \( p_1 \colon X \times Y \to X \) injective?
:::

::: {.solution}
Exactly when \( X = \emptyset \) or \( Y \) has at most one element. If \( x \in X \) and \( y \ne y' \) in \( Y \), then \( (x, y) \ne (x, y') \) (@def-ordered-pair), and both have the value \( x \): two witnesses against injectivity. If \( X = \emptyset \), then \( X \times Y = \emptyset \) (@prp-product-set-laws), and \( p_1 \) is the empty function, injective vacuously. If \( Y \) has at most one element and \( p_1(x, y) = p_1(x', y') \), then \( x = x' \), and \( y = y' \) because both lie in \( Y \); so \( (x, y) = (x', y') \).
:::

## Examples from algebra and calculus

The methods of the first subsection now meet maps from school mathematics. Three times below, a single feature decides an answer: a coefficient, a theorem of Chapter 1, and an order property.

::: {#exm-maps-from-algebra}
[Maps from arithmetic]

Decide whether each map is injective and whether it is surjective.

(a) For integers \( a \ne 0 \) and \( b \), the map \( \nZ \to \nZ \), \( n \mapsto an + b \).

(b) The map \( \nN \times \nN \to \nN \), \( (m, n) \mapsto mn \).

(c) The map \( \varphi \colon \nZ \times \{0, 1\} \to \nZ \), \( \varphi(q, r) = 2q + r \).
:::

::: {.solution}
(a) The maps \( n \mapsto 3n \) and \( n \mapsto 5n - 2 \) of the first subsection generalize. *Injective:* \( an_1 + b = an_2 + b \) gives \( a(n_1 - n_2) = 0 \), so \( n_1 = n_2 \), since \( a \ne 0 \) and a product of integers is \( 0 \) only if a factor is. *Surjective exactly when \( a = 1 \) or \( a = -1 \).* If \( a = \pm 1 \), then \( a^2 = 1 \); for \( m \in \nZ \) put \( n \coloneqq a(m - b) \), and then \( an + b = a^2 (m - b) + b = m \). If \( a \ne \pm 1 \), then \( \abs{a} \ge 2 \), and \( b + 1 \) is not a value: \( an + b = b + 1 \) means \( an = 1 \), which is false for \( n = 0 \), and false for \( n \ne 0 \) because then \( \abs{an} = \abs{a} \abs{n} \ge 2 \).

(b) *Surjective:* each \( k \in \nN \) is the value at \( (k, 1) \). *Not injective:* \( (1, 2) \ne (2, 1) \) (@def-ordered-pair), and both are sent to \( 2 \). Any formula symmetric in \( m \) and \( n \) fails injectivity in the same way; the sum \( (m, n) \mapsto m + n \) is Exercise B1 (b).

(c) *Surjective:* by @thm-even-or-odd, every \( n \in \nZ \) is \( 2k \) or \( 2k + 1 \) for some \( k \in \nZ \), that is, \( \varphi(k, 0) \) or \( \varphi(k, 1) \). *Injective:* let \( 2q + r = 2q' + r' \). If \( r = r' \), then \( 2q = 2q' \), so \( q = q' \), and the pairs are equal (@def-ordered-pair). If \( r \ne r' \), then, since the equation is symmetric in the two pairs, we may assume \( r = 0 \) and \( r' = 1 \) (@exm-method-cases); now \( 2q = 2q' + 1 \) is an integer that is both even and odd, which @thm-even-or-odd excludes. So \( \varphi \) is a bijection.

So "every integer is even or odd, and not both" is exactly the statement that \( \varphi \) is a bijection: "even or odd" is surjectivity, and "not both" is injectivity.
:::

For real functions, injectivity often comes from order. A function that keeps every strict inequality, or reverses every one, cannot take a value twice.

::: {#prp-strictly-monotone-injective}
[Strictly Monotone Maps Are Injective]

Let \( A, B \subseteq \nR \) and \( f \colon A \to B \). Call \( f \) **strictly increasing** if, for all \( x, x' \in A \), \( x < x' \) implies \( f(x) < f(x') \), and **strictly decreasing** if \( x < x' \) implies \( f(x) > f(x') \). If \( f \) is strictly increasing or strictly decreasing, then \( f \) is injective.
:::

::: {.proof}
We use the contrapositive form of @def-injective. Let \( x, x' \in A \) with \( x \ne x' \). By trichotomy, \( x < x' \) or \( x' < x \), and since the claim is symmetric in \( x \) and \( x' \), we may assume \( x < x' \). Then \( f(x) < f(x') \) or \( f(x) > f(x') \), as \( f \) is increasing or decreasing; in either case \( f(x) \ne f(x') \).
:::

::: {#exm-maps-from-calculus}
[Maps from calculus]

Decide whether each map is injective and whether it is surjective.

(a) \( \nR \to \nR \), \( x \mapsto x^3 \).

(b) The **floor** map \( \nR \to \nZ \), \( x \mapsto \floor{x} \), where \( \floor{x} \) is the unique integer \( m \) with \( m \le x < m + 1 \).

(c) Differentiation of polynomials of degree at most \( 2 \), recorded on coefficients: since \( a + bx + cx^2 \) has derivative \( b + 2cx \), this is the map \( D \colon \nR^3 \to \nR^2 \), \( D(a, b, c) = (b, 2c) \).
:::

::: {.solution}
(a) *Injective.* The map is strictly increasing. Let \( x < y \). Then
\[
\begin{aligned}
y^3 - x^3 &= (y - x)\bigl(x^2 + xy + y^2\bigr), \\
x^2 + xy + y^2 &= \bigl(x + \tfrac12 y\bigr)^2 + \tfrac34 y^2 .
\end{aligned}
\]
The second expression is positive unless \( x = y = 0 \): if \( y \ne 0 \), then \( \tfrac34 y^2 > 0 \); if \( y = 0 \), it equals \( x^2 \), which is positive unless \( x = 0 \). And \( x = y = 0 \) is excluded by \( x < y \). So both factors are positive, \( x^3 < y^3 \), and @prp-strictly-monotone-injective applies. *Surjective:* every real \( y \) has a real cube root \( \sqrt[3]{y} \), with \( (\sqrt[3]{y})^3 = y \). So the map is bijective.

(b) *Surjective:* for \( n \in \nZ \), \( \floor{n} = n \), since \( n \le n < n + 1 \). *Not injective:* \( \floor{0} = 0 = \floor{\tfrac12} \), since \( 0 \le \tfrac12 < 1 \).

(c) *Surjective:* for \( (u, v) \in \nR^2 \), \( D(0, u, v/2) = (u, v) \). *Not injective:* \( D(0, 0, 0) = (0, 0) = D(1, 0, 0) \); a constant has derivative \( 0 \). In general the first coordinate \( a \) of a preimage is free: it is the constant of integration.

In (a), injectivity came from an order property, not from the equation \( x_1^3 = x_2^3 \). Exercise B1 (c) uses the same property on \( \nZ \).
:::

::: {.check}
Is \( n \mapsto n^2 \) injective as a map \( \nN \to \nN \)? As a map \( \nZ \to \nN \)? Is either surjective?
:::

::: {.solution}
On \( \nN \) it is injective, because it is strictly increasing. Let \( n < m \). If \( m^2 \le n^2 \), then \( m \le n \) by \( (\Leftarrow) \) of @fd1:thm-squares-order (both numbers are \( \ge 0 \)), which trichotomy excludes, since \( n < m \). So \( n^2 < m^2 \), and @prp-strictly-monotone-injective applies with \( A = B = \nN \). On \( \nZ \) it is not injective: \( (-1)^2 = 1 = 1^2 \). Neither map is surjective: \( 2 \) is not the square of an integer, since \( \abs{n} \le 1 \) gives \( n^2 \le 1 \), and \( \abs{n} \ge 2 \) gives \( n^2 \ge 4 \).
:::

## Cancellation

For numbers, \( ab = ac \) with \( a \ne 0 \) gives \( b = c \). For functions, an equation \( f \circ g = f \circ h \) does not always give \( g = h \). Squaring, the function \( q_1 \) of @exm-square-three-ways, satisfies \( q_1 \circ \id_{\nR} = q_1 \circ (-\id_{\nR}) \), where \( -\id_{\nR} \) is the function \( x \mapsto -x \), because \( x^2 = (-x)^2 \); yet \( \id_{\nR} \ne -\id_{\nR} \), since their values at \( 1 \) differ. The failure is made of the two witnesses \( 1 \) and \( -1 \) against the injectivity of \( q_1 \). *Before reading on, guess which property of \( f \) makes cancellation on the left legal, and which property makes it legal on the right.*

::: {#thm-cancellation}
[Cancellation]

Let \( f \colon X \to Y \) be a function.

(a) \( f \) is injective if and only if, for every set \( W \) and all functions \( g, h \colon W \to X \), \( f \circ g = f \circ h \) implies \( g = h \).

(b) \( f \) is surjective if and only if, for every set \( Z \) and all functions \( g, h \colon Y \to Z \), \( g \circ f = h \circ f \) implies \( g = h \).
:::

Injections cancel on the left, and surjections on the right.

::: {.idea}
[Scratch work]

The two directions \( (\Rightarrow) \) only unwind @prp-function-equality: to show \( g = h \), compare the values at an arbitrary point. The directions \( (\Leftarrow) \) are the content. Their hypothesis speaks about functions and their goal about points, so the gap is to turn points into functions. For (a), the bridge is that a point of \( X \) is as good as a function from a one-element set into \( X \): the point \( x \) gives the function \( \{0\} \to X \), \( 0 \mapsto x \).

| Givens | Goal |
|---|---|
| cancellation on the left; \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \) | \( x_1 = x_2 \) |
| the hypothesis needs functions into \( X \) | \( g, h \colon \{0\} \to X \), \( g(0) \coloneqq x_1 \), \( h(0) \coloneqq x_2 \) |
| \( (f \circ g)(0) = f(x_1) = f(x_2) = (f \circ h)(0) \) | \( f \circ g = f \circ h \), so \( g = h \): the gap closes at \( x_1 = g(0) = h(0) = x_2 \) |

For (b), argue by contrapositive. If a point \( y_0 \in Y \) is missed by \( f \), then two functions on \( Y \) that differ only at \( y_0 \) cannot be told apart after \( f \), because \( f \) never arrives at \( y_0 \). Two values suffice: take the constant function \( 0 \) and the indicator function of \( \{ y_0 \} \) (@exm-first-functions (d)), both \( Y \to \{0, 1\} \).
:::

::: {.proof}
(a) \( (\Rightarrow) \) Suppose \( f \) is injective. Let \( W \) be a set and \( g, h \colon W \to X \) functions with \( f \circ g = f \circ h \), and let \( w \in W \). Then \( f(g(w)) = f(h(w)) \) by @def-composition, so \( g(w) = h(w) \) by the injectivity of \( f \). Since \( g \) and \( h \) have the same domain and codomain and agree at every point, \( g = h \) (@prp-function-equality).

\( (\Leftarrow) \) Suppose the cancellation property of (a) holds, and let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \). Define \( g, h \colon \{0\} \to X \) by \( g(0) \coloneqq x_1 \) and \( h(0) \coloneqq x_2 \); each is a function, with one input and one value. The composites agree at \( 0 \), the only point of their domain: \( (f \circ g)(0) = f(x_1) = f(x_2) = (f \circ h)(0) \). So \( f \circ g = f \circ h \) (@prp-function-equality), and the hypothesis with \( W = \{0\} \) gives \( g = h \). Therefore \( x_1 = g(0) = h(0) = x_2 \), and \( f \) is injective.

(b) \( (\Rightarrow) \) Suppose \( f \) is surjective. Let \( Z \) be a set and \( g, h \colon Y \to Z \) functions with \( g \circ f = h \circ f \), and let \( y \in Y \). By surjectivity there is \( x \in X \) with \( f(x) = y \) [\( \rulename{\exists E} \): the name \( x \) is fresh], and then
\[
g(y) = g(f(x)) = (g \circ f)(x) = (h \circ f)(x) = h(f(x)) = h(y) .
\]
So \( g = h \) (@prp-function-equality).

\( (\Leftarrow) \) It suffices to prove the contrapositive: if \( f \) is not surjective, then the cancellation property of (b) fails. The step back from the contrapositive to \( (\Leftarrow) \) is @fd1:prp-contrapositive-converse, which uses \( \rulename{RAA} \). Suppose \( f \) is not surjective. Negating the bounded quantifiers of @def-surjective (@fd1:prp-bounded-quantifier-negation, a classical law), there is \( y_0 \in Y \) with \( f(x) \ne y_0 \) for every \( x \in X \). Let \( Z \coloneqq \{0, 1\} \), let \( g \colon Y \to Z \) be the constant function \( 0 \), and let \( h \coloneqq \ind_{\{y_0\}} \colon Y \to Z \). For every \( x \in X \) we have \( f(x) \ne y_0 \), so \( h(f(x)) = 0 = g(f(x)) \); hence \( g \circ f = h \circ f \) (@prp-function-equality). But \( h(y_0) = 1 \ne 0 = g(y_0) \), so \( g \ne h \). This proves the contrapositive, and with it \( (\Leftarrow) \).
:::

The proofs needed only \( W = \{0\} \) and \( Z = \{0, 1\} \): maps from a one-point set detect injectivity, and maps into a two-point set detect surjectivity.

::: {#exm-method-cancel}
[Method: cancel an injection or a surjection]

**Template.** To prove \( g = h \), find a function \( f \) with \( f \circ g = f \circ h \) and \( f \) injective, or with \( g \circ f = h \circ f \) and \( f \) surjective. Compute the two composites, often with @prp-composition-associative; prove that \( f \) is injective or surjective; then cancel by @thm-cancellation.

**When to use it.** When \( g \) and \( h \) are known through equations rather than formulas, or when the composites are easier to compute than \( g \) and \( h \) themselves.

**The usual failure.** Canceling a non-injective \( f \) on the left, as with squaring before @thm-cancellation; and canceling on the wrong side. An injection does not cancel on the right: \( f \colon \{0\} \to \{0, 1\} \), \( f(0) = 0 \), is injective, and \( g = \id_{\{0, 1\}} \) and the constant \( h = 0 \) satisfy \( g \circ f = h \circ f \), with \( g \ne h \).
:::

::: {#exm-cancel-parity-map}
[Canceling the parity map]

Let \( g, h \colon \nZ \to \nZ \) be functions.

(a) Suppose \( g(2q + r) = h(2q + r) \) for all \( q \in \nZ \) and \( r \in \{0, 1\} \). Show that \( g = h \) by cancellation.

(b) Suppose only that \( g(2q) = h(2q) \) for all \( q \in \nZ \). Must \( g = h \)?
:::

::: {.solution}
(a) Let \( \varphi \colon \nZ \times \{0, 1\} \to \nZ \), \( \varphi(q, r) = 2q + r \), be the map of @exm-maps-from-algebra (c). The hypothesis says that \( (g \circ \varphi)(q, r) = (h \circ \varphi)(q, r) \) at every point of \( \nZ \times \{0, 1\} \), so \( g \circ \varphi = h \circ \varphi \) (@prp-function-equality). The map \( \varphi \) is surjective (@exm-maps-from-algebra (c)), so it cancels on the right (@thm-cancellation (b)): \( g = h \).

(b) No. The hypothesis now says \( g \circ \psi = h \circ \psi \) for \( \psi \colon \nZ \to \nZ \), \( \psi(q) = 2q \), and \( \psi \) is not surjective: \( 1 = 2q \) would make \( 1 \) even, while \( 1 \) is odd, and @thm-even-or-odd says no integer is both. Here is a pair that the hypothesis cannot tell apart. Let \( O \subseteq \nZ \) be the set of odd integers, \( g \coloneqq \id_{\nZ} \), and \( h(n) \coloneqq n + \ind_O(n) \), with the indicator function of @exm-first-functions (d). Then \( h(2q) = 2q = g(2q) \) for every \( q \in \nZ \), since \( 2q \) is even and so not odd; but \( h(1) = 2 \ne 1 = g(1) \).

The odd numbers, the points that \( \psi \) misses, are exactly where \( g \) and \( h \) may differ: they play the part of \( y_0 \) in the proof of @thm-cancellation (b).
:::

::: {.check}
Functions \( g, h \colon \nR \to \nR \) satisfy \( 2g(x) + 1 = 2h(x) + 1 \) for every real \( x \). Which function is canceled, on which side, and why is that allowed? Could \( t \mapsto t^2 \) be canceled in the same way?
:::

::: {.solution}
The function \( u \colon \nR \to \nR \), \( u(t) = 2t + 1 \), is canceled on the left: the hypothesis says \( u \circ g = u \circ h \), and \( u \) is injective, since \( 2t_1 + 1 = 2t_2 + 1 \) gives \( t_1 = t_2 \). So \( g = h \) by @thm-cancellation (a). Squaring cannot be canceled in this way, because it is not injective: \( g = \id_{\nR} \) and \( h = -\id_{\nR} \) satisfy \( g(x)^2 = h(x)^2 \) for every \( x \), and \( g \ne h \).
:::

::: {.second-reading title="Part (a) by cancellation"}
Part (a) of @prp-composite-partial-converse has a second proof by cancellation. Suppose \( g \circ f \) is injective, and let \( u, v \colon W \to X \) with \( f \circ u = f \circ v \). Then \( (g \circ f) \circ u = g \circ (f \circ u) = g \circ (f \circ v) = (g \circ f) \circ v \) by @prp-composition-associative, so \( u = v \), because the injective \( g \circ f \) cancels on the left (@thm-cancellation (a), \( (\Rightarrow) \)). So \( f \) cancels on the left, and it is injective by the same theorem, \( (\Leftarrow) \). Part (b) is the mirror image, with surjections canceled on the right.
:::

::: {.remark}
[Looking ahead]

Chapter 3 proves the division algorithm, which makes \( (q, r) \mapsto qn + r \) a bijection \( \nZ \times \{0, \dots, n - 1\} \to \nZ \) for every integer \( n \ge 1 \), as @exm-maps-from-algebra (c) did for \( n = 2 \). Chapter 4 proves the facts of @exm-injective-surjective-first (c), (d) in general, from the pigeonhole principle of the lattice-point puzzle of Section 1.1, and, in an exercise, counts the injections between finite sets.
:::

## Exercises

### A. Check your understanding

::: {#exr-functions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define "\( f \colon X \to Y \) is injective" in symbols, and write its negation in symbols.
2. Is the empty function \( \emptyset \to \{1\} \) injective? Is it surjective? Justify your answers.
3. Which of these relations on \( \{1, 2, 3\} \) are graphs of functions \( \{1, 2, 3\} \to \{1, 2, 3\} \)? For each that is not, name the clause of the definition that fails.
   \( R_1 = \{ (1, 2), (2, 2), (3, 1) \} \), \( R_2 = \{ (1, 1), (2, 3) \} \), \( R_3 = \{ (1, 1), (1, 2), (2, 2), (3, 3) \} \).
4. How many functions \( \{1, 2\} \to \{a, b, c\} \) are there, and how many of them are injective? Answer by listing.
:::
:::

::: {.solution}
(a) \( f \) is injective: \( \forall x_1 \in X \ \forall x_2 \in X \ \bigl( f(x_1) = f(x_2) \to x_1 = x_2 \bigr) \) (@def-injective). Its negation: \( \exists x_1 \in X \ \exists x_2 \in X \ \bigl( f(x_1) = f(x_2) \wedge x_1 \ne x_2 \bigr) \). The bounds stay as they are, and the negated implication becomes "hypothesis and not conclusion", by the negation laws of *Logic and Proof*, Chapter 6.

(b) Injective: yes. The condition "for all \( x_1, x_2 \in \emptyset \), …" holds vacuously, since there are no \( x_1 \in \emptyset \) (@fd1:prp-vacuous-implication). Surjective: no. The witness is \( 1 \): there is no \( x \in \emptyset \) at all, so none with value \( 1 \).

(c) \( R_1 \) is a function (\( 1 \mapsto 2 \), \( 2 \mapsto 2 \), \( 3 \mapsto 1 \)). \( R_2 \) is not: clause (Fn1) fails at \( 3 \), which has no output. \( R_3 \) is not: clause (Fn2) fails at \( 1 \), which has the two outputs \( 1 \) and \( 2 \).

(d) A function \( f \colon \{1, 2\} \to \{a, b, c\} \) is determined by the pair of values \( (f(1), f(2)) \) (@prp-function-equality), and each value can be any of the three letters. Listing the pairs:
\[
\begin{aligned}
&(a, a), \ (a, b), \ (a, c), \\
&(b, a), \ (b, b), \ (b, c), \\
&(c, a), \ (c, b), \ (c, c).
\end{aligned}
\]
There are \( 9 \) functions. A function on \( \{1, 2\} \) is injective exactly when \( f(1) \ne f(2) \), since \( 1 \) and \( 2 \) are the only two different inputs. Removing the three pairs with equal entries, on the diagonal of the list, leaves \( 6 \) injective functions.
:::

### B. Practice

::: {#exr-functions-b1}
[B1: Five functions]

Determine which of the following are injective, which are surjective, and which are not functions at all. Justify your answers.

::: {.enumerate options="label=(\alph*)"}
1. \( \nZ \to \nZ \), \( n \mapsto 2n \).
2. \( \nN \times \nN \to \nN \), \( (m, n) \mapsto m + n \).
3. \( \nZ \to \nZ \), \( n \mapsto n^3 \).
4. \( \nR \to (-1, 1) \), \( x \mapsto x / \sqrt{1 + x^2} \).
5. \( \nZ_{>0} \to \nZ_{>0} \), \( n \mapsto n + (-1)^n \).
:::
:::

::: {.solution}
(a) *Injective:* \( 2n_1 = 2n_2 \) gives \( n_1 = n_2 \). *Not surjective:* the witness is \( 1 \), which is odd, while every \( 2n \) is even, and no integer is both even and odd (@thm-even-or-odd).

(b) *Not injective:* \( (1, 2) \ne (2, 1) \) (@def-ordered-pair), and both are sent to \( 3 \). *Surjective:* for \( k \in \nN \), the pair \( (0, k) \) lies in \( \nN \times \nN \) and is sent to \( k \).

(c) *Injective:* \( x \mapsto x^3 \) is strictly increasing on \( \nR \) (@exm-maps-from-calculus (a)), so also on \( \nZ \), and @prp-strictly-monotone-injective applies. *Not surjective:* the witness is \( 2 \). If \( n \le 1 \), then \( n^3 \le 1 \); if \( n \ge 2 \), then \( n^3 \ge 8 \). So \( n^3 \ne 2 \) for every integer \( n \).

(d) *A function:* for every \( x \), \( 1 + x^2 > x^2 \ge 0 \), so \( \sqrt{1 + x^2} \) is defined and exceeds \( \sqrt{x^2} = \abs{x} \); hence \( \abs{x / \sqrt{1 + x^2}} < 1 \), and the value lies in \( (-1, 1) \). *Injective.* Suppose \( y = x/\sqrt{1 + x^2} \). The denominator is positive, so \( y \) has the sign of \( x \), and squaring gives \( y^2 (1 + x^2) = x^2 \), that is, \( x^2 (1 - y^2) = y^2 \). Since \( \abs{y} < 1 \) (shown above), \( 1 - y^2 > 0 \), so \( x^2 = y^2/(1 - y^2) \). Of the square roots of this number, \( x \) is the one with the sign of \( y \):
\[
x = \frac{y}{\sqrt{1 - y^2}} .
\]
So \( x \) is determined by \( y \): two inputs with the same output \( y \) are both equal to \( y/\sqrt{1 - y^2} \), hence equal. *Surjective.* Let \( y \in (-1, 1) \) and put \( x \coloneqq y/\sqrt{1 - y^2} \), a real number since \( 1 - y^2 > 0 \). Then \( 1 + x^2 = 1/(1 - y^2) \), so \( \sqrt{1 + x^2} = 1/\sqrt{1 - y^2} \), and
\[
\frac{x}{\sqrt{1 + x^2}} = \frac{y}{\sqrt{1 - y^2}} \cdot \sqrt{1 - y^2} = y .
\]
So the function is bijective. (For example, \( x = \tfrac34 \mapsto \tfrac{3/4}{5/4} = \tfrac35 \), and \( y = \tfrac35 \) comes back to \( x = \tfrac{3/5}{4/5} = \tfrac34 \).) The same plan as in @exm-fraction-map works, with \( \sqrt{1 + x^2} \) in place of \( 1 + \abs{x} \) and squaring in place of the split by sign.

(e) *Not a function* \( \nZ_{>0} \to \nZ_{>0} \): at \( n = 1 \) the formula gives \( 1 + (-1) = 0 \), and \( 0 \notin \nZ_{>0} \), so (Fn1) fails at \( 1 \). This is the planted failure: the question whether it is injective or surjective does not arise. (On \( \nN = \{0, 1, 2, \dots\} \) the same formula is a function, and a bijection: it swaps \( 0 \leftrightarrow 1 \), \( 2 \leftrightarrow 3 \), and so on.)
:::

::: {#exr-functions-b2}
[B2: Put the proof in order]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions. The following lines contain a proof that **if \( g \circ f \) is surjective and \( g \) is injective, then \( f \) is surjective**, shuffled, together with two lines that do not belong. Write the six correct lines in an order that makes a proof, and say why each of the other two lines fails.

(i) Since \( g \) is injective, \( f(x) = y \).

(ii) Let \( z \in Z \).

(iii) Then \( g(y) \in Z \).

(iv) Since \( y \) was arbitrary, \( f \) is surjective.

(v) Since \( g \circ f \) is surjective, there is \( x \in X \) with \( g(f(x)) = g(y) \).

(vi) Let \( y \in Y \).

(vii) Since \( f \) is injective, \( x = y \).

(viii) So \( y \) has the preimage \( x \) under \( f \).
:::

::: {.solution}
The order is (vi), (iii), (v), (i), (viii), (iv):

> Let \( y \in Y \). Then \( g(y) \in Z \). Since \( g \circ f \) is surjective, there is \( x \in X \) with \( g(f(x)) = g(y) \). Since \( g \) is injective, \( f(x) = y \). So \( y \) has the preimage \( x \) under \( f \). Since \( y \) was arbitrary, \( f \) is surjective.

No other order is admissible. Each line uses the one before it: (iii) needs the \( y \) of (vi); (v) applies the surjectivity of \( g \circ f \) at the point \( g(y) \) of (iii) [\( \rulename{\exists E} \): the name \( x \) is fresh], using @def-composition to write \( (g \circ f)(x) \) as \( g(f(x)) \); (i) applies the injectivity of \( g \) to the equation of (v), at the points \( f(x) \) and \( y \) of \( Y \); (viii) is the \( \rulename{\exists I} \) that (i) makes possible; and (iv) closes the \( \rulename{\forall I} \) opened by (vi).

The distractor (ii) opens with an arbitrary element of the wrong set. The goal "\( f \) is surjective" is \( \forall y \in Y \ \exists x \in X \ f(x) = y \), so the proof must take an arbitrary \( y \in Y \); the point of \( Z \) that the proof needs is \( g(y) \), and it is built, not given. The distractor (vii) uses a hypothesis the statement does not have, since nothing says \( f \) is injective; and it equates a point of \( X \) with a point of \( Y \), which is not what the goal asks for.

The hypothesis "\( g \) injective" is needed. In the example before @prp-composite-partial-converse, \( g \circ f = \id_{\{1\}} \) is surjective and \( f \) is not; there \( g \) is not injective.
:::

::: {#exr-functions-b3}
[B3: Examples on the natural numbers]

Give an example of a function \( \nN \to \nN \) that is surjective and not injective, and one that is injective and not surjective. Check each property.
:::

::: {.solution}
*Surjective, not injective.* Let \( s(0) \coloneqq 0 \) and \( s(n) \coloneqq n - 1 \) for \( n \ge 1 \); for \( n \ge 1 \), \( n - 1 \in \nN \), so \( s \colon \nN \to \nN \) is a function. It is surjective: for \( m \in \nN \), \( m + 1 \ge 1 \), so \( s(m + 1) = m \). It is not injective: \( s(0) = 0 = s(1) \) and \( 0 \ne 1 \).

*Injective, not surjective.* Let \( t(n) \coloneqq n + 1 \). It is injective: \( n_1 + 1 = n_2 + 1 \) gives \( n_1 = n_2 \). It is not surjective: \( 0 \) is not an output, since \( n + 1 \ge 1 \).

Many other answers are correct. An answer to the first part must have: every value in \( \nN \) (so it is a function into \( \nN \)); at least one value taken at two different inputs, with the two inputs named; and every \( m \in \nN \) reached, with a preimage given as a formula in \( m \), since checking some \( m \) is not enough. An answer to the second part must have: values in \( \nN \); a proof that equal outputs come from equal inputs; and one named natural number that is never reached, with the reason.
:::

::: {#exr-functions-b4}
[B4: Prove or disprove]

Prove each true statement by the methods of @exm-method-injectivity and @exm-method-surjectivity, and refute each false one with a concrete counterexample.

::: {.enumerate options="label=(\alph*)"}
1. The function \( \nZ \to \nZ \), \( n \mapsto n^2 + n \), is injective.
2. The function \( \nR \to \nR \), \( x \mapsto x^3 + 2x \), is injective.
3. The function \( \nZ \times \nZ \to \nZ \), \( (m, n) \mapsto 2m + 3n \), is surjective.
4. The function \( \nZ \times \nZ \to \nZ \), \( (m, n) \mapsto 2m + 4n \), is surjective.
5. The formula \( x \mapsto x^2 + 4x \) defines a bijection from \( [-2, \infty) \) to \( [-4, \infty) \).
:::
:::

::: {.solution}
(a) **False.** The inputs \( 0 \) and \( -1 \) are different, and both are sent to \( 0 \): \( 0^2 + 0 = 0 = (-1)^2 + (-1) \).

(b) **True.** Let \( x^3 + 2x = y^3 + 2y \). Then
\[
0 = (x^3 - y^3) + 2(x - y) = (x - y)\bigl(x^2 + xy + y^2 + 2\bigr),
\]
and \( x^2 + xy + y^2 + 2 = (x + \tfrac12 y)^2 + \tfrac34 y^2 + 2 \ge 2 > 0 \). A product of two reals is \( 0 \) only if a factor is \( 0 \), so \( x - y = 0 \), that is, \( x = y \).

(c) **True.** Let \( k \in \nZ \). The pair \( (-k, k) \) lies in \( \nZ \times \nZ \), and \( 2(-k) + 3k = k \). (The scrap-paper search: \( 3 - 2 = 1 \), so multiply that solution of \( 2m + 3n = 1 \) by \( k \).)

(d) **False.** The witness is \( 1 \). For all integers \( m \) and \( n \), \( 2m + 4n = 2(m + 2n) \) is even, and \( 1 \) is odd; no integer is both (@thm-even-or-odd). So \( 2m + 4n \ne 1 \).

(e) **True.** First, the formula is a function into \( [-4, \infty) \): \( x^2 + 4x = (x + 2)^2 - 4 \ge -4 \). *Injective:* let \( x_1, x_2 \ge -2 \) with \( x_1^2 + 4x_1 = x_2^2 + 4x_2 \). Then \( (x_1 + 2)^2 = (x_2 + 2)^2 \), and both bases are \( \ge 0 \), so \( x_1 + 2 = x_2 + 2 \) by @fd1:thm-squares-order (used twice, as in @exm-square-three-ways (b)), and \( x_1 = x_2 \). *Surjective:* let \( y \ge -4 \) and put \( x \coloneqq -2 + \sqrt{y + 4} \), defined since \( y + 4 \ge 0 \). Then \( x \ge -2 \), and \( x^2 + 4x = (x + 2)^2 - 4 = (y + 4) - 4 = y \).
:::

::: {#exr-functions-b5}
[B5: Prove or disprove]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions in (a) and (b). Prove each true statement, and refute each false one with a concrete counterexample.

::: {.enumerate options="label=(\alph*)"}
1. If \( g \circ f \) is injective and \( g \) is surjective, then \( f \) is surjective.
2. If \( g \circ f \) is surjective and \( f \) is injective, then \( g \) is injective.
3. If \( g, h \colon \nR \to \nR \) satisfy \( g(x)^3 = h(x)^3 \) for every real \( x \), then \( g = h \).
4. If \( g, h \colon \nR \to \nR \) satisfy \( g(x^2) = h(x^2) \) for every real \( x \), then \( g = h \).
5. If \( g, h \colon \nR \to \nR \) satisfy \( g(x^3) = h(x^3) \) for every real \( x \), then \( g = h \).
:::
:::

::: {.solution}
(a) **False.** Let \( X = \{1\} \), \( Y = \{1, 2\} \), \( Z = \{1\} \), \( f(1) = 1 \), and \( g \) the constant function \( 1 \). Then \( g \circ f \) is injective, since its domain has one element; \( g \) is surjective, since \( 1 = g(1) \); and \( 2 \) is not a value of \( f \).

(b) **False.** On \( \nN \), let \( f(n) = 2n \), and let \( g(m) = m/2 \) for even \( m \) and \( g(m) = (m - 1)/2 \) for odd \( m \). By @thm-even-or-odd each \( m \in \nN \) falls under exactly one case, and in each case \( g(m) \in \nN \); so \( g \colon \nN \to \nN \) is a function. Then \( g(f(n)) = 2n/2 = n \), so \( g \circ f = \id_{\nN} \) (@prp-function-equality), which is surjective. And \( f \) is injective, since \( 2n_1 = 2n_2 \) gives \( n_1 = n_2 \). But \( g(0) = 0 = g(1) \), so \( g \) is not injective.

(c) **True.** Let \( k \colon \nR \to \nR \), \( k(t) = t^3 \). The hypothesis says \( k \circ g = k \circ h \), and \( k \) is injective (@exm-maps-from-calculus (a)). Canceling \( k \) on the left (@thm-cancellation (a)) gives \( g = h \).

(d) **False.** Let \( g = \id_{\nR} \) and \( h(t) = \abs{t} \). Then \( g(x^2) = x^2 = \abs{x^2} = h(x^2) \) for every \( x \), since \( x^2 \ge 0 \); but \( g(-1) = -1 \ne 1 = h(-1) \). Squaring \( \nR \to \nR \) is not surjective, so it cannot be canceled on the right, and \( g \) and \( h \) differ exactly on the negative numbers, which squaring misses.

(e) **True.** With \( k \) as in (c), the hypothesis says \( g \circ k = h \circ k \), and \( k \) is surjective, since every real number has a real cube root (@exm-maps-from-calculus (a)). Canceling \( k \) on the right (@thm-cancellation (b)) gives \( g = h \).
:::

### C. Going deeper

::: {#exr-functions-c1}
[C1: Exit check: composites]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( g \circ f \) is injective and \( f \) is surjective, then \( g \) is injective.
2. Give an example in which \( g \circ f \) is injective and \( g \) is not injective, and say which hypothesis of (a) fails.
:::
:::

::: {.solution}
(a) Suppose \( g \circ f \) is injective and \( f \) is surjective. Let \( y_1, y_2 \in Y \) with \( g(y_1) = g(y_2) \); we must show \( y_1 = y_2 \). Since \( f \) is surjective, there are \( x_1, x_2 \in X \) with \( f(x_1) = y_1 \) and \( f(x_2) = y_2 \) [\( \rulename{\exists E} \), twice: the names \( x_1 \) and \( x_2 \) are fresh and different]. Then, by @def-composition,
\[
(g \circ f)(x_1) = g(y_1) = g(y_2) = (g \circ f)(x_2) ,
\]
so \( x_1 = x_2 \), since \( g \circ f \) is injective. Hence \( y_1 = f(x_1) = f(x_2) = y_2 \), and \( g \) is injective.

(b) Take the example before @prp-composite-partial-converse: \( f \colon \{1\} \to \{1, 2\} \), \( f(1) = 1 \), and \( g \colon \{1, 2\} \to \{1\} \), \( g(1) = g(2) = 1 \). Then \( g \circ f \colon \{1\} \to \{1\} \) is injective, because its domain has only one element: if \( x_1, x_2 \in \{1\} \), then \( x_1 = 1 = x_2 \). And \( g \) is not injective: \( g(1) = g(2) \) with \( 1 \ne 2 \). The hypothesis of (a) that fails is the surjectivity of \( f \): \( 2 \) is not a value of \( f \).

**Marking scheme.** (10 points)
- 2: fixes arbitrary \( y_1, y_2 \in Y \) with \( g(y_1) = g(y_2) \) and states the goal \( y_1 = y_2 \).
- 3: names preimages \( x_1 \), \( x_2 \) under \( f \), with fresh and different names, by the surjectivity of \( f \).
- 3: rewrites \( g(y_1) = g(y_2) \) as an equation of values of \( g \circ f \), invokes the injectivity of \( g \circ f \), and returns to \( y_1 = y_2 \) through \( f \).
- 2: an example with explicit sets and functions, both claims checked (\( g \circ f \) injective; two different points with the same value under \( g \)), and the failing hypothesis named.

Fatal errors (0 for the step): assuming \( g \) is injective; one name for both preimages, so that \( y_1 = f(x) = y_2 \) is assumed from the start (entry (N4) of *Logic and Proof*, Chapter 8's catalogue); starting from \( y_1 = y_2 \) and deriving \( g(y_1) = g(y_2) \) (the converse, entry (N5)).
:::

::: {#exr-functions-c2}
[C2: When the composite is a bijection]

::: {.enumerate options="label=(\alph*)"}
1. Give functions \( f, g \colon \nN \to \nN \) with \( g \circ f \) bijective and neither \( f \) nor \( g \) bijective.
2. Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions. Prove that if \( g \circ f \) is bijective and \( f \) is surjective, then \( f \) and \( g \) are both bijective.
:::
:::

::: {.solution}
(a) Let \( f(n) = n + 1 \), and let \( g(0) = 0 \) and \( g(m) = m - 1 \) for \( m \ge 1 \); both are functions \( \nN \to \nN \), since \( m - 1 \in \nN \) for \( m \ge 1 \). Then \( g(f(n)) = (n + 1) - 1 = n \), since \( n + 1 \ge 1 \); so \( g \circ f = \id_{\nN} \) (@prp-function-equality), which is bijective. But \( f \) misses \( 0 \), since \( n + 1 \ge 1 \), so \( f \) is not surjective; and \( g(0) = 0 = g(1) \), so \( g \) is not injective.

(b) Suppose \( g \circ f \) is bijective and \( f \) is surjective. Since \( g \circ f \) is injective, \( f \) is injective by @prp-composite-partial-converse (a); with the hypothesis, \( f \) is bijective. Since \( g \circ f \) is surjective, \( g \) is surjective by @prp-composite-partial-converse (b). Since \( g \circ f \) is injective and \( f \) is surjective, \( g \) is injective by @exr-functions-c1 (a). So \( g \) is bijective too.
:::

<!-- dependency ledger
def-surjective (claim): (the warning after it) x^2 + x + 1 = (x + 1/2)^2 + 3/4 > 0; values 0, 2, 6, 12 | school algebra (F1-F2 convention); computation inline
def-injective (claim): negation of bounded quantifiers and of an implication | F1.8 §02 (paid): prp-bounded-quantifier-negation, prp-negated-implication, prose pointer "*Logic and Proof*, Chapter 6"
exm-injective-surjective-first (example): dividing by 3; n >= 1 gives 3n >= 3, n <= 0 gives 3n <= 0 | school algebra and order facts (F1-F2 convention); proved in AN1.1 (order) and F2.2 (integers)
exm-injective-surjective-first (claim): a function from a 3-element set to a 2-element set is not injective, etc. | F2.3 §01 (promised in the Looking-ahead box at the end of the main line, "Chapter 4", pigeonhole, the principle stated in F2.1 §01's lattice-point puzzle); only the two specific cases (c), (d) are proved, by listing; nothing depends on the general claim
exm-square-three-ways (example): x^2 >= 0 > -1; existence of sqrt(y) for y >= 0 | school fact (F1-F2 convention); proved in AN1.1
thm-composition-injective-surjective (proof): f(x1), f(x2) in Y | (**) in def-function's paraphrase (every value lies in the codomain)
thm-composition-injective-surjective (proof): forall-E, exists-E, exists-I, forall-I in the prose tags | F1.4 (promised): quantifier rules (F1.4 §03-F1.4 §06), prose pointer; the bounded forms in the derivation are prp-bounded-quantifier-rules (cited)
thm-composition-injective-surjective (claim): level 0 = full derivation | F1.5 (promised): def-levels-of-proof (prose pointer, F1.5 §03)
thm-composition-injective-surjective (claim): closing lines of ->I and forall-I may be silent | F1.5 (promised): def-silent-steps, prose pointer
exr-functions-b1 (solution): parity (1 is odd, 2n even, not both) | thm-even-or-odd (F2.1 §01)
exr-functions-b1 (solution): (c) n <= 1 gives n^3 <= 1, n >= 2 gives n^3 >= 8, every integer is <= 1 or >= 2; a function strictly increasing on R is strictly increasing on Z | school order facts on Z (F1-F2 convention); proved in AN1.1 and F2.2
exr-functions-b1 (solution): (d) for x/sqrt(1+x^2): sqrt increasing on [0, inf), sqrt(x^2) = |x|, sqrt(1/t) = 1/sqrt(t) for t > 0 | school algebra (F1-F2 convention); proved in AN1.1
exr-functions-b1 (solution): 0 in N and 0 + k = k | school arithmetic of N; F2.2 (promised; STATUS row "F2.1 §02, §03, F2.6 §02 → F2.2", ℕ closed under + and · by lem-naturals-arithmetic (b); 0 + k = k as in AN1.1)
exr-functions-b1 (solution): in (e), (-1)^n is defined, and is 1 for even n and -1 for odd n | F2.2 (promised; STATUS row "F2.1 §02, §03, F2.6 §02 → F2.2", (−1)^n by prp-power-laws (b), thm-recursion); parity: thm-even-or-odd (F2.1 §01)
def-surjective (example): the Quick check on n -> n + 1 uses n + 1 in N and n + 1 >= 1 for n in N; m - 1 in Z for m in Z | F2.2 (promised; STATUS row "F2.1 §02, §03, F2.6 §02 → F2.2": m − 1 in Z by prp-integers-closed, n + 1 in N by lem-naturals-arithmetic (b); n + 1 >= 1 for n in N since n >= 0 by lem-naturals-arithmetic (a))
exr-functions-b3 (solution): n >= 1 gives n - 1 in N; n + 1 >= 1 for n in N | F2.2 (promised; STATUS row "F2.1 §02, §03, F2.6 §02 → F2.2"; n - 1 in N for n >= 1 by lem-naturals-arithmetic (c); n + 1 >= 1 since n >= 0 by (a))
exr-functions-a1 (solution): negation laws | F1.8 §02 (paid): prp-bounded-quantifier-negation, prp-negated-implication, prose pointer "*Logic and Proof*, Chapter 6"
exm-fraction-map (example): 1 + |x| >= 1 > 0; |x|/(1 + |x|) < 1; f(x) has the sign of x; |x| = x for x >= 0 and -x for x < 0; clearing denominators; |y| < 1 gives 1 - |y| > 0 | school algebra and order facts (F1-F2 convention); proved in AN1.1
exm-fraction-map (example): the case split on the sign of y (y >= 0 or y < 0) | trichotomy of the order on R, school fact (F1-F2 convention); proved in AN1.1
def-surjective (claim): (the quick check after exm-fraction-map) 5n = 2 has no integer solution: n >= 1 gives 5n >= 5, n <= 0 gives 5n <= 0, and every integer is >= 1 or <= 0 | school order facts on Z ("no integer lies strictly between 0 and 1"; F1-F2 convention); proved in AN1.1
exr-functions-b4 (solution): (b) x^3 - y^3 = (x - y)(x^2 + xy + y^2) and the completed square; a product of reals is 0 only if a factor is 0 | school algebra (F1-F2 convention); proved in AN1.1
exr-functions-b4 (solution): (c), (d) integer arithmetic; 2(m + 2n) is even (m + 2n in Z) | school arithmetic (closure of Z under + and ·, F1-F2 convention); thm-even-or-odd (cited) for "not both"
exr-functions-b4 (solution): (e) (x + 2)^2 >= 0; sqrt(y + 4) exists and is >= 0 for y >= -4 | school fact (F1-F2 convention); proved in AN1.1; thm-squares-order (cited)
prp-composite-partial-converse (proof): (a) applying g to both sides of f(x1) = f(x2): a function gives equal outputs at equal inputs | (Fn2) of def-function (substitution of equals); as in the old C1 solution
prp-composite-partial-converse (claim): the lead's example: g o f = id_{1}, g(1) = g(2), 2 not a value of f | computation inline; prp-function-equality for g o f = id_{1} (one point)
exm-structure-maps (solution): (a) "X subset of A and A subset of X give A = X" | prp-subset-antisymmetric (F2.1 §02)
exm-structure-maps (solution): (c) "at most one element": X = empty or X = {x}, so X x X is empty or {(x, x)} | prp-product-set-laws (empty factor); def-cartesian-product; case split on whether X has two different points (classical, LEM)
exm-structure-maps (solution): (d) chain: De Morgan (d) and double negation (b) use RAA; disjunctive syllogism; vee-I; and-E | cited inline (fd1:prp-de-morgan, fd1:prp-double-negation, fd1:prp-disjunctive-syllogism), classical, as in exm-method-chain-of-iff
exm-structure-maps (claim): (the projection Quick check) case split "Y has at most one element or two different points" | classical (LEM), as in the case splits of F2.1
exm-maps-from-algebra (solution): (a) integers: a product is 0 only if a factor is; a != 0, a != +-1 gives |a| >= 2; |an| = |a||n|; n != 0 gives |n| >= 1; a^2 = 1 for a = +-1 | school arithmetic and order of Z (F1-F2 convention); proved in F3.2 (integers) and AN1.1
exm-maps-from-algebra (solution): (c) 2q = 2q' gives q = q' | school arithmetic of Z (cancellation of a nonzero factor), as in (a)
prp-strictly-monotone-injective (proof): trichotomy of < on R: x != x' gives x < x' or x' < x | school order fact (F1-F2 convention); proved in AN1.1
exm-maps-from-calculus (solution): (a) y^3 - x^3 factorization; completed square; product of positives is positive; every real has a real cube root | school algebra (F1-F2 convention); cube roots: AN1.1 thm-nth-root (with a sign change)
exm-maps-from-calculus (example): floor(x) exists and is unique for x in R | school fact (F1-F2 convention); for x in Q: F3.2 §05 prp-rational-integer-part; for x in R: AN1.1 (Archimedean property)
exm-maps-from-calculus (example): (c) derivative of a + bx + cx^2 is b + 2cx; "constant of integration" | motivation only: D is defined by its formula on R^3, and nothing in the solution uses calculus
exm-maps-from-calculus (claim): (the n^2 Quick check) n < m and m <= n are incompatible (trichotomy); |n| <= 1 or |n| >= 2 for integers; |n| >= 2 gives n^2 >= 4 | school order facts (F1-F2 convention); fd1:thm-squares-order (cited) for the step m^2 <= n^2 => m <= n
thm-cancellation (proof): g, h: {0} -> X defined by one value are functions | def-function: the graph {(0, x1)} satisfies (Fn1), (Fn2); as in exm-first-functions (c)
thm-cancellation (proof): the constant function 0 and ind_{y0} are functions Y -> {0, 1} | exm-first-functions (c), (d)
thm-cancellation (proof): (b)(<=) "not surjective" negated to "some y0 is missed"; contrapositive back to (<=) | cited inline: fd1:prp-bounded-quantifier-negation, fd1:prp-contrapositive-converse (RAA)
exm-method-cancel (example): f: {0} -> {0, 1}, f(0) = 0; id and constant 0 agree at 0, differ at 1 | computation inline
exm-cancel-parity-map (solution): (b) n + ind_O(n) is an integer; 2q even hence not odd; 1 odd | thm-even-or-odd (cited); closure of Z under + (school arithmetic, F1-F2 convention)
exm-cancel-parity-map (claim): (the Quick check after it) 2t1 + 1 = 2t2 + 1 gives t1 = t2 | school algebra (F1-F2 convention)
exr-functions-b2 (solution): (v) uses def-composition to read (g o f)(x) as g(f(x)); g(y) in Z since g maps into Z | (**) in def-function's paraphrase (every value lies in the codomain)
exr-functions-b5 (solution): (b) m/2 and (m - 1)/2 are natural numbers for even and odd m in N; 2n/2 = n | school arithmetic of N (F1-F2 convention); thm-even-or-odd (cited) for "exactly one case"
exr-functions-b5 (solution): (d) |x^2| = x^2 since x^2 >= 0 | school fact (F1-F2 convention)
exr-functions-c2 (solution): (a) m - 1 in N for m >= 1; n + 1 >= 1 for n in N; (n + 1) - 1 = n | F2.2 (promised; STATUS row "F2.1 §02, §03, F2.6 §02 → F2.2"; lem-naturals-arithmetic (a), (c))
-->
