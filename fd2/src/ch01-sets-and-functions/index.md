# Sets and Functions: Proofs from Definitions

Every definition of analysis is a sentence about sets and functions. "The supremum of \( A \) is the least element of the set of upper bounds of \( A \)." "A function is continuous if the preimage of every open set is open." *Logic and Proof*, Chapters 1 to 8 supplied the grammar of such sentences: the connectives, the quantifiers, and the prose that carries their rules. This chapter supplies the nouns: sets and subsets, unions and intersections of whole families of sets, ordered pairs and products, relations, functions, inverses, images and preimages. It is also where proofs start being about mathematics rather than about logic: each section teaches one method of proof on the material it introduces, starting in Section 1.1 with statements about integers proved straight from their definitions. And it is where the logic of the first eight chapters becomes visible inside mathematics. Inclusion is a "for every" around an "implies", a union is an "or", the union of a family is a "there exists", and a function is a "for every there exists exactly one". *The laws of sets are the laws of logic, read through membership*, and the chapter uses this from its second section to its last.

Two surprises drive the chapter. The first is that the naive rule "any property defines a set" is contradictory (Russell's paradox), so we must say which sets exist, and every set in this book is cut out of a set already given. The second is the chapter's motivating problem. *For \( f(x) = x^2 \), is \( f(A \cap B) = f(A) \cap f(B) \)? Is \( f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D) \)? Why is the second always true and the first not?* The answer is a single quantifier: membership in an image hides a "there exists", and membership in a preimage hides nothing. Preimages therefore respect every set operation, and images only unions. This asymmetry is why analysis defines continuity by preimages.

**What you need.** *Logic and Proof*, Chapters 1–8. From *Logic and Proof*, Chapters 1 and 2: the rules for the connectives and the derived laws used as rules, above all distributivity (@fd1:prp-distributivity), De Morgan's laws (@fd1:prp-de-morgan), an iff as two implications (@fd1:prp-iff-two-implications), the contrapositive (@fd1:prp-contrapositive), vacuous implication (@fd1:prp-vacuous-implication), and derived rules (@fd1:def-derived-rule). From *Logic and Proof*, Chapter 4: induction (@fd1:ax-induction), the standard equivalences (@fd1:prp-standard-equivalences) and completeness (@fd1:thm-completeness). From *Logic and Proof*, Chapters 5 and 6: the rules for "for every" and "there exists", bounded quantifiers (@fd1:def-bounded-quantifier) and their rules (@fd1:prp-bounded-quantifier-rules), the rules for equality (@fd1:def-rules-equality), unique existence (@fd1:def-unique-existence, @fd1:prp-unique-existence-use), and the laws for negating quantifiers. From *Logic and Proof*, Chapter 8: plain-prose proofs, the convention on which steps may be silent, and the catalogue of what is not allowed (@fd1:exm-not-allowed-catalogue). The number sets \( \nN \), \( \nZ \), \( \nQ \), \( \nR \) are used as familiar sets, with their school arithmetic and order.

**Time.** About 40 hours on the core track (all of A, one B and one C per section, the exit checks); about 55 hours for everything.

## Roadmap

