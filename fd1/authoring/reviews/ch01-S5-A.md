# Chapter 1 — S5 Referee A (proofs)

**Scope:** `src/ch01-connectives-and-derivations/` §01–§07 and index (read-only), against the binding blueprint `authoring/blueprints/ch01.md` (S2 v3, `authoring/reviews/ch01v3-S2.md`); STYLE §4, §10, §11; NOTATION "Logic (Part 0)"; `latex/fitch-book.sty`.
**Referee:** A (proofs), blind to Referee B. Verdicts are **not** written to `authoring/ledger/ch01.yaml` (the reviser records them).
**Build copy:** `/tmp/claude-1000/-home-akizumi-coding-analysis/8d99e54f-c6f3-4bed-98e0-b546ef5dc565/scratchpad/S5a-ch01/` (rsync of the tree, `.venv` and `_build` excluded).

## Method

- `python3 tools/check_fitch.py --notes src/ch01-connectives-and-derivations`: 119 blocks (7 expect-invalid, 29 schema), **0 errors**, 118 notes. Every note was read: all are skipped schema lines, `\vdots` gaps, or text justifications (`Tr`, `Sh`, `Flip`, `algebra`, `(i)`–`(iv)`, `?`, `∧E*`), each hand-checked below.
- **Hand-checked** every `% schema` block (the rule schemas of §02 Tr/Sh, §03, §04, §05 →I and R (two drawings), §06, §07 and the §07 reference page, §03 C2(d) ∧E\*; the partial derivations 03:173, 04:163, 07:876; the unjustified A1 grid 02:323) and every `% expect-invalid` block (03:353, 03:551, 04:456, 05:257, 05:696, 07:135, 07:599): each fails exactly at the line and for the reason the text names. The two unmarked deliberately invalid blocks (02:280, 02:476, forward citation written as literal text) were checked by hand: each line is an instance of Tr and the only fault is the forward citation, as the text says.
- **Rule-order check** (the critical check): a script (`scratchpad/rules.py`) listed every rule macro in every non-schema `nd` block per file against the rules available at the end of that section (§02: Tr/Sh/Flip only; §03: ∧I, ∧E; §04: +→E; §05: +→I, R; §06: +∨I; §07: +∨E). **No violation. No `\open` before §05. No `\neg`, `\bot` or `\leftrightarrow` in any derivation of the chapter**, and no negation rule macro (`\ni \ne \be \raa \nni \nne \mt \lem \ds \dm \ctp`) anywhere. Prose proofs were read for the same condition: §03–§04 prose uses only ∧ and →E; the §05–§06 examples use boxes only from §05 on; ∨E appears only in §07. Negation occurs only as notation in §01 (translation, parsing) and as the atomic reading `x ≠ 0` at 07:275, never as a step.
- **Cross-references:** every `@label` in the chapter resolves to a label defined in the chapter (scripted diff, empty). No `@ref` outside the chapter; pointers to Chapter 2 are prose only (checked: 04:33 "Section 2.3 returns to this card" is paid by `src/ch02-negation-and-classical-logic/03-derived-rules.md:279`).
- **Sidecars:** all 72 scripts in `verify/ch01/` run with exit 0.
- Every proof and Idea: reason for each step, hypotheses used, one dropped-hypothesis counterexample attempt per result (table below). Every meta-argument and every "needs / does not need / cannot" claim checked (table below).
- Earlier findings (`ch01v2-S5-A.md`, `-S5-B.md`, `-S6.md`, `-S7-recheck.md`, `-S8-seam.md`): the one v2 finding that concerned material now in this chapter (v2 03:373, "the one place where ∨I…") has **not** returned: 06:247 now says "the first place in this section … it will not be the last", which is true (06:312, 06:479, 06:540, 06:558 do the same). The other v2 A findings concern Chapter 2 material (derived rules, RAA, `thm-squares-order`, `exm-iff-negations`) and are out of scope here.

**Counts (Findings table):** correct 148 · minor 4 · gap 0 · error 0. (Two of the minors, 06:100 and 06:204, also appear in the meta-argument table; they are counted once.)

## Dropped-hypothesis counterexample attempts

Propositional counterexamples give a valuation making the remaining premises true and the conclusion false (so, by soundness, Chapter 3, no derivation exists).

