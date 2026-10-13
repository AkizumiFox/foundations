# Counter-models

*S3-PLACEHOLDER: opening frame of Section 7.2, split off in D2.*

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

The two-element structure is the \( \nZ \) structure's idea at its smallest: each element is related to something, and nothing is related to everything. Finite counter-models are convenient because every clause can be checked by listing. They are not always available: Exercise C1 below gives a sentence that is true in every finite structure and false in an infinite one, and Exercise C2 a sentence with only infinite models.

**The converse of @prp-exists-and.** Section 5.6 derived \( \exists x\, (P(x) \wedge Q(x)) \vdash \exists x\, P(x) \wedge \exists x\, Q(x) \) and asked about the converse. We show
\[
\exists x\, P(x) \wedge \exists x\, Q(x) \not\models \exists x\, (P(x) \wedge Q(x)) .
\]
Backwards from the conclusion: it is false when no element is in both \( P^{\fM} \) and \( Q^{\fM} \). The premise needs \( P^{\fM} \) and \( Q^{\fM} \) non-empty. So take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \). The premise holds by (S5) and (S7), with witnesses \( a \) for \( P \) and \( b \) for \( Q \). The conclusion fails: at \( d = a \), \( a \notin Q^{\fM} \); at \( d = b \), \( b \notin P^{\fM} \). In arithmetic: in \( \nZ \), some integer is even and some integer is odd, but no integer is both. The two witnesses of the premise are different objects, and the conclusion needs one.

**The converse of the \( \forall \)/\( \vee \) law.** The one-way law \( \forall x\, P(x) \vee \forall x\, Q(x) \vdash \forall x\, (P(x) \vee Q(x)) \) of @prp-quantifier-distribution has a false converse, and the same structure shows it:
\[
\forall x\, (P(x) \vee Q(x)) \not\models \forall x\, P(x) \vee \forall x\, Q(x) .
\]
With \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \): each element is in \( P^{\fM} \) or in \( Q^{\fM} \), so the premise holds; \( \forall x\, P(x) \) fails at \( b \) and \( \forall x\, Q(x) \) fails at \( a \), so by (S5) the disjunction fails. In \( \nZ \): every integer is even or odd, but it is false that every integer is even, and false that every integer is odd.

**A witness is not a named constant.** @exr-existential-introduction-c2 asked why \( \exists x\, P(x) \vdash P(c) \) cannot be derived. Take \( D = \{ a, b \} \), \( c^{\fM} = a \) and \( P^{\fM} = \{ b \} \). The premise holds with the witness \( b \); the conclusion \( P(c) \) fails, since the value of \( c \) is \( a \notin P^{\fM} \). So \( \exists x\, P(x) \not\models P(c) \). The premise says that something has \( P \), and nothing says that the object named \( c \) is that something.

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
which say that \( < \) is a **strict order** (never \( x < x \); \( x < y \) and \( y < z \) give \( x < z \)) **with no largest element**. The structure \( (\nN, <) \) is a model of all three: no number is less than itself, the order is transitive, and \( d + 1 > d \) is a witness for the third sentence. It is the one the sentences were written with in mind, but not the only one: in \( (\nZ, <) \) and \( (\nQ, <) \) all three are true, by the same checks. These models differ in ways the three sentences cannot see: \( \nZ \) has no least element, and \( \nQ \) has a third element between any two. And the one-element structure \( D = \{ a \} \) is not a model of the three sentences: if \( (a, a) \in <^{\fM} \) the first sentence fails, and if not, the third fails at \( d = a \). Exercise C2 shows that no **finite** structure is a model of them.

::: {.check}
Give a counter-model to \( \forall x\, P(x) \to \forall x\, Q(x) \models \forall x\, (P(x) \to Q(x)) \). (Think about what makes an implication with a universal hypothesis true cheaply.)
:::

::: {.solution}
Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \emptyset \). The premise is an implication whose hypothesis \( \forall x\, P(x) \) is false (it fails at \( b \)), so by (S5) the premise is true. The conclusion fails at \( d = a \): \( a \in P^{\fM} \) and \( a \notin Q^{\fM} \), so \( P(x) \to Q(x) \) is not satisfied under \( \ell[x \mapsto a] \). (Any structure with \( P^{\fM} \ne D \) and some element in \( P^{\fM} \) but not in \( Q^{\fM} \) works.)
:::