- **Proofs from definitions.** Even, odd, divides and prime; a direct proof unwinds a definition and rewinds another; proofs by cases and without loss of generality; refuting a claim by one counterexample; a puzzle about lattice points that the book finishes in Chapter 2.
- **Sets, subsets and Russell's paradox.** What a set is allowed to be, equality by elements, the subset relation and the element-chasing proofs that establish it, equality by two inclusions, describing sets by a property cut out of an ambient set, the empty set, and why no set contains every set.
- **Unions, intersections, complements and families.** The set operations as the connectives read through membership, laws of sets proved by a chain of equivalences, the algebra of sets as propositional logic, power sets, unions and intersections of arbitrary families, and De Morgan's laws for families, including the empty one.
- **Ordered pairs, products and relations.** An object that remembers order, proofs of existence and uniqueness, the product \( A \times B \) and how it interacts with the set operations, and relations as sets of pairs.
- **Functions, composition, injections and surjections.** A function as a graph with a declared target, when two functions are equal, composition, and the two questions of injectivity and surjectivity, each with its method of proof (the second solved backwards and proved forwards), with the squaring map as three different functions.
- **Left, right and two-sided inverses.** Proofs that construct an object and then verify it: a left inverse exists exactly for injective maps (on a nonempty domain), a right inverse forces surjectivity, bijections are the maps with a two-sided inverse, and the question whether every surjection has a right inverse, which needs a new principle.
- **Images and preimages.** What a function does to sets, why preimages respect every operation and images only unions, where injectivity and surjectivity repair the failures, how to hunt for a counterexample, and sets of numbers such as \( -A \) and \( A + B \) as images.

## Named moves

The first ten are method boxes; each section that introduces one cites it from then on.

- **Direct proof from a definition** (@exm-method-direct-proof). Unwind the hypothesis into its definition, naming each witness; say what the goal demands; close the gap by computation; write it forwards. (Section 1.1)
- **Proof by cases** (@exm-method-cases). Split on a disjunction you already have, such as even or odd, and reach the same goal in every case; "without loss of generality" when the cases are symmetric. (Section 1.1)
- **Disproof by counterexample, proof by example** (@exm-method-counterexample). One instance refutes a "for every"; one witness proves a "there exists". (Section 1.1)
- **Element-chasing** (@exm-method-element-chasing). To prove \( A \subseteq B \): "let \( x \in A \)", unwind the definition of \( A \), and rewind into the definition of \( B \). (Section 1.2)
- **Two inclusions** (@exm-method-double-inclusion). To prove \( A = B \): prove \( A \subseteq B \) and \( B \subseteq A \). (Section 1.2)
- **A chain of equivalences** (@exm-method-chain-of-iff). For \( L = R \): \( x \in L \iff \dots \iff x \in R \), each step a definition or a named law of logic. (Section 1.3)
- **Existence and uniqueness** (@exm-method-uniqueness). Produce one object, then show that any two are equal. (Section 1.4)
- **Proving injectivity** (@exm-method-injectivity). From \( f(x_1) = f(x_2) \), derive \( x_1 = x_2 \). (Section 1.5)
- **Proving surjectivity** (@exm-method-surjectivity). Solve \( f(x) = y \) backwards on scrap paper; prove forwards: "let \( y \in Y \); put \( x \coloneqq \dots \)", and check. (Section 1.5)
- **Construct and verify** (@exm-method-construct-and-verify). Find where the object's values are forced and where they are free, define it, check it is the kind of object claimed, then verify the property. (Section 1.6)
- **Unwind the image.** "\( y \in f(A) \)" means "there is \( a \in A \) with \( f(a) = y \)": name the witness before using it. A preimage has no witness to name. (Section 1.7)
- **Refute with a small witness.** The method of @exm-method-counterexample for statements about sets and functions: a two- or three-element set, the map \( x \mapsto x^2 \), the empty set.

## Threads

- **The lattice points.** Section 1.1 asks why, among any five points with integer coordinates, two have a midpoint with integer coordinates, and states the principle the answer needs without using it. Section 2.5 proves the pigeonhole principle and comes back to the five points.
- **The five strings.** Section 1.5 plants a game: given five strings of five symbols \( 0 \) or \( 1 \), write one not on the list. Section 3.3 comes back to it with the diagonal argument.
- **Russell to Cantor.** Russell's theorem in Section 1.2 is the first contradiction about sets: a set built to disagree with each candidate on the candidate itself. Cantor's theorem in Section 3.3 is the same shape of argument, as a theorem rather than a paradox.
- **Same size.** The bijections of Section 1.6 are how the book says that two sets have the same size; Section 2.5 makes this a definition, and Section 4.2 meets it again as an example of an equivalence-like relation.

