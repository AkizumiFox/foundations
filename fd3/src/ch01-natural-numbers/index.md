# The Natural Numbers

The two earlier volumes counted with the natural numbers and never asked what they are. *Logic and Proof* took induction as an axiom about numbers it did not build, and *Sets and Functions* described \( \nN \) as a subset of the school \( \nR \) and proved the recursion theorem there. A volume that builds the real numbers cannot start from a subset of \( \nR \). This chapter takes one assumption instead: there is a **Peano system**, a set with a start \( 0 \), a step \( \mathrm{S} \), and three demands on them (the start is not a step, the step never merges two numbers, and the only subset that contains the start and is closed under the step is everything). From that one assumption the chapter derives induction, the recursion theorem, addition and multiplication with their laws, the order, well-ordering, and powers.

A reader may fear that the choice of Peano system matters. Section 1.4 shows it does not: any two Peano systems are alike in exactly one way, so every statement about one is a statement about the other, and the \( \nN \) of this chapter, the \( \nN \) of *Logic and Proof* and the \( \nN \) of *Sets and Functions* are identified by a citing rule that says which earlier results carry over. Section 1.5, short and without proofs, says where a Peano system comes from: sets are the raw material, the natural numbers form the least inductive set, and pairs are sets. The proofs belong to *Axiomatic Set Theory*.

**What you need.** *Logic and Proof*, Chapter 4 (induction and strong induction: @fd1:ax-induction, @fd1:thm-strong-induction) and Chapter 8 (the catalogue of what a proof may not do, for the find-the-error exercises: @fd1:exm-not-allowed-catalogue). *Sets and Functions*, Chapter 1 (sets cut out by a property, ordered pairs and products: @fd2:def-set-builder, @fd2:def-ordered-pair, @fd2:def-cartesian-product, @fd2:prp-smallest-closed-set); *Sets and Functions*, Chapter 2 (functions, injective, surjective and bijective maps, composition, inverses: @fd2:def-function, @fd2:prp-function-equality, @fd2:def-injective, @fd2:def-surjective, @fd2:def-bijective, @fd2:def-composition, @fd2:thm-bijection-iff-inverse); *Sets and Functions*, Chapter 3 (induction, the recursion theorem, well-ordering and the three proof boxes: @fd2:thm-induction, @fd2:thm-recursion, @fd2:thm-well-ordering, @fd2:lem-naturals-arithmetic, @fd2:exm-method-induction-step, @fd2:exm-method-least-element, @fd2:exm-method-smallest-counterexample); *Sets and Functions*, Chapter 4 (finite and infinite sets, for the citing rule of Section 1.4: @fd2:def-finite, @fd2:def-infinite, @fd2:thm-finite-no-proper-copy); and *Sets and Functions*, Chapter 5 (partial orders: @fd2:def-partial-order).

**Time.** About 20 hours on the core track (all of A, one B and one C per section, the exit checks); about 30 hours for everything.

## Roadmap

- **Peano's Axioms and Induction.** What counting needs, and why the smallest closed subset of the school \( \nR \) does not do; a Peano system \( (M, e, s) \) and the assumption that one exists, which names its set \( \nN \); the three clauses (P3), (P4), (P5) shown independent by three small structures, one of them two copies of \( \nN \); induction in the set form and the statement form; and the predecessor, the proof that every natural number except \( 0 \) is a successor of exactly one, and that no number is its own successor.
- **The Recursion Theorem; Addition and Multiplication.** A function on \( \nN \) defined by a start and a step, existing and unique, by the smallest closed set of pairs; the sum and product defined by recursion, the numerals, successor cancellation, and the laws of arithmetic (associativity, commutativity, distributivity, cancellation) proved by induction on the recursion variable.
- **Order and Well-Ordering of the Natural Numbers.** \( m \le n \) when \( n = m + j \); the order and its compatibility with sum and product; a strict total order; every non-empty set has a least element; powers and the parity of \( n \cdot n \).
- **All Peano Systems Are Alike.** The categoricity theorem: any two Peano systems are isomorphic by exactly one isomorphism, which carries sum, product and order along; the identification of this \( \nN \) with the \( \nN \) of *Logic and Proof* and *Sets and Functions*, and the citing rule that lets a later chapter cite their results about \( \nN \).
- **Where \( \nN \) Comes From.** Seven axioms of set theory said in one line each, zero and the successor as sets, \( \omega \) as the least inductive set and why it is a Peano system, and pairs as sets. No proofs: they are in *Axiomatic Set Theory*.

## Named moves

