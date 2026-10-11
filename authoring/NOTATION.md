# Book-wide notation

This list is fixed. A chapter that needs a new symbol adds it **here**, and a new macro in
`latex/macros.tex`, before using it. The left column is what to type.

The conventions in "Standing conventions" are shared with the linear-algebra companion; the
tables below are the analysis book's. Fill a row the first time a symbol is used, not later.

## Standing conventions

These are book-independent. Keep them.

- **Points and vectors are plain italic** (\( x \in \nR^n \), \( f \in C[a,b] \)), unlike
  the linear-algebra companion's bold vectors: in analysis the same letter moves between ℝ,
  ℝⁿ and function spaces, and bold would have to switch on and off. The bold one-letter
  macros (`\v`, `\A`, …) exist in `latex/macros.tex` for the engine; this book does not use
  them.
- **Ordered things go in parentheses, unordered in braces.** An ordered basis is
  `\sB = (\v_1, \dots, \v_n)`; a set is `\{ \v_1, \dots, \v_n \}`. The distinction is load
  bearing the first time order matters, and a reader who has seen it kept everywhere trusts
  it.
- **The two-slot bracket rule.** `\coord{x}{B}` renders \( [x]_{B} \) and `\mtx{T}{B}{C}`
  renders \( [T]_{B}^{C} \): the object in brackets, the data it is taken relative to hanging
  off the brackets, **source below and target above**, always in that order. One notation for
  "X relative to Y", chosen once. Never write a second one for the same thing; the linear
  algebra book carried two for a year and every cross-reference had to be checked by hand
  when one was retired.
- **One symbol, one meaning, book-wide.** If a symbol must be reused with a different
  meaning in a later chapter, say so in its row here and state where the two uses could meet
  and why they do not.
- **Define it before you use it.** No symbol appears before the row that introduces it.
- **`\coloneqq` for "is defined to be"**, not `=` and not `:=` typed by hand.
- **Set-builder notation uses a colon**, `\{ x \in S : P(x) \}`, not a bar, so a bar is free
  to mean divisibility, restriction or absolute value.
- **Functions:** `f \colon X \to Y` and `x \mapsto f(x)`; composition is `g \circ f`.
- **Every symbol here has a macro** in `latex/macros.tex`, so the PDF and the website agree
  and a change of mind is one edit. Nothing ad hoc in a section file.

## Numbers, sets, logic

