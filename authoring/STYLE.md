# Writing standard for the book

This file is for anyone who writes a section: me, or a drafting agent. Read all of it before you write. Also read `authoring/NOTATION.md` and the chapter's blueprint in `authoring/blueprints/`.

The method comes from the kwok-proof skill (`/home/akizumi/coding/kw/skill/kwok-proof/`). Read these parts of it before your first section:

- `SKILL.md`: the sections "How he thinks", "Typeset register" and "Board register".
- `references/explaining.md`: §1–§7, and the exemplar in §8 closest to your topic.
- `references/written-solutions.md`: §1–§3 and two exemplars.
- `references/ana.md`: all of §1 (heuristics H1–H28), §2–§3, and §5 (the spoken-vs-written gap: backwards Idea, forward Proof; constants placed first and justified last). This is the analysis reference; `la1.md`/`la2.md` only when a chapter leans on linear algebra.
- `references/problem-setting.md`: §1–§4, for the exercises.

**Hard rules**
- **Nobody is named.** The book never names, quotes or alludes to the lecturer the skill was distilled from. It uses his method silently. Never write "as X would say", course weeks or theorem numbers from his notes.
- **No copying.** The reference books (converted to Markdown under `~/coding/analysis/converted/`, listed in `blueprint/sources.yaml`) are copyrighted. You may use them to check which topics exist and whether a statement is true. Do not paraphrase their prose or copy their examples or exercises. Standard theorems are common property, but the explanation, the examples and the exercises must be our own. `blueprint/originality.py <chapter>` checks this; run it before handing a chapter back.
- **No forward references in proofs.** A proof may cite only results that appear **earlier** in the book: an earlier section, or earlier in the same section. The blueprint lists what each section may use. A forward pointer in the prose ("we will prove in Chapter 11 that …") is fine. It must never be a step in an argument.
- **Every claim is true.** Check every computation (with sympy, privately: the book text never mentions software, "sympy confirms" or how a result was verified; write a by-hand check the reader can follow instead), and state every hypothesis (non-empty, bounded, closed, compact, complete, σ-finite, 1 ≤ p < ∞, …). If you are unsure, compute it in a sidecar script (§9) or leave a `TODO(verify)` comment. Never guess.

---

## 1. The reader

The reader is a motivated student working **alone**. They have no lecture to fill gaps and no one to ask. Care for them:

- **Say why before what.** Explain what problem a definition or theorem solves before stating it.
- **Recall before use.** When an earlier result is used, recall it in a clause, name it, and link it with `@label`.
- **Warn early.** Name a known trap *before* the reader can fall into it, with a concrete failing case.
- **Let the reader check themselves.** Put a Quick check with a folded answer in every section.
- **Show every move.** Where a move is not visible ("why this basis?"), give one clause of reason. The written proof stays minimal and forward; the Idea block carries the discovery.
- **Stay calm.** No hype and no "clearly" or "obviously" hiding a step. "Trivially" is allowed only for something that really is one line and is then written out.
- **One new notion at a time.** Use at most two new **major** notions per section. Minor definitions (notation, auxiliary terms) may exceed this when they are introduced just before their first use; if a section carries more than two major notions, the blueprint splits it.
- **Taper the scaffolding.** The reader is taught to read and write proofs early and is then trusted to do it. §11 says what is dense in Parts 0–I and sparse afterwards.

## 2. Page skeleton

Each section is one Markdown file, `src/chNN-slug/MM-slug.md`, whose first line is `# Title`.

```markdown
# Title of the Section

Opening frame: 2–4 sentences. Where we are, what question is open, what this section
does. Plain prose, no heading.

## First subsection heading

...notion or theorem blocks...

## Exercises

### A. Check your understanding
### B. Practice
### C. Going deeper
### R. Review

<!-- dependency ledger
...one line per fact a proof uses without an @ref (§9)...
-->
```

