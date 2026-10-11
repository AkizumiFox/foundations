# Chapter 1 — S5 Referee A (proofs)

**Scope:** `src/ch01-propositional-natural-deduction/` §01–§07 (read-only), against the frozen blueprint `authoring/blueprints/ch01.md` and `authoring/reviews/ch01-S2.md`; STYLE §4, §10; NOTATION "Logic (Part 0)"; `latex/fitch-book.sty`.
**Referee:** A (proofs), blind to Referee B. Verdicts are recorded in `authoring/ledger/ch01.yaml` (stage S5a, by refereeA).

**Method.**
- `tools/check_fitch.py src/ch01-propositional-natural-deduction --notes`: 104 blocks (29 expect-invalid), 0 errors. Hand-checked: every expect-invalid block (the 5 flawed derivations fail exactly where the text says: 02:191 line 7, 02:575 line 10, 03:108 line 5, 03:405 line 5, 06:777 line 6; the RAA/② /③ /C1 schemata and every §07 partial derivation and reference-sheet schema match `def-rules-*` and the final numbering), and every `\by{…}` line the tool skips (04:201 CP shape; 04:326–334 √2 skeleton; 02:418–421 and 07:718 intentional blanks).
- Every prose proof: reason for each step, hypotheses used, one dropped-hypothesis counterexample per theorem (in the evidence column).
- Meta-arguments flagged by drafters: all checked (see "Flagged arguments" below).
- Number facts: 2047 = 23·89; (3k+2)² = 3(3k²+4k+1)+1; 3(2j+1) = 2(3j+1)+1; line counts (13, 11, 14, 15→12, 8, "six lines", "three lines", "nine of fourteen") all verified.

**Counts:** correct 132 · minor 4 · gap 1 · error 0 (137 ledger items).

## Flagged arguments

| Claim | Verdict | Evidence |
|---|---|---|
| 06:66 RAA on a negated goal can be replaced by ¬I | local step correct; concluding sentence **gap** | Replacement (¬I box on Q, ¬¬I inside, cite it for the old assumption) is valid. "So RAA is never needed to prove a negation" does not follow (inner RAAs survive); true propositionally only via Glivenko; false with quantifiers (¬¬∀x(Px∨¬Px)). |
| 07:36–40 goal-directed steps and RAA lose nothing | correct | Each step is inverted by one elimination (→E, ∧E, ¬E, ↔E) appended to a derivation with the new assumption added as a premise; RAA by one ¬E. |
| thm-classical-rules-interderivable ③ availability | correct | Every box containing m contains old k, hence k+3; the ∨E boxes at k+1, k+2..k+4 are available at k+5; later citations of k go to k+5 in the same boxes. |
| prp-provable-equivalence-basics pasting observation | correct | Added enclosing boxes contain both ends of every internal citation; box-availability ("exactly the boxes containing k") preserved; premise lines become repetitions of an available line. |
| def-derived-rule pasting claim | correct for one expansion; **minor** | Needs "repeat for derived-rule lines inside the copied derivation; terminates since only earlier results are cited". |
| exm-search-distribute "nine of the fourteen lines" | correct | Goal-directed: 2, 6, 7, 8, 9, 11, 12, 13, 14; premise-directed: 3, 4, 5, 10; plus premise 1. |

## "Needs RAA / no RAA" claims

- Proved by exhibiting an RAA-free derivation: contrapositive, MT, DS, ex falso, vacuous implication, ¬¬I, ¬(P∨Q)⊢¬P, exm-iff-negations, DM (a)–(c), implication-as-disjunction (a), thm-square-even-implies-even, exm-skeleton-odd-product, 06 B1(a), 07 B1(b) "¬Q needs none", 07 C3(b).
- Negative claims ("cannot be done without RAA"): 06:27 (¬¬P⊢P, pointer to Ch.2), 05:92 (marked without proof), 06:371 DM (d) (marked), 07:348 Peirce (marked), 07:642 B1(b) (marked), 07:874 C2 (explicitly only about the method) — none relied on. 05:177 (converse of exm-iff-negations) gives an informal reason without the "without proof" marker: minor. 06:674 (B2) is a "why" heuristic, acceptable.

## Findings (every ledger item)

