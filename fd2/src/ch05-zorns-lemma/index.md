# Zorn's Lemma

Some objects are built one piece at a time: an injection one pair at a time, a set of representatives one class at a time, a total order one comparison at a time. When the pieces can be listed, induction finishes the job, one step for each natural number. When they cannot, as for the elements of \( \nR \), the words "and so on" stand in for a step that is never given, and that is not a proof. Zorn's lemma is the principle that replaces them. *If every unfinished partial object can be enlarged, and every growing chain of partial objects has a partial object above it, then there is one that cannot be enlarged, and it is complete.*

The chapter states the lemma and says why it is not proved here: it is equivalent to the axiom of choice of Chapter 3, and this volume proves only the half that gives choice. It turns the lemma into a single method of proof, the maximality template, and runs the template four times. The third run settles the question Section 3.4 left open: any two sets are comparable in size.

**What you need.** *Logic and Proof*, Chapters 1–8, in particular the rule \( \rulename{\exists E} \) (@fd1:def-rules-existential) and the catalogue of what is not allowed (@fd1:exm-not-allowed-catalogue), above all (N13), "an 'and so on' needs its step". From this volume: Section 4.3 on orders (@def-partial-order, @def-order-bounds, @def-greatest-element, @def-maximal-element, @prp-greatest-maximal, @prp-greatest-unique); Section 4.2 on equivalence relations (@def-equivalence-relation, @def-equivalence-class, @thm-classes-partition, @exm-reals-mod-integers); Chapter 3 on sizes and choice (@ax-choice, @def-card-le, @thm-schroder-bernstein, @prp-card-le-surjection, @prp-countable-image, @prp-union-two-countable, @thm-reals-uncountable-decimal); Section 2.5 on finite sets (@prp-subset-finite, @exm-hilbert-hotel, @prp-disjoint-union-count, @cor-pigeonhole-finite-sets, @prp-equinumerous-properties); Sections 2.1–2.2 (@thm-well-ordering, @thm-induction); Chapter 1 (@def-relation, @def-function). Proof methods: proof by contradiction (@exm-method-choosing-the-form, Chapter 2) and disproof by counterexample (@exm-method-counterexample, Chapter 1).

**Time.** About 10 hours on the core track (all of A, one B and one C per section, the exit checks); about 15 hours for everything.

## Roadmap

- **Chains and Zorn's lemma.** A pair-by-pair matching that cannot finish; chains in a partially ordered set, and why finitely many elements of the union of a chain of sets lie in one member; Zorn's lemma, why each hypothesis is needed, and why it is stated and not proved; the axiom of choice from Zorn's lemma, as the first run of the maximality template; a set of representatives for any equivalence relation.
- **Using Zorn's lemma.** Any two sets are comparable, so sizes satisfy trichotomy; every partial order extends to a total order, one added comparison at a time; and, in an optional last subsection, how the same template gives every vector space a basis (*Linear Algebra*, Section 1.8).

## Named moves

- **The maximality template** (@exm-method-maximality). Partial objects ordered by extension; the union of a chain is again a partial object; Zorn's lemma gives a maximal one; a maximal one is complete, since a missing piece would give a strictly larger partial object. (Section 5.1)
- **Finitely many, so one member** (@lem-chain-union). A condition that mentions finitely many elements of the union of a chain of sets is checked inside a single member of the chain. (Section 5.1)

## Threads

- **Comparing sizes.** Section 3.4 asked whether any two sets are comparable. Section 5.1 opens with a pair-by-pair matching that does not finish, and Section 5.2 finishes it with Zorn's lemma (@thm-cardinal-comparability).
- **Choice.** Chapter 3 stated the axiom of choice. Section 5.1 derives it from Zorn's lemma (@thm-choice-from-zorn), and *Axiomatic Set Theory* proves the converse.

## Summary

A chain is a subset of a partially ordered set on which the order is total (@def-chain), and finitely many elements of the union of a chain of sets lie in one member (@lem-chain-union). Zorn's lemma (@thm-zorn): a non-empty partially ordered set in which every non-empty chain has an upper bound has a maximal element, usually one of many and not a greatest one. It is stated without proof; it implies the axiom of choice (@thm-choice-from-zorn), and the converse belongs to *Axiomatic Set Theory*. The maximality template (@exm-method-maximality) gives a set of representatives for any equivalence relation (@exm-zorn-representatives), shows that any two sets are comparable in size (@thm-cardinal-comparability), so that exactly one of \( \card{A} < \card{B} \), \( \card{A} = \card{B} \), \( \card{B} < \card{A} \) holds (@cor-cardinal-trichotomy), and extends every partial order to a total order (@thm-order-extension), by adding one comparison at a time (@lem-one-step-order-extension).

Every object built in this chapter is shown to exist and none is written down: no formula is known for a set of representatives of \( \nR \) modulo \( \nQ \), for an injection between two arbitrary sets, or for a total order containing \( \subseteq \) on \( \powerset{\nR} \). Where a formula exists, as for divisibility on \( \nN \) (@exm-divisibility-linear-extension), it is the better proof.

## Terms

- **chain**: a subset in which any two elements are comparable (@def-chain).
- **linear extension**: a total order containing a given partial order; "linear order" is a synonym of "total order" (@thm-order-extension).
- **maximality template**: partial objects, unions of chains, Zorn's lemma, completeness of a maximal object (@exm-method-maximality).
- **partial choice function**: a set of pairs \( (i, x) \) with \( x \in A_i \), at most one for each index (@thm-choice-from-zorn).
- **partial matching**: a relation \( G \subseteq A \times B \) in which each element of \( A \) and of \( B \) occurs in at most one pair (@thm-cardinal-comparability).
- **set of representatives**: a set meeting every equivalence class in exactly one element (@exm-zorn-representatives).
- **Zorn's lemma**: a non-empty partially ordered set in which every non-empty chain has an upper bound has a maximal element (@thm-zorn).
