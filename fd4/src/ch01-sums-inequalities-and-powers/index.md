# Inequalities, Finite Sums, and Real Powers

Analysis proves that a sequence \( a_n \) tends to \( a \) by forcing an inequality: it bounds \( \abs{a_n - a} \) by something it can see tend to zero. To do that it needs sums it can rearrange, powers and roots it can estimate, and a few inequalities in which a product or a power is bounded by something simpler. Algebra needs the same sums, and the binomial theorem, in every commutative ring, including rings where one cannot divide. This chapter proves those rules once, in the generality both need, and names the moves that turn them into estimates.

Section 1.1 states the rules for finite sums and powers in a commutative ring and teaches telescoping. Section 1.2 proves the binomial theorem, with coefficients defined by Pascal's rule and never by division. Section 1.3 sharpens Bernoulli's inequality and proves the inequality between the arithmetic and the geometric mean. Section 1.4 turns these into estimates for limits. Section 1.5 constructs \( n \)-th roots and the powers \( a^{m/n} \). The word "real" in the title is used for rational exponents of positive reals; Chapter 8 extends the powers to every real exponent.

**What you need.** *Logic and Proof*, Chapter 4: induction (@fd1:ax-induction), and one recalled example of strengthening a claim before inducting (@fd1:exm-strengthen-the-claim). *Sets and Functions*, Chapter 3: recursion (@fd2:thm-recursion), the definitions of finite sums, products and powers (@fd2:def-sum-product, @fd2:def-power), the laws of powers (@fd2:prp-power-laws), the sum of the first \( n \) numbers and the geometric sum (@fd2:prp-sum-first-n, @fd2:prp-geometric-sum), induction in practice (@fd2:thm-induction), and Bernoulli's inequality for real numbers (@fd2:thm-bernoulli), which Sections 1.2–1.4 use constantly. *Number Systems: From \(\nN\) to \(\nR\)*: from Chapter 2, commutative rings and their algebra (@fd3:def-commutative-ring-and-field, @fd3:prp-ring-algebra), the rules of an ordered ring, including the multiples of Section 2.4 (@fd3:prp-ordered-ring-rules); from Chapter 4, the rules of an ordered field and the absolute value (@fd3:prp-ordered-field-halves, @fd3:prp-absolute-value-ordered-field, @fd3:lem-field-fraction-rules), the natural numbers inside an ordered field (@fd3:def-naturals-in-ordered-field, @fd3:prp-naturals-in-ordered-field), the Archimedean property (@fd3:prp-archimedean-reciprocal), limits and the method for proving one from the definition (@fd3:def-sequence-limit-ordered-field, @fd3:exm-method-limit-from-definition); from Chapters 5 and 6, completeness of \( \nR \) and the construction of a point as a supremum (@fd3:thm-reals-complete-ordered-field, @fd3:def-complete-ordered-field, @fd3:prp-cof-square-roots, @fd3:exr-measuring-by-rationals-b2), which Section 1.5 runs for every exponent. Nothing from the other chapters of this volume is used; this chapter comes first.

**No borrowed facts.** Everything in the chapter is proved from the results above.

**Time.** About 15 hours on the core track (all of A, one B and one C per section, the exit checks); about 25 hours for everything.

## Roadmap

- **Finite Sums.** The laws of powers and of natural multiples in a commutative ring (@prp-power-laws-commutative-ring, @lem-natural-multiples); the rules for finite sums, which work in any commutative ring (@lem-ring-finite-sums); reindexing, comparing sums termwise and double sums over a rectangle (@prp-sum-reindex, @prp-sum-order, @prp-double-sum); telescoping sums and products (@thm-telescoping), with the method named and run on reciprocals and on the sum of squares; and the difference of powers (@lem-difference-of-powers), proved by telescoping.
- **The Binomial Theorem.** The binomial coefficients by Pascal's rule, with the absorption identity and the closed form with factorials as a consequence, not a definition (@def-binomial-coefficients, @prp-binomial-absorption, @prp-binomial-factorial); the binomial theorem in every commutative ring (@thm-binomial-commutative-ring); expansions, and the real-number corollaries that keep one or two terms for a lower bound (@cor-binomial-real); and the bound that \( 2^n \) beats \( n^2 \).
- **Inequalities for Sums and Products.** The strict Bernoulli inequality (@lem-bernoulli-strict); products of factors below one (@prp-weierstrass-product); the arithmetic–geometric mean inequality with its equality case (@thm-am-gm); the method of bounding a product by a power, used on \( n! \) and on the compound-interest sequence.
- **Estimates for Limits.** Two moves for finding the bound in \( \abs{a_n - a} < \varepsilon \): keep the dominant term of a quotient, and bound a power from below by one term of the binomial theorem. They prove that geometric sequences tend to zero (@prp-power-null), that powers beat \( n \) (@prp-linear-over-power-null), and that factorials beat powers of two.
- **Roots and Rational Powers.** The unique non-negative \( n \)-th root of a non-negative real, constructed as a supremum (@lem-reals-nth-root), and its rules (@lem-root-rules); integer powers in a field (@def-integer-power, @prp-integer-power-laws); rational powers, well defined and with the laws of powers (@def-rational-power, @prp-rational-power-well-defined, @prp-rational-power-laws); the arithmetic–geometric mean inequality for roots (@cor-am-gm-roots); and two root estimates that show \( \sqrt[n]{a} \to 1 \) (@prp-root-estimates).

