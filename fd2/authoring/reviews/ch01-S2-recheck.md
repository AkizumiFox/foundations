# Chapter 6 — S2a statement referee, recheck after the logic split

Blueprint: `authoring/blueprints/ch06.md` (hand-written). Recheck of 2026-09-28 against the drafted `src/` (Chapter 1 connectives-and-derivations, Chapter 2 negation-and-classical-logic, Chapter 3 semantics-soundness-completeness, Chapter 11), the hand-written blueprints of Chapters 4, 5, 7, 8, `blueprint/book.yaml`, and the reference books.

Evidence files (scratch, not in the tree):
- derivations: `/tmp/claude-1000/-home-akizumi-coding-analysis/8d99e54f-c6f3-4bed-98e0-b546ef5dc565/scratchpad/ch06-S2a/deriv.md` (`python3 tools/check_fitch.py` on it: 4 derivations, 0 errors, 0 notes);
- brute force over all subsets of a 3-element universe and all maps between sets of size ≤ 3: `.../ch06-S2a/brute.py` (every set law, image/preimage law and count below; all pass).

Edits were applied to the blueprint for every finding marked **applied**. `.venv/bin/python blueprint/check_blueprint.py 6`: 0 problems before and after.

Verdict counts: **correct 62, minor 15, gap 6, error 1.** All gaps and the error are fixed in the blueprint; no finding is left open.

---

## 1. Cited labels (do they exist, and say what the route needs?)

| Label | Where | Statement found | Verdict |
|---|---|---|---|
| `prp-distributivity` | src ch01 §07:207 | \(P\wedge(Q\vee R) \dashv\vdash (P\wedge Q)\vee(P\wedge R)\) — **only ∧ over ∨** | correct as far as it goes; see G1 |
| `prp-de-morgan` | src ch02 §05:315 | (a)–(d); (d) \(\neg(P\wedge Q)\vdash\neg P\vee\neg Q\) is the classical one | correct; see G1 for how it is used |
| `prp-iff-two-implications` | src ch02 §04:112 | both directions | correct |
| `prp-contrapositive` | src ch02 §03:56 | \(P\to Q\vdash\neg Q\to\neg P\) | correct (the working form of injectivity) |
| `prp-vacuous-implication` | src ch02 §01:154 | \(\neg P\vdash P\to Q\) | correct (∅ ⊆ A; `prp-empty-set-unique`) |
| `thm-soundness`, `cor-refuting-row` | src ch03 §05:124, 266 | as assumed | correct; role in R2 clarified (M11) |
| `prp-excluded-middle`, `def-rule-raa` | src ch02 §05:225, 43 | as assumed | correct (R3; now also §05, M9) |
| `def-bounded-quantifier`, `def-rules-universal`, `def-rules-existential`, `def-unique-existence`, `prp-unique-existence-use`, `prp-quantifier-negation`, `prp-negated-implication`, `prp-bounded-quantifier-negation`, `prp-exists-forall-swap` | ch04 blueprint (lines 43–46, 285, 342–344) | as assumed; `prp-quantifier-negation` (a) classical; bounded form keeps the bound | correct, but not in `src/` (G6) |
| `def-levels-of-proof`, `def-silent-steps`, `exm-not-allowed-catalogue` (N1, N4, N5, N7) | ch05 blueprint (lines 115–120, 158–171) | entries (N1) instances→∀, (N4) reused witness name, (N5) converse, (N7) missing case: match every use in ch06 | correct, but not in `src/` (G6) |
| Section pointers "Ch 4 §03–§06, §09", "Ch 5 §03, §04, §05" | ch04/ch05 blueprint headings | ∀E, ∀I, ∃I, ∃E; quantifier laws; levels; reading; writing | correct |
| Newly cited for G1: `prp-and-commutes`, `prp-and-associative` (ch01 §03), `exm-disjunction-first-derivations`, `exm-disjunction-regroup` (ch01 §07), `def-derived-rule` (ch02 §03), `prp-standard-equivalences` (ch03 §04:162, clauses (b),(f),(g),(h)), `thm-completeness` (ch03 §06:396) | src | read and confirmed | added to Allowed prerequisites |
| Later-chapter hooks: Ch 8 thm-surjection-right-inverse / ax-choice (§03), prp-power-set-count (§01), exm-reals-open-interval with \(x/(1+\abs x)\) (§05); Ch 7 §04 relations and \(R^{-1}\) (its C1), §03 recursion; Ch 11 §05 ℕ as \(\{x\in\nR: x\in S \text{ for every inductive } S\}\), Ch 11 §03 \(-A \coloneqq \{-a : a\in A\}\) | ch07/ch08 blueprints, src ch11 | all delivered as the promises say; ℕ is a relative intersection inside ℝ, which `def-family-union-intersection` covers | correct |

