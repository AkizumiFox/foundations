# Chapter 2 — S5 Referee A (proofs)

**Scope:** `src/ch02-negation-and-classical-logic/` §01–§06 and `index.md` (read-only), against the frozen blueprint `authoring/blueprints/ch02.md` and `authoring/reviews/ch02v3-S2.md`; `latex/fitch-book.sty`; Chapter 1's `def-derivation`, `def-derivable`, `exm-derivations`, `exm-disjunction-first-derivations`, `exm-cases-on-hypothesis`, `exm-or-hypothesis-split` (read for the citations). Referee A, blind to Referee B. Verdicts are **not** written to the ledger (the reviser records them).

**Method.**
- Scratch copy (`scratchpad/S5a-refA`): `python3 tools/check_fitch.py src/ch02-negation-and-classical-logic --notes`: 119 blocks (2 expect-invalid, 37 schema), 0 errors. Both expect-invalid blocks fail exactly where the text says (01:584 line 4 cites line 3 of a closed box; 05:893 line 6 cites line 3 of a closed sibling box). All sidecars `verify/ch02/*.py` pass.
- Hand-checked everything the tool skips: every `% schema` block (the definition schemas; ② and ③ and C1 of §05; every §06 snapshot, whose line numbers match the finished derivations; the reference sheet, which matches the definitions); every `\by{…}` line (02:262–265 √2 skeleton, 03:319, 06:767 VI); the intentional blanks 06:832 and 06:915.
- Every prose proof: the reason for each step, the hypotheses used, one dropped-hypothesis counterexample per theorem/proposition (evidence column). The only chosen constant is ε = x/2 in `exm-raa-zero` (depends on x only, chosen after x): correct.
- Rule order: no `\raa`, `\lem`, `\nne`, `\nni`, `\dm`, RAA or LEM in §01–§04; no `\ni` in §01; no MT/CP/DS in §01–§02; no ↔ rule before §04. **Each section uses only rules introduced by then.**
- Every non-derivability claim was checked for truth with the Kripke/G3 helpers of `verify/ch02/_s05s06_logic.py` (all 11 refuted without RAA, all classically valid), and on the page for its marking.
- Line counts verified by writing out the undisplayed routes: De Morgan (d) by LEM 11; postpone-or by LEM on P 22; §06 C3 by LEM on P 11; B1(b) primitive 15; `exm-derived-rules-in-use` (a) expanded 11.

**Counts (120 ledger items):** correct 112 · minor 7 · gap 0 · error 1. Plus 2 chapter-level minor findings on text outside any ledger item (§06 method box and "A search that fails").

## Critical checks asked for

| Check | Verdict | Evidence |
|---|---|---|
| Only rules introduced by then; no RAA before §05 | correct | grep of every rule macro and rule name by section (above); §01's theorem is proved without ¬I, CP, DS; §01 `exm-vacuous-square` writes the five lines out (derived rules are §03). |
| "Needs RAA / not derivable" claims | correct except two unmarked (minor) | Marked "without proof" and relied on by nothing: 03:341, 04:209, 05:37 (other two stalls), 05:221, 05:309, 05:443, 05:602, 06:759, 06:1019 (explicitly only about the method). Promised to Ch 3 (`thm-raa-independent`): 04:227, 05:37 (¬¬P ⊢ P). 02:80 "needs a rule we have not met" is the blueprint's sanctioned wording. **Unmarked:** the title of `exm-search-raa` (06:355–356, "must assume the negation of its goal") and the §06 C3 scheme (06:1085, "needs a second classical step"). All are true (Kripke). |
| §06 search method, justification paragraphs | correct | Goal-directed steps inverted by one appended →E/∧E/¬E/↔E; RAA by one ¬E; LEM split adds a resource; ∨I not invertible (P∨Q ⊢ Q∨P). |
| Step-5 clause "try the same with a goal further out" | correct; one minor | Sound (it is step 5 at an outer gap, covered by the same one-¬E argument); matches `prp-peirce`'s narrated search (05:277) and 06:439 exactly. Minor: "A search that fails" (06:462) does not try the new clause (RAA on ¬(Q→P) at the outer gap; it also returns to the goal Q→P), so the claim "every route returns to one gap" is not shown for the route the clause adds. |
| `exm-search-raa` | correct derivation; minor title | See item row. |
| §03 `\by{comm.\ of $\vee$}` vs §06 "(or commutes)" | minor | Settle on §06's name: 03:319 `\by{or commutes}{1}`; 03:299 "(or commutes, the sequent P∨Q ⊢ Q∨P of @exm-disjunction-first-derivations, used as a derived rule)". The §04 table (04:263) already says "@exm-disjunction-first-derivations"; no other `\by` names disagree with the §06 table (VI matches row "VI (vacuous implication)"). |
| Earlier review problems (ch01v2-S5-A/B, S6) | none returned | "RAA never needed to prove a negation" is now the last-step claim (05:79); `def-derived-rule` iteration clause present (03:126); converse of `exm-iff-negations` marked (04:209); `thm-squares-order` remark matches its proof (04:326); A1(a) contrapositive wording (06:711, 03:345); "part (d) below" (05:920); LEM aftermath (05:262); `def-provable-equivalence` points to Ch 3 (04:227); C1 cites `@exr-negation-and-contradiction-b3` (04:591); §06 C2 scheme accepts RAA (06:1030); √6 Hint 2 softened (02:450). |