| Type | Renders / meaning |
|---|---|
| `\nN, \nZ, \nQ, \nR, \nC` | ℕ, ℤ, ℚ, ℝ, ℂ. **ℕ = {0, 1, 2, …} contains 0** (series-wide convention, math-atlas spec/06 item 1). For indices or numbers starting at 1, write \( n \ge 1 \) or \( \nZ_{>0} \); there is no separate macro for the positive integers. **In fd3, ℕ ≔ ω** (F3.1 §07, `cor-omega-identification` and the citing rule after it): from F3.2 on, \( \nN \) means the set \( \omega \) of F3.1 §03 with its \( 0 \), \( + \), \( \cdot \), \( < \); F3.1 itself writes \( \omega \) throughout and \( \nN \) only for F1.3–F2.3's ℕ. **In fd3, ℤ and ℚ are built** (F3.2): \( \nZ \coloneqq (\nN \times \nN)/{\sim} \) (§01, `def-integers-as-classes`) and \( \nQ \coloneqq (\nZ \times \nZ_{>0})/{\sim} \) (§04, `def-rationals-as-classes`); after the identification remarks of §02 (\( n \) for \( \iota(n) \), `prp-naturals-embed-integers`) and §04 (\( m \) for \( j(m) \), `prp-integers-embed-rationals`), \( \nN \subseteq \nZ \subseteq \nQ \), a convenient abuse of notation made honest by the injective embeddings (\( 0 = \emptyset \notin \nZ \) literally, since every class is non-empty) |
| `\nZ_{>0}`, `\nQ_{>0}` | \( \nZ_{>0} \coloneqq \{ n \in \nN : n \ne 0 \} \), the positive integers (F2.2 §01, written there inside the familiar reals; **recalled, not redefined**, in F3.2 §02, after `prp-naturals-embed-integers`, as a subset of the constructed ℤ, and again before `thm-integers-ordered-ring`, whose clause (b) proves \( \nZ_{>0} = \{ n \in \nZ : n > 0 \} \)); \( \nQ_{>0} \coloneqq \{ x \in \nQ : x > 0 \} \), the positive rationals (F3.2 §05, after `thm-rationals-ordered-field`). No macro beyond `\nZ`, `\nQ` |
| (F1)–(F9); (O1)–(O4); (P1)–(P2) | clause names: the axioms of a **commutative ring** ((F1)–(F7), (F9), with \( 1 = 0 \) allowed) and a **field** (also \( 1 \ne 0 \) and (F8)) (F3.2 §03, `def-commutative-ring-and-field`), numbered as in linear algebra's field and Ch 11's `def-ordered-field`; the order axioms of an **ordered commutative ring** / **ordered field** (F3.2 §03, `def-ordered-ring-and-field`), numbered as in AN1.1; the positive-set clauses (P1) closure under \( + \), \( \cdot \) and (P2) trichotomy for \( P \subseteq R \) (F3.2 §03, `prp-order-from-positives`, local). (P1)–(P2) are the third use of "(P…)", after the partition clauses (P1)–(P3) of F2.2 §05 and the Peano clauses (P1)–(P5) of F3.1 §04; the text says so at `prp-order-from-positives`, and F3.9 cites "(P2)" by this name. In a ring, \( a - b \coloneqq a + (-b) \); in a field, \( a^{-1} \) (unique, F3.2 §03) and \( a/b \coloneqq a b^{-1} \) |
| `P`, `P_{\nZ}`, `P_{\nQ}` | a **positive set** of a commutative ring (F3.2 §03, `prp-order-from-positives`; \( a < b \iff b - a \in P \)); the positive integers as a set of classes, \( P_{\nZ} \coloneqq \{ [(a, b)] : b < a \} \) (F3.2 §03, `def-integer-order`), and the positive rationals \( P_{\nQ} \coloneqq \{ [(p, q)] : p > 0 \} \) (F3.2 §05, `def-rational-order`); after the theorems, \( P_{\nZ} = \nZ_{>0} \) and \( P_{\nQ} = \nQ_{>0} \) |
| `\nNz` | **Retired.** ℕ now contains 0, so ℕ₀ is just `\nN` (F3.1's construction route and Peano's axioms included). Do not use: the macro is removed from `latex/macros.tex`, so a use fails to render |
| `\varepsilon` | ε, always the variant (never `\epsilon`) |
| `\coloneqq` | "is defined to be" |
| `\{ x \in S : P(x) \}` | set-builder notation, with a colon |
| `S \setminus T`, `\card{S}` | difference, cardinality |
| `f \colon X \to Y`, `x \mapsto f(x)` | functions |
| `\id_X` | identity function |
| `\powerset{X}` | power set 𝒫(X) |
| `x \in A`, `x \notin A` | membership. In bounds such as \( n \in \nZ_{>0} \) from F1.1; as a predicate of an arbitrary set from F1.4 §01 (\( \in A \) for a fixed set \( A \) is a one-place predicate symbol, F1.4 §02); sets are developed in F2.1 §01 |
| `\emptyset` | the empty set. Informal first use F1.4 §01 ("The empty set", bounded quantifiers over \( \emptyset \)); defined in F2.1 §01, `def-empty-set`: the set with no elements, unique by `prp-empty-set-unique`; \( \emptyset \subseteq A \) for every set \( A \), and \( \{\emptyset\} \ne \emptyset \) |
| `A \subseteq B`, `A \subsetneq B` | subset (equality allowed), proper subset (F2.1 §01, `def-subset`). Used for lists of formulas from F1.3 §05 (\( \Gamma_i \subseteq \Gamma_k \)); glossed for sets in F1.4 §01 (every element of \( A \) is an element of \( B \)). The book never writes `\subset`, which other books use for either |
| `A \cup B`, `A \cap B`, `X \setminus A` | union, intersection, difference (F2.1 §02, `def-set-operations`). **No `A^c`:** a complement is always written `X \setminus A` with the ambient set named, so the reader never guesses it (there is no complement without one, by `thm-russell`) |
| `(A_i)_{i \in I}`, `\bigcup_{i \in I} A_i`, `\bigcap_{i \in I} A_i`; `\bigcup \sS`, `\bigcap \sS` | a family indexed by \( I \) (parentheses: indexed); its union, and its intersection taken inside a named ambient \( X \), so the empty intersection is \( X \) (F2.1 §02, `def-indexed-family`, `def-family-union-intersection`); \( \bigcap \sS \) only for non-empty \( \sS \subseteq \powerset{X} \). From F3.1 §01 (`prp-zf-basic-sets` (c)), \( \bigcap \sS \) is also written for any non-empty set \( \sS \) **with no ambient set**: \( \{ x \in A_0 : x \in S \text{ for every } S \in \sS \} \) for any \( A_0 \in \sS \), independent of \( A_0 \); the two agree when \( \sS \subseteq \powerset{X} \). \( \bigcup \sS \) exists for every set \( \sS \) by (Z4); \( \bigcap \emptyset \) stays undefined (it would contain every set) |
| `(a, b)`, `(x_1, \dots, x_n)` | ordered pair and \( n \)-tuple (F2.1 §03, `def-ordered-pair`), known through the characteristic property \( (a, b) = (c, d) \iff a = c \wedge b = d \) and one working convention: a pair is not a number, and tuples of different lengths are different kinds of object, so a triple is not a pair (F2.1 §03). The pair/interval double reading of `(a, b)` is stated once, in F2.1 §03. **In F3.1's picture** (every object a set) the pair is the Kuratowski pair \( (a, b) \coloneqq \{\{a\}, \{a, b\}\} \) (F3.1 §02, `def-kuratowski-pair`), with the characteristic property proved (`thm-kuratowski-pair`); from F3.1 §06 an \( n \)-tuple with \( n \ge 3 \) is the graph \( \{(1, x_1), \dots, (n, x_n)\} \) of a function \( \{1, \dots, n\} \to X \) (`prp-tuples-as-sets`). The working convention becomes theorems there: no pair or \( n \)-tuple is a natural number (`prp-pair-not-natural`, `prp-tuples-as-sets` (e)), and for \( n \ge 3 \) no \( n \)-tuple is a pair (`prp-tuples-as-sets` (c)) |
| `A \times B`, `X^2`, `X^n` | Cartesian product; \( X \times X \); the set of \( n \)-tuples from \( X \) (F2.1 §03, `def-cartesian-product`). \( X^n \) has a number as exponent; \( Y^X \) (below) has a set. In F3.1, where numbers are sets, a natural-number exponent is always read as a number: \( X^n \) is the set of \( n \)-tuples and \( b^n \) for \( b \in \omega \) is the power on \( \omega \) (`u^n` row), never F2.1's \( Y^X \) with the set \( n \) in place of \( X \); and the base of \( X^n \) is never an element of \( \omega \) (F3.1 §06, the paragraph after `prp-tuples-as-sets`). In F3.1 §06 (`prp-tuples-as-sets` (a)), \( X^n \) for \( n \ge 3 \) is the set of graphs of functions \( \{1, \dots, n\} \to X \), a set by (Z5), (Z6); \( X^2 = X \times X \) |
| `a \mathrel{R} b`, `R^{-1}` | \( (a, b) \in R \) for a relation \( R \subseteq A \times B \); the inverse relation \( \{ (b, a) : (a, b) \in R \} \) (F2.1 §03, `def-relation`). For the graph of a bijection \( f \), the inverse relation is the graph of the inverse function \( f^{-1} \) of F2.1 §05 |
| `f\|_A` | restriction of \( f \colon X \to Y \) to \( A \subseteq X \), a function \( A \to Y \) (F2.1 §04). The bar is one of the uses the colon-for-set-builder convention keeps free |
| (Z1)–(Z6); (Z7) | the axioms of the ZF fragment (F3.1 §01, `ax-zf-fragment`): (Z1) Extensionality, (Z2) Empty set, (Z3) Pairing, (Z4) Union, (Z5) Power set, (Z6) Separation; (Z7) Infinity, "there is an inductive set" (F3.1 §03, `ax-infinity`). Clause names only, no macro. They replace F2.1 §01's working rules (W1)–(W6) in F3.1's picture (`prp-working-rules-from-axioms`); Replacement, Foundation and Choice are not among them |
| `\mathrm{S}(x)` | the **successor** of a set, \( \mathrm{S}(x) \coloneqq x \cup \{x\} \) (F3.1 §03, `def-set-successor`). Upright S, typed directly (no macro), so that it never collides with an italic set named \( S \) (as in F2.1's `prp-smallest-closed-set`). For \( n \in \omega \), \( \mathrm{S}(n) = n + 1 \) once + exists (F3.1 §05, `def-omega-arithmetic` (c)); the \( n^{+} \) of Enderton and Halmos is not used. From F3.1 §04 the same letter also names the function \( \mathrm{S} \colon \omega \to \omega \), whose graph is \( \{ (n, \mathrm{S}(n)) : n \in \omega \} \) (`thm-omega-peano`); its value at \( n \) is the successor \( \mathrm{S}(n) \), so the two uses agree wherever both are defined. Only the function is a set: the operation on all sets has no graph, by `thm-russell` (F3.1 §04, the paragraph after `thm-omega-peano`) |
| `\omega`; inductive (of a set) | the least inductive set (F3.1 §03, `def-omega`, `thm-omega-least-inductive`); its elements are the **natural numbers** of F3.1, the von Neumann numerals \( 0 \coloneqq \emptyset \), \( 1 \coloneqq \mathrm{S}(0) = \{0\} \), \( 2 \coloneqq \{0, 1\} \), … (`exm-von-neumann-numerals`). A set \( I \) is **inductive** if \( \emptyset \in I \) and \( \mathrm{S}(x) \in I \) for every \( x \in I \) (`def-zf-inductive-set`; not AN1.1's inductive subset of \( \nR \), `def-inductive-set`, which has base \( 0 \) and step \( x \mapsto x + 1 \) inside \( \nR \)). In the later chapters of fd3 \( \omega \) is written \( \nN \) (ℕ row above) |
| `(M, e, s)`; (P1)–(P5) | a **Peano system**: a set \( M \), an element \( e \in M \), a function \( s \colon M \to M \) with (P3) \( s(x) \ne e \), (P4) \( s \) injective, (P5) every subset of \( M \) containing \( e \) and closed under \( s \) is \( M \) ((P1), (P2) are built into the data) (F3.1 §04, `def-peano-system`; \( (\omega, 0, \mathrm{S}) \) is one by `thm-omega-peano`). Not \( N \), too close to \( \nN \). An **isomorphism** \( (M, e, s) \to (M', e', s') \) is a bijection \( \psi \) with \( \psi(e) = e' \) and \( \psi \circ s = s' \circ \psi \) (F3.1 §07, defined in prose before `thm-peano-categoricity`). The clause names (P1)–(P3) of F2.2 §05's partitions are a different use; see the \( \sP \) row. For the operations \( \oplus \), \( \otimes \) of a Peano system, and for the functions \( M_m \) of F3.1 §05, see the next two rows |
| `A_m`, `M_m` | for \( m \in \omega \), the functions \( \omega \to \omega \) given by `thm-omega-recursion` with \( m + n \coloneqq A_m(n) \) and \( m \cdot n \coloneqq M_m(n) \) (local to F3.1 §05, `def-omega-arithmetic` and its well-definedness paragraph). The subscripted \( M_m \) is not the set \( M \) of a Peano system (see the `(M, e, s)` row) |
| `\oplus`, `\otimes` | for a Peano system \( (M, e, s) \), operations \( M \times M \to M \) with \( x \oplus e = x \), \( x \oplus s(y) = s(x \oplus y) \), \( x \otimes e = e \), \( x \otimes s(y) = (x \otimes y) \oplus x \): the recursion equations of + and · read in \( M \) (local to F3.1 §07, `prp-isomorphism-preserves-arithmetic`, restated where used); not a direct sum or a tensor product |
| `n - m` on \( \omega \) | for \( m \le n \) in \( \omega \), the unique \( j \in \omega \) with \( m + j = n \) (F3.1 §06, `prp-omega-order-arithmetic` (a)); undefined for \( m > n \). Agrees with F2.2's \( n - m \in \nN \) (`lem-naturals-arithmetic` (d)) under `cor-omega-identification` |
| `Y^X` | the set of all functions \( X \to Y \) (F2.1 §04); \( \{0, 1\}^{\nN} \) in F2.3. A function is the pair (graph, codomain), so the codomain is part of the function (F2.1 §04, `def-function`) |
| `2\nN` | the even natural numbers, \( 2\nN \coloneqq \{ 2n : n \in \nN \} \) (F2.3 §01, before `exm-hilbert-hotel`; a set-builder abbreviation, stated where used) |
| `A_1 \times \dots \times A_k` | for an integer \( k \ge 2 \): with \( U \coloneqq \bigcup_{i \in \{1, \dots, k\}} A_i \), the set of \( (x_1, \dots, x_k) \in U^k \) with \( x_i \in A_i \) for every \( i \) (F2.3 §02, before `cor-product-countable`); \( X \times \dots \times X = X^k \) |
| `0.d_1 d_2 d_3 \ldots`; `t_n` | a **digit sequence** \( k \mapsto d_k \) from \( \nZ_{>0} \) to \( \{0, 1, \dots, 9\} \), indexed from \( 1 \), and its truncation \( t_n \coloneqq \sum_{k=1}^{n} d_k 10^{-k} \); it is a decimal expansion of \( x \in [0, 1] \) if \( t_n \le x \le t_n + 10^{-n} \) for every \( n \ge 1 \) (F2.3 §04, `def-decimal-expansion`); \( x = 0.d_1 d_2 d_3 \ldots \) means that \( x \) is the number of which the sequence is an expansion, unique by (D2), so \( 0.4999\ldots = 0.5000\ldots \). "Ends in all \( 9 \)s": \( d_k = 9 \) for every \( k \ge N \), some \( N \ge 1 \) (likewise \( 0 \)s) |
| `\mathrm{Alg}`, `\mathrm{Alg}_d`; `p_c`, `R(c)`, `Z_d` | the algebraic real numbers, and those that are roots of a non-zero polynomial of degree at most \( d \); for a coefficient tuple \( c \in \nZ^{d+1} \), \( p_c(x) \coloneqq \sum_{k=0}^{d} c_k x^k \) and its root set \( R(c) \coloneqq \{ x \in \nR : p_c(x) = 0 \} \); \( Z_d \) the non-zero tuples in \( \nZ^{d+1} \) (local to F2.3 §03, `thm-algebraic-countable` and C2; \( \mathrm{Alg} \) alone again in §04, `cor-transcendental-exist`, restated there; no formal polynomials in F1–F2) |
| `\mathrm{Seq}`, `\mathrm{Seq}_k`, `x \frown m`; `\mathrm{ZSeq}` | the finite sequences of natural numbers (graphs of functions \( \{1, \dots, k\} \to \nN \)), those of length \( k \), and \( x \) with \( m \) appended, \( x \cup \{ (k + 1, m) \} \); the same with \( \nZ \) in place of \( \nN \) (local to F2.3 §03, exercises B2 and C2) |
| `\sF`, `S_N(F)`; `\sI` | the set of finite subsets of \( \nN \), and \( S_N(F) \coloneqq \sum_{k=0}^{N} \ind_F(k)\, 2^k \) for \( F \subseteq \{0, \dots, N\} \) (local to F2.3 §02 C1); \( \sF \) again with \( \sI \), the infinite subsets of \( \nN \) (local to F2.3 §04 B2). Restated where used |
| `f(A)`, `f^{-1}(B)`, `f^{-1}` | image \( \{ f(a) : a \in A \} \subseteq Y \) and preimage \( \{ x \in X : f(x) \in B \} \subseteq X \), defined for **every** \( f \colon X \to Y \), \( A \subseteq X \), \( B \subseteq Y \) (F2.1 §06, `def-image`, `def-preimage`); \( f(X) \) for the range of \( f \) is first used in F2.1 §05, before `thm-left-inverse-iff-injective`; in \( f^{-1}(B) \) the whole expression names a set, and \( f^{-1} \) is not applied to \( B \). Whether \( f(\cdot) \) is a value or an image is decided by the declared argument, a point or a subset. The inverse function \( f^{-1} \colon Y \to X \) exists only for a bijection (F2.1 §05, `def-inverse-function`). Where the two uses meet: for a bijection, \( f^{-1}(B) \) read as a preimage under \( f \) and read as the image of \( B \) under \( f^{-1} \) are the same set (F2.1 §06, the remark "Two readings of the inverse symbol", proved there), so the notation is never ambiguous |
| `\card{S}` | cardinality. In F1–F2 only inside a relation: \( \card{A} = n \), "\( A \) has \( n \) elements", for a finite set (F2.3 §01, `def-finite`), and \( \card{A} = \card{B} \), \( \card{A} \le \card{B} \), \( \card{A} < \card{B} \) (Relations table). No object \( \card{A} \) is defined for an infinite \( A \): the collection of all sets equinumerous with \( A \) is not a set (F2.3 §01, the remark after `prp-equinumerous-properties`, by `thm-russell`) |
| `\ind_{A}` | indicator function 𝟏_A of a set A |
| `\sup A`, `\inf A`, `\max`, `\min` | supremum and infimum (sup ∅ = −∞ and sup of an unbounded set = +∞ only from MT (*Measure and Integration*) on, where it is announced) |
| `\abs{x}` | absolute value of a number: defined by cases in F1.1 (first in §01 C2, displayed in §07; school algebra), formally in AN1.1 (`def-absolute-value`); \( \abs{x - y} \) is the distance from \( x \) to \( y \) |
| `d \mid n`, `d \nmid n` | d divides n: n = dk for some integer k (first used F1.2 §04, C1); formally defined in F2.2 §02, `def-divides`, with \( k \in \nZ \) (so every integer divides 0); `\nmid` is its negation (F2.2 §02). As a partial order on ℕ: F2.2 §04, `prp-divides-partial-order` |
| `\{1, \dots, n\}`, `\{0, \dots, n\}` | for \( n \in \nN \): \( \{ k \in \nN : 1 \le k \le n \} \) and \( \{ k \in \nN : k \le n \} \) (F2.2 §01); \( \{1, \dots, 0\} = \emptyset \). On \( \omega \) (F3.1 §06, `thm-omega-order` (c), (e)) the same definitions give \( \{0, \dots, n\} = \mathrm{S}(n) \) and \( \{1, \dots, n\} = \mathrm{S}(n) \setminus \{0\} \), and \( n = \{0, \dots, n - 1\} \) for \( n \ne 0 \). No bracket notation \( [n] \): \( [a] \) is an equivalence class |
| `\{x_1, \dots, x_n\}` | the set whose elements are the terms of the list \( x_1, \dots, x_n \), \( n \ge 1 \) (F2.2 §03 `prp-finite-max`, §06 R4); passing from a finite set to such a list is F2.3's definition of finite. For a variable \( n \in \omega \) (\( n = 0, 1 \) allowed) and \( x \colon \{1, \dots, n\} \to X \), it is the image of \( x \), a set by (Z6) inside \( X \) (F3.1 §06, `prp-tuples-as-sets` (d)) |
| `\sum_{k=1}^{n} a_k`, `\prod_{k=1}^{n} a_k`; `\sum_{k=m}^{n} a_k`, `\prod_{k=m}^{n} a_k` | finite sum and product, defined by recursion for \( n \in \nN \) (F2.2 §03, `def-sum-product`): the empty sum is \( 0 \), the empty product \( 1 \); from \( m \) to \( n \) for integers \( m \le n + 1 \), by shifting the index to start at \( 1 \) |
| `n!` | factorial, \( n! \coloneqq \prod_{k=1}^{n} k \) for \( n \in \nN \), so \( 0! = 1 \) (F2.2 §03, `def-sum-product`) |
| `u^n` | power of a real \( u \) for \( n \in \nN \): \( u^0 \coloneqq 1 \), \( u^{n+1} \coloneqq u^n u \) (F2.2 §03, `def-power`), so \( 0^0 = 1 \); the laws in `prp-power-laws`. Roots \( a^{1/n} \) are AN1.1 (row above), real exponents AN1.10. The same symbol \( b^n \) for \( b, n \in \omega \): \( b^0 \coloneqq 1 \), \( b^{n+1} \coloneqq b^n \cdot b \), by `thm-omega-recursion` (F3.1 §06, `prp-omega-powers-parity`); the two agree under the identification of F3.1 §07 (`cor-omega-identification`), so no second symbol is needed. It is never written \( X^n \) with \( X \in \omega \); see the \( X^n \) row |
| `\Delta_X` | the diagonal \( \{ (x, x) : x \in X \} \) of \( X \times X \) (local to F2.2 §04 C1, defined where used) |
| `-A \coloneqq \{ -a : a \in A \}` | reflection of a set of numbers (first defined F2.1 §06, as an image: `exm-sets-of-numbers-as-images`; used from AN1.1); \( \inf A = -\sup(-A) \) |
| `cA \coloneqq \{ ca : a \in A \}` | scaling of a set of numbers by \( c \in \nR \) (first defined F2.1 §06, as an image: `exm-sets-of-numbers-as-images`; used from AN1.1) |
| `A + B \coloneqq \{ a + b : a \in A, \ b \in B \}` | sum of two sets of numbers (first defined F2.1 §06, as the image of \( A \times B \): `exm-sets-of-numbers-as-images`; used from AN1.1); later also for subsets of a vector space |
| `U(A)` | the set of all upper bounds of \( A \) in the ambient ordered field (AN1.1, local to exercises: §02 C2 in \( F \), §03 C2 in \( \nR \); restated where used). Always written with its argument, so it does not clash with \( U \) for an open set |
| `\sqrt[n]{a}`, `a^{1/n}` | for \( a > 0 \) and an integer \( n \ge 1 \), the unique \( s > 0 \) with \( s^n = a \) (AN1.1 `thm-nth-root`); `\sqrt{a}` is \( n = 2 \). In F1.1–F3.2, \( \sqrt{a} \) for \( a \ge 0 \) is a school fact. \( \sqrt[n]{0} = 0 \) (AN1.1 §06). For **odd** \( n \) and \( a < 0 \), \( \sqrt[n]{a} \coloneqq -\sqrt[n]{-a} \), the unique real \( s \) with \( s^n = a \) (first used F2.1 §04, §05 for the real cube root of every real number, a school fact there; AN1.1's `thm-nth-root` with a sign change). `a^{m/n} \coloneqq (a^{1/n})^m` for \( a > 0 \) (AN1.1 §06); \( a^x \) for irrational \( x \) from AN1.10 |
| `\nR(x)` | the field of rational functions \( p/q \) with real coefficients in one indeterminate \( x \), ordered by the signs of the leading coefficients (AN1.1 §05, `exm-nonarchimedean-field`): the book's non-Archimedean ordered field. Here \( x \) is the indeterminate, not a real number |
| `\limsup_{n \to \infty} a_n`, `\liminf` | upper and lower limits |
| `\floor{x}`, `\ceil{x}` | floor and ceiling. \( \floor{x} \) is first defined for \( x \in \nQ \) in F3.2 §05 (`prp-rational-integer-part`: the unique \( m \in \nZ \) with \( m \le x < m + 1 \), called the integer part); F3.2 never writes it for a non-rational argument |
| `(a_n)_{n \ge 1}` or `(a_n)` | a sequence (parentheses: ordered); `\{a_n : n \ge 1\}` is its set of values |
| `(a, b)`, `[a, b]`, `(a, b]` | intervals; an ordered pair is written `(a, b)` too and context decides, stated once in F2.1 §03 |

## The book's objects

The main characters: what letter each kind of object gets.

| Letter | Meaning |
|---|---|
| \( x, y, z, a, b \) | points or real numbers |
| \( (x_n), (a_n) \) | sequences; subsequences \( (x_{n_k}) \) |
| \( f, g, h \) | functions; \( (f_n) \) sequences of functions |
| \( A, B, S, E \) | subsets; \( K \) compact; \( U, V, W \) open; \( F \) closed |
| \( (X, d), (Y, \rho) \) | metric spaces; \( B(x, r) \) open ball, \( \overline{B}(x, r) \) closed ball |
| \( (X, \norm{\cdot}) \), \( H \) | normed spaces; Hilbert spaces |
| \( \varepsilon, \delta, r \) | small positive numbers; \( N, M \) thresholds (natural numbers: written \( \exists N \in \nN \), unless the formula needs \( N \ge 1 \), e.g. with \( 1/N \) or \( 1/n \), when \( \nZ_{>0} \) is used) |
| \( (X, \sM, \mu) \) | a measure space: σ-algebra \( \sM \), measure \( \mu \); Lebesgue measure \( m \) |
| \( z, w \); \( \Omega \) | complex numbers; an open set in ℂ or ℝⁿ |
| \( T, S \) | operators between normed spaces |

## Logic (F1)

| Type | Meaning |
|---|---|
| `\wedge, \vee, \to, \leftrightarrow, \neg, \bot` | and, or, implies, iff, not, contradiction (in derivations; prose says "implies", and theorems use `\Rightarrow`, `\iff`) |
| `\forall, \exists` | quantifiers |
| `\Gamma \vdash P` | P is derivable from the assumptions Γ |
| `\varphi, \psi, \chi` | metavariables standing for any statements, in rule schemas and in general claims about derivations (introduced in F1.1 §02 after `def-rule-schema`, used from F1.1 §03); P, Q, R are statement letters |
| `P \dashv\vdash Q` | P and Q are provably equivalent: P ⊢ Q and Q ⊢ P (F1.2 §04, `def-provable-equivalence`) |
| `\mathsf{X}`, `\mathsf{Y}` | a variable standing for a rule, in statements about rules (F1.2 §05, "X derives Y" before `thm-classical-rules-interderivable`) |
| `nd` environment | a Fitch derivation: fitch.sty via `latex/fitch-book.sty` (syntax and rule macros documented there). Quantifier and equality rule tags (F1.4): `\Ae`, `\Ai`, `\Ei`, `\Ee`, `\eqi`, `\eqe` (∀E, ∀I, ∃I, ∃E, =I, =E); the bounded rules of F1.4 §08 reuse them; an arithmetic fact is `\by{arith}{…}`. A flagged box is `\open[x_0]`. A proved sequent used as one line has a short tag: VI (`prp-vacuous-implication`, F1.2 §06, F1.4 §04, §09), QN (`prp-quantifier-negation`, written with its part, `\by{QN (a)}{…}`, `\by{QN (b)}{…}`; F1.4 §09), NIm (`prp-negated-implication`, F1.4 §09) |
| `\rulename{\wedge I}` | a rule name: ∧I, ∧E, →I, →E, ∨I, ∨E, ¬I, ¬E, ⊥E, RAA, ↔I, ↔E, R, ∀I, ∀E, ∃I, ∃E, =I, =E; derived: ¬¬I, ¬¬E, MT, CP, DS, DM, LEM; plus R (repetition, (D3) of `def-derivation`) |
| `p, q, r, p_1, p_2, \dots` | atoms (propositional letters), symbols of the formal language (F1.3 §01, `def-formula`); each atom is one symbol. From F1.3 on, \( \varphi, \psi, \chi \) are metavariables for **formulas** and never occur in them; the capitals \( P, Q, R \) of F1.1–2 were placeholders, read in F1.3 as atoms or as arbitrary formulas (F1.3 §01, "Letters, metavariables and substitution"). From F1.4 §02 on, \( p, q \) are also **object variables** ("for primes and other natural numbers", F1.4 §01); the two uses never meet, because a first-order formula has no propositional atoms (atomic formulas replace them, F1.4 §02 (Fm1)); in F1.4, \( p, q, r \) are atoms in §01's opening argument (written in F1.3's language) and wherever a later section reads a formula with a truth table (F1.4 §11, R1 and R4); inside a first-order formula they are variables |
| `\circ` | in the logic chapters (F1.3–5): a metavariable for a binary connective, \( (\varphi \circ \psi) \) any of \( (\varphi \wedge \psi), (\varphi \vee \psi), (\varphi \to \psi), (\varphi \leftrightarrow \psi) \). From F2.1 on (still F1–F2; F2.1 §04, `def-composition`), \( g \circ f \) is composition of functions. The two never meet: F1.1–5 compose no functions, and from F2.1 on no connective metavariable \( \circ \) is used |
| `\Gamma, \Delta` | finite lists of formulas (premises), as in `def-derivable` |
| `\hgt(\varphi)` | height of a formula, printed \( \operatorname{ht}(\varphi) \): nodes on a longest branch of its parse tree (F1.3 §01 `def-height`; recursive form F1.3 §02). Not `\height`, which the PDF preamble already defines as a length |
| `\atoms(\varphi)` | the set of atoms occurring in a formula (F1.3 §02, `exm-recursive-definitions`) |
| `\operatorname{len}(\varphi)` | length of a formula: its number of symbols (F1.3 §02) |
| `\operatorname{ex}(s)` | excess of a string: number of left minus number of right parentheses (local to F1.3 §02, `lem-parenthesis-count`) |
| `\operatorname{nodes}(\varphi)`, `\operatorname{neg}(\varphi)` | number of nodes of the parse tree; number of occurrences of \( \neg \) (local to F1.3 §02 exercises B3, C3) |
| `P(n)`, `P(\varphi)` | a property of natural numbers / of formulas, in induction principles (F1.3 §02); the statement letter \( P \) of F1.1–2 never takes an argument |
| `\mathrm{T}, \mathrm{F}` | the truth values true and false (F1.3 §03). No macro: `\T` is the bold one-letter macro. In truth tables, rows are listed T before F, the last atom alternating fastest |
| `v, w` ; `v(\varphi)` | valuations (F1.3 §03 `def-valuation`); the truth value of a formula under \( v \) (`def-truth-value`, clauses (V1)–(V6)) |
| `\Gamma \models \psi`, `\models \psi`, `\Gamma \not\models \psi` | semantic entailment: every valuation making all of Γ true makes ψ true (F1.3 §04 `def-valid-argument`); a valuation making Γ true and ψ false is a *refuting row*. Not a formula: never nested inside one. **For first-order formulas (F1.4 §11 on, `def-first-order-entailment`):** every structure and every assignment satisfying all of Γ satisfy ψ; a structure with an assignment satisfying Γ and not ψ is a *counter-model*, which plays the refuting row's part. The two readings never clash: the kind of formula decides which applies (valuations for F1.3's formulas with atoms, structures and assignments for first-order formulas) |
| `\Gamma \nvdash \psi` | ψ is not derivable from Γ (F1.3 §05, `cor-refuting-row`) |
| `\varphi \equiv \psi` | semantic equivalence of formulas: φ ⊨ ψ and ψ ⊨ φ (F1.3 §04 `def-semantic-equivalence`). F2.2 uses \( a \equiv b \pmod n \) for congruence; the two never meet (the congruence always carries its modulus) |
| `\sigma(\chi)`, `\sigma(\Gamma)` | the result of a substitution σ of formulas for atoms, applied to a formula or to each formula of a list (F1.3 §04, before `lem-substitution`) |
| `\Gamma_k`, `\varphi_k`; `\Delta \subseteq \Delta'` | the context of line k of a derivation (F1.1 `def-derivation`) and the formula on line k (F1.3 §05); for lists, every formula of Δ occurs in Δ' (F1.3 §05, before `lem-context-inclusion`) |
| `u`, `\models_3` | a three-valued valuation (values 0 < ½ < 1) and its entailment (local to F1.3 §05, the optional `thm-raa-independent`) |
| `v_{\mathrm{T}}` | the all-T valuation: every atom true (local to F1.3 §03 C2, §07 `thm-adequate-connectives` (b) and C2 (a)); not \( u \), which is three-valued |
| `\varphi^{v}`, `p^{v}` | the formula signed by a valuation: φ if v(φ) = T, ¬φ if v(φ) = F (F1.3 §06, before `lem-truth-table-line`; the literals of §07 rows) |
| `\mathbin{\vert}`, `\downarrow`, `\mathsf{M}` | NAND ("not both"; the source writes `\mathbin{|}`, which a pipe table cannot show), NOR ("neither"), and the three-place majority connective (local to F1.3 §04 C1 and §07 exercises C1, C2) |
| `\mathrm{occ}(\varphi)`, `\mathrm{bin}(\varphi)` | number of atom occurrences; number of binary connectives (local to F1.3 §03 exercise B2) |
| `P(x)`, `R(x, y)`, `\mathrm{Prime}(p)`; `<`, `\le`, `=`, `\in A` | predicate symbols with their holes (F1.4 §01; symbols of the first-order language, each with an arity \( n \ge 1 \), F1.4 §02). With parentheses \( P, Q, R, S \) are predicate symbols; a bare \( P, Q, R \) is still a statement letter of F1.1–3 (F1.4 §01, "A clash of letters"). `\mathrm{Prime}` is typed directly (no macro yet) |
| `x, y, z, u`; `x_0, y_0, \varepsilon_0, \delta_0` | variables of a first-order language (F1.4 §02, with \( \varepsilon, \delta, N, n, k, L \) and \( p, q \) in analysis); in a derivation, a subscript 0 marks a **fresh name** of a flagged box (\( \rulename{\forall I} \), \( \rulename{\exists E} \), F1.4 §§04, 06), always a variable, never a constant; elsewhere \( x_0 \) is an ordinary name |
| `\forall x \in A \; \varphi`, `\exists x \in A \; \varphi`, `\forall \varepsilon > 0 \; \varphi` | bounded quantifiers: abbreviations of \( \forall x\, (x \in A \to \varphi) \), \( \exists x\, (x \in A \wedge \varphi) \), and likewise with \( >, \ge, <, \le \) (F1.4 §01, `def-bounded-quantifier`); \( \exists! \, y \in Y \; \psi \) abbreviates \( \exists! \, y \, (y \in Y \wedge \psi) \) (first used F2.1 §04, `def-function`); not symbols of the language. Their derived rules: F1.4 §08, `prp-bounded-quantifier-rules` |
| `\varphi[t/x]`, `s[t/x]` | substitution of the term \( t \) for the **free** occurrences of the variable \( x \) in a formula, or for every occurrence in a term; read "\( \varphi \) with \( t \) for \( x \)" (F1.4 §02, `def-substitution`). No macro: typed directly; the slash is a separator, not division. A different operation from F1.3's \( \sigma(\chi) \), which puts formulas in for atoms. "\( x \) **appears in** \( \varphi \)" (written anywhere, after a quantifier symbol included) is wider than "an occurrence of \( x \)" (inside a term); freshness conditions use "appears" (F1.4 §02, after `def-free-variable`) |
| `\mathrm{Var}(t)`, `\mathrm{FV}(\varphi)` | the set of variables of a term; the set of free variables of a formula (local to F1.4 §02 exercises B2 and C1 and their solutions) |
| `\exists! x\, \varphi` | there is exactly one \( x \) with \( \varphi \); shorthand for \( \exists x\, (\varphi \wedge \forall y\, (\varphi[y/x] \to y = x)) \), \( y \) not appearing in \( \varphi \); not a symbol of the language (F1.4 §07, `def-unique-existence`) |
| `\fM`; `D`; `c^{\fM}`, `f^{\fM}`, `R^{\fM}`; `\fM_{\nN}` | a structure (model) of predicate logic, printed \( \mathfrak{M} \), with domain \( D \) and the interpretations of a constant, a function symbol and a predicate symbol (F1.4 §11, `def-structure`); a subscript names the domain of a standard structure, and \( \fM_1, \fM_2 \) are structures numbered within an example. Not `\sM`, which is the σ-algebra of MT (one symbol, one meaning) |
| `\ell`, `\ell(x)`, `\ell[x \mapsto d]` | an assignment of elements of \( D \) to the variables; the assignment that changes only the value at \( x \) to \( d \) (F1.4 §11, `def-assignment`). Unrelated to the \( \ell \) of the sequence spaces \( \ell^p \) (Operators table); the two never meet, since \( \ell^p \) always carries its exponent and the assignment never leaves F1 |
| `t^{\fM, \ell}` | the value in \( D \) of a term \( t \) under the assignment \( \ell \) (F1.4 §11, "Assignments and the value of a term") |
| `\fM, \ell \models \varphi`, `\fM, \ell \not\models \varphi`, `\fM, \ell \models \Gamma`; `\fM \models \varphi` | satisfaction: \( \fM \) satisfies \( \varphi \) under \( \ell \), clauses (S1)–(S7) (F1.4 §11, `def-satisfaction`); for a list, every formula of \( \Gamma \). For a sentence, \( \fM \models \varphi \), "\( \varphi \) is true in \( \fM \)", since the assignment does not matter (F1.4 §11, after `lem-free-coincidence`) |

Typesetting rules for logic (learned in the F1.1 pilot):
- **Derivations** are fitch.sty `nd` environments in a raw LaTeX block (```` ```{=latex} ````, inside `\begin{center} $ … $ \end{center}`), never `array`s. The PDF typesets them; the website gets an SVG compiled at build time (filters/tikz.lua). `\open`/`\close` make boxes, `\begin{nd}[schema]` prints each line's own label (i, j, k) instead of a number for a rule pattern, `\hypo` an assumption or premise, `\have` a derived line; justifications are the rule macros of `latex/fitch-book.sty` (`\ai{3,2}`, `\ii{3-5}`, `\oe{1,3-5,6-8}`, `\raa{i-j}`) or `\by{text}{refs}`. A derivation cannot carry an `{#eq-…}` label: refer to it in prose ("the derivation after @def-…").
- A rule name in prose: `\( \rulename{\neg I} \)`; with a relation symbol, brace it: `\rulename{{\to}I}`. A bare Unicode ¬, ∧, → in prose stops pdflatex.
- A range of cited lines in prose: `\lines{2}{5}` (no non-ASCII inside math).
- Truth tables, and any table whose headers are formulas, are display arrays (`\begin{array}{cc|c} … \hline …`), not pipe tables.
- Citing lines follows `def-derivation` (F1.1, F1.1 §05). A line may cite any **available** line: an earlier line such that every box containing it also contains the citing line (that is, not inside a box that has already closed). A closed box, cited as a whole, must sit directly in the part of the derivation where the citing line is.
- **Repetition** is clause (D3) of `def-derivation`, typeset `\r{i}` ("R i"): it copies an available line into the current box. Most rules may cite the available line directly, so R is needed only when a rule wants the statement as a line **of a particular box** — \( \rulename{{\to}I} \), \( \rulename{\neg I} \), \( \rulename{\vee E} \), \( \rulename{{\leftrightarrow}I} \) and RAA require the box's conclusion as a line of that box itself, not inside a further box (e.g. \( \vdash P \to (Q \to P) \) repeats \( P \) inside the box of \( Q \)).
- A result already derived may be used as one line (a derived rule), citing the result; this abbreviates pasting in its derivation with premises replaced by repetitions.

## Operators and named maps

| Type | Meaning |
|---|---|
| `\diam A`, `\dist(x, A)` | diameter, distance to a set |
| `\closure{A}`, `\interior{A}`, `\boundary{A}` | closure, interior, boundary |
| `\supp f` | support |
| `\esssup` | essential supremum |
| `\osc` | oscillation |
| `\iota \colon \nN \to \nZ`; `j \colon \nZ \to \nQ` | the embeddings \( \iota(n) \coloneqq [(n, 0)] \) (F3.2 §02, `prp-naturals-embed-integers`) and \( j(m) \coloneqq [(m, 1)] \) (F3.2 §04, `prp-integers-embed-rationals`), injective and preserving \( + \), \( \cdot \) (and order, `thm-integers-ordered-ring` (a), `thm-rationals-ordered-field`); used only until the identification remarks of §02 and §04, after which \( n \) and \( m \) are written for \( \iota(n) \), \( j(m) \) (row for \( \nN, \nZ, \nQ \)). The \( \iota \) is not an inclusion map; F3.9's \( \iota_F \) (the copy of ℚ in an ordered field) carries a subscript |
| `n \cdot a` | the \( n \)-th multiple of an element \( a \) of a ring, \( n \in \nN \): \( 0 \cdot a \coloneqq 0 \), \( (n + 1) \cdot a \coloneqq n \cdot a + a \) (F3.2 §03, "Multiples", by `thm-recursion` read on ω; the sum law in `prp-ordered-ring-rules` (h)). The dot is not the ring's multiplication; for \( R = \nZ \) the two agree (§03) |
| `\operatorname{lc}(p)`, `\deg p` | leading coefficient and degree of a non-zero polynomial \( p \) (AN1.1 §05 C2 and §07 C3 solutions, defined where used); \( \operatorname{lc}(pq) = \operatorname{lc}(p)\operatorname{lc}(q) \) |
| `Df(a)`, `f'(a)` | Fréchet derivative at a; the derivative on ℝ |
| `\pd{f}{x_i}` | partial derivative |
| `C[a,b]`, `C(K)`, `C^k`, `C_c` | continuous, k-times continuously differentiable, compactly supported functions |
| `\hat{f}(n)`, `\hat{f}(\xi)` | Fourier coefficient; Fourier transform |
| `f * g` | convolution |
| `L^p`, `\ell^p`, `\norm{f}_p` | Lebesgue spaces, sequence spaces, their norms |

## Relations

One row per relation symbol, saying what it relates and to what. A relation reused with a
second meaning is recorded here, with the reason the two uses never meet.

| Type | Meaning |
|---|---|
| `x \mathrel{R} y` | \( (x, y) \in R \) for a general relation \( R \) on a set \( X \) (relations: F2.1 §03, `def-relation`); reflexive on \( X \), symmetric, antisymmetric, transitive: F2.2 §04, `def-relation-properties`. Local relation letters (e.g. a plain \( R \) in a non-example, \( L \) for the pointwise order of F2.2 §04 B1(c)) are defined where used |
| `\sim`; `[a]`, `[a]_\sim`; `X/{\sim}`; `q` | an equivalence relation, clauses (Eq1)–(Eq3) (F2.2 §05, `def-equivalence-relation`); the class of \( a \), with the relation named when needed (`def-equivalence-class`); the quotient set and the quotient map \( q(a) \coloneqq [a] \) (`def-quotient-set`). Reserved for equivalence relations: F2.3 writes equinumerosity as \( \card{A} = \card{B} \), never with \( \sim \). **Reused in F3.2** for the two relations that build the number systems, with no subscript: \( (a, b) \sim (c, d) \iff a + d = b + c \) on \( \nN \times \nN \) (§01, `def-integers-as-classes`, `prp-integer-pairs-equivalence`) and \( (p, q) \sim (r, s) \iff ps = rq \) on \( \nZ \times \nZ_{>0} \) (§04, `def-rationals-as-classes`, `prp-rational-pairs-equivalence`); both are equivalence relations, so this is the same meaning, and the carrier set (pairs of natural numbers versus pairs in \( \nZ \times \nZ_{>0} \)) tells them apart |
| `[(a, b)]`, `[(p, q)]` | the class of a pair: of \( (a, b) \in \nN \times \nN \), an integer (F3.2 §01, `def-integers-as-classes`), and of \( (p, q) \in \nZ \times \nZ_{>0} \), a rational (F3.2 §04, `def-rationals-as-classes`). F2.2's \( [a] \) applied to a pair, never a new bracket symbol; no "\( a - b \)" or "\( p/q \)" for a class until the embeddings make them honest (§02, §04) |
| `\approx`, `\approx_1`, … | a second equivalence relation (or candidate relation), always local and restated where used: on \( Y \) beside \( \sim \) on \( X \) in `thm-well-defined-on-classes` (F3.2 §02); the product relation of the non-example after `prp-integer-pairs-equivalence` and the three candidate relations \( \approx_1, \approx_2, \approx_3 \) of exercise B1 (F3.2 §01); \( ps = rq \) on \( Y \coloneqq \nZ \times (\nZ \setminus \{0\}) \), classes \( [(p, q)]_{\approx} \) (F3.2 §04, `exm-fractions-nonzero-denominators`). Not "approximately equal" anywhere in fd3 |
| `\sP`; `\sim_{\sP}`, `\sim_f` | 𝒫, a partition of \( X \), clauses (P1)–(P3) (F2.2 §05, `def-partition`; not the power set, which is `\powerset{X}`); the equivalence relation of a partition (`thm-partition-equivalence`) and the fibers relation \( f(x) = f(y) \) of a function (`exm-fibres-of-function`), both local to F2.2 §05. The clause names (P1)–(P3) are reused by the Peano clauses (P1)–(P5) of F3.1 §04 (`def-peano-system`); the two never meet, since no F3.1 passage mentions a partition and F2.2 §05 has no Peano system. A third use is the positive-set clauses (P1)–(P2) of F3.2 §03 (row (F1)–(F9) above), local to ordered rings; the text flags it |
| `a \equiv b \pmod{n}`; `\nZ/n`; `[a]_n` | congruence modulo \( n \in \nZ_{>0} \): \( n \mid a - b \) (F2.2 §05, `def-congruence`); the integers modulo \( n \), the quotient set (`prp-integers-mod-n`); a residue class with its modulus named, when two moduli are in play (F2.2 §05 B3). The congruence always carries its modulus, so it never meets \( \varphi \equiv \psi \) of F1.3 |
| `\preceq`, `\prec`; `\succeq`, `\succ` | a general partial order, clauses (PO1)–(PO3) (F2.2 §06, `def-partial-order`), and its strict part \( x \prec y \iff x \preceq y \wedge x \ne y \); the reverse order \( x \succeq y \iff y \preceq x \) and its strict part. \( \le \) keeps its meaning on numbers |
| `m < n`, `m \le n` on \( \omega \) | for \( m, n \in \omega \): \( m < n \) **means** \( m \in n \), and \( m \le n \) means \( m < n \) or \( m = n \) (F3.1 §06, `def-omega-order`); a strict total order (`thm-omega-order` (a)), \( m \le n \iff m \subseteq n \) (§06 B1), and \( n = \{ m \in \omega : m < n \} \) (`thm-omega-order` (c)). It agrees with \( < \) on F2.2's ℕ under `cor-omega-identification`; on arbitrary sets \( \in \) is not transitive, so the reading is for \( \omega \) only |
| `\sup A`, `\inf A` in \( (X, \preceq) \) | least upper bound and greatest lower bound in a partially ordered set, clauses (S1)–(S2) (F2.2 §06, `def-order-supremum`); AN1.1's `def-supremum` is the case \( (\nR, \le) \) |
| `\card{A} = \card{B}`; `\card{A} \le \card{B}`, `\card{A} < \card{B}` | \( A \) and \( B \) are equinumerous: there is a bijection \( A \to B \) (F2.3 §01, `def-equinumerous`); there is an injection \( A \to B \), and that with no bijection (F2.3 §05, `def-card-le`). **Relations between sets**, not relations on a set: they relate any two sets, and there is no set of all sets for them to live on (`thm-russell`), so no object \( \card{A} \) is defined for an infinite \( A \); \( \card{A} = n \) for a finite set agrees with them (`def-finite`). **Not written with \( \sim \)**, which is kept for an equivalence relation on a set |

## Retired notation

Notation the book used and no longer uses. Keep the row: it stops a drafting agent
reintroducing it, and it explains an old label that cannot be renamed.

| Was | Now | Why |
|---|---|---|
| | | |

## Major notions

The notions that get the full eleven-step explain template (`authoring/STYLE.md` §3),
listed once so the judgement is not remade per section.

- The list in `authoring/STYLE.md` §3; add a notion here when a blueprint promotes one. 
