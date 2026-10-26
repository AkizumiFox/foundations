<!-- hand-written -->
# Blueprint: Chapter 9 (F4.8) Coordinates and Vectors in ℝⁿ, merged book, stage S1

**Status: S1, 2026-10-26.** Supersedes `f4-8.md` (S1 2026-10-25, never refereed). Next: S2a (list in §8), then freeze.

**What this is.** The final S1 blueprint for Chapter 9 of the merged volume *Preliminaries for Analysis and Algebra* (fd4 slot kept, fd5 retired; `fd4/authoring/design/merge-proposal.md`, author's answers of 2026-10-26: Q1 (a), Q2 (a), Q3 (a) F4.11 to AN1, Q4 (b) cut to about 257/326 h). Book order: Ch1 F4.6, Ch2 F5.1, Ch3 F4.1, Ch4 F5.2, Ch5 F5.3, Ch6 F5.4, Ch7 F5.5, Ch8 F4.7, **Ch9 F4.8**, Ch10 F4.9. Directory `fd4/src/ch09-coordinates-and-vectors/`, six section files `0k-<slug>.md` plus `index.md`. Sections are numbered 9.1–9.6.

**Changes from `f4-8.md`.**
1. **Cauchy–Schwarz has its only home here** (proposal §3.3–§3.4). Chapter 1 no longer proves a finite Cauchy–Schwarz or Lagrange's identity. This chapter adds `cor-cauchy-schwarz-sums` (the sum form that AN1 quotes) and Lagrange's identity as §05 C2.
2. **ℂ comes earlier now** (Chapter 3). ℂ is literally ℝ² (`@def-complex-numbers`), so §04 adds `prp-plane-is-complex-plane` (⟨z, w⟩ = Re(z w̄), ‖z‖ = |z|). §05's hook is Section 3.3's proof of the triangle inequality, which used complex multiplication and so has no analogue for n ≥ 3. Every former "prose pointer only" to F4.1 becomes a same-book citation.
3. **F4.10 and the angle.** F4.10 is retired, and the isometry and rotation material leaves the book (Q4 (b)). The Looking-ahead box no longer promises that a later chapter defines θ (§4.6).
4. **R group** now reaches back into the merged book: R1 Ch8 (factor out y − x), R2 Ch5 (homomorphisms), R3 Ch3 (spiral, Part I), R4 no hint. The old root-count R1 becomes §06 B3 (b), citing Ch7.
5. **Moderate difficulty and size.** Each section has one A item (≤ 6 parts), 2–4 B and 1–2 C; six old C items are cut or folded into the text, two are new (Lagrange, the defect identity). Total target: **25 h core / 35 h full** (§7).
6. Old labels are kept (`f4-9.md`, `f4-11.md` cite them); new: `prp-plane-is-complex-plane`, `cor-cauchy-schwarz-sums`.

**House manner** (STYLE §1, last bullet; §12.14). Every main definition is motivated before it is stated. Weird examples appear as Quick checks, and the naive attempt serves as the hook. A `[Scratch work]` idea with a Givens/Goal table in prose form comes at each method's first proof, kept apart from the forward-written proof. Every method section has a method box `exm-method-<slug>` and one *Prove or disprove* B item (verdict first in the solution). Scaffolding fades from full to Idea to terse. There are no footnotes, no jokes and no first-person persona; history appears in one line only where it carries mathematics. **Level reference** (coverage only, never text, examples or exercises): Lang *Basic Mathematics* ch. 5, 8–9; Apostol *Calculus* I ch. 12; Rudin *PMA* 1.36–1.38; Pugh 1.5. Nothing is copied from `~/book`. All examples and items are ours.

**Scope.** ℝⁿ is the set of n-tuples. The chapter covers vector operations, the dot product, norm and distance, Cauchy–Schwarz with its equality case, the triangle inequality, coordinate bounds (for AN1.4), projection onto a line through 0, and the cosine of the angle. **It leaves out** abstract vector spaces (LA1.1), matrices and linear maps, dimension, topology and open balls (AN1.4, AN2.1, where F4.11 now goes), lines not through 0, hyperplanes and convexity (Ch10), and the angle θ itself.

**Signature moves** (index "Named moves"; scaffolding levels per STYLE §12.14):

| Move | Box | Full | Idea | Terse |
|---|---|---|---|---|
| Work coordinatewise | `exm-method-coordinatewise` | §02 | §03 | §04 on |
| Expand the square | `exm-method-expand-the-square` | §04 | §05 | §06 |
| Normalize | `exm-method-normalize` | §05 | §06 | — |
| Subtract the projection | `exm-method-subtract-the-projection` | §06 | — | — |

---

## 1. Devices as applied

- **Method sections:** §02, §04, §05, §06 (box, `[Scratch work]` with Givens/Goal table, two worked examples, Prove-or-disprove B). §01 and §03 are not method sections. §03 uses coordinatewise at Idea level and carries a find-the-error item.
- **Key proofs** (STYLE §11.2; comprehension parts in each section's A item): `prp-norm-coordinate-bounds` with `cor-balls-and-boxes-rn` (§04), `thm-cauchy-schwarz-rn` (§05), `thm-projection-closest-point` (§06).
- **Find the error with a true conclusion:** §03 C1 ((N1)) and §04 C1 ((N9) of `@fd1:exm-not-allowed-catalogue`). **False-conclusion warning:** after `thm-triangle-inequality-rn`.
- **Proof ordering:** §05 B1. **Faded triple** (expand the square): full in the proof of `prp-parallelogram-law-rn` (§04), last step blank in §05 B2, last half blank in §06 B1. Each blank says "*Name the move, then complete it.*"
- **Try it first:** `thm-cauchy-schwarz-rn`, `thm-projection-closest-point`. **Self-explanation prompts:** three (§4.5, §4.6).
- **Exit checks** with marking schemes: §02 C1, §05 C1, §06 C1. **Hint ladders** (two rungs) on every C item except the two find-the-error items.
- **Almost-correct proof to repair:** §04 C1, plus the hook of §05 (the coordinatewise attempt that stalls).

## 2. Prerequisites (every label cited; grepped 2026-10-26)

All of the following exist in `fd*/src` at `96a11ee` unless marked *proposed*.

- **fd1:** `@fd1:ax-induction` (on ℕ through `@fd3:cor-omega-identification`), `@fd1:exm-not-allowed-catalogue` ((N1), (N9)).
- **fd2:** `@fd2:def-ordered-pair`, `@fd2:def-cartesian-product`, F2.1 §04's unlabelled "Longer lists" paragraph (n-tuples; ledgered), `@fd2:def-function`, `@fd2:def-injective`, `@fd2:def-bijective`, `@fd2:thm-recursion`, `@fd2:def-sum-product` (template for vector sums), `@fd2:prp-finite-max`, `@fd2:def-order-bounds`, `@fd2:def-order-supremum`.
- **fd3:** `@fd3:def-commutative-ring-and-field`, `@fd3:prp-ring-algebra`, `@fd3:prp-ordered-ring-rules` ((b) sums, strict if one strict; (c) products; (e) a ≠ 0 ⇒ a² > 0; (g) for a, b ≥ 0, a < b ⟺ a² < b²; (i) total order), `@fd3:lem-field-fraction-rules` ((d) no zero divisors), `@fd3:prp-absolute-value-ordered-field` ((a), (b) |x|² = x², (c) −|x| ≤ x ≤ |x|, (d) |x| ≤ r ⟺ −r ≤ x ≤ r, (e) triangle), `@fd3:prp-ordered-field-halves` ((d) 0 ≤ a ≤ b, 0 ≤ c ≤ d ⇒ ac ≤ bd), `@fd3:def-complete-ordered-field`, `@fd3:thm-reals-complete-ordered-field`, `@fd3:prp-cof-square-roots` (existence **and uniqueness**).
- **Chapter 1 (F4.6), same book, no blueprint yet. Requests for its S1** (names *proposed*, reconciled at S2):
  - `prp-sum-rules` covers (a) Σ(a_k + b_k) = Σa_k + Σb_k and Σca_k = cΣa_k; (b) a_k ≤ b_k for all k ⇒ Σa_k ≤ Σb_k; (c) (Σ_j a_j)(Σ_k b_k) = Σ_j Σ_k a_j b_k.
  - `lem-nonnegative-sum-zero`: for a_k ≥ 0, Σa_k ≥ 0, and Σa_k = 0 iff every a_k = 0.
  - Square-root facts, as the n = 2 case of Chapter 1's n-th roots: √(a²) = |a|; for a, b ≥ 0, a ≤ b ⟺ √a ≤ √b; √(ab) = √a√b.
  - **Fallback.** Any missing item is proved here, in a second-reading fold: the two sum lemmas in §03, by induction from `@fd3:prp-ordered-ring-rules` (b); `lem-square-root-rules` in §04, by uniqueness in `@fd3:prp-cof-square-roots` plus (g), (i). Chapter 1 must **not** state a Cauchy–Schwarz inequality or Lagrange's identity; it may point forward in prose.
- **Chapter 3 (F4.1):** `@def-complex-numbers` (ℂ ≔ ℝ²), `@prp-reals-embed-complex`, `@def-conjugate-modulus`, `@thm-conjugate-properties`, `@lem-real-part-at-most-modulus`, `@thm-complex-triangle-inequality`, `@cor-complex-triangle-variants`, `@ax-cosine-sine` (Looking-ahead box only, never in a proof).
- **Chapter 4 (F5.2):** `@def-field` (one prose remark in §02: the laws hold in Fⁿ for any field F; no proof uses it).
- **Chapter 5 (F5.3):** `@def-group`, `@def-group-homomorphism`, `@prp-homomorphism-injective-iff-kernel-trivial` (R2 only).
- **Chapter 7 (F5.5):** `@thm-polynomial-root-count` (§06 B3). Evaluating the formal polynomial gives the real function, by `@thm-evaluation-respects-operations` (Ch6).
- **Chapter 8 (F4.7):** method box `exm-method-factor-difference` and `def-monotone-function` (*proposed* in `f4-7.md` §02; reconcile with the merged Ch8 blueprint). Used in R1 only.
- **Not allowed:** an1, la, analysis volumes; Ch10 (prose pointers only); any school fact about √, angles, cos or figures as a proof step. Pictures never serve as reasons.

**Prerequisite ledger** (used without `@ref`): n-tuples and their equality (F2.1 §04); Σ over ℝ and over ℝⁿ by the recursion of `@fd2:def-sum-product` (template line, as Chapter 3 does for ℂ); max{|x_1|, …, |x_n|} by `@fd2:prp-finite-max` with F2.2's remark that its proof works in any totally ordered set. **School facts: none. Borrowed results: none** (cos appears only in the Looking-ahead box).

## 3. Labels

- §01 `points-and-coordinates`: `def-real-n-space`, `def-box-rn`, `exm-subsets-of-the-plane`.
- §02 `vector-operations`: `def-vector-operations-rn`, `exm-method-coordinatewise`, `prp-vector-space-laws-rn`, `lem-vector-sums-coordinatewise`, `def-standard-basis-rn`, `prp-standard-basis-expansion`, `def-parallel-rn`, `exm-midpoints-and-parallelograms`.
- §03 `dot-product`: `def-dot-product-rn`, `prp-dot-product-laws-rn`, `def-orthogonal-rn`, `prp-orthogonal-test-rn`, `exm-dot-products-computed`.
- §04 `length-and-distance`: `def-norm-rn`, `prp-norm-basic-rn`, `def-unit-vector-rn`, `def-distance-rn`, `prp-distance-basic-rn`, `prp-plane-is-complex-plane`, `exm-method-expand-the-square`, `prp-pythagoras-rn`, `prp-parallelogram-law-rn`, `prp-polarization-rn`, `prp-norm-coordinate-bounds`, `cor-balls-and-boxes-rn` (fallback `lem-square-root-rules`).
- §05 `cauchy-schwarz-and-the-triangle-inequality`: `thm-cauchy-schwarz-rn`, `cor-cauchy-schwarz-sums`, `exm-method-normalize`, `thm-triangle-inequality-rn`, `cor-triangle-finite-sums-rn`, `cor-norm-sum-bound`, `exm-cauchy-schwarz-applications`.
- §06 `projection-and-angle`: `def-projection-rn`, `exm-method-subtract-the-projection`, `thm-projection-closest-point`, `exm-distance-to-a-line-through-the-origin`, `def-angle-cosine-rn`, `prp-angle-cosine-properties`, `exm-angles-computed`.
- Exercises: `exr-<section-slug>-a1`, `-b1` …, `-c1` …, `-r1` … `-r4` (in §06).

All were grepped against `fd*/src` and the fd4 blueprints. None collides; hits in `f4-9.md` and `f4-11.md` are citations of these labels. The `-rn` suffix keeps them apart from LA's `thm-cauchy-schwarz`, `def-norm` and the like.

**Notation** (NOTATION.md rows; macros exist). The `\nR^n` row: "ℝⁿ (n ≥ 1) is the set of n-tuples (§9.1); ℝ¹ is identified with ℝ; ℝ² is the underlying set of ℂ (Section 3.1)". Vectors are plain italic, with coordinates as subscripts. `0` is the zero vector and `e_k` the standard vectors. `\inner{x}{y}` is the dot product (one mention of x · y). `x \perp y`. `\norm{x}`; `d(x, y)` ≔ ‖x − y‖; `\operatorname{proj}_y x`. `\cos\angle(x, y)` is **one symbol**, and the row warns that ∠ alone is undefined. max_k |x_k| is not named ‖x‖_∞ here.

---

## 4. Per-section plans

### 4.1 Section 9.1 Points and Coordinates (`01-points-and-coordinates.md`)

*Budget 2,800 main line; fold ≤ 200. Not a method section.*

- **Hook.** In school the plane is a picture first and pairs second. Analysis reverses this: a point **is** its list of coordinates, and every geometric statement is a statement about reals. One line of history: coordinates replaced figures by equations. Chapter 3 already did this once, for ℂ = ℝ².
- **Standing setup** (one paragraph): ℝ is the complete ordered field (`@fd3:thm-reals-complete-ordered-field`).
- **`def-real-n-space`** (major; slogan *a point is its list of coordinates*). For n ≥ 1, ℝⁿ is the set of n-tuples x = (x_1, …, x_n) of reals. Equality is equality in every place. For n = 2 it is ℝ × ℝ (`@fd2:def-cartesian-product`), the same set as ℂ (`@def-complex-numbers`). The convention ℝ¹ = ℝ is said to be a convention. "Point" and "vector" are synonyms.
- **Remark.** The model of the line and the plane (origin, unit, two perpendicular axes) is motivation only, never a reason.
- **`exm-subsets-of-the-plane`.** Subsets of ℝ² by conditions: the first axis; the closed first quadrant; the diagonal; the graph {(t, f(t))} (pointer to Section 8.1); {x : x_1² + x_2² ≤ 1} (§04 rewrites it as ‖x‖ ≤ 1). For each, one point in and one out.
- **`def-box-rn`.** For a_k ≤ b_k, the closed box ∏[a_k, b_k] ≔ {x : a_k ≤ x_k ≤ b_k ∀k}. The open box uses strict inequalities and needs a_k < b_k. Both are non-empty, with a point named. n = 1 gives an interval, n = 2 a rectangle.
- **Warning.** (1, 2) ≠ (2, 1) and (1, 2) ≠ {1, 2}. ℝ² × ℝ is not literally ℝ³: its elements are pairs whose first entry is a pair. **Fold** `[Second reading: gluing tuples]`: the map ((x_1, …, x_m), (y_1, …, y_n)) ↦ (x_1, …, y_n) is a bijection ℝᵐ × ℝⁿ → ℝ^{m+n} (`@fd2:def-bijective`). Injective because equal images agree in all m + n places; surjective by splitting a tuple. The book uses the identification only in words.
- **Quick check.** Which of (0, 0, 0), (1, 2), ((1, 2), 3) lie in ℝ³? How many points has {0, 1}³? *(Only the first; eight.)*
- **Exercises.**
  - **A1** (5 parts). (a) Solve (s + t, s − t) = (4, 2). *(s = 3, t = 1.)* (b) Is (1, 1/2) in [0, 1] × [1/2, 1]? Is (1/2, 0)? *(Yes; no.)* (c) Describe {x ∈ ℝ² : x_1 = x_2, x_1 + x_2 = 1}. *({(1/2, 1/2)}.)* (d) Is (0, 2) in the open box (0, 1) × (1, 3)? *(No: 0 < 0 fails.)* (e) Write the closed box with corners (−1, 0, 2) and (1, 1, 2), and say how many of its points have all coordinates integers. *([−1, 1] × [0, 1] × [2, 2]; 3 · 2 · 1 = 6.)*
  - **B1.** For closed boxes P = ∏[a_k, b_k] and Q = ∏[c_k, d_k], prove P ⊆ Q iff c_k ≤ a_k and b_k ≤ d_k for every k. *Answer.* (⇐) c_k ≤ a_k ≤ x_k ≤ b_k ≤ d_k. (⇒) The corners a and b lie in P because a_k ≤ b_k, hence in Q; read coordinate k. The solution remarks that a_k ≤ b_k is used here: an empty "box" would lie in every Q.
  - **B2.** (a) P ∩ Q = {x : max{a_k, c_k} ≤ x_k ≤ min{b_k, d_k} ∀k}: a closed box when every max ≤ min, empty otherwise. (b) [0, 1]² ∪ ([2, 3] × [0, 1]) is not a closed box. *Answer (b).* If it equals ∏[p_k, q_k], then (0, 0) and (3, 0) give p_1 ≤ 0 and 3 ≤ q_1, and p_2 ≤ 0 ≤ q_2. So (3/2, 0) is in the box, but it lies in neither rectangle.
  - **C1.** Let P be a closed box in ℝⁿ. Prove P = Q for a closed box Q = ∏[c_k, d_k] only if c_k = a_k and d_k = b_k for all k: the corners of a box are determined by the set. *Hint ladder:* (1) use B1 in both directions; (2) ≤ both ways gives equality. *Answer.* P ⊆ Q and Q ⊆ P give c_k ≤ a_k, b_k ≤ d_k, a_k ≤ c_k and d_k ≤ b_k, so equality by antisymmetry (`@fd3:prp-ordered-ring-rules` (i)). The solution adds that this is what makes "the box [a_1, b_1] × ⋯" an unambiguous name.

### 4.2 Section 9.2 Adding Points and Scaling Them (`02-vector-operations.md`)

*Budget 4,000; fold ≤ 300 (proof of `lem-vector-sums-coordinatewise`). Method section: **work coordinatewise**, full.*

- **Hook.** Two operations make ℝⁿ more than a set. Each of their laws is a law of ℝ, used in each coordinate. The section turns that observation into a method, and the method's failure case ("x ≠ 0") is part of it.
- **`def-vector-operations-rn`** (major). x + y, cx, 0, −x ≔ (−1)x, x − y. "Point" is used when we locate, "vector" when we add. The **displacement** from a to b is b − a; arrows are not a new kind of object.
- **`[Scratch work]` + Givens/Goal** (prose). Givens: x, y ∈ ℝⁿ, c ∈ ℝ. Goal: c(x + y) = cx + cy. Then Goal becomes "the k-th coordinates agree for every k", by tuple equality. Then Goal becomes c(x_k + y_k) = cx_k + cy_k, by the definition. The gap is closed by distributivity (`@fd3:def-commutative-ring-and-field`).
- **`exm-method-coordinatewise`** `[Method: work coordinatewise]`. *Template:* fix k, compute the k-th coordinate of each side, and prove the equation in ℝ. *When:* equations built from +, scalars and coordinates. *Usual failure:* a condition that is not "for every k". "x ≠ 0" means **some** x_k ≠ 0, and "parallel" is not coordinatewise. Worked examples: law (g), and law (j).
- **`prp-vector-space-laws-rn`.** (a) associativity, (b) commutativity, (c) x + 0 = x, (d) x + (−x) = 0, (e) c(dx) = (cd)x, (f) 1x = x, (g) c(x + y) = cx + cy, (h) (c + d)x = cx + dx, (i) 0x = 0, c0 = 0, (−c)x = −(cx) = c(−x), (j) cx = 0 ⇒ c = 0 or x = 0. *Proof:* (a)–(i) coordinatewise, each naming its field law. For (j), suppose x ≠ 0; that gives **one** k with x_k ≠ 0; then cx_k = 0 forces c = 0 (`@fd3:lem-field-fraction-rules` (d)). *Remark:* the proofs use only field laws, so they hold verbatim in Fⁿ for any field F (`@def-field`). LA1.1 takes (a)–(h) as axioms.
- **`lem-vector-sums-coordinatewise`.** Σ_{j=1}^m v_j is defined by recursion with X = ℝⁿ, the empty sum being 0. Then (Σ_j v_j)_k = Σ_j (v_j)_k and Σ_j (c_j v_j + d_j w_j) = Σ_j c_j v_j + Σ_j d_j w_j. *Proof* (fold): induction on m.
- **`def-standard-basis-rn`**, **`prp-standard-basis-expansion`**: x = Σ_k x_k e_k, and the coefficients are unique. *Proof:* the j-th coordinate of Σ_k c_k e_k is c_j.
- **`def-parallel-rn`.** x, y are parallel if y = cx or x = cy for some c. *Remarks:* 0 is parallel to everything, and the "or" is needed (x = 0, y = e_1). **For x ≠ 0, y is parallel to x iff y = tx for some t** (stated and proved in the text, two lines: if x = cy then c ≠ 0 and y = (1/c)x). This replaces old C1 and is cited by §04, §05.
- **`exm-midpoints-and-parallelograms`.** (a) m = (a + b)/2 satisfies m − a = b − m; for a = (1, 4), b = (5, −2), m = (3, 1). (b) b − a = c − d iff (a + c)/2 = (b + d)/2.
- **Warning.** e_1 ≠ 0 although its second coordinate is 0. There is no vector product here: (1, 2)(3, 4) is undefined in this chapter, even though ℝ² = ℂ has one (Chapter 3); §03's product is a number.
- **Quick check.** Is (2, 4, −6) parallel to (−1, −2, 3)? Is (1, 2) parallel to (2, 3)? *(Yes, with factor −2; no, since c would have to be both 2 and 3/2, or both 1/2 and 2/3.)*
- **Exercises.**
  - **A1** (5 parts). (a) Compute 2(1, 0, −1) − 3(0, 1, 1) + (1, 1, 1) as Σc_k e_k. *((3, −2, −4) = 3e_1 − 2e_2 − 4e_3.)* (b)–(e) Which conditions are "for every k": x = y; x ≠ y; x + y = 0; x parallel to e_1? *(Yes; no, it means "some k"; yes; yes once rewritten as x_k = 0 for k ≥ 2, by the remark under `def-parallel-rn`, since e_1 ≠ 0.)*
  - **B1 [Prove or disprove]** (verdict first). (a) x + y = x + z ⇒ y = z. *(**True**, coordinatewise.)* (b) cx = cy ⇒ x = y. *(**False**: c = 0, x = e_1, y = e_2.)* (c) cx = dx and x ≠ 0 ⇒ c = d. *(**True**: (c − d)x = 0, then (j).)* (d) Parallelism is transitive. *(**False**: e_1, 0, e_2.)* (e) If x, y are parallel and both nonzero, then y = cx with c ≠ 0. *(**True**: by the remark, y = cx, and c ≠ 0 since y ≠ 0.)*
  - **B2.** (a) Find all t with (1, t, 2) parallel to (2, 6, 4). *(t = 3: the first coordinate forces the factor 2.)* (b) Prove (b) of `exm-midpoints-and-parallelograms` both ways, naming the laws used.
  - **C1 [Exit check: two vectors that are not parallel].** x, y are not parallel iff sx + ty = 0 implies s = t = 0. *Hint ladder:* (1) for (⇒), suppose s ≠ 0 and solve for x; (2) for (⇐), use the contrapositive and choose s, t. *Answer.* (⇒) If s ≠ 0 then x = (−t/s)y, which is parallel, a contradiction. So s = 0 and ty = 0. Then y ≠ 0 (else y = 0 would be parallel to x), so t = 0 by (j). (⇐) If y = cx, take s = c, t = −1; if x = cy, take s = −1, t = c. **Marking (10):** 2 setup; 3 case s ≠ 0; 2 case s = 0 with y ≠ 0 justified; 2 (⇐) with both clauses of the definition; 1 conclusion. *Fatal:* dividing by s unchecked; treating only y = cx; t = 0 without y ≠ 0.

### 4.3 Section 9.3 The Dot Product (`03-dot-product.md`)

*Budget 3,500. Coordinatewise at Idea level. Not a method section.*

- **Hook.** By Pythagoras, length in the plane is √(x_1² + x_2²), and Chapter 3 named it |x_1 + x_2 i|. The expression under the root is a sum of products of coordinates. Taking it apart for two vectors gives a product that is a **number**.
- **`def-dot-product-rn`** (major; slogan *multiply coordinate by coordinate, then add*). ⟨x, y⟩ ≔ Σ_k x_k y_k; for n = 1 it is xy.
- **`prp-dot-product-laws-rn`.** (a) symmetry; (b) linearity in each slot; (c) ⟨x, x⟩ = Σx_k² ≥ 0, with equality iff x = 0; (d) ⟨x, e_k⟩ = x_k and ⟨e_j, e_k⟩ = δ_jk; (e) ⟨x, 0⟩ = 0. *Idea:* back-reference to `exm-method-coordinatewise`; the laws of ℝ apply term by term, and Chapter 1's Σ rules collect the terms. *Proof:* (a), (b) termwise plus `prp-sum-rules` (a); (c) by `@fd3:prp-ordered-ring-rules` (e) and `lem-nonnegative-sum-zero`, with x_k² = 0 iff x_k = 0; (d) one nonzero term; (e) from (b).
- **Displayed expansions** (used from §04 on): ⟨x ± y, x ± y⟩ = ⟨x, x⟩ ± 2⟨x, y⟩ + ⟨y, y⟩, with each step named.
- **`def-orthogonal-rn`** (major), motivated first: (1, 2) and (−2, 1) "look perpendicular", and their product is 0. *Remarks:* 0 ⊥ everything; 0 is the only self-orthogonal vector; e_j ⊥ e_k for j ≠ k.
- **`prp-orthogonal-test-rn`.** (a) ⟨x, z⟩ = 0 for all z ⇒ x = 0. (b) The following are equivalent: x = y; ⟨x, z⟩ = ⟨y, z⟩ for all z; ⟨x, e_k⟩ = ⟨y, e_k⟩ for all k. *Proof:* (a) take z = x; (b) by (d).
- **`exm-dot-products-computed`.** ⟨(1, 2, −1), (3, 0, 4)⟩ = −1. (1, 1, 1, 1) ⊥ (1, −1, 1, −1). The vectors ⊥ (1, 1) in ℝ² are exactly t(1, −1). In ℝ³, x ⊥ e_3 iff x_3 = 0.
- **Warning.** There is no cancellation (e_1; e_2, 2e_2) and no associativity (⟨e_1, e_1⟩e_2 ≠ e_1⟨e_1, e_2⟩ = 0). ⟨x, y⟩ = 0 does not force a zero factor.
- **Quick check.** Is (2, −1, 3) ⊥ (1, 5, 1)? What is ⟨x, x⟩ for (1, −2, 0, 3)? *(Yes; 14.)*
- **Exercises.**
  - **A1** (4 parts). (a) ⟨(1, −2, 0, 3), (4, 1, 7, −1)⟩. *(−1.)* (b)–(d) True or false for all x, y: ⟨2x, 2y⟩ = 2⟨x, y⟩; ⟨x, x⟩ = 0 ⇒ x = 0; ⟨x, y⟩ = 0 ⇒ x = 0 or y = 0. *(False, it is 4⟨x, y⟩; true, (c); false, e_1 and e_2.)*
  - **B1.** All x ∈ ℝ³ orthogonal to (1, 1, 0) and (0, 1, 1). *(x = t(1, −1, 1).)*
  - **B2.** ⟨x − y, x + y⟩ = ⟨x, x⟩ − ⟨y, y⟩, naming each law. Deduce that ⟨x, x⟩ = ⟨y, y⟩ iff x − y ⊥ x + y.
  - **B3.** For a ≠ 0 and r ∈ ℝ, x ≔ (r/⟨a, a⟩)a satisfies ⟨a, x⟩ = r, and it is the only solution parallel to a. *(Existence: ⟨a, a⟩ > 0. Uniqueness: a vector parallel to a is ta (§02 remark), and ta works only for t = r/⟨a, a⟩.)* The solution adds that for n ≥ 2 there are other solutions not parallel to a.
  - **C1 [Find the error, true conclusion].** "If ⟨x, z⟩ = 0 for every z, then x = 0. *Proof:* take z = e_1; then 0 = ⟨x, e_1⟩ = x_1. Hence x = 0." *Solution:* the conclusion is true (`prp-orthogonal-test-rn` (a)). The failing line is "Hence x = 0": it draws a claim about every coordinate from one instance ((N1)). The step is invalid in general: for n = 2 and x = e_2, x_1 = 0 yet x ≠ 0. Repair: take z = x, or z = e_k for every k. For n = 1 the step is valid.

### 4.4 Section 9.4 Length and Distance (`04-length-and-distance.md`)

*Budget 4,700; fold ≤ 400 (fallback lemma, if needed). Method section: **expand the square**, full. Key proof: coordinate bounds.*

- **Hook.** ⟨x, x⟩ is the square of the length. Its root exists because ℝ is complete. Lengths are awkward (a root of a sum) and their squares are polynomial; the method is to move to squares and back.
- **`def-norm-rn`** (major; slogan *length is the root of the dot product with itself*), preceded by the Quick check "is there a nonzero vector of length 0?" ‖x‖ ≔ √⟨x, x⟩. ‖(3, 4)‖ = 5.
- **`prp-norm-basic-rn`.** (a) ‖x‖ ≥ 0, with equality iff x = 0; (b) ‖cx‖ = |c|‖x‖; (c) ‖x‖² = ⟨x, x⟩; (d) ‖x‖ = |x| for n = 1; (e) ‖e_k‖ = 1. *Proof* from the dot-product laws and Chapter 1's root facts (√(c²) = |c|).
- **`def-unit-vector-rn`.** For x ≠ 0, x/‖x‖ is a unit vector, and the unit vectors parallel to x are exactly ±x/‖x‖.
- **`def-distance-rn`**, **`prp-distance-basic-rn`** (positivity, symmetry, translation, scaling; one line each). The triangle inequality waits for §05, "the one property that needs an idea".
- **`prp-plane-is-complex-plane`** (new). For z = (a, b) and w = (c, d) in ℝ² = ℂ: (a) z + w is the same in both readings, and for real t, tz (vector) = (t, 0)z (complex product) (`@prp-reals-embed-complex`); (b) ⟨z, w⟩ = Re(z w̄); (c) ‖z‖ = |z| (`@def-conjugate-modulus`), so d(z, w) = |z − w|. *Proof:* (a) by the multiplication rule of `@def-complex-numbers`: (t, 0)(a, b) = (ta, tb). (b) (a + bi)(c − di) has real part ac + bd. (c) Both are √(a² + b²). *Aftermath:* everything proved below for ℝⁿ applies to ℂ, and for n = 2 the coordinate bound (a) below is `@lem-real-part-at-most-modulus`.
- **`[Scratch work]` + Givens/Goal** for Pythagoras. Givens: x, y. Goal: ‖x + y‖² = ‖x‖² + ‖y‖² iff ⟨x, y⟩ = 0. Then Goal in dot products. Then expand. The gap closes by cancelling and dividing by 2.
- **`exm-method-expand-the-square`** `[Method: expand the square]`. *Template:* (1) to compare lengths, compare squares (both sides ≥ 0); (2) write ‖v‖² = ⟨v, v⟩; (3) expand; (4) compare and return. *When:* identities and inequalities among norms of sums and multiples. *Usual failures:* dropping the cross term; squaring sides that may be negative (‖x‖ − ‖y‖). Worked examples: Pythagoras, then the parallelogram law.
- **`prp-pythagoras-rn`.** ‖x ± y‖² = ‖x‖² + ‖y‖² iff x ⊥ y.
- **`prp-parallelogram-law-rn`.** ‖x + y‖² + ‖x − y‖² = 2‖x‖² + 2‖y‖². This is the **full** member of the faded triple.
- **`prp-polarization-rn`.** (a) ⟨x, y⟩ = ¼(‖x + y‖² − ‖x − y‖²); (b) 2⟨x, y⟩ = ‖x‖² + ‖y‖² − ‖x − y‖². *Aftermath:* lengths determine dot products; a map that preserves distances and fixes 0 preserves dot products (prose; that study belongs to the geometry volume).
- **`prp-norm-coordinate-bounds`** (key proof). With M ≔ max_k |x_k|: (a) |x_k| ≤ ‖x‖ for every k, so M ≤ ‖x‖; (b) ‖x‖ ≤ √n M. *Proof:* (a) ‖x‖² ≥ x_k², dropping nonnegative terms (`lem-nonnegative-sum-zero`, `@fd3:prp-ordered-ring-rules` (b)), then take roots. (b) x_j² ≤ M² (`@fd3:prp-ordered-field-halves` (d)), so ‖x‖² ≤ nM² (`prp-sum-rules` (b)), then √(nM²) = √n M.
- **`cor-balls-and-boxes-rn`.** For r > 0: (a) ‖x − a‖ < r ⇒ |x_k − a_k| < r for all k; (b) |x_k − a_k| < r/√n for all k ⇒ ‖x − a‖ < r. *Proof:* apply the proposition to x − a; in (b) M < r/√n. A picture is described in words. Pointer: AN1.4.
- **Warning.** ‖(1, 1)‖ = √2, not |1| + |1|; ‖e_1 + e_2‖ = √2 ≠ 2.
- **Quick checks.** ‖(1, 2, 2)‖? Is (3/5, 0, 4/5) a unit vector? *(3; yes.)*
- **Exercises.**
  - **A1** (6 parts, key proof). (a) ‖(2, −3, 6)‖ and its unit vector. *(7; (2, −3, 6)/7.)* (b) d((1, −1, 0), (3, 1, 1)). *(3.)* (c) Check both bounds for x = (2, −1, 2, 0). *(2 ≤ 3 ≤ 4.)* (d) Where are "the other terms ≥ 0" used? *(In (a), to drop them.)* (e) Why r/√n and not r in (b)? *(x = a + (r/2)(1, …, 1) has |x_k − a_k| = r/2 < r but ‖x − a‖ = (r/2)√n ≥ r once n ≥ 4.)* (f) The idea of (b) in two sentences.
  - **B1 [Prove or disprove].** (a) ‖x‖ = ‖y‖ ⇒ x = ±y. *(**False**: e_1, e_2.)* (b) ‖x‖ = ‖y‖ ⇒ x + y ⊥ x − y. *(**True**: §03 B2.)* (c) x ⊥ y ⇒ ‖x − y‖ = ‖x + y‖. *(**True**: both squares are ‖x‖² + ‖y‖².)* (d) ‖x + y‖² ≤ 2‖x‖² + 2‖y‖². *(**True**: parallelogram law.)* (e) x ⊥ y ⇒ d(x, 0) + d(0, y) = d(x, y). *(**False**: e_1, e_2 give 2 ≠ √2.)*
  - **B2.** For a = (1, 2), b = (4, 6), c = (−3, 5): b − a ⊥ c − a, and Pythagoras holds. *((3, 4)·(−4, 3) = 0; 25 + 25 = ‖(7, 1)‖² = 50.)*
  - **B3.** For a ≠ b, d(x, a) = d(x, b) iff ⟨x, b − a⟩ = (‖b‖² − ‖a‖²)/2, and the midpoint satisfies this. *(Square both sides and expand; for the midpoint use §03 B2.)* Pointer: Ch10 calls this set a hyperplane.
  - **C1 [Find the error, true conclusion].** "|x_k| ≤ ‖x‖. *Proof:* ‖x‖² ≥ x_k²; taking roots, ‖x‖ ≥ √(x_k²); since √(a²) = a for every real a, ‖x‖ ≥ x_k; applying this to −x gives ‖x‖ ≥ −x_k, so ‖x‖ ≥ |x_k|." *Solution:* the conclusion is true. The one bad line is "√(a²) = a for every real a" ((N9)); a = −3 is a counterexample. The other lines are correct, and the −x step would even rescue the argument if the line read √(a²) ≥ a. The solution says so, to separate reaching the conclusion from justifying every line. Repair: √(x_k²) = |x_k|.

### 4.5 Section 9.5 Cauchy–Schwarz and the Triangle Inequality (`05-cauchy-schwarz-and-the-triangle-inequality.md`)

*Budget 4,600. Method section: **normalize**, full; expand the square at Idea level. Key proof: `thm-cauchy-schwarz-rn`.*

- **Hook** (naive attempt first). In ℝ the triangle inequality came from cases on signs. In ℂ = ℝ² (Section 3.3, `@thm-complex-triangle-inequality`) it came from Re(z w̄) ≤ |z w̄| = |z||w|, which by `prp-plane-is-complex-plane` is ⟨z, w⟩ ≤ ‖z‖‖w‖, proved with the multiplication of ℂ. For n ≥ 3 we have no such multiplication. Expanding ‖x + y‖² shows that everything rests on ⟨x, y⟩ ≤ ‖x‖‖y‖. The attempt "Σx_k y_k ≤ Σ|x_k||y_k| ≤ …" stalls, because a coordinate-by-coordinate bound loses the geometry. The proof below uses only the laws of §03.
- **`thm-cauchy-schwarz-rn`** (key proof; major). (a) |⟨x, y⟩| ≤ ‖x‖‖y‖. (b) Equality holds iff x, y are parallel. (c) ⟨x, y⟩ = ‖x‖‖y‖ iff x = 0 or y = cx with c ≥ 0. (c′) ⟨x, y⟩ = −‖x‖‖y‖ iff x = 0 or y = cx with c ≤ 0. (c′) is stated so that §06 can cite it.
  - *Try it first (ten minutes): for unit u, v expand ‖u − v‖² ≥ 0. What does it say about ⟨u, v⟩? What else could you expand?*
  - **`[Scratch work]` + Givens/Goal.** Givens: x, y. Goal: |⟨x, y⟩| ≤ ‖x‖‖y‖. Row 2: both sides scale by a > 0 when x ↦ ax, so add the Givens x, y ≠ 0 (zero cases are 0 ≤ 0); the Goal becomes |⟨u, v⟩| ≤ 1 for u = x/‖x‖, v = y/‖y‖. Row 3: ‖u ∓ v‖² = 2 ∓ 2⟨u, v⟩ ≥ 0. The Try-it gives only one side; the other expansion closes the gap.
  - *Proof.* Zero cases first. Then ⟨x, y⟩ = ‖x‖‖y‖⟨u, v⟩; the two expansions give −1 ≤ ⟨u, v⟩ ≤ 1 (`@fd3:prp-absolute-value-ordered-field` (d)); multiply by ‖x‖‖y‖ > 0. For (c): ⟨u, v⟩ = 1 iff ‖u − v‖ = 0 iff u = v iff y = (‖y‖/‖x‖)x. Conversely y = cx with c ≥ 0 gives c‖x‖² = ‖x‖‖cx‖. (c′) is the same argument with u = −v. (b) combines (c) and (c′) with the remark under `def-parallel-rn`.
  - *Self-explanation prompt* at "Let x, y ≠ 0": *where is x ≠ 0 used, and why are both expansions needed?*
- **`cor-cauchy-schwarz-sums`** (new). For reals x_k, y_k: (Σx_k y_k)² ≤ (Σx_k²)(Σy_k²), with equality iff (x_k) and (y_k) are parallel as vectors. *Proof:* square (a), using `@fd3:prp-ordered-ring-rules` (g) and |t|² = t². *Remark:* this is the form AN1 quotes. Chapter 1 does not prove it; §05 C2 gives the classical second route, Lagrange's identity.
- **`exm-method-normalize`** `[Method: normalize]`. *Template:* if replacing x by ax (a > 0) scales both sides by the same positive factor (the statement is homogeneous), and likewise for y, then settle 0 separately, prove the statement for unit vectors and scale back. *When:* inequalities between ⟨·,·⟩ and products of norms; statements about directions. *Usual failures:* normalizing 0; scaling by a negative factor; non-homogeneous statements (‖x + y‖ ≤ 2). Worked examples: the theorem, and `exm-cauchy-schwarz-applications` (b).
- **`thm-triangle-inequality-rn`.** (a) ‖x + y‖ ≤ ‖x‖ + ‖y‖, with equality iff x = 0 or y = cx, c ≥ 0; (b) |‖x‖ − ‖y‖| ≤ ‖x − y‖; (c) d(x, z) ≤ d(x, y) + d(y, z). *Idea:* back-reference to the expand-the-square box; the cross term is bounded by Cauchy–Schwarz. *Proof* (a) is lines (i)–(vi) of B1; equality iff lines (iii) and (iv) are equalities, iff ⟨x, y⟩ = ‖x‖‖y‖. (b), (c) as usual. *Self-explanation prompt:* *which equality case of Cauchy–Schwarz is used, and why not (b)?* For n = 2 this recovers `@thm-complex-triangle-inequality`, with an equality case.
- **Warning (false conclusion).** "Parallel ⇒ ‖x + y‖ = ‖x‖ + ‖y‖." This fails for y = −x ≠ 0.
- **`cor-triangle-finite-sums-rn`** (induction). **`cor-norm-sum-bound`**: ‖x‖ ≤ Σ|x_k| ≤ √n‖x‖. *Proof:* the first by `prp-standard-basis-expansion` and the triangle inequality; the second by Cauchy–Schwarz with (|x_k|) and (1, …, 1). For n = 2 the first is `@lem-real-part-at-most-modulus`'s last inequality.
- **`exm-cauchy-schwarz-applications`.** (a) (a + b + c)² ≤ 3(a² + b² + c²), with equality iff a = b = c. (b) The maximum of 2x_1 + 3x_2 − x_3 over unit x is √14, attained only at (2, 3, −1)/√14 (normalize; theorem (c)).
- **Quick check.** x = (1, −2, 3), y = −2x: is |⟨x, y⟩| = ‖x‖‖y‖? Is ‖x + y‖ = ‖x‖ + ‖y‖? *(Yes, both are 28; no, √14 against 3√14.)*
- **Exercises.**
  - **A1** (5 parts, key proof). (a) Where is x ≠ 0 used? *(To form u.)* (b) Which expansion gives which bound? *(‖u − v‖² gives ≤ 1; ‖u + v‖² gives ≥ −1.)* (c) Run the proof on (3, 4), (4, 3). *(⟨u, v⟩ = 24/25; ‖u − v‖² = 2/25; 24 ≤ 25.)* (d) What fails if u is not a unit vector? *(‖u − v‖² ≠ 2 − 2⟨u, v⟩.)* (e) The idea in two sentences.
  - **B1 (proof ordering).** The proof of (a) of the triangle inequality, shuffled. Lines: (i) ‖x + y‖² = ⟨x + y, x + y⟩; (ii) = ‖x‖² + 2⟨x, y⟩ + ‖y‖²; (iii) ≤ ‖x‖² + 2|⟨x, y⟩| + ‖y‖² (by (c) of the absolute-value rules); (iv) ≤ ‖x‖² + 2‖x‖‖y‖ + ‖y‖² (by Cauchy–Schwarz); (v) = (‖x‖ + ‖y‖)²; (vi) both sides are ≥ 0, so take roots (`@fd3:prp-ordered-ring-rules` (g)). Distractors: (D1) taking roots term by term (√(2⟨x, y⟩) may be undefined); (D2) "≤ ‖x‖² + 2⟨x, y⟩² + ‖y‖²", which fails at x = y = e_1/2 (1/2 > 1/8). The only admissible order is (i)–(vi), with (vi)'s remark allowed first.
  - **B2 (faded, last step blank).** ‖x − y‖ = ‖x + y‖ iff x ⊥ y. Given: both expansions. *Name the move, then complete it.* *(Expand the square: both norms are ≥ 0, so they are equal iff their squares are, iff 4⟨x, y⟩ = 0.)*
  - **B3 [Prove or disprove].** (a) ⟨x, y⟩ ≤ ½(‖x‖² + ‖y‖²). *(**True**: ‖x − y‖² ≥ 0.)* (b) ‖x + y‖ ≥ ‖x‖. *(**False**: y = −x ≠ 0.)* (c) Unit u, v with ⟨u, v⟩ = 1 are equal. *(**True**.)* (d) Equality in Cauchy–Schwarz only when x = y. *(**False**: y = 2x ≠ 0.)* (e) ⟨x, y⟩ ≤ ‖x‖‖y‖/2. *(**False**: x = y = e_1. The statement is homogeneous, so normalizing is legitimate and reduces it to "⟨u, v⟩ ≤ 1/2 for unit u, v", which fails at u = v.)*
  - **B4.** (a) (Σx_k)² ≤ nΣx_k², with equality iff all x_k are equal. (b) Minimize ‖x‖² subject to x_1 + 2x_2 + 2x_3 = 9. *(9 ≤ 3‖x‖, so the minimum is 9, attained only at (1, 2, 2).)*
  - **C1 [Exit check: Cauchy–Schwarz].** Prove (a) and (b) from the definitions. *Hint ladder:* (1) dispose of the zero cases, then scale to length 1; (2) expand ‖u ∓ v‖². **Marking (10):** 1 zero cases; 2 reduction with homogeneity and factor > 0; 3 |⟨u, v⟩| ≤ 1 (any correct route); 1 scale back; 3 equality case both ways. *Fatal:* dividing by ‖x‖ unchecked; proving only the one-sided inequality and claiming the absolute value; omitting the converse. Second routes: projection (§06) or Lagrange (C2), each mapped onto the same points.
  - **C2 (Lagrange's identity).** Prove (Σx_k²)(Σy_k²) − (Σx_k y_k)² = ½ Σ_j Σ_k (x_j y_k − x_k y_j)², and deduce `cor-cauchy-schwarz-sums` with its equality case: equality iff x_j y_k = x_k y_j for all j, k, iff x and y are parallel. *Hint ladder:* (1) expand the square inside the double sum and use `prp-sum-rules` (c) three times; (2) for "parallel", if x = 0 it is clear; otherwise pick m with x_m ≠ 0 and set c = y_m/x_m. *Answer.* The double sum of x_j²y_k² − 2x_j y_j x_k y_k + x_k²y_j² is 2(Σx_j²)(Σy_k²) − 2(Σx_j y_j)². The right side is ≥ 0 and is zero iff every term is zero (`lem-nonnegative-sum-zero`). If all minors vanish and x_m ≠ 0, then y_k = (y_m/x_m)x_k for every k. Conversely y = cx makes each minor c(x_j x_k − x_k x_j) = 0.

### 4.6 Section 9.6 Projection onto a Line and the Cosine of an Angle (`06-projection-and-angle.md`)

*Budget 4,200 (R group in the exercises). Method section: **subtract the projection**, full; normalize at Idea level; expand the square terse. Key proof: `thm-projection-closest-point`.*

- **Hook.** Which point of {ty} is nearest to x? In the plane one drops a perpendicular. Without pictures, we look for t with x − ty ⊥ y; Pythagoras then shows the point is nearest. Divided by lengths, the same split gives the cosine of an angle.
- **`[Scratch work]` + Givens/Goal.** Givens: x, y with y ≠ 0. Goal: find t with ‖x − ty‖ ≤ ‖x − sy‖ for all s. Row 2 (guess: the error is perpendicular): ⟨x − ty, y⟩ = 0, so t₀ = ⟨x, y⟩/‖y‖². Row 3: x − sy = (x − t₀y) + (t₀ − s)y, two orthogonal pieces. The gap is closed by Pythagoras.
- **`def-projection-rn`** (major). For y ≠ 0, proj_y x ≔ (⟨x, y⟩/‖y‖²)y. For unit u it is ⟨x, u⟩u; proj_{e_k} x = x_k e_k.
- **`exm-method-subtract-the-projection`** `[Method: subtract the projection]`. *Template:* write x = p + (x − p) with p = proj_y x; then x − p is orthogonal to every multiple of y, and Pythagoras splits each length. *When:* distance to a line through 0; inequalities between ⟨x, y⟩ and lengths. *Usual failures:* y = 0; projecting onto the wrong vector (B2 (e)); dividing by ‖y‖ instead of ‖y‖². Worked examples: the theorem and `exm-distance-to-a-line-through-the-origin`.
- **`thm-projection-closest-point`** (key proof). Let y ≠ 0, t₀ = ⟨x, y⟩/‖y‖² and p = t₀y. (a) x − p ⊥ y, and t₀ is the only t with x − ty ⊥ y. (b) For all t, ‖x − ty‖² = ‖x − p‖² + (t − t₀)²‖y‖², so ‖x − ty‖ ≥ ‖x − p‖, with equality iff t = t₀. (c) ‖x‖² = ‖p‖² + ‖x − p‖², and ‖p‖ = |⟨x, y⟩|/‖y‖.
  - *Try it first: for x = (3, 1), y = (1, 1), minimize ‖x − ty‖² by completing the square in t; then do it in general.* *Idea:* completing the square works but hides why; orthogonality explains it.
  - *Proof:* (a) ⟨x − ty, y⟩ = ⟨x, y⟩ − t‖y‖². (b) Split, apply Pythagoras and `prp-norm-basic-rn` (b); the extra term is ≥ 0, and zero iff t = t₀. (c) is (b) at t = 0. *Self-explanation prompt* at (a): *why is t₀ the only such t?*
  - **"Alternatively"** (STYLE §4): by (c), ⟨x, y⟩²/‖y‖² ≤ ‖x‖², which is Cauchy–Schwarz again, and ‖x‖²‖y‖² − ⟨x, y⟩² = ‖y‖²‖x − p‖²: the defect is a squared distance.
- **`exm-distance-to-a-line-through-the-origin`.** (a) x = (3, 1), y = (1, 1): t₀ = 2, p = (2, 2), distance √2. (b) x = (1, 2, 3), y = (1, 1, 1): t₀ = 2, ‖x − ty‖² = 2 + 3(t − 2)² (at t = 0 this is 14). Lines not through 0 are Ch10's.
- **`def-angle-cosine-rn`** (major; slogan *the dot product of the two directions*). Weird examples come first as a Quick check: x with itself, with −x, with an orthogonal vector *(1, −1, 0)*. For x, y ≠ 0, cos∠(x, y) ≔ ⟨x, y⟩/(‖x‖‖y‖) ∈ [−1, 1] by Cauchy–Schwarz.
- **`prp-angle-cosine-properties`.** (a) It is symmetric and equals ⟨x/‖x‖, y/‖y‖⟩ (Idea: back-reference to normalize). (b) For ab ≠ 0, cos∠(ax, by) = ±cos∠(x, y), with the sign of ab. (c) It is 1 iff y = cx with c > 0, −1 iff y = cx with c < 0, and 0 iff x ⊥ y (by (c), (c′) of `thm-cauchy-schwarz-rn`; c ≠ 0 since y ≠ 0). (d) The law of cosines, ‖x − y‖² = ‖x‖² + ‖y‖² − 2‖x‖‖y‖cos∠(x, y), proved tersely.
- **`exm-angles-computed`.** cos∠((1, 0), (1, 1)) = 1/√2. cos∠((1, 2, 2), (2, −1, 2)) = 4/9. In the unit cube: body diagonal against edge, 1/√3; two body diagonals (1, 1, 1), (1, 1, −1), 1/3; body against face diagonal (1, 1, 0), √6/3.
- **Looking-ahead box** `[Looking ahead: the angle itself]`. An angle θ ∈ [0, π] with cos θ = cos∠(x, y) needs the function cos. This book only borrows cos, in Section 3.5's facts (T1)–(T5) (`@ax-cosine-sine`). Nothing in this chapter or the next defines or uses θ; the analysis volumes do, once cos has been constructed. Next, Ch10 uses projection for distances to lines and hyperplanes.
- **Warning.** proj_y x is a vector, while ⟨x, y⟩/‖y‖ is a number. proj_y x depends only on the line of y, but ⟨x, y⟩ depends on y's length.
- **Quick check.** proj_{(1, 0)}(2, 3)? cos∠((1, 1), (−1, −1))? *((2, 0); −1.)*
- **Exercises.**
  - **A1** (5 parts, key proof). (a) Why y ≠ 0? *(We divide by ‖y‖²; for y = 0 every t gives 0, so uniqueness fails.)* (b) Where is x − p ⊥ y used? *(It kills the cross term.)* (c) Run (b) on x = (1, 2, 3), y = (1, 1, 1) at t = 0 and t = 1. *(14 = 2 + 12; 5 = 2 + 3.)* (d) Compute proj_{(1, 2, 2)}(3, 0, 0) and check the orthogonality. *(p = (1/3, 2/3, 2/3); (8/3, −2/3, −2/3) · (1, 2, 2) = 0.)* (e) The idea in two sentences.
  - **B1 (faded, last half blank).** Apollonius: ‖x − z‖² + ‖y − z‖² = ½‖x − y‖² + 2‖z − m‖² with m = (x + y)/2. Given: x − z = (x − m) + (m − z) and y − z = −(x − m) + (m − z). *Name the move, then complete it.* *(Expand: the cross terms cancel, leaving 2‖x − m‖² + 2‖m − z‖², and 2‖x − m‖² = ½‖x − y‖².)*
  - **B2 [Prove or disprove]** (y ≠ 0). (a) proj_y proj_y x = proj_y x. *(**True**.)* (b) proj_y(x + z) = proj_y x + proj_y z. *(**True**.)* (c) proj_{cy} x = proj_y x for c ≠ 0. *(**True**.)* (d) ‖proj_y x‖ ≤ ‖x‖. *(**True**, by (c).)* (e) proj_y x = proj_x y for nonzero x, y. *(**False**: (1, 0), (1, 1) give (1/2, 1/2) ≠ (1, 0).)* (f) x ⊥ y ⇒ proj_y x = 0. *(**True**.)*
  - **B3.** (a) The point of {t(2, 1, −2)} nearest (1, 1, 1), and the distance. *(t₀ = 1/9, p = (2/9, 1/9, −2/9), distance √26/3; check 3 − 1/9 = 26/9.)* (b) For y ≠ 0, show there are at most two t with ‖x + ty‖ = 1. *(Square: ‖y‖²t² + 2⟨x, y⟩t + ‖x‖² − 1 = 0. The polynomial ‖y‖²X² + 2⟨x, y⟩X + (‖x‖² − 1) ∈ ℝ[X] has degree 2 because ‖y‖² ≠ 0, and its value at t is the left side (`@thm-evaluation-respects-operations`). So `@thm-polynomial-root-count` allows at most 2 roots.)*
  - **C1 [Exit check: the projection theorem].** For y ≠ 0, exactly one t minimizes ‖x − ty‖; it is t₀, and x − t₀y ⊥ y. *Hint ladder:* (1) make x − ty orthogonal to y; (2) split and use Pythagoras. **Marking (10):** 2 t₀ from orthogonality, dividing by ‖y‖² ≠ 0; 2 x − t₀y ⊥ y; 3 the identity (or completing the square); 2 minimality and uniqueness from ‖y‖² > 0; 1 conclusion. *Fatal:* an unchecked division; derivatives (unavailable); "the vertex of a parabola" without the identity.
  - **C2.** Combine the "Alternatively" identity with §05 C2: ‖y‖²‖x − proj_y x‖² = ½ΣΣ(x_j y_k − x_k y_j)². For n = 2, deduce that the distance from x to the line of y is |x_1y_2 − x_2y_1|/‖y‖. *Hint ladder:* (1) both expressions equal ‖x‖²‖y‖² − ⟨x, y⟩²; (2) for n = 2 the double sum has two nonzero terms, each (x_1y_2 − x_2y_1)². *Answer* as hinted; take nonnegative roots. The solution adds in prose that |x_1y_2 − x_2y_1| will be the area of the parallelogram on x and y; area is not defined in this book.
  - **R. Review** (no source named in the problems; solutions cite; each ≤ 20 min).
    - **R1** (Ch8, factor out y − x). For y ≠ 0 and t₀ as above, g(t) ≔ ‖x − ty‖ is strictly increasing on [t₀, ∞). *Solution:* for t₀ ≤ s < t, g(t)² − g(s)² = (t − s)(t + s − 2t₀)‖y‖² > 0, by the theorem's (b) and Ch8's method box; both values are ≥ 0, so g(s) < g(t) (`@fd3:prp-ordered-ring-rules` (g)); `def-monotone-function` closes it.
    - **R2** (Ch5, homomorphisms). Fix a ∈ ℝⁿ. Show that φ(x) ≔ ⟨a, x⟩ is a homomorphism (ℝⁿ, +) → (ℝ, +), find its kernel, and decide when φ is injective. *Solution:* (ℝⁿ, +) is a group by laws (a)–(d) (`@def-group`); φ(x + y) = φ(x) + φ(y) by linearity (`@def-group-homomorphism`); ker φ = {x : x ⊥ a}. If a = 0 the kernel is ℝⁿ. If n ≥ 2 and a ≠ 0, the kernel contains a nonzero vector: with a_1 ≠ 0 take a_2e_1 − a_1e_2, and with a_1 = 0 take e_1. If n = 1 and a ≠ 0 the kernel is {0}. So φ is injective iff n = 1 and a ≠ 0 (`@prp-homomorphism-injective-iff-kernel-trivial`).
    - **R3** (spiral, Part I: Ch3). For z, w ∈ ℂ, prove |z + w| = |z| + |w| iff z = 0 or w = cz for a real c ≥ 0. *Solution:* by `prp-plane-is-complex-plane` (a), (c), this is the equality case of `thm-triangle-inequality-rn` (a) for n = 2; real multiples in ℂ are scalar multiples. Section 3.3 proved the inequality by conjugates (`@thm-complex-triangle-inequality`).
    - **R4** (no hint). Find all x ∈ ℝⁿ with Σx_k = n and Σx_k² = n. *Solution:* with 1 = (1, …, 1), n = ⟨x, 1⟩ ≤ ‖x‖√n = n, so equality holds and x = c1 with c ≥ 0 (theorem (c)); hence x = 1. A second route: Σ(x_k − 1)² = 0. Look-alike that fails: coordinatewise reasoning, since each equation mixes all coordinates.

### 4.7 `index.md`

- **Story.** Analysis in several variables needs, constantly, that a straight path is shortest. In ℝ that is |·|'s triangle inequality (cases on signs). In ℂ = ℝ² it came from complex multiplication. In ℝⁿ neither tool exists: this chapter measures length with the dot product and proves the inequality with no picture, through Cauchy–Schwarz. The same tools give the distance to a line and the cosine of an angle.
- **What you need:** *Number Systems*, Chapters 2, 4, 5, 6 (by label); *Sets and Functions*, Chapters 1–3 (tuples, functions, recursion, finite sums and maxima); this book's Chapter 1 (finite sums, square roots) and Chapter 3 (ℂ, for §04's link and one hook). Chapters 2, 4–8 appear only in remarks and review items. Linear algebra is not needed.
- **Time** line (§7). **Roadmap**: one sentence per section, with delivered titles. **Named moves**: the four boxes. One sentence for readers who know linear algebra: this is the standard inner product on ℝⁿ done in coordinates, and LA1.1 and LA3.11 give the abstract version.
- **Summary** and **Terms** (box, distance, dot product, norm, orthogonal, parallel, projection, standard vectors, unit vector, cosine of the angle), each with its label.

---

## 5. Exports (planned consumers)

| Labels | Consumers |
|---|---|
| `def-real-n-space`, `def-vector-operations-rn`, `prp-vector-space-laws-rn`, `def-standard-basis-rn` | Ch10; AN1.4, AN1.7, AN2.1 (ex-F4.11 material, citing `@fd4:`); LA1.1 (see) |
| `def-box-rn`, `prp-norm-coordinate-bounds`, `cor-balls-and-boxes-rn` | AN1.4, AN1.2, AN2.3, AN3.4 |
| `def-dot-product-rn`, `prp-dot-product-laws-rn`, `prp-orthogonal-test-rn`, `prp-polarization-rn` | Ch10 (hyperplanes ⟨a, x⟩ = c), AN1.7, LA3.11 (see), GEO (isometries, now out of this book) |
| `def-norm-rn`, `def-distance-rn`, `prp-norm-basic-rn`, `prp-distance-basic-rn`, `prp-parallelogram-law-rn` | Ch10, AN2.1 (d₂ as the model metric; the parallelogram law separates d₂ from d₁), AN2.3, AN1.7 |
| `thm-cauchy-schwarz-rn`, `cor-cauchy-schwarz-sums`, `thm-triangle-inequality-rn`, `cor-triangle-finite-sums-rn`, `cor-norm-sum-bound` | Ch10, AN1.2, AN1.4, AN2.1, AN1.7, AN1.8, AN2.12 (sum form); AN3.1 (norm comparison) |
| `prp-plane-is-complex-plane` | CA.1 (ℂ as a metric space), AN1.7 (complex derivative) |
| `def-projection-rn`, `thm-projection-closest-point` | Ch10 (distance to a line), LA3.11 (see) |
| `def-angle-cosine-rn`, `prp-angle-cosine-properties` | AN3.2 (prose), CA.1 (arg; prose) |

**Same statement elsewhere** (atlas triage): as in `f4-8.md`'s twins table (LA3.11 special cases and instances), plus `thm-triangle-inequality-rn` (a) at n = 2 = `@thm-complex-triangle-inequality` (other proof).

## 6. Promises

**Paid:** the spec/08 F4.8 bullet and chapter-constraints rule (§01–§06); Lang 5, 8–9 (§01, §02, §04); AN1.4, AN2.3 and AN1.7 `s: F4.8` (exports); the merge proposal §3.3 "Cauchy–Schwarz 唯一的家" (§05) and §3.4 "F4.8 points back to F4.1" (`prp-plane-is-complex-plane`).
**Opened (for STATUS):** Ch1 must provide the requests of §2 and must not state Cauchy–Schwarz or Lagrange's identity; Ch3's next revision may add a forward pointer "see Section 9.4" in its §02 (Ch3 is frozen; prose only, no action now); Ch10 uses projection and polarization; AN2.1 (ex-F4.11) uses d₂ and `cor-norm-sum-bound`; plan-edges for F4.8 should read `s: [F4.6, F2.1, F2.2, F3.2, F3.9, F3.4, F4.1]`, `see: [F5.3, F5.5, F4.7]` (atlas agent's call; not edited here).

## 7. Budgets and Time

| Section | Main line | Fold | Exercises A/B/C |
|---|---|---|---|
| 9.1 Points and Coordinates | 2,800 | 200 | 1 / 2 / 1 |
| 9.2 Adding Points and Scaling Them | 4,000 | 300 | 1 / 2 / 1 |
| 9.3 The Dot Product | 3,400 | (300 if fallback) | 1 / 3 / 1 |
| 9.4 Length and Distance | 4,600 | (400 if fallback) | 1 / 3 / 1 |
| 9.5 Cauchy–Schwarz and the Triangle Inequality | 4,600 | 0 | 1 / 4 / 2 |
| 9.6 Projection and the Cosine of an Angle | 4,200 | 0 | 1 / 3 / 2 + R1–R4 |
| **Total** | **≈ 23,600** | ≈ 500–1,200 | 6 / 17 / 8 + 4 = 35 items |

Hard cap 5,000 main-line words per section. **Time** (STYLE §11.9 formula). Reading: 23,600/400 × 15 min ≈ 14.75 h. Core: 6 A + 6 B + 6 C (exit checks included) ≈ 18 items × 30 min ≈ 9 h, so **about 25 h core**. Full: reading plus folds ≈ 15.5 h, plus 35 items × 30 min ≈ 17.5 h, so **about 35 h full** (33 rounds to 35). This matches the proposal's F4.8 row (25/40) less the C-item cut of Q4 (b), and sits inside the book total of about 257/326. Recompute from delivered counts; above 24,500 main-line words, trim §01 and §03 first.

## 8. S2a list (attack first)

1. `prp-vector-space-laws-rn` (j) and the remark under `def-parallel-rn` ("for x ≠ 0, parallel iff y = tx"): the "some k" step, n = 1, and x = 0 against y = 0.
2. Every use of "parallel" handles zero vectors (§02 B1, C1; Cauchy–Schwarz (b); §05 C2).
3. §03 C1: the solution must state its counterexample **to the step**, not to the claim.
4. Chapter 1 requests (§2): confirm Ch1's frozen labels provide `prp-sum-rules` (a)–(c), `lem-nonnegative-sum-zero` and the root facts; otherwise switch on the fallback folds. Confirm Ch1 states no Cauchy–Schwarz.
5. `prp-plane-is-complex-plane`: (a) against the exact rules of `@def-complex-numbers` and `@prp-reals-embed-complex`; (b) the sign in Re(z w̄).
6. `prp-norm-coordinate-bounds` (b) and `cor-balls-and-boxes-rn` (b): strictness, n = 1, and §04 A1 (e)'s "n ≥ 4" (n = 4 gives exactly r, so "≥ r" is right).
7. §04 C1: exactly one bad line; the remark about the −x step is accurate.
8. `thm-cauchy-schwarz-rn` (b), (c), (c′): converse directions; the case x ≠ 0, y = 0 (c = 0) and x = 0, y ≠ 0.
9. `cor-cauchy-schwarz-sums`: squaring |a| ≤ b with b ≥ 0; the equality clause.
10. §05 C2: the factor ½ and the double-sum expansion; the minors-to-parallel step when x = 0 or y = 0.
11. `thm-triangle-inequality-rn` (a) equality and B1's distractor (D2) numbers.
12. `thm-projection-closest-point` (b) for all t; §06 B3 (b): degree exactly 2, and the evaluation link from the formal polynomial in ℝ[X] to the real function (the cited Ch6 and Ch7 labels say what is needed, over the field ℝ).
13. `prp-angle-cosine-properties` (b), (c), and the use of (c′).
14. R2: kernel computation for n ≥ 2 with a_1 = 0 or a_1 ≠ 0; n = 1. R1: the sign of t + s − 2t₀ when s = t₀.
15. Looking-ahead box: the meta-claim "nothing in this chapter or the next defines or uses θ" must hold for the merged Ch10 blueprint (isometries and rotations removed under Q4 (b)).
16. Numbers (sidecars, exact `Fraction`): §01 A1 (e); §04 A1, B2; §05 A1 (c), B4 (b), the applications example (b); §06 A1 (c), (d), B3 (a) (234/81 = 26/9), the angles example, C2 for n = 2.
