# Compactness and Maximal Consistent Sets

This section is optional, and nothing outside it depends on it.

Every list of premises in this chapter has been finite, and the proof of completeness needed that: its Step 1 lists the atoms of \( \Gamma \) and \( \psi \), and there are only finitely many of them because \( \Gamma \) is a finite list (@thm-completeness). But a statement about infinitely many objects can come with infinitely many premises. Give each \( n \ge 1 \) an atom \( p_n \), read "the \( n \)-th lamp is on", and the rules "the first lamp is on" and "if the \( n \)-th lamp is on, so is the next" are one premise for each \( n \). This section defines \( \vdash \) and \( \models \) for such collections of premises, proves completeness for them by a route different from that of Section 4.8, and deduces from it the compactness theorem: a collection of formulas can be made true all at once as soon as each finite part of it can. The word "collection" keeps its everyday sense throughout; nothing here needs more.

## Infinitely many premises

*A derivation is finite, so from infinitely many premises it can use only finitely many; a valuation, on the other hand, gives every formula a value at once.*

::: {#def-infinite-entailment}
[Derivability and Entailment from Infinitely Many Premises]

Let \( \Gamma \) be a collection of formulas, finite or infinite, and \( \psi \) a formula. \( \Gamma \vdash \psi \) if \( \psi \) is derivable from some finite list of members of \( \Gamma \); \( \Gamma \) is **consistent** if \( \Gamma \nvdash \bot \). \( \Gamma \models \psi \) if every valuation that makes every member of \( \Gamma \) true makes \( \psi \) true; \( \Gamma \) is **satisfiable** if some valuation makes every member of \( \Gamma \) true.
:::

In words: a derivation has finitely many lines, so it can cite only finitely many premises. That is why \( \vdash \) goes through finite lists of members, while \( \models \) looks at all of \( \Gamma \) at once. For a finite list the new definitions agree with the old. A derivation from part of a list is a derivation from the list, by @lem-weakening-cut (a), so \( \vdash \) means what @def-derivable said, and *consistent* means what @def-inconsistent-set said. The definitions of \( \models \) and *satisfiable* say for a finite list exactly what @def-valid-argument and @def-satisfiable said. "Finite list of members" allows repetitions and any order; neither matters, by @lem-weakening-cut (a) and by the definitions of \( \models \) and *satisfiable*.

An example. Let \( \Gamma \) consist of \( p_1 \) and every formula \( p_n \to p_{n+1} \) with \( n \ge 1 \). Then \( \Gamma \vdash p_3 \): from the finite list \( p_1, \ p_1 \to p_2, \ p_2 \to p_3 \), two \( \rulename{{\to}E} \) lines give \( p_2 \) and then \( p_3 \). And \( \Gamma \models p_n \) for every \( n \ge 1 \): a valuation making every member of \( \Gamma \) true makes \( p_1 \) true, and makes \( p_{n+1} \) true whenever it makes \( p_n \) true, so it makes every \( p_n \) true, by @ax-induction on \( n \), started at \( 1 \).

::: {.check}
Is the collection consisting of \( p_1 \vee p_2 \) and every \( \neg p_n \) with \( n \ge 2 \) satisfiable? Is it consistent?
:::

::: {.solution}
Satisfiable: the valuation making \( p_1 \) true and every other atom false makes every member true. Hence consistent. A derivation of \( \bot \) would use some finite list of members; that list is made true by the same valuation, so it is satisfiable, hence consistent by Section 4.7, and derives no \( \bot \).
:::

## Listing all formulas

The construction below goes through all formulas one at a time, so it needs them in one list.

::: {#lem-formula-enumeration}
[The Formulas Can Be Listed]

There is a list \( \varphi_0, \varphi_1, \varphi_2, \dots \) of formulas in which every formula occurs.
:::

In words: the atoms are listed already (\( p, q, r, p_1, p_2, \dots \)), and each formula is a finite string of symbols, so the formulas can be listed by size, finitely many at each stage.

::: {.second-reading title="How to list every formula"}
::: {.idea}
List by size. At stage \( n \), allow only the first \( n \) atoms and strings of at most \( n \) symbols. Each stage is finite, and every formula fits into some stage.
:::

::: {.proof}
Write the atoms in one list \( a_1, a_2, a_3, \dots \) (say \( p, q, r, p_1, p_2, \dots \) in this order). For each \( n \ge 1 \), consider the strings of length at most \( n \) over the \( n + 8 \) symbols
\[
a_1, \dots, a_n, \ \bot, \ \neg, \ \wedge, \ \vee, \ \to, \ \leftrightarrow, \ (, \ ) .
\]
There are finitely many such strings (at most \( (n+8)^n \) of each length up to \( n \)), so finitely many of them are formulas. Stage \( n \) lists, in any order, the formulas among them that no earlier stage listed. Write the stages one after another and number the entries \( \varphi_0, \varphi_1, \dots \). Each stage \( n \) lists at least the atom \( a_n \), which is available for the first time, so the stages together list infinitely many formulas.

Every formula occurs. Let \( \varphi \) have length \( \ell \), and let its atoms be among \( a_1, \dots, a_m \) (with \( m = 0 \) if it has none). At stage \( n = \max\{\ell, m\} \) (note \( \ell \ge 1 \)), \( \varphi \) is a string of length at most \( n \) over the symbols of that stage, so it is listed then, or earlier.
:::
:::

## Lindenbaum's construction

The new proof of completeness works the other way round from Section 4.8. It does not build a derivation. It starts from a consistent collection and builds a row that makes all of it true. The row is read off a collection that has made up its mind about every formula.

A collection \( \Delta \) is **maximal consistent** if it is consistent and, for every formula \( \varphi \), \( \varphi \) is in \( \Delta \) or \( \neg\varphi \) is.

The construction rests on one step. Exercise C2 of Section 3.2 (@exr-four-kinds-of-task-c2) proved it for finite lists; here it is again, for collections, with its proof.

**The key step.** *If \( \Delta \) is consistent, then \( \Delta \) with \( \varphi \) added, or \( \Delta \) with \( \neg\varphi \) added, is consistent.* Suppose both were inconsistent. Then there are finite lists \( \Delta_1 \) and \( \Delta_2 \) of members of \( \Delta \) with \( \Delta_1, \varphi \vdash \bot \) and \( \Delta_2, \neg\varphi \vdash \bot \) (if a derivation of \( \bot \) does not use \( \varphi \), or \( \neg\varphi \), adding it as a premise changes nothing, by weakening). By weakening, both hold with the list \( \Delta_1, \Delta_2 \) in place of \( \Delta_1 \) and of \( \Delta_2 \). A \( \rulename{\neg I} \) box on \( \varphi \) gives \( \Delta_1, \Delta_2 \vdash \neg\varphi \), and an \( \rulename{RAA} \) box on \( \neg\varphi \) gives \( \Delta_1, \Delta_2 \vdash \varphi \) (this is @prp-derivable-iff-negation-inconsistent). Then \( \rulename{\neg E} \), by chaining (@lem-weakening-cut (c)), gives \( \Delta_1, \Delta_2 \vdash \bot \), and \( \Delta \) would be inconsistent.

::: {#lem-lindenbaum}
[Lindenbaum's Lemma]

Every consistent collection of formulas is contained in a maximal consistent collection.
:::

::: {.idea}
Go through the list of all formulas, and add each one or its negation, whichever keeps the collection consistent. The key step says one of them always does. At the end, every formula has been decided, and no contradiction has been let in, because a contradiction would show up at some finite stage.
:::

::: {.proof}
Let \( \Gamma \) be consistent, and let \( \varphi_0, \varphi_1, \dots \) be the list of @lem-formula-enumeration. Define collections \( \Delta_0, \Delta_1, \dots \) by recursion on \( n \), each from the one before:
\[
\Delta_0 \coloneqq \Gamma ; \qquad
\Delta_{n+1} \coloneqq
\begin{cases}
\Delta_n \text{ with } \varphi_n \text{ added}, & \text{if that collection is consistent;} \\
\Delta_n \text{ with } \neg\varphi_n \text{ added}, & \text{otherwise.}
\end{cases}
\]
Every \( \Delta_n \) is consistent, by @ax-induction: \( \Delta_0 = \Gamma \) is; and if \( \Delta_n \) is, then \( \Delta_{n+1} \) is, by its definition in the first case and by the key step in the second. Each \( \Delta_n \) contains the one before.

Let \( \Delta \) consist of the formulas that belong to some \( \Delta_n \). Then \( \Delta \) contains \( \Gamma = \Delta_0 \).

\( \Delta \) is consistent. A derivation of \( \bot \) from \( \Delta \) uses a finite list of members of \( \Delta \). Each of them is in some \( \Delta_n \), so all of them are in the \( \Delta_N \) with the largest of those indices \( N \) (\( N = 0 \) if the list is empty), since the collections grow. That derivation would then show \( \Delta_N \vdash \bot \), but \( \Delta_N \) is consistent.

\( \Delta \) is maximal. Every formula is some \( \varphi_n \), and \( \varphi_n \) or \( \neg\varphi_n \) is in \( \Delta_{n+1} \), hence in \( \Delta \). This proves the lemma.
:::

::: {.check}
Start from \( \Gamma = \{p \vee q, \ \neg p\} \) with a list of formulas beginning \( p, q \). What are \( \Delta_1 \) and \( \Delta_2 \)?
:::

::: {.solution}
\( \Gamma \) with \( p \) added is inconsistent (\( p \) and \( \neg p \) give \( \bot \) by \( \rulename{\neg E} \)), so \( \Delta_1 \) adds \( \neg p \), which is already there: \( \Delta_1 = \Gamma \). \( \Delta_1 \) with \( q \) added is satisfiable (\( p = \mathrm{F} \), \( q = \mathrm{T} \)), hence consistent (Section 4.7), so \( \Delta_2 \) adds \( q \): \( \Delta_2 = \{p \vee q, \ \neg p, \ q\} \).
:::

## A row from a maximal consistent collection

A maximal consistent collection behaves like the collection of formulas that are true in one row: it contains a negation exactly when it lacks the negated formula, a conjunction exactly when it contains both parts, and so on through the clauses of @def-truth-value.

::: {#lem-maximal-consistent}
[Maximal Consistent Collections]

Let \( \Delta \) be maximal consistent, and let \( \varphi \), \( \psi \) be formulas.

::: {.enumerate options="label=(\alph*)"}
1. If \( \Delta \vdash \varphi \), then \( \varphi \in \Delta \).
2. Exactly one of \( \varphi \), \( \neg\varphi \) is in \( \Delta \); and \( \bot \notin \Delta \).
3. \( \varphi \wedge \psi \in \Delta \) iff \( \varphi \in \Delta \) and \( \psi \in \Delta \); \( \varphi \vee \psi \in \Delta \) iff \( \varphi \in \Delta \) or \( \psi \in \Delta \); \( \varphi \to \psi \in \Delta \) iff \( \varphi \notin \Delta \) or \( \psi \in \Delta \); \( \varphi \leftrightarrow \psi \in \Delta \) iff \( \varphi \) and \( \psi \) are both in \( \Delta \) or both not in \( \Delta \).
:::
:::

In words: whatever \( \Delta \) derives, it already contains; it decides every formula, one way only; and it treats each connective as the truth table does.

::: {.second-reading title="The proof: a maximal collection decides everything"}
::: {.idea}
For each clause, find the derivable sequent that says the same thing as the truth table, and let (a) put what \( \Delta \) derives into \( \Delta \); where a formula must be shown missing, derive its negation instead and use (b).
:::

::: {.proof}
Derivations from \( \Delta \) are combined by @lem-weakening-cut throughout: two finite lists of members of \( \Delta \) can be joined into one, and a sequent already proved can be applied by chaining.

*(a)* Suppose \( \Delta \vdash \varphi \) and \( \varphi \notin \Delta \). By maximality \( \neg\varphi \in \Delta \), so \( \Delta \vdash \neg\varphi \) by a one-line derivation, and \( \rulename{\neg E} \) gives \( \Delta \vdash \bot \), against consistency.

*(b)* At least one of \( \varphi \), \( \neg\varphi \) is in \( \Delta \), by maximality. If both were, \( \rulename{\neg E} \) would give \( \Delta \vdash \bot \). And \( \bot \in \Delta \) would give \( \Delta \vdash \bot \) at once.

*(c)* Each clause comes from (a), (b) and a derivable sequent.

\( \wedge \). If \( \varphi \wedge \psi \in \Delta \), then \( \rulename{\wedge E} \) gives \( \Delta \vdash \varphi \) and \( \Delta \vdash \psi \), so both are in \( \Delta \) by (a). If both are in \( \Delta \), \( \rulename{\wedge I} \) gives \( \Delta \vdash \varphi \wedge \psi \), so it is in \( \Delta \) by (a).

\( \vee \). If \( \varphi \in \Delta \) or \( \psi \in \Delta \), then \( \rulename{\vee I} \) gives \( \Delta \vdash \varphi \vee \psi \), so it is in \( \Delta \) by (a). If neither is in \( \Delta \), then \( \neg\varphi, \neg\psi \in \Delta \) by (b), and \( (\vee 3) \) of @lem-connective-rows gives \( \Delta \vdash \neg(\varphi \vee \psi) \); so \( \neg(\varphi \vee \psi) \in \Delta \) by (a), and \( \varphi \vee \psi \notin \Delta \) by (b).

\( \to \). If \( \varphi \to \psi \in \Delta \) and \( \varphi \in \Delta \), then \( \rulename{{\to}E} \) gives \( \Delta \vdash \psi \), so \( \psi \in \Delta \) by (a); hence \( \varphi \notin \Delta \) or \( \psi \in \Delta \). Conversely, if \( \varphi \notin \Delta \), then \( \neg\varphi \in \Delta \) by (b), and \( ({\to}1) \) gives \( \Delta \vdash \varphi \to \psi \); if \( \psi \in \Delta \), then \( ({\to}2) \) gives it. Either way \( \varphi \to \psi \in \Delta \) by (a).

\( \leftrightarrow \). If both \( \varphi \), \( \psi \) are in \( \Delta \), \( ({\leftrightarrow}1) \) gives \( \Delta \vdash \varphi \leftrightarrow \psi \); if neither, then \( \neg\varphi, \neg\psi \in \Delta \) and \( ({\leftrightarrow}2) \) gives it; in both cases \( \varphi \leftrightarrow \psi \in \Delta \) by (a). If exactly one is in \( \Delta \), the other's negation is in \( \Delta \) by (b), and \( ({\leftrightarrow}3) \) or \( ({\leftrightarrow}4) \) gives \( \Delta \vdash \neg(\varphi \leftrightarrow \psi) \); so \( \neg(\varphi \leftrightarrow \psi) \in \Delta \) by (a), and \( \varphi \leftrightarrow \psi \notin \Delta \) by (b). (With \( \varphi \leftrightarrow \psi \in \Delta \), \( \rulename{{\leftrightarrow}E} \) passes membership from either part to the other, which is the same fact read from the other side.)
:::
:::

So a maximal consistent collection names a row: make an atom true exactly when the collection contains it.

::: {#lem-truth-lemma}
[Truth Lemma]

Let \( \Delta \) be maximal consistent, and let \( v_\Delta \) be the valuation that makes an atom \( p \) true exactly when \( p \in \Delta \). Then for every formula \( \varphi \): \( v_\Delta(\varphi) = \mathrm{T} \) iff \( \varphi \in \Delta \).
:::

::: {.idea}
Induct on \( \varphi \). Each clause of @def-truth-value has a twin in @lem-maximal-consistent: part (b) for \( \neg \), part (c) for the binary connectives. The induction hypothesis turns "true under \( v_\Delta \)" into "in \( \Delta \)" for the parts, and the twin does the rest.
:::

::: {.proof}
By @thm-structural-induction, with the property "\( v_\Delta(\varphi) = \mathrm{T} \) iff \( \varphi \in \Delta \)".

*Atoms:* this is the definition of \( v_\Delta \). *\( \bot \):* \( v_\Delta(\bot) = \mathrm{F} \) by (V1), and \( \bot \notin \Delta \) by @lem-maximal-consistent (b), so both sides of the "iff" fail.

*\( \neg\varphi \):* \( v_\Delta(\neg\varphi) = \mathrm{T} \) iff \( v_\Delta(\varphi) = \mathrm{F} \), by (V2); iff \( \varphi \notin \Delta \), by the induction hypothesis; iff \( \neg\varphi \in \Delta \), by @lem-maximal-consistent (b).

*\( \varphi \wedge \psi \):* \( v_\Delta(\varphi \wedge \psi) = \mathrm{T} \) iff \( v_\Delta(\varphi) = \mathrm{T} \) and \( v_\Delta(\psi) = \mathrm{T} \), by (V3); iff \( \varphi \in \Delta \) and \( \psi \in \Delta \), by the induction hypothesis; iff \( \varphi \wedge \psi \in \Delta \), by @lem-maximal-consistent (c). The cases \( \vee \), \( \to \), \( \leftrightarrow \) are the same: the clause of @def-truth-value for the connective and the clause of @lem-maximal-consistent (c) for it say the same thing, once "true under \( v_\Delta \)" is read as "in \( \Delta \)" for the two parts, as the induction hypothesis allows. This proves the lemma.
:::

## Completeness again

::: {#thm-completeness-infinite}
[Completeness for Infinitely Many Premises]

For every collection \( \Gamma \) of formulas, finite or infinite, and every formula \( \psi \): if \( \Gamma \models \psi \), then \( \Gamma \vdash \psi \). Equivalently, every consistent collection is satisfiable.
:::

::: {.idea}
If \( \Gamma \) does not derive \( \psi \), then adding \( \neg\psi \) cannot lead to \( \bot \), since an \( \rulename{RAA} \) box would turn such a derivation into one of \( \psi \). Extend \( \Gamma \) with \( \neg\psi \) to a maximal consistent collection and read off its row: it makes every member of \( \Gamma \) true and \( \psi \) false.
:::

::: {.proof}
We prove the contrapositive of the first sentence. Suppose \( \Gamma \nvdash \psi \). Then \( \Gamma \) with \( \neg\psi \) added is consistent. For suppose some finite list of its members derived \( \bot \); adding \( \neg\psi \) to the list if it is not there (weakening), we have \( \Gamma_0, \neg\psi \vdash \bot \) for a finite list \( \Gamma_0 \) of members of \( \Gamma \), and an \( \rulename{RAA} \) box on \( \neg\psi \) gives \( \Gamma_0 \vdash \psi \), so \( \Gamma \vdash \psi \). By @lem-lindenbaum, \( \Gamma \) with \( \neg\psi \) is contained in a maximal consistent \( \Delta \). By @lem-truth-lemma, \( v_\Delta \) makes every member of \( \Delta \) true, in particular every member of \( \Gamma \), and \( \neg\psi \). So \( v_\Delta \) makes \( \psi \) false, and \( \Gamma \not\models \psi \).

The equivalence: by @def-infinite-entailment and (V1), \( \Gamma \) is satisfiable iff \( \Gamma \not\models \bot \), and consistent iff \( \Gamma \nvdash \bot \). So the first sentence with \( \psi = \bot \) is the second. Conversely, given the second, if \( \Gamma \nvdash \psi \), then \( \Gamma \) with \( \neg\psi \) is consistent, as just shown, hence satisfiable, by a row that refutes \( \Gamma \models \psi \).
:::

**Two proofs, two prices.** Section 4.8 glued the rows of a truth table into one derivation. That is a construction one can carry out, from \( 2^n \) row derivations for \( n \) atoms, but only for finitely many premises. This section never writes a derivation. It shows that if none exists, then a row exists, by a construction that passes through infinitely many formulas, one at a time, and cannot be finished by hand. The first proof is effective (it writes the derivation down) and limited to finite lists; the second reaches infinite collections and produces no derivation. The second is the route that extends beyond propositional logic.

::: {.second-reading title="A remark on the list of formulas"}
Besides the rules, and the structural induction and recursion of Section 4.3, the proof used one new fact about the formulas: that they can be listed (@lem-formula-enumeration). The construction then decides the formulas in the order of the list, and a different list may give a different \( \Delta \) and a different row; any of them refutes \( \Gamma \models \psi \). The proof cites @prp-excluded-middle nowhere, but its key step uses \( \rulename{RAA} \), and so does the step from \( \Gamma \nvdash \psi \) to the consistency of \( \Gamma \) with \( \neg\psi \). It is classical in the same way as the splitting of Section 4.8, which used excluded middle.
:::

## Compactness

::: {#thm-compactness}
[Compactness]

A collection \( \Gamma \) of formulas is satisfiable if and only if every finite list of members of \( \Gamma \) is satisfiable. Consequently, \( \Gamma \models \psi \) if and only if some finite list of members of \( \Gamma \) entails \( \psi \).
:::

::: {.proof}
"Only if": a valuation making every member of \( \Gamma \) true makes every member of each finite list true. "If": every finite list of members of \( \Gamma \) is satisfiable, hence consistent, by Section 4.7. So \( \Gamma \) is consistent, since a derivation of \( \bot \) from \( \Gamma \) would use a finite list of members. By @thm-completeness-infinite, \( \Gamma \) is satisfiable.

For the second sentence: \( \Gamma \models \psi \) iff \( \Gamma \) with \( \neg\psi \) added is unsatisfiable (a valuation making \( \Gamma \) true and \( \psi \) false is exactly one making both \( \Gamma \) and \( \neg\psi \) true); iff, by the first sentence, some finite list of its members is unsatisfiable; iff some finite list \( \Gamma_0 \) of members of \( \Gamma \) has \( \Gamma_0, \neg\psi \) unsatisfiable (adding \( \neg\psi \) to an unsatisfiable list keeps it unsatisfiable, and \( \Gamma_0, \neg\psi \) is itself such a list); iff \( \Gamma_0 \models \psi \), by Section 4.5's reduction of entailment to unsatisfiability.
:::

::: {#exm-compactness-chain}
[Infinitely many premises, finitely many used]

Let \( \Gamma \) consist of \( p_1 \) and every \( p_n \to p_{n+1} \) with \( n \ge 1 \), the lamps of the opening.

::: {.enumerate options="label=(\alph*)"}
1. Show \( \Gamma \models p_{100} \), and find a finite list of members of \( \Gamma \) that entails \( p_{100} \).
2. Show that a finite list of members of \( \Gamma \) that leaves out \( p_{50} \to p_{51} \) does not entail \( p_{100} \).
:::
:::

::: {.solution}
*(a)* A valuation making every member of \( \Gamma \) true makes \( p_1 \) true and passes truth from each \( p_n \) to \( p_{n+1} \), so it makes every \( p_n \) true (@ax-induction, started at \( 1 \)), \( p_{100} \) among them. The hundred formulas \( p_1, \ p_1 \to p_2, \ \dots, \ p_{99} \to p_{100} \) already entail \( p_{100} \): a row making them all true makes \( p_1, p_2, \dots, p_{100} \) true, one after another.

*(b)* Take the valuation making \( p_1, \dots, p_{50} \) true and every other atom false. It makes \( p_1 \) true; it makes \( p_n \to p_{n+1} \) true for \( n < 50 \) (true conclusion) and for \( n > 50 \) (false hypothesis); only \( p_{50} \to p_{51} \) is false. So it makes every member of the finite list true, and \( p_{100} \) false.

Compactness says that this is no accident: an entailment from infinitely many premises always rests on finitely many of them. Here every finite list that entails \( p_{100} \) must contain all ninety-nine implications up to \( p_{99} \to p_{100} \), since (b)'s argument works with any \( p_k \to p_{k+1} \), \( k < 100 \), in place of \( p_{50} \to p_{51} \), and it must contain \( p_1 \), since the valuation making every atom false makes all the implications true.
:::

::: {.warning}
Compactness promises **one** valuation for the whole collection when each finite part has one. The valuations of the finite parts may all differ, and the theorem does not say how to find the single one: its proof went through a maximal consistent collection, which nobody writes down.
:::

::: {.remark}
[Looking ahead]

Chapter 7 states completeness and compactness for predicate logic (Section 7.6, optional), without proof; its sketch of completeness follows the route of this section.
:::

## Exercises

### A. Check your understanding

::: {#exr-compactness-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Why is \( \Gamma \vdash \psi \) defined through finite lists of members of \( \Gamma \)?
2. True or false: an infinite collection \( \Gamma \) is consistent iff every finite list of its members is consistent.
3. In the proof of @lem-lindenbaum, why can \( \Delta_n \) with \( \varphi_n \) added and \( \Delta_n \) with \( \neg\varphi_n \) added not both be inconsistent?
4. \( \Delta \) is maximal consistent, \( p \in \Delta \) and \( q \notin \Delta \). Is \( p \to q \) in \( \Delta \)? Is \( \neg(p \wedge \neg q) \)?
5. Which result of Section 4.7 does the proof of @thm-compactness use?
:::
:::

::: {.solution}
*(a)* A derivation has finitely many lines, so it uses finitely many premises.

*(b)* True, by @def-infinite-entailment: \( \Gamma \vdash \bot \) means that some finite list of members derives \( \bot \).

*(c)* By the key step: \( \rulename{\neg I} \) and \( \rulename{RAA} \) would derive \( \neg\varphi_n \) and \( \varphi_n \) from finitely many members of \( \Delta_n \), and \( \rulename{\neg E} \) then \( \bot \), making \( \Delta_n \) inconsistent.

*(d)* Neither. \( p \to q \notin \Delta \) by @lem-maximal-consistent (c), since \( p \in \Delta \) and \( q \notin \Delta \). And \( \neg q \in \Delta \) by (b), so \( p \wedge \neg q \in \Delta \) by (c), so \( \neg(p \wedge \neg q) \notin \Delta \) by (b).

*(e)* That a satisfiable list is consistent (soundness).
:::

::: {#exr-compactness-a2}
[A2: Drill]

The parts run from judging collections, through the definitions and single stages of the construction, to the lemmas and the theorem, and end with one more collection to judge.

::: {.enumerate options="label=(\alph*)"}
1. Is the collection of all \( p_n \) with \( n \ge 1 \) satisfiable?
2. Is the collection of \( p_1 \) and every \( \neg p_n \) with \( n \ge 2 \) consistent?
3. Does the collection of all \( p_n \to p_{n+1} \) with \( n \ge 1 \) entail \( p_1 \to p_7 \)? If so, which finite list of members does?
4. Is the collection of \( p_1 \vee p_2 \), \( \neg p_1 \), \( \neg p_2 \) and every \( p_n \) with \( n \ge 3 \) satisfiable?
5. For a finite \( \Gamma \), does @def-infinite-entailment change what \( \Gamma \vdash \psi \) means?
6. Run Lindenbaum's construction from \( \Gamma = \{p\} \) with a list beginning \( q, \neg p \). What are \( \Delta_1 \) and \( \Delta_2 \)?
7. \( \Delta \) is maximal consistent and \( p \notin \Delta \). Is \( \neg p \in \Delta \)? When is \( p \vee q \in \Delta \)?
8. \( p \in \Delta \) and \( \neg q \in \Delta \), with \( \Delta \) maximal consistent. Is \( p \wedge \neg q \in \Delta \)?
9. Can a maximal consistent \( \Delta \) contain \( p \to q \), \( p \) and \( \neg q \)?
10. How many formulas of length 1 contain no atom other than \( p \) and \( q \)?
11. Can \( \Gamma \models \psi \) hold with no finite list of members of \( \Gamma \) entailing \( \psi \)?
12. Is the collection of all \( p_n \leftrightarrow \neg p_{n+1} \) with \( n \ge 1 \) satisfiable?
:::
:::

::: {.solution}
(a) Yes: every atom true.

(b) Yes: it is satisfiable (\( p_1 \) true, every other atom false), hence consistent.

(c) Yes; the list \( p_1 \to p_2, \ \dots, \ p_6 \to p_7 \) does.

(d) No: its first three members already have no common row.

(e) No (@lem-weakening-cut (a)).

(f) \( \Delta_1 = \{p, q\} \), which is satisfiable, hence consistent. \( \Delta_1 \) with \( \neg p \) is inconsistent, so \( \Delta_2 = \{p, q, \neg\neg p\} \).

(g) Yes, by @lem-maximal-consistent (b); and \( p \vee q \in \Delta \) exactly when \( q \in \Delta \), by (c).

(h) Yes, by @lem-maximal-consistent (c).

(i) No: \( \rulename{{\to}E} \) and \( \rulename{\neg E} \) would derive \( \bot \).

(j) Three: \( p \), \( q \), \( \bot \).

(k) No, by @thm-compactness.

(l) Yes: make \( p_n \) true for odd \( n \) and false for even \( n \).
:::

### B. Practice

::: {#exr-compactness-b1}
[B1: Running the construction]

Run the construction of @lem-lindenbaum on \( \Gamma = \{p \vee q, \ \neg p\} \) for the first four formulas of a list beginning \( p, \ q, \ \neg q, \ p \wedge q \). Justify each "consistent" by a row and each "inconsistent" by a short derivation of \( \bot \). Then say which values \( v_\Delta \) gives \( p \) and \( q \), whatever the rest of the list.
:::

::: {.solution}
\( \Delta_0 = \Gamma \).

\( p \): \( \Gamma \) with \( p \) is inconsistent (\( p \) and \( \neg p \), then \( \rulename{\neg E} \)), so \( \Delta_1 \) adds \( \neg p \), which is already there.

\( q \): \( \Delta_1 \) with \( q \) is consistent, since the row \( p = \mathrm{F} \), \( q = \mathrm{T} \) makes \( p \vee q \), \( \neg p \), \( q \) true (Section 4.7); \( \Delta_2 \) adds \( q \).

\( \neg q \): \( \Delta_2 \) with \( \neg q \) is inconsistent (\( q \) and \( \neg q \), then \( \rulename{\neg E} \)); \( \Delta_3 \) adds \( \neg\neg q \).

\( p \wedge q \): \( \Delta_3 \) with \( p \wedge q \) is inconsistent (\( \rulename{\wedge E} \) gives \( p \), which clashes with \( \neg p \)); \( \Delta_4 \) adds \( \neg(p \wedge q) \).

Whatever the rest of the list, \( \neg p \) and \( q \) are in \( \Delta \), so \( p \notin \Delta \) by @lem-maximal-consistent (b), and \( v_\Delta \) makes \( p \) false and \( q \) true. Later stages only add formulas, so they cannot change this.

**Marking scheme.** (6 points)

- 4: one per stage, with its justification (a row checked, or a derivation of \( \bot \)).
- 2: the row of \( v_\Delta \) on \( p \), \( q \), and why later stages cannot change it.
:::

::: {#exr-compactness-b2}
[B2: The clause for implication]

Prove the \( \to \) clause of @lem-maximal-consistent (c) in full, from parts (a) and (b) and the sequents of @lem-connective-rows.
:::

::: {.solution}
(\( \Rightarrow \)) Let \( \varphi \to \psi \in \Delta \). If \( \varphi \in \Delta \), the two-premise list \( \varphi \to \psi, \ \varphi \) of members of \( \Delta \) derives \( \psi \) by one \( \rulename{{\to}E} \) line, so \( \Delta \vdash \psi \), and \( \psi \in \Delta \) by (a). So either \( \varphi \notin \Delta \) or \( \psi \in \Delta \).

(\( \Leftarrow \)) If \( \varphi \notin \Delta \), then \( \neg\varphi \in \Delta \) by (b), and \( ({\to}1) \), \( \neg\varphi \vdash \varphi \to \psi \), shows \( \Delta \vdash \varphi \to \psi \); so \( \varphi \to \psi \in \Delta \) by (a). If \( \psi \in \Delta \), then \( ({\to}2) \), \( \psi \vdash \varphi \to \psi \), does the same.

**Marking scheme.** (6 points)

- 3: (\( \Rightarrow \)), with (a) cited.
- 3: (\( \Leftarrow \)), both cases, with (b) used in the first.
:::

### C. Going deeper

::: {#exr-compactness-c1}
[C1: Coloring an infinite graph]

A graph on the vertices \( 1, 2, 3, \dots \) is given by saying which pairs of vertices are joined. A **3-coloring** gives each vertex one of three colors so that joined vertices get different colors. Suppose every finite set of vertices, with the joins among them, can be 3-colored. Prove that the whole graph can. Use atoms \( c_{n,i} \), read "vertex \( n \) gets color \( i \)" for \( i = 1, 2, 3 \), where the \( c_{n,i} \) are distinct atoms (for instance, \( c_{n,i} \) is \( p_{3n+i} \)).
:::

::: {.solution}
Let \( \Gamma \) consist of three kinds of formulas:

- \( c_{n,1} \vee c_{n,2} \vee c_{n,3} \), for every vertex \( n \);
- \( \neg(c_{n,i} \wedge c_{n,j}) \), for every vertex \( n \) and all \( i \ne j \);
- \( \neg(c_{m,i} \wedge c_{n,i}) \), for every joined pair \( m \), \( n \) and every \( i \).

A valuation making every member of \( \Gamma \) true gives each vertex exactly one color (the first two kinds), and joined vertices different colors (the third kind): it is a 3-coloring, coloring \( n \) with the \( i \) for which \( c_{n,i} \) is true.

Every finite list \( \Gamma_0 \) of members of \( \Gamma \) is satisfiable. Its members mention finitely many vertices; call that finite set \( F \). By hypothesis, \( F \) with the joins among its vertices has a 3-coloring \( \kappa \). Let \( v \) make \( c_{n,i} \) true exactly when \( n \in F \) and \( \kappa(n) = i \). Each member of \( \Gamma_0 \) mentions only vertices of \( F \), and \( v \) makes it true: the first kind because \( \kappa \) colors every vertex of \( F \), the second because it gives each one color, the third because \( \kappa \) colors joined vertices of \( F \) differently.

By @thm-compactness, \( \Gamma \) is satisfiable, and a satisfying valuation is a 3-coloring of the whole graph.

**Marking scheme.** (10 points)

- 3: the collection \( \Gamma \), with all three kinds.
- 2: a valuation making \( \Gamma \) true gives a 3-coloring.
- 4: every finite part satisfiable, with the restriction to the vertices it mentions.
- 1: @thm-compactness cited.

Fatal errors (0 for the step): coloring the vertices one at a time and claiming the choices can always be continued, with no argument; a "finite part" argument that colors only the vertices \( 1, \dots, n \) without checking that every member of \( \Gamma_0 \) mentions only them.
:::

::: {#exr-compactness-c2}
[C2: Challenge: Compactness without derivations]

Suppose the atoms are listed \( a_1, a_2, \dots \), and every finite list of members of \( \Gamma \) is satisfiable. Choose truth values for \( a_1, a_2, \dots \) one at a time, keeping this property:

\( (P_n) \) every finite list of members of \( \Gamma \) is made true by some valuation that agrees with the choices made for \( a_1, \dots, a_n \).

::: {.enumerate options="label=(\alph*)"}
1. Show that if \( P_n \) holds, a value for \( a_{n+1} \) can be chosen so that \( P_{n+1} \) holds.
2. Show that the valuation \( v \) given by all the choices makes every member of \( \Gamma \) true.
3. Which earlier results does (b) use?
:::
:::

::: {.solution}
[Hint 1]

For (a), suppose neither value works, and take one finite list witnessing each failure.
:::

::: {.solution}
*(a)* \( P_0 \) is the hypothesis. Suppose \( P_n \) holds and neither value of \( a_{n+1} \) works. Then there is a finite list \( F_1 \) that no valuation agreeing with the choices and making \( a_{n+1} \) true satisfies, and a finite list \( F_2 \) that no valuation agreeing with the choices and making \( a_{n+1} \) false satisfies. By \( P_n \), the finite list \( F_1, F_2 \) is satisfied by some valuation \( u \) agreeing with the choices for \( a_1, \dots, a_n \). If \( u \) makes \( a_{n+1} \) true, it satisfies \( F_1 \); if false, it satisfies \( F_2 \). Either way a contradiction. So some value works: choose \( \mathrm{T} \) if \( \mathrm{T} \) works, and \( \mathrm{F} \) otherwise. This gives \( P_{n+1} \), and the rule defines the values by recursion on \( n \).

*(b)* By (a) and @ax-induction, \( P_n \) holds for every \( n \). Let \( \gamma \in \Gamma \), with its atoms among \( a_1, \dots, a_N \). By \( P_N \), the one-member list \( \gamma \) is made true by some valuation agreeing with \( v \) on \( a_1, \dots, a_N \). By @lem-coincidence, \( v \) makes \( \gamma \) true.

*(c)* @lem-coincidence, @ax-induction (\( P_n \) for every \( n \), from (a)), and a definition by recursion on \( n \) (each choice depends on the earlier ones). No derivation and no completeness theorem is used: this proves @thm-compactness directly.

**Marking scheme.** (10 points)

- 5: (a), with the joint list \( F_1, F_2 \) and both cases of \( u \).
- 4: (b), with \( N \) chosen from the atoms of \( \gamma \), \( P_N \) obtained from (a) by @ax-induction, and @lem-coincidence cited.
- 1: (c).

Fatal errors (0 for the step): in (a), choosing a value that works for each finite list separately, possibly different for different lists.
:::

<!-- dependency ledger
def-infinite-entailment (claim): collection, finite list of members | everyday sense; F2.3 (promised: countable listing; STATUS row F1.3 §10, paid by exr-countable-unions-and-choice-b2 with thm-countable-union)
def-infinite-entailment (claim): for a finite list the definitions agree with def-derivable, def-inconsistent-set, def-valid-argument, def-satisfiable | lem-weakening-cut (a) (cited); the same content otherwise (def-valid-argument, def-satisfiable)
lem-formula-enumeration (proof): finitely many strings of bounded length over a finite alphabet | school counting
lem-lindenbaum (proof): definition by recursion on the natural numbers | F2.2 (promised; STATUS row F1.3 §10 'recursion; maximum of a finite set', paid by thm-recursion)
lem-lindenbaum (proof): a non-empty finite set of natural numbers has a maximum (N = 0 for an empty list) | F2.2 (promised; STATUS row F1.3 §10 'recursion; maximum of a finite set', paid by prp-finite-max)
lem-lindenbaum (proof): the key step: Delta consistent implies Delta with phi or with not-phi consistent | proved in full in the text; exr-four-kinds-of-task-c2 recalled by label (finite lists), not relied on
lem-lindenbaum (proof): the key step's derivations | rules neg-I, RAA, neg-E; lem-weakening-cut (a), (c); prp-derivable-iff-negation-inconsistent (cited)
lem-maximal-consistent (proof): each clause from a derivable sequent | lem-connective-rows (vee 3), (to 1), (to 2), (iff 1)-(iff 4); rules and-E, and-I, vee-I, to-E
lem-truth-lemma (proof): structural induction; the clauses of the truth value | thm-structural-induction, def-truth-value (cited)
thm-completeness-infinite (proof): Gamma not deriving psi makes Gamma with not-psi consistent | RAA, lem-weakening-cut (a) (argued inline)
thm-compactness (proof): satisfiable implies consistent | F1.3 §07, in prose (thm-soundness, cor-refuting-row: a satisfiable list derives no bot)
thm-compactness (proof): Gamma_0 entails psi iff Gamma_0, not-psi is unsatisfiable | F1.3 §05, the reduction after def-valid-argument (unlabeled), recalled in prose
exm-compactness-chain (example): truth passed along p_n -> p_(n+1) reaches every p_n | ax-induction, started at 1 (cited)
exr-compactness-c1 (solution): a finite set of vertices mentioned by a finite list | everyday finiteness
exr-compactness-c2 (solution): a choice of values by recursion on n | F2.2 (promised; STATUS row F1.3 §10 'recursion; maximum of a finite set', paid by thm-recursion); lem-coincidence (cited)
exr-compactness-c2 (solution): P_n for every n, from P_0 and (a) | ax-induction (cited)
-->
