# Chapter Review

## Summary

A structure fixes a domain and a meaning for every symbol, and an assignment fixes the values of the free variables. Seven clauses then decide every formula (@def-satisfaction). A sentence is true or false in a structure, never "true" on its own.

A counter-model makes the premises true and the conclusion false. By soundness for predicate logic, stated in [Section 7.2](#from-counter-models-to-non-derivability) and proved in the optional Section 7.3, a counter-model rules out every derivation. So the stalled searches of Chapters 5 and 6 become proofs that no derivation exists, and each side condition of the quantifier rules is shown to be needed.

A theory is a set of axioms (@def-theory). One model shows a theory consistent (@prp-model-shows-consistency). Two models show a sentence independent of it (@prp-model-shows-independence): the two-dot order does this for comparability, and the triangle for commutativity. Formulas define sets (@def-definable-set). On the second pass, isomorphic structures satisfy the same sentences (@thm-isomorphism-invariance).

What was proved: the semantics, and every non-derivability result the chapter gets from a counter-model, given the soundness statement. Some facts were stated without proof:

- that derivability cannot be decided by any procedure (Church and Turing), in Section 7.2 and again in Section 7.6;
- the \( 2^k \) bound on counter-models of claims with only one-place predicate symbols, in Section 7.2;
- in the optional Section 7.6, completeness (every consistent theory has a model), compactness, the Löwenheim–Skolem theorem, and the decidability of sentences with only one-place predicate symbols;
- in the solution to Exercise R2 of Section 7.5, that \( P \wedge Q \) cannot be derived from its premise without \( \rulename{RAA} \). Nothing depends on it.

Beyond this volume lies Gödel's incompleteness theorem, named in Section 7.6. Take a consistent theory whose axioms a procedure can list, and which derives the basic facts of arithmetic. Then some sentence about \( \nN \) is neither derivable nor refutable in it. Chapter 8 turns derivations into the prose of mathematics.

## Proof methods in this chapter

- **Refute with a model.** Give one structure in which the premises are true and the conclusion is false. (Section 7.2)
- **Prove by meaning, clause by clause.** Unwind the premises and the conclusion through the seven clauses of satisfaction. (Section 7.1)
- **Search for a counter-model.** Start from the premises and the negated conclusion. Meet the demands for witnesses first, and add only the elements you are forced to add. (Section 7.2)
- **Expand over a small domain.** On two or three elements, a \( \forall \) is a long \( \wedge \) and an \( \exists \) a long \( \vee \). (Section 7.2)
- **Consistent by a model; independent by two models.** (Section 7.4)
- **Define by a formula.** (Section 7.5)
- **An automorphism moves what cannot be defined.** A set that some automorphism moves is defined by no formula. (Section 7.5, second pass)

## Terms

- **assignment**: a value for each variable (@def-assignment).
- **automorphism**: an isomorphism of a structure onto itself (@def-isomorphism-of-structures).
- **consistent, inconsistent theory**: a theory is inconsistent when finitely many of its axioms derive \( \bot \), and consistent otherwise (@def-inconsistent-theory).
- **counter-model**: a structure and an assignment with the premises true and the conclusion false (@def-first-order-entailment).
- **definable set**: the elements where a formula holds (@def-definable-set).
- **domain**: the set that a structure's quantifiers range over (@def-structure).
- **independent sentence**: a sentence the theory neither derives nor refutes (@prp-model-shows-independence).
- **isomorphism of structures**: a one-to-one and onto map that respects every symbol (@def-isomorphism-of-structures).
- **model of a theory**: a structure in which every axiom is true (@def-model-of-theory).
- **satisfaction, \( \fM, \ell \models \varphi \)**: the seven clauses of @def-satisfaction.
- **semantic entailment, \( \Gamma \models \varphi \)**: there is no counter-model (@def-first-order-entailment).
- **structure**: a domain and a meaning for every symbol (@def-structure).
- **theory, \( T \vdash \sigma \)**: a set of axioms; \( T \vdash \sigma \) when finitely many of them derive \( \sigma \) (@def-theory).
- **true in a structure, \( \fM \models \sigma \)**: satisfied under every assignment, as [Section 7.1](#only-the-free-variables-matter) shows.

## Results used from earlier volumes

None: *Logic and Proof* is the first volume of the series. The chapter builds on Chapters 1–6 of this book.

## Five tempting claims

Each claim below is tempting, and each is wrong as it stands. Decide each one, then check the answer and the section that settles it.

::: {.check}
1. "\( \forall x\, \exists y\, (x < y) \) is true."
2. "A search for a derivation of \( \Gamma \vdash \varphi \) stalled, so \( \Gamma \nvdash \varphi \)."
3. "If \( \sigma \) is true in \( (\nN, <) \), then \( \sigma \) is derivable."
4. "Every group is commutative: the integers under addition are."
5. "\( (\nN, <) \) and the even numbers with \( < \) can be told apart by some sentence, since one is part of the other."
:::

::: {.second-reading title="Answers"}
1. Not until a structure is fixed. It is true in \( (\nN, <) \) and false in \( (\{ 1, 2, 3 \}, <) \) (Section 7.1).
2. No. A stalled search proves nothing; a counter-model does (Section 7.2).
3. No. Derivable sentences are true in **every** structure. The sentence \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \) and false in a three-element order (Section 7.2).
4. No. The six symmetries of a triangle form a group in which two motions, done in the two orders, give different results (Section 7.4).
5. No. Doubling matches them element for element and order for order, and matched structures satisfy the same sentences (Section 7.5, second pass).
:::

## Where this goes

*Sets and Functions*, Chapters 1 and 2, develop the sets, pairs and functions that Sections 7.1 and 7.5 use in their everyday sense. Its Chapter 6 builds a counter-model by the procedure of Section 7.2, and its Chapter 5 studies the relations of Section 7.4.
