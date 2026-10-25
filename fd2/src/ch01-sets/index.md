# Sets

Every definition of analysis is a sentence about sets and functions. "The supremum of \( A \) is the least element of the set of upper bounds of \( A \)." "A function is continuous if the preimage of every open set is open." *Logic and Proof*, Chapters 1 to 8 supplied the grammar of such sentences: the connectives, the quantifiers, and the prose that carries their rules. This chapter supplies the first nouns: sets and subsets, unions and intersections of whole families of sets, ordered pairs, products, and relations as sets of pairs. Chapter 2 then builds functions out of them. It is also where proofs start being about mathematics rather than about logic: each section teaches one method of proof on the material it introduces, starting in Section 1.1 with statements about integers proved straight from their definitions. And it is where the logic of the first eight chapters becomes visible inside mathematics. Inclusion is a "for every" around an "implies", a union is an "or", the union of a family is a "there exists", and a product is an "and". *The laws of sets are the laws of logic, read through membership*, and the chapter uses this from its second section to its last.

Two questions drive the chapter. The first is a puzzle of Section 1.1: *among any five points with integer coordinates, why do two have a midpoint with integer coordinates?* Parity reduces it to a principle about counting, which Chapter 4 proves. The second is a surprise: the naive rule "any property defines a set" is contradictory (Russell's paradox), so we must say which sets exist, and every set in this book is cut out of a set already given.

**What you need.** *Logic and Proof*, Chapters 1–8. From *Logic and Proof*, Chapters 1 and 2: the rules for the connectives and the derived laws used as rules, above all distributivity (@fd1:prp-distributivity), De Morgan's laws (@fd1:prp-de-morgan), an iff as two implications (@fd1:prp-iff-two-implications), the contrapositive (@fd1:prp-contrapositive), vacuous implication (@fd1:prp-vacuous-implication), and derived rules (@fd1:def-derived-rule). From *Logic and Proof*, Chapter 4: induction (@fd1:ax-induction), the standard equivalences (@fd1:prp-standard-equivalences) and completeness (@fd1:thm-completeness). From *Logic and Proof*, Chapters 5 and 6: the rules for "for every" and "there exists", bounded quantifiers (@fd1:def-bounded-quantifier) and their rules (@fd1:prp-bounded-quantifier-rules), the rules for equality (@fd1:def-rules-equality), unique existence (@fd1:def-unique-existence, @fd1:prp-unique-existence-use), and the laws for negating quantifiers. From *Logic and Proof*, Chapter 8: plain-prose proofs, the convention on which steps may be silent, and the catalogue of what is not allowed (@fd1:exm-not-allowed-catalogue). The number sets \( \nN \), \( \nZ \), \( \nQ \), \( \nR \) are used as familiar sets, with their school arithmetic and order.

**Time.** About 25 hours on the core track (all of A, one B and one C per section); about 35 hours for everything.

## Roadmap

- **Proofs from definitions.** Even, odd, divides and prime; a direct proof unwinds a definition and rewinds another; proofs by cases and without loss of generality; refuting a claim by one counterexample; a puzzle about lattice points that the book finishes in Chapter 4.
- **Sets, subsets and Russell's paradox.** What a set is allowed to be, equality by elements, the subset relation and the element-chasing proofs that establish it, equality by two inclusions, describing sets by a property cut out of an ambient set, the empty set, and why no set contains every set.
- **Unions, intersections, complements and families.** The set operations as the connectives read through membership, laws of sets proved by a chain of equivalences, the algebra of sets as propositional logic, power sets, unions and intersections of arbitrary families, and De Morgan's laws for families, including the empty one.
- **Ordered pairs, products and relations.** An object that remembers order, proofs of existence and uniqueness, the product \( A \times B \) and how it interacts with the set operations, and relations as sets of pairs.

## Named moves

All seven are method boxes; each section that introduces one cites it from then on.

- **Direct proof from a definition** (@exm-method-direct-proof). Unwind the hypothesis into its definition, naming each witness; say what the goal demands; close the gap by computation; write it forwards. (Section 1.1)
- **Proof by cases** (@exm-method-cases). Split on a disjunction you already have, such as even or odd, and reach the same goal in every case; "without loss of generality" when the cases are symmetric. (Section 1.1)
- **Disproof by counterexample, proof by example** (@exm-method-counterexample). One instance refutes a "for every"; one witness proves a "there exists". (Section 1.1)
- **Element-chasing** (@exm-method-element-chasing). To prove \( A \subseteq B \): "let \( x \in A \)", unwind the definition of \( A \), and rewind into the definition of \( B \). (Section 1.2)
- **Two inclusions** (@exm-method-double-inclusion). To prove \( A = B \): prove \( A \subseteq B \) and \( B \subseteq A \). (Section 1.2)
- **A chain of equivalences** (@exm-method-chain-of-iff). For \( L = R \): \( x \in L \iff \dots \iff x \in R \), each step a definition or a named law of logic. (Section 1.3)
- **Existence and uniqueness** (@exm-method-uniqueness). Produce one object, then show that any two are equal. (Section 1.4)

## Threads

- **The lattice points.** Section 1.1 asks why, among any five points with integer coordinates, two have a midpoint with integer coordinates, and states the principle the answer needs without using it. Section 4.1 proves the pigeonhole principle and comes back to the five points.
- **Russell to Cantor.** Russell's theorem in Section 1.2 is the first contradiction about sets: a set built to disagree with each candidate on the candidate itself. Cantor's theorem in Section 4.3 is the same shape of argument, as a theorem rather than a paradox.
- **Pairs to functions.** Section 1.4 ends with relations as sets of pairs (@def-relation). Section 2.1 defines a function as a relation with exactly one value at each input, and Chapter 5 returns to relations of every other kind.

## Summary

Statements about integers were proved from the definitions of even, odd and divides: divisibility is transitive (@prp-divides-transitive), and every integer is even or odd and not both (@thm-even-or-odd), the first proof by cases of the volume. Sets are equal when they have the same elements (@def-set-equality), inclusion is proved by element-chasing, and no set contains every set (@thm-russell). The laws of sets are the laws of propositional logic (@thm-set-algebra), and De Morgan's laws hold for families of any size (@thm-de-morgan-families). Ordered pairs remember order (@def-ordered-pair), products are sets of pairs (@def-cartesian-product), and a relation is a subset of a product (@def-relation).

What is open: what is a function, and what does it do to a set? Chapter 2 answers both, and shows why preimages respect every set operation while images respect only unions. The lattice-point puzzle waits for Chapter 4.

## Terms

- **Cartesian product**: \( A \times B \), the set of pairs \( (a, b) \) with \( a \in A \), \( b \in B \) (@def-cartesian-product).
- **complement of \( A \) in \( X \)**: \( X \setminus A \), for \( A \subseteq X \) (@def-set-operations).
- **difference**: \( A \setminus B \), the elements of \( A \) not in \( B \) (@def-set-operations).
- **disjoint**: \( A \cap B = \emptyset \) (@def-set-operations).
- **divides**: \( a \mid b \) if \( b = ka \) for some \( k \in \nZ \) (@def-divides).
- **empty set**: a set with no elements (@def-empty-set).
- **equality of sets**: the same elements (@def-set-equality).
- **even, odd**: \( n = 2k \), \( n = 2k + 1 \), for some \( k \in \nZ \) (@def-parity).
- **indexed family**: a set \( A_i \) for each \( i \in I \) (@def-indexed-family).
- **intersection**: \( A \cap B \); of a family, \( \bigcap_{i \in I} A_i \) (@def-set-operations, @def-family-union-intersection).
- **ordered pair**: \( (a, b) = (c, d) \) exactly when \( a = c \) and \( b = d \) (@def-ordered-pair).
- **power set**: the set of all subsets (@def-power-set).
- **prime**: an integer \( p \ge 2 \) whose only positive divisors are \( 1 \) and \( p \) (@def-prime).
- **relation**: a subset of \( A \times B \) (@def-relation).
- **specification**: \( \{ x \in A : P(x) \} \), a set cut out of a given set (@def-set-builder).
- **subset**: \( A \subseteq B \), every element of \( A \) is in \( B \) (@def-subset).
- **union**: \( A \cup B \); of a family, \( \bigcup_{i \in I} A_i \) (@def-set-operations, @def-family-union-intersection).
