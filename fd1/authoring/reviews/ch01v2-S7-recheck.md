# Chapter 1 — S7 re-referee (fresh)

**Scope:** commit `4cc9af0` (`src`, `verify`, `authoring/NOTATION.md`, `authoring/STATUS.md`) against every finding of `ch01-S5-A.md`, `ch01-S5-B.md` and `ch01-S6.md`, with their Resolution notes. Re-referee has not written or reviewed Chapter 1 before. Verdicts recorded in `authoring/ledger/ch01.yaml` (stage S7r, by rereferee).

**Gates re-run:** `check_fitch.py src/ch01-propositional-natural-deduction`: 104 derivations, 0 errors. All `verify/ch01/*.py` sidecars exit 0. `check_numbers.py`: 89 sidecars, 0 fatal. `check_structure.py`: 0 fatal, 3 advisories (word counts, as before). `promises.py --reconcile`: the one unrecorded promise is Ch 10 §07 → Ch 15; no Ch 1 promise unrecorded. `ledger.py stale 1`: 0 stale.

**Unintended changes:** none. Every hunk in the diff maps to a finding below. `build/tikz.py` is not in this commit (R1 was fixed in `ade6b9e`).

**Counts:** 27 finding rows re-checked (25 distinct; 05:201 and 03:373 were raised by both S5 referees). Fixed correctly: 26. Fixed but introduced a new problem: 1 (minor). Not fixed: 0. No fix rejected.

## S5 Referee A

| Finding | Verdict | Evidence |
|---|---|---|
| 06:66 `def-rule-raa` (gap): "RAA is never needed to prove a negation" | fixed correctly | The new sentence claims only what the argument shows: "the **last** step of a derivation of a negation never needs RAA, though steps inside its box still may". It no longer claims anything that fails with quantifiers. The only later use, 06:198 (an inner goal that is a negation, where the RAA can be avoided), is a last-step use, so it is still covered. No other occurrence (grep "never need"). |
| 03:373 `exm-cases-on-hypothesis`: "one place ∨I used for something other than finishing a case" | fixed correctly | The claim is now "manufactures the hypothesis of a premise". I scanned every `\oi` in §03, exercises included. Only lines 3→4 and 7→8 of this derivation feed a ∨I line to →E as the hypothesis of a premise. Distributivity (lines 5 and 10) and regroup (3 and 7) do not, and neither do A1(d), B1 or B3. |
| 04:193 `def-derived-rule`: expansion needs iteration | fixed correctly | Adds "If the copy itself uses derived rules, expand those lines in the same way; this stops, because each derivation cites only results proved before it." Well-founded, and it fits the pasting argument just before it. |
| 05:177 `exm-iff-negations`: informal reason, not marked | fixed correctly | The reason is now concrete: in the box of P the goal is Q, and a box on ¬Q reaches ⊥ and so closes to ¬¬Q, not Q. The claim is marked "we state it without proof, and nothing depends on it", and it is added to §05's dependency ledger. The claim is true: a two-world Kripke model with P forced only at the top and Q everywhere makes ¬P ↔ ¬Q forced but not P ↔ Q. The phrase "a box on ¬Q ends in ¬¬Q" is loose (the box ends in ⊥; closing it gives ¬¬Q), but it is not wrong. |
| 05:201/225 `thm-squares-order`: "used by one direction each" | fixed correctly | Lead-in: "each hypothesis is needed: dropping either one breaks one of the two directions". True, by the witnesses (−2, 1) and (1, −2). Remark: (⇒) "needs" x ≥ 0, and the proof's use of y ≥ 0 "already follows from y ≥ x ≥ 0". True. (⇐) "used only y ≥ 0": the proof at 05:217 uses y ≥ 0 (for x > 0 and for y² ≤ xy) and never x ≥ 0. This agrees with C2(a) (05:505). |

## S5 Referee B

