# Counter-models

Section 7.1 gave every formula a meaning in a structure. This section uses it to answer the question Chapters 5 and 6 left open: when a search for a derivation stalls, is there no derivation, or only no derivation found yet? The answer is a **counter-model**, a structure with an assignment in which the premises are true and the conclusion false (@def-first-order-entailment), together with one statement, soundness for predicate logic, that turns it into a proof that no derivation exists.

::: {.remark}
[Looking back]

Sections 4.5 and 4.6 refuted a propositional claim by a row that made its counterexample set true, and searched for that row systematically; Section 4.7 proved that a refuting row rules out every derivation. This section does the same with structures: the counter-model is the row, the procedure below is the search, and the side-condition table plays the part of Section 4.7's rule-by-rule table.
:::

## Three pictures

Section 5.3 called a reading in which the premises are true and the conclusion false a counter-reading. Here are three, drawn as in Section 7.1.

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \begin{scope}
    \node at (0.8,1.3) {(A)};
    \node[elt, label=below:$a$, label=above:$P$] (pa) at (0,0) {};
    \node[elt, label=below:$b$, label=above:$Q$] (pb) at (1.6,0) {};
  \end{scope}
  \begin{scope}[xshift=3.4cm]
    \node at (1.6,1.3) {(B)};
    \node at (-0.6,0) {$\cdots$};
    \node[elt, label=below:$-1$] (m1) at (0,0) {};
    \node[elt, label=below:$0$] (n0) at (0.8,0) {};
    \node[elt, label=below:$1$] (n1) at (1.6,0) {};
    \node[elt, label=below:$2$] (n2) at (2.4,0) {};
    \node[elt, label=below:$3$] (n3) at (3.2,0) {};
    \node at (3.8,0) {$\cdots$};
    \draw[rel] (n0) -- node[above] {\small is above} (m1);
    \draw[rel] (n1) -- (n0);
    \draw[rel] (n2) -- (n1);
    \draw[rel] (n3) -- (n2);
  \end{scope}
  \begin{scope}[xshift=8.4cm]
    \node at (0.8,1.3) {(C)};
    \node[elt, label=below:{$a$, named $c$}] (ca) at (0,0) {};
    \node[elt, label=below:$b$, label=above:$P$] (cb) at (1.6,0) {};
  \end{scope}
\end{tikzpicture}
\end{center}
```

*Three counter-readings. (A) \( P \) holds at \( a \) and \( Q \) at \( b \): \( \exists x\, P(x) \wedge \exists x\, Q(x) \) is true, with the witnesses \( a \) and \( b \), and \( \exists x\, (P(x) \wedge Q(x)) \) is false, since no dot has both labels; so the converse of @prp-exists-and does not follow (Section 5.6 asked). (B) The integers, with \( R(x, y) \) read as \( x > y \). Only the arrows to the next integer down are drawn; \( R \) is the whole order \( > \), so \( R(x, y) \) holds whenever a chain of arrows leads from \( x \) to \( y \). \( \forall y\, \exists x\, R(x, y) \) is true, since every integer \( y \) has \( y + 1 \) above it, and \( \exists x\, \forall y\, R(x, y) \) is false, since an integer above every integer would be above itself; so the converse of @prp-exists-forall-swap does not follow. (C) \( P \) holds at \( b \), and the constant \( c \) names \( a \): \( \exists x\, P(x) \) is true, at \( b \), and \( P(c) \) is false (@exr-existential-introduction-c2 asked why no derivation was found).*

Each picture is a structure in the sense of Section 7.1: a domain with a meaning for every symbol. The rest of this section checks such pictures by the clauses, finds them by a procedure, and shows why one of them rules out every derivation.

::: {.check}
Draw two dots that make \( \forall x\, (P(x) \vee Q(x)) \) true and \( \forall x\, P(x) \vee \forall x\, Q(x) \) false.
:::

::: {.solution}
Picture (A) again: each dot has \( P \) or \( Q \); \( \forall x\, P(x) \) fails at \( b \), and \( \forall x\, Q(x) \) fails at \( a \).
:::

::: {.check}
In picture (C), which clauses of @def-satisfaction decide \( \exists x\, P(x) \), and at which element?
:::

::: {.solution}
(S7) asks for some \( d \in D \) with \( \fM, \ell[x \mapsto d] \models P(x) \); at \( d = b \), (S1) asks whether \( b \in P^{\fM} \), and it is.
:::

## Counter-models

A counter-model is found the way a refuting row was found in Chapter 4, by working backwards from what must fail. The conclusion must be false, so read off what that demands; the premises must be true, so read off what they demand; and then build the smallest structure meeting both. The worked examples that follow (the swap, the converses of @prp-exists-and and of the \( \forall \)/\( \vee \) law, \( \exists x\, P(x) \vdash P(c) \), and \( P(x_0) \vdash \forall x\, P(x) \)) are sequents whose derivations stalled or were blocked in earlier sections.

::: {#exm-counter-model-swap}
[The swap of \( \exists \) and \( \forall \)]

Show that
\[
\forall y\, \exists x\, R(x, y) \not\models \exists x\, \forall y\, R(x, y) ,
\]
first by a structure on \( \nZ \), then by a structure with two elements.
:::

::: {.solution}
Both formulas are sentences, so by @lem-free-coincidence we need only a structure; any assignment will do.

*A structure on \( \nZ \).* Let \( \fM \) have domain \( \nZ \) and \( R^{\fM} = \{ (x, y) : x > y \} \), so that \( R(x, y) \) says "\( x > y \)". The premise says "every integer has an integer above it". To check it by (S6) and (S7): for each \( e \in \nZ \) we need some \( d \in \nZ \) with \( (d, e) \in R^{\fM} \), that is, \( d > e \); \( d = e + 1 \) works. The conclusion says "some integer is above every integer". By (S7) and (S6) it would need a \( d \in \nZ \) with \( d > e \) for **every** \( e \in \nZ \); but \( e = d \) gives \( d > d \), which is false. So \( \fM \models \forall y\, \exists x\, R(x, y) \) and \( \fM \not\models \exists x\, \forall y\, R(x, y) \).

*A structure with two elements.* Let \( D = \{ a, b \} \) and \( R^{\fM} = \{ (a, a), (b, b) \} \), so that \( R(x, y) \) says "\( x \) is \( y \)". Premise: for \( e = a \) take \( d = a \), and for \( e = b \) take \( d = b \); both pairs are in \( R^{\fM} \). Conclusion: \( d = a \) fails at \( e = b \), since \( (a, b) \notin R^{\fM} \), and \( d = b \) fails at \( e = a \). So the premise is true and the conclusion false.

The pattern is the one Section 5.1 read as a game. In the premise the witness \( x \) is chosen **after** \( y \) and may depend on it (\( x = y + 1 \), or \( x = y \)); the conclusion asks for one \( x \) that works for every \( y \) in advance. A one-element structure cannot separate the two sentences: with \( D = \{ a \} \), both are true if \( (a, a) \in R^{\fM} \) and both false otherwise. Two elements are the least that will do.
:::

The two-element structure is the \( \nZ \) structure's idea at its smallest: each element is related to something, and nothing is related to everything.

**Picture (A), checked by the clauses.** With \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \), the premise of the converse of @prp-exists-and holds by (S5) and (S7), with witnesses \( a \) and \( b \), and the conclusion fails, since \( a \notin Q^{\fM} \) and \( b \notin P^{\fM} \):
\[
\exists x\, P(x) \wedge \exists x\, Q(x) \not\models \exists x\, (P(x) \wedge Q(x)) .
\]
The same structure refutes the converse of the \( \forall \)/\( \vee \) law of @prp-quantifier-distribution, since each element is in \( P^{\fM} \) or in \( Q^{\fM} \), and neither set is all of \( D \):
\[
\forall x\, (P(x) \vee Q(x)) \not\models \forall x\, P(x) \vee \forall x\, Q(x) .
\]
Picture (C): with \( c^{\fM} = a \) and \( P^{\fM} = \{ b \} \), \( \exists x\, P(x) \) holds with the witness \( b \), and \( P(c) \) fails, since \( a \notin P^{\fM} \). So \( \exists x\, P(x) \not\models P(c) \). In \( \nZ \), with \( P \) and \( Q \) read as "even" and "odd": some integer is even and some integer is odd, but no integer is both; and every integer is even or odd, but it is false that every integer is even, and false that every integer is odd.

**The assignment is part of a counter-model.** Section 5.4 showed why \( \rulename{\forall I} \) may not generalize over a name in a premise: from \( P(x_0) \) one would "derive" \( \forall x\, P(x) \). Here \( x_0 \) is a **variable**, free in the premise, so a counter-model needs an assignment as well as a structure. Let \( \fM \) have domain \( \nZ \) with \( P^{\fM} \) the set of even integers, and let \( \ell(x_0) = 2 \). Then \( \fM, \ell \models P(x_0) \), since \( 2 \) is even, and \( \fM, \ell \not\models \forall x\, P(x) \), since (S6) fails at \( d = 1 \). So \( P(x_0) \not\models \forall x\, P(x) \). Under the assignment with \( \ell(x_0) = 1 \) the premise is false, and that assignment refutes nothing; the counter-model is the structure **with** \( \ell(x_0) = 2 \).

::: {.warning}
A "counter-model" that falsifies a premise refutes nothing. For \( \forall y\, \exists x\, R(x, y) \vdash \exists x\, \forall y\, R(x, y) \), the structure \( (\nN, <) \), with \( R(x, y) \) read as "\( x < y \)", makes the conclusion false, since no natural number is below every natural number; but it also makes the premise false, since nothing in \( \nN \) is below \( y = 0 \). It is not a counter-model, and it proves nothing about the sequent. As with rows in Chapter 4, check the premises **first**.
:::

**A model of a list of sentences.** Counter-models are one use of structures; describing a whole kind of object is another. Consider the three sentences
\[
\begin{aligned}
&\forall x\, \neg(x < x), \\
&\forall x\, \forall y\, \forall z\, \bigl( (x < y \wedge y < z) \to x < z \bigr), \\
&\forall x\, \exists y\, (x < y),
\end{aligned}
\]
which say that \( < \) is a **strict order** (never \( x < x \); \( x < y \) and \( y < z \) give \( x < z \)) **with no largest element**. The structure \( (\nN, <) \) is a model of all three: no number is less than itself, the order is transitive, and \( d + 1 > d \) is a witness for the third sentence. It is the one the sentences were written with in mind, but not the only one: in \( (\nZ, <) \) and \( (\nQ, <) \) all three are true, by the same checks.

::: {.second-reading title="Finite and infinite models"}
Finite counter-models are convenient because every clause can be checked by listing. They are not always available: Exercise C1 below gives a sentence that is true in every finite structure and false in an infinite one, and Exercise C2 a sentence with only infinite models.

These models differ in ways the three sentences cannot see: \( \nZ \) has no least element, and \( \nQ \) has a third element between any two. And the one-element structure \( D = \{ a \} \) is not a model of the three sentences: if \( (a, a) \in <^{\fM} \) the first sentence fails, and if not, the third fails at \( d = a \). Exercise C2 shows that no **finite** structure is a model of them.
:::

::: {.check}
Give a counter-model to \( \forall x\, P(x) \to \forall x\, Q(x) \models \forall x\, (P(x) \to Q(x)) \). (Think about what makes an implication with a universal hypothesis true cheaply.)
:::

::: {.solution}
Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \emptyset \). The premise is an implication whose hypothesis \( \forall x\, P(x) \) is false (it fails at \( b \)), so by (S5) the premise is true. The conclusion fails at \( d = a \): \( a \in P^{\fM} \) and \( a \notin Q^{\fM} \), so \( P(x) \to Q(x) \) is not satisfied under \( \ell[x \mapsto a] \). (Any structure with \( P^{\fM} \ne D \) and some element in \( P^{\fM} \) but not in \( Q^{\fM} \) works.)
:::

## Finding a counter-model

A counter-model is a structure with an assignment under which every member of the **counterexample set** \( \Gamma, \neg\varphi \) (@def-counterexample-set) is true. Section 4.6 searched for a row; here is the search for a structure, the named move **search for a counter-model**.

1. Write the counterexample set, and push each \( \neg \) inward (Section 6.2), so that every demand is visible as a \( \forall \) or an \( \exists \).
2. Meet the **existential demands first**: each \( \exists x\, \psi \) asks for an element; try one already present, and add a new one only if every present one clashes.
3. Then impose each **universal constraint** on every element so far, deciding the atomic facts it forces.
4. **Add only forced elements.** If a constraint creates a new existential demand, return to step 2.
5. If every attempt at size \( n \) clashes, try size \( n + 1 \); if each new element forces another, look for a familiar infinite structure (\( \nN \), \( \nZ \), \( \nQ \)) with that pattern.
6. **Check**: premises first (the warning above), then the conclusion, clause by clause.

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc start] (s) {the counterexample set $\Gamma, \neg\varphi$,\\$\neg$ pushed inward};
  \node[fc step, below=of s] (w) {meet each $\exists$ demand:\\reuse an element, else add one};
  \node[fc step, below=of w] (u) {impose each $\forall$ constraint\\on every element so far};
  \node[fc test, below=of u] (t) {a clash, or a\\new $\exists$ demand?};
  \node[fc start, right=of t] (d) {neither: check the premises,\\then the conclusion};
  \node[fc step, below=of t] (x) {a clash: one element more,\\or try $\nN$, $\nZ$, $\nQ$};
  \coordinate (r) at ($(d.east)+(0.4,0)$);
  \draw[fc arrow] (s) -- (w);
  \draw[fc arrow] (w) -- (u);
  \draw[fc arrow] (u) -- (t);
  \draw[fc arrow] (t) -- node[above, font=\scriptsize] {neither} (d);
  \draw[fc arrow] (t.west) -- ++(-0.6,0) |- node[pos=0.25, left, font=\scriptsize] {new demand} (w.west);
  \draw[fc arrow] (t) -- node[right, font=\scriptsize] {clash} (x);
  \draw[fc arrow] (x.east) -- (x.east -| r) |- (w.east);
\end{tikzpicture}
\end{center}
```