## Summary

Statements about integers were proved from the definitions of even, odd and divides: divisibility is transitive (@prp-divides-transitive), and every integer is even or odd and not both (@thm-even-or-odd), the first proof by cases of the volume. Sets are equal when they have the same elements (@def-set-equality), inclusion is proved by element-chasing, and no set contains every set (@thm-russell). The laws of sets are the laws of propositional logic (@thm-set-algebra), and De Morgan's laws hold for families of any size (@thm-de-morgan-families). A function has a left inverse exactly when it is injective, on a nonempty domain (@thm-left-inverse-iff-injective); a right inverse forces surjectivity (@prp-right-inverse-surjective); the bijections are exactly the maps with a two-sided inverse (@thm-bijection-iff-inverse). Preimages respect every set operation (@thm-preimage-operations), images respect unions (@thm-image-union), and injectivity repairs intersections (@thm-image-intersection).

What is open: does every surjection have a right inverse? Nothing proved so far builds one without a rule, and Chapter 3 adds the principle that does. Before that, Chapter 2 turns to the natural numbers, induction and finite sets, and finishes the lattice-point puzzle.

## Terms

- **bijective**: injective and surjective (@def-bijective).
- **Cartesian product**: \( A \times B \), the set of pairs \( (a, b) \) with \( a \in A \), \( b \in B \) (@def-cartesian-product).
- **complement of \( A \) in \( X \)**: \( X \setminus A \), for \( A \subseteq X \) (@def-set-operations).
- **composite**: \( g \circ f \), "\( g \) after \( f \)" (@def-composition).
- **difference**: \( A \setminus B \), the elements of \( A \) not in \( B \) (@def-set-operations).
- **disjoint**: \( A \cap B = \emptyset \) (@def-set-operations).
- **divides**: \( a \mid b \) if \( b = ka \) for some \( k \in \nZ \) (@def-divides).
- **empty set**: a set with no elements (@def-empty-set).
- **equality of sets**: the same elements (@def-set-equality).
- **even, odd**: \( n = 2k \), \( n = 2k + 1 \), for some \( k \in \nZ \) (@def-parity).
- **function**: a graph with exactly one value at each input, and a declared codomain (@def-function).
- **image**: \( f(A) \), the values of \( f \) at points of \( A \) (@def-image).
- **indexed family**: a set \( A_i \) for each \( i \in I \) (@def-indexed-family).
- **injective**: different inputs, different outputs (@def-injective).
- **intersection**: \( A \cap B \); of a family, \( \bigcap_{i \in I} A_i \) (@def-set-operations, @def-family-union-intersection).
- **inverse, two-sided**: a left and a right inverse at once, written \( f^{-1} \) (@def-inverse-function).
- **left inverse, right inverse**: \( g \circ f = \id_X \); \( f \circ g = \id_Y \) (@def-left-right-inverse).
- **ordered pair**: \( (a, b) = (c, d) \) exactly when \( a = c \) and \( b = d \) (@def-ordered-pair).
- **power set**: the set of all subsets (@def-power-set).
- **preimage**: \( f^{-1}(B) \), the inputs whose values lie in \( B \) (@def-preimage).
- **prime**: an integer \( p \ge 2 \) whose only positive divisors are \( 1 \) and \( p \) (@def-prime).
- **relation**: a subset of \( A \times B \) (@def-relation).
- **specification**: \( \{ x \in A : P(x) \} \), a set cut out of a given set (@def-set-builder).
- **subset**: \( A \subseteq B \), every element of \( A \) is in \( B \) (@def-subset).
- **surjective**: every element of the codomain is a value (@def-surjective).
- **union**: \( A \cup B \); of a family, \( \bigcup_{i \in I} A_i \) (@def-set-operations, @def-family-union-intersection).
