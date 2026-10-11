# Curriculum specification, stage by stage (planning record)

This file condenses the planning research of 2026-09-27. For each stage it lists what the reader must know and be able to prove, with benchmarks drawn from:
- Cambridge Tripos schedules (lecture counts given in brackets);
- Oxford;
- Princeton (the Stein–Shakarchi sequence, MAT 215);
- MIT 18.102;
- ETH;
- the UCLA and Berkeley qualifying exams;
- NTU.

Chapter blueprints take their content from here. Parts are mapped to stages in `decisions.md`. The route changes of 2026-09-28 (`roadmap.md` A1–A8) moved some placements; the stage sections below state the current ones, and `blueprint/book.yaml` is authoritative.

Every stage has the same fields:
- **(a)** goal
- **(b)** definitions
- **(c)** theorems the reader must be able to prove unaided
- **(d)** examples and counterexamples
- **(e)** skills
- **(f)** motivating problems
- **(g)** exit checks
- **(h)** time
- **(i)** benchmark texts

---

## Stage 0 — Proof bridge and foundations (Part 0)

**(a) Goal.** The reader formalizes and correctly negates any statement with three nested quantifiers, and chooses the right proof skeleton: direct, contradiction, contrapositive, induction or cases.

**(b) Definitions.**
- Propositions and connectives; the conditional and its contrapositive; ∀ and ∃ and their negations.
- Set operations, power set, Cartesian product.
- Relations and equivalence classes.
- Functions: injective, surjective and bijective maps, images and preimages.
- Well-ordering, induction and strong induction.
- Countable and uncountable sets, comparison of cardinalities.

**(c) Prove unaided.**
- ℚ is countable.
- A countable union of countable sets is countable. Flag the use of choice here, without developing it.
- ℝ is uncountable, by the diagonal argument.
- Cantor: there is no surjection X → P(X).
- √2 is irrational.
- Preimages preserve union, intersection and complement; images preserve only union.

**(d) Examples.**
- f(A∩B) ⊊ f(A)∩f(B).
- ∀x∃y versus ∃y∀x, on x+y=0.
- An infinite set is equinumerous with a proper subset of itself.

**(e) Skills.** Quantifiers (formalize, negate, order); choosing a proof skeleton; contrapositive and contradiction; induction; diagonalization; self-explanation (mark each line with where it comes from); proof verification (find the error).

**(f) Motivation.** Are there more rationals or more reals? Why does 0.999… = 1 need a definition at all?

**(g) Exit checks.**
- Negate "f is uniformly continuous on A" and "fₙ → f uniformly".
- Judge four student proofs and locate the error in each (a Selden & Selden style task).
- Prove that a countable union of countable sets is countable.

**(h) Time.** About 12 Cambridge lectures, the logic, set, induction and countability part of Numbers and Sets.

**(i) Benchmark texts.** Velleman chapters 1–6 and 8; for the logic, Huth & Ryan chapters 1–2 (§1.1–1.5, §2.1–2.4).

### Natural deduction content (Part 0, logic chapters 1–5)

*(Amended 2026-09-28.)* The logic is five chapters, modelled on Huth & Ryan ch. 1–2: `connectives-and-derivations` (statements, the derivation format, the rules for ∧, →, ∨, one per section) and `negation-and-classical-logic` (¬, ⊥, derived rules MT, contrapositive, DS, ↔, RAA and classical logic, finding derivations) — the former `propositional-natural-deduction`, split 2026-09-28 — `semantics-soundness-completeness` (formulas as a formal language, parse trees, truth tables, ⊨ versus ⊢, structural induction, soundness and completeness proved in full, CNF/DNF), `predicate-logic` (terms, free and bound variables, substitution, the ∀/∃/= rules with side conditions, quantifier equivalences, models briefly, the worked example and the catalogue below) and `from-derivations-to-prose` (the rhetoric of each rule, levels of abbreviation, self-explanation, proof verification, and the excluded-middle dispute as its last section).

**Rules.**
- Introduction and elimination rules for ∧, →, ∨, ¬, ∀, ∃ and =, plus ⊥-elimination and RAA (classical).
- Each rule is set beside the phrase that carries it in mathematical writing and beside its Lean tactic:

| Rule | Lean tactic |
|---|---|
| ∧I, ∧E | `constructor`, `.1` |
| →I, →E | `intro`, `apply` / `exact h hp` |
| ∨I, ∨E | `left`/`right`, `rcases` |
| ¬I | `intro` … `False` |
| RAA | `by_contra` |
| ⊥E | `exfalso` |
| ∀I, ∀E | `intro x`, `h a` / `specialize` |
| ∃I, ∃E | `use`, `obtain ⟨x,hx⟩` |
| = | `rw`, `calc` |

**Side conditions.** The eigenvariable condition on ∀I, and the fresh-name condition on ∃E.

**Worked example.** "Uniformly continuous ⇒ continuous", annotated rule by rule. The converse fails because the witness δ would have to be chosen before x is introduced.

**"What is not allowed" catalogue.** Each common error is tied to the rule it breaks:
- verifying one instance and concluding ∀ breaks ∀I;
- a δ that depends on x, while claiming uniformity, breaks ∃I;
- treating the x from ∃E as arbitrary breaks ∃E;
- proving the converse reverses the direction of →I;
- a missing case breaks ∨E;
- circular reasoning cites what is not yet available;
- using an assumption after its box has closed breaks the scope of →I.

**The "strange" parts, made natural.**
- Vacuous truth follows from ⊥E.
- Truth tables summarize the rules; soundness and completeness are proved in full (Chapter 3).
- RAA needs LEM, whereas ¬I does not.
- The "if" of a definition means "iff".

**Chapter order.**
1. Connectives, taught by their rules.
2. Fitch boxes and scope.
3. Truth tables as a summary.
4. Quantifier rules.
5. Equality.
6. The "not allowed" catalogue.
7. Exercises: annotate an informal proof with its rules, and write fluent prose from a rule skeleton.
8. Final section: the dispute over excluded middle (see `decisions.md` item 3).

About half the exercises annotate or build real proofs from analysis.

### Number construction (Part 0, route beside the main line)
- **Set theory.** List the ZF axioms and use them to build ℕ, either as von Neumann ordinals or by assuming Peano. No metamathematics.
- **Choice.** Stated here and flagged where it is used later: countable unions, the Vitali set, Hahn–Banach, Tychonoff.
- **ℤ and ℚ.** Built as equivalence classes. Prove a few representative cases in full and leave the rest to exercises.
- **ℝ.** Built by Dedekind cuts, which give the least upper bound property directly.
- **Closing theorem.** A complete ordered field is unique up to isomorphism.

---

## Stage S1 — Analysis on ℝ (Part I)

**(a) Goal.** Fluency with ε-δ and ε-N; the equivalent forms of completeness and their consequences; the full Riemann theory.

**(b) Definitions.**
- The supremum axiom and the Archimedean property.
- Sequence limits and subsequences, limsup and liminf, Cauchy sequences.
- Series, absolute and conditional.
- Open, closed and compact sets (sequential and cover versions), limit points.
- Function limits, continuity, uniform continuity, the derivative.
- The Riemann (Darboux) integral.
- Pointwise and uniform convergence; power series and the radius of convergence.

**(c) Prove unaided.**
- Monotone convergence; Bolzano–Weierstrass; the Cauchy criterion; Heine–Borel in ℝ.
- The intermediate and extreme value theorems.
- A continuous function on a compact set is uniformly continuous (ℝ).
- Rolle, the mean value theorem, Taylor with Lagrange remainder.
- A continuous function is integrable; the fundamental theorem of calculus.
- A uniform limit of continuous functions is continuous; integration commutes with uniform limits; the Weierstrass M-test.
- The Riemann rearrangement theorem (outline).
- The theorem that the forms of completeness are equivalent. It is a separate node at the end of Part I, so as to avoid a cycle with the LUB axiom:
  - LUB ⇔ monotone convergence ⇔ BW ⇔ (Cauchy complete + Archimedean) ⇔ (nested intervals + Archimedean);
  - the Levi-Civita field and the hyperreals show that "Archimedean" cannot be dropped.

**(d) Examples.**
- The Cantor set, the Dirichlet function, the Thomae function.
- x² sin(1/x); xⁿ on [0,1].
- Rearrangements of the alternating harmonic series; Σ sin(nx)/n.