## Chapter-level findings (no ledger item)

| file:line | item | verdict | evidence |
|---|---|---|---|
| 06:462 | "A search that fails" vs step 5's new clause | minor | Step 5 now says "if that gives nothing, try the same with a goal further out whose box contains the stalled gap". The walkthrough tries RAA on ¬P, LEM on P and LEM on Q, but not the outer goal: an RAA box on ¬(Q→P) around the whole search, whose clash needs Q→P, the goal again. Add that sentence so "every route returns to one gap" covers the method as stated. |
| 06:65–67 | the `.algorithm` block, control flow | minor | Step 4 makes a manufactured statement χ "the new goal", and step 5 ends "Then return to step 3", but nothing says to apply step 2 to that new goal. The worked searches do so (06:381 "step 2 sets up two boxes" for P↔Q; 06:1047–1048 for ¬Q and ¬P∧Q). Add to step 4 "…manufacture it, starting again at step 2 for that goal". |

## Chapter 1 changes needed

None found by this referee. Every Chapter 1 label that Chapter 2 cites exists and says what is cited: `exm-derivations` (a) is the one-line P ⊢ P; `exm-disjunction-first-derivations` contains P∨Q ⊢ Q∨P and P∨P ⊢ P; `exm-cases-on-hypothesis` and `exm-or-hypothesis-split` are the two directions in the §04/§06 tables; `def-derivable`'s "premises all belong to Γ" licenses the unused premise (01:120) and the §06 justification (06:74).

## Findings (every ledger item)

