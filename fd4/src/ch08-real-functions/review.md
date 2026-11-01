# Chapter Review

## Summary

A real function is a set of pairs with one value over each input (@def-real-function), and the operations on functions are operations on values. A strictly monotone function is injective, reflects the order, and has a strictly monotone inverse (@thm-monotone-inverse). The values of a function on a non-empty set have a supremum and an infimum when they are bounded. They are found by bounding every value and then producing a witness, and the rules of @thm-sup-function-rules compare them. The floor makes the integer part a function (@def-floor-ceiling), and step functions are built from it. Two of the three borrowed facts about the exponential determine it (@thm-exp-unique), and the logarithm is its inverse. The power \( a^x \) is then defined for every positive \( a \) and real \( x \). It agrees with the roots of Chapter 1 (@prp-real-power-consistent) and obeys the laws of powers (@prp-real-power-laws).

What is open: continuity and limits of functions, which *Analysis on the Real Line* defines, and the integral, which *Integration, Series, and Function Spaces* defines; both test them on the functions of Section 8.6. Also open are the three borrowed facts about the exponential.

## Proof methods in this chapter

- **Read a graph as a set of pairs** (@exm-method-graph-pairs). To move a graph by a bijection of the plane, fix a point \( (x, y) \) and unwind "\( (x, y) \in \operatorname{graph} g \)" into "\( x \in D_g \) and \( y = g(x) \)". Introduced in Section 8.1.
- **Factor out \( y - x \)** (@exm-method-factor-difference). To show that \( f \) is strictly increasing, write \( f(y) - f(x) = (y - x)\,Q(x, y) \) and show \( Q > 0 \) for \( x < y \). Introduced in Section 8.2.
- **Bound every value, then find a witness** (@exm-method-sup-two-halves). To prove \( \sup_A f = M \), show \( f(x) \le M \) for every \( x \in A \). Then for each \( \varepsilon > 0 \) produce \( x \in A \) with \( f(x) > M - \varepsilon \). Introduced in Section 8.3.
- **Pin the floor by its inequality** (@exm-method-floor-inequality). To show \( \floor{A} = m \), check that \( m \) is an integer with \( m \le A < m + 1 \), or that \( j \le A \iff j \le m \) for every integer \( j \). Introduced in Section 8.4.
- **Squeeze, then close the gap by Archimedes** (@exm-method-archimedes-squeeze). To prove \( \sup S = L \), bound the set by \( L \) and find elements within \( C/n \) of it, with \( C \) fixed before \( n \) is chosen. Introduced in Section 8.5, where it proves the two-sided bound for the exponential.

## Terms

- **bounded function**: a function whose values on a set \( A \) satisfy \( \abs{f(x)} \le M \) for one \( M \) (@def-bounded-function).
- **ceiling**, **floor**, **fractional part**: \( \ceil{x} \), \( \floor{x} \) and \( x - \floor{x} \) (@def-floor-ceiling).
- **Dirichlet function**, **Thomae's function**: the indicator of the rationals, and the function that is \( 1/q \) at \( p/q \) in lowest terms and \( 0 \) at irrational numbers (@def-dirichlet-function, @def-thomae-function).
- **even function**, **odd function**: \( f(-x) = f(x) \) and \( f(-x) = -f(x) \) (@def-even-odd-function).
- **graph**: the set \( \{(x, f(x)) : x \in D\} \) (@def-real-function).
- **logarithm**: the inverse of the exponential, \( \log \colon (0, \infty) \to \nR \) (@def-logarithm).
- **monotone function**: an increasing or decreasing function, strictly or not (@def-monotone-function).
- **periodic function**: a function that has a period \( p \ne 0 \), with \( f(x + p) = f(x) \) for every \( x \) of its domain (@def-periodic-function).
- **real power**: \( a^x \) for \( a > 0 \) and \( x \in \nR \), defined through the exponential (@def-real-power).
- **step function**: a function on \( [a, b] \) that is constant on each open piece of a partition \( a = x_0 < \dots < x_n = b \) (@def-step-function).
- **supremum of a function**: the supremum of its values on a set, \( \sup_A f \) (@def-sup-of-function).

## Results used from earlier volumes

*Logic and Proof*:

- from Chapter 4, induction (@fd1:ax-induction), in Sections 8.1, 8.5 and 8.6;
- from Chapter 6, the negation of quantifiers (@fd1:prp-quantifier-negation), in Section 8.2.

*Sets and Functions*:

- from Chapter 1, ordered pairs, Cartesian products and relations (@fd2:def-ordered-pair, @fd2:def-cartesian-product, @fd2:def-relation);
- from Chapter 2, functions (@fd2:def-function), equality of functions (@fd2:prp-function-equality), the empty function (@fd2:prp-empty-function), images (@fd2:def-image), composition and its associativity (@fd2:def-composition, @fd2:prp-composition-associative), restrictions (@fd2:def-restriction-extension) and indicator functions (@fd2:def-indicator);
- from Chapter 2, inverses (@fd2:def-inverse-function, @fd2:thm-bijection-iff-inverse), composites of injections and surjections (@fd2:thm-composition-injective-surjective), and strictly monotone maps are injective (@fd2:prp-strictly-monotone-injective);
- from Chapter 2, the examples that this chapter revisits (@fd2:exm-piecewise-as-gluing, @fd2:exm-sets-of-numbers-as-images, @fd2:exm-maps-from-calculus, @fd2:exm-fraction-map, @fd2:exm-two-sided-inverses);
- from Chapter 3, induction in practice (@fd2:thm-induction), powers and their laws (@fd2:def-power, @fd2:prp-power-laws), finite sums (@fd2:def-sum-product), Bernoulli's inequality (@fd2:thm-bernoulli) and the largest term of a finite list (@fd2:prp-finite-max);
- from Chapter 4, finite sets and counting (@fd2:def-finite, @fd2:prp-subset-finite, @fd2:prp-disjoint-union-count, @fd2:cor-finite-size-unique), in Sections 8.4 and 8.6;
- from Chapter 5, the supremum of an ordered set (@fd2:def-order-supremum).

