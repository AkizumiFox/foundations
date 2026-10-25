# Injections and Surjections

<!-- S3: rewrite per blueprint (2.2: opening frame; new topics: cancellation (thm-cancellation, exm-method-cancel), prp-composite-partial-converse, structure maps, examples from algebra and calculus; layout §1) -->

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

Parts (c) and (d) show two more things. A function from a three-element set to a two-element set cannot be injective, and one from a two-element set to a three-element set cannot be surjective: there are too many inputs in the first case and too few in the second. Section 4.1 proves facts of this kind in general, from the pigeonhole principle of the lattice-point puzzle of Section 1.1.

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

The converses are more interesting, and they are the exercises of this section. An injective composite \( g \circ f \) forces \( f \) to be injective and says nothing of the kind about \( g \) (exit check C1). A surjective composite forces \( g \) to be surjective, and \( f \) may miss points (B2). Section 2.4 builds on these facts: a function \( f \) with a function \( g \) such that \( g \circ f = \id_X \) is forced to be injective.

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
3. \( \nR \to \nR \), \( x \mapsto x^3 \).
4. \( \nR \to (-1, 1) \), \( x \mapsto x / \sqrt{1 + x^2} \).
5. \( \nZ_{>0} \to \nZ_{>0} \), \( n \mapsto n + (-1)^n \).
:::
:::

::: {.solution}
(a) *Injective:* \( 2n_1 = 2n_2 \) gives \( n_1 = n_2 \). *Not surjective:* the witness is \( 1 \), which is odd, while every \( 2n \) is even, and no integer is both even and odd (@thm-even-or-odd).

(b) *Not injective:* \( (1, 2) \ne (2, 1) \) (@def-ordered-pair), and both are sent to \( 3 \). *Surjective:* for \( k \in \nN \), the pair \( (0, k) \) lies in \( \nN \times \nN \) and is sent to \( k \).

(c) *Injective.* Let \( x_1^3 = x_2^3 \). Then
\[
0 = x_1^3 - x_2^3 = (x_1 - x_2)\bigl(x_1^2 + x_1 x_2 + x_2^2\bigr),
\qquad
x_1^2 + x_1 x_2 + x_2^2 = \bigl(x_1 + \tfrac12 x_2\bigr)^2 + \tfrac34 x_2^2 .
\]
If \( x_1 \ne x_2 \), the second factor is positive: if \( x_2 \ne 0 \), then \( \tfrac34 x_2^2 > 0 \); if \( x_2 = 0 \), it equals \( x_1^2 > 0 \), because \( x_1 \ne 0 \). Then the product is nonzero, a contradiction. So \( x_1 = x_2 \). *Surjective:* for \( y \in \nR \), every real number has a real cube root, and \( x \coloneqq \sqrt[3]{y} \) satisfies \( x^3 = y \). So the function is bijective.

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

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions. The following lines contain a proof that **if \( g \circ f \) is surjective, then \( g \) is surjective**, shuffled, together with two lines that do not belong. Write the six correct lines in an order that makes a proof, and say why each of the other two lines fails.

(i) Then \( g(y) = g(f(x)) = (g \circ f)(x) = z \), by @def-composition.

(ii) Let \( y \in Y \).

(iii) Since \( g \circ f \) is surjective, there is \( x \in X \) with \( (g \circ f)(x) = z \).

(iv) Since \( z \) was arbitrary, \( g \) is surjective.

(v) Let \( y \coloneqq f(x) \), an element of \( Y \).

(vi) Since \( f \) is surjective, \( y = f(x) \) for some \( x \in X \).

(vii) Let \( z \in Z \).

(viii) So \( z \) has a preimage under \( g \), namely \( y \).
:::

::: {.solution}
The order is (vii), (iii), (v), (i), (viii), (iv):

> Let \( z \in Z \). Since \( g \circ f \) is surjective, there is \( x \in X \) with \( (g \circ f)(x) = z \). Let \( y \coloneqq f(x) \), an element of \( Y \). Then \( g(y) = g(f(x)) = (g \circ f)(x) = z \), by @def-composition. So \( z \) has a preimage under \( g \), namely \( y \). Since \( z \) was arbitrary, \( g \) is surjective.

No other order is admissible. Each line uses the one before it: (iii) needs the \( z \) of (vii); (v) needs the \( x \) of (iii); (i) needs the \( y \) of (v); (viii) is the \( \rulename{\exists I} \) that (i) makes possible; and (iv) closes the \( \rulename{\forall I} \) opened by (vii).

The distractor (ii) opens with an arbitrary element of the wrong set. The goal "\( g \) is surjective" is \( \forall z \in Z \ \exists y \in Y \ g(y) = z \), so the proof must take an arbitrary \( z \in Z \); the \( y \) is the witness to be found, not something given. The distractor (vi) uses a hypothesis the statement does not have: nothing says \( f \) is surjective, and the claim holds without it. For example, with \( f \colon \{1\} \to \{1, 2\} \), \( f(1) = 1 \), and \( g \colon \{1, 2\} \to \{1\} \) constant, \( g \circ f \) and \( g \) are surjective and \( f \) is not.
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

### C. Going deeper

::: {#exr-functions-c1}
[C1: Exit check: composites]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( g \circ f \) is injective, then \( f \) is injective.
2. Give an example in which \( g \circ f \) is injective and \( g \) is not injective, and check both claims.
:::
:::

::: {.solution}
(a) Suppose \( g \circ f \) is injective. Let \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \); we must show \( x_1 = x_2 \). Applying \( g \) to both sides gives \( g(f(x_1)) = g(f(x_2)) \), because a function gives equal outputs at equal inputs. By @def-composition, this says \( (g \circ f)(x_1) = (g \circ f)(x_2) \). Since \( g \circ f \) is injective, \( x_1 = x_2 \). So \( f \) is injective.

