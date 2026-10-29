# Design decisions (record)

These decisions were made on 2026-09-27, across two planning conversations and the plan that followed them. `curriculum.md` (same directory) holds the stage-by-stage content specification, and `sources.md` holds the reference books and their roles. Blueprints and chapters follow this file. When a decision changes, edit this file and say why. The route changes of 2026-09-28 (`roadmap.md` A1–A8, A10; evidence in `research-route.md` and `research-reader.md`) are recorded below where they amend an item. Also on 2026-09-28 the author expanded Part 0's logic from two chapters to four (items 1–3), which renumbered the book to 77 chapters (`roadmap.md`).

## The book
- **One book, seven Parts, written in English first.** A Chinese edition comes later; the engine has no CJK support yet (xelatex + ctex, interface strings and spell check all still to do).
- **The reader** is a motivated student who has never written a proof. By the end of Part VI they reach the level of a graduate qualifying exam in analysis. As benchmarks, the UCLA real and complex quals set the floor and the ceiling, and Fredholm theory, Sobolev spaces and Lax–Milgram are added from Cambridge Part II.
- **Linear algebra is not re-taught.** Our linear-algebra book (linear-algebra.akizumifox.com) is the companion text. It is cited with `@la:<label>` (amended 2026-09-28: the engine now resolves references into another book, config `external-books`; see STYLE §10 "The companion book"). Before that it was cited by chapter in prose, which remains the form for a whole chapter and the fallback when the companion is not built.

| Part | Title (working) | Course stage |
|---|---|---|
| 0 | Foundations: logic, sets, cardinality (+ optional ZF, ℕ, ℤ, ℚ) | three-year route, first semester; two-year route, a 3–4 week bridge (logic and sets only) |
| I | Analysis on the real line (+ optional Dedekind cuts and uniqueness of ℝ at the end) | S1 |
| II | Metric spaces, several variables and ODE | S2 |
| III | Fourier analysis (Riemann setting; finite groups optional) | Summer 1 |
| IV | Measure and integration (+ surfaces and the divergence theorem, probability) | S3 |
| V | Complex analysis | after IV on the two-year schedule (not in parallel: roadmap A10); or straight after II on the `complex-early` path |
| VI | General topology, functional analysis and distributions | S4, ending with the Dirichlet-problem capstone |

## Structural decisions
1. **Proof skills are practised inside analysis, not in a separate logic course.** Every rule Part 0's logic introduces comes with an example from real analysis. *(Amended 2026-09-28.)* The logic is five chapters, modelled on the depth of Huth & Ryan, *Logic in Computer Science*, ch. 1–2: `connectives-and-derivations` and `negation-and-classical-logic` (the former `propositional-natural-deduction`, split in two 2026-09-28), `semantics-soundness-completeness`, `predicate-logic` and `from-derivations-to-prose`; the two-year bridge reads selected sections of them.
2. **Logic is taught through natural deduction, as the grammar of proof.**
   - Each connective is defined by its introduction and elimination rules, and truth tables come afterwards (the next chapter), with soundness and completeness proved in full; structural induction is introduced there just in time.
   - A central table lines up rule, phrase in mathematical writing and Lean tactic.
   - A worked example annotates "uniformly continuous ⇒ continuous" step by step and shows, rule by rule, why the converse fails: an ∃-intro witness may not depend on a variable introduced later.
   - A catalogue of "what is not allowed" lists common errors and the rule each one violates, and Fitch boxes make the scope of assumptions visible.
   - The vacuous truth of implication is derived from ⊥-elimination.
   - A definition's "if" means "iff"; this is a convention of language, not a rule of logic.
3. **The last section of the logic chapters (the end of `from-derivations-to-prose`, Chapter 5) is the dispute over excluded middle.**
   - LEM, double-negation elimination and proof by contradiction are one extra rule, and intuitionistic logic still proves ¬¬(P ∨ ¬P).
   - The BHK reading of the connectives.
   - Irrational numbers a and b with aᵇ rational, proved with and without a witness: √2^√2 versus √2^(log₂9) = 3.
   - The history: Brouwer 1908, Hilbert's reply of 1927 and the Grundlagenstreit, Heyting 1930, the Gödel–Gentzen double-negation translation, and Bishop 1967.
   - Its consequences for analysis: sup of a located set, Specker's sequence, the approximate intermediate value theorem, the non-constructive step in Bolzano–Weierstrass.
   - Curry–Howard; Lean's `Classical.em` via Diaconescu, and `noncomputable`.
   - The main line stays classical.
