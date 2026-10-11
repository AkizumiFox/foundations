# Gate 0: Part 0 Examination

Part 0 ends here. Its eight main-line chapters taught one skill in many forms: reading a mathematical statement exactly, and proving it in sentences that a reader can check line by line. This section is an examination on all of it, and the test of whether Part I will be readable: from Chapter 11 on, every proof assumes that negating a quantified statement, naming a witness, running an induction and chasing an element through a preimage are routine. A reader who comes to the book by a reading path that begins at Part I, such as a first course in real analysis, takes this Gate first, as an entry test, and goes back only to the sections that the remediation map at the end names. Grading your own work is a skill too; the front matter's page on getting feedback without a teacher describes the loop of attempting, writing, grading against the scheme and only then reading the solution.

## Instructions

::: {.algorithm}
- **Time: 2 hours.** Closed book, no notes; paper and pen. Attempt all six problems. The times in brackets are a guide; they add up to 120 minutes.
- Write complete proofs in plain prose, at level 3 of @def-levels-of-proof. Rule tags are allowed where a problem asks for them.
- Each problem is worth 10 points, 60 in all. Its solution is folded. Open a solution only after the two hours, and **grade before you read it**: apply the marking scheme at the end of the solution to your own script, point by point, and only then read the book's proof.
- **Pass line: 70% overall (42 of 60 points), and no core problem at 0.** The core problems are marked `core`: P1, P2, P4 and P5. They test what Chapter 11 uses from its first page: quantifiers and their negation, turning a derivation into prose, induction and recursion, sets and functions. P3 and P6 are not core.
- If you fail, follow the remediation map, then wait a week and retake the whole Gate (the same problems) before starting Part I.
:::

The definition drill comes first and is not scored. It is the one retrieval list of Part 0: every major definition of the Part, to be written from memory before the clock starts.

::: {.warning}
A proof that reads well is not thereby correct, and grading your own script is where a reader working alone is most easily fooled. Grade the step, not the impression: a marking-scheme line such as "\( y \) given as a function of \( \delta \)" is either on your page or it is not. A script that says "choose \( y \) close to \( 1 \)" in Problem P1 has not given \( y \) as a function of \( \delta \), however clear the idea, and loses those points.
:::

## Definition drill

::: {.check}
State each of the following **in symbols**, with every quantifier and every bound written out, as the book defines it. Allow about fifteen minutes, before the two hours start.

::: {.enumerate options="label=(Q\arabic*)"}
1. \( \Gamma \vdash \psi \).
2. \( \Gamma \models \psi \), for formulas of propositional logic.
3. \( \varphi \) is a tautology.
4. The side conditions of \( \rulename{\forall I} \) and of \( \rulename{\exists E} \) on the flagged name \( x_0 \).
5. \( \exists! x\, \varphi \).
6. \( A \subseteq B \).
7. \( \bigcap_{i \in I} A_i \), for a family \( (A_i)_{i \in I} \) of subsets of a set \( X \).
8. A function \( f \colon X \to Y \).
9. \( f \colon X \to Y \) is injective; \( f \) is surjective.
10. The image \( f(A) \) and the preimage \( f^{-1}(B) \).
11. An equivalence relation on \( X \); a partition of \( X \).
12. A greatest element and a maximal element of \( A \subseteq X \), for a partial order \( \preceq \) on \( X \).
13. A least upper bound of \( A \) in a partially ordered set \( (X, \preceq) \).
14. The principle of induction; the well-ordering of \( \nN \).
15. \( A \) is countable.
16. \( \card{A} = \card{B} \); \( \card{A} \le \card{B} \).
17. The axiom of choice.
:::
:::

::: {.solution}
The answers are the definitions as the book states them; the label after each answer is where to look when an answer is wrong.

