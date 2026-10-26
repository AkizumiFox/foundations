<!-- hand-written -->
# Blueprint: Ch10 (F4.9) Lines, Convexity, and Isometries, absorbing F4.10, merged *Preliminaries for Analysis and Algebra*, stage S1

**Status: S1, 2026-10-26.** Next: S2, S2a (§8), S3. Supersedes `f4-9.md`. No F4.10 draft existed; §5.5 plans it from scratch.

**Authority.** The author's answers (2026-10-26) to `fd4/authoring/design/merge-proposal.md`: fd4 kept, fd5 retired, F5.x ids kept; title *Preliminaries for Analysis and Algebra*; F4.11 to AN1; book cut to about 257 / 326 h, so **the classification of isometries leaves this chapter** (§6) and C items are reduced. Proposal §3.3–§3.4: F4.10's rotations, arguments and isometries of ℂ join F4.9; F4.10's id retires. Earlier direction: moderate difficulty, proof methods in practice.

**Directory.** `fd4/src/ch10-lines-convexity-isometries/` (slug from proposal §3.3). Prose pointers: "Section 10.k" in the chapter; "Chapter 3" (F4.1, Complex Numbers), "Chapter 5" (F5.3, Groups), "Chapter 9" (F4.8, Coordinates and Vectors) as same-book pointers; other books by title. Sidecars `fd4/verify/ch10/`, ledger `fd4/authoring/ledger/ch10.yaml`.

**Title.** `# Lines, Convexity, and Isometries` (§10.5 works in ℂ; registry title updated by the coordinator, §6).

**Level reference** (coverage only): Lang *Basic Mathematics* ch. 6, 10, 12; Apostol *Calculus* I ch. 13. Every example, item and answer is the book's own; nothing from `~/book`.

**Purpose.** Give analysis the geometry of ℝⁿ it cites; say geometric notions with distances, so that isometries keep segments, lines and convexity; in the plane, read Chapter 3's multiplication as rotations and reflections, with their group, arguments, the principal argument and oriented angles (paying Chapter 9's cos∠ promise).

**Binding rules.**
1. **No linear algebra.** No span, basis, dimension, matrix, determinant. The classification "every isometry of ℝⁿ is x ↦ Ax + b with orthonormal columns", and its plane case "every isometry of ℂ is az + b or a z̄ + b", are **stated once in a Looking-ahead box (§5.5) and not proved**; linearity of an isometry fixing 0 is not proved either.
2. **Trigonometry only through Chapter 3.** §§10.1–10.4 use no cos, sin, π. §10.5 uses (T1)–(T5) of `@ax-cosine-sine` only through Chapter 3's polar form and its results, and names the fact used each time, as Chapter 3 does. No radians, no limits, no continuity ("jump" is said with two values, §5.5).
3. **No re-proof.** Chapter 9 owns inner product, norm, Cauchy–Schwarz, the triangle inequality **with its equality case**, Pythagoras, polarization, projection with the closest-point theorem, and the cosine of an angle; Chapter 3 owns ℂ, conjugation, modulus, 𝕋, polar form, n-th roots; Chapter 5 owns groups, subgroups, symmetric groups, homomorphisms. Each is recalled in a clause and cited.
4. **No topology.** "Open ball", "closed ball" are names (§10.3); one prose sentence points to *Real Numbers, Metric Spaces, and Derivatives* (AN1), which now also holds the metrics-and-norms material (former F4.11).
5. **House manner** (STYLE §1, §2 item 6, §12.5, §12.13.4, §12.14): motivation first, scratch work apart from proofs, method boxes (Template / When to use it / The usual failure, ≤ 130 words each), prose Givens/Goal tables, one Prove-or-disprove B item per method section (verdict first in the answer); moderate difficulty; no footnotes, jokes, history or first person. Quick checks about one per 800–1,000 words.
6. **Fewer C items.** One C item per section (the exit check, with marking scheme). §10.5 is an application section: no B4, R group of two.

---

## 1. Devices as applied

- **Method boxes (4)**, `::: {#exm-method-<slug>}` titled `[Method: …]`, linked from Named moves: `exm-method-parametrize`, `exm-method-equality-case` (§10.1), `exm-method-two-point-test` (§10.3), `exm-method-distances-only` (§10.4). **Reused:** Chapter 9's `exm-method-expand-the-square`, Idea level in `prp-perpendicular-bisector` and `prp-reflection-properties` (a), terse in `prp-isometry-preserves-inner-product`.
- **Non-box moves:** "Peel off the last point" (§10.3), "Reduce to the origin" (§10.4), "Turn the plane with a unit complex number" (§10.5).
- **Scratch work** at first appearances, with Givens/Goal table where marked: `exm-two-lines-in-space`, `thm-betweenness` (table), `prp-balls-convex` (table), `thm-isometry-preserves-segments` (table), `prp-reflection-in-line-complex`.
- **Fading.** Parametrize: full §10.1, Idea `prp-line-meets-sphere`. Equality case: full §10.1, Idea §10.3 B3. Two-point test: full §10.3, terse `cor-isometry-convex-image`. Distances only: full §10.4, Idea §10.4 B4 (c).
- **Prove or disprove:** B4 in §§10.1–10.4. **Try it first:** before `thm-isometry-preserves-segments`. **Motivation first:** `def-line-rn`, `def-convex-set-rn`, `def-isometry-rn`, `def-principal-argument`.
- **Threads** (index list): (1) *Must a distance-preserving map be onto?* planted §10.4, paid for ℝ (§10.4 C1) and for the maps az + b, a z̄ + b (`prp-complex-isometry-group`), in general by the Looking-ahead box; (2) *betweenness by distances*, §10.1 → §10.4, its failure for other distances (§10.3 B3) → AN1; (3) *convex and star-shaped sets* → AN2.3, CA, AM (prose); (4) *arguments are not unique* → AN2 (principal logarithm), CA (branches).

## 2. Section map, budgets, hours

| § | File | Budget | Expected |
|---|---|---|---|
| 10.1 | `01-lines-and-segments.md` | ≤ 5,000 | ~3,600 |
| 10.2 | `02-hyperplanes-and-nearest-points.md` | ≤ 5,000 | ~3,300 |
| 10.3 | `03-convex-sets-and-hulls.md` | ≤ 5,000 | ~3,400 |
| 10.4 | `04-isometries-of-rn.md` | ≤ 5,000 | ~3,300 |
| 10.5 | `05-rotations-and-the-complex-plane.md` | ≤ 5,000 | ~3,900 |

Expected main line ~17,500 words; folds ~600. **Time** (index): "about 18 hours on the core track and about 22 hours for everything", recomputed with `check_structure.py --words` after S3. Derivation, consistent with the approved 257 / 326 h book total: proposal §3.3 row 10 (32 / 45, with F4.10 absorbed) − classification (14 / 20, proposal §3.5 item 2) − C-item cut (0 / 3) = **18 / 22**.

## 3. Labels

All new; grepped 2026-10-26 against `foundations/fd*/src`, `linear-algebra/src`, `linear-algebra-split`, `analysis-series`: no collision in any src. Blueprint overlaps resolved as pointers (§6): `def-principal-argument` (an2), `def-star-shaped` (am), `def-ball-rn` (f4-11). Slugs `convex-sets-and-hulls`, `isometries-of-rn` avoid LA's `exr-convex-sets-*`.