**(e) Skills.** ε allocation (ε/2, ε/3); extracting subsequences; sup approximation (aₙ > sup − 1/n); telescoping and comparison; the checklist for exchanging limits; from a cover to a finite subcover; refining partitions.

**(f) Motivation.** Why does the IVT fail over ℚ? When may a power series be differentiated term by term?

**(g) Exit checks.**
- Prove, without the book, that a continuous function on [a,b] is uniformly continuous, twice: once by BW and contradiction, once by the Lebesgue number.
- Show that the two definitions of limsup agree.
- A sequence of continuous functions converging pointwise to a non-integrable function: construct one or explain why none exists.

**(h) Time.** Cambridge Analysis I [24] plus the first 7 lectures of Analysis II.

**(i) Benchmark texts.** Abbott chapters 1–7, or Rudin PMA chapters 1–7.

### The least upper bound axiom node (first chapter of Part I)

**Type.** An axiom (`ax`) on the main line; a theorem on the Dedekind route.

**Definitions.** Kept as separate `def` nodes before the axiom:
- upper bound;
- sup and inf;
- maximum. sup A need not belong to A, and this is the key distinction.
- The conventions sup ∅ = −∞ and sup of an unbounded set = +∞. Mention them now; they are used only in measure theory.

**Results.**
- Uniqueness of sup.
- The **ε-characterization** (both directions), the most used tool in S1.
- inf A = −sup(−A).
- **Archimedes**, by contradiction via sup ℕ; corollary: 1/n < ε.
- **ℚ is dense**. The step that chooses an integer uses well-ordering.
- **√2 exists**: S = {x>0 : x²<2}, ruling out s²<2 and s²>2. This is the template for the IVT.
- **Nested intervals**, via the sup of the left endpoints.
- **Algebra of sup**: monotone under inclusion, sup(cA) = c sup A, and sup(A+B) = sup A + sup B, which needs both inequalities and the ε-characterization.

**Examples.**
- (0,1).
- {1−1/n}. Prove it with ε, not by intuition.
- Finite sets.
- The core counterexample: {x∈ℚ : x²<2} has no sup in ℚ.
- ℝ(x) with x infinite: ℕ is bounded there and has no sup, so Archimedes needs the axiom.

**Skills introduced.** Sup approximation; proving an equality by two inequalities; constructing a point as a sup. The last is used again in the IVT and Heine–Borel.

**Misconceptions to address.**
- sup = max.
- Every bounded set has a maximum.
- Forgetting "nonempty".
- Forgetting that the a chosen in the ε-characterization depends on ε.
- Proving one direction only.

**Exit checks.**
1. The ε-characterization, both directions.
2. sup(A+B), both directions.
3. The existence of √2, and the fact that it has no sup in ℚ.
4. Archimedes from the axiom, and where the proof fails in ℝ(x).
5. Verification: find the wrong line in a proof that silently assumes sup A ∈ A.

**Prerequisites.** Quantifiers; ordered-field axioms (their own node); sets and functions (−A, A+B); well-ordering.

**Successors.** limsup/liminf, monotone convergence, BW, IVT, Heine–Borel(ℝ).

**Long-range descendants, reached as a sup operation.** The Riemann integral (sup of lower sums), the sup norm on C(K), the operator norm, outer measure (an inf), and ess sup.

---

## Stage S2 — Metric spaces, function spaces, several variables (Part II)

**(a) Goal.** Lift convergence, completeness, compactness and continuity to metric spaces, and use C(K) to solve ODE and approximation problems.

**(b) Definitions.**
- Metric, open ball, closure, dense, separable.
- Complete, totally bounded; sequentially and cover compact.
- Connected and path-connected.
- Baire space, meager and comeager sets.
- Equicontinuity, Lipschitz maps, contractions.
- Norms and norm equivalence, the operator norm.
- The Fréchet derivative, C¹ and Cᵏ.

**(c) Prove unaided.**
- In a metric space, compact ⇔ sequentially compact ⇔ complete and totally bounded.
- A continuous function on a compact set is uniformly continuous (metric version). This is the gate for the second half of the stage.
- Baire; C(K) is complete.
- Arzelà–Ascoli.
- Stone–Weierstrass: Weierstrass first, by Bernstein or by convolution, then the lattice or algebra version.
- Banach's contraction mapping theorem; Picard–Lindelöf.
- All norms on a finite-dimensional space are equivalent.
- The chain rule; continuous partials ⇒ differentiable; the mean value inequality.
- The inverse function theorem, by contraction; the implicit function theorem; Lagrange multipliers.