| file:line | item | verdict | evidence |
|---|---|---|---|
| 01:24 | `def-rules-contradiction` | minor | Schemas match fitch-book.sty and the §06 reference sheet. But l.58 "The only way a line ⊥ is ever written, apart from being assumed, is by ¬E" is false: ∨E writes ⊥ (prp-de-morgan (b), (c), line 9: "⊥ ∨E 4,5-6,7-8"), →E from φ→⊥ and φ (§02's own table), ∧E, R, and ⊥E itself (l.56 says ⊥E may write ⊥). l.60's soundness sketch ("⊥ was written from some φ and ¬φ") rests on the same sentence; its conclusion is true (Ch 3), the reason as stated is not. Fix: "¬E is the only rule whose conclusion is always ⊥; any other rule writes ⊥ only from lines that already contain it". |
| 01:62 | `check:01-contradiction-and-vacuous-truth:1` | correct | (i) φ=Q∧R; (ii) φ=¬P, order ¬P then ¬¬P; (iii) main connective →, not a negation. Checked against def-main-connective. |
| 01:84 | `exm-first-contradictions` | correct | (a) 2 lines, (b) 5 lines; ¬E 3,2 order right; unused half P legal by def-derivable (premises 'belong to'). check_fitch 0 errors. |
| 01:125 | `prp-ex-falso` | correct | Drop ¬P: P ⊬ Q (P true, Q false). |
| 01:135 | `proof:prp-ex-falso` | correct | 4 lines, ¬E 1,2 then ⊥E; checked. |
| 01:154 | `prp-vacuous-implication` | correct | Drop ¬P: ⊬ P→Q (P true, Q false). |
| 01:164 | `proof:prp-vacuous-implication` | correct | 5 lines; box 2-4 ends on Q as its own line; ¬E 2,1 cites premise (no box). Uses only §01 rules + Ch1. |
| 01:188 | `exm-manufactured-clash` | correct | 6 lines; ∨I manufactures P∨Q; ¬E 3,1. Checked. |
| 01:221 | `exm-impossible-case` | correct | 9 lines; one-line box 8-8 legal (as exm-disjunction-first-derivations); ∨E 1,4-7,8-8 boxes available at 9. No DS named (DS is §03). Drop ¬R: P∨Q, P→R ⊬ Q (P,R true, Q false). |
| 01:283 | `thm-square-even-implies-even` | correct | No ¬I, CP or DS (blueprint). Drop 'integer': parity undefined; drop (E2) from the premises and the 12-line skeleton loses line 9 (row E false, O true, S,T true satisfies E∨O, O→T but not S→E). |
| 01:293 | `proof:thm-square-even-implies-even` | correct | Every step tagged; 12-line skeleton checked (line 8 cites 4: box 4-11 contains 8); line table matches; quantifier steps flagged to Ch 4. (2k+1)^2 = 2(2k^2+2k)+1 verified. |
| 01:347 | `check:01-contradiction-and-vacuous-truth:2` | correct | Line 10, cites 9, writes E. |
| 01:365 | `exm-vacuous-square` | correct | Five lines written out, not cited as one line (derived rules are §03): matches blueprint order. |
| 01:422 | `exr-contradiction-and-vacuous-truth-a1` | minor | (a),(b),(d),(e) correct. (c) solution l.439 "The only rule so far that writes ⊥ is ¬E" is false at §01: ⊥E writes ⊥ (φ:=⊥, l.56), →E writes ⊥ from φ→⊥, ∧E from ⊥∧ψ. The True/False verdict (false) is right; the reason should be "⊥E needs a line ⊥; the rule whose conclusion is ⊥ is ¬E, and it needs φ and ¬φ". |
| 01:448 | `exr-contradiction-and-vacuous-truth-b1` | correct | (a) 6 lines, (b) 7 lines, ⊥E with φ=¬R; checked. |
| 01:494 | `exr-contradiction-and-vacuous-truth-b2` | correct | n=2k gives n+1=2k+1 odd; clash with (E2) for n+1; ⊥E closes; both cases end in 'n odd'. Uses only §01 rules. |
| 01:512 | `exr-contradiction-and-vacuous-truth-b3` | correct | x^2+1 ≥ 1 > 0; derivation 5 lines; both vacuous; checked. |
| 01:542 | `exr-contradiction-and-vacuous-truth-c1` | correct | (a) 8 lines checked; (b) reading correct, converse by ∨I. |
| 01:576 | `exr-contradiction-and-vacuous-truth-c2` | correct | expect-invalid block fails exactly at line 4 (tool: 'line 4 cites line 3, inside a box that has closed'); lines 5-7 fine given 4; (c) ¬P ⊢ Q refuted at x=-1 (¬(x>0) true, x=7 false); (d) 5 lines; scheme 2+3+3+2=10. |
| 02:15 | `def-rules-negation` | correct | ¬I schema + recalled ¬E; 'line of the box itself' clause; ⊢ ¬⊥ one-line box legal; non-instance (box ending ¬φ) correct. |
| 02:91 | `exm-double-negation-introduction` | correct | (a) 4 lines, (b) 6 lines; assumption used twice; l.134 remark on line 4 vs 6 correct. |
| 02:139 | `check:02-negation-and-contradiction:1` | correct | 5 lines; ∨I, ¬E, ¬I; comparison with exm-manufactured-clash accurate. |
| 02:165 | `exm-triple-negation` | correct | 7 lines; line 4 cites 2 (box 2-6 contains 4); no ¬¬E used. |
| 02:205 | `exm-square-plus-one` | correct | x^2+1=0 gives x^2=-1<0; clash with ¬(x^2<0); ¬I. |
| 02:227 | `thm-sqrt2-irrational` | correct | No hypotheses; A1(d) is the dropped-clause test: without 'not both even', 2=4/2 is a witness that the proof reaches no clash. |
| 02:237 | `proof:thm-sqrt2-irrational` | correct | Steps: (L) choice, p^2=r^2q^2=2q^2, thm-square-even-implies-even (→E) twice, q^2=2m^2, ∧I, ¬E against (L), ¬I. Hand-checked the 13-line skeleton (tool skips \by and \text lines): 8 →E 3,7; 10 →E 4,9; 11 ∧I 8,10; 12 ¬E 11,2; 13 ¬I 5-12. ¬I, not RAA (box opens r^2=2). |
| 02:243 | `check:02-negation-and-contradiction:2` | correct | Lines 11 and 2, step line 12 — matches skeleton. |
| 02:295 | `exr-negation-and-contradiction-a1` | correct | (b) ¬I with 1≠0; (d) 2=4/2; (e) stall at q^2=k^2, r=2/1 witness. All verified. |
| 02:321 | `exr-negation-and-contradiction-b1` | correct | 7 lines, box in box; checked. |
| 02:351 | `exr-negation-and-contradiction-b2` | correct | (x-1/2)^2+3/4 = x^2-x+1 verified; ¬I/¬E tagged. |
| 02:371 | `exr-negation-and-contradiction-b3` | correct | (3k+1)^2=3(3k^2+2k)+1, (3k+2)^2=3(3k^2+4k+1)+1 verified; (b) p^2=3q^2, q^2=3m^2; p=q=3 shows parity-(L) gives no clash. Words, not \mid. |
| 02:405 | `exr-negation-and-contradiction-b4` | correct | 7 lines checked; line 6 needed (box must end on ⊥). |
| 02:435 | `exr-negation-and-contradiction-c1` | correct | p^2=2(3q^2); 3q^2=2m^2; q odd ⇒ q^2=2j+1 ⇒ 3q^2=2(3j+1)+1 odd; clash (E2); ⊥E; ∨E; ∧I; ¬E vs (L); ¬I. Scheme 2+2+3+2+1=10. |
| 02:472 | `exr-negation-and-contradiction-c2` | correct | False lemma fails at n=2; the (L)-variant 'not both divisible by 4' is itself true; ¬I applied correctly to a box with an unjustified line. |
| 03:21 | `prp-modus-tollens` | correct | Proved from primitives before def-derived-rule (S2 #19 order). Drop ¬Q: P→Q ⊬ ¬P. |
| 03:31 | `proof:prp-modus-tollens` | correct | 6 lines; →E, ¬E, ¬I only. |
| 03:56 | `prp-contrapositive` | correct | 'only the rules so far' wording (no 'no RAA'). Drop the premise: ⊬ ¬Q→¬P (Q false, P true). |
| 03:66 | `proof:prp-contrapositive` | correct | 7 lines; line 5 cites 2 (box 2-6 contains 5); lines 3-6 = MT lines 3-6 citation for citation (verified). |
| 03:100 | `def-derived-rule` | correct | Uniform substitution; 'already derived'; availability. l.126 expansion argument: repetitions by (D3) in the current box, copy's citations internal or to repetitions, copy's boxes close before its last line, iterated expansion terminates (S5-A clause present). Correct. |
| 03:151 | `prp-disjunctive-syllogism` | correct | Drop ¬P: P∨Q ⊬ Q (P true, Q false). |
| 03:161 | `proof:prp-disjunctive-syllogism` | correct | 7 lines; comparison with exm-impossible-case (lines 5-6 vs 4) accurate. |
| 03:189 | `exm-derived-rules-in-use` | correct | (a) 5 lines, MT twice (instances stated correctly); 11-line natural expansion checked; (b) DS then →E; 'seven lines' = literal paste (2 repetitions + 5) — fine. |
| 03:258 | `check:03-derived-rules:1` | correct | (iii) none; (iv) MT needs ¬¬Q — correct. |
| 03:272 | `exm-modus-tollens-instance` | correct | x>2>0 ⇒ x^2=x·x>2x>4 verified; x^2≤4 is ¬(x^2>4). Green-card paragraph: MT gives ¬E; E, ¬R, E→R give ⊥ by →E, ¬E; red card is affirming the consequent. Correct. |
| 03:290 | `exm-square-even-via-contrapositive` | minor | 13-line derivation correct (12 DS 11,10 on O∨E with ¬O; 9 CP 3; 10 →E 9,8); 'every negation introduced, none removed' true of the expansion; l.330 line correspondences with §01's skeleton checked. Minor (cross-drafter mismatch): line 11 (l.319) is \by{comm.\ of $\vee$}{1}, but §06's derived-rule table (06:664) names this rule '(or commutes)', and §04's table and l.299 prose call it 'the exchange of disjuncts'. Fix in §03: \by{or commutes}{1} (and l.299 '(or commutes, @exm-disjunction-first-derivations)'). |
| 03:362 | `exr-derived-rules-a1` | correct | (b) 7 lines checked; (c) CP on ¬Q→¬P gives ¬¬P→¬¬Q — correct. |
| 03:409 | `exr-derived-rules-b1` | correct | (a) 7 lines checked; (b) x≠-1 from x>0, then (a) as a derived rule — legitimate. |
| 03:442 | `exr-derived-rules-b2` | correct | Order (iii),(v),(vii),(ii),(vi),(iv),(i) unique; (viii) wrong box, (ix) closed-box citation. Checked. |
| 03:466 | `exr-derived-rules-b3` | correct | 12 lines; MT with φ=P∨Q; checked. |
| 03:503 | `exr-derived-rules-c1` | correct | (a) 7 lines, second MT with φ=¬P gives ¬¬P, ¬E 5,6 order right; (b) 9 lines; (c) does not claim necessity (only 'uses the rule of Section 2.5'). |
| 03:555 | `exr-derived-rules-c2` | correct | Circularity names the 'already derived' clause; MT replacement legitimate (MT proved from primitives). |
| 03:606 | `exr-derived-rules-c3` | correct | 12-line derivation checked; (2k)^2=2(2k^2); scheme 2+2+3+2+1=10; alternative (→I box) credited. |
| 04:11 | `def-rules-biconditional` | correct | Schemas match reference sheet; sibling boxes; ↔E both ways. |
| 04:59 | `exm-iff-symmetric` | correct | (a) 6 lines, (b) 6 lines; checked. |
| 04:112 | `prp-iff-two-implications` | correct | Both directions derived; supports the 'could have been an abbreviation' remark. |
| 04:122 | `proof:prp-iff-two-implications` | correct | Two 8-line derivations checked. |
| 04:170 | `exm-iff-negations` | correct | 12 lines, no RAA (only ↔E, ¬E, ¬I); converse claim l.209 stated without proof, nothing depends on it (true: Kripke refutation, verify/_s05s06_logic). |
| 04:217 | `def-provable-equivalence` | correct | l.227 ¬¬P⊢P pointer to Ch 3 (covered by thm-raa-independent); warning's P ⊬ P∧Q refuted by P: 2>1, Q: 1>2 — correct. |
| 04:231 | `prp-provable-equivalence-basics` | correct | Drop one direction in (a): P∧Q ⊢ P but ⊬ (P∧Q)↔P. |
| 04:246 | `proof:prp-provable-equivalence-basics` | correct | Copy observation: added boxes contain both ends of every internal citation; box availability preserved; premise lines → repetitions of an available line. (⇒),(⇐),(b) checked. |
| 04:282 | `thm-odd-iff-square-odd` | correct | Hypothesis n integer (parity undefined otherwise). |
| 04:292 | `proof:thm-odd-iff-square-odd` | correct | (⇐) ∨E on (E1), even case: n^2=2(2k^2), ∧I, ¬E (E2), ⊥E. l.300 one-breath version (¬I, MT, DS) correct. |
| 04:304 | `thm-squares-order` | correct | Counterexamples verified: x=-2,y=1 kills (⇒) without x≥0; x=1,y=-2 kills (⇐) without y≥0. Remark matches the printed proof (S5 fix present). |
| 04:317 | `proof:thm-squares-order` | correct | (⇒) x^2≤xy≤y^2; (⇐) y<x ⇒ x>0 ⇒ xy<x^2, y^2≤xy ⇒ y^2<x^2 clash; ⊥E. Correct. |
| 04:331 | `check:04-biconditional-and-definitions:1` | correct | (⇐) proved by ∨E; (⇒) via (x-1)(x+1)=0. |
| 04:361 | `exm-strictly-increasing-both-ways` | correct | (a) 3x-5<3y-5; (b) ↔E then →E; (c) h(-1)=1, h(0)=0, 1<0 false, ¬I. |
| 04:393 | `prp-equivalence-cycle` | correct | Drop R→P: P→Q, Q→R ⊬ P↔Q (P false, Q true). |
| 04:403 | `proof:prp-equivalence-cycle` | correct | 9 lines; rotation argument: premises map to themselves as a set. |
| 04:435 | `exm-unit-interval-tfae` | correct | (b)⇒(c): x≤0 ⇒ x≤x^2 clash; divide by x>0 twice; (c)⇒(a). DS legitimately available (after §03). |
| 04:472 | `exr-biconditional-and-definitions-a1` | correct | (c) k=5; (d) x=-2 refutes the converse. |
| 04:495 | `exr-biconditional-and-definitions-b1` | correct | 9 lines checked. |
| 04:527 | `exr-biconditional-and-definitions-b2` | correct | n+3=2(k+1)+1; n=2(j-1). Correct. |
| 04:541 | `exr-biconditional-and-definitions-b3` | correct | thm-squares-order with roles exchanged, exm-iff-negations as derived rule, then the quoted fact. Correct. |
| 04:553 | `exr-biconditional-and-definitions-c1` | correct | 36k^2=6(6k^2); n^2=2(3j)=3(2j); 3b=6c+3=2(3c+1)+1. Cites @exr-negation-and-contradiction-b3 (a) (S5 fix present). Scheme 1+2+3+4=10; alternative 1+3·3=10. |
| 04:598 | `exr-biconditional-and-definitions-c2` | correct | (a) (⇐) survives, (⇒) fails at x=-2,y=1; (b) |x|^2=x^2. |
| 05:13 | `exm-raa-zero` | correct | ε=x/2 chosen after x (depends on x only); x≤x/2 ⇒ x≤0 clash with x>0. Drop x≥0: x=-1 satisfies x≤ε ∀ε>0 and x≠0. Rule-by-rule reading l.616-622 correct (DS on x=0∨x>0; ¬E with x≤0 first). |
| 05:43 | `def-rule-raa` | correct | Schema and clauses correct. l.79 last-step argument valid (¬¬ψ derived at the top of the new ¬I box is available wherever the old assumption was); only the last step claimed (S5-A gap fixed). l.37: ¬¬P⊬P promised to Ch 3; the other two stalls marked without proof (both true: Kripke refutations checked). |
| 05:85 | `check:05-reductio-and-classical-rules:1` | correct | (i) RAA, (ii) ¬I, (iii) neither. Correct. |
| 05:128 | `prp-double-negation` | correct | (a) no RAA, (b) RAA. Drop the premise in (b): ⊬ P. |
| 05:145 | `proof:prp-double-negation` | correct | Both 4-line derivations checked; non-example (¬I writing P) correctly rejected. |
| 05:187 | `prp-contrapositive-converse` | minor | Derivation correct (RAA at 6); necessity marked without proof (true, Kripke). l.221 remark on Q a negation correct. Minor wording: l.221 "going from P→Q to ¬Q→¬P needs only the rules for ¬" — the derivation also uses →I and →E (l.185 says correctly 'the rules for → and ¬'). Write 'needs no RAA'. |
| 05:197 | `proof:prp-contrapositive-converse` | correct | 7 lines; line 5 cites 2 (open box). |
| 05:225 | `prp-excluded-middle` | correct | No premises; the aftermath 'the paragraph after De Morgan's laws ... and part (b) of the result after them' is true (S5-B fix present). |
| 05:235 | `proof:prp-excluded-middle` | correct | 8 lines, RAA once; assumption used at 4 and 7. |
| 05:266 | `prp-peirce` | correct | Try-it-first present; 'every derivation must use RAA' marked 'we do not prove it' (true, Kripke). |
| 05:280 | `proof:prp-peirce` | correct | 10 lines, RAA at 9; idea's 'one level out' narration matches the derivation and §06's step-5 clause. |
| 05:315 | `prp-de-morgan` | correct | (d) necessity marked without proof. Drop the premise of (d): ⊬ ¬P∨¬Q. |
| 05:336 | `proof:prp-de-morgan` | correct | (a)-(c) 10 lines each, no RAA; (d) 13 lines, RAA at 6,10,13. LEM route recounted: 11 lines (verified by writing it out). |
| 05:445 | `check:05-reductio-and-classical-rules:2` | correct | Line 6 first to lose justification; (a)-(c) survive. |
| 05:457 | `prp-implication-as-disjunction` | correct | (a) no RAA; (b) LEM. Drop premise of (b): ⊬ ¬P∨Q. |
| 05:474 | `proof:prp-implication-as-disjunction` | correct | (a) 11 lines (R at 9 needed), (b) 8 lines; checked. |
| 05:537 | `thm-classical-rules-interderivable` | correct | Dropped-hypothesis attempt: remove ⊥E from the base list — ③ fails at k+4; the text's claim that LEM then no longer derives ¬¬E is marked without proof and is true (read ⊥ and every ¬φ as true: all rules but ⊥E and RAA preserve truth, LEM true, ¬¬P⊢P fails at P false). |
| 05:549 | `proof:thm-classical-rules-interderivable` | correct | ① 3-line and 8-line replacements; ② ¬I then ¬¬E, box unchanged; ③ six lines, k+3 cites m legally, ∨E boxes available at k+5; renumbering paragraph; chaining LEM⇒RAA via ②+③ and ¬¬E⇒LEM via ①+② correct. Schemas hand-checked. |
| 05:648 | `exr-reductio-and-classical-rules-a1` | correct | (a) ¬I (3<7/2<4); (b) RAA ((x-1)^2<0); (c) →I; (f) lines 5, 9; (g) ¬I. Correct. |
| 05:680 | `exr-reductio-and-classical-rules-b1` | correct | (a) 12 lines, three ¬I boxes, no RAA; (b) 7 lines, RAA. Checked. |
| 05:742 | `exr-reductio-and-classical-rules-b2` | correct | 12 lines, RAA at 6 and 11. |
| 05:781 | `exr-reductio-and-classical-rules-b3` | correct | 4 lines; R needed. |
| 05:806 | `exr-reductio-and-classical-rules-b4` | correct | x>1 ⇒ x>0 ⇒ x^2>x; ② gives ¬¬(x≤1) then ¬¬E. Correct. |
| 05:835 | `exr-reductio-and-classical-rules-c1` | correct | Fragment schema hand-checked (i=h+2, ∨E h,h+1-h+1,i-j+1); box unmoved so citations unchanged; (b) savings correct. |
| 05:885 | `exr-reductio-and-classical-rules-c2` | correct | expect-invalid fails exactly at line 6 (cites line 3 of closed sibling box); (c) P∨Q ⊢ P refuted by P false, Q true; (d) 11 lines checked; 'part (d) below' wording present. |
| 05:955 | `exr-reductio-and-classical-rules-c3` | correct | 9 lines, primitive rules only, RAA line 9 classical; second route correct; scheme 2+3+2+2+1=10. |
| 06:29 | `def-partial-derivation` | correct | Definition consistent with def-derivation; non-example (open box at bottom) correct. |
| 06:41 | `check:06-finding-derivations:1` | error | Solution l.46: "Lines 1, 8 and 9 ... line 7 lies below the gap" is false. In the second snapshot (l.129-148) line 7, ¬(P∧Q) by ¬I 2-6, stands at top level ABOVE the box opened at line 8; it is in no box and 7 < 11, so it is available at line 11 (def-derivation) and is a resource. Correct answer: lines 1, 7, 8, 9 (lines 2-6 excluded, closed box). The same omission is in exm-search-distribute l.154. |
| 06:80 | `check:06-finding-derivations:2` | correct | (a) ¬I, (b) →I then postpone, (c) ∧I, (d) LEM on P route verified. |
| 06:99 | `exm-search-distribute` | minor | Snapshots and 14-line derivation checked; 'nine of the fourteen' (2,6,7,8,9,11,12,13,14) and 'four' (3,4,5,10) correct. Minor: l.154 "The resources are lines 1, 8 and 9" omits line 7 (available at 11; see check:06:1). Harmless to the search. |
| 06:192 | `exm-search-cases` | correct | 8 lines; snapshot numbering matches; 'current goal' paragraph correct. |
| 06:253 | `exm-search-postpone-or` | correct | Dead end analysis correct; rows (P,Q true,R false) and (P,R true,Q false) verified; LEM-on-Q derivation 14 lines; the LEM-on-P alternative written out: 22 lines, as stated. |
| 06:355 | `exm-search-raa` | minor | Sequent valid; 13-line derivation checked; snapshots' numbering matches; 'stuck a second time' after LEM on P true (case ¬P needs RAA for Q). Minor: the title "A search that must assume the negation of its goal" is a necessity claim that is neither proved nor marked (true intuitionistically — sidecar's Kripke witness — but not in the book), and read literally it is contradicted by l.436 (LEM on P also works). Retitle, e.g. "A search that reaches step 5 at once". |
| 06:472 | `exm-skeleton-odd-product` | correct | mn=2(kn); CP, ¬I via (E2), DS on even∨odd; no RAA — true. |
| 06:695 | `exr-finding-derivations-a1` | correct | (a) S5-B-corrected wording present; (b)-(f) correct. |
| 06:726 | `exr-finding-derivations-b1` | correct | (a) 7 lines; (b) 12 lines with VI (hand-checked the \by{VI} line), 15 primitive; necessity of RAA for P marked 'we do not prove' (true); (c) 8 lines; RAA alternative works (checked). |
| 06:812 | `exr-finding-derivations-b2` | correct | →I 3-8; 9 lines. |
| 06:864 | `exr-finding-derivations-b3` | correct | 10 lines checked. |
| 06:897 | `exr-finding-derivations-c1` | correct | Blank schema numbering matches the 12-line completion; checked. |
| 06:965 | `exr-finding-derivations-c2` | correct | 13 lines; (b) claims only that the method needs step 5 (argued); scheme 3+2+2+1+2=10, RAA route credited (S6 fix present). |
| 06:1033 | `exr-finding-derivations-c3` | minor | RAA route 13 lines checked, search steps match; LEM-on-P route 11 lines (written out and counted); scheme 2+2+2+3+1=10. Minor: the scheme's parenthesis "LEM on Q also works, but needs a second classical step, an RAA for P in the case Q" is an unmarked necessity claim (true: ¬(¬P∧Q), Q ⊬ P without RAA, Kripke-checked). Say 'our route then uses a second classical step'. |
| 06:1092 | `exr-finding-derivations-c4` | correct | (a) 6 lines, (b) 6 lines RAA; 'needed' is about the reader's derivations; no unmarked necessity claim. |
| 06:1145 | `exr-finding-derivations-r1` | correct | Cases a≥b / a<b; correct. |
| 06:1161 | `exr-finding-derivations-r2` | correct | 11 lines checked; translation ¬(N∨G) correct. |
| 06:1201 | `exr-finding-derivations-r3` | correct | 9 lines checked; converse refuted by P=R=F (either Q), pointer to Ch 3. |

## Resolution (S7, reviser, round 1)

| finding | resolution |
|---|---|
| 01:24 `def-rules-contradiction` (l.58, l.60) | Fixed. l.58: other rules (⊥E, →E from φ → ⊥) only pass a ⊥ along and need ⊥ in a line they use; apart from assumptions, ⊥ first appears only by ¬E, "the one rule whose new line is always ⊥". l.60: the honesty remark now argues only for a ⊥ written by ¬E and leaves the rules that pass ⊥ along to Chapter 3. |
| 01:422 A1(c) | Fixed: "⊥E needs a line ⊥ to start from. The rule that records a clash as ⊥ is ¬E, and it needs two lines φ and ¬φ." |
| 03:290 "comm. of ∨" | Fixed: `\by{or commutes}{1}` (as `\by{VI}`, no parentheses), and the prose step reads "[or commutes], by the exchange of disjuncts of @exm-disjunction-first-derivations used as a derived rule". check_fitch now notes "(or commutes)". |
| 05:187 l.221 | Fixed: "needs no RAA". |
| 06:41 check (error) and 06:99 l.154 | Fixed: "Lines 1, 7, 8 and 9 … Line 7 lies in no box and above the gap, so it is available, though this gap will not need it. Lines 2–6 … a box that has closed." l.154: "lines 1, 7, 8 and 9, and line 7 is not needed". |
| 06:355 `exm-search-raa` title | Fixed: "A search that reaches step 5 at once". |
| 06:1033 C3 scheme | Fixed: "LEM on Q also works; our route with it then uses a second classical step …". The section's dependency-ledger line was aligned. |
| 06:462 "A search that fails" vs the step-5 clause | Fixed: added the outer route — an RAA box on ¬(Q → P) around the whole search needs Q → P for its clash, and step 2 opens the same box on Q with goal P. |
| 06:65–67 algorithm control flow | Fixed: step 4 now ends "… and manufacture it, starting again at step 2 for that goal." |

Chapter 1 changes needed: none.