## 2. Findings

### E1 (error, applied) — `def-function` versus `prp-function-equality` (§04)
The blueprint defines a function as a relation \(f\subseteq X\times Y\) (a set) and then states `prp-function-equality`: equal iff same domain, **same codomain** and same values. Counterexample: the graph of \(x\mapsto x^2\) as \([0,\infty)\to\nR\) and as \([0,\infty)\to[0,\infty)\) is one set, so by `def-set-equality` the two "functions" are equal, while the proposition (and `exm-square-three-ways`, "same rule, three functions") says they differ. **Fix applied:** a function from \(X\) to \(Y\) is the pair \((G, Y)\) of its graph and declared codomain (one sentence on the page, \(f\) written for both); route for `prp-function-equality` via the characteristic property of pairs and `def-set-equality`. The lead sentence now says "given by a relation (its graph)". Families become functions \(I\to\powerset X\) (M15).

### G1 (gap, applied) — `thm-set-algebra` route
The route said "distributivity from `@prp-distributivity`, the difference laws from `@prp-de-morgan`" and promised a table giving, for each law, "the Chapter 1, 2 or 3 equivalence it comes from". (i) `prp-distributivity` is only ∧ over ∨; no Chapter 1–2 label derives ∨ over ∧, which \(A\cup(B\cap C)=(A\cup B)\cap(A\cup C)\) needs. (ii) Commutativity and associativity of ∨ are only worked examples (`exm-disjunction-first-derivations`, `exm-disjunction-regroup`). (iii) Neither difference law is De Morgan alone: \(x\in A\wedge\neg(x\in B\vee x\in C)\) needs De Morgan (a)/(b) plus regrouping; \(A\setminus(B\cap C)\) needs De Morgan (d), classical, plus distributivity. **Fix applied:** the table cites `@prp-standard-equivalences` (b),(f),(g),(h) for every law, the Chapter 1–2 derivation where one exists, and the uniform licence `prp-standard-equivalences` → `@thm-completeness` → `@def-derived-rule` (substituting \(x\in A\) etc. for letters). The classical step in the second difference law is to be named. Brute force: all six laws hold on all \(8^3\) triples of subsets of \(\{1,2,3\}\).

### G2 (gap, applied) — `thm-left-inverse-iff-injective` hypothesis placement (§05)
The theorem was stated under the global hypothesis \(X\ne\emptyset\). `thm-bijection-iff-inverse` (⇐) needs "left inverse ⇒ injective" for every \(f\), including \(f\colon\emptyset\to\emptyset\) (bijective, with inverse ∅→∅). A route citing the theorem there would violate its hypothesis. **Fix applied:** (a) left inverse ⇒ injective, no hypothesis; (b) \(X\ne\emptyset\) and injective ⇒ left inverse; the (⇐) route of `thm-bijection-iff-inverse` now cites (a) and `prp-right-inverse-surjective`. Hypothesis check: \(X\ne\emptyset\) is needed in (b) (empty function \(\emptyset\to\{1\}\): injective, no left inverse, as the blueprint already says); it is redundant in (a).

### G3 (gap, applied) — `prp-product-set-laws` lacks the mirror-image laws (§03)
Stated only with the varying factor on the right. §03 B1 rewrites \([0,2]\times[0,1]\) using \((B\cup C)\times A\), and `prp-empty-function` needs \(\emptyset\times Y=\emptyset\) (the only relation \(\subseteq\emptyset\times Y\) is ∅). **Fix applied:** the mirror laws are stated (same proofs). All eight laws pass brute force.

