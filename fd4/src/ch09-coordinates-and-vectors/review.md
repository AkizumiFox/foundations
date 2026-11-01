# Chapter Review

## Summary

\( \nR^n \) is the set of lists of \( n \) reals (@def-real-n-space). Addition and scaling coordinate by coordinate obey the laws of a vector space (@prp-vector-space-laws-rn). The dot product is symmetric, linear in each place and positive on non-zero vectors (@prp-dot-product-laws-rn). The norm \( \norm{x} = \sqrt{\inner{x}{x}} \) and the distance \( \norm{x - y} \) obey Pythagoras, the parallelogram law and polarization (@prp-pythagoras-rn, @prp-parallelogram-law-rn, @prp-polarization-rn). Cauchy–Schwarz, \( \abs{\inner{x}{y}} \le \norm{x}\norm{y} \), holds with equality exactly for parallel vectors (@thm-cauchy-schwarz-rn), and it gives the triangle inequality (@thm-triangle-inequality-rn). The projection of \( x \) onto \( y \) is the closest point of the line \( \nR y \) (@thm-projection-closest-point). The quotient \( \inner{x}{y}/(\norm{x}\norm{y}) \) lies in \( [-1, 1] \) (@prp-angle-cosine-properties).

What is open: the angle itself, which needs the function \( \cos \). Lines, hyperplanes and convex sets come next, in Chapter 10, built from this chapter. Distance and convergence for abstract spaces are taken up by the analysis volumes.

## Proof methods in this chapter

- **Work coordinatewise** (@exm-method-coordinatewise). To prove an equation between vectors, fix a coordinate \( k \) and compute the \( k \)-th coordinate of each side. Prove the equation in \( \nR \), naming the law used, and conclude that the vectors agree in every place. Introduced in Section 9.2.
- **Expand the square** (@exm-method-expand-the-square). Lengths are roots of sums, and their squares are dot products. Compare squares, write \( \norm{v}^2 = \inner{v}{v} \), expand by linearity and symmetry, and return to lengths by comparing squares. Introduced in Section 9.4, where it proves the Pythagorean theorem and the parallelogram law.
- **Normalize** (@exm-method-normalize). If a statement is homogeneous in \( x \) and in \( y \), settle \( x = 0 \) and \( y = 0 \) separately and prove it for the unit vectors \( x/\norm{x} \) and \( y/\norm{y} \). Introduced in Section 9.5, where it proves Cauchy–Schwarz.
- **Subtract the projection** (@exm-method-subtract-the-projection). Given \( x \) and \( y \ne 0 \), split \( x \) into its projection onto \( y \) and the remainder, which is orthogonal to \( y \). Introduced in Section 9.6, where it proves the closest-point theorem.

## Terms

- **box**: the product \( [a_1, b_1] \times \dots \times [a_n, b_n] \) of closed intervals (@def-box-rn).
- **cosine of the angle**: \( \inner{x}{y}/(\norm{x}\norm{y}) \) for non-zero \( x \), \( y \) (@def-angle-cosine-rn).
- **distance**: \( \norm{x - y} \) (@def-distance-rn).
- **dot product**: \( \inner{x}{y} = \sum_k x_k y_k \) (@def-dot-product-rn).
- **norm**, **length**: \( \norm{x} = \sqrt{\inner{x}{x}} \) (@def-norm-rn).
- **orthogonal vectors**: vectors with dot product \( 0 \) (@def-orthogonal-rn).
- **parallel vectors**: vectors one of which is a real multiple of the other (@def-parallel-rn).
- **projection onto a line**: \( \operatorname{proj}_y x = \frac{\inner{x}{y}}{\norm{y}^2}\, y \) (@def-projection-rn).
- **standard vectors**: the vectors \( e_1, \dots, e_n \) with a single coordinate \( 1 \) (@def-standard-basis-rn).
- **unit vector**: a vector of norm \( 1 \) (@def-unit-vector-rn).

## Results used from earlier volumes

*Logic and Proof*, Chapter 8:

- the catalogue of what a proof may not do (@fd1:exm-not-allowed-catalogue), for the find-the-error exercises of Sections 9.3 and 9.4.

*Sets and Functions*:

- ordered pairs (@fd2:def-ordered-pair), Cartesian products (@fd2:def-cartesian-product) and bijections (@fd2:def-bijective), in Section 9.1;
- recursion (@fd2:thm-recursion) and induction (@fd2:thm-induction);
- finite sums and products (@fd2:def-sum-product) and maxima of finite sets (@fd2:prp-finite-max).

*Number Systems: From \(\nN\) to \(\nR\)*:

- the rules of an ordered ring (@fd3:prp-ordered-ring-rules) and an ordered field (@fd3:prp-ordered-field-halves), on nearly every page;
- the absolute value (@fd3:def-absolute-value-ordered-field, @fd3:prp-absolute-value-ordered-field);
- the rules of a commutative ring (@fd3:def-commutative-ring-and-field, @fd3:prp-ring-algebra) and of fractions in a field (@fd3:lem-field-fraction-rules);
- \( \nR \) as a complete ordered field (@fd3:thm-reals-complete-ordered-field) and its square roots (@fd3:prp-cof-square-roots), which define the length.

## Results used from earlier chapters

- Chapter 1, Section 1.1: the rules for finite sums (@lem-ring-finite-sums), comparing sums termwise (@prp-sum-order) and double sums over a rectangle (@prp-double-sum), for the dot product laws and Cauchy–Schwarz for sums.
- Chapter 3, for Section 9.4: the complex numbers as pairs (@def-complex-numbers, @prp-reals-embed-complex), the modulus and the conjugate (@def-conjugate-modulus, @prp-modulus-of-real, @thm-conjugate-properties).
- Chapter 3, for Section 9.5: the triangle inequality in \( \nC \) and its variants (@thm-complex-triangle-inequality, @cor-complex-triangle-variants, @lem-real-part-at-most-modulus).
- Chapter 3, for Section 9.6 only: the unit circle and polar form (@prp-polar-form) and the borrowed cosine and sine (@ax-cosine-sine).
- For the review exercises of Section 9.6 only: fields (@def-field), groups and homomorphisms with their kernels (@def-group, @def-group-homomorphism, @prp-homomorphism-injective-iff-kernel-trivial), degree and evaluation of polynomials (@def-degree, @thm-evaluation-respects-operations, @thm-polynomial-root-count), and monotone functions (@def-monotone-function, @exm-method-factor-difference).

## Borrowed facts

The chapter borrows nothing new. It defines the cosine of the angle between two vectors as a quotient, so it needs no function \( \cos \) and no \( \pi \). Section 9.6 mentions the facts about cosine and sine borrowed in Section 3.5 only once, to compare the quotient with the cosine of a number \( \theta \) when \( n = 2 \).

## Threads

- **Same statement, three places.** The triangle inequality for the plane is proved in Section 3.3 for \( \nC \) and again in Section 9.5 for every \( \nR^n \), by a different route. Cauchy–Schwarz is stated here only for \( \nR^n \) and for finite sums. The linear algebra volumes prove it for abstract inner product spaces.
- **Chapter 10 on distances.** Hyperplanes \( \inner{a}{x} = c \), nearest points on lines and hyperplanes, and betweenness stated by distances all come from the dot product and the projection of this chapter.
- **The angle.** Section 9.6 defines only the cosine of the angle between two vectors. An angle \( \theta \) with that cosine needs the function \( \cos \). For \( n = 2 \) Chapter 3 supplies it through polar form, and for general \( n \) the analysis volumes do.