**(d) Examples.**
- The L¹ norm on C[0,1] is incomplete.
- The unit ball of ℓ² is not compact (eₙ).
- The discrete metric; the topologist's sine curve.
- Weierstrass's nowhere-differentiable function; by Baire, the typical continuous function is nowhere differentiable.
- The ODE y' = y^{1/3} has non-unique solutions.
- xy/(x²+y²); the Peano curve.

**(e) Skills.** Diagonal extraction; density arguments; Baire arguments; fixed-point iteration with error bounds; the 3ε argument; transferring compactness through continuous images; passing from local to global by connectedness.

**(f) Motivation.** When does y' = f(t,y) have a unique solution? (contraction) Does Peano's existence theorem hold under continuity alone? (Arzelà–Ascoli) Are polynomials dense? (Stone–Weierstrass) Is a typical continuous function nowhere differentiable? (Baire)

**(g) Exit checks.**
- Nowhere-differentiable functions form a comeager set in C[0,1].
- Peano's theorem via Arzelà–Ascoli.
- The unit ball of ℓ² is not compact; compare with finite dimensions.
- Derive the implicit function theorem and compute a tangent plane.

**Additions.**
- ~~A 2-week module on topological spaces~~ *(moved 2026-09-28, roadmap A2)*: general topology is now a two-chapter block at the start of Part VI. Part II keeps metric topology only, plus the metric Urysohn function and the Tietze extension theorem for metric spaces (in the compactness chapter), which is all Part IV needs.
- Linear systems, the matrix exponential and the flow (roadmap A4), after the inverse function theorem: e^{tA}, variation of constants, stability, C¹ dependence on initial data, the flow's group property, and a Sturm–Liouville preview.
- A 1-week module on the Riemann integral on ℝⁿ: Jordan content, Fubini for continuous functions, linear change of variables. (Green's theorem moved to Part IV's surfaces chapter, roadmap A1.)
- The completion of a metric space, and ℝ as the completion of ℚ.

**(i) Benchmark texts.** Pugh chapters 2, 4, 5 (forms optional).

**Linear algebra II (companion book).** Inner products, the spectral theorem, SVD, the double dual.

**Linear-algebra gates (roadmap A8).** Determinants and eigenvalues before the derivative in ℝⁿ; eigenvalues and Jordan form before linear systems; inner products, the spectral theorem and SVD before Part III's mean-square chapter.

---

## Stage Summer 1 — Fourier analysis in the Riemann setting (Part III)

**(a) Goal.** The convergence and summability theory of Fourier series, and the Fourier transform on 𝒮(ℝᵈ). Collect, systematically, **the list of what the Riemann framework lacks**; this list motivates Part IV.

**(b) Definitions.**
- Fourier coefficients and partial sums.
- The Dirichlet, Fejér and Poisson kernels; good kernels and approximate identities.
- Cesàro and Abel summability; convolution.
- The Schwartz space and the Fourier transform.
- Characters of finite abelian groups (optional chapter, roadmap A7).

**(c) Prove unaided.**
- Uniqueness: a continuous function with all coefficients zero is zero.
- Fejér's theorem.
- Parseval for Riemann-integrable functions, including L² convergence.
- Riemann–Lebesgue.
- Pointwise convergence at a point where the function is locally Lipschitz.
- Inversion and Plancherel on 𝒮.
- Poisson summation.
- Weyl's equidistribution criterion.

**(d) Examples.**
- A continuous function whose Fourier series diverges at a point.
- The Gibbs phenomenon.
- ‖D_N‖₁ ~ log N.
- The heat and Poisson kernels.
- Lacunary series.

**(e) Skills.** Approximate identities; regularizing by convolution; summability in place of convergence; Parseval arguments; symmetry and characters. This is the first just-in-time use of groups, in the optional finite-group chapter (roadmap A7).

**(f) Motivation.** The heat and wave equations; the isoperimetric inequality (Hurwitz); equidistribution of {nγ}; optionally, Dirichlet's theorem. Kirchhoff's formula, descent and the Radon transform are optional sections (roadmap A7).