- **10.1:** `def-line-rn`, `prp-line-parametrizations`, `prp-line-through-two-points`, `def-collinear`, `exm-two-lines-in-space`, `exm-method-parametrize`, `def-segment-rn`, `lem-subsegment`, `thm-betweenness`, `exm-method-equality-case`, `cor-point-pinned-on-segment`; `exr-lines-and-segments-a1`, `-a2`, `-b1`…`-b4`, `-c1`.
- **10.2:** `def-hyperplane-rn`, `prp-hyperplane-normals`, `exm-lines-in-the-plane`, `prp-perpendicular-bisector`, `prp-nearest-point-on-line`, `prp-nearest-point-on-hyperplane`, `def-sphere-rn`, `prp-line-meets-sphere`, `prp-segment-crosses-hyperplane`; `exr-hyperplanes-and-nearest-points-a1`, `-a2`, `-b1`…`-b4`, `-c1`.
- **10.3:** `def-convex-set-rn`, `def-ball-rn`, `exm-method-two-point-test`, `prp-balls-convex`, `prp-convex-examples`, `prp-convex-operations`, `def-convex-combination-rn`, `thm-convex-contains-combinations`, `def-convex-hull-rn`, `thm-convex-hull-combinations-rn`, `exm-triangle-as-hull`, `def-star-shaped`, `exm-star-not-convex`; `exr-convex-sets-and-hulls-a1`, `-a2`, `-b1`…`-b4`, `-c1`.
- **10.4:** `def-isometry-rn`, `exm-isometry-examples`, `def-reflection-hyperplane`, `prp-reflection-properties`, `prp-isometry-composition`, `prp-isometry-reduce-to-origin`, `prp-isometry-preserves-inner-product`, `exm-method-distances-only`, `thm-isometry-preserves-segments`, `cor-isometry-convex-image`; `exr-isometries-of-rn-a1`, `-a2`, `-b1`…`-b4`, `-c1`.
- **10.5:** `lem-complex-plane-inner-product`, `prp-complex-plane-isometries`, `def-rotation-about-point`, `prp-reflection-in-line-complex`, `thm-two-reflections-rotation`, `prp-complex-isometry-group`, `def-argument-set`, `prp-argument-of-product`, `def-principal-argument`, `exm-principal-argument-not-additive`, `thm-angle-in-the-plane`; `exr-rotations-and-the-complex-plane-a1`, `-a2`, `-b1`…`-b3`, `-c1`, `-r1`, `-r2`.

**Key proofs** (STYLE §11.2): `thm-betweenness`, `thm-isometry-preserves-segments`, `thm-convex-hull-combinations-rn`, `prp-complex-isometry-group`.

## 4. Allowed prerequisites (every label cited)

- **fd2** (exist at HEAD, grepped): `@fd2:def-injective`, `@fd2:def-surjective`, `@fd2:def-inverse-function`, `@fd2:thm-bijection-iff-inverse`, `@fd2:def-family-union-intersection`, `@fd2:prp-smallest-closed-set` (pattern), `@fd2:thm-induction`.
- **fd3** (exist at HEAD; item letters re-checked at S2a, fd3 is being re-cut): `@fd3:prp-ordered-ring-rules` ((b) adding, (e) squares positive, (f) no zero divisors, (g) 0 ≤ a < b ⇔ a² < b²), `@fd3:prp-ordered-field-halves`, `@fd3:prp-absolute-value-ordered-field`, `@fd3:prp-cof-square-roots` with `@fd3:thm-reals-complete-ordered-field`, `@fd3:def-complete-ordered-field` (§10.3 C1), `@fd3:thm-cof-complete-archimedean` and `@fd3:prp-integer-part-ordered-field` (§10.5, principal argument).
- **Same book, Chapter 3 (F4.1; now `fd4/src/ch01-complex-numbers/`, grepped):** `@def-complex-numbers`, `@def-conjugate-modulus`, `@thm-conjugate-properties`, `@prp-complex-square-roots`, `@prp-unit-circle`, `@ax-cosine-sine`, `@def-polar-form`, `@thm-polar-multiplication`, `@prp-polar-form`, `@exm-special-angles`, `@thm-complex-nth-roots`.
- **Same book, Chapter 5 (F5.3; now `fd5/src/ch03-groups-and-permutations/`, grepped):** `@def-group`, `@def-symmetric-group`, `@thm-subgroup-test`, `@def-group-homomorphism`, `@prp-homomorphism-injective-iff-kernel-trivial`.
- **Same book, Chapter 9 (F4.8; labels from `f4-8.md` §Labels, provisional, S2a 1):** `def-vector-operations-rn`, `def-norm-rn`, `prp-norm-basic-rn`, `def-distance-rn`, `exm-method-expand-the-square`, `prp-pythagoras-rn`, `prp-polarization-rn`, `thm-triangle-inequality-rn`, `def-projection-rn`, `thm-projection-closest-point`, `def-angle-cosine-rn`.
- **Same book, Chapter 1 (F4.6):** no blueprint yet; this chapter cites nothing from it by label (re-indexing a finite sum and completing a square are done inline in one line each). S2a 6.
- **Never:** an1/an2/ca/am, la*, geo; later chapters. Prose pointers by title only.

**Notation** (`NOTATION.md` rows, coordinator at S3; macros `\inner`, `\norm`, `\abs`, `\conj`, `\nT` exist):
- p + ℝv, the line (`def-line-rn`); [p, q] the segment (`def-segment-rn`), **clash** with intervals: for n = 1 and p ≤ q it is the interval [p, q], for p > q the interval [q, p]; written only for declared points of ℝⁿ.
- H_{a,c} = {x : ⟨a, x⟩ = c}, a ≠ 0 (`def-hyperplane-rn`); S(c, r) sphere; B(c, r), B̄(c, r) balls (amend the metric-space row: Euclidean case first here, general case AN1); `\operatorname{conv} S`.
- τ_b translation, ρ_{a,c} reflection in H_{a,c} (§10.4); σ_u(z) ≔ u² z̄ for u ∈ 𝕋, local to §10.5 (restated where used).
- `\arg z` ⊆ ℝ, a **set** (`def-argument-set`); `\operatorname{Arg} z` ∈ (−π, π] (`def-principal-argument`). Amend the `\cos\angle(x, y)` row: "the promise to F4.10 is paid in F4.9 §05 (`thm-angle-in-the-plane`)".

---

## 5. Per-section plans

### 5.0 `index.md`

- **Story** (~150 words): what the distance alone determines (lines, segments, hyperplanes, spheres, balls, convex sets); "between" is a statement about distances, so isometries keep segments, lines and convex sets; in the plane, turning is multiplying by a unit complex number and these maps form a group; arguments are sets, and choosing one number per point breaks "arguments add", a first sign of branches.
- **What you need.** Chapter 9; Chapter 3, Sections 3.2, 3.4, 3.5; Chapter 5, Sections 5.1–5.3 (§10.5 only); *Number Systems* and *Sets and Functions* as in §4.
- **Borrowed results.** Box **No new borrowed facts.**: Sections 10.1–10.4 use no cosine, sine or π; Section 10.5 uses (T1)–(T5) only through Chapter 3's polar form.
- **Time** as §2. **Roadmap**: one bullet per section, naming its main result. **Named moves**, **Threads**: §1.

### 5.1 Section 10.1: Lines and Segments (`01-lines-and-segments.md`)

**Budget** ≤ 5,000 (~3,600). One fold (p = q in `cor-point-pinned-on-segment`). Three Quick checks, one warning, one notation remark.

**Opening (~100).** In ℝ² a line is ax + by = c; in ℝ³ one equation gives a plane: {x₁ + x₂ + x₃ = 1} contains (1, 0, 0), (0, 1, 0), (0, 0, 1), which lie on no common line (shown after the definition: the line through the first two is (1, 0, 0) + ℝ(−1, 1, 0), third coordinate always 0). A line has one degree of freedom: one parameter.

**`## Lines` (~800).**
1. **`def-line-rn`** `[Lines in ℝⁿ]`: for p, v ∈ ℝⁿ, v ≠ 0, p + ℝv ≔ {p + tv : t ∈ ℝ}; L is a **line** if L = p + ℝv for some such p, v; t ↦ p + tv is a **parametrization**.
2. **Quick check** (weird examples): (a) is {p} a line? (b) is ℝ a line in ℝ¹? (c) is (3, 5, 7) on (1, 1, 1) + ℝ(1, 2, 3)? (d) is the parameter of a point unique? *Solution:* (d) first: p + tv = p + uv gives (t − u)v = 0, so |t − u|‖v‖ = 0 (`prp-norm-basic-rn`), t = u; hence (a) no, a line has distinct points for distinct t; (b) yes, 0 + ℝ·1; (c) yes, t = 2.
3. **`prp-line-parametrizations`** `[When Two Parametrizations Give the Same Line]`: p + ℝv = p′ + ℝv′ iff p′ ∈ p + ℝv and v′ = λv, λ ≠ 0. *Proof.* (⇐) p′ = p + sv gives p′ + tv′ = p + (s + tλ)v and p + tv = p′ + ((t − s)/λ)v′. (⇒) p′, p′ + v′ ∈ p + ℝv: p′ = p + sv, p′ + v′ = p + uv; subtract: v′ = (u − s)v, nonzero factor since v′ ≠ 0.
4. **`prp-line-through-two-points`** `[Two Points Determine a Line]`: for p ≠ q exactly one line contains both, p + ℝ(q − p). *Proof.* t = 0, 1. If r + ℝv contains both, q − p = (u − s)v with u ≠ s; apply 3.
5. **`def-collinear`**: points are collinear if one line contains them all.