| Result | Hypothesis dropped | Attempt | Outcome |
|---|---|---|---|
| `prp-and-commutes` (03:164) | the premise P∧Q | ⊢ Q∧P: P, Q false | fails without it; premise used (lines 2, 3) |
| `prp-and-associative` (03:216) | the premise | ⊢ P∧(Q∧R): all false | premise used at lines 2–5 |
| `prp-implication-transitive` (05:75) | Q→R | P→Q ⊢ P→R: P, Q true, R false | fails; both premises cited (lines 4, 5) |
| same | P→Q | Q→R ⊢ P→R: P true, Q, R false | fails |
| Remark 05:123 | conjunctive premise | ⊢ P→R: P true, R false | fails |
| `prp-curry` (05:392), first | the premise | ⊢ P→(Q→R): P, Q true, R false | fails; premise used at line 5 |
| `prp-curry`, second | the premise | ⊢ (P∧Q)→R: same valuation | fails; premise used at line 5 |
| `prp-distributivity` (07:207), both | the premise | ⊢ (P∧Q)∨(P∧R), ⊢ P∧(Q∨R): all false | fails; premise used |
| `exm-first-boxes` (c) (05:315) | the premise | ⊢ Q→(P→R): P, Q true, R false | fails |
| `exm-cases-on-hypothesis` (07:166) | premise | ⊢ (P∨Q)→R: P true, R false | fails |
| `exm-or-hypothesis-split` (06:214) | premise | ⊢ (P→R)∧(Q→R): P true, R false | fails |
| skeleton 07:324 | P∨Q | P→R, Q→R ⊬ R: all false | fails |
| same | Q→R | P∨Q, P→R ⊬ R: Q true, P, R false | fails (this is exactly 07:598 A1(d), whose instance x = −1 is correct) |
| `exm-product-in-unit-interval` (03:309) | 0 < x | x = −2, y = ½: xy = −1 < 0 | conclusion fails |
| same | x < 1 | x = 3, y = ½: xy = 1.5 > 1 | conclusion fails |
| `exm-abs-at-least-x` (07:349) | premise 1 (x≥0 ∨ x<0) of the derivation | P∨Q-free version: from 2, 3 alone, no line reaches the goal for all x | needed |
| same | premise 3 (x<0 → \|x\|>x) | only case 1 closes; for x = −1 the goal needs it | needed |
| `exm-abs-product-cases` (07:394) | remark \|a\| = −a for a ≤ 0 | case x = 0, y < 0: xy = 0, not < 0; the text itself (07:416) names this hole | correct |
| `exm-triangle-inequality-cases` (07:420) | lemma −a ≤ \|a\| | case x+y<0 cannot bound −x−y | needed; both halves of the lemma used |
| `exm-product-zero` (06:293) | the school fact | ⊢ a=0 → ab=0 as propositional letters: A true, B false | fails |
| `exm-illegal-citation` (05:252) | (the would-be sequent) P→Q, Q→R ⊢ R | x = 0 with P: x>3, Q: x>2, R: x>1 | the text's own witness is correct |
| 05 C1(c) (05:780) | P→Q… ⊢ R via "R 5" | x = 0 with P: x>2, Q: x>3, R: x>1; premise true for all x | correct |

## Meta-arguments and "needs / cannot" claims

