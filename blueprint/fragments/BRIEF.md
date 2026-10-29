# Brief: build one Part's DAG fragment and chapter plan

You are planning **one or two Parts** of a proof-based analysis textbook, "the book", written in English. The book runs in one sequence from logic to Sobolev spaces. This repository, `~/coding/analysis-book`, holds it. Its engine and workflow copy a finished sibling, `~/coding/math-atlas/books/regression`: read that repository's `blueprint/book.yaml` and `blueprint/dag.json` to see the target shape.

## Read first
- `authoring/design/decisions.md` sets the Part structure and the rules.
- `authoring/design/curriculum.md` lists, stage by stage, what the reader must know and prove. Your chapters have to cover your stage **completely**.
- `blueprint/sources.yaml` lists the reference books, their codes and their roles.
- `.venv/bin/python blueprint/toc.py CODE` prints a reference book's table of contents: section files, PDF pages and headings. Open a section file under `~/math-refs/analysis/converted/<dir>/sections/` when a heading alone does not tell you what the section covers. Never copy any text from these books; you only read them to plan.

## Write: `blueprint/fragments/part-<X>.yaml`
Use exactly this schema. The sample entries are illustrative.

```yaml
part: I                      # or "0", "II", ...; one file per Part
title: "Analysis on the Real Line"
summary: "One sentence: what this Part does and what forces it."
nodes:                       # one per chapter (or appendix) of each of YOUR assigned reference books that the Part draws on
  ABB.1: {book: ABB, ch: "1", title: "The Real Numbers", pages: 37, files: "005-016"}
  PMA.2: {book: PMA, ch: "2", title: "Basic Topology", pages: 26, files: "010-018"}
hard:                        # a must be read before b (the reference books' own prerequisite logic, within and across your books)
  - [ABB.1, ABB.2]
soft:                        # helpful, not required
  - [BRR.1, ABB.2]
alt:                         # alternative treatments of the same material
  - [ABB.2, PMA.3]
external:                    # prerequisites on material in OTHER Parts, in words (the merger resolves them)
  - {needs: "sup/inf, LUB axiom (Part I ch 1)", for_chapter: metric-spaces}
chapters:                    # the BOOK's chapters for this Part, in reading order
  - slug: least-upper-bound                  # kebab-case, unique across the book
    title: "Ordered Fields and the Least Upper Bound Axiom"
    pages: 30                                # sum of source pages actually drawn on (the page budget)
    sources: [[ABB.1, "§1.3–1.4"], [PMA.1, "ordered fields, LUB"], [TAO1.5, "§5.4–5.5 (depth)"]]
    outline:                                 # 4–8 planned sections, each one line saying what it does
      - "Ordered fields and why Q is not enough"
      - "Upper bounds, suprema, and the axiom"
    must_prove: ["ε-characterization of sup", "Archimedean property", "density of Q", "existence of √2"]
    key_examples: ["{x∈Q : x²<2} has no sup in Q", "ℝ(x) is non-Archimedean"]
    exit_checks: ["sup(A+B) = sup A + sup B, both directions"]
    optional: false          # true for chapters that sit beside the main line (e.g. Part 0 constructions)
    note: "anything the drafter must know: placement decisions, splits, cross-Part hooks"
cut: {}                      # nodes of your books deliberately not used, with the reason, e.g. {PMA.10: "forms deferred (decisions.md 12)"}
exemptions: []               # hard edges your chapter order crosses, each with a justification: {edge: [a,b], why: "..."}
coverage_gaps: []            # items in curriculum.md your stage lists that no source chapter covers well (these become original writing)
```

## Rules
- **Chapter size.** Aim for 25 to 60 source pages per chapter and 4 to 8 sections each. Regression averages about 45 pages over 45 chapters. The whole book will likely have about 60 chapters, so Parts I, II, IV and VI get roughly 8 to 11 chapters each, and Parts 0, III and V roughly 5 to 9.
- **Order.** Order chapters so that no chapter needs a later one. The reference books' hard edges must be respected, unless an entry in `exemptions` justifies crossing one.
- **Decisions.md placement.** Follow the placements in `decisions.md` exactly:
  - the three-way split of point-set topology;
  - Lᵖ duality and Riesz–Markov go in Part VI;
  - Fubini and change of variables are proved in full in Part IV;
  - the Riemann integral on ℝⁿ goes in Part II;
  - completion goes in Part II;
  - the Part 0 constructions are optional;
  - the LUB axiom opens Part I, and the equivalent forms of completeness come at the end of Part I;
  - Green's theorem is a node;
  - the second layer of complex analysis is covered.
- **Coverage.** Every item under (b), (c) and (g) of your stage in `curriculum.md` must appear in some chapter's `outline` or `must_prove`. At the end of your reply, list any item you placed elsewhere or dropped, with the reason.
- **What not to write.** Do not write book prose, and do not edit any file except your own `part-<X>.yaml` files.
- **Reply.** When you finish, reply with at most 300 words:
  - the chapter list, with page budgets;
  - your notable placement decisions;
  - any conflicts with `decisions.md` that you could not resolve.