**`## Meeting points` (~600).**
1. **`exm-two-lines-in-space`**: L₁ = (1, 0, 1) + ℝ(1, 1, 0), L₂ = (0, 2, 0) + ℝ(1, 0, 1), L₃ = (2, 1, 1) + ℝ(0, 1, 1). Do L₁, L₂ meet? L₁, L₃?
   - **`[Scratch work]`** (≤ 10 lines): a common point has a parameter on each line, not necessarily equal; two letters; one equation per coordinate.
   - *Solution.* (1 + s, s, 1) = (t, 2, t): s = 2, t = 1, then 3 ≠ 1: no common point; directions not multiples ((1, 1, 0) = λ(1, 0, 1) forces λ = 1 and λ = 0): **skew**. (1 + s, s, 1) = (2, 1 + u, 1 + u): u = 0, s = 1, first coordinate 2 = 2: they meet at (2, 1, 1).
2. **`exm-method-parametrize`** `[Method: parametrize and solve]`. *Template.* Give each line or segment its own parameter; one equation per coordinate; solve; check every equation, and for a segment the range [0, 1]. *When.* Membership in lines, segments, rays; meeting points. *Usual failure.* One letter for two parameters; not checking the unused coordinates.

**`## Segments` (~600).**
1. **`def-segment-rn`**: [p, q] ≔ {(1 − t)p + tq : t ∈ [0, 1]}; midpoint (p + q)/2. Remarks: (1 − t)p + tq = p + t(q − p); [p, q] = [q, p]; [p, p] = {p}.
2. **Notation remark** `**Segments and intervals.**` (the clash, §4).
3. **`lem-subsegment`**: x, y ∈ [p, q] ⇒ [x, y] ⊆ [p, q]. *Proof.* x = p + s(q − p), y = p + u(q − p); (1 − t)x + ty = p + ((1 − t)s + tu)(q − p) with 0 ≤ (1 − t)s + tu ≤ 1 (`@fd3:prp-ordered-field-halves`, `@fd3:prp-ordered-ring-rules` (b)).
4. **Quick check.** Is (2, 0, 1) on [(1, −1, 2), (3, 0, 0)]? *Solution:* no; (1, 1, −1) is not a multiple of (2, 1, −2) (first coordinates force 1/2, second 1).

**`## Between by distances` (~1,400).**
1. Lead (~80): ‖p − q‖ ≤ ‖p − x‖ + ‖x − q‖; the picture says equality exactly on [p, q]. Chapter 9 already knows when the triangle inequality is an equality (`thm-triangle-inequality-rn` (a): ‖u + w‖ = ‖u‖ + ‖w‖ iff u = 0 or w = cu, c ≥ 0); recall it in one sentence, no proof.
2. **`thm-betweenness`** `[Points Between Two Points]`: x ∈ [p, q] iff ‖p − x‖ + ‖x − q‖ = ‖p − q‖. Moreover, if x = (1 − t)p + tq with t ∈ [0, 1], then ‖p − x‖ = t‖p − q‖, ‖x − q‖ = (1 − t)‖p − q‖.
   - **`[Scratch work]`** with table. Name u ≔ x − p, w ≔ q − x; u + w = q − p.

     | Givens | Goal |
     |---|---|
     | ‖p − x‖ + ‖x − q‖ = ‖p − q‖ | x = p + t(q − p), t ∈ [0, 1] |
     | ‖u‖ + ‖w‖ = ‖u + w‖ | same |
     | u = 0, or w = cu with c ≥ 0 (Chapter 9) | u = 0: t = 0. w = cu: q − p = (1 + c)u, t = 1/(1 + c) ∈ (0, 1] |

   - *Proof.* (⇒, moreover) x − p = t(q − p), q − x = (1 − t)(q − p), norms by `prp-norm-basic-rn` (b) with t, 1 − t ≥ 0; they add to ‖p − q‖. (⇐) as in the table, citing `thm-triangle-inequality-rn` (a); 1 + c ≥ 1 > 0, so 0 < 1/(1 + c) ≤ 1.
   - Aftermath: the right side mentions only distances; Section 10.4 uses exactly this.
3. **`exm-method-equality-case`** `[Method: use the equality case]`. *Template.* A known inequality A ≤ B holds with A = B. Recall its exact equality condition (usually: vectors are non-negative multiples of each other), write it with a named multiplier, solve. *When.* A sum of distances equals a distance; Cauchy–Schwarz is sharp; "extreme case" questions. *Usual failure.* Dropping the sign (c ≥ 0 separates [p, q] from the rest of the line) or the case u = 0.
4. **`cor-point-pinned-on-segment`** `[A Point Is Pinned by Its Distances to the Ends]`: if s, r ≥ 0 and s + r = ‖p − q‖, exactly one x has ‖p − x‖ = s, ‖x − q‖ = r; for p ≠ q it is p + (s/‖p − q‖)(q − p). *Proof.* That point works (moreover clause, t = s/‖p − q‖). Any such x lies on [p, q] by the theorem, x = (1 − t′)p + t′q, and s = t′‖p − q‖ fixes t′, hence x. p = q in the fold.
5. **Quick check.** The midpoint is the only point at distance ‖p − q‖/2 from both ends. *Solution:* s = r = ‖p − q‖/2.
6. **Warning** `**Equal distances do not make a midpoint.**` p = (−1, 0), q = (1, 0), x = (0, 1): ‖p − x‖ = ‖x − q‖, x ∉ [p, q]. Section 10.2 finds all such x.

**Exercises.**
- **A1.** (a) Parametrize the line through (1, −1, 2) and (3, 0, 0); is (5, 1, −2) on it? (b) The midpoint of the segment between them. *Answers:* (a) (1, −1, 2) + ℝ(2, 1, −2); yes, t = 2. (b) (2, −1/2, 1).
- **A2.** Show (1, 2), (3, 5), (7, 11) are collinear and find which lies between the others. *Answer:* (6, 9) = 3(2, 3): parameters 0, 1, 3 on (1, 2) + ℝ(2, 3); (3, 5) = (1, 2) + (1/3)((7, 11) − (1, 2)), so (3, 5) is between.
- **B1.** For v ≠ 0 and a < b: p + tv ∈ [p + av, p + bv] iff a ≤ t ≤ b. *Answer:* (⇐) s ≔ (t − a)/(b − a) ∈ [0, 1] gives (1 − s)(p + av) + s(p + bv) = p + tv. (⇒) p + tv = p + ((1 − s)a + sb)v, s ∈ [0, 1]; parameters are unique, so t = a + s(b − a) ∈ [a, b].
- **B2.** In ℝ², v, v′ ≠ 0. (a) v′ is a multiple of v iff v₁v′₂ − v₂v′₁ = 0. (b) If not, p + ℝv and p′ + ℝv′ meet in exactly one point. *Answer:* (a) (⇒) substitute. (⇐) if v₁ ≠ 0, λ ≔ v′₁/v₁ gives λv₂ = v₁v′₂/v₁ = v′₂; if v₁ = 0 then v₂ ≠ 0 and λ ≔ v′₂/v₂ works. (b) With d ≔ p′ − p, p + sv = p′ + tv′ is sv₁ − tv′₁ = d₁, sv₂ − tv′₂ = d₂; D ≔ v₁v′₂ − v₂v′₁ ≠ 0; eliminating, sD = d₁v′₂ − d₂v′₁, tD = d₁v₂ − d₂v₁; so at most one solution, and substitution shows it is one. (Sidecar.)
- **B3.** Show ℝ(1, 0, 0) and (0, 1, 0) + ℝ(0, 0, 1) are skew. *Answer:* (s, 0, 0) = (0, 1, t) fails in the second coordinate; (1, 0, 0) = λ(0, 0, 1) fails in the first.
- **B4** (prove or disprove). (a) ‖p − x‖ = ‖x − q‖ = ‖p − q‖/2 ⇒ x is the midpoint. (b) ‖p − x‖ = ‖x − q‖ ⇒ x ∈ [p, q]. (c) Any three points of ℝ² are collinear. (d) p + ℝv = p + ℝw ⇒ v = w. (e) Two lines with two distinct common points are equal. *Answers:* (a) true (Quick check). (b) false (the warning). (c) false: (0, 0), (1, 0), (0, 1). (d) false: w = 2v. (e) true: `prp-line-through-two-points`.
- **C1** (exit check). Of three distinct collinear points, exactly one lies between the other two. *Answer:* one parametrization p + t_iv, distinct t_i, relabel t₁ < t₂ < t₃; by B1 the middle one is between the others; if p + t₁v ∈ [p + t₂v, p + t₃v], B1 gives t₂ ≤ t₁, contradiction; likewise t₃. *Marking scheme* (5): common parametrization with distinct parameters (1); ordering (1); existence (1); uniqueness of parameters used (1); the two exclusions (1).

