<!-- hand-written -->
# Blueprint: Ch10 (F4.9) Lines, Hyperplanes, and Convex Sets, merged *Preliminaries for Analysis and Algebra*

**Frozen after S2 (2026-10-26).** Next: S2a (§8), S3. Supersedes `f4-9.md`. S2 round 1 cut the S1 plan to three sections (replies at the end); the S1 plans of the dropped Sections 10.4 (isometries of ℝⁿ) and 10.5 (rotations, the group E, arguments, oriented angle) stay in git history (commit `a347ec8`, this file) for the blueprints that receive them (§6).

**Authority.** The author's answers (2026-10-26) to `fd4/authoring/design/merge-proposal.md`: fd4 kept, fd5 retired, F5.x ids kept; title *Preliminaries for Analysis and Algebra*; F4.11 to AN1; Q4 **(b)**, book cut to about 257 / 326 h. Option (b) as written in proposal §3.5 item 2: "F4.9 的等距分類（§04–§06）移到 GEO 或 LA3，F4.9 只留直線、超平面、最近點與凸集：約 −14／−20。代價：F4.10 吸收的旋轉內容要另找地方（CA.1 開頭）". **This blueprint follows that text literally** (S2 ruling, reply 1): Ch10 keeps lines, segments, hyperplanes, nearest points and convex sets; all isometry material, and F4.10's rotations, arguments and oriented angle, leave the book (§6). F4.10's id retires into F4.9 (proposal §3.4) with no content kept here. Earlier direction: moderate difficulty, proof methods in practice.

