# fd1 D2: downstream sweep report (applied 2026-10-25)

**Applied 2026-10-25**, after all eight chapters passed S5–S8. The dry run was regenerated on the current texts (117 mechanical rewrites in 33 files, 176 hand hits), the map checked against layout-final §5.1, and every hand hit resolved by the `@fd1:` labels on or near its line. Pointer changes per volume:

| | fd2 | fd3 | fd4 | an1 | root `authoring/STATUS.md` | Σ |
|---|---:|---:|---:|---:|---:|---:|
| mechanical (renumber.py) | 77 | 29 | 3 | 3 | 5 | **117** |
| by hand: old Chapter 4, Sections 4.7, 4.11, ranges, and pointers renumber.py cannot see ("its Chapter 3", "induction, Chapter 3 (@fd1:…)", "from Section 5.6") | 31 | 22 | 14 | 3 | 2 | **72** |
| chapter counts ("five chapters" → "eight"; Gate 0's "those eight chapters" → "eleven"; fd2 Ch 1 "the first five chapters" → "eight") | 3 | 0 | 0 | 0 | 0 | **3** |
| atlas tags (`F1.4 §07` → `§08` for the maximum, `F1.4 §09` → `F1.8 §02`, `F1.4 §11` → `F1.6 §01`/`§02`, `F1.4 §12` → `F1.6 §03`) in src ledger rows and blueprints | 11 | 4 | 2 | 0 | 0 | **17** |
| blueprint/ledger quotes of changed pointers | 0 | 2 | 0 | 0 | 0 | **2** |

The 19 "Chapter 2" hits were screened: none means the search method (now Chapter 3). Every Chapter 2 hit and every unchanged "Chapters 1 and 2" stands. The fd2 Gate 0 map (07:94, 363–366) names every fd1 item by its current section. Checks after the sweep: `build.py check` passes in fd2, fd3, fd4 and an1; `promises.py --reconcile` reports 0 unrecorded promises in fd1–fd4 (one new false match, fd3 Ch 4 index:7 "chiefly Chapter 6", recorded in STATUS row F3.9 → F3.4); `ledger.py stale` reports 0 stale verdicts in every chapter of fd2, fd3, fd4 and an1 (pointer masking), so no S8 verdict needed recording. STATUS.md's deferred note (fd1 Ch 8 deepening, (b)) is closed. Not done, left to the author: the optional content upgrades of layout-final §8 (fd2 1.1 citing `@fd1:thm-barber`, fd3 6.5 citing `@fd1:thm-isomorphism-invariance`); analysis-series `authoring/NOTATION.md` (a copy of foundations' NOTATION.md, still with the old F1.3/F1.4 tags) and `authoring/series.json` are refreshed by their own sync, not by this sweep. Ledger evidence that names old fd1 paths (fd3 ch03–05, fd4 ch02–03) is history and was left.

The report below is the dry run of 2026-10-13, kept as the record of the method.

---


Generated 2026-10-13 during the D2 restructure. **Nothing below has been applied**: per the D2 brief, fd2, fd3, fd4 and analysis-series are swept at the very end, after the author merges D2.

Command (from `foundations/`; `downstream-map.json` is layout-final §5.1 written as a renumber.py map, without moves):

```
.venv/bin/python tools/renumber.py downstream-map.json --series series-no-fd1/authoring/series.json \
    --exclude 'authoring/pilot-archive/*' --exclude 'authoring/reviews/*' --dry-run
```

`series-no-fd1` is `authoring/series.json` with fd1 made unreachable, so fd1's already-swept files are not mapped twice. The map is layout-final §5.1 with no moves; "Section 3.2" is mechanical downstream (all hits are numerical induction → 4.2).

## Totals

| | fd2 | fd3 | fd4 | an1 | root `foundations/authoring` | Σ |
|---|---:|---:|---:|---:|---:|---:|
| mechanical rewrites | 77 | 29 | 3 | 3 | 4 | **116** (33 files) |
| to read by hand | 37 | 94 | 28 | 3 | 8 | **170** |

