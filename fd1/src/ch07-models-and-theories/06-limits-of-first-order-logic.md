# What First-Order Logic Can and Cannot Say

This section is optional, and nothing outside it depends on it. Every theorem in it is **stated without proof**, except where a short argument from a stated theorem is given and marked as such; its results carry no optional marker of their own, and the section as a whole is the unit a reader may skip.

Section 7.4 asked of a theory two questions that sound different: is it consistent, that is, does no finite list of its axioms derive \( \bot \)? And has it a model? A model answers the first question (@prp-model-shows-consistency), but nothing so far says that a consistent theory must have one. This section states the theorem that says so, Gödel's completeness theorem, and then follows its consequences. The first is compactness: a theory has a model as soon as each finite part of it has one. From compactness come the surprises. A first-order theory cannot fix the size of its infinite models; the true sentences about \( \nN \) have a model with an element larger than every number; and the property "finite" cannot be written as a sentence. The section ends with what can and cannot be decided by a mechanical procedure, and names the incompleteness theorem, which is a different matter from completeness.

::: {.remark}
[Looking back]

Section 4.8 proved that every valid propositional claim is derivable, and the optional Section 4.10 proved compactness for propositional logic. Both hold for predicate logic too; this section states them, and then shows what they cost: a first-order language cannot pin down the natural numbers.
:::

## Completeness

The soundness statement of Section 7.2 runs from derivations to truth: whatever a list of premises derives is true in every structure where the premises are true. The completeness theorem runs back.