| file:line | claim | verdict | evidence |
|---|---|---|---|
| 02:235 | before §1.5, ⊢ψ holds for no ψ | correct | Tr, Sh, ∧I, ∧E, →E each cite ≥1 line; a list with no premise lines has no citable first line. §05:341 pays it with ⊢ P→P. |
| 02:436–438 | forward chaining uses m−1 applications; "no cleverer derivation does better" stated without proof | correct | count checked (m=3 → 2); lower bound true (each Tr joins two leaves of a binary tree), explicitly not proved, not used. |
| 02:520 | citing only earlier lines rules out loops; citations traced back end at premises | correct | strictly decreasing numbers in {1..n}; with Tr only, a line citing nothing is a premise. The 0<0 loop is two instances of Tr with a=b=c=0. |
| 03:303 | any rearrangement of a ∧-only statement is derivable from any other with the same letters | correct | stated as an observation about the recipe; recipe is complete when every goal letter occurs in the premise. |
| 03:523–531 | C1: no line of a {∧I, ∧E} derivation from P∧Q contains R | correct | first-bad-line argument covers premise, ∧I, ∧E; meta-level "for a contradiction" is legitimate (least element of a finite set). |
| 03:602 | ∧E\* is eliminable | correct | replacement by two ∧E lines; renumbering and redirected citations checked; box-free context so availability = earlier. |
| 04:82 | Chapter 3 proves P→Q, Q ⊬ P for the rules of Chs 1–2 | correct | true by soundness (P false, Q true), RAA included; prose pointer. |
| 04:479 | C1(c): nothing new about D follows from D→E, E with ∧I, ∧E, →E | correct | closure argument is complete: lines are ∧-trees of D→E and E; →E would need the line D, never produced. |
| 05:17 | with ∧I, ∧E, →E an implication stands on a line only as a premise or a piece of an earlier line | correct | ∧I writes conjunctions; ∧E/→E write parts. |
| 05:341 | P→P is the first statement derivable from no premises | correct | see 02:235. |
| 05:450 | inner box closes first, forced by def-derivation | correct | boxes disjoint or nested. |
| 05:682 | B4: the order is the only admissible one | correct | premise first; (vi) needs box ii…i; (i) is a line of that box, so its box ix…iii lies inside; within it ix < viii < iii forced; the swapped nesting proves the premise again. |
| 05:838 | C2: the premise cannot be used until a third box is opened | correct | →E on line 1 needs P→Q on a line; no available line contains it as a part, so only →I (a box) writes it. |
| 06:50, 06:67, 06:568 | ∨I is the only rule so far that builds a disjunction on the spot / whose added side is free | correct | ∧I, ∧E, →E, →I, R checked against their schemas. |
| 06:100 | "choose P, and the subgoal P cannot be reached from Q at all (take P false and Q true)" | **minor** | see Findings. |
| 06:204 | "neither P→Q nor P mentions R, so no rule can take R out of them" | **minor** | see Findings. |
| 06:263–285 | stall on P∨Q ⊢ Q∨P: "we cannot find a derivation" | correct | worded as the blueprint asks (not "none exists"); the displayed 7-line derivation is valid and shows P∨Q ⊢ Q→(Q∨P). |
| 06:417, 07:1013 | choosing the other side would leave an unreachable subgoal | correct | heuristic remarks, each with the side named; semantic reading obvious (P ⊬ R). |
| 07:162 | "different last lines lose nothing" | correct | χ₁∨χ₂ reachable by ∨I at the end of each box; B3 (07:696) carries it out. |
| 07:625 | A1(d): the gap cannot be filled; instance x = −1 | correct | flagged as relying on Chapter 3; instance P: x>1, Q: x<1, R: x>0 checked. |
| 07:772 | a sign split needs four cases | correct | with one sign fixed, \|y\| has no formula. |

## Findings (every item)