The 170 hand hits: 117 are plain "Chapter N"/"Section N.M" pointers on a line that also names *Logic and Proof* (renumber.py cannot tell whether they point into fd1 or into the file's own volume); 44 are fd1 "Chapter 4" (mapped to "?": 5, 6 or 7); 9 are fd1 Sections 4.11 and 4.7 (mapped to "?").

## Mechanical rewrites by file

| File | Rewrites | Hand hits |
|---|---:|---:|
| `analysis-series/an1/src/ch01-least-upper-bound/02-suprema.md` | 0 | 1 |
| `analysis-series/an1/src/ch01-least-upper-bound/05-archimedean-property.md` | 2 | 1 |
| `analysis-series/an1/src/ch01-least-upper-bound/index.md` | 1 | 1 |
| `authoring/STATUS.md` | 4 | 8 |
| `fd2/authoring/ledger/ch01.yaml` | 1 | 0 |
| `fd2/src/ch01-sets-and-functions/01-sets-and-subsets.md` | 4 | 10 |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md` | 5 | 10 |
| `fd2/src/ch01-sets-and-functions/03-products-and-relations.md` | 2 | 0 |
| `fd2/src/ch01-sets-and-functions/04-functions.md` | 5 | 2 |
| `fd2/src/ch01-sets-and-functions/05-inverses.md` | 1 | 2 |
| `fd2/src/ch01-sets-and-functions/06-images-and-preimages.md` | 11 | 0 |
| `fd2/src/ch01-sets-and-functions/index.md` | 4 | 1 |
| `fd2/src/ch02-relations-and-induction/01-naturals-and-well-ordering.md` | 10 | 1 |
| `fd2/src/ch02-relations-and-induction/02-induction-in-practice.md` | 8 | 0 |
| `fd2/src/ch02-relations-and-induction/03-recursion.md` | 3 | 0 |
| `fd2/src/ch02-relations-and-induction/05-equivalence-relations.md` | 1 | 0 |
| `fd2/src/ch02-relations-and-induction/index.md` | 4 | 1 |
| `fd2/src/ch03-countable-and-uncountable/03-countable-unions-and-choice.md` | 0 | 1 |
| `fd2/src/ch03-countable-and-uncountable/04-diagonal-arguments.md` | 2 | 0 |
| `fd2/src/ch03-countable-and-uncountable/05-comparing-cardinalities.md` | 1 | 0 |
| `fd2/src/ch03-countable-and-uncountable/06-infinite-sets.md` | 0 | 1 |
| `fd2/src/ch03-countable-and-uncountable/07-gate-0.md` | 11 | 1 |
| `fd2/src/ch03-countable-and-uncountable/index.md` | 4 | 5 |
| `fd2/src/index.md` | 0 | 2 |
| `fd3/authoring/blueprints/ch04.md` | 0 | 3 |
| `fd3/authoring/blueprints/ch06.md` | 0 | 1 |
| `fd3/authoring/ledger/ch03.yaml` | 0 | 1 |
| `fd3/src/ch01-zf-and-natural-numbers/01-sets-from-axioms.md` | 1 | 3 |
| `fd3/src/ch01-zf-and-natural-numbers/03-the-set-omega.md` | 2 | 1 |
| `fd3/src/ch01-zf-and-natural-numbers/06-order-on-omega.md` | 1 | 0 |
| `fd3/src/ch01-zf-and-natural-numbers/07-categoricity.md` | 7 | 0 |
| `fd3/src/ch01-zf-and-natural-numbers/index.md` | 8 | 1 |
| `fd3/src/ch02-integers-and-rationals/index.md` | 4 | 4 |
| `fd3/src/ch03-divisibility-and-congruences/01-division-with-remainder.md` | 0 | 3 |
| `fd3/src/ch03-divisibility-and-congruences/index.md` | 2 | 13 |
| `fd3/src/ch04-ordered-field-sequences/index.md` | 1 | 24 |
| `fd3/src/ch05-reals-from-cauchy/index.md` | 2 | 18 |
| `fd3/src/ch06-complete-ordered-field/05-axioms-or-model.md` | 0 | 2 |
| `fd3/src/ch06-complete-ordered-field/index.md` | 0 | 10 |
| `fd3/src/ch07-reals-dedekind-cuts/index.md` | 1 | 10 |
| `fd4/src/ch01-complex-numbers/04-square-roots-and-order.md` | 0 | 4 |
| `fd4/src/ch01-complex-numbers/index.md` | 0 | 8 |
| `fd4/src/ch02-fields/index.md` | 0 | 2 |
| `fd4/src/ch03-groups-and-permutations/index.md` | 1 | 5 |
| `fd4/src/ch04-formal-polynomials/index.md` | 1 | 3 |
| `fd4/src/ch05-polynomials-over-a-field/index.md` | 1 | 6 |

## The "?" hits (fd1 Chapter 4, Sections 4.7 and 4.11) with the expected resolution

| File:line | Pointer | Expected (layout-final §5.1, §5.2) |
|---|---|---|
| `fd2/src/ch01-sets-and-functions/01-sets-and-subsets.md:31` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/01-sets-and-subsets.md:87` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/01-sets-and-subsets.md:106` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/01-sets-and-subsets.md:115` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/01-sets-and-subsets.md:174` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/01-sets-and-subsets.md:399` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/01-sets-and-subsets.md:409` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:225` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:300` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:318` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:328` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:335` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:353` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:361` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:421` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/02-set-operations.md:463` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/04-functions.md:296` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/04-functions.md:498` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/05-inverses.md:107` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/05-inverses.md:214` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch01-sets-and-functions/index.md:7` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch02-relations-and-induction/01-naturals-and-well-ordering.md:150` | *Logic and Proof*, Section 4.7 | 5.8 (the maximum, ∃!) |
| `fd2/src/ch02-relations-and-induction/index.md:7` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch03-countable-and-uncountable/03-countable-unions-and-choice.md:18` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd2/src/ch03-countable-and-uncountable/06-infinite-sets.md:281` | *Logic and Proof*, Section 4.11 | 7.2 (counter-model statement) |
| `fd2/src/ch03-countable-and-uncountable/07-gate-0.md:365` | *Logic and Proof*, Section 4.11 | 7.2 (counter-model statement) |
| `fd2/src/ch03-countable-and-uncountable/index.md:7` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch01-zf-and-natural-numbers/01-sets-from-axioms.md:13` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch01-zf-and-natural-numbers/01-sets-from-axioms.md:245` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch01-zf-and-natural-numbers/01-sets-from-axioms.md:245` | *Logic and Proof*, Section 4.11 | 7.1 (structures / non-empty domains / ℂ square root check) |
| `fd3/src/ch01-zf-and-natural-numbers/03-the-set-omega.md:161` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch01-zf-and-natural-numbers/index.md:7` | *Logic and Proof*, Chapters 2 and 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch02-integers-and-rationals/index.md:7` | *Logic and Proof*, Chapters 2 and 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch02-integers-and-rationals/index.md:18` | *Logic and Proof*, Chapters 2, 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch04-ordered-field-sequences/index.md:7` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch04-ordered-field-sequences/index.md:18` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch06-complete-ordered-field/05-axioms-or-model.md:51` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch06-complete-ordered-field/05-axioms-or-model.md:105` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch06-complete-ordered-field/index.md:7` | *Logic and Proof*, Chapters 2–4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd3/src/ch07-reals-dedekind-cuts/index.md:7` | *Logic and Proof*, Chapters 4 and 5 | Chapters 5, 6 and 8 (layout §5.1 example) |
| `fd3/authoring/blueprints/ch06.md:87` | *Logic and Proof*, Chapters 2–4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `fd4/src/ch01-complex-numbers/04-square-roots-and-order.md:3` | *Logic and Proof*, Section 4.11 | 7.1 (structures / non-empty domains / ℂ square root check) |
| `fd4/src/ch01-complex-numbers/04-square-roots-and-order.md:74` | *Logic and Proof*, Section 4.11 | 7.1 (structures / non-empty domains / ℂ square root check) |
| `fd4/src/ch01-complex-numbers/04-square-roots-and-order.md:326` | Logic and Proof, Section 4.11 | 7.1 (structures / non-empty domains / ℂ square root check) |
| `fd4/src/ch01-complex-numbers/index.md:7` | *Logic and Proof*, Section 4.11 | 7.1 (structures / non-empty domains / ℂ square root check) |
| `analysis-series/an1/src/ch01-least-upper-bound/02-suprema.md:25` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `analysis-series/an1/src/ch01-least-upper-bound/05-archimedean-property.md:92` | *Logic and Proof*, Chapter 4 | Chapter 6 (quantifier negation, 6.2) |
| `analysis-series/an1/src/ch01-least-upper-bound/index.md:7` | *Logic and Proof*, Chapter 4 | Chapter 5 by default (rules, syntax, equality); 6 if the sentence is about translation, negating quantifiers or uniform continuity; 7 if about models |
| `authoring/STATUS.md:165` | *Logic and Proof*, Section 4.11 | 7.1 (structures / non-empty domains / ℂ square root check) |

## Not handled by renumber.py (hand pass at sweep time)

- **Atlas-form tags** (`F1.x §NN`) downstream, by the §5.4 map (`fd1-atlas-tags.json`): F1.3 §02 ×15 (read: §02 numbers or §03 formulas; fd2, fd3, root authoring), F1.4 §07 ×11 (read: §07 or §08; fd2, fd3, root), F1.4 §11 ×19 (read: F1.6 §01 or §02; fd2, fd3, fd4, root), F1.4 §12 ×3 → F1.6 §03 (fd2, fd3), F1.4 §09 ×4 → F1.8 §02 (fd2, root), F1.4 §08 ×2 → F1.8 §01, F1.3 §03–§07 ×19 and F1.2 §06 ×1 (root `foundations/authoring` design notes, outside STATUS). STATUS.md's F1 rows were already rewritten in D2 with atlas ids only.
- **"five chapters"**: `fd2/src/ch03-countable-and-uncountable/07-gate-0.md:3` ("The five chapters of *Logic and Proof*") → "eight chapters"; also check `fd2/src/ch01-sets-and-functions/index.md:3`.
- **"Chapter 2"** (19 downstream hits): screen by hand; none is known to mean the search method (which is now Chapter 3).
- **fd2 Gate 0 map** (`07-gate-0.md` 94, 363, 365): re-check after the sweep (layout-final §5.5).
- **Ledger evidence** in `fd3/authoring/ledger/ch03–05.yaml` and `fd4/authoring/ledger/ch02–03.yaml` (6 old fd1 path mentions): history, leave.
- **analysis-series `authoring/series.json`**: regenerate there with `tools/series.py refresh ../math-atlas/registry` once the atlas commit lands (foundations' copy was refreshed in D2).
- **fd1 Chapter 1** (excluded from D2 while its referee runs): its forward pointers are written new-style by `ch01-deepen`; confirm with the fd1 gate grep after the referee finishes.