*The search for a counter-model. The procedure need not stop: Exercise C1 below gives a claim whose counter-models are all infinite, and Exercise C2 a sentence whose models are all infinite.*

::: {#exm-counter-model-procedure}
[A Counter-model, Found by the Procedure]

Show that
\[
\forall x\, \bigl( P(x) \to \exists y\, R(x, y) \bigr), \ \exists x\, P(x) \not\models \exists x\, \exists y\, \bigl( R(x, y) \wedge P(y) \bigr) .
\]
:::

::: {.solution}
*Step 1.* The counterexample set, with the negated conclusion pushed inward:
\[
\forall x\, \bigl( P(x) \to \exists y\, R(x, y) \bigr), \quad \exists x\, P(x), \quad \forall x\, \forall y\, \bigl( R(x, y) \to \neg P(y) \bigr) .
\]

*Step 2.* The demand \( \exists x\, P(x) \) asks for an element: call it \( a \), with \( P(a) \).

*Step 3.* The first member, at \( a \), now demands some \( y \) with \( R(a, y) \).

*Step 2 again.* Try \( y = a \), already present: then the third member, at \( x = a \), \( y = a \), forces \( \neg P(a) \), a clash. So add \( b \), with \( R(a, b) \), and, by the third member, \( \neg P(b) \).

*Step 3 again.* The constraints at \( b \): the first member at \( b \) demands nothing, since \( P(b) \) is false; the third member holds for every pair, since the only related pair is \( (a, b) \) and \( b \) lacks \( P \). No new demand: stop adding.

*Step 6.* Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( R^{\fM} = \{ (a, b) \} \). The first premise holds at \( a \), with the witness \( b \), and at \( b \), whose hypothesis is false. The second holds at \( a \). The conclusion fails: its only candidate pair \( (a, b) \) has \( b \notin P^{\fM} \).

In numbers: on \( \nN \), read \( P(x) \) as "\( x \) is even" and \( R(x, y) \) as "\( y = 2x + 1 \)". Every even number \( x \) has the number \( 2x + 1 \) related to it, some number is even, and every number \( 2x + 1 \) is odd, so no pair \( (x, y) \) has \( R(x, y) \) with \( y \) even.
:::

::: {.check}
In the example, why was \( y = a \) tried before adding \( b \)?
:::

::: {.solution}
Step 2: a demand is met by an element already present when possible, since every new element brings new constraints. Here \( a \) clashed, so \( b \) was forced.
:::

## Small domains, by expansion

Over a domain with few elements, say \( D = \{ a, b \} \), the clauses can be unwound to the end. By (S6), \( \fM, \ell \models \forall x\, \varphi \) exactly when \( \varphi \) is satisfied under \( \ell[x \mapsto a] \) **and** under \( \ell[x \mapsto b] \); by (S7), \( \fM, \ell \models \exists x\, \varphi \) exactly when \( \varphi \) is satisfied under \( \ell[x \mapsto a] \) **or** under \( \ell[x \mapsto b] \); (S4) and (S5) treat the connectives as before; and at the bottom each atomic formula is decided by (S1) as a fact about elements, such as "the pair \( (a, b) \) is in \( R^{\fM} \)".

The **expansion** is the record of that check: \( \forall x \) is written as a long \( \wedge \) over the elements and \( \exists x \) as a long \( \vee \), the long \( \wedge \) and \( \vee \) of Section 5.1, and \( R(a, b) \) is written for the fact \( (a, b) \in R^{\fM} \). Here \( a \) and \( b \) are the elements themselves, not new constants, and no formula \( \varphi[a/x] \) is formed: the expansion is notation for the finite table of (S6) and (S7) cases, so it is true exactly when the sentence is, by (S6), (S7) and (S1) alone. After the expansion only facts like \( R(a, b) \) remain, each true or false, and the search for a counter-model of that size is a search for a row (Section 4.6).

::: {#exm-small-domains}
[Size One Fails, Size Two Works]

Find the least size of a counter-model to
\[
\forall x\, \exists y\, R(x, y), \ \forall x\, \forall y\, \bigl( R(x, y) \to R(y, x) \bigr) \models \exists x\, R(x, x) .
\]
:::

::: {.solution}
*Size 1*, \( D = \{ a \} \). The first premise expands to \( R(a, a) \), which is also the conclusion's expansion. Whenever the first premise is true, so is the conclusion: no counter-model.

*Size 2*, \( D = \{ a, b \} \). The conclusion is false exactly when \( \neg R(a, a) \wedge \neg R(b, b) \). The first premise expands to
\[
\bigl( R(a, a) \vee R(a, b) \bigr) \wedge \bigl( R(b, a) \vee R(b, b) \bigr) ,
\]
which then forces \( R(a, b) \) and \( R(b, a) \). The second premise expands to four implications, \( R(a, a) \to R(a, a) \), \( R(a, b) \to R(b, a) \), \( R(b, a) \to R(a, b) \), \( R(b, b) \to R(b, b) \), all true with \( R^{\fM} = \{ (a, b), (b, a) \} \).

So the least size is \( 2 \): two elements, each related to the other and neither to itself. In numbers: on \( \{ 0, 1 \} \), read \( R(x, y) \) as \( x \ne y \).
:::

::: {.remark}
If a claim uses only one-place predicate symbols, \( k \) of them, and no constants, function symbols or \( = \), and it has a counter-model at all, then it has one with at most \( 2^k \) elements: merge any two elements that have the same predicates. This book does not prove it. Once a two-place predicate symbol is allowed, no such bound exists: by Exercise C2 below, the claim \( \models \neg\tau \), in which only the two-place symbol \( < \) occurs, has counter-models (the models of \( \tau \), such as \( (\nZ, <) \)), and every one of them is infinite. A function symbol with \( = \) does the same: the claim \( \models \sigma \) of Exercise C1 has no finite counter-model at all.
:::

::: {.check}
Expand \( \exists x\, \forall y\, R(x, y) \) over \( \{ a, b \} \).
:::

::: {.solution}
\( \bigl( R(a, a) \wedge R(a, b) \bigr) \vee \bigl( R(b, a) \wedge R(b, b) \bigr) \): the outer \( \exists x \) becomes the \( \vee \), and the inner \( \forall y \) the \( \wedge \) inside each disjunct.
:::

## Each side condition, broken

Chapter 5 introduced each side condition with a step that breaks it and a reading in which that step leads from truth to falsehood; here they are together, each reading now a counter-model.

| Side condition | WRONG (breaks it) | RIGHT (keeps it) | Counter-model to the WRONG sequent |
|---|---|---|---|
| \( \rulename{\forall E} \): \( t \) free for \( x \) (5.3) | from \( \forall x\, \exists y\, (y \ne x) \), \( \exists y\, (y \ne y) \) | from the renamed premise \( \forall x\, \exists z\, (z \ne x) \), \( \exists z\, (z \ne y) \) | \( D = \{ 0, 1 \} \): the premise holds; \( \exists y\, (y \ne y) \) never does |
| \( \rulename{\forall I} \): flag in no premise (5.4) | \( P(x_0) \vdash \forall x\, P(x) \) | \( P(x_0) \vdash \exists x\, P(x) \), by \( \rulename{\exists I} \) | \( \nZ \), \( P \) "even", \( \ell(x_0) = 2 \) |
| \( \rulename{\forall I} \): flag in no open assumption (5.4) | \( \vdash x_0 > 0 \to \forall x\, (x > 0) \) | \( \vdash \forall x\, (x > 0 \to x + 1 > 0) \), the boxes nested the other way | \( \nZ \), \( \ell(x_0) = 1 \) |
| \( \rulename{\forall I} \): flag not in the conclusion (5.4; 5.5, @exr-existential-introduction-c1) | from \( \forall x\, (x \le x) \), a box flagged \( y_0 \) ending in \( y_0 \le y_0 \) gives \( \forall x\, (x \le y_0) \), then \( \exists y\, \forall x\, (x \le y) \) by \( \rulename{\exists I} \) | from the same box, \( \forall y\, (y \le y) \) | \( \nN \) with \( \le \): the premise holds, and no number is at least every number (\( y + 1 \) exceeds \( y \)) |
| \( \rulename{\exists I} \): \( t \) free for \( x \) (5.5) | from \( \forall y\, R(y, y) \), \( \exists x\, \forall y\, R(x, y) \) | from the same line, \( \exists x\, R(x, x) \) (\( \rulename{\forall E} \) at \( x_0 \), then \( \rulename{\exists I} \)) | \( \nZ \), \( R \) as \( \le \): no least integer |
| \( \rulename{\exists E} \): \( x_0 \) not in \( \chi \) (5.6) | \( \exists x\, (x > 5) \vdash \forall x\, (x > 5) \), through an \( \rulename{\exists E} \) line that keeps \( x_0 \) | \( \exists x\, (x > 5) \vdash \exists x\, (x > 6) \) | \( \nN \): the premise holds at \( 6 \), the conclusion fails at \( 0 \) |
| \( \rulename{\exists E} \): \( x_0 \) in no premise or open assumption (5.6) | \( \exists x\, P(x), \neg P(x_0) \vdash \bot \) | \( \exists x\, P(x), \forall x\, \neg P(x) \vdash \bot \) | \( D = \{ 1, 2 \} \), \( P^{\fM} = \{ 2 \} \), \( \ell(x_0) = 1 \) |
| \( \rulename{\exists E} \): \( x_0 \) not in \( \exists x\, \varphi \) (5.6) | \( \forall y\, \exists x\, R(x, y) \vdash \exists z\, R(z, z) \) | \( \forall y\, \exists x\, R(x, y) \vdash \exists z\, \exists x\, R(x, z) \) | three dots, \( a \to b \to c \to a \) |
| \( \rulename{{=}E} \): terms free for \( x \) (5.7) | \( a = y, \exists y\, (y < a) \vdash \exists y\, (y < y) \) | \( a = y, \exists z\, (z < a) \vdash \exists z\, (z < y) \), after renaming the premise | \( \nZ \), \( a \) and \( y \) both naming \( 0 \) |

Each counter-model makes the WRONG sequent's premises true and its conclusion false, so, by the statement in the next subsection, no correct derivation reaches that conclusion: the side condition is not a fussy extra, it is what keeps the rule from leading from truth to falsehood. Each RIGHT step is legal, and its sequent has no counter-model, with one proviso. The RIGHT derivations of the rows "flag in no open assumption" and "\( x_0 \) not in \( \chi \)", taken from Sections 5.4 and 5.6, use an "arith" line, which records an arithmetic fact and is not a rule. Those two sequents hold in every structure in which that fact (\( \forall x\, (x > 0 \to x + 1 > 0) \), or \( \forall x\, (x > 5 \to x + 1 > 6) \)) is true, such as \( \nN \) or \( \nZ \) with the usual meanings, and not in every structure: read \( + \) as subtraction on \( \nZ \), and \( \forall x\, (x > 0 \to x + 1 > 0) \) fails at \( 1 \). Section 7.3 (optional) shows the same thing from the other side: each side condition is used in exactly one case of the soundness proof.

## From counter-models to non-derivability {#from-counter-models-to-non-derivability}

A counter-model shows \( \Gamma \not\models \varphi \). The stalled searches asked something else: whether \( \Gamma \vdash \varphi \). The bridge is the same as in Chapter 4, where @thm-soundness turned a refuting row into a proof that no derivation exists (@cor-refuting-row). For predicate logic it reads:

*Soundness for predicate logic.* If \( \Gamma \vdash \varphi \) with the rules of Chapters 1 and 2 and the quantifier and equality rules of Sections 5.3 to 5.7, then \( \Gamma \models \varphi \) in the sense of @def-first-order-entailment. Consequently, a counter-model to \( \Gamma \models \varphi \) shows \( \Gamma \nvdash \varphi \).

This statement is **not proved in this section**. Its proof extends Chapter 4's to the new rules, and it is the subject of Section 7.3, which is optional. The proof is where each side condition of the quantifier rules is used: the fresh-name conditions of \( \rulename{\forall I} \) and \( \rulename{\exists E} \), and "free for" in \( \rulename{\forall E} \), \( \rulename{\exists I} \), and \( \rulename{{=}E} \). A reader who skips Section 7.3 may take the statement on trust, as the rest of the book does; a reader who reads it will see why the side conditions are exactly as strict as they are.

With the statement, the examples above and the three pictures at the start of this section become non-derivability results. \( \forall y\, \exists x\, R(x, y) \nvdash \exists x\, \forall y\, R(x, y) \): the converse search of @prp-exists-forall-swap had to stall, and the two lines where it stalled, the blocked \( \rulename{\forall I} \) and the blocked close of the \( \rulename{\exists E} \) box, are not a lack of cleverness. Likewise the converse of @prp-exists-and, the converse of the \( \forall \)/\( \vee \) law, \( \exists x\, P(x) \vdash P(c) \), and \( P(x_0) \vdash \forall x\, P(x) \) have no derivations. And the same reasoning is the semantic side of Section 6.4: there, @exm-square-not-uniform showed that \( x^2 \) on \( \nR \) is continuous and not uniformly continuous, so the arithmetic structure on \( \nR \), with \( f \) read as squaring, is a counter-model to "continuous entails uniformly continuous".

::: {.check}
Which row of the side-condition table does picture (C) belong to, if \( \exists x\, P(x) \vdash P(c) \) is "derived" by an \( \rulename{\exists E} \) box with witness \( c \)?
:::

::: {.solution}
None exactly: \( c \) is a constant, not a variable, so it cannot be the name of an \( \rulename{\exists E} \) box at all. With a variable \( x_0 \) in its place, the box would end in \( P(x_0) \), and the derivation would break the row "\( x_0 \) not in \( \chi \)". Either way, picture (C) shows that no derivation exists.
:::

::: {.warning}
A counter-model proves **non**-derivability; it never proves derivability, and a structure in which a sentence is true says nothing about whether the sentence is derivable. \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \), yet it is not derivable: it is false in \( (\{ 1, 2, 3 \}, <) \). To show \( \Gamma \vdash \varphi \), write a derivation.
:::

**What this certifies.** Chapters 5 and 6 said, at every stall, that a counter-reading would settle the question and that Section 7.2 would explain why. Each of those readings is a structure, and the statement above turns each into a theorem:

- Section 5.1: the swapped pair of @exm-quantifier-order-sum, read over \( \nR \): \( \forall x\, \exists y\, (x + y = 0) \) is true and \( \exists y\, \forall x\, (x + y = 0) \) false, so the first does not derive the second (5.1's other refutation is a row, which @cor-refuting-row already settled in Chapter 4).
- Section 5.3: the three tiny worlds of the common errors (capture, a buried quantifier, some occurrences only), named in the paragraph on [counter-readings](#counter-readings), and the breaks of @exr-universal-elimination-b5.
- Section 5.4: \( P(x_0) \vdash \forall x\, P(x) \) and the open-assumption error; the stalled converse of @exr-universal-introduction-b2, \( \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \nvdash \forall x\, (P(x) \to Q(x)) \), by the reading over \( \nN \) with \( P \) "even" and \( Q \) "odd" (the premise holds because its hypothesis \( \forall x\, \neg Q(x) \) fails at \( 1 \); the conclusion fails at \( 0 \), even and not odd; Exercise B3 asks for a counter-model with exactly two elements); and the breaks (b), (d), (f) of @exr-universal-introduction-b5 (Section 7.4 makes (d) and (f) models).
- Section 5.5: \( \exists x\, P(x) \vdash P(c) \) (picture (C)), the capture in \( \rulename{\exists I} \) (no least integer), \( \forall x\, (x \le x) \nvdash \exists y\, \forall x\, (x \le y) \) (@exr-existential-introduction-c1), and the breaks of @exr-existential-introduction-b4.
- Section 5.6: the three counter-worlds of the \( \rulename{\exists E} \) clauses, the converse of @prp-exists-and (picture (A)), the swap (picture (B), @exm-counter-model-swap), and the breaks of @exr-existential-elimination-b4.
- Section 5.7: the capture in \( \rulename{{=}E} \), the two-dot counter-reading to the converse of @exm-extensionality-logical-half (the subsection "Extensionality" below), and the breaks of @exr-equality-and-uniqueness-b5.
- Section 5.8: the one-element domain with \( 0 \in 0 \), in which any two sets without elements are equal and no set without elements exists (@exr-counting-and-descriptions-b4 (b)).
- Section 6.1: the readings of the translation table, each separating the wrong formula from the right one. In rows (c)–(e) the right formula is true and the wrong one false, so the wrong one is not derivable from the right one; in rows (a) and (b) it is the other way round, so the right one is not derivable from the wrong one. Also the converse in @exr-translation-c3 (b).
- Section 6.2: the converses of (c) and (d) of @prp-quantifier-distribution (6.2 read them over \( \nZ \); picture (A) and the first Quick check draw them), and the breaks of @exr-quantifier-laws-b4.
- Section 6.3: every break of @exr-first-order-search-b1 and @exr-first-order-search-c2 (a), and the move "test the subgoal by a counter-reading".
- Section 6.4: continuity does not give uniform continuity (@exm-square-not-uniform, as above), and the break in @exr-uniform-continuity-rule-by-rule-c3 (b).

None of them was used as a reason before now; each is now a proof that no derivation exists.

## Three classes of sentences

Fix the symbols of arithmetic: the constant \( 0 \), the one-place function symbol \( S \), the two-place function symbols \( + \) and \( \cdot \), and the two-place predicate symbol \( < \). A sentence in these symbols is

- an **instance of a tautology** if its propositional skeleton (@def-propositional-skeleton) is a tautology (@def-tautology);
- **valid** if it is true in every structure for these symbols (\( \models \sigma \));
- **true in \( \nN \)** if it is true in the structure \( (\nN; 0, S, +, \cdot, <) \), with \( S \) the successor, \( S(n) = n + 1 \).

Each class lies inside the next, and neither inclusion is an equality.

::: {#exm-three-classes}
[Three Classes of Sentences]

Place each sentence in the narrowest class it belongs to.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, (x < S(x)) \vee \neg\forall x\, (x < S(x)) \).
2. \( \forall x\, (x = x) \).
3. \( \forall x\, \neg(S(x) = 0) \).
4. \( \exists x\, (S(x) = 0) \).
:::
:::

::: {.solution}
*(a)* An instance of a tautology: its skeleton is \( p \vee \neg p \).

*(b)* Valid, by (S2) and (S6): every element equals itself. Not an instance of a tautology: its skeleton is one letter, \( p \).

*(c)* True in \( \nN \): no successor is \( 0 \). Not valid: in the structure with \( D = \{ a \} \), \( 0^{\fM} = a \), \( S^{\fM}(a) = a \) (and \( + \), \( \cdot \), \( < \) read in any way), \( S(0) = 0 \) holds.

*(d)* False in \( \nN \), so in none of the three classes.
:::

Why the inclusions hold: a valid sentence is true in \( \nN \) because \( \nN \) is one structure; an instance of a tautology whose different prime formulas have different letters (every sentence classified here) is valid because (S3)–(S5) compute a formula's truth from the truth of the prime formulas its skeleton's letters stand for, exactly as a truth table does (the first fold below gives the argument); that every instance is valid, including those where renamed prime formulas share a letter, is shown in the optional Section 7.3. The classes meet derivations as follows: an instance of a tautology is derivable (by \( \rulename{TAUT} \), @prp-taut-skeleton); a valid sentence need not be derivable by \( \rulename{TAUT} \) alone; and a sentence true in \( \nN \) but not valid is never derivable, by the statement of this section.

```{=latex}
\begin{center}
\begin{tikzpicture}
  \draw (-5,-2.6) rectangle (5,2.6);
  \node[anchor=north west] at (-5,2.6) {sentences of $0, S, +, \cdot, <$};
  \draw (0.6,0) ellipse (4 and 2.2);
  \draw (1.2,0) ellipse (2.8 and 1.6);
  \draw (1.8,0) ellipse (1.4 and 0.9);
  \node at (0.6,1.9) {true in $\nN$};
  \node at (-0.2,1.05) {valid};
  \node[align=center, font=\footnotesize] at (1.8,0.35) {instances of\\tautologies};
  \fill (1.8,-0.45) circle (1.5pt) node[right, font=\footnotesize] {(1)};
  \fill (-0.5,0.15) circle (1.5pt) node[below, font=\footnotesize] {$\forall x\,(x = x)$};
  \fill (-0.8,-1.85) circle (1.5pt) node[right, font=\footnotesize] {$\forall x\,\neg(S(x) = 0)$};
  \fill (-4.5,-2.1) circle (1.5pt) node[right, font=\footnotesize] {$\exists x\,(S(x) = 0)$};
\end{tikzpicture}
\end{center}
```

*The three classes, each inside the next. The point (1) is \( \forall x\, (x < S(x)) \vee \neg\forall x\, (x < S(x)) \); the other three points are labeled with their sentences.*

::: {.check}
Classify \( \forall x\, (x < S(x)) \to (0 < S(0)) \).
:::

::: {.solution}
Valid: if \( \forall x\, (x < S(x)) \) holds in a structure, then by (S6) at \( d = 0^{\fM} \) so does \( 0 < S(0) \), and (S5) makes the implication true; if it fails, (S5) makes the implication true anyway. Not an instance of a tautology: its skeleton is \( p \to q \).
:::

::: {.second-reading title="Why an instance of a tautology is valid"}
Let \( \sigma \) be a sentence whose skeleton is a tautology and in which different prime formulas get different letters, and fix a structure \( \fM \) and an assignment \( \ell \). Give each letter of the skeleton the truth value, under \( \fM \) and \( \ell \), of the prime formula it stands for. This is one row of the skeleton's truth table. By induction on the skeleton, the skeleton's value in that row is \( \mathrm{T} \) exactly when \( \fM, \ell \models \sigma \): at a letter this is how the row was chosen, and at \( \neg \), \( \wedge \), \( \vee \), \( \to \), \( \leftrightarrow \) the clauses (S3)–(S5) compute exactly as the clauses (V1)–(V6) of @def-truth-value do. A tautology has value \( \mathrm{T} \) in every row, so \( \sigma \) is satisfied in every structure under every assignment: it is valid.

When two different prime formulas share a letter (@def-propositional-skeleton gives one letter to prime formulas that differ only by renaming bound variables), the same argument works, since the row above is well chosen only if the two formulas have the same truth value. They do, because renaming keeps meaning; the optional Section 7.3 proves this, and nothing in this section relies on it, since every sentence this section classifies gives different prime formulas different letters. The argument is about meaning and does not go through soundness.
:::

::: {.second-reading title="A failed search proves nothing here, either"}
A stalled derivation search proves nothing, as Chapters 5 and 6 said at every stall. A stalled counter-model search proves nothing either: the counter-models may all be infinite (Exercise C1), or simply larger than the sizes tried. Chapter 4's truth tables decided every propositional claim in finitely many rows (@prp-search-decides). For predicate logic, no mechanical procedure decides derivability: this is a theorem of Church and of Turing (1936), stated here without proof, and again in the optional Section 7.6. So the two searches are run side by side, and the reader's judgment chooses which to push.
:::

## Extensionality: an axiom, not a law of logic

Write \( \in \) for a two-place predicate symbol. Section 5.7 derived that equal sets have the same members,
\[
\vdash \forall x\, \forall y\, \bigl( x = y \to \forall z\, (z \in x \leftrightarrow z \in y) \bigr)
\]
(@exm-extensionality-logical-half), and read its converse, **extensionality**,
\[
\forall x\, \forall y\, \bigl( \forall z\, (z \in x \leftrightarrow z \in y) \to x = y \bigr) ,
\]
in two dots with \( \in \) holding nowhere. That reading is a structure: \( D = \{ a, b \} \), \( \in^{\fM} = \emptyset \). Every \( z \) is a member of neither \( a \) nor \( b \), so \( a \) and \( b \) have the same members, and \( a \ne b \). By the statement of this section, extensionality is not derivable.

So extensionality is a fact about sets, not about logic: a theory of sets must take it as an axiom (Section 7.4 says what that means). The counter-model is not a strange set theory; it is a structure in which "\( \in \)" is read as a relation that holds nowhere.

::: {.remark}
[Looking ahead]

*Axiomatic Set Theory* takes extensionality as the first axiom of its set theory, (Z1), for exactly this reason: no derivation could supply it.
:::

## Exercises

### A. Check your understanding

::: {#exr-counter-models-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a counter-model to \( \Gamma \models \varphi \).
2. State the soundness statement of this section, and say where it is proved.
3. True or false, with a reason: if no structure with at most five elements is a counter-model to \( \Gamma \models \varphi \), then \( \Gamma \vdash \varphi \).
4. True or false, with a reason: a structure in which the sentence \( \sigma \) is true shows \( \vdash \sigma \).
5. Which step of the search for a counter-model comes first, and which kind of demand is met first?
6. Give, in one sentence, the reason that an instance of a tautology whose different prime formulas have different letters, such as (a) of @exm-three-classes, is valid.
:::
:::

::: {.solution}
*(a)* A structure \( \fM \) and an assignment \( \ell \) with \( \fM, \ell \models \Gamma \) and \( \fM, \ell \not\models \varphi \).

*(b)* If \( \Gamma \vdash \varphi \) with the rules of Chapters 1, 2 and 5, then \( \Gamma \models \varphi \); so a counter-model shows \( \Gamma \nvdash \varphi \). It is proved in the optional Section 7.3.

*(c)* False. The sentence \( \sigma \) of @exr-models-c1 has no finite counter-model at all, and it is not derivable.

*(d)* False: a structure in which \( \sigma \) is true says nothing about derivability (the warning after the soundness statement). \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \) and not derivable.

*(e)* Writing the counterexample set with \( \neg \) pushed inward comes first; existential demands are met before universal constraints are imposed.

*(f)* The clauses (S3)–(S5) compute truth in a structure from the truth of the prime formulas behind the skeleton's letters exactly as a row does, and a tautology is true in every row.
:::

::: {#exr-counter-models-a2}
[A2: Drill]

Each part takes a line or two. (a)–(c) give or judge a counter-model; (d) judges two infinite ones; (e) and (f) complete a structure; (g) and (h) expand over \( \{ a, b \} \); (i)–(k) classify a sentence in the symbols \( 0 \), \( S \), \( + \), \( \cdot \), \( < \) as an instance of a tautology, valid but not an instance of a tautology, or true in \( \nN \) but not valid; (l) builds a counter-model.

::: {.enumerate options="label=(\alph*)"}
1. Give a counter-model to \( \exists x\, \neg P(x) \models \neg\exists x\, P(x) \).
2. Is \( D = \{ a \} \), \( P^{\fM} = \{ a \} \) a counter-model to \( \forall x\, P(x) \models \exists x\, P(x) \)?
3. Give a counter-model to \( \forall x\, (P(x) \to Q(x)) \models \forall x\, (Q(x) \to P(x)) \).
4. Is \( \nZ \), with \( R(x, y) \) read as \( x < y \), a counter-model to \( \forall y\, \exists x\, R(x, y) \models \exists x\, \forall y\, R(x, y) \)? And \( \nN \), with \( R(x, y) \) read as \( x > y \)?
5. \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \). Choose \( Q^{\fM} \) so that the structure is a counter-model to \( \forall x\, (P(x) \vee Q(x)) \models \forall x\, Q(x) \).
6. \( D = \{ a, b \} \), and \( (a, b) \in R^{\fM} \). Add pairs to \( R^{\fM} \) so that the structure is a counter-model to \( \forall x\, \exists y\, R(x, y) \models \exists y\, \forall x\, R(x, y) \).
7. Expand \( \forall x\, \exists y\, R(y, x) \) over \( \{ a, b \} \).
8. Expand \( \exists x\, \bigl( P(x) \wedge \forall y\, R(x, y) \bigr) \) over \( \{ a, b \} \).
9. \( \forall x\, (x < x) \to \forall x\, (x < x) \).
10. \( \forall x\, (0 + x = x) \to (0 + 0 = 0) \).
11. \( \forall x\, \forall y\, (x + y = y + x) \).
12. Give a counter-model to \( \forall x\, (P(x) \to Q(x)), \ \exists x\, Q(x) \models \exists x\, P(x) \).
:::
:::

::: {.solution}
(a) \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \): \( \neg P \) holds at \( b \), and \( \exists x\, P(x) \) holds at \( a \), so \( \neg\exists x\, P(x) \) fails.

(b) No: both sentences are true there. And no structure is a counter-model, since domains are non-empty: if every element has \( P \), some element does.

(c) \( D = \{ a \} \), \( P^{\fM} = \emptyset \), \( Q^{\fM} = \{ a \} \): the premise holds since no element has \( P \); the conclusion fails at \( a \).

(d) Yes, both. In \( \nZ \) each \( y \) has \( y - 1 \) below it, and nothing is below everything (nothing is below itself). In \( \nN \) each \( y \) has \( y + 1 \) above it, and nothing is above everything (nothing is above itself).

(e) \( Q^{\fM} = \{ b \} \): it must contain \( b \), which lacks \( P \), and omit \( a \), to break the conclusion.

(f) Add \( (b, a) \) and nothing else: \( b \) needs an arrow out, \( (b, b) \) would give \( b \) an arrow from every element, and \( (a, a) \) together with \( (b, a) \) would do the same for \( a \).

(g) \( \bigl( R(a, a) \vee R(b, a) \bigr) \wedge \bigl( R(a, b) \vee R(b, b) \bigr) \).

(h) \( \bigl( P(a) \wedge R(a, a) \wedge R(a, b) \bigr) \vee \bigl( P(b) \wedge R(b, a) \wedge R(b, b) \bigr) \).

(i) An instance of a tautology: its skeleton is \( p \to p \).

(j) Valid, by (S6) at \( d = 0^{\fM} \) and (S5); not an instance of a tautology, since its skeleton is \( p \to q \).

(k) True in \( \nN \), not valid: on \( D = \{ a, b \} \), read \( x + y \) as "\( x \)" (and the other symbols in any way); then \( a + b = a \) and \( b + a = b \).

(l) \( D = \{ a \} \), \( P^{\fM} = \emptyset \), \( Q^{\fM} = \{ a \} \): the first premise holds since no element has \( P \), the second at \( a \), and the conclusion fails.
:::

### B. Practice

::: {#exr-models-b1}
[B1: Three counter-models, used later]

Give a counter-model for each of the following, and check each premise and the conclusion against @def-satisfaction.

::: {.enumerate options="label=(\roman*)"}
1. \( \exists x\, P(x) \not\models \forall x\, P(x) \).
2. \( \forall x\, (P(x) \to Q(x)) \not\models \exists x\, P(x) \to \forall x\, Q(x) \).
3. \( \not\models \exists x\, P(x) \to P(x) \). (Here \( x \) is free in the last \( P(x) \); the assignment is part of the answer.)
:::
:::

::: {.solution}
*(i)* Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \). The premise holds by (S7) with \( d = a \). The conclusion fails by (S6) at \( d = b \), since \( b \notin P^{\fM} \).

*(ii)* Take \( D = \{ a, b \} \), \( P^{\fM} = Q^{\fM} = \{ a \} \). Premise: at \( d = a \), \( P(x) \) and \( Q(x) \) are both satisfied, so \( P(x) \to Q(x) \) is; at \( d = b \), \( P(x) \) is not satisfied, so \( P(x) \to Q(x) \) is, by (S5). Hence the premise holds by (S6). Conclusion: \( \exists x\, P(x) \) holds (\( d = a \)) and \( \forall x\, Q(x) \) fails (at \( d = b \)), so by (S5) the implication fails. In words: whatever has \( P \) has \( Q \), and something has \( P \); that does not make everything have \( Q \).

*(iii)* Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), and an assignment with \( \ell(x) = b \). The hypothesis \( \exists x\, P(x) \) holds by (S7) with \( d = a \); its \( x \) is bound, and the value \( \ell(x) \) is overwritten. The conclusion \( P(x) \) has \( x \) free, with value \( \ell(x) = b \notin P^{\fM} \), so it fails. By (S5) the implication fails under \( \ell \). Under an assignment with \( \ell(x) = a \) the implication holds; so the formula is satisfied under some assignments and not others, and a counter-model must name \( \ell \). Now take \( \varphi \) and \( \psi \) both to be \( P(x) \). The formula \( \forall x\, (P(x) \to P(x)) \) is satisfied in every structure under every assignment, since \( P(x) \to P(x) \) is satisfied at every \( d \) by (S5) and (S6). So this structure, with \( \ell \), is a counter-model to \( \forall x\, (P(x) \to P(x)) \models \exists x\, P(x) \to P(x) \), and by the soundness statement of this section that sequent is not derivable. This is why the passage law \( \forall x\, (\varphi \to \psi) \dashv\vdash \exists x\, \varphi \to \psi \) of @prp-quantifier-passage needs \( x \) not free in \( \psi \).
:::

::: {#exr-counter-models-b2}
[B2: Prove it or break it]

For each claim \( \Gamma \models \varphi \), either prove it by meaning (clause by clause or condensed) or give a counter-model, and state what follows about \( \Gamma \vdash \varphi \). For (a) and (c), if the claim holds, also give a derivation.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, (P(x) \to Q(x)), \ \forall x\, \neg Q(x) \models \forall x\, \neg P(x) \).
2. \( \forall x\, (P(x) \to Q(x)), \ \exists x\, \neg P(x) \models \exists x\, \neg Q(x) \).
3. \( \exists x\, \forall y\, R(x, y) \models \exists x\, R(x, x) \).
4. \( \forall x\, \exists y\, R(x, y) \models \forall x\, \exists y\, R(y, x) \).
5. \( \forall x\, \bigl( P(x) \to \exists y\, Q(y) \bigr) \models \exists x\, P(x) \to \exists y\, Q(y) \).
6. \( \exists x\, P(x) \to \forall y\, Q(y) \models \forall x\, (P(x) \to Q(x)) \).
7. \( \forall x\, (P(x) \vee Q(x)), \ \exists x\, \neg P(x) \models \forall x\, Q(x) \).
8. \( \forall x\, (P(x) \vee Q(x)), \ \forall x\, \neg P(x) \models \forall x\, Q(x) \).
:::
:::

::: {.solution}
*(a) Holds.* If some \( d \) were in \( P^{\fM} \), then \( d \in Q^{\fM} \) by the first premise, against the second; so no \( d \) is in \( P^{\fM} \). A derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, \neg Q(x)}
  \open[x_0]
  \open
  \hypo {3} {P(x_0)}
  \have {4} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {5} {Q(x_0)} \ie{4,3}
  \have {6} {\neg Q(x_0)} \Ae{2}
  \have {7} {\bot} \ne{5,6}
  \close
  \have {8} {\neg P(x_0)} \ni{3-7}
  \close
  \have {9} {\forall x\, \neg P(x)} \Ai{3-8}
