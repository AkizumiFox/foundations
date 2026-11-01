# Chapter Review

## Summary

Finite sums obey the rules of @lem-ring-finite-sums in every commutative ring, and a sum whose terms are differences telescopes (@thm-telescoping). The binomial theorem holds in every commutative ring with coefficients defined by Pascal's rule (@thm-binomial-commutative-ring). In the real numbers it bounds a power from below by one or two of its terms (@cor-binomial-real). Bernoulli's inequality becomes strict (@lem-bernoulli-strict) and extends to products, and the arithmetic mean bounds the geometric mean (@thm-am-gm). With these, geometric sequences, \( n/r^n \) and \( r^n/n! \) tend to zero. Every non-negative real has a unique non-negative \( n \)-th root (@lem-reals-nth-root). The powers \( a^{m/n} \) of a positive real are well defined and obey the laws of powers (@prp-rational-power-laws).

What is open: powers with irrational exponents, which Chapter 8 defines through the exponential function, and the limit of the compound-interest sequence, which *Analysis on the Real Line* identifies.

## Proof methods in this chapter

- **Telescoping** (@exm-method-telescoping). When a sum has terms \( b_{k+1} - b_k \), the middle cancels and only the ends survive. Introduced in Section 1.1, where it sums reciprocals and squares and proves the difference of powers. Its "verification form" checks a guessed closed form instead of finding it.
- **Bound a product by a power** (@exm-method-am-gm). Replace the factors by their arithmetic mean, which is easy to compute, and let the arithmetic–geometric mean inequality turn the product into a power. Introduced in Section 1.3.
- **Keep the dominant term** (@exm-method-dominant-term). In a quotient of sums, keep the term that grows fastest and absorb the others into it from some index on. The quotient is then bounded by a quotient of single powers. Introduced in Section 1.4.
- **Bound a power from below** (@exm-method-power-lower-bound). Write a base above one as \( 1 + h \) and keep one term of the expansion, by Bernoulli or by the binomial theorem. This makes \( r^n \) at least a multiple of a power of \( n \). Introduced in Section 1.4, with exercises B1 and C2.
- **Recalled from earlier volumes.** Proving a limit from the definition (@fd3:exm-method-limit-from-definition); induction on the last term (@fd2:exm-method-induction-step); well-definedness (@fd2:exm-method-well-definedness). Constructing a point as a supremum, from *Number Systems: From \(\nN\) to \(\nR\)*, is run again in Section 1.5.

## Terms

- **arithmetic mean**, **geometric mean**: \( (a_1 + \dots + a_n)/n \) and \( \sqrt[n]{a_1 \cdots a_n} \), compared in @thm-am-gm.
- **binomial coefficient**: the natural number \( \binom{n}{k} \) given by Pascal's rule, never by a quotient of factorials (@def-binomial-coefficients).
- **integer power**: \( a^{-n} \coloneqq (a^{-1})^n \) for \( a \ne 0 \) in a field (@def-integer-power).
- **natural multiple**: \( n \cdot a \), the sum of \( n \) copies of \( a \), with its laws (@lem-natural-multiples).
- **\( n \)-th root**: the unique \( b \ge 0 \) with \( b^n = a \), written \( \sqrt[n]{a} \) (@lem-reals-nth-root).
- **rational power**: \( a^{m/n} \coloneqq (\sqrt[n]{a})^m \) for \( a > 0 \) (@def-rational-power).
- **telescoping sum**: a sum of terms \( b_{k+1} - b_k \), equal to the difference of its ends (@thm-telescoping).

## Results used from earlier volumes

Nothing in the chapter is borrowed: everything is proved from the results below. No other chapter of this volume is used, since this chapter comes first.

*Logic and Proof*, Chapter 4:

- induction (@fd1:ax-induction);
- strengthening a claim before inducting (@fd1:exm-strengthen-the-claim).

*Sets and Functions*, Chapter 3:

- the recursion theorem (@fd2:thm-recursion) and induction in practice (@fd2:thm-induction);
- finite sums and products (@fd2:def-sum-product) and powers (@fd2:def-power);
- the laws of powers (@fd2:prp-power-laws);
- the sum of the first \( n \) numbers (@fd2:prp-sum-first-n) and the geometric sum (@fd2:prp-geometric-sum);
- Bernoulli's inequality for real numbers (@fd2:thm-bernoulli), used in Sections 1.2–1.4.

*Number Systems: From \(\nN\) to \(\nR\)*:

- commutative rings and fields (@fd3:def-commutative-ring-and-field) and the algebra of a ring (@fd3:prp-ring-algebra), from Chapter 2;
- the rules of an ordered ring, including the multiples of Section 2.4 (@fd3:prp-ordered-ring-rules);
- the rules of an ordered field (@fd3:prp-ordered-field-halves), the absolute value (@fd3:prp-absolute-value-ordered-field) and fractions in a field (@fd3:lem-field-fraction-rules), from Chapter 4;
- the natural numbers inside an ordered field (@fd3:def-naturals-in-ordered-field, @fd3:prp-naturals-in-ordered-field);
- the Archimedean property (@fd3:prp-archimedean-reciprocal);
- limits of sequences (@fd3:def-sequence-limit-ordered-field) and how to prove one from the definition (@fd3:exm-method-limit-from-definition);
- the completeness of \( \nR \) (@fd3:thm-reals-complete-ordered-field, @fd3:def-complete-ordered-field), from Chapters 5 and 6;
- square roots in \( \nR \) (@fd3:prp-cof-square-roots) and a point constructed as a supremum (@fd3:exr-measuring-by-rationals-b2), which Section 1.5 runs for every exponent.

## Threads

- **From sums to Cauchy–Schwarz.** The rules for finite sums of Section 1.1 are what Chapter 9 uses to prove the Cauchy–Schwarz inequality. Chapter 4 uses the same sums with terms in a field.
- **Binomial theorem and Fermat.** The binomial coefficients are defined without division because Chapter 4 needs them in \( \nF_p \), where \( p! \) is zero. There \( (x + y)^p = x^p + y^p \).
- **Rational to real powers.** Section 1.5 stops at rational exponents. Chapter 8 defines \( a^x \) for every real \( x \) from the exponential function. *Analysis on the Real Line* proves the facts about the exponential that Chapter 8 borrows.
