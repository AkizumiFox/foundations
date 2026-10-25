# Functions

Chapter 1 built sets, pairs and relations. This chapter is about the relations that matter most to analysis: those that send each input to exactly one output. *Is the rule "send \( p/q \) to \( p \)" a function on the rationals? When are two functions equal? If \( g \circ f \) is injective, which of \( f \) and \( g \) must be?* The chapter gives the questions exact statements, and each section teaches one method of proof for answering them: to prove a function injective, to prove it surjective, to cancel an injection or a surjection, to define a function by gluing pieces, to construct an inverse and verify it, and to unwind an image.

The chapter also holds the book's first motivating problem about sets. *For \( f(x) = x^2 \), is \( f(A \cap B) = f(A) \cap f(B) \)? Is \( f^{-1}(C \cap D) = f^{-1}(C) \cap f^{-1}(D) \)? Why is the second always true and the first not?* The answer is a single quantifier: membership in an image hides a "there exists", and membership in a preimage hides nothing. Preimages therefore respect every set operation, and images only unions. This asymmetry is why analysis defines continuity by preimages. Section 2.5 proves it.

Two constructions run through the chapter and return later. A subset of \( X \) is the same thing as a function \( X \to \{0, 1\} \), which Section 2.3 proves and Chapter 4 uses to count subsets and to compare \( \powerset{X} \) with \( X \). A bijection is a function with an inverse on both sides (Section 2.4), and Chapter 4 takes a bijection as the meaning of "the same size".

**What you need.** *Logic and Proof*, Chapters 1–8, and Chapter 1 of this volume. From *Logic and Proof*, Chapters 1 and 2: the contrapositive and its converse (@fd1:prp-contrapositive, @fd1:prp-contrapositive-converse), proof by contradiction (@fd1:def-rule-raa), double negation, excluded middle and the disjunctive syllogism (@fd1:prp-double-negation, @fd1:prp-excluded-middle, @fd1:prp-disjunctive-syllogism), De Morgan's laws (@fd1:prp-de-morgan), vacuous implication (@fd1:prp-vacuous-implication) and the negations of an iff (@fd1:exm-iff-negations). From *Logic and Proof*, Chapter 4, induction (@fd1:ax-induction). From *Logic and Proof*, Chapters 5 and 6: the rules for equality (@fd1:def-rules-equality), bounded quantifiers and their rules and negations (@fd1:def-bounded-quantifier, @fd1:prp-bounded-quantifier-rules, @fd1:prp-bounded-quantifier-negation) and unique existence (@fd1:def-unique-existence, @fd1:prp-unique-existence-use). From *Logic and Proof*, Chapter 8, the catalogue of what a proof may not do (@fd1:exm-not-allowed-catalogue). From Chapter 1: subsets and equality of sets (@def-subset, @def-set-equality, @prp-subset-antisymmetric), the empty set (@def-empty-set, @prp-empty-set-unique), sets cut out by a property (@def-set-builder), Russell's theorem (@thm-russell), the set operations and their laws (@def-set-operations, @thm-set-algebra), families of sets (@def-family-union-intersection), ordered pairs and products (@def-ordered-pair, @def-cartesian-product, @prp-product-set-laws), relations (@def-relation), parity (@thm-even-or-odd), and the method boxes for cases, counterexamples, chains of equivalences and uniqueness (@exm-method-cases, @exm-method-counterexample, @exm-method-chain-of-iff, @exm-method-uniqueness). The numbers \( \nN \), \( \nZ \), \( \nQ \) and \( \nR \) are used as familiar sets with their school arithmetic and order; every use of a school fact is named where it occurs, and Chapter 3 proves the facts about \( \nN \) and \( \nZ \).

**Time.** About 30 hours on the core track (all of A, one B and one C per section, the exit checks); about 40 hours for everything.

## Roadmap

- **Functions and composition.** A function as a graph with a declared codomain, when two functions are equal, the empty function, families, sequences and the set \( Y^X \) of all functions, and composition with its associative law.
- **Injections and surjections.** The two questions of injectivity and surjectivity, each with its method of proof (the second solved backwards and proved forwards); the squaring map as three different functions; what composition does to the two properties and which converses survive; the maps between sets that every construction supplies (inclusions, projections, the diagonal, complement); examples from algebra and calculus; and cancellation, which reads the two properties through composition.
- **Gluing and characteristic functions.** Restriction and extension; when pieces defined on parts of the domain make one function, and when that function is injective; indicator functions, which turn equations between sets into arithmetic; and the correspondence between subsets of \( X \) and functions \( X \to \{0, 1\} \).
- **Left, right and two-sided inverses.** Proofs that construct an object and then verify it: a left inverse exists exactly for injective maps (on a nonempty domain), a right inverse forces surjectivity, bijections are the maps with a two-sided inverse, and the question whether every surjection has a right inverse, which needs a new principle.
- **Images and preimages.** What a function does to sets, why preimages respect every operation and images only unions, where injectivity and surjectivity repair the failures, how to hunt for a counterexample, and sets of numbers such as \( -A \) and \( A + B \) as images.

## Named moves

The first five are method boxes; each section that introduces one cites it from then on.