### G4 (gap, applied) — source policy: exercises copied from Hammack and Velleman
Our blueprint says "none of [Hammack's] exercises is reused", and STYLE §0 forbids copying exercises. Found:
- §03 B3 \((A\times B)\cap(C\times D)=(A\cap C)\times(B\cap D)\) = Hammack §9.3 exercise 6 (`Hammack .../sections/047-9.3-Disproof-by-Contradiction.md:47`);
- §03 C1 \((A\times B)\cup(C\times D)\) vs \((A\cup C)\times(B\cup D)\) = Hammack §9.3 exercise 5 and ch. 8 exercise 25 (`.../047...md:46`, `.../045-Exercises-for-Chapter-8.md:41`);
- §03 C2 \(A\times B=B\times A\) iff \(A=B\) or one is empty = Velleman Theorem 4.1.4 (`Velleman .../sections/050-Example-4.1.2..md:83`);
- §02 C1 first part \(\powerset A\cap\powerset B=\powerset{A\cap B}\) = Hammack §9.3 exercise 14 (`.../047...md:55`).
**Fix applied:** §03 B3 → \((A\times B)\cap(B\times A)=(A\cap B)\times(A\cap B)\); §03 C1 → \((A\cup B)^2\) vs \(A^2\cup B^2\) (witness \((1,2)\) with \(A=\{1\},B=\{2\}\)) and the exact four-term formula; §03 C2 → "\(A\times B\subseteq B\times A\) iff \(A=B\) or \(A=\emptyset\) or \(B=\emptyset\)" (one inclusion forces equality; marking scheme updated); §02 C1(a) → \(\powerset{A\setminus B}\) vs \(\powerset A\setminus\powerset B\) (never equal: ∅), with the non-empty-subset inclusion. All four new claims brute-forced. The \(\powerset A\cup\powerset B\) "iff" part stays (Hammack proves only ⊆ in Example 8.8; the characterization is standard, and the wording is ours). Huth & Ryan (the logic reference) has no set-theory material that overlaps. R3's sequent is a relative of H&R Example 1.23 (\(p\wedge\neg q\to r,\ \neg r,\ p\vdash q\), `Huth & Ryan .../sections/005-1.2-Natural-deduction-19.md:140`) but not the same sequent. Ours has no \(\neg r\) premise and concludes \(p\to(q\vee r)\), and the set reading is ours. It is kept, see M17. The image/preimage identities (§06) are standard theorems, common property.

### G5 (gap, applied) — R4 uses \(\bigcup S\), which was not defined, and \(S\) may contain non-sets
`def-family-union-intersection` defined only \(\bigcap\sS\) for unindexed sets of sets. R4's solution takes \(\bigcup S\) for an arbitrary \(S\) containing every singleton, whose elements need not all be sets (numbers are familiar objects). **Fix applied:** the definition adds \(\bigcup\sS\) for a set \(\sS\) of sets. R4's solution first cuts \(S\) down to its singletons by specification. The argument is then valid: \(x\in\{x\}\in T\), so \(\bigcup T\) contains every set, against `thm-russell`.

### G6 (gap → process note, applied) — Chapter 4/5 labels are not in `src/`
Twelve Chapter 4 labels and three Chapter 5 labels are cited with `@`. They exist in the hand-written blueprints, so `check_blueprint.py` accepts them, but `src/` has no Chapter 4 or 5. The wave instructions say not to `@ref` them. **Fix applied:** a drafting note under Allowed prerequisites says to write each as a prose pointer, record it as a STATUS promise, and let S8 convert it.