(b) Let \( X = \{1\} \), \( Y = \{1, 2\} \), \( Z = \{1\} \); let \( f(1) = 1 \), and let \( g \colon \{1, 2\} \to \{1\} \) be the constant function \( g(1) = g(2) = 1 \). Then \( g \circ f \colon \{1\} \to \{1\} \) is injective, because its domain has only one element: if \( x_1, x_2 \in \{1\} \), then \( x_1 = 1 = x_2 \). And \( g \) is not injective: \( g(1) = g(2) \) with \( 1 \ne 2 \).

**Marking scheme.** (10 points)
- 2: fixes arbitrary \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \) and states the goal \( x_1 = x_2 \).
- 2: applies \( g \) to both sides, with the reason that a function gives equal outputs at equal inputs.
- 3: rewrites the result as an equation of values of \( g \circ f \) and invokes the injectivity of \( g \circ f \).
- 3: an example with explicit sets and functions, and both claims checked: \( g \circ f \) injective, and two different points with the same value under \( g \).

Fatal errors (0 for the step): assuming \( g \) is injective; starting from \( x_1 = x_2 \) and deriving \( f(x_1) = f(x_2) \) (the converse, entry (N5) of *Logic and Proof*, Chapter 8's catalogue); an example in which \( g \circ f \) is not defined because the codomain of \( f \) is not the domain of \( g \).
A proof by contrapositive (from \( x_1 \ne x_2 \), \( g \circ f \) injective gives \( g(f(x_1)) \ne g(f(x_2)) \), hence \( f(x_1) \ne f(x_2) \), since equal values of \( f \) would give equal values of \( g \)) earns full marks: 2 points for fixing \( x_1 \ne x_2 \) and the goal, 3 for the use of the injectivity of \( g \circ f \), and 2 for the step from \( g(f(x_1)) \ne g(f(x_2)) \) to \( f(x_1) \ne f(x_2) \).
:::

::: {#exr-functions-c2}
[C2: When the composite is a bijection]

Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be functions.

::: {.enumerate options="label=(\alph*)"}
1. Deduce from @exr-functions-c1 and @exr-functions-b2 that if \( g \circ f \) is bijective, then \( f \) is injective and \( g \) is surjective.
2. Give an example in which \( g \circ f \) is bijective and neither \( f \) nor \( g \) is bijective.
:::
:::

::: {.solution}
(a) Suppose \( g \circ f \) is bijective. Then \( g \circ f \) is injective, so \( f \) is injective by part (a) of @exr-functions-c1. And \( g \circ f \) is surjective, so \( g \) is surjective by the proof put in order in @exr-functions-b2.

(b) Take the functions of @exr-functions-c1 (b): \( f \colon \{1\} \to \{1, 2\} \), \( f(1) = 1 \), and \( g \colon \{1, 2\} \to \{1\} \), \( g(1) = g(2) = 1 \). Then \( g \circ f \colon \{1\} \to \{1\} \) sends \( 1 \) to \( 1 \), so \( g \circ f = \id_{\{1\}} \) by @prp-function-equality, which is bijective. But \( f \) is not surjective, since \( 2 \) is not an output; and \( g \) is not injective, since \( g(1) = g(2) \). So neither is bijective. Part (a) is sharp: it gives exactly the half of each property that survives, and this example shows that the other halves can fail together.
:::

<!-- dependency ledger
def-surjective (claim): (the warning after it) x^2 + x + 1 = (x + 1/2)^2 + 3/4 > 0; values 0, 2, 6, 12 | school algebra (F1-F2 convention); computation inline
def-injective (claim): negation of bounded quantifiers and of an implication | F1.8 §02 (paid): prp-bounded-quantifier-negation, prp-negated-implication, prose pointer "*Logic and Proof*, Chapter 6"
exm-injective-surjective-first (example): dividing by 3; n >= 1 gives 3n >= 3, n <= 0 gives 3n <= 0 | school algebra and order facts (F1-F2 convention); proved in AN1.1 (order) and F2.2 (integers)
exm-injective-surjective-first (claim): a function from a 3-element set to a 2-element set is not injective, etc. | F2.3 §01 (prose pointer "Section 4.1", pigeonhole, the principle stated in F2.1 §01's lattice-point puzzle); only the two specific cases (c), (d) are proved, by listing; nothing depends on the general claim
exm-square-three-ways (example): x^2 >= 0 > -1; existence of sqrt(y) for y >= 0 | school fact (F1-F2 convention); proved in AN1.1
thm-composition-injective-surjective (proof): f(x1), f(x2) in Y | (**) in def-function's paraphrase (every value lies in the codomain)
thm-composition-injective-surjective (proof): forall-E, exists-E, exists-I, forall-I in the prose tags | F1.4 (promised): quantifier rules (F1.4 §03-F1.4 §06), prose pointer; the bounded forms in the derivation are prp-bounded-quantifier-rules (cited)
thm-composition-injective-surjective (claim): level 0 = full derivation | F1.5 (promised): def-levels-of-proof (prose pointer, F1.5 §03)
thm-composition-injective-surjective (claim): closing lines of ->I and forall-I may be silent | F1.5 (promised): def-silent-steps, prose pointer
exr-functions-b1 (solution): parity (1 is odd, 2n even, not both) | thm-even-or-odd (F2.1 §01)
exr-functions-b1 (solution): x1^3 - x2^3 factorization; real cube roots exist; for x/sqrt(1+x^2): sqrt increasing on [0, inf), sqrt(x^2) = |x|, sqrt(1/t) = 1/sqrt(t) for t > 0 | school algebra (F1-F2 convention); cube roots proved in AN1.1 (thm-nth-root with a sign change)
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
-->