*Number Systems: From \(\nN\) to \(\nR\)*:

- from Chapter 2, commutative and ordered rings (@fd3:prp-ring-algebra, @fd3:def-ordered-ring-and-field, @fd3:thm-integers-ordered-ring) and the rules of an ordered ring (@fd3:prp-ordered-ring-rules), on nearly every page;
- from Chapter 3, reciprocals and order (@fd3:prp-reciprocal-order), the integer part of a rational (@fd3:prp-rational-integer-part) and the irrationality of \( \sqrt 2 \) (@fd3:thm-no-rational-square-two);
- from Chapter 4, the rules of an ordered field (@fd3:lem-field-fraction-rules, @fd3:prp-ordered-field-halves), the absolute value (@fd3:def-absolute-value-ordered-field, @fd3:prp-absolute-value-ordered-field), the Archimedean property (@fd3:prp-archimedean-reciprocal), the integer part (@fd3:prp-integer-part-ordered-field), \( \nQ \) inside an ordered field and dense in it (@fd3:thm-rationals-embed-ordered-field, @fd3:thm-rationals-dense-ordered-field) and limits of sequences (@fd3:def-sequence-limit-ordered-field);
- from Chapter 5, \( \nR \) as a complete ordered field (@fd3:thm-reals-complete-ordered-field, @fd3:def-complete-ordered-field) and two of its exercises that this chapter proves: infima by reflection (@fd3:exr-the-least-upper-bound-property-b1), in Section 8.3, and the density of the irrationals (@fd3:exr-rationals-inside-the-reals-c2), in Section 8.6;
- from Chapter 6, square roots and the Archimedean property in a complete ordered field (@fd3:prp-cof-square-roots, @fd3:thm-cof-complete-archimedean), and its uniqueness (@fd3:thm-cof-uniqueness), for the borrowed exponential of Section 8.5.

## Results used from earlier chapters

- Chapter 1: power laws and the difference of powers in a commutative ring (@prp-power-laws-commutative-ring, @lem-difference-of-powers) and the rules for roots (@lem-root-rules), in Section 8.2; roots (@lem-reals-nth-root), in Sections 8.2, 8.4, 8.5 and 8.6; the binomial theorem (@thm-binomial-commutative-ring), integer powers (@def-integer-power, @prp-integer-power-laws) and rational powers (@def-rational-power), in Section 8.5.
- Chapter 2: lowest terms of a fraction (@prp-rationals-lowest-terms), in Section 8.6.
- Chapter 3: the real numbers inside the complex numbers (@prp-reals-embed-complex) and the modulus of a real number (@prp-modulus-of-real), in Section 8.3; the borrowed cosine and sine (@ax-cosine-sine), for a comparison in Section 8.5.
- Chapter 5: groups (@exm-groups) and the subgroup test (@thm-subgroup-test), in Section 8.6.
- Chapters 6 and 7, only for polynomials: evaluation as a function (@def-polynomial-evaluation, @prp-polynomial-function-map), the identity theorem (@thm-polynomial-identity-from-values) and the root count (@thm-polynomial-root-count), in Sections 8.1 and 8.6.
- Chapter 7, for Section 8.3: the growth bound (@lem-complex-polynomial-growth) and the real root of an odd-degree polynomial (@cor-real-odd-degree-root).

Chapter 4 is not needed.

## Borrowed facts

Section 8.5 assumes three facts about the exponential function, @ax-exponential, and proves everything else about the exponential, the logarithm and real powers from them. Nothing in Sections 8.1–8.4 uses these facts, and neither does the part of Section 8.5 before them. *Integration, Series, and Function Spaces*, Chapter 7 constructs the exponential and proves the three facts.

## Threads

- **Order and inverses.** The inverse of a strictly monotone function gives roots as functions in Section 8.2. *Analysis on the Real Line* proves that a continuous injective function on an interval is strictly monotone. Section 8.2 shows why both hypotheses are needed.
- **Suprema of functions.** The rules of Section 8.3 are used again for the spread of values. *Integration, Series, and Function Spaces* calls it the oscillation and measures integrability with it.
- **Functions that resist drawing.** The functions of Section 8.6 and the distance to the integers of Section 8.4 are where the analysis volumes test continuity, differentiability and the integral. A function that is continuous everywhere and differentiable nowhere is built there from tents of the form \( \dist(2^k x, \nZ)/2^k \). The zigzag of Section 8.6 is replaced by the sine once the sine exists.
- **The exponential.** The exponential, borrowed in Section 8.5, is constructed in *Integration, Series, and Function Spaces*, Chapter 7. The sine and cosine borrowed in Section 3.5 are constructed there as well.