\end{nd}$
\end{center}
```

So \( \Gamma \vdash \varphi \).

*(b) Fails.* \( D = \{ a \} \), \( P^{\fM} = \emptyset \), \( Q^{\fM} = \{ a \} \): the first premise holds since its hypothesis is false at \( a \), the second holds at \( a \), and the conclusion fails since \( a \in Q^{\fM} \). So \( \Gamma \nvdash \varphi \), by the soundness statement.

*(c) Holds.* The premise's witness \( d \) has \( (d, e) \in R^{\fM} \) for every \( e \), in particular for \( e = d \). A derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, \forall y\, R(x, y)}
  \open[x_0]
  \hypo {2} {\forall y\, R(x_0, y)}
  \have {3} {R(x_0, x_0)} \Ae{2}
  \have {4} {\exists x\, R(x, x)} \Ei{3}
  \close
  \have {5} {\exists x\, R(x, x)} \Ee{1,2-4}
\end{nd}$
\end{center}
```

*(d) Fails.* \( D = \{ a, b \} \), \( R^{\fM} = \{ (a, b), (b, b) \} \): each element has an arrow out, and \( a \) has none in. So \( \Gamma \nvdash \varphi \).

*(e) Holds.* If \( \exists x\, P(x) \) is true, with witness \( d \), the premise at \( d \) gives \( \exists y\, Q(y) \); if it is false, the conclusion is true by (S5).