**(g) Exit checks.**
- Fejér's theorem, and hence that trigonometric polynomials are dense in C(𝕋).
- Explain why the Riemann-integrable functions are incomplete in the L² distance, and write the "what we need" list.
- The theta functional equation, by Poisson summation.

**(i) Benchmark texts.** Stein–Shakarchi I, chapters 1–6.

---

## Stage S3-A — Measure and integration (Part IV)

**(a) Goal.** Build the Lebesgue theory, starting from two problems: the Riemann space is incomplete, and limit exchange is too restricted. Complete differentiation on ℝⁿ.

**(b) Definitions.**
- Outer measure, Carathéodory measurability, σ-algebras, Borel sets, π-λ.
- Measure spaces, measurable and simple functions, the integral, almost everywhere, convergence in measure, Lᵖ.
- Product measure.
- Signed measures, total variation, absolute continuity, mutual singularity, the RN derivative.
- Lebesgue points, the Hardy–Littlewood maximal function.
- BV and AC functions.
- The distribution function, mollifiers, Lebesgue–Stieltjes measure.

**(c) Prove unaided.**
- **Lebesgue measure:** its construction and translation invariance; the Vitali non-measurable set.
- **Convergence theorems:** MCT, Fatou, DCT; Egorov; Lusin; Vitali convergence and uniform integrability.
- **Products:** Fubini–Tonelli, in full.
- **Lᵖ:** Hölder and Minkowski; Lᵖ complete (Riesz–Fischer); C_c dense in Lᵖ (p<∞); translation continuous in Lᵖ.
- **Differentiation:** the Vitali covering lemma, the weak (1,1) maximal inequality, Marcinkiewicz interpolation (diagonal case, roadmap A5), Lebesgue differentiation; BV functions are differentiable a.e.; the FTC for AC functions.
- **Surfaces (roadmap A1):** surface measure on C¹ hypersurfaces; the divergence theorem on bounded C¹ domains; Green's identities; the mean value property of harmonic functions in ℝⁿ.
- **Probability (roadmap A3):** independence via product measure; Borel–Cantelli; the weak law and the L⁴ strong law; the CLT by Lindeberg's replacement method.
- **Signed measures:** the Hahn and Jordan decompositions; Radon–Nikodym by von Neumann's L² proof; Lebesgue decomposition.
- **Change of variables:** linear, with the general C¹ case in outline.

**(d) Examples.**
- The Vitali set; the Cantor function; the fat Cantor set.
- The four modes-of-convergence sequences: the typewriter, n·1_(0,1/n), 1_[n,n+1], n^{-1/p}·1_[0,n].
- Fubini fails without σ-finiteness or integrability: counting × Lebesgue, and a double-series example.

**(e) Skills.** Three layers of approximation (simple, C_c, step); the good-sets principle and monotone class; truncation; choosing between MCT, DCT, Fatou and Vitali; covering lemmas; the maximal-function argument (prove it on a dense class, extend by the maximal inequality); Egorov and Lusin as trading ε of space for uniformity.

**(f) Motivation.** The completion of the Riemann space; the L² theory of Fourier series; when the integral of a derivative recovers the increment.

**(g) Exit checks.**
- Six UCLA real-analysis qual problems in 3 hours, at least 3 essentially complete.
- Lebesgue differentiation, from the covering lemma up.
- The implication diagram of the four modes of convergence, with a counterexample for every non-implication.

**Placement.** *(Amended 2026-09-28.)* No general topology in Part IV: Lusin and C_c density use the metric Urysohn and Tietze theorems of Part II (roadmap A2). Surfaces and the divergence theorem follow change of variables (A1); probability closes the Part and carries Gate IV (A3, reader B2). Lᵖ duality, Riesz–Markov and weak convergence move to Part VI.

**(i) Benchmark texts.** Folland chapters 1–3 and 6 (first half), or Stein–Shakarchi III chapters 1–3 and 6.

---

## Stage S3-B — Complex analysis (Part V)

**Placement.** On the two-year schedule Part V follows Part IV, not alongside it (roadmap A10). Part V is logically independent of Parts III–IV, so the `complex-early` path reads it straight after Part II (roadmap A6); where it cites Part IV's Green's identities it keeps a self-contained disc case.