4. **The number systems are constructed on a route beside the main line.**
   - Part 0 builds ℕ (Peano), ℤ and ℚ (equivalence classes) and ℝ (Dedekind cuts). It ends with the uniqueness of the complete ordered field, the bridge between "assume the axiom" and "build a model".
   - Part I opens from the **least upper bound axiom** (environment `ax`, label `ax-least-upper-bound`) and depends on no Part 0 construction. The constructions are `.optional`, so no main-line proof may cite them.
   - Routine verifications (the operations are well defined, the field axioms hold) are left mostly as exercises, to avoid becoming Landau.
   - **Placement (settled at the merge, 2026-09-27):** ZF with ℕ, and ℤ with ℚ, are optional chapters at the end of Part 0. The Dedekind-cut construction of ℝ and the uniqueness theorem are optional chapters at the **end of Part I**, after "The Forms of Completeness". They need Part I Chapter 1's ordered-field axioms, and a proof may not cite a later chapter, so this placement is forced. It also carries out the old recommendation to read Part I first and come back to the constructions.
   - **The axiom of choice is on the main line.** It is stated as `ax-choice` in Part 0's cardinality chapter, because Vitali, Hahn–Banach and Tychonoff cite it. Zorn's lemma is proved from it just in time, in Part VI's Hahn–Banach chapter.
5. **Cauchy completion is a spiral node in Part II.** The completion of a metric space, applied to ℚ, gives ℝ a second time; Lᵖ later reappears as a completion too.
6. **The spiral.** Convergence, completeness, compactness and continuity each return on ℝ, on ℝⁿ, on metric spaces and C(K), on normed and Banach spaces, on Hilbert spaces, and on Lᵖ and the weak* topology (see the spiral table in `curriculum.md`). When a concept comes back at a higher stage, the text explicitly recalls the earlier version.
7. **Every abstraction is forced by a concrete problem.**
   - ODE existence leads to contraction maps and Arzelà–Ascoli.
   - Whether Fourier series converge leads to the list of what the Riemann integral lacks, and so to Lebesgue.
   - The Dirichlet problem leads to Hilbert spaces and Lax–Milgram.
   - Polynomial approximation leads to Stone–Weierstrass.
8. **Point-set topology: metric in Part II, general in one block in Part VI.** *(Amended 2026-09-28, roadmap A2 / route R2. The earlier split into three places, end of Part II, start of Part IV and before Alaoglu, is reversed: no programme or text surveyed splits general topology, and nothing in Parts II–V uses the abstract theory.)*
   - Part II: metric topology only. `compactness-connectedness` carries a section on the metric Urysohn function d(x,A)/(d(x,A)+d(x,B)) and the Tietze extension theorem for metric spaces; that is all Part IV needs (Lusin, density of C_c in Lᵖ(ℝᵈ)).
   - Start of Part VI, just before its users: `topological-spaces-compactness` (topologies, bases, subspaces and arbitrary products, Hausdorff, compactness, the compact-to-Hausdorff theorem; quotient gluing as an optional section) and `separation-urysohn-lch` (normal spaces, Urysohn and Tietze, locally compact Hausdorff spaces, C_c and C_0, partitions of unity). Riesz–Markov uses the second at once.
   - Tychonoff (with Zorn) stays in `weak-topologies-alaoglu`, just before Banach–Alaoglu, with the diagonal proof in the separable case.
   - The block replaces the former chapters `topological-spaces`, `compactness-quotients` (Part II) and `urysohn-tietze` (Part IV), and is about 40 pages shorter.
