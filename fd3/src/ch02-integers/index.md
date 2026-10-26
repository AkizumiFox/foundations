# The Integers

In the natural numbers, "subtract \( 5 \) from \( 3 \)" has no answer. The school integers answer it by a stroke of the pen: add negative numbers, and trust that everything still works. This chapter builds them instead, with no new assumption. A pair \( (a, b) \) of natural numbers records the difference \( a - b \) without performing it, two pairs record the same difference when \( a + d = b + c \), and an integer is a class of such pairs. The quotient set of *Sets and Functions*, Section 5.2 makes this a set, and the number of pairs per integer is infinite, so nothing about an integer may depend on which pair we use to write it.

That is the danger of the whole chapter. A formula that looks fine on pairs can give different answers for two pairs of the same class, and then it is no operation on integers. Section 2.2 proves one lemma that tells us what to check, and the check is done once, one argument at a time. With the operations in hand, Section 2.3 names the structure they form, a commutative ring, and checks every law by pushing it down to the natural numbers. Section 2.4 adds the order, from one choice, the set of positive elements, and proves the rules for inequalities that every later chapter uses. Section 2.5 closes with division with remainder and the even-odd split. At the end \( \nZ \) is an ordered ring in which every set bounded below has a least element, and it is still not a field.

**What you need.** Chapter 1: induction and the recursion theorem on \( \nN \) (@thm-omega-induction, @thm-omega-recursion), with the citing rule of Section 1.4 for results of the earlier volumes (@cor-omega-identification), the arithmetic and order of \( \nN \) (@def-omega-arithmetic, @cor-omega-successor-cancellation, @thm-omega-arithmetic-laws, @prp-omega-order-arithmetic, @thm-omega-order), well-ordering (@thm-omega-well-ordering), and parity (@prp-omega-powers-parity). *Sets and Functions*: ordered pairs, products, functions and their equality (@fd2:def-ordered-pair, @fd2:def-cartesian-product, @fd2:def-function, @fd2:prp-function-equality); equivalence relations, classes, quotient sets and the partition theorem, with the method for checking a rule on representatives, from its Section 5.2 (@fd2:def-equivalence-relation, @fd2:def-equivalence-class, @fd2:def-quotient-set, @fd2:thm-classes-partition, @fd2:exm-method-well-definedness, @fd2:exm-ill-defined-class-map); the least-element method (@fd2:exm-method-least-element); for Section 2.4's C1 only, finite and infinite sets from its Section 4.1 (@fd2:def-finite, @fd2:def-infinite, @fd2:cor-pigeonhole-finite-sets, @fd2:prp-subset-finite); and, for Section 2.5 only, the school facts about division and parity that it compares with (@fd2:thm-division-algorithm, @fd2:thm-even-or-odd, @fd2:def-divides, @fd2:def-prime). *Logic and Proof*: the square of an even integer (@fd1:thm-square-even-implies-even), for a comparison in Section 2.5.

**Time.** About 20 hours on the core track (all of A, one B and one C per section, the exit checks); about 25 hours for everything.

## Roadmap

- **The Integers as Classes of Pairs.** Why \( 3 - 5 \) needs a new kind of number; pairs of natural numbers with \( (a, b) \sim (c, d) \) when \( a + d = b + c \), checked to be an equivalence relation; \( \nZ \) as the quotient set; pictures of the classes on a staircase; and the normal form, by which every class contains exactly one pair of the form \( (n, 0) \) or \( (0, n) \).
- **Well-Definedness, and the Arithmetic of the Integers.** The lemma on functions defined on classes through representatives, with its one-argument-at-a-time check; the sum, product and negative of integers, shown well defined; rules that look like functions and are not; and the copy of \( \nN \) inside \( \nZ \), which turns the class \( [(a, b)] \) into the difference \( a - b \).
- **Commutative Rings; the Integers Are One.** The ring and field axioms; the integers a commutative ring with \( 1 \ne 0 \), every law checked by the move that reduces it to the level below; the algebra that follows from the axioms alone.
- **Ordered Rings and the Rules for Inequalities.** Ordered rings and fields; an order from a positive set; the order of \( \nZ \); the rules for inequalities, including multiplication by a positive and by a negative element; multiples; least and greatest elements of sets of integers; and a ring that cannot be ordered.
- **Division with Remainder.** Divisibility on the constructed integers and its rules; division with remainder, existence and uniqueness, with the existence proof by a least element; and even and odd integers, exactly one of the two.

## Named moves

