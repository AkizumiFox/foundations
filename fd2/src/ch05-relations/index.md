# Relations

This chapter is about relations. When is "the same" a legitimate way to identify different things, as a clock identifies \( 2 \) with \( 14 \), or a function identifies two points with the same value? And what does "larger" mean when not everything can be compared, as with sets under inclusion or natural numbers under divisibility? The motivating problem: *in what sense is "\( 9 + 5 = 2 \) on a clock" a true statement?* The answer is an equivalence relation, the partition it cuts its set into, and a check that arithmetic on the pieces does not depend on which integer names a piece. Every function gives such a relation, "same value", and factors through its classes as a surjection, a bijection and an injection. For orders the answer is that "largest" splits into two notions, greatest and maximal, which agree only when every two elements are comparable. The last section reaches least upper bounds in a general partially ordered set (*Analysis on the Real Line*, Chapter 1's supremum is the case of \( \le \) on \( \nR \), and its axiom says that such suprema exist) and closes with well-ordered sets, the order-theoretic name for what Section 3.1 proved about \( \nN \).

Two methods of proof are new. Section 5.1 decides a property of a relation by a proof for all elements or by one witness against it, and records the verdicts in a table. Section 5.2 checks that a definition made through a representative does not depend on the representative: the check called well-definedness, promised in Section 2.1. Section 5.3 uses the methods of Chapters 1 to 4 without new scaffolding.

**What you need.** *Logic and Proof*, Chapters 1–8, and *Sets and Functions*, Chapters 1–4. From *Logic and Proof*: the rules for "there exists" (@fd1:def-rules-existential), equality (@fd1:def-rules-equality, @fd1:prp-equality-symmetric-transitive), negating bounded quantifiers and implications (@fd1:prp-bounded-quantifier-negation, @fd1:prp-negated-implication), De Morgan and double negation (@fd1:prp-de-morgan, @fd1:prp-double-negation), the catalogue of what a proof may not do (@fd1:exm-not-allowed-catalogue), squares and order (@fd1:thm-squares-order), and induction (@fd1:ax-induction). From Chapters 1 and 2: subsets, set equality and sets cut out by a property (@def-subset, @def-set-equality, @def-set-builder, @prp-empty-set-unique, @prp-subset-antisymmetric, @prp-subset-transitive); power sets and unions of families (@def-power-set, @def-family-union-intersection); ordered pairs and relations as sets of pairs (@def-ordered-pair, @def-relation); functions, their equality, and rules that are not functions (@def-function, @prp-function-equality, @exm-not-a-function); surjections and two-sided inverses (@def-surjective, @thm-bijection-iff-inverse); restriction and inclusion maps (@def-restriction-extension); gluing, for one exercise (@thm-gluing, @exm-piecewise-as-gluing); composites of injections and surjections (@thm-composition-injective-surjective); inverse functions (@def-inverse-function); the empty function (@prp-empty-function); images and preimages (@def-image, @def-preimage, @prp-image-preimage); Russell's theorem (@thm-russell); divisibility and parity (@def-divides, @prp-divides-transitive, @thm-even-or-odd); and the methods direct proof, cases, counterexample, double inclusion, uniqueness, injectivity and construct-and-verify (@exm-method-direct-proof, @exm-method-cases, @exm-method-counterexample, @exm-method-double-inclusion, @exm-method-uniqueness, @exm-method-injectivity, @exm-method-construct-and-verify). From Chapters 3 and 4: well-ordering and the least-element method (@thm-well-ordering, @cor-well-ordering-integers, @exm-method-least-element); the arithmetic of the integers (@prp-integers-closed, @lem-naturals-arithmetic); induction from a base (@thm-induction); the division algorithm and prime factors (@thm-division-algorithm, @thm-prime-factor); powers (@def-power, @prp-power-laws); finite maxima (@prp-finite-max); choosing between direct proof, contrapositive and contradiction (@exm-method-choosing-the-form); equinumerous, finite and infinite sets (@def-equinumerous, @prp-equinumerous-properties, @cor-finite-size-unique, @def-finite, @def-infinite, @prp-subset-finite, @exm-hilbert-hotel); disjoint unions of finite sets (@prp-disjoint-union-count). From Chapter 4: images of countable sets and the countability of \( \nZ \) (@prp-countable-image, @thm-integers-rationals-countable), for one review exercise. The arithmetic and order of \( \nR \) are school facts, as before.

**Time.** About 20 hours on the core track (all of A, one B and one C per section, the exit check 5.2 C1); about 25 hours for everything.

## Roadmap

- **Properties of relations.** Reflexive, symmetric, antisymmetric and transitive; deciding each one by a proof for all elements or by a single witness, with the verdicts collected in a table of eight relations; divisibility as the relation whose antisymmetry depends on the set.
- **Equivalence relations and partitions.** Relations that behave like equality, the proof that their classes partition the set and that every partition arises from exactly one of them (a correspondence proved in both directions), the integers modulo \( n \), the fibers of a function, and the factorization of every function as a quotient map, a bijection and an inclusion, and the method for checking that a definition on classes is well defined.
- **Partial orders, maximal and greatest elements.** Relations that behave like \( \le \), greatest elements against maximal ones and when the two agree, uniqueness from antisymmetry, least upper bounds in a partially ordered set, and well-ordered sets.

## Named moves

The first two are method boxes; Chapters 1–4's boxes are cited where they are used.

- **Prove or disprove each property** (@exm-method-relation-properties). A property that holds is a "for all": take arbitrary related elements and unwind. A property that fails needs one witness: an element, a pair or a triple. (Section 5.1)
- **Well-definedness** (@exm-method-well-definedness). For a rule that reads a representative, take two representatives of one class and show that the outputs agree. (Section 5.2)
- **Classes from a relation, a relation from classes.** Pass between an equivalence relation and its partition, whichever description makes the next step easier.
- **Uniqueness by antisymmetry.** Two candidates, each below the other, are equal: the method of @exm-method-uniqueness with (PO2) closing the gap. (Section 5.3)

## Threads

- **Same size.** The bijections of Section 2.4 say when two sets have the same size; Section 4.1 makes this a definition (@def-equinumerous); Section 5.2 meets it as an equivalence relation on the subsets of one set (@exm-same-size-subsets), and explains why it is not one on all sets.
- **The clock.** The arithmetic of \( \nZ/n \) in Section 5.2 returns in *Number Systems: From \(\nN\) to \(\nR\)*, Section 3.4, where \( \nZ/n \) becomes a ring.
- **Fractions.** Section 2.1 found that "send \( p/q \) to \( p \)" is not a function (@exm-not-a-function). Section 5.2 locates the failure with the factorization (@exm-fraction-map-factorization), and *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 2 builds \( \nQ \) as these classes.
- **Maximal elements and chains.** Section 5.3 ends by asking when a partially ordered set must have a maximal element; Chapter 6 answers with Zorn's lemma.

## Summary

A relation on a set may be reflexive, symmetric, antisymmetric or transitive (@def-relation-properties); each property is proved for all elements or refuted by one witness. The relations with the first, second and fourth are the equivalence relations (@def-equivalence-relation); their classes partition the set (@thm-classes-partition), and every partition comes from exactly one of them (@thm-partition-equivalence). Congruence modulo \( n \) gives \( \nZ/n = \{[0], \dots, [n - 1]\} \) (@prp-integers-mod-n), whose sum and product are well defined (@prp-congruence-arithmetic), while some rules on classes are not functions at all (@exm-ill-defined-class-map). The fibers of a function are the classes of "same value", one for each value (@prp-fibres-partition), and every function is a quotient map followed by a bijection and an inclusion (@thm-canonical-factorization). The relations with the first, third and fourth are the partial orders (@def-partial-order). A greatest element is unique (@prp-greatest-unique) and maximal, and the converse needs totality (@prp-greatest-maximal); a supremum is the least upper bound (@def-order-supremum), and under divisibility it is the least common multiple (@exm-divisibility-lcm).

What is open: in a partially ordered set where every chain has an upper bound, must there be a maximal element? Nothing proved so far decides it. Chapter 6 states the principle that does, Zorn's lemma, and puts it to work.

## Terms

- **antisymmetric**: \( x \mathrel{R} y \) and \( y \mathrel{R} x \) give \( x = y \) (@def-relation-properties).
- **block**: one of the sets of a partition (@def-partition).
- **bounded**: bounded above and below, that is, with an upper and a lower bound (@def-order-bounds).
- **comparable**: \( x \preceq y \) or \( y \preceq x \) (@def-partial-order).
- **congruent modulo \( n \)**: \( a \equiv b \pmod{n} \), that is, \( n \mid a - b \) (@def-congruence).
- **equivalence class**: \( [a] = \{ x \in X : x \sim a \} \) (@def-equivalence-class).
- **equivalence relation**: reflexive, symmetric and transitive (@def-equivalence-relation).
- **fiber**: the preimage \( f^{-1}(\{y\}) \) of one point (@exm-fibres-of-function).
- **greatest element**: an element of \( A \) above every element of \( A \) (@def-greatest-element).
- **infimum**: a greatest lower bound (@def-order-supremum).
- **least element**: an element of \( A \) below every element of \( A \) (@def-greatest-element).
- **lower bound**: an element of \( X \) below every element of \( A \) (@def-order-bounds).
- **maximal element**: an element of \( A \) with nothing in \( A \) strictly above it (@def-maximal-element).
- **minimal element**: an element of \( A \) with nothing in \( A \) strictly below it (@def-maximal-element).
- **partially ordered set**: a set with a reflexive, antisymmetric and transitive relation (@def-partial-order).
- **partition**: a set of non-empty, pairwise disjoint subsets whose union is the whole set (@def-partition).
- **quotient map**: \( x \mapsto [x] \), from \( X \) onto \( X/{\sim} \) (@def-quotient-set).
- **quotient set**: the set \( X/{\sim} \) of all equivalence classes (@def-quotient-set).
- **reflexive**: \( x \mathrel{R} x \) for every \( x \in X \) (@def-relation-properties).
- **representative**: an element of a class, which names the class (@def-equivalence-class).
- **strict part**: \( x \prec y \), that is, \( x \preceq y \) and \( x \ne y \) (@def-partial-order).
- **supremum**: a least upper bound (@def-order-supremum).
- **symmetric**: \( x \mathrel{R} y \) gives \( y \mathrel{R} x \) (@def-relation-properties).
- **total**: every two elements are comparable (@def-partial-order).
- **transitive**: \( x \mathrel{R} y \) and \( y \mathrel{R} z \) give \( x \mathrel{R} z \) (@def-relation-properties).
- **upper bound**: an element of \( X \) above every element of \( A \) (@def-order-bounds).
- **well defined**: a rule on classes whose output does not depend on the representative (@exm-method-well-definedness).
- **well-ordered set**: a partially ordered set whose order is total and in which every non-empty subset has a least element (@def-well-ordered-set).