::: {#thm-first-order-completeness}
[Gödel's Completeness Theorem]

For every theory \( T \) and sentence \( \sigma \): \( T \vdash \sigma \) if and only if \( T \models \sigma \). Equivalently, a theory is consistent if and only if it has a model.
:::

This theorem is stated without proof. One direction is the soundness statement of Section 7.2; the other is new. Here \( T \vdash \sigma \) and \( T \models \sigma \) are those of @def-theory and @def-model-of-theory: some finite list of axioms derives \( \sigma \), and \( \sigma \) is true in every model of \( T \). The two forms say the same thing. Take \( \sigma = \bot \): \( T \vdash \bot \) says that \( T \) is inconsistent (@def-inconsistent-theory), and \( T \models \bot \) says that no model of \( T \) exists, since \( \bot \) is true in no structure. In the other direction, \( T \models \sigma \) means that the theory \( T \) with \( \neg\sigma \) added, the counterexample set of the claim, has no model; and \( T \vdash \sigma \) means that this theory is inconsistent, by \( \rulename{\neg E} \) in one direction and \( \rulename{RAA} \) in the other.

What the theorem means for this chapter is best said with its two halves side by side. Faced with a claim \( T \vdash \sigma \), Chapters 5 and 6 searched for a derivation, and this chapter searched for a counter-model, a model of \( T \) in which \( \sigma \) is false. Soundness says that both cannot succeed. Completeness says that one of them must: a stalled derivation search and a missing counter-model cannot both be real. The words "consistent" and "has a model", which Section 7.4 kept apart and never swapped, are now known to coincide, but only here, and with a theorem stated and not proved. Nothing outside this section uses the coincidence.

Section 7.4's group axioms show both outcomes. They derive that the identity is unique (@prp-group-identity-unique), and that settles one claim by a derivation. They do not derive (Comm), and the triangle group of @exm-triangle-group, a model of the axioms in which (Comm) is false, settles that claim by a counter-model. Completeness says that every claim about groups is settled in one of these two ways, though it does not say which, or how long the search for either will take.

The theorem says nothing about how to find the derivation or the model, and the last part of this section explains why no method finds one of them in every case.

::: {.second-reading title="How the proof goes: a model made of names"}
This is a sketch, not a proof. It follows the route of Section 4.10's proof of propositional compactness through Lindenbaum's lemma (@lem-lindenbaum).

Start from a consistent theory \( T \); we want a model. The idea is to build the model out of the language itself, with the closed terms as its elements. Two difficulties arise, and each has a remedy.

*Witnesses.* A sentence \( \exists x\, \varphi \) of the theory may hold with no closed term to show for it. So add new constants, and for each sentence \( \exists x\, \varphi \) a **witness axiom** \( \exists x\, \varphi \to \varphi[c/x] \), with \( c \) a constant new to everything so far. Adding it keeps the theory consistent, for the same reason the name in an \( \rulename{\exists E} \) box must be fresh: an old name already carries information, and a new one carries none, so assuming that it names a witness can lead to no contradiction that the bare \( \exists x\, \varphi \) did not already give. This is repeated, since the new constants make new sentences, each with its own witness.

*Deciding every sentence.* A consistent theory may leave a sentence undecided, and a structure cannot. So extend the theory, one sentence at a time, to a **maximal** consistent set: list all sentences, and add each one if the result stays consistent. As in Lindenbaum's lemma, the result decides every sentence, containing it or its negation.

*The structure.* Its elements are the closed terms, with two terms identified when the set contains their equation; a constant names itself, a function symbol builds the longer term, and a predicate holds of the terms for which the set says it holds. An induction on sentences, the propositional one of Section 4.10 with a case for each quantifier, where the witness axioms do their work, shows that this structure satisfies exactly the sentences of the set. It satisfies \( T \) in particular.

The details, for countably many symbols, fill a chapter of a logic text; this book stops at the outline.
:::

## Compactness

Completeness ties models to derivations, and a derivation uses only finitely many premises. That one fact has a consequence about models alone.

::: {#thm-first-order-compactness}
[Compactness Theorem]

If every finite subset of a theory \( T \) has a model, then \( T \) has a model.
:::

*A short argument from completeness.* Suppose \( T \) had no model. Then \( T \) is inconsistent, by @thm-first-order-completeness, so some finite list of its axioms derives \( \bot \) (@def-inconsistent-theory). The finite subset made of those axioms is then itself an inconsistent theory, so by @prp-model-shows-consistency it has no model, against the hypothesis.

::: {.warning}
"Every finite subset has a model" is not "has a finite model". The finite subsets are finite lists of **axioms**; the models that satisfy them may be infinite, and the model the theorem gives may be infinite even when every finite subset has a finite model. Compactness never makes a structure smaller.
:::

Read the theorem from the side of what a theory forbids. A structure fails to be a model of \( T \) when some axiom is false in it. The theorem says that a property needing infinitely many axioms at once to fail is never enforced by first-order sentences: whatever a theory forbids, some finite part of it already forbids. That is the source of everything below.

The standard tool is a list of sentences that count. For \( n \ge 2 \), let \( \sigma_n \) be the sentence "there are at least \( n \) elements": \( n \) variables bound by \( \exists \), followed by the conjunction of \( \neg(x_i = x_j) \) for all \( i < j \). It is true in a structure exactly when the domain has \( n \) or more elements. Any finite set of the \( \sigma_n \) is true in a large enough finite structure; all of them together are true only in an infinite one. Every use of compactness below follows one pattern: add infinitely many axioms that no single intended structure satisfies all at once, check that each finite part of the result has a model, and conclude that the whole has one. The model it gives is then a new structure, with properties the intended ones lack.

::: {.check}
Let \( \sigma_n \) say "there are at least \( n \) elements". Write \( \sigma_3 \).
:::

::: {.solution}
\( \exists x\, \exists y\, \exists z\, \bigl( \neg(x = y) \wedge \neg(x = z) \wedge \neg(y = z) \bigr) \).
:::

::: {.check}
Does compactness hold for propositional logic?
:::

::: {.solution}
Yes: the optional Section 4.10 proved it; this section states the first-order version.
:::

## Large models and small ones

A set can be **listed** if its elements can be written as a sequence \( d_0, d_1, d_2, \dots \) in which every element appears; \( \nN \), \( \nZ \) and \( \nQ \) can, and every finite set can. "Listed" here has its everyday meaning.

::: {#thm-lowenheim-skolem}
[Löwenheim–Skolem Theorem]

Let \( T \) be a theory in countably many symbols (the symbols can be listed \( s_0, s_1, s_2, \dots \)). If \( T \) has an infinite model, then it has a model whose domain can be listed as \( d_0, d_1, d_2, \dots \), and also a model whose domain cannot be so listed.
:::

This theorem is stated without proof. Two consequences show its force. First, take for \( T \) all the sentences true in \( (\nR; 0, 1, +, \cdot, <) \). The theorem gives a structure that satisfies every one of them and whose elements can be listed, although the elements of \( \nR \) cannot be (a fact stated here, not proved). Every first-order property of the real numbers holds in that structure, so the property that separates \( \nR \) from a listable set is not first-order. Second, take for \( T \) the sentences true in \( (\nN; 0, S, +, \cdot, <) \), with \( S \) the successor. The theorem gives a model of all of them that cannot be listed: far too large to be \( \nN \) under other names.

So no first-order theory with an infinite model fixes the size of its models. Section 7.5 showed that isomorphic structures satisfy the same sentences; here are structures that satisfy the same sentences and are not isomorphic, since one can be listed and the other cannot.

How can a listable structure satisfy every first-order sentence true in \( \nR \), when \( \nR \) is "complete": every non-empty set of reals bounded above has a supremum? The answer is the one the next two subsections give for \( \nN \). Completeness of \( \nR \) speaks of **all** sets of reals. A first-order sentence can speak only of sets defined by formulas (Section 7.5): for each formula there is a sentence "if the set this formula defines is non-empty and bounded above, it has a supremum", and each of these is true in \( \nR \). The listable model satisfies all of them, and fails the statement about all sets, which is not a first-order sentence.

::: {.check}
A theory \( T \) in countably many symbols has the model \( (\nQ, <) \). Must it also have a model whose domain cannot be listed?
:::

::: {.solution}
Yes: \( (\nQ, <) \) is an infinite model, so by @thm-lowenheim-skolem \( T \) also has a model that cannot be listed. For the strict order axioms, \( (\nR, <) \) is one.
:::

## Numbers that are not numerals

The symbols of arithmetic are \( 0 \), the one-place \( S \) for successor, \( + \), \( \cdot \) and \( < \), read in \( \nN \) as usual. The **numeral** \( \underline{n} \) is the closed term \( S(S(\cdots S(0) \cdots)) \) with \( n \) letters \( S \); its value in \( \nN \) is \( n \).

::: {#exm-non-standard-naturals}
[A Model of Arithmetic with an Infinite Number]

Let \( T \) be the set of all sentences in \( 0, S, +, \cdot, < \) that are true in \( \nN \). Add a new constant \( c \), and to \( T \) add the axioms
\[
\underline{0} < c, \quad \underline{1} < c, \quad \underline{2} < c, \quad \dots ,
\]
one for each \( n \in \nN \). Call the result \( T' \).

*Every finite subset of \( T' \) has a model.* A finite subset contains finitely many sentences of \( T \) and finitely many axioms \( \underline{n} < c \); let \( N \) be the largest \( n \) among them. Read the symbols in \( \nN \) as usual and \( c \) as \( N + 1 \). The sentences of \( T \) do not mention \( c \), and they are true in \( \nN \); each \( \underline{n} < c \) in the subset says \( n < N + 1 \), which is true.

*So \( T' \) has a model.* By @thm-first-order-compactness there is a structure \( \fM \) in which every sentence of \( T' \) is true. In \( \fM \) every sentence true in \( \nN \) is true, and \( c^{\fM} \) is above the value in \( \fM \) of every numeral. It differs from each of them: if \( c^{\fM} \) were the value of \( \underline{n} \), the axiom \( \underline{n} < c \) would put an element below itself, while \( \forall x\, \neg(x < x) \) is true in \( \nN \), so in \( T \), so in \( \fM \).
:::

An element of \( \fM \) that is the value of no numeral is called **non-standard**; the values of numerals are the **standard** elements. \( \fM \) satisfies every first-order sentence that \( \nN \) satisfies, and still has an element that no numeral names. Its standard elements lie at the bottom: the sentences \( \forall x\, (x < \underline{n + 1} \to x = \underline{0} \vee \dots \vee x = \underline{n}) \), one for each \( n \), are true in \( \nN \) and so in \( \fM \), and they say that nothing non-standard lies below a standard element.

The model \( \fM \) is not \( \nN \) under another name. In \( \nN \) itself, read as usual, no value of \( c \) works for the whole of \( T' \): if \( c \) is read as the number \( n \), the axiom \( \underline{n} < c \) says \( n < n \). Each finite part of \( T' \) is satisfied by \( \nN \), each with its own value for \( c \); the whole set is satisfied only by a structure that compactness supplies, and that structure has elements \( \nN \) lacks. Since \( \fM \) satisfies the same sentences in \( 0, S, +, \cdot, < \) as \( \nN \), no first-order sentence about arithmetic can tell the two apart; yet they are not isomorphic, since an isomorphism would send each numeral's value to the same numeral's value, and \( c^{\fM} \) to an element of \( \nN \) above every number, and there is none.

::: {.check}
Is \( c^{\fM} = S^{\fM}(d) \) for some element \( d \) of \( \fM \)?
:::

::: {.solution}
Yes. The sentence \( \forall x\, (\neg(x = 0) \to \exists y\, (S(y) = x)) \) is true in \( \nN \), so it is true in \( \fM \); and \( c^{\fM} \ne 0^{\fM} \), since \( \underline{0} < c \) is an axiom and \( \forall x\, \neg(x < x) \) holds in \( \fM \).
:::

## Induction: a schema and an axiom

How can \( \fM \) satisfy induction, when its standard elements contain \( 0 \), are closed under successor, and are not everything? The answer turns on what first-order induction says.

The **induction schema** of first-order arithmetic is one sentence for each formula \( \varphi \) with free variable \( x \):
\[
\bigl( \varphi[0/x] \wedge \forall x\, (\varphi \to \varphi[S(x)/x]) \bigr) \to \forall x\, \varphi ,
\]
with its other free variables, if any, bound by \( \forall \) in front. Each instance is true in \( \nN \), by induction, so each is in \( T \) and true in the model \( \fM \) of @exm-non-standard-naturals. Yet the set of standard elements of \( \fM \) contains \( 0^{\fM} \) and is closed under \( S^{\fM} \), and is not all of the domain. There is no contradiction: the schema speaks only about sets **defined by formulas** (Section 7.5), and the standard elements are not such a set.

The argument is short. Suppose a formula \( \varphi \) with free variable \( x \) defined the standard elements in \( \fM \). By @lem-term-substitution (Section 7.3; \( 0 \) is closed, and \( S(x) \) is free for \( x \) in \( \varphi \)), \( \varphi[0/x] \) holds in \( \fM \) exactly when \( \varphi \) holds of \( 0^{\fM} \), and \( \varphi[S(x)/x] \) holds under an assignment \( \ell \) exactly when \( \varphi \) holds of \( S^{\fM}(\ell(x)) \). Then \( \varphi[0/x] \) holds in \( \fM \), since \( 0^{\fM} \) is standard, and \( \forall x\, (\varphi \to \varphi[S(x)/x]) \) holds, since the successor of a standard element is standard. The induction instance for \( \varphi \) is a sentence true in \( \nN \), so it is in \( T \) and true in \( \fM \); it gives \( \forall x\, \varphi \) in \( \fM \), so every element would be standard, against \( c^{\fM} \). (Exercise C2 reaches the same conclusion another way, by least elements.)

The induction principle of Section 4.2 (@ax-induction) is stated for **every** property of natural numbers. Read in a structure, that is a statement about all subsets of the domain, not only the definable ones: it quantifies over sets, and is a **second-order** statement. Applied to the set of standard elements, it would rule out non-standard elements at once, and so a structure satisfying it, with \( 0 \) and successor read as usual, has no room for \( c^{\fM} \). First-order logic can state the schema, not the axiom; compactness is the price of its completeness.

## What can be decided

A question about sentences is **decidable** if a mechanical procedure answers it, correctly and in finitely many steps, for every sentence. Three facts, each stated without proof here, mark the boundary.

::: {.remark}
**Decidable: propositional logic.** Chapter 4's search tree decides every propositional claim in finitely many steps (@prp-search-decides): it either closes, and the claim is valid, or it leaves an open branch, which gives a refuting row.
:::

::: {.remark}
**Undecidable: predicate logic (Church and Turing, 1936).** No mechanical procedure decides, for every first-order sentence, whether it is derivable. With completeness, the boundary can be said exactly: listing all derivations, shortest first, finds one when one exists; what no procedure can do is announce, in every case, that none exists. A stalled search, the situation of Chapter 6, is the normal state of affairs and not a sign that more cleverness was needed.
:::

::: {.remark}
**Decidable: the monadic fragment.** For sentences with only one-place predicate symbols and no constants, function symbols or \( = \), the bound of Section 7.2's remark makes the counter-model search finite: if such a sentence has a counter-model at all, it has one of bounded size, and there are finitely many structures of each size to try.
:::

::: {.remark}
**Incompleteness, named.** Gödel showed in 1931 that no consistent theory whose axioms a mechanical procedure can list, and which derives the basic facts of arithmetic, derives every sentence true in \( \nN \). Completeness says every sentence true in **all** models of a theory is derivable from it; incompleteness says that the sentences true in **the** intended model \( \nN \) are not all true in all models of any such theory. The two theorems do not conflict: the non-standard models are where they part.
:::

::: {.check}
A sentence \( \sigma \) is true in \( \nN \) and false in some model of a theory \( T \) of arithmetic. Can \( T \vdash \sigma \)?
:::

::: {.solution}
No: by the soundness statement of Section 7.2, \( T \vdash \sigma \) would make \( \sigma \) true in every model of \( T \).
:::

::: {.remark}
[Looking ahead]

*Number Systems: From \(\nN\) to \(\nR\)*, Chapter 1, takes the second-order induction principle as clause (P5) of a Peano system and proves that any two Peano systems are isomorphic; this section explains why no first-order list of axioms could do the same.
:::

## Exercises

### A. Check your understanding

::: {#exr-limits-of-first-order-logic-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State @thm-first-order-completeness in its two forms.
2. State @thm-first-order-compactness, and give the short argument from completeness in three sentences.
3. What is a non-standard element of a model of arithmetic?
4. Why does the induction schema not rule non-standard elements out?
5. Name one decidable and one undecidable question about sentences.
:::
:::

::: {.solution}
*(a)* For every theory \( T \) and sentence \( \sigma \), \( T \vdash \sigma \) if and only if \( T \models \sigma \). Equivalently, a theory is consistent if and only if it has a model.

*(b)* If every finite subset of \( T \) has a model, so has \( T \). If \( T \) had no model, it would be inconsistent by completeness, so a finite list of its axioms would derive \( \bot \). That finite subset would be inconsistent, and so, by @prp-model-shows-consistency, without a model, against the hypothesis.

*(c)* An element that is not the value of any numeral \( \underline{n} \).

*(d)* Each instance speaks of a set defined by a formula, and the standard elements are not such a set (the argument in "Induction: a schema and an axiom").

*(e)* Decidable: validity of a propositional claim (or of a monadic sentence). Undecidable: derivability of a first-order sentence.
:::

::: {#exr-limits-of-first-order-logic-a2}
[A2: Drill]

Each part takes a line or two. The parts run from writing a counting sentence, through naming the theorem that answers a question, to judging what a theorem does and does not say.

::: {.enumerate options="label=(\alph*)"}
1. Write \( \sigma_2 \), "there are at least two elements".
2. Write "there are at most two elements".
3. Which theorem says "every consistent theory has a model"?
4. Which says "if every finite part of \( T \) has a model, \( T \) has one"?
5. True or false: completeness says that every sentence true in \( (\nN; 0, S, +, \cdot, <) \) is derivable with no premises.
6. True or false: a theory with models of every finite size has an infinite model.
7. Is "the domain is finite" expressible by one sentence?
8. True or false: in a model of all sentences true in \( \nN \), every element is the value of a numeral.
9. Over what does the second-order induction principle quantify that the schema does not?
10. Is derivability of a propositional claim decidable? Of a monadic first-order sentence (one-place predicate symbols only; no constants, function symbols or \( = \))? Of a first-order sentence in general?
11. Does \( (\nR; 0, 1, +, \cdot, <) \) have a model of the same sentences whose domain can be listed?
12. Why is a theory whose models are exactly the structures of size \( 3 \) possible, and one whose models are exactly the finite structures not?
:::
:::

::: {.solution}
(a) \( \exists x\, \exists y\, \neg(x = y) \).

(b) \( \forall x\, \forall y\, \forall z\, (x = y \vee x = z \vee y = z) \).

(c) Completeness, in its second form.

(d) Compactness.

(e) False: with no premises, completeness makes derivable only the sentences true in **every** structure. \( \forall x\, \neg(S(x) = 0) \) is true in \( \nN \) and false in a one-element structure (Section 7.2).

(f) True, by compactness, as in B1.

(g) No (C1).

(h) False: @exm-non-standard-naturals gives such a model with a non-standard element.

(i) All sets (properties) of elements, not only those defined by formulas.

(j) Yes; yes; no.

(k) Yes, by @thm-lowenheim-skolem.

(l) "At least \( 3 \) and at most \( 3 \) elements" is one sentence, \( \sigma_3 \) with the "at most" sentence. "Finite" would contradict compactness (C1).
:::

### B. Practice

::: {#exr-limits-of-first-order-logic-b1}
[B1: Arbitrarily large finite models]

Prove: if a theory \( T \) has, for every \( n \), a finite model with at least \( n \) elements, then \( T \) has an infinite model. Apply it to the theory of an equivalence relation \( R \) in which every class has exactly two elements, with that last condition written as one sentence.
:::

::: {.solution}
Let \( T' \) be \( T \) with every \( \sigma_n \), \( n \ge 2 \), added. A finite subset of \( T' \) contains only finitely many \( \sigma_n \); let \( N \) be the largest such \( n \) (or \( 2 \) if there is none). By hypothesis \( T \) has a finite model with at least \( N \) elements, and it satisfies every \( \sigma_n \) with \( n \le N \), so it is a model of the finite subset. By @thm-first-order-compactness \( T' \) has a model. It satisfies every \( \sigma_n \), so it has at least \( n \) elements for every \( n \): it is infinite. And it is a model of \( T \).

Application. The axioms are (Refl), (Sym), (Trans) for \( R \) and
\[
\forall x\, \exists y\, \bigl( \neg(x = y) \wedge R(x, y) \wedge \forall z\, (R(x, z) \to (z = x \vee z = y)) \bigr) ,
\]
"each \( x \) is related to exactly one element besides itself". For each \( k \ge 1 \), a set of \( 2k \) elements split into \( k \) pairs, with \( R \) "in the same pair", is a model, so there are models with at least \( n \) elements for every \( n \). So an infinite model exists; \( \nZ \) with \( R(x, y) \) read as \( \floor{x/2} = \floor{y/2} \), which pairs \( 2m \) with \( 2m + 1 \), is one.

**Marking scheme.** (10 points) 3 for \( T' \) defined with the \( \sigma_n \). 3 for every finite subset having a model, with the size argument. 2 for compactness applied and the model shown infinite. 2 for the application's sentence and models. Fatal error (0 for the proof): applying compactness to \( T' \) without checking its finite subsets.
:::

::: {#exr-limits-of-first-order-logic-b2}
[B2: Which theorem settles it?]

For each question, say which statement of this section or of Section 7.2 settles it, and answer it.

::: {.enumerate options="label=(\roman*)"}
1. \( \models \sigma \) is known. Is \( \vdash \sigma \)?
2. \( T \nvdash \bot \). Has \( T \) a model?
3. \( \sigma \) is true in every finite structure. Is \( \sigma \) valid?
4. Is there a structure satisfying every sentence true in \( \nN \), with an element above the value of every numeral?
5. Is there a procedure that decides validity for sentences built from one-place predicate symbols only (no constants, function symbols or \( = \))?
:::
:::

::: {.solution}
(i) Completeness: yes.

(ii) Completeness, second form: yes.

(iii) No theorem makes it so, and it need not be: the sentence of @exr-models-c1 is true in every finite structure and false in \( \nN \) with \( f \) read as the successor, so it is not valid.

(iv) Compactness: yes (@exm-non-standard-naturals).

(v) The monadic remark: yes.

**Marking scheme.** (10 points) 2 for each part: 1 for the statement named, 1 for the answer. Fatal error (0 for (iii)): answering "yes, by completeness".
:::

### C. Going deeper

::: {#exr-limits-of-first-order-logic-c1}
[C1: "Finite" is not first-order]

Prove that no sentence \( \varphi \) is true in exactly the finite structures for its symbols.
:::

::: {.solution}
[Hint 1]

Use @exr-limits-of-first-order-logic-b1.
:::

::: {.solution}
[Hint 2]

Suppose \( \varphi \) were one, and consider the theory \( T = \{ \varphi \} \).
:::

::: {.solution}
Suppose \( \varphi \) is true in every finite structure for its symbols and in no infinite one. For each \( n \ge 1 \) there is a structure of size \( n \) for the symbols of \( \varphi \): take any \( n \)-element set, read each constant as one fixed element \( a \) of it, each function symbol as the function with the constant value \( a \), and each predicate symbol as the empty relation. It is finite, so \( \varphi \) is true in it. So \( T = \{ \varphi \} \) has finite models of every size, and by @exr-limits-of-first-order-logic-b1 it has an infinite model, in which \( \varphi \) is true: a contradiction.

**Marking scheme.** (10 points) 3 for the supposition stated precisely. 4 for models of every finite size exhibited. 3 for B1 (or compactness directly) applied, and the contradiction named. Fatal error (0 for the proof): a "proof" that only shows that one particular sentence fails.
:::

::: {#exr-limits-of-first-order-logic-c2}
[C2: Challenge: least elements in a non-standard model]

Let \( \fM \) be the model of @exm-non-standard-naturals.

::: {.enumerate options="label=(\alph*)"}
1. For a formula \( \psi \) with free variable \( x \), write a sentence saying "if some element satisfies \( \psi \), some least element satisfies \( \psi \)", and explain why it is true in \( \fM \).
2. Take \( \psi = \neg\varphi \), where \( \varphi \) is a formula supposed to define the standard elements in \( \fM \). The sentence of (a) then names a least non-standard element \( e \). Choose an element below \( e \) that is also non-standard, and conclude, without using the induction argument of this section, that no such \( \varphi \) exists.
:::
:::

::: {.solution}
*(a)* Rename the bound variables of \( \psi \) so that \( y \) does not occur in \( \psi \); then \( y \) is free for \( x \) in \( \psi \). The sentence is
\[
\exists x\, \psi \to \exists x\, \bigl( \psi \wedge \forall y\, (y < x \to \neg\psi[y/x]) \bigr) ,
\]
with any other free variables of \( \psi \) bound by \( \forall \) in front. By @lem-term-substitution (Section 7.3; \( y \) is free for \( x \)), \( \neg\psi[y/x] \) is satisfied under \( \ell \) exactly when \( \psi \) fails of \( \ell(y) \), so the sentence says what (a) asks, in \( \nN \) and in \( \fM \) alike. It is true in \( \nN \) by the least-number principle (every non-empty set of natural numbers has a least element), whatever set \( \psi \) defines there. So it belongs to \( T \), and it is true in \( \fM \).

*(b)* \( \neg\varphi \) is satisfied by \( c^{\fM} \), which is non-standard, so (a) gives a least \( e \) satisfying \( \neg\varphi \): a least non-standard element. \( e \ne 0^{\fM} \), since \( 0^{\fM} \) is standard; and \( \forall x\, (\neg(x = 0) \to \exists y\, (S(y) = x)) \) is true in \( \nN \), so in \( \fM \). Choose \( d \) with \( S^{\fM}(d) = e \). Then \( d < e \) in \( \fM \), since \( \forall y\, (y < S(y)) \) is true in \( \nN \). And \( d \) is non-standard: if \( d \) were the value of \( \underline{n} \), then \( e = S^{\fM}(d) \) would be the value of \( \underline{n + 1} \). So \( d \) satisfies \( \neg\varphi \) and lies below \( e \), against the choice of \( e \).

**Marking scheme.** (10 points) 4 for (a): the sentence, with the renaming that makes \( y \) free for \( x \) and the reading of \( \neg\psi[y/x] \) by @lem-term-substitution, its truth in \( \nN \) by the least-number principle, and the transfer to \( \fM \) through \( T \). 4 for (b): the predecessor \( d \) obtained from a sentence true in \( \nN \), with \( d < e \) and \( d \) non-standard both argued. 2 for the contradiction named. Fatal error (0 for (a)): the least-number principle used for an arbitrary subset of \( \fM \) rather than through a sentence of \( T \).
:::

<!-- dependency ledger
thm-first-order-completeness (claim): Godel's completeness theorem | stated without proof, marked; nothing outside the section depends on it
thm-first-order-completeness (claim): the two forms are equivalent (sigma = bot; T with not-sigma added) | inline; def-theory, def-model-of-theory, def-inconsistent-theory (cited); S3 of def-satisfaction for bot
thm-first-order-completeness (claim): T |- sigma iff T with not-sigma added is inconsistent | not-E and RAA (def-rules-negation, def-rule-raa, Chapters 1-2), inline
thm-first-order-completeness (proof): the Henkin sketch, witness axioms consistent to add, Lindenbaum extension, term model | a sketch, marked "not a proof"; nothing rests on it; lem-lindenbaum (F1.3 §10, cited) for the route
thm-first-order-thm-first-order-compactness (claim): compactness for first-order theories | short argument from thm-first-order-completeness, inline and marked; prp-model-shows-consistency, def-inconsistent-theory (cited)
thm-first-order-compactness (claim): sigma_n is true exactly in structures with at least n elements | (S2), (S4), (S5), (S7) of def-satisfaction; verify/ch07/exr-limits-of-first-order-logic-a2.py (sizes 1-4)
thm-lowenheim-skolem (claim): downward and upward Lowenheim-Skolem for countably many symbols | stated without proof, marked; nothing outside the section depends on it
thm-lowenheim-skolem (claim): R cannot be listed | stated, not proved; F2.3 (promised)
thm-lowenheim-skolem (claim): N, Z, Q and finite sets can be listed | everyday listing; F2.3 (promised), prose only
exm-non-standard-naturals (example): every finite subset of T' is modelled by N with c read as N + 1; c differs from every numeral | inline; thm-first-order-compactness (cited)
exm-non-standard-naturals (claim): the sentences forall x (x < n+1 -> x = 0 or ... or x = n) are true in N | school arithmetic of N
exm-non-standard-naturals (solution): Quick check, every non-zero natural number is a successor | school arithmetic of N
exm-non-standard-naturals (claim): each instance of the induction schema is true in N | ax-induction (F1.3 §02), applied to the property defined by phi in N
exm-non-standard-naturals (claim): phi[0/x] and phi[S(x)/x] read in M; S(x) free for x in phi | lem-term-substitution (F1.6 §03, optional, cited by name; this section is optional too)
exm-non-standard-naturals (claim): no formula defines the standard elements of M | inline argument from the schema instance
thm-first-order-completeness (claim): What can be decided, propositional validity decidable | prp-search-decides (F1.3 §06, cited)
thm-first-order-completeness (claim): What can be decided, Church-Turing undecidability of first-order derivability; listing derivations finds one when one exists | stated without proof, marked; nothing depends on it
thm-first-order-completeness (claim): What can be decided, monadic sentences without constants, function symbols or = decidable via the bound of 7.2's remark | stated without proof here; the bound is F1.6 §02's remark (stated there)
thm-first-order-completeness (claim): What can be decided, Godel's incompleteness theorem (1931) | named, stated without proof; nothing depends on it
exm-non-standard-naturals (claim): Looking ahead, (P5) and categoricity of Peano systems | F3.1 def-peano-system, thm-peano-categoricity (exist; Looking ahead only)
exr-limits-of-first-order-logic-a2 (solution): the sentences of (a), (b) on structures of sizes 1-4 | verify/ch07/exr-limits-of-first-order-logic-a2.py
exr-limits-of-first-order-logic-a2 (solution): forall x not(S(x) = 0) false in a one-element structure | F1.6 §02 (the three classes of sentences, in-chapter)
exr-limits-of-first-order-logic-b1 (solution): the pairing structures of even size are models; floor(x/2) = floor(y/2) on Z | verify/ch07/exr-limits-of-first-order-logic-b1.py (sizes 2-8; Z on a window)
exr-limits-of-first-order-logic-b2 (solution): (iii) the sentence of exr-models-c1 | exr-models-c1 (F1.6 §02, cited)
exr-limits-of-first-order-logic-c1 (solution): a structure of each finite size exists for any symbols | inline (constant functions, empty relations)
exr-limits-of-first-order-logic-c2 (solution): the least-number principle in N | F2.2 well-ordering (promised), as in F1.3 §02
exr-limits-of-first-order-logic-c2 (solution): reading of not-psi[y/x] in M | lem-term-substitution (F1.6 §03, optional, cited)
exr-limits-of-first-order-logic-c2 (solution): forall y (y < S(y)) and every non-zero element a successor are true in N | school arithmetic of N
-->
