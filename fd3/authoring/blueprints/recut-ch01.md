<!-- hand-written -->
# Blueprint: F3.1 The Natural Numbers (fd3 Chapter 1, re-cut), stage S1

**Frozen after S2 (2026-10-26).** Two blind referees, one round; every finding applied or answered in "S2 replies (round 1)" at the end. Next: S2a, S3.

**What this is.** The S1 blueprint for fd3 Chapter 1 under the approved layout `fd3/authoring/design/layout-proposal.md` (§0 Q1 「多留一小節」; §3 Chapter 1; §5 items 1–4; §9). All five sections are pipeline **F**. The drafter works from this file, `fd3/src/ch01-natural-numbers/` at `b401a06`, `authoring/STYLE.md` (§1 house manner from fd2 on, §2, §6, §12.0, §12.5, §12.13.4, §12.14), `DRAFTING.md`, `PIPELINE.md`, `NOTATION.md`. Format: `fd2/authoring/blueprints/ch02-functions.md`, leaner. Math is written in plain Unicode here; the drafter typesets it.

**Line references** at `b401a06`: `11:` = `01-peano-axioms.md`, `12:` = `02-recursion-and-arithmetic.md`, `13:` = `03-order-and-well-ordering.md`, `14:` = `04-categoricity.md`. `05-where-n-comes-from.md` and `index.md` are title-only stubs. The parked ZF text (`fd3/authoring/parked/st/`) is for checking facts only.

| § | File | Main now | Budget | Expected main / fold |
|---|---|---|---|---|
| 1.1 | `01-peano-axioms.md` | ≈ 2,500 | ≤ 5,000 | ~3,800 / 0 |
| 1.2 | `02-recursion-and-arithmetic.md` | 5,475 | ≤ 5,000 | ~4,600 / ~650 |
| 1.3 | `03-order-and-well-ordering.md` | 6,807 | ≤ 5,000 | ~4,600 / ~850 |
| 1.4 | `04-categoricity.md` | 5,696 | ≤ 5,000 | ~4,300 / ~950 |
| 1.5 | `05-where-n-comes-from.md` | 0 | 2,000–3,000 | ~2,500 / 0 |

**House manner.** Motivation first (the failed attempt as hook), `[Scratch work]` with a Givens/Goal table apart from the proof, method boxes (≤ 130 words: Template, When to use it, The usual failure), one Prove-or-disprove B item per method section, a Quick check per 800–1,000 words. No footnotes, jokes, history or first person. Nothing from `/home/akizumi/book`; every example and exercise is new or the book's own. Difficulty moderate.

**Binding rules.**
1. **One assumption.** From 1.1 on, ℕ is the Peano system (ℕ, 0, S) fixed by the new `ax-natural-numbers`. No proof in 1.1–1.4 uses the school ℝ except `cor-omega-identification` (a), which is about fd2's ℕ inside ℝ, and the exercises about it (1.4 B2, 1.5 C1), which say so. No proof cites a parked label (`ax-zf-fragment`, `thm-kuratowski-pair`, `lem-omega-transitive`, `thm-omega-peano`, `def-set-successor`, `exm-von-neumann-numerals`, `thm-omega-least-inductive`, `prp-cartesian-product-exists`, `def-transitive-set`); each such citation is replaced as listed below.
2. **Cite back only:** fd1, fd2, earlier blocks of Chapter 1 in the new order (every `@label` here grepped at `b401a06`). Nothing cites 1.5; 1.1–1.4 may point to it in prose.
3. **No label lost or renamed**, except `exr-categoricity-r4`, parked (§5). `exr-categoricity-r1`…`-r3` move to 1.5 (titles [R1]–[R3]). Changed statements (S4/S5 changed items): `exm-peano-axioms-independent` (iii), `thm-omega-induction`, `def-omega-arithmetic` (c), `def-omega-order`, `thm-omega-order` (c), (e), `cor-omega-identification`, and every exercise marked rewritten.
4. **Clause letters stay.** Downstream cites `prp-omega-order-arithmetic` (a)–(d), (f); `thm-omega-order` (a), (b), (d); `thm-omega-arithmetic-laws` (a)–(f); `def-omega-arithmetic` (a)–(c); `prp-omega-powers-parity` (a), (d); `cor-omega-identification` (b) (54 times).
5. **Notation.** ℕ = `\nN`, successor upright `\mathrm{S}`, written n + 1 once 1.2 proves n + 1 = S(n). Peano systems stay (M, e, s). fd2's natural numbers inside ℝ: ℕ_ℝ (`\nN_{\nR}`, 1.4–1.5 only). "ω" becomes "ℕ" in all block titles and text; labels keep `omega`.

## 1. Devices

- **New boxes:** `exm-method-closed-subset` (1.1), `exm-method-induct-on-recursion-variable` (1.2), `exm-method-build-by-recursion` (1.4). Idea-level back-references: `@fd2:exm-method-induction-step` (1.1), `@fd2:exm-method-least-element` (1.3), `@fd2:exm-method-smallest-counterexample` (1.3 C1).
- **Scratch work + Givens/Goal:** `prp-peano-predecessor` (a), `thm-omega-recursion`, `thm-omega-arithmetic-laws` (a), `thm-peano-categoricity`.
- **Worked examples:** 1.1 the two parts of `prp-peano-predecessor`; 1.2 laws (a) and (c); 1.4 `thm-peano-categoricity` (b) and the map for (ℕ ∖ {0}, 1, S).
- **Prove or disprove:** 1.1 B3, 1.2 B3, 1.4 B3. 1.3 and 1.5 are not method sections.
- **Fading:** closed subset full in 1.1, Idea in 1.4 (onto); recursion variable full in 1.2, Idea in 1.3 and 1.4; build by recursion full in 1.4, terse in 1.5 R2.

## 2. Labels

**New** (grepped free): `ax-natural-numbers`, `prp-peano-predecessor`, the three boxes, `exr-peano-properties-b3`, `exr-recursion-and-arithmetic-b3`, `exr-categoricity-b3`, `exr-where-n-comes-from-a1`, `-b1`, `-b2`, `-c1`. All other labels of 11–14 stay in their files.

---

## 3. Per-section plans

### 3.1 Section 1.1: Peano's Axioms and Induction (`01`)

Scaffold full (new box).