### 5.2 Section 10.2: Hyperplanes and Nearest Points (`02-hyperplanes-and-nearest-points.md`)

**Budget** ≤ 5,000 (~3,300). Three Quick checks. Uses Chapter 9's expand-the-square at Idea level; counts as a method section for the B4 rule (the move in a new setting).

**Opening (~80).** One linear equation cuts out a hyperplane; distances to it have a formula, and expanding a square linearizes distance conditions.

**`## Hyperplanes` (~1,000).**
1. **`def-hyperplane-rn`**: for a ≠ 0, c ∈ ℝ, H_{a,c} ≔ {x : ⟨a, x⟩ = c}; a is a **normal vector**; {⟨a, x⟩ ≤ c}, {≥ c} closed half-spaces, < and > open half-spaces. Sentence: p₀ ≔ (c/‖a‖²)a ∈ H_{a,c}, and x ∈ H_{a,c} iff x − p₀ ⊥ a.
2. **`prp-hyperplane-normals`**: H_{a,c} = H_{a′,c′} iff (a′, c′) = (λa, λc), λ ≠ 0. *Proof.* (⇐) clear. (⇒) ⟨a′, p₀ + w⟩ = c′ for all w ⊥ a; w = 0 gives ⟨a′, p₀⟩ = c′, so ⟨a′, w⟩ = 0 for all w ⊥ a. Take w ≔ a′ − proj_a a′, ⊥ a by `thm-projection-closest-point` (a); then ‖w‖² = ⟨a′, w⟩ − μ⟨a, w⟩ = 0 with μ = ⟨a′, a⟩/‖a‖², so a′ = μa, μ ≠ 0, c′ = μc.
3. **`exm-lines-in-the-plane`** `[Lines of ℝ² Are Its Hyperplanes]`: (a) in ℝ², H_{a,c} = p₀ + ℝ(−a₂, a₁); (b) p + ℝv = H_{a,c} with a = (−v₂, v₁), c = ⟨a, p⟩. *Solution.* (a) ⊇: ⟨a, (−a₂, a₁)⟩ = 0. ⊆: w ≔ x − p₀ has a₁w₁ + a₂w₂ = 0, and w = t(−a₂, a₁) with t ≔ (a₁w₂ − a₂w₁)/‖a‖² (check coordinates using a₂w₂ = −a₁w₁). (b) ⟨a, v⟩ = 0 gives ⊆; (a) and `prp-line-parametrizations` give equality. Aftermath: in ℝ³ a hyperplane is not a line (§10.1 opening).
4. **Quick check.** The line through (1, 3), (4, −1) as an equation. *Solution:* normal (4, 3): 4x + 3y = 13.

**`## Equidistant points` (~600).**
1. **`prp-perpendicular-bisector`**: for p ≠ q, {x : ‖x − p‖ = ‖x − q‖} = H_{q−p, c}, c = (‖q‖² − ‖p‖²)/2; it contains (p + q)/2; and ‖x − p‖ < ‖x − q‖ iff ⟨q − p, x⟩ < c. *Proof* (Idea citing `exm-method-expand-the-square`): square (non-negative sides, `@fd3:prp-ordered-ring-rules` (g)), expand; ‖x − p‖² − ‖x − q‖² = 2⟨q − p, x⟩ − (‖q‖² − ‖p‖²).
2. **Quick check.** Points of ℝ² equidistant from (0, 0) and (2, 4). *Solution:* x₁ + 2x₂ = 5.

**`## Nearest points` (~900).**
1. **`prp-nearest-point-on-line`**: for L = p + ℝv and x, with t₀ ≔ ⟨x − p, v⟩/‖v‖², m ≔ p + t₀v: ‖x − (p + tv)‖² = ‖x − m‖² + (t − t₀)²‖v‖², x − m ⊥ v; m is the unique nearest point of L. *Proof* (terse): `thm-projection-closest-point` applied to x − p and v (Chapter 9 did lines through 0; translate).
2. **`prp-nearest-point-on-hyperplane`** `[Distance to a Hyperplane]`: x* ≔ x − ((⟨a, x⟩ − c)/‖a‖²)a ∈ H_{a,c}; ‖x − y‖² = ‖x − x*‖² + ‖x* − y‖² for y ∈ H_{a,c}; x* is the unique nearest point; distance |⟨a, x⟩ − c|/‖a‖. *Proof.* ⟨a, x*⟩ = c; x − x* is a multiple of a, x* − y ⊥ a; `prp-pythagoras-rn`.
3. **Quick check.** Distance from (1, 2, 3) to x₁ + x₂ + x₃ = 0. *Solution:* 2√3, nearest point (−1, 0, 1).

**`## Spheres and lines; crossing` (~700).**
1. **`def-sphere-rn`**: S(c, r) ≔ {x : ‖x − c‖ = r}, r > 0.
2. **`prp-line-meets-sphere`**: with d the distance from c to L = p + ℝv and m = p + t₀v its nearest point: L ∩ S(c, r) is ∅ if d > r, {m} if d = r, two points p + (t₀ ± √(r² − d²)/‖v‖)v if d < r. *Proof* (Idea: parametrize): ‖p + tv − c‖² = d² + (t − t₀)²‖v‖² = r² iff (t − t₀)² = (r² − d²)/‖v‖²; square roots by `@fd3:prp-cof-square-roots`, exactly two when positive (`@fd3:prp-ordered-ring-rules` (f)). d = r: **tangent**.
3. **`prp-segment-crosses-hyperplane`**: if ⟨a, p⟩ < c < ⟨a, q⟩, [p, q] meets H_{a,c} in exactly one point, t = (c − ⟨a, p⟩)/(⟨a, q⟩ − ⟨a, p⟩). *Proof.* t ↦ ⟨a, (1 − t)p + tq⟩ is ⟨a, p⟩ + t(⟨a, q⟩ − ⟨a, p⟩), slope > 0.

**Exercises.**
- **A1.** For 2x₁ − x₂ + 2x₃ = 6: a normal, the distance from 0, the nearest point to 0. *Answer:* (2, −1, 2); 2; (4/3, −2/3, 4/3).
- **A2.** Are 0 and (3, 0, 1) on the same side of that plane? *Answer:* 0 < 6 < 8: opposite sides; crossing at t = 3/4, point (9/4, 0, 3/4).
- **B1.** Nearest point of (1, 0, 0) + ℝ(1, 1, 1) to (0, 3, 0), and the distance. *Answer:* t₀ = 2/3, m = (5/3, 2/3, 2/3), distance² = 26/3.
- **B2.** Where does ℝ(1, 2, 2) meet S((3, 0, 0), 3)? *Answer:* 9t² − 6t + 9 = 9: t = 0, 2/3; points 0 and (2/3, 4/3, 4/3).
- **B3.** For m ∈ S(c, r), v ≠ 0: m + ℝv meets S(c, r) only at m iff ⟨m − c, v⟩ = 0. *Answer:* ‖m + tv − c‖² = r² + 2t⟨m − c, v⟩ + t²‖v‖² = r² iff t(2⟨m − c, v⟩ + t‖v‖²) = 0; the only root is 0 iff ⟨m − c, v⟩ = 0.
- **B4** (prove or disprove). (a) H_{a,c} ∩ H_{a,c′} = ∅ for c ≠ c′. (b) Any two distinct hyperplanes of ℝ³ meet. (c) For n ≥ 2 the only point equidistant from p ≠ q is the midpoint. (d) ⟨a, p⟩ < c and ⟨a, q⟩ < c ⇒ [p, q] misses H_{a,c}. (e) The distance from 0 to H_{a,c} is |c|. *Answers:* (a) true. (b) false: x₁ = 0, x₁ = 1. (c) false: for (±1, 0), all (0, y). (d) true: (1 − t)⟨a, p⟩ + t⟨a, q⟩ < c. (e) false: a = (2, 0), c = 2 gives 1.
- **C1** (exit check). Three non-collinear points of ℝ² lie on exactly one circle. *Answer:* a centre lies on the bisectors of p, q and of q, r, lines with normals q − p, r − q (`prp-perpendicular-bisector`, `exm-lines-in-the-plane`); these are not multiples (else r is on the line pq), so by §10.1 B2 (b) the bisectors meet in exactly one z; ρ ≔ ‖z − p‖ = ‖z − q‖ = ‖z − r‖ > 0; any circle through the three has centre on both bisectors, so it is S(z, ρ). Stem example: (0, 0), (4, 0), (0, 2): centre (2, 1), radius √5. *Marking scheme* (5): bisector reduction (1); normals not parallel (1); unique intersection (1); circle exists (1); uniqueness (1).