## From counter-models to non-derivability {#from-counter-models-to-non-derivability}

A counter-model shows \( \Gamma \not\models \varphi \). The stalled searches asked something else: whether \( \Gamma \vdash \varphi \). The bridge is the same as in Chapter 4, where @thm-soundness turned a refuting row into a proof that no derivation exists (@cor-refuting-row). For predicate logic it reads:

*Soundness for predicate logic.* If \( \Gamma \vdash \varphi \) with the rules of Chapters 1 and 2 and the quantifier and equality rules of Sections 5.3 to 5.7, then \( \Gamma \models \varphi \) in the sense of @def-first-order-entailment. Consequently, a counter-model to \( \Gamma \models \varphi \) shows \( \Gamma \nvdash \varphi \).

This statement is **not proved in this section**. Its proof extends Chapter 4's to the new rules, and it is the subject of Section 7.3, which is optional. The proof is where each side condition of the quantifier rules is used: the fresh-name conditions of \( \rulename{\forall I} \) and \( \rulename{\exists E} \), and "free for" in \( \rulename{\forall E} \), \( \rulename{\exists I} \), and \( \rulename{{=}E} \). A reader who skips Section 7.3 may take the statement on trust, as the rest of the book does; a reader who reads it will see why the side conditions are exactly as strict as they are.

With the statement, the examples above become non-derivability results. \( \forall y\, \exists x\, R(x, y) \nvdash \exists x\, \forall y\, R(x, y) \): the converse search of @prp-exists-forall-swap had to stall, and the two lines where it stalled, the blocked \( \rulename{\forall I} \) and the blocked close of the \( \rulename{\exists E} \) box, are not a lack of cleverness. Likewise the converse of @prp-exists-and, the converse of the \( \forall \)/\( \vee \) law, \( \exists x\, P(x) \vdash P(c) \), and \( P(x_0) \vdash \forall x\, P(x) \) have no derivations. And the same reasoning is the semantic side of Section 6.4: there, @exm-square-not-uniform showed that \( x^2 \) on \( \nR \) is continuous and not uniformly continuous, so the arithmetic structure on \( \nR \), with \( f \) read as squaring, is a counter-model to "continuous entails uniformly continuous".

::: {.warning}
A counter-model proves **non**-derivability; it never proves derivability, and a structure in which a sentence is true says nothing about whether the sentence is derivable. \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \), yet it is not derivable: it is false in \( (\{ 1, 2, 3 \}, <) \). To show \( \Gamma \vdash \varphi \), write a derivation.
:::

## Exercises

### A. Check your understanding

<!-- S3-PLACEHOLDER: items -->

### B. Practice