::: {.enumerate options="label=(Q\arabic*)"}
1. For a list \( \Gamma = \varphi_1, \dots, \varphi_n \) (\( n \ge 0 \)): \( \Gamma \vdash \psi \) if **there is** a derivation whose premises all belong to \( \Gamma \) and whose last line is \( \psi \) (@def-derivable).
2. \( \Gamma \models \psi \) if for **every** valuation \( v \): if \( v(\varphi) = \mathrm{T} \) for every \( \varphi \) in \( \Gamma \), then \( v(\psi) = \mathrm{T} \) (@def-valid-argument).
3. \( v(\varphi) = \mathrm{T} \) for **every** valuation \( v \) (@def-tautology).
4. \( \rulename{\forall I} \), closing a flagged box with name \( x_0 \) and writing \( \forall x\, \varphi \) on line \( k \): at line \( k \), \( x_0 \) appears in no premise, in no assumption of a box still open at line \( k \), and not in \( \forall x\, \varphi \) (@def-rules-universal). \( \rulename{\exists E} \), from \( \exists x\, \varphi \) and a flagged box with name \( x_0 \) assuming \( \varphi[x_0/x] \) and ending in \( \chi \), writing \( \chi \) on line \( k \): \( x_0 \) does not appear in \( \chi \), in \( \exists x\, \varphi \), in any premise, or in any assumption of a box still open at line \( k \) (@def-rules-existential). "Appears" means written anywhere, after a quantifier symbol included.
5. \( \exists x\, \bigl( \varphi \wedge \forall y\, (\varphi[y/x] \to y = x) \bigr) \), where \( y \) is a variable other than \( x \) that does not appear in \( \varphi \) (@def-unique-existence).
6. \( \forall x\, (x \in A \to x \in B) \) (@def-subset).
7. \( \bigcap_{i \in I} A_i \coloneqq \{ x \in X : \forall i \in I\ (x \in A_i) \} \); for \( I = \emptyset \) it is \( X \) (@def-family-union-intersection).
8. A relation \( G \subseteq X \times Y \), the graph, with \( \forall x \in X\ \exists! \, y \in Y\ (x, y) \in G \), together with the codomain \( Y \): formally \( f = (G, Y) \) (@def-function).
9. Injective: \( \forall x_1 \in X\ \forall x_2 \in X\ \bigl( f(x_1) = f(x_2) \to x_1 = x_2 \bigr) \) (@def-injective). Surjective: \( \forall y \in Y\ \exists x \in X\ f(x) = y \) (@def-surjective).
10. For \( A \subseteq X \): \( y \in f(A) \iff y \in Y \wedge \exists a \in A\ f(a) = y \) (@def-image). For \( B \subseteq Y \): \( x \in f^{-1}(B) \iff x \in X \wedge f(x) \in B \) (@def-preimage).
11. A relation \( \sim \) on \( X \) with (Eq1) \( \forall x \in X\ x \sim x \); (Eq2) \( \forall x, y \in X\ (x \sim y \to y \sim x) \); (Eq3) \( \forall x, y, z \in X\ (x \sim y \wedge y \sim z \to x \sim z) \) (@def-equivalence-relation). A set \( \sP \) of subsets of \( X \) with (P1) \( \forall P \in \sP\ P \ne \emptyset \); (P2) \( \forall P, Q \in \sP\ (P \ne Q \to P \cap Q = \emptyset) \); (P3) \( \bigcup \sP = X \) (@def-partition).
12. \( g \) is a greatest element: \( g \in A \wedge \forall a \in A\ a \preceq g \) (@def-greatest-element). \( m \) is a maximal element: \( m \in A \wedge \neg \exists a \in A\ m \prec a \), where \( m \prec a \) means \( m \preceq a \wedge m \ne a \) (@def-maximal-element).
13. \( s \in X \) with (S1) \( \forall a \in A\ a \preceq s \), and (S2) \( \forall u \in X\ \bigl( (\forall a \in A\ a \preceq u) \to s \preceq u \bigr) \) (@def-order-supremum).
14. For every property \( P \) of natural numbers: if \( P(0) \) and \( \forall n \in \nN\ \bigl( P(n) \to P(n + 1) \bigr) \), then \( \forall n \in \nN\ P(n) \) (@ax-induction). Every non-empty \( S \subseteq \nN \) has a least element: \( S \ne \emptyset \to \exists m \in S\ \forall s \in S\ m \le s \) (@thm-well-ordering).
15. \( A = \emptyset \), or there is \( f \colon \nN \to A \) with \( \forall a \in A\ \exists n \in \nN\ f(n) = a \) (@def-countable).
16. \( \card{A} = \card{B} \) if there is a bijection \( A \to B \) (@def-equinumerous); \( \card{A} \le \card{B} \) if there is an injection \( A \to B \) (@def-card-le).
17. For every set \( I \) and every family \( (A_i)_{i \in I} \) of sets with \( \forall i \in I\ A_i \ne \emptyset \), there is \( c \colon I \to \bigcup_{i \in I} A_i \) with \( \forall i \in I\ c(i) \in A_i \) (@ax-choice).
:::

Count an item right only if every quantifier, every bound and the order of the quantifiers match. The commonest slips are a missing "\( \in X \)" bound in (Q9), "\( \exists y \)" for "\( \exists! \, y \)" in (Q8), and, in (Q12), "\( \forall a \in A\ a \preceq m \)" for maximal, which is the definition of greatest.
:::

## The problems