### 5.3 Section 10.3: Convex Sets and Hulls (`03-convex-sets-and-hulls.md`)

**Budget** ≤ 5,000 (~3,400). One fold (λ_{k+1} = 1 in the induction). Three Quick checks.

**Opening (~250).** Analysis moves between points along segments (mean value theorem, connectedness, Cauchy's theorem). **Weird-examples Quick check** before the definition: which of a disc, an annulus 1 ≤ ‖x‖ ≤ 2, a line, two points, ∅, the union of the axes contain the segment between any two of their points? *Solution:* disc yes (below); annulus no ((±3/2, 0), midpoint 0); line yes; two points no; ∅ yes (nothing to check); axes no ((1, 0), (0, 1)).

**`## Convex sets and balls` (~800).**
1. **`def-convex-set-rn`**: C convex if [p, q] ⊆ C for all p, q ∈ C.
2. **`def-ball-rn`**: B(c, r) ≔ {‖x − c‖ < r}, B̄(c, r) ≔ {‖x − c‖ ≤ r}, r > 0. "Open", "closed" are names; AN1 explains them and defines balls for any distance (prose).
3. **`prp-balls-convex`**.
   - **`[Scratch work]`** with table: Givens ‖p − c‖ < r, ‖q − c‖ < r, t ∈ [0, 1]; Goal ‖(1 − t)p + tq − c‖ < r; row 2: write c = (1 − t)c + tc, the vector is (1 − t)(p − c) + t(q − c); gap closed by the triangle inequality and homogeneity.
   - *Proof.* ‖(1 − t)(p − c) + t(q − c)‖ ≤ (1 − t)‖p − c‖ + t‖q − c‖ < (1 − t)r + tr = r (one of the weights is positive; if t = 0 or 1, immediate). Closed ball with ≤.
4. **`exm-method-two-point-test`** `[Method: the two-point test]`. *Template.* Take p, q ∈ C, t ∈ [0, 1]; write the condition for p and q; split the vector or sum for (1 − t)p + tq as (1 − t)(…) + t(…); conclude by the triangle inequality or linearity. *When.* Proving convexity from a definition. *Usual failure.* Checking only t = 1/2 (§10.3 B4 (e)); allowing t outside [0, 1].

**`## Examples and operations` (~700).**
1. **`prp-convex-examples`**: lines, segments, hyperplanes, half-spaces are convex. *Proof* (terse): (1 − t)(p + sv) + t(p + uv) = p + ((1 − t)s + tu)v; `lem-subsegment`; ⟨a, (1 − t)x + ty⟩ = (1 − t)⟨a, x⟩ + t⟨a, y⟩.
2. **`prp-convex-operations`**: (a) any intersection of convex sets is convex (`@fd2:def-family-union-intersection`); (b) b + C and λC are convex; (c) a union of two convex sets need not be ({p} ∪ {q}).
3. **Quick check.** {x₁ ≥ 0, x₂ ≥ 0, x₁ + x₂ ≤ 1} is convex: three half-spaces, (a).

**`## Convex combinations and the hull` (~1,200).**
1. **`def-convex-combination-rn`**: Σλ_ip_i with λ_i ≥ 0, Σλ_i = 1 (k ≥ 1); k = 2 gives [p₁, p₂].
2. **`thm-convex-contains-combinations`**: a convex set contains every convex combination of its points. *Proof* by induction on k (`@fd2:thm-induction`), move "peel off the last point": scratch (≤ 6 lines): convexity speaks about two points, so split one off. If λ_{k+1} ≠ 1, s ≔ 1 − λ_{k+1} > 0 and Σ_{i≤k+1}λ_ip_i = s·Σ_{i≤k}(λ_i/s)p_i + λ_{k+1}p_{k+1}, a point of a segment between two points of C. λ_{k+1} = 1 in the fold.
3. **`def-convex-hull-rn`**: conv S ≔ intersection of all convex sets containing S; the smallest such (pattern of `@fd2:prp-smallest-closed-set`; ℝⁿ is one, so the family is non-empty).
4. **`thm-convex-hull-combinations-rn`** (key proof): conv S = K, the set of convex combinations of finitely many points of S. *Proof.* K ⊆ conv S by 2. K ⊇ S and K is convex: (1 − t)Σλ_ip_i + tΣμ_jq_j is a combination of the joined list with weights (1 − t)λ_i, tμ_j, summing to 1; so conv S ⊆ K.
5. **`exm-triangle-as-hull`**: conv{p₁, p₂, p₃} is the filled triangle. (1, 1) is in the hull of (0, 0), (3, 0), (0, 3) (weights 1/3 each); (2, 2) is not (3λ₂ = 3λ₃ = 2 forces λ₂ + λ₃ = 4/3 > 1).

**`## Star-shaped sets` (~350).**
1. **`def-star-shaped`**: S is star-shaped about c ∈ S if [c, x] ⊆ S for every x ∈ S. A non-empty convex set is star-shaped about each of its points.
2. **`exm-star-not-convex`**: the union A of the axes of ℝ² is star-shaped about 0, not convex; not star-shaped about (1, 0) ((1/2, 1/2) ∈ [(1, 0), (0, 1)]).

**Exercises.**
- **A1.** Convex or not: (a) {y ≥ x²}; (b) {y ≤ x²}; (c) ℤ²; (d) {1 ≤ ‖x‖ ≤ 2} ⊆ ℝ². *Answers:* (a) yes (B1); (b) no: (±1, 1), midpoint (0, 1); (c) no: midpoint (1/2, 0); (d) no: (±3/2, 0).
- **A2.** Is (1, 2) in conv{(0, 0), (3, 0), (0, 3)}? *Answer:* yes, (1/3)(3, 0) + (2/3)(0, 3).
- **B1.** Prove A1 (a). *Answer:* (1 − t)b + td ≥ (1 − t)a² + tc² = ((1 − t)a + tc)² + t(1 − t)(a − c)² ≥ ((1 − t)a + tc)² (identity by expanding; sidecar).
- **B2.** C, D convex ⇒ C + D convex. *Answer:* (1 − t)(x + y) + t(x′ + y′) = ((1 − t)x + tx′) + ((1 − t)y + ty′).
- **B3** (strict convexity; Idea citing `exm-method-equality-case`). For p ≠ q in S(c, r) and 0 < t < 1, ‖(1 − t)p + tq − c‖ < r. *Answer:* ≤ r by the triangle inequality; equality gives, by the equality case with u = (1 − t)(p − c) ≠ 0, t(q − c) = λ(1 − t)(p − c), λ ≥ 0, so q − c = μ(p − c), μ ≥ 0; equal norms force μ = 1, q = p. Aftermath: for the square {max(|x₁|, |x₂|) ≤ 1} the analogue fails (its edge contains [(1, −1), (1, 1)]); AN1 returns to this (prose).
- **B4** (prove or disprove). (a) A union of two convex sets is convex. (b) The complement of a convex subset of ℝ² is convex. (c) conv(S ∪ T) = conv S ∪ conv T. (d) {x : ‖x − p‖ ≤ ‖x − q‖} is convex. (e) A set containing the midpoint of any two of its points is convex. *Answers:* (a) false (`prp-convex-operations` (c)). (b) false: complement of B̄(0, 1), (±2, 0). (c) false: S = {p}, T = {q}. (d) true: a closed half-space (`prp-perpendicular-bisector`; ℝⁿ if p = q). (e) false: ℚ² ⊆ ℝ² contains midpoints of its points, but [(0, 0), (1, 0)] contains (√2/2, 0) ∉ ℚ² (`@fd3:thm-no-rational-square-two`, √2 from `@fd3:prp-cof-square-roots`).
- **C1** (exit check). A non-empty convex C ⊆ ℝ is an interval: with α ≔ inf C (or −∞), β ≔ sup C (or +∞), (α, β) ⊆ C ⊆ [α, β] ∩ ℝ. *Answer:* for α < x < β there are a, b ∈ C with a < x < b (x is neither a lower nor an upper bound; `@fd3:def-complete-ordered-field` for inf and sup), and x ∈ [a, b] ⊆ C; the second inclusion is the definition of inf and sup. *Marking scheme* (4): inf/sup or infinite cases (1); a, b found (1); segment = interval for n = 1 (1); conclusion (1).

### 5.4 Section 10.4: Isometries of ℝⁿ (`04-isometries-of-rn.md`)

**Budget** ≤ 5,000 (~3,300). One fold (t < 0 in `thm-isometry-preserves-segments` (b)). Three Quick checks, one Try-it-first.

**Opening: the hook (~200).** Translations, reflections and turns keep distances. Which other maps do? Must a map keeping all distances be **onto**, or could it squeeze ℝⁿ into part of itself, as x ↦ x + 1 squeezes [0, ∞) into [1, ∞)? This section collects what distances alone force.

**`## Definition and examples` (~900).**
1. **`def-isometry-rn`**: f: ℝⁿ → ℝⁿ with ‖f(x) − f(y)‖ = ‖x − y‖ for all x, y. Not assumed onto.
2. **Quick check** (weird candidates): x ↦ −x (yes); x ↦ 2x (no); on ℝ, x ↦ |x| (no: ±1); (x₁, x₂) ↦ (x₂, x₁) (yes); constant maps (no).
3. **`exm-isometry-examples`**: translations τ_b(x) ≔ x + b; permuting coordinates; changing signs of coordinates (‖·‖² is a sum of squares, unchanged by reordering or signs).
4. **`def-reflection-hyperplane`**: ρ_{a,c}(x) ≔ x − 2((⟨a, x⟩ − c)/‖a‖²)a. Prose: ρ_{a,c}(x) = 2x* − x with x* the nearest point (`prp-nearest-point-on-hyperplane`).
5. **`prp-reflection-properties`**: (a) ρ_{a,c} is an isometry; (b) ρ_{a,c} ∘ ρ_{a,c} = id, so it is a bijection, its own inverse (`@fd2:thm-bijection-iff-inverse`); (c) its fixed points are exactly H_{a,c}; (d) for p ≠ q, the reflection in the bisector of `prp-perpendicular-bisector` exchanges p and q. *Proof.* (a) Idea citing `exm-method-expand-the-square`: w = x − y, μ = ⟨a, w⟩/‖a‖², ‖w − 2μa‖² = ‖w‖² − 4μ⟨a, w⟩ + 4μ²‖a‖² = ‖w‖². (b) ⟨a, ρ(x)⟩ − c = −(⟨a, x⟩ − c). (c) correction term 0 iff ⟨a, x⟩ = c. (d) a = q − p, ⟨a, p⟩ − c = −‖q − p‖²/2, so ρ(p) = p + a = q; ρ(q) = p by (b).

**`## Composites and the origin` (~600).**
1. **`prp-isometry-composition`**: (a) composites of isometries are isometries; (b) isometries are injective; (c) the inverse of a bijective isometry is an isometry.
2. **`prp-isometry-reduce-to-origin`**: g ≔ τ_{−f(0)} ∘ f is an isometry fixing 0 and f = τ_{f(0)} ∘ g (move "reduce to the origin").
3. **`prp-isometry-preserves-inner-product`**: if f(0) = 0, then ‖f(x)‖ = ‖x‖ and ⟨f(x), f(y)⟩ = ⟨x, y⟩. *Proof* (terse): ‖f(x)‖ = ‖f(x) − f(0)‖; `prp-polarization-rn` (b) expresses ⟨x, y⟩ by ‖x‖, ‖y‖, ‖x − y‖. One sentence: from here the linear algebra volumes show f is linear (Looking-ahead box, §10.5).

**`## What distances force` (~1,300).**
1. **`exm-method-distances-only`** `[Method: describe it by distances alone]`. *Template.* Find a description of the objects that mentions only distances between points; apply f; the images satisfy the same description. *When.* Midpoints, segments, spheres, balls, bisectors under isometries; later, anything defined by a metric (AN1). *Usual failure.* Using a description with a parameter or a sum p + tv and claiming f respects it: that is what must be proved.
2. **Try it first:** "Show that an isometry maps the midpoint of [p, q] to the midpoint of [f(p), f(q)]." Folded answer: the midpoint is the only point at distance ‖p − q‖/2 from both ends (`cor-point-pinned-on-segment`), and f keeps all three distances.
3. **`thm-isometry-preserves-segments`** (key proof): (a) f((1 − t)p + tq) = (1 − t)f(p) + tf(q) for t ∈ [0, 1]; so f([p, q]) = [f(p), f(q)] and midpoints go to midpoints. (b) f(p + tv) = f(p) + t(f(p + v) − f(p)) for all t ∈ ℝ; for v ≠ 0, f maps p + ℝv onto the line f(p) + ℝ(f(p + v) − f(p)).
   - **`[Scratch work]`** with table:

     | Givens | Goal |
     |---|---|
     | x = (1 − t)p + tq; f keeps distances | f(x) = (1 − t)f(p) + tf(q) |
     | ‖p − x‖ = t‖p − q‖, ‖x − q‖ = (1 − t)‖p − q‖ (`thm-betweenness`) | f(x) is at distances t‖f(p) − f(q)‖, (1 − t)‖f(p) − f(q)‖ from f(p), f(q) |
     | the same with f applied | `cor-point-pinned-on-segment`: that point is f(p) + t(f(q) − f(p)) |

   - *Proof.* (a) as in the table (p = q trivial); onto [f(p), f(q)] by reading the formula backwards. (b) t ∈ [0, 1]: (a) with q = p + v. t > 1: p + v = (1 − 1/t)p + (1/t)(p + tv), apply (a), solve. t < 0 (fold): p = (1 − s)(p + tv) + s(p + v), s = −t/(1 − t) ∈ (0, 1), apply (a), solve using 1/(1 − s) = 1 − t, s/(1 − s) = −t. Lines: f(p + v) ≠ f(p) by injectivity.
4. **`cor-isometry-convex-image`** (terse, two-point test): f(C) convex for convex C; f(B(c, r)) ⊆ B(f(c), r), f(S(c, r)) ⊆ S(f(c), r). "⊆" cannot yet be "=": that needs onto (thread 1).
5. **Quick check.** f(0, 0) = (1, 1), f(2, 0) = (1, 3): f(1, 0)? f(3, 0)? *Solution:* (1, 2); (1, 1) + 3((1, 2) − (1, 1)) = (1, 4).

**Exercises.**
- **A1.** Isometries of ℝ²? (a) (x, y) ↦ (y + 1, x − 2); (b) (x, 2y); (c) (x, x + y); (d) ((3x − 4y)/5, (4x + 3y)/5); (e) (|x|, y). *Answers:* (a) yes; (b) no, (0, 0), (0, 1) → distance 2; (c) no, (1, 0) → (1, 1), distance √2; (d) yes: the map is additive and ((3u − 4w)² + (4u + 3w)²)/25 = u² + w² (§10.5 identifies it as multiplication by (3 + 4i)/5); (e) no, (±1, 0).
- **A2.** The reflection of ℝ³ in x₁ + x₂ + x₃ = 3 and the image of 0. *Answer:* ρ(x) = x − (2/3)(x₁ + x₂ + x₃ − 3)(1, 1, 1); ρ(0) = (2, 2, 2).
- **B1.** An isometry fixing p ≠ q fixes the whole line through them. *Answer:* `thm-isometry-preserves-segments` (b), v = q − p.
- **B2.** The reflection exchanging (1, 0, 0) and (0, 1, 0). *Answer:* `prp-reflection-properties` (d): a = (−1, 1, 0), c = 0, ρ(x) = (x₂, x₁, x₃).
- **B3** (faded: last step blank in the hint). ρ_{a,c′} ∘ ρ_{a,c} is the translation by 2((c′ − c)/‖a‖²)a. *Hint given:* ⟨a, ρ_{a,c}(x)⟩ = 2c − ⟨a, x⟩; "*name the move, then complete it*". *Answer:* x − 2((⟨a, x⟩ − c)/‖a‖²)a − 2((2c − ⟨a, x⟩ − c′)/‖a‖²)a = x + 2((c′ − c)/‖a‖²)a.
- **B4** (prove or disprove). (a) Isometries map midpoints to midpoints. (b) A map sending every segment onto a segment is an isometry. (c) An isometry of ℝ² fixing three non-collinear points is the identity. (d) The composite of two reflections is a reflection. (e) An isometry of ℝ maps [a, b] onto an interval. *Answers:* (a) true. (b) false: x ↦ 2x. (c) true: if f(z) = w ≠ z, the three fixed points are equidistant from z and w, so lie on one bisector, a line. (d) false: B3 with c ≠ c′ gives a translation without fixed points, while a reflection fixes a hyperplane. (e) true: (a) of the theorem with n = 1.
- **C1** (exit check; thread 1 for n = 1). Every isometry of ℝ is x ↦ x + b or x ↦ −x + b; hence every isometry of ℝ is a bijection. *Answer:* b ≔ f(0), g ≔ f − b fixes 0 and |g(x)| = |x|, so g(x) = ±x (`@fd3:prp-absolute-value-ordered-field`); ε ≔ g(1) ∈ {1, −1}. If g(x) = −εx for some x ≠ 0, then |g(x) − g(1)| = |−εx − ε| = |x + 1| must equal |x − 1|, forcing x = 0 (square both sides: 4x = 0): contradiction. So g(x) = εx, f(x) = εx + b, with inverse y ↦ ε(y − b). *Marking scheme* (5): reduction (1); g(x) = ±x (1); ε (1); mixed sign excluded (1); bijectivity (1).

### 5.5 Section 10.5: Rotations and the Complex Plane (`05-rotations-and-the-complex-plane.md`)

**Budget** ≤ 5,000 (~3,900). Application section (terse scaffolding; no B4; R group). Three Quick checks, one Looking-ahead box.

**Opening (~150).** Chapter 3 proved "multiply the lengths, add the angles". As maps of the plane: multiplying by a unit complex number turns the plane about 0, conjugation reflects it. This section makes that precise with Section 10.4's isometries, collects these maps into a group, and shows that picking one argument per point costs the rule that arguments add.

**`## The plane as ℂ` (~500).**
1. Prose: ℂ = ℝ² as sets (`@def-complex-numbers`); addition is vector addition (`def-vector-operations-rn`); |z − w| = ‖z − w‖ = d(z, w) (`@def-conjugate-modulus`, `def-norm-rn`: the same formula). So an isometry of ℝ² is a map f: ℂ → ℂ with |f(z) − f(w)| = |z − w|.
2. **`lem-complex-plane-inner-product`**: for z = a + bi, w = c + di, z̄w = (ac + bd) + (ad − bc)i; so Re(z̄w) = ⟨z, w⟩ and Im(z̄w) = ad − bc. *Proof.* Multiply out.
3. **Quick check.** z = 1 + 2i, w = 3 − i: ⟨z, w⟩ = 1; z̄w = (1 − 2i)(3 − i) = 1 − 7i. ✓

**`## Rotations and reflections` (~1,300).**
1. **`prp-complex-plane-isometries`**: for a ∈ 𝕋, b ∈ ℂ, f(z) ≔ az + b and g(z) ≔ a z̄ + b are isometries of ℂ and bijections, with inverses z ↦ ā(z − b) and z ↦ a z̄ − a b̄, of the same two forms. *Proof.* |f(z) − f(w)| = |a||z − w| and |g(z) − g(w)| = |a||conj(z − w)| (`@thm-conjugate-properties` (a), (b), (d)); inverses by substitution, ā = a⁻¹ (`@prp-unit-circle` (a)).
2. **`def-rotation-about-point`**: for c ∈ ℂ, u ∈ 𝕋, the **rotation about c by u** is z ↦ c + u(z − c). If u = e^{iθ} (`@prp-polar-form` (a)), it is the rotation by angle θ; the angle is determined only up to 2πℤ (`@prp-polar-form` (b)). Picture in words via `@thm-polar-multiplication` (c): z − c = re^{iφ} goes to re^{i(φ + θ)}.
3. **Quick check.** A1 (d) of Section 10.4 is z ↦ ((3 + 4i)/5)z: (3 + 4i)/5 ∈ 𝕋 and ((3 + 4i)/5)(x + iy) = ((3x − 4y) + (4x + 3y)i)/5.
4. **`[Scratch work]`** (≤ 8 lines): a reflection in the line ℝu (u ∈ 𝕋) should fix u, send iu to −iu; z ↦ z̄ does this for u = 1; turn by ū, conjugate, turn back by u: u·conj(ūz) = u² z̄.
5. **`prp-reflection-in-line-complex`**: for u ∈ 𝕋, the line ℝu through 0 is H_{iu,0}, and ρ_{iu,0}(z) = u² z̄ ≕ σ_u(z). *Proof.* ⟨iu, u⟩ = Re(conj(iu)u) = Re(−i) = 0 (lemma), so ℝu ⊆ H_{iu,0}, equal by `exm-lines-in-the-plane`. ‖iu‖ = 1, ⟨iu, z⟩ = Re(−iūz) = Im(ūz). Write ūz = s + ti; then z = u(s + ti) and ρ(z) = z − 2t·iu = u(s − ti) = u·conj(ūz) = u² z̄.
6. **`thm-two-reflections-rotation`**: for u, v ∈ 𝕋: (a) σ_v ∘ σ_u is the rotation about 0 by (vū)²; with u = e^{iα}, v = e^{iβ}, by angle 2(β − α); (b) every rotation about 0 is a composite of two reflections in lines through 0. *Proof.* (a) v² conj(u² z̄) = v²ū²z (`@thm-conjugate-properties`); polar form by `@thm-polar-multiplication`. (b) for w ∈ 𝕋 choose v with v² = w (`@prp-complex-square-roots`; |v|² = |w| = 1); then σ_v ∘ σ_1 is z ↦ wz.

**`## A group of isometries` (~700).**
1. **`prp-complex-isometry-group`** (key proof): let E be the set of maps z ↦ az + b and z ↦ a z̄ + b (a ∈ 𝕋, b ∈ ℂ). (a) E is a subgroup of the symmetric group S_ℂ (`@def-symmetric-group`), and E⁺ ≔ {z ↦ az + b} is a subgroup of E. (b) Each f ∈ E determines its form: b = f(0), a = f(1) − f(0), and f is of the first kind iff f(i) − f(0) = ai. (c) u ↦ (z ↦ uz) is an injective homomorphism (𝕋, ·) → E⁺ (`@def-group-homomorphism`, `@prp-homomorphism-injective-iff-kernel-trivial`). *Proof.* (a) `@thm-subgroup-test`: E ≠ ∅ (identity); E ⊆ S_ℂ by `prp-complex-plane-isometries`; composites, e.g. (a z̄ + b)∘(a′ z̄ + b′) = aā′z + a b̄′ + b, stay in E with coefficients in 𝕋 (`@prp-unit-circle` (a)), and E⁺ is closed too; inverses by `prp-complex-plane-isometries`. (b) evaluate at 0, 1, i; for the second kind f(i) − f(0) = −ai ≠ ai. (c) uu′ composes to (uu′)z; kernel {1}.
2. The first kind are **direct**, the second **opposite**; well defined by (b).
3. **Looking-ahead box** `[Looking ahead: every isometry]` (≤ 120 words): "Every isometry of the plane belongs to E, and every isometry of ℝⁿ has the form x ↦ Ax + b where the columns of the array A are orthonormal; in particular every isometry is onto. The proof starts from `prp-isometry-preserves-inner-product` and shows linearity; it belongs to *Inner Products and Spectral Theory*, and *Affine and Projective Geometry* lists the plane isometries." (Home: coordinator, §6.)

**`## Arguments` (~800).**
1. **`def-argument-set`** (motivation: `@def-polar-form` says "**an** argument"): for z ≠ 0, arg z ≔ {θ ∈ ℝ : z = |z|e^{iθ}}. By `@prp-polar-form`, arg z = θ₀ + 2πℤ for any θ₀ ∈ arg z.
2. **Quick check.** arg i = π/2 + 2πℤ; arg(−1) = π + 2πℤ; arg(1 + i) = π/4 + 2πℤ (`@exm-special-angles`).
3. **`prp-argument-of-product`**: for z, w ≠ 0, arg(zw) = arg z + arg w ≔ {θ + φ}; arg z̄ = arg(1/z) = −arg z. *Proof.* ⊇ by `@thm-polar-multiplication` (c). ⊆: for ψ ∈ arg(zw) and θ ∈ arg z, w = zw/z = |w|e^{i(ψ − θ)} (`@thm-polar-multiplication` (a), (b)), so ψ − θ ∈ arg w. Conjugates: conj(e^{iθ}) = e^{−iθ}; 1/z = z̄/|z|².
4. **`def-principal-argument`** (motivation: one number per z is wanted): Arg z ≔ the unique element of arg z in (−π, π]. Existence and uniqueness: for θ ∈ arg z, put x ≔ (θ + π)/(2π); ℝ is Archimedean (`@fd3:thm-cof-complete-archimedean`), so by `@fd3:prp-integer-part-ordered-field` there is one m ∈ ℤ with m ≤ −x < m + 1; k ≔ −m − 1 is the only integer with k < x ≤ k + 1, that is with θ − 2πk ∈ (−π, π]. Two elements of arg z in (−π, π] differ by 2πj with |2πj| < 2π, so j = 0.
5. **`exm-principal-argument-not-additive`**: Arg(−1) = π, Arg i = π/2, Arg((−1)i) = Arg(−i) = −π/2 ≠ 3π/2. And two nearby points: Arg(−1 + i) = 3π/4, Arg(−1 − i) = −3π/4 (e^{i3π/4} = i e^{iπ/4} = (−1 + i)/√2). No choice of one argument per point both keeps "arguments add" and avoids such a jump across the negative real axis: prose pointer to the principal logarithm (*Integration, Series, and Function Spaces*) and branches (*Complex Analysis*).

**`## Angles in the plane` (~450).**
1. **`thm-angle-in-the-plane`**: for z, w ∈ ℂ∖{0} and θ ∈ arg(z̄w) = arg w − arg z: (a) cos∠(z, w) = cos θ and Im(z̄w) = |z||w| sin θ; (b) for every rotation f(ζ) = uζ + b, arg(conj(f(z) − f(0)) (f(w) − f(0))) = arg(z̄w); for σ_v it is −arg(z̄w). *Proof.* (a) |z̄w| = |z||w|, so z̄w = |z||w|e^{iθ}; real and imaginary parts, `lem-complex-plane-inner-product`, `def-angle-cosine-rn`. (b) conj(uz)(uw) = |u|²z̄w = z̄w; conj(v²z̄)(v²w̄) = z w̄ = conj(z̄w), and `prp-argument-of-product`.
2. Aftermath: θ is the **oriented angle from z to w** (Chapter 9's promise paid); rotations keep it, reflections reverse it.

**Exercises.**
- **A1.** The rotation about 1 + i by i; the images of 0 and 2. *Answer:* z ↦ (1 + i) + i(z − 1 − i); 0 ↦ 2, 2 ↦ 2 + 2i (both at distance √2 from 1 + i, as before).
- **A2.** Arg of −√3 + i, −2, 1 − i, and of the products (−2)(1 − i), (−√3 + i)(−2). *Answer:* 5π/6 (−√3 + i = 2e^{iπ}e^{−iπ/6}, `@exm-special-angles`); π; −π/4; Arg(−2 + 2i) = 3π/4 = π + (−π/4); Arg(2√3 − 2i) = −π/6, while 5π/6 + π = 11π/6 differs from it by 2π.
- **B1.** The reflection in the line c + ℝu (u ∈ 𝕋) is z ↦ c + u² conj(z − c). Find the reflection in the vertical line through 1. *Answer:* that line is H_{iu,⟨iu,c⟩}, and from `def-reflection-hyperplane`, ρ_{a,⟨a,c⟩}(z) = c + ρ_{a,0}(z − c); then `prp-reflection-in-line-complex`. With c = 1, u = i: z ↦ 1 − conj(z − 1) = 2 − z̄ (0 ↦ 2 ✓).
- **B2.** The composite of the rotations about c by u and about c′ by u′ is a rotation about some point by uu′ if uu′ ≠ 1, and the translation by (1 − u′)(c′ − c) if uu′ = 1. Two half-turns give the translation by 2(c′ − c). *Answer:* the composite is z ↦ uu′z + K, K = c′ + u′(c − c′) − uu′c. If uu′ ≠ 1, d ≔ K/(1 − uu′) satisfies K = d(1 − uu′), so the map is z ↦ d + uu′(z − d). If uu′ = 1, K = c′ + u′c − u′c′ − c = (1 − u′)(c′ − c). u = u′ = −1: 2(c′ − c).
- **B3.** The oriented angle from 1 + i to i, and from i to 1 + i; check cos∠ directly. *Answer:* conj(1 + i)·i = 1 + i = √2e^{iπ/4}: π/4 (mod 2π); the reverse is −π/4 by `prp-argument-of-product`; ⟨(1, 1), (0, 1)⟩/√2 = 1/√2 = cos(π/4) (`@exm-special-angles`).
- **C1** (exit check). Let g(z) = a z̄ + b, a ∈ 𝕋. (a) g has a fixed point iff a b̄ + b = 0. (b) If g(c) = c, then g is the reflection in c + ℝv for any v ∈ 𝕋 with v² = a. (c) Does z ↦ z̄ + 1 have one? *Answer:* (a) if g(c) = c then b = c − a c̄, so a b̄ = a c̄ − c (aā = 1) and a b̄ + b = 0; conversely g(b/2) = a b̄/2 + b = b/2. (b) b = c − a c̄ gives g(z) = c + a conj(z − c); v exists by `@prp-complex-square-roots` (|v|² = 1); B1. (c) no: a b̄ + b = 2 (a glide reflection, named only). *Marking scheme* (5): each direction of (a) (1 + 1); rewriting g about c (1); v ∈ 𝕋 (1); (c) (1).
- **R1.** Let n ≥ 1, ω ≔ e^{2πi/n}. The 2n maps z ↦ ω^k z and z ↦ ω^k z̄ (0 ≤ k < n) are distinct, map μ_n onto μ_n, and form a subgroup of E. *Answer:* (ω^kζ)^n = 1; ζ̄ = ζ⁻¹ ∈ μ_n (μ_n ⊆ 𝕋, `@prp-unit-circle` (a)); onto, since the inverses ω^{−k}z and ω^k z̄ are of the same forms; distinct by `prp-complex-isometry-group` (b) and `@thm-complex-nth-roots` (c); closure: ω^k conj(ω^l z̄) = ω^{k−l}z (ω̄ = ω⁻¹), and the other products likewise; subgroup test. (Prose: the symmetries of the regular n-gon, studied in *Groups*.)
- **R2.** Arg z̄ = −Arg z iff z is not a negative real. *Answer:* −Arg z ∈ arg z̄ (`prp-argument-of-product`) and lies in [−π, π); it lies in (−π, π] iff Arg z ≠ π, iff z ≠ −|z|, i.e. z is not a negative real.

---

## 6. Pointers and promises (coordinator; S1 touches no src, config, ledger or registry)

- **Registry:** F4.9 title "Lines, Convexity, and Isometries"; plan-edges F4.9 `s: [F4.8, F4.1]`, `see: [F5.3]` (or `s`, coordinator's call); F4.10 → F4.9 (proposal §4.1; CA.1, AN1.10, apostol-ma follow). chapter-constraints: F4.9 rule rewritten (no classification; only `prp-isometry-preserves-inner-product`, rest in the Looking-ahead box), F4.10's rule folded in minus "classify". Promise row: classification to LA3 (plane list GEO); coordinator fixes the home.
- **Downstream:** AN2 ch07 cites `@fd4:def-principal-argument` instead of redefining Arg; AM ch05 cites `@fd4:def-star-shaped`; AN1 (metric spaces, former F4.11) cites `@fd4:def-ball-rn` and picks up thread 2.
- **Chapter 9 blueprint:** its §05 C3 is the (⇐) half of `thm-betweenness` (replace or point forward); its "F4.10 proves cos∠ = cos θ" → `thm-angle-in-the-plane`.

## 7. Notes for S3

Sidecars: §10.1 B2; §10.3 B1; §10.5 A1, A2, B2, `lem-complex-plane-inner-product`, `prp-reflection-in-line-complex`, R1 for n = 4, 6. Ledger lines for each (T_k) use in §10.5, as Chapter 3 does.

## 8. S2a: claims to verify

1. Chapter 9 labels (§4) against the frozen F4.8 blueprint or src, with the content used: `thm-triangle-inequality-rn` (a) equality case "u = 0 or w = cu, c ≥ 0"; `thm-projection-closest-point` (a), (b); `prp-polarization-rn` (b); `def-angle-cosine-rn`; `prp-norm-basic-rn` (b).
2. Chapter 9 §05 C3 duplicate (§6).
3. fd3 labels and item letters after the fd3 re-cut (§4 list; `prp-integer-part-ordered-field` with the ℤ ⊆ ℝ identification).
4. fd2 labels after the fd2 re-cut (all exist at HEAD 2026-10-26).
5. Same-book labels after the structural move, with the item letters cited (Chapter 3, Chapter 5).
6. Chapter 1 (F4.6), once blueprinted: cite re-indexing or completing the square by label?
7. Label uniqueness re-grep at S3, including new src of Chapters 1, 8, 9.
8. Hours after S3 by `check_structure.py --words`; if over 18 / 22, trim `prp-segment-crosses-hyperplane` or R1 first.