| Finding | Verdict | Evidence |
|---|---|---|
| R1 (error) SVGs uncropped | fixed correctly (outside this diff) | Fixed in `ade6b9e`: `build/tikz.py:58–61` drops standalone's `tikz` option. Of the 100 newest files in `_build/html/tikz`, 98 have cropped viewBoxes. The 2 full-page files (`fe1be3c1…`, `e42b9d2d…`, dated 15:50, before the fix) are referenced by no page. They are stale cache. |
| R2 04:3 break before comma | fixed correctly | The comma is removed ("has square 2 or that x²+1 is never 0"). The sentence is still grammatical. The engine-level cause is acknowledged and remains. |
| R3 (gap) STATUS promise table | fixed correctly | `promises.py --reconcile` records every Ch 1 promise. Spot-checked: differentiable ⇒ continuous is §05:281 → Ch 16. The ¬¬P ⊢ P row points to Ch 2 `thm-raa-independent` (optional, `blueprints/ch02.md:39,144`), as 05:92 and 06:27 do. The history row points to Ch 4 final section. The dropped rows ("prime divisor", "outside its box → Ch 3") have no occurrence in the prose. |
| R4 blueprint deviations | fixed correctly | STATUS "Blueprint deviations" lists the six labels for S2a. |
| R5 NOTATION rows | **fixed, new minor problem** | The `\abs` row is correct (§01:363 C2 defines \|x\| by cases; §03 displays it). The new `d \mid n` row says "first used Ch 1 §05, C1". But §04:596, in the fatal errors of `exr-negation-and-contradiction-c1`'s marking scheme, already writes "6 ∣ n² ⇒ 6 ∣ n". That use comes before the definition at §05:451 and has no gloss. Fix: in §04:596 write "6 divides n² ⇒ 6 divides n" (as B3 does), or change the row's first use. The `\mathsf{X}`, `\mathsf{Y}` row matches §06:459. |
| R6 index:18 Roadmap | fixed correctly | "why reductio, double-negation elimination and excluded middle stand or fall together" names the three rules of `thm-classical-rules-interderivable`. |
| R9 §06 A1 lacks a part on the theorem | fixed correctly | The new A1(g) asks which rule justifies line k of ② and why the box is unchanged. Answer (g): ¬I, because the box opens with ¬P and ends in ⊥, and both rules ask only for such a box. This matches the schema at 06:480–495 (line k is `\ni{i-j}`) and the proof's own sentence. It is a fair A-level comprehension part. It does not duplicate the *Before reading on* question, which is on ③. |
| 07:594 A1(a) contrapositive note | fixed correctly | "Suppose x ≥ 0" inside the frame opens an RAA box on the goal x < 0: it is the exact negation for reals, as the 06:68 warning requires. The contrapositive route proves x ≥ 0 → x³ ≥ 0, and CP gives ¬(x³ ≥ 0) → ¬(x ≥ 0), that is, x³ < 0 → x < 0. Correct. |
| 06:804 C2(a) "(d)" | fixed correctly | "part (d) below". |
| 06:239 "The next two results use it that way" | fixed correctly | "The paragraph after the next result" is 06:371, which gives the LEM route to DM (d) and follows the DM proof directly. "Part (b) of the result after that" is `prp-implication-as-disjunction` (b), which uses LEM. Both are true. |
| 05:92 vs 06:27 | fixed correctly | "and Chapter 2 proves it". This agrees with 06:27 and with the ch02 blueprint (optional `thm-raa-independent`), and is ledgered in §05. |
| 05:201, 224 | fixed correctly | See S5-A row. |
| 05:488 C1 scheme "B3" | fixed correctly | Now "part (a) of @exr-negation-and-contradiction-b3". B3(a) (04:512) is exactly 3 ∣ n² ⇒ 3 ∣ n. |
| 03:373 | fixed correctly | See S5-A row. |
| 03:617–625 dependency ledger | fixed correctly | "Even prime" is removed. The new entries (a = 0 or b = 0 ⇒ ab = 0; even or odd; t² ≥ 0) are exactly the facts A1(b) invokes (03:395–398), and the soundness pointer is the one in A1(d) (03:426). §05 now ledgers the warning's soundness pointer (05:135), the ¬¬P ⊢ P claim and the converse claim of `exm-iff-negations`. |

## S6

| Finding | Verdict | Evidence |
|---|---|---|
| 1 `exr-statements-and-connectives-b1` answered at 01:88 | fixed correctly | The prose example is now "2 is prime but not odd", which is a true conjunction. B1(a) is no longer quoted. It resembles A1(c) ("n is prime but not even", 01:251) in form. That is acceptable for an A item that rehearses the text, and the prose gives no symbolisation. |
| 2 `check:02-…:2` spoiled B3(a) | fixed correctly | The check now asks about P → (Q∧R) ⊢ (P→Q) ∧ (P→R). The answer "two" is right: ∧I opens no box, and each implication needs its own →I box, closed with Q or with R. One box cannot yield two implications. The derivation sketched (→E on the premise, then ∧E) is valid. The sequent occurs nowhere else in the chapter (grep). B3(a) is no longer spelled out in advance. |
| 3 02 C2 Hint 2 too direct | fixed correctly | It now names the tool (→I, and what it needs) and does not execute the third box. The ladder escalates from Hint 1. The solution and marking scheme are unchanged and still grade fairly. |
| 4 04 C1 Hint 2 gives key idea | fixed correctly | It now says "imitate the shape" of `thm-square-even-implies-even` for 3q² and q. That proof goes through "odd ⇒ square odd" and DS, and the imitation gives "q odd ⇒ 3q² odd", which is the solution's step. The hint does not suggest the fatal error ("applying" the theorem to q). |
| 5 05 C1 scheme and Hint 2 | fixed correctly | The @ref is fixed. The alternative-cycle allocation, 1 + 3·3, sums to 10, and the book's own allocation, 1 + 2 + 3 + 4, sums to 10. The new Hint 2 ("the two halves of (ii) must be used together") names the difficulty of (ii) ⇒ (i) without executing it. The solution uses 2 ∣ n and n = 3b together (05:481). |
| 6 07 C2 scheme penalises RAA | fixed correctly | I wrote the RAA route: ¬G; a ¬I box on Q, with P → Q by repeating Q and ∨I clashing with ¬G, giving ¬Q; a box on Q clashing with ¬Q, then ⊥E, giving Q → P; ∨I, clash, RAA. That is 15 lines, and it matches the scheme's mapping (repeat-box implication, clash-and-⊥E implication, ∨I lines clashing with the RAA assumption). The points are 3 + 2 + 2 + 1 + 2 = 10. The paragraph bullet accepts "the RAA line". The fatal errors still make sense for both routes. |
| 7 check_numbers QUOTED (G3 witnesses) | fixed correctly | In `verify/ch01/prp-peirce.py` and `exr-finding-derivations-b1.py`, the witnesses are now plain constants with the same asserts, and QUOTED holds only numbers the text states (15, 8; none for Peirce). Both scripts pass, and `check_numbers` reports 0 fatal. The text quotes no three-valued value (07:348, 07:642 state the claims without proof). |

## Open item from this re-check

- **R5 / `exr-negation-and-contradiction-c1` (minor):** §04:596 writes `6 \mid n^2 \Rightarrow 6 \mid n` before `d \mid n` is defined (§05:451). This contradicts the new NOTATION row "first used Ch 1 §05, C1". Write it in words at §04:596, or define it there and move the row's first use.