1. **Delete** 11:3, 11:5, 11:9, 11:25–28, 11:74–116, 11:120, 11:137–157.
2. **Opening frame** (~170 words): *Sets and Functions*, Chapter 3 took ℕ inside the familiar ℝ and borrowed ℝ's arithmetic when convenient. This volume builds ℤ, ℚ and ℝ; starting from the ℕ inside ℝ would make ℝ rest on ℝ. So we need ℕ on its own. One assumption: a set with a start and a step obeying three rules. The section shows each rule is needed, proves induction in the form we use, and proves that every natural number except 0 has exactly one predecessor.
3. **`## What counting needs`** (~600, new). Two failed attempts: "ℕ = {0, 1, 2, …}" (the dots are the content); "the smallest subset of ℝ containing 0 and closed under x ↦ x + 1" (@fd2:prp-smallest-closed-set gives a smallest closed subset of ℝ, and identifying it with fd2's ℕ uses ℝ and the set form of @fd1:ax-induction: either way the description needs ℝ). So describe what counting must do: a start, a step, and three ways it goes wrong, as pictures before the definition: a **loop** ({p, q, r}, p ↦ q ↦ r ↦ p), a **merge** (p ↦ q ↦ r ↦ q), an **extra row** (a second copy of the counting numbers, never reached; in words). Then 11:11–21 verbatim (`def-peano-system`), and 11:23 verbatim except its last parenthesis: "(if one object is wanted, take the pair ((M, e), s) of @fd2:def-ordered-pair)".
   - **Quick check:** "For the loop (e = p), which of (P3)–(P5) fail?" *Solution:* only (P3): s(r) = p = e. (P4): the values q, r, p differ. (P5): a subset containing p and closed contains q, then r.
4. **`## The one assumption`** (~450, new).
   - **`ax-natural-numbers`** `[The Natural Numbers]`: "There is a Peano system." Prose: we fix one and write it (ℕ, 0, S); its elements are the **natural numbers**, 0 is **zero**, S(n) the **successor** of n. Why believe it: if the school ℝ is trusted, fd2's ℕ is one (Section 1.4 checks it); *Axiomatic Set Theory* builds one from sets (Section 1.5 describes how). The choice does not matter (Section 1.4). Every fact about ℕ is proved from this one assumption.
   - **`exm-peano-axioms-independent`**: 11:30 and (i), (ii) verbatim; (iii) **rewritten**: "(**Two copies of ℕ.**) Let a ≠ b be two objects, M ≔ ℕ × {a, b}, e ≔ (0, a), s(n, t) ≔ (S(n), t)." Solution (i), (ii) verbatim (11:52–54); (iii): s is a function M → M. (P3): (S(n), t) = (0, a) gives S(n) = 0 (@fd2:def-ordered-pair), against (P3) for ℕ. (P4): equal values give t = t′, S(m) = S(n), so m = n. (P5) fails: ℕ × {a} contains e, is closed, misses (0, b). After it (~80, optional two-row tikz): (0, b) has no arrow in and is not e; (P5) is the clause that says "nothing else". One back-reference sentence: (P5) quantifies over all subsets, which is why it excludes the extra row, where a first-order induction scheme could not (@fd1:exm-non-standard-naturals; the [Looking ahead] at the end of fd1 7.6 promised this). Exercise C2 builds a structure where every element except e has an arrow in and (P5) still fails.
5. **`## Induction in the form we use`** (~500).
   - **`thm-omega-induction`** `[Induction on ℕ]` **rewritten**: (a) 11:126 with ω → ℕ; (b) "(Property form.) Let P(n) be a property of natural numbers, possibly with other variables as parameters. If P(0) holds and, for every n ∈ ℕ, P(n) implies P(S(n)), then P(n) holds for every n ∈ ℕ." *Proof:* (a) is (P5) for ℕ (@ax-natural-numbers, @def-peano-system). (b) A ≔ {n ∈ ℕ : P(n)} (@fd2:def-set-builder) contains 0 and is closed; apply (a).
   - Paragraph (~120, replaces 11:137): (b) is @fd1:ax-induction with S(n) for n + 1 (1.2 shows they agree). There it was taken on trust for a ℕ that came with school arithmetic; here (P5) is part of the one assumption and arithmetic is not assumed at all.
   - **Warning:** "**Both halves of the hypothesis are needed.** ℕ ∖ {0} is closed under S, by (P3), and is not ℕ. {0} contains 0 and is not closed, since S(0) ≠ 0."
   - **Quick check:** "Let P(n) be 'n = 0'. Base? Step? What does the theorem conclude?" *Solution:* base yes; step no (P(0) holds, P(S(0)) fails by (P3)); no conclusion, and indeed P fails at S(0).
6. **`## Every natural number except 0 has one predecessor`** (~1,000, new; S2 R2.1: the disjunction trick and the unused hypothesis are fd2's, cited, not re-taught). Lead: fd2 used "n − 1 ∈ ℕ for n ≠ 0" (@fd2:lem-naturals-arithmetic (c)), computed in ℝ; ℕ has no subtraction, and 1.2–1.4 split "n = 0 or n = S(k)" constantly.
   - **`prp-peano-predecessor`** `[Predecessors in a Peano System]`: "Let (M, e, s) be a Peano system. (a) For every x ∈ M with x ≠ e there is exactly one y ∈ M with s(y) = x. (b) s(x) ≠ x for every x ∈ M." For ℕ: every n ≠ 0 is S(k) for exactly one k, its **predecessor**.
   - **[Scratch work]** for (a) (worked example 1): at most one is (P4); at least one can only come from (P5), which speaks of subsets, so choose the subset. The new point is the choice of a subset inside an abstract M, where nothing can be computed (no subtraction). "x = s(y) for some y" fails at e; the cure is the shape of @fd2:lem-naturals-arithmetic (c), cited in one clause: carry "z = e or …".

     | Givens | Goal |
     |---|---|
     | (M, e, s) Peano; x ≠ e | some y with s(y) = x |
     | A ≔ {z ∈ M : z = e or z = s(y) for some y} | A = M; then x ∈ A, x ≠ e gives y |
     | (P5) | e ∈ A; z ∈ A ⇒ s(z) ∈ A, since s(z) is a value of s |

     One clause after the table: the step never uses z ∈ A, as in @fd2:exm-predecessor-no-hypothesis (no further discussion).
   - *Proof:* (a) via A and (P5); uniqueness by (P4). (b) A′ ≔ {x : s(x) ≠ x}: e ∈ A′ by (P3); if s(x) ≠ x and s(s(x)) = s(x), (P4) gives s(x) = x; so A′ = M (worked example 2: here the hypothesis is used). A two-line Idea precedes the proof.
   - **`exm-method-closed-subset`** `[Method: induction through a closed subset]`. **Template.** (1) Name A ≔ {x ∈ M : P(x)}. (2) Show e ∈ A. (3) Take x ∈ A, show s(x) ∈ A, using P(x) if needed. (4) Conclude A = M by (P5). If P fails at e, carry "x = e or P(x)" (the shape of @fd2:lem-naturals-arithmetic (c)). **When to use it.** A statement about every element of a Peano system whose elements are not known one by one: an abstract (M, e, s), the image of a map out of ℕ, a set of pairs. **The usual failure.** A property false at e; closure checked only for elements of a special form (x = s(y)), forgetting e; (P5) applied to a set not inside M. One sentence after: on ℕ this is @thm-omega-induction (b), and @fd2:exm-method-induction-step still finds P(n) inside P(S(n)); the box adds the choice of the set.
   - **Quick check:** "In structure (ii) of @exm-peano-axioms-independent, which element has two predecessors, and which conclusions of @prp-peano-predecessor fail?" *Solution:* 1 = s(0) = s(1); "exactly one" in (a) fails ((P4) fails), and (b) fails at 1.
   - **Quick check:** "Does the loop satisfy (a)? What does that say about the converse?" *Solution:* yes (r ↦ p, p ↦ q, q ↦ r: one predecessor each); the conclusion does not give back the axioms (C2: even with (P3), (P4)).
7. **Closing** (replaces 11:155–157): 1.2 uses (P3), (P4), (P5) once each to prove recursion, then defines + and ·.
8. **Exercises.**
   - **A1** (rewritten): (a) 11:167 verbatim. (b) "In the proof of @prp-peano-predecessor (a), which axiom gives at least one y, which at most one?" (c) "Is ℕ ∖ {0} closed under S? Is it ℕ? Which hypothesis of @thm-omega-induction (a) fails?" (d) "True or false: in a Peano system, s is a bijection M → M." *Solution:* (a) as 11:175. (b) (P5) via A; (P4). (c) Yes (P3); no; 0 ∈ A. (d) False: injective by (P4), e not a value by (P3) (@fd2:def-surjective).
   - **B1** (rewritten) `[B1: Put the proof in order]`: "Let (M, e, s) be a Peano system. Below is a shuffled proof that s(s(x)) ≠ x for every x ∈ M, with two lines that do not belong. Order the six correct lines and say why the other two fail. (i) Let x ∈ A; we show s(x) ∈ A. (ii) Let A ≔ {x ∈ M : s(s(x)) ≠ x}. (iii) Then s(s(x)) = x by (P4), contradicting x ∈ A. (iv) e ∈ A, since s(s(e)) is a value of s, so not e, by (P3). (v) Suppose s(s(s(x))) = s(x). (vi) So s(s(s(x))) ≠ s(x), that is, s(x) ∈ A; by (P5), A = M. (vii) Since s is a bijection, write x = s(y) and apply the hypothesis to y. (viii) Since s(s(e)) ≠ e and every element is reached from e by steps, s(s(x)) ≠ x for every x." *Solution:* admissible orders: (ii) first; then (i), (v), (iii), (vi) in that order ((i), (v), (iii) open and close the supposition, (vi) applies (P5)); (iv) anywhere after (ii) and before (vi), stating the base first, (ii), (iv), (i), (v), (iii), (vi), being the convention. (vii) cites a false fact, s is not surjective ((P3)): (N9) of @fd1:exm-not-allowed-catalogue. (viii) is "and so on" without the step: (N13).
   - **B2** (kept): ω → ℕ, d ≔ S ∘ S; hint "look at ℕ ∖ {S(0)}"; solution 11:231–235 with "(P3) of @thm-omega-peano" → "(P3) for ℕ", "1" → "S(0)".
   - **B3** (new) `[B3: Prove or disprove]`: "Let (M, e, s) be a Peano system. (a) If A ⊆ M contains s(e) and is closed under s, then A ∪ {e} = M. (b) If A ⊆ M is non-empty and closed under s, then A = M. (c) Every x ≠ e is s(y) for some y with y ≠ x. (d) If f: M → M has f(e) = e and f(s(x)) = s(f(x)) for every x, then f = id_M. (e) Every x ∈ M is e or s(s(y)) for some y." *Solution:* (a) **True:** A ∪ {e} contains e; x = e gives s(e) ∈ A, x ∈ A gives s(x) ∈ A; (P5). (b) **False:** M ∖ {e} contains s(e) and is closed (P3), misses e. (c) **True:** y exists by @prp-peano-predecessor (a); y = x would give s(x) = x, against (b). (d) **True:** {x : f(x) = x} contains e and is closed; (P5), @fd2:prp-function-equality. (e) **False:** s(e) ≠ e, and s(e) = s(s(y)) gives e = s(y) (P4), against (P3).
   - **C1** (kept): M ≔ ℕ ∖ {0}, e ≔ S(0); "S(n) ∈ ω by (P2)" (11:251) → "S(n) ∈ ℕ since S maps ℕ into ℕ", "The set A′ … is inductive" (11:254) → "A′ contains 0 and is closed under S"; in 11:247–256 delete the "(Z6) … @thm-kuratowski-pair" sentence ("s: M → M is a function, since its values lie in M"); "of @thm-omega-peano" → "for ℕ"; the alternative becomes ℕ ∖ {0, S(0)}, start S(S(0)).
   - **C2** (rewritten) `[C2: Every element but one is a successor]`: "Let a, b, c be three different objects, M ≔ ℕ × {a, b, c}, e ≔ (0, a), and for n, k ∈ ℕ: s(n, a) ≔ (S(n), a), s(n, b) ≔ (S(n), b), s(0, c) ≔ (0, b), s(S(k), c) ≔ (k, c). (a) Why is s a function M → M? (b) Show (P3), (P4). (c) Show every x ≠ e is a value of s. (d) Show (P5) fails. (e) Which conclusions of @prp-peano-predecessor hold in M?" [Hint 1] "For (a), apply @prp-peano-predecessor (a) to ℕ." [Hint 2] "For (d), try ℕ × {a}." *Solution:* (a) Rows a, b: one formula. Row c: each k′ is 0 or S(k) for exactly one k, not both (@prp-peano-predecessor (a), (P3)). (b) Sort values by second coordinate (@fd2:def-ordered-pair): a: (S(n), a); b: (S(n), b), (0, b); c: (k, c). (P3): a value (0, a) would be (S(n), a) with S(n) = 0. (P4): equal values share the second coordinate; rows a and c by (P4) for ℕ; in row b, (S(n), b) ≠ (0, b), so both values have one form and the inputs agree. (c) (S(n), a) = s(n, a), (S(n), b) = s(n, b), (0, b) = s(0, c), (k, c) = s(S(k), c). (d) ℕ × {a} contains e, is closed, misses (0, b). (e) Both: (a) by (b), (c); (b) since S(n) ≠ n in ℕ, (0, b) ≠ (0, c), (k, c) ≠ (S(k), c). So neither conclusion gives back (P5). Picture: row a a copy of ℕ; rows b, c a chain infinite both ways ((n, b) as n, (k, c) as −(k + 1)).
9. **Ledger** rewritten (pairs: @fd2:def-ordered-pair; no ZF lines).

### 3.2 Section 1.2: Recursion; Addition and Multiplication (`02`)

Scaffold full (new box). Title kept.

1. **Delete** 12:3, 12:5, 12:9, 12:24–135, 12:165, 12:272.
2. **Opening frame** (~160): ℕ has 0, S and induction, no addition. *Sets and Functions*, Section 3.3 proved recursion with partial solutions on {0, …, n}, using order facts from ℝ; ℕ has no order yet. This section proves recursion by a construction needing no order (the smallest set of pairs the equations force), defines + and ·, and proves the laws by one move.
3. **`## Recursion on ℕ`.** 12:11–20 with ω → ℕ (`[Recursion Theorem on ℕ]`). 12:22: "This is the statement of @fd2:thm-recursion, with ℕ the Peano system of @ax-natural-numbers and S(n) in place of n + 1." (no `prp-cartesian-product-exists`; ℕ × X by @fd2:def-cartesian-product).
4. **[Scratch work]** (~350): "define f by the two equations" names f on both sides; a definition must produce the graph. It must contain (0, a) and, with each (n, x), also (S(n), g(n, x)). Take the smallest such subset of ℕ × X, by @fd2:prp-smallest-closed-set (start (0, a), step (n, x) ↦ (S(n), g(n, x)), into ℕ × X because g maps into X); call it R. Is R a graph?

   | Givens | Goal |
   |---|---|
   | R smallest closed in ℕ × X | each n has exactly one x with (n, x) ∈ R |
   | induction on n | base: only (0, a); step: only (S(n), g(n, x_n)) |
   | an extra pair (n, y) ∈ R | R ∖ {(n, y)} still closed, against "smallest" |

   Removing a pair is where (P3), (P4) enter. *Before reading on: where is each used?*
5. **Proof** (~600, new). *Step 1 (uniqueness):* 12:51–55 (ω → ℕ). *Step 2:* R. *Step 3, claim* (for every n exactly one x with (n, x) ∈ R; @thm-omega-induction (b)). Base: (0, a) ∈ R; if (0, b) ∈ R, b ≠ a, then R′ ≔ R ∖ {(0, b)} contains (0, a) and is closed, since each (S(m), g(m, x)) ≠ (0, b) by (P3); so R ⊆ R′, impossible. Step: let x_n be the partner of n; (S(n), g(n, x_n)) ∈ R. If (S(n), y) ∈ R with y ≠ g(n, x_n), then R′ ≔ R ∖ {(S(n), y)} contains (0, a) (S(n) ≠ 0) and is closed: (S(m), g(m, x)) = (S(n), y) with (m, x) ∈ R′ forces m = n (P4), x = x_n (hypothesis), y = g(n, x_n). Contradiction as before. *Step 4:* f ≔ (R, X) is a function (@fd2:def-function); f(0) = a; closure gives f(S(n)) = g(n, f(n)).
6. **After the proof** (~120): (P3) in the base, (P4) in the step, (P5) through induction. No choice is made. (No comparison with @fd1:thm-unique-readability here: R3 in 1.5 asks for it.) Then 12:131's second half ("From now on … **defined by recursion**").
   - **Quick check** (moved here from item 7): "For X = ℕ, a = 0, g(n, x) = S(S(x)): which pairs of R have first coordinate 0, 1, 2?" *Solution:* (0, 0), (1, 2), (2, 4) (g(1, 2) = 4); no others, by the claim. (Uses S(S(2)) = 4 by the numerals only.)
   - **Quick check:** "In the claim's step, why does R′ ≔ R ∖ {(S(n), y)} still contain (0, a)? Which axiom?" *Solution:* (P3): S(n) ≠ 0, so the removed pair is not (0, a).
   - **Warning** 12:137–139: ω → ℕ, "(P3) of @thm-omega-peano" → "(P3)"; last sentence → "The proof breaks at Step 2: this step does not map ℕ × X into itself, so @fd2:prp-smallest-closed-set does not apply."
7. **`## Addition and multiplication`.** 12:143–145 (ω → ℕ). **`def-omega-arithmetic`** (a), (b) with ω → ℕ; **(c) rewritten**: "The **numerals** are 1 ≔ S(0), 2 ≔ S(1), 3 ≔ S(2), and so on. For every n ∈ ℕ, n + 1 = S(n); in particular 1 + 1 = 2 and k + 2 = (k + 1) + 1." 12:163 verbatim. **Well-definedness** (~70, replaces 12:165): each g maps into ℕ, so (b) uses (a); (m, n) ↦ A_m(n) is a function because each A_m exists and is unique; likewise ·. 12:167–211 verbatim (ω → ℕ), with the corollary's proof "(P4) for ℕ … (P3) (@ax-natural-numbers)".
8. **`## The laws of arithmetic`.** 12:215 (ω → ℕ).
   - **[Scratch work]** for 0 + n = n (worked example 1, ~200): the equations speak of 0 and successors in the **second** place, where n sits, so induct on n. Table: Givens "m + 0 = m, m + S(n) = S(m + n)" / Goal "0 + n = n"; Givens "0 + 0 = 0" / Goal "0 + S(n) = S(n)"; Givens "IH 0 + n = n" / Goal "0 + S(n) = S(0 + n) = S(n): closed".
   - `thm-omega-arithmetic-laws` 12:217–231 (ω → ℕ).
   - **`exm-method-induct-on-recursion-variable`** `[Method: fix the others, induct on the recursion variable]`. **Template.** (1) Find the variable the definition recurses on: the second argument of + and ·, the exponent of b^n. (2) Fix the others. (3) Induct on it: the base is the equation at 0; the step opens the term at n + 1 by the other equation, applies the hypothesis inside, closes up. (4) If the variable sits where no equation applies (a first argument), first prove the lemma that moves it. **When to use it.** Identities between terms built by recursion: laws of +, ·, powers, sums. **The usual failure.** Inducting on a first argument (the warning below); citing a law not yet proved, such as commutativity before (a).
   - **Proof** (replaces 12:237–270): two-line Idea citing the box; (a) first half from the scratch work, second half one paragraph (row 12:258); (c) in full, 12:240–252 (worked example 2); then "(b), (d)–(g) follow by the same move, in the order of the table in the fold below." **Fold** `[Proofs of (b) and (d)–(g)]` (~650): first line 12:238's last sentence ("'Def' refers to the equations of @def-omega-arithmetic, 'IH' to the induction hypothesis"), then 12:253, the table 12:255–268 without rows (a), (c), and 12:269 without its sentence on (a), ending "This proves the theorem."
   - 12:272 → "The laws (a)–(g) are the rules of school arithmetic, now proved from @ax-natural-numbers. The next section defines the order by them." 12:274–278 verbatim (ω → ℕ).
   - **Quick check:** "Which variable would you induct on for (km)n = k(mn), and which law opens the step?" *Solution:* n, the recursion variable on both sides; (km)(n + 1) = (km)n + km = k(mn) + km = k(mn + m) = k(m(n + 1)), by @def-omega-arithmetic (b) and law (d).
9. **Exercises.**
   - **A1** (rewritten): "(a) In the proof of @thm-omega-recursion, where are (P3) and (P4) used? (b) Why does uniqueness need only an induction, while existence needs R? (c) Name the move and the variable for proving 0 · n = 0. (d) State the idea of the existence proof in two sentences." *Solution:* (a) (P3) in the claim's base: no step produces first coordinate 0, so (0, b) can be removed; (P4) in its step: a pair stepping to first coordinate S(n) has first coordinate n, where the hypothesis applies. (b) 12:302 adapted: uniqueness compares given functions; induction builds nothing, so existence needs an object, R. (c) Fix the others, induct on the recursion variable: n (0 · 0 = 0; 0 · (n + 1) = 0 · n + 0 = 0). (d) The smallest closed set of pairs exists; each n has one partner in it, because a second could be removed without breaking closure.
   - **B1, B2** (kept): ω → ℕ; B2's solution names the new box.
   - **B3** (new) `[B3: Prove or disprove]`: "For all natural numbers: (a) m + n = 0 ⇒ m = n = 0; (b) mn = m ⇒ n = 1; (c) m · (n + 1) = m · n + n; (d) m + n = m ⇒ n = 0; (e) n · n = n ⇒ n = 0. You may use @thm-omega-arithmetic-laws." *Solution:* (a) **True:** n ≠ 0 gives n = k + 1 (@prp-peano-predecessor (a)) and m + n = (m + k) + 1 ≠ 0 (@cor-omega-successor-cancellation); so n = 0 and m = m + 0 = 0. (b) **False:** m = n = 0. (c) **False** (a look-alike of @def-omega-arithmetic (b), whose last term is m): m = 0, n = 1 gives 0 · 2 = 0, while 0 · 1 + 1 = 1. (d) **True:** induct on m for "for every n, m + n = m ⇒ n = 0": 0 + n = n (law (a)); (m + 1) + n = (m + n) + 1 (law (a)) = m + 1 gives m + n = m, so n = 0. (e) **False:** n = 1 (1 · 1 = 0 + 1 = 1).
   - **C1** (kept, exit check; marking scheme kept), **C2** (kept), **C3** (kept): ω → ℕ; C3 "(P2) of @thm-omega-peano applied twice" → "S maps ℕ into ℕ", and "partial solutions … @exr-recursion-and-arithmetic-a1 (b)" → "R contains (1, 2) and (2, 4) (the first Quick check after @thm-omega-recursion)".
10. **Ledger** rewritten.

### 3.3 Section 1.3: Order and Well-Ordering (`03`)

Scaffold Idea (no box). Title kept. **New block order:** `def-omega-order`, `prp-omega-order-arithmetic`, `thm-omega-order`, `thm-omega-well-ordering`, powers (antisymmetry needs cancellation).

1. **Delete** 13:3, 13:5, 13:9, 13:19–21, 13:35–71, 13:83–105, 13:107–113 (the old Quick check, a membership argument; the new Quick check of item 4 replaces it), 13:117, 13:179.
2. **Opening frame** (~150): fd2 ordered ℕ by ℝ's order. ℕ has no line, but it has addition: m comes before n when we count up from m to n. The section takes that as the definition, ties it to arithmetic, proves it is a total order and a well-ordering, and records powers and parity.
3. **`## Counting up from m to n`** (~400). Italic: "*m ≤ n when n is reached from m by adding a natural number.*" **`def-omega-order`** rewritten: "For m, n ∈ ℕ, m ≤ n if n = m + j for some j ∈ ℕ, and m < n if m ≤ n and m ≠ n. As usual, n ≥ m means m ≤ n, and n > m means m < n." Examples: 2 ≤ 5 (2 + 3 = S(2 + 2) = 5); 0 ≤ n (n = 0 + n, law (a)). Nothing yet says that 5 ≤ 2 fails or that ≤ is an order: antisymmetry needs "a sum is 0 only if both terms are", totality an induction.
4. **`## Order and arithmetic`** (moved up). Lead (~80): cancellation needs no order; then (c)–(g) translate m < n into n = m + j with j ≠ 0. **`prp-omega-order-arithmetic`** 13:119–133 (ω → ℕ). Idea 13:135–137: drop the old (a) induction; add "(f) by induction on m, the first factor, using law (e) to open (m + 1)k (step (4) of @exm-method-induct-on-recursion-variable)". Proof: (b) verbatim. (a): "the equivalence is @def-omega-order"; uniqueness verbatim; strict case verbatim with "(by @def-omega-order)" replacing the irreflexivity citation. (c), (e), (g) verbatim; (d) with @prp-peano-predecessor (a) for @lem-omega-transitive (d). **(f) new:** fix k ≠ 0, induct on m for "for every n, mk = nk ⇒ m = n". Base: 0 · k = 0, so nk = 0 and n = 0 by (d). Step: k = i + 1, so (m + 1)k = mk + k = (mk + i) + 1 ≠ 0; thus n = n′ + 1, mk + k = n′k + k (law (e)), mk = n′k by (b), m = n′ by hypothesis. 13:175 verbatim (ω → ℕ; "by the Quick check above" → "by the example after @def-omega-order", which shows 5 = 2 + 3).
   - **Quick check:** "Show 3 ≤ 5, naming j. Is n ≤ n + 1? Is n + 1 ≤ n?" *Solution:* 5 = 3 + 2 (3 + 2 = S(S(3))), so 5 − 3 = 2; yes, j = 1; no: n = (n + 1) + j = n + (j + 1) would give j + 1 = 0 by uniqueness in (a), against @cor-omega-successor-cancellation.
5. **`## A total order`** (~1,000). **`thm-omega-order`**: (a), (b), (d) verbatim (ω → ℕ); **(c)**: "For n ∈ ℕ, {0, …, n} ≔ {k ∈ ℕ : k ≤ n} satisfies {0, …, 0} = {0} and {0, …, S(n)} = {0, …, n} ∪ {S(n)}, with S(n) ∉ {0, …, n}." **(e)**: "For n ∈ ℕ, {1, …, n} ≔ {k ∈ ℕ : 1 ≤ k ≤ n} satisfies {1, …, 0} = ∅ and {1, …, S(n)} = {1, …, n} ∪ {S(n)}."
   - Idea (~80): ≤ is reflexive (j = 0), transitive (associativity), antisymmetric (cancel, then a zero sum), total (induction on n with "for every m" inside). The rest unwinds (b).
   - Proof (~600). Partial order (@fd2:def-partial-order): (PO1) n = n + 0; (PO3) law (c); (PO2) n = m + j, m = n + i give m + 0 = m + (j + i), so j + i = 0 (uniqueness in @prp-omega-order-arithmetic (a)); i = i′ + 1 would give j + i = (j + i′) + 1 ≠ 0; so i = 0, m = n. *Total:* induction on n for "for every m, m ≤ n or n ≤ m": 0 ≤ m; if n = m + j then n + 1 = m + (j + 1); if m = n + j, then j = 0 gives m ≤ n + 1, and j = j′ + 1 gives m = (n + 1) + j′. *(a)* irreflexive by definition; k < m < n gives k ≤ n, and k = n would force k = m by (PO2); at least one by totality, at most one by (PO2). *(b)* (⇐) S(n) = m + (j + 1); (⇒) S(n) = m + (i + 1) = S(m + i) gives n = m + i (P4); nothing between, by trichotomy. *(c)* k ≤ 0 forces k = 0 (zero sum); the union by (b); S(n) ≤ n contradicts n < S(n). *(d)* n = 0 + n; n ≠ 0 gives n = k + 1 = 1 + k; 1 = 0 + 1 ≠ 0. *(e)* from (c), (d).
   - 13:67 rewritten (~60): fd2's {0, …, n}, {1, …, n} keep their meaning; (b) says n + 1 is the next number.
   - **Quick check:** "Is there k ∈ ℕ with 4 < k < 5? List {0, …, 3} by (c)." *Solution:* no: 5 = S(4) and (b); {0} ∪ {1} ∪ {2} ∪ {3} = {0, 1, 2, 3}.
   - **Warning:** "**Cancelling a factor needs it to be non-zero.** 5 · 0 = 2 · 0, yet 5 ≠ 2: clause (f) of @prp-omega-order-arithmetic carries k ≠ 0 for this reason. Clause (e) carries it too, since 2 < 5 while 2 · 0 < 5 · 0 fails."
6. **`## Well-ordering`** (~650). 13:75 rewritten (fd2 went through strong induction; here a direct induction on {0, …, n}). `thm-omega-well-ordering` 13:77–81 (ω → ℕ). Idea (~70): if A had no least element, no element of {0, …, n} lies in A, by induction: the first element met on the way up would be least. Contrast with @fd2:exm-method-least-element, which uses a least element. Proof (~250): suppose none; B(n): {0, …, n} ∩ A = ∅. B(0): 0 ∈ A would be least by (d). Step: by (c), {0, …, S(n)} ∩ A = {S(n)} ∩ A; if S(n) ∈ A, each x ∈ A has n < x (B(n), trichotomy), so S(n) ≤ x (by (b)), and S(n) is least. So B(n) for all n, and a ∈ A gives a ∈ {0, …, a} ∩ A. Uniqueness 13:99–100. Then 13:103 rewritten (~60: RAA; @fd2:thm-well-ordering read on ℕ) and 13:105's first and last sentences.
   - **Quick check** (from old A1 (c)): "Least element of {n ∈ ℕ : n · n > 10}, and why?" *Solution:* 4: 3 · 3 = 9 < 10 < 16 = 4 · 4 (10 = 9 + 1, 16 = 10 + 6); any smaller x lies in {0, 1, 2, 3} (@thm-omega-order (c)) with x · x ≤ 9.
7. **`## Powers and parity`** (~450 + fold ~850). Lead: fd2 Ch4 counted with 2^m 3^n and parity, taken from ℝ and ℤ; here they are on ℕ, for 1.4's citing rule and Chapter 4. 13:181–202 (ω → ℕ; Idea adds "(a), (b) by the recursion-variable method").
   - **Quick check** (after the definition of b^n): "Compute 2^3 from the two equations." *Solution:* 2^0 = 1, 2^1 = 1 · 2 = 2, 2^2 = 2 · 2 = 4, 2^3 = 4 · 2 = 8. **Fold** `[Proof of the proposition]`: 13:204–237 with "(@thm-kuratowski-pair)" → "(@fd2:def-ordered-pair)". 13:239: second sentence → "Section 1.4 and Chapter 4 use it."
8. **Exercises.**
   - **A1** (rewritten): "(a) True or false: m < n ⇒ m + 1 ≤ n. (b) Is 5 ≤ 2? (c) Which clause of @thm-omega-order says {0, …, n} grows by one element per step? List {0, …, 2} and {1, …, 2}. (d) Which clause defines n − m? Compute 5 − 2." *Solution:* (a) True: n = m + j, j = 1 + i (@thm-omega-order (d)), so n = (m + 1) + i. (b) No: 2 < 5, and trichotomy. (c) (c); {0, 1, 2}, {1, 2}. (d) @prp-omega-order-arithmetic (a); 3.
   - **B1** (rewritten, title kept) `[B1: Order as inclusion]`: "Prove m ≤ n iff {0, …, m} ⊆ {0, …, n}, and m < n iff the inclusion is proper." *Solution:* (⇒) transitivity; (⇐) m ∈ {0, …, m}. Proper: n ∉ {0, …, m} when m < n (trichotomy). Conversely, a proper inclusion gives m ≤ n, and m ≠ n, since m = n would make the sets equal.
   - **B2** (kept): ω → ℕ.
   - **C1** (kept, marking scheme kept): ω → ℕ; "(Z6) of @ax-zf-fragment" → "@fd2:def-set-builder"; the comparison mentions @fd2:exm-method-smallest-counterexample.
   - **C2** (rewritten) `[C2: Find the error]`: "Is the conclusion true? Is the proof correct? If not, give the first failing line, the error, and a counterexample to the step. **Claim.** For all m, n ∈ ℕ: m ≤ n or n ≤ m. (1) Fix m; induct on n (@thm-omega-induction (b)) for 'm ≤ n or n ≤ m'. (2) n = 0: 0 ≤ m, since m = 0 + m. (3) Suppose m ≤ n or n ≤ m. (4) If n = m + j, then n + 1 = m + (j + 1), so m ≤ n + 1. (5) If n ≤ m, then n + 1 ≤ m, because n < n + 1 and nothing lies strictly between n and n + 1. (6) So m ≤ n + 1 or n + 1 ≤ m. (7) By induction the claim holds." *Solution:* conclusion **true** (totality); proof **not** correct. Line (5) fails, for two independent reasons. First, n ≤ m includes n = m, where n + 1 ≤ n is false: a missing case, (N7); counterexample to the step: m = n = 0. Second, even for n < m the stated reason needs a comparison of m with n + 1, and "nothing lies strictly between" (@thm-omega-order (b)) is itself proved from trichotomy, the claim being proved: (N9). Repair: if n = m, then m ≤ n + 1; if n < m, then m = n + j with j ≠ 0 (@prp-omega-order-arithmetic (a)), j = j′ + 1, so m = (n + 1) + j′, which uses no comparison. Fixing m is harmless. **Marking scheme** (10): 2 verdicts; 3 line (5) with either defect; 2 classification, (N7) or (N9); 2 counterexample (or, for an (N9) answer, the circular citation named); 1 repair. Fatal: calling the conclusion false; blaming line (1).
9. **Ledger** rewritten.

### 3.4 Section 1.4: All Peano Systems Are Alike (`04`)

Scaffold full (new box). The R group moves to 1.5.

1. **Delete** 14:3, 14:5, 14:45–57, 14:86 (first sentence), 14:94–104, 14:163, 14:207–239.
2. **Opening frame** (~150): 1.1 fixed one Peano system as ℕ; fd2's ℕ_ℝ is another, (ℕ ∖ {0}, 1, S) a third, *Axiomatic Set Theory* builds a fourth. Does the choice matter? Any two are copies by exactly one matching, which carries +, ·, <; then how later chapters read fd1 Ch4 and fd2 Ch3–4 about ℕ.
3. **`## Two Peano systems …`.** 14:9–25 (ω → ℕ); 14:9's exercise pointer → "Exercise C1 of Section 1.1 asked for the check; here it is"; "@thm-omega-peano (P3)/(P4)" → "(P3)/(P4) for ℕ"; "not ∅" → "not 0".
4. **`## The categoricity theorem`.** 14:29–43 (ω → ℕ). **[Scratch work]** replaces 14:45–57: ①–③ and the (c) sentence kept (② adds "by @exm-method-closed-subset"), plus:

   | Givens | Goal |
   |---|---|
   | (M, e, s) Peano | φ: ℕ → M, φ(0) = e, φ(S(n)) = s(φ(n)), bijective |
   | @thm-omega-recursion, X = M, a = e, g(n, x) = s(x) | (a) |
   | image φ(ℕ) contains e, closed | onto, by (P5) for M |
   | Q(n): ∀m (φ(m) = φ(n) ⇒ m = n) | one-to-one: base (P3), step (P4) for M |

   then 14:56. Proof 14:59–84 with: "Let g: ℕ × M → M, g(n, x) ≔ s(x), a function because s is"; "@thm-omega-peano (P2)" → "S maps ℕ into ℕ"; "@lem-omega-transitive (d)" → "@prp-peano-predecessor (a)" (twice).
   - **`exm-method-build-by-recursion`** `[Method: build by recursion, compare by induction]`. **Template.** (1) To make a map out of ℕ, give its value at 0 and how the value at S(n) comes from the value at n; @thm-omega-recursion builds it, uniquely. (2) To show two maps out of ℕ equal, check both satisfy the same two equations; cite uniqueness. (3) To prove a property of the map (onto, one-to-one, preserving an operation), induct, or apply (P5) to its image. **When to use it.** Maps between Peano systems; operations defined by recursion; recognizing a formula as the recursively defined map. **The usual failure.** "And so on" instead of the theorem, (N13); citing uniqueness when the equations differ (another start or step); fixing m outside Q(n). 14:86's second sentence follows.
   - **Quick check** (after the box): "f, g: ℕ → ℕ satisfy f(0) = g(0) = 3, f(n + 1) = f(n) + 2, g(n + 1) = g(n) + 2. Which step of the box gives f = g? What is f(2)?" *Solution:* step (2), uniqueness in @thm-omega-recursion (a = 3, g(n, x) = x + 2); f(2) = 7.
   - **Worked example 2** (~120, from 14:98–104): for (ℕ ∖ {0}, 1, S), n ↦ S(n) satisfies the two equations, so it is φ by uniqueness; φ(n) = n + 1, φ(3) = 4.
   - 14:88–92 with (iii) → "In the two copies of ℕ, which fail (P5) only, φ is n ↦ (n, a) (step (2)), injective by @fd2:def-ordered-pair, missing (0, b)." Plus one sentence: C2 asks the reverse question for @exr-peano-properties-c2's structure.
   - **Quick check:** "ψ is an isomorphism (ℕ, 0, S) → (ℕ, 0, S). What is ψ(3)?" *Solution:* 3: id_ℕ is one, and by (c) the only one.
5. **`## Arithmetic and order travel …`.** 14:108–159 (ω → ℕ); Idea cites step (3) of the box.
   - **Quick check:** "For (ℕ ∖ {0}, 1, S) and φ(n) = n + 1: φ(2 + 3) = 6, but φ(2) + φ(3) = 7. Does this contradict @prp-isomorphism-preserves-arithmetic (a)?" *Solution:* no: the proposition uses the ⊕ of the target system, with x ⊕ e = x for e = 1; so 3 ⊕ 1 = 3, 3 ⊕ 2 = 4, 3 ⊕ 3 = 5, 3 ⊕ 4 = 6 = φ(5).
6. **`## Identifying the two sets of natural numbers`.** Lead (~110): (a) is about ℕ_ℝ and uses ℝ; (b), (c) are about ℕ, from @ax-natural-numbers.
   - **`cor-omega-identification`** `[Our ℕ and the ℕ of Sets and Functions]`, **rewritten**: (a) 14:169 with "Write ℕ_ℝ ⊆ ℝ for the set …", fd2's ℕ → ℕ_ℝ, ω → ℕ (φ: ℕ → ℕ_ℝ). (b) "**About ℕ, proved from @ax-natural-numbers.** The statements of @fd1:ax-induction and @fd2:thm-recursion, read on ℕ with n + 1 ≔ S(n), are @thm-omega-induction (b) and @thm-omega-recursion. Induction from a base b ∈ ℕ (@fd2:thm-induction with n_0 = b) is @prp-omega-order-arithmetic (g)." (c) 14:175 (ω → ℕ). Idea and proof 14:179–205 with the same substitutions.
   - Paragraph (~90, replaces 14:207): (a) is why the choice does not matter, but used ℝ; later chapters lean on (b), (c), where ℝ never enters.
   - **Warning** (replaces 14:209–211): "The isomorphism carries 0, the successor, +, · and <, nothing else. In ℕ_ℝ, 3 − 5 and 3/5 are real numbers; in ℕ neither exists until Chapters 2 and 3. In the construction from sets of Section 1.5, 2 ∈ 3 is true; in ℕ_ℝ it means nothing. No later theorem asks such questions."
7. **`## How later chapters cite …`** (one paragraph ~260 + fold). Paragraph: in the rest of the volume ℕ is the system of @ax-natural-numbers with this chapter's 0, +, ·, <. fd1 Ch4 and fd2 Ch3–4 proofs used ℝ's arithmetic (14:217's evidence in one clause), so they are read through (b), (c), @thm-omega-well-ordering, @thm-omega-arithmetic-laws, @thm-omega-order, @prp-omega-order-arithmetic, @prp-omega-powers-parity. The results then fall into three groups, **numbered as before because later chapters cite them**: (i) run on ℕ, citable anywhere (finite and countable sets of fd2 Ch4); (ii) also use powers, parity or cancellation in ℝ, run on ℕ through @prp-omega-powers-parity and @prp-omega-order-arithmetic (b), (f), citable only in review exercises; (iii) templates (@fd2:def-sum-product, @fd2:prp-power-laws) used over an ordered field. **Fold** `[The three groups in full]`: 14:231–235 (ω → ℕ), with 14:233's clause "and Section 1.2 left such families to the axiom of Replacement" → "such families are left to *Axiomatic Set Theory*", its sentences "A list given as a function …" through "… in that form." replaced by "A later chapter that needs (b) proves it on ℕ first.", and every "through the dictionary" / "With the dictionary" in 14:229–235 → "through the citing rule above" / "With the citing rule above". The table 14:217–227 and 14:237–239 are deleted. Closing (~60): all that fd1 Ch4 and fd2 Ch3 assumed about ℕ is proved from @ax-natural-numbers; 1.5 says where a Peano system comes from; Chapter 2 builds ℤ.
8. **Exercises** (no R).
   - **A1** (edited): (b) → "Inside @thm-omega-recursion: in its claim's step, a pair stepping to first coordinate S(n) has first coordinate n, by (P4) for ℕ."
   - **B1** (edited): drop "E is a set by (Z6) inside ω: it is"; "(@thm-omega-peano (P3))" → "((P3) for ℕ)". **B2** (edited): φ: ℕ → ℕ_ℝ; "in ℕ" → "in ℕ_ℝ"; "In ω" → "In ℕ".
   - **B3** (new) `[B3: Prove or disprove]`: "(a) Exactly one f: ℕ → ℕ has f(0) = 1, f(n + 1) = 2f(n). (b) Exactly one f: ℕ → ℕ has f(0) = 0 and f(n + 1) = f(n) + 2n + 1, and it is f(n) = n · n. (c) Some injective f: ℕ → ℕ has f(n + 1) = f(n) for all n. (d) If f(0) = g(0), f(n + 1) = f(n) + n and g(n + 1) = g(n) + n for all n, then f = g. (e) Every bijection ψ: ℕ → ℕ with ψ(0) = 0 is an isomorphism (ℕ, 0, S) → (ℕ, 0, S)." *Solution:* (a) **True:** recursion, a = 1, g(n, x) = 2x. (b) **True:** recursion (a = 0, g(n, x) = x + 2n + 1) gives exactly one f; n ↦ n · n satisfies both equations, since 0 · 0 = 0 and (n + 1)(n + 1) = n · n + 2n + 1 by @thm-omega-arithmetic-laws (d), (e) and 2n = n + n; so it is f, by step (2) of the box. (c) **False:** f(1) = f(0). (d) **True:** same equations (a = f(0), g(n, x) = x + n); uniqueness. (e) **False:** τ (the first warning): τ(S(0)) = 2 ≠ 1 = S(τ(0)).
   - **C1** (edited): @prp-peano-predecessor (a) for @lem-omega-transitive (d); marking scheme kept.
   - **C2** (edited): statement becomes "Let (M, e, s) be the structure of @exr-peano-properties-c2: M = ℕ × {a, b, c}, e = (0, a), s(n, a) = (S(n), a), s(n, b) = (S(n), b), s(0, c) = (0, b), s(S(k), c) = (k, c). Show that there is **no** function f: M → ℕ …" (rest of 14:340 with ω → ℕ). Solution 14:344–351 with (k, 2) → (k, c) and (0, 2) → (0, c) throughout, ω → ℕ, the "(Z6)" clause deleted, "u ∈ S(u) = t, that is, u < t (@def-omega-order)" → "t = u + 1, so u < t (@prp-omega-order-arithmetic (a))", and 14:350's citation "(@exm-peano-axioms-independent)" → "(@exr-peano-properties-c2 (b), (d))".
9. **Ledger** rewritten; the (a) school-ℝ lines kept.

### 3.5 Section 1.5: Where ℕ Comes From (`05`, new)

~2,500 words. **No proofs and no labelled results in the main line**: prose, displays, a Quick check, a warning, exercises. All proofs are in *Axiomatic Set Theory*; nothing cites this section. New prose (parked files for facts only).

1. **Opening frame** (~130): 1.1 assumed a Peano system exists. Inside ℝ there is one (1.4 (a)), but that presupposes ℝ; *Axiomatic Set Theory* builds one from sets alone. This section describes how, without proofs; nothing later depends on it.
2. **`## Sets as the raw material`** (~550): fd2 used sets informally, naming a few principles (@fd2:def-set-builder, @fd2:def-power-set, unions). Set theory lists its axioms; the ones this construction uses, each in one line: extensionality, an empty set, pairs {a, b}, unions, power sets, specification, and infinity (below). One clause: *Axiomatic Set Theory* states the rest (replacement, foundation, choice). Every mathematical object, numbers included, is then a set.
3. **`## Zero and the successor as sets`** (~500): 0 ≔ ∅, S(x) ≔ x ∪ {x}; 1 = {0}, 2 = {0, 1}, 3 = {0, 1, 2}: each numeral is the set of the earlier ones, so m < n reads m ∈ n, in this construction only (1.4's warning).
   - **Quick check:** "Write 3 with ∅ and braces. Is 1 ⊆ 3? Is 3 ∈ 1?" *Solution:* {∅, {∅}, {∅, {∅}}}; yes (0 ∈ 3); no (the only element of 1 is ∅, and 3 ≠ ∅).
4. **`## The least inductive set`** (~650): I is **inductive** if ∅ ∈ I and x ∈ I ⇒ S(x) ∈ I; the axiom of infinity gives one; ω is the least, as in @fd2:prp-smallest-closed-set (start ∅, step S). (ω, ∅, S) is a Peano system: (P5) is leastness; (P3) since ∅ has no elements and x ∈ S(x); (P4) is the real work (sets whose elements are also subsets), done in *Axiomatic Set Theory*. By @thm-peano-categoricity, ω is a copy of ℕ; so @ax-natural-numbers reduces to the axioms for sets.
   - **Warning:** "**An inductive set need not be ω.** The axiom gives *some* inductive set. Likewise ℝ contains 0 and is closed under x ↦ x + 1, and is not ℕ_ℝ. Arguments about natural numbers use leastness, (P5), not mere closure."
5. **`## Pairs as sets`** (~450): @fd2:def-ordered-pair took (a, b) as a new object. In set theory (a, b) ≔ {{a}, {a, b}} (Kuratowski), with the characteristic property proved in *Axiomatic Set Theory*; a = b gives {{a}}; {a, b} itself fails since {a, b} = {b, a}. Products, functions and ℕ × ℕ are then sets; Chapter 2 needs only fd2's pairs.
   - **Quick check:** "Is {{0}} a pair? Of what?" *Solution:* yes: (0, 0) = {{0}, {0, 0}} = {{0}} (as a set it is {1}, since 1 = {0}).
6. **Exercises.**
   - **A1:** "(a) List the elements of S(3). (b) True or false: 2 ∈ 3 and 2 ⊆ 3 in this construction. (c) Why can {a, b} not be the ordered pair? (d) Which Peano axiom is 'ω is least' in disguise?" *Solution:* (a) 0, 1, 2, 3 (S(3) = 4). (b) Both true. (c) {1, 2} = {2, 1}. (d) (P5).
   - **B1** `[B1: Numerals by hand]`: "(a) Write S(4) as a set of numerals; how many elements has n, for n ≤ 5? (b) Compute 2 ∪ 3, 2 ∩ 3. (c) Is {1} ⊆ 3? Is {1} one of 0, …, 5?" *Solution:* (a) {0, 1, 2, 3, 4} = 5; n elements. (b) 3 and 2: larger and smaller. (c) Yes (1 ∈ 3). No: one element, so only 1 could match, and 1 = {0} ≠ {1}.
   - **B2** `[B2: Pairs as sets]`: "Write (0, 1), (1, 0), (1, 1) by Kuratowski; show (0, 1) ≠ (1, 0); how many elements has (a, b) when a ≠ b, when a = b?" *Solution:* (0, 1) = {{0}, {0, 1}} = {1, 2}; (1, 0) = {{1}, 2}; (1, 1) = {{1}}. 1 ∈ (0, 1), but 1 ≠ {1} (0 ∈ 1) and 1 ≠ 2 (1 ∈ 2, 1 ∉ 1), so 1 ∉ (1, 0). Two elements if a ≠ b, one if a = b. ((0, 1) lacks 0, so it is not a numeral.)
   - **C1** `[C1: Closed is not least]`: "ℝ, [0, ∞) and ℕ_ℝ ∪ {n + ½ : n ∈ ℕ_ℝ} each contain 0 and are closed under x ↦ x + 1. With e = 0, s(x) = x + 1, which of (P3)–(P5) hold? Which subset of ℝ is the least such set?" *Solution* (school ℝ, as in 1.4 (a)): (P4) in all three; (P3) fails only in ℝ (−1 + 1 = 0); (P5) fails in all three: ℕ_ℝ contains 0, is closed, and misses −1, ½, ½. The least is ℕ_ℝ: if S ⊆ ℝ contains 0 and is closed, then S ∩ ℕ_ℝ contains 0 and is closed, so it is ℕ_ℝ by the set form of @fd1:ax-induction (the remark at the start of *Sets and Functions*, Section 3.1); hence ℕ_ℝ ⊆ S.
   - **R1–R3** (moved, `exr-categoricity-r1`…`-r3`): R1 "ω" → "ℕ", "through the dictionary of this section (group (i))" → "through the citing rule of Section 1.4 (group (i))"; S: ℕ → ℕ ∖ {0} bijective by (P3), (P4), @prp-peano-predecessor (a). R2: L(0) ≔ 0, L(S(k)) ≔ k, a function by @prp-peano-predecessor (a) and (P3) (no (Z6)). R3: "no n has n = S(n) (@prp-peano-predecessor (b))" for the @lem-omega-transitive (c) argument. Rest verbatim.
7. **Ledger:** R items and C1 only.

### 3.6 Chapter index (`index.md`, coordinator after S3)

- `# The Natural Numbers`. **Story** (2 paragraphs): we cannot start from the ℕ inside ℝ; one assumption, a Peano system, yields induction, recursion, arithmetic, order and well-ordering; categoricity makes the choice harmless; 1.5 says where one comes from.
- **What you need** (final list by grep): fd1 Ch4 (@fd1:ax-induction, @fd1:thm-strong-induction, @fd1:thm-unique-readability), Ch8 (@fd1:exm-not-allowed-catalogue); fd2 Ch1 (set-builder, pairs, products, @fd2:prp-smallest-closed-set), Ch2 (functions, injective/surjective, composition, inverses, images), Ch3 (@fd2:thm-recursion, @fd2:lem-naturals-arithmetic, @fd2:thm-well-ordering, three boxes), Ch4 (finite sets), 5.3 (@fd2:def-partial-order).
- **Time** recomputed (`check_structure.py --words`); expected ~20 h core / 28 h full (layout 18/25 plus 1.5's +2/+3).
- **Roadmap** (5 bullets, one per section). **Named moves:** the three boxes; "Translate ≤ into n = m + j" (1.3). ("Carry a disjunction" is fd2's move, @fd2:lem-naturals-arithmetic; not listed.)
- **Summary**, **Terms:** Peano system, natural number, successor, predecessor, defined by recursion, sum, product, numeral, ≤, <, well-ordering, power, isomorphism of Peano systems. (1.5's inductive set, von Neumann numerals and Kuratowski pair have no labelled definitions, so they appear in the Summary only, STYLE §12.13.5.)

---

## 4. Budgets, Time, deviations

Budgets: top table. New exercises: 1.1 B3; 1.2 B3; 1.4 B3; 1.5 A1, B1, B2, C1. Rewritten: 1.1 A1, B1, C2; 1.2 A1; 1.3 A1, B1, C2. Core track: all A, one B and one C per section, 1.2 C1, R1–R3.

**Deviations from the layout** (for the author; not blocking):
1. A box in 1.1 (`exm-method-closed-subset`), absent from layout §5's list: 1.1 is full scaffold, and 1.4 reuses the move.
2. `thm-omega-order` keeps five clauses: auto-lettering would move (d) otherwise; (c), (e) are refilled with Peano-side facts (no downstream use of (c), (e)).
3. `prp-omega-order-arithmetic` precedes `thm-omega-order`; its (f) is proved by induction.
4. `thm-omega-arithmetic-laws` (b), (d)–(g) go to a fold, not to exercises: a theorem cited about 40 times downstream cannot rest on exercises; B2, C1, C2 still ask for them first.
5. The R group moves to 1.5 (STYLE §2); `exr-categoricity-r4` is parked for ST.1.
6. `exm-peano-axioms-independent` (iii) becomes two copies of ℕ; the two-sided chain becomes 1.1 C2 (used by 1.4 C2).
7. Recursion via the smallest closed set of pairs (layout §5's first option). Powers and parity proof folded.

## 5. Edits outside the chapter

- **Park** `exr-categoricity-r4` → `fd3/authoring/parked/st/from-1.7-r4-union-of-successor.md` (standard header), its ledger item → `parked/ledger-parked.yaml`, sidecar → `parked/st/verify/`.
- **`fd3/config/known-unresolved.json`:** drop the Chapter 1 group (5.5 entries stay).
- **Later fd3 prose saying ω or "axioms for sets"** (for their S passes, not this drafter): 2.1:5, 2.2, 2.3, 3.3 (five; "ℕ = ω through the dictionary" → "ℕ through the citing rule"), 4.2, 4.3, 4.5, 4.6 (three), 5.1, 5.5, Ch6 index. Their `@cor-omega-identification` and "group (i)/(ii)" references stay valid; so do fd5 and an1 ledger lines.
- **NOTATION** (both copies, `tools/series.py`): S row (successor of the system of `ax-natural-numbers`; x ∪ {x} and ω are ST.1, described in F3.1 §05); ℕ row; (M, e, s) row ("(ℕ, 0, S) is one by `ax-natural-numbers`"); new ℕ_ℝ (F3.1 §04–05); A_m, M_m: ω → ℕ.
- **STATUS:** F3.1 rows 206–209 → "ℕ is a Peano system (`ax-natural-numbers`)"; new labels and boxes.
- **Atlas:** none.

## 6. S2a: claims to verify

1. 1.1: (iii) two copies; `prp-peano-predecessor` and its fd2 back-references; the four Quick checks; B1's admissible orders and diagnoses; B3 (T, F, T, T, F); C2 (a)–(e).
2. 1.2: the new recursion proof (R′ closed via (P3), (P4)); the warning's new sentence; `def-omega-arithmetic` (c); R-pairs and R′ Quick checks; the laws Quick check; the fold table without rows (a), (c) still in order; A1; B3 (T, F, F, T, F).
3. 1.3: proposition before theorem with no forward citation; new (f); new `thm-omega-order` proof and (c), (e); well-ordering via {0, …, n}; the four Quick checks; warning; A1, B1, C2 (both defects of line (5)).
4. 1.4: table; edited proof; φ = S; (iii) n ↦ (n, a); ψ = id; the two new Quick checks; B3 (T, T, F, T, F); C2 on the new structure and its new citation; corollary substitutions; edited 14:233.
5. 1.5: every factual sentence; both Quick checks; A1–C1 ((0, 1) = {1, 2}); R1–R3.
6. After S3: no Chapter 1 `@label` to a parked label or past Chapter 1; no Chapter 1 entry in `known-unresolved.json`; labels unique (`blueprint/check_blueprint.py`).

## 7. Notes for S3 and S4

- **Drafters** (one workflow at a time; Opus):
  - **(A) 1.1, 1.2.** Sidecars `fd3/verify/ch01/`: update `exm-peano-axioms-independent.py`, `exr-peano-properties-b2.py`, `def-omega-arithmetic.py`, `thm-omega-arithmetic-laws.py`, `exr-recursion-and-arithmetic-a1.py`, `-b1.py`, `-c3.py`; new `prp-peano-predecessor.py`, `exr-peano-properties-c2.py` (rows truncated at 30), `exr-recursion-and-arithmetic-b3.py`.
  - **(B) 1.3, 1.4**, after (A). Update `thm-omega-order.py`, `prp-omega-order-arithmetic.py`, `prp-omega-powers-parity.py`, `exr-order-on-omega-a1.py`, `-b2.py`, `-c2.py`, `thm-peano-categoricity.py`, `exr-categoricity-a1.py`, `-b1.py`, `-b2.py`; new `exr-categoricity-b3.py`.
  - **(C) 1.5** with R1–R3; new `exr-where-n-comes-from-b1.py`, `-b2.py` (frozensets).
  - **Coordinator:** index last; R4 parking; `known-unresolved.json`; NOTATION, STATUS; ledgers (`tools/ledger.py`).
- **Checks:** `./build.py check` (fd1–fd5, an1); `check_structure.py --book fd3` (0 fatal, `--words`); forward-deps.
- **Review:** changed-only blind review of all of Chapter 1 (all F), then S7 (S7r), round 2 by hand, minor revisers on Sonnet. Merges and S9 stay with the author.

## S2 replies (round 1)

Two blind referees (R1: 16 findings; R2: 14 findings). Duplicates are answered once. Line references checked at `b401a06`; fd1/fd2 labels grepped.

**Errors**
1. **Old Quick check 13:107–113 survives (R1.1).** Applied: added to §3.3 item 1's delete list; the new Quick check of item 4 replaces it.
2. **13:175 "5 − 2 = 3, by the Quick check" (R1.2, R2.4).** Applied: the pointer becomes "by the example after @def-omega-order" (2 + 3 = 5, above). The Quick check keeps 3 ≤ 5 and now also states 5 − 3 = 2.
3. **Fold 14:231–235 (R1.3).** Applied: 14:233's Replacement clause → "such families are left to *Axiomatic Set Theory*"; every "dictionary" in 14:229–235 → "the citing rule above".
4. **1.5 C1 citation (R1.6).** Applied: C1's last sentence now proves ℕ_ℝ least from the set form of @fd1:ax-induction (the remark opening fd2 3.1, verified). 1.1's second failed attempt reworded: @fd2:prp-smallest-closed-set gives a smallest closed subset of ℝ, and identifying it with ℕ_ℝ needs ℝ.
5. **1.3 C2 line (5) also circular (R1.7, R2.2).** Applied the "accept both" option: line (5) stays (a natural fake); the solution names the missing case (N7) and the circular reliance on @thm-omega-order (b) (N9); the repair goes through @prp-omega-order-arithmetic (a); the scheme gives the classification points for either.

**Gaps**
6. **1.1 re-teaches fd2 (R2.1).** Applied: the scratch work keeps the new point (choosing a subset inside an abstract M); the disjunction is credited to @fd2:lem-naturals-arithmetic (c), the unused hypothesis to @fd2:exm-predecessor-no-hypothesis, one clause each; the box's clause carries the credit; "Carry a disjunction" dropped from Named moves; section budget ~1,000, 1.1 total ~3,800.
7. **R1 "this section … dictionary" (R1.4, R2.7).** Applied in §3.5 item 6.
8. **1.4 C2 edit underspecified (R1.5).** Applied: full statement on ℕ × {a, b, c}, (k, 2) → (k, c), (0, 2) → (0, c), and 14:350 cites @exr-peano-properties-c2 (b), (d).
9. **1.4 B3 (b) duplicate, resting on the 14:86 remark (R2.3, R1.15).** Applied: replaced by the recursion item f(0) = 0, f(n + 1) = f(n) + 2n + 1, f = n · n (true, by step (2) of the box). Truth pattern unchanged.
10. **1.2 paragraph pre-empts R3 (R2.5).** Applied: the unique-readability clause dropped from 1.2; R3 makes the link.
11. **Quick-check density (R2.6).** Applied: 1.2 + R′ check (after the proof) and the (km)n check (after the laws); 1.3 + "4 < k < 5" (after `thm-omega-order`) and 2^3 (after the powers definition); 1.4 + the f = g check (after the box) and the φ(2 + 3) check (after `prp-isomorphism-preserves-arithmetic`); 1.5 + "Is {{0}} a pair?". Counts now 1.1: 4, 1.2: 4, 1.3: 4, 1.4: 3, 1.5: 2.

**Minor**
12. **1.1 B1 order not unique (R1.8).** Applied: the solution lists the admissible orders ((iv) floats before (vi)).
13. **Idea for (f) (R1.9).** Applied: "by induction on m, the first factor, using law (e) … (step (4) of the box)".
14. **1.3 B1 converse (R1.10).** Applied as proposed.
15. **"Def"/"IH" key (R1.11).** Applied: 12:238's last sentence opens the fold.
16. **R Quick check placement and C3 pointer (R1.12, R2.11).** Applied: the check moves to right after "After the proof"; C3 points to "the first Quick check after @thm-omega-recursion".
17. **Line references (R1.13).** Applied: 12:302, 12:51–55.
18. **1.1 C1 "inductive", (P2) (R1.14).** Applied as proposed.
19. **Duplicate Prove-or-disprove items (R1.15, R2.10).** Applied: 1.1 B3 (c) → "every x ≠ e is s(y) for some y ≠ x" (true, by @prp-peano-predecessor (a), (b)); 1.2 B3 (c) → the look-alike m(n + 1) = mn + n (false; pattern now T, F, F, T, F). 1.1 A1 (d) and B1's distractor (vii) both touch surjectivity; kept, since one is a recall item and the other a wrong line to reject.
20. **Binding rule 1 vs exercises (R1.16).** Applied: rule 1 names 1.4 B2 and 1.5 C1.
21. **ZF list reads as complete (R2.8).** Applied: "the ones this construction uses", plus one clause for replacement, foundation, choice.
22. **Terms and Time (R2.9).** Applied: the three 1.5 terms go to the Summary only; Time ~20/28.
23. **fd1 7.6 back-reference (R2.12).** Applied: one sentence after (iii) cites @fd1:exm-non-standard-naturals and fd1 7.6's [Looking ahead].
24. **1.3 warning (R2.13).** Applied: 5 · 0 = 2 · 0, yet 5 ≠ 2, tied to (f); (e) explained separately.