**(b) Definitions.**
- Holomorphic functions and Cauchy–Riemann; contour integrals, winding numbers.
- Laurent series, the three kinds of isolated singularity, residues, meromorphic functions.
- Local uniform convergence, normal families.
- Conformal maps, Möbius maps.
- Harmonic and subharmonic functions, the Poisson kernel.
- Infinite products, the order of an entire function.
- Analytic continuation, monodromy.

**(c) Prove unaided.**
- **Cauchy theory:** Goursat; Cauchy's theorem and integral formula on a disc; Cauchy estimates, Liouville, the fundamental theorem of algebra; Morera; the identity theorem.
- **Local behaviour:** maximum modulus; the open mapping theorem; Casorati–Weierstrass.
- **Residues:** the residue theorem and real integrals; the argument principle, Rouché, Hurwitz.
- **Conformal maps:** the Schwarz lemma and automorphisms of the disc; Montel; the Riemann mapping theorem.
- **Products:** Weierstrass products; Hadamard (outline); Mittag-Leffler.
- **Harmonic functions:** the mean value property and maximum principle; the Poisson formula and the Dirichlet problem on the disc; Harnack; Schwarz reflection.
- **Picard:** little Picard, by Bloch/Landau or by the modular function.

**(d) Examples.** e^{1/z}; log and z^α; the natural boundary of Σz^{2ⁿ}; the plane is not conformally equivalent to the disc; annuli; Γ and ζ.

