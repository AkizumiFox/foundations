# Inequalities, Finite Sums, and Real Powers

Analysis proves that a sequence \( a_n \) tends to \( a \) by forcing an inequality: it bounds \( \abs{a_n - a} \) by something it can see tend to zero. To do that it needs sums it can rearrange, powers and roots it can estimate, and a few inequalities in which a product or a power is bounded by something simpler. Algebra needs the same sums, and the binomial theorem, in every commutative ring, including rings where one cannot divide. This chapter proves those rules once, in the generality both need, and shows how to turn them into estimates.

The chapter starts with finite sums and the binomial theorem, which hold in every commutative ring. It then proves inequalities for real numbers and uses them to estimate limits. It ends by constructing \( n \)-th roots and the powers \( a^{m/n} \) of a positive real. The word "real" in the title refers to these rational exponents; Chapter 8 extends the powers to every real exponent.

**What you need.**

- Induction, from *Logic and Proof*, Chapter 4 (@fd1:ax-induction).
- Recursion, finite sums and products, powers, and Bernoulli's inequality, from *Sets and Functions*, Chapter 3 (@fd2:thm-bernoulli).
- Commutative rings and ordered rings, from *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 2 (@fd3:prp-ordered-ring-rules).
- Ordered fields, the absolute value and limits of sequences, from *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 4 (@fd3:def-sequence-limit-ordered-field).
- The completeness of \( \nR \), from *Number Systems: From \(\nN\) to \(\nR\)*, Chapters 5 and 6 (@fd3:thm-reals-complete-ordered-field).

**Time.** About 15 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 25 hours for everything.

## Roadmap

- **Finite Sums.** The rules for finite sums and powers in any commutative ring, and telescoping, where the middle terms of a sum cancel (@thm-telescoping).
- **The Binomial Theorem.** Binomial coefficients defined by Pascal's rule, with no division, and the expansion of \( (x + y)^n \) in every commutative ring (@thm-binomial-commutative-ring).
- **Inequalities for Sums and Products.** A strict form of Bernoulli's inequality, and the inequality between the arithmetic and the geometric mean (@thm-am-gm), used to bound \( n! \).
- **Estimates for Limits.** Two ways to find the bound in \( \abs{a_n - a} < \varepsilon \), which prove that geometric sequences tend to zero (@prp-power-null) and that powers beat \( n \).
- **Roots and Rational Powers.** The \( n \)-th root of a non-negative real, constructed as a supremum, and the powers \( a^{m/n} \) with the laws of powers (@prp-rational-power-laws).
