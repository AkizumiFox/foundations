# Models and Theories

The axioms of a partial order say that \( \le \) is reflexive, antisymmetric and transitive. Do they prove that any two elements are comparable, \( \forall x\, \forall y\, (x \le y \vee y \le x) \)? A search for a derivation stalls, and a stalled search proves nothing. Two dots settle it: a domain \( \{ a, b \} \) in which each element is \( \le \) itself and nothing else. All three axioms are true there and comparability is false, so, by a statement of Section 7.2, no derivation exists. *What does "true there" mean, and why does one picture rule out every derivation?* This chapter answers both, and then uses such pictures on whole theories: in Section 7.4, "is every group commutative?" is answered by the six symmetries of a triangle.

**How to read this chapter.** First reading: Sections 7.1, 7.2 and 7.4, and Section 7.5 up to "Isomorphic structures". Second pass: the rest of Section 7.5. Optional: Sections 7.3 and 7.6. The statement that a counter-model rules out every derivation is on the trunk, in Section 7.2; its proof is optional, in Section 7.3. Nothing on the first-reading list uses anything off it.

**Before you start: five tempting claims.** Each is a claim this chapter corrects; decide each now, and check again at the section named.

::: {.check}
1. "\( \forall x\, \exists y\, (x < y) \) is true."
2. "A search for a derivation of \( \Gamma \vdash \varphi \) stalled, so \( \Gamma \nvdash \varphi \)."
3. "If \( \sigma \) is true in \( (\nN, <) \), then \( \sigma \) is derivable."
4. "Every group is commutative: the integers under addition are."
5. "\( (\nN, <) \) and the even numbers with \( < \) can be told apart by some sentence, since one is part of the other."
:::

::: {.second-reading title="Answers"}
1. Not until a structure is fixed: true in \( (\nN, <) \), false in \( (\{ 1, 2, 3 \}, <) \) (Section 7.1).
2. No. A stalled search proves nothing; a counter-model does (Section 7.2).
3. No. Derivable sentences are true in **every** structure; \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \) and false in a three-element order (Section 7.2).
4. No. The six symmetries of a triangle form a group in which two motions done in the two orders differ (Section 7.4).
5. No. Doubling matches them element for element and order for order, and matched structures satisfy the same sentences (Section 7.5, second pass).
:::

**What you need.** Chapters 1–6, above all the semantics of Chapter 4 (rows, \( \models \), soundness) and the quantifier rules of Chapter 5. Section 7.5's second half uses functions and bijections in their everyday sense.

**Time.** About 20 hours on the core track (Sections 7.1, 7.2, 7.4 and the first half of 7.5: all of A, one B and one C per section, the exit checks); about 45 hours for everything.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, core; Sections 7.1–7.2 before its Section 2.5; Sections 7.4–7.5 recommended.

## Roadmap

- **Structures and Satisfaction.** A domain and a meaning for every symbol, an assignment for the free variables, clauses that decide every formula; finite structures drawn; proofs by meaning.
- **Counter-models.** Three pictures, a procedure for finding one, small domains by expansion, each side condition of Chapter 5 broken, and the statement that a counter-model rules out every derivation.
- **Soundness for Predicate Logic** (optional). The proof of that statement, by Chapter 4's induction.
- **Theories and Their Models.** Axioms as sentences, consistency by a model, independence by two models.
- **Definability and Isomorphism.** A formula defines a set; \( \exists \) is a projection. Second pass: isomorphic structures satisfy the same sentences; automorphisms move what is not definable.
- **What First-Order Logic Can and Cannot Say** (optional). Completeness, compactness, non-standard numbers, undecidability, all stated without proof.

## Named moves

- **Refute with a model.** One structure with the premises true and the conclusion false. (Section 7.2)
- **Prove by meaning, clause by clause.** Unwind the premises and the conclusion through (S1)–(S7). (Section 7.1)
- **Search for a counter-model.** Start from the counterexample set, meet the existential demands first, add only forced elements. (Section 7.2)
- **Expand over a small domain.** On two or three elements a quantifier is a long \( \wedge \) or \( \vee \). (Section 7.2)
- **Consistent by a model; independent by two models.** (Section 7.4)
- **Define by a formula.** (Section 7.5)
- **An automorphism moves what cannot be defined.** (Section 7.5, second pass)

**Where this goes.** *Sets and Functions*, Chapter 1 develops the sets, pairs and functions that Sections 7.1 and 7.5 use in their everyday sense, and its Chapter 3 builds a counter-model by Section 7.2's procedure; its Chapter 4 studies the relations of Section 7.4.

## Summary

A structure fixes a domain and a meaning for every symbol, an assignment fixes the free variables, and seven clauses decide every formula (@def-satisfaction); a sentence is true or false in a structure, never "true" alone. A counter-model makes the counterexample set true; by soundness for predicate logic (stated in [Section 7.2](#from-counter-models-to-non-derivability), proved in the optional Section 7.3) it rules out every derivation: the stalled searches of Chapters 5 and 6 become theorems of non-derivability, and each side condition of the quantifier rules is shown needed. A theory is a set of axioms (@def-theory); a model shows it consistent (@prp-model-shows-consistency), and two models show a sentence independent of it (@prp-model-shows-independence), as the antichain does for comparability and the triangle for commutativity. Formulas define sets (@def-definable-set), and, on the second pass, isomorphic structures satisfy the same sentences (@thm-isomorphism-invariance).

Proved: the semantics, and every non-derivability result the chapter gets from a counter-model, given the soundness statement. Stated without proof: the undecidability of derivability (Church and Turing; Section 7.2, again in 7.6) and the \( 2^k \) bound on counter-models of monadic claims (Section 7.2); in the optional Section 7.6, completeness (every consistent theory has a model), compactness, the Löwenheim–Skolem theorem and the decidability of monadic sentences; and, in the solution to Exercise R2 of Section 7.5, that \( P \wedge Q \) cannot be derived from its premise without \( \rulename{RAA} \) (nothing depends on it). Beyond this volume: why no consistent theory whose axioms a procedure can list, and which derives the basic facts of arithmetic, decides every sentence about \( \nN \) (Gödel's incompleteness theorem, named in Section 7.6). Chapter 8 turns derivations into the prose of mathematics.

## Terms

- **assignment**: a value for each variable (@def-assignment).
- **automorphism**: an isomorphism onto itself (@def-isomorphism-of-structures).
- **consistent, inconsistent theory**: no finite list of axioms derives \( \bot \) (@def-inconsistent-theory).
- **counter-model**: premises true, conclusion false (@def-first-order-entailment).
- **definable set**: the elements where a formula holds (@def-definable-set).
- **domain**: what a structure's quantifiers range over (@def-structure).
- **independent sentence**: neither derivable nor refutable (@prp-model-shows-independence).
- **isomorphism of structures**: a bijection respecting every symbol (@def-isomorphism-of-structures).
- **model of a theory**: a structure with every axiom true (@def-model-of-theory).
- **satisfaction, \( \fM, \ell \models \varphi \)**: the clauses (S1)–(S7) (@def-satisfaction).
- **semantic entailment, \( \Gamma \models \varphi \)**: no counter-model (@def-first-order-entailment).
- **structure**: a domain and a meaning for every symbol (@def-structure).
- **theory, \( T \vdash \sigma \)**: a set of axioms; derivable from finitely many (@def-theory).
- **true in a structure, \( \fM \models \sigma \)**: satisfied under every assignment ([Section 7.1](#only-the-free-variables-matter)).