### Minor findings (applied unless marked "recorded")
- **M1** `prp-empty-set-unique` was routed through "each is a subset of the other", i.e. `prp-subset-antisymmetric`, which the section prints later. The route now goes through `def-set-equality`, `@prp-vacuous-implication` and `@prp-iff-two-implications` directly.
- **M2** \(\bigcup_i A_i=\{x:\exists i,\ x\in A_i\}\) is a set-builder with no ambient set, right after §01 says every set-builder names one. The blueprint now says the union exists by the "unions" working rule (now listed for families), and gives the ambient form when all \(A_i\subseteq X\).
- **M3** `thm-de-morgan-families`' second law, ⊆ direction, needs the **bounded** negation \(\neg\forall i\in I \vdash \exists i\in I\,\neg\). The citation is now `@prp-bounded-quantifier-negation`, whose classical direction rests on `prp-quantifier-negation` (a). The A1(a) answer is updated to match.
- **M4** §02 A1(d): \(x\notin\bigcap_iA_i\) is "\(x\notin X\) or \(\exists i,\ x\notin A_i\)" because the intersection is taken inside \(X\). The question now says "for \(x\in X\)", and the answer is written out.
- **M5** §02 B3 used \(B\triangle C\), which the chapter never defines. It is now stated in words.
- **M6** §03 A1(b): "\((1,2)\ne 1\)" does not follow from the characteristic property. The solution now names the convention that numbers and pairs are different objects.
- **M7** §03 B1's answer was missing. Added: \([0,1]\times[1,2]\).
- **M8** §04 C2's first part repeated B2's proof. C2 now deduces from C1 and B2, and its example is spelled out.
- **M9** §05: the case split \(y\in f(X)\) / \(y\notin f(X)\) that defines \(g\) is exhaustive only by LEM. The blueprint now cites `@prp-excluded-middle` and names this as the proof's one classical step. It also writes \(g\) as a set by specification.
- **M10** R1's Fitch skeleton was misdescribed ("∀I containing →I containing ∀I"). It is corrected to →I[\(A\subseteq B\)] ⊃ ∀I[\(S\)] ⊃ →I[\(S\in\powerset A\)] ⊃ ∀I[\(x\)] ⊃ →I[\(x\in S\)].
- **M11** R2: the counterexample row gives concrete sets, which are checked by computation. `@cor-refuting-row` is now cited only for "no element-chasing proof can exist". The answer is correct: the rows with \(x\in A\), \(x\in C\) (any \(B\)) differ.
- **M12** Coverage check ran `originality.py 5`. Changed to `6`.
- **M13** §01 C1(b) said "Deduce", but its solution uses the theorem, not (a). Reworded to "Show, from the theorem".
- **M14** book.yaml's binding must-prove list includes "right inverse **iff** surjective (flag choice)". The blueprint proves only (⇒) and defers (⇐) to Chapter 8. This is a deliberate deviation, consistent with the Chapter 8 blueprint (its promise row, line 63), and is now recorded explicitly.
- **M15** "Families are functions on \(I\)" needs a codomain. The blueprint now says a family of subsets of \(X\) is a function \(I\to\powerset X\).
- **M17** (recorded, no blueprint change) R3 is close in shape to Huth & Ryan Example 1.23. The drafter must build the derivation from the goal \(Q\vee R\) (LEM on \(Q\), or RAA on \(\neg(Q\vee R)\), deriv.md D1/D2), not follow H&R's layout or wording.
- **M16** (recorded, no page change) `thm-de-morgan-families`: \(A_i\subseteq X\) is needed only to define \(\bigcap_iA_i\) in the second law; the first law holds for arbitrary \(A_i\).

## 3. Attempts that found nothing (correct)

Each attempt is listed with its small, boundary and degenerate cases.

**§01.** `prp-subset-antisymmetric` (correct). Transitivity of ⊆ (correct; unlabelled, which is fine because nothing cites it). `thm-russell`: the propositional core \(Q\leftrightarrow(S\wedge\neg Q)\vdash\neg S\) is derived **without RAA** (deriv.md D3, checked), so the printed route is intuitionistic as claimed; "no set of all sets": \(R_U\in U\) contradicts; urelements do not break it. `exm-set-builder-small` (\(\{-2,\dots,2\}\); the ⊆ direction needs \(\abs x\ge3\Rightarrow x^2\ge9\) for integers outside, a ledgered school fact). \(\{x\in\nR:x^2<0\}=\emptyset\). \(\{\emptyset\}\ne\emptyset\); \(\{1,1,2\}=\{1,2\}=\{2,1\}\). Non-example \(\{1,\{1\}\}\). Warnings. Quick checks (yes; no; none of ∅, {∅}, {{∅}} equal). A1(b) (true, false, true, false). A1(c) \(\{\pm1,\pm2,\pm3\}\). B1 \((x-1)(x-2)\). B2. B3 (witness 2). C1(a),(b). C2.

**§02.** `def-family-union-intersection` at \(I=\emptyset\) (∪ = ∅, ∩ = X). `thm-de-morgan-families` at \(I=\emptyset\) (X = X, ∅ = ∅). Classical content: only the second law's ⊆. `exm-families-real-parameter` (witness \(x/2\in(0,1)\); \(t=\abs x\); \(t=x\)): no Archimedes. Non-example \([0,t)\) vs \((0,t)\), with 0 lost. Warning witnesses. Quick check (\([0,2]\), \([0,1]\)). A1(b) (integers prime to 6). B1 (deriv.md D4: intuitionistic core). B2 (\([t,1+t]\): union \((0,\infty)\), intersection ∅; \((-t,1/t)\): union ℝ, intersection \(\{0\}\); both without Archimedes). C1(b) "iff" (brute force). C2 counterexample \(A=B=\{1\}\), \(C=\emptyset\), \(x=1\), and the repair.

