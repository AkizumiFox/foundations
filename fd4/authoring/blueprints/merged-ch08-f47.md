<!-- hand-written -->
# Blueprint: Chapter 8 (F4.7) Real Functions and Their Graphs, merged book, stage S1

**Frozen after S2 (2026-10-26).** Supersedes `f4-7.md`. S2 round 1 applied (replies at the end). Next: S2a, S3, S4, lean review (changed-only, S7, S7r).

**Book and place.** *Preliminaries for Analysis and Algebra* (fd4 after the merge with fd5; `fd4/authoring/design/merge-proposal.md`, approved 2026-10-26: slot fd4, F5.x ids kept, F4.11 to AN1, total about 257 core / 326 full hours). Chapter **8**, the first chapter of Part III *Functions and Space* (Ch8 F4.7, Ch9 F4.8, Ch10 F4.9 with F4.10). Directory `fd4/src/ch08-real-functions/`, sidecars `fd4/verify/ch08/`, ledger `fd4/authoring/ledger/ch08.yaml`. Sections are numbered 8.1–8.6.

**What changed against `f4-7.md`.**
1. **Old §05 "Polynomial Functions and Their Roots" is deleted.** The factor theorem, the root count, the identity principle and the growth bound are proved in Chapters 6–7 for every field (and for ℂ); this chapter cites them and proves nothing about polynomials. Polynomial and rational functions become one definition in 8.1; the growth bound becomes an example in 8.3; "at most d roots" is used in 8.6 R1 and R4.
2. Seven sections become six; the "leading term" box goes (it is `@lem-complex-polynomial-growth`).
3. **No re-proof.** fd2's `@fd2:prp-strictly-monotone-injective` and `@fd2:exm-maps-from-calculus` (a) (x³) are cited; fd2's solution of `@fd2:exm-maps-from-calculus` (a) already proves x³ strictly increasing, so it is cited, not re-proved; Chapter 3's `@lem-reals-nth-root` gives roots and monotone n-th powers; `@thm-binomial-commutative-ring` the binomial theorem (Chapter 1 after the merge, proposal §3.4; label kept; currently `fd5/src/ch02-fields/06-frobenius-and-fermat.md` until the structural move).
4. **No dependence on Chapter 1's unwritten labels**: the old ⟨F4.6⟩ citations are replaced by existing labels; rational powers are reached through exp (`prp-real-power-consistent`). See the reconciliation table.
5. **C items reduced** (author: 「再砍到約 257/326 小時」): at most two C per section, two exit checks; 62 exercises become 47.
6. Moderate difficulty (「太多不必要的太難的知識」): the (E3)-from-completeness item and the polynomial exit check go; `prp-iterated-sup` is a fold.

**House manner** (STYLE §1 "House manner from fd2 on", §12.14; model `fd2/authoring/blueprints/ch02-functions.md`). Motivation first, the naive attempt as hook; `[Scratch work]` with a Givens/Goal table at each method's first full appearance, kept apart from the proof; method boxes `exm-method-<slug>`; one *Prove or disprove* B item per method section; Quick checks about one per 900 main-line words, with answers. No footnotes, no jokes, no persona (voice "we"), history only in a line that carries mathematics. Nothing from `/home/akizumi/book` or the sources is copied; every example and item below is ours.

**Purpose.** AN1 adds, composes, inverts, bounds and floors functions D → ℝ and uses exp, log and real powers as examples; this chapter supplies that vocabulary **with proofs from the complete ordered field**, and opens the table of strange functions AN1 tests its definitions against. **No limit, continuity or derivative is used**; the only completeness tool is the supremum. Sources for coverage only: Lang *Basic Mathematics* ch. 13, Spivak ch. 3–4, Apostol *Calculus I* §1.3–1.12.

**Named moves** (index): the five method boxes `exm-method-graph-pairs` (8.1), `-factor-difference` (8.2), `-sup-two-halves` (8.3), `-floor-inequality` (8.4), `-archimedes-squeeze` (8.5).

## Prerequisites (all grepped in `fd*/src` on 2026-10-26)