- **Proving injectivity** (@exm-method-injectivity). From \( f(x_1) = f(x_2) \), derive \( x_1 = x_2 \). (Section 2.2)
- **Proving surjectivity** (@exm-method-surjectivity). Solve \( f(x) = y \) backwards on scrap paper; prove forwards: "let \( y \in Y \); put \( x \coloneqq \dots \)", and check. (Section 2.2)
- **Cancel an injection or a surjection** (@exm-method-cancel). To prove \( g = h \), find an injective \( f \) with \( f \circ g = f \circ h \), or a surjective \( f \) with \( g \circ f = h \circ f \), compute the composites, and cancel by @thm-cancellation. (Section 2.2)
- **Define a function by gluing** (@exm-method-gluing). Give the pieces and the formulas, check that the pieces cover the domain, and check that the formulas agree wherever two pieces meet. (Section 2.3)
- **Construct and verify** (@exm-method-construct-and-verify). Find where the object's values are forced and where they are free, define it, check it is the kind of object claimed, then verify the property. (Section 2.4)
- **Unwind the image.** "\( y \in f(A) \)" means "there is \( a \in A \) with \( f(a) = y \)": name the witness before using it. A preimage has no witness to name. (Section 2.5)

## Threads

- **The five strings.** Section 2.1 plants a game: given five strings of five symbols \( 0 \) or \( 1 \), write one not on the list. Section 4.3 comes back to it with the diagonal argument.
- **Subsets are functions.** Section 2.1 observes that subsets of \( X \) and functions \( X \to \{0, 1\} \) correspond; Section 2.3 proves it (@thm-power-set-two-power); Section 4.5 uses it to compare \( \powerset{X} \) with \( \{0, 1\}^X \) and to prove Cantor's theorem for power sets.
- **Right inverses.** Section 2.4 shows that a right inverse forces surjectivity and cannot build one in general. Chapter 6 adds the axiom of choice and gives every surjection a right inverse (@thm-surjection-right-inverse).
- **Same size.** The bijections of Section 2.4 are how the book says that two sets have the same size; Section 4.1 makes this a definition (@def-equinumerous), and Section 5.2 meets it again as an example of an equivalence-like relation.
- **Counting maps.** Section 2.2 proves that a function from a three-element set to a two-element set is not injective by listing the cases; Section 4.1 proves the pigeonhole principle and counts the injections between finite sets.

## Summary

A function is a graph with exactly one value at each input and a declared codomain (@def-function), and two functions are equal when they agree at every input (@prp-function-equality). Composition is associative (@prp-composition-associative). A composite of injections is injective and a composite of surjections is surjective (@thm-composition-injective-surjective); if \( g \circ f \) is injective then \( f \) is, and if it is surjective then \( g \) is (@prp-composite-partial-converse). A function is injective exactly when it cancels on the left, and surjective exactly when it cancels on the right (@thm-cancellation). Pieces defined on a cover of the domain and agreeing on the overlaps glue to exactly one function (@thm-gluing), and subsets of \( X \) correspond to functions \( X \to \{0, 1\} \) (@thm-power-set-two-power). A function has a left inverse exactly when it is injective, on a nonempty domain (@thm-left-inverse-iff-injective); a right inverse forces surjectivity (@prp-right-inverse-surjective); the bijections are exactly the maps with a two-sided inverse (@thm-bijection-iff-inverse). Preimages respect every set operation (@thm-preimage-operations), images respect unions (@thm-image-union), and injectivity repairs intersections (@thm-image-intersection).

What is open: does every surjection have a right inverse? Nothing proved so far builds one without a rule, and Chapter 6 adds the principle that does. Before that, Chapter 3 turns to the natural numbers, induction and recursion, and Chapter 4 to the sizes of sets.

## Terms

- **bijective**: injective and surjective (@def-bijective).
- **cancellation**: \( f \) is injective exactly when \( f \circ g = f \circ h \) implies \( g = h \), and surjective exactly when \( g \circ f = h \circ f \) implies \( g = h \) (@thm-cancellation).
- **composite**: \( g \circ f \), "\( g \) after \( f \)" (@def-composition).
- **restriction, extension**: \( f|_A \) is \( f \) cut down to \( A \); an extension of \( g \colon A \to Y \) is a function \( f \) on a larger domain with \( f|_A = g \) (@def-restriction-extension).
- **function**: a graph with exactly one value at each input, and a declared codomain (@def-function).
- **gluing**: the one function whose restriction to each piece is the given function on that piece (@thm-gluing).
- **image**: \( f(A) \), the values of \( f \) at points of \( A \) (@def-image).
- **indicator function**: \( \ind_A(x) = 1 \) for \( x \in A \) and \( 0 \) otherwise (@def-indicator).
- **injective**: different inputs, different outputs (@def-injective).
- **inverse, two-sided**: a left and a right inverse at once, written \( f^{-1} \) (@def-inverse-function).
- **left inverse, right inverse**: \( g \circ f = \id_X \); \( f \circ g = \id_Y \) (@def-left-right-inverse).
- **preimage**: \( f^{-1}(B) \), the inputs whose values lie in \( B \) (@def-preimage).
- **surjective**: every element of the codomain is a value (@def-surjective).