::: {#exr-gate-0-p1}
[P1: core]

*(20 minutes.)* Say that a function \( f \colon \nR \to \nR \) has **property L** if for every \( x \in \nR \) there is \( \delta > 0 \) such that for every \( y \in \nR \) with \( \abs{y - x} < \delta \), we have \( f(y) \ge f(x) \).

::: {.enumerate options="label=(\alph*)"}
1. Write property L in symbols, with bounded quantifiers.
2. Write its negation with no \( \neg \) in front of a quantifier, a connective or a parenthesis.
3. Prove that \( f(x) = x^2 \) does not have property L.
4. Prove that the function \( f \colon \nR \to \nR \) with \( f(x) = 1 \) for \( x > 0 \) and \( f(x) = 0 \) for \( x \le 0 \) (the indicator of \( (0, \infty) \), with codomain \( \nR \)) has property L, and that it does **not** have the property obtained from L by moving "there is \( \delta > 0 \)" to the front.
:::
:::

::: {.solution}
*(a)* Property L is
\[
\forall x \in \nR\ \exists \delta > 0\ \forall y \in \nR\ \bigl( \abs{y - x} < \delta \to f(y) \ge f(x) \bigr).
\]

*(b)* Push the negation inward one symbol at a time, as in the procedure of Section 4.9 ("Negating a definition, mechanically"): @prp-bounded-quantifier-negation three times, the bound of each quantifier kept, and @prp-negated-implication once. Write \( \alpha \) for \( \abs{y - x} < \delta \) and \( \beta \) for \( f(y) \ge f(x) \).
\[
\begin{aligned}
&\neg\, \forall x \in \nR\ \exists \delta > 0\ \forall y \in \nR\ (\alpha \to \beta) \\
&\dashv\vdash \exists x \in \nR\ \forall \delta > 0\ \neg\, \forall y \in \nR\ (\alpha \to \beta) \\
&\dashv\vdash \exists x \in \nR\ \forall \delta > 0\ \exists y \in \nR\ \neg (\alpha \to \beta) \\
&\dashv\vdash \exists x \in \nR\ \forall \delta > 0\ \exists y \in \nR\ (\alpha \wedge \neg\beta) .
\end{aligned}
\]
The first step does two moves at once (\( \neg\forall \) to \( \exists\neg \), then \( \neg\exists \) to \( \forall\neg \)). After the chain, \( \neg\beta \), that is \( \neg\bigl(f(y) \ge f(x)\bigr) \), is replaced by \( f(y) < f(x) \), a fact about the order of \( \nR \) and not a law of logic. The negation of L is therefore
\[
\exists x \in \nR\ \forall \delta > 0\ \exists y \in \nR\ \bigl( \abs{y - x} < \delta \wedge f(y) < f(x) \bigr).
\]
Note what stays: the bound \( \delta > 0 \) is kept, and only the quantifier in front of it changes; "\( \exists \delta \le 0 \)" would be the error of negating the bound. The implication becomes a conjunction, never another implication.

*(c)* We prove the negation (b) for \( f(x) = x^2 \), with the witness \( x = 1 \). Let \( \delta > 0 \) be arbitrary, and put
\[
y \coloneqq 1 - \tfrac12 \min\{\delta, 1\} .
\]
Since \( 0 < \min\{\delta, 1\} \le 1 \), we have \( \frac12 \le y < 1 \). Then \( \abs{y - 1} = \frac12 \min\{\delta, 1\} \le \frac12 \delta < \delta \), and, as \( 0 < y < 1 \), \( y^2 = y \cdot y < y \cdot 1 < 1 = f(1) \). So \( \abs{y - 1} < \delta \) and \( f(y) < f(1) \). Since \( \delta > 0 \) was arbitrary, the negation of L holds at \( x = 1 \), and \( x^2 \) does not have property L.

The order of the choices is the order of the quantifiers in (b): \( x \) is fixed before \( \delta \), and \( y \) is a function of \( \delta \). The minimum with \( 1 \) is needed: \( y \coloneqq 1 - \delta/2 \) fails for large \( \delta \), since \( \delta = 4 \) gives \( y = -1 \) and \( y^2 = 1 \not< 1 \).

*(d)* Let \( f \colon \nR \to \nR \) be the function of (d): \( f(x) = 1 \) for \( x > 0 \) and \( f(x) = 0 \) for \( x \le 0 \). Let \( x \in \nR \).

*Case 1: \( x > 0 \).* Take \( \delta \coloneqq x \), which is positive. If \( \abs{y - x} < x \), then \( y > x - x = 0 \), so \( f(y) = 1 = f(x) \), and \( f(y) \ge f(x) \).

*Case 2: \( x \le 0 \).* Take \( \delta \coloneqq 1 \). For every \( y \), \( f(y) \in \{0, 1\} \), so \( f(y) \ge 0 = f(x) \).

So \( f \) has property L. In Case 1, \( \delta \) **depends on \( x \)**: points close to \( 0 \) need small \( \delta \).

The swapped property is \( \exists \delta > 0\ \forall x \in \nR\ \forall y \in \nR\ (\abs{y - x} < \delta \to f(y) \ge f(x)) \). We prove its negation, \( \forall \delta > 0\ \exists x \in \nR\ \exists y \in \nR\ (\abs{y - x} < \delta \wedge f(y) < f(x)) \). Let \( \delta > 0 \), and take \( x \coloneqq \delta/4 \) and \( y \coloneqq -\delta/4 \). Then \( \abs{y - x} = \delta/2 < \delta \), while \( f(y) = 0 < 1 = f(x) \), since \( y < 0 < x \). So no single \( \delta \) serves every \( x \). Here \( x \) depends on \( \delta \), which is legitimate, because \( \delta \) is now fixed first.

**Marking scheme.** (10 points)
- 2: (a) correct, with \( \forall x \in \nR \), \( \exists \delta > 0 \), \( \forall y \in \nR \) in this order and the condition \( \abs{y - x} < \delta \) as the hypothesis of an implication (or as a bound \( \forall y \in \nR \) with \( \abs{y - x} < \delta \)).
- 3: (b) correct: the bounds kept (\( \forall \delta > 0 \), not \( \exists \delta \le 0 \)), every quantifier switched, and the implication negated to a conjunction.
- 2: (c) a witness \( x \) fixed **before** \( \delta \), and a \( y \) given as a function of \( \delta \) that works for **every** \( \delta > 0 \) (any correct \( y \), such as \( 1 - \frac12\min\{\delta, 1\} \) or \( 1 - \min\{\delta/2, \frac12\} \), earns the points).
- 3: (d) 2 for the case split proving L, with a \( \delta \) for each \( x \); 1 for refuting the swap, with \( x \) and \( y \) depending on \( \delta \).
Fatal errors (0 for the step): a negation that keeps "\( \to \)"; in (c), \( y \) chosen before \( \delta \) or for one particular \( \delta \); in the first half of (d), a single \( \delta \) claimed for all \( x \).
:::

::: {#exr-gate-0-p2}
[P2: core]

*(20 minutes.)* Here is a derivation of
\[
\begin{aligned}
&\forall z\, \exists y\, G(y, z),\ \forall y\, \exists x\, F(x, y), \\
&\forall x\, \forall y\, \forall z\, \bigl( (F(x, y) \wedge G(y, z)) \to H(x, z) \bigr) \vdash \forall z\, \exists x\, H(x, z),
\end{aligned}
\]
with four justifications left blank, marked (i)–(iv).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall z\, \exists y\, G(y, z)}
  \hypo {2} {\forall y\, \exists x\, F(x, y)}
  \hypo {3} {\forall x\, \forall y\, \forall z\, ((F(x, y) \wedge G(y, z)) \to H(x, z))}
  \open[z_0]
  \have {4} {\exists y\, G(y, z_0)} \Ae{1}
  \open[y_0]
  \hypo {5} {G(y_0, z_0)}
  \have {6} {\exists x\, F(x, y_0)} \by{(i)}{}
  \open[x_0]
  \hypo {7} {F(x_0, y_0)}
  \have {8} {\forall y\, \forall z\, ((F(x_0, y) \wedge G(y, z)) \to H(x_0, z))} \Ae{3}
  \have {9} {\forall z\, ((F(x_0, y_0) \wedge G(y_0, z)) \to H(x_0, z))} \Ae{8}
  \have {10} {(F(x_0, y_0) \wedge G(y_0, z_0)) \to H(x_0, z_0)} \Ae{9}
  \have {11} {F(x_0, y_0) \wedge G(y_0, z_0)} \ai{7,5}
  \have {12} {H(x_0, z_0)} \ie{10,11}
  \have {13} {\exists x\, H(x, z_0)} \by{(ii)}{}
  \close
  \have {14} {\exists x\, H(x, z_0)} \by{(iii)}{}
  \close
  \have {15} {\exists x\, H(x, z_0)} \Ee{4,5-14}
  \close
  \have {16} {\forall z\, \exists x\, H(x, z)} \by{(iv)}{}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Fill in the justifications (i)–(iv): the rule and the cited lines.
2. Explain why line 13 sits inside both of the boxes that begin at lines 5 and 7, and why each of these two boxes may close where it does.
3. Read \( F(x, y) \) as "\( f(x) = y \)", \( G(y, z) \) as "\( g(y) = z \)" and \( H(x, z) \) as "\( g(f(x)) = z \)", for functions \( f \colon X \to Y \) and \( g \colon Y \to Z \). Write the plain-prose proof that this derivation encodes, that the composite of two surjections is surjective, with one sentence for each box.
:::
:::

::: {.solution}
*(a)* (i) \( \rulename{\forall E} \) 2, with the term \( y_0 \) for \( y \). (ii) \( \rulename{\exists I} \) 12, with the witness \( x_0 \) for \( x \) in \( H(x, z_0) \). (iii) \( \rulename{\exists E} \) 6, 7–13: the existential of line 6 and the box of \( x_0 \). (iv) \( \rulename{\forall I} \) 4–15: the flagged box of \( z_0 \), whose range runs from its first line, line 4, to its last line, line 15 (@def-rules-universal).

*(b)* Line 12, \( H(x_0, z_0) \), contains the witness \( x_0 \). A box of \( \rulename{\exists E} \) may close only on a last line in which its own name does not appear (@def-rules-existential). So the box of \( x_0 \) cannot close on line 12; the \( \rulename{\exists I} \) of line 13 replaces \( x_0 \) by a bound variable first, and it must come **before** that box closes, that is, inside it, and therefore inside the box of \( y_0 \) that contains it.

The box of \( x_0 \) closes at line 14. Its name \( x_0 \) does not appear in the last line \( \exists x\, H(x, z_0) \), nor in the existential \( \exists x\, F(x, y_0) \) of line 6, nor in the premises 1–3 (where only the bound variable \( x \) is written), nor in the one open assumption at line 14, \( G(y_0, z_0) \) on line 5. The box of \( y_0 \) closes at line 15. Its name \( y_0 \) does not appear in \( \exists x\, H(x, z_0) \), nor in \( \exists y\, G(y, z_0) \) of line 4, nor in the premises; the only box still open at line 15 is the flagged box of \( z_0 \), which has no assumption. Of the four clauses, the last-line clause is the one that shapes this derivation: the other three hold for any fresh names, while the last line had to be prepared by line 13. The names \( x_0 \) and \( y_0 \) may not leave their boxes because each names one witness, about which only its box's assumption is known; outside, it would be treated as arbitrary, which is error (N3) of @exm-not-allowed-catalogue. The name \( z_0 \) is different: it may appear in lines 14 and 15, because its box is closed by \( \rulename{\forall I} \) at line 16, where it no longer appears.

*(c)* Let \( f \colon X \to Y \) and \( g \colon Y \to Z \) be surjective, and let \( z \in Z \) be arbitrary (the box of \( z_0 \)). Since \( g \) is surjective, there is \( y \in Y \) with \( g(y) = z \); fix one (the box of \( y_0 \), lines 5–14, eliminating line 4). Since \( f \) is surjective, there is \( x \in X \) with \( f(x) = y \); fix one (the box of \( x_0 \), lines 7–13, eliminating line 6). Then \( g(f(x)) = g(y) = z \), so \( z \) is a value of \( g \circ f \) (lines 8–13; premise 3 is the substitution of equals that the equation chain performs). Since \( z \) was arbitrary, \( g \circ f \) is surjective, which is the surjectivity half of @thm-composition-injective-surjective. The derivation leaves the bounds \( z \in Z \), \( y \in Y \), \( x \in X \) implicit; the prose restores them.

**Marking scheme.** (10 points)
- 4: (a), one point per blank: the \( \rulename{\forall E} \) with its line and instance term; the \( \rulename{\exists I} \) with its line; the inner \( \rulename{\exists E} \) citing line 6 and the box 7–13; the final \( \rulename{\forall I} \) citing the box 4–15.
- 2: (b) the fresh-name condition of \( \rulename{\exists E} \) stated with all its clauses, in terms of where the name **appears**, for each box's own name; and why \( x_0 \) and \( y_0 \) may not leave their boxes (so the \( \exists \)I must come first).
- 4: (c) "let \( z \in Z \)", "choose \( y \) with \( g(y) = z \)", "choose \( x \) with \( f(x) = y \)", "then \( g(f(x)) = z \)", in this order, each sentence carrying its box.
Fatal errors (0 for the step): "let \( x \) be arbitrary" for an \( \rulename{\exists E} \); prose in which \( y \) is chosen before \( z \) is fixed.
:::

::: {#exr-gate-0-p3}
[P3]

*(20 minutes.)* For each argument below, answer three questions. Is the conclusion true? Does the argument prove it? If not, which line fails, which entry of @exm-not-allowed-catalogue does it fall under, and what is a counterexample **to the illegal step** (not merely to the conclusion)?

::: {.enumerate options="label=(\alph*)"}
1. *Claim:* \( n^2 + n \) is even for every \( n \in \nN \). *Proof:* \( 0^2 + 0 = 0 \) is even. Assume that \( n^2 + n \) is even for all \( n \in \nN \). Then \( (n + 1)^2 + (n + 1) = (n^2 + n) + 2(n + 1) \) is even. By induction, the claim holds.
2. *Claim:* if \( A_n \subseteq \nR \) is bounded above for every \( n \in \nN \), then \( \bigcup_{n \in \nN} A_n \) is bounded above. *Proof:* For each \( n \), let \( M_n \) be an upper bound of \( A_n \). Let \( M \) be a number larger than every \( M_n \). Then \( M \) is an upper bound of the union.
:::
:::

::: {.solution}
*(a)* **The conclusion is true.** Let \( n \in \nN \). By @thm-division-algorithm with divisor \( 2 \), \( n = 2q + r \) with \( q \in \nZ \) and \( r \in \{0, 1\} \). If \( r = 0 \), then \( n^2 + n = n(n + 1) = 2\bigl(q(n + 1)\bigr) \); if \( r = 1 \), then \( n + 1 = 2(q + 1) \) and \( n^2 + n = 2\bigl(n(q + 1)\bigr) \). In both cases the factor in brackets is an integer (@prp-integers-closed), so \( 2 \mid n^2 + n \) (@def-divides).

**The argument does not prove it.** The failing line is "Assume that \( n^2 + n \) is even for all \( n \in \nN \)". That assumption is the claim itself, so everything after it is circular: entry (N9) of @exm-not-allowed-catalogue, citing a line that is not available, here the goal. The step of an induction is a \( \rulename{{\to}I} \) box inside a \( \rulename{\forall I} \) box: fix one arbitrary \( n \in \nN \), assume that \( n^2 + n \) is even **for this \( n \)**, and derive that \( (n + 1)^2 + (n + 1) \) is even. With that one line changed, the rest of the argument is correct: the identity holds, since both sides equal \( n^2 + 3n + 2 \), and a sum of two even integers is even (\( 2a + 2b = 2(a + b) \)).

*A counterexample to the illegal step.* The argument infers \( \forall n\, P(n) \) from \( P(0) \) and from "if \( P(n) \) for all \( n \), then \( P(n + 1) \) for all \( n \)". Take \( P(n) \): "\( n = 0 \)". Then \( P(0) \) holds, and the second premise holds because its hypothesis "\( P(n) \) for all \( n \)" is false (\( P(1) \) fails), so the implication is vacuously true. Yet \( \forall n\, P(n) \) is false. The conclusion of (a) is true, so it has no counterexample; the step has one.

*(b)* **The conclusion is false.** Take \( A_n \coloneqq \{n\} \). Each \( A_n \) is bounded above, by \( n \). The union is \( \nN \), and \( \nN \) is not bounded above in \( \nR \): for every real \( M \) there is a natural number larger than \( M \) (a school fact here; Chapter 11 proves it from its axiom).

**The failing line** is "Let \( M \) be a number larger than every \( M_n \)". From "for every \( n \) there is a number larger than \( M_n \)" it passes to "there is a number larger than \( M_n \) for every \( n \)": from \( \forall n\, \exists M \) to \( \exists M\, \forall n \). This is entry (N2) of @exm-not-allowed-catalogue, a witness that depends on \( n \) presented as uniform. It is the converse of @prp-exists-forall-swap, and the converse is not even valid: @exm-counter-model-swap gives a counter-model. *A counterexample to the step:* \( M_n \coloneqq n \). For each \( n \) there is a number larger than \( M_n \), namely \( n + 1 \), and no real number is larger than every \( n \).

The line before it is not the error. Choosing an upper bound \( M_n \) for every \( n \) at once, with no rule, is a use of the axiom of choice (@ax-choice), and the book allows it, flagged. And for **finitely** many indices the bad line becomes correct: \( \max\{M_0, \dots, M_k\} + 1 \) exists by @prp-finite-max, so a union of finitely many sets bounded above is bounded above.

**Marking scheme.** (10 points)
- (a), 5 points. 1: says the conclusion is true, with a reason (a proof or a correct induction). 2: points to the line "assume … for all \( n \)". 1: names the error, circularity, (N9). 1: gives a counterexample to the step, not to the conclusion.
- (b), 5 points. 1: says the conclusion is false, with a witness such as \( A_n = \{n\} \). 2: points to the line "let \( M \) be larger than every \( M_n \)". 1: names the quantifier swap \( \forall n\, \exists M \) to \( \exists M\, \forall n \), or (N2). 1: gives a counterexample to the step, not to the conclusion, such as \( M_n = n \).
Fatal errors (0 for the part): in (a), calling the argument correct; in (b), locating the error in the choice of the \( M_n \).
:::

::: {#exr-gate-0-p4}
[P4: core]

*(20 minutes.)* Let \( a_0 = 0 \), \( a_1 = 1 \) and \( a_{n+2} = 3a_{n+1} - 2a_n \) for \( n \in \nN \).

::: {.enumerate options="label=(\alph*)"}
1. Say which result guarantees that these equations define a sequence.
2. Prove that \( a_n = 2^n - 1 \) for every \( n \in \nN \).
3. Suppose instead that \( a_1 = 2 \), with \( a_0 \) and the rule unchanged. Compute \( a_2 \) and \( a_3 \), and say exactly which line of your proof in (b) fails.
:::
:::

::: {.solution}
*(a)* Two-step recursion, @cor-two-step-recursion, with \( X = \nR \), \( a = 0 \), \( b = 1 \) and \( h(n, x, y) \coloneqq 3y - 2x \): there is exactly one sequence \( (a_n)_{n \in \nN} \) of reals with \( a_0 = 0 \), \( a_1 = 1 \) and \( a_{n+2} = 3a_{n+1} - 2a_n \) for every \( n \in \nN \).

*(b)* The rule looks two steps back, so the induction carries two values at once. For \( n \in \nN \) let \( Q(n) \) be the statement
\[
a_n = 2^n - 1 \quad \text{and} \quad a_{n+1} = 2^{n+1} - 1 .
\]
*Base case.* \( Q(0) \) says \( a_0 = 2^0 - 1 = 0 \) and \( a_1 = 2^1 - 1 = 1 \), and both hold.

*Step.* Let \( n \in \nN \) and suppose \( Q(n) \). The second half of \( Q(n) \) is the first half of \( Q(n + 1) \). For the second half, by the rule and both halves of \( Q(n) \),
\[
\begin{aligned}
a_{n+2} &= 3a_{n+1} - 2a_n = 3(2^{n+1} - 1) - 2(2^n - 1) \\
&= 3 \cdot 2^{n+1} - 2^{n+1} - 1 = 2 \cdot 2^{n+1} - 1 = 2^{n+2} - 1 ,
\end{aligned}
\]
where \( 2 \cdot 2^n = 2^{n+1} \) and \( 2 \cdot 2^{n+1} = 2^{n+2} \) by @def-power. So \( Q(n + 1) \) holds. By @ax-induction, \( Q(n) \) holds for every \( n \in \nN \), and in particular \( a_n = 2^n - 1 \) for every \( n \in \nN \). This is the pair induction of the two-step example in Section 7.3, after @def-power.

*Alternatively,* by strong induction (@thm-strong-induction): let \( n \in \nN \) and suppose \( a_k = 2^k - 1 \) for every \( k < n \). If \( n = 0 \) or \( n = 1 \), check the value directly. If \( n \ge 2 \), then \( n - 1 \) and \( n - 2 \) are natural numbers (@lem-naturals-arithmetic (c), twice) smaller than \( n \), so the hypothesis applies to both, and the same computation with \( n - 2 \) in place of \( n \) gives \( a_n = 2^n - 1 \). The two values \( n = 0, 1 \) are exactly where the hypothesis would be used out of range.

*(c)* Now \( a_2 = 3 \cdot 2 - 2 \cdot 0 = 6 \) and \( a_3 = 3 \cdot 6 - 2 \cdot 2 = 14 \), while \( 2^2 - 1 = 3 \) and \( 2^3 - 1 = 7 \). The failing line is the base case at \( n = 1 \): in the proof of (b), the half "\( a_1 = 2^1 - 1 \)" of \( Q(0) \), since now \( a_1 = 2 \ne 1 \). The check \( a_0 = 0 \) still holds, and the step is still a valid implication; but every value from \( a_2 \) on is computed from \( a_1 \), so the failure propagates. (The same induction proves \( a_n = 2^{n+1} - 2 \) for the new sequence.)

**Marking scheme.** (10 points)
- 1: (a) names two-step recursion (@cor-two-step-recursion), or @thm-recursion applied to pairs.
- 2: (b) states a form of induction under which both \( a_0 \) and \( a_1 \) are checked: two base cases for strong induction, or the base \( Q(0) \) of a pair statement.
- 3: (b) the step's algebra, \( 3(2^{n+1} - 1) - 2(2^n - 1) = 2^{n+2} - 1 \) (or the same with shifted indices).
- 1: (b) the induction hypothesis used only for indices where it is available (no \( a_{-1} \); in strong induction, \( n \ge 2 \) in the step).
- 1: (b) the conclusion, citing the induction principle used.
- 2: (c) \( a_2 = 6 \), \( a_3 = 14 \) (1), and the failing line identified as the check of \( a_1 \) (1).
Fatal errors (0 for the step): only \( a_0 \) checked, so \( a_1 \) is never verified; an induction hypothesis "for all \( n \)", entry (N9) of @exm-not-allowed-catalogue.
:::

::: {#exr-gate-0-p5}
[P5: core]

*(20 minutes.)* Let \( f \colon X \to Y \) be a function.

::: {.enumerate options="label=(\alph*)"}
1. For a family \( (B_i)_{i \in I} \) of subsets of \( Y \), prove that
\[
f^{-1}\Bigl( Y \setminus \bigcup_{i \in I} B_i \Bigr) = \bigcap_{i \in I} \bigl( X \setminus f^{-1}(B_i) \bigr),
\]
with the intersection taken in \( X \).
2. Prove that \( f(X \setminus A) \subseteq Y \setminus f(A) \) for **every** \( A \subseteq X \) if and only if \( f \) is injective.
:::
:::

::: {.solution}
*(a)* Put \( B \coloneqq \bigcup_{i \in I} B_i \), a subset of \( Y \) since every \( B_i \) is. Then
\[
\begin{aligned}
f^{-1}(Y \setminus B) &= X \setminus f^{-1}(B) = X \setminus \bigcup_{i \in I} f^{-1}(B_i) \\
&= \bigcap_{i \in I} \bigl( X \setminus f^{-1}(B_i) \bigr).
\end{aligned}
\]
The first equality is @thm-preimage-operations (c), the second is @thm-preimage-operations (a), and the third is @thm-de-morgan-families, applied to the family \( \bigl(f^{-1}(B_i)\bigr)_{i \in I} \) of subsets of \( X \), with the intersection taken in \( X \). Nothing excludes \( I = \emptyset \): then both sides are \( X \).

*Alternatively,* element by element. For every \( x \): \( x \in f^{-1}(Y \setminus B) \) iff \( x \in X \) and \( f(x) \in Y \setminus B \), iff \( x \in X \) and \( f(x) \notin B \) (as \( f(x) \in Y \) anyway), iff \( x \in X \) and there is no \( i \in I \) with \( f(x) \in B_i \), iff \( x \in X \) and for every \( i \in I \), \( x \notin f^{-1}(B_i) \), iff \( x \in X \) and for every \( i \in I \), \( x \in X \setminus f^{-1}(B_i) \), iff \( x \in \bigcap_{i \in I} (X \setminus f^{-1}(B_i)) \). The steps use @def-preimage, @def-family-union-intersection, @def-set-operations and @prp-bounded-quantifier-negation (b).

*(b)* \( (\Leftarrow) \) Suppose \( f \) is injective, and let \( A \subseteq X \) and \( y \in f(X \setminus A) \). By @def-image there is \( x \in X \setminus A \) with \( f(x) = y \); in particular \( y \in Y \). Suppose, for contradiction, that \( y \in f(A) \). Then there is \( a \in A \) with \( f(a) = y \). So \( f(x) = f(a) \), and injectivity gives \( x = a \in A \), contradicting \( x \notin A \). Hence \( y \notin f(A) \), so \( y \in Y \setminus f(A) \). As \( y \) was arbitrary, \( f(X \setminus A) \subseteq Y \setminus f(A) \), and \( A \) was arbitrary.

\( (\Rightarrow) \) By contrapositive, as in @exm-square-even-via-contrapositive. Suppose \( f \) is not injective: by @prp-bounded-quantifier-negation (a), twice, and @prp-negated-implication there are \( x_1, x_2 \in X \) with \( f(x_1) = f(x_2) \) and \( x_1 \ne x_2 \). Take \( A \coloneqq \{x_1\} \). Then \( x_2 \in X \setminus A \), so \( f(x_2) \in f(X \setminus A) \). But \( f(x_2) = f(x_1) \in f(A) \), so \( f(x_2) \notin Y \setminus f(A) \). So the inclusion fails for this \( A \), and it does not hold for every \( A \subseteq X \).

The two inclusions hide one witness each: \( y \in f(X \setminus A) \) hands us an \( x \), and \( y \in f(A) \) hands us an \( a \). The proof works by comparing the two, which is what injectivity is for. Compare @thm-image-intersection (b), which characterizes injectivity through intersections in the same way.

**Marking scheme.** (10 points)
- 4: (a) by either route. For the first, each cited result must match its use (which part of @thm-preimage-operations, and De Morgan in \( X \)); for the second, each equivalence justified by a definition. A proof of the two inclusions separately earns the same marks.
- 3: (b) \( (\Leftarrow) \), with the witness \( x \in X \setminus A \) of \( y \in f(X \setminus A) \) and the witness \( a \in A \) of \( y \in f(A) \) both named, and injectivity applied to them.
- 3: (b) \( (\Rightarrow) \), by contrapositive or contradiction, with a correct set \( A \) built from the two points with the same value.
Fatal errors (0 for the step): treating \( y \in f(A) \) as "\( x \in A \)" for the \( x \) already in hand (a skipped \( \rulename{\exists E} \)); proving \( (\Rightarrow) \) from the inclusion for one given \( A \) only (the hypothesis "for every \( A \)" dropped; choosing one \( A \) where it fails, as above, is correct), or with "for every \( A \)" read as "for some \( A \)".
:::

::: {#exr-gate-0-p6}
[P6]

*(20 minutes.)* Let \( S \) be the set of sequences \( (a_n)_{n \in \nN} \) of natural numbers, indexed from \( 0 \), with \( a_n \le n \) for every \( n \in \nN \); a sequence is a function \( \nN \to \nN \), so \( S \subseteq \nN^{\nN} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( S \) is uncountable.
2. A sequence \( (a_n) \) is **eventually constant** if there is \( N \in \nN \) with \( a_n = a_N \) for every \( n \ge N \). Let \( E \subseteq S \) consist of the sequences in \( S \) that are eventually constant. Prove that \( E \) is countable, and explain why running your construction from (a) on a list of \( E \) produces no contradiction.
:::
:::

::: {.solution}
*(a)* The obvious diagonal, \( g(n) \coloneqq f_n(n) + 1 \), leaves \( S \): already \( g(0) \ge 1 > 0 \). Worse, place \( 0 \) offers no room at all, since every sequence in \( S \) has \( a_0 = 0 \). So the diagonal is shifted by one place: the \( n \)-th sequence of the list is made to differ at place \( n + 1 \), where there are at least two values to choose from.

Let \( f \colon \nN \to S \) be an arbitrary function, and write \( f_n \coloneqq f(n) \). Define \( g \colon \nN \to \nN \) by \( g(0) \coloneqq 0 \) and, for \( n \in \nN \),
\[
g(n + 1) \coloneqq
\begin{cases}
0 & \text{if } f_n(n + 1) \ne 0, \\
1 & \text{if } f_n(n + 1) = 0 .
\end{cases}
\]
This defines \( g \) on all of \( \nN \), since every natural number is \( 0 \) or \( n + 1 \) for exactly one \( n \in \nN \) (@lem-naturals-arithmetic (c)). Then \( g \in S \): \( g(0) = 0 \le 0 \), and \( g(n + 1) \le 1 \le n + 1 \). For every \( n \in \nN \), \( g(n + 1) \ne f_n(n + 1) \) by the two cases, so \( g \ne f_n \). Hence \( g \) is not a value of \( f \), and \( f \) is not surjective. Since \( f \) was arbitrary, there is no surjection \( \nN \to S \). And \( S \ne \emptyset \), since the zero sequence lies in \( S \). By @def-countable, \( S \) is not countable.

*(b)* For \( N \in \nN \) let \( E_N \) be the set of sequences \( (a_n) \in S \) with \( a_n = a_N \) for every \( n \ge N \). By the definition of eventually constant, \( E = \bigcup_{N \in \nN} E_N \).

*Each \( E_N \) is countable.* For \( N = 0 \), a sequence in \( E_0 \) is constant with value \( a_0 \le 0 \), so \( E_0 \) has one element, the zero sequence; a constant map \( \nN \to E_0 \) is onto, and \( E_0 \) is countable. Let \( N \ge 1 \), and define \( \pi \colon E_N \to \nN^{N+1} \) by \( \pi(a) \coloneqq (a_0, a_1, \dots, a_N) \), an \( (N + 1) \)-tuple. It is injective: if \( \pi(a) = \pi(b) \), then \( a_k = b_k \) for \( k \le N \), by the characteristic property of tuples (Section 6.3), and for \( n \ge N \), \( a_n = a_N = b_N = b_n \); so \( a = b \) (@prp-function-equality). The set \( \nN^{N+1} \) is countable by @cor-product-countable, as \( N + 1 \ge 2 \), so by @thm-countable-characterizations, (i) \( \Rightarrow \) (ii), there is an injection \( j \colon \nN^{N+1} \to \nN \). Then \( j \circ \pi \colon E_N \to \nN \) is injective (@thm-composition-injective-surjective), and \( E_N \) is countable by (ii) \( \Rightarrow \) (i).

*So \( E \) is countable,* as a union of countably many countable sets, by @thm-countable-union. That theorem uses the axiom of choice once, to pick a list of each \( E_N \). Here the choice can be avoided (compare @exm-choice-free-unions; see the marking scheme). The solution does not need this; citing @thm-countable-union is a complete proof.

In fact each \( E_N \) is finite: \( a_0, a_1, \dots, a_N \) can take \( 1, 2, \dots, N + 1 \) values, so \( E_N \) has \( (N + 1)! \) elements (@def-sum-product), which is \( 1, 2, 6, 24, 120 \) for \( N = 0, \dots, 4 \). This count rests on @exr-finite-sets-c2 and an induction on the number of factors, and it earns the same marks.

*Why there is no contradiction.* The set \( E \) is countable and non-empty, so it has a list: a surjection \( e \colon \nN \to E \). The construction of (a) applies to \( e \), since \( e \) is in particular a function \( \nN \to S \), and produces \( g \in S \) with \( g \ne e(n) \) for every \( n \). Since every element of \( E \) is some \( e(n) \), this shows \( g \notin E \): the diagonal sequence is not eventually constant. That is all it shows. A diagonal argument proves that a given list misses something in the set the diagonal element lives in, here \( S \); it contradicts the countability of \( E \) only if the diagonal element lies in \( E \), and it does not.

**Marking scheme.** (10 points)
- 1: (a) starts from an arbitrary list, a function \( \nN \to S \), not a particular one.
- 2: (a) defines a diagonal element that lies in \( S \), with the problem at place \( 0 \) handled.
- 2: (a) shows that it differs from every \( f_n \), at a named place.
- 1: (a) concludes, with the form "countable means empty or the image of \( \nN \)" handled (\( S \ne \emptyset \)).
- 2: (b) writes \( E \) as a countable union of countable sets, with a reason why each piece is countable (an injection into \( \nN \), a surjection from \( \nN \), or finiteness via @exr-finite-sets-c2). Alternative route, same 2 points: an injection of \( E \) into the finite sequences of @exr-countable-unions-and-choice-b2, \( a \mapsto (k \mapsto a_{k-1}) \) on \( \{1, \dots, N + 1\} \) with \( N \) least such that \( a \in E_N \), with injectivity checked and @thm-countable-characterizations cited.
- 2: (b) explains that the diagonal element of a list of \( E \) lies in \( S \) but not in \( E \), so it contradicts nothing.
Fatal errors (0 for the step): a diagonal element not in \( S \), such as \( g(n) \coloneqq f_n(n) + 1 \), which already has \( g(0) \ge 1 > 0 \); proving (a) for one particular list.
:::

## Remediation map

Add up your points. A pass is 42 of 60 with no core problem (P1, P2, P4, P5) at \( 0 \). For each problem where you lost more than 3 points, reread the sections in its row, redo their A exercises and one C exercise. Then retake that problem if you passed, or the whole Gate after a week if you failed. A wrong answer in the definition drill sends you to the label printed after its answer.

| Problem | What it tests | Sections to reread |
|---|---|---|
| P1 | quantifiers, bounds and their negation; the order of choices | Section 4.1 (@def-bounded-quantifier); Section 4.9 (@prp-quantifier-negation, @prp-negated-implication, @prp-bounded-quantifier-negation); Section 4.10 (@exm-uniform-implies-continuous); Section 5.2 (@exm-rhetoric-universal) |
| P2 | the quantifier rules and their side conditions; a derivation read as prose | Sections 4.3–4.6 (@def-rule-universal-elimination, @def-rules-universal, @def-rule-existential-introduction, @def-rules-existential); Sections 5.2–5.3 (@exm-rhetoric-existential, @def-levels-of-proof); Section 6.4 (@thm-composition-injective-surjective) |
| P3 | checking a proof; is the conclusion true, and does the argument prove it | Section 5.6 (@exm-not-allowed-catalogue); Section 3.2 (@ax-induction); Section 4.6 (@prp-exists-forall-swap); Section 4.11 (@exm-counter-model-swap); Section 7.2 (@thm-induction, and "How induction proofs go wrong", @exm-all-equal-induction) |
| P4 | recursion and induction with two starting values | Section 3.2 (@thm-strong-induction); Section 7.2 (@thm-strong-induction-from-base); Section 7.3 (@cor-two-step-recursion, and the two-step example after @def-power) |
| P5 | images and preimages, element by element | Section 6.2 (@thm-de-morgan-families); Section 6.6 (@thm-preimage-operations, @thm-image-intersection) |
| P6 | countable sets and the diagonal argument | Section 8.2 (@def-countable); Section 8.3 (@thm-countable-union); Section 8.4 (@thm-binary-sequences-uncountable, @thm-cantor) |

<!-- dependency ledger
exr-gate-0-p1 (solution): of two reals exactly one of a < b, a >= b holds; min{d, 1} > 0 and <= d for d > 0; 0 < y < 1 implies y^2 < y < 1; |y - x| < x implies y > 0 | school facts about the order of R (Part 0 convention; Ch 11 states them as axioms)
exr-gate-0-p1 (solution): a law may be applied to a part of a formula under quantifiers, in the chain of (b) | Ch 4 Section 4.9, the paragraph after the procedure "Negating a formula" (unlabelled; recalled in prose by the subsection name)
exr-gate-0-p3 (solution): N is not bounded above in R (for every real M some natural number exceeds M) | school fact (Part 0 convention); Chapter 11 proves it, prose pointer only
exr-gate-0-p3 (solution): (n + 1)^2 + (n + 1) = (n^2 + n) + 2(n + 1); a sum of two even integers is even | school algebra; def-divides with prp-integers-closed, inline
exr-gate-0-p4 (solution): integer arithmetic 3 * 2^(n+1) - 2^(n+1) = 2 * 2^(n+1) (distributivity) | school algebra; prp-power-laws
exr-gate-0-p6 (solution): each E_N has (N + 1)! elements (an aside, not used by the proof) | exr-finite-sets-c2 iterated by induction on the number of factors (a solution may cite an earlier exercise)
exr-gate-0-p6 (solution): two (N + 1)-tuples are equal exactly when they agree in every place | Section 6.3, "Longer lists" (prose, no label)
-->
