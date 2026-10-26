# Parked: old Section 6.5, merge source for 6.3

<!-- Parked from fd3 (fd3/authoring/design/layout-proposal.md §4, approved 2026-10-26). Not part of any book's src; nothing builds or scans it.
Old section: fd3 6.5 Axioms or a Model? (src/ch06-complete-ordered-field/05-axioms-or-model.md)
Labels: exr-axioms-or-model-a1, exr-axioms-or-model-b1, exr-axioms-or-model-b2, exr-axioms-or-model-c1, exr-axioms-or-model-r1, exr-axioms-or-model-r2, exr-axioms-or-model-r3, exr-axioms-or-model-r4
Intended home: fd3 6.3 (S3 merges a compressed version, about 1,500 words: the AN1 table, the zero = ∅ example, limits carried across the isomorphism); R1–R4 and the real-closed-field remark are deleted (they repeat exm-truncations-equivalent, exm-finite-ring-not-orderable, ℝ(x), exm-cof-sup-one-minus-reciprocals)
-->

# Assume the Axioms or Build a Model

Section 6.3 showed that two complete ordered fields are always linked, and by exactly one order-preserving field isomorphism (@thm-cof-uniqueness). This last section asks what that theorem means for the rest of the series. There are two honest ways to begin analysis: assume the axioms of a complete ordered field, or build a model of them. We compare the two, show what an isomorphism carries from one model to another and what it does not, and list what *Analysis on the Real Line* takes from this volume.

## Two ways to begin analysis

**(A) Assume the axioms.** Declare that \( \nR \) is a set with an addition, a multiplication and a relation \( < \) satisfying the field axioms (F1)–(F9) and \( 1 \ne 0 \) of @def-commutative-ring-and-field, the order axioms (O1)–(O4) of @def-ordered-ring-and-field, and completeness, @def-complete-ordered-field: every non-empty subset that is bounded above has a supremum. Then prove theorems from these axioms and nothing else. *Analysis on the Real Line*, Chapter 1 begins this way. It assumes an ordered field containing \( \nQ \) in which the least upper bound axiom holds, and every theorem of that volume about real numbers is proved from this assumption, with the logic and set theory of the earlier volumes.

**(B) Build a model.** Start from the axioms of set theory and construct the objects one by one. This volume did that: the natural numbers as the set \( \omega \) in Chapter 1, the integers and rationals as classes of pairs in Chapter 2, and the real numbers as classes of Cauchy sequences of rationals in Chapter 5. The result is a complete ordered field (@thm-reals-complete-ordered-field), and no property of it was assumed.

Route (A) is shorter, and it is the route of most analysis courses. On its own, though, it leaves two questions open.

::: {.enumerate options="label=(Q\arabic*)"}
1. *Is there a complete ordered field at all?* A list of axioms can be contradictory: a list of demands that nothing meets. Theorems proved from a contradictory list would all be worthless.
2. *If there are several, which one is \( \nR \)?* Route (A) says "let \( \nR \) be **a** complete ordered field". The article matters.
:::

Route (B) answers (Q1). The Cauchy model of Chapter 5 is a complete ordered field, built inside the set theory of Chapter 1. So if a contradiction could be derived from the axioms of a complete ordered field, the same derivation, run in the Cauchy model, would be a contradiction about one particular set built in that set theory. In short, the axioms are consistent if the set theory of Chapter 1 is. That is the most a construction can give: it moves the question of consistency from the axioms of \( \nR \) to the axioms of set theory.

Route (B) alone does not answer (Q2). A second builder who uses Dedekind cuts, as the optional Chapter 7 does, obtains a different set, whose elements are sets of rationals rather than classes of sequences. The answer to (Q2) is the theorem of Section 6.3, and the rest of this section explains why it is the right answer.

## What uniqueness adds

Throughout this part, \( F \) and \( L \) are complete ordered fields and \( \varphi \colon F \to L \) is the order-preserving field isomorphism of @thm-cof-uniqueness. By definition (@def-cof-order-preserving-map), \( \varphi \) is a bijection that respects \( + \), \( \cdot \), \( 1 \) and \( < \). Everything else we need follows in a line or two. Within this section, (P1)–(P6) name the six facts below; they are not the positive-set clauses (P1)–(P2) of @prp-order-from-positives used in Section 6.4.

::: {.enumerate options="label=(P\arabic*)"}
1. \( \varphi(0) = 0 \), \( \varphi(-x) = -\varphi(x) \) and \( \varphi(x - y) = \varphi(x) - \varphi(y) \). Indeed \( \varphi(0) = \varphi(0 + 0) = \varphi(0) + \varphi(0) \), and adding \( -\varphi(0) \) gives \( \varphi(0) = 0 \); then \( \varphi(x) + \varphi(-x) = \varphi(0) = 0 \).
2. \( \varphi(x^{-1}) = \varphi(x)^{-1} \) for \( x \ne 0 \), since \( \varphi(x)\varphi(x^{-1}) = \varphi(1) = 1 \).
3. \( x < y \) **if and only if** \( \varphi(x) < \varphi(y) \): the forward direction is the definition, and the backward one is the reflection of order shown just after @def-cof-order-preserving-map. With (P1), \( x > 0 \) if and only if \( \varphi(x) > 0 \).
4. \( \varphi(\abs{x}) = \abs{\varphi(x)} \). If \( x \ge 0 \), then \( \varphi(x) \ge 0 \) by (P3), and both sides are \( \varphi(x) \). If \( x < 0 \), then \( \varphi(x) < 0 \), and both sides are \( \varphi(-x) = -\varphi(x) \) (@def-absolute-value-ordered-field, (P1)).
5. \( \varphi(\iota_F(q)) = \iota_L(q) \) for every \( q \in \nQ \) (@prp-cof-map-fixes-rationals): each rational goes to the same rational.
6. The inverse \( \varphi^{-1} \colon L \to F \) is again an order-preserving field isomorphism (the remark after @cor-cof-isomorphic-to-cauchy-reals). So everything said about \( \varphi \) holds for \( \varphi^{-1} \) too.
:::

The map acts on larger objects through their elements. A subset \( A \subseteq F \) goes to its image \( \varphi(A) = \{ \varphi(a) : a \in A \} \); a sequence \( (a_n) \) in \( F \) goes to \( (\varphi(a_n)) \); a function \( f \colon F \to F \) goes to \( \varphi \circ f \circ \varphi^{-1} \colon L \to L \). Because \( \varphi \) is a bijection, \( x \in A \) if and only if \( \varphi(x) \in \varphi(A) \), and every subset, sequence or function of \( L \) arises in this way from exactly one of \( F \).