| file:line | item | verdict | evidence |
|---|---|---|---|
| 01:27 | `def-statement` | correct | definition consistent with fitch-book.sty rules and later uses |
| 01:35 | `exm-statements` | correct | checked line by line |
| 01:117 | `def-main-connective` | correct | definition consistent with fitch-book.sty rules and later uses |
| 01:146 | `check:01-statements-and-connectives:1` | correct | answer checked |
| 01:178 | `def-sequent` | correct | definition consistent with fitch-book.sty rules and later uses |
| 01:196 | `check:01-statements-and-connectives:2` | correct | answer checked |
| 01:245 | `exr-statements-and-connectives-a1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 01:274 | `exr-statements-and-connectives-b1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 01:297 | `exr-statements-and-connectives-b2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 01:326 | `exr-statements-and-connectives-c1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 01:355 | `exr-statements-and-connectives-c2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 02:9 | `def-rules-conjunction` | correct | definition consistent with fitch-book.sty rules and later uses |
| 02:18 | `exm-product-in-unit-interval` | correct | checked line by line |
| 02:63 | `def-rules-implication` | correct | definition consistent with fitch-book.sty rules and later uses |
| 02:116 | `def-derivation` | correct | definition consistent with fitch-book.sty rules and later uses |
| 02:141 | `def-derivable` | correct | definition consistent with fitch-book.sty rules and later uses |
| 02:153 | `exm-derivations` | correct | (a) one-line premise, (b) 1-1 box legal, (c) ok; flawed block 02:188 fails at line 7 as stated; instance x>3,x>2,x>1 at x=0 correct |
| 02:211 | `check:02-conjunction-implication-derivations:1` | correct | answer checked |
| 02:259 | `prp-and-commutes` | correct | statement ok; proof cites exm-derivations (c): derivation 02:36 checked |
| 02:265 | `proof:prp-and-commutes` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 02:269 | `prp-implication-transitive` | correct | drop Q→R: P→Q ⊬ P→R (P true, R false) |
| 02:275 | `proof:prp-implication-transitive` | correct | 02:74 derivation + check table 02:245 verified line by line |
| 02:281 | `prp-curry` | correct | checked line by line |
| 02:291 | `proof:prp-curry` | correct | both derivations 02:294, 02:316 checked; scope remarks 02:312 correct |
| 02:379 | `check:02-conjunction-implication-derivations:2` | correct | answer checked |
| 02:406 | `exr-conjunction-implication-derivations-a1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 02:452 | `exr-conjunction-implication-derivations-b1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 02:480 | `exr-conjunction-implication-derivations-b2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 02:532 | `exr-conjunction-implication-derivations-b3` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 02:567 | `exr-conjunction-implication-derivations-c1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 02:668 | `exr-conjunction-implication-derivations-c2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 03:23 | `def-rules-disjunction` | correct | definition consistent with fitch-book.sty rules and later uses |
| 03:60 | `exm-disjunction-first-derivations` | correct | checked line by line |
| 03:125 | `check:03-disjunction-and-cases:1` | correct | answer checked |
| 03:139 | `exm-abs-product-cases` | correct | checked line by line |
| 03:165 | `exm-triangle-inequality-cases` | correct | checked line by line |
| 03:197 | `check:03-disjunction-and-cases:2` | correct | answer checked |
| 03:215 | `prp-distributivity` | correct | checked line by line |
| 03:225 | `proof:prp-distributivity` | correct | checked line by line |
| 03:281 | `exm-disjunction-regroup` | correct | checked line by line |
| 03:320 | `exm-cases-on-hypothesis` | minor | 03:373 'the one place in this section where ∨I is used for something other than finishing a case' is false: prp-distributivity 2nd derivation lines 5,10 (Q∨R fed to ∧I), exm-disjunction-regroup lines 3,7 (P∨Q fed to ∨I), and 03:50 (x=0 to x≤0). Derivations themselves correct. |
| 03:390 | `exr-disjunction-and-cases-a1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 03:431 | `exr-disjunction-and-cases-b1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 03:471 | `exr-disjunction-and-cases-b2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 03:489 | `exr-disjunction-and-cases-b3` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 03:526 | `exr-disjunction-and-cases-c1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 03:580 | `exr-disjunction-and-cases-c2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 04:13 | `def-rules-negation` | correct | definition consistent with fitch-book.sty rules and later uses |
| 04:25 | `exm-square-plus-one` | correct | checked line by line |
| 04:54 | `exm-double-negation-introduction` | correct | both derivations checked; 04:92 'no rule so far removes a negation' is motivation, Ch.2 pointer at 06:27 |
| 04:94 | `check:04-negation-and-contradiction:1` | correct | answer checked |
| 04:120 | `prp-contrapositive` | correct | no RAA: derivation uses only →I,→E,¬I,¬E (04:152 true) |
| 04:130 | `proof:prp-contrapositive` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 04:156 | `prp-modus-tollens` | correct | drop ¬Q: P→Q ⊬ ¬P (P,Q true); 04:183 'lines 3–6 line for line' verified; CP route 04:196 shape checked by hand (CP i gives ¬Q→¬P); 'lines 2–7 of CP' correct |
| 04:162 | `proof:prp-modus-tollens` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 04:185 | `def-derived-rule` | minor | 04:193 pasting argument is correct for one level (repetitions are available; copy's citations stay inside the copy; copy's boxes close before its last line; checked against def-derivation scope rule). But the copied derivation may itself contain derived-rule lines (e.g. MT via CP, DS in 07 postpone-or), so 'derivable with derived rules => with primitive rules alone' needs one clause: repeat the expansion, which terminates because each derivation cites only earlier results. |
| 04:208 | `exm-modus-tollens-instance` | correct | checked line by line |
| 04:224 | `prp-disjunctive-syllogism` | correct | drop ¬P: P∨Q ⊬ Q (P true, Q false) |
| 04:230 | `proof:prp-disjunctive-syllogism` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand; 6-6 one-line box legal |
| 04:270 | `thm-square-even-implies-even` | correct | hypothesis n integer needed (n=√2: n²=2 even, n not an integer); no RAA claim verified: CP, DS on (E1) in the order odd∨even, ¬I, ¬E, →I only |
| 04:280 | `proof:thm-square-even-implies-even` | correct | each step's rule named; DS instance P=n odd, Q=n even matches (E1) order; (E2) supplies the clash (∧I implicit) |
| 04:292 | `thm-sqrt2-irrational` | correct | (L) 'not both even' is essential (A1(d)); with 4 for 2 the proof stalls at q²=k² (A1(e)) — both verified |
| 04:302 | `proof:thm-sqrt2-irrational` | correct | p²=r²q²=2q², p=2m, q²=2m² verified; skeleton 04:317 lines 8,10 →E, 11 ∧I, 12 ¬E 11,2, 13 ¬I 5-12 correct; Before-reading-on answer (lines 6,8) consistent |
| 04:308 | `check:04-negation-and-contradiction:2` | correct | answer checked |
| 04:350 | `prp-ex-falso` | correct | drop ¬P: P ⊬ Q |
| 04:356 | `proof:prp-ex-falso` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 04:371 | `prp-vacuous-implication` | correct | drop ¬P: ⊬ P→Q |
| 04:377 | `proof:prp-vacuous-implication` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 04:422 | `exr-negation-and-contradiction-a1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 04:451 | `exr-negation-and-contradiction-b1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 04:483 | `exr-negation-and-contradiction-b2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 04:507 | `exr-negation-and-contradiction-b3` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 04:537 | `exr-negation-and-contradiction-b4` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 04:565 | `exr-negation-and-contradiction-c1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 04:600 | `exr-negation-and-contradiction-c2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 05:11 | `def-rules-biconditional` | correct | definition consistent with fitch-book.sty rules and later uses |
| 05:22 | `prp-iff-two-implications` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 05:32 | `proof:prp-iff-two-implications` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 05:82 | `def-provable-equivalence` | correct | definition consistent with fitch-book.sty rules and later uses |
| 05:96 | `prp-provable-equivalence-basics` | correct | (a),(b) true |
| 05:111 | `proof:prp-provable-equivalence-basics` | correct | pasting observation 05:112 correct (added enclosing boxes contain both citing and cited lines; box availability preserved); premise lines -> repetitions of an available line; last line of D lies in no box of D so it is a line of the new box; transitivity reverse direction by swapping P,R correct |
| 05:140 | `exm-iff-negations` | minor | Derivation correct, no RAA (checked). 05:177 'its converse … needs the rule of Section 1.6 … nothing met so far produces a positive statement from negated ones' is offered as a reason but is not a proof and is imprecise (⊥E, DS produce positive statements); unlike 05:92 it is not marked 'stated without proof'. Claim itself true (2-world Kripke model); not relied on. |
| 05:185 | `thm-odd-iff-square-odd` | correct | n=2k gives n²=2(2k²); ∨E on (E1) with impossible case closed by ¬E,⊥E |
| 05:191 | `proof:thm-odd-iff-square-odd` | correct | every step named; (E1),(E2),(E3) used |
| 05:203 | `thm-squares-order` | minor | Statement and both counterexamples correct (x=-2,y=1 kills (⇒) without x≥0; x=1,y=-2 kills (⇐) without y≥0). But remark 05:225 / lead-in 05:201 ('each hypothesis used by one direction each', '(⇒) used x≥0') misdescribes the printed (⇒) proof, which also multiplies by y≥0 (05:217). True that (⇒) needs only x≥0 (y≥0 follows from x≤y), but the proof as written uses both. |
| 05:216 | `proof:thm-squares-order` | correct | (⇒) x²≤xy≤y²; (⇐) y<x ⇒ x>0, xy<x², y²≤xy ⇒ y²<x² clash — all valid |
| 05:230 | `check:05-biconditional-and-definitions:1` | correct | answer checked |
| 05:260 | `exm-strictly-increasing-both-ways` | correct | checked line by line |
| 05:292 | `prp-equivalence-cycle` | correct | drop R→P: P→Q,Q→R ⊬ P↔Q (P false, Q,R true) |
| 05:302 | `proof:prp-equivalence-cycle` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand; rotation P,Q,R->Q,R,P permutes the premise set, verified |
| 05:332 | `exm-unit-interval-tfae` | correct | (b)⇒(c): x≤0 ⇒ x≤0≤x² clash; divisions by x>0 justified |
| 05:369 | `exr-biconditional-and-definitions-a1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 05:392 | `exr-biconditional-and-definitions-b1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 05:422 | `exr-biconditional-and-definitions-b2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 05:436 | `exr-biconditional-and-definitions-b3` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 05:448 | `exr-biconditional-and-definitions-c1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 05:494 | `exr-biconditional-and-definitions-c2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 06:13 | `exm-raa-zero` | correct | hypothesis x≥0 used (drop it: x=-1 satisfies x≤ε ∀ε>0, x≠0); ε=x/2>0 justified |
| 06:33 | `def-rule-raa` | gap | 06:66 'So RAA is never needed to prove a negation'. The argument given only replaces the LAST RAA step (box on ¬¬Q -> ¬I box on Q + ¬¬I); RAA steps inside the box may remain, so the global sentence does not follow. It is true propositionally only by Glivenko's theorem (not in the book) and FALSE in first-order logic (⊢ ¬¬∀x(Px∨¬Px) needs a classical rule), so it will mislead once Ch.3 adds quantifiers. Local use at 06:198 is fine. Fix: 'the last step of a derivation of a negation never needs RAA'. |
| 06:93 | `prp-double-negation` | correct | (a) no RAA, (b) RAA; 'no derivation of P from ¬¬P without RAA' stated with Ch.2 pointer, not relied on |
| 06:108 | `proof:prp-double-negation` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 06:148 | `check:06-reductio-and-classical-rules:1` | correct | answer checked |
| 06:164 | `prp-contrapositive-converse` | correct | RAA at line 6; 06:198 local RAA-avoidance when Q=¬S verified |
| 06:174 | `proof:prp-contrapositive-converse` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 06:204 | `prp-excluded-middle` | correct | one RAA at line 8; 8-line count correct |
| 06:214 | `proof:prp-excluded-middle` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 06:245 | `prp-de-morgan` | correct | (a)-(c) no RAA (derivations close boxes by ¬I/∨E only); (d) RAA at 6,10,13; 'no derivation of (d) avoids RAA' marked without proof, not relied on; LEM route 06:371 checked |
| 06:266 | `proof:prp-de-morgan` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand; A1(f) lines 5,9 cite line 2 — correct |
| 06:373 | `check:06-reductio-and-classical-rules:2` | correct | answer checked |
| 06:385 | `prp-implication-as-disjunction` | correct | (a) no RAA, (b) LEM only |
| 06:400 | `proof:prp-implication-as-disjunction` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand |
| 06:461 | `thm-classical-rules-interderivable` | correct | hypothesis-drop: without ⊥E in the base list, LEM does not derive ¬¬E (read ⊥ as true: all remaining rules + LEM sound, ¬¬E not), and ⊥E is used at ③ line k+4 |
| 06:473 | `proof:thm-classical-rules-interderivable` | correct | ① 3-line and 8-line replacements valid; ② ¬I then ¬¬E, box needs no change; ③ 6 lines, line m available at k+3 since every box containing m contains old k; ∨E boxes available at k+5; later citations of k -> fragment's last line (same boxes); chaining terminates (fragments introduce no new Y) |
| 06:554 | `exr-reductio-and-classical-rules-a1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 06:583 | `exr-reductio-and-classical-rules-b1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 06:638 | `exr-reductio-and-classical-rules-b2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 06:677 | `exr-reductio-and-classical-rules-b3` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 06:702 | `exr-reductio-and-classical-rules-b4` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 06:731 | `exr-reductio-and-classical-rules-c1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 06:769 | `exr-reductio-and-classical-rules-c2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:42 | `check:07-finding-derivations:1` | correct | 07:36-40 'goal-directed steps / RAA lose nothing' verified: A→B, A∧B, ¬A, A↔B each recovered by one →E/∧E/¬E/↔E; RAA: G derivable ⇒ ⊥ from Γ,¬G. (d) needs step 5 — correct |
| 07:61 | `exm-search-distribute` | correct | 'nine of the fourteen lines' verified: goal-directed wrote 2,6,7,8,9,11,12,13,14; premise-directed 3,4,5,10; premise line 1; 'only steps 2,3,4' true; partial blocks 07:73,89 consistent with final numbering |
| 07:148 | `exm-search-cases` | correct | partial 07:160 and final derivation checked |
| 07:207 | `exm-search-postpone-or` | correct | dead end partial 07:219 correct; rows for neither side verified; final 14-line derivation, DS 10,8 instance P:=Q,Q:=R correct |
| 07:307 | `prp-peirce` | correct | RAA at line 9; 'every derivation must use RAA' marked without proof |
| 07:319 | `proof:prp-peirce` | correct | check_fitch rerun: 104 blocks, 0 errors; every cited line/box availability re-checked by hand; ¬P used at lines 4 and 8 as stated |
| 07:381 | `exm-skeleton-odd-product` | correct | no RAA claim true: CP, (E2), DS on 'even or odd' |
| 07:578 | `exr-finding-derivations-a1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:609 | `exr-finding-derivations-b1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:698 | `exr-finding-derivations-b2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:752 | `exr-finding-derivations-c1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:820 | `exr-finding-derivations-c2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:886 | `exr-finding-derivations-c3` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:963 | `exr-finding-derivations-c4` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:1003 | `exr-finding-derivations-r1` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:1043 | `exr-finding-derivations-r2` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |
| 07:1059 | `exr-finding-derivations-r3` | correct | solution derivations/arguments checked line by line; check_fitch 0 errors; number facts verified |

## Hypothesis-drop attempts (summary)

- `thm-squares-order`: without x ≥ 0, x = −2, y = 1 breaks (⇒); without y ≥ 0, x = 1, y = −2 breaks (⇐). Both hold as the book says.
- `thm-classical-rules-interderivable`: without ⊥E in the base list, LEM no longer derives ¬¬E (interpret ⊥ as true: every remaining rule and LEM is sound, ¬¬E is not); ⊥E is used at line k+4 of ③.
- `exm-raa-zero`: without x ≥ 0, x = −1 satisfies x ≤ ε for all ε > 0 and x ≠ 0.
- `thm-sqrt2-irrational`: without "not both even" in (L) no clash (2 = 4/2); with 4 in place of 2 the proof stalls at q² = k².
- `prp-equivalence-cycle`: without R → P, the row P false, Q, R true refutes P ↔ Q.
- MT / DS / ex falso / vacuous implication / transitivity: dropping the second premise gives a refuting row (evidence column).
- `thm-square-even-implies-even`, `thm-odd-iff-square-odd`: the hypothesis "n integer" is what makes "even/odd" meaningful (n = √2 has n² = 2 even).

## Resolution (S7, reviser, 2026-09-28)

Ledger: each item below has an S7 verdict `correct` by `reviser` (the ledger has no `fixed` verdict; `correct` on the new text is the closest), awaiting the S7 re-referee.

| Finding | Resolution |
|---|---|
| 06:66 `def-rule-raa` (gap) | The sentence now claims only the last step: "So the **last** step of a derivation of a negation never needs RAA, though steps inside its box still may; RAA earns its place on the other goals." No global claim remains; 06:198's local use is unchanged. |
| 03:373 `exm-cases-on-hypothesis` | Now "the one place in this section where ∨I manufactures the hypothesis of a premise" (also S5-B). |
| 04:193 `def-derived-rule` | Added: "If the copy itself uses derived rules, expand those lines in the same way; this stops, because each derivation cites only results proved before it." |
| 05:177 `exm-iff-negations` | The reason is now precise (the natural box on ¬Q ends in ¬¬Q) and the claim is marked "we state it without proof, and nothing depends on it"; added to §05's dependency ledger. |
| 05:201/225 `thm-squares-order` | Lead-in: "each hypothesis is needed: dropping either one breaks one of the two directions". Remark: (⇒) "needs" x ≥ 0, with a parenthesis that its proof's use of y ≥ 0 follows from y ≥ x ≥ 0; (⇐) "used only" y ≥ 0 (also S5-B). |