*(f) Holds.* If \( d \in P^{\fM} \), then \( \exists x\, P(x) \) holds, so \( \forall y\, Q(y) \) holds by the premise, so \( d \in Q^{\fM} \).

*(g) Fails.* \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \): every element is in \( P^{\fM} \) or \( Q^{\fM} \), \( b \notin P^{\fM} \), and \( a \notin Q^{\fM} \). So \( \Gamma \nvdash \varphi \).

*(h) Holds.* Each \( d \) is in \( P^{\fM} \) or \( Q^{\fM} \), and not in \( P^{\fM} \); so it is in \( Q^{\fM} \).

A proof by meaning shows \( \Gamma \models \varphi \), not \( \Gamma \vdash \varphi \). The derivations of (a) and (c) show \( \vdash \); for (e), (f) and (h) the matching derivations exist but are not asked for (each is a short exercise with Chapter 5's rules). The pairs (a) and (b), and (g) and (h), are look-alikes; so are (c) and (d), with opposite prefixes: an \( \exists\forall \) premise gives a loop, while a \( \forall\exists \) premise does not even give every element an incoming arrow.

**Marking scheme.** (10 points)

- 8: 1 per part (a)–(h): the correct verdict with its justification, either a proof by meaning that covers every premise, or a counter-model with the premises checked true and the conclusion checked false. A bare verdict scores 0.
- 1: the two derivations of (a) and (c), checked rule by rule (both needed).
- 1: stating, at a failing claim, that the counter-model gives \( \Gamma \nvdash \varphi \) by the soundness statement.

Fatal errors (0 for that part): a "counter-model" that falsifies a premise; a proof by meaning offered as a derivation; a verdict given without a justification.
:::

::: {#exr-models-b3}
[B3: The converse from Section 5.4]

@exr-universal-introduction-b2 derived \( \forall x\, (P(x) \to Q(x)) \vdash \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \), and its search for the converse stalled; this section settled that converse above, in "What this certifies", with an infinite structure. Find a counter-model to
\[
\forall x\, \neg Q(x) \to \forall x\, \neg P(x) \models \forall x\, (P(x) \to Q(x))
\]
with exactly two elements, working backwards from the conclusion: say which element breaks the conclusion and how the premise is made true most cheaply.
:::

::: {.solution}
Work backwards. The conclusion fails when some \( d \) has \( d \in P^{\fM} \) and \( d \notin Q^{\fM} \). The premise is cheapest to make true through a false hypothesis: make \( \forall x\, \neg Q(x) \) false by putting some element in \( Q^{\fM} \). Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \).

Premise: \( \forall x\, \neg Q(x) \) fails at \( d = b \), since \( b \in Q^{\fM} \); so the implication holds by (S5). Conclusion: at \( d = a \), \( a \in P^{\fM} \) and \( a \notin Q^{\fM} \), so \( P(x) \to Q(x) \) fails under \( \ell[x \mapsto a] \), and (S6) fails. By the soundness statement of this section, the converse is not derivable, and the stalled search could not have succeeded.
:::

::: {#exr-counter-models-b4}
[B4: Each side condition earns its place]

Each derivation below breaks a side condition. For (a)–(c), name the line that breaks a side condition and the condition it breaks, give a counter-model to the sequent of its last line, and, where you can, repair the derivation so that it reaches a correct conclusion. For (d), say whether the conclusion is true (follows from the premise) and whether the derivation proves it.

*(a)*

```{=latex}
\begin{center}
% expect-invalid: line 3 generalizes over x_0 while the assumption P(x_0) on line 1 is open
$\begin{nd}
  \open[x_0]
  \open
  \hypo {1} {P(x_0)}
  \open[x_0]
  \have {2} {P(x_0)} \r{1}
  \close
  \have {3} {\forall x\, P(x)} \Ai{2-2}
  \close
  \have {4} {P(x_0) \to \forall x\, P(x)} \ii{1-3}
  \close
  \have {5} {\forall y\, (P(y) \to \forall x\, P(x))} \Ai{1-4}
\end{nd}$
\end{center}
```

*(b)*

```{=latex}
\begin{center}
% expect-invalid: y is not free for x in forall y (x = y)
$\begin{nd}
  \hypo {1} {\forall y\, (y = y)}
  \have {2} {\exists x\, \forall y\, (x = y)} \Ei{1}
\end{nd}$
\end{center}
```

*(c)*

```{=latex}
\begin{center}
% expect-invalid: the exists-E line 6 keeps its name x_0
$\begin{nd}
  \hypo {1} {\exists x\, P(x)}
  \hypo {2} {\forall x\, (P(x) \to Q(x))}
  \open[x_0]
  \hypo {3} {P(x_0)}
  \have {4} {P(x_0) \to Q(x_0)} \Ae{2}
  \have {5} {Q(x_0)} \ie{4,3}
  \close
  \have {6} {Q(x_0)} \Ee{1,3-5}
\end{nd}$
\end{center}
```

*(d)*

```{=latex}
\begin{center}
% expect-invalid: line 3 generalizes over x_0, which appears in the premise
$\begin{nd}
  \hypo {1} {P(x_0) \wedge \forall x\, P(x)}
  \open[x_0]
  \have {2} {P(x_0)} \ae{1}
  \close
  \have {3} {\forall x\, P(x)} \Ai{2-2}
\end{nd}$
\end{center}
```
:::

::: {.solution}
*(a)* Line 3: \( x_0 \) appears in the assumption on line 1, which is open at line 3. Line 5 is a legal \( \rulename{\forall I} \): no premise, no open assumption, and \( x_0 \) is not in the conclusion. (This is the same-name nesting of Section 5.4's fold "The same error, as a false sentence", read there over \( \nZ \) with \( x > 0 \); here \( P \) is left open.) Counter-model to \( \models \forall y\, (P(y) \to \forall x\, P(x)) \): \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \). At \( y = a \), \( P(a) \) holds and \( \forall x\, P(x) \) fails at \( b \). No derivation reaches this conclusion: the counter-model shows it. A repair to a correct conclusion drops the inner box and uses \( \rulename{\exists I} \) in place of the illegal \( \rulename{\forall I} \):

```{=latex}
\begin{center}
$\begin{nd}
  \open[x_0]
  \open
  \hypo {1} {P(x_0)}
  \have {2} {\exists x\, P(x)} \Ei{1}
  \close
  \have {3} {P(x_0) \to \exists x\, P(x)} \ii{1-2}
  \close
  \have {4} {\forall y\, (P(y) \to \exists x\, P(x))} \Ai{1-3}
\end{nd}$
\end{center}
```

This is the RIGHT entry of the second row of the side-condition table, generalized.

*(b)* Line 2: in \( \varphi = \forall y\, (x = y) \) the term \( y \) is not free for \( x \), since it would be captured by \( \forall y \). Counter-model: any domain with two elements; the premise holds, and no element equals both. Repairs: \( \exists x\, \forall y\, (y = y) \) by \( \rulename{\exists I} \) from line 1, with \( x \) not in \( \varphi \); or \( z = z \) by \( \rulename{\forall E} \) at \( z \), then \( \exists x\, (x = z) \) by \( \rulename{\exists I} \).

*(c)* Line 6: \( x_0 \) appears in \( \chi = Q(x_0) \). The last line has \( x_0 \) free, so the counter-model needs an assignment: \( D = \{ a, b \} \), \( P^{\fM} = Q^{\fM} = \{ a \} \), \( \ell(x_0) = b \). Both premises hold, and \( Q(x_0) \) fails. Repair: forget the witness before the box closes.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, P(x)}
  \hypo {2} {\forall x\, (P(x) \to Q(x))}
  \open[x_0]
  \hypo {3} {P(x_0)}
  \have {4} {P(x_0) \to Q(x_0)} \Ae{2}
  \have {5} {Q(x_0)} \ie{4,3}
  \have {6} {\exists y\, Q(y)} \Ei{5}
  \close
  \have {7} {\exists y\, Q(y)} \Ee{1,3-6}
\end{nd}$
\end{center}
```

*(d)* The conclusion is true: it follows from the premise, and is derived correctly in one line, \( \forall x\, P(x) \) by \( \rulename{\wedge E} \) from line 1; so the sequent has no counter-model. The derivation does not prove it: line 3 breaks "the flag appears in no premise", since \( x_0 \) is in line 1. The counterexample is to the **step**, not to the conclusion: the same step takes \( P(x_0) \) to \( \forall x\, P(x) \), and \( \nZ \), with \( P \) read as "even" and \( \ell(x_0) = 2 \), makes \( P(x_0) \) true and \( \forall x\, P(x) \) false (the second row of the side-condition table).

**Marking scheme.** (10 points)

- 6: (a)–(c), 1 each for the line with its condition, and 1 each for a checked counter-model.
- 1: the repairs of (a)–(c), and the remark that (a)'s original conclusion is unreachable.
- 3: (d): the conclusion judged true, with the one-line derivation (1); the illegal line and its condition named (1); a counter-model to the step pattern rather than to the conclusion (1).

Fatal errors (0 for the step): in (c), a counter-model with the assignment omitted, although the last line has a free variable; in (d), a claimed counter-model to the conclusion.
:::

### C. Going deeper

::: {#exr-models-c1}
[C1: True in every finite model, used later]

Let \( f \) be a one-place function symbol, and let \( \sigma \) be the sentence
\[
\forall x\, \forall y\, \bigl( f(x) = f(y) \to x = y \bigr) \to \forall y\, \exists x\, \bigl( f(x) = y \bigr) ,
\]
"if \( f \) is injective, then \( f \) is surjective".

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sigma \) is true in every structure whose domain is finite.
2. Give a structure with an infinite domain in which \( \sigma \) is false.
3. Deduce that \( \sigma \) is not derivable, although no finite structure is a counter-model.
:::
:::

::: {.solution}
[Hint 1]

For (a), suppose \( f^{\fM} \) is injective on a finite \( D \) with \( n \) elements, and count the elements of its image.
:::

::: {.solution}
[Hint 2]

For (b), look for an operation on \( \nN \) that never repeats a value but misses a value.
:::

::: {.solution}
*(a)* Let \( \fM \) have a finite domain \( D \) with \( n \ge 1 \) elements. If the hypothesis of \( \sigma \) is false in \( \fM \), then \( \sigma \) is true by (S5). So suppose it is true: by (S6), (S5) and (S2), for all \( d, e \in D \), \( f^{\fM}(d) = f^{\fM}(e) \) implies \( d = e \); that is, \( f^{\fM} \) takes different values at different elements. Then the \( n \) elements of \( D \) have \( n \) different values, so the set of values \( \{ f^{\fM}(d) : d \in D \} \) is a subset of \( D \) with \( n \) elements. A subset of an \( n \)-element set with \( n \) elements is the whole set (a counting fact from school, proved in *Sets and Functions*, Section 4.1). So every \( e \in D \) is \( f^{\fM}(d) \) for some \( d \), which is the conclusion of \( \sigma \) by (S6), (S7) and (S2). Hence \( \sigma \) is true in \( \fM \).

*(b)* Take \( D = \nN \) and \( f^{\fM}(d) = d + 1 \). The hypothesis holds: \( d + 1 = e + 1 \) gives \( d = e \). The conclusion fails at \( y = 0 \): there is no \( d \in \nN \) with \( d + 1 = 0 \), since \( d \ge 0 \) gives \( d + 1 \ge 1 \). So \( \sigma \) is false in \( \fM \).

*(c)* The structure of (b) is a counter-model to \( \models \sigma \) (with \( \Gamma \) empty). By the soundness statement of this section, \( \sigma \) is not derivable. By (a), no finite structure could have shown this: a search for counter-models that lists finite structures of size 1, 2, 3, … would never stop.

**Marking scheme.** (10 points)

- 1: (a) disposes of the case where the hypothesis of \( \sigma \) is false, by the clause for \( \to \).
- 3: (a) reads the hypothesis as injectivity of \( f^{\fM} \) and uses finiteness to get surjectivity, naming the counting fact.
- 3: (b) a structure with infinite domain, with the hypothesis checked and the conclusion refuted at a named element.
- 3: (c) concludes non-derivability through soundness and says why finite structures could not have done it.

Fatal errors (0 for the step): in (b), a "counter-model" in which \( f^{\fM} \) is not injective; in (a), an argument that never uses finiteness.
:::

::: {#exr-models-c2}
[C2: A sentence with no finite model, used later]

Let \( \tau \) be the conjunction of the three sentences of the text saying that \( < \) is a strict order with no largest element:
\[
\forall x\, \neg(x < x) \ \wedge \ \forall x\, \forall y\, \forall z\, \bigl( (x < y \wedge y < z) \to x < z \bigr) \ \wedge \ \forall x\, \exists y\, (x < y) .
\]
Prove that every model of \( \tau \) has an infinite domain. Where does your proof use that domains are non-empty?
:::

::: {.solution}
[Hint 1]

Start from one element and keep climbing with the third conjunct.
:::

::: {.solution}
[Hint 2]

Prove by induction on \( k \) that there are elements \( d_1 < d_2 < \dots < d_k \) of \( D \) with \( d_i < d_j \) whenever \( i < j \).
:::

::: {.solution}
Let \( \fM \) be a model of \( \tau \), with domain \( D \), and write \( d < e \) for \( (d, e) \in <^{\fM} \). We prove, for every \( k \ge 1 \), the statement \( A(k) \): *there are elements \( d_1, \dots, d_k \) of \( D \) with \( d_i < d_j \) whenever \( 1 \le i < j \le k \).* We use @ax-induction, applied to the property \( A(m + 1) \) of \( m \in \nN \), so that the base case is \( A(1) \).

*Base.* \( D \) is non-empty (@def-structure, (M1)), so there is some \( d_1 \in D \), and \( A(1) \) holds, with no pairs \( i < j \) to check. This is the one place the proof uses non-emptiness. If an empty domain were allowed, with "for every \( d \in \emptyset \)" read as having nothing to check, all three conjuncts would hold in it (each begins with \( \forall \)), and it has no elements at all: the statement "every model is infinite" would fail.

*Step.* Suppose \( d_1, \dots, d_k \) are as in \( A(k) \). By the third conjunct and (S6), (S7), there is \( d_{k+1} \in D \) with \( d_k < d_{k+1} \). For \( i < k \), we have \( d_i < d_k \) by \( A(k) \), and then \( d_i < d_{k+1} \) by the second conjunct (transitivity). So \( A(k + 1) \) holds.

Now the elements \( d_1, \dots, d_k \) are all different: if \( d_i = d_j \) with \( i < j \), then \( d_i < d_j \) says \( d_i < d_i \), which the first conjunct forbids. So for every \( k \ge 1 \), the domain contains \( k \) different elements. A finite set with \( n \) elements does not contain \( n + 1 \) different elements, so \( D \) is not finite. Since \( (\nN, <) \) is a model of \( \tau \) (as the text checked), \( \tau \) has models, and all of them are infinite.

**Marking scheme.** (10 points)

- 2: names the non-empty domain as the start of the construction, and says what fails without it.
- 3: an induction producing, for every \( k \), a chain of \( k \) elements, using the third conjunct for the step.
- 2: uses transitivity to keep the whole chain increasing, not only neighbors.
- 3: uses irreflexivity to show the elements are different, and concludes that \( D \) is infinite.

A second route: a proof that every non-empty finite subset of \( D \) has a \( < \)-maximal element (induction on its size, with irreflexivity in the base and transitivity in the step), applied to \( D \), which is non-empty, and contradicted by the third conjunct, earns 2 for using \( D \) non-empty, 3 for the induction, 2 for transitivity in the step, and 3 for irreflexivity plus the contradiction with the third conjunct.

Fatal errors (0 for the step): building the chain without showing its elements are distinct; an "infinite chain" asserted without an induction or a recursion.
:::

::: {#exr-models-c3}
[C3: Exit check: formalize, negate, decide]

Work over the domain \( \nR \), with \( n \in \nZ_{>0} \) as a bound as in Section 5.1, and \( 1/n \) as a term.

::: {.enumerate options="label=(\alph*)"}
1. Formalize, with bounded quantifiers: "for every \( \varepsilon > 0 \) there is \( N \in \nZ_{>0} \) such that \( 1/n < \varepsilon \) for every \( n \in \nZ_{>0} \) with \( n \ge N \)."
2. Formalize the sentence obtained from (a) by moving "there is \( N \in \nZ_{>0} \)" to the front.
3. Negate each of (a) and (b) into positive form: no \( \neg \) left in front of a quantifier or an implication, and \( \neg(s < t) \) written as \( s \ge t \).
4. Decide which of (a) and (b) is true in \( \nR \). For the true sentence give a proof, saying what each chosen number depends on; for the false one, prove its negation, giving the witnesses it asks for.
:::

*You may use that for every real number there is a natural number larger than it.*
:::

::: {.solution}
*A remark on the term \( 1/n \).* In the structure \( \nR \), the symbol \( / \) must be a function on all of \( \nR^2 \) (@def-structure, (M3)); give \( x/0 \) a value for every \( x \in \nR \), say \( x/0 \coloneqq 0 \). The bound \( n \in \nZ_{>0} \) keeps \( n \ge 1 \), so those values are never used.

*(a)* \( \forall \varepsilon > 0\ \exists N \in \nZ_{>0}\ \forall n \in \nZ_{>0}\ \bigl( n \ge N \to 1/n < \varepsilon \bigr) \).

*(b)* \( \exists N \in \nZ_{>0}\ \forall \varepsilon > 0\ \forall n \in \nZ_{>0}\ \bigl( n \ge N \to 1/n < \varepsilon \bigr) \).

*(c)* Push \( \neg \) inward one quantifier at a time, keeping each bound (@prp-bounded-quantifier-negation), then negate the implication (@prp-negated-implication):
\[
\begin{aligned}
\neg(a): &\quad \exists \varepsilon > 0\ \forall N \in \nZ_{>0}\ \exists n \in \nZ_{>0}\ \bigl( n \ge N \wedge 1/n \ge \varepsilon \bigr), \\
\neg(b): &\quad \forall N \in \nZ_{>0}\ \exists \varepsilon > 0\ \exists n \in \nZ_{>0}\ \bigl( n \ge N \wedge 1/n \ge \varepsilon \bigr).
\end{aligned}
\]

*(d)* **(a) is true.** Let \( \varepsilon > 0 \). Choose a natural number \( N \) with \( N > 1/\varepsilon \), by the fact allowed in the problem; since \( 1/\varepsilon > 0 \), \( N \in \nZ_{>0} \), and \( N \) depends on \( \varepsilon \). Let \( n \in \nZ_{>0} \) with \( n \ge N \). Then \( n \ge N > 1/\varepsilon > 0 \), and multiplying \( n > 1/\varepsilon \) by the positive number \( \varepsilon / n \) gives \( \varepsilon > 1/n \). Since \( n \) was arbitrary, and then \( \varepsilon \), (a) holds.

**(b) is false; its negation is true.** Let \( N \in \nZ_{>0} \). Take \( \varepsilon = 1/N \), which is positive, and \( n = N \), which is in \( \nZ_{>0} \) with \( n \ge N \). Then \( 1/n = 1/N \ge 1/N = \varepsilon \). Both witnesses depend on \( N \), as the order \( \forall N\ \exists \varepsilon\ \exists n \) allows. Since \( N \) was arbitrary, \( \neg(b) \) holds, so (b) is false. In words: no single \( N \) works for every \( \varepsilon \), because \( \varepsilon = 1/N \) defeats that \( N \).

The two sentences differ only in the order of \( \forall \varepsilon \) and \( \exists N \). In (a) the \( N \) is chosen after \( \varepsilon \) and may depend on it; in (b) it must be chosen first, which is the swap of @exm-counter-model-swap in an analysis setting.

**Marking scheme.** (10 points)

- 2: both formalizations, with the bounds \( \varepsilon > 0 \), \( N \in \nZ_{>0} \), \( n \in \nZ_{>0} \) attached to the right quantifiers and \( \to \) under the \( \forall n \).
- 3: both negations in positive form, with every bound kept, the quantifier order of each preserved, and \( \wedge \) under the \( \exists n \).
- 2: verdict "true" for (a), with a proof in which \( N \) is chosen after \( \varepsilon \) and said to depend on it.
- 3: verdict "false" for (b), with \( \varepsilon \) and \( n \) given as functions of \( N \) and the three facts \( \varepsilon > 0 \), \( n \ge N \), \( 1/n \ge \varepsilon \) checked.

Fatal errors (0 for the step): in the negation of (b), \( \varepsilon \) chosen before \( N \) (a single \( \varepsilon \) for all \( N \)); a bound negated instead of the quantifier (\( \exists \varepsilon \le 0 \), or \( \exists n < N \)).
:::

::: {#exr-counter-models-c4}
[C4: The least size of a counter-model]

For each claim, find the least size of a counter-model, and prove by expansion that no smaller one exists.

::: {.enumerate options="label=(\alph*)"}
1. \( \exists x\, P(x), \ \exists x\, Q(x), \ \exists x\, R(x) \models \exists x\, (P(x) \wedge Q(x)) \vee \exists x\, (Q(x) \wedge R(x)) \vee \exists x\, (P(x) \wedge R(x)) \).
2. \( \forall x\, \exists y\, R(x, y), \ \forall x\, \neg R(x, x) \models \exists x\, \exists y\, \bigl( R(x, y) \wedge R(y, x) \bigr) \).
3. \( \exists x\, P(x), \ \exists x\, \neg P(x), \ \exists x\, Q(x), \ \exists x\, \neg Q(x) \models \exists x\, (P(x) \wedge Q(x)) \vee \exists x\, (\neg P(x) \wedge \neg Q(x)) \).
:::
:::

::: {.solution}
[Hint]

In each part, the premises demand witnesses. Count how many of them can share an element before the conclusion becomes true.
:::

::: {.solution}
*(a) Least size 3:* \( D = \{ a, b, c \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \), \( R^{\fM} = \{ c \} \). The premises hold with the witnesses \( a \), \( b \), \( c \), and no element has two of the three predicates, so each disjunct of the conclusion fails. With at most two elements, the three witnesses for \( P \), \( Q \), \( R \) lie among two elements, so one element is a witness for two of them, and the matching disjunct holds. (Over \( \{ a, b \} \): the premises expand to \( P(a) \vee P(b) \), \( Q(a) \vee Q(b) \), \( R(a) \vee R(b) \); of the three letters chosen, two fall on the same element.)

*(b) Least size 3:* \( D = \{ a, b, c \} \), \( R^{\fM} = \{ (a, b), (b, c), (c, a) \} \), a three-cycle: every element has an arrow out, none has a loop, and no two elements have arrows both ways. Size 1: the first premise expands to \( R(a, a) \), against the second. Size 2: the second premise gives \( \neg R(a, a) \wedge \neg R(b, b) \), so the first, \( (R(a, a) \vee R(a, b)) \wedge (R(b, a) \vee R(b, b)) \), forces \( R(a, b) \) and \( R(b, a) \), and the conclusion holds at \( x = a \), \( y = b \).

*(c) Least size 2:* \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \): each element has exactly one of \( P \), \( Q \), so neither disjunct of the conclusion holds. Size 1: \( \exists x\, P(x) \) and \( \exists x\, \neg P(x) \) expand to \( P(a) \) and \( \neg P(a) \), which cannot both hold.

**Marking scheme.** (10 points)

- 4: (a): the counter-model checked (2); the counting argument for size 2 (2).
- 4: (b): the counter-model (1); size 1 (1); size 2 by expansion (2).
- 2: (c).

Fatal errors (0 for the step): a size claim without the proof that every smaller structure fails.
:::

<!-- dependency ledger
exm-counter-model-swap (claim): Figure 7.2-M: the three pictures (A), (B), (C) and the two Quick checks after them | inline; verify/ch07/exm-counter-model-swap.py ((B) on a window of Z and by the argument given)
exm-counter-model-swap (solution): Z with >, the two-element identity; no one-element counter-model | inline; verify/ch07/exm-counter-model-swap.py
exm-counter-model-swap (example): converses of prp-exists-and and of the forall/or law; exists x P(x) |/= P(c); P(x_0) |/= forall x P(x); strict-order models Z, Q and the one-element non-model; the Quick check on the universal hypothesis | inline; verify/ch07/exm-counter-model-swap.py
exm-counter-model-swap (example): every integer is even or odd, and not both (the Z illustrations of the two converses) | F2.2 (promised); STATUS F1.1 row, as in F1.1 §01 and F1.1 §07
exm-counter-model-procedure (claim): the search procedure and its flowchart: a guide, no claim of termination or completeness | remark; nothing rests on it
exm-counter-model-procedure (solution): the negated conclusion pushed inward; the structure on {a, b}; the N reading (P even, R(x, y) as y = 2x + 1) | prp-quantifier-negation (c), twice (F1.8 §02, cited by section); then on the matrix not(R(x,y) and P(y)) == R(x,y) -> not P(y) by prp-standard-equivalences (b), (c) (F1.3 §05; derivably, prp-taut-skeleton, F1.8 §03); inline; every integer is even or odd and not both (2x + 1 is odd, not even): F2.2 (promised), STATUS F1.1 row; verify/ch07/exm-counter-model-procedure.py
exm-small-domains (claim): the expansion is true exactly when the sentence is | inline: the expansion records the (S6)/(S7)/(S1) check over the elements, with no substitution and no new constants (lem-term-substitution is not used)
exm-small-domains (solution): no counter-model of size 1; the size-2 counter-model, unique | inline; verify/ch07/exm-small-domains.py
exm-small-domains (claim): the monadic bound 2^k | stated without proof and marked so; nothing depends on it
exm-three-classes (claim): the side-condition table: each WRONG step and its counter-model, each RIGHT step legal; each RIGHT sequent valid, the F1.4 §04 and §06 rows only together with their arith premise (forall x (x > 0 -> x + 1 > 0), forall x (x > 5 -> x + 1 > 6)), F1.6 §03 Step 1 (pointer) | F1.4 §03-§07 (the delivered counterexamples, cited by section; exr-existential-introduction-c1 cited); counter-models checked by verify/ch07/exm-three-classes.py
def-first-order-entailment (claim): Gamma |- phi implies Gamma |= phi (soundness for predicate logic) | stated without proof in this section and marked so; proved in F1.6 §03 (optional; thm-first-order-soundness, never cited here)
def-first-order-entailment (claim): x^2 on R is continuous and not uniformly continuous | exm-square-not-uniform (F1.8 §04), cited in prose
def-first-order-entailment (claim): What this certifies: each listed counter-reading of F1.4 §01-F1.8 §04 | pointers to the cited labels and sections; no proof rests on them
exm-three-classes (solution): the four sentences' classes; the one-element structure for forall x not(S(x) = 0) | truth tables (skeletons); inline; verify/ch07/exm-three-classes.py
exm-three-classes (claim): an instance of a tautology is valid | fold "Why an instance of a tautology is valid" (inline argument, def-truth-value cited); for prime formulas sharing a letter, renaming keeps meaning, F1.6 §03 (optional; named by section, no label cited)
exm-three-classes (claim): an instance of a tautology is derivable | prp-taut-skeleton (cited)
exm-three-classes (claim): no mechanical procedure decides derivability (Church, Turing 1936) | stated without proof and marked so; nothing depends on it
exm-three-classes (claim): extensionality's logical half is derivable; the two-dot reading | exm-extensionality-logical-half (F1.4 §07, cited); inline
exm-three-classes (claim): (Z1) is the first axiom of Axiomatic Set Theory | ST.1 (ax-zf-fragment; Looking ahead, no reason rests on it)
exr-counter-models-a1 (solution): (c) exr-models-c1's sentence; (d) the warning's example | exr-models-c1 (cited); inline
exr-counter-models-a2 (solution): every part | inline; verify/ch07/exr-counter-models-a2.py
exr-models-b1 (solution): the three finite counter-models | verify/ch07/exr-models-b1.py
exr-models-b1 (solution): (iii) non-derivability from the counter-model with l(x) = b; forall x (P(x) -> P(x)) is satisfied everywhere by (S5), (S6) | the soundness statement of this section (not proved here; F1.6 §03); inline
exr-counter-models-b2 (solution): the eight verdicts, the counter-models, the derivations of (a) and (c) | inline; verify/ch07/exr-counter-models-b2.py (all structures of size <= 3); tools/check_fitch.py
exr-counter-models-b2 (solution): derivations for (e), (f), (h) exist | stated, not given; each is a short exercise with the rules of F1.4 §03-§06
exr-models-b3 (solution): the two-element counter-model | verify/ch07/exr-models-b3.py
exr-models-b3 (solution): non-derivability from a counter-model | the soundness statement of this section (not proved here; F1.6 §03)
exr-counter-models-b4 (solution): the broken lines, the counter-models (with the assignment in (c)), the repairs | inline; verify/ch07/exr-counter-models-b4.py; tools/check_fitch.py (the four WRONG blocks marked expect-invalid; the repairs of (a) and (c) checked; the repaired (a)'s conclusion valid on small structures)
exr-models-c1 (solution): a subset of an n-element set with n elements is the whole set | school counting fact, named in the solution; F2.3 (promised) proves it
exr-models-c1 (solution): successor on N is injective and misses 0 | inline
exr-models-c1 (solution): non-derivability from a counter-model | the soundness statement of this section (not proved here; F1.6 §03)
exr-models-c2 (solution): a finite set with n elements does not contain n + 1 different elements | school counting fact, named in the solution; F2.3 (promised)
exr-models-c3 (solution): for every real there is a larger natural number | given in the problem; thm-naturals-unbounded (AN1.1), not cited
exr-models-c3 (solution): n > 1/eps > 0 implies 1/n < eps | school algebra of < (AN1.1 ordered-field rules)
exr-counter-models-c4 (solution): the least sizes 3, 3, 2, with the smaller sizes excluded | inline (expansion, pigeonhole on two elements); verify/ch07/exr-counter-models-c4.py
-->