*An isomorphism is a renaming: it changes what the elements are called and keeps every relation between them.*

Here is the renaming at work on a statement with three quantifiers.

**Example: limits are carried across.** Let \( (a_n) \) be a sequence in \( F \) and \( a \in F \). Then \( a_n \to a \) in \( F \) (@def-sequence-limit-ordered-field) if and only if \( \varphi(a_n) \to \varphi(a) \) in \( L \).

For (\( \Rightarrow \)), let \( \varepsilon \in L_{>0} \), and put \( \varepsilon' \coloneqq \varphi^{-1}(\varepsilon) \). Then \( \varepsilon' > 0 \) by (P3), since \( \varphi(\varepsilon') = \varepsilon > 0 \). Since \( a_n \to a \), there is \( N \in \nN \), depending on \( \varepsilon' \) and so on \( \varepsilon \), with \( \abs{a_n - a} < \varepsilon' \) for every \( n \ge N \). For such \( n \), by (P1), (P4) and (P3),
\[
\abs{\varphi(a_n) - \varphi(a)} = \varphi\bigl(\abs{a_n - a}\bigr) < \varphi(\varepsilon') = \varepsilon .
\]
So \( \varphi(a_n) \to \varphi(a) \). For (\( \Leftarrow \)), apply (\( \Rightarrow \)) to \( \varphi^{-1} \), which is allowed by (P6).

The step that needs \( \varphi \) to be **onto** is the first one: the tolerance \( \varepsilon \) is an element of \( L \), and the hypothesis speaks only about tolerances in \( F \). Onto is also what carries "converges to some limit" back, since that limit must have a preimage. The map \( \kappa = \iota_{\nR} \colon \nQ \to \nR \) (@thm-rational-embedding (d)) is an order-preserving field map that is not onto, and it fails here: the Newton sequence \( (x_n) \) has no limit in \( \nQ \) (@thm-sqrt2-cauchy-no-rational-limit), while \( (\kappa(x_n)) \) converges in \( \nR \) (@thm-terms-converge-to-class) to \( r = [(x_n)] \), which is not \( \kappa \) of any rational (@exm-sqrt2-class).

The example shows the general pattern. Take a statement about a complete ordered field that is phrased with \( + \), \( \cdot \), \( < \), elements, and subsets, sequences and functions built from elements, with quantifiers ranging over these. Rename every object by \( \varphi \). Each basic piece keeps its truth value: an equation because \( \varphi \) respects \( + \) and \( \cdot \) and is injective, with (P1), (P2), (P4) and (P5) for terms that contain \( - \), \( {}^{-1} \), \( \abs{\cdot} \) or rationals; an inequality by (P3) as well; and a membership because \( \varphi \) is a bijection, as noted above. Quantifiers match as well: "for every element of \( F \)" matches "for every element of \( L \)" because \( \varphi \) is onto; the same holds for subsets, sequences and functions. So the statement is true in \( F \) exactly when it is true in \( L \). We do not state this as a theorem. Making "statement" precise is the business of formal languages, which *Logic and Proof*, Chapter 5 begins with its first-order formulas, and the proof would be an induction on how statements are built. A particular instance is checked as the example was: one renaming for each object, and one preservation fact for each basic piece.

::: {.check}
Let \( F \), \( L \) and \( \varphi \) be as above, and suppose some \( x \in F \) satisfies \( x^3 = x + 1 \). Show that some \( y \in L \) satisfies \( y^3 = y + 1 \).
:::

::: {.solution}
Take \( y \coloneqq \varphi(x) \). By @def-naturals-in-ordered-field (b), \( x^3 = ((1 \cdot x) x) x \), and \( \varphi \) respects \( 1 \) and products, so \( \varphi(x^3) = \varphi(x)^3 \). Hence \( y^3 = \varphi(x^3) = \varphi(x + 1) = \varphi(x) + \varphi(1) = y + 1 \).
:::

**Theorems need no uniqueness; truth does.** One consequence of route (A) holds for any list of axioms, with no uniqueness theorem: a statement **proved** from the axioms is true in every structure satisfying them, since the proof can be run in each. The ordered-field axioms alone have the models \( \nQ \), \( \nQ(\sqrt 2) \) (@def-cof-sqrt2-field) and \( \nR(x) \) (@def-cof-rational-functions), and every result proved from those axioms, such as the rules of @prp-ordered-ring-rules, holds in all three. Yet the three disagree about statements the axioms do not settle:

- "some \( x \) has \( x \cdot x = 1 + 1 \)" is true in \( \nQ(\sqrt 2) \) and false in \( \nQ \) (@thm-no-rational-square-two);
- "some \( y \) lies above \( n \cdot 1 \) for every \( n \in \nN \)" is true in \( \nR(x) \) (witness \( y = x \), @prp-cof-rational-functions-not-archimedean) and false in \( \nQ \) (@thm-rationals-archimedean).

For complete ordered fields no such disagreement can occur. Every statement of the kind described above has the same truth value in all complete ordered fields, **whether or not** anybody has a proof of it from the axioms. That is what uniqueness adds to route (A): its axioms describe one structure, not a family of structures that agree only on what the axioms prove.

## What is not carried across

The renaming keeps relations between elements. It does not keep what the elements are made of. In the Cauchy model, the zero is \( 0_{\nR} = [(0)_n] \) (@def-reals-operations), a class that contains the constant sequence \( (0)_n \); so the zero of \( \nR \) is not the empty set. In another complete ordered field the zero can be the empty set, because the elements of a model can be chosen almost at will.

**A model with any elements we like.** Let \( F \) be a complete ordered field, \( X \) a set, and \( \beta \colon F \to X \) a bijection. Define, for \( u, v \in X \),
\[
\begin{aligned}
u \oplus v &\coloneqq \beta\bigl(\beta^{-1}(u) + \beta^{-1}(v)\bigr) , \qquad
u \odot v \coloneqq \beta\bigl(\beta^{-1}(u) \, \beta^{-1}(v)\bigr) , \\
u \prec v \ &\text{if and only if} \ \beta^{-1}(u) < \beta^{-1}(v) .
\end{aligned}
\]
Then \( X \), with \( \oplus \), \( \odot \) and \( \prec \), is a complete ordered field, and \( \beta \) is an order-preserving field isomorphism. Indeed, with \( u = \beta(a) \) and \( v = \beta(b) \), the definitions read \( \beta(a + b) = \beta(a) \oplus \beta(b) \), \( \beta(ab) = \beta(a) \odot \beta(b) \), and \( a < b \) if and only if \( \beta(a) \prec \beta(b) \). Each axiom for \( X \), rewritten in this way, becomes the same axiom for \( F \): for (F1), \( u \oplus v = \beta(a + b) = \beta(b + a) = v \oplus u \); the zero and one of \( X \) are \( \beta(0) \) and \( \beta(1) \), and \( \beta(1) \ne \beta(0) \) because \( \beta \) is injective and \( 1 \ne 0 \) in \( F \); (F2)–(F9) and (O1)–(O4) go the same way. For completeness, let \( B \subseteq X \) be non-empty and bounded above by \( w \). Then \( \beta^{-1}(B) \) is non-empty and bounded above by \( \beta^{-1}(w) \), so it has a supremum \( s \) in \( F \), and \( \beta(s) \) is a supremum of \( B \), because \( \beta \) and \( \beta^{-1} \) both preserve the order by the definition of \( \prec \).

Apply this to the Cauchy model with \( X \coloneqq (\nR \setminus \{0_{\nR}\}) \cup \{\emptyset\} \), \( \beta(0_{\nR}) \coloneqq \emptyset \) and \( \beta(x) \coloneqq x \) otherwise. Every element of \( \nR \) is a class \( [a] \), which contains \( a \) and so is not empty; hence \( \emptyset \notin \nR \), and \( \beta \) is a bijection. The zero of \( X \) is \( \beta(0_{\nR}) = \emptyset \). So the statement "the zero element is the empty set" is false in \( \nR \) and true in \( X \), although the two are isomorphic. The statement is about what an element is made of, and no renaming can be expected to keep that.

::: {.warning}
**Isomorphic is not equal.** The isomorphism links two models; it does not make them one set, and it does not make \( \nQ \) a subset of \( \nR \). In the Cauchy model the rational number \( 2 \) is a class of pairs of integers (@def-rationals-as-classes), while the real number \( 2 \) is \( \kappa(2) = [(2)_n] \), a class of sequences (@def-rational-embedding); they are different sets, and, as Section 5.2 noted after @def-reals-cauchy-classes, the rational \( 2 \) is not an element of \( \nR \). "\( \nQ \subseteq \nR \)" is shorthand for the embedding \( \iota_{\nR} \), the one copy of \( \nQ \) that @thm-rationals-embed-ordered-field provides, and every isomorphism respects that copy by (P5).
:::

So "which construction is \( \nR \)?" has no mathematical content. Every construction yields a complete ordered field; any two are linked by exactly one isomorphism; and that isomorphism decides, in the same way in both, every question posed with \( + \), \( \cdot \) and \( < \). Questions such as "is \( \sqrt 2 \) a set of rationals?" do depend on the model. In the Cauchy model, \( \sqrt 2 \) is the element \( r \) of @exm-sqrt2-class, a set of sequences; in the cut model of Chapter 7 it is the set of rationals below it. Nothing in analysis depends on the answer, and from *Analysis on the Real Line* on the question is never asked again.

## What *Analysis on the Real Line* takes from here

The analysis volume uses route (A). The table matches each of its assumptions with the place where this series supplies or justifies it.

| Assumed in *Analysis on the Real Line*, Chapter 1 | Supplied or justified here |
|---|---|
| \( \nR \) is an ordered field, axioms (F1)–(F9), (O1)–(O4) | the axioms: @def-commutative-ring-and-field, @def-ordered-ring-and-field, in the same numbering (in *Analysis on the Real Line*, (F7) includes \( 1 \ne 0 \); here it is a separate clause of the field definition); a model: @thm-reals-ordered-field |
| \( \nR \) contains \( \nQ \) | every ordered field contains exactly one copy of \( \nQ \): @thm-rationals-embed-ordered-field; isomorphisms respect it: @prp-cof-map-fixes-rationals |
| the least upper bound axiom | the property: @def-complete-ordered-field; a model: @thm-reals-complete-ordered-field |
| "the" real numbers | any two models are isomorphic, by exactly one isomorphism: @thm-cof-uniqueness, @cor-cof-isomorphic-to-cauchy-reals |
| logic and set theory | *Logic and Proof*, *Sets and Functions*, and Chapter 1 of this volume |

Some results are proved in both volumes, from different starting points. *Analysis on the Real Line*, Chapter 1 proves from its axioms that \( \nN \) is not bounded above, that \( \nQ \) is dense in \( \nR \), and that positive numbers have square roots. Here the same three facts were proved for an arbitrary complete ordered field: @thm-cof-complete-archimedean, @thm-rationals-dense-ordered-field (which needs Archimedes, supplied by the first) and @prp-cof-square-roots. The two volumes start from different places, and neither volume's proofs cite the other's.

::: {.remark}
**Not proved here.** The supremum property speaks about **all subsets** of the field, and that is why it pins \( \nR \) down. Properties that speak only about elements do not. For instance, there are ordered fields that are not Archimedean, yet in which, as in \( \nR \), every positive element is a square and every polynomial function of odd degree with coefficients in the field has a zero. The distinction is between statements whose quantifiers range over elements only, the first-order formulas of *Logic and Proof*, Chapter 5 (@fd1:def-first-order-formula), and statements that also quantify over subsets. This volume does not prove that such fields exist, and nothing in it depends on them.
:::

This ends the main line of the volume. The optional Chapter 7 builds a second complete ordered field from Dedekind cuts; by @thm-cof-uniqueness it is a copy of the Cauchy model, and the chapter can be read as a second look at the rationals-below sets of Section 6.1.

## Exercises

### A. Check your understanding

::: {#exr-axioms-or-model-a1}
[A1]

Throughout, \( F \) and \( L \) are complete ordered fields and \( \varphi \colon F \to L \) is the order-preserving field isomorphism.

::: {.enumerate options="label=(\alph*)"}
1. For each statement, decide whether its truth could depend on which complete ordered field is taken as \( \nR \), and justify your answer: (i) \( \sqrt 2 + \sqrt 3 > 3 \); (ii) the rational number \( 0 \) is an element of the set \( \sqrt 2 \); (iii) \( \nR \) is uncountable.
2. True or false: "The ordered-field axioms prove every statement that is true in \( \nQ \)."
3. Which step of the example "limits are carried across" uses that \( \varphi \) is onto?
4. Why does a model of the axioms, built inside set theory, show that the axioms of a complete ordered field cannot contradict each other unless that set theory does?
:::
:::

::: {.solution}
(a) (i) No. Write \( b \) and \( c \) for the non-negative square roots of \( 2 \) and \( 3 \) in \( F \), which exist and are unique by @prp-cof-square-roots. Then \( \varphi(b) \ge 0 \) by (P3) and \( \varphi(b)^2 = \varphi(b^2) = \varphi(2) = 2 \) by (P5), so \( \varphi(b) \) is the non-negative square root of \( 2 \) in \( L \), by the uniqueness in @prp-cof-square-roots; likewise for \( c \). By (P3) and (P5), \( b + c > 3 \) if and only if \( \varphi(b) + \varphi(c) > 3 \). (The statement is in fact true: both sides are positive, \( (b + c)^2 = 5 + 2bc \), and \( bc \) is the non-negative square root of \( 6 \), so \( 5 + 2bc > 9 \) if and only if \( bc > 2 \), if and only if \( 6 > 4 \), by @prp-ordered-ring-rules (g).)

(ii) Yes. In the Cauchy model, \( \sqrt 2 = r \) is a class of sequences \( \nN \to \nQ \) (@exm-sqrt2-class). By @fd2:def-function each such sequence is the pair \( (G, \nQ) \) of its graph and its codomain, that is, the set \( \{\{G\}, \{G, \nQ\}\} \) of @def-kuratowski-pair, with at most two elements. The rational \( 0 \) is the class \( 0_{\nQ} = \{ (0, s) : s \in \nZ_{>0} \} \) of @def-rationals-as-classes; its elements \( (0, 1) \), \( (0, 2) \), \( (0, 3) \) are pairwise different by @thm-kuratowski-pair, so it has more than two elements. So \( 0_{\nQ} \) is not a sequence, and \( 0_{\nQ} \notin r \).

Now apply the construction above with \( F \coloneqq \nR \), \( X \coloneqq (\nR \setminus \{r\}) \cup \{\{0_{\nQ}\}\} \), \( \beta(r) \coloneqq \{0_{\nQ}\} \) and \( \beta(x) \coloneqq x \) otherwise. Every element of \( \nR \) is a class \( [a] \), which contains the sequence \( a \); the only element of \( \{0_{\nQ}\} \) is \( 0_{\nQ} \), which is not a sequence. So \( \{0_{\nQ}\} \notin \nR \), and \( \beta \) is a bijection. By the argument of (i) with \( \varphi \coloneqq \beta \), the non-negative square root of \( 2 \) in the complete ordered field \( X \) is \( \beta(r) = \{0_{\nQ}\} \), which contains the rational \( 0 \). (In the cut model of the optional Chapter 7, \( \sqrt 2 \) contains \( 0_{\nQ} \) as well.)

(iii) No. A set is countable exactly when it injects into \( \nN \) (@fd2:thm-countable-characterizations). If \( L \) were countable, an injection \( g \colon L \to \nN \) composed with the bijection \( \varphi \) would give an injection \( g \circ \varphi \colon F \to \nN \); and symmetrically with \( \varphi^{-1} \). So \( F \) is countable exactly when \( L \) is.

(b) False. "No \( x \) has \( x \cdot x = 1 + 1 \)" is true in \( \nQ \) (@thm-no-rational-square-two) and false in the ordered field \( \nQ(\sqrt 2) \) (@prp-cof-sqrt2-field-archimedean), which contains \( \sqrt 2 = 0 + 1\sqrt 2 \) (@def-cof-sqrt2-field) with \( \sqrt 2 \cdot \sqrt 2 = 2 = 1 + 1 \) by the choice of \( \sqrt 2 \) (@prp-cof-square-roots). A statement proved from the ordered-field axioms is true in every ordered field (for these first-order statements this is @fd1:thm-first-order-soundness), so this one is not provable from them.

(c) The first: the tolerance \( \varepsilon \) is given in \( L \), and the hypothesis \( a_n \to a \) speaks only about tolerances in \( F \). Surjectivity provides \( \varepsilon' = \varphi^{-1}(\varepsilon) \in F \).

(d) A contradiction derived from the axioms could be run in the model, where it would become a contradiction about one set built in the set theory; so the set theory would be inconsistent. In this volume the model is the Cauchy model (@thm-reals-complete-ordered-field) and the set theory is that of Chapter 1.
:::

### B. Practice

::: {#exr-axioms-or-model-b1}
[B1]

Let \( F \) and \( L \) be complete ordered fields and \( \varphi \colon F \to L \) the order-preserving field isomorphism. Let \( a \in F \) with \( a \ge 0 \), and let \( b \) be the non-negative square root of \( a \). Show that \( \varphi(a) \ge 0 \) and that \( \varphi(b) \) is the non-negative square root of \( \varphi(a) \).
:::

::: {.solution}
Since \( 0 \le a \), (P1) and the order-preservation of \( \varphi \) (or equality) give \( 0 = \varphi(0) \le \varphi(a) \). So \( \varphi(a) \) has exactly one non-negative square root in \( L \), by @prp-cof-square-roots applied in the complete field \( L \). Now \( \varphi(b) \ge \varphi(0) = 0 \) in the same way, and \( \varphi(b)^2 = \varphi(b^2) = \varphi(a) \), since \( \varphi \) respects products. By the uniqueness in @prp-cof-square-roots, \( \varphi(b) \) is the non-negative square root of \( \varphi(a) \).

The argument used only that \( \varphi \) is an order-preserving field map into a complete ordered field; it needs neither bijectivity nor completeness of \( F \), beyond the existence of \( b \).
:::

::: {#exr-axioms-or-model-b2}
[B2]

Let \( F \), \( L \) and \( \varphi \) be as in B1, and let \( (a_n) \) be a sequence in \( F \). Prove that \( (a_n) \) is a Cauchy sequence in \( F \) (@def-cauchy-sequence-ordered-field) if and only if \( (\varphi(a_n)) \) is a Cauchy sequence in \( L \).
:::

::: {.solution}
(\( \Rightarrow \)) Let \( \varepsilon \in L_{>0} \), and put \( \varepsilon' \coloneqq \varphi^{-1}(\varepsilon) \). Since \( \varphi(\varepsilon') = \varepsilon > 0 = \varphi(0) \), and \( \varphi \) reflects order, \( \varepsilon' > 0 \). Since \( (a_n) \) is Cauchy, there is \( N \in \nN \), depending on \( \varepsilon \), with \( \abs{a_m - a_n} < \varepsilon' \) for all \( m, n \ge N \). For such \( m, n \),
\[
\abs{\varphi(a_m) - \varphi(a_n)} = \varphi\bigl(\abs{a_m - a_n}\bigr) < \varphi(\varepsilon') = \varepsilon ,
\]
by (P1), (P4) and (P3). So \( (\varphi(a_n)) \) is Cauchy in \( L \).

(\( \Leftarrow \)) The inverse \( \varphi^{-1} \) is an order-preserving field isomorphism \( L \to F \) (P6), so the same argument with the roles of \( F \) and \( L \) exchanged shows that \( (\varphi^{-1}(\varphi(a_n))) = (a_n) \) is Cauchy in \( F \).
:::

### C. Going deeper

::: {#exr-axioms-or-model-c1}
[C1: Which hypothesis does the work]

::: {.enumerate options="label=(\alph*)"}
1. Prove that there is no map \( \sigma \colon \nQ(\sqrt 2) \to \nQ \) with \( \sigma(1) = 1 \) that respects \( + \) and \( \cdot \). In particular \( \nQ \) and \( \nQ(\sqrt 2) \) are not isomorphic, even as fields.
2. Prove that there is no order-preserving field isomorphism \( \nR \to \nR(x) \).
3. For each of the two pairs, say which hypothesis of @thm-cof-uniqueness fails, and give a statement phrased with \( + \), \( \cdot \) and \( < \) that is true in one field of the pair and false in the other.
:::
:::

::: {.solution}
[Hint 1]

In (a), ask where \( \sigma \) sends \( \sqrt 2 \). In (b), apply the inverse map to the element \( x \).
:::

::: {.solution}
[Hint 2]

In (b), the inverse \( \chi^{-1} \colon \nR(x) \to \nR \) of a supposed isomorphism \( \chi \) is an order-preserving field map, and it fixes the copies of \( \nN \).
:::

::: {.solution}
(a) Suppose \( \sigma \) is such a map. Then \( \sigma(2) = \sigma(1 + 1) = 1 + 1 = 2 \), and
\[
\sigma(\sqrt 2)^2 = \sigma(\sqrt 2 \cdot \sqrt 2) = \sigma(2) = 2 ,
\]
so the rational \( \sigma(\sqrt 2) \) squares to \( 2 \), against @thm-no-rational-square-two. A field isomorphism \( \nQ(\sqrt 2) \to \nQ \) would be such a map, so there is none. A field isomorphism \( \nQ \to \nQ(\sqrt 2) \) would have such a map as its inverse (the inverse respects \( 1 \), \( + \) and \( \cdot \), by the argument for the symmetric clause in the remark after @cor-cof-isomorphic-to-cauchy-reals, which does not use the order), so there is none in that direction either.

(b) Suppose \( \chi \colon \nR \to \nR(x) \) is an order-preserving field isomorphism. Its inverse \( \psi \coloneqq \chi^{-1} \colon \nR(x) \to \nR \) is an order-preserving field map (the remark after @cor-cof-isomorphic-to-cauchy-reals). By @prp-cof-map-fixes-rationals, \( \psi(n \cdot 1) = \psi(\iota_{\nR(x)}(n)) = \iota_{\nR}(n) = n \cdot 1_{\nR} \) for every \( n \in \nN \) (@thm-rationals-embed-ordered-field). In \( \nR(x) \), \( n \cdot 1 < x \) for every \( n \in \nN \) (@prp-cof-rational-functions-not-archimedean). Applying the strictly increasing \( \psi \), \( n \cdot 1_{\nR} < \psi(x) \) for every \( n \in \nN \). But \( \nR \) is complete (@thm-reals-complete-ordered-field), hence Archimedean (@thm-cof-complete-archimedean), so some \( n \) has \( \psi(x) < n \cdot 1_{\nR} \) (@def-archimedean-ordered-field), and (O1) is violated. So \( \chi \) does not exist.

(c) *\( \nQ \) and \( \nQ(\sqrt 2) \).* Both are Archimedean ordered fields (@thm-rationals-archimedean, @prp-cof-sqrt2-field-archimedean), and **neither is complete**: \( \nQ(\sqrt 2) \) by @prp-cof-sqrt2-field-incomplete, and \( \nQ \) because a complete field would contain a square root of \( 2 \) (@prp-cof-square-roots), against @thm-no-rational-square-two. The hypothesis that fails is completeness, for both fields. Separating statement: "some \( x \) has \( x \cdot x = 1 + 1 \)", true in \( \nQ(\sqrt 2) \), false in \( \nQ \).

*\( \nR \) and \( \nR(x) \).* \( \nR \) is complete, and \( \nR(x) \) is not (@prp-cof-rational-functions-not-archimedean): completeness fails for one field of the pair. Separating statement: "some \( y \) satisfies \( n \cdot 1 < y \) for every \( n \in \nN \)", true in \( \nR(x) \), false in \( \nR \).

In both pairs the fields are ordered fields; Archimedes alone, as in the first pair, does not rescue the conclusion of @thm-cof-uniqueness.

**Marking scheme.** (10 points)
- 3: (a), \( \sigma(2) = 2 \) from additivity and \( \sigma(1) = 1 \), then \( \sigma(\sqrt 2)^2 = 2 \) and @thm-no-rational-square-two.
- 4: (b), Archimedes or completeness carried across the supposed isomorphism, either through \( \chi^{-1} \) (an order-preserving field map that fixes every \( n \cdot 1 \)) or through \( \chi \) and its surjectivity, with the reason \( \nR \) is complete and Archimedean, and the contradiction with @prp-cof-rational-functions-not-archimedean.
- 3: (c), the failing hypothesis named for each pair with its source, and a correct separating statement for each.
Fatal errors (0 for the step): in (a), assuming \( \sigma \) preserves order or is onto; in (b), assuming (rather than deriving from the supposed isomorphism) that \( \nR(x) \) is Archimedean, or asserting "\( \nR(x) \) is not complete, so not isomorphic" without showing that completeness or Archimedes is carried by the isomorphism.
:::

### R. Review

::: {#exr-axioms-or-model-r1}
[R1]

In the field \( \nR \) of classes of Cauchy sequences of rationals, for \( n \in \nN \) let \( k_n \) be the largest natural number \( k \) with \( k^2 \le 2 (2^n)^2 \), and let \( q_n \coloneqq k_n / 2^n \in \nQ \).

::: {.enumerate options="label=(\alph*)"}
1. Show that \( k_n \) exists and that \( 1 \le q_n < 2 \).
2. Show that \( (q_n) \in \sC \).
3. Show that \( [(q_n)]^2 = 2 \) in \( \nR \), and that \( [(q_n)] \) is the non-negative square root of \( 2 \) in \( \nR \).
:::
:::

::: {.solution}
This is the binary version of @exm-truncations-equivalent, and every estimate is in \( \nQ \). Here \( 2^n \) is the power \( (2 \cdot 1_{\nQ})^n \) of @def-naturals-in-ordered-field; by @prp-naturals-in-ordered-field (c), (d) it is the natural number \( 2^n \), and \( 2^n \ge n + 1 \ge 1 \) by @lem-power-two-bound with \( F = \nQ \). The first values are \( q_0, \dots, q_5 = 1, 1, 5/4, 11/8, 11/8, 45/32 \).

(a) Let \( S_n \coloneqq \{ m \in \nN : m^2 > 2 (2^n)^2 \} \). It is bounded below by \( 0 \), and non-empty: \( (2 \cdot 2^n)^2 = 4 (2^n)^2 > 2 (2^n)^2 \), as \( (2^n)^2 > 0 \). By @prp-integer-least-element it has a least element \( m^\ast \). Since \( 0 \notin S_n \), \( m^\ast \ge 1 \) by discreteness (@thm-integers-ordered-ring (c)), so \( k_n \coloneqq m^\ast - 1 \in \nN \). It is not in \( S_n \), so \( k_n^2 \le 2 (2^n)^2 \); and every natural \( k > k_n \) has \( k \ge m^\ast \), so \( k^2 \ge (m^\ast)^2 > 2 (2^n)^2 \) (@prp-ordered-ring-rules (g)). So \( k_n \) is the largest such \( k \), and it is unique. In particular
\[
\Bigl( q_n + \frac{1}{2^n} \Bigr)^2 = \frac{(k_n + 1)^2}{(2^n)^2} > 2 , \qquad q_n^2 \le 2 . \tag{$\ast$}
\]
Since \( k = 2^n \) has \( k^2 \le 2 (2^n)^2 \), \( k_n \ge 2^n \) and \( q_n \ge 1 \). Since \( q_n \ge 0 \) and \( q_n^2 \le 2 < 4 = 2^2 \), \( q_n < 2 \) (@prp-ordered-ring-rules (g)).

(b) *Monotone.* By \( 2^{n+1} = 2^n \cdot 2 \) (@def-naturals-in-ordered-field (b)), \( (2 k_n)^2 = 4 k_n^2 \le 8 (2^n)^2 = 2 (2^{n+1})^2 \), so \( 2 k_n \le k_{n+1} \) and \( q_{n+1} = k_{n+1}/2^{n+1} \ge 2k_n/(2^n \cdot 2) = q_n \). By @fd1:ax-induction (base \( P(0) \): \( q_n \le q_{n+0} \)), \( q_n \le q_{n+i} \) for every \( i \in \nN \), and every \( m \ge n \) is \( n + i \) for some \( i \) (@prp-omega-order-arithmetic (a)).

*A gap bound.* Let \( m \ge n \). If \( q_m \ge q_n + 1/2^n \), then, both sides being non-negative, \( q_m^2 \ge (q_n + 1/2^n)^2 > 2 \) by @prp-ordered-ring-rules (g) and \( (\ast) \), against \( q_m^2 \le 2 \). So, with @prp-reciprocal-order (b) and \( 2^n \ge n + 1 \),
\[
0 \le q_m - q_n < \frac{1}{2^n} \le \frac{1}{n + 1} \qquad (m \ge n) .
\]
*Cauchy.* Let \( \varepsilon \in \nQ_{>0} \). Since \( \nQ \) is Archimedean (@thm-rationals-archimedean), @prp-archimedean-reciprocal with \( F = \nQ \) gives \( N \in \nZ_{>0} \), depending on \( \varepsilon \), with \( 1/j < \varepsilon \) for every \( j \ge N \). For \( m, n \ge N \), say \( m \ge n \) (the other case is symmetric), \( \abs{q_m - q_n} < 1/(n + 1) < \varepsilon \), since \( n + 1 \ge N \). So \( (q_n) \in \sC \) (@def-rational-cauchy-sequences).

(c) Expanding \( (\ast) \), \( 2 < q_n^2 + 2q_n/2^n + 1/(2^n)^2 \). With \( q_n < 2 \) and \( 0 < 1/2^n \le 1 \),
\[
0 \le 2 - q_n^2 < \frac{1}{2^n} \Bigl( 2 q_n + \frac{1}{2^n} \Bigr) \le \frac{5}{2^n} \le \frac{5}{n + 1} .
\]
The sequence \( (1/(n + 1)) \) is null in \( \nQ \) (@exm-first-sequences-ordered-field (b)), so \( (5/(n + 1)) \) is null (@thm-limit-laws-ordered-field (b)). By the squeeze @prp-limit-preserves-order-ordered-field (c), between \( (0)_n \) and \( (5/(n + 1)) \), the sequence \( (2 - q_n^2) \) is null, and so is \( (q_n^2 - 2) \) (@thm-limit-laws-ordered-field (b), \( c = -1 \)). Both \( (q_n^2) \) and \( (2)_n \) are in \( \sC \) (@thm-cauchy-algebra-ordered-field (a), (c)), so \( (q_n^2) \sim (2)_n \) (@def-cauchy-equivalent), and by @def-reals-operations and @def-rational-embedding,
\[
[(q_n)]^2 = [(q_n^2)] = [(2)_n] = \kappa(2) ,
\]
which is \( 2 \) in \( \nR \) under the identification of \( q \) with \( \kappa(q) \).
Since \( q_n \ge 1 \) for every \( n \), @lem-termwise-order gives \( [(q_n)] \ge [(1)_n] = 1_{\nR} > 0 \). So \( [(q_n)] \) is a non-negative element of \( \nR \) whose square is \( 2 \). The element \( r \) of @exm-sqrt2-class is another, and \( \nR \) is complete (@thm-reals-complete-ordered-field), so the uniqueness in @prp-cof-square-roots gives \( [(q_n)] = r \): the binary truncations, the decimal truncations and the Newton sequence all name the same real number.
:::

::: {#exr-axioms-or-model-r2}
[R2]

Show that no relation \( < \) makes the field \( \nZ/5\nZ \) an ordered field. More generally, show that if \( F \) is a field in which \( n \cdot 1 = 0 \) for some \( n \in \nN \) with \( n \ge 1 \), then no relation makes \( F \) an ordered field.
:::

::: {.solution}
The general statement first. Suppose \( < \) makes \( F \) an ordered field (@def-ordered-ring-and-field). Since \( 1 \ne 0 \) in a field, @prp-ordered-ring-rules (h) gives \( n \cdot 1 > 0 \) for every \( n \ge 1 \). If \( n \cdot 1 = 0 \), this says \( 0 > 0 \), against (O1). So no such relation exists.

\( \nZ/5\nZ \) is a field because \( 5 \) is prime (@thm-integers-mod-prime-field), and \( 5 \cdot [1] = [5] = [0] \) by @thm-integers-mod-n-ring (d). The general statement with \( n = 5 \) applies. (For the ring, this is the case \( n = 5 \) of @thm-integers-mod-n-ring (e).) So \( \nZ/5\nZ \) satisfies every field axiom and admits no order, while \( \nQ \), \( \nQ(\sqrt 2) \) and \( \nR(x) \) admit one: the field axioms do not determine the order axioms.
:::

::: {#exr-axioms-or-model-r3}
[R3]

Let \( X \) be the complete ordered field of this section whose zero is \( \emptyset \), and let \( \mathcal S \coloneqq \{ \nQ, \nQ(\sqrt 2), \nR(x), \nR, X \} \), with \( \nR \) the Cauchy model. Isomorphism of ordered fields, \( \cong \), is an equivalence relation on \( \mathcal S \). Find its equivalence classes, and the number of elements of the quotient set \( \mathcal S/{\cong} \). For each two fields in different classes, name a property that one has and the other lacks, and prove that an order-preserving field isomorphism carries it across.
:::

::: {.solution}
By the remark after @cor-cof-isomorphic-to-cauchy-reals, \( \cong \) is an equivalence relation on \( \mathcal S \) (@fd2:def-equivalence-relation).

*Two transfer facts.* Let \( \chi \colon F \to L \) be an order-preserving field isomorphism. By the remark after @cor-cof-isomorphic-to-cauchy-reals, \( \chi^{-1} \colon L \to F \) is one too, so each fact below also holds with \( F \) and \( L \) exchanged. Recall \( \chi(n \cdot 1_F) = \chi(\iota_F(n)) = \iota_L(n) = n \cdot 1_L \) for \( n \in \nN \) (@prp-cof-map-fixes-rationals).

(i) *Square roots of \( n \cdot 1 \).* If \( b \in F \) has \( b^2 = n \cdot 1_F \), then \( \chi(b)^2 = \chi(b^2) = \chi(n \cdot 1_F) = n \cdot 1_L \), since \( \chi \) respects products. So if \( n \cdot 1 \) is a square in \( F \), it is a square in \( L \), and conversely.

(ii) *Archimedes.* Let \( F \) be Archimedean (@def-archimedean-ordered-field), and let \( y \in L \). Take \( n \in \nN \) with \( \chi^{-1}(y) < n \cdot 1_F \). Since \( \chi \) is strictly increasing, \( y = \chi(\chi^{-1}(y)) < \chi(n \cdot 1_F) = n \cdot 1_L \). So \( L \) is Archimedean, and conversely.

*The classes.* The map \( \beta \colon \nR \to X \) of this section is an order-preserving field isomorphism, so \( \nR \cong X \). The other pairs are not isomorphic:

- \( \nR(x) \) is not Archimedean (@prp-cof-rational-functions-not-archimedean), while \( \nQ \) (@thm-rationals-archimedean), \( \nQ(\sqrt 2) \) (@prp-cof-sqrt2-field-archimedean), \( \nR \) and \( X \) (complete, by @thm-reals-complete-ordered-field and by the construction of \( X \), hence Archimedean by @thm-cof-complete-archimedean) are. By (ii), \( \nR(x) \) is isomorphic to none of the four.
- \( 2 \) is not a square in \( \nQ \) (@thm-no-rational-square-two), while it is one in \( \nQ(\sqrt 2) \) (\( \sqrt 2 \in \nQ(\sqrt 2) \), @def-cof-sqrt2-field) and in the complete fields \( \nR \) and \( X \) (@prp-cof-square-roots). By (i) with \( n = 2 \), \( \nQ \) is isomorphic to none of these three.
- \( 3 \) is not a square in \( \nQ(\sqrt 2) \) (@prp-cof-sqrt2-field-incomplete), while it is one in \( \nR \) and \( X \) (@prp-cof-square-roots). By (i) with \( n = 3 \), \( \nQ(\sqrt 2) \not\cong \nR \) and \( \nQ(\sqrt 2) \not\cong X \).

So the equivalence classes (@fd2:def-equivalence-class), \( [K] = \{ K' \in \mathcal S : K' \cong K \} \), are \( \{ \nQ \} \), \( \{ \nQ(\sqrt 2) \} \), \( \{ \nR(x) \} \) and \( \{ \nR, X \} \), and the quotient set \( \mathcal S/{\cong} \) (@fd2:def-quotient-set) has four elements. The two complete fields share a class, as @thm-cof-uniqueness requires; the other three fall into three classes.
:::

::: {#exr-axioms-or-model-r4}
[R4]

Let \( F \) be a complete ordered field, and for \( n \in \nN \) write \( 10^{-n} \) for \( \bigl((10 \cdot 1_F)^n\bigr)^{-1} \). Prove that
\[
\sup \{ 1 - 10^{-n} : n \in \nN \} = 1 .
\]
:::

::: {.solution}
*The tool* is the Archimedean property of \( F \), which holds by @thm-cof-complete-archimedean, together with a lower bound for the powers \( (10 \cdot 1_F)^n \) of @def-naturals-in-ordered-field.

*The bound.* We show \( (10 \cdot 1_F)^n \ge (1 + 9n) \cdot 1_F \) for every \( n \in \nN \), by @fd1:ax-induction with base \( P(0) \): \( (10 \cdot 1_F)^0 = 1_F = (1 + 0) \cdot 1_F \). For the step, \( 10 \cdot 1_F > 0 \) (@prp-naturals-in-ordered-field (b)), so by @def-naturals-in-ordered-field (b), \( P(n) \), @prp-ordered-ring-rules (c) (or equality), and @prp-naturals-in-ordered-field (a), (b),
\[
\begin{aligned}
(10 \cdot 1_F)^{n+1} &= (10 \cdot 1_F)^n (10 \cdot 1_F) \ge \bigl((1 + 9n) \cdot 1_F\bigr)(10 \cdot 1_F) \\
&= (10 + 90n) \cdot 1_F \ge (10 + 9n) \cdot 1_F = \bigl(1 + 9(n + 1)\bigr) \cdot 1_F ,
\end{aligned}
\]
using \( 10 + 9n \le 10 + 90n \) in \( \nN \). In particular \( (10 \cdot 1_F)^n \ge 1_F > 0 \), so \( 10^{-n} \) is defined and positive (@prp-reciprocal-order (a)).

*Upper bound.* \( 10^{-n} > 0 \) gives \( 1 - 10^{-n} < 1 \) for every \( n \).

*Least.* Let \( b \in F \) with \( b < 1 \). Then \( 1 - b > 0 \), and @prp-archimedean-reciprocal gives \( N \in \nZ_{>0} \), depending on \( b \), with \( 1/(N \cdot 1_F) < 1 - b \). Since \( (10 \cdot 1_F)^N \ge (1 + 9N) \cdot 1_F \ge N \cdot 1_F > 0 \) (@prp-naturals-in-ordered-field (b)), @prp-reciprocal-order (b) (or equality) gives \( 10^{-N} \le 1/(N \cdot 1_F) < 1 - b \), so the element \( 1 - 10^{-N} \) of the set exceeds \( b \), and \( b \) is not an upper bound. By (O1), every upper bound is \( \ge 1 \). So the supremum is \( 1 \).

*Why the look-alike tools fail.* Reading \( 1 - 10^{-n} \) as \( 0.9 \), \( 0.99 \), \( \dots \) and summing a geometric series uses infinite decimals, which this volume never defined; and an argument by limits would need the limit of \( (10^{-n}) \), which is the same Archimedean estimate with more machinery. The estimate is also where Archimedes cannot be skipped: in the non-Archimedean \( \nR(x) \) of @def-cof-rational-functions, \( (10 \cdot 1)^n = (10^n) \cdot 1 \) (@prp-naturals-in-ordered-field (c)) lies below \( x \) for every \( n \) (@prp-cof-rational-functions-not-archimedean), so \( 10^{-n} > 1/x > 0 \) (@prp-reciprocal-order), and \( 1 - 1/x \) is an upper bound of the set that lies below \( 1 \).
:::

<!-- dependency ledger
sec-axioms-or-model (claim): an1 Chapter 1 assumes an ordered field containing Q with the least upper bound axiom, and proves N unbounded, Q dense, square roots; an1 does not cite fd3 | an1 Chapter 1 (prose pointer, read in an1/src/ch01-least-upper-bound/03, 05, 06); nothing depends on it
sec-axioms-or-model (claim): consistency of the complete-ordered-field axioms relative to the set theory of Chapter 1 | thm-reals-complete-ordered-field (cited); informal meta-argument in prose, nothing depends on it
sec-axioms-or-model (claim): in the cut model of Chapter 7 a real number is a set of rationals, and sqrt 2 is the set of rationals below it | F3.3 (optional chapter, prose pointer; blueprint ch07 def-dedekind-cut); illustration only, nothing depends on it
sec-axioms-or-model (claim): (P1)-(P6) for the isomorphism phi | inline, from def-cof-order-preserving-map, prp-cof-map-fixes-rationals, cor-cof-isomorphic-to-cauchy-reals remark (cited)
sec-axioms-or-model (claim): every statement in +, *, < (elements, subsets, sequences, functions) has the same truth value in F and L | not stated as a theorem; explained by pattern, instance proved (limits); nothing depends on it
sec-axioms-or-model (claim): transport of structure along a bijection beta gives a complete ordered field and beta is an isomorphism | inline
sec-axioms-or-model (claim): empty set is not an element of the Cauchy R (every class contains its representative) | inline, fd2 equivalence classes (def-reals-cauchy-classes recalled)
sec-axioms-or-model (claim): non-Archimedean ordered fields in which every positive element is a square and every odd-degree polynomial function has a zero exist (real closed fields) | not proved here; marked so in the text; nothing depends on it
exr-axioms-or-model-a1 (solution): (b + c)^2 = 5 + 2bc, bc = sqrt 6, 5 + 2 sqrt 6 > 9 iff 6 > 4 | inline; verify/ch06/exr-axioms-or-model-a1.py
exr-axioms-or-model-a1 (solution): composite of an injection and a bijection is an injection | fd2:thm-composition-injective-surjective (a); inline
exr-axioms-or-model-a1 (solution): the rational 0 is {(0, s) : s in Z_{>0}}, with more than two elements; a sequence N -> Q is the pair (G, Q), a set with at most two elements | def-rationals-as-classes, fd2:def-function, def-kuratowski-pair, thm-kuratowski-pair (cited)
exr-axioms-or-model-a1 (solution): a complete ordered field whose sqrt 2 contains the rational 0 | inline (transport construction of this section, with the argument of (a)(i)); the cut model of F3.3 mentioned in a parenthesis only
exr-axioms-or-model-a1 (solution): provable from the ordered-field axioms implies true in every ordered field | fd1:thm-first-order-soundness (cited; the axioms and the statement are first-order); inline
sec-axioms-or-model (claim): a statement proved from a list of axioms is true in every structure satisfying them | inline (a proof from the axioms is a proof about an arbitrary model; for first-order statements the formal version is fd1:thm-first-order-soundness); nothing depends on it
exr-axioms-or-model-r1 (solution): q_0..q_5 values; 2 - q^2 < (1/2^n)(2q + 1/2^n) <= 5/2^n; 4 k^2 <= 8 (2^n)^2 = 2 (2^{n+1})^2 | inline; verify/ch06/exr-axioms-or-model-r1.py
exr-axioms-or-model-r3 (solution): the inverse of an order-preserving field isomorphism is one | remark after cor-cof-isomorphic-to-cauchy-reals (cited; proved in the second-reading fold there)
exr-axioms-or-model-r3 (solution): chi(n 1_F) = n 1_L; a square equal to n 1 and the Archimedean property carry across an isomorphism | prp-cof-map-fixes-rationals (iota_F(n) = n 1_F); inline; verify/ch06/exr-axioms-or-model-r3.py
exr-axioms-or-model-r3 (solution): R = X up to isomorphism; R(x), Q, Q(sqrt 2) pairwise non-isomorphic and not isomorphic to R | transport construction of this section; prp-cof-rational-functions-not-archimedean, thm-rationals-archimedean, prp-cof-sqrt2-field-archimedean, thm-reals-complete-ordered-field, thm-cof-complete-archimedean, thm-no-rational-square-two, def-cof-sqrt2-field, prp-cof-square-roots, prp-cof-sqrt2-field-incomplete (cited)
exr-axioms-or-model-r4 (solution): (1 + 9n) * 10 = 10 + 90n, 1 + 9(n + 1) = 10 + 9n <= 10 + 90n in N | omega arithmetic (thm-omega-arithmetic-laws); verify/ch06/exr-axioms-or-model-r4.py
-->
