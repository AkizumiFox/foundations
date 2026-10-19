# Drafting brief (shared by all section-drafting agents)

You are drafting sections of a comprehensive, reader-caring textbook (Pandoc Markdown -> static site + PDF). The repository root is the book; `./build.py` builds it.

Drafting is stage **S3** of the per-chapter pipeline (`authoring/PIPELINE.md`). Before you start, the chapter's blueprint has been expanded (S1) and verified (S2) and is **frozen**: its statements, hypotheses and proof routes have been checked by a referee who hunted for counterexamples. After you finish, mechanical gates (S4), two blind referees (S5) and an exercise verifier (S6) read what you wrote. They also read your sidecar scripts and your dependency ledger, so write those for them.

## Read before writing
1. `authoring/STYLE.md`: the writing standard. Follow it exactly: explain template, Idea/Proof registers, Quick checks, warnings, A/B/C (and R) exercises with complete solutions, the dependency-ledger and meta-claim rules of §9, the reader-alone formats of §11, and §12: the second-reading fold, the forward-reference budget and, in fd1 and other introductory volumes, the entry conventions (rule card, Givens/Goal table, snapshots, drills, quick-check density).
2. `authoring/NOTATION.md`: fixed notation and the typesetting rules for logic; `latex/macros.tex` for available macros; `latex/fitch-book.sty` for derivations (Part 0).
3. `~/coding/book-template/src/ch00-demo/01-every-environment.md`: the markup of every environment. The approved exemplar chapter named in `authoring/STATUS.md` shows it in use in this book; imitate its register, density and exercise design.
4. `authoring/blueprints/chNN.md`: your chapter's **frozen** blueprint is the spec: content, labels to create, statements with all hypotheses, proof routes, examples, exercises with intended answers, key proofs, exit checks, where the §11 items go, and the promises to pay. `authoring/design/decisions.md` and `curriculum.md` explain why the book is shaped as it is; read the parts about your chapter.
5. The earlier chapters' label lists: `grep -rho "{#[a-z]*-[^} ]*" src/chNN-*/` for each earlier chapter. Read the specific earlier results you cite, so your recall of them is accurate.
6. The promise table in `authoring/STATUS.md` (and `tools/promises.py`'s list for your chapter): the promises your chapter must pay.
7. Old versions of your files (if any), to preserve labels.

## Rules
- **Original prose only.** Do not copy from any textbook. A reference work may be consulted only to check that a statement is true or that coverage is complete. Never paraphrase its text, examples or exercises. Copyrighted material is never committed to this repository.
- **Follow the frozen blueprint.** If you find it wrong (a false statement, a missing hypothesis, a route citing a label that does not say what the route needs), write the correct mathematics in your draft and report it under "Blueprint deviations" with a counterexample or the reason. The coordinator sends it back to S2's referee.
- **Displays.** Keep every display inside the text column: a formula wider than about 60 characters of ordinary math is broken with `aligned` or `cases` (a `\tag` goes after `\end{aligned}`, never inside). No blank line inside a `\[ ... \]`.
- **Second-reading fold** (STYLE §12.0). `::: {.second-reading title="…"}` takes what a first reading may skip: a meta-proof (its statement and one-sentence meaning stay on the main line), edge cases and minimal-change non-examples, long justifications, instructor notes. It is **not** `.optional`: a result proved inside it may be cited later, and the gates read it as main line. Never fold a definition the main line uses, the section's only Quick check or warning, a heading, or another fold. Close every fold and reread: the main line must still teach the section. Moving a cited proof into a fold moves it verbatim.
- **Forward references** (STYLE §12.1). No `@ref` to a result the reader has not met may serve as a reason, in a proof or in prose; in fd1 and introductory volumes, at most one "Looking ahead" remark per section, at the end of the main line, naming the chapter in words.
- **Effort in proportion to difficulty** (STYLE §12.2): three bullets for a rule or notion with nothing hidden; the full clause-by-clause reading only where the conditions bite.
- **Entry conventions (fd1 and introductory volumes; STYLE §12.3–§12.12):** edge cases into the fold or one "Is this legal? Is it useful?" A item; every worked derivation shown as two or three snapshots (goal at the bottom, `\vdots` gap row, final line numbers) before the finished one; scratch work as a Givens / Goal table; a rule card at the end of every rule section, cumulative at the end of a run of them; about one Quick check per 800–1,000 main-line words; a drill bank under A with folded answers (15 parts in fd1 Chapters 1–2, 12 elsewhere, in §12.8's ramp from recognition to construction), at least one scaffolded B item ("Name the move, then complete it."), meta-proof and hard C items titled as challenges; a school-level example before the analysis one; the notation rules of §12.10; ∧I cited in either order (the written line decides), →E implication first.
- **Deepening devices (fd1; STYLE §12.13):** assumption purposes ("asm, for →I": inferred by the engine, written as `\purpose{\ii}` only where no line closes the box yet); a rule-instance gallery beside each rule card (three instances with large compound substitutions, one tempting non-instance with its reason); a "Not allowed" warning after each rule card (three to five wrong steps, each tagged with the clause it breaks, WRONG beside RIGHT where a side condition bites); at least one derive-or-break B item per rule section from 1.5 on, verdict withheld; the chapter `index.md` ends with `## Summary` and `## Terms`; `, used later` in the title of an exercise a later section comes back to.
- **Structure.** Section length ~2,500–5,000 prose words **on the main line** (math spans count as one word; prose inside second-reading folds is counted apart, and the blueprint gives it its own budget). Complete: opening frame; notions per the explain template; theorems with lead-in / Idea / Proof / aftermath; ≥1 `::: {.check}` followed (not nested) by a `::: {.solution}` block; ≥1 `::: {.warning}`; `## Exercises` with `### A. Check your understanding` / `### B. Practice` / `### C. Going deeper`, and `### R. Review` in the chapter's **last** section only; each exercise `::: {#exr-<section-slug>-a1}` titled `[A1]` (`-r1` titled `[R1]`, and so on) followed by a complete `::: {.solution}`. A Gate section follows STYLE §11.10 instead.
- **Math.** `\( \)` and `\[ \]` only. Relation symbols are typeset, never unicode characters: proof-direction tags are `\( (\Rightarrow) \)`, `\( (\Leftarrow) \)`, `\( (\subseteq) \)`, `\( (\supseteq) \)`, and a chain reads `(a) \( \Rightarrow \) (b)`. Pandoc fenced divs must be closed, with blank lines around them.
- **Derivations (Part 0)** are fitch.sty `nd` environments in a raw LaTeX block, as `latex/fitch-book.sty` and NOTATION.md describe: `\hypo`, `\have`, `\open`/`\close`, the rule macros (`\ai{…}`, `\ie{…}`, `\raa{…}`, …) or `\by{text}{refs}`; an assumption's purpose `\purpose{\ii}` (STYLE §12.13); a truth-functional step `\taut{refs}` (`\by{TAUT}{refs}`), only from F1.3 §08 on: for propositional formulas in Chapter 4, over the propositional skeleton from F1.8 §03 on (NOTATION.md, TAUT). Never `array`s. A deliberately invalid derivation (a find-the-error item) carries the marker that `tools/check_fitch.py` documents, so the checker expects its failure.
- **Labels** are globally unique: grep `src/` before creating one. Keep every "keep label" exactly.
- **References.** `@label` refs only to earlier material (earlier chapters, earlier sections of this chapter, or earlier in your file). Forward pointers in prose say "in Chapter N" without an `@ref`. Linear algebra is cited from the companion book with `@la:<label>` (STYLE, "The companion book"). No proof, idea or claim may rest on an exercise, and every result is either proved or plainly marked as not proved here, with nothing depending on it.
- **Sidecar scripts.** Every non-trivial computation and every chosen constant (N, δ, r, a bound, a numeric answer) is checked by `verify/chNN/<label>.py`, named after the block that quotes the values. Put the values the text quotes in a dict `QUOTED = {...}` at the top, then `assert` each one from an independent computation (sympy, exact fractions, or a numeric check of a constant on several values). The script exits non-zero on failure and runs with `.venv/bin/python` from the repo root. One script may cover several values of one block. Never mention the scripts, or any software, in the book text (runnable `{.python .run}` cells are the only exception).
- **Dependency ledger.** Every section file ends with the `<!-- dependency ledger … -->` comment of STYLE §9: every fact a proof, idea, claim, solution or example uses without an `@ref`, with its source; `none:` if there are none. Be honest. An unledgered fact that a referee finds is a finding against the section; a ledgered one is a note.
- **Meta-claims.** Every sentence about the book's own text ("the classical step comes after the proof", "everything else fails in ℚ") points at something on the page and is true of it (STYLE §9). If you cannot make one checkable, cut it.
- **Reader-alone items** (STYLE §11) go where the blueprint puts them: comprehension parts for key proofs; find-the-error with a true conclusion; proof ordering and faded proofs (Parts 0–I, later only for new moves); try-it-first (at most two per chapter); hint ladders on C items; and a `**Marking scheme.**` ending every exit check's and write-up C item's solution.
- **index.md.** If you write the chapter's `index.md`, write it last, against the delivered sections. It has the **Time** line (STYLE §2), computed from your sections' prose word counts and exercise counts by the formula in `authoring/design/research-reader.md` B1: the core track from main-line prose only, the full track adding the folded prose. `python3 tools/check_structure.py --words src/chNN-…` prints both counts and their reading hours.
- **Spelling.** American spelling. Add genuine new words to `spelling.txt` (append only).
- **Scope.** Do not delete or rename files other than those assigned; do not edit other sections, the config, or `authoring/STATUS.md` (report promises instead).

## Diagrams

Draw a picture where the structure is spatial: every finite structure as an arrow or Hasse diagram, search and refutation trees, the square of opposition, a procedure as a flowchart. The engine's `latex/book-diagrams.sty` gives each a TikZ template, in the PDF and (compiled to an SVG) on the website. A picture is a raw LaTeX block holding a `tikzpicture` written out in full: the website finds a picture by its `\begin{tikzpicture}`, so never hide one in a macro. No colours and no white fills: the website's dark mode inverts the SVG. Each example below compiles as it stands (the engine's `tests/test_diagrams.py` builds the same files).

**A finite structure as an arrow diagram** (`structure`, `elt`, `rel`, and `universe` for a frame round the domain): elements are dots labelled with `label=below:…`, the relation is arrows, a loop is `to[loop above]`.

```latex
\begin{tikzpicture}[structure]
  \node[elt, label=below:$0$] (a) at (0,0) {};
  \node[elt, label=below:$1$] (b) at (1.6,0) {};
  \node[elt, label=below:$2$] (c) at (3.2,0) {};
  \draw[rel] (a) to[bend left] (b);
  \draw[rel] (b) to[bend left] (a);
  \draw[rel] (b) -- (c);
  \draw[rel] (c) to[loop above] (c);
  \node[universe, fit=(a)(b)(c)] {};
\end{tikzpicture}
```

**A Hasse diagram** (`hasse`, and `hpt` for unlabelled points): greater elements higher, plain edges for the covering pairs only.

```latex
\begin{tikzpicture}[hasse]
  \node (e) at (0,0) {$\varnothing$};
  \node (a) at (-1.2,1.1) {$\{a\}$};
  \node (b) at (1.2,1.1) {$\{b\}$};
  \node (t) at (0,2.2) {$\{a,b\}$};
  \path (e) edge (a) (e) edge (b) (a) edge (t) (b) edge (t);
\end{tikzpicture}
```

**A truth tree or refutation tree** (`tree`): each node is a stack of formulas separated by `\\`; `\ticked` marks a formula already used, `\closedbranch` (×) ends a closed branch, `\openbranch` an open one; `tlabel` for an edge label. A node hangs from its top, so give a tall first stack room with `level 1/.style={level distance=…}`.

```latex
\begin{tikzpicture}[tree, level 1/.style={level distance=23mm}]
  \node {$P \to Q$ \ticked \\ $Q \to R$ \ticked \\ $\neg(P \to R)$ \ticked \\ $P$ \\ $\neg R$}
    child {node {$\neg P$ \\ \closedbranch}}
    child {node {$Q$}
      child {node {$\neg Q$ \\ \closedbranch}}
      child {node {$R$ \\ \closedbranch}}};
\end{tikzpicture}
```

**The square of opposition**: `\oppositionsquare[side]{A}{E}{I}{O}` inside `\begin{tikzpicture}[square]` draws the corners (nodes `A`, `E`, `I`, `O`) and names the four relations.

```latex
\begin{tikzpicture}[square]
  \oppositionsquare{$\forall x\,(S(x) \to P(x))$}{$\forall x\,(S(x) \to \neg P(x))$}
                   {$\exists x\,(S(x) \wedge P(x))$}{$\exists x\,(S(x) \wedge \neg P(x))$}
\end{tikzpicture}
```

**A flowchart** (`flowchart`, `fc start`, `fc step`, `fc test`, `fc arrow`), placed with `below=of`, `right=of`; `\\` breaks a line inside a node.

```latex
\begin{tikzpicture}[flowchart]
  \node[fc start] (s) {start: the counterexample set};
  \node[fc test, below=of s] (t) {an unticked formula\\on an open branch?};
  \node[fc step, below=of t] (d) {apply its rule; close every\\branch holding $\varphi$ and $\neg\varphi$};
  \node[fc start, right=of t] (e) {stop: all closed, valid;\\else an open branch refutes};
  \draw[fc arrow] (s) -- (t);
  \draw[fc arrow] (t) -- node[right, font=\scriptsize] {yes} (d);
  \draw[fc arrow] (t) -- node[above, font=\scriptsize] {no} (e);
  \draw[fc arrow] (d.west) -- ++(-0.5,0) |- (t.west);
\end{tikzpicture}
```

## The glossary page

A volume's glossary is a plain Markdown page, `src/glossary.md`, listed in its `config/config.json` under `"back-matter": ["src/glossary.md"]`; the engine builds it as an unnumbered page after the last chapter, links it from the sidebar, and prints it at the end of the book PDF. It opens with `# Glossary` and one sentence, then one bulleted list, alphabetical, merging every chapter's `## Terms` list (STYLE §12.13) with each entry's link kept: `- **counterexample set**: the premises together with the negated conclusion (@def-…).` It holds no definitions of its own and no theorem environments. It is assembled in the whole-volume pass, after the chapters' Terms lists exist; until then the config does not list it.

## When done
1. Run your sidecars: `for f in verify/chNN/*.py; do .venv/bin/python "$f" || echo "FAIL $f"; done`.
2. Run the first-tranche gates on your files, as each tool's `--help` documents: `tools/check_structure.py`, `tools/check_fitch.py` (Part 0), `tools/promises.py`. Fix everything they report in YOUR files.
3. Build in your own copy (see below): `./build.py html 2>&1 | grep -i "warn\|error" | head -30`, then `tools/check_rendered.py` on that build. Fix warnings originating in your files; ignore issues from files that are not yours.
4. Run `.venv/bin/python blueprint/originality.py <chapter>` and rewrite any flagged prose.

**Reply with**, in this order:
- **Files written**, with prose word counts per section (main line + folded, as `check_structure.py --words` prints them).
- **Labels created.**
- **Sidecars:** the scripts written, and confirmation that all pass.
- **Dependency ledger:** the number of ledger lines per section, and every line whose source is `chNN (promised)`, verbatim.
- **Promises opened:** each prose pointer, with file, line and target chapter.
- **Promises paid:** each promise from STATUS's table that you paid, with the paying label.
- **Blueprint deviations** and why, with a counterexample where the blueprint was wrong.
- **Gate results:** each tool's result on your files.
- **Claims you were unsure about**, with file and line.

## Building while other agents work

Several drafting agents may run at once, and **the scratchpad directory is shared between all of them**. Never build in the shared source tree (concurrent builds corrupt `_build/cache`), and never build in a generically named scratch folder such as `scratchpad/repo/`: in one chapter two agents used the same one and one `rsync --delete`d the other's copy. Copy the repo into a directory named after your own sections, for example `scratchpad/ch17-s05-s07/repo/`, and build there.