## Named moves

- **Telescoping** (@exm-method-telescoping). When a sum has terms \( b_{k+1} - b_k \), the middle cancels and only the ends survive. Named in Section 1.1, where it sums reciprocals and squares and proves the difference of powers; the "verification form" checks a guessed closed form instead of finding it.
- **Bound a product by a power** (@exm-method-am-gm). Replace the factors by their arithmetic mean, which is easy to compute, and let the arithmetic–geometric mean inequality turn the product into a power. Named in Section 1.3.
- **Keep the dominant term** (@exm-method-dominant-term). In a quotient of sums, keep the term that grows fastest and absorb the others into it from some index on, so that the quotient is bounded by a quotient of single powers. Named in Section 1.4.
- **Bound a power from below** (@exm-method-power-lower-bound). Write a base above one as \( 1 + h \) and keep one term of the expansion, by Bernoulli or by the binomial theorem, which makes \( r^n \) at least a multiple of a power of \( n \). Named in Section 1.4, with the faded exercises B1 and C2.
- **Recalled from earlier volumes.** Proving a limit from the definition (@fd3:exm-method-limit-from-definition); induction on the last term (@fd2:exm-method-induction-step); well-definedness (@fd2:exm-method-well-definedness); construct a point as a supremum, run again in Section 1.5.

## Threads

- **From sums to Cauchy–Schwarz.** The rules for finite sums of Section 1.1 are what Chapter 9 uses to prove the Cauchy–Schwarz inequality, and Chapter 4 uses the same sums with terms in a field.
- **Binomial theorem and Fermat.** The binomial coefficients are defined without division because Chapter 4 needs them in \( \nF_p \), where \( p! \) is zero; there \( (x + y)^p = x^p + y^p \).
- **Rational to real powers.** Section 1.5 stops at rational exponents. Chapter 8 defines \( a^x \) for every real \( x \) from the exponential function, and *Analysis on the Real Line* proves the facts about the exponential that Chapter 8 borrows.

## Summary

Finite sums obey the rules of @lem-ring-finite-sums in every commutative ring, and a sum whose terms are differences telescopes (@thm-telescoping). The binomial theorem holds in every commutative ring with coefficients defined by Pascal's rule (@thm-binomial-commutative-ring), and in the real numbers it bounds a power from below by one or two of its terms (@cor-binomial-real). Bernoulli's inequality becomes strict (@lem-bernoulli-strict) and extends to products, and the arithmetic mean bounds the geometric mean (@thm-am-gm). With these, geometric sequences, \( n/r^n \) and \( r^n/n! \) tend to zero. Every non-negative real has a unique non-negative \( n \)-th root (@lem-reals-nth-root), and the powers \( a^{m/n} \) of a positive real are well defined and obey the laws of powers (@prp-rational-power-laws).

What is open: powers with irrational exponents, which Chapter 8 defines through the exponential function, and the limit of the compound-interest sequence, which *Analysis on the Real Line* identifies.

## Terms

- **arithmetic mean**, **geometric mean**: \( (a_1 + \dots + a_n)/n \) and \( \sqrt[n]{a_1 \cdots a_n} \), compared in @thm-am-gm.
- **binomial coefficient**: the natural number \( \binom{n}{k} \) given by Pascal's rule, never by a quotient of factorials (@def-binomial-coefficients).
- **integer power**: \( a^{-n} \coloneqq (a^{-1})^n \) for \( a \ne 0 \) in a field (@def-integer-power).
- **natural multiple**: \( n \cdot a \), the sum of \( n \) copies of \( a \), with its laws (@lem-natural-multiples).
- **\( n \)-th root**: the unique \( b \ge 0 \) with \( b^n = a \), written \( \sqrt[n]{a} \) (@lem-reals-nth-root).
- **rational power**: \( a^{m/n} \coloneqq (\sqrt[n]{a})^m \) for \( a > 0 \) (@def-rational-power).
- **telescoping sum**: a sum of terms \( b_{k+1} - b_k \), equal to the difference of its ends (@thm-telescoping).