- **Induction through a closed subset** (@exm-method-closed-subset). To prove a property of every natural number, let \( A \) be the set of numbers that have it; show \( 0 \in A \) and that \( n \in A \) gives \( \mathrm{S}(n) \in A \); then \( A = \nN \) by (P5). It is used for induction in Section 1.1 and for the uniqueness half of the recursion theorem. (Section 1.1)
- **Fix the others, induct on the recursion variable** (@exm-method-induct-on-recursion-variable). A law about a sum or product is proved by induction on the variable the definition is a recursion on, with the other variables fixed. It proves the laws of arithmetic in Section 1.2 and is reused in Section 1.3. (Section 1.2)
- **Translate \( \le \) into a sum.** Replace \( m \le n \) by \( n = m + j \) for some \( j \), and every order claim becomes a claim about sums, which Section 1.2 already controls. (Section 1.3)
- **Build by recursion, compare by induction** (@exm-method-build-by-recursion). To compare two structures, build the map between them by the recursion theorem and prove it respects everything by induction. It proves categoricity in Section 1.4.

## Threads

- **Induction.** *Logic and Proof* took it as an axiom, *Sets and Functions* proved it from a subset of \( \nR \), and here it is clause (P5); Section 1.4 shows the three agree.
- **Recursion.** The recursion theorem of Section 1.2 builds the sum, the product and the power, and Section 1.4 uses it to build the isomorphism between two Peano systems. Chapter 2 uses it again for multiples in a ring.
- **Well-ordering and least elements.** Section 1.3 proves it for \( \nN \); Section 2.4 extends it to sets of integers bounded below, and Section 2.5 uses it to find remainders.
- **The citing rule.** Section 1.4 says which results of *Logic and Proof* and *Sets and Functions* may be cited about this \( \nN \) and why; every later chapter cites through it with @cor-omega-identification.

## Summary

A Peano system is a set \( M \) with an element \( e \) and a function \( s \colon M \to M \) such that \( e \) is not a value of \( s \), \( s \) is injective, and the only subset of \( M \) that contains \( e \) and is closed under \( s \) is \( M \) (@def-peano-system). The chapter assumes one and calls its set \( \nN \) (@ax-natural-numbers); the last clause is induction (@thm-omega-induction), and every element but \( 0 \) has exactly one predecessor (@prp-peano-predecessor). A start and a step define exactly one function on \( \nN \) (@thm-omega-recursion), which defines the sum and the product (@def-omega-arithmetic); they satisfy cancellation (@cor-omega-successor-cancellation) and the usual laws (@thm-omega-arithmetic-laws). The order \( m \le n \) when \( n = m + j \) (@def-omega-order) is compatible with the operations (@prp-omega-order-arithmetic), is a strict total order (@thm-omega-order), and every non-empty set has a least element (@thm-omega-well-ordering); powers and parity follow (@prp-omega-powers-parity). Any two Peano systems are isomorphic by exactly one isomorphism (@thm-peano-categoricity), which preserves sums, products and order (@prp-isomorphism-preserves-arithmetic), so the \( \nN \) of the earlier volumes may be identified with this one (@cor-omega-identification). Section 1.5 describes, without proofs, how set theory supplies a Peano system: \( \omega \), the least inductive set, whose elements are the von Neumann numerals, with pairs built as sets.

What is open: nothing here lets us subtract \( 5 \) from \( 3 \). Chapter 2 builds the integers from pairs of natural numbers to fix that.

## Terms

- **Peano system**: a set with a start and a step satisfying (P3), (P4), (P5) (@def-peano-system).
- **natural number**, \( \nN \), \( 0 \), \( \mathrm{S} \), **successor**: the elements, start and step of the assumed Peano system (@ax-natural-numbers).
- **predecessor**: the one \( m \) with \( \mathrm{S}(m) = n \), for \( n \ne 0 \) (@prp-peano-predecessor).
- **defined by recursion**: determined by a start and a step (@thm-omega-recursion).
- **sum, product, numeral**: the operations defined by recursion, and \( 1 \coloneqq \mathrm{S}(0) \), \( 2 \coloneqq \mathrm{S}(1) \), and so on (@def-omega-arithmetic).
- **\( \le \), \( < \)**: the order on \( \nN \) (@def-omega-order).
- **well-ordering**: every non-empty subset has a least element (@thm-omega-well-ordering).
- **power**: \( b^n \) defined by recursion on \( n \) (@prp-omega-powers-parity).
- **isomorphism of Peano systems**: a bijection that carries start to start and step to step (@thm-peano-categoricity).