- **Check on representatives, one argument at a time** (@exm-method-one-argument-at-a-time, with @fd2:exm-method-well-definedness and @thm-well-defined-on-classes). Change one representative with the other fixed; each change is one identity at the level below. A formula symmetric in its two inputs gets the second change free. (Section 2.2)
- **Reduce to the level below** (@exm-method-reduce-to-level-below). Write a law about classes on representatives; the two sides become the same pair, or two related pairs, by an identity in \( \nN \). (Section 2.3)
- **Turn the comparison into one positive element** (@exm-method-one-positive-element). To compare \( a \) and \( b \), look at \( b - a \) and ask whether it is in the positive set. (Section 2.4)
- **Order from a positive set** (@prp-order-from-positives). Say which elements are positive, check (P1) and (P2), and read off every rule for inequalities. (Section 2.4)
- **Least element** (@fd2:exm-method-least-element). A set of integers bounded below has a least element; it finds the remainder in Section 2.5 and the integer part in Chapter 3. (Sections 2.4 and 2.5)

## Threads

- **Well-definedness, the level below and positive sets.** Section 2.1 makes integers from pairs of naturals, Section 3.1 makes rationals from pairs of integers, and Chapter 5 makes real numbers from classes of sequences of rationals, each time by the lemma and the check of Section 2.2, the move of Section 2.3 and the order of Section 2.4.
- **Least elements.** Chapter 1 proves it for \( \nN \), Section 2.4 for sets of integers bounded below, Section 2.5 uses it for the remainder, and *Algebraic Preliminaries*, Chapter 1 takes it up for divisibility and the Euclidean algorithm.
- **The copy of \( \nN \).** Section 2.2 identifies \( n \) with \( [(n, 0)] \); every later chapter writes \( \nN \subseteq \nZ \subseteq \nQ \) without further comment.

## Summary

A pair \( (a, b) \) of natural numbers records the difference \( a - b \), and the relation \( a + d = b + c \) is an equivalence relation (@prp-integer-pairs-equivalence); its classes form \( \nZ \) (@def-integers-as-classes), and each class has a normal form \( (n, 0) \) or \( (0, n) \) (@prp-integer-normal-form). A rule defined on classes through representatives is a function when it passes the check of @thm-well-defined-on-classes; the sum, product and negative do (@def-integer-operations, @prp-integer-operations-well-defined), and \( n \mapsto [(n, 0)] \) copies \( \nN \) into \( \nZ \) (@prp-naturals-embed-integers). \( \nZ \) is a commutative ring with \( 1 \ne 0 \) (@def-commutative-ring-and-field, @thm-integers-commutative-ring), and the algebra of a ring follows (@prp-ring-algebra). The positive classes make \( \nZ \) an ordered ring (@def-ordered-ring-and-field, @prp-order-from-positives, @def-integer-order, @thm-integers-ordered-ring) with the usual rules for inequalities (@prp-ordered-ring-rules); a set of integers bounded below has a least element (@prp-integer-least-element). Divisibility has its usual rules (@prp-divisibility-rules-integers), division with remainder exists and is unique (@thm-integers-division-remainder), and every integer is even or odd and not both (@cor-integers-even-odd).

What is open: \( \nZ \) is not a field, since \( 2x = 1 \) has no solution. Chapter 3 repeats the construction with pairs of integers to supply quotients.

## Terms

- **integer**: a class \( [(a, b)] \) of pairs of natural numbers under \( a + d = b + c \) (@def-integers-as-classes).
- **normal form**: the one pair \( (n, 0) \) or \( (0, n) \) in a class (@prp-integer-normal-form).
- **well defined**, **induced function**: a rule on classes that does not depend on the representatives, and the function it gives (@thm-well-defined-on-classes).
- **commutative ring**, **field**: a set with addition and multiplication satisfying the laws (F1)–(F7), (F9), and also \( 1 \ne 0 \) and (F8) for a field (@def-commutative-ring-and-field).
- **ordered commutative ring**, **ordered field**: a ring or field with a relation \( < \) satisfying (O1)–(O4) (@def-ordered-ring-and-field).
- **positive set**: a subset \( P \) closed under sums and products, with every element exactly one of positive, zero or negative (@prp-order-from-positives).
- **discreteness**: no integer lies strictly between \( n \) and \( n + 1 \) (@thm-integers-ordered-ring).
- **multiple** \( n \cdot a \): \( a \) added \( n \) times, defined by recursion (Section 2.4).
- **divides**, **prime**: \( a \mid b \) when \( b = ka \) for an integer \( k \); \( p \) is prime when \( p \ge 2 \) and its only positive divisors are \( 1 \) and \( p \) (@prp-divisibility-rules-integers).
- **quotient, remainder**: the \( q \) and \( r \) with \( a = qn + r \) and \( 0 \le r < n \) (@thm-integers-division-remainder).
- **even, odd**: \( a = 2q \) or \( a = 2q + 1 \) (@cor-integers-even-odd).