| file:line | item | verdict | evidence |
|---|---|---|---|
| index:3–27 | Roadmap, Named moves (mathematical content) | correct | each section introduces exactly the rule named; move statements match 07:565 table. |
| 01:13–17 | Argument A / Argument B | correct | (2k+1)² = 2(2k²+2k)+1; Argument B proves the converse; ledgered "even or odd, not both". |
| 01:27 | `def-statement` | correct | consistent with later uses. |
| 01:35 | `exm-statements` | correct | 2047 = 23·89; (e)/(f) open sentence vs instance. |
| 01:97 | warning inclusive "or" | correct | exclusive or = (P∨Q)∧¬(P∧Q); x = 0 satisfies both sides of x≥0 ∨ x≤0. |
| 01:101 | warning "if" in definitions | correct | converse of "4∣n ⇒ n even" fails at n = 2. |
| 01:108–116 | translations; ¬P∧Q vs ¬(P∧Q) | correct | n = −4 satisfies ¬(even ∧ positive) and not "odd and positive". |
| 01:131 | `def-main-connective` + tree, 01:162 second parse | correct | x>1 ∨ x<−1 ⇒ x²>1 ∧ x⁴>1 true. |
| 01:166 | check: main connectives | correct | ∨, ¬, ∧. |
| 01:198 | `def-sequent` + paraphrase | correct | existence claim; n = 0 case. |
| 01:216 | check: same form | correct | (i) affirms the consequent, witness n = 2 correct; (ii) P compound. |
| 01:255 | ∧ rules never lead from true to false | correct | one-line semantic check; soundness pointer. |
| 01:261 | Argument B's error / Chapter 3 promise | correct | B opened with P (conclusion) to prove Q→P; "cannot be derived" wording as S2 v3 requires. |
| 01:282 | `exr-statements-and-connectives-a1` | correct | (g) main connective ∧, rule ∧I. |
| 01:314 | `…-b1` | correct | C∧¬D, V→B, R∨¬R, K↔U. |
| 01:337 | `…-b2` | correct | all four parenthesizations; xy>0 for x, y>0. |
| 01:366 | `…-c1` | correct | only-if, unless; x = −2 witness; x ≠ 0 ⇒ x² > 0. |
| 01:395 | `…-c2` | correct | x² = x·x > x > 1 for x > 1; x = −2 witness; (x>1)∨(x<−1) necessary and sufficient, via \|x\| > 1 given. |
| 02:36 | `def-rule-schema` (Tr schema) | correct | one new line; "given lines and boxes, possibly none" covers →I, ∨E, =I. |
| 02:62–64 | instance / non-instance | correct | b forced to ½ and ⅓. |
| 02:66 | Sh schema and 02:78 | correct | x+1 < 3+2 rejected (c inconsistent); x+1<4 is a different string. |
| 02:85 | warning 2/4 vs 1/2 | correct | symbol-for-symbol matching. |
| 02:92 | `def-box-free-derivation` | correct | clauses (i), (ii); n ≥ 1; degenerate single premise (02:109). |
| 02:115 | `exm-chaining-derivation` (a)–(c) | correct | Tr 1,2; Tr 4,3 / Tr 2,3; Tr 4,1 / Tr 3,2; Tr 1,4; alternative route 02:174 (Tr 1,3 then Tr 4,2) checked. |
| 02:179 | check Tr 1,3 vs 3,1 | correct | b would be 1 and 0. |
| 02:191 | `def-derivable` + four remarks | correct | monotone in the rule list; unused premises allowed. |
| 02:212 | check: sequent of (c) | correct | u<v, w<z, v<w ⊢ u<z with Tr. |
| 02:220 | `exm-derivations` | correct | (a) P ⊢ P; (b) empty list, no ⊢ψ before §1.5; (c) clause check. |
| 02:240 | warning: premises given | correct | 1<0, 0<−1 ⊢ 1<−1 with Tr. |
| 02:254 | checking table | correct | letters' values per line. |
| 02:266 | `exm-not-a-derivation` | correct | (a) lines 5,3,4 an instance; fails "earlier" only; (b) b = 1 and 0, fails instance only. |
| 02:304 | chain 0 < 1/(n+1) < 1/n ≤ 1 | correct | two steps, the second a different pattern (< then ≤), as S2 v3 fixed. |
| 02:316 | `exr-derivations-a1` | correct | (b) Tr 2,3; Tr 1,4; Sh 5 (c=2), uniqueness claim for line 5 true; (c) line 3 cites 4; (e) soundness in miniature. |
| 02:357 | `exr-derivations-b1` | correct | Sh 1 (c = 1), Tr 3,2, middle y+1. |
| 02:380 | `exr-derivations-b2` | correct | (a),(b),(d),(f) instances; (c) middle x vs 3; (e) c = 1 vs 2. |
| 02:413 | `exr-derivations-b3` | correct | see meta table. |
| 02:443 | `exr-derivations-c1` | correct | Flip 1 passes all three questions; unsound. |
| 02:471 | `exr-derivations-c2` | correct | repaired derivation Tr 1,2; Tr 5,3; Tr 6,4; fault only at line 5; loop argument. |
| 03:21 | `def-rules-conjunction` | correct | three schemas, one new line each (S2 v3). |
| 03:50–64 | clause-by-clause reading | correct | citation order; i = j; one layer; φ := P∧Q, ψ := R. |
| 03:66, 03:70, 03:78 | warning, two checks | correct | (P∧Q)∧(R∧S) gives only P∧Q, R∧S; ∧I 5,2 = R∧(P∧Q). |
| 03:88 | safety of ∧ rules | correct | semantic one-liner, soundness pointer. |
| 03:100 | "Section 1.2 already found one derivation backwards, from the goal \( a < d \) of @exm-chaining-derivation" | **minor** | The example's backward part (02:123, (c)) has goal \( u < z \), premises \( u < v, w < z, v < w \); no goal \( a < d \) occurs in §02 (it is the blueprint's wording, 01 blueprint §02 item 3, renamed in the draft). Fix: "the goal \( u < z \) of part (c) of @exm-chaining-derivation". |
| 03:106 | `exm-conjunction-warm-ups` | correct | ∧I 2,1; ∧I 1,1; ∧E 1 (second form). |
| 03:164 | `prp-and-commutes` + Idea + proof | correct | ∧E 1 twice, ∧I 3,2. |
| 03:216 | `prp-and-associative` + Idea + proof | correct | 7 lines; replacements stated correctly; 03:248 reordering remark correct. |
| 03:250 | Remark (converse by B1; not cited later) | correct | grep: no later text rests on B1. |
| 03:262 | P∧Q, R ⊢ (P∧R)∧(Q∧R) | correct | line 2 cited twice. |
| 03:286 | four-letter rearrangement | correct | 10 lines, citation orders 7,5 / 4,6 / 8,9. |
| 03:309 | `exm-product-in-unit-interval` | correct | xy<x<1 from y<1, x>0 and x<1; algebra lines cite 3,5 and 3,4,6 (the lines actually used). |
| 03:349 | warning ∧E on (P∧Q)→R + expect-invalid 03:353 | correct | premise true for all x (vacuous at x = −1), x > 0 false at −1. |
| 03:365 | citation/conjunct mismatch | correct | ∧I 3,2 writes Q∧P. |
| 03:382 | `exr-conjunction-a1` | correct | (b) P or Q∧R; (c) (P∧Q)→R; (d); (e) ∧E1, ∧E1, ∧E3, ∧I 4,2. |
| 03:420 | `exr-conjunction-b1` | correct | 7 lines checked. |
| 03:446 | `exr-conjunction-b2` | correct | 1+3 < x+y < 2+4. |
| 03:464 | `exr-conjunction-b3` | correct | (a),(c),(e) correct; (b) two layers; (d) order reversed. |
| 03:504 | `exr-conjunction-c1` | correct | see meta table; marking scheme sums to 10. |
| 03:546 | `exr-conjunction-c2` | correct | expect-invalid block fails at line 2; repair 5 lines; ∧E\* schema and elimination correct; sums to 10. |
| 04:9 | `exm-wason-selection` | correct | 6 and green; red card cannot falsify. Green card paid in Ch 2 §03 (checked). |
| 04:39 | `def-rule-implication-elimination` | correct | schema; one new line. |
| 04:56–68 | clause-by-clause reading | correct | exact match; order of citation cannot change ψ; φ = ψ degenerate. |
| 04:70 | √2 < 1.5 < 2 instance | correct | 1.5² = 2.25 > 2; ∀E named as Chapter 4 and taken as given. |
| 04:78–86 | affirming the consequent + warning | correct | not an instance; n = 2 and x = −3 witnesses. |
| 04:88 | check P→(Q→R) with Q / with P | correct | nothing / Q→R. |
| 04:96 | remark: implications used, not proved | correct | see 05:17. |
| 04:110 | check: backward search with a dead branch | correct | Q→S dead; R→S then P→R. |
| 04:118 | `exm-implication-chains` (a)–(e) | correct | all five derivations and both pictures of (b) checked; 04:202 "first →E on a →E conclusion" true for derivation lines. |
| 04:241 | "each is a box-free derivation with ∧I, ∧E, →E" | correct | no R, no boxes. |
| 04:254 | checking table incl. wrong line | correct | wrong line fails both (Q ≠ P, R ≠ Q→R). |
| 04:264 | x>2 ⇒ x²>4 ⇒ x²+1>5 | correct | x² > 2x > 4. |
| 04:297 | warning: whole hypothesis; f(x) = x on (0,1) | correct | (a+1)/2 ∈ (0,1) and > a. |
| 04:319 | `exr-using-an-implication-a1` | correct | (b) only Q∧R; (d) false, →E needs a hypothesis line. |
| 04:342 | `exr-using-an-implication-b1` | correct | 7 and 6 lines; hypothesis rebuilt in order P∧Q (∧I 4,3). |
| 04:388 | `exr-using-an-implication-b2` | correct | x² < x ⇒ x(x−1) < 0 ⇒ x > 0 ⇒ x³ < x². |
| 04:412 | `exr-using-an-implication-b3` | correct | uses 1, 2, 6; forward search writes five lines (Q, R, S, U, T). |
| 04:447 | `exr-using-an-implication-c1` | correct | expect-invalid block fails at 3 as stated; 10 = 6·1+4; (c) see meta table. |
| 04:482 | `exr-using-an-implication-c2` | correct | 9 lines; search description; sums to 10. |
| 05:29 | `def-rules-implication` | correct | →I schema, →E recalled; "a line of that box itself" inside the block (Chapter 3 wording). |
| 05:55–69 | clause-by-clause reading, degenerate i = j | correct | consistent with def-derivation. |
| 05:75 | `prp-implication-transitive` + Idea + proof | correct | x>3 ⇒ x²>9 ⇒ x²>4 instance (x² > 3x > 9). |
| 05:123 | Remark: conjunctive premise (book.yaml must-prove) | correct | 7 lines checked. |
| 05:145 | warning: converse error (pays §01) | correct | box from P to Q gives P→Q. |
| 05:157 | `def-derivation` (scope rule, D1–D4, R schema) | **minor** | Content correct and consistent with every derivation in the chapter (∨E sibling boxes, nested →I, curry's inner box all satisfy it). One wording point: "A box is available at line \( k \) if … the boxes containing it are **exactly** the boxes containing line \( k \)". Read literally, a box contains itself, so it would be among "the boxes containing it" but not among those containing \( k \), and no box would ever be available. The paraphrase at 05:197 and every worked availability check (05:244, 05:427, 07:198) use the intended reading "the **other** boxes containing it". Chapter 3's soundness proof cites this label, so the reviser may want "the boxes other than itself that contain it" (a one-word fix; not raised in v2). |
| 05:189–203 | paraphrase; "nothing earlier changes"; length, context | correct | box-free + R (S2 v3 wording); context of last line = premises. |
| 05:205 | R typical-use drawing | correct | line i in no closed box. |
| 05:224 | warning: unclosed box | correct | last line outside every box. |
| 05:238 | checking table with context column | correct | availability of 1–5 and of box 3–5 at 6. |
| 05:252 | `exm-illegal-citation` | correct | expect-invalid fails at 7 (scope); x = 0 witness. |
| 05:283 | warning x>1 slip | correct | x³ > 1 fails at x = 0 outside the box. |
| 05:287 | check: which lines may cite line 2 | correct | 3, 4, 5. |
| 05:315 | `exm-first-boxes` (a)–(c) | correct | 1-line box; nested boxes with R 1 (legal); (c) 7 lines, a>0, x>1 reading correct. |
| 05:392 | `prp-curry` + Idea + both proofs + prompt | correct | availability explanation 05:427 correct; dropped-hypothesis above. |
| 05:454 | check: one box or two | correct | 8 lines; two disjoint boxes. |
| 05:494 | "a derivation that needs an earlier result must repeat its steps" | correct | no derived rule used anywhere in the chapter (script). |
| 05:500 | `exr-proving-an-implication-a1` | correct | (b) →E 1,3; →E 4,2; →I 3–5; (c) lines 1, 2; (d) line 3 unavailable; (e)–(f) curry comprehension. |
| 05:546 | `…-b1` | correct | 5 lines, no premises. |
| 05:574 | `…-b2` | correct | R 1 needed; R 2 in (b) legal; x² ≥ 0 instance. |
| 05:626 | `…-b3` | correct | 7 lines; \|x−2\| < 1 instance. |
| 05:661 | `…-b4` (ordering) | correct | see meta table; both distractors fail for the stated reasons. |
| 05:691 | `…-c1` (exit check) | correct | expect-invalid fails at line 10; repair (14 lines) valid; x = 0 witness; scheme 3/3/1/3. |
| 05:792 | `…-c2` | correct | 10 lines; R 3 legal; sums to 10. |
| 05:851 | `…-c3` (exit check) | correct | 9 lines; x>4 ⇒ x² > 4x > 16; scheme 2/2/2/1/3. |
| 06:25 | `def-rule-disjunction-introduction` | correct | two schemas, one new line each. |
| 06:48–65 | reading, instance, three non-examples | correct | Q∨P not a side of P∨Q. |
| 06:67–71 | why / why safe | correct | inclusive reading. |
| 06:73, 06:77 | warnings | correct | x = −1; x = 2 both sides true. |
| 06:81 | check x = 2 | correct | (iv) only after unfolding ≥; second schema. |
| 06:100 | "choose \( P \), and the new subgoal \( P \) cannot be reached from \( Q \) at all (take \( P \) false and \( Q \) true)" | **minor** | The claim (Q ⊬ P) is true, but the parenthesis proves it only through soundness, which is Chapter 3's; the sentence gives no pointer, while the parallel claim at 07:625 is flagged ("informally: … which Chapter 3 proves"). Fix: add "(Chapter 3 shows that a derivation never leads from true premises to a false conclusion)", or say "cannot be reached: with P false and Q true, it would lead from truth to falsehood". |
| 06:110 | `exm-disjunction-introduction-derivations` (a)–(d) | correct | all derivations checked; 06:201 "every rule so far except ∧E and R" true for (d). |
| 06:204 | "neither the premise \( P \to Q \) nor the assumption \( P \) mentions \( R \), so no rule can take \( R \) out of them" | **minor** | The conclusion (R not derivable from P→Q, P) is true, and the next warning's instance (x = 2.5) confirms it semantically. But the syntactic reason offered is not sound as stated: ∨I (and →I) can write lines that mention R from these lines (P∨R, R→R), so "mentions R" is not preserved the way §03 C1's "contains R" was for ∧ alone. Fix: drop "so no rule can take \( R \) out of them" and let the warning's instance carry the claim, or say "no rule can produce the line \( R \) by itself from them; the instance in the next warning shows why". |
| 06:206 | warning: side chosen too early; x = 2.5 | correct | P: x>2, Q: x>1, R: x>3 checked. |
| 06:214 | `exm-or-hypothesis-split` | correct | 10 lines (S2 v3 count); two schemas of ∨I; boxes disjoint. |
| 06:247–249 | "first place … not the last"; x ≥ 0 ⇒ x³ ≥ 0 reading | correct | v2 finding not returned. |
| 06:251 | check: why line 3 is needed | correct | exact hypothesis. |
| 06:261 | stall P∨Q ⊢ Q∨P | correct | see meta table. |
| 06:293 | `exm-product-zero` | correct | 5-line derivation; x>0 ⇒ (x>0)∨(x=0). |
| 06:352 | `exr-disjunction-introduction-a1` | correct | (b) ∨I, ∨I+→E, ∧E, →E. |
| 06:379 | `…-b1` | correct | 6 and 3 lines; P unused (noted). |
| 06:420 | `…-b2` (faded) | correct | line 7 = →I 3–6. |
| 06:464 | `…-b3` | correct | 5 lines; school fact x ≥ 1 ⇒ x² ≥ x true. |
| 06:492 | `…-c1` | correct | x = −1 instances in (a) and (c); scheme 3/3/3/1. |
| 06:521 | `…-c2` | correct | 6 lines each; (c) prediction argument correct. |
| 07:25 | `def-rules-disjunction` | correct | ∨E schema; ∨I recalled; "each χ is a line of its box itself" inside the block. |
| 07:61–69 | clause-by-clause reading, degenerate case | correct | availability of both boxes at n per def-derivation. |
| 07:71 | warning: case using the other case's assumption | correct | \|x\| = x fails at −1. |
| 07:85 | `exm-disjunction-first-derivations` | correct | 6 lines (∨I second/first schema); P∨P ⊢ P with boxes 2–2, 3–3. |
| 07:133 | expect-invalid variant | correct | fails only on "same last line". |
| 07:154 | check: missing box | correct | clause "two boxes". |
| 07:162 | why the rule is built so | correct | see meta table. |
| 07:166 | `exm-cases-on-hypothesis` | correct | 10 lines; inner ∨E availability at 9. |
| 07:201 | "each derivable from the other"; 4k+1, 4k+3 reading | correct | converse is 06:214. |
| 07:207 | `prp-distributivity` + Idea + both proofs + prompt | correct | 10 and 12 lines; 07:273 "line 8 re-derives P" required by scope rule. |
| 07:275 | reading x ≠ 0, x>0, x<0 | correct | atomic reading only, no negation rule. |
| 07:279 | `exm-disjunction-regroup` | correct | 12 lines; 07:317 remark on line 11 correct. |
| 07:324 | skeleton P∨Q, P→R, Q→R ⊢ R | correct | 8 lines. |
| 07:349 | `exm-abs-at-least-x` | correct | prose tags; derivation 10 lines; \|x\|>x fails at 1, \|x\|=x fails at −1. |
| 07:394 | `exm-abs-product-cases` | correct | four cases; \|a\| = −a for a ≤ 0 remark used exactly in the mixed cases. |
| 07:420 | `exm-triangle-inequality-cases` | correct | begins with a ≤ \|a\| and −a ≤ \|a\| (both halves by one split), then splits on sign of x+y, as Chapter 11 requires. |
| 07:440, 07:446, 07:450 | warnings: missing case, exhaust, overlap | correct | x=1, y=−1: 0 ≤ 2; x = 0 dropped. |
| 07:452 | check: x² ≥ 0 splits | correct | (i), (iii) exhaustive. |
| 07:476–569 | reference schemas and move table | correct | schemas identical to the defining blocks. |
| 07:589 | `exr-disjunction-and-cases-a1` | correct | (d) expect-invalid fails at 5 (one box); (e), (f) comprehension answers correct. |
| 07:634 | `…-b1` | correct | 13 lines; inner split legal. |
| 07:674 | `…-b2` | correct | max(3, −5) = 3 ≥ −1. |
| 07:692 | `…-b3` | correct | 10 lines; 4k², 4(k²+k)+1. |
| 07:729 | `…-c1` | correct | both cases; \|−a\| = \|a\| proved inline; scheme 2/3/3/2. |
| 07:785 | `…-c2` (find the error) | correct | only Case 2b's sentence cites Case 1's assumption (1a, 1b, 2a each checked); x = −3, y = −1; repair valid. |
| 07:822 | `…-c3` (exit check) | correct | 12 lines; second route 14 lines (1 + 7 + 5 + 1, counted); change description matches `prp-distributivity`'s second derivation. |
| 07:871 | `…-c4` (faded) | correct | 11 lines; splitting outside the box also correct, as said. |
| 07:936 | `…-r1` | correct | 6 lines; ∧I 3,2 matches C∧B. |
| 07:961 | `…-r2` | correct | 9 lines. |
| 07:989 | `…-r3` | correct | 6 lines, no premises. |

## Not in scope, noted for the coordinator

- `verify/ch01/` still holds the pre-split sidecars of material that moved to Chapter 2 (`exm-modus-tollens-instance.py`, `exr-negation-and-contradiction-*`, `exr-biconditional-and-definitions-*`, `exr-reductio-and-classical-rules-*`, `exr-finding-derivations-*`, `prp-de-morgan.py`, `prp-peirce.py`, `thm-sqrt2-irrational.py`, `thm-square-even-implies-even.py`, `thm-squares-order.py`, `prp-equivalence-cycle.py`, `exm-search-postpone-or.py`, `exm-strictly-increasing-both-ways.py`, `exm-unit-interval-tfae.py`, `exr-conjunction-implication-derivations-c1.py` (retired label), `_s06s07_logic.py`). All pass, but none checks a Chapter 1 label (bookkeeping for Referee B / S8).

## Resolution (S7, reviser, round 1, 2026-09-28)

Verdicts recorded in `authoring/ledger/ch01.yaml` (stage S5a, `--by refereeA`); S7 resolutions recorded `--by reviser`. Gates re-run in `scratchpad/ch01-S7r1/repo`: check_fitch 119 blocks, 0 errors; check_structure 0 fatal (word-count advisories only, exempt); check_numbers ch01 0 fatal; html built; pdf: all eight ch01 files built (the two failures are Ch 3 files, drafted concurrently); `./build.py check`: 3 problems, all unresolved references in Ch 3; check_rendered: 0 errors in ch01; pytest 295 passed; originality 0 shared 8-grams.

| Finding | Fix |
|---|---|
| 03:100, goal \( a < d \) | Now "from the goal \( u < z \) of part (c) of @exm-chaining-derivation". |
| 05:157, "exactly the boxes containing line k" | Now "the boxes other than itself that contain it are **exactly** the boxes containing line \( k \)". |
| 06:100, Q ⊬ P without a pointer | Now "cannot be reached from \( Q \) at all: with \( P \) false and \( Q \) true, a derivation would lead from a true premise to a false conclusion, and Chapter 3 proves that no derivation does." |
| 06:204, "no rule can take R out of them" | Fixed together with Referee B row 7. The letter argument is gone. The sentence now says that the box would need \( R \) from \( P \to Q \) and \( P \) alone, and that the next warning's instance makes both true and \( R \) false, so no derivation reaches \( R \) (with a Chapter 3 pointer). |
| Out of scope: pre-split sidecars in `verify/ch01/` | Already gone from `verify/ch01/` at S7 (38 sidecars plus helpers, all ch01 labels). |

## Resolution (S7, reviser, round 2, 2026-09-28)

No finding of this review was rejected by the re-check (`ch01-S7-recheck.md`); nothing here changed in round 2. The round-2 edits (§05 A1 (e), §06 A1 (d)) answer S6 finding 5's new problems N1 and N2.