**Directory.** `fd4/src/ch10-lines-hyperplanes-convex-sets/` (new slug, replacing proposal §3.3's `ch10-lines-convexity-isometries/`; coordinator records it, §6). Prose pointers: "Section 10.k" in the chapter; "Chapter 1" (F4.6), "Chapter 3" (F4.1), "Chapter 6" (F5.4), "Chapter 9" (F4.8) as same-book pointers; other books by title. Sidecars `fd4/verify/ch10/`, ledger `fd4/authoring/ledger/ch10.yaml`.

**Title.** `# Lines, Hyperplanes, and Convex Sets` (registry title updated by the coordinator, §6).

**Level reference** (coverage only): Lang *Basic Mathematics* ch. 6, 10; Apostol *Calculus* I ch. 13. Every example, item and answer is the book's own; nothing from `~/book`.

**Purpose.** Give analysis the geometry of ℝⁿ it cites (lines, segments, hyperplanes, distances to them, spheres, balls, convex sets and hulls), and say "between" with distances alone, the form that later carries over to metric spaces.

**Binding rules.**
1. **No linear algebra.** No span, basis, dimension, matrix, determinant.
2. **No trigonometry.** No cos, sin, π, angles; no limits, no continuity.
3. **No re-proof.** Chapter 9 owns inner product, norm, Cauchy–Schwarz, the triangle inequality **with its equality case**, Pythagoras, polarization, projection with the closest-point theorem, the coordinate bounds, and ℝ² = ℂ (`prp-plane-is-complex-plane`); Chapter 1 owns the finite-sum rules. Each is recalled in a clause and cited.
4. **No topology.** "Open ball", "closed ball" are names (§10.3); one prose sentence points to *Real Numbers, Metric Spaces, and Derivatives* (AN1), which now also holds the metrics-and-norms material (former F4.11).
5. **House manner** (STYLE §1, §2 item 6, §12.5, §12.13.4, §12.14): motivation first, scratch work apart from proofs, method boxes (Template / When to use it / The usual failure, ≤ 130 words each), prose Givens/Goal tables, one Prove-or-disprove B item per method section (verdict first in the answer); at least one warning and one non-example per section (named in each section plan); moderate difficulty; no footnotes, jokes, history or first person. Quick checks about one per 800–1,000 words.
6. **Fewer C items.** One C item per section (the exit check, with marking scheme).

---

## 1. Devices as applied

- **Method boxes (3)**, `::: {#exm-method-<slug>}` titled `[Method: …]`, linked from Named moves: `exm-method-parametrize`, `exm-method-equality-case` (§10.1), `exm-method-two-point-test` (§10.3). **Reused:** Chapter 9's `exm-method-expand-the-square`, Idea level in `prp-perpendicular-bisector`.
- **Non-box move:** "Peel off the last point" (§10.3).
- **Scratch work** at first appearances, with Givens/Goal table where marked: `exm-two-lines-in-space`, `thm-betweenness` (table), `prp-balls-convex` (table).
- **Fading.** Parametrize: full §10.1, Idea `prp-line-meets-sphere`. Equality case: full §10.1, Idea §10.3 B3. Two-point test: full §10.3 (`prp-balls-convex`), Idea §10.3 B2, terse in the alternative route of R2.
- **Prove or disprove:** B4 in §§10.1–10.3. **Try it first:** before `thm-convex-hull-combinations-rn`. **Motivation first:** `def-line-rn`, `def-hyperplane-rn`, `def-convex-set-rn`.
- **Warnings:** §10.1 "Equal distances do not make a midpoint"; §10.2 "A hyperplane has many normal vectors, and a = 0 gives none"; §10.3 "Midpoints are not enough" (ℚ²).
- **Threads** (index list): (1) *betweenness by distances*, §10.1 (`thm-betweenness`) → its failure for other distances (§10.3 B3 aftermath) → AN1 (metric spaces) and GEO (distance-preserving maps keep segments), prose; (2) *convex and star-shaped sets* → AN2.3, CA, AM (prose).

## 2. Section map, budgets, hours

| § | File | Budget | Expected |
|---|---|---|---|
| 10.1 | `01-lines-and-segments.md` | ≤ 5,000 | ~3,600 |
| 10.2 | `02-hyperplanes-and-nearest-points.md` | ≤ 5,000 | ~3,400 |
| 10.3 | `03-convex-sets-and-hulls.md` | ≤ 5,000 | ~3,600 |

Expected main line ~10,600 words; folds ~300. **Time** (index): "about 10 hours on the core track and about 20 hours for everything", recomputed with `check_structure.py --words` after S3.

**Derivation** (STYLE §2 item 4, `research-reader.md` B1; not from the proposal's estimates). Reading at 15 min per 400 words: core 10,600 words ≈ 6.6 h, full 10,900 ≈ 6.8 h. Exercises at 20 min (A), 35 min (B), 40 min (C), 20 min (R): core = 6 A + 3 B + 3 C = 345 min ≈ 5.8 h; full = 6 A + 12 B + 3 C + 3 R = 720 min = 12 h. Unrounded **12.4 / 18.8 h**, rounded to the nearest 5 as STYLE requires: **10 / 20**. Book total: proposal row 10 was 32 / 45 with F4.10 absorbed; option (b) removes 14 / 20 and the C-item cut, leaving at most 18 / 22 for this chapter in the 257 / 326 total. At 12.4 / 18.8 the chapter sits about 6 / 3 h under that allowance, so the book stays within 257 / 326 (about 251 / 323 by this chapter's change alone).

## 3. Labels

All new; grepped 2026-10-26 against `foundations/fd*/src`, `linear-algebra/src`, `linear-algebra-split`, `analysis-series`: no collision in any src. Blueprint overlaps resolved as pointers (§6): `def-star-shaped` (am), `def-ball-rn` (f4-11). Slug `convex-sets-and-hulls` avoids LA's `exr-convex-sets-*`.

- **10.1:** `def-line-rn`, `prp-line-parametrizations`, `prp-line-through-two-points`, `def-collinear`, `exm-two-lines-in-space`, `exm-method-parametrize`, `def-segment-rn`, `lem-subsegment`, `thm-betweenness`, `exm-method-equality-case`, `cor-point-pinned-on-segment`; `exr-lines-and-segments-a1`, `-a2`, `-b1`…`-b4`, `-c1`.
- **10.2:** `def-hyperplane-rn`, `prp-hyperplane-normals`, `exm-lines-in-the-plane`, `prp-perpendicular-bisector`, `prp-nearest-point-on-line`, `prp-nearest-point-on-hyperplane`, `def-sphere-rn`, `prp-line-meets-sphere`, `prp-segment-crosses-hyperplane`; `exr-hyperplanes-and-nearest-points-a1`, `-a2`, `-b1`…`-b4`, `-c1`.
- **10.3:** `def-convex-set-rn`, `def-ball-rn`, `exm-method-two-point-test`, `prp-balls-convex`, `prp-convex-examples`, `prp-convex-operations`, `def-convex-combination-rn`, `thm-convex-contains-combinations`, `def-convex-hull-rn`, `thm-convex-hull-combinations-rn`, `exm-triangle-as-hull`, `def-star-shaped`, `exm-star-not-convex`; `exr-convex-sets-and-hulls-a1`, `-a2`, `-b1`…`-b4`, `-c1`, `-r1`…`-r3`.

**Key proofs** (STYLE §11.2; comprehension parts in §10.1 A2 (b), §10.3 A2 (b)): `thm-betweenness`, `thm-convex-hull-combinations-rn`.

## 4. Allowed prerequisites (every label cited)

- **fd2** (exist at HEAD, grepped): `@fd2:def-family-union-intersection`, `@fd2:prp-smallest-closed-set` (pattern), `@fd2:thm-induction`.
- **fd3** (grepped in the working tree 2026-10-26 while fd3 is being re-cut; item letters re-checked at S2a): `@fd3:prp-ordered-ring-rules` ((b) adding, (e) squares positive, (f) no zero divisors, (g) 0 ≤ a, b: a < b ⇔ a² < b², (i) total order), `@fd3:prp-ordered-field-halves` ((d) products of comparisons), `@fd3:prp-absolute-value-ordered-field` ((d) |x| ≤ r ⇔ −r ≤ x ≤ r), `@fd3:prp-cof-square-roots` with `@fd3:thm-reals-complete-ordered-field`, `@fd3:def-complete-ordered-field` (§10.3 C1), `@fd3:thm-no-rational-square-two` (§10.3 warning).
- **Same book, Chapter 1 (F4.6; `merged-ch01-f46.md`, S1, labels moved or new there):** `@lem-ring-finite-sums` (b) (constants through sums), `@prp-sum-reindex` (b) (splitting), both in `thm-convex-hull-combinations-rn`. Square roots stay with `@fd3:prp-cof-square-roots`; completing a square is not needed (`prp-line-meets-sphere` goes through the projection formula).
- **Same book, Chapter 3 (F4.1; now `fd4/src/ch01-complex-numbers/`, grepped):** `@thm-conjugate-properties` (d), `@prp-unit-circle` (a); R3 only.
- **Same book, Chapter 6 (F5.4; now `fd5/src/ch04-formal-polynomials/04-evaluation-and-substitution.md`, grepped):** `@thm-evaluation-respects-operations`; R2 only.
- **Same book, Chapter 9 (F4.8; labels from the frozen `merged-ch09-f48.md`, which supersedes `f4-8.md`; checked at S2 with the content used):** `def-vector-operations-rn`, `def-norm-rn`, `prp-norm-basic-rn` ((b) ‖cx‖ = |c|‖x‖), `def-distance-rn`, `exm-method-expand-the-square`, `prp-pythagoras-rn`, `thm-triangle-inequality-rn` ((a) with equality iff x = 0 or y = cx, c ≥ 0), `def-projection-rn`, `thm-projection-closest-point` ((a), (b)), `prp-norm-coordinate-bounds` ((a), (b); R1), `prp-plane-is-complex-plane` ((c); R3).
- **Never:** an1/an2/ca/am, la*, geo; later chapters. Prose pointers by title only.

**Notation** (`NOTATION.md` rows, coordinator at S3; macros `\inner`, `\norm`, `\abs` exist):
- p + ℝv, the line (`def-line-rn`); [p, q] the segment (`def-segment-rn`), **clash** with intervals: for n = 1 and p ≤ q it is the interval [p, q], for p > q the interval [q, p]; written only for declared points of ℝⁿ.
- H_{a,c} = {x : ⟨a, x⟩ = c}, a ≠ 0 (`def-hyperplane-rn`); S(c, r) sphere; B(c, r), B̄(c, r) balls (amend the metric-space row: Euclidean case first here, general case AN1); `\operatorname{conv} S`.

---

## 5. Per-section plans

### 5.0 `index.md`

- **Story** (~130 words): what the distance alone determines (lines, segments, hyperplanes, spheres, balls); "between" is a statement about distances (`thm-betweenness`); one linear equation cuts out a hyperplane, and distances to it have a formula; convex sets are those closed under segments, and the hull of a set is the set of its convex combinations. Analysis uses all of these from its first chapters.
- **What you need.** Chapter 9; Chapter 1, Section 1.1 (finite sums); for the review items only, Chapter 3, Sections 3.2 and 3.5, and Chapter 6, Section 6.4; *Number Systems* and *Sets and Functions* as in §4.
- **Borrowed results.** Box **No new borrowed facts.**: the chapter uses no cosine, sine or π.
- **Time** as §2. **Roadmap**: one bullet per section, naming its main result. **Named moves**, **Threads**: §1.

### 5.1 Section 10.1: Lines and Segments (`01-lines-and-segments.md`)

**Budget** ≤ 5,000 (~3,600). One fold (p = q in `cor-point-pinned-on-segment`). Three Quick checks, one notation remark. **Warning:** "Equal distances do not make a midpoint" (`## Between by distances` item 6). **Non-example:** the Quick check after `lem-subsegment` ((2, 0, 1) is not on the segment), and the skew pair in `exm-two-lines-in-space`.

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
3. **`lem-subsegment`**: x, y ∈ [p, q] ⇒ [x, y] ⊆ [p, q]. *Proof.* x = p + s(q − p), y = p + u(q − p); (1 − t)x + ty = p + ((1 − t)s + tu)(q − p) with 0 ≤ (1 − t)s + tu ≤ (1 − t)·1 + t·1 = 1: products of comparisons of non-negative numbers by `@fd3:prp-ordered-field-halves` (d), sums by `@fd3:prp-ordered-ring-rules` (b).
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
   - Aftermath: the right side mentions only distances. That is the form which survives when ℝⁿ is replaced by a set with a distance (*Real Numbers, Metric Spaces, and Derivatives*), and it is why distance-preserving maps keep segments (*Affine and Projective Geometry*); both prose, by title (thread 1).
3. **`exm-method-equality-case`** `[Method: use the equality case]`. *Template.* A known inequality A ≤ B holds with A = B. Recall its exact equality condition (usually: vectors are non-negative multiples of each other), write it with a named multiplier, solve. *When.* A sum of distances equals a distance; Cauchy–Schwarz is sharp; "extreme case" questions. *Usual failure.* Dropping the sign (c ≥ 0 separates [p, q] from the rest of the line) or the case u = 0.
4. **`cor-point-pinned-on-segment`** `[A Point Is Pinned by Its Distances to the Ends]`: if s, r ≥ 0 and s + r = ‖p − q‖, exactly one x has ‖p − x‖ = s, ‖x − q‖ = r; for p ≠ q it is p + (s/‖p − q‖)(q − p). *Proof.* That point works (moreover clause, t = s/‖p − q‖). Any such x lies on [p, q] by the theorem, x = (1 − t′)p + t′q, and s = t′‖p − q‖ fixes t′, hence x. p = q in the fold.
5. **Quick check.** The midpoint is the only point at distance ‖p − q‖/2 from both ends. *Solution:* s = r = ‖p − q‖/2.
6. **Warning** `**Equal distances do not make a midpoint.**` p = (−1, 0), q = (1, 0), x = (0, 1): ‖p − x‖ = ‖x − q‖, x ∉ [p, q]. Section 10.2 finds all such x.

**Exercises.**
- **A1.** (a) Parametrize the line through (1, −1, 2) and (3, 0, 0); is (5, 1, −2) on it? (b) The midpoint of the segment between them. *Answers:* (a) (1, −1, 2) + ℝ(2, 1, −2); yes, t = 2. (b) (2, −1/2, 1).
- **A2.** (a) Show (1, 2), (3, 5), (7, 11) are collinear and find which lies between the others. (b) *(Proof comprehension, key proof `thm-betweenness`.)* In the (⇐) direction, where is c ≥ 0 used? Take p = 0, q = (1, 0), x = (2, 0): which hypothesis of the theorem fails, and what does the equality case give? *Answer:* (a) (6, 9) = 3(2, 3): parameters 0, 1, 3 on (1, 2) + ℝ(2, 3); (3, 5) = (1, 2) + (1/3)((7, 11) − (1, 2)), so (3, 5) is between. (b) c ≥ 0 makes 1 + c > 0, so t = 1/(1 + c) is defined and lies in (0, 1]. For x = (2, 0): ‖p − x‖ + ‖x − q‖ = 3 ≠ 1 = ‖p − q‖; with u = x − p = (2, 0), w = q − x = (−1, 0) = −½u, the multiplier is negative, so the equality case does not apply.
- **B1.** For v ≠ 0 and a < b: p + tv ∈ [p + av, p + bv] iff a ≤ t ≤ b. *Answer:* (⇐) s ≔ (t − a)/(b − a) ∈ [0, 1] gives (1 − s)(p + av) + s(p + bv) = p + tv. (⇒) p + tv = p + ((1 − s)a + sb)v, s ∈ [0, 1]; parameters are unique, so t = a + s(b − a) ∈ [a, b].
- **B2.** In ℝ², v, v′ ≠ 0. (a) v′ is a multiple of v iff v₁v′₂ − v₂v′₁ = 0. (b) If not, p + ℝv and p′ + ℝv′ meet in exactly one point. *Answer:* (a) (⇒) substitute. (⇐) if v₁ ≠ 0, λ ≔ v′₁/v₁ gives λv₂ = v₁v′₂/v₁ = v′₂; if v₁ = 0 then v₂ ≠ 0 and λ ≔ v′₂/v₂ works. (b) With d ≔ p′ − p, p + sv = p′ + tv′ is sv₁ − tv′₁ = d₁, sv₂ − tv′₂ = d₂; D ≔ v₁v′₂ − v₂v′₁ ≠ 0; eliminating, sD = d₁v′₂ − d₂v′₁, tD = d₁v₂ − d₂v₁; so at most one solution, and substitution shows it is one. (Sidecar.)
- **B3.** Show ℝ(1, 0, 0) and (0, 1, 0) + ℝ(0, 0, 1) are skew. *Answer:* (s, 0, 0) = (0, 1, t) fails in the second coordinate; (1, 0, 0) = λ(0, 0, 1) fails in the first.
- **B4** (prove or disprove). (a) ‖p − x‖ = ‖x − q‖ = ‖p − q‖/2 ⇒ x is the midpoint. (b) ‖p − x‖ = ‖x − q‖ ⇒ x ∈ [p, q]. (c) Any three points of ℝ² are collinear. (d) p + ℝv = p + ℝw ⇒ v = w. (e) Two lines with two distinct common points are equal. *Answers:* (a) true (Quick check). (b) false (the warning). (c) false: (0, 0), (1, 0), (0, 1). (d) false: w = 2v. (e) true: `prp-line-through-two-points`.
- **C1** (exit check). Of three distinct collinear points, exactly one lies between the other two. *Answer:* one parametrization p + t_iv, distinct t_i, relabel t₁ < t₂ < t₃; by B1 the middle one is between the others; if p + t₁v ∈ [p + t₂v, p + t₃v], B1 gives t₂ ≤ t₁, contradiction; likewise t₃. *Marking scheme* (5): common parametrization with distinct parameters (1); ordering (1); existence (1); uniqueness of parameters used (1); the two exclusions (1).

### 5.2 Section 10.2: Hyperplanes and Nearest Points (`02-hyperplanes-and-nearest-points.md`)

**Budget** ≤ 5,000 (~3,400). Three Quick checks. Uses Chapter 9's expand-the-square at Idea level; counts as a method section for the B4 rule (the move in a new setting). **Warning:** "A hyperplane has many normal vectors, and a = 0 gives none" (after `prp-hyperplane-normals`). **Non-example:** in ℝ³ a hyperplane is not a line (aftermath of `exm-lines-in-the-plane`, using the §10.1 opening).

**Opening (~80).** One linear equation cuts out a hyperplane; distances to it have a formula, and expanding a square linearizes distance conditions.

**`## Hyperplanes` (~1,100).**
1. **`def-hyperplane-rn`**: for a ≠ 0, c ∈ ℝ, H_{a,c} ≔ {x : ⟨a, x⟩ = c}; a is a **normal vector**; {⟨a, x⟩ ≤ c}, {≥ c} closed half-spaces, < and > open half-spaces. Sentence: p₀ ≔ (c/‖a‖²)a ∈ H_{a,c}, and x ∈ H_{a,c} iff x − p₀ ⊥ a.
2. **`prp-hyperplane-normals`**: H_{a,c} = H_{a′,c′} iff (a′, c′) = (λa, λc), λ ≠ 0. *Proof.* (⇐) clear. (⇒) ⟨a′, p₀ + w⟩ = c′ for all w ⊥ a; w = 0 gives ⟨a′, p₀⟩ = c′, so ⟨a′, w⟩ = 0 for all w ⊥ a. Take w ≔ a′ − proj_a a′, ⊥ a by `thm-projection-closest-point` (a); then ‖w‖² = ⟨a′, w⟩ − μ⟨a, w⟩ = 0 with μ = ⟨a′, a⟩/‖a‖², so a′ = μa, μ ≠ 0, c′ = μc.
3. **Warning** `**A hyperplane has many normal vectors, and a = 0 gives none.**` H_{(1,1),1} = H_{(2,2),2} = H_{(−1,−1),−1}: "the normal" means "a normal", fixed only up to a non-zero factor (`prp-hyperplane-normals`); a formula using a normal (distance, nearest point, below) must give the same answer for λa, λc, and it does. For a = 0, {x : ⟨0, x⟩ = c} is ∅ (c ≠ 0) or ℝⁿ (c = 0), neither a hyperplane; this is why the definition demands a ≠ 0.
4. **`exm-lines-in-the-plane`** `[Lines of ℝ² Are Its Hyperplanes]`: (a) in ℝ², H_{a,c} = p₀ + ℝ(−a₂, a₁); (b) p + ℝv = H_{a,c} with a = (−v₂, v₁), c = ⟨a, p⟩. *Solution.* (a) ⊇: ⟨a, (−a₂, a₁)⟩ = 0. ⊆: w ≔ x − p₀ has a₁w₁ + a₂w₂ = 0, and w = t(−a₂, a₁) with t ≔ (a₁w₂ − a₂w₁)/‖a‖² (check coordinates using a₂w₂ = −a₁w₁). (b) ⟨a, v⟩ = 0 gives ⊆; (a) and `prp-line-parametrizations` give equality. Aftermath: in ℝ³ a hyperplane is not a line (§10.1 opening).
5. **Quick check.** The line through (1, 3), (4, −1) as an equation. *Solution:* normal (4, 3): 4x + 3y = 13.

**`## Equidistant points` (~600).**
1. Lead (one sentence, prose recall, not a reason): Chapter 9, Section 9.4, Exercise B3 found the equation of the equidistant set; here it is named as a hyperplane and the two sides are read off.
2. **`prp-perpendicular-bisector`**: for p ≠ q, {x : ‖x − p‖ = ‖x − q‖} = H_{q−p, c}, c = (‖q‖² − ‖p‖²)/2; it contains (p + q)/2; and ‖x − p‖ < ‖x − q‖ iff ⟨q − p, x⟩ < c. *Idea* (one line, citing `exm-method-expand-the-square`): compare squares instead of norms; the squares of the two norms differ by a linear expression in x. *Proof.* For non-negative a, b: a < b iff a² < b² (`@fd3:prp-ordered-ring-rules` (g)), and by totality (item (i)) also a = b iff a² = b². Expanding, ‖x − p‖² − ‖x − q‖² = 2⟨q − p, x⟩ − (‖q‖² − ‖p‖²); so equality of the norms is ⟨q − p, x⟩ = c, a hyperplane since q − p ≠ 0, and the strict inequality is the open half-space ⟨q − p, x⟩ < c. The midpoint: ⟨q − p, (p + q)/2⟩ = (‖q‖² − ‖p‖²)/2.
3. **Quick check.** Points of ℝ² equidistant from (0, 0) and (2, 4). *Solution:* x₁ + 2x₂ = 5.

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
- **C1** (exit check). Three non-collinear points of ℝ² lie on exactly one circle. *Answer:* a centre lies on the bisectors of p, q and of q, r, hyperplanes with normals q − p, r − q (`prp-perpendicular-bisector`). By `exm-lines-in-the-plane` (a) they are lines whose directions come from the normals by (a₁, a₂) ↦ (−a₂, a₁), and two such directions are multiples of each other iff the normals are. The normals are not multiples (if r − q = λ(q − p), r lies on the line through p and q), so Section 10.1's B2 (b) applies: the bisectors meet in exactly one z; ρ ≔ ‖z − p‖ = ‖z − q‖ = ‖z − r‖ > 0; any circle through the three has centre on both bisectors, so it is S(z, ρ). Stem example: (0, 0), (4, 0), (0, 2): centre (2, 1), radius √5. *Marking scheme* (5): bisector reduction (1); normals not parallel, carried to the directions (1); unique intersection (1); circle exists (1); uniqueness (1).

### 5.3 Section 10.3: Convex Sets and Hulls (`03-convex-sets-and-hulls.md`)

**Budget** ≤ 5,000 (~3,600). One fold (λ_{k+1} = 1 in the induction). Three Quick checks, one Try-it-first. The chapter's last section, so it carries the **R group** (STYLE §11.5). **Warning:** "Midpoints are not enough" (after the two-point-test box). **Non-examples:** the annulus and the axes (opening Quick check), `exm-star-not-convex`.

**Opening (~250).** Analysis moves between points along segments (mean value theorem, connectedness, Cauchy's theorem). **Weird-examples Quick check** before the definition: which of a disc, an annulus 1 ≤ ‖x‖ ≤ 2, a line, two points, ∅, the union of the axes contain the segment between any two of their points? *Solution:* disc yes (below); annulus no ((±3/2, 0), midpoint 0); line yes; two points no; ∅ yes (nothing to check); axes no ((1, 0), (0, 1)).

**`## Convex sets and balls` (~800).**
1. **`def-convex-set-rn`**: C convex if [p, q] ⊆ C for all p, q ∈ C.
2. **`def-ball-rn`**: B(c, r) ≔ {‖x − c‖ < r}, B̄(c, r) ≔ {‖x − c‖ ≤ r}, r > 0. "Open", "closed" are names; AN1 explains them and defines balls for any distance (prose).
3. **`prp-balls-convex`**.
   - **`[Scratch work]`** with table: Givens ‖p − c‖ < r, ‖q − c‖ < r, t ∈ [0, 1]; Goal ‖(1 − t)p + tq − c‖ < r; row 2: write c = (1 − t)c + tc, the vector is (1 − t)(p − c) + t(q − c); gap closed by the triangle inequality and homogeneity.
   - *Proof.* ‖(1 − t)(p − c) + t(q − c)‖ ≤ (1 − t)‖p − c‖ + t‖q − c‖ < (1 − t)r + tr = r (one of the weights is positive; if t = 0 or 1, immediate). Closed ball with ≤.
4. **`exm-method-two-point-test`** `[Method: the two-point test]`. *Template.* Take p, q ∈ C, t ∈ [0, 1]; write the condition for p and q; split the vector or sum for (1 − t)p + tq as (1 − t)(…) + t(…); conclude by the triangle inequality or linearity. *When.* Proving convexity from a definition. *Usual failure.* Checking only t = 1/2 (the warning below); allowing t outside [0, 1].
5. **Warning** `**Midpoints are not enough.**` ℚ² ⊆ ℝ² contains the midpoint ((a + c)/2, (b + d)/2) of any two of its points, but it is not convex: (√2/2, 0) = (1 − t)(0, 0) + t(1, 0) with t ≔ √2/2. Here √2 exists by `@fd3:prp-cof-square-roots` (with `@fd3:thm-reals-complete-ordered-field`); 1 < 2 < 4 gives 1 < √2 < 2 (`@fd3:prp-ordered-ring-rules` (g)), so t ∈ [0, 1]; and t ∉ ℚ, since otherwise √2 = 2t ∈ ℚ, against `@fd3:thm-no-rational-square-two`. So the point lies on [(0, 0), (1, 0)] but not in ℚ².

**`## Examples and operations` (~700).**
1. **`prp-convex-examples`**: lines, segments, hyperplanes, half-spaces are convex. *Proof* (terse): (1 − t)(p + sv) + t(p + uv) = p + ((1 − t)s + tu)v; `lem-subsegment`; ⟨a, (1 − t)x + ty⟩ = (1 − t)⟨a, x⟩ + t⟨a, y⟩.
2. **`prp-convex-operations`**: (a) any intersection of convex sets is convex (`@fd2:def-family-union-intersection`); (b) b + C and λC are convex; (c) a union of two convex sets need not be ({p} ∪ {q}).
3. **Quick check.** {x₁ ≥ 0, x₂ ≥ 0, x₁ + x₂ ≤ 1} is convex: three half-spaces, (a).

**`## Convex combinations and the hull` (~1,200).**
1. **`def-convex-combination-rn`**: Σλ_ip_i with λ_i ≥ 0, Σλ_i = 1 (k ≥ 1); k = 2 gives [p₁, p₂].
2. **`thm-convex-contains-combinations`**: a convex set contains every convex combination of its points. *Proof* by induction on k (`@fd2:thm-induction`), move "peel off the last point": scratch (≤ 6 lines): convexity speaks about two points, so split one off. If λ_{k+1} ≠ 1, s ≔ 1 − λ_{k+1} > 0 and Σ_{i≤k+1}λ_ip_i = s·Σ_{i≤k}(λ_i/s)p_i + λ_{k+1}p_{k+1}, a point of a segment between two points of C. λ_{k+1} = 1 in the fold.
3. **`def-convex-hull-rn`**: conv S ≔ intersection of all convex sets containing S; the smallest such (pattern of `@fd2:prp-smallest-closed-set`; ℝⁿ is one, so the family is non-empty).
4. **Try it first** (ten minutes): "Describe conv{p, q, r} without the word *intersection*." Folded answer leads into the theorem: the segments [p, q], [q, r], [r, p] are not enough (their union is not convex); points of [x, r] with x ∈ [p, q] are.
5. **`thm-convex-hull-combinations-rn`** (key proof): conv S = K, the set of convex combinations of finitely many points of S. *Proof.* K ⊆ conv S by 2. K ⊇ S and K is convex: (1 − t)Σλ_ip_i + tΣμ_jq_j is a combination of the joined list with weights (1 − t)λ_i, tμ_j (constants through sums by `@lem-ring-finite-sums` (b)); the sum over the joined list splits into the two sums (`@prp-sum-reindex` (b)), so the weights sum to (1 − t) + t = 1; hence conv S ⊆ K.
6. **`exm-triangle-as-hull`**: conv{p₁, p₂, p₃} is the filled triangle. (1, 1) is in the hull of (0, 0), (3, 0), (0, 3) (weights 1/3 each); (2, 2) is not (3λ₂ = 3λ₃ = 2 forces λ₂ + λ₃ = 4/3 > 1).

**`## Star-shaped sets` (~350).**
1. **`def-star-shaped`**: S is star-shaped about c ∈ S if [c, x] ⊆ S for every x ∈ S. A non-empty convex set is star-shaped about each of its points.
2. **`exm-star-not-convex`**: the union A of the axes of ℝ² is star-shaped about 0, not convex; not star-shaped about (1, 0) ((1/2, 1/2) ∈ [(1, 0), (0, 1)]).

**Exercises.**
- **A1.** Convex or not: (a) {y ≥ x²}; (b) {y ≤ x²}; (c) ℤ²; (d) {1 ≤ ‖x‖ ≤ 2} ⊆ ℝ². *Answers:* (a) yes (B1); (b) no: (±1, 1), midpoint (0, 1); (c) no: midpoint (1/2, 0); (d) no: (±3/2, 0).
- **A2.** (a) Is (1, 2) in conv{(0, 0), (3, 0), (0, 3)}? (b) *(Proof comprehension, key proof `thm-convex-hull-combinations-rn`.)* Which half of the proof uses `thm-convex-contains-combinations`, and why is the family of convex sets containing S non-empty? *Answer:* (a) yes, (1/3)(3, 0) + (2/3)(0, 3). (b) K ⊆ conv S: conv S is convex and contains S, so it contains every convex combination of points of S. The family contains ℝⁿ.
- **B1.** Prove A1 (a). *Answer:* (1 − t)b + td ≥ (1 − t)a² + tc² = ((1 − t)a + tc)² + t(1 − t)(a − c)² ≥ ((1 − t)a + tc)² (identity by expanding; sidecar).
- **B2.** C, D convex ⇒ C + D convex. *Answer:* (1 − t)(x + y) + t(x′ + y′) = ((1 − t)x + tx′) + ((1 − t)y + ty′).
- **B3** (strict convexity; Idea citing `exm-method-equality-case`). For p ≠ q in S(c, r) and 0 < t < 1, ‖(1 − t)p + tq − c‖ < r. *Answer:* ≤ r by the triangle inequality; equality gives, by the equality case with u = (1 − t)(p − c) ≠ 0, t(q − c) = λ(1 − t)(p − c), λ ≥ 0, so q − c = μ(p − c), μ ≥ 0; equal norms force μ = 1, q = p. Aftermath: for the square {max(|x₁|, |x₂|) ≤ 1} the analogue fails (its edge contains [(1, −1), (1, 1)]); AN1 returns to this (prose).
- **B4** (prove or disprove). (a) A union of two convex sets is convex. (b) The complement of a convex subset of ℝ² is convex. (c) conv(S ∪ T) = conv S ∪ conv T. (d) {x : ‖x − p‖ ≤ ‖x − q‖} is convex. (e) If C is convex and λ, μ ≥ 0, then λC + μC = (λ + μ)C. *Answers:* (a) false (`prp-convex-operations` (c)). (b) false: complement of B̄(0, 1), (±2, 0). (c) false: S = {p}, T = {q}, p ≠ q: the midpoint is in neither hull of a point. (d) true: a closed half-space (`prp-perpendicular-bisector` with totality for ≤; ℝⁿ if p = q). (e) true: ⊇ since (λ + μ)c = λc + μc; ⊆: for λ + μ > 0, λx + μy = (λ + μ)((λ/(λ + μ))x + (μ/(λ + μ))y), a point of (λ + μ)C by convexity; for λ = μ = 0 both sides are {0} if C ≠ ∅ and ∅ if C = ∅.
- **C1** (exit check). A non-empty convex C ⊆ ℝ is an interval: with α ≔ inf C (or −∞), β ≔ sup C (or +∞), (α, β) ⊆ C ⊆ [α, β] ∩ ℝ. *Answer:* sup C exists when C is bounded above (`@fd3:def-complete-ordered-field`, with `@fd3:thm-reals-complete-ordered-field`); if C is bounded below, −C ≔ {−c : c ∈ C} is bounded above, and −sup(−C) is a lower bound of C that every lower bound c′ satisfies c′ ≤ −sup(−C) (as −c′ is an upper bound of −C): so inf C = −sup(−C) (derived here in two lines, not cited). For α < x < β there are a, b ∈ C with a < x < b (x is neither a lower nor an upper bound), and x ∈ [a, b] ⊆ C; the second inclusion is the definition of inf and sup. *Marking scheme* (4): inf/sup or infinite cases, inf via −sup(−C) (1); a, b found (1); segment = interval for n = 1 (1); conclusion (1).

- **R1** (one chapter back; Chapter 9). Let Q ≔ {x ∈ ℝⁿ : |x_k| ≤ 1 for every k}. Show that Q is convex and that B̄(0, 1) ⊆ Q ⊆ B̄(0, √n). *Answer:* |x_k| ≤ 1 iff ⟨e_k, x⟩ ≤ 1 and ⟨−e_k, x⟩ ≤ 1 (`@fd3:prp-absolute-value-ordered-field` (d)), so Q is the intersection of 2n closed half-spaces (`prp-convex-examples`, `prp-convex-operations` (a)). ‖x‖ ≤ 1 gives |x_k| ≤ ‖x‖ ≤ 1 (`prp-norm-coordinate-bounds` (a)); x ∈ Q gives max_k |x_k| ≤ 1, so ‖x‖ ≤ √n (`prp-norm-coordinate-bounds` (b)). (Prose in the solution: the two inclusions are the ones AN1 uses to compare balls and boxes.)
- **R2** (four chapters back; Chapter 6; no hint of method). Identify a + bx + cx² ∈ ℝ[x] with (a, b, c) ∈ ℝ³. Show that the set P of these polynomials f with f(t) ≥ 0 for every t ∈ [0, 1] is convex. *Answer:* for fixed t, evaluation respects sums and real multiples (`@thm-evaluation-respects-operations`), so f(t) = ⟨(1, t, t²), (a, b, c)⟩ and {f : f(t) ≥ 0} is a closed half-space with normal (1, t, t²) ≠ 0; P is the intersection of these half-spaces over t ∈ [0, 1] (`prp-convex-operations` (a)). (Two-point test directly also works: ((1 − s)f + sg)(t) = (1 − s)f(t) + sg(t) ≥ 0.)
- **R3** (spiral; Chapter 3). For c ∈ ℂ, r > 0 and u ∈ 𝕋, show that D ≔ {z ∈ ℂ : |z − c| < r} is convex as a subset of ℝ², and that z ↦ uz maps D onto {z : |z − uc| < r}. *Answer:* |z − c| = ‖z − c‖ (`prp-plane-is-complex-plane` (c)), so D = B(c, r), convex by `prp-balls-convex`. |uz − uc| = |u||z − c| = |z − c| (`@thm-conjugate-properties` (d)), so the image lies in the second disc; onto: for |w − uc| < r, z ≔ ūw has uz = w (`@prp-unit-circle` (a)) and |z − c| = |ū||w − uc| < r. (Prose: turning the plane by a unit complex number is the subject of the opening of *Complex Analysis*.)

---

## 6. Pointers and promises (coordinator; this blueprint touches no src, config, ledger or registry)

- **Registry:** F4.9 title "Lines, Hyperplanes, and Convex Sets", directory slug `ch10-lines-hyperplanes-convex-sets`; plan-edges F4.9 `s: [F4.8, F4.6]`, `see: [F4.1, F5.4]` (review items only; coordinator's call), **not** `s: [F4.8, F4.1]` as proposal §4 has it. F4.10 → F4.9 rename stays (proposal §4.1), but CA.1's and AN1.10's F4.10 edges should point to their new homes below rather than to F4.9. chapter-constraints: F4.9's isometry rule is withdrawn (proposal §3.5 item 2: "chapter-constraints 的「不用線代」規則要撤"); F4.10's rule moves with its material. exam-targets apostol-ma (F4.10 lines 103, 108, 110): re-point to the new homes, not to F4.9.
- **Rehoming of the S1 Sections 10.4–10.5** (plans in commit `a347ec8`; reviewers' S2 fixes for them listed so the receiving blueprint can apply them):
  - Isometries of ℝⁿ (`def-isometry-rn`, reflections ρ_{a,c}, `thm-isometry-preserves-segments`, the classification, ℝ² read as ℂ, `thm-two-reflections-rotation`, the group E): **GEO** (*Affine and Projective Geometry*) for the plane list and the segment-preserving theorem, **LA3** (*Inner Products and Spectral Theory*) for x ↦ Ax + b. Fixes to carry: `thm-angle-in-the-plane` (b) should say "direct isometry f(ζ) = uζ + b (u ∈ 𝕋)"; the two-rotations exercise must state the order of composition; `prp-complex-isometry-group` cites `@exm-groups` (c) for S_ℂ and Chapter 5's 𝕋-subgroup example; the dihedral item cites `@thm-complex-nth-roots` (b) for distinctness; ℝ's isometry exit check cites absolute value (b) and ring rules (f).
  - Rotations as multiplication by u ∈ 𝕋, `def-argument-set`, `prp-argument-of-product`, the oriented angle: **CA.1 opening** (proposal's stated cost of option (b)). `def-principal-argument`: **AN2 ch07** (which already planned Arg) or CA.1, coordinator's call. Fixes to carry: the non-additivity argument is algebraic (A(1) = 2A(1) gives A(1) = 0, then 4A(i) = A(1) = 0, so A(i) = 0 ∉ arg i), with no "jump" language; existence of Arg on the main line by a one-sentence Idea, the integer-part computation in a fold; Re(z̄w) = ⟨z, w⟩ cited from `@fd4:prp-plane-is-complex-plane` (b), only Im(z̄w) = ad − bc new.
- **Chapter 9 blueprint (frozen, `merged-ch09-f48.md`) must be amended by the coordinator** to match this cut (its S2 round aligned it with this file's S1 version): change 3 and the Looking-ahead box `[Looking ahead: the angle itself]` (line 210) should send θ for n = 2 to *Complex Analysis* (CA.1) and drop "Section 10.5 (`thm-angle-in-the-plane`)"; the exports table rows for `prp-polarization-rn` (Ch10 §10.4), `prp-plane-is-complex-plane` (Ch10 §10.5) and `def-angle-cosine-rn` (Ch10 §10.5) should name Ch10 §10.3 R3 for `prp-plane-is-complex-plane` and drop the other Ch10 entries; its S2a item 15 and the Opened item asking Ch10 to adopt `prp-plane-is-complex-plane` (b) close as "Ch10 cites (c) in R3; §10.5 left the book". Ch9's §9.4 B3 stays as is; this chapter recalls it in prose before `prp-perpendicular-bisector`.
- **NOTATION.md:** no rows for τ_b, ρ_{a,c}, σ_u, arg, Arg; the `\cos\angle(x, y)` row is **not** amended by this chapter.
- **Downstream:** AM ch05 cites `@fd4:def-star-shaped`; AN1 (metric spaces, former F4.11) cites `@fd4:def-ball-rn` and picks up thread 1; AN2 ch07 keeps its own Arg unless the coordinator homes `def-principal-argument` elsewhere.

## 7. Notes for S3

Sidecars: §10.1 B2, A2 (b); §10.2 A1, A2, B1, B2, C1 stem example; §10.3 B1, `exm-triangle-as-hull`, B4 (e).

## 8. S2a: claims to verify

1. Chapter 9 labels (§4) against `merged-ch09-f48.md` (checked at S2: all exist with the content used) and again against Ch9 src once drafted.
2. fd3 labels and item letters after the fd3 re-cut (§4 list; especially ring rules (g), (i), halves (d), absolute value (d)).
3. fd2 labels after the fd2 re-cut (all exist at HEAD 2026-10-26).
4. Chapter 1 labels `lem-ring-finite-sums` (b), `prp-sum-reindex` (b) against Ch1 src once drafted (item letters as in `merged-ch01-f46.md`).
5. Same-book labels for the review items: Chapter 3 (`thm-conjugate-properties` (d), `prp-unit-circle` (a)), Chapter 6 (`thm-evaluation-respects-operations`), after the structural move.
6. Label uniqueness re-grep at S3, including new src of Chapters 1, 8, 9.
7. Hours after S3 by `check_structure.py --words`; if over 15 / 20 unrounded, trim `prp-segment-crosses-hyperplane` or R3 first.
8. Coordinator: the Chapter 9 amendment of §6 is made before Ch9 or Ch10 goes to S3.

---

## S2 replies (round 1)

Two blind reviews (R-A, R-B). Every finding is applied or answered below.

**R-A**
1. *Error, scope vs approved option.* **Applied.** Ch10 is cut to Sections 10.1–10.3, title "Lines, Hyperplanes, and Convex Sets". 10.4 and 10.5 move to GEO/LA3 and CA.1 (AN2 ch07 for Arg); §6 lists the homes. Threads 1 and 4 are removed, and so are the Chapter 5 dependence and the old promise that Ch9 would be amended toward 10.5. The Authority line quotes the approved text. The coordinator's relayed wording ("isometry classification moves") is read as shorthand for that option, not as a new scope, so no question goes to the author. Hours are recomputed from word counts (§2). Ch9/Ch10 agreement: at the time of this round, the frozen Ch9 (`d1da300`) had been aligned with this file's S1 version and points to §10.5. §6 and S2a 8 ask the coordinator to amend Ch9 before S3 (I may edit only this file).
2. *Gap, re-proof of the Ch9 inner-product identity.* **Applied by removal.** `lem-complex-plane-inner-product` left with §10.5. The citation fix (`prp-plane-is-complex-plane` (b), new part only Im) is passed to the receiving blueprint (§6). R3 cites `prp-plane-is-complex-plane` (c), which is in §4.
3. *Gap, stale Ch9 references.* **Applied.** §4 points at `merged-ch09-f48.md`, and the eleven labels plus `prp-norm-coordinate-bounds` and `prp-plane-is-complex-plane` were checked. The §05 C3 remark and the old S2a item 2 are deleted. `prp-perpendicular-bisector` now has a one-sentence prose recall of Section 9.4 B3, a one-line Idea, and a short proof that names the hyperplane reading and the strict half-space.
4. *Gap, Arg non-additivity sentence.* **Answered: section removed.** The corrected algebraic argument is recorded in §6 for CA.1/AN2.
5. *Minor, Ch5/Ch3 prerequisites in §10.5.* **Answered: section removed.** The fixes (`@exm-groups` (c), the 𝕋-subgroup example, Section 3.6, de Moivre before nth roots) are in §6. "What you need" no longer lists Chapter 5.
6. *Minor, "rotation" for uζ + b.* **Answered: removed.** The fix ("direct isometry") is in §6.
7. *Minor, B2 order of composition.* **Answered: removed.** The fix is in §6.
8. *Minor, §10.3 B4 (e) fd3 label.* **Applied.** The ℚ² example is now the §10.3 warning (R-B 6). It cites `@fd3:thm-no-rational-square-two` (added to §4) and spells out 1 < √2 < 2 by ring rules (g), so t = √2/2 ∈ [0, 1], and t ∈ ℚ ⇒ √2 = 2t ∈ ℚ. B4 (e) is replaced by λC + μC = (λ + μ)C (true).
9. *Minor, loose citations.* **Applied** for `lem-subsegment` (halves (d), ring rules (b)) and for `prp-perpendicular-bisector` (equality of non-negative quantities from (g) with totality (i)). The §10.4 C1 item left with its section; its fix is in §6.
10. *Minor, inf in §10.3 C1.* **Applied.** The answer derives inf C = −sup(−C) in two lines and cites `def-complete-ordered-field` only for sup. It does not cite fd3's exercise.
11. *Minor, §10.2 C1 conversion.* **Applied.** The answer passes from normals to directions by `exm-lines-in-the-plane` (a) and notes that the multiples correspond; the marking scheme follows.
12. *Minor, Chapter 1 line.* **Applied.** `merged-ch01-f46.md` was checked. `thm-convex-hull-combinations-rn` cites `@lem-ring-finite-sums` (b) and `@prp-sum-reindex` (b). Square roots stay with fd3, and no completing of squares is needed. The old S2a 6 is closed.
13. *Minor, core/full gap.* **Applied.** Hours are recomputed from word counts and exercise counts (§2): 12.4 / 18.8 unrounded, 10 / 20 rounded. With three sections and an R group, the full track is now about 1.5 times the core.

**R-B**
1. *Error, scope and hours.* **Applied**, as R-A 1. Retitled, registry row, Looking-ahead box, threads 1 and 4 dropped; thread 2 (now 1) ends in a prose pointer to AN1/GEO in the aftermath of `thm-betweenness`. Hours by the research-reader formula, placed inside 257 / 326 (§2). The 14 / 20 figure is no longer used as the derivation.
2. *Error, conflict with Ch9 on θ.* **Applied on this side.** `thm-angle-in-the-plane` and the NOTATION amendment are removed, and so is the §6 bullet that edited Ch9's "F4.10 proves cos∠ = cos θ". The frozen Ch9 now points to Section 10.5 (its S2 followed this file's S1), so §6 lists the exact Ch9 lines that must change in the same round. This is coordinator work, and S2a 8 tracks it.
3. *Gap, lemma re-proves Ch9.* **Applied by removal**, as R-A 2.
4. *Minor, f4-8.md source.* **Applied**, as R-A 3.
5. *Minor, §05 C3 / §9.4 B3.* **Applied.** The C3 bullet and its S2a item are deleted. The bisector proposition recalls B3 in prose, gives a one-line Idea and proves only the hyperplane reading and the strict half-space. Ch9's B3 stays as a forward-pointing exercise.
6. *Gap, warnings per section.* **Applied.** Each section plan names its warning and its non-example: §10.1 equal distances; §10.2 normals not unique, a = 0; §10.3 midpoint-convex is not convex (ℚ², promoted from B4 (e), which now holds a different item). §1 lists them.
7. *Minor, "What you need".* **Applied.** Chapter 5 is dropped. Chapter 3 (Sections 3.2, 3.5) and Chapter 6 (Section 6.4) are listed for the review items only, and Chapter 1, Section 1.1 for sums. The plan-edges proposal becomes `s: [F4.8, F4.6]`, `see: [F4.1, F5.4]` (§6). The Chapter 1 line is updated (R-A 12).
8. *Minor, R1 (b) vs (c).* **Answered: removed.** The fix is in §6.
9. *Minor, Arg existence bookkeeping.* **Answered: removed.** The fold instruction is in §6 for its new home.

**Added in this round (STYLE requirements that the cut exposed):** §10.3 is now the chapter's last section, so it gets an R group: R1 Ch9 (cube between two balls), R2 Ch6 (non-negative quadratics on [0, 1], no hint), R3 Ch3 spiral (discs and turning by u ∈ 𝕋). Proof-comprehension parts are added to §10.1 A2 and §10.3 A2 for the two key proofs. The Try-it-first moves from the old §10.4 to `thm-convex-hull-combinations-rn`.

**Open:** the Chapter 9 amendment (§6, S2a 8); the homes of the rehomed material (GEO / LA3 / CA.1 / AN2 ch07) and the plan-edges, chapter-constraints and exam-targets edits (coordinator); fd3 item letters after the re-cut (S2a 2).