- **fd1:** `@fd1:ax-induction`, `@fd1:prp-quantifier-negation`, `@fd1:prp-contrapositive`, `@fd1:exm-not-allowed-catalogue`.
- **fd2:** `@fd2:def-ordered-pair`, `@fd2:def-cartesian-product`, `@fd2:def-function`, `@fd2:prp-function-equality`, `@fd2:def-composition`, `@fd2:prp-composition-associative`, `@fd2:def-restriction-extension`, `@fd2:exm-piecewise-as-gluing`, `@fd2:def-indicator`, `@fd2:def-injective`, `@fd2:def-bijective`, `@fd2:prp-strictly-monotone-injective`, `@fd2:exm-maps-from-calculus`, `@fd2:thm-composition-injective-surjective`, `@fd2:def-inverse-function`, `@fd2:thm-bijection-iff-inverse`, `@fd2:def-image`, `@fd2:thm-image-intersection`, `@fd2:exm-sets-of-numbers-as-images`, `@fd2:def-sum-product`, `@fd2:def-power`, `@fd2:prp-power-laws`, `@fd2:prp-geometric-sum`, `@fd2:thm-bernoulli` (real x ≥ −1), `@fd2:def-finite`, `@fd2:prp-subset-finite`, `@fd2:prp-disjoint-union-count`, `@fd2:exr-finite-sets-b3` (finite unions; 8.6 only), `@fd2:prp-finite-max`, `@fd2:cor-finite-size-unique`, `@fd2:def-partial-order`, `@fd2:def-order-bounds`, `@fd2:def-order-supremum`.
- **fd3:** `@fd3:def-complete-ordered-field`, `@fd3:thm-reals-complete-ordered-field`, `@fd3:thm-cof-complete-archimedean`, `@fd3:prp-ordered-ring-rules`, `@fd3:prp-ordered-field-halves`, `@fd3:prp-reciprocal-order`, `@fd3:lem-field-fraction-rules`, `@fd3:def-absolute-value-ordered-field`, `@fd3:prp-absolute-value-ordered-field` ((d) |x| ≤ r, (e) triangle, (f) reverse), `@fd3:thm-rationals-embed-ordered-field`, `@fd3:prp-archimedean-reciprocal`, `@fd3:prp-integer-part-ordered-field`, `@fd3:thm-integers-ordered-ring` ((c) discreteness), `@fd3:thm-rationals-dense-ordered-field`, `@fd3:prp-cof-square-roots`, `@fd3:thm-no-rational-square-two`, `@fd3:prp-rational-integer-part` (8.4 hook), `@fd3:exr-rationals-inside-the-reals-c2` (recalled in 8.6), `@fd3:def-sequence-limit-ordered-field` (R3 only).
- **Earlier chapters of this book (same-book labels):** Ch2 `@prp-rationals-lowest-terms`; Ch3 `@lem-reals-nth-root`, `@prp-reals-embed-complex`, `@prp-modulus-of-real`; Ch1 `@thm-binomial-commutative-ring` (8.5 B2 (a) only; label now in fd5 ch02 §06); Ch5 `@exm-groups`, `@thm-subgroup-test` (R2 only); Ch6 `@def-polynomial-evaluation`, `@prp-polynomial-function-map`; Ch7 `@thm-polynomial-identity-from-values`, `@thm-polynomial-root-count`, `@thm-polynomial-remainder-factor`, `@lem-complex-polynomial-growth`, `@cor-real-odd-degree-root`.
- **Forbidden:** Ch9–Ch10, AN1/AN2, and every fact about cos, sin, π, limits (except R3's fd3 sequence limit), continuity or derivatives. No school fact in a proof. `@ax-cosine-sine` is not used.

## Notation (NOTATION.md rows; drafter confirms at S3)

- `f \colon D \to \nR`, D ⊆ ℝ: a real function; the domain is always stated, no natural-domain convention. `\operatorname{graph} f \coloneqq \{(x, f(x)) : x \in D\}`.
- `f + g`, `fg`, `cf`, `f/g`, `\max(f, g)`, `\abs{f}` pointwise on D_f ∩ D_g (f/g also off the zeros of g); `g \circ f` on {x ∈ D_f : f(x) ∈ D_g}.
- increasing: x < y ⇒ f(x) ≤ f(y); strictly increasing: ⇒ f(x) < f(y); no "non-decreasing".
- `\sup_A f`, `\inf_A f`: sup and inf of f(A).
- `\floor{x}`, `\ceil{x}` for every real x (amends the row); fractional part written x − ⌊x⌋, never `\{x\}`. `\dist(x, \nZ)`: distance to the nearest integer (not ‖x‖, which Ch9 reserves).
- `\exp`, `\log`, `e`, `a^x` (a > 0): amends the `u^n` and `\sqrt[n]` rows ("real exponents AN1.10" → "Ch8 §05, from the borrowed box paid in AN1.10"). No `\ln`. `e^x` only after `prp-real-power-consistent`.

## Labels

- **Definitions:** `def-real-function`, `def-function-algebra`, `def-polynomial-rational-function`, `def-even-odd-function`, `def-monotone-function`, `def-bounded-function`, `def-sup-of-function`, `def-floor-ceiling`, `def-distance-to-integer`, `def-periodic-function`, `def-step-function`, `ax-exponential`, `def-euler-number`, `def-logarithm`, `def-real-power`, `def-dirichlet-function`, `def-thomae-function`.
- **Results:** `prp-graph-vertical-line`, `prp-graph-transformations`, `prp-even-odd-decomposition`, `prp-monotone-algebra`, `prp-strictly-monotone-order-reflecting`, `thm-monotone-inverse`, `prp-real-infimum`, `prp-real-sup-approximation`, `thm-sup-function-rules`, `prp-sup-oscillation`, `prp-iterated-sup`, `prp-floor-rules`, `prp-distance-to-integer`, `prp-step-function-algebra`, `prp-exp-first-consequences`, `thm-exp-unique`, `prp-log-rules`, `prp-real-power-consistent`, `prp-real-power-laws`, `prp-exp-beats-powers`, `lem-irrationals-dense`, `prp-dirichlet-properties`, `prp-thomae-large-values`, `prp-staircase-squeeze`, `prp-zigzag-all-values`.
- **Examples:** `exm-first-real-functions`, `exm-method-graph-pairs`, `exm-method-factor-difference`, `exm-mobius-increasing`, `exm-squash-function`, `exm-injective-not-monotone`, `exm-odd-roots`, `exm-method-sup-two-halves`, `exm-sup-not-attained`, `exm-sup-attained-parabola`, `exm-polynomial-unbounded`, `exm-method-floor-inequality`, `exm-method-archimedes-squeeze`, `exm-strange-functions`, `exm-strange-involution`, `exm-strange-jump`, `exm-strange-staircase`, `exm-strange-zigzag`, `exm-strange-unbounded`, `exm-strange-sup-missed`.
- **Exercises:** `exr-<file-slug>-a1` …
- None exists in `fd4/src` or `fd5/src` (checked); the old `prp-strictly-monotone-injective` is dropped for fd2's.

**Scaffolding** (Part III of an entry volume: full formats for new moves, STYLE §11.12).
- Full-level method sections: 8.2, 8.3. Idea level: 8.1, 8.4, 8.5. Terse: 8.6 (one Idea).
- **Key proofs** (A item in the section): `thm-monotone-inverse` (8.2), `prp-sup-oscillation` (8.3), `thm-exp-unique` (8.5).
- **Faded triple** for "bound every value, then find a witness": full in `thm-sup-function-rules` (b), (d); last step blank 8.3 B1; last half blank 8.3 C2. Each blank: "*Name the move, then complete it.*"
- **Proof ordering:** 8.5 B3 (`thm-exp-unique`).
- **Find the error:** true conclusion 8.2 C1, 8.5 C1; false conclusion 8.3 B4.
- **Try it first:** `thm-monotone-inverse`, `prp-sup-oscillation`.
- **Self-explanation prompts:** `thm-monotone-inverse` ("where is totality of ≤ used?"), `prp-sup-oscillation` ("why ε/2?"), `thm-exp-unique` ("why must n exceed |x|?").
- **Exit checks** (marking schemes, STYLE §11.6): 8.3 C1, 8.5 C2.
- **"used later":** 8.1 C1 (→ 8.6 C1). (8.2 C2 is recalled backward from 8.6 J; 8.4 C2 is no longer tagged, S2.)
- **Forward pointers** (STYLE §12.1): at most one `[Looking ahead]` remark per section, at the end of the main line before the Exercises, naming the volume in words: 8.2, 8.3, 8.4, 8.6 have one; 8.1 and 8.5 none (8.5's borrowed box is a borrow, not a pointer). No other prose pointer to a later volume.
- **R group** in 8.6 only.

**Figures** (plain TikZ, illustration only, captions say what they show), marked "Figure" in the plans; 8.6 adds the staircase against y = x, the zigzag on [1/6, 1] and dot plots of D and T.

---

## index.md

- **Story.** Before analysis asks whether f(x) gets close to f(a) or how fast exp x outruns x¹⁰, the functions must be in hand: what a real function is, how to combine, invert and bound one, which concrete ones exist, proved from the complete ordered field; plus a catalogue of strange functions for later definitions to be tested on.
- **What you need** (written last, by chapter, from the Prerequisites list): *Number Systems*, *Sets and Functions*, *Logic and Proof*; Chapters 2, 3, 6, 7 of this book, plus Chapter 1 (the binomial theorem, in one exercise, 8.5 B2) and Chapter 5 (groups, in one review item, 8.6 R2). A reader on the analysis path (Ch1–3, 8–10) meets Part II only through a few cited statements, each restated where used.
- **What this chapter borrows:** three facts about exp, from `ax-exponential` in 8.5 on; nothing before it, nothing in 8.6.
- **Time.** About **25 hours** core, **40 hours** full (rounded to the nearest 5, STYLE §2 item 4). Basis (STYLE §11.9, at the fd4 rate of about 1,600 main-line words per hour and about half an hour per exercise): main line about 22,300 words ≈ 13.9 h (Quick checks included, inside the section budgets); folds 200 + 300 + 400 + 200 + 300 + 0 = 1,400 words ≈ 0.9 h; core = 24 exercises (all A, one B, one C per section, the C being the exit check where there is one) = 12 h, so core ≈ 13.9 + 12 ≈ 26 h → 25; full = 47 exercises ≈ 23.5 h, so full ≈ 13.9 + 0.9 + 23.5 ≈ 38 h → 40. Recomputed at S3 from delivered counts. Consistent with the book total 257/326 (proposal §3.5: F4.7 had 30/43 before the cuts).
- **Roadmap**, **Named moves**, **Summary**, **Terms**.

---

## 8.1 `01-real-functions-and-graphs.md` — Real Functions and Their Graphs

Budget: 3,600 main-line words; fold ≤ 200. Idea-level method section.

- **Hook.** "Let f(x) = x²/x. What is f(0)?" A formula is not a function until its domain is named (`@fd2:def-function`, `@fd2:prp-function-equality`).
- **`def-real-function`.** f: D → ℝ with D ⊆ ℝ; graph f ≔ {(x, f(x)) : x ∈ D} ⊆ ℝ² (`@fd2:def-cartesian-product`); equal iff same domain and same values.
- **`exm-first-real-functions`.** Constants, identity, |x|, 1/x on ℝ∖{0}, √x on [0, ∞) (`@fd3:prp-cof-square-roots`), restrictions (`@fd2:def-restriction-extension`), 𝟙_A (`@fd2:def-indicator`), a piecewise function glued from two (`@fd2:exm-piecewise-as-gluing`). Figure.
- **`prp-graph-vertical-line`.** G ⊆ ℝ² is the graph of a function on D iff each a ∈ D has exactly one y with (a, y) ∈ G and no (a, y) ∈ G has a ∉ D. Proof: unwind `@fd2:def-function`, three sentences.
- **Warning.** No natural domain: x²/x on ℝ∖{0} is the restriction of x on ℝ, not equal to it. The circle {x² + y² = 1} is a graph over no D: (0, 1), (0, −1).
- **Quick check 1.** Graph or not, over which D: {y = x²}; {x = y²}; {y ≥ 0, x = y²}? *Answer:* yes over ℝ; no, (1, 1) and (1, −1); yes over [0, ∞), the graph of √.
- **`def-function-algebra`.** f + g, fg, cf on D_f ∩ D_g; f/g off the zeros of g; max, min, |f|; g ∘ f on {x ∈ D_f : f(x) ∈ D_g}, which is fd2's composite of g with a restriction of f (`@fd2:def-composition`); associativity by `@fd2:prp-composition-associative`, both domains being {x : f(x) ∈ D_g, g(f(x)) ∈ D_h}.
- **Quick check 2.** Domain of √x + 1/x? Of the composite of √ with x ↦ x − 1? *Answer:* [0, ∞) ∩ (ℝ∖{0}) = (0, ∞); {x : x − 1 ∈ [0, ∞)} = [1, ∞).
- **`def-polynomial-rational-function`.** For p ∈ ℝ[x], the polynomial function of p (`@def-polynomial-evaluation`) restricted to D ⊆ ℝ. Three facts, **cited, not proved**: sums and products of polynomial functions are those of the sums and products of the polynomials (`@prp-polynomial-function-map` (b)); on an infinite D a polynomial function determines p (`@thm-polynomial-identity-from-values` (a), with n + 1 points of D), so its degree and leading coefficient are well defined; a non-zero p has at most deg p roots (`@thm-polynomial-root-count`). A rational function is p/q on {x ∈ ℝ : q(x) ≠ 0} with q ≠ 0, which omits at most deg q points. One sentence: Chapters 6–7 proved these over every field; ℝ is a field, and nothing new is needed.
- **Quick check 3.** Is |x| on [0, ∞) a polynomial function? Are (x² − 1)/(x − 1) and x + 1 the same function? *Answer:* yes, the restriction of the polynomial function of x; no, the domains differ (ℝ∖{1} and ℝ), though they agree on ℝ∖{1}.
- **`exm-method-graph-pairs`** `[Method: reading a graph as a set of pairs]`. To prove "graph g is graph f moved by M", show (x, y) ∈ graph g ⟺ M⁻¹(x, y) ∈ graph f by unwinding y = g(x). When: transformations, inverses (8.2), symmetry. Usual failure: moving the wrong way.
- **`[Scratch work]`** at `prp-graph-transformations` (a), kept apart from the proof. Givens/Goal table:

  | Givens | Goal |
  |---|---|
  | f: D → ℝ; g(x) = f(x − a) + b on D + a | (x, y) ∈ graph g ⟺ (x − a, y − b) ∈ graph f |

  Naive guess "x ↦ f(x − a) moves left" tested at f = |·|, a = 1: the vertex of |x − 1| is at x = 1, so right. Unwinding: (x, y) ∈ graph g ⟺ x − a ∈ D and y − b = f(x − a).
- **`prp-graph-transformations`.** f: D → ℝ, a, b ∈ ℝ, c > 0: (a) x ↦ f(x − a) + b on D + a has graph graph f + (a, b); (b) x ↦ f(−x) on −D: reflection in the y-axis; (c) −f: reflection in the x-axis; (d) cf: {(x, cy)}; x ↦ f(x/c) on cD: {(cx, y)}. Proof (a) in full, (b)–(d) one line each. Figure: |x| and |x − 1| − 2.
- **Quick check 4.** Which function on ℝ has graph (graph |·|) + (−1, 2)? *Answer:* x ↦ |x + 1| + 2, by (a) with a = −1, b = 2; vertex (−1, 2).
- **`def-even-odd-function`**, symmetric D; graph language by (b), (c).
- **`prp-even-odd-decomposition`.** Unique f = e + o; uniqueness: e − e′ = o′ − o is even and odd, so h(x) = h(−x) = −h(x), 2h(x) = 0.
- **Exercises.**
  - **A1.** Graph or not, over which D: (a) {x + y² = 0}; (b) {y = |x|}; (c) {x = 2}; (d) {xy = 1}. *Answers:* (a) no, (−1, ±1); (b) yes, ℝ; (c) no: (2, 0), (2, 1); (d) yes, ℝ∖{0}, the function 1/x.
  - **A2** `[Is this legal? Is it useful?]` f(x) = x − 1 on ℝ, g(y) = 1/y on ℝ∖{0}: domains of g ∘ f and f ∘ g; equal? *Answer:* ℝ∖{1}; ℝ∖{0}; no: domains differ, and g(f(2)) = 1, f(g(2)) = −1/2.
  - **B1.** max(f, g) = (f + g + |f − g|)/2, min(f, g) = (f + g − |f − g|)/2. *Answer:* case f(x) ≥ g(x): |f(x) − g(x)| = f(x) − g(x), giving f(x) and g(x); other case symmetric (`@fd3:def-absolute-value-ordered-field`).
  - **B2.** Graph of 2|x − 1| − 3 from |·|. *Answer:* scale vertically by 2, right 1, down 3; vertex (1, −3); zeros where |x − 1| = 3/2: x = −1/2, 5/2.
  - **B3.** Even and odd parts of 1/(1 − x) on ℝ∖{−1, 1}. *Answer:* e = 1/(1 − x²), o = x/(1 − x²), from 1/(1 − x) ± 1/(1 + x) = 2/(1 − x²), 2x/(1 − x²).
  - **B4** `[Prove or disprove]` (a) product of two odd functions on D is even; (b) a function both even and odd is 0; (c) the composite of two odd f, g: ℝ → ℝ is odd; (d) the sum of an even and an odd function on ℝ is never even. *Answers:* (a) true, (−f(x))(−g(x)); (b) true, the uniqueness argument of `prp-even-odd-decomposition`; (c) true, f(g(−x)) = f(−g(x)) = −f(g(x)); (d) false: x² + 0, and 0 is odd.
  - **C1** `[used later]` f: ℝ → ℝ with f(x + y) = f(x) + f(y): prove f(0) = 0, f(−x) = −f(x), f(nx) = nf(x) (n ∈ ℤ), f(q) = cq for q ∈ ℚ, c ≔ f(1). Hints: "x = y = 0"; "for q = m/n compute n·f(qx) two ways". *Answer:* f(0) = 2f(0); f(x) + f(−x) = f(0); induction on n ≥ 0 (`@fd1:ax-induction`), oddness for n < 0; n f(qx) = f(nqx) = f(mx) = m f(x), take x = 1.

## 8.2 `02-monotone-functions-and-inverses.md` — Monotone Functions and Inverse Functions

Budget: 3,800 main-line words; fold ≤ 300. **Full-level method section.**

- **Hook.** "1/x is decreasing": on ℝ∖{0}, −1 < 1 but 1/(−1) < 1/1. Decreasing on each half, not on the union; the definition must name the set.
- **`def-monotone-function`.** On A ⊆ D: increasing, strictly increasing, decreasing, strictly decreasing, monotone; quantifiers in symbols. Constants are increasing and decreasing. Recall: fd2 already met "strictly increasing" for maps between subsets of ℝ (`@fd2:prp-strictly-monotone-injective`) and the definition agrees.
- **Quick check 1.** Is a constant increasing? 1/x decreasing on ℝ∖{0}? 𝟙_{[0, ∞)} increasing? *Answer:* yes and decreasing, not strictly; no (hook); yes, not strictly.
- **`exm-method-factor-difference`** `[Method: factor out y − x]`. Fix x < y in A; write f(y) − f(x) = (y − x)·Q(x, y); show Q > 0 (≥ 0, < 0). Differences of powers: yⁿ − xⁿ = (y − x)Σ_{j<n} x^j y^{n−1−j} (`@fd2:prp-geometric-sum`). Failures: concluding strict from Q ≥ 0; using a sign valid on part of A only (split A first). **Givens/Goal table:**

  | Givens | Goal |
  |---|---|
  | x, y ∈ A, x < y; the formula for f | f(x) < f(y), i.e. f(y) − f(x) > 0 |
- **`exm-mobius-increasing`** (worked example 1, with `[Scratch work]`). g(x) = (x − 1)/(x + 2) on (−2, ∞) is strictly increasing. Scratch work: "the numerator increases, so the quotient does" fails, since the denominator increases too; subtract over a common denominator: (y − 1)(x + 2) − (x − 1)(y + 2) = 3(y − x), so g(y) − g(x) = 3(y − x)/((x + 2)(y + 2)), Q = 3/((x + 2)(y + 2)) > 0 on (−2, ∞). Proof then written in four lines. (x³ is not redone: fd2 proved it strictly increasing, `@fd2:exm-maps-from-calculus` (a).)
- **`exm-squash-function`** (worked example 2). σ(x) = x/(1 + |x|) strictly increasing on ℝ with image (−1, 1). Split A: 0 ≤ x < y: (y − x)/((1 + x)(1 + y)); x < y ≤ 0: (y − x)/((1 − x)(1 − y)); x < 0 ≤ y: σ(x) < 0 ≤ σ(y). Image: |σ| < 1; v ∈ [0, 1) from x = v/(1 − v), v ∈ (−1, 0) from x = v/(1 + v). Sidecar checks both formulas.
- **`prp-monotone-algebra`.** (a) sums (strict if one strict); (b) c ≥ 0 keeps, −f reverses; (c) f, g increasing and ≥ 0 ⇒ fg increasing; (d) f increasing, > 0 ⇒ 1/f decreasing; (e) composites: inc∘inc, dec∘dec increasing, mixed decreasing, strict if both strict. One line each (`@fd3:prp-ordered-ring-rules`, `@fd3:prp-ordered-field-halves` (d), `@fd3:prp-reciprocal-order`). Warning after (c): without ≥ 0, x·x = x² fails at −1 < 0.
- **Quick check 2.** On [0, ∞), x and x² + 1 are increasing and ≥ 0. Is x(x² + 1) increasing there, and by which rule? *Answer:* yes, (c).
- **`prp-strictly-monotone-order-reflecting`.** f strictly increasing on A ⇒ for x, y ∈ A: x < y ⟺ f(x) < f(y), and x ≤ y ⟺ f(x) ≤ f(y). Injectivity is cited (`@fd2:prp-strictly-monotone-injective`); the new half is (⇐) by trichotomy (`@fd3:prp-ordered-field-halves` (a)): if x ≥ y then f(x) ≥ f(y).
- **Quick check 3.** Which half of `prp-strictly-monotone-order-reflecting` uses trichotomy, and how? *Answer:* (⇐): if not x < y, then x ≥ y, so f(x) ≥ f(y), against f(x) < f(y).
- **`exm-injective-not-monotone`.** f(0) = 1, f(1) = 0, f(x) = x otherwise: injective, f(0) > f(1), f(1) < f(2). Also 1/x on ℝ∖{0}. (The AN1 fact goes to the section's Looking-ahead box.)
- **`thm-monotone-inverse`** (key proof; try it first, ten minutes: "why should f⁻¹ be increasing?"). f: A → ℝ strictly increasing ⇒ f: A → f(A) is a bijection, f⁻¹: f(A) → A is strictly increasing, graph f⁻¹ = {(y, x) : (x, y) ∈ graph f}. Same for decreasing. Proof: surjective onto f(A) by `@fd2:def-image`, injective by `@fd2:prp-strictly-monotone-injective`, inverse by `@fd2:thm-bijection-iff-inverse`; for u < v in f(A), u = f(x), v = f(y), and x < y by `prp-strictly-monotone-order-reflecting`; graph by the method of 8.1. Self-explanation: "where is totality of ≤ used?" (in the order-reflecting step: not x < y means x ≥ y only in a total order).
- **Quick check 4.** Inverse of g of `exm-mobius-increasing`, and its domain? *Answer:* g = 1 − 3/(x + 2) takes exactly the values in (−∞, 1); g⁻¹(v) = (1 + 2v)/(1 − v) on (−∞, 1) (check g(g⁻¹(v)) = v; sidecar).
- **`exm-odd-roots`.** By `@lem-reals-nth-root` (a), (b), x ↦ xⁿ is strictly increasing on [0, ∞) with image [0, ∞), and ⁿ√ is its inverse, strictly increasing by `thm-monotone-inverse`. For odd n, xⁿ is strictly increasing on ℝ ((−x)ⁿ = −xⁿ, the halves meet at 0) with image ℝ, so ⁿ√y exists for all real y, ⁿ√(−y) = −ⁿ√y (agrees with the NOTATION row). Figure.
- **`exm-strange-jump`** (first appearance). H(x) = x for x < 0, x + 1 for x ≥ 0: strictly increasing, image (−∞, 0) ∪ [1, ∞), not an interval; H⁻¹ exists on the image. Figure.
- **`[Looking ahead]`** (the section's one pointer): *Analysis on the Real Line* proves that a continuous injective function on an interval is strictly monotone, which H and `exm-injective-not-monotone` show needs both words.
- **Exercises.**
  - **A1** (key proof comprehension, `thm-monotone-inverse`). (a) Run it on x² on [0, 2]: f(A) = [0, 4], f⁻¹ = √ on [0, 4]; (b) which cited result gives injectivity? (`@fd2:prp-strictly-monotone-injective`); (c) the idea in two sentences.
  - **A2.** Classify: x² on [−1, 1] (neither); x² on [0, ∞) (strictly increasing); −x³ on ℝ (strictly decreasing: x³ strictly increasing by `@fd2:exm-maps-from-calculus` (a), then (b) of the rules); 1/x on (0, ∞) (strictly decreasing: 1/y − 1/x = −(y − x)/(xy)).
  - **B1.** x + 1/x strictly increasing on [1, ∞), strictly decreasing on (0, 1]. *Answer:* f(y) − f(x) = (y − x)(xy − 1)/(xy); xy > 1 for 1 ≤ x < y, 0 < xy < 1 for 0 < x < y ≤ 1.
  - **B2** `[Prove or disprove]` (a) composite of two strictly decreasing functions ℝ → ℝ is strictly increasing; (b) f strictly increasing and > 0 ⇒ 1/f strictly decreasing; (c) the sum of a strictly increasing and a strictly decreasing function on ℝ is monotone; (d) x ↦ x³ − x is strictly increasing on [1/2, ∞). *Answers:* (a) true, rule (e); (b) true; (c) false: x³ + (−x) has values 0, 3/8, 0 at −1, −1/2, 0; (d) false: the method gives f(y) − f(x) = (y − x)(x² + xy + y² − 1), and the bracket is 0.25 + 0.3 + 0.36 − 1 < 0 at x = 1/2, y = 3/5; indeed f(1/2) = −3/8 = −375/1000 > −384/1000 = −48/125 = f(3/5) (sidecar). Repair: on [1, ∞) the bracket is > 3 − 1 > 0, so true there.
  - **B3.** f(x) = x|x| on ℝ is a strictly increasing bijection; find f⁻¹. *Answer:* 0 ≤ x < y: y² − x² > 0; x < y ≤ 0: f(y) − f(x) = x² − y² = (x − y)(x + y) > 0 (both factors negative); x < 0 ≤ y: f(x) < 0 ≤ f(y). Image: v ≥ 0 from √v, v < 0 from −√(−v). f⁻¹(v) = √v for v ≥ 0, −√(−v) for v < 0.
  - **C1** `[Find the error]` (true conclusion). "x³ − 3x strictly increasing on [1, ∞): (i) 1 ≤ x < y; (ii) f(y) − f(x) = (y − x)(y² + xy + x² − 3); (iii) x, y ≥ 1 give y² + xy + x² ≥ 3; (iv) y − x > 0, so f(y) − f(x) > 0." *Answer:* (iv) fails: (iii) gives only ≥ 0, and positive × nonnegative is ≥ 0 (1·0 = 0). Repair: y > 1, so y² > 1 and the bracket is > 0.
  - **C2** `[used later]` f: ℝ → ℝ increasing with f(f(x)) = x for all x ⇒ f = id. Hints: "split by the sign of f(x) − x"; "apply f to f(x) > x". *Answer:* f(x) > x gives x = f(f(x)) ≥ f(x) > x; f(x) < x symmetric. Without "increasing" it fails: x ↦ −x is an involution other than id. (8.6 J recalls this item backward; no pointer here.)

## 8.3 `03-bounds-and-suprema.md` — Bounded Functions and Their Suprema

Budget: 4,200 main-line words; fold ≤ 400 (`prp-iterated-sup`). **Full-level method section.** Frame recalls `@fd3:def-complete-ordered-field`, `@fd2:def-order-supremum`.

- **Hook.** x/(1 + x) on [0, ∞) stays below 1, creeps toward it, never reaches it. "Its maximum is 1" is false; "its least upper bound is 1" is true, and needs two halves.
- **`prp-real-infimum`.** Non-empty A bounded below has inf A = −sup(−A) (`@fd2:exm-sets-of-numbers-as-images`). Proof: lower bounds of A are the negatives of upper bounds of −A.
- **`prp-real-sup-approximation`.** For an upper bound s of non-empty A: s = sup A iff ∀ε > 0 ∃a ∈ A, a > s − ε. Mirror for inf. Proof: (⇒) s − ε is not an upper bound; (⇐) an upper bound u < s and ε ≔ s − u give a > u, a contradiction.
- **Quick check 1.** Is 0.99 the supremum of [0, 1)? *Answer:* no: it is not even an upper bound (0.995 ∈ [0, 1)); the ε-test applies only to upper bounds.
- **`def-bounded-function`**, **`def-sup-of-function`** (sup_A f ≔ sup f(A); attained iff sup_A f ∈ f(A), then = max).
- **`exm-method-sup-two-halves`** `[Method: bound every value, then find a witness]`. (≤) f(x) ≤ M for all x ∈ A; (≥) for each ε > 0 an x ∈ A with f(x) > M − ε. Failures: only (≤); a witness for one ε; mixing witnesses of two functions (B4). **Givens/Goal table:**

  | Givens | Goal |
  |---|---|
  | f on A; candidate M | (≤) ∀x ∈ A f(x) ≤ M; (≥) ∀ε > 0 ∃x ∈ A f(x) > M − ε |
- **`exm-sup-not-attained`** (worked example 1, `[Scratch work]`). sup_{[0, ∞)} x/(1 + x) = 1, not attained. Scratch: solve x/(1 + x) > 1 − ε backwards for 0 < ε < 1: x > (1 − ε)/ε, so x ≔ 1/ε works. Proof: x/(1 + x) < 1; for every ε > 0, x ≔ 1/ε gives x/(1 + x) = 1/(1 + ε) > 1 − ε, as (1 − ε)(1 + ε) = 1 − ε² < 1 (no case split; the scratch work's restriction ε < 1 was only for solving backwards). inf = 0, attained.
- **Quick check 2.** For ε = 2, which x does the proof take, and does it beat 1 − ε? *Answer:* x = 1/2, value 1/3 > −1.
- **`exm-sup-attained-parabola`** (worked example 2). sup_{[0, 1]} x(1 − x) = 1/4 = 1/4 − (x − 1/2)² at 1/2; an attained value is its own witness.
- **Quick check 3.** sup, inf of x² on (−1, 2); of 𝟙_ℚ on [0, 1]. *Answer:* 4 not attained, 0 attained; 1 at any rational and 0 at any irrational of [0, 1], e.g. √2/2 (if √2/2 = q ∈ ℚ then √2 = 2q ∈ ℚ, against `@fd3:thm-no-rational-square-two` transported to ℝ by `@fd3:thm-rationals-embed-ordered-field`), so both are attained.
- **`thm-sup-function-rules`.** Let A ≠ ∅ and f, g: A → ℝ be bounded above on A. (a) f ≤ g ⇒ sup f ≤ sup g; (b) sup(f + g) ≤ sup f + sup g; (c) sup(f + c) = sup f + c; (d) c ≥ 0: sup(cf) = c sup f; (e) if f is bounded below on A (A ≠ ∅ as above), then −f is bounded above and sup(−f) = −inf f; (f) B ⊆ A non-empty: sup_B f ≤ sup_A f; (g) if f, g are bounded (above and below) on the non-empty A, then |sup f − sup g| ≤ sup|f − g|. (a), (b), (f) by the first half; (c), (d) both halves, (d) with c = 0 apart; (e) by `prp-real-infimum`; (g) from f ≤ g + sup|f − g|, (a), (c), symmetry. Faded triple, full: (b), (d) written with both halves named. Warning: (b) can be strict (x, 1 − x on [0, 1]: 1 < 2).
- **Quick check 4.** Which half of the method does (f) need? *Answer:* only (≤): every value of f on B is a value on A, so sup_A f bounds f(B).
- **`prp-sup-oscillation`** (key proof; try it first, ten minutes: "which two points make |f(x) − f(y)| almost sup f − inf f?"). Let A ≠ ∅ and f: A → ℝ be bounded (above and below). Then sup{|f(x) − f(y)| : x, y ∈ A} = sup_A f − inf_A f. Idea: a maximizer and minimizer may not exist; take near ones within ε/2. Proof: (≤) f(x) − f(y) ≤ sup − inf both ways, `@fd3:prp-absolute-value-ordered-field` (d); (≥) witnesses by `prp-real-sup-approximation`. Self-explanation "why ε/2?"
- **`exm-polynomial-unbounded`.** A polynomial function of degree d ≥ 1 is unbounded on ℝ, and all its roots lie in (−R, R), R as in `@lem-complex-polynomial-growth`. Proof: regard p ∈ ℝ[x] in ℂ[x] (`@prp-reals-embed-complex`); for real |x| ≥ R the lemma gives |p(x)| ≥ ½|a_d||x| > 0 (modulus = absolute value, `@prp-modulus-of-real`); given M, x ≔ R + 2M/|a_d| gives |p(x)| ≥ ½|a_d|x > M. Remark: odd degree gives a real root (`@cor-real-odd-degree-root`, Chapter 7), not by signs alone. Statement only of what the lemma gives; no new bound.
- **Quick check 5.** Is x³ − 100x bounded on [−20, 20]? On ℝ? *Answer:* yes, |x³ − 100x| ≤ 8000 + 2000; no, `exm-polynomial-unbounded`.
- **`prp-iterated-sup`** (fold `title="Suprema over a product"`). For A, B non-empty and f: A × B → ℝ bounded above: sup_{A×B} f = sup_a sup_b f = sup_b sup_a f. Proof: each inner sup ≤ S; each f(a, b) ≤ sup_a sup_b f. (Later users are listed only in "What later chapters cite".)
- **`[Looking ahead]`** (the section's one pointer): *Analysis on the Real Line* calls sup f − inf f on a set the oscillation of f there, and measures integrability with it.
- **Exercises.**
  - **A1** (key proof comprehension, `prp-sup-oscillation`). (a) x² on [−1, 2): sup 4 (not attained), inf 0, so the sup of |f(x) − f(y)| is 4, not attained (needs f(x) = 4, x = ±2 ∉ A); (b) which line uses "bounded below"? (the choice of y near inf f, which exists by `prp-real-infimum`); (c) the idea in two sentences.
  - **A2.** True or false: (a) sup_A f ∈ f(A); (b) inf_A f ≤ sup_A f; (c) sup_A |f| = max(|sup_A f|, |inf_A f|) for bounded f. *Answers:* false (`exm-sup-not-attained`); true (any x ∈ A); true: inf ≤ f(x) ≤ sup gives |f(x)| ≤ the max, and witnesses near sup or near inf give the other half.
  - **B1** (faded, last step blank). inf_A(f + g) ≥ inf_A f + inf_A g. Given: "for each x, f(x) + g(x) ≥ inf f + inf g." *Answer:* bound every value: so inf f + inf g is a lower bound of (f + g)(A), and the infimum is the greatest one.
  - **B2** `[Prove or disprove]` (a) sup(f + g) = sup f + sup g; (b) sup max(f, g) = max(sup f, sup g); (c) f, g > 0 ⇒ sup fg = sup f · sup g; (d) sup f = −inf(−f). *Answers:* false (x, 1 − x on [0, 1]); true (≤ termwise; ≥ by rule (a) from f, g ≤ max(f, g)); false (x, 1 − x on (0, 1): 1/4 vs 1); true (rule (e) applied to −f).
  - **B3.** sup and inf of x/(x² + 1) on ℝ. *Answer:* 1/2 at 1, −1/2 at −1: 1/2 − x/(x² + 1) = (x − 1)²/(2(x² + 1)) ≥ 0 and the mirror (sidecar).
  - **B4** `[Find the error]` (false conclusion). "sup(f + g) = sup f + sup g: ≤ is (b); for ≥ pick x with f(x) > sup f − ε/2, y with g(y) > sup g − ε/2; then f(x) + g(y) > sup f + sup g − ε." *Answer:* conclusion false (B2 (a)); the last line: f(x) + g(y) with x ≠ y is not a value of f + g. x, 1 − x on [0, 1], x = 1, y = 0: 2 ∉ {1}.
  - **C1** (exit check). f ≥ 0 bounded on A: sup f² = (sup f)². *Answer:* s ≔ sup f. (≤) 0 ≤ f(x) ≤ s ⇒ f(x)² ≤ s² (`@fd3:prp-ordered-field-halves` (d)). (≥) s = 0 ⇒ f = 0. s > 0: witness f(x) > s − ε/(2s); if s − ε/(2s) ≥ 0, f(x)² > s² − ε + ε²/(4s²) > s² − ε; otherwise s² < ε/2 and f(x)² ≥ 0 > s² − ε. Marking (10): 2 both halves as goal; 3 upper half with nonnegativity named; 3 witness chosen from ε before use; 2 cases s = 0 and s − ε/(2s) < 0. Fatal: squaring an inequality between possibly negative numbers; witness independent of ε.
  - **C2** (faded, last half blank). |f(x) − f(y)| ≤ L|x − y| on [a, b] ⇒ f bounded and sup − inf ≤ L(b − a). Given: "by `prp-sup-oscillation` it suffices to bound |f(x) − f(y)|." *Answer:* |f(x)| ≤ |f(a)| + L(b − a); each |f(x) − f(y)| ≤ L(b − a), an upper bound of the set, so its sup is at most L(b − a).

## 8.4 `04-floor-and-step-functions.md` — Floor, Distance to the Integers, and Step Functions

Budget: 3,400 main-line words; fold ≤ 200. Idea-level method section.

- **Hook.** fd3 gave every element of an Archimedean field an integer part, and Chapter 2 cited the integer part of a rational (`@fd3:prp-rational-integer-part`); here the same integer part becomes a function on all of ℝ: ⌊x⌋ is the book's first function that jumps, and the tool behind counting and the strange functions of 8.6.
- **`def-floor-ceiling`.** ℝ is Archimedean (`@fd3:thm-reals-complete-ordered-field`, `@fd3:thm-cof-complete-archimedean`), so `@fd3:prp-integer-part-ordered-field` gives the unique m ∈ ℤ with m ≤ x < m + 1: ⌊x⌋ ≔ m; ⌈x⌉ ≔ −⌊−x⌋; fractional part x − ⌊x⌋ ∈ [0, 1). fd2's `@fd2:exm-maps-from-calculus` (b) used it as a school fact; now it is proved. Figure.
- **`exm-method-floor-inequality`** `[Method: pin the floor by its inequality]`. Show m ∈ ℤ and m ≤ A < m + 1; or "∀j ∈ ℤ: j ≤ A ⟺ j ≤ m" (rule (g)). Failure: "drop the decimals" (⌊−2.5⌋ = −3). **Givens/Goal table:**

  | Givens | Goal |
  |---|---|
  | an expression A; a candidate integer m | m ≤ A < m + 1 (first form), or ∀j ∈ ℤ: j ≤ A ⟺ j ≤ m (second form) |
- **`prp-floor-rules`.** (a) x − 1 < ⌊x⌋ ≤ x, equality iff x ∈ ℤ; (b) ⌊x + n⌋ = ⌊x⌋ + n; (c) increasing; (d) ⌊x⌋ + ⌊y⌋ ≤ ⌊x + y⌋ ≤ ⌊x⌋ + ⌊y⌋ + 1; (e) ⌊−x⌋ = −⌊x⌋ for x ∈ ℤ, −⌊x⌋ − 1 otherwise; (f) ⌈x⌉ is the unique m with m − 1 < x ≤ m; (g) j ≤ x ⟺ j ≤ ⌊x⌋ for j ∈ ℤ; (h) ⌊⌊x⌋/k⌋ = ⌊x/k⌋, k ∈ ℤ_{>0}. Proofs: (a), (b), (d)–(f) by the method's first form; (g) by discreteness `@fd3:thm-integers-ordered-ring` (c); (c) from (g); (h) worked in full by the second form (`[Scratch work]` here: trying the first form stalls on bounding ⌊x⌋/k; the second form turns it into a chain of ⟺).
- **Quick check 1.** ⌊−7/2⌋, ⌈−7/2⌉, ⌊7/2⌋ + ⌊−7/2⌋. *Answer:* −4, −3, −1.
- **Quick check 2.** Compute ⌊⌊7.5⌋/2⌋ and ⌊7.5/2⌋. *Answer:* ⌊7/2⌋ = 3 and ⌊3.75⌋ = 3, as (h) says.
- **`def-distance-to-integer`**, **`prp-distance-to-integer`.** (a) dist(x, ℤ) = min{|x − n| : n ∈ ℤ}, attained at ⌊x⌋ or ⌊x⌋ + 1; (b) 0 ≤ dist ≤ 1/2, = 0 iff x ∈ ℤ, = 1/2 iff x − 1/2 ∈ ℤ; (c) period 1, even; (d) dist(x, ℤ) ≤ |x|, subadditive, |dist(x, ℤ) − dist(y, ℤ)| ≤ |x − y|. Proofs from (a) and the floor rules. Figure: the tent.
- **`def-periodic-function`.** Periods form a set closed under negation and under sums that are non-zero; x − ⌊x⌋ and dist(·, ℤ) have period 1.
- **Quick check 3.** Is 1/2 a period of dist(·, ℤ)? *Answer:* no: dist(0, ℤ) = 0, dist(1/2, ℤ) = 1/2.
- **`def-step-function`.** φ: [a, b] → ℝ constant on each open piece of a finite partition; values at the points arbitrary. Example ⌊x⌋ on [a, b] (finitely many integers, `@fd2:def-finite`). Non-example: x on [0, 1].
- **Quick check 4.** Step functions on [0, 1] or not: 𝟙_{[0, 1/2]}; the indicator of {1/n : n ∈ ℤ_{>0}}? *Answer:* yes, partition 0, 1/2, 1 (the value at 1/2 is free); no: the first open piece (0, x₁) contains some 1/n (`@fd3:prp-archimedean-reciprocal`), where the value is 1, and the point between 1/(n + 1) and 1/n, where it is 0.
- **`prp-step-function-algebra`.** φ + ψ, φψ, cφ, max(φ, ψ), |φ| are step functions: merge the two finite partitions (`@fd2:prp-subset-finite`, listing by `@fd2:prp-finite-max`; detail folded).
- **`[Looking ahead]`** (the section's one pointer): *Analysis on the Real Line* builds a function that is continuous everywhere and differentiable nowhere from the tents dist(2ᵏx, ℤ)/2ᵏ.
- **Exercises.**
  - **A1.** ⌊−0.01⌋, ⌈2⌉, ⌊2.999⌋ + ⌈−2.999⌉, dist(−2.7, ℤ), dist(13/4, ℤ). *Answers:* −1; 2; 0; 0.3; 1/4.
  - **A2.** True or false for all real x, y: (a) ⌊2x⌋ = 2⌊x⌋; (b) ⌊x⌋⌊y⌋ ≤ ⌊xy⌋; (c) dist(2x, ℤ) ≤ 2 dist(x, ℤ). *Answers:* false (x = 1/2); false (x = y = −1/2: 1 > 0); true ((d) with y = x).
  - **B1** `[Prove or disprove]` (a) ⌊2x⌋ = ⌊x⌋ + ⌊x + 1/2⌋; (b) ⌈x⌉ − ⌊x⌋ = 1; (c) ⌊√⌊x⌋⌋ = ⌊√x⌋ for x ≥ 0; (d) ⌊x⌋ + ⌊−x⌋ = 0. *Answers:* (a) true: m = ⌊x⌋, t = x − m, cases t < 1/2 and t ≥ 1/2; (b) false for x ∈ ℤ; (c) true: for j ∈ ℕ, j ≤ √⌊x⌋ ⟺ j² ≤ ⌊x⌋ ⟺ j² ≤ x ⟺ j ≤ √x (rule (g), `@lem-reals-nth-root` (a) with n = 2), negative j lie below both; then the second form; (d) false: x = 1/2.
  - **B2.** The number of multiples of k in {1, …, N} is ⌊N/k⌋. *Answer:* jk ≤ N ⟺ j ≤ N/k ⟺ j ≤ ⌊N/k⌋; the multiples are k, …, ⌊N/k⌋k (`@fd2:cor-finite-size-unique`).
  - **B3.** φ(x) = ⌊2x⌋ − 2⌊x⌋ on [0, 2] is a step function. *Answer:* partition 0, 1/2, 1, 3/2, 2, values 0, 1, 0, 1 on the open pieces.
  - **C1.** (Hermite) Σ_{k=0}^{n−1} ⌊x + k/n⌋ = ⌊nx⌋. Hints: "compare x and x + 1/n"; "show the difference F has period 1/n and vanishes on [0, 1/n)". *Answer:* shifting by 1/n rotates the terms and turns the last into ⌊x⌋ + 1, while ⌊nx + 1⌋ = ⌊nx⌋ + 1; on [0, 1/n) both sides are 0; every x is y + j/n with j = ⌊nx⌋, y ∈ [0, 1/n).
  - **C2.** For n ∈ ℤ_{>0}: (a) dist(nx, ℤ) ≤ n dist(x, ℤ); (b) equality holds whenever dist(x, ℤ) ≤ 1/(2n); (c) find x with strict inequality for n = 2. Hint: "if |y − k| ≤ 1/2 for an integer k, then dist(y, ℤ) = |y − k|." *Answer:* (a) induction on n from subadditivity, `prp-distance-to-integer` (d); (b) hint from (a): |y − j| ≥ |j − k| − |y − k| ≥ 1 − 1/2 for j ≠ k; take k nearest to x, t ≔ x − k, |t| ≤ 1/(2n), so nx = nk + nt with |nt| ≤ 1/2 and dist(nx, ℤ) = n|t| = n dist(x, ℤ); (c) x = 1/2: 0 < 1 (A2 (c) was the inequality only; here the equality range is new).

## 8.5 `05-exponential-and-logarithm.md` — The Exponential, the Logarithm, and Real Powers

Budget: 4,500 main-line words; fold ≤ 300. Idea-level method section.

- **Hook.** Chapter 3 gave ⁿ√2, hence 2^{3/2} = (√2)³. What is 2^{√2}? Not a root, and "the limit of 2^q as q → √2" needs limits. The way through is exp, whose construction needs power series; we borrow exactly three facts, in one box, and derive the rest, including that those three already pin exp down.
- **`ax-exponential`** `[What This Volume Borrows about the Exponential]`. exp: ℝ → ℝ with (E1) exp(x + y) = exp x exp y; (E2) exp x ≥ 1 + x; (E3) every y > 0 is a value. **Assumed here, proved in AN1.10** (S3 names the volume and chapter as books.json gives them; same place as `@ax-cosine-sine`'s box, Open 2). As in Chapter 3's box: nothing above uses it; these three only; each use named. Three, not spec/08's four: uniqueness is proved.
- **Warning.** e^x is not notation until `prp-real-power-consistent`; continuity and exp′ = exp are true, not in the box, not used.
- **`prp-exp-first-consequences`.** (a) exp 0 = 1; (b) exp x > 0, exp(−x) = 1/exp x; (c) strictly increasing; (d) exp x ≤ 1/(1 − x) for x < 1; (e) exp(nx) = (exp x)ⁿ, n ∈ ℤ. Proofs: (a) exp 0 = (exp 0)² and exp 0 ≥ 1 (cancel, `@fd3:lem-field-fraction-rules` (d)); (b) exp x exp(−x) = 1, exp x = exp(x/2)² ≥ 0; (c) factor-out in multiplicative form: exp y = exp x exp(y − x) ≥ exp x (1 + y − x) > exp x; (d) exp(−x) ≥ 1 − x > 0, `@fd3:prp-reciprocal-order`; (e) induction and (b).
- **Quick check 1.** Which box facts does each use: exp 0 = 1; exp strictly increasing; log defined on all of (0, ∞)? *Answer:* (E1), (E2); (E1), (E2); (E3) with (c).
- **`exm-method-archimedes-squeeze`** `[Method: squeeze, then close the gap by Archimedes]`. To prove sup S = L: every s ≤ L, and for n ≥ N₀ some s_n ≥ L − C/n with C fixed in advance; then L′ < L is exceeded by `@fd3:prp-archimedean-reciprocal` with ε ≔ (L − L′)/C, which needs **C > 0**. Failure: C depending on n; C = 0 allowed. **Givens/Goal table:**

  | Givens | Goal |
  |---|---|
  | every s ∈ S has s ≤ L; for n ≥ N₀ some s_n ∈ S with s_n ≥ L − C/n, C > 0 fixed in advance | no L′ < L is an upper bound of S |
- **`thm-exp-unique`** (key proof). exp x = sup{(1 + x/n)ⁿ : n ∈ ℤ_{>0}, n > |x|}; hence any E with (E1), (E2) equals exp. `[Scratch work]` first: the naive (1 + x/n)ⁿ ≤ exp x is (E2) at x/n raised to the n-th power, legal only for 1 + x/n ≥ 0, which is why n > |x|; the upper estimate comes from (d) at x/n. Proof: n > |x|; exp x = exp(x/n)ⁿ ≥ (1 + x/n)ⁿ (`@lem-reals-nth-root` (a) for n-th powers on [0, ∞), (e)); exp x ≤ (1 − x/n)^{−n} by (d); (1 + x/n)ⁿ = (1 − x²/n²)ⁿ(1 − x/n)^{−n} ≥ (1 − x²/n²)ⁿ exp x ≥ (1 − x²/n) exp x ≥ exp x − (x² + 1) exp x / n (`@fd2:thm-bernoulli`, −x²/n² ≥ −1); method with C ≔ (x² + 1) exp x > 0, which also covers x = 0. Second sentence: the set and its sup were built from (E1), (E2) alone. Self-explanation: "why must n exceed |x|?" (both bases positive, to raise inequalities to the n-th power and to invert). Sidecar checks the two-sided bound numerically.
- **`def-euler-number`.** e ≔ exp 1; (1 + 1/n)ⁿ ≤ e ≤ (1 − 1/n)^{−n} for n ≥ 2.
- **`def-logarithm`.** exp: ℝ → (0, ∞) bijective ((b), (c), (E3)); log its inverse, strictly increasing (`thm-monotone-inverse`); graph reflected in y = x. Figure.
- **Quick check 2.** log(exp 2)? log(1/e)? *Answer:* 2; −1, since exp(−1) = 1/exp 1 = 1/e by (b) of `prp-exp-first-consequences`.
- **`prp-log-rules`.** (a) log 1 = 0, log e = 1; (b) log(xy) = log x + log y, log(1/x) = −log x; (c) 1 − 1/x ≤ log x ≤ x − 1, equality only at 1. Apply exp (injective); (c) from (E2) at log x and at log(1/x); strictness from exp t > 1 + t for t ≠ 0: t ≥ −2 gives exp t = exp(t/2)² ≥ (1 + t/2)² = 1 + t + t²/4; t < −2 gives exp t > 0 > 1 + t.
- **`def-real-power`.** a > 0, x ∈ ℝ: a^x ≔ exp(x log a); 0^x ≔ 0 for x > 0; no real powers of negative bases (odd roots are `exm-odd-roots`, a different symbol). So log(a^x) = x log a by definition.
- **Quick check 3.** Is 0^0 defined? Is (1/2)^{−1} = 2? *Answer:* no, base 0 only for x > 0; yes: exp(−log(1/2)) = exp(log 2) = 2 by `prp-log-rules` (b).
- **`prp-real-power-consistent`.** For a > 0, m ∈ ℤ, n ∈ ℤ_{>0}: a^{m/n} = ⁿ√(a^m) (Chapter 3's root; negative m as reciprocals); for n = 1 it is fd2's power (`@fd2:def-power`); e^x = exp x. Proof: (e) gives (a^{m/n})ⁿ = exp(m log a) = a^m, and a^{m/n} > 0, so uniqueness in `@lem-reals-nth-root` (b). If Chapter 1 defines a^q, this proposition says the two agree (reconciliation table).
- **Quick check 4.** Is 4^{1/2} = 2 by `prp-real-power-consistent`? *Answer:* yes: 4^{1/2} = √(4¹), the positive square root, which is 2 since 2 > 0 and 2² = 4.
- **`prp-real-power-laws`.** a^{x+y} = a^x a^y; (a^x)^y = a^{xy}; (ab)^x = a^x b^x; a^{−x} = 1/a^x; a^x > 0; monotone in x (a > 1 increasing, a < 1 decreasing) and in a (x > 0 increasing, x < 0 decreasing). One line each from (E1), `prp-log-rules`, `prp-monotone-algebra` (e).
- **`prp-exp-beats-powers`.** (a) For x > 0, k ∈ ℕ: exp x > (x/(k + 1))^{k+1}; so exp x > M x^k for x > M(k + 1)^{k+1}. (b) log x < m x^{1/m} for x > 0, m ∈ ℤ_{>0}; so log x < εx for x > 4/ε². Proofs: (a) exp(x/(k + 1))^{k+1} ≥ (1 + x/(k + 1))^{k+1}; (b) log x = m log(x^{1/m}) ≤ m(x^{1/m} − 1); m = 2 and 2√x ≤ εx ⟺ x ≥ 4/ε².
- **Quick check 5.** Is 2^{√2} > 2? Is (√2)^{√2} < 2? *Answer:* yes, x ↦ 2^x is increasing and √2 > 1; yes: (√2)^{√2} = 2^{√2/2} < 2^1 since √2/2 < 1.
- **Exercises.**
  - **A1** (key proof comprehension, `thm-exp-unique`). (a) Which box facts are used? ((E1), (E2) only); (b) where Bernoulli enters, with which x (−x²/n²); (c) bounds at x = 1, n = 2: 9/4 ≤ e ≤ 4; (d) the failing step for x = −3, n = 2 (1 + x/n = −1/2 < 0: the n-th power step is illegal).
  - **A2.** True or false: (a) exp(2x) = (exp x)²; (b) log(x + y) = log x + log y; (c) (−8)^{1/3} is defined by `def-real-power`; (d) a^x b^y = (ab)^{x+y}. *Answers:* true, (E1); false: x = y = 1 gives log 2 = 0, but log 2 > log 1; false (∛(−8) = −2 is `exm-odd-roots`); false: a = 1, b = 2, x = 1, y = 0 gives 1 vs 2.
  - **B1.** 2.5 < e < 3. *Answer:* n = 6: e ≥ (7/6)⁶ = 117649/46656 > 2.5 (117649 > 116640); e ≤ (6/5)⁶ = 46656/15625 < 3 (46656 < 46875). Sidecar.
  - **B2** `[Prove or disprove]` (a) exp x ≥ 1 + x + x²/2 for x ≥ 0; (b) log x ≤ x/e; (c) a ≤ b ⇒ a^x ≤ b^x for all x; (d) exp is a polynomial function. *Answers:* (a) true: (1 + x/n)ⁿ ≥ 1 + x + (1 − 1/n)x²/2 by `@thm-binomial-commutative-ring` (terms ≥ 0), then `thm-exp-unique` and Archimedes; (b) true: log x = 1 + log(x/e) ≤ x/e by (c) of the log rules; (c) false: x = −1, a = 1, b = 2; (d) false: for x ≥ 1, |p(x)| ≤ (S + |a_d|)x^d (S the sum of the other |a_i|), against `prp-exp-beats-powers` (a) with k = d, M = S + |a_d| + 1.
  - **B3** (proof ordering, `thm-exp-unique`, the lower bound). Lines: (i) fix x and n > |x|; (ii) 1 + x/n > 0 and 1 − x/n > 0; (iii) by (d), exp(x/n) ≤ 1/(1 − x/n), so exp x ≤ (1 − x/n)^{−n}; (iv) (1 + x/n)ⁿ = (1 − x²/n²)ⁿ (1 − x/n)^{−n}; (v) so (1 + x/n)ⁿ ≥ (1 − x²/n²)ⁿ exp x; (vi) Bernoulli with −x²/n² ≥ −1 gives (1 − x²/n²)ⁿ ≥ 1 − x²/n; (vii) hence (1 + x/n)ⁿ ≥ exp x − x² exp x / n. Distractors: (D1) "by (E2), exp x ≥ 1 + x, so (1 + x/n)ⁿ ≥ 1 + x" (true but irrelevant: it bounds the wrong quantity); (D2) "Bernoulli with x²/n² gives (1 − x²/n²)ⁿ ≥ 1 + x²/n" (wrong sign). *Answer:* a partial order, every linear extension accepted: (i) < (ii) < {(iii), (iv), (vi)} in any order among themselves ((iv) is an identity needing only (ii); (vi) needs only (i)); (v) after (iii) and (iv); (vii) after (v) and (vi). One valid order: (i)(ii)(iii)(iv)(v)(vi)(vii).
  - **C1** `[Find the error]` (true conclusion). "exp strictly increasing: for x < y, exp y − exp x = exp(y − x) ≥ 1 + (y − x) > 0." *Answer:* conclusion true ((c)); the first equality is false: (E1) gives the quotient exp y/exp x = exp(y − x), not the difference (x = 0, y = 1: e − 1 vs e).
  - **C2** (exit check). For every ε > 0 there is X with log x < εx for all x > X; then the same with ε x^{1/m}. *Answer:* first part as `prp-exp-beats-powers` (b), X = 4/ε²; second: y = x^{1/m}, log x = m log y < m(ε/m)y for y > Y = 4m²/ε², i.e. for x > Y^m (monotonicity, `prp-real-power-laws`). Marking (10): 3 a bound log x ≤ c√x with the box fact named; 3 explicit X(ε); 2 substitution with monotonicity justified; 2 quantifier order ε, X, x. Fatal: X depending on x; derivatives or l'Hôpital.

## 8.6 `06-strange-functions.md` — A Table of Strange Functions

Budget: 2,800 main-line words; fold ≤ 0. Terse, one Idea. Last section: R group.

- **Hook.** Continuity, limit and integral will be tested on functions that resist drawing; we collect them, prove what needs no limits, and record the questions.
- **`lem-irrationals-dense`.** a < b ⇒ an irrational x ∈ (a, b): rational q in (a − √2, b − √2) (`@fd3:thm-rationals-dense-ordered-field`), x ≔ q + √2; rational x would make √2 rational (`@fd3:thm-no-rational-square-two`, transported by `@fd3:thm-rationals-embed-ordered-field`). Opens with: fd3 asked this as an exercise (`@fd3:exr-rationals-inside-the-reals-c2`); we record it as a lemma because 8.6 cites it. A recall, not a new move.
- **Quick check 1.** Why √2 and not 1/2 in the proof? *Answer:* q + 1/2 is rational.
- **`def-dirichlet-function`** D = 𝟙_ℚ. **`prp-dirichlet-properties`.** (a) the periods are exactly the non-zero rationals; (b) on every (a, b), sup D = 1, inf D = 0, both attained, so the oscillation is 1 (`prp-sup-oscillation`); (c) monotone on no (a, b).
- **x·D(x)** (table entry, inline): |xD(x)| ≤ |x|; near a ≠ 0 there are points with |xD(x) − aD(a)| ≥ |a|/2. Question: where is it continuous?
- **`def-thomae-function`.** T(p/q) = 1/q in lowest terms (`@prp-rationals-lowest-terms`, Chapter 2), T = 0 on irrationals, T(0) = 1. **`prp-thomae-large-values`.** (a) period 1; (b) {x ∈ [a, b] : T(x) ≥ ε} is finite; (c) every (a, b) has points with T > 0 and T = 0. Idea: T(x) ≥ ε forces q ≤ 1/ε, and for each q finitely many p. Proof of (b), for ε > 0: the set is contained in S_1 ∪ … ∪ S_Q, Q ≔ ⌊1/ε⌋, S_q ≔ {p/q : p ∈ ℤ, ⌈aq⌉ ≤ p ≤ ⌊bq⌋}; each S_q is finite, being in bijection with a finite integer interval by p ↦ p/q (`@fd2:def-finite`); a finite union of finite sets is finite (fd2's `@fd2:exr-finite-sets-b3`; the two-line induction is restated: A ∪ B is the disjoint union of A and B ∖ A, finite by `@fd2:prp-subset-finite` and `@fd2:prp-disjoint-union-count`); then `@fd2:prp-subset-finite`. The sets S_q overlap (1/2 = 2/4), which is why the union, not a count, is used.
- **Quick check 2.** T(3/4), T(−6/8), T(0.6), T(√2/2). *Answer:* 1/4, 1/4, 1/5, 0.
- **`exm-strange-involution`.** J(x) = x on ℚ, −x off ℚ: J ∘ J = id, a bijection (`@fd2:thm-bijection-iff-inverse`), monotone on no interval (rationals increase, irrationals decrease, `lem-irrationals-dense`); recalls 8.2 C2 backward: an involution need not be id once "increasing" is dropped.
- **`exm-strange-jump`** recalled (H).
- **`exm-strange-staircase`.** s(0) = 0, s(x) = 1/⌊1/x⌋ on (0, 1]. **`prp-staircase-squeeze`.** s increasing on [0, 1], infinitely many values, and 0 ≤ s(x) − x < 2x² for x ∈ (0, 1] (at x = 0 both sides are 0). Proof, for x ∈ (0, 1]: n = ⌊1/x⌋, x ≤ 1/n, s(x) − x < 1/(n(n + 1)) ≤ 2/(n + 1)² < 2x². Question: continuous at 0? differentiable there?
- **`exm-strange-zigzag`.** Z(0) = 0, Z(x) = dist(1/x, ℤ). **`prp-zigzag-all-values`.** ∀δ > 0 ∀t ∈ [0, 1/2] ∃x ∈ (0, δ) with Z(x) = t; |xZ(x)| ≤ |x|/2. Proof: n > 1/δ, x = 1/(n + t), `prp-distance-to-integer` (b), (c); |xZ(x)| ≤ |x|/2 by (b) of `prp-distance-to-integer` (dist ≤ 1/2). (The sine remark moves into the Looking-ahead box.)
- **`exm-strange-unbounded`** R(0) = 0, R = 1/x on (0, 1]; **`exm-strange-sup-missed`** M = x on [0, 1), M(1) = 0. Question: what hypothesis prevents both?
- **Quick check 3.** Is s a step function on [0, 1]? *Answer:* no: a step function with n pieces takes at most 2n + 1 values, s infinitely many.
- **`exm-strange-functions`** `[A Table of Strange Functions]`: function (label) | definition | proved here | question later. Rows D, x·D, T, J, H, s, Z and x·Z, R, M. No answers, no chapter names inside the table.
- **`[Looking ahead]`** (the section's one box): *Analysis on the Real Line* answers the continuity and extreme-value questions, the integration chapters the integrability ones, and replaces dist(1/x, ℤ) by the sine once it has one; and, checkably, no limit, continuity or derivative was used in this chapter.
- **Exercises.**
  - **A1.** sup, inf of D on (0, 1) and of T on [0, 1]; attained? *Answer:* 1, 0, both attained; T: sup 1 at 0 and 1, inf 0 at any irrational.
  - **A2.** Is x·D(x) bounded on [−5, 5]? Is it monotone on (0, 1)? *Answer:* yes, |xD(x)| ≤ 5; no: 1/2 < √2/2 < 3/4 (square: 1/4 < 1/2 < 9/16) with values 1/2, 0, 3/4, so it is neither increasing nor decreasing.
  - **B1.** All x ∈ [0, 1] with T(x) ≥ 1/4. *Answer:* 0, 1, 1/2, 1/3, 2/3, 1/4, 3/4.
  - **B2** `[Prove or disprove]` (a) D(x) + D(x + √2) ≤ 1; (b) J restricted to ℚ is increasing; (c) every bijection ℝ → ℝ is monotone on some interval; (d) T(x + 1) = T(x). *Answers:* true (not both rational); true (identity there); false (J); true ((a) of the proposition).
  - **B3.** s(0.4) and the squeeze there. *Answer:* n = 2, s = 1/2, s − x = 0.1 < 0.32.
  - **C1** (uses 8.1 C1). Additive and increasing f: ℝ → ℝ is f(x) = cx. Hints: "8.1 C1 gives f on ℚ; trap x between rationals"; "if f(x) > cx, take rational q > x with cq < f(x)". *Answer:* c = f(1) ≥ f(0) = 0; for c > 0 and f(x) > cx, a rational q ∈ (x, f(x)/c) gives f(q) = cq < f(x) though q > x; symmetric for f(x) < cx; c = 0: f(p) = 0 ≤ f(x) ≤ 0 = f(q). Closing line of the solution, no pointer: a non-linear additive function cannot be written down without the axiom of choice (ZF alone does not prove that one exists); this series builds none.
  - **C2.** An increasing f: [a, b] → ℝ is bounded and attains its sup and inf. *Answer:* f(a) ≤ f(x) ≤ f(b); contrast M.
  - **R. Review** (STYLE §11.5; texts do not name source chapters).
    - **R1** (one chapter back, Ch7). A polynomial function p on ℝ with p(x + 1) = p(x) for all x is constant. *Answer:* q ≔ p − p(0) vanishes at every n ∈ ℕ (induction); a non-zero q would have at most deg q roots (`@thm-polynomial-root-count`), but 0, 1, …, deg q are deg q + 1 of them; so q = 0.
    - **R2** (three chapters back, Ch5). The strictly increasing bijections ℝ → ℝ form a subgroup of the group of bijections of ℝ; do the strictly decreasing ones? *Answer:* `@exm-groups` (c), `@thm-subgroup-test`: id is in it, composites by `prp-monotone-algebra` (e), inverses by `thm-monotone-inverse` (image ℝ). Decreasing: no: id is not strictly decreasing, and the composite of two strictly decreasing maps is increasing (x ↦ −x twice gives id).
    - **R3** (spiral, fd3). (⌊nx⌋/n) converges to x. *Answer:* 0 ≤ x − ⌊nx⌋/n < 1/n (`prp-floor-rules` (a)), then `@fd3:prp-archimedean-reciprocal`, `@fd3:def-sequence-limit-ordered-field`.
    - **R4** (no hint). Is there a polynomial function p with p(x) = |x| on ℝ? *Answer:* no: p agrees with x at 0, 1, …, max(deg p, 1), so p is the polynomial x (`@thm-polynomial-identity-from-values` (a)); then p(−1) = −1 ≠ 1. Look-alikes that fail: growth (|x| grows like degree 1, no contradiction); "|x| is even, so p has even powers only" (needs the identity principle itself).

---

## What later chapters cite

| Later | Cites |
|---|---|
| Ch10 (F4.9 with F4.10) | `thm-monotone-inverse` (arg on a half-turn), `def-periodic-function` |
| AN1 sequences | `prp-floor-rules`, `prp-exp-beats-powers`, `prp-log-rules` (c), `prp-real-power-laws` |
| AN1 limits and continuity | 8.1–8.2 definitions, `def-floor-ceiling`, `exm-strange-functions` and entries, `lem-irrationals-dense` |
| AN1 continuous functions on intervals | `def-sup-of-function`, `thm-sup-function-rules`, `exm-strange-unbounded`, `exm-strange-sup-missed`, `exm-polynomial-unbounded` |
| AN1 derivative | `exm-method-factor-difference`, `prp-distance-to-integer`, `prp-staircase-squeeze` |
| AN1.10 | pays `ax-exponential`; uses `thm-exp-unique` |
| AN1 metric spaces (AN2.1, with old F4.11) | `thm-sup-function-rules` (b), (g), `def-bounded-function`, `prp-iterated-sup` |
| AN2 integration, AN2.15 | step functions, `prp-sup-oscillation`, `prp-iterated-sup`, `prp-dirichlet-properties`; AN2.15 closes the table |

## Promises

**Paid:** spec/08 F4.7 bullet (monotone, inverse, bounds, sup/inf of functions, floor; exp by a borrowed box; the strange-function table), with "factor theorem and root count without F5" **withdrawn** by the merge (proposal §3.4; now cited from Ch6–7). **Opened:** `ax-exponential` → AN1.10; table → AN1, AN2.15; Looking-ahead boxes → AN1 (8.2 continuous injective ⇒ monotone; 8.3 oscillation; 8.4 nowhere-differentiable function; 8.6 the table's questions and the sine); NOTATION amendments above. `chapter-constraints.yaml` row for F4.7 changes per proposal §4.2 (coordinator).

## Reconciliation with Chapter 1 (F4.6, apply when its blueprint is frozen)

| Here | If Chapter 1 has it |
|---|---|
| `prp-real-infimum`, `prp-real-sup-approximation` (owned) | 8.3 cites Chapter 1's labels and drops these two |
| `prp-real-power-consistent` (compares with ⁿ√(a^m)) | add "= Chapter 1's a^q" to the statement, same proof |
| `@thm-binomial-commutative-ring` | label unchanged wherever it lives |
| `@fd2:thm-bernoulli` | cite Chapter 1's real Bernoulli if it is made canonical |

## S2a list (statement referees)

1. `thm-exp-unique`: the two-sided bound for n > |x|, every hypothesis (positive bases; Bernoulli's x ≥ −1); only (E1), (E2) used, including in `prp-exp-first-consequences`.
2. `prp-log-rules` (c) strictness split (t ≥ −2, t < −2).
3. `prp-real-power-consistent`: negative m; the uniqueness clause of `@lem-reals-nth-root` (b) applies (a^{m/n} > 0).
4. `exm-polynomial-unbounded`: that `@lem-complex-polynomial-growth` applies to real coefficients via `@prp-reals-embed-complex` and that the value computed in ℂ is the real value; the choice x = R + 2M/|a_d|.
5. `prp-floor-rules` (d), (e), (h); 8.4 B1 (c) (negative j, x ∈ [0, 1)).
6. `prp-distance-to-integer` (a)–(d), in particular "= 1/2 iff x − 1/2 ∈ ℤ" and the Lipschitz bound; new 8.4 C2 (b).
7. `prp-staircase-squeeze` inequalities, and monotonicity at the endpoints 1/n.
8. `prp-thomae-large-values` (b) covering set; T(0) = 1 with 0 = 0/1.
9. `lem-irrationals-dense` transport of √2 ∉ ℚ to ℝ.
10. `thm-sup-function-rules` (d) at c = 0 and (g); `prp-iterated-sup` with a singleton factor.
11. 8.3 A1 (value 4, non-attainment); C1 (witness ε/(2s), both cases); 8.3 Quick check 3 (irrational in [0, 1]).
12. `thm-monotone-inverse` decreasing version and graph clause; `prp-strictly-monotone-order-reflecting` (≤ version).
13. `exm-mobius-increasing` difference formula and 8.2 Quick check 4 inverse; `exm-squash-function` image; 8.2 B3 (x|x|).
14. 8.5 B1 arithmetic; B2 (a), (d); B3 lines, distractors and the partial-order answer; A2 (d); Quick checks 2–5. New 8.2 B2 (d) values f(1/2), f(3/5).
15. 8.6 R1, R2 (decreasing bijections not closed, id missing), R4.
16. Cited labels still exist with the cited content at S3 (fd2, fd3 revised in parallel).
17. For each must-prove statement, what fails when each hypothesis is dropped (STYLE §10).

## Open for the coordinator

1. No TikZ `graph` style in `book-diagrams.sty`; add one or let drafters write plain TikZ.
2. `ax-exponential` and `@ax-cosine-sine` must name the same paying volume and chapter after the AN renumbering.
3. `check_blueprint.py` loads `chNN.md`: check a scratch copy `ch08.md`.
4. 8.2 and 8.5 cite Ch3's `lem-reals-nth-root`; it must survive any Ch1 root construction.

## S2 replies (round 1)

Two referee reports; overlapping findings answered once. All applied unless marked.

1. **8.2 B2 (d) re-proves fd2's x³** (both). Applied. fd2's `exm-maps-from-calculus` (a) solution proves x³ strictly increasing (checked, fd2 ch02 §02). The parenthesis in `exm-mobius-increasing`, "What changed" item 3 and A2 (−x³) now cite it. B2 (d) is now the false "x³ − x strictly increasing on [1/2, ∞)", which needs the factor-out move (bracket x² + xy + y² − 1 < 0 at 1/2, 3/5; f(1/2) = −3/8 > −48/125 = f(3/5)), repaired on [1, ∞). Referee 2's alternative "x³ − x on [1/2, ∞) (true)" is false, so we use it as the disprove case.
2. **8.4 C2 and the 8.6 zigzag remark** (both). Applied. `prp-distance-to-integer` (d) keeps subadditivity on the main line. C2 is new: dist(nx, ℤ) ≤ n dist(x, ℤ), equality when dist(x, ℤ) ≤ 1/(2n), and strictness at x = 1/2. The `[used later]` tag is dropped. The zigzag remark now cites (b) (dist ≤ 1/2) for |xZ(x)| ≤ |x|/2.
3. **`exm-sup-not-attained`, ε = 1** (R1). Applied: x ≔ 1/ε for every ε > 0, using (1 − ε)(1 + ε) = 1 − ε² < 1.
4. **`prp-staircase-squeeze` at x = 0** (R1). Applied: the squeeze is stated on (0, 1], with monotonicity on [0, 1].
5. **`thm-sup-function-rules` (e), (g) hypotheses** (R1). Applied. (e) has its own clause "f bounded below", and (g) "f, g bounded on the non-empty A". A ≠ ∅ is in the lead-in.
6. **`prp-sup-oscillation`, `prp-iterated-sup` hypotheses** (R1). Applied, as suggested.
7. **Archimedes squeeze with C = 0 at x = 0** (R1). Applied. The method box requires C > 0, and the proof takes C ≔ (x² + 1) exp x.
8. **8.5 B3 answer** (R1). Applied: the answer is a partial order and every linear extension is accepted.
9. **Thomae (b) finite union** (R1). Applied with a different citation: `@fd2:exm-images-finite` does not exist (grepped). The proof now uses the S_q, each finite by p ↦ p/q (`@fd2:def-finite`), and fd2's finite-unions exercise `@fd2:exr-finite-sets-b3`, with its two-line induction restated (`@fd2:prp-disjoint-union-count`, `@fd2:prp-subset-finite`) so that the main line does not rest on an exercise alone. The proof assumes ε > 0.
10. **Quick check √2/2** (R1). Applied, with the transport spelled out.
11. **"What you need" omits Ch1/Ch5** (both). Applied. Following referee 2, the binomial theorem is Chapter 1's (proposal §3.4 confirms it is proved only there), and its label currently sits in fd5 ch02 §06 until the structural move.
12. **Time arithmetic and rounding** (both). Applied: folds 1,400 words, core exercises 12 h, about 25 h core and 40 h full after rounding to the nearest 5.
13. **Quick check density** (both). Applied: 25 checks (8.1: 4, 8.2: 4, 8.3: 5, 8.4: 4, 8.5: 5, 8.6: 3), each with its answer and placed after the idea it tests, inside the existing word budgets.
14. **8.6 C1 "need choice" wording** (R1). Applied, with referee 1's wording, as a plain line in the solution with no pointer.
15. **Forward pointers scattered** (R2). Applied. Each section has at most one `[Looking ahead]` box at the end of the main line: 8.2 (continuous injective ⇒ monotone), 8.3 (oscillation), 8.4 (nowhere-differentiable), 8.6 (the table's questions plus the sine). The "used by AN2/AN1" sentence is deleted from `prp-iterated-sup`. 8.2 C2 no longer points forward: it gives the counterexample x ↦ −x, and 8.6 J refers back to it. The 8.5 borrowed box is a borrow, not a pointer.
16. **`lem-irrationals-dense` repeats fd3's exercise** (R2). Applied: the lemma now opens with the recall of `@fd3:exr-rationals-inside-the-reals-c2`.
17. **Floor hook** (R2). Applied in a weaker form. fd5 ch01 cites `@fd3:prp-rational-integer-part` but does not use the symbol ⌊·⌋ (grepped), so the hook says that Chapter 2 cited the integer part of a rational, not that it used ⌊a/n⌋.
18. **8.1 A1 (a) repeats Quick check 1** (R2). Applied: it is now {x + y² = 0}, which is not a graph because of (−1, ±1).
19. **Givens/Goal tables in 8.4, 8.5** (R2). Applied: both are now two-column tables.

Open: none for the drafter. For S2a: new 8.2 B2 (d) values, new 8.4 C2 (b), 8.5 Quick checks 2–5 (added to the S2a list).