9. **Load moved out of measure theory into Part VI.** Lᵖ duality, the Riesz–Markov theorem for C(K)*, weak topologies and abstract Hilbert space theory all go in Part VI. Part IV uses L² only for the von Neumann proof of Radon–Nikodym.
10. **Fubini–Tonelli and change of variables are proved in full** in Part IV. Part II covers the Riemann integral on ℝⁿ: Jordan content, Fubini for continuous functions, and linear change of variables.
11. **Complex analysis covers the qualifying-exam "second layer".** That means harmonic functions and Harnack, subharmonic functions, normal families, Hurwitz, infinite products, Weierstrass and Mittag-Leffler, Hadamard (in outline), analytic continuation and monodromy, Schwarz reflection, and little Picard.
12. **The divergence theorem is main line; differential forms and the general Stokes theorem are deferred.** *(Amended 2026-09-28, roadmap A1 / route R1.)* The main-line chapter `surfaces-divergence-theorem` (Part IV, right after `change-of-variables`) covers C¹ hypersurfaces as local graphs, surface measure, C¹ domains and the outward normal, the divergence theorem by partition of unity, Fubini and the FTC, Green's identities, and harmonic functions in ℝⁿ (mean value property, fundamental solution). Green's theorem on a rectangle and a disc moved there from `riemann-integral-rn` and keeps its label `thm-green`. Its users are `harmonic-functions` (Part V; the disc case stays self-contained there for the `complex-early` path), `distributions` (ΔΦ = δ), `poincare-rellich` (traces) and the capstone. No forms are used. An optional chapter on forms and Stokes is still open (roadmap A9).
13. **Abstract algebra is taught just in time.** Groups and characters appear with Fourier analysis on finite abelian groups (Part III), which is now an **optional** chapter (roadmap A7 / route R7: no main-line chapter after Part III needs it; its users, Dirichlet's theorem and Gelfand theory, are optional). Ideals and quotients appear with Gelfand theory, an optional chapter of Part VI. In the same trim, the Kirchhoff/descent/Huygens and Radon sections of `fourier-transform-rd` are optional.
14. **Cross-cutting skills are named and recur**, in Quick checks, warnings and C-exercises:
    - quantifier management;
    - ε allocation;
    - extracting subsequences, including the diagonal argument and weak compactness;
    - density arguments;
    - a checklist for exchanging limits;
    - approximation machinery;
    - Baire arguments;
    - duality arguments;
    - self-explanation;
    - proof verification (finding the error).
15. **Every chapter ends with exit checks.** These are C-level exercises taken from the "exit check" items in `curriculum.md`. Examples include proving that a continuous function on [a,b] is uniformly continuous in two different ways, and the capstone at the end of Part VI.
16. **Every Part ends with a Gate** (roadmap B2 / reader B2): the last section of the Part's last main-line chapter is a timed, closed-book exam with a marking scheme, a pass line and an `@ref` remediation map. Gate 0 is in `countable-and-uncountable` (ch. 8), Gate I in `forms-of-completeness` (ch. 21, replacing the Part I review), Gate II in `riemann-integral-rn` (ch. 33), Gate III in `riemann-limits` (ch. 42), Gate IV in `probability-measure-spaces` (ch. 54; its probability problems are non-core, so a reader who defers that chapter sits Gate IV after ch. 53), Gate V in `continuation-and-picard` (ch. 62) and Gate VI in the capstone (ch. 78). The UCLA-style qual checks that used to be exit checks of ch. 53 and ch. 62 are now inside Gates IV and V.
17. **ODE covers linear systems and the flow** (roadmap A4 / route R4). `linear-odes-flows` (Part II, after `inverse-implicit`) adds the matrix exponential, fundamental matrices and variation of constants, stability of x′ = Ax, C¹ dependence on initial data and the local flow, with a Sturm–Liouville preview that `compact-operators-spectral` answers. Jordan form is cited from the companion book.
18. **Probability is on the main line** (roadmap A3 / route R3). `probability-measure-spaces` closes Part IV: random variables and distributions, independence through product measure, Borel–Cantelli and the 0–1 law, the weak law and the L⁴ strong law, normal numbers, and the CLT by Lindeberg's replacement method (no Fourier). No later chapter depends on it, so on the two-year schedule it may be read after Part VI. Characteristic functions, weak convergence of measures, Lévy continuity and Prokhorov are an optional last section of `tempered-distributions-fourier`.
19. **Interpolation is the harmonic-analysis on-ramp** (roadmap A5 / route R5). Marcinkiewicz (diagonal case) is proved in `lebesgue-differentiation` and gives the maximal function's Lᵖ bound. The short main-line chapter `interpolation` (Part VI, after `tempered-distributions-fourier`) proves the three-lines lemma, Riesz–Thorin, Young's convolution inequality and Hausdorff–Young, and previews the Hilbert transform on L²; the capstone does not depend on it.
20. **Linear-algebra gates are published** (roadmap A8 / route R8), as `external_prerequisites` of the Part II and Part III openers and of the chapters concerned: the companion book through determinants and eigenvalues before `derivative-rn`; eigenvalues and Jordan form before `linear-odes-flows`; inner products, orthogonal projection, the spectral theorem and SVD before `mean-square-pointwise`; alternating multilinear forms before any forms chapter (A9).

## Reading paths (`config.json` `reading-paths`)
- *(Amended 2026-09-28, roadmap B6 and A10.)* The two-year and three-year routes are **schedules** on the "How to read this book" page (`authoring/READING.md`), not reading paths. On the two-year schedule **Parts IV and V run in sequence, not in parallel** (in parallel they would be about 32 hours a week).
- Narrower paths are defined in `READING.md`, among them `measure-only`, `complex-only` and `foundations`.
- **`complex-early`** (roadmap A6 / route R6): Parts 0 → I → II → V. Part V needs nothing from Parts III–IV beyond the Poisson/Abel link, and wherever it cites Part IV (Green's identities, now in `surfaces-divergence-theorem`) it keeps a self-contained disc-case fallback, so the path is valid.

## Source policy
- Original prose only. The converted reference books (`~/math-refs/analysis/converted/`) may be used to check truth and coverage and for nothing else.
- `blueprint/originality.py` flags shared n-grams against the source sections listed for each chapter.
- Converted text is never committed.

## Deferred on purpose
- Roadmap A9 (decide after Part IV is written): optional chapters on Hausdorff measure and on differential forms and Stokes; interior H² regularity in the capstone; Hilbert before Banach in Part VI; the bounded self-adjoint spectral theorem.
- The one-node-per-file YAML knowledge graph, `term:` links, natural-deduction rule tags on proof steps, and `uses_choice` / `nonconstructive` flags. For now the engine's `@ref` graph, `graph.json` and the reading paths stand in for them.
- The Chinese edition.