**§03.** Product laws, incl. \(A\times(B\setminus C)\) (brute force). B2's faded step (the characteristic property gives \(b=b'\)). `exm-relations-as-sets` (three pairs for <). Warning witnesses. Quick check. A1(c),(d).

**§04.** `prp-empty-function` (both halves; degenerate \(\emptyset\to\emptyset\) has exactly one function). `exm-not-a-function` (circle at \(x=0\), \(x=2\); \(p/q\mapsto p\)). Composition non-commutative. `exm-square-three-ways` (all three verdicts). `thm-composition-injective-surjective`. Quick check (ℕ from 1, per NOTATION). A1(b) (injective, not surjective). A1(d) 9 and 6 (brute force). B1 (\(x/(1+\abs x)\) and \(y/(1-\abs y)\) are mutually inverse, checked by cases on sign; \((m,n)\mapsto m+n\) misses 1). B2 ordering (no admissible reordering; the distractors fail as stated). B3. C1 (example and marking scheme, total 10).

**§05.** Left inverses of \(n\mapsto2n\). `exm-left-inverse-construction` (two left inverses, depending on \(x_0\): brute force). `prp-right-inverse-surjective`. `prp-inverse-unique` chain. `thm-bijection-iff-inverse` (⇒) without choice. Quick checks. A1(c),(e). B1 (2 and 2: brute force). B2. B3. C1. C2 (4 left inverses: brute force).

**§06.** Hook (\(\{0\}\) vs \([0,1]\)). `exm-images-of-square` (all four). `exm-sets-of-numbers-as-images` (matches Ch 11 §03's \(-A\coloneqq\{-a:a\in A\}\)). `thm-preimage-operations` (all four laws, incl. \(I=\emptyset\): both sides X). `prp-preimage-composition`. `thm-image-union` (\(I=\emptyset\): ∅ = ∅; no Ch 4 ∃∃-swap label exists, so the inline swap is needed). `thm-image-intersection` (⇒ via singletons; brute force of "equality for all A, B iff injective"). `prp-image-preimage` (both "iff"s and \(f(f^{-1}(B))=B\cap f(X)\): brute force). `exm-image-two-witnesses` (\(A=\{-1\}\), \(B=\{1\}\)). Quick check (\(\{-2,2\}\), ∅, \([0,1]\)). A1(b) (\([-2,-1]\cup[1,2]\) both ways). B1 (\(m-n\) over \(m>n\) gives ℕ; codomain ℤ). B3. C1 (inclusion; the witness \(A=\{-1,1\}\), \(B=\{1\}\); "iff injective": brute force). C2 (counterexample to the step; repair). C3 (marking scheme totals 10). R3: \((P\wedge\neg Q)\to R\vdash P\to(Q\vee R)\) derived both via RAA (D1) and via LEM (D2), both checked by the checker; the set reading "if \(A\setminus B\subseteq C\) then \(A\subseteq B\cup C\)" is correct; with \(R=\bot\) the sequent is not intuitionistically valid, so "needs LEM or RAA" is right.

**Promises.** Every row of "Promises this chapter pays" is covered by the label named; the Ch 11 S8 row (ℕ as ⋂) is present. Promises opened: Ch 8 delivers thm-surjection-right-inverse (ch08 blueprint lines 63, 126).

## 4. Hypothesis audit (each must-prove statement)
- `thm-left-inverse-iff-injective` (b): \(X\ne\emptyset\) is needed (empty function into \(\{1\}\)). (a): no hypothesis.
- `thm-de-morgan-families`: \(A_i\subseteq X\) is needed for law 2 only (M16). \(I\) arbitrary, including ∅.
- `thm-preimage-operations`, `thm-image-union`, `prp-image-preimage`, `prp-preimage-composition`, `thm-composition-injective-surjective`, `prp-inverse-unique`, `thm-russell`: no hypotheses, and none needed.
- `thm-image-intersection`: "for all \(A,B\)" is essential. For fixed \(A,B\), equality can hold for non-injective \(f\) (e.g. \(A=B\)).
- `prp-product-set-laws`: none.

Blueprint status after edits: S2a recheck closed. `check_blueprint.py 6` reports 0 problems. Ready to freeze once the ledger entry `authoring/ledger/ch06.yaml` records the hash (outside this stage's write scope).
