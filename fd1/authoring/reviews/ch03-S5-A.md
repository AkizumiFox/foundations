# Chapter 3 — S5 Referee A (proofs)

**Scope:** `src/ch03-semantics-soundness-completeness/` §01–§07 and `index.md` (read-only), against `authoring/blueprints/ch03.md`. The Chapter 1–2 labels it cites were read in `src/ch01-connectives-and-derivations/` and `src/ch02-negation-and-classical-logic/`: `def-derivation` (Ch 1 05:157–203: scope rule, nesting, context, last line in no box), `def-rules-implication`, `def-rules-disjunction`, `def-rules-negation`, `def-rule-raa`, `def-rules-biconditional` (each says the box's last line is a line of that box itself), `def-derived-rule`, `prp-contrapositive`, `prp-vacuous-implication`, `prp-ex-falso`, `exm-double-negation-introduction`, `prp-de-morgan` (Ch 2 05:438 says (a)–(c) use no RAA), `prp-peirce` (stated as ⊢ ((P→Q)→P)→P), `exm-search-postpone-or`, `exr-finding-derivations-c2` (13 lines), `exm-disjunction-regroup` (line 11 remark), and the §06 reference sheet (primitive-rule list). Referee A, blind to Referee B. Verdicts are **not** written to the ledger.

**Method.**
- Scratch copy `scratchpad/S5a-ch03-refA`. `python3 tools/check_fitch.py src/ch03-semantics-soundness-completeness --notes`: 31 derivations (2 schema), 20 truth tables, 0 errors, **but 116 lines "shape not checked"**: the checker reads only capital letters as propositional atoms, so every lowercase-atom derivation and every table header was skipped. I therefore ran it again on a transformed copy (`up/tr.py`: inside `nd` blocks and `array` headers, p q r s → P Q R S, α β → A B, φ ψ χ → X Y Z): 31 derivations, 20 tables, **0 errors**; the remaining notes are the `\by{…}` lines (hand-checked below), the two schema blocks, and 5 table columns with `\neg` glued to a metavariable (hand-checked: standard columns). **Tooling note for the orchestrator:** the untransformed run's "0 errors" certifies almost nothing in this chapter.
- All 59 sidecars `verify/ch03/*.py` pass (`.venv/bin/python`).
- Hand-checked: the schema blocks 02:51 (→I box for the inductive step) and 06:370 (shape of `lem-atom-splitting`, matches the proof's steps 1–5); every `\by{…}` line: 05:507 (Y), 06:321–323, 06:480/485/495/500, 06:698, 06:757, 06:766 — each is an instance of the named row of `lem-connective-rows` with the stated α, β, and cites available lines.
- Every proof read step by step, reason named; each hypothesis traced to its use; one dropped-hypothesis counterexample per theorem/lemma (evidence column). No ε/δ arguments; the chosen objects are k = n−3 (depends on n only), the valuations w (depends on v) in `lem-substitution`, v⁺/v⁻ (depend on v and j) in `thm-completeness`, and the refuting valuation of `prp-cnf-validity` (depends on the clause): all chosen after what they depend on.
- Every "needs / does not need RAA" claim checked: the three-valued cases by hand (and by the sidecar); the unproved non-derivability claims (05:356 De Morgan (d), (p→q)∨(q→p); 06:776 ¬(p↔q) ⊢ ¬p↔q) checked for truth by two-world Kripke models, and each is marked "without proof".
- Optional result: `thm-raa-independent` is pointed at only in prose (06:11, 06:562); no proof, idea, claim-in-a-proof or solution rests on it (STYLE §Optional results allows prose pointers). No proof rests on an exercise.

**Counts (106 labelled items):** correct 100 · minor 6 · gap 0 · error 0.

## Critical checks

| Check | Verdict | Evidence |
|---|---|---|
| Induction chain has no circularity | correct | `ax-induction` → `thm-strong-induction` (Q(n) = "P(k) for all k ≤ n") → `thm-structural-induction` (strong induction on position in a formation sequence, 02:216) → `lem-parenthesis-count` → `thm-unique-readability` → `thm-structural-recursion` (ordinary induction on length with "n-good" functions; blueprint said strong induction on symbols, equivalent). No use of height before 02:340; the 02:230 remark only mentions it. |
| `lem-context-inclusion` (b) hypothesis "cited by a box rule" | correct | Proof 05:83–87 uses the box scope rule (Ch 1 05:162, "boxes other than itself that contain it are exactly the boxes containing line k") and the last-line sentence of each of the five box rules (all present in the Ch 1–2 blocks). Drop "cited by a box rule": the 05:97 derivation (box 2–4 ending on inner box 3–4) has Γ₄ = p, q, r ≠ Γ₅, p. |
| Soundness: every primitive rule has a case | correct | 13 rules of the Ch 2 §06 reference sheet (R, ∧I, ∧E, →I, →E, ∨I, ∨E, ¬I, ¬E, ⊥E, RAA, ↔I, ↔E) all treated; skipped halves (∧E right, ↔E second form) are exact mirrors. Derived rules removed in Step 1 (via `def-derived-rule`, Ch 2 §2.3). |
| Three-valued RAA independence | correct (one minor) | All 12 non-RAA cases re-derived by hand: →E (x ≤ y or u(φ→ψ) = y), →I (min{m,x} ≤ y < x forces min = m), ¬I, ¬E (u(¬φ) ∈ {0,1}), ∨E (split x ≥ y / y > x), ↔I/↔E via min of implications. u(p)=½: u(¬¬p)=1 > ½; u(p∨¬p)=½ < 1. Peirce at (½,0) = ½ checked. De Morgan (d) and (p→q)∨(q→p) indeed pass (¬ is 0/1-valued; the order is linear). |
| Completeness uses RAA exactly once | correct | `lem-connective-rows`: 7 printed derivations (checked, no RAA), cited results `prp-vacuous-implication` (Ch 2 §01), `exm-double-negation-introduction` (§02), De Morgan (b),(c) (no RAA, Ch 2 05:438); `prp-ex-falso` (§01). Only LEM in `lem-atom-splitting`. |
| Downward induction in Step 3 | correct | T(m): "m ≤ n+1 ⇒ S(n+1−m)"; T(1) = S(n); step needs 1 ≤ j = n+1−m ≤ n, from 1 ≤ m ≤ n; T(n+1) = S(0); a valuation exists (all-T). n = 0 covered (06:450). |
| Pasting lemmas | correct (one minor) | `lem-weakening-cut` (∗): premise-last-line case split off; redirected citations land on lines in no box, earlier than E; box sets unchanged so availability is unchanged. `lem-atom-splitting`: premise p (resp. ¬p) redirected to the box assumption, which is available throughout its box; D ending on a premise handled (assumption alone, or R line); final ∨E cites a line and two boxes in no box. |

## Findings (every labelled item)

| file:line | item | verdict | evidence |
|---|---|---|---|
| 01:41 | `def-formula` | correct | Length bounds (¬φ ≥ 2, (φ∘ψ) ≥ 5) and the first-symbol test follow from "looking at the last step" (01:65–71). Substitution paragraph 01:363–369: formation sequence, rule instance (schemas contain no atoms), citations unchanged — sound. (Note only: at 01:365 an old atom entry becomes a copy of the last entry of a prefixed sequence; it is a legal entry because it is built from the same earlier entries — obvious, not stated.) |
| 01:73 | `exm-formation-sequences` | correct | All four sequences legal; entry 5 = (χ₄ → χ₁). |
| 01:99 | `exm-not-formulas` | correct | Lengths 4, 4, 4, 3 right; (¬p) fails because ¬p contains no binary connective. |
| 01:161 | `def-parse-tree` | correct | Existence along a formation sequence (01:177). |
| 01:181 | `exm-parse-trees` | correct | (c) 10 nodes, 9 subformulas, heights 4 and 4 (01:252, 01:264). |
| 01:236 | `def-subformula` | correct | Check 01:268: 8 subformulas, height 4. |
| 01:258 | `def-height` | correct | Well-definedness deferred to 02:340, as stated; ¬(p∧¬q) 7 symbols, ((p∧q)∧(r∧p)) 13 symbols height 3. |
| 01:302 | `exm-shorthand-translation` | correct | p=q=r=F: p→(q→r) T, (p→q)→r F. |
| 01:400 | `exr-formulas-and-parse-trees-a1` | correct | (iv) "(p" has length 2 and begins with "(" — not a formula; (c) true: a branch below the root extends by the root path. |
| 01:434 | `exr-formulas-and-parse-trees-b1` | correct | Heights 3, 3, 3; 5, 5, 6 subformulas. |
| 01:471 | `exr-formulas-and-parse-trees-b2` | correct | (b) (p → ((q∨r) → ¬p)), ((¬p∧q) ↔ r). |
| 01:492 | `exr-formulas-and-parse-trees-c1` | correct | c₄ = 2+1+2 = 5; Catalan C₁₀ = 16796 for 11 atoms. |
| 02:21 | `ax-induction` | correct | Axiom. Warning 02:122: 2n² ≥ (n+1)² iff n ≥ 1+√2; 2³ = 8 < 9. |
| 02:68 | `exm-sum-consecutive-products` | correct | n(n+1)(n+2)/3 + (n+1)(n+2) = (n+1)(n+2)(n+3)/3; IH used once. |
| 02:99 | `exm-power-inequality` | correct | 3·3ⁿ ≥ 6n+3 ≥ 2n+3. |
| 02:131 | `thm-strong-induction` | correct | Base: vacuous k < 1 gives P(1); step: k < n+1 ⇔ k ≤ n. Drop the hypothesis at n = 1 (only n ≥ 2): P(n) := "n ≥ 2" satisfies it and fails at 1. |
| 02:165 | `exm-threes-and-fives` | correct | k = n−3 ≥ 8 for n ≥ 11; 7 = 3a+5b impossible. |
| 02:195 | `thm-structural-induction` | correct | Q(i) = "i ≤ m ⇒ P(χᵢ)"; j, l < i ≤ m. Drop (i) for ⊥: "contains an atom" (warning 02:234); drop (ii): the property of check 02:244 fails at ¬p. |
| 02:257 | `lem-parenthesis-count` | **minor** | Proof correct: five kinds of initial segment exhaustive and disjoint, strict clause for the middle three; (c) gives 1 before ∘, ≥ 2 elsewhere. But 02:269 says "(b) and (c) are what the unique readability theorem needs", while the proof of `thm-unique-readability` (02:333) uses only (a) and (c), and `exr-induction-a1` (d) (02:451) correctly says "Part (b) is not used in that proof". (b) is used by `exr-induction-c1`. Fix 02:269: "(c), with (a), is what the unique readability theorem needs; (b) gives a second proof of it (Exercise C1)". |
| 02:309 | `thm-unique-readability` | correct | Main connective = unique binary connective with prefix excess 1; φ, φ′ are the same substring. Drop parentheses from (F3): p∧q∨r splits two ways. Unique parse tree paragraph 02:340 is a correct structural induction. |
| 02:350 | `thm-structural-recursion` | correct | n-good functions well posed (parts shorter); existence uses UR at length n+1; uniqueness does not; f(χ) := h_{len χ}(χ) obeys the clauses since h_m restricts to h_n. Drop UR: the 02:387 remark (two values at one string). |
| 02:389 | `exm-recursive-definitions` | correct | Height 4, atoms {p,q}, 4 connectives, length 14 (6+5+3). |
| 02:428 | `exr-induction-a1` | correct | (a)(ii) 12–15 as 4a+5b; (e) uniqueness by structural induction indeed needs no UR. |
| 02:458 | `exr-induction-b1` | correct | 2(n+1) ≥ n+2. |
| 02:478 | `exr-induction-b2` | correct | 1+s(φ)+s(ψ) ≤ len(φ)+len(ψ)+1 < len+3. |
| 02:500 | `exr-induction-b3` | correct | 2^a, 2^b ≤ 2^{h−1}; ¬ case 2^h ≤ 2^{h+1}−1; 7 nodes at height 3. |
| 02:527 | `exr-induction-c1` | correct | ¬ case: u = ¬u′, u′ = φ″ nonempty proper segment of φ; binary case by (b) vs (a); (b) of the exercise avoids UR. |
| 02:572 | `exr-induction-c2` | correct | Line 5 applies the hypothesis to the non-formula φ∘ψ; same move with property (c) on (p∧q) asserts a falsehood. |
| 02:605 | `exr-induction-c3` | correct | Restriction inside the property; ∧ case uses both hypotheses; ⊥/∨/→/↔ vacuous. |
| 03:53 | `def-valuation` | correct | |
| 03:75 | `def-truth-value` | correct | Well defined by `thm-structural-recursion` (03:115); p∧q∨r at (F,F,T): T vs F. Opening motivation (03:9–45) is marked motivation only; Q ⊢ P→Q derivation checked. |
| 03:121 | `exm-value-down-the-tree` | correct | Value T. |
| 03:164 | `lem-coincidence` | correct | All six cases written; C(φ) quantifies over all v, w. Drop agreement on atoms: check 03:203 (φ∧r differs). |
| 03:212 | `def-truth-table` | correct | Existence (extend by F) and independence (coincidence) both shown; empty list gives 1 row. |
| 03:224 | `exm-truth-table-modus-ponens` | correct | Table checked by tool. |
| 03:249 | `exm-table-contrapositive` | correct | Table checked. |
| 03:273 | `exm-backwards-from-f` | correct | Table checked; one F-row TTF. |
| 03:329 | `exr-valuations-and-truth-tables-a1` | correct | Tables checked; (e) false: p→(q→p) is a tautology. |
| 03:383 | `exr-valuations-and-truth-tables-b1` | correct | (a),(b) valid; (c) TFF, FTF; (d) p=F, r=T, q free — all verified by sidecar and by hand. |
| 03:406 | `exr-valuations-and-truth-tables-b2` | correct | → case identical to ∧ case. |
| 03:456 | `exr-valuations-and-truth-tables-b3` | correct | Table checked; DS. |
| 03:478 | `exr-valuations-and-truth-tables-c1` | correct | (E) forces (T,F)↦F; (I) with Γ empty, φ=ψ=p forces TT, FF; Γ = q, φ = p, ψ = q forces FT; no → in the formulas used. |
| 03:526 | `exr-valuations-and-truth-tables-c2` | correct | Error in line (4); p→q; repair by true conclusion. |
| 04:11 | `def-tautology` | correct | Atom-free formulas constant (coincidence). |
| 04:28 | `def-satisfiable` | correct | p→q, q→r, r→¬p: satisfiable at (F,T,T); p = T forces r→¬p false. |
| 04:54 | `def-valid-argument` | correct | Paraphrases (empty Γ, unsatisfiable Γ, more premises, Γ,¬ψ unsatisfiable) each argued from V2 and the definition. |
| 04:86 | `exm-affirming-the-consequent` | correct | Row p=F, q=T. |
| 04:100 | `exm-three-premise-entailment` | correct | Backwards from F reaches p∨q false. |
| 04:114 | `exm-grouping-of-implications` | correct | First holds; second refuted by p=r=F. |
| 04:146 | `def-semantic-equivalence` | correct | ≡ iff equal values iff ⊨ φ↔ψ; argued both ways. |
| 04:162 | `prp-standard-equivalences` | **minor** | Proof correct (values of both sides depend only on (a,b,c); all tables checked by tool on the transformed copy). Many-term paragraph 04:251: induction on n over all lists, correct. Minor: 04:242 "some directions only with RAA or LEM (@prp-de-morgan (d), @prp-double-negation, @prp-implication-as-disjunction)" reads as a necessity claim; for (d) and implication-as-disjunction it is true (Kripke) but unproved and not marked "without proof" as Chapter 2 and 05:356 mark it. Fix: "some directions with RAA or LEM (…); that they cannot do without it is Chapter 2's statement without proof, except for ¬¬P ⊢ P (optional @thm-raa-independent)". |
| 04:271 | `lem-replacement` | correct | Occurrence at root or in exactly one immediate part (UR); binary case by the same clause. Drop ≡ for one-way ⊨: warning 04:306 (¬(p∧q) vs ¬p at TF). Chain 04:298–300 checked. |
| 04:326 | `lem-substitution` | correct | w(p) := v(σ(p)); claim v(σχ) = w(χ) by structural induction; (a), (b) follow. Drop uniformity: q→p from p→p (04:360). |
| 04:383 | `exr-entailment-and-equivalence-a1` | correct | All classifications and rows verified. |
| 04:406 | `exr-entailment-and-equivalence-b1` | correct | Derivations (a) MT, (b) DS, (d) ∨E checked by tool; (c) row F,T. |
| 04:473 | `exr-entailment-and-equivalence-b2` | correct | Table checked. |
| 04:493 | `exr-entailment-and-equivalence-b3` | correct | Both directions via V5. |
| 04:516 | `exr-entailment-and-equivalence-c1` | correct | NAND case via V7 and both hypotheses. |
| 04:557 | `exr-entailment-and-equivalence-c2` | correct | σ(φ↔ψ) = σφ ↔ σψ; the "creating an equivalence" remark (p vs ¬q, q ↦ ¬p) is right. |
| 05:65 | `lem-context-inclusion` | correct | See critical checks. Drop "available" in (a): a line of a closed box cited later would have Γᵢ ⊄ Γₖ. |
| 05:124 | `thm-soundness` | correct | Step 1 reduction; S(k) by strong induction; (∗) from (a), (∗∗) from (b); all 13 cases; Step 4 via "adding premises keeps ⊨" and `def-derivable` "belong to Γ". Check 05:112 (line 5 of contrapositive) and exm run verified. Dropped hypothesis: add rule Y (C1(b)) — Claim 2 fails, p ⊢_Y q refuted by p=T, q=F. |
| 05:224 | `exm-soundness-run` | correct | Derivation checked; contexts and cases right. |
| 05:266 | `cor-refuting-row` | correct | Contrapositive of soundness. Payments: p→q ⊬ q→p (F,T); p→q, q ⊬ p (F,T); ¬(p∧q) ⊬ ¬p (T,F), ⊬ ¬q (F,T); check p→r ⊬ (p∨q)→r (F,T,F). Drop "every premise true": warning 05:293. |
| 05:323 | `thm-raa-independent` (optional) | **minor** | All cases correct (see critical checks). The statement covers "derived rules derived from those", but the proof begins "Fix a derivation that uses only the primitive rules other than RAA" without the reduction of derived-rule lines. Add one sentence: "As in Step 1 of the proof of @thm-soundness, a derived rule derived without RAA abbreviates a pasted derivation in the primitive rules other than RAA, so it is enough to consider those." |
| 05:363 | `exr-soundness-a1` | correct | (a) line 5 cites line 2, three back; (c) contexts; (d) row F,T. |
| 05:415 | `exr-soundness-b1` | correct | Rows (a) TFF, (b) TF, (c) FFT verified; (d) derivable (`exm-search-postpone-or`), only refuting candidate TFF makes the premise false. |
| 05:440 | `exr-soundness-b2` | correct | Order (iii),(v),(vii),(i),(viii),(iv),(ii) and the alternative both respect dependencies; (vi) applies IH to line k; (ix) uses Γₖ for line b. |
| 05:476 | `exr-soundness-c1` | correct | X case via V3, V4; Y derivation (4 lines, ∨I, Y, ∧E) and row T,F; failing line 3. |
| 05:525 | `exr-soundness-c2` | correct | Model answer matches the proof; marking scheme sums to 10. |
| 06:30 | `lem-weakening-cut` | **minor** | Proof of (a) and (∗) correct (see critical checks). Drop Γ ⊢ φ in (b): Γ empty, φ = ψ = p gives p ⊢ p but ⊬ p. Minor: 06:68 says part (c) "is the precise form of 'abbreviates'" and that "when a derivation cites a sequent proved earlier as a single line, the lemma … is the reason the result is a derivation in the primitive rules". (c) only chains whole derivations at the top level; the chapter's own derivations cite rows inside boxes (06:480, 485, 495, 500, 698, 757, 766), which the lemma does not cover. No proof depends on this (`lem-truth-table-line` and `thm-completeness` use (c) only at sequent level), and Step 1 of soundness rests on `def-derived-rule`, not on this lemma. Fix: "part (c) is the precise form of 'abbreviates' for a sequent applied to whole derivations; inside a box, @def-derived-rule's pasting is the same bookkeeping". |
| 06:82 | `lem-connective-rows` | correct | All 17 rows accounted for; 7 printed derivations checked by tool (4, 6, 7, 9, 6, 6, 2 lines), no RAA; cited sources verified RAA-free. Rows' directions right; warning 06:232 (p∨q ⊬ p). |
| 06:253 | `lem-truth-table-line` | correct | Property with the "atoms among" guard; ⊥ via (⊥1) and weakening; ¬ two subcases; ∧ and → three exhaustive cases each; ∨, ↔ cases fully named at 06:296. Drop "includes every atom": φ = q, list p, v(q)=T: p ⊢ q refuted by p=T, q=F. |
| 06:305 | `exm-truth-table-line-run` | correct | (¬1), (∧3) with β = ¬p, (→3) with β = q∧¬p: each \by line is an instance. |
| 06:343 | `lem-atom-splitting` | correct | See critical checks. Drop one hypothesis: Δ empty, p ⊢ p holds but ⊬ p (all-F row). Prompt answer: classical step only at LEM. |
| 06:396 | `thm-completeness` | correct | Claim: Case 1 via `lem-truth-table-line`; Case 2 via ¬γ, γ and `prp-ex-falso` by chaining. Step 3 and Step 4 as in critical checks. Drop finiteness: 06:536 remark and A1(f); drop RAA: optional result (prose pointer). |
| 06:456 | `exm-completeness-run` | correct | 20-line derivation checked on the transformed copy; \by lines 5 (→2 from q), 8 (→1, α = q), 14, 17 (→1 from line 11, available); it is exactly the pasting of the proof (split on q twice, then p). 13-line comparison verified in Ch 2. |
| 06:519 | `cor-derivable-iff-valid` | correct | Both directions cited; 2ⁿ rows by coincidence. |
| 06:572 | `exr-completeness-a1` | correct | (d) Case 2, p, ¬p, q ⊢ p∨q; (e) distinctness used for v± agreeing on p₁…p_{j−1}. |
| 06:603 | `exr-completeness-b1` | correct | 5, 5, 9 lines, checked, no RAA. |
| 06:669 | `exr-completeness-b2` | correct | 21 lines checked; line 8 (→3) from 4, 7; one-line box 6–6 legal; row cases right. |
| 06:727 | `exr-completeness-b3` | correct | Table checked; 12-line derivation checked (line 4 (↔2) with α=p, β=q; line 9 (↔1)); 22-line count by redirected pasting (7+5 non-premise lines) verified. "No derivation avoids RAA": true (two worlds w₀ < w₁, q forced only at w₁, p nowhere: ¬(p↔q) forced at w₀, ¬p→q not), marked without proof. |
| 06:781 | `exr-completeness-c1` | correct | Three ∨ cases and four ↔ cases, exhaustive. |
| 06:806 | `exr-completeness-c2` | correct | Model answer matches 06:356–447; scheme sums to 10. |
| 07:13 | `eq-many-term-values` | correct | Recalled from 04:251, proved there. |
| 07:22 | `def-literal` | correct | |
| 07:37 | `def-dnf` | correct | Examples 1–4 and check 07:66 verified. |
| 07:43 | `def-cnf` | correct | |
| 07:83 | `eq-row-conjunct` | correct | Each p_i^v true under w iff w(p_i) = v(p_i). |
| 07:86 | `exm-dnf-exclusive-or` | correct | |
| 07:102 | `thm-dnf` | correct | Case 1 k ≥ 1 and k = 0 (p₁∧¬p₁); Case 2 atom-free. |
| 07:132 | `thm-cnf` | **minor** | Proof correct (opposite literals; chain of four iff's; atoms of ¬φ = atoms of φ). Minor in the "Alternatively" paragraph 07:160: the rewriting steps (eliminate ↔, →; push ¬; remove ¬¬; distribute) do not remove ⊥, which is not a literal, so they do not reach a CNF for, e.g., p ∨ ⊥ or ¬⊥ ∧ p. Add "replace ⊥ by p ∧ ¬p for an atom p" or restrict the paragraph to formulas without ⊥. |
| 07:162 | `exm-normal-forms-two-routes` | **minor** | Table (tool), seven T-rows, one F-row FFF, CNF p∨q∨r, rewriting result and distribution all correct. Minor: φ = (p→q)→(¬q→r) has **three** implications, but 07:193 says "Eliminate both implications" and 07:201 "using (c) … twice"; the first displayed step uses (c) three times, and the second line already drops ¬¬q. Fix: "Eliminate the three implications … using (c) three times, then De Morgan's law (b), then double negation (d) twice". |
| 07:214 | `prp-cnf-validity` | correct | (a) both directions; refuting valuation well defined because no pair; (b) dual; duality paragraph 07:243 (K ≡ ¬D) correct. |
| 07:247 | `exm-cnf-validity-glance` | correct | (a) four pairs, 16 rows; (b) row s=r=T, q=F. |
| 07:270 | `def-truth-function` | correct | 2^(2^n); majority DNF right. |
| 07:283 | `def-adequate` | correct | |
| 07:291 | `thm-adequate-connectives` | correct | (a) D expresses f (k = 0 case included); t₁, t₂, t₃ values: ¬(¬a∧¬b), ¬(¬a∨¬b), (a→(b→⊥))→⊥, (a→⊥)→b all checked on four rows; D contains no ⊥, →, ↔ so the unused clauses are harmless. (b) all-T induction with the → case by the true conclusion. Drop ⊥ from {→,⊥}: warning 07:339. Check 07:343 row T,F gives F. |
| 07:354 | `exr-normal-forms-a1` | correct | (c) first not a tautology (row p=q=F), second is. |
| 07:380 | `exr-normal-forms-b1` | correct | (a) DNF/CNF of p↔¬q; (b) ¬p∨¬q∨r; (c) ¬p∧q∧¬r; rows checked. |
| 07:400 | `exr-normal-forms-b2` | correct | Table checked by tool. |
| 07:423 | `exr-normal-forms-b3` | correct | Four conjuncts; minimality: a satisfiable conjunct missing an atom is true on two rows of different parity, so every useful conjunct covers one row. |
| 07:441 | `exr-normal-forms-c1` | correct | α∣α ≡ ¬α, (α∣β)∣(α∣β) ≡ α∧β; dually for ↓. |
| 07:460 | `exr-normal-forms-c2` | correct | (a) ↔ case T,T ↦ T; (b) M is self-dual (at least two T after flip iff at most one T before), p₁∧p₂ is F on TF and FT. |
| 07:498 | `exr-normal-forms-c3` | correct | (a) 10 lines, (d) 9 lines checked, no RAA; (b) row TFF; (c) row T,·,F. |
| 07:573 | `exr-normal-forms-c4` | correct | T-rows TTT, TFT, TFF, FTT (table checked); DNF (p∧¬q)∨(q∧r); CNF and the redundancy of p∨r (resolution on q). |
| 07:625 | `exr-normal-forms-r1` | correct | 9 lines checked, no RAA. |
| 07:657 | `exr-normal-forms-r2` | correct | Only candidate row e=a=T, b=F falsifies the first premise. |
| 07:671 | `exr-normal-forms-r3` | correct | Backwards from F contradiction; 10 lines checked, no RAA; completeness correctly said not to settle "without RAA". |

## Outside this chapter (for the orchestrator, not a Chapter 3 finding)

- `tools/check_fitch.py` accepts only capital letters as propositional atoms, so on this chapter an untransformed run skips 116 lines and every truth-table header while reporting 0 errors.

## Resolution (S7, reviser, round 1)

| finding | resolution |
|---|---|
| 02:257 `lem-parenthesis-count` (02:269) | Fixed, together with Referee B's 02:249/269 row. 02:249: "two refinements: one that the next theorem needs, and one that Exercise C1 uses". 02:269: "(c), with (a), is what the unique readability theorem needs, and (b) shows that no proper initial segment of a formula is a formula (Exercise C1). The steps for (b) and (c) use (a) for the parts, so the three are proved together." |
| 04:162 `prp-standard-equivalences` (04:242) | Fixed, together with Referee B's 04:242 row: "some directions with derivations that use RAA or LEM (…) and others without. That some of them cannot do without a classical rule, Chapter 2 stated without proof (for De Morgan (d), for instance); for ¬¬P ⊢ P, Section 3.5 proves it in an optional result." |
| 05:323 `thm-raa-independent` | Fixed: the proof now opens "As in Step 1 of the proof of @thm-soundness, a derived rule derived without RAA abbreviates a pasted derivation in the primitive rules other than RAA, so it is enough to consider those." |
| 06:30 `lem-weakening-cut` (06:68) | Fixed, together with Referee B's 06:42/68 row. 06:42: "Part (c) is @def-derived-rule for sequents: applying a proved sequent to formulas already derived, outside every box. Inside a box, Section 2.3's expansion does the same job." 06:68: the lemma covers a line in no box, @def-derived-rule a line inside a box; "for whole derivations, part (c) is the precise form of 'abbreviates', and inside a box the pasting of @def-derived-rule is the same bookkeeping." |
| 07:132 `thm-cnf` (07:160) | Fixed: the rewriting paragraph now begins "First replace each ⊥, which is not a literal, by p ∧ ¬p for an atom p; both are false in every row." |
| 07:162 `exm-normal-forms-two-routes` | Fixed: "Eliminate the three implications" and "using (c) of @prp-standard-equivalences three times". |
| Outside this chapter: `check_fitch.py` reads only capital atoms | Not a Chapter 3 change; left to the coordinator (tools are outside S7's remit). No derivation or table was edited in this round. |

Ledger: S5a verdicts recorded for all 144 items (`--by refereeA`); S7 `correct` by reviser on every item touched. Gates re-run in `scratchpad/ch03-S7r1/repo`: html, pdf (ch03), check, pytest, check_fitch, check_structure, check_numbers, check_rendered, originality, promises all pass.

## Resolution (S7, reviser, round 2)

| finding | resolution |
|---|---|
| 07:132 `thm-cnf` (07:160), rejected at S7 recheck (N1) | Fixed. The sentence after the new first step now reads "the equivalences are \( \bot \equiv p \wedge \neg p \) and those of @prp-standard-equivalences, which hold for arbitrary formulas". |
| all other rows | Upheld as fixed at the recheck; unchanged. |

Ledger: S7 `correct` by reviser on `thm-cnf` (round 2). Gates re-run in `scratchpad/ch03-S7r2/repo`: `./build.py html`, `pdf` (all ch03 sections), `check` (378 labels, 1225 references), pytest (295 passed, 5 skipped), check_fitch (31 derivations, 20 tables, 0 errors), check_structure (0 fatal), check_numbers (60 sidecars, 0 fatal), check_rendered (0 errors), promises (0 unrecorded). originality.py 3 lists 24 shared 8-grams, all truth-table value rows (t/f strings) and one roman-numeral list, none of them prose; this round changed no table.