**(e) Skills.** Choosing and estimating contours (Jordan's lemma); local to global via the identity theorem; normal-family compactness (the complex spiral node of Arzelà–Ascoli); extremal problems; counting zeros.

**(g) Exit checks.**
- Six UCLA complex qual problems, 3 essentially complete.
- The Riemann mapping theorem, unaided.

**(i) Benchmark texts.** Stein–Shakarchi II chapters 1–3, 5 and 8, plus Ahlfors chapters 4, 5, 6 and 8 for the second layer.

---

## Stage S4 — Functional analysis, distributions, Sobolev, capstone (Part VI)

**(b) Definitions.**
- Topological spaces, bases, subspaces and products, Hausdorff and normal spaces, cover compactness, locally compact Hausdorff spaces, C_c and C_0 (the Part VI topology block, roadmap A2).
- Banach and Hilbert spaces, bounded operators, duals, sublinear functionals.
- Weak and weak* topologies, reflexive and separable spaces, orthonormal bases.
- Compact and Hilbert–Schmidt operators, adjoints, spectrum and resolvent, Fredholm operators.
- Locally convex spaces, for 𝒟 and 𝒮 only.
- Distributions and weak derivatives; Hˢ, W^{k,p}, H¹₀; traces.

**(c) Prove unaided.**
- **Duality and Baire:** Hahn–Banach, analytic and geometric (Zorn); the UBP; open mapping and closed graph; Lᵖ duality (1<p<∞, and p=1 when σ-finite); Riesz–Markov for C(K)* (outline allowed).
- **Topology:** compact subsets of Hausdorff spaces are closed; a continuous bijection from a compact space to a Hausdorff space is a homeomorphism; Urysohn and Tietze for normal spaces; the LCH Urysohn lemma and partitions of unity.
- **Weak compactness:** Tychonoff; Banach–Alaoglu (the separable case by a diagonal argument); Mazur.
- **Interpolation (roadmap A5):** the three-lines lemma, Riesz–Thorin, Young's convolution inequality, Hausdorff–Young.
- **Hilbert space:** projection and Riesz representation; Bessel, Parseval, Riesz–Fischer; Lax–Milgram.
- **Compact operators:** Fredholm alternative; the spectral theorem for compact self-adjoint operators.
- **Fourier and Sobolev:** Fourier on 𝒮′; Plancherel; Poincaré; Rellich–Kondrachov, on an interval or torus at least.

**(d) Examples.**
- The duals of c₀, ℓ¹ and ℓ^∞; c₀ is not reflexive.
- eₙ ⇀ 0 weakly but not strongly.
- L¹ is not a dual space.
- By the UBP, a continuous function with a divergent Fourier series exists.
- The right shift; the Volterra operator.
- δ and p.v. 1/x.
- H¹ embeds in C in dimension 1 but not in dimension 2 (log log).

**(e) Skills.** Duality (test against functionals); Baire; weak-compactness extraction; a priori estimates ⇒ existence; the BLT principle; compactness ⇒ discrete spectrum; differentiating distributions.

**(f) Motivation.** The Dirichlet principle made rigorous; integral equations u − Ku = f; eigenfunction expansions of a vibrating string.

**(g) Capstone.**
1. Lax–Milgram gives a unique weak solution in H¹₀(Ω).
2. Rellich and the compact self-adjoint spectral theorem show that the Dirichlet-Laplacian eigenfunctions form an orthonormal basis of L²(Ω).
3. A mixed qualifying exam.

**Optional.** Gelfand theory; ideals and quotients just in time. Characteristic functions, weak convergence of probability measures, Lévy continuity and Prokhorov (a section of the tempered-distributions chapter, roadmap A3). Quotient gluing (a section of the topology block).

**(i) Benchmark texts.** Brezis chapters 1–6 and 8–9, or Stein–Shakarchi IV chapters 1, 3, 4; Folland chapters 8–9 for distributions.

---

## Branches after Part VI (out of scope for now; entry nodes only)

| Branch | Entry nodes | First milestones |
|---|---|---|
| Harmonic analysis | maximal function, Lebesgue differentiation, weak Lᵖ, Plancherel, approximate identities, interpolation (Marcinkiewicz, Riesz–Thorin, Hausdorff–Young), the Hilbert transform on L² | Lᵖ bounds for the Hilbert transform, Calderón–Zygmund |
| PDE | Sobolev, Lax–Milgram, Rellich, distributions, harmonic functions, the divergence theorem and Green's identities, linear ODE flows (characteristics) | H² regularity, energy methods |
| Probability | abstract measure, RN, Fubini, the probability chapter of Part IV (LLN, Lindeberg CLT), characteristic functions (optional, Part VI) | conditional expectation, martingales, Brownian motion |
| Ergodic theory | measure-preserving maps, L² projection | von Neumann and Birkhoff |

---

## Spiral table (concept × stage)

| Concept | ℝ | ℝⁿ | metric / C(K) | normed / Banach | Hilbert | Lᵖ / weak* |
|---|---|---|---|---|---|---|
| compact | Heine–Borel, BW | closed and bounded | complete + totally bounded; Arzelà–Ascoli | unit ball compact iff finite-dimensional; compact operators | bounded ⇒ weakly convergent subsequence | Alaoglu; Kolmogorov–Riesz; Rellich |
| complete | forms of LUB; ℝ built from Cauchy sequences of rationals, Cauchy-complete + Archimedean ⇒ LUB (F3.10) | coordinatewise | C(K); Baire; contraction; completion of a metric space, ℝ as the completion of ℚ (AN2.2, returning to F3.10) | ℓᵖ; quotients; completion | Riesz–Fischer | Lᵖ complete; Riemann space incomplete |
| convergence | ε-N; pointwise vs uniform | norm equivalence | uniform = sup metric | norm vs weak | orthogonal expansions | a.e., in measure, Lᵖ, weak*, distributional |
| continuity | ε-δ, uniform | Fréchet | equicontinuity, Lipschitz | bounded = continuous; closed graph | adjoint | weak lower semicontinuity of the norm; translation |
| density | ℚ dense (in any Archimedean field, F3.9; in the constructed ℝ, F3.10) | polynomials | Stone–Weierstrass | Hahn–Banach criterion | orthonormal basis | C_c and mollifiers |

## Evidence from mathematics education (for STYLE and exercise design)
- **Concept image vs concept definition** (Tall & Vinner 1981). Every definition gets a counterexample that challenges the image it tends to create.
- **Quantifier order** (Dubinsky & Yiparaki 2000). Readers misread ∃∀ as ∀∃. Drill uniform continuity, uniform convergence and equicontinuity by swapping the quantifiers.
- **Strategic knowledge** (Weber 2001). Skills carry triggers, e.g. "bounded sequence → extract a subsequence".
- **Proof verification.** Selden & Selden 2003 and Inglis & Alcock 2012 show that students judge proofs poorly. Use find-the-error exercises, and check two columns separately: "true?" and "follows?" (Alcock & Weber 2005).
- **Self-explanation training** (Hodds, Alcock & Inglis 2014; d = 0.95). Add self-explanation prompts to key proofs.