::: {#exr-models-b1}
[B1: Three counter-models]

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

::: {#exr-models-b3}
[B3: The converse from Section 5.4]

@exr-universal-introduction-b2 derived \( \forall x\, (P(x) \to Q(x)) \vdash \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \), and its search for the converse stalled. Show
\[
\forall x\, \neg Q(x) \to \forall x\, \neg P(x) \not\models \forall x\, (P(x) \to Q(x)) .
\]
:::

::: {.solution}
Work backwards. The conclusion fails when some \( d \) has \( d \in P^{\fM} \) and \( d \notin Q^{\fM} \). The premise is cheapest to make true through a false hypothesis: make \( \forall x\, \neg Q(x) \) false by putting some element in \( Q^{\fM} \). Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \).

Premise: \( \forall x\, \neg Q(x) \) fails at \( d = b \), since \( b \in Q^{\fM} \); so the implication holds by (S5). Conclusion: at \( d = a \), \( a \in P^{\fM} \) and \( a \notin Q^{\fM} \), so \( P(x) \to Q(x) \) fails under \( \ell[x \mapsto a] \), and (S6) fails. By the soundness statement of this section, the converse is not derivable, and the stalled search could not have succeeded.
:::

### C. Going deeper

::: {#exr-models-c1}
[C1: True in every finite model]

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
*(a)* Let \( \fM \) have a finite domain \( D \) with \( n \ge 1 \) elements. If the hypothesis of \( \sigma \) is false in \( \fM \), then \( \sigma \) is true by (S5). So suppose it is true: by (S6), (S5) and (S2), for all \( d, e \in D \), \( f^{\fM}(d) = f^{\fM}(e) \) implies \( d = e \); that is, \( f^{\fM} \) takes different values at different elements. Then the \( n \) elements of \( D \) have \( n \) different values, so the set of values \( \{ f^{\fM}(d) : d \in D \} \) is a subset of \( D \) with \( n \) elements. A subset of an \( n \)-element set with \( n \) elements is the whole set (a counting fact from school, proved in *Sets, Relations, and Cardinality*, Chapter 3). So every \( e \in D \) is \( f^{\fM}(d) \) for some \( d \), which is the conclusion of \( \sigma \) by (S6), (S7) and (S2). Hence \( \sigma \) is true in \( \fM \).

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
[C2: A sentence with no finite model]

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

### R. Review

::: {#exr-models-r1}
[R1]

Decide whether each sequent is derivable, and justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (p \to q) \to r \vdash p \to r \).
2. \( (p \to q) \to r \vdash q \to r \).
:::
:::

::: {.solution}
*(a)* Not derivable. Look for a refuting row, backwards from the conclusion: \( p \to r \) is false only when \( p = \mathrm{T} \) and \( r = \mathrm{F} \). The premise must then be true, so its hypothesis \( p \to q \) must be false, which needs \( q = \mathrm{F} \). In the row \( p = \mathrm{T} \), \( q = \mathrm{F} \), \( r = \mathrm{F} \), the premise is \( \mathrm{F} \to \mathrm{F} \), true, and the conclusion is \( \mathrm{T} \to \mathrm{F} \), false. By @cor-refuting-row there is no derivation.

*(b)* Derivable. The goal is an implication, so open a box on \( q \); the premise is waiting for \( p \to q \), which a box on \( p \) produces by repeating \( q \) (the goal-directed and premise-directed steps of the search method of Section 3.1).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(p \to q) \to r}
  \open
  \hypo {2} {q}
  \open
  \hypo {3} {p}
  \have {4} {q} \r{2}
  \close
  \have {5} {p \to q} \ii{3-4}
  \have {6} {r} \ie{1,5}
  \close
  \have {7} {q \to r} \ii{2-6}
\end{nd}$
\end{center}
```

The row method of (a) could not settle (b): no row refutes it, and only a derivation (or @thm-completeness) shows it is derivable.
:::

::: {#exr-models-r2}
[R2]

Derive \( \neg(P \to \neg Q) \vdash \neg\neg P \wedge \neg\neg Q \) without \( \rulename{RAA} \) and without derived rules that use it. Which rule would you need to derive \( P \wedge Q \) itself?
:::

::: {.solution}
The goal is a conjunction, so derive each conjunct. Each is a negation, so each gets a \( \rulename{\neg I} \) box, whose goal is \( \bot \). The only way to use the premise \( \neg(P \to \neg Q) \) is to clash with it, so inside each box we build \( P \to \neg Q \). In the first box, from \( \neg P \): a \( \rulename{{\to}I} \) box on \( P \) clashes \( P \) with \( \neg P \) and uses \( \rulename{\bot E} \) (the pattern of @prp-vacuous-implication). In the second, from \( \neg Q \): a \( \rulename{{\to}I} \) box on \( P \) simply repeats \( \neg Q \). These are the rules of Chapters 1 and 2 (@def-rules-negation, @def-rules-contradiction, @def-rules-implication).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \to \neg Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {\neg Q} \be{4}
  \close
  \have {6} {P \to \neg Q} \ii{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {\neg\neg P} \ni{2-7}
  \open
  \hypo {9} {\neg Q}
  \open
  \hypo {10} {P}
  \have {11} {\neg Q} \r{9}
  \close
  \have {12} {P \to \neg Q} \ii{10-11}
  \have {13} {\bot} \ne{12,1}
  \close
  \have {14} {\neg\neg Q} \ni{9-13}
  \have {15} {\neg\neg P \wedge \neg\neg Q} \ai{8,14}
\end{nd}$
\end{center}
```

No \( \rulename{RAA} \) is used. To reach \( P \wedge Q \) we would need \( P \) from \( \neg\neg P \) and \( Q \) from \( \neg\neg Q \), that is, \( \rulename{\neg\neg E} \), which is derived with \( \rulename{RAA} \) (@prp-double-negation), or an \( \rulename{RAA} \) box directly (@def-rule-raa). The look-alike is @exr-finding-derivations-b1 (b), \( \neg(P \to Q) \vdash P \wedge \neg Q \): there the conjunct \( P \) needed \( \rulename{RAA} \), while \( \neg Q \) came by \( \rulename{\neg I} \) alone. Here both conjuncts stop at a double negation. That no derivation of \( P \) (or of \( P \wedge Q \)) from the premise avoids \( \rulename{RAA} \) is true, but we state it without proof, and nothing depends on it.
:::

::: {#exr-models-r3}
[R3]

Derive \( \neg\exists x\, (P(x) \to \neg Q(x)) \vdash \forall x\, \bigl( \neg\neg P(x) \wedge \neg\neg Q(x) \bigr) \) without \( \rulename{RAA} \).
:::

::: {.solution}
The goal is \( \forall x \), so open a flagged box with a fresh name \( x_0 \) (@def-rules-universal); the new goal is \( \neg\neg P(x_0) \wedge \neg\neg Q(x_0) \). Inside, run the derivation of R2 (@exr-models-r2) with \( P(x_0) \) and \( Q(x_0) \) in place of \( P \) and \( Q \). One change: the premise is now \( \neg\exists x\, (P(x) \to \neg Q(x)) \), not \( \neg(P \to \neg Q) \), so each clash first turns \( P(x_0) \to \neg Q(x_0) \) into \( \exists x\, (P(x) \to \neg Q(x)) \) by \( \rulename{\exists I} \) at \( x_0 \) (@def-rule-existential-introduction).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \exists x\, (P(x) \to \neg Q(x))}
  \open[x_0]
  \open
  \hypo {2} {\neg P(x_0)}
  \open
  \hypo {3} {P(x_0)}
  \have {4} {\bot} \ne{3,2}
  \have {5} {\neg Q(x_0)} \be{4}
  \close
  \have {6} {P(x_0) \to \neg Q(x_0)} \ii{3-5}
  \have {7} {\exists x\, (P(x) \to \neg Q(x))} \Ei{6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {\neg\neg P(x_0)} \ni{2-8}
  \open
  \hypo {10} {\neg Q(x_0)}
  \open
  \hypo {11} {P(x_0)}
  \have {12} {\neg Q(x_0)} \r{10}
  \close
  \have {13} {P(x_0) \to \neg Q(x_0)} \ii{11-12}
  \have {14} {\exists x\, (P(x) \to \neg Q(x))} \Ei{13}
  \have {15} {\bot} \ne{14,1}
  \close
  \have {16} {\neg\neg Q(x_0)} \ni{10-15}
  \have {17} {\neg\neg P(x_0) \wedge \neg\neg Q(x_0)} \ai{9,16}
  \close
  \have {18} {\forall x\, (\neg\neg P(x) \wedge \neg\neg Q(x))} \Ai{2-17}
\end{nd}$
\end{center}
```

The side condition of \( \rulename{\forall I} \) at line 18: \( x_0 \) does not appear in the premise on line 1, no box is open at line 18, and \( x_0 \) does not appear in the conclusion. The flagged box immediately contains the \( \rulename{\neg I} \) box of line 2, so it is cited from line 2, the first line of that inner box. Lines 7 and 14 are legal \( \rulename{\exists I} \) steps: \( P(x_0) \to \neg Q(x_0) \) is \( (P(x) \to \neg Q(x))[x_0/x] \). The whole derivation is R2's, run inside a flagged box, with an \( \rulename{\exists I} \) before each clash.
:::

::: {#exr-models-r4}
[R4]

Is the sentence \( \forall x\, \exists y\, (x < y) \to \exists y\, \forall x\, (x < y) \) true in \( (\nN, <) \)? Is it derivable?
:::

::: {.solution}
*True in \( (\nN, <) \)?* No. The hypothesis \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \): each \( d \) has \( d + 1 \) above it. The conclusion \( \exists y\, \forall x\, (x < y) \) is false: a candidate \( e \) fails at \( x = e \), since \( e < e \) is false. By (S5) of @def-satisfaction, an implication with a true hypothesis and a false conclusion is false.

*Derivable?* No. By the soundness statement of this section, a derivable sentence is true in every structure; this one is false in \( (\nN, <) \), so no derivation exists.

*Why these tools.* A structure settles the question in two lines, while a derivation search could only fail, and a failed search proves nothing. A truth table is the wrong look-alike: it reads the sentence as \( p \to q \) with two atoms, and a refuting row for \( p \to q \) says nothing here, since the sentence \( \forall x\, P(x) \to \exists x\, P(x) \) has the same shape and is derivable (@prp-forall-implies-exists, then \( \rulename{{\to}I} \)). The soundness statement used here is proved in Section 7.3.
:::

<!-- dependency ledger
exm-counter-model-swap (solution): Z with >, the two-element identity; no one-element counter-model | inline; verify/ch07/exm-counter-model-swap.py
exm-counter-model-swap (example): converses of prp-exists-and and of the forall/or law; exists x P(x) |/= P(c); P(x_0) |/= forall x P(x); strict-order models Z, Q and the one-element non-model; the second Quick check | inline; verify/ch07/exm-counter-model-swap.py
exm-counter-model-swap (example): every integer is even or odd, and not both (the Z illustrations of the two converses) | F2.2 (promised); STATUS F1.1 row, as in F1.1 §01 and F1.1 §07
def-first-order-entailment (claim): Gamma |- phi implies Gamma |= phi (soundness for predicate logic) | stated without proof in this section and marked so; proved in F1.6 §03 (optional; thm-first-order-soundness, never cited here)
def-first-order-entailment (claim): x^2 on R is continuous and not uniformly continuous | exm-square-not-uniform (F1.8 §04), cited in prose
exr-models-b1 (solution): the three finite counter-models | verify/ch07/exr-models-b1.py
exr-models-b3 (solution): the two-element counter-model | verify/ch07/exr-models-b3.py
exr-models-c1 (solution): a subset of an n-element set with n elements is the whole set | school counting fact, named in the solution; F2.3 (promised) proves it
exr-models-c1 (solution): successor on N is injective and misses 0 | inline
exr-models-c2 (solution): a finite set with n elements does not contain n + 1 different elements | school counting fact, named in the solution; F2.3 (promised)
exr-models-c3 (solution): for every real there is a larger natural number | given in the problem; thm-naturals-unbounded (AN1.1), not cited
exr-models-c3 (solution): n > 1/eps > 0 implies 1/n < eps | school algebra of < (AN1.1 ordered-field rules)
exr-models-b1 (solution): (iii) non-derivability from the counter-model with l(x) = b; forall x (P(x) -> P(x)) is satisfied everywhere by (S5), (S6) | the soundness statement of this section (not proved here; F1.6 §03); inline
exr-models-b3 (solution): non-derivability from a counter-model | the soundness statement of this section (not proved here; F1.6 §03)
exr-models-c1 (solution): non-derivability from a counter-model | the soundness statement of this section (not proved here; F1.6 §03)
exr-models-r4 (solution): non-derivability from a false instance | the soundness statement of this section (not proved here; F1.6 §03)
exr-models-r1 (solution): refuting row and derivation | cor-refuting-row; verify/ch07/exr-models-r1.py
exr-models-r2 (solution): neg-neg-E is derived with RAA | prp-double-negation (cited)
exr-models-r2 (solution): no RAA-free derivation of P or P and Q from not(P -> not Q) | stated without proof and marked so; nothing depends on it
exr-models-r3 (solution): the derivation of R2 rerun with P(x_0), Q(x_0) inside a flagged box | exr-models-r2 (cited)
-->