Section titles (the `#` line) contain no math, since they appear in navigation links and page titles. Use `##` for subsections (they appear in the page's table of contents) and `###` only inside Exercises or for a long worked computation. Aim for **2,500–5,000 words of main-line prose**; prose inside second-reading folds (§12) is counted apart and does not use up the budget, though it is not free either (it is on the full track). Split a longer section at a natural seam. The `### R. Review` group appears only in the chapter's last section (§6), and the dependency ledger closes every section file (§9).

A chapter's `index.md` contains, in this order:
1. `# Chapter Title`.
2. A 1–2 paragraph story of the chapter: the question it answers and why the reader should care.
3. **What you need:** the earlier chapters or sections used, with links.
4. **Time:** one line, `**Time.** About N hours on the core track (all of A, one B and one C per section, the exit checks); about M hours for everything.` Until there are reader logs, N and M come from the formula in `authoring/design/research-reader.md` B1: about 15 minutes per 400 words of prose for reading, plus 20–45 minutes per exercise. **N counts main-line prose only; M adds the prose inside second-reading folds** (§12). `python3 tools/check_structure.py --words src/chNN-…` prints both word counts and their reading hours. Round to the nearest 5 hours. Replace them with the median of logged hours when there is one.
5. **Roadmap:** a bullet per section, with one sentence each.
6. **Named moves:** a short list of the proof techniques this chapter introduces, so the reader can transfer them.

The **last main-line chapter of each Part** also ends with a **Gate** section (§11.10). The Gate is a section like any other in the Roadmap, and it has no Exercises heading of its own: its problems are the section.

## 3. Introducing a notion (the explain template)

For each new definition, in order:

1. **Situate** (1–2 sentences). Where does it sit? Objects then maps, an object then its subobjects, or a question left open.
2. **Hook.** Choose **one**:
   - a naive notion that fails, shown failing;
   - a recurring expression that deserves a name;
   - the standard example, generalised;
   - a goal theorem stated first ("we want to prove …; we need a word for …");
   - an everyday word.
3. **Slogan.** One sentence in plain words, written in *italics* as its own paragraph.
4. **Definition.**
   - Every quantifier, and what it is defined on.
   - **Bold** the term defined and the small words that carry weight: **for every**, **there exists**, **strictly**, **a** vs **the**, **non-empty**, **eventually**, **uniformly**.
5. **Paraphrase** clause by clause ("In words: the first condition says …").
6. **Well-definedness**, if there is anything to check: independence of choices, existence, uniqueness.
7. **Examples**, 2–4 of them, simplest first.
   - Check each against the definition clause by clause.
   - Spread them across the families: sequences in ℝ, functions on intervals, ℝⁿ, sequence spaces (ℓᵖ), function spaces (C[a,b], Lᵖ), the discrete metric.
   - Include one degenerate case (the empty set, a singleton, a constant sequence, the zero function) and say why it matters. In an introductory volume the degenerate case may go into the second-reading fold instead (§12.3).
8. **Non-example by minimal change.** Change one example slightly, say what still works, and name the exact clause that fails. (fd1 and introductory volumes: into the fold, or into the section's one "Is this legal? Is it useful?" A item, §12.3.)
9. **Why this definition.** What breaks if a clause is dropped or a convention changed. Where the name comes from, if it helps.
10. **Warning** (`::: {.warning}`). The misconception, with a concrete failing case.
11. **Payoff.** The first small result, a link to an earlier concept, and one sentence on where this is going.

Not every notion needs every step at full size. A minor auxiliary definition may use steps 4, 7 and 8 only. **Major notions get all eleven.** These include: supremum, limit of a sequence, Cauchy sequence, series convergence, open/closed/compact set, continuity, uniform continuity, derivative, Riemann integral, uniform convergence, metric space, completeness, compactness, connectedness, equicontinuity, Fréchet derivative, topology, Fourier series, σ-algebra, measure, measurable function, Lebesgue integral, Lᵖ, holomorphic function, contour integral, residue, normed and Banach space, Hilbert space, dual space, weak convergence, compact operator, distribution, Sobolev space, and similar.

## 4. Theorems and proofs

For each theorem:

1. **Lead-in sentence.** Say what the result does or what need it fills ("It turns out that a continuous function cannot skip a value:").
2. **The statement**, complete and self-contained, with all hypotheses. Give it a short `[Name]` title when it has a standard name or will be cited later.
3. **Idea** (`::: {.idea}`, 2–6 lines, plain prose).
   - The reasoning found backwards, a picture described in words (or TikZ), a small case, or a numbered plan ① ② ③.
   - This is where "why do we do this?" is answered.
   - Omit it for proofs of 3 lines or fewer.
   - For at most two theorems per chapter, a *Try it first* prompt comes between the statement and the Idea, and the Idea then starts from what the attempt runs into (§11.8).
4. **Proof** (`::: {.proof}`), in the typeset register:
   - **First sentence does mathematics:** "Let …", "Suppose …", "Since …", "By @thm-x, …". Never motivation (that went in the Idea).
   - **Chain the steps** with Therefore / Hence / Thus / In particular / Then.
   - **Every step names its reason**: a hypothesis, a definition, or a cited result (`@label`, not restated). Where a display hides a reason, add "where the second equality uses …".
   - **Always justify:**
     - each clause of a definition being verified;
     - why a choice is possible (a sup exists because the set is non-empty and bounded above);
     - what each chosen constant depends on;
     - non-zero before dividing, positive before taking a square root or logarithm;
     - the theorem licensing every exchange of limits, sums, integrals and derivatives;
     - measurability and integrability before integrating (from Part IV on).
   - **You may skip:** a symmetric half ("swapping the roles of \( d_1 \) and \( d_2 \) gives the reverse inequality"), and a repeat of an argument just given.
   - **Labels:** `\( (\Rightarrow) \)`/`\( (\Leftarrow) \)`, `\( (\subseteq) \)`/`\( (\supseteq) \)`, *Case 1.*/*Case 2.*, and `::: {.claim}` with a nested `::: {.proof}` for a genuinely separate fact inside a long proof.
   - **Ending:** "This shows …" / "This proves …" / "as claimed".
   - **Length:** most proofs are 5–20 lines. For a long theorem (Heine–Borel, Arzelà–Ascoli, the inverse function theorem, Carathéodory, Lebesgue differentiation, Radon–Nikodym, the Riemann mapping theorem, Rellich), write a **Step roadmap** in the Idea, then `**Step 1.**` … inside the proof, with Claims.
   - **One proof per theorem.** A second route gets at most one short "Alternatively," paragraph, and only when it teaches something.
5. **Aftermath** (1–2 sentences). What is this result for? What does it let us do now? Use a `::: {.remark}` only if it needs a separate block, e.g. "the converse fails: …".

**Preferred proof routes.** These are the analysis heuristics of `references/ana.md` §1, in the book's words. Use whichever fits.

- **Givens and goal first (H1).** Unwind the goal into its definition; the definition tells you what to fix arbitrarily (a point, ε, a sequence, an open cover).
- **Backwards Idea, forward Proof (H17, G1–G2).** For ε–N and ε–δ, the Idea works backwards from the target inequality, bounding by "something a little bigger" when it cannot be solved. The Proof then places the constant first (`Let \( \delta \coloneqq \min\{1, \varepsilon/10\} \)`) and justifies it last. Never make the reader reverse-engineer where a constant came from.
- **Say what each chosen constant depends on.** "Choose \( N \) (depending on \( \varepsilon \))", "\( \delta \) depends on \( \varepsilon \) **and on \( x \)**". Quantifier order is the single commonest source of false proofs in analysis, and the page must make dependence visible (see §10).
- **Combine constraints with a max or min (H13),** and say that finiteness is what makes it legitimate.
- **Insert a third point (H14).** Use the triangle inequality through the limit, a subsequence term, or an approximant; the 3ε argument; telescoping plus a geometric series for Cauchy bounds.
- **Suppose not; negate quantifier by quantifier (H4, H23).** Write the negation as its own display line. Then specialise δ = 1/n to get a sequence.
- **Sup and inf (H24).** Split into "upper bound" and "least"; use "least" through "sup S − ε is not an upper bound", which hands you a witness.
- **Bounded sequence ⇒ Bolzano–Weierstrass (H19),** then closedness keeps the limit inside.
- **Compactness (H10).** To prove it, take an arbitrary cover or sequence. To use it, manufacture a cover from the data, keep finitely many, and exploit the finiteness.
- **Existence by completeness (H25).** Show the natural sequence is Cauchy and let completeness supply the limit. For "X is complete": find a candidate, upgrade the convergence, and check the limit is in the space.
- **Switch characterization (H12).** Use sequences for discontinuity, and preimages of open sets for inverses and regions.
- **Reduce to real numbers (H15),** by coordinates or by freezing a point.
- **Density.** Prove it on a dense class, then extend by a uniform or norm bound.
- **Exchange of limits.** Before swapping lim with lim, sum, ∫ or d/dx, name the theorem that licenses it (uniform convergence, M-test, MCT, DCT, Fubini–Tonelli) and check its hypotheses on the page.
- **Give each hypothesis a job (H6).** An unused hypothesis is where the finish comes from.
- **Refute with one concrete witness (H9).** The discrete metric, ℚ, (0,1), xⁿ, a shrinking interval, the typewriter sequence.

### Optional results

Some results are worth stating and proving and yet nobody is obliged to read them: an illustration of a definition just given, a remark that deserves a proof, a bridge showing how this corner of the book meets another. Keep writing them. Mark them:

```markdown
::: {#thm-adjoint-vs-dual .optional}
[The Adjoint Is the Dual Map Read Through Riesz]
```

`.optional` goes on the statement's div, beside its id. Both editions then print a marker on the title line — *Optional: nothing later depends on this.* — and the reader may skip the block, its Idea and its proof without wondering what they lost.

**What it buys.** The reading paths (`tools/reading_path.py`) treat an optional result's citations as context rather than prerequisites. Nothing requires the result, so nothing it cites can be required through it, and it puts no section on anybody's path. That is the point: `thm-adjoint-vs-dual`, a two-line verification that the adjoint is the dual map read through Riesz, put two sections of Chapter 6 and one of Chapter 1 onto seven of the ten reading paths. Marked optional, it puts nothing on any of them, and the label stays in the book.

**The invariant.** *Nothing anywhere may be proved from an optional result.* No proof, proof idea, claim or written solution may cite one — in the whole book, not just later in the section. `tools/check_optional.py` checks it and `./build.py check` fails on it, naming the citing sites:

```
ch12-spectral-theory/04: thm-spectral cites thm-aside in its proof,
but thm-aside is marked optional (ch11-inner-products/06)
```

When that fires, one of two things is true: the result is genuinely used, so drop `.optional`; or the citing argument can be written without it, so write it that way. Never both mark a result optional and lean on it — the marker is a promise printed on the page.

Prose, statements, remarks, warnings and quick checks may point at an optional result freely. That is how a connection is meant to be referred to.

**When to reach for it.** An illustration, or a connection between two parts of the book. Reach for it especially when a short result cites material from a chapter the surrounding section otherwise never needs; the marker is what lets the material stay without taxing the reader. Never use it on something a later proof needs, and never as a way to keep a result whose citations you would rather not justify. If in doubt, ask what breaks if the reader skips it: if the answer is anything but "a sentence elsewhere loses a pointer", it is not optional.

Run `python3 tools/check_optional.py --list` to see everything currently marked.

## 5. Examples, checks, warnings, remarks

- **Examples** `::: {#exm-slug}` with a `[Title]` first line. State the question inside the example. Put the worked answer in a following `::: {.solution}`; it starts folded on the web. Choose data so the computation is clean: explicit ε-thresholds that come out as integers, sums that telescope, functions whose integrals are elementary.
- **Quick check** `::: {.check}`: one short question. Its answer is a `::: {.solution}` placed **right after** the check block closes, never nested inside it. Put at least one per section **on the main line** (a check inside a second-reading fold does not count), placed right after the idea it tests; in fd1 and introductory volumes, about one per 800–1,000 words of main-line prose (§12.7). Good checks:
  - a non-example failing only clause k;
  - "why must this be strict?";
  - "is this look-alike an example?";
  - a tiny computation.
- **Warning** `::: {.warning}`: one misconception, a concrete failing case, 1–4 sentences.
- **Remark** `::: {.remark}`: 1–3 sentences with one job (converse fails, other names or notations, in other words, outlook).
- **Pictures:** TikZ inside `\begin{center}\begin{tikzpicture}…\end{tikzpicture}\end{center}` in a raw LaTeX block, or with the tikz syntax already used in `src/`. Use one idea per figure. Colour must never be the only carrier of meaning.
- **Interactive:** `::: {.plot fn= x= y= params=}` for functions with sliders, `{.python .run}` for small numpy/sympy experiments, and `::: {.widget src=}` with a `::: {.print}` fallback. Use them sparingly and only where exploring helps (partial sums of a series, uniform vs pointwise convergence of fₙ, Fejér means, a contraction's iterates). **They illustrate objects, never a proof's steps**: no animated or stepped-through proof, no narrated walkthrough (§11.11). A proof is read, not watched.
- **Meta-claims.** A sentence about the book's own text ("the classical step comes after the proof", "every other property fails in ℚ", "this proof never assumes n odd") is a mathematical claim and must be true of what is on the page. Write it so that a reader can check it by looking: point at the line, the table row or the label (§9).

## 6. Exercises

Each section ends with `## Exercises` and three groups, A, B and C. The **last section of a chapter** has a fourth group, R. The exercise formats of §11 (comprehension parts, find-the-error, proof ordering, faded proofs, example generation) live inside these groups; they are not groups of their own.

**A. Check your understanding.** Exactly one exercise with 2–6 lettered parts: define, state, decide true/false with a reason, negate a definition, name the method. Readers should be able to answer before moving on. (fd1 and introductory volumes: a rule section adds the drill bank of §12.8, and may add §12.3's "Is this legal? Is it useful?" item, as further A items.)
- In the section holding one of the chapter's two or three **key proofs**, at least one part is a **proof-comprehension** question about it (§11.2).
- A proof-ordering item (§11.4) may be the A exercise's last part or a B item.

**B. Practice.** 2–4 exercises "like the examples", each with a worked example type in the section:
- A "Determine which of the following … Justify your answer." batch with one or two planted failures.
- A computation (a limit, a sup, an explicit N or δ, an integral) ending in "Hence …".
- A routine proof applying one theorem once.
- **Example generation:** "Give an example of … such that …; check each property." Where the answer space is narrow, the solution lists the properties an answer must have, so a *different* correct example can be checked against them.

**C. Going deeper.** 1–4 exercises:
- a (a) Prove / (b) Deduce pair;
- a counterexample, construction or dropped-hypothesis item ("Is this still true on (0,1)?");
- optionally one harder problem, made reachable with scaffolded parts and a hint ladder.

The chapter's **exit checks** are C items titled `[C1: Exit check: …]`, and the chapter's find-the-error items (§10, §11.3) are usually C items.

**R. Review** (last section only; §11.5). 3–4 exercises labelled `-r1` … `-r4`, each short (at most 20 minutes): one reaching one chapter back, one 3–4 chapters back, one spiral item from an earlier Part, and optionally one that gives no hint of its method. The problem never names its source; the solution does, with `@ref`.

**Format.** Every exercise is `::: {#exr-<section-slug>-a1}` (then `-b1`, `-b2`, `-c1`, `-r1`, …) whose first line is a title `[A1]`, `[B2: Short name]`, `[R1]`, etc. It is followed by a `::: {.solution}` written in the typeset register (complete, not a sketch).

**Parts** use a lettered list:

```markdown
::: {.enumerate options="label=(\alph*)"}
1. ...
2. ...
:::
```

**Wording:** "Prove that", "Determine whether … Justify your answer.", "Give an example of …", "Explain why … is **not** …", "Hence deduce …".

**Hints.**
- An A or B item may carry **one** hint, at the end of the problem in italics: *Hint: consider the kernel of …*. It names a tool or an object, never a step.
- A C item may instead carry a **hint ladder** of two folded rungs, placed between the problem and the solution (§11.7): rung 1 names the tool or object; rung 2 gives the first line of the proof. Neither executes the key idea. Until the engine has a hint block, write each rung as a `::: {.solution}` whose first line is `[Hint 1]` or `[Hint 2]`, so it folds on the web.

**Marking schemes.** Every exit check, every Gate problem and any C item a reader is likely to write up in full ends its solution with a `**Marking scheme.**` paragraph (§11.6).

**Calibration:**
- B uses one theorem once.
- C combines two ideas, generalizes (ℝ → metric space → normed space), or drops a hypothesis and asks what survives.
- A harder C item uses three ingredients, one from an earlier chapter.
- An R item uses one method from its source chapter, applied to data it has not seen.
- A later exercise may cite an earlier one ("By @exr-span-b2 …"). A proof in the text never may (§9).

## 7. Prose

- **Voice.** "We" for the author and reader together; "you" sparingly, for direct advice. Median sentence 12–18 words. Paragraphs of 1–4 sentences. Vary rhythm; no walls of text.
- **Emphasis.** Bold is for defined terms and load-bearing small words, italics for slogans and light emphasis. No exclamation marks, and no "Note that" at the start of every other sentence.
- **Names.** Name results by content ("the Bolzano–Weierstrass Theorem"), with `@label`. Titles of named theorems match exactly so the dependency graph picks up mentions.
- **Promises.** Every forward promise ("we will see in @sec…" or "in Chapter 10") must be paid off. Forward pointers are budgeted (§12.1): no `@ref` to a result the reader has not met may serve as a reason, and an introductory volume allows one "Looking ahead" box per section. A drafter reports each promise it opens and each it pays (with the paying label); the coordinator enters them in `authoring/STATUS.md`, and `tools/promises.py` reconciles the table with the text. Never promise what you have not checked the target chapter's blueprint will deliver.
- **Spelling.** American spelling: "normalize", "color", "behavior", "center". Mathematical names keep their accents (Gershgorin, Schur, Cauchy–Schwarz with an en dash).
- **Math delimiters.** `\( … \)` inline and `\[ … \]` display, never `$` (except inside TikZ and inside `\tag{$\ast$}`). Numbered equations take `{#eq-slug}` **on the same line as the closing `\]`, with no space** (`\]{#eq-normal-equations}`), and are cited with `@eq-slug`; on its own line, or after a blank line, the label is just text.
- **Relation symbols are typeset, never plain characters.** Write `\( \Rightarrow \)`, `\( \subseteq \)`, `\( \in \)`, `\( \le \)`, not the unicode characters — including proof-direction tags `\( (\Rightarrow) \)` and chains such as `(a) \( \Rightarrow \) (b)`. (An arrow used rhetorically, as in "abstract space → write down a matrix", is ordinary prose and stays plain, as does an environment title such as `[The 2 × 2 puzzle]`.)
- **Vectors are plain.** Unlike the linear-algebra companion, points of ℝⁿ, of a metric space and of a function space are plain italic (x, y, f); bold is reserved for defined terms in prose. Matrices, when they appear (Jacobians, linear maps of ℝⁿ), are plain capitals (A, Df(a)).
- **Displays must fit the text column.** A formula wider than about 60 characters of ordinary math should be broken with `aligned`, `split` or `cases` inside `\[ … \]`, aligned at `=` or at a natural operator, rather than left to overflow.
- **Macros** are in `latex/macros.tex`; use those listed in `NOTATION.md`. Define nothing ad hoc. If a new macro is needed, add it to `macros.tex` and `NOTATION.md`.

## 8. Authoring syntax reference

```markdown
::: {#thm-bolzano-weierstrass}
[Bolzano–Weierstrass Theorem]

Every bounded sequence in \( \nR \) has a convergent subsequence.
:::

::: {.idea}
We want ...
:::

::: {.proof}
Let ...  This proves the theorem.
:::
```

- **Environment prefixes:** `thm`, `lem`, `cor`, `prp`, `ax` (shared counter; `ax` is Axiom, used for the least upper bound axiom); `def`; `exm`; `exr`; `cnj`. Small blocks with no label: `.proof`, `.solution`, `.remark`, `.claim`, `.idea`, `.warning`, `.check`, `.algorithm`.
- **Labels** are lowercase-hyphenated and describe content (`thm-bolzano-weierstrass`, not `thm-3`). They are global across the book and must be unique.
- **References:** `@thm-bolzano-weierstrass` renders as "Theorem 3.12" with a hover preview; `@eq-slug` works for equations.
- **References to the linear-algebra companion:** `@la:thm-spectral-real` renders as "Linear Algebra, Theorem 12.4", linked, with the preview; `[@la:thm-spectral-real]` renders as "[LA, Theorem 12.4]". See §10.
- **Optional results:** `::: {#thm-foo .optional}` marks a result nothing later depends on (§4). Nothing may be proved from one; `./build.py check` enforces it.
- **Second-reading fold:** `::: {.second-reading title="Why the order is loss-free"}` … `:::` folds material a first reading may skip (§12). Not `.optional`: what it proves may be cited. Math in the title is `$…$` (in an attribute a backslash is an escape). Folds do not nest and hold no heading.
- **Labeled lists:** `::: {.enumerate options="label=(O\arabic*)"}` wraps an ordered list.
- **Web-only content:** `::: {.content-visible when-format="html"}`.

## 9. Before handing a section back

Two things are written for the reviewers rather than the reader: the sidecar scripts and the dependency ledger. The meta-claim rule is here because referees found more errors in meta-claims than in proofs (`authoring/design/research-production.md` §3.1).

### Sidecar scripts

Every non-trivial computation and every chosen constant (N, δ, r, a bound, a numeric answer in an example or solution) is checked by a script `verify/chNN/<label>.py`, keyed by the label of the block that quotes the values (`fd3/verify/ch01/exm-geometric-tail.py`). The script **asserts** the values the text quotes, so that a changed number fails it. It is not a private CAS session that nobody can rerun. The book text never mentions it (hard rules, above): the page gives a by-hand check the reader can follow.

### The dependency ledger

Every section file ends with a **dependency ledger**: an HTML comment, which Pandoc passes through to the web page as an invisible comment and drops from the PDF, so the reader never sees it. It lists every fact a proof, idea, claim or solution in the section **uses without an `@ref`**: an arithmetic or order fact, a property of ℕ or ℤ, a fact from the linear-algebra companion, a standard identity, "by induction" before Chapter 5. For each it says where the fact comes from.

```markdown
<!-- dependency ledger
lem-integer-part (proof): every non-empty set of integers bounded above has a maximum | ch06 (promised; STATUS)
thm-archimedean (proof): n + 1 > n for n in N | ax-ordered-field (O1), recalled in prose
exr-archimedean-properties-c1 (solution): 2^n >= n + 1 | proved inline by induction; Ch 7 not yet available -> flagged
none: (write this line alone if the section uses nothing without an @ref)
-->
```

- **Format:** the first line is exactly `<!-- dependency ledger`; then one line per fact, `<label> (<kind>): <fact> | <source>`; the last line is `-->`. The kind is `proof`, `idea`, `claim`, `solution` or `example`. The source is an earlier label, `chNN (promised)` for a fact owed by an earlier chapter that is not yet written, `companion ch N` for linear algebra used without an `@la:` citation, or `inline` if the section proves it on the spot.
- **What it is for.** Referee B checks it against what each proof actually uses, and the seam referee checks that every `chNN (promised)` source is in STATUS's promise table. A fact whose source is a *later* chapter is a forward dependency: fix the proof, do not ledger it.
- **Keep it short and honest.** Standard facts about the ordered field ℝ after Chapter 11 need no line. Anything the reader could reasonably ask "where was that proved?" about does.

### Meta-claims

A **meta-claim** is a sentence about the book's own content: "the classical step comes after the proof", "everything else fails in ℚ", "this proof never assumes n odd", "we did not use completeness", "this is the only place choice is used". Each must be true of the page, and **checkable on the page**: name the line, the step, the table row or the label it is about, so that a reader (and Referee B) can look. If a meta-claim cannot be made checkable, cut it. Pilot referees found 3 false sentences of this kind and no false proofs.

### Checklist

- [ ] Every definition is preceded by its need. Major notions follow §3 in full.
- [ ] Every proof cites only earlier results, and every step names its reason. No proof, idea or claim rests on an exercise.
- [ ] Every example's arithmetic and every chosen constant (N, δ, r) has a sidecar script `verify/chNN/<label>.py` that asserts the quoted values.
- [ ] There is at least one Quick check (its solution a sibling block after it), one warning and one non-example. The exercises have A, B and C groups (and R in the chapter's last section), each exercise with a complete solution.
- [ ] Every B-type task has a worked example in the text.
- [ ] If the section holds a key proof, its A exercise has a proof-comprehension part (§11.2). Exit checks and write-up C items end their solutions with a marking scheme (§11.6).
- [ ] Every meta-claim points at something on the page and is true of it.
- [ ] The file ends with a dependency ledger in the format above (or its `none:` line).
- [ ] Every forward pointer in prose ("in Chapter N") is reported for STATUS's promise table, and every promise this section pays names the label that pays it.
- [ ] Notation matches `NOTATION.md`. No symbol is used before it is introduced, and none is reused with a new meaning.
- [ ] Labels are unique (grep `src/`), and every `@ref` target exists or is created in this chapter.
- [ ] Second-reading folds hold only what §12.0 allows; every folded proof's statement and one-sentence meaning are on the main line; the main line still teaches the section with every fold closed.
- [ ] Forward pointers within budget (§12.1): no `@ref` to an unseen result used as a reason; at most one "Looking ahead" box (introductory volumes).
- [ ] Anything marked `.optional` is genuinely skippable: no proof, idea, claim or solution anywhere cites it (`python3 tools/check_optional.py`).
- [ ] Every theorem's hypotheses are each used, and each major theorem has a remark or exercise showing what fails when one is dropped.
- [ ] Every chosen constant says what it depends on.
- [ ] Scaffolding matches the Part (§11.12): no Part 0 density of prompts after Part I.
- [ ] No copied text or examples from the references (`blueprint/originality.py`), and no attribution to any person.

## Hyphenation of "non-"

The book writes **non-negative**, **non-empty**, **non-zero**, **non-decreasing**, **non-increasing**, **non-measurable** and **non-Archimedean** with a hyphen, as the linear-algebra companion does. Labels and directory names are exempt: write `thm-nonempty-bounded-sup`, not `thm-non-empty-...`.

## 10. Analysis-specific rules

These come from the planning record (`authoring/design/decisions.md`, `curriculum.md`) and from the education research summarized there.

- **Quantifiers are shown, not hidden.** A definition with nested quantifiers is also given in symbols (∀ε > 0 ∃N ∈ ℕ ∀n ≥ N …) after its prose form. When a uniform notion first appears (uniform continuity, uniform convergence, equicontinuity), a Quick check asks the reader to swap two quantifiers and say what changes.
- **A counterexample for every hypothesis that matters.** Each major theorem is followed by a remark, warning or exercise showing what fails when one hypothesis is dropped, with a named witness. The four modes of convergence, compact versus closed-and-bounded, and Riemann versus Lebesgue all get their own tables of witnesses.
- **The spiral is written out.** When a concept returns at a higher stage (compactness on ℝ, then in a metric space, then weakly), the opening frame of the section recalls the earlier version with `@label` and says in one sentence what changes and what survives. The spiral table in `curriculum.md` lists the returns.
- **Motivating problems come first.** Each chapter's `index.md` names the concrete problem that forces the chapter's main abstraction. A section never introduces a notion without saying what problem it answers (§3, step 2).
- **Proof verification is practised.** At least one exercise per chapter (usually a C item) gives a flawed proof and asks for the exact line that fails and the reason; at least one such argument per chapter has a **true** conclusion (§11.3). In Part 0 the reason names the natural-deduction rule broken; after Part 0 it names the missing hypothesis or the illegal step.
- **Self-explanation prompts.** For the three or four hardest proofs of a chapter, the Idea ends with a prompt such as "*Before reading on: where will compactness be used?*" or "*Self-explain lines 3–5.*" (at most one per proof). From Chapter 6 on they remind the reader of a trained habit (§11.1).
- **Part 0's rule tags.** In Part 0 only, proofs may annotate steps with the natural-deduction rule in small caps in brackets (e.g. `[∀I]`, `[∃E]`). Later Parts do not, but the "what is not allowed" catalogue of Part 0 is cited (`@...`) when a warning concerns one of its errors.
- **Choice and non-constructive steps are flagged in prose.** Where a proof uses the axiom of choice (countable unions, Vitali, Hahn–Banach, Tychonoff) or a genuinely non-constructive step discussed in the excluded-middle section, one clause says so. Do not dwell on it.
- **The companion book.** Linear algebra is never re-proved. It is cited with `@la:<label>`, the label as it stands in the linear-algebra book (e.g. `@la:thm-spectral-real`; the registry is `../linear-algebra/_build/crossref_labels.json`): in running text `@la:…` prints "Linear Algebra, Theorem 12.4" and links to it with a preview; in brackets, `[@la:…]` prints the short form "[LA, Theorem 12.4]". The config's `external-books` sets this up, and `./build.py check` fails on a label the companion does not have. An `@la:` citation is not a dependency inside this book: it never counts as forward and is not ledgered. When the companion is not built on the machine, the build prints "Linear Algebra, <label>" and check only warns; build it (`./build.py html` in `../linear-algebra`) before checking numbers. For a whole chapter with no single result to point at, the prose form "the linear-algebra companion, Chapter N" is still right.

## 11. The reader working alone

The reader of §1 has no teacher, no marker and no classmates. The rules below give them what a course would: training in how to read a proof, feedback they can apply to themselves, review spaced over months, and a checkpoint at the end of each Part. Most rest on controlled studies; the evidence and the sources are in `authoring/design/research-reader.md` (B2–B4, B7). Where a rule sets a count ("at most two per chapter"), the count is binding; the blueprint says where the items go.

**11.1 Self-explanation is taught once.** The book has exactly one training passage on self-explanation, in Chapter 5, `from-derivations-to-prose` (the self-explanation section; the blueprint names it). It takes one short proof and shows it explained twice:
- **well:** each line justified by earlier lines, definitions and named results ("line 4 follows from lines 2 and 3 by @def-…; this is where x > 0 is needed");
- **badly:** each line paraphrased ("so now we know the thing is small").

It then says why the first helps and the second does not. Write it as our own passage; take the method from the research, never its example. Every later "*Before reading on*" prompt (§10) assumes this training and may simply say "*Self-explain lines 3–5.*" Do not re-teach it elsewhere.

**11.2 Key proofs get comprehension questions.** For the two or three key proofs of a chapter (the blueprint names them), the A exercise of the section holding each proof includes at least one proof-comprehension part:
- why line k (or the displayed step) follows;
- where hypothesis H is used;
- the proof's idea in two sentences;
- the proof run on a given example (a specific set, sequence or function);
- which step fails if H is dropped.

Every part has a short answer the reader can check against the folded solution. No part asks for an opinion.

**11.3 Find the error, with a true conclusion.** The find-the-error exercise of §10 keeps two questions apart: *is the conclusion true?* and *does the argument prove it?* At least one flawed argument per chapter has a **true** conclusion; that is the case readers miss. Aim for two such items per chapter in Parts 0 and I, then one. The solution names:
- the exact line that fails;
- the rule broken (Part 0) or the hypothesis missing or the illegal step (later);
- a counterexample **to the illegal step**, not just to the conclusion (for a true conclusion there is none to the conclusion);
- where the error is one of Part 0's catalogued errors, the `@ref` to it.

The flawed argument is written to be plausible: the error sits in one line, and the rest is correct.

**11.4 Proof ordering and faded proofs, tapering.**
- **Proof ordering.** Give 6–10 lines of a proof, shuffled and numbered (i), (ii), …, plus one or two **distractors**: a line with the quantifiers in the wrong order, an ε of the wrong kind, a constant that depends on the wrong thing. The reader writes an order. The folded solution gives an admissible order, says which other orders are also admissible (any order respecting what each line uses), and says why each distractor fails.
- **Faded proofs.** The chapter's main named move appears three times: worked in full; with the last step blank; with the last half blank. Each blank carries the prompt "*Name the move, then complete it.*" The three may be spread across the chapter (an example, then a B item, then a C item). Good moves to fade: ε/2, "construct a point as a sup", the 3ε argument, the diagonal argument, density plus a uniform bound.
- **Taper.** In Parts 0 and I every chapter has one proof-ordering item and one faded triple. From Part II on, use them only where a genuinely new named move appears. Readers who have the skill are slowed by the scaffold (the expertise-reversal effect).

**11.5 The R. Review group.** The last section of each chapter has a fourth exercise group, `### R. Review`, with 3–4 items labelled `-r1` …:
- **R1:** one item whose method comes from the previous chapter;
- **R2:** one from 3–4 chapters back;
- **R3:** one spiral item from an earlier Part, taken from the spiral table in `curriculum.md` ("you proved X on ℝ; prove it in a metric space", or "say what now fails");
- **R4 (optional):** one item that gives no hint of its method. Its solution names the tool and says why the look-alike tools fail.

Rules:
- The problem text **never names its source chapter**; the solution does, with `@ref`.
- **Chapters that end in a Gate.** The R group sits in the last section that has an exercise set, just before the Gate section.
- **Early chapters.** Where the book has too few earlier chapters (Chapter 1 has none; Chapters 3–5 have no earlier Part), R items reach back as far as the book allows, within the chapter if need be, spaced as far apart as possible.
- Each item takes at most 20 minutes.
- Prefer results that later chapters rarely cite in proofs: a heavily cited result is reviewed for free, a dormant one is forgotten.

**11.6 Marking schemes.** Every exit check, every Gate problem, and any C item a reader is likely to write up in full ends its solution with a paragraph:

```markdown
**Marking scheme.** (10 points)
- 2: fixes \( \varepsilon > 0 \) arbitrary and states the goal \( \abs{f(x) - f(y)} < \varepsilon \).
- 3: chooses \( \delta \) from compactness, **uniformly in \( x \)**, and says so.
- 3: verifies the inequality, citing the triangle inequality.
- 2: concludes with the quantifiers in the right order.
Fatal errors (0 for the step): \( \delta \) depends on \( x \); compactness used for an open set.
```

- 3–6 key steps, with points summing to 10, then the named **fatal errors**.
- Write it so that another person, or a program, could grade a **different** correct proof fairly. Award the step, not the wording: "shows the sequence is Cauchy", not "writes the displayed inequality".
- The scheme follows the book's solution but must not require its route. If there is a second natural route, add one line saying how its steps map to the points.

**11.7 The hint ladder.** A C item may have two folded hints between the problem and its solution (markup in §6):
1. the tool or the object ("*Consider the set of points where f > c.*");
2. the first line of the proof ("*Let s = sup{…}; it exists because …*").

Neither gives the execution of the key idea. The failure the ladder prevents is opening the full solution too early. A or B items keep a single italic hint, or none.

**11.8 Try it first.** At most two theorems per chapter are preceded, between the statement and the Idea, by an italic paragraph naming what to attempt and for how long:

```markdown
*Try it first (ten minutes): which point would you build, and from which set?*
```

The Idea that follows **starts from the obstacles such an attempt meets** ("the obvious candidate is …; it fails because …"). Choose theorems where a reader can get somewhere in ten minutes; an unanswerable prompt costs a lone reader more than a student in class.

**11.9 The chapter's time line.** Every chapter `index.md` has the **Time** line of §2, after **What you need**. The core track is all of A, one B and one C per section, the exit checks, and the main-line prose; the full track is everything, including the prose inside second-reading folds (§12). The estimate is a promise to the reader about their week, so round honestly and do not shade it down.

**11.10 Gates.** The last main-line chapter of each Part ends with a **Gate** section: in the 78-chapter numbering, Chapters 8, 21 (its §06 review becomes the Gate), 33, 42, 54, 62 and 78 (§08, the mixed qualifying exam). Renumbering may move these; the Gate follows the Part's last main-line chapter. A Gate section contains, in order:
1. **Instructions:** time allowed (2 hours for Gate 0, 3 hours after), closed book, and the pass line: 70% overall, with no *core* problem at 0.
2. **Definition drill:** every major definition of the Part, to be stated in symbols, answers folded. This is the Part's one retrieval list.
3. **The problems** (6 for Gate 0 and Gate III, 8 otherwise), each `::: {#exr-<section-slug>-p1}` titled `[P1]`, or `[P1: core]` for a core problem, followed by a folded solution ending in a marking scheme (§11.6).
4. **Remediation map:** for each problem, the sections it tests, as `@ref`s, so a failed item sends the reader to named sections, not "reread Part II".

Gate problems are original. They may take the style and level of a qualifying exam (the floor of a good one for Gate I, real- and complex-analysis exams for Gates IV and V), never their text. A reader arriving by a reading path takes the Gate of the Part before their target as an entry test; the Gate's opening frame says so.

**11.11 No narration in proofs.** Interactive elements illustrate objects: a sequence of functions, a kernel, the iterates of a contraction. They never step through, animate or narrate a proof, and there is no "watch the proof" alternative to reading it. A proof is read, not watched.

**11.12 Taper the scaffolding.** Scaffolding decreases through the book:
- **Part 0** annotates rules on proof lines, orders lines for the reader, and prompts often.
- **Part I** keeps the formats of §11.2–§11.5 at full density but annotates less.
- **Parts II–III** keep the comprehension items, find-the-error, R groups and marking schemes, and use ordering and fading only for new moves.
- **Parts IV–VI** expect the reader to supply routine ε-management, measurability checks and "take a subsequence" without comment; prompts are for the genuinely new step.

Do not carry Part 0's density of prompts into Part IV. A reader who is told everything twice learns to skim.

## 12. The main line, the second reading, and the entry volumes

A section has two readers: the one meeting the material for the first time, who needs the shortest path through it, and the one coming back to see why it all holds. This section says how to serve both on the same page. Rules marked **(fd1 and introductory volumes)** apply to *Logic and Proof* and to any volume a reader may open first; the others apply everywhere. They come from the fd1 revision plan (novice-reader reports, and a comparison with the standard logic texts for technique only: no text, example or exercise is taken from any of them).

### 12.0 The second-reading fold

```markdown
::: {.second-reading title="Why the order of the premises is loss-free"}
Material a first reading may skip.
:::
```

On the website the fold is closed, with a marker and its title ("Second reading" if it has none); in the PDF it is printed in place between two light rules under the same head. Everything inside behaves as it would outside: theorems, proofs and derivations are numbered, labelled, cited and searchable, and a link to a label inside a closed fold opens it.

**What goes in.**
- A **meta-proof** whose statement stays on the main line (§12.12).
- **Edge cases**: the degenerate case, the non-example by minimal change, the "silly but legal" step (§12.3).
- **Long justifications**: "why the order is loss-free", "convenience, not power", "why a step may act on a part buried inside".
- **Instructor notes**: comparisons with other calculi, remarks on conventions, history.

**What never goes in.** A statement a later proof cites; the definition of anything used on the main line; the only Quick check or the only warning of the section (`tools/check_structure.py` counts main-line ones only); a heading (a fold sits inside a section: use a bold lead-in); another fold (folds do not nest). The build and `check_structure.py` both refuse the last two.

**It is not `.optional`.** An optional result (§4) promises that *nothing* depends on it; a fold promises only that a *first reading* may skip it. A result proved in a fold may be cited by any later proof, and `check_optional.py` and `check_forward_deps.py` read fold content as main line. Use `.optional` for what nobody needs, a fold for what everybody needs proved but not everybody needs to read now. The two may combine: an optional result inside a fold.

**The test.** Read the section with every fold closed. It must still teach the section: every rule usable, every main-line statement understood, every A and B exercise doable. If a fold must be open for that, its content belongs on the main line.

**How Time counts it.** The core track's reading time counts main-line prose only; the full track adds the folded prose (§2, §11.9). The section budget of 2,500–5,000 words is the main line's; folded prose is reported beside it, and the blueprint gives it a budget too, so that folding is not a way to grow the section.

### 12.1 The forward-reference budget

- A result the reader has not met is never a **reason**. No `@ref` to an unseen theorem in a proof, an idea, a claim or a justification; a heuristic is justified by a plain counterexample on the page, not by a theorem proved later. (This sharpens the hard rule on forward references: prose that *argues* from a later result is a forward dependency even outside a proof.)
- **(fd1 and introductory volumes)** At most **one** forward pointer per section, in a small box at the end of the main line, before the Exercises:

  ```markdown
  ::: {.remark}
  [Looking ahead]

  Chapter 3 checks that no rule leads from truth to falsehood.
  :::
  ```

  It names the chapter in words, never with `@ref`, and is reported to STATUS's promise table like any other promise. In fd1, soundness is promised once, in Section 1.2, and is not used as a reason anywhere before Chapter 3; one global note in Chapter 2's `index.md` ("steps about every and some are used as ordinary reasoning until Chapter 4") replaces per-proof caveats.

### 12.2 Effort in proportion to difficulty

A rule or definition with nothing hidden in it gets a short treatment; one with conditions that bite gets the full one. **(fd1 and introductory volumes)** The trivial rules (∧I, ∧E, ∨I, ∀E, ∃I, =I) get three bullets each: the schema, one line of reading, one example. The full clause-by-clause reading is kept for →I, ∨E, ¬I, RAA, ∀I and ∃E, and each of those opens with "This rule has conditions that matter; read each one." Elsewhere the same principle is §3's: a minor notion uses steps 4, 7 and 8, a major one all eleven.

### 12.3 Edge cases

Degenerate cases, minimal-change non-examples and "legal but useless" steps go into the second-reading fold, or into **one** A item per section titled `[A2: Is this legal? Is it useful?]` (fd1 and introductory volumes). Two exceptions stay on the main line in fd1 because later work uses them: the one-line box deriving ⊢ P → P, and P ∨ P ⊢ P. In other volumes, §3 step 7's degenerate case stays on the main line when it is the first place the reader meets it, and may be folded on its later returns.

### 12.4 Partial derivations (fd1 and introductory volumes)

Every worked derivation in a volume's rule sections (fd1: Chapters 1–2 and Sections 4.4–4.6) is shown growing, in two or three snapshots before the finished one: the goal at the bottom, the gap marked with a `\vdots` row, the available lines at the top, and **line numbers as they will be at the end**. Snapshots use the ordinary `nd` environment: a gap row is `\have[\ ][0]{}{\vdots}`, and the next row jumps the count to its final number with `\have[][7]{7}{…}` (`tools/check_fitch.py` accepts a forward jump only across a gap row). The finished derivation follows the last snapshot.

### 12.5 The Givens / Goal table (fd1 and introductory volumes)

Scratch work is drawn as a two-column table, introduced where the two directions of reasoning are (fd1: Section 1.2) and reused wherever a proof is planned (fd1: 3.1, 4.4–4.6, and step 1 of 5.5's procedure):

```markdown
| Givens | Goal |
|---|---|
| \( P \to Q \), \( Q \to R \) | \( P \to R \) |
| \( P \to Q \), \( Q \to R \), \( P \) | \( R \) |
```

Each row is one move, and each rule is a change to the table: →I moves the hypothesis into the Givens, ∀I adds a fresh name, ∃E adds a witness. A rule section says, in one line, what its rule does to the table.

### 12.6 The rule card (fd1 and introductory volumes)

Every rule section ends its main line with a **rule card**: a small table of the rules so far, each with a one-line picture (premises ⟹ conclusion) and its everyday phrase ("so", "suppose … then", "in either case"). The card grows section by section; the cumulative card is a one-page reference at the end of a run of rule sections (fd1: after 1.6, 3.1 and 5.6 (the quantifier card)), and the goal/premise decision chart grows with it.

### 12.7 Quick-check density (fd1 and introductory volumes)

About one Quick check per 800–1,000 words of main-line prose, most of them cheap: "Is this line legal? Which rule? Which lines does it cite?". The rule of §5 (at least one per section, its solution a sibling after it) still holds everywhere.

### 12.8 Drills and scaffolded items (fd1 and introductory volumes)

- **Drill bank.** Each rule section has, under A, a second item `[A2: Drill]` (or A3 when A2 is §12.3's item) of short parts in a ramp from recognition to construction: **15 parts in fd1 Chapters 1 and 2, 12 elsewhere** (the author's choice of the heavier workload, 2026-10-12; a chapter blueprint may not go below it). The ramp runs, in this order: one-step parts ("write the line this rule gives from these lines"), then a missing premise ("which line must be above for this step?"), then filling the justification column of a given derivation, then "is this application correct? If not, which clause does it break?", then 2–8-line derivations. Every part has its answer in the folded solution. For Time, the bank counts by B1's formula as one exercise per four parts, since each part is a one-line task.
- **Scaffolded B items.** At least one B item per rule section gives the premises and the last line, with the gaps marked `\vdots`, and asks "*Name the move, then complete it.*" (fd1's 1.5 B2 and 1.6 C4 are the model).
- **Challenge items.** A C item that is a meta-proof or needs mathematics beyond the section is titled `[C3: Challenge: …]` and is not on the core track; the core track's "one C per section" is a non-challenge C.

### 12.9 School-level examples first (fd1 and introductory volumes)

A logical point is first carried by an example from school mathematics (parity, divisibility, inequalities between numbers, a small finite set); the analysis example (the extreme value theorem, differentiability, ε–δ, uniform continuity) follows as the payoff, never as the first or only example.

### 12.10 Notation (fd1 and introductory volumes)

- ⊢ is introduced once, right after the reader has seen a derivation (fd1: Section 1.2). Γ is read "capital gamma" and explained as a list of statements.
- Schema letters are separated from statements once, with one sentence and an analogy: φ, ψ are holes in a pattern, like *a* and *b* in (a + b)² = a² + 2ab + b²; P, Q are statements. Each Greek letter is introduced once.
- In fd1 Chapter 1 nested → is always written with its parentheses; the right-association convention is a one-line remark (NOTATION.md keeps it).
- A substitution of a compound term parenthesizes the term, \( \varphi[(y+1)/x] \), rather than switching notation; no notation is swept across volumes.
- "≤ and ≥ are written out as disjunctions in a derivation whenever a rule (∨I, ∨E) has to see the disjunction; otherwise \( a \le b \) may stand as one statement" is stated once, in a box (fd1: Section 1.5), and reused after.

### 12.11 Citation order of ∧I

∧I cites its two lines in **either order**; the written line decides which conjunct is which (NOTATION.md, "Citing lines"; `tools/check_fitch.py` checks it so). The text never teaches a fixed order for ∧I or makes an exercise of it. →E keeps its convention, implication first and antecedent second, because every →E line then reads the same way; that is a writing convention, not a rule the reader can break.

### 12.12 Meta-proofs

A meta-proof (soundness of a rule, closure under substitution, copying a derivation, unique readability, structural recursion) goes into the second-reading fold. The **statement and a one-sentence meaning** stay on the main line, so the result can be cited and understood without the proof:

```markdown
::: {#lem-more-premises}
[More Premises]

If \( \Gamma \vdash \varphi \) and every formula of \( \Gamma \) is in \( \Delta \), then \( \Delta \vdash \varphi \).
:::

*In words: more premises never hurt.*

::: {.second-reading title="The proof: copy the derivation"}
::: {.proof}
…
:::
:::
```

A fold moves a proof; it never changes it. A proof that later volumes cite keeps its content verbatim when it is folded, and a changed proof goes back through S2a.

### 12.13 The deepening devices (fd1; other introductory volumes may adopt them)

Six devices of the fd1 deepening plan (2026-10-12). Each rule section of fd1 (Chapters 1 and 2, and the rule sections of Chapter 4) has all six where they apply; other fd1 sections use the ones that fit.

**1. Purpose-annotated assumptions.** Every assumption that opens a box says what it is for, in the justification column: "asm, for →I", "asm, for ¬I", "asm, for RAA", "asm, for ∨E", "asm, for ∃E". The engine prints it, read off the rule that closes the box, when the book config says `"fitch-purposes": "infer"`; a drafter writes nothing. Write it by hand, `\hypo {3} {P} \purpose{\ii}`, only where no line closes the box yet: a snapshot of a growing derivation (§12.4), a schema, a partial derivation in an exercise. `tools/check_fitch.py` checks every stated purpose against the rule that closes the box, and `--purposes` lists them all. Prose reads the annotation as the step it names ("suppose, for contradiction" is "asm, for RAA"), so the dictionary row of the prose chapter is a reading of a line the reader has seen since Section 1.4. A ∀I box has no assumption; its flag \( x_0 \) beside the bar says what the box is for.

**2. The rule-instance gallery.** Beside the rule card of every rule section, an example titled `[Instances of →E]` (`exm-<section-slug>-instances`) shows **three instances with large compound substitutions** and **one tempting look-alike that is not an instance**, with the reason:

```markdown
::: {#exm-proving-an-implication-instances}
[Instances of →I]

| φ | ψ | the instance |
|---|---|---|
| \( P \wedge \neg Q \) | \( (R \vee P) \to Q \) | … |

**Not an instance.** … : the box assumed \( Q \), not \( P \wedge \neg Q \), so the line it gives is \( Q \to … \).
:::
```

Each substitution is a compound formula (in Chapter 4, compound terms such as \( f(f(c)) \) and \( \varepsilon/2 \)), never a single letter, so the reader sees the schema match a shape and not a letter. The look-alike is the error a reader will actually make with this rule.

**3. The "Not allowed" block.** Each rule card is followed by a warning titled `[Not allowed: →I]` listing three to five one-line wrong steps, each tagged with the clause of the rule it breaks ("cites a box that is still open: clause (ii)"). Where a side condition bites (→I's discharge, ∀I's flag, ∃E's fresh witness, ∨E's two boxes), one wrong step is shown as a derivation **beside** the right one, WRONG on the left (marked `% expect-invalid` before its `\begin{nd}`), RIGHT on the right, in one raw block separated by `\qquad`. A wrong step that is an entry of the frozen catalogue `exm-not-allowed-catalogue` cites it by number ("(N3)"); the catalogue keeps its numbering, wording and instances.

**4. Derive-or-break items.** From Section 1.5 on, at least one B item per rule section is titled `[Bn: Derive or break]` and lists several claims Γ ⊢ φ, some valid and some invalid look-alikes, **without saying which**. The reader either derives φ or breaks the claim by showing the **counterexample set** (Γ together with ¬φ; NOTATION.md) can be made true all at once. The means of breaking grows with the book: a situation making the premises true and the conclusion false (until Chapter 4), or a refuting row (once Section 4.7 has proved soundness), or a counter-model (from the counter-model section of the models chapter). The solution states the verdict first, then the derivation or the breaking case.

**5. Chapter Summary and Terms.** Each chapter's `index.md` ends with two sections:

```markdown
## Summary

What the chapter proved, in four to eight sentences, and what it left open (the next chapter's question).

## Terms

- **derivation**: a list of lines, each a premise, an assumption or a rule's result (@def-derivation).
- **discharged assumption**: … (@def-…).
```

The Terms list is a glossary of the chapter's definitions, alphabetical, one line each, every entry linked to its definition by label. The volume's glossary page `src/glossary.md` (listed in the config under `"back-matter"`, which the engine builds as an unnumbered page after the last chapter) collects every chapter's Terms list, merged alphabetically, each entry keeping its link. The Summaries of Chapters 3 and 5 close with a paragraph on what is proved and what is open, under no special name (not "Interlude").

**6. The "used later" marker.** An exercise whose result or object a later section comes back to (a later exercise builds on it, a later example reuses its structure, a later remark recalls it) carries `, used later` in its title: `[B3, used later]`. The later place refers to it by label. No proof rests on an exercise (DRAFTING.md, "References"): a later proof that needs the fact proves it or cites a labelled result, and the marker only tells the reader not to skip the item.
