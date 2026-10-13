<!-- hand-written -->
# Deepening blueprint: F1.7 Finding Derivations (fd1 Chapter 3), stage S1

**Status: S1 draft (2026-10-13), revised after S2 round 1 (2026-10-13); replies in §11.**

**What this is.** The S1 blueprint for the new Chapter 3 of *Logic and Proof* in the final layout (`layout-final.md` §1.3: Chapter 3, F1.7, *Finding Derivations*, three core sections). It is the unit that `layout-final.md` §6.2 item 3 calls `ch03-finding-derivations.md`, written under the name the coordinator gave it, in the format of `ch01-deepen.md`. It is complete on its own. A drafter executes it with:
- this file;
- the current `fd1/src/ch03-finding-derivations/` (`01-finding-derivations.md` is old Section 2.6, moved verbatim by D2 at commit `034a2ae`; `index.md` is an S3-PLACEHOLDER; `02-…` and `03-…` do not exist yet);
- `ch02-revision.md` §4.6 (R3, frozen at S2 on 2026-10-12), which still binds Section 3.1 wherever this file does not change it (§4.1 lists every change);
- `authoring/STYLE.md` (§11, §12, and §12.8 and §12.13 as amended by D1), `DRAFTING.md` (including `\purpose` and the Diagrams templates of `latex/book-diagrams.sty`) and `NOTATION.md`;
- the delivered, deepened Chapter 1 (`fd1/src/ch01-connectives-and-derivations/`, drafted per `ch01-deepen.md`, S4 passed at `450fb43`) as the model of the register and of the devices.

Line numbers are those of the current files (HEAD `034a2ae`). `01:NNN` is `ch03-finding-derivations/01-finding-derivations.md` line NNN. D2 moved old `06-finding-derivations.md` without editing it, so `01:NNN` is the same line as R3's `06:NNN`, and R3's references can be read across directly.

**Inputs.**
- The deepening plan (`deepening-plan.md` §3.0 volume-wide devices; §3.2's items for old 2.6 and the new 2.7; §3.6's item 6.4, argument extraction; and the binding *Critic review*).
- The final layout (`layout-final.md` §1.3 Chapter 3 rows, §1.4 new labels, §2 reading-path rules G10, §3 size and time, §4 migration, §6 what stands).
- `labelmap.json`.
- The gap matrix (`gap-matrix.md` rows 1.4, 1.9, 2.7, 3.3, 3.6, 3.19, 7.1, 7.3, 7.8, 7.9, 9.7, and the device and exercise-type tables). It is used for **technique only**.
- The frozen R3 blueprint `ch02-revision.md` §4.6.
- STATUS.md promise rows touching F1.7.
- The ledger `fd1/authoring/ledger/ch03.yaml` (19 items, 0 stale).

Every example, drill, exercise, figure and answer below is the book's own, in mathematical dress, school mathematics first. No text, example, exercise, sequent list or figure is taken from any of the twelve books or closely paraphrased (plan, binding rule 3).

**Binding rules for this chapter.**
1. **No label is lost, renamed or changed in content except where this file says so.** All 17 labels now in the chapter keep their names (§3.1). Three move to Section 3.3, as `layout-final.md` §4.2 says: `exr-finding-derivations-r1`, `-r2`, `-r3`, with their prefix kept. Every cited block keeps its statement and proof. The new labels are listed in §3.2. They include the three fixed by `layout-final.md` §1.4: `def-inconsistent-set`, `prp-inconsistent-derives-everything` and `prp-derivable-iff-negation-inconsistent`.
2. **Section 3.1 is R3's §4.6 plus this file's §4.1.** R3's items 1–11 are executed as written, with three exceptions:
   - item 8 (Peirce's search) is executed and then moved, verbatim, into a fold;
   - item 12 (the Looking-ahead box) moves to Section 3.3;
   - R3 §9 D9 ("no separate decision chart") is superseded in part by the method flowchart of §4.1, item 3.

   The R3 S2a items for 2.6 (R3 §8, items 30–38 and 44) stay in force and are re-run by S2a on the delivered text.
3. **Non-derivability wording (layout G10).** Before Section 4.7, no text asserts that something is not derivable, except as a forward claim in a Looking-ahead box or in a plain pointer to Chapter 4 inside a solution. The same holds for "consistent": Chapter 3 **defines** the word, but it never says of a particular list that it **is** consistent. A list whose members can all be made true at once "breaks the claim that it derives \( \bot \)", and that is all Chapter 3 says of it. "Inconsistent" is shown only by a derivation of \( \bot \). S2a checks every sentence of §4 against this rule (§9, item 1).
4. **No truth tables, no "row", no ⊨, no "valid" or "satisfiable" on the main line.** Breaking is done as in Chapter 1: by a choice of statements that makes the counterexample set true, often statements about one number. The choice may also be written as "\( P \) true, \( Q \) false", realised by a true and a false statement, as `01:286` already does. The word *satisfiable* appears only in Section 3.2's Looking-ahead box, as Chapter 4's word.
5. **TAUT is not used** anywhere in Chapter 3 (layout §2 rule 3: TAUT starts in Section 4.8). Every derivation cites primitive rules or derived rules already proved (`def-derived-rule`). No step replaces a part of a line by an equivalent (that is `lem-replacement` in 4.5 and `prp-replacement` in 6.2). Section 3.3's library says so in its lead (§4.3, item 6).
6. **Γ is a finite list** (`def-derivable`). `def-inconsistent-set` is stated for finite lists only. Infinite sets are Section 4.10's business (Critic, small correction 1), and theories are Section 7.4's (`def-inconsistent-theory`, small correction 2). Chapter 3 points to neither on the main line.
7. **Batteries and libraries are fd1's own** (Critic, small correction 7). Section 3.3's library is grouped by fd1's named moves, in fd1's order. Its 15-item battery is fd1's own selection, in mathematical dress on the integer key of Section 1.1 B5. Neither reproduces Lemmon's numbered sequents or their order.
8. **Depends on D0, D1, the Chapter 1 pilot, and D2.** `"fitch-purposes": "infer"` is already set in `fd1/config/config.json`, so the engine prints "asm, for →I" and the rest. `\purpose{…}` is written by hand only where no justified line closes the box yet:
   - every snapshot whose closing line is unjustified or absent;
   - every scaffold;
   - the WRONG half of a WRONG/RIGHT pair.

   S4 runs `tools/check_fitch.py --purposes` on the chapter. This applies to the existing snapshots of `01-finding-derivations.md` too: the dead end at `01:263–284` (assumptions 2, 4 and 5) and the failed search at `01:449–459` (assumption 2) have closing lines with empty citations, and they gain `\purpose{\ii}` and `\purpose{\oe}`.

---

## 0. Chapter frame

**Title.** Finding Derivations (`index.md`'s `#` line; atlas F1.7; Part I, between Chapter 2's rules and Chapter 4's meaning).

**Motivating question** (layout §1.3, verbatim): *"You know every propositional rule. Given a sequent, how do you find a derivation, or decide to stop looking?"*

**One new idea per section** (layout §3):
- 3.1: the search method, with the detour rule and three new moves;
- 3.2: the task type decides the search, and the syntactic notion `def-inconsistent-set`;
- 3.3: argument extraction and two-column items.

**What you need.** Chapters 1 and 2. In particular:
- the rules for every connective and `def-derivation` with its boxes and scope rule;
- derived rules (`def-derived-rule`) and `lem-weakening-cut`, which layout-final moves to Section 2.3 (ch02-deepen);
- the classical rules of Section 2.5;
- the counterexample set (`def-counterexample-set`) and the move *try to break it* (Section 1.1);
- the format note "Derive it or break it" (Section 1.5).

The index also carries the quantifier note (§4.0, item 3).

**Roadmap** (three bullets, §4.0 item 6).

**Named moves** (nine; §4.0 item 7). The chapter's own are:
- *Find the goal among the resources*;
- *Derive what needs nothing new before opening a box*;
- *Look first for a clash partner already on a line*;
- *No detours*;
- *Let the task choose the search*;
- *Try to break it first*;
- *Name the unstated fact*;
- *Two columns*.

*Work from both ends* is gathered from Chapter 1 and completed here.

**Time** (§5): core about 14.5 h, written as **"About 15 hours"**; full about 27.3 h, written as **"about 25 hours"**. Layout §3 targets 16 / 27; the difference is rounding and the new sections coming in under their caps.

**The chapter's place in two threads** (layout §1.2):
- *The counterexample set.* Link 2 of its thread is "inconsistent: \( \Gamma, \neg\varphi \vdash \bot \)", in Section 3.2.
- *The mirror.* 3.1's twin is 6.3, 3.2's twins are 6.3 and 6.2, and 3.3's twin is 6.1. Each twin in Chapter 6 names its Chapter 3 twin in its Looking-back box. Chapter 3 names no twin, since its twins come later.

---

## 1. The volume-wide devices, as applied to Chapter 3

Chapter 3 is a **tasks** chapter and has no rule sections. STYLE §12.13 says the other fd1 sections "use the ones that fit". Here is what fits and where.

D1. **Purpose-annotated assumptions** (§12.13.1). They are printed by the engine. They are written by hand only as binding rule 8 says. Prose reads them once more:
- 3.1 says "the annotation names the step of the method that opened the box" (one sentence, §4.1 item 2);
- 3.3's two-column example reads "asm, for →I" as "Suppose" and "asm, for ¬I" as "If \( n \) were …" (§4.3 item 5).

D2. **Instance gallery** (§12.13.2). No rule section, so there is no rule gallery. Its analogue for the chapter's one definition is `exm-inconsistent-lists` (3.2): three inconsistent lists with compound members, and one tempting look-alike with its reason.

D3. **"Not allowed" blocks** (§12.13.3).
- 3.2: `[Not allowed: claims about inconsistency]`, five tagged lines.
- 3.3: `[Not allowed: extracting an argument]`, five tagged lines.
- 3.1 gets **no** new block. It already has three warnings: `01:347`, `01:490` and `01:687`. Its new material, the detour rule, is legal-but-useless advice, not a wrong step.
- No WRONG/RIGHT pair: no side condition is new in this chapter.
- No entry cites `exm-not-allowed-catalogue` by number, for the reason `ch01-deepen.md` D3 gives (it lives in Chapter 8).

D4. **The counterexample set** (§12.13.4, NOTATION). It is recalled by name in 3.2, where it becomes link 2 of the thread: `prp-derivable-iff-negation-inconsistent` says that \( \Gamma \vdash \varphi \) exactly when the counterexample set of the claim is inconsistent. Every "break" verdict in the chapter is phrased as "the counterexample set … is made true by …".

D5. **Derive-or-break items, verdict withheld** (§12.13.4). 3.2 makes this a **task type**, with a worked search and a flowchart. Section 1.5's "Derive it or break it" is recalled by name (the seam recorded in `ch01-deepen.md` §6). The items are:
- 3.2 B3, **used later**;
- 3.2 B4, the same format applied to lists, "derive ⊥ or make every member true";
- 3.3 B3, items 11–15.

The means of breaking is unchanged from Chapter 1: statements that make the counterexample set true.

D6. **Drill banks of 12** (§12.8: "12 elsewhere"; layout §3: "24 + battery").
- 3.1 completes R3's 11-part bank to 12, reordered into the ramp.
- 3.2 has a new 12-part bank.
- 3.3 has **no** A2 bank. Its 15-item B battery replaces one (layout §1.3, G17).

Each bank's one folded solution answers every part in one or two lines.

D7. **One fixed symbolization key** (plan §3.0.7). 3.3 **reuses Section 1.1 B5's integer key by name**: \( E \), \( P \), \( T \), \( G \). This is the seam that `ch01-deepen.md` D7 left open. It adds three facts about integers, F1–F3, stated once. The key is used throughout 3.3: the worked examples, the battery, the exit check and the ordering item, though B4's ordering item is about real numbers (§4.3). Reading back is used as a named check. Consequence for Chapter 1: at the S8 seam pass, `exr-statements-and-connectives-b5`'s title gains ", used later" (§6).

D8. **Chapter close** (§12.13.5). `index.md` ends with `## Summary` and `## Terms`. The Summary closes with a paragraph on what is proved and what is open (not titled "Interlude"). The index also gets the "Minimum for fd2" line (layout G14).

D9. **"Used later" markers** (§12.13.6). There are two, each recorded as a promise for the Chapter 4 S1 (§6):
- 3.2 B3 (derive or break): 4.6 recalls its four breaking claims and 4.7's retroactive paragraph certifies them (layout G5);
- 3.2 C2 (Challenge: splitting an inconsistency): 4.10's Lindenbaum step recalls it.

No proof rests on either: 4.6, 4.7 and 4.10 prove what they need. 3.3 uses Section 1.1 B5 (D7).

D10. **Pictures where the structure is spatial** (DRAFTING, Diagrams). Three new TikZ figures, each a raw LaTeX block with the `tikzpicture` written out in full, using only `book-diagrams.sty` styles, with no colours and no white fills:
- 3.1: a flowchart of the method (`flowchart`);
- 3.2: a flowchart for a claim with its verdict withheld (`flowchart`);
- 3.3: an argument map, the premises and unstated facts with arrows into the conclusion (`structure`, `elt`, `rel`).

There are no truth tables, no search trees and no rows-as-regions pictures (those belong to 4.4–4.6).

D11. **Not adopted in Chapter 3, with reasons.**
- (a) The inline "(Why?)" prompt (plan §3.0.9): STYLE §12.13 does not carry it, as in Chapter 1.
- (b) An opening quiz in the index: layout §1.3's index row for Chapter 3 lists none, and the index cap is 1,000 words.
- (c) A rule card or gallery per section: there are no rule sections. 3.1 keeps R3's cumulative 13-row card as the one-page reference (STYLE §12.6: "after … 2.6", now 3.1).
- (d) A Givens/Goal table in 3.2 and 3.3: the four-task table and the two-column tables do that job. R3's two tables in 3.1 stay, the second (`exm-skeleton-odd-product`'s) in fold F3.1-g for the budget (§4.1).

---

## 2. Section map

| § | Title (the `#` line) | File | Kind (layout keys) | Main line: now → budget | One new idea; what is added (details in §4) |
|---|---|---|---|---|---|
| index | Finding Derivations | `index.md` | N (placeholder replaced) | placeholder → ≤ 1,000 | Motivating question; What you need with the quantifier note; Time; Minimum for fd2; Roadmap; nine Named moves; Summary; Terms |
| 3.1 | How to Find a Derivation | `01-finding-derivations.md` | M, E | 4,652 → ≤ 5,000 | R3 §4.6, plus: four refinements (*find the goal among the resources*, *derive what needs nothing new first*, *a clash partner already on a line*, *no detours*) in a new subsection with `exm-search-free-lines`; the method flowchart; five new folds (Peirce's search, moved; other splits; Harman; why a detour's line was within reach; the odd product's Givens/Goal table, moved); A2 to 12; B4 (cut the detours); R items out to 3.3; Looking-ahead box out to 3.3 |
| 3.2 | Four Kinds of Task | `02-four-kinds-of-task.md` | N | 0 → ≤ 4,600 | The task decides the search; four worked searches (theorem, equivalence, inconsistency, derive or break); `def-inconsistent-set`, `prp-inconsistent-derives-everything`, `prp-derivable-iff-negation-inconsistent`; gallery of inconsistent lists; Not allowed; "One task in four costumes"; flowchart; A1, A2 (12), B1–B4, C1 (exit check), C2 (Challenge, used later) |
| 3.3 | From Argument to Derivation | `03-from-argument-to-derivation.md` | N | 0 → ≤ 3,400 | One key (1.1 B5) and three facts; extracting an argument (`exm-extract-argument`, argument map); Not allowed; two columns (`exm-two-columns`); the library of standard sequents grouped by use; Looking ahead (the chapter's question); A1, B1, B2 (scaffolded two-column), B3 (15-item battery), B4 (proof ordering), C1 (exit check), C2 (Challenge: Curry); R1–R3 (moved), R4 (dialogue) |

Files: `02-four-kinds-of-task.md` and `03-from-argument-to-derivation.md` are new (layout §4.1). The config lists chapter directories only (`fd1/config/config.json`), so no config edit is needed.

---

## 3. Labels

### 3.1 Every label now in the chapter (17): all kept

All 17 keep their names. Three move to Section 3.3, as layout §4.2 says, and keep their prefix. Cited outside ch03 (grep of `fd1/src`, `fd2/src`, `fd3/src`, `fd4/src`, `an1/src`, 2026-10-13):
- `exm-search-cases` (ch04 09);
- `exm-search-postpone-or` (ch04 07);
- `exr-finding-derivations-b1` (ch06 02, ch07 02);
- `exr-finding-derivations-c2` (ch04 08, twice: "found by search … has 13 lines").

None of these changes content.

| Label | Where | Change | Cited outside |
|---|---|---|---|
| `def-partial-derivation` | 01:29 | kept, block verbatim; moved after the first snapshot (R3 item 3) | — |
| `exm-search-distribute` | 01:99 | kept; R3's Givens/Goal table and the moved Quick check (R3 item 5) | — |
| `exm-search-cases` | 01:192 | kept; first snapshot added (R3 item 6) | ch04 09:641 |
| `exm-search-postpone-or` | 01:253 | kept; R3 item 7 (the `@cor-refuting-row` parenthetical of 01:286 cut). 01:344's last two sentences move verbatim to fold F3.1-d (§4.1 item 6); the dead-end snapshot gains `\purpose` (binding rule 8) | ch04 07:435 |
| `exm-search-raa` | 01:355 | kept; 01:436's last sentence moves verbatim to fold F3.1-d | — |
| `exm-skeleton-odd-product` | 01:472 | kept; R3 item 10 (Givens/Goal table, placed in fold F3.1-g, §4.1 item 9; the last parenthetical of 01:487 cut) | — |
| `exr-finding-derivations-a1` | 01:695 | kept; (b)'s solution loses its last parenthetical (R3) | — |
| `exr-finding-derivations-b1` | 01:726 | **frozen** (R3) | ch06 02, ch07 02 |
| `exr-finding-derivations-b2` | 01:812 | kept (the faded triple's middle) | — |
| `exr-finding-derivations-b3` | 01:864 | kept | — |
| `exr-finding-derivations-c1` | 01:897 | kept (the faded triple's last) | — |
| `exr-finding-derivations-c2` | 01:965 | frozen, except (b)'s solution: R3's change (`@cor-refuting-row` → plain "Chapter 4"), plus two words for G10 (§4.1, item 11) | ch04 08:13, 08:510 |
| `exr-finding-derivations-c3` | 01:1033 | kept (exit check); step 6's pointer reworded (R3) | — |
| `exr-finding-derivations-c4` | 01:1092 | kept | — |
| `exr-finding-derivations-r1` | 01:1145 → **3.3** | moved verbatim | — |
| `exr-finding-derivations-r2` | 01:1161 → **3.3** | moved verbatim | — |
| `exr-finding-derivations-r3` | 01:1201 → **3.3** | moved; solution reworded (R3; G10 wording, §4.3 item 13); stem's second question reworded as derive-or-break (S2 round 1) | — |

The prefix `finding-derivations` of the three R labels is **not** "fixed" in 3.3 (layout §1.4's last paragraph).

The heading ids of 3.1 that other chapters cite in prose stay unchanged: "The rules in one place" (ch04 07:37, ch05 07:284) and "A search that fails" (ch04 07:3, 07:278). Only `01:466`'s paragraph changes, by R3's rewrite plus one sentence (§4.1, item 8).

### 3.2 New labels (29; grep of `fd1/src`, `fd2/src`, `fd3/src`, `fd4/src`, `an1/src` on 2026-10-13 finds none)

| § | Label | Kind | Main line or fold |
|---|---|---|---|
| 3.1 | `exr-finding-derivations-a2` | drill bank (planned by R3 §4.6; 12 parts here) | exercises |
| 3.1 | `exm-search-free-lines` | worked search | main |
| 3.1 | `exr-finding-derivations-b4` | B item | exercises |
| 3.2 | `def-inconsistent-set` | definition (minor: STYLE §3 steps 4, 7, 8) | main (layout-fixed name) |
| 3.2 | `prp-inconsistent-derives-everything` | proposition (proof folded, STYLE §12.12) | main statement, fold proof (layout-fixed) |
| 3.2 | `prp-derivable-iff-negation-inconsistent` | proposition (proof folded) | main statement, fold proof (layout-fixed) |
| 3.2 | `exm-theorem-search` | worked search | main |
| 3.2 | `exm-equivalence-search` | worked search | main |
| 3.2 | `exm-inconsistency-search` | worked search | main |
| 3.2 | `exm-inconsistent-lists` | gallery | main |
| 3.2 | `exm-derive-or-break-search` | worked search, two claims | main |
| 3.2 | `exr-four-kinds-of-task-a1`, `-a2`, `-b1`, `-b2`, `-b3`, `-b4`, `-c1`, `-c2` | exercises (B3, C2 "used later") | exercises |
| 3.3 | `exm-extract-argument` | worked example | main |
| 3.3 | `exm-two-columns` | worked example | main |
| 3.3 | `exr-from-argument-to-derivation-a1`, `-b1`, `-b2`, `-b3`, `-b4`, `-c1`, `-c2`, `-r4` | exercises (`-r4` new R item) | exercises |

Notes on the table:
- "29" counts the 11 new labels on the main line and the 18 new exercise labels: `exr-finding-derivations-a2` and `-b4`, eight `exr-four-kinds-of-task-*` and eight `exr-from-argument-to-derivation-*`.
- No new `thm-` or `lem-` label. No `def-` label beyond `def-inconsistent-set`: "theorem of logic" is defined in the text by `def-derivable`'s notation \( \vdash \varphi \), and no `def-theorem` is added, since that name would collide in meaning with every volume's theorems.
- No `def-satisfiable-set` and no `def-semantically-consistent` (Critic C1; layout §1.4).
- The library of 3.3 is an unlabelled subsection; its heading id `a-library-of-standard-sequents` may be cited, for instance by 6.3's first-order library.
- The drafter greps again before creating each label (DRAFTING, "Labels").

### 3.3 Bookkeeping (coordinator, S4)

- **`fd1/authoring/ledger/ch03.yaml`**:
  - new entries for the 29 new labels and their Quick checks;
  - the three R items change file (`01-…` → `03-…`) with their verdicts carried where the hash is unchanged (R1, R2), while R3 goes stale (solution reworded) and is re-reviewed;
  - `exr-finding-derivations-c2` goes stale (solution, two words) and is re-reviewed;
  - every item that R3 changes goes stale as R3 §3.3 already foresaw;
  - `ledger.py init 3` is run at S4.
- **`fd1/verify/ch03/`**:
  - **new sidecars:**
    - `exm-inconsistency-search.py`: the four conditions for \( -200 \le n \le 200 \); no \( n \) meets all four; every three are met, by \( n = 6, 1, 3, 12 \) (§9, item 9);
    - `exr-four-kinds-of-task-b3.py`: each of the nine claims checked by truth table; each break at its stated number;
    - `exr-four-kinds-of-task-b4.py`;
    - `exr-four-kinds-of-task-c1.py`: the break of (d) at \( x = 1 \);
    - `exm-derive-or-break-search.py`: (b) at \( x = 2 \);
    - `exm-extract-argument.py`: F1–F3 for \( -500 \le n \le 500 \), and the reasons "the only even prime is 2", "the only prime multiple of 3 is 3";
    - `exr-from-argument-to-derivation-b1.py`: (a) on a grid; (c) \( ab = 0 \), \( a \ne 0 \Rightarrow b = 0 \);
    - `exr-from-argument-to-derivation-b3.py`: items 11, 13 and 15 at \( n = 2, 15, 25 \); every sequent of 1–15 by truth table;
    - `exr-from-argument-to-derivation-b4.py`: the fact \( a \le 1 \wedge b \le 1 \Rightarrow a + b \le 2 \) on a grid;
    - `exr-from-argument-to-derivation-c1.py`: (e) at \( n = 2 \);
    - `exr-from-argument-to-derivation-r4.py`: the three facts on a grid of reals;
  - **updated:** `exr-finding-derivations-r*.py` move with their items (paths unchanged; the directory is per chapter);
  - **for every sidecar:** every derive verdict is also checked valid by truth table, and every typeset derivation passes `check_fitch.py`.
- **`authoring/STATUS.md`**: the rows of §6.
- **`authoring/NOTATION.md`**: the *consistent* row says "F1.2's new section on inconsistent sets, `def-inconsistent-set`, planned". It becomes "F1.7 §02, `def-inconsistent-set`". This is a coordinator edit; it changes no meaning.

---

## 4. Per-section plans

Budgets: **main line** = prose words by `tools/check_structure.py`'s `prose_words`, outside `.second-reading` folds and before `## Exercises` (math spans count one word; raw LaTeX does not count). "Now" for 3.1 was measured on `01-finding-derivations.md` at `034a2ae`: 4,652 words, of which "The method" 876, "The rules in one place" 481, "A mathematical goal" 457. Every new main-line derivation of four or more lines gets two snapshots (STYLE §12.4), unless this file names an exemption.

### 4.0 `index.md` (replaces the placeholder; written last, against the delivered sections)

**Budget:** ≤ 1,000 words. Expected about 975: story ~200, What you need ~110, Time ~30, Minimum ~25, Roadmap ~110, Named moves ~245, Summary ~170, Terms ~120. No fold.

1. **Story** (new, ~200 words; replaces index:3).
   - Chapters 1 and 2 gave a rule for using and a rule for proving every connective, and a derivation can be checked line by line with no idea at all. Finding one is another matter: an assumption may be any statement, and every Idea so far found its derivation with a handful of moves.
   - Then the motivating question, in italics, verbatim (§0).
   - The chapter answers it in three steps:
     - Section 3.1 puts the moves in order as a method, says why the order loses nothing, and watches it succeed and fail;
     - Section 3.2 shows that the **task** shapes the search, and names the syntactic idea behind them all, an **inconsistent** list, one that derives \( \bot \);
     - Section 3.3 starts from a paragraph of mathematics instead of a sequent.
   - Closing sentence: "The chapter ends on a question its methods cannot answer: a search that fails proves nothing, so how could anyone show that something is **not** derivable?" (No chapter named here; the Looking-ahead box of 3.3 names Chapter 4.)
2. **What you need** (~110 words). "Chapters 1 and 2: the rules for every connective; derivations with boxes and the scope rule (@def-derivation); derived rules (@def-derived-rule) and @lem-weakening-cut; the classical rules of Section 2.5; and from Section 1.1 the counterexample set (@def-counterexample-set) and the move *try to break it*."
3. **Quantifier note** (one sentence, part of What you need). "Steps about 'every' and 'some', such as 'say \( m = 2k \)', are used as ordinary reasoning, as in Chapter 2, until Chapter 5 gives them their rules." This replaces, for Chapter 3, the per-proof caveats that R3 cut (`01:487`, A1(b)'s solution). It carries STATUS row "F1.7 §01 quantifier steps" (§6).
4. **Time** (one line). Recomputed by the drafter from the delivered text (§5). Expected: "**Time.** About 15 hours on the core track (all of A, one B and one C per section, the exit checks); about 25 hours for everything."
5. **Minimum for fd2** (one line, layout G14). "**Minimum for fd2.** Chapters 1–6 and 8, core; Chapter 7 (Sections 7.1–7.2) before *Sets, Relations, and Cardinality*, Chapter 3."
6. **`## Roadmap`** (three bullets, one or two sentences each).
   - **How to Find a Derivation.** The moves of Chapters 1 and 2 put in order as one method, the reason the order loses nothing, four refinements including the detour rule, searches that succeed and one that fails, and every rule on one card.
   - **Four Kinds of Task.** Theorems, equivalences, inconsistent lists and claims whose verdict is withheld: how each task starts its search, and why all four are one question about whether a list derives \( \bot \).
   - **From Argument to Derivation.** Extracting the argument from a paragraph, naming the facts it leaves unsaid, writing a proof and its derivation side by side, and a library of standard sequents grouped by what they are for.
7. **`## Named moves`** (nine, in order, each one line with its section):
   - **Work from both ends.** The method: read the skeleton off the goal, use the resources by their main connectives, keep the classical step for last. (Section 3.1)
   - **Find the goal among the resources.** If the current goal is already available, cite it or copy it by \( \rulename{R} \). (Section 3.1)
   - **Derive what needs nothing new before opening a box.** Lines written outside the boxes are available in all of them. (Section 3.1)
   - **Look first for a clash partner already on a line.** For the goal \( \bot \), aim at the statement whose negation you already have. (Section 3.1)
   - **No detours.** Never build a line by an introduction rule and take it apart at once by the matching elimination. (Section 3.1)
   - **Let the task choose the search.** A theorem starts at the goal, an equivalence needs two derivations, an inconsistency aims at a clash. (Section 3.2)
   - **Try to break it first.** Before searching, try to make the counterexample set true. An attempt that is forced into a clash at every turn is usually a derivation read backwards: its forced statements suggest the boxes, and its clash the \( \bot \). (Section 3.2)
   - **Name the unstated fact.** An argument in prose leaves premises unsaid; write each one down and check it. (Section 3.3)
   - **Two columns.** Write the proof beside the derivation it mirrors, and see which lines the prose leaves silent. (Section 3.3)
8. **`## Summary`** (new, ~170 words, STYLE §12.13.5). Points, in five to seven sentences:
   - The search method reads boxes off the goal and eliminations off the resources, and its goal steps and its classical step never turn a derivable gap into one that is not (Section 3.1's fold).
   - Postponing \( \vee \) and the four refinements make it efficient.
   - Every task is a question about derivability, and every question about derivability is a question about whether a list is **inconsistent** (@prp-derivable-iff-negation-inconsistent): proving \( \varphi \) from \( \Gamma \) is showing the counterexample set \( \Gamma, \neg\varphi \) inconsistent.
   - An inconsistent list proves everything (@prp-inconsistent-derives-everything).
   - Arguments in prose become sequents once their unstated facts are named.

   **What is open** (closing paragraph, two sentences, not titled): every method of the chapter can show that something **is** derivable, and none can show that something is **not**; a claim that breaks, or a search that stalls, has not been shown underivable. "That is Chapter 4's question." (This is a plain pointer in the index; the promise is the 3.3 box.)
9. **`## Terms`** (new, ≤ 130 words): alphabetical, one line each, every entry linked, at most nine words of gloss.
   - **consistent list**: a list from which \( \bot \) is not derivable (@def-inconsistent-set).
   - **counterexample set** (recalled): the premises together with the negated conclusion (@def-counterexample-set).
   - **current goal**: the written line below a gap (@def-partial-derivation).
   - **gap**: a stretch of a partial derivation still missing (@def-partial-derivation).
   - **inconsistent list**: a list from which \( \bot \) is derivable (@def-inconsistent-set).
   - **partial derivation**: a derivation with gaps still to fill (@def-partial-derivation).
   - **provably equivalent** (recalled): each derivable from the other (@def-provable-equivalence).
   - **resources**: the lines available at a gap's current goal (@def-partial-derivation).
   - **theorem (of logic)**: a statement derivable from no premises, \( \vdash \varphi \) (@def-derivable).

### 4.1 Section 3.1: How to Find a Derivation (`01-finding-derivations.md`)

**Purpose.** To turn the moves of Chapters 1 and 2 into one method with an order, to say why the order loses nothing, and to watch it work and fail. **Kind:** M (moved from 2.6) and E (expanded). **Budget:** main line ≤ 5,000 (now 4,652). Expected about 4,993, by this tally (corrected at S2 round 1 and updated at round 2; the S1 tally summed to 5,045, omitted items 2 and 5, and under-counted the refinements subsection):
- R3's own estimate ≈ 4,870;
- refinements subsection ≈ 479 (itemised in item 7: lead 29, three moves 135, `exm-search-free-lines` 140, its Quick check 40, the detour paragraph's main-line part 95, its Quick check 40; S2 round 2 added 4 words to the lead and a net 5 to the detour paragraph);
- figure lead ≈ 42 (S2 round 2: the two termination sentences, item 3);
- `01:466` +15;
- item 2's new sentence +25;
- item 5's Peirce pointer +17;
- R3's Looking-ahead box −40, moved to 3.3;
- Peirce passage to a fold −115;
- other splits to a fold −100;
- R3's three bullets trimmed to lead-in plus one sentence each −60, R3's own fallback, now taken in advance;
- **trims 1, 2 and 4 of the S1 trim order, now taken in advance:** the 13-row card's Lean sentence (−20); 01:186's second sentence (−25); the Givens/Goal table of `exm-skeleton-odd-product` (−95), moved verbatim into fold F3.1-g (item 9).

That is 4,870 + 479 + 42 + 15 + 25 + 17 − 40 − 115 − 100 − 60 − 140 = 4,993 (S2 round 2; 4,967 at round 1).

Folds ≤ 975 (expected ~955: F3.1-a 68, F3.1-b ~315, F3.1-c ~115 plus snapshots, F3.1-d ~100, F3.1-e ~160, F3.1-f ~100, F3.1-g ~95).

**Trim order if the delivered count still exceeds 5,000:**
1. `exm-search-free-lines`'s closing comparison sentence (−25);
2. the refinements lead's last sentence (−10);
3. the first refinement's illustrating sentence ("Step 2 would open a box …", −25).

No forward pointer remains on the main line (the Looking-ahead box moves to 3.3; see item 8).

**What the section teaches, in the order of the file.** Items 1–11 are R3 §4.6's items 1–11 as written, except where noted. New material is marked **new**.

1. **Opening** 01:3: kept (R3 item 1).
2. **`## The moves so far`** 01:5–23: R3 item 2, executed: two rows added ("resource \( \neg\varphi \)", "resource \( \varphi \leftrightarrow \psi \)"), and "Eleven moves" becomes "Thirteen moves". **New, one sentence** appended to 01:23's replacement (~25 words): "Every assumption a search opens says, in its justification column, which move opened it: 'asm, for →I' is the goal step for \( \to \), 'asm, for ∨E' the resource step for \( \vee \), 'asm, for RAA' step 5." [D1]
3. **`## Partial derivations`** and **`## The method`**: R3 items 3 and 4, executed.
   - The bullets are trimmed in advance to their bold lead-ins plus one sentence each. Kept sentences:
     - "Step 2 loses nothing: if a gap with the goal \( \psi \to \chi \) can be filled at all, so can the gap inside a box on \( \psi \) with the goal \( \chi \)."
     - "Choosing a side of \( \vee \) can leave a goal that does not follow: from \( P \vee Q \), with \( P \) true and \( Q \) false, the step to \( Q \) breaks."
     - "Step 5 loses nothing either, and still comes last: the goal \( \bot \) gives step 2 nothing to work with, and a good statement to split on must be chosen."
   - Fold F3.1-b (R3's F2.6-b, renamed) follows them.
   - **New: Figure 3.1-F**, the method as a flowchart, placed after the bullets and fold and before the Quick check 01:80. [Technique: Hu (flowcharts for decision methods); the chart grows Section 1.6's chart (07:936) to every connective.]
     - Lead (~42 words; S2 round 2): "The same method as a chart. A move counts only if the gap it makes is not already open above it, with the same goal and resources. When no move is left, go back to the gap that made this one."
     - Template `flowchart`, laid out as 1.6's chart (tests down the left, actions to the right, a return line on the far right to a merge point under the start).
     - Nodes:
       - (s) `fc start` "a gap: its goal\\and its resources";
       - (t0) `fc test` "is the goal\\a resource?";
       - (e0) `fc start` "done: cite it,\\or copy it by R";
       - (t1) `fc test` "is the goal a $\wedge$, $\to$,\\$\neg$ or $\leftrightarrow$?";
       - (b1) `fc step` "step 2: its introduction\\rule (boxes or two gaps)";
       - (t2) `fc test` "can a resource be taken apart\\by a move untried for this gap?";
       - (b2) `fc step` "step 3: its elimination rule\\($\vee$E: both boxes end in the goal)";
       - (t3) `fc test` "is the goal $\bot$, or do the\\resources clash, with a clash\\untried for this gap?";
       - (b3) `fc step` "step 4: find or build\\the clash; $\bot$E if needed";
       - (t4) `fc test` "is RAA on this goal, or LEM on\\a statement a resource waits for,\\still untried for this gap?";
       - (b4) `fc step` "step 5: RAA on the goal\\(not $\bot$), or LEM\\on that statement";
       - (e4) `fc start` "no move left: back to the gap\\that made this one; at the first\\gap, stop and try to break the claim".
     - Arrows:
       - s→t0;
       - each test –yes→ its action;
       - t0 –no→ t1 –no→ t2 –no→ t3 –no→ t4 –no→ e4;
       - b1, b2, b3, b4 return to the merge point above t0 (one line on the right, as in 07:936).
     - Caption sentence after the figure (counted in the 25): none beyond the lead.
     - The disjunctive goal goes "no" at t1, so step 2 postpones it, as the algorithm says.
     - **Termination (decided at S2 round 2; replaces round 1's "not yet used").** Three rules, all on the page (the lead's two sentences and the words "untried for this gap" in t2, t3, t4):
       - *A gap* is a goal with its resources. A move whose new gap has the same goal and the same resources as a gap still open above it (the current gap included) is not a move: the chart skips it. This replaces "a goal already being sought is not new", which is too strong: inside an RAA box on \( \neg(P \vee Q) \), aiming at \( P \vee Q \) is the right move (3.2 B3 (i), and \( \vdash P \vee \neg P \)), and there the resources differ by the assumption.
       - *Untried for this gap*: each move is tried at most once in a gap. ∧E on a line already taken apart, a LEM split whose case adds a statement already a resource, and RAA on the goal \( \bot \) (its box would seek \( \bot \) again; b4 says "not \( \bot \)") are not moves.
       - *t4's candidates are bounded*: RAA on the current goal, and LEM only on a statement some resource waits for (the antecedent of \( \to \), a side of \( \leftrightarrow \), the \( \chi \) of a resource \( \neg\chi \)). This is step 5's "a well-chosen statement" made finite, and it is what 01:462's failed search does (LEM on \( P \), then on \( Q \)).
       - *Back up*: a gap with no move left returns to the gap that made it, where that move now counts as tried; at the first gap, e4 stops the search. This is step 5's "try the same with a goal further out" and fold F3.1-c's Peirce search.
       - Why it ends (for S2a, not for the text): every statement in any gap is a part of the claim or the negation of one, so there are finitely many gaps; on any route resources only grow and no gap repeats one open above it; so every route is finite, and the search is a finite tree. §9 item 9 gives the run on \( P \to Q \vdash Q \to P \).
     - This chart reads the algorithm's **order**. The table of moves reads **situations**. R3 §9 D9's objection was to a second decision chart duplicating the table; this one does not (§10 records the supersession).
   - Quick check 01:80–93 kept.
4. **`## Splitting the goal`**, **`## Cases must end in the goal`**, **`## Postponing a disjunction`**: R3 items 5, 6 and 7, executed. Two further changes:
   - In `exm-search-postpone-or`, 01:344's last two sentences ("\( \rulename{LEM} \) on \( P \), the first split one thinks of, also succeeds, but less well: … 22 lines against these 14.") move verbatim to fold F3.1-d (item 6).
   - The dead-end snapshot 01:263–284 gains `\purpose{\ii}` on line 2's assumption and `\purpose{\oe}` on the two case assumptions (binding rule 8).
5. **`## When nothing else works`**: `exm-search-raa` kept (R3 item 8's first sentence).
   - 01:436's last sentence ("A split by \( \rulename{LEM} \) on \( P \) also works, but less well: … stuck there a second time.") moves verbatim to fold F3.1-d.
   - R3 item 8's rewrite of 01:439 (Peirce's search, two snapshots and its Quick check) is executed as R3 wrote it, **and then placed verbatim in fold F3.1-c** `title="Step 5 one level out: the search for Peirce's law"`. Its lead sentence keeps its pointer to @prp-peirce in Section 2.5's fold.
   - One main-line sentence remains in its place (~17 words, new): "Step 5's advice to try a goal further out is shown on Peirce's law in the fold below."
   - The fold test holds: the algorithm states the advice on the main line, and no A or B item needs the fold.
6. **New: fold F3.1-d** `title="Other splits that also work"` (~100 words, verbatim moves only). It is placed after `exm-search-raa`'s solution, before F3.1-c, and holds 01:344's last two sentences and 01:436's last sentence. Each moved passage is led by the bold name of its example (`**In @exm-search-postpone-or.**`, `**In @exm-search-raa.**`); the lead-ins add 6 words. Moving them is not a change (STYLE §12.0).
7. **New: `## Four refinements`** (new subsection after "When nothing else works" and its folds, before "A search that fails"; ≈ 470 words with two Quick checks, itemised in the budget). [Technique: LB (find the goal in the premises; derive before opening a box; a clash partner already on a line); vD (the detour rule, stated without proof).]
   - **Lead** (~29 words): "The method finds a derivation; these four refinements usually find a shorter or more direct one. Each fits into one step, and none changes what the method can find." (S2 round 2: "usually … or more direct", because cutting a detour can cost a line, 3.3 C2 (a) and gallery row 2.)
   - **The three moves**, as a bold-lead-in list, one or two sentences each (~135 words):
     - "**Find the goal among the resources.** Before step 2, ask whether the current goal is already available; if so, cite it, or copy it into the current box by \( \rulename{R} \). Step 2 would open a box for a goal \( P \to Q \) that is already a premise, and write three lines where none is needed."
     - "**Derive what needs nothing new before opening a box.** \( \rulename{\wedge E} \) on a resource, and \( \rulename{{\to}E} \) or \( \rulename{{\leftrightarrow}E} \) when both of their lines stand, may be written at once, above the boxes the goal asks for: a line outside the boxes is available inside all of them, so it is written once instead of once per box." (\( \rulename{\vee E} \) is not such a step: it opens boxes.)
     - "**Look first for a clash partner already on a line.** When the goal is \( \bot \), scan the resources for a negation \( \neg\chi \) whose \( \chi \) is cheap, or for \( \chi \) and \( \neg\chi \) both in reach, before manufacturing anything (step 4)." (Illustrated on the main line by `exm-inconsistency-search` in 3.2 and by 3.2 C1 (b), which cite this refinement by name; 3.1's own example illustrates the first two.)
   - **`exm-search-free-lines`** `[Lines that need nothing new]` (~140 words of prose). **Rebuilt at S2 round 1** (option (b) of the finding): the S1 version split \( \neg Q \vee R \) by \( \rulename{\vee E} \) above the boxes, a move neither the method (step 3 ends both boxes in the current goal) nor the refinement (which excludes \( \rulename{\vee E} \)) allows. Now only \( \rulename{\wedge E} \) and \( \rulename{{\to}E} \) lines go above the boxes.
     - Statement: "Find a derivation of \( P \wedge (P \to Q), \ Q \to R \vdash (S \to R) \wedge (T \to (Q \wedge R)) \)."
     - *Search*:
       - The goal is a conjunction of two implications, so step 2 will open a box on \( S \) and a box on \( T \). Before it does, the resources give lines that need nothing new: \( P \) and \( P \to Q \) by \( \rulename{\wedge E} \), then \( Q \) by \( \rulename{{\to}E} \), and then \( R \) by \( \rulename{{\to}E} \) on the second premise.
       - With \( Q \) and \( R \) outside every box, the two boxes are short. In the box of \( S \) the goal \( R \) is a resource, copied by \( \rulename{R} \). In the box of \( T \), \( \rulename{\wedge I} \) joins \( Q \) and \( R \).
     - **Snapshot S1** (`% schema (partial derivations: …)`):
       - 1 \( P \wedge (P \to Q) \) and 2 \( Q \to R \), premises;
       - gap;
       - 13 \( (S \to R) \wedge (T \to (Q \wedge R)) \), unjustified.
     - **Snapshot S2:**
       - lines 1–2 as in S1;
       - 3 \( P \), ∧E 1; 4 \( P \to Q \), ∧E 1; 5 \( Q \), →E 4, 3; 6 \( R \), →E 2, 5;
       - 7 | \( S \), asm `\purpose{\ii}`; gap; 8 | \( R \), unjustified;
       - 9 \( S \to R \), →I 7–8;
       - 10 | \( T \), asm `\purpose{\ii}`; gap; 11 | \( Q \wedge R \), unjustified;
       - 12 \( T \to (Q \wedge R) \), →I 10–11;
       - 13 ∧I 9, 12.

       (Lines 7 and 10 carry `\purpose` because 8 and 11 are unjustified. Their boxes are closed by justified lines, but S4's `--purposes` run accepts the hand annotation either way.)
     - **Finished derivation (13 lines):** S2 with 8 \( R \), R 6, and 11 \( Q \wedge R \), ∧I 5, 6.
     - *Closing sentence* (the first trim candidate): "Opened first, each box would have to repeat lines 3–6, and the derivation would have 16 lines instead of 13." (Count: box of \( S \): asm, \( P \), \( P \to Q \), \( Q \), \( R \) = 5 lines; box of \( T \): asm, \( P \), \( P \to Q \), \( Q \), \( R \), \( Q \wedge R \) = 6 lines; plus 2 premises, 2 →I lines and the ∧I line = 16.)
   - **Quick check (new, ~40 words):** "In @exm-search-free-lines, which refinement does line 8 use, and which do lines 3–6 use?" *Solution:* Line 8 finds the goal \( R \) among the resources (line 6) and copies it into the box of \( S \). Lines 3–6 need nothing new and are written before any box opens, so both boxes can use them.
   - **No detours** (~90 words on the main line), a bold-lead-in paragraph:
     - "**No detours.** Never build a line by an introduction rule and then, at once, take that line apart by the matching elimination. The line the pair produces was within reach without it."
     - One sentence (S2 round 1): "This includes \( \rulename{\neg I} \) followed by \( \rulename{\neg E} \) on the negation it built." (Ruling: a ¬I line used as the **negation** premise of ¬E is a detour; used as the other premise, as in a manufactured clash, it is not.)
     - One sentence: "A manufactured clash is not a detour: \( \rulename{\vee I} \) followed by \( \rulename{\neg E} \) against \( \neg(\varphi \vee \psi) \) uses the new line with a different connective."
     - One sentence (reworded at S2 round 2): "The book uses this as advice, not as a theorem: a detour is legal, and cutting one need not shorten a derivation, since an introduced line cited elsewhere stays." (The clause "the line it makes was within reach without it" is dropped here: the paragraph's second sentence already says it. The length clause is now on the main line, so 3.3 C2 (a)'s solution and gallery row 2 cite a sentence the reader has seen. Net +5 words.)
   - **New: fold F3.1-f** `title="Why a detour's line was within reach"` (~100 words; right after the detour paragraph, before its Quick check). Moved off the main line at S2 round 1 for the budget. The fold test holds: the main line states the rule; A2 (i) and B4 (a)–(c) need only the rule, and B4 (d)'s stem says what is copied. Content, one sentence each:
     - After \( \rulename{\wedge I} \) joins lines \( i \) and \( j \), \( \rulename{\wedge E} \) on the new line gives back \( i \) or \( j \).
     - After \( \rulename{{\to}I} \) closes a box from \( \varphi \) to \( \psi \), \( \rulename{{\to}E} \) on the new implication and a line \( \varphi \) gives \( \psi \). The box's lines, copied with that line in place of the assumption, give \( \psi \) directly.
     - After \( \rulename{\neg I} \) closes a box from \( \varphi \) to \( \bot \), \( \rulename{\neg E} \) on the new negation and a line \( \varphi \) gives \( \bot \); the box's lines, copied likewise, give \( \bot \) directly.
     - After \( \rulename{\vee I} \) builds \( \varphi \vee \psi \) from \( \varphi \), \( \rulename{\vee E} \) on it gives what its first case gives, which the first case's lines, copied with the line \( \varphi \) for the assumption, give directly.
     - Closing clause: every copied citation stays legal by the scope rule of @def-derivation, since the line put in place of the assumption stands above the copy.
   - **Quick check (new, ~40 words):** "Lines 2 and 3 are \( P \) and \( R \); line 4 is \( P \wedge R \), ∧I 2, 3; line 5 is \( R \), ∧E 4. Which refinement does this break, and what should line 5 cite instead?" *Solution:* No detours. Lines 4–5 build a conjunction and take it apart at once; line 5's statement is line 3, so cite line 3, or copy it by \( \rulename{R} \) where it must lie in the current box.
8. **`## A search that fails`**: R3 item 9, executed: the table, the close, the Quick check, 01:464 kept, and 01:466's rewrite.
   - **New, one sentence** appended to R3's rewrite of 01:466 (~15 words): "Section 3.2 gives this question a sharper form, and the chapter ends on it."
   - R3 item 12's Looking-ahead box is **not** placed here: its content moves to 3.3 (§4.3, item 9). This follows layout §1.3: "3.3's Looking-ahead box carries the question 'how could we show something is *not* derivable?', and Chapter 4's index opens with it."
   - Ch04 01:3 ("Chapter 3 ended on a question …") and 07:3 ("Chapter 3 ended on a question it could not answer. Section 3.1 searched …") stay true.
9. **`## A mathematical goal`**: R3 item 10, executed. Warning 01:490–492 kept.
   - **New: fold F3.1-g** `title="The givens and the goal"` (~95 words, verbatim move only; S2 round 1, the S1 trim 4 taken in advance). R3's Givens/Goal table for `exm-skeleton-odd-product` moves, verbatim, into this fold, placed right after the example's solution. One main-line clause stays where the table stood (counted in the tally as part of the −95): "The givens and the goal are tabulated in the fold below." Moving it is not a change (STYLE §12.0). The fold test holds: no A or B item cites the table.
   - **New: fold F3.1-e** `title="Logic permits; it does not choose"` (~160 words; after the warning 01:490–492, before "The rules in one place"). [Technique: Co (Harman's remark that logic licenses but does not choose), told in fd1's own words; no name.] Content:
     - A derivation of \( \Gamma \vdash \varphi \) says that whoever accepts every member of \( \Gamma \) is committed to \( \varphi \). It does not say that \( \varphi \) should now be believed.
     - If \( \varphi \) is plainly false, say \( 0 = 1 \), the derivation is a reason to give up a member of \( \Gamma \), and it does not say which. A mathematician who derives \( 0 = 1 \) from the hypotheses of a lemma has learned that those hypotheses cannot hold together; Section 3.2 calls such a list inconsistent, and a proof by contradiction is built to reach exactly that.
     - In the other direction, at every gap the rules permit far more lines than any search writes: \( \rulename{\wedge E} \) on every conjunction, \( \rulename{\vee I} \) with any statement at all. The rules choose none of them. "The method chooses, and the method is advice, not logic: two searchers may find two different derivations, and both are correct."
     - (Within-chapter pointer only; no forward chapter named.)
10. **`## The rules in one place`**: R3 item 11, executed. That gives the 13-row card, the schemas 01:496–655 kept, the derived-rules table 01:657–685 kept, and the decision-chart sentence. That sentence gains four words: "…; Figure 3.1-F puts the method's order in a chart." The warning 01:687–689 is kept.
11. **Exercises.**
    - **A1**: kept (R3: (b)'s parenthetical cut).
    - **A2: Drill** (`exr-finding-derivations-a2`, new label planned by R3). Twelve parts in the ramp, with R3's letters in brackets:
      - *One step: what does the method write?*
        - (a) [a] The goal is \( \neg(P \vee Q) \). What does step 2 set up? — A box opened with \( P \vee Q \), with the goal \( \bot \).
        - (b) [b] The goal is \( (P \to Q) \wedge \neg R \). Which gaps does step 2 leave? — Two boxes: one on \( P \) with the goal \( Q \), and one on \( R \) with the goal \( \bot \).
        - (c) [d] The goal is \( \bot \), and the resources are \( \neg(P \wedge Q) \), \( P \), \( Q \). What are the next two lines? — \( P \wedge Q \) by ∧I, then \( \bot \) by ¬E.
        - (d) [c] The goal is \( P \vee Q \), and the one resource is \( \neg P \to Q \). Which step does the work, and how? — Step 2 postpones the goal. Step 3 cannot fire, since it needs \( \neg P \). So step 5: LEM on \( P \), the statement the resource waits for.
      - *Which lines are available?*
        - (e) [e] In a partial derivation the current goal is line 9, inside the boxes opened at lines 3 and 6. Line 1 is a premise, and lines 4–5 form a box inside box 3 that has closed. Which of lines 1, 3, 4, 6 are resources? — 1, 3 and 6; not 4.
      - *Recall.*
        - (f) [f] Which step of the method opens an RAA box, and when? — Step 5, when steps 2–4 give nothing.
      - *Is this correct?*
        - (g) [g] True or false: a failed search shows that the sequent is not derivable. — False: it shows only that this search failed.
        - (h) [h] The goal is \( R \), and the resources are \( P \vee Q \), \( P \to R \), \( Q \to S \). Should the search be expected to succeed? — No. \( P \) false, \( Q \) true, \( R \) false, \( S \) true makes every resource true and \( R \) false, so the claim breaks. In ∨E, the case \( Q \) gives only \( S \).
        - (i) **new** Lines 3 and 4 are \( Q \to R \) (a premise) and \( Q \). A searcher writes 5 | \( Q \), asm; 6 | \( R \), →E 3, 5; 7 \( Q \to R \), →I 5–6; 8 \( R \), →E 7, 4. Which refinement of the section does this break, and what single line replaces lines 5–8? — Two refinements. Lines 7–8 are a detour (→I, then →E on its own implication). Line 7 rebuilds a resource, and *find the goal among the resources* would have cited line 3. Replace lines 5–8 by 5 \( R \), →E 3, 4. (Not the B4 derivation, and not the Quick check's ∧-detour.)
      - *Derivations.*
        - (j) [i] Find a derivation of \( P \vee Q, \ \neg P \vdash Q \vee R \). — 3 \( Q \), DS 1, 2; 4 \( Q \vee R \), ∨I 3.
        - (k) [j] Find a derivation of \( (P \vee Q) \to R \vdash Q \to R \). — 2 | \( Q \); 3 | \( P \vee Q \), ∨I 2; 4 | \( R \), →E 1, 3; 5 \( Q \to R \), →I 2–4.
        - (l) [k] Find a derivation of \( P \to (Q \to R), \ P \wedge \neg R \vdash \neg Q \). — 3 \( P \), ∧E 2; 4 \( \neg R \), ∧E 2; 5 \( Q \to R \), →E 1, 3; 6 \( \neg Q \), MT 5, 4.
    - **B1** (frozen), **B2** (scaffolded; the faded triple's middle), **B3**: kept.
    - **B4** (new) `[B4: Cut the detours]`. [Technique: vD (detours); Hu (find what is wrong in a legal derivation).]
      - Stem: "The derivation below of \( P \wedge Q, \ Q \to R \vdash R \wedge P \) is correct but contains detours. (a) Find each pair of lines in which a line is built by an introduction rule and taken apart at once by the matching elimination. (b) Which line rebuilds a premise? (c) Rewrite the derivation without the detours. (d) To cut the →I/→E detour, the box is copied with a line in place of its assumption: which line, and what does the copy give?"
      - The derivation (11 lines; a raw `nd` block; it passes `check_fitch.py`): 1 \( P \wedge Q \); 2 \( Q \to R \); 3 \( Q \), ∧E 1; 4 | \( Q \), asm; 5 | \( R \), →E 2, 4; 6 \( Q \to R \), →I 4–5; 7 \( R \), →E 6, 3; 8 \( P \), ∧E 1; 9 \( R \wedge P \), ∧I 7, 8; 10 \( R \), ∧E 9; 11 \( R \wedge P \), ∧I 10, 8.
      - *Answer:*
        - (a) Lines 6–7: →I, then →E on line 6. Lines 9–10: ∧I, then ∧E on line 9. (Line 11 then rebuilds line 9.)
        - (b) Line 6 is premise 2, rebuilt by a box. *Find the goal among the resources* would have cited line 2.
        - (c) 1 \( P \wedge Q \); 2 \( Q \to R \); 3 \( Q \), ∧E 1; 4 \( R \), →E 2, 3; 5 \( P \), ∧E 1; 6 \( R \wedge P \), ∧I 4, 5. That is six lines instead of eleven.
        - (d) Line 3 takes the place of the assumption on line 4. The box's one other line, "\( R \), →E 2, 4", becomes "\( R \), →E 2, 3", which is line 4 of (c).
      - Worked example type: "Four refinements", the detour paragraph and its Quick check.
    - **C1** (the faded triple's last), **C3** (exit check), **C4**: kept, with C3's step-6 pointer reworded per R3.
    - **C2** frozen, except (b)'s solution: R3's change (the `@cor-refuting-row` cut, plain "Chapter 4" kept), plus two wording changes for layout G10, both listed in S2a (§9, item 4):
      - "neither side is derivable from no premises" → "neither side follows from no premises";
      - "Chapter 4 turns such rows into proofs" → "Chapter 4 turns such choices into proofs". The word "row" is Chapter 4's, and Chapter 3 now precedes it.

      Ch04 08:13 and 08:510 cite only the derivation (13 lines), which is unchanged.
    - **R1, R2, R3**: **move to Section 3.3** (§4.3, item 13). Section 3.1 has no `### R. Review`, since the R group belongs to the chapter's last section (STYLE §6).

**Quick checks (main line):**
- first goals (kept);
- the moved resources check (R3);
- the failed-search table (R3);
- refinements (new);
- detours (new).

Five in ~4,990 words, about one per 1,000. Peirce's Quick check is in fold F3.1-c.

**Sidecars:** none new (every item is in letters); `exr-finding-derivations-a2.py` is not needed. **Ledger lines:** F3.1-e makes no mathematical claim beyond "0 = 1 is false". `exm-search-free-lines` has no facts. The detour's copying claims are argued in fold F3.1-f, from `def-derivation`'s scope rule: lines above a box stay available after it.

### 4.2 Section 3.2: Four Kinds of Task (`02-four-kinds-of-task.md`, new)

**Purpose.** To show that the **task** decides the shape of a search, and to name the syntactic idea under all four tasks: an **inconsistent** list, one from which \( \bot \) is derivable. With it, Chapter 1's counterexample set gets its second link: a claim is derivable exactly when its counterexample set is inconsistent. **Kind:** N. [Technique: LB, vD (inconsistency, Γ ∪ {¬φ} ⊢ ⊥ as the syntactic counterexample set); LB, LPL (task types; derive or refute, verdict withheld); Hu (flowchart); Sm, Le (deliberate failure shown).] **Sources in fd1:** plan §3.2 "2.7 Four Kinds of Task", first half; layout §1.3 row 3.2. None of the prose exists yet; everything below is **newly written**.

**Budget:** main line ≤ 4,600. Expected about 3,500:
- opening 150;
- four tasks 350;
- theorems 260;
- equivalences 380;
- inconsistent lists 1,000;
- the counterexample set, derived 250;
- one task in four costumes 290;
- derive or break 640;
- Looking ahead 55;
- small links 125.

Folds ≤ 350 (F3.2-a, the two proofs, ~280). One forward pointer, the Looking-ahead box (item 9). **Snapshots:** two each for the worked derivations of four or more lines, as listed; no exemption (S2 round 1 withdrew the one S1 claimed for `exm-equivalence-search` (⇒)).

**What the section teaches, in order.**

1. **Opening** (~150 words, no heading). Section 3.1's method answers one kind of question: here are premises, here is a conclusion, find a derivation. Mathematics asks others:
   - prove a statement from nothing;
   - show that two statements say the same;
   - show that some conditions cannot all be met;
   - decide whether a conclusion follows at all, when nobody says whether it does.

   Each changes where a search starts and what ends it. This section takes the four in turn, and finds that underneath they are one question.
2. **`## Four tasks, one method`** (~220 words, a table, and a Quick check). [Named move: *Let the task choose the search*.] A table, columns *Task* | *The claim* | *Where the search starts* | *What ends it*:
   - theorem | \( \vdash \varphi \) | step 2 on the goal; every resource is an assumption the goal asks for | the goal reached outside every box
   - equivalence | \( \varphi \dashv\vdash \psi \) (@def-provable-equivalence) | two searches, one from each side | two derivations
   - inconsistency | \( \Gamma \vdash \bot \) | step 4: the goal is \( \bot \); look for a clash partner already on a line | \( \bot \) outside every box
   - derive or break | \( \Gamma \vdash \varphi \)? (verdict withheld) | try to break it first | a derivation, or statements that make the counterexample set true

   Then two sentences: "Only the last task can end in 'no'. In the other three, a failed search leaves the question open, as Section 3.1's failed search did."

   **Quick check (new, ~50 words):** "Which task is each? (i) \( \vdash P \vee \neg P \). (ii) \( P \wedge Q \dashv\vdash Q \wedge P \). (iii) Show that \( P, \ \neg P \vee Q, \ \neg Q \) cannot all be accepted together. (iv) Does \( P \to Q, \ Q \vdash P \) hold?" *Solution:* (i) a theorem; (ii) an equivalence; (iii) an inconsistency, the claim \( P, \neg P \vee Q, \neg Q \vdash \bot \); (iv) derive or break. It breaks, as affirming the consequent (Section 1.3).
3. **`## Theorems`** (~260 words). **`exm-theorem-search`** `[A statement that implies a contradiction]`.
   - Statement: "Find a derivation of \( \vdash (P \to (Q \wedge \neg Q)) \to \neg P \)."
   - Reading, one sentence before the solution: "In words: a statement that implies a contradiction is false. Every proof that begins 'suppose \( P \)' and ends 'which is impossible' has this shape."
   - *Search.*
     - There are no premises, so step 1 writes only the goal.
     - Step 2 opens a box on \( P \to (Q \wedge \neg Q) \) with the goal \( \neg P \), and again a box on \( P \) with the goal \( \bot \).
     - Now there are two resources, both assumptions the goal asked for. Step 3 fires the first on the second, giving \( Q \wedge \neg Q \), and splits it by \( \rulename{\wedge E} \). Step 4 finds the clash.
   - **S1:** box 1 \( P \to (Q \wedge \neg Q) \), asm; gap; 7 | \( \neg P \), unjustified; 8 \( (P \to (Q \wedge \neg Q)) \to \neg P \), →I 1–7.
   - **S2:** box 1; box 2 \( P \), asm; gap; 6 \( \bot \), unjustified; 7 \( \neg P \), ¬I 2–6; 8 as before.
   - **Finished (8 lines):** 1 | \( P \to (Q \wedge \neg Q) \), asm; 2 | | \( P \), asm; 3 | | \( Q \wedge \neg Q \), →E 1, 2; 4 | | \( Q \), ∧E 3; 5 | | \( \neg Q \), ∧E 3; 6 | | \( \bot \), ¬E 4, 5; 7 | \( \neg P \), ¬I 2–6; 8 →I 1–7.
   - *Aftermath* (two sentences): "A theorem has no premises, so the goal does all the early work. Once proved, it is a derived rule with nothing above the line (@def-derived-rule): any derivation, from any premises, may write an instance of it, as derivations already write \( \rulename{LEM} \)."
4. **`## Equivalences`** (~380 words). **`exm-equivalence-search`** `[Proving a disjunction by refuting one side]`.
   - Statement: "Show that \( P \to (Q \vee R) \dashv\vdash (P \wedge \neg Q) \to R \)."
   - Reading, one sentence: "This is how mathematics proves a disjunction: to show that \( ab = 0 \) implies \( a = 0 \) or \( b = 0 \), assume \( ab = 0 \) and \( a \ne 0 \), and show \( b = 0 \). The equivalence says that this changes nothing."
   - *(⇒)* Idea, one sentence: the goal is an implication, so a box on \( P \wedge \neg Q \); \( \rulename{\wedge E} \) splits it; the premise fires on \( P \); and \( \rulename{DS} \) removes the refuted side.
     - Finished (7 lines): 1 \( P \to (Q \vee R) \); 2 | \( P \wedge \neg Q \), asm; 3 | \( P \), ∧E 2; 4 | \( \neg Q \), ∧E 2; 5 | \( Q \vee R \), →E 1, 3; 6 | \( R \), DS 5, 4; 7 \( (P \wedge \neg Q) \to R \), →I 2–6.
     - **S1:** 1 \( P \to (Q \vee R) \); box 2 \( P \wedge \neg Q \), asm `\purpose{\ii}`; gap; 6 | \( R \), unjustified; 7 \( (P \wedge \neg Q) \to R \), →I 2–6.
     - **S2:** 1; 2; 3 | \( P \), ∧E 2; 4 | \( \neg Q \), ∧E 2; 5 | \( Q \vee R \), →E 1, 3; gap; 6 | \( R \), unjustified; 7.
     - (S2 round 1: `ch01-revision.md` §1 item 4's classes (i)–(vi) do not cover a 7-line derivation that comes first and differs in shape from its partner, so both snapshots are written, as STYLE §12.4 asks. Raw LaTeX, +0 words.)
   - *(⇐)*
     - The goal is an implication: a box on \( P \) with the goal \( Q \vee R \), a disjunction, postponed (Section 3.1, step 2).
     - The premise waits for \( P \wedge \neg Q \). \( P \) is in hand, \( \neg Q \) is not, and nothing clashes. That is step 5, \( \rulename{LEM} \) on \( Q \), the statement the premise waits for.
     - In the case \( Q \), \( \rulename{\vee I} \) gives the left side. In the case \( \neg Q \), \( \rulename{\wedge I} \) builds \( P \wedge \neg Q \), the premise gives \( R \), and \( \rulename{\vee I} \) gives the right side.
     - **S1:** 1; box 2 \( P \), asm; gap; 10 | \( Q \vee R \), unjustified; 11 →I 2–10.
     - **S2:** 1; box 2; 3 | \( Q \vee \neg Q \), LEM; box 4 \( Q \), asm; gap; 5 | | \( Q \vee R \), unjustified; box 6 \( \neg Q \), asm; gap; 9 | | \( Q \vee R \), unjustified; 10 | \( Q \vee R \), ∨E 3, 4–5, 6–9; 11.
     - **Finished (11 lines):** 1 \( (P \wedge \neg Q) \to R \); 2 | \( P \), asm; 3 | \( Q \vee \neg Q \), LEM; 4 | | \( Q \), asm; 5 | | \( Q \vee R \), ∨I 4; 6 | | \( \neg Q \), asm; 7 | | \( P \wedge \neg Q \), ∧I 2, 6; 8 | | \( R \), →E 1, 7; 9 | | \( Q \vee R \), ∨I 8; 10 | \( Q \vee R \), ∨E 3, 4–5, 6–9; 11 \( P \to (Q \vee R) \), →I 2–10.
   - *Aftermath* (~60 words): "An equivalence is two searches, and they need not be alike. One direction used a derived rule and no classical step. The other reached step 5, because its goal was a disjunction with no side in hand. When one direction is easy, do it first: it is a check that the statements are worth comparing, and its lines often suggest the other direction's split."
5. **`## Inconsistent lists`** (~1,000 words with the gallery and the block).
   - **Lead** (~60 words): "Sometimes the task is not to reach a conclusion but to show that some statements cannot be accepted together. Examples: a puzzle's conditions that no number meets, the hypotheses of a lemma that contradict each other, or the assumption of a proof by contradiction together with what is given. A derivation of \( \bot \) does that, and the list it starts from gets a name."
   - **`def-inconsistent-set`** (block, verbatim as drafted here):

     ```
     ::: {#def-inconsistent-set}
     [Inconsistent and Consistent Lists]

     Let \( \Gamma \) be a list of statements \( \varphi_1, \dots, \varphi_n \), where \( n \ge 0 \). The list
     \( \Gamma \) is **inconsistent** if \( \Gamma \vdash \bot \): some derivation whose premises all belong to
     \( \Gamma \) has \( \bot \) as its last line. It is **consistent** if it is not inconsistent, that is,
     if **no** derivation with premises in \( \Gamma \) ends with \( \bot \).
     :::
     ```

     Then (~80 words): "In words: a list is inconsistent when a derivation from it reaches \( \bot \) outside every box. The definition speaks only of derivations, and says nothing about whether the statements are true. The list \( P, \neg P \) is inconsistent, by one \( \rulename{\neg E} \) line, and so is any list with \( \bot \) as a member. To show a list inconsistent, exhibit a derivation. To show one consistent, one would have to rule out every derivation, and nothing in this chapter can do that." (The last sentence is the G10-safe statement of the situation. It claims nothing about any particular list.)
   - **`prp-inconsistent-derives-everything`** (block):

     ```
     ::: {#prp-inconsistent-derives-everything}
     [An Inconsistent List Proves Everything]

     For a list of statements \( \Gamma \), the following are equivalent:

     ::: {.enumerate options="label=(\roman*)"}
     1. \( \Gamma \) is inconsistent;
     2. \( \Gamma \vdash \psi \) for **every** statement \( \psi \);
     3. \( \Gamma \vdash \chi \) and \( \Gamma \vdash \neg\chi \) for **some** statement \( \chi \).
     :::
     :::
     ```

     *In words:* "an inconsistent list proves every statement, and a list that proves some statement and its negation is inconsistent." Its proof is in fold F3.2-a (item 6). One sentence: "This is @prp-ex-falso grown from two premises to any inconsistent list."

     **Quick check (new, ~35 words):** "Without writing a derivation, explain why \( P, \ \neg P \vdash Q \wedge \neg Q \)." *Solution:* The list \( P, \neg P \) is inconsistent (one ¬E line), so by @prp-inconsistent-derives-everything, (i) ⇒ (ii), it derives every statement, \( Q \wedge \neg Q \) included.
   - **`exm-inconsistency-search`** `[Four conditions that no integer meets]` (~330 words).
     - Statement: "Let \( n \) be an integer. A puzzle asks for an \( n \) such that: (1) if \( n \) is even, then \( n \) is a multiple of \( 4 \); (2) \( n \) is even or a multiple of \( 3 \); (3) if \( n \) is a multiple of \( 3 \), then \( n \) is even; (4) \( n \) is not a multiple of \( 4 \). With \( E \): '\( n \) is even', \( F \): '\( n \) is a multiple of \( 4 \)', \( T \): '\( n \) is a multiple of \( 3 \)', show that the list \( E \to F, \ E \vee T, \ T \to E, \ \neg F \) is inconsistent."
     - *Search.*
       - The goal is \( \bot \). Look first for a clash partner already on a line (Section 3.1): line 4 is \( \neg F \), so aim at \( F \).
       - \( F \) is the conclusion of line 1, so the new goal is \( E \), a letter. Line 3 gives \( E \) from \( T \), but \( T \) is not in hand, and \( E \vee T \) does not say which side holds. So use it by \( \rulename{\vee E} \), with both cases ending in \( E \). The case \( E \) is a one-line box; the case \( T \) fires line 3.
     - **S1:** lines 1–4; gap; 9 \( F \), unjustified; 10 \( \bot \), ¬E 9, 4.
     - **S2:** lines 1–4; 5 | \( E \), asm (one-line box); 6 | \( T \), asm; gap; 7 | \( E \), unjustified; 8 \( E \), ∨E 2, 5–5, 6–7; 9 \( F \), →E 1, 8; 10.
     - **Finished (10 lines):** S2 with 7 \( E \), →E 3, 6.
     - Reading (~70 words): "Read as a proof about \( n \), the derivation shows that no integer meets all four conditions: by (2) and (3), \( n \) is even in either case; by (1) it is a multiple of \( 4 \); and (4) says it is not. Yet any three of the conditions can be met together: \( n = 6 \) meets all but (1), \( n = 1 \) all but (2), \( n = 3 \) all but (3), and \( n = 12 \) all but (4). The inconsistency belongs to the four together. The derivation does not say which condition to drop (the fold 'Logic permits; it does not choose' in Section 3.1)."

     **Quick check (new, ~30 words):** "Which integers between \( 1 \) and \( 10 \) meet conditions (1), (2) and (4) of @exm-inconsistency-search, and which condition does each break?" *Solution:* \( 3 \) and \( 9 \): odd, so (1) promises nothing; multiples of \( 3 \), so (2) holds; not multiples of \( 4 \). Each breaks (3).
   - **`exm-inconsistent-lists`** `[Three inconsistent lists, and a look-alike]` (~170 words). [Technique: Hu (gallery with a tempting non-instance), applied to the chapter's definition.] Table, columns *The list* | *The clash it reaches* | *The derivation of \( \bot \), in brief*:
     - \( (P \vee Q) \to R, \ P \wedge \neg R \) | \( R \), \( \neg R \) | \( P \) ∧E; \( P \vee Q \) ∨I; \( R \) →E; \( \neg R \) ∧E; \( \bot \) ¬E (7 lines)
     - \( P \leftrightarrow \neg P \) | \( P \), \( \neg P \) | a box on \( P \): \( \neg P \) ↔E, \( \bot \) ¬E; \( \neg P \) ¬I; then \( P \) ↔E, and \( \neg P \) ↔E again from that \( P \); \( \bot \) ¬E (8 lines)
     - \( \neg(P \to Q), \ \neg P \) | \( P \to Q \), \( \neg(P \to Q) \) | \( P \to Q \) by VI from \( \neg P \) (@prp-vacuous-implication); \( \bot \) ¬E (4 lines)

     One sentence on the second row: "By @prp-derivable-iff-negation-inconsistent below, its inconsistency is the same fact as @lem-not-iff-own-negation of Section 2.4, \( \vdash \neg(P \leftrightarrow \neg P) \)." (A backward pointer to the label fixed by layout §1.4. If ch02-deepen does not deliver it, S3 drops this sentence.)
     - **Row 2 is a recall, not a new item** (S2 round 1): the list \( P \leftrightarrow \neg P \) is the 2.4 lemma's, seen again as a list; it is kept because the gallery's point is that the chapter's earlier results are inconsistencies in disguise. Its derivation is written **detour-free** (§9, item 3): the 7-line version would apply ¬E to line 5's \( \neg P \), built by ¬I, which is the ¬I/¬E detour of 3.1's paragraph. Lines: 1 \( P \leftrightarrow \neg P \); 2 | \( P \), asm; 3 | \( \neg P \), ↔E 1, 2; 4 | \( \bot \), ¬E 2, 3; 5 \( \neg P \), ¬I 2–4; 6 \( P \), ↔E 1, 5; 7 \( \neg P \), ↔E 1, 6; 8 \( \bot \), ¬E 6, 7. Line 5 stays, being cited at line 6; only the elimination is replaced (the case the detour paragraph's last sentence names: "an introduced line cited elsewhere stays"). The table's third column gives the line count only.

     **Not an instance.** "\( P \to Q, \ P \to \neg Q \). The two members look opposed. But with \( P \) false (say \( P \): '\( 0 = 1 \)') both are true, whatever \( Q \) says, so the claim \( P \to Q, \ P \to \neg Q \vdash \bot \) breaks. What the list does derive is \( \neg P \): from \( P \) it would give \( Q \) and \( \neg Q \). This chapter does not call the list inconsistent, and it does not call it consistent either. Whether a break rules out every derivation of \( \bot \) is the question the chapter ends on (Section 3.3)."
   - **Not allowed** (after the gallery; ~140 words): warning `[Not allowed: claims about inconsistency]`, one line each, tagged:
     - "The list is inconsistent because one of its members is false." Inconsistency is a derivation of \( \bot \) (@def-inconsistent-set), not a false member: the one-member list "\( 2 > 3 \)" has a false member and no derivation of \( \bot \) is offered.
     - "\( P \to Q \) and \( P \to \neg Q \) contradict each other, so the list is inconsistent." Nothing has been derived. Both members are true when \( P \) is false, and the claim of inconsistency breaks.
     - "Line 7, inside the box of the assumption \( P \), is \( \bot \); so the premises are inconsistent." The \( \bot \) depends on \( P \): it shows the list \( \Gamma, P \) inconsistent, and so \( \Gamma \vdash \neg P \). The last line must lie outside every box (@def-derivation).
     - "A search for \( \bot \) stalled, so the list is consistent." A stalled search proves nothing (Section 3.1). Consistency is the absence of **every** derivation of \( \bot \).
     - "The list is inconsistent, so its first member is false." Inconsistency belongs to the list. It says that the members cannot all be accepted together, not which one fails (compare the four conditions above).
6. **`## The counterexample set, derived`** (~250 words, and fold F3.2-a).
   - **Lead** (~50 words): "Proving and refuting meet in one list. The counterexample set of a claim \( \Gamma \vdash \varphi \) is the list \( \Gamma, \neg\varphi \) (@def-counterexample-set). Breaking the claim makes that list true. Deriving the claim, it turns out, is showing that list inconsistent."
   - **`prp-derivable-iff-negation-inconsistent`** (block):

     ```
     ::: {#prp-derivable-iff-negation-inconsistent}
     [Derivable Exactly When the Counterexample Set Is Inconsistent]

     Let \( \Gamma \) be a list of statements and \( \varphi \) a statement.

     ::: {.enumerate options="label=(\alph*)"}
     1. \( \Gamma \vdash \neg\varphi \) if and only if the list \( \Gamma, \varphi \) is inconsistent.
     2. \( \Gamma \vdash \varphi \) if and only if the list \( \Gamma, \neg\varphi \) is inconsistent.
     :::
     :::
     ```

     *In words* (~60 words): "(b) says that a claim is derivable exactly when its counterexample set is inconsistent. (a) is the same for a negated conclusion. (a) rests on \( \rulename{\neg I} \) alone, and (b) on \( \rulename{RAA} \): Section 2.5's distinction between the two rules, stated about whole derivations. Section 1.1's two attacks on a claim are now two tasks on one list: make it true, or derive \( \bot \) from it."
   - **Fold F3.2-a** `title="The proofs: append a line, or copy a derivation into a box"` (~270 words), holding two `::: {.proof}` blocks.
     - *Proof of @prp-inconsistent-derives-everything.*
       - (i) ⇒ (ii): A derivation of \( \bot \) with premises in \( \Gamma \), followed by the line \( \psi \), ⊥E, is a derivation of \( \psi \). Its last line lies in no box, since the last line of the first derivation does not.
       - (ii) ⇒ (iii): Take any \( \chi \), and apply (ii) to \( \chi \) and to \( \neg\chi \).
       - (iii) ⇒ (i): The sequent \( \chi, \neg\chi \vdash \bot \) has a one-step derivation (¬E). By @lem-weakening-cut (c), \( \Gamma \vdash \bot \).
     - *Proof of @prp-derivable-iff-negation-inconsistent.*
       - (b) (⇒): From \( \Gamma \vdash \varphi \), @lem-weakening-cut (a) gives \( \Gamma, \neg\varphi \vdash \varphi \). The one-line derivation of the premise \( \neg\varphi \) gives \( \Gamma, \neg\varphi \vdash \neg\varphi \). By @lem-weakening-cut (c) with \( \varphi, \neg\varphi \vdash \bot \), we get \( \Gamma, \neg\varphi \vdash \bot \).
       - (b) (⇐): Let \( D \) be a derivation of \( \bot \) with premises in \( \Gamma, \neg\varphi \).
         - If \( D \)'s last line is a premise that belongs to \( \Gamma \), then \( \bot \in \Gamma \), and \( \Gamma \vdash \varphi \) by ⊥E.
         - Otherwise, write as premises those premises of \( D \) that belong to \( \Gamma \). Open a box with the assumption \( \neg\varphi \). Inside it, copy the lines of \( D \) that are not premises, in order, with their boxes, renumbering every citation, and letting every citation of the premise \( \neg\varphi \) cite the box's assumption instead. Close the box after the copy of \( D \)'s last line and write \( \varphi \) by RAA.
       - Every copied citation is legal. A cited premise of \( \Gamma \) lies above the box and in no box. The assumption is available throughout the box. And \( D \)'s own boxes sit inside the new box exactly as they sat in \( D \), so every line that was available keeps being available (the scope rule of @def-derivation). \( D \)'s last line lies in no box of \( D \), so its copy is a line of the new box itself, as RAA requires. If \( D \) never cites \( \neg\varphi \), the copy is still correct.
       - (a) is the same with \( \varphi \) in place of \( \neg\varphi \), and ¬I in place of RAA. If \( D \)'s last line is the premise \( \varphi \) itself (possible only when \( \varphi \) is \( \bot \)), nothing is copied: the box is its one assumption line, and ¬I closes it at once. In (⇒), \( \Gamma, \varphi \vdash \varphi \) by its one-line derivation and \( \Gamma, \varphi \vdash \neg\varphi \) by weakening, and ¬E finishes.
     - One closing sentence: "The copying is the same move as turning a premise into an assumption in Section 1.4, Exercise C4 (b), run backwards."
   - **Quick check (new, ~45 words):** "By @prp-derivable-iff-negation-inconsistent, which list must be shown inconsistent to prove \( \vdash \neg(P \wedge \neg P) \)? Show it." *Solution:* By (a), with \( \Gamma \) empty and \( \varphi = P \wedge \neg P \), the list is \( P \wedge \neg P \): 2 \( P \), ∧E 1; 3 \( \neg P \), ∧E 1; 4 \( \bot \), ¬E 2, 3.
7. **`## One task in four costumes`** (~220 words and a table).
   - Text: "Every task of this section is a claim that something is derivable, and by @prp-derivable-iff-negation-inconsistent every such claim is a claim that a list is inconsistent."
   - Table, columns *Task* | *As a claim of derivability* | *As a claim of inconsistency* | *It breaks when some choice of statements makes*:
     - theorem | \( \vdash \varphi \) | the list \( \neg\varphi \) | \( \varphi \) false
     - equivalence | \( \varphi \vdash \psi \) and \( \psi \vdash \varphi \) | the lists \( \varphi, \neg\psi \) and \( \psi, \neg\varphi \) | one of \( \varphi \), \( \psi \) true and the other false
     - inconsistency | \( \Gamma \vdash \bot \) | the list \( \Gamma \) | every member of \( \Gamma \) true
     - derive or break | \( \Gamma \vdash \varphi \) | the list \( \Gamma, \neg\varphi \) | every member of \( \Gamma, \neg\varphi \) true
   - One sentence on equivalences: "\( \varphi \dashv\vdash \psi \) holds exactly when \( \vdash \varphi \leftrightarrow \psi \). Copy each of the two derivations into a box, as in the fold above, and close both by \( \rulename{{\leftrightarrow}I} \). Conversely, add the premise \( \varphi \) to a derivation of \( \varphi \leftrightarrow \psi \) and write \( \psi \) by \( \rulename{{\leftrightarrow}E} \), and likewise for \( \psi \)."
   - Closing (~50 words): "So the four tasks are one: is this list inconsistent? Each costume starts the search in a different place, which is why the task chooses the search. And each row has a second half, the last column: what to do when the list might instead be made true. That is the fourth task."
8. **`## Derive or break`** (~640 words with the example and the figure). [Named move: *Try to break it first*. Technique: LPL, Si, En (verdict withheld); Sm (a forced failed attempt read as a plan).]
   - **Lead** (~90 words): Section 1.5 introduced claims listed without a verdict ("Derive it or break it"). Here the format becomes a task with its own first move: **decide before you search**. Spend a few minutes trying to make the counterexample set true, starting where the conclusion is false (Section 1.1's "Where to look first"). Either some choice of statements works, and the claim breaks; or every attempt is forced into a clash. Then search for a derivation. The forced attempt usually suggests a plan for it: the statements the attempt had to make true suggest the assumptions of the derivation's boxes, and the clash it met suggests the derivation's \( \bot \). (S2 round 1: heuristic wording; that a closed attempt always yields a derivation is the 4.8 Challenge's business, §6.)
   - **`exm-derive-or-break-search`** `[Two claims, one connective apart]`.
     - Statement: "Derive or break each claim: (a) \( P \to (Q \to R), \ P \to \neg R \vdash P \to \neg Q \); (b) \( P \to (Q \vee R), \ P \to \neg R \vdash P \to \neg Q \)."
     - *(a), trying to break it.* The conclusion is false only with \( P \) true and \( \neg Q \) false, that is, \( Q \) true. Then the first premise needs \( Q \to R \) true, so \( R \) true. The second needs \( \neg R \) true, so \( R \) false. Every choice is forced, and the forcing ends in a clash. So search.
     - *(a), the derivation.* The attempt's plan: a box on \( P \) (the conclusion's hypothesis), a box on \( Q \) (the statement whose negation is wanted), and the clash \( R \), \( \neg R \). Before the box on \( Q \) opens, both premises fire on \( P \): lines that need nothing new (Section 3.1).
       - **S1:** 1, 2; box 3 \( P \), asm; gap; 9 | \( \neg Q \), unjustified; 10 \( P \to \neg Q \), →I 3–9.
       - **S2:** 1, 2; 3 | \( P \); 4 | \( Q \to R \), →E 1, 3; 5 | \( \neg R \), →E 2, 3; box 6 \( Q \), asm; gap; 8 | | \( \bot \), unjustified; 9 | \( \neg Q \), ¬I 6–8; 10.
       - **Finished (10 lines):** S2 with 7 | | \( R \), →E 4, 6, and 8 | | \( \bot \), ¬E 7, 5.
     - *(b), trying to break it.* The same start: \( P \) true, \( Q \) true. Now the first premise asks only that \( Q \vee R \) be true, and \( Q \) already makes it so. \( R \) is free, and the second premise asks for \( R \) false. Nothing clashes: with \( P \) and \( Q \) true and \( R \) false, every member of the counterexample set \( P \to (Q \vee R), \ P \to \neg R, \ \neg(P \to \neg Q) \) is true. With statements about a real number \( x \): \( P \): "\( x > 0 \)", \( Q \): "\( x > 1 \)", \( R \): "\( x > 3 \)", at \( x = 2 \). The claim breaks.
     - Closing (~50 words): "The two claims differ in one connective. Trying to break each found its verdict, and for (a) it also found the derivation. The method of Section 3.1 would have found (a) without the attempt. On (b) the method of Section 3.1 could only search, and a stall is not a verdict; the break is." (Reworded at S2 round 2: the closing speaks of this chapter's method only, and draws nothing about every search from the break, §9 item 1.)
   - **Figure 3.2-F** (after the example; lead ~30 words: "The task as a chart. The loop at the bottom is honest: nothing in this chapter promises that it ends."). Template `flowchart`.
     - Nodes:
       - (s) `fc start` "a claim $\Gamma \vdash \varphi$,\\verdict withheld";
       - (t1) `fc test` "can the counterexample set\\be made true? (start where\\the conclusion is false)";
       - (e1) `fc start` "it breaks:\\give the statements";
       - (b1) `fc step` "search for a derivation\\(Section 3.1): the forced\\clash suggests a plan";
       - (t2) `fc test` "has the search\\finished?";
       - (e2) `fc start` "derived".
     - Arrows:
       - s→t1;
       - t1 –"yes"→ e1, to the right;
       - t1 –"every try is forced into a clash"→ b1, below;
       - b1→t2;
       - t2 –"yes"→ e2, to the right;
       - t2 –"stalled"→ back to t1, as a line on the left: `(t2.west) -- ++(-0.6,0) |- (t1.west)`.
   - **Quick check (new, ~45 words):** "Change one symbol of the first premise of claim (b) in @exm-derive-or-break-search so that the claim can be derived, and derive it." *Solution:* For example (S2 round 1: "Two answers" was wrong, and the S1 answer \( \neg Q \) inserted a symbol and rested on DS's exercise form):
     - Replace \( \vee \) by \( \to \): that is claim (a), derived above.
     - Or replace \( \vee \) by \( \wedge \): from \( P \), the premises give \( Q \wedge R \) and \( \neg R \), which clash. The lines: 3 | \( P \), asm; 4 | \( Q \wedge R \), →E 1, 3; 5 | \( R \), ∧E 4; 6 | \( \neg R \), →E 2, 3; 7 | \( \bot \), ¬E 5, 6; 8 | \( \neg Q \), ⊥E 7; 9 \( P \to \neg Q \), →I 3–8.
     - The solution ends: "\( \leftrightarrow \) for \( \vee \), or \( R \) for \( Q \), works too." (Each checked by truth table, §9 item 19.)
9. **Looking ahead** (`::: {.remark}` `[Looking ahead]`, ~40 words, no `@ref`): "Chapter 4 calls a list whose members can all be made true at once *satisfiable*, and proves that the satisfiable lists are exactly the consistent ones."

**Quick checks:**
- which task (item 2);
- \( Q \wedge \neg Q \) from \( P, \neg P \) (item 5);
- the integers \( 3 \), \( 9 \) (item 5);
- \( \neg(P \wedge \neg P) \) (item 6);
- one symbol (item 8).

Five in ~3,500 words, about one per 700.

**Exercises.**

- **A1** (`exr-four-kinds-of-task-a1`), five parts:
  - (a) When is a list of statements inconsistent? — When \( \bot \) is derivable from it (@def-inconsistent-set).
  - (b) By @prp-derivable-iff-negation-inconsistent, which list is inconsistent exactly when \( P \to Q, \ Q \to R \vdash P \to R \)? — \( P \to Q, \ Q \to R, \ \neg(P \to R) \).
  - (c) True or false: every list that has \( \bot \) as a member is inconsistent. — True: the one-line derivation whose line is the premise \( \bot \).
  - (d) True or false: if \( \Gamma \) is inconsistent, so is every list \( \Gamma, \psi \). — True, by @lem-weakening-cut (a).
  - (e) Name the task and the first move: "show that \( P \wedge Q \dashv\vdash Q \wedge P \)". — An equivalence: two derivations, each starting with ∧E on its premise. Each is @prp-and-commutes, with the letters exchanged for the second.
- **A2: Drill** (`exr-four-kinds-of-task-a2`), twelve parts in the ramp:
  - *Recognition.*
    - (a) Which task is "show \( \vdash (P \wedge Q) \to P \)"? — A theorem.
    - (b) "Show that \( P \to \neg Q \) and \( Q \to \neg P \) are provably equivalent." Which two derivations? — \( P \to \neg Q \vdash Q \to \neg P \) and \( Q \to \neg P \vdash P \to \neg Q \).
    - (c) Write "\( P \), \( P \to Q \) and \( \neg Q \) cannot all be accepted together" as a sequent. — \( P, \ P \to Q, \ \neg Q \vdash \bot \).
  - *One step.*
    - (d) A search for \( \bot \) from \( P \wedge \neg Q, \ P \to Q \) begins. Name its first three lines after the premises. — \( P \), ∧E 1; \( Q \), →E 2, 3; \( \neg Q \), ∧E 1. (Then \( \bot \), ¬E.)
    - (e) Which list must be shown inconsistent to prove \( P \to Q \vdash \neg Q \to \neg P \) by @prp-derivable-iff-negation-inconsistent (b)? — \( P \to Q, \ \neg(\neg Q \to \neg P) \).
  - *Missing piece.*
    - (f) The list \( Q, \ \neg P, \ \neg\neg R \) is the counterexample set of which claims? — Of \( Q, \neg P \vdash \neg R \) (with \( \neg\neg R \) the negated conclusion) and of \( Q, \neg\neg R \vdash P \) (with \( \neg P \) the negated conclusion). \( Q \) is not a negation, so it is not the negated conclusion of any claim.
  - *Is this correct?*
    - (g) "\( P \to Q, \ P \to \neg Q \) is inconsistent, since its members contradict each other." — No. Both are true when \( P \) is false, and nothing has been derived.
    - (h) "Inside the box of the assumption \( P \), line 6 is \( \bot \); so the premises are inconsistent." — No. It shows the premises together with \( P \) inconsistent, so the premises derive \( \neg P \).
    - (i) "A search for \( \bot \) from \( P \vee Q, \neg P \) stalled; so the list is consistent." — No: a stalled search proves nothing.
    - (j) "Since \( P, \neg P \vdash \bot \), the list \( P, \neg P \) derives both \( Q \) and \( \neg Q \)." — Yes: @prp-inconsistent-derives-everything, (i) ⇒ (ii).
  - *Derivations.*
    - (k) Derive \( \bot \) from \( P \to Q, \ Q \to R, \ P, \ \neg R \). — 5 \( Q \), →E 1, 3; 6 \( R \), →E 2, 5; 7 \( \bot \), ¬E 6, 4.
    - (l) Derive \( \bot \) from \( P \vee Q, \ \neg P, \ \neg Q \). — 4 | \( P \); 5 | \( \bot \), ¬E 4, 2; 6 | \( Q \); 7 | \( \bot \), ¬E 6, 3; 8 \( \bot \), ∨E 1, 4–5, 6–7.
- **B1** `[B1: Three theorems]`. [Technique: LB, Le.] Stem: "Derive each theorem, and say which step of Section 3.1's method opens each box." (a) \( \vdash \neg(P \wedge \neg P) \wedge \neg\neg(P \vee \neg P) \). (b) \( \vdash ((P \to Q) \wedge (P \vee Q)) \to Q \). (c) \( \vdash ((P \to Q) \to Q) \to ((Q \to P) \to P) \).
  - *Answer.*
    - (a) 1 | \( P \wedge \neg P \), asm; 2 | \( P \), ∧E 1; 3 | \( \neg P \), ∧E 1; 4 | \( \bot \), ¬E 2, 3; 5 \( \neg(P \wedge \neg P) \), ¬I 1–4; 6 | \( \neg(P \vee \neg P) \), asm; 7 | | \( P \), asm; 8 | | \( P \vee \neg P \), ∨I 7; 9 | | \( \bot \), ¬E 8, 6; 10 | \( \neg P \), ¬I 7–9; 11 | \( P \vee \neg P \), ∨I 10; 12 | \( \bot \), ¬E 11, 6; 13 \( \neg\neg(P \vee \neg P) \), ¬I 6–12; 14 ∧I 5, 13.
      - Boxes 1 and 6 come from step 2 (goals \( \neg\ldots \)). Box 7 comes from step 4: it manufactures \( \neg P \), so that \( \rulename{\vee I} \) can build the disjunction that clashes with line 6.
      - The solution adds one sentence: the second conjunct needed no classical rule, although \( P \vee \neg P \) itself does in this book's derivation (@prp-excluded-middle).
    - (b) (Replaced at S2 round 1: the S1 item was `exm-derive-or-break-search` (a) curried.) 1 | \( (P \to Q) \wedge (P \vee Q) \), asm; 2 | \( P \to Q \), ∧E 1; 3 | \( P \vee Q \), ∧E 1; 4 | | \( P \), asm; 5 | | \( Q \), →E 2, 4; 6 | | \( Q \), asm; 7 | \( Q \), ∨E 3, 4–5, 6–6; 8 \( ((P \to Q) \wedge (P \vee Q)) \to Q \), →I 1–7. Box 1 comes from step 2; boxes 4 and 6 from step 3, the resource \( P \vee Q \) split by ∨E with both cases ending in the goal \( Q \) (the case \( Q \) a one-line box). Lines 2–3 need nothing new. Reading: "if \( P \) implies \( Q \), and \( P \) or \( Q \) holds, then \( Q \) holds".
    - (c) 1 | \( (P \to Q) \to Q \); 2 | | \( Q \to P \); 3 | | | \( \neg P \), asm; 4 | | | \( P \to Q \), VI 3; 5 | | | \( Q \), →E 1, 4; 6 | | | \( P \), →E 2, 5; 7 | | | \( \bot \), ¬E 6, 3; 8 | | \( P \), RAA 3–7; 9 | \( (Q \to P) \to P \), →I 2–8; 10 →I 1–9. Boxes 1 and 2 come from step 2, and box 3 from step 5: the goal \( P \) is a letter and the resources wait for \( P \to Q \).
  - Worked example type: `exm-theorem-search`. (None is a sequent of the text: checked against §9 item 15's list.)
- **B2** `[B2: Two directions]` (scaffolded, STYLE §12.8). [Technique: LPL, Le.] Stem: "Show that \( (P \wedge Q) \to R \dashv\vdash (P \wedge \neg R) \to \neg Q \)."
  - The parts:
    - (a) The search for (⇐) has reached the stage below. *Name the move, then complete it.*
    - (b) Derive (⇒).
    - (c) Which direction used a classical rule, and why did the other not need one?
  - The scaffold (a raw `nd` block, `% schema (partial derivations: …)`): 1 \( (P \wedge \neg R) \to \neg Q \); box 2 \( P \wedge Q \), asm `\purpose{\ii}`; gap; 9 | \( R \), unjustified; 10 \( (P \wedge Q) \to R \), →I 2–9.
  - *Answer.*
    - (a) The move is step 5: the current goal \( R \) is a letter, no resource gives it, and nothing clashes, so assume \( \neg R \) for RAA. 3 | \( P \), ∧E 2; 4 | \( Q \), ∧E 2; 5 | | \( \neg R \), asm; 6 | | \( P \wedge \neg R \), ∧I 3, 5; 7 | | \( \neg Q \), →E 1, 6; 8 | | \( \bot \), ¬E 4, 7; 9 | \( R \), RAA 5–8; 10.
    - (b) 1 \( (P \wedge Q) \to R \); 2 | \( P \wedge \neg R \); 3 | \( P \), ∧E 2; 4 | \( \neg R \), ∧E 2; 5 | | \( Q \); 6 | | \( P \wedge Q \), ∧I 3, 5; 7 | | \( R \), →E 1, 6; 8 | | \( \bot \), ¬E 7, 4; 9 | \( \neg Q \), ¬I 5–8; 10 \( (P \wedge \neg R) \to \neg Q \), →I 2–9.
    - (c) (⇐) used RAA at line 9, because its goal \( R \) is a letter. (⇒) needed none, because its goal \( \neg Q \) is a negation, which ¬I builds. This is a claim about our derivations only.
  - The solution adds the reading: to prove "if \( P \) and \( Q \), then \( R \)", it is enough to prove "if \( P \) and not \( R \), then not \( Q \)", a contrapositive in one hypothesis.
- **B3** `[B3: Derive or break, used later]`. [Technique: LPL, Si, En; look-alikes seeded.] Stem: "For each claim, derive it or break it. Try to break it first. To break a claim, give statements that make its counterexample set true."
  - The claims:
    - (a) \( \neg(P \wedge Q) \vdash \neg P \wedge \neg Q \)
    - (b) \( \neg(P \leftrightarrow Q), \ P \vdash \neg Q \)
    - (c) \( P \to Q, \ \neg P \to (R \vee Q), \ \neg R \vdash Q \)
    - (d) \( P \to Q, \ \neg P \to (R \vee Q), \ \neg R \vdash P \)
    - (e) \( (P \to Q) \to R, \ \neg R \vdash P \)
    - (f) \( (P \to Q) \to R, \ \neg R \vdash Q \)
    - (g) \( P \vee Q, \ P \vdash \neg Q \)
    - (h) \( P \vee Q, \ \neg(P \wedge Q), \ P \vdash \neg Q \)
    - (i) \( \neg(P \vee Q) \to P \vdash P \vee Q \)
  - (S2 round 1: the S1 (c) and (i) reproduced textbook exercises; they were replaced, and (c)/(d) share their premises. S2 round 2: the round 1 replacements were textbook items plus one ∧E line; replaced again. The new (c) splits by LEM on \( P \), and its two cases reach \( Q \) by different rules: →E in the case \( P \), →E and then DS in the case \( \neg P \). The new (i) has a disjunctive goal, so step 2 postpones it; RAA on the goal supplies the hypothesis the premise waits for, and the clash with the RAA assumption must be manufactured by ∨I.)
  - *Answer* (verdict first, then the derivation or the break; \( x \) is a real number):
    - (a) Breaks. \( P \): "\( x > 0 \)", \( Q \): "\( x > 2 \)", at \( x = 1 \): \( \neg(P \wedge Q) \) is true and \( \neg P \) is false.
    - (b) Derive. 3 | \( Q \), asm; 4 | | \( P \), asm; 5 | | \( Q \), R 3; 6 | | \( Q \), asm; 7 | | \( P \), R 2; 8 | \( P \leftrightarrow Q \), ↔I 4–5, 6–7; 9 | \( \bot \), ¬E 8, 1; 10 \( \neg Q \), ¬I 3–9.
    - (c) Derive. 4 \( P \vee \neg P \), LEM; 5 | \( P \); 6 | \( Q \), →E 1, 5; 7 | \( \neg P \); 8 | \( R \vee Q \), →E 2, 7; 9 | \( Q \), DS 8, 3; 10 \( Q \), ∨E 4, 5–6, 7–9. (Step 5: the goal \( Q \) is a letter, and the first two premises wait for \( P \) and for \( \neg P \), so LEM on \( P \). DS matches as stated in Section 2.3, refuting the **left** disjunct \( R \); that is why the premise is written \( R \vee Q \).)
    - (d) Breaks. \( P \): "\( x > 5 \)", \( Q \): "\( x > 0 \)", \( R \): "\( x > 10 \)", at \( x = 1 \): \( P \) is false, so \( P \to Q \) is true; \( \neg P \) and \( Q \) are true, so \( \neg P \to (R \vee Q) \) is true; \( \neg R \) is true; and \( P \) is false. (Trying to break it first: with \( P \) false, the premises force \( Q \) true and \( R \) false, and nothing clashes. The tempting step from "\( P \) gives \( Q \)" and "\( Q \) holds", which (c) derives, to \( P \) is affirming the consequent, Section 1.3.)
    - (e) Derive. 3 \( \neg(P \to Q) \), MT 1, 2; 4 | \( \neg P \), asm; 5 | \( P \to Q \), VI 4; 6 | \( \bot \), ¬E 5, 3; 7 \( P \), RAA 4–6.
    - (f) Breaks. \( P \): "\( x > 0 \)", \( Q \): "\( x > 2 \)", \( R \): "\( x > 3 \)", at \( x = 1 \): \( P \to Q \) is false, so \( (P \to Q) \to R \) is true; \( \neg R \) is true; \( Q \) is false.
    - (g) Breaks (affirming a disjunct, Section 1.6). \( P \): "\( x > 1 \)", \( Q \): "\( x > 2 \)", at \( x = 3 \).
    - (h) Derive. 4 | \( Q \); 5 | \( P \wedge Q \), ∧I 3, 4; 6 | \( \bot \), ¬E 5, 2; 7 \( \neg Q \), ¬I 4–6. The premise \( P \vee Q \) is not needed.
    - (i) Derive. 2 | \( \neg(P \vee Q) \), asm; 3 | \( P \), →E 1, 2; 4 | \( P \vee Q \), ∨I 3; 5 | \( \bot \), ¬E 4, 2; 6 \( P \vee Q \), RAA 2–5. (Step 2 postpones the disjunction; the premise waits for \( \neg(P \vee Q) \), which RAA on the goal supplies; step 4 then manufactures the clash partner \( P \vee Q \) from line 3 by ∨I, a manufactured clash and not a detour. Reading: a statement whose failure would force one of its own sides holds.)
  - Closing sentence: (c)/(d) and (e)/(f) are look-alike pairs: each pair has the same premises and differs in the conclusion. (h) is (g) repaired by "not both". (a) is a De Morgan look-alike with the wrong connective inside.
  - **Used later:** Section 4.6 recalls the four breaking claims (a), (d), (f), (g) by label, and Section 4.7's retroactive paragraph certifies them (§6).
- **B4** `[B4: Derive ⊥, or make every member true]`. Stem: "For each list, either derive \( \bot \) from it, or give statements that make every member true at once." (a) \( P \to Q, \ Q \to \neg P, \ P \). (b) \( P \vee Q, \ P \to \neg Q, \ Q \to \neg P \). (c) \( \neg(P \to Q), \ Q \vee \neg P \). (d) \( P \to (Q \wedge \neg Q) \). (e) \( \neg(P \vee Q), \ P \vee (Q \wedge R) \). (f) \( \neg(P \wedge Q), \ \neg(P \wedge \neg Q), \ \neg(\neg P \wedge Q) \).
  - *Answer:*
    - (a) Derive. 4 \( Q \), →E 1, 3; 5 \( \neg P \), →E 2, 4; 6 \( \bot \), ¬E 3, 5.
    - (b) True at once. \( P \): "\( x > 0 \)", \( Q \): "\( x < 0 \)", at \( x = 1 \): \( P \vee Q \) is true, \( P \to \neg Q \) is true, and \( Q \to \neg P \) is true since \( Q \) is false.
    - (c) Derive. 3 | \( Q \); 4 | | \( P \); 5 | | \( Q \), R 3; 6 | \( P \to Q \), →I 4–5; 7 | \( \bot \), ¬E 6, 1; 8 | \( \neg P \); 9 | \( P \to Q \), VI 8; 10 | \( \bot \), ¬E 9, 1; 11 \( \bot \), ∨E 2, 3–7, 8–10.
    - (d) True at once, with \( P \) false (\( P \): "\( 0 = 1 \)", any \( Q \)). A member that mentions a contradiction is not itself a clash: with \( P \) false every member is true, so the claim that the list derives \( \bot \) breaks.
    - (e) Derive. 3 | \( P \); 4 | \( P \vee Q \), ∨I 3; 5 | \( \bot \), ¬E 4, 1; 6 | \( Q \wedge R \); 7 | \( Q \), ∧E 6; 8 | \( P \vee Q \), ∨I 7; 9 | \( \bot \), ¬E 8, 1; 10 \( \bot \), ∨E 2, 3–5, 6–9.
    - (f) True at once, with \( P \) and \( Q \) both false (\( P \): "\( 1 > 2 \)", \( Q \): "\( 2 > 3 \)"). Adding the fourth member \( \neg(\neg P \wedge \neg Q) \) would give a list from which \( \bot \) can be derived: the four exclude every way for \( P \) and \( Q \) to be. The solution gives the 4-member derivation in one sentence: LEM on \( P \) and on \( Q \), each of the four cases clashing with one member.
  - Last sentence of the solution, a plain pointer: "Section 4.7 shows that a list made true at once, as in (b), (d), (f), is consistent."
- **C1** `[C1: Exit check: the counterexample set]`. Stem: "Let \( \Gamma \) be the list \( P \to (Q \vee R), \ Q \to S, \ R \to S \). (a) Write the counterexample set of \( \Gamma \vdash P \to S \). (b) Show that it is inconsistent. (c) What does @prp-derivable-iff-negation-inconsistent conclude? Give also a direct derivation of \( \Gamma \vdash P \to S \), and compare the two. (d) Replace one premise so that the claim breaks, and break it."
  - *Answer.*
    - (a) \( P \to (Q \vee R), \ Q \to S, \ R \to S, \ \neg(P \to S) \).
    - (b) The goal is \( \bot \), and the clash partner \( \neg(P \to S) \) is on a line, so aim at \( P \to S \): 5 | \( P \); 6 | \( Q \vee R \), →E 1, 5; 7 | | \( Q \); 8 | | \( S \), →E 2, 7; 9 | | \( R \); 10 | | \( S \), →E 3, 9; 11 | \( S \), ∨E 6, 7–8, 9–10; 12 \( P \to S \), →I 5–11; 13 \( \bot \), ¬E 12, 4.
    - (c) By (b) of the proposition, \( \Gamma \vdash P \to S \). The direct derivation is lines 1–3 and 5–12 of (b), renumbered: 11 lines. The route through the counterexample set adds the premise \( \neg(P \to S) \) and one ¬E line, and gains nothing here. It pays when the goal gives step 2 nothing (a letter, or a disjunction with no side in hand), and then it is step 5.
    - (d) For instance, replace \( R \to S \) by \( R \to T \). With \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)", \( R \): "\( x < 2 \)", \( S \): "\( x > 3 \)", \( T \): "\( x < 10 \)", at \( x = 1 \): \( P \to (Q \vee R) \) is true, \( Q \to S \) is true (\( Q \) false), \( R \to T \) is true, and \( P \to S \) is false. Any replacement that a choice of statements breaks is accepted.
  - **Marking scheme.** (10 points)
    - 2: the counterexample set, with \( \neg(P \to S) \), not \( \neg P \to S \) or \( P \to \neg S \).
    - 3: the derivation of \( \bot \): \( P \to S \) built by a box, the cases of \( Q \vee R \) both ending in \( S \), ¬E outside every box.
    - 2: the conclusion drawn by the proposition, and the direct derivation.
    - 3: (d), a changed premise with statements checked against all four members of the new counterexample set.
    - Fatal errors (0 for the step): \( \bot \) written inside the box of \( P \) and taken as the end; a "break" in (d) that leaves a premise false.
- **C2** `[C2: Challenge: Splitting an inconsistency, used later]`. Stem: "Let \( \Gamma \) be a list and \( \varphi \) a statement. (a) Prove that if \( \Gamma, \varphi \) and \( \Gamma, \neg\varphi \) are both inconsistent, then so is \( \Gamma \). (b) Deduce: if \( \Gamma \) is consistent, then at least one of \( \Gamma, \varphi \) and \( \Gamma, \neg\varphi \) is consistent. (c) Does (b) say which one?"
  - *Answer.*
    - (a) By @prp-derivable-iff-negation-inconsistent (a), \( \Gamma \vdash \neg\varphi \). By (b), \( \Gamma \vdash \varphi \). So (iii) of @prp-inconsistent-derives-everything holds with \( \chi = \varphi \), and \( \Gamma \) is inconsistent.
    - (b) This is the contrapositive of (a): if both were inconsistent, \( \Gamma \) would be.
    - (c) No. It says that one of the two lists is consistent and gives no way to tell which. Deciding that would need a way to show a list consistent, which this chapter does not have.
  - The solution's last sentence (plain pointer): "Section 4.10 (optional) adds statements to a consistent list one at a time, in exactly this way."
  - **Marking scheme.** (10 points)
    - 4: (a) uses both parts of the proposition, (a) for \( \neg\varphi \) and (b) for \( \varphi \).
    - 3: (a) concludes by @prp-inconsistent-derives-everything or by @lem-weakening-cut (c) with one ¬E.
    - 2: (b) as the contrapositive.
    - 1: (c) "no".
    - Fatal error: (b) claimed to show that a particular list is consistent.
  - **Used later:** 4.10's Lindenbaum step recalls it (§6).

**Sidecars:** `exm-inconsistency-search.py`, `exm-derive-or-break-search.py`, `exr-four-kinds-of-task-b3.py`, `-b4.py`, `-c1.py` (§3.3). **Ledger lines:**
- `exm-inconsistency-search`: the readings of (1)–(4); \( 6 \), \( 1 \), \( 3 \), \( 12 \), each meeting three conditions (sidecar); the Quick check's \( 3 \), \( 9 \).
- `exm-derive-or-break-search`: at \( x = 2 \) (sidecar).
- `exm-equivalence-search`: the \( ab = 0 \) reading, "divide by \( a \)" (school algebra, AN1.1 promised, used only as a reading).
- `prp-*`: the proofs cite `lem-weakening-cut` (Section 2.3, after ch02-deepen) and `def-derivation` (cited).
- The gallery's second row cites `lem-not-iff-own-negation` (Section 2.4, after ch02-deepen).

### 4.3 Section 3.3: From Argument to Derivation (`03-from-argument-to-derivation.md`, new)

**Purpose.** To start from what mathematics actually supplies, a paragraph, and turn it into a sequent and a derivation; and in the other direction, to set a written proof beside the derivation it mirrors. The section also gives the one-page library of standard sequents grouped by use, the chapter's battery, its R items, and the question the chapter cannot answer. **Kind:** N. [Technique: Ho, Hu (argument extraction, suppressed premises); LB, Sm (one fixed key, reading back); LPL, Le (the informal proof first, then the mirroring derivation); Le, LB (a numbered library, regrouped by fd1's moves); Si, vD, En (pictures where the structure is spatial); Hu (dialogue extraction); Co (Curry).] **Sources in fd1:** plan §3.2 "2.7", second half; plan §3.6 item 6.4 (argument extraction), moved here by layout §6.1 and §6.3 and only recalled in 8.4. Everything is **newly written**, except the three moved R items.

**Budget:** main line ≤ 3,400. Expected about 2,300:
- opening 120;
- the key 240;
- extracting 610;
- Not allowed 150;
- two columns 390;
- library 540;
- Looking ahead 60;
- links 190.

Folds: none planned (budget ≤ 150 in reserve). One forward pointer, the Looking-ahead box (item 9), which carries the chapter's closing question (layout §1.3).

**What the section teaches, in order.**

1. **Opening** (~120 words). Sections 3.1 and 3.2 started from a sequent, with its letters, premises and conclusion given. Mathematics starts from a paragraph. Its premises are scattered among words such as "since" and "so"; some of them are not written at all; and its letters must be chosen. This section turns paragraphs into sequents, and then writes a proof beside its derivation. One last page collects the sequents that searches keep needing.
2. **`## One key for the section`** (~200 words and a Quick check). [D7; seam with Section 1.1 B5.]
   - Lead: "Section 1.1, Exercise B5, fixed one key for an integer \( n \), and this section keeps it: \( E \): '\( n \) is even', \( P \): '\( n \) is prime', \( T \): '\( n \) is a multiple of \( 3 \)', \( G \): '\( n > 10 \)' (@exr-statements-and-connectives-b5)."
   - Then the three facts, a display list, each with its English and its reason. "A prime is an integer greater than \( 1 \) whose only positive divisors are \( 1 \) and itself", stated once.
     - **F1** \( (P \wedge E) \to \neg G \): an even prime is at most \( 10 \). The only even prime is \( 2 \): an even \( n > 2 \) has the divisor \( 2 \).
     - **F2** \( (P \wedge T) \to \neg G \): a prime multiple of \( 3 \) is at most \( 10 \). The only one is \( 3 \): a multiple of \( 3 \) greater than \( 3 \) has the divisor \( 3 \).
     - **F3** \( (E \wedge T) \to \neg P \): no even multiple of \( 3 \) is prime. It is a multiple of \( 6 \); a positive multiple of \( 6 \) has the divisor \( 2 \) and is greater than \( 2 \), and \( 0 \) and the negative integers are not prime.
   - One sentence: "Each fact is true for every integer \( n \). An argument may use any of them as a premise, and a derivation lists the ones it uses."
   - One sentence on **reading back** (Section 1.1): "A translation is checked by reading it back, letter by letter: F3 reads back as 'if \( n \) is even and a multiple of \( 3 \), then \( n \) is not prime'."
   - **Quick check (new, ~40 words):** "On the key, translate '\( n \) is an odd prime greater than \( 10 \)'; then read back \( G \to \neg(P \wedge E) \)." *Solution:* \( (\neg E \wedge P) \wedge G \). And "if \( n > 10 \), then \( n \) is not an even prime".
3. **`## Extracting an argument`** (~220 words of method, the example, a figure, and a Quick check). [Named move: *Name the unstated fact*.]
   - The method, a numbered list (~160 words):
     1. *Find the conclusion.* Words such as *so*, *hence*, *therefore*, *thus*, *it follows that* introduce it.
     2. *Find the stated premises.* Words such as *since*, *because*, *for*, *given that* introduce them. A supposition ("suppose", "let \( n \) be …") is a premise, or the assumption of a box.
     3. *Name the unstated facts.* Wherever a step does not follow by a rule from the lines before it, write the fact that would make it follow, as an implication, and check that the fact is true. Supply the weakest fact that closes the gap: a stronger one may prove more than the paragraph claims, or be false. (Compare Section 1.3, Exercise B5 (d), where a missing implication was written and checked. The advice to choose the weakest such fact is new here; S2 round 1 dropped the S1 attribution.)
     4. *Translate on a key*, with Section 1.1's phrase book.
     5. *Derive the sequent, or break it.*
   - Lead-out sentence: "Steps 1–4 are reading. Step 5 is the rest of this book."
   - **`exm-extract-argument`** `[An argument about a prime, extracted]` (~330 words).
     - Statement: "Extract the argument of this paragraph and derive it. *Let \( n \) be an integer, and suppose that \( n \) is a prime greater than \( 10 \). Then \( n \) is odd, since the only even prime is \( 2 \). Nor is \( n \) a multiple of \( 3 \), because the only prime that is a multiple of \( 3 \) is \( 3 \) itself. So \( n \) is neither even nor a multiple of \( 3 \).*"
     - *Solution*, by the five steps:
       1. The conclusion follows "So": \( n \) is neither even nor a multiple of \( 3 \), that is, \( \neg E \wedge \neg T \) ("neither … nor", Section 1.1's phrase book).
       2. The stated premise is the supposition, "\( n \) is a prime greater than \( 10 \)": \( P \wedge G \), since "a prime greater than \( 10 \)" is a conjunction. "\( n \) is odd" and "nor is \( n \) a multiple of \( 3 \)" are not premises. They are steps, each with a reason after "since" or "because".
       3. The reasons are facts about numbers, but not in a form a rule can use. "The only even prime is \( 2 \)" is used as "an even prime is not greater than \( 10 \)", which is F1; the second reason is used as F2.
       4. The sequent is \( F1, \ F2, \ P \wedge G \vdash \neg E \wedge \neg T \), with F1 and F2 written out.
       5. A derivation, read off the goal: two ¬I boxes joined by ∧I, as in Section 3.1.
     - **S1:** premises 1 \( P \wedge G \), 2 \( (P \wedge E) \to \neg G \), 3 \( (P \wedge T) \to \neg G \); 4 \( P \), ∧E 1; 5 \( G \), ∧E 1; gap; 10 \( \neg E \), unjustified; gap; 15 \( \neg T \), unjustified; 16 \( \neg E \wedge \neg T \), ∧I 10, 15.
     - **S2:** lines 1–5; box 6 \( E \), asm; gap; 9 | \( \bot \), unjustified; 10 \( \neg E \), ¬I 6–9; box 11 \( T \), asm; gap; 14 | \( \bot \), unjustified; 15 \( \neg T \), ¬I 11–14; 16.
     - **Finished (16 lines):** S2 with 7 | \( P \wedge E \), ∧I 4, 6; 8 | \( \neg G \), →E 2, 7; 9 | \( \bot \), ¬E 5, 8; 12 | \( P \wedge T \), ∧I 4, 11; 13 | \( \neg G \), →E 3, 12; 14 | \( \bot \), ¬E 5, 13.
     - Aftermath (~45 words): "Lines 4–5 need nothing new and are written before the boxes (Section 3.1). Had the supposition been kept as a supposition, the claim would be \( F1, F2 \vdash (P \wedge G) \to (\neg E \wedge \neg T) \): the same lines inside one more box, closed by →I."
   - **Figure 3.3-F** (after the example). Lead (~30 words): "The argument as a map: each statement a dot, each step an arrow into what it gives. The unstated facts are the dots nobody wrote."
     - Template `structure`.
     - `elt` nodes:
       - (f1) at (0,2.4), `label=above:{F1 (unstated)}`;
       - (g) at (2,2.4), `label=above:{$P \wedge G$ (given)}`;
       - (f2) at (4,2.4), `label=above:{F2 (unstated)}`;
       - (e) at (1,1.2), `label=left:{$\neg E$}`;
       - (t) at (3,1.2), `label=right:{$\neg T$}`;
       - (c) at (2,0), `label=below:{$\neg E \wedge \neg T$}`.
     - `rel` arrows: f1→e, g→e, g→t, f2→t, e→c, t→c.
     - No caption beyond the lead. (A map of support, not of a derivation's lines: it leaves out the boxes, and the text says so in the lead's second sentence if S4 finds the picture read as a derivation.)
   - **Quick check (new, ~30 words):** "Which line of the derivation in @exm-extract-argument is the paragraph's sentence 'Then \( n \) is odd', and which lines does the paragraph leave silent?" *Solution:* Line 10. The paragraph is silent on lines 4–9, the box that shows it, apart from the reason F1 behind line 8.
4. **Not allowed** (after the Quick check; ~150 words): warning `[Not allowed: extracting an argument]`, one line each, tagged with the step it breaks:
   - "Writing '\( n \) is odd' among the premises" (step 2): a step taken as a premise. The derivation then proves nothing about whether \( n \) is odd.
   - "Reading '\( n \) is odd, since \( n \) is a prime greater than \( 10 \)' with '\( n \) is odd' as the premise" (steps 1–2): *since* introduces the premise, not the conclusion.
   - "Supplying 'every prime is odd' for the first step" (step 3): the supplied fact must be true, and this one fails at \( n = 2 \).
   - "Supplying \( \neg E \wedge \neg T \) itself as the unstated fact" (step 3): the derivation is legal and proves nothing. Supply the weakest fact that closes the gap.
   - "Translating '\( n \) is a prime greater than \( 10 \)' as \( P \to G \)" (step 4): a noun with an adjective is a conjunction, \( P \wedge G \) (Section 1.1).
5. **`## Two columns`** (~390 words with the table and a Quick check). [Named move: *Two columns*.]
   - Lead (~70 words): "The other direction: a proof is written, and its derivation is wanted. Write the proof in the left column and the derivation in the right, each sentence on the row of the lines it says. A line that no sentence says is a **silent step**; a sentence that matches no line is a gap in the proof, or a step this book's rules cannot take."
   - **`exm-two-columns`** `[A proof and its derivation, side by side]`.
     - Statement: "Let \( n \) be an integer. Claim: if \( n \) is even and prime, then \( n \) is not a multiple of \( 3 \). Proof: *Suppose \( n \) is even and prime. If \( n \) were a multiple of \( 3 \), it would be an even multiple of \( 3 \), and no even multiple of \( 3 \) is prime; but \( n \) is prime. So \( n \) is not a multiple of \( 3 \).* Write the derivation the proof mirrors, in two columns."
     - Solution: the sequent is \( F3 \vdash (E \wedge P) \to \neg T \).
     - **S1:** 1 \( (E \wedge T) \to \neg P \); box 2 \( E \wedge P \), asm; gap; 9 | \( \neg T \), unjustified; 10 \( (E \wedge P) \to \neg T \), →I 2–9.
     - **S2:** 1; 2; 3 | \( E \), ∧E 2; 4 | \( P \), ∧E 2; box 5 \( T \), asm; gap; 8 | | \( \bot \), unjustified; 9 | \( \neg T \), ¬I 5–8; 10.
     - Then the two-column table (columns *The proof* | *The derivation*), eight rows:
       - "Suppose \( n \) is even and prime." | 2 \( E \wedge P \), asm, for →I
       - (silent) | 3 \( E \), 4 \( P \), ∧E 2
       - "If \( n \) were a multiple of \( 3 \)," | 5 \( T \), asm, for ¬I
       - "it would be an even multiple of \( 3 \)," | 6 \( E \wedge T \), ∧I 3, 5
       - "and no even multiple of \( 3 \) is prime;" | 1 \( (E \wedge T) \to \neg P \), F3; 7 \( \neg P \), →E 1, 6
       - "but \( n \) is prime." | 8 \( \bot \), ¬E 4, 7
       - "So \( n \) is not a multiple of \( 3 \)." | 9 \( \neg T \), ¬I 5–8
       - (the claim) | 10 \( (E \wedge P) \to \neg T \), →I 2–9
     - (The table is the finished derivation; no separate `nd` block is needed. If S4 wants `check_fitch.py` to see it, the finished derivation is also typeset after the table.)
     - Aftermath (~50 words): "The proof says lines 2 and 5–9. It is silent on lines 3–4, taking the conjunction apart, and on line 10, since closing the outer box is the claim itself. Its 'Suppose' is line 2's 'asm, for →I', and its 'If \( n \) were' is line 5's 'asm, for ¬I'. The proof hides the fact F3 in a clause; the derivation lists it."
   - **Quick check (new, ~45 words):** "If the claim in @exm-two-columns were 'if \( n \) is even and prime, then \( n \) is at most \( 10 \)', which fact would replace F3, and what would happen to the box of line 5?" *Solution:* F1 replaces F3. The box of line 5 disappears: the goal \( \neg G \) is F1's conclusion, so after ∧E and ∧I give \( P \wedge E \), one →E line reaches it.
6. **`## A library of standard sequents`** (heading id `a-library-of-standard-sequents`; ~120 words of lead and a table of ~420 words). [Technique: Le, LB (a library cited by name), regrouped by fd1's moves; Critic small correction 7.]
   - **Lead** (~120 words): "Chapters 1 and 2 and Section 3.2 proved sequents that searches keep needing. Here they are grouped by what they are for: a searcher with a resource or a goal of a given shape looks up its row. Each row is a derived rule (@def-derived-rule). It is applied to **whole** available lines, never to a part of a line, and it is cited by the name in its middle column. 'The rules in one place' in Section 3.1 lists the same rules by the chapter that proved them; this page lists them by use. The last group is different: it holds facts about derivations, which change the task rather than add a line."
   - **The table** (columns *Sequent* | *In a justification* | *Proved in*; each group a bold row):
     - **To use an implication**
       - \( P \to Q, \ \neg Q \vdash \neg P \) | \( \rulename{MT} \) | @prp-modus-tollens
       - \( P \to Q, \ Q \to R \vdash P \to R \) | (implication is transitive) | @prp-implication-transitive
       - \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \) | (curry) | @prp-curry
       - \( P \to Q \vdash \neg P \vee Q \) | (implication as disjunction) | @prp-implication-as-disjunction (b)
     - **To use a disjunction**
       - \( P \vee Q, \ \neg P \vdash Q \); \( P \vee Q, \ \neg Q \vdash P \) | \( \rulename{DS} \) | @prp-disjunctive-syllogism; @exr-derived-rules-b1 (a)
       - \( (P \to R) \wedge (Q \to R) \dashv\vdash (P \vee Q) \to R \) | (cases on a hypothesis) | @exm-cases-on-hypothesis; @exm-or-hypothesis-split
       - \( (P \to R) \wedge (Q \to S), \ P \vee Q \vdash R \vee S \) | (constructive dilemma) | @exm-constructive-dilemma
     - **To use a negation or a clash**
       - \( P, \ \neg P \vdash Q \) | (ex falso) | @prp-ex-falso
       - \( \neg P \vdash P \to Q \) | VI | @prp-vacuous-implication
       - \( \neg\neg P \vdash P \) | \( \rulename{\neg\neg E} \) | @prp-double-negation (b)
       - \( \neg(P \vee Q) \vdash \neg P \wedge \neg Q \); \( \neg(P \wedge Q) \vdash \neg P \vee \neg Q \) | \( \rulename{DM} \) | @prp-de-morgan (a), (d)
     - **To reach a negation**
       - \( P \to Q \vdash \neg Q \to \neg P \) | \( \rulename{CP} \) | @prp-contrapositive
       - \( \vdash (P \to (Q \wedge \neg Q)) \to \neg P \) | (implies a contradiction) | @exm-theorem-search
       - \( \neg P \wedge \neg Q \vdash \neg(P \vee Q) \); \( \neg P \vee \neg Q \vdash \neg(P \wedge Q) \) | \( \rulename{DM} \) | @prp-de-morgan (b), (c)
       - \( P \vdash \neg\neg P \) | \( \rulename{\neg\neg I} \) | @prp-double-negation (a)
     - **To reach an implication**
       - \( \neg P \vee Q \vdash P \to Q \) | (implication as disjunction) | @prp-implication-as-disjunction (a)
       - \( \neg Q \to \neg P \vdash P \to Q \) | (\( \rulename{CP} \), converse) | @prp-contrapositive-converse
     - **To reach a disjunction**
       - \( \vdash P \vee \neg P \) | \( \rulename{LEM} \) | @prp-excluded-middle
       - \( (P \wedge \neg Q) \to R \dashv\vdash P \to (Q \vee R) \) | (refute one side) | @exm-equivalence-search
     - **To rearrange**
       - \( P \wedge Q \vdash Q \wedge P \); \( P \vee Q \vdash Q \vee P \) | (and commutes); (or commutes) | @prp-and-commutes; @exm-disjunction-first-derivations
       - \( (P \wedge Q) \wedge R \vdash P \wedge (Q \wedge R) \); \( P \vee (Q \vee R) \vdash (P \vee Q) \vee R \) | (and regroups); (or regroups) | @prp-and-associative; @exm-disjunction-regroup
       - \( P \wedge (Q \vee R) \dashv\vdash (P \wedge Q) \vee (P \wedge R) \) | (distributivity) | @prp-distributivity
       - \( P \leftrightarrow Q \vdash Q \leftrightarrow P \) | (iff symmetric) | @exm-iff-symmetric
       - \( P \leftrightarrow Q \dashv\vdash (P \to Q) \wedge (Q \to P) \) | (iff as two implications) | @prp-iff-two-implications
       - \( P \to Q, \ Q \to R, \ R \to P \vdash P \leftrightarrow Q \) | (equivalence cycle) | @prp-equivalence-cycle
     - **To change the task** (facts about derivations, not lines)
       - more premises never hurt; a derived statement may be used as a premise | (weakening, cut) | @lem-weakening-cut
       - \( \Gamma \vdash \varphi \) exactly when \( \Gamma, \neg\varphi \) is inconsistent | — | @prp-derivable-iff-negation-inconsistent
       - an inconsistent list derives every statement | — | @prp-inconsistent-derives-everything
   - One sentence after the table: "Rows proved in exercises (the second form of \( \rulename{DS} \)) may be used by exercises, as in Section 3.1; the text's own derivations use only rows proved in the text."
   - The groups and their order are fd1's own: by the resource or the goal a row serves, following the method's steps 3 and 2. No book's list or order is followed (§9, item 26).
   - **Quick check (new, ~40 words):** "Which row would you look up first? (i) The goal is \( \neg(P \vee Q) \). (ii) A resource is \( \neg(P \wedge Q) \), and the goal is \( \neg P \vee \neg Q \). (iii) Resources \( P \to Q \) and \( \neg Q \)." *Solution:* (i) \( \rulename{DM} \) (b), under "To reach a negation"; (ii) \( \rulename{DM} \) (d), which gives the goal in one line; (iii) \( \rulename{MT} \).
7. **Not repeated here**: the derive-or-break flowchart and the four-task table stay in 3.2. 3.3 recalls them in one sentence each where its battery and C items use them.
8. *(No rule card: there are no rules in this section.)*
9. **Looking ahead** (`::: {.remark}` `[Looking ahead]`, ~60 words, no `@ref`; R3 item 12's content, moved, with one word changed): "We show that something is derivable by exhibiting a derivation; how could we ever show that something is not? Chapter 4 gives each statement a truth value and proves that the rules never lead from true premises to a false conclusion. Then one choice of truth values, such as \( P \) false and \( Q \) true for the failed search of Section 3.1, proves that no derivation exists."
   - Ch04 index:3 and 01:3 open with this question; ch04 07:3 and 07:278 answer it.

**Quick checks:**
- the key (item 2);
- the silent lines (item 3);
- F1 for F3 (item 5);
- the library (item 6).

Four in ~2,300 words, about one per 600.

**Exercises.** There is no A2 bank: B3's battery replaces it (layout).

- **A1** (`exr-from-argument-to-derivation-a1`), five parts:
  - (a) In "Since \( n^2 \) is even, \( n \) is even", which is the premise and which the conclusion? — Premise: "\( n^2 \) is even". Conclusion: "\( n \) is even".
  - (b) Find the conclusion: "\( n \) is odd, for \( n \) is prime and greater than \( 10 \)." — "\( n \) is odd". *For* introduces the premise.
  - (c) Name the unstated fact: "\( n \) is a multiple of \( 6 \), so \( n \) is even." — Every multiple of \( 6 \) is even: if \( 6 \mid n \), then \( 2 \mid n \).
  - (d) On the key, translate "\( n \) is an odd prime at most \( 10 \)." — \( (\neg E \wedge P) \wedge \neg G \).
  - (e) In @exm-two-columns, which sentence of the proof is line 5, and what does line 5's annotation read? — "If \( n \) were a multiple of \( 3 \)"; "asm, for ¬I".
- **B1** `[B1: Extract, then derive]`. [Technique: Ho, Hu.] Stem: "For each paragraph, find the conclusion, the stated premises and any unstated fact; choose letters; write the sequent; derive it."
  - The paragraphs:
    - (a) "Let \( x \) be a real number with \( x^2 \le x \). If \( x \) were greater than \( 1 \), then \( x^2 = x \cdot x \) would be greater than \( x \). If \( x \) were negative, \( x^2 \) would be positive, hence greater than \( x \). So \( x \) is at least \( 0 \) and at most \( 1 \)."
    - (b) "Let \( n \) be an integer. Since \( n^2 \) is odd, \( n \) is odd."
    - (c) "Let \( a \) and \( b \) be real numbers with \( ab = 0 \). If \( a \ne 0 \), we may divide by \( a \) and find \( b = 0 \). So \( a = 0 \) or \( b = 0 \)."
  - *Answer.*
    - (a) Letters \( A \): "\( x > 1 \)", \( B \): "\( x < 0 \)", \( C \): "\( x^2 > x \)". The stated facts are \( A \to C \) and \( B \to C \), each with its reason. The premise "\( x^2 \le x \)" is \( \neg C \), by the convention of Section 2.1. The conclusion "at least \( 0 \) and at most \( 1 \)" is \( \neg B \wedge \neg A \) by the same convention, or \( \neg A \wedge \neg B \) (either order, with ∧I's citation order, NOTATION). The sequent is \( A \to C, \ B \to C, \ \neg C \vdash \neg A \wedge \neg B \): 4 \( \neg A \), MT 1, 3; 5 \( \neg B \), MT 2, 3; 6 \( \neg A \wedge \neg B \), ∧I 4, 5. Nothing is unstated except the order convention.
    - (b) Letters \( E \): "\( n \) is even", \( S \): "\( n^2 \) is even". The premise is \( \neg S \) and the conclusion \( \neg E \). The unstated fact is \( E \to S \), "the square of an even integer is even", true since \( (2k)^2 = 4k^2 = 2(2k^2) \). Derivation: 3 \( \neg E \), MT 1, 2.
      - The tempting wrong supply is "the square of an odd integer is odd", \( \neg E \to \neg S \). It is true, but with the premise \( \neg S \) it gives nothing: that step would be affirming the consequent (Section 1.3).
    - (c) Letters \( A \): "\( a = 0 \)", \( B \): "\( b = 0 \)", \( Z \): "\( ab = 0 \)". The stated fact is \( (Z \wedge \neg A) \to B \), dividing by \( a \): \( b = a^{-1}(ab) = 0 \). The premise is \( Z \) and the conclusion \( A \vee B \). Derivation, by step 5 (@exm-equivalence-search's pattern): 3 \( A \vee \neg A \), LEM; 4 | \( A \); 5 | \( A \vee B \), ∨I 4; 6 | \( \neg A \); 7 | \( Z \wedge \neg A \), ∧I 2, 6; 8 | \( B \), →E 1, 7; 9 | \( A \vee B \), ∨I 8; 10 \( A \vee B \), ∨E 3, 4–5, 6–9.
  - Worked example type: `exm-extract-argument`.
- **B2** `[B2: Two columns]` (scaffolded, STYLE §12.8). Stem: "Claim: if \( n \) is prime and \( n > 10 \), then \( n \) is not a multiple of \( 6 \). Proof: *Suppose \( n \) is prime and \( n > 10 \). If \( n \) were a multiple of \( 6 \), it would be an even multiple of \( 3 \), and no even multiple of \( 3 \) is prime; but \( n \) is prime. So \( n \) is not a multiple of \( 6 \).* (a) On the key, '\( n \) is a multiple of \( 6 \)' is \( E \wedge T \). The derivation the proof mirrors has reached the stage below. *Name the move, then complete it.* (b) Write the two-column table. (c) Which hypothesis does the derivation never cite? What claim does that show, and is it true?"
  - The scaffold: 1 \( (E \wedge T) \to \neg P \); box 2 \( P \wedge G \), asm `\purpose{\ii}`; gap; 7 | \( \neg(E \wedge T) \), unjustified; 8 \( (P \wedge G) \to \neg(E \wedge T) \), →I 2–7.
  - *Answer.*
    - (a) The goal \( \neg(E \wedge T) \) is a negation, so step 2 opens a ¬I box on \( E \wedge T \). F3 fires on it, and the clash partner \( P \) comes from line 2. Lines: 3 | \( P \), ∧E 2; 4 | | \( E \wedge T \), asm; 5 | | \( \neg P \), →E 1, 4; 6 | | \( \bot \), ¬E 3, 5; 7 | \( \neg(E \wedge T) \), ¬I 4–6; 8.
    - (b) The two columns:
      - "Suppose \( n \) is prime and \( n > 10 \)." | 2
      - (silent) | 3
      - "If \( n \) were a multiple of \( 6 \)," | 4
      - "it would be an even multiple of \( 3 \), and no even multiple of \( 3 \) is prime;" | 1 (F3), 5. Line 4 already is \( E \wedge T \), so "an even multiple of \( 3 \)" is a rereading, not a step.
      - "but \( n \) is prime." | 6
      - "So \( n \) is not a multiple of \( 6 \)." | 7
      - (the claim) | 8
    - (c) \( G \) (that is, \( n > 10 \)) is never cited: no line uses it. Lines 3–7, with \( P \) as the box's assumption, derive \( F3 \vdash P \to \neg(E \wedge T) \): no prime is a multiple of \( 6 \). That is true for every integer, by F3. The hypothesis \( n > 10 \) was idle.
- **B3** `[B3: Fifteen items]` (the battery, in place of an A2 bank; counted as four exercises for Time, by the drill rule). Stem: "Items 1–5: derive each sequent, using a row of the library where it shortens the derivation, and name the row. Items 6–10: translate on the key, using the facts F1–F3 as premises where needed, and derive. Items 11–15: derive or break. The facts may be used as premises. A break is an integer \( n \) at which the premises are true and the conclusion false; since F1–F3 hold at every \( n \), such an \( n \) makes the whole counterexample set true."
  - *Derive, with the library.*
    1. \( \neg(P \vee Q) \vdash P \to R \).
    2. \( P \vee Q, \ P \to R, \ \neg R \vdash Q \wedge \neg P \).
    3. \( \neg(P \wedge \neg Q) \vdash P \to Q \).
    4. \( (P \vee Q) \to R \vdash \neg R \to (\neg P \wedge \neg Q) \).
    5. \( \neg P \to Q, \ \neg Q \vdash P \wedge (\neg Q \vee R) \).
  - *Translate on the key, then derive.*
    6. "\( n \) is an even multiple of \( 3 \); so \( n \) is not prime, and \( n \) is not a prime greater than \( 10 \)."
    7. "\( n \) is a prime at most \( 10 \), or \( n \) is odd; so if \( n \) is even, \( n \) is at most \( 10 \)."
    8. "\( n \) is a prime multiple of \( 3 \); so \( n \) is at most \( 10 \), and \( n \) is odd."
    9. "\( n \) is prime; \( n \) is not a multiple of \( 3 \) or \( n \) is at most \( 10 \); and \( n \) is a multiple of \( 3 \). So \( n \) is at most \( 10 \)."
    10. "If \( n \) is greater than \( 10 \), then \( n \) is not an even prime."
  - *Derive or break.*
    11. "\( n \) is even but not a multiple of \( 3 \); so \( n \) is not prime."
    12. "\( n \) is an even prime; so \( n \) is at most \( 10 \)."
    13. "\( n \) is odd and greater than \( 10 \); so \( n \) is prime."
    14. "\( n \) is odd; so \( n \) is not an even prime."
    15. "\( n \) is not prime; so \( n \) is even or a multiple of \( 3 \)."
  - *Answers:*
    1. 2 \( \neg P \wedge \neg Q \), DM 1; 3 \( \neg P \), ∧E 2; 4 \( P \to R \), VI 3.
    2. 4 \( \neg P \), MT 2, 3; 5 \( Q \), DS 1, 4; 6 \( Q \wedge \neg P \), ∧I 5, 4.
    3. 2 | \( P \); 3 | | \( \neg Q \), asm; 4 | | \( P \wedge \neg Q \), ∧I 2, 3; 5 | | \( \bot \), ¬E 4, 1; 6 | \( Q \), RAA 3–5; 7 \( P \to Q \), →I 2–6. The library route (DM (d), then ¬¬I, DS and ¬¬E inside the box) is no shorter. The solution says so: a library row is worth citing only when it saves lines.
    4. 2 | \( \neg R \); 3 | \( \neg(P \vee Q) \), MT 1, 2; 4 | \( \neg P \wedge \neg Q \), DM 3; 5 \( \neg R \to (\neg P \wedge \neg Q) \), →I 2–4.
    5. 3 \( \neg\neg P \), MT 1, 2; 4 \( P \), ¬¬E 3; 5 \( \neg Q \vee R \), ∨I 2; 6 \( P \wedge (\neg Q \vee R) \), ∧I 4, 5.
    6. \( E \wedge T, \ F3 \vdash \neg P \wedge \neg(P \wedge G) \): 3 \( \neg P \), →E 2, 1; 4 | \( P \wedge G \); 5 | \( P \), ∧E 4; 6 | \( \bot \), ¬E 5, 3; 7 \( \neg(P \wedge G) \), ¬I 4–6; 8 \( \neg P \wedge \neg(P \wedge G) \), ∧I 3, 7.
    7. \( (P \wedge \neg G) \vee \neg E \vdash E \to \neg G \), with no fact needed: 2 | \( E \); 3 | | \( P \wedge \neg G \); 4 | | \( \neg G \), ∧E 3; 5 | | \( \neg E \); 6 | | \( \bot \), ¬E 2, 5; 7 | | \( \neg G \), ⊥E 6; 8 | \( \neg G \), ∨E 1, 3–4, 5–7; 9 \( E \to \neg G \), →I 2–8.
    8. \( P \wedge T, \ F2, \ F3 \vdash \neg G \wedge \neg E \): 4 \( \neg G \), →E 2, 1; 5 \( P \), ∧E 1; 6 \( T \), ∧E 1; 7 | \( E \); 8 | \( E \wedge T \), ∧I 7, 6; 9 | \( \neg P \), →E 3, 8; 10 | \( \bot \), ¬E 5, 9; 11 \( \neg E \), ¬I 7–10; 12 \( \neg G \wedge \neg E \), ∧I 4, 11.
    9. \( P, \ \neg T \vee \neg G, \ T \vdash \neg G \): 4 \( \neg\neg T \), ¬¬I 3; 5 \( \neg G \), DS 2, 4. The premise \( P \) is not needed.
    10. \( F1 \vdash G \to \neg(P \wedge E) \): 2 | \( G \); 3 | | \( P \wedge E \); 4 | | \( \neg G \), →E 1, 3; 5 | | \( \bot \), ¬E 2, 4; 6 | \( \neg(P \wedge E) \), ¬I 3–5; 7 \( G \to \neg(P \wedge E) \), →I 2–6. (Or 3 \( \neg\neg G \), ¬¬I 2; 4 \( \neg(P \wedge E) \), MT 1, 3.)
    11. Breaks at \( n = 2 \): even, not a multiple of \( 3 \), and prime.
    12. Derive: 3 \( \neg G \), →E 2, 1 (premises 1 \( P \wedge E \), 2 F1).
    13. Breaks at \( n = 15 \): odd, greater than \( 10 \), not prime.
    14. Derive: 2 | \( P \wedge E \); 3 | \( E \), ∧E 2; 4 | \( \bot \), ¬E 3, 1; 5 \( \neg(P \wedge E) \), ¬I 2–4. No fact is needed.
    15. Breaks at \( n = 25 \): not prime, odd, not a multiple of \( 3 \).
  - Closing sentence: (11)/(12) and (13)/(14) pair a break with a derivation on nearby words; (15) reverses F3's direction.
- **B4** `[B4: Put the proof in order]` (the chapter's proof-ordering item, STYLE §11.4). Stem: "Let \( a \) and \( b \) be real numbers. Claim: if \( a + b > 2 \), then \( a > 1 \) or \( b > 1 \). (a) Put six of these sentences in an order that proves the claim; two do not belong. (b) Match each sentence of your order to a line of the derivation below, with \( A \): '\( a > 1 \)', \( B \): '\( b > 1 \)', \( S \): '\( a + b > 2 \)'."
  - The sentences:
    - (i) "This contradicts \( a + b > 2 \)."
    - (ii) "Suppose \( a + b > 2 \)."
    - (iii) "Then \( a > 1 \), since \( a + b > 2 \)."
    - (iv) "Adding, \( a + b \le 2 \)."
    - (v) "Hence \( a > 1 \) or \( b > 1 \)."
    - (vi) "Suppose, for a contradiction, that neither \( a > 1 \) nor \( b > 1 \)."
    - (vii) "Suppose \( a > 1 \) or \( b > 1 \)."
    - (viii) "Then \( a \le 1 \) and \( b \le 1 \)."
  - The derivation (given): 1 \( (\neg A \wedge \neg B) \to \neg S \), a fact; 2 | \( S \), asm; 3 | | \( \neg(A \vee B) \), asm; 4 | | \( \neg A \wedge \neg B \), DM 3; 5 | | \( \neg S \), →E 1, 4; 6 | | \( \bot \), ¬E 2, 5; 7 | \( A \vee B \), RAA 3–6; 8 \( S \to (A \vee B) \), →I 2–7.
  - *Answer.*
    - (a) (ii), (vi), (viii), (iv), (i), (v). No other order is admissible: each sentence uses the one before it. The distractors:
      - (iii) does not follow: \( a = 0 \), \( b = 3 \) has \( a + b > 2 \) and \( a \le 1 \).
      - (vii) assumes the conclusion, a box opened on the goal (Section 3.1's warning "Do not assume what you want to prove").
    - (b) (ii) ↔ 2 (asm, for →I); (vi) ↔ 3 (asm, for RAA); (viii) ↔ 4, by DM and the order convention (\( \neg(a > 1) \) is \( a \le 1 \)); (iv) ↔ 5, with the fact on line 1, adding the two inequalities; (i) ↔ 6; (v) ↔ 7. The claim is line 8. The fact on line 1 is the one step of school algebra: \( a \le 1 \) and \( b \le 1 \) give \( a + b \le 2 \).
- **C1** `[C1: Exit check: from a paragraph to a derivation]`. Stem: "*Let \( n \) be an integer greater than \( 10 \), and suppose \( n \) is even or a multiple of \( 3 \). Then \( n \) is not prime. Indeed, suppose \( n \) were prime. If \( n \) is even, \( n \) is an even prime, and every even prime is at most \( 10 \). If \( n \) is a multiple of \( 3 \), \( n \) is a prime multiple of \( 3 \), and every such number is at most \( 10 \). Either way \( n \) is at most \( 10 \), which is false. So \( n \) is not prime.*"
  - The parts:
    - (a) Name the conclusion, the stated premises, and the facts the paragraph gives as reasons, each on the key.
    - (b) Write the sequent.
    - (c) Derive it.
    - (d) Write the two-column table.
    - (e) Is the premise "\( n > 10 \)" needed? Break the claim without it.
  - *Answer.*
    - (a) The conclusion is \( \neg P \). The premises are \( G \) and \( E \vee T \). The facts are F1 ("every even prime is at most \( 10 \)") and F2.
    - (b) \( G, \ E \vee T, \ F1, \ F2 \vdash \neg P \).
    - (c) 1 \( G \); 2 \( E \vee T \); 3 \( (P \wedge E) \to \neg G \); 4 \( (P \wedge T) \to \neg G \); 5 | \( P \), asm; 6 | | \( E \), asm; 7 | | \( P \wedge E \), ∧I 5, 6; 8 | | \( \neg G \), →E 3, 7; 9 | | \( T \), asm; 10 | | \( P \wedge T \), ∧I 5, 9; 11 | | \( \neg G \), →E 4, 10; 12 | \( \neg G \), ∨E 2, 6–8, 9–11; 13 | \( \bot \), ¬E 1, 12; 14 \( \neg P \), ¬I 5–13.
    - (d) The two columns:
      - "Let \( n \) … greater than \( 10 \), and suppose \( n \) is even or a multiple of \( 3 \)." | 1, 2
      - "Then \( n \) is not prime." | the goal, line 14
      - "suppose \( n \) were prime." | 5 (asm, for ¬I)
      - "If \( n \) is even, … at most \( 10 \)." | 6–8 with 3
      - "If \( n \) is a multiple of \( 3 \), … at most \( 10 \)." | 9–11 with 4
      - "Either way \( n \) is at most \( 10 \)," | 12
      - "which is false." | 13
      - "So \( n \) is not prime." | 14
    - (e) It is needed. Without \( G \), the claim \( E \vee T, \ F1, \ F2 \vdash \neg P \) breaks at \( n = 2 \): even, so \( E \vee T \) holds; F1 and F2 hold, as at every \( n \); and \( 2 \) is prime.
  - **Marking scheme.** (10 points)
    - 2: (a)–(b), the sequent, with F1 and F2 named as unstated (or stated-as-reason) facts in implication form.
    - 3: (c), the ¬I box on \( P \), the two cases both ending in \( \neg G \), and the clash with \( G \) outside the cases.
    - 2: (d), every sentence placed, the two "suppose"s matched to their annotations.
    - 3: (e), "needed", with a break that makes every member of the new counterexample set true.
    - Fatal errors (0 for the step): \( \neg P \) taken as a premise; the cases of ∨E ending in different statements; a "break" in (e) at an \( n \) where a premise fails.
    - A derivation that splits \( E \vee T \) first and opens a ¬I box in each case earns full marks for (c).
- **C2** `[C2: Challenge: A statement that promises anything]`. [Technique: Co (Curry's paradox in a natural-deduction system), in fd1's own dress.] Stem: "(a) Derive \( C \leftrightarrow (C \to Q) \vdash Q \). (b) Let \( Q \) be '\( 0 = 1 \)'. What does (a) say about a statement \( C \) that is equivalent to 'if \( C \), then \( 0 = 1 \)'? (c) Which rules does your derivation use? Compare @lem-not-iff-own-negation."
  - *Answer.*
    - (a) (Detour-free, S2 round 1.) 2 | \( C \), asm; 3 | \( C \to Q \), ↔E 1, 2; 4 | \( Q \), →E 3, 2; 5 \( C \to Q \), →I 2–4; 6 \( C \), ↔E 1, 5; 7 \( C \to Q \), ↔E 1, 6; 8 \( Q \), →E 7, 6.
      - The solution adds two sentences: "The shorter ending 7 \( Q \), →E 5, 6 is a detour: line 5 was built by →I and is taken apart at once. Cutting it costs a line here, because line 5 is cited again at line 6, so it stays. This is the case Section 3.1 names: cutting a detour need not shorten a derivation, and the rule is advice, not a theorem." (S2 round 2: the sentence now cites the clause of 3.1's detour paragraph.)
    - (b) Read as an argument, the derivation proves \( 0 = 1 \) from the condition on \( C \). So no statement can meet the condition. In this chapter's words, the list \( C \leftrightarrow (C \to Q), \ \neg Q \) is inconsistent: add 9 \( \bot \), ¬E 8, \( \neg Q \).
    - (c) Only ↔E, →I and →E: no rule for \( \neg \) or \( \bot \), and no RAA. @lem-not-iff-own-negation shows that no statement is equivalent to its own negation; this shows more, for "if \( C \), then \( Q \)" with any \( Q \), and without "not". The trouble is self-reference, not negation. The solution names the item: "This is known as Curry's paradox, after the logician whose name is also on the law @prp-curry." Plain pointer: "Section 5.6 meets the same shape with 'for every', in the barber and Russell's theorem."
  - **Marking scheme.** (10 points)
    - 4: (a), the box on \( C \) (lines 2–4, with the assumption \( C \) cited twice), \( C \) recovered outside it by ↔E (line 6), and \( Q \) reached outside every box. The 7-line ending →E 5, 6 earns full marks; the detour remark is not required.
    - 3: (b), the conclusion that no statement meets the condition, with the inconsistency.
    - 3: (c), the rules named, and the point that no negation rule is used.
    - Fatal error: \( Q \) obtained inside the box and carried out of it.
- **R1, R2**: `exr-finding-derivations-r1`, `-r2`, moved verbatim from 01:1145–1199 (labels and prefix kept; layout §1.4).
- **R3**: `exr-finding-derivations-r3`, moved from 01:1201–1235. Its solution's last paragraph combines R3's change (no `@ref`) with layout G10.
  - Was: "The converse is not derivable, but a search can only stall, not show it. … Chapter 4 proves that such a row rules out every derivation (@cor-refuting-row): the chapter's open question, in a new place."
  - Becomes (S2 round 1, G10): "The converse breaks: with \( P \) and \( R \) false (and \( Q \) either way), the premise \( P \to (Q \to R) \) is true because \( P \) is false, while \( P \to Q \) is true and \( R \) is false, so the conclusion is false. Chapter 4 proves that such a choice rules out every derivation, so that a search for it can only stall: the chapter's open question, in a new place." (The stall is now the consequence of Chapter 4's theorem, stated inside the plain pointer, not an inference made in Chapter 3.)
  - **Stem, changed** (S2 round 1): the second question "And is its converse, \( P \to (Q \to R) \vdash (P \to Q) \to R \)?" becomes "Derive or break its converse, \( P \to (Q \to R) \vdash (P \to Q) \to R \)." As worded, the stem asked whether the converse is derivable, which Chapter 3 cannot answer "no" to; the new stem asks for what the solution gives. R3's content changes, so it re-enters the ledger (it was already going stale).
- **R4** (new) `exr-from-argument-to-derivation-r4` `[R4]` (dialogue extraction). [Technique: Hu (dialogue extraction).] Stem (the problem never names its source, STYLE §11.5):
  - The dialogue:
    > **Ana.** Let \( x \) be a real number with \( x^2 < x \). Then \( x \) is positive.
    > **Ben.** Why can't it be negative?
    > **Ana.** A negative number is less than its square.
    > **Ben.** And zero?
    > **Ana.** At zero, \( x^2 \) equals \( x \). And \( x \) is less than \( 1 \), because for \( x \ge 1 \) we would have \( x^2 \ge x \).
    > **Ben.** So \( 0 < x < 1 \). But you never said why \( x^2 \ge x \) when \( x \ge 1 \).
    > **Ana.** Multiply \( x \ge 1 \) by \( x \), which is positive.
  - The parts:
    - (a) What is the conclusion, and who states it?
    - (b) With \( N \): "\( x < 0 \)", \( Z \): "\( x = 0 \)", \( B \): "\( x \ge 1 \)", \( L \): "\( x^2 < x \)", write the premise and the three facts used, and the sequent.
    - (c) Derive it.
    - (d) Is Ana's last answer enough?
  - *Answer.*
    - (a) "\( 0 < x < 1 \)", stated by Ben. Ana's first line, "\( x \) is positive", is an intermediate step.
    - (b) The premise is \( L \). The facts: \( N \to \neg L \) (Ana: a negative \( x \) has \( x^2 > 0 > x \)); \( Z \to \neg L \) (Ana: \( x^2 = x \) at \( 0 \)); \( B \to \neg L \) (Ana, then justified at Ben's request). The conclusion \( (\neg N \wedge \neg Z) \wedge \neg B \) reads as "\( x \ge 0 \), \( x \ne 0 \), \( x < 1 \)", that is, \( 0 < x < 1 \), by the convention of Section 2.1. The sequent is \( N \to \neg L, \ Z \to \neg L, \ B \to \neg L, \ L \vdash (\neg N \wedge \neg Z) \wedge \neg B \).
    - (c) 5 \( \neg\neg L \), ¬¬I 4; 6 \( \neg N \), MT 1, 5; 7 \( \neg Z \), MT 2, 5; 8 \( \neg B \), MT 3, 5; 9 \( \neg N \wedge \neg Z \), ∧I 6, 7; 10 \( (\neg N \wedge \neg Z) \wedge \neg B \), ∧I 9, 8. MT needs the negation of each fact's conclusion, and that is \( \neg\neg L \), hence line 5.
    - (d) Yes: \( x \ge 1 \) gives \( x > 0 \), and multiplying \( x \ge 1 \) by the positive \( x \) gives \( x^2 \ge x \).
  - The solution names its sources: @prp-modus-tollens, @prp-double-negation (a) (Chapter 2); Section 3.3's extraction (@exm-extract-argument).

**Sidecars:** `exm-extract-argument.py`, `exr-from-argument-to-derivation-b1.py`, `-b3.py`, `-b4.py`, `-c1.py`, `-r4.py` (§3.3). **Ledger lines:**
- F1–F3 and their reasons: school arithmetic, sidecar for \( |n| \le 500 \); "prime" as defined in the section; AN1.1 / F2.2 not needed.
- B1 (a) the order facts \( x > 1 \Rightarrow x^2 > x \), \( x < 0 \Rightarrow x^2 > x \); (b) \( (2k)^2 = 2(2k^2) \); (c) division by \( a \ne 0 \). All school algebra, AN1.1 promised.
- B4 the sum of inequalities (school algebra).
- R4 the three order facts (school algebra).
- C2's reading ("no statement can meet the condition") is argued from the derivation read as an argument, as every example of the book is.
- R1–R3 keep their ledger lines.

---

## 5. Budgets and the Time line

| § | Main line now (before Exercises) | Main-line budget | Expected | Folds now | Fold budget |
|---|---|---|---|---|---|
| index | placeholder (~60) | ≤ 1,000 | ~975 | — | — |
| 3.1 | 4,652 | ≤ 5,000 | ~4,995 | 0 | ≤ 975 (expected ~955) |
| 3.2 | — (new) | ≤ 4,600 | ~3,500 | — | ≤ 350 (expected ~280) |
| 3.3 | — (new) | ≤ 3,400 | ~2,300 | — | ≤ 150 (none planned) |
| sections | 4,652 | ≤ 13,000 (layout §3) | ~10,770 | 0 | ≤ 1,475 (expected ~1,235) |

Every section file stays at or under 5,000 main-line words (layout §1.3 caps). The whole-file advisory count of `check_structure.py`, exercises included, will exceed 5,000 in 3.1 and 3.2. It is advisory.

**Exercises after the deepening.**
- 3 A1, two new: 3.2, 3.3.
- 2 A2 banks of 12 (**24 parts**: 3.1's, R3's 11 plus one; 3.2's, new), counted for Time as 6 exercises (STYLE §12.8).
- 12 B, 9 new:
  - 3.1 B1–B3 kept, B4 new;
  - 3.2 B1–B4;
  - 3.3 B1, B2, B4, and **B3, the 15-item battery**, counted as four exercises by the drill rule.
- 8 C, 4 new: 3.1 C1–C4 kept; 3.2 C1 (exit check), C2 (Challenge); 3.3 C1 (exit check), C2 (Challenge).
- 4 R: three moved, one new.

The chapter's exit checks are 3.1 C3, 3.2 C1 and 3.3 C1.

**Time** (B1 formula: 15 min per 400 main-line words; A1 25 min; a drill bank one exercise per four parts at 30 min; one B 30 min and one non-Challenge C 40 min per section; R 40 min; index pages not counted, as in layout §3).
- **Core track:**
  - reading ~10,770 words ≈ 6.7 h (6.73);
  - A1 3 × 25 min = 1.25 h;
  - A2 6 × 30 min = 3 h;
  - one B per section, 3 × 30 min = 1.5 h;
  - one non-Challenge C per section, the three exit checks, 3 × 40 min = 2 h.

  Total **≈ 14.5 h** (6.73 + 1.25 + 3 + 1.5 + 2 = 14.48). Rounded to the nearest 5 hours (STYLE §2): **"About 15 hours on the core track."** Layout §3's 16 h assumed full caps (13,000 words); the sections come in under them.
- **Full track:**
  - reading ~10,770 + ~1,235 folded ≈ 12,005 words ≈ 7.5 h (7.50);
  - A1 1.25 h;
  - A2 3 h;
  - B: 11 ordinary + 4 for the battery = 15 × 30 min = 7.5 h;
  - C 8 × 40 min ≈ 5.3 h;
  - R 4 × 40 min ≈ 2.7 h.

  Total **≈ 27.3 h** (7.50 + 1.25 + 3 + 7.5 + 5.33 + 2.67 = 27.25; layout: 27 h): **"about 25 hours for everything."** §0 states the same figures (S2 round 1).
- The drafter of `index.md` recomputes both from the delivered text (`check_structure.py --words`) and the delivered exercise counts, by the same rule, and does not shade either down (STYLE §11.9). If the delivered core reaches 17.5 h, the line reads "About 20 hours".

---

## 6. Pointers from Chapter 3 into other chapters (new numbering), and promises

Every forward pointer in Chapter 3 after this plan. Each section has at most one on its main line, in its Looking-ahead box (STYLE §12.1); 3.1 has none. The others are plain pointers inside exercise solutions or the index.

| Where | Text (new numbering) | Was | Paid by |
|---|---|---|---|
| index, What you need | "… used as ordinary reasoning, as in Chapter 2, until Chapter 5 gives them their rules" | 01:487, 01:713 parentheticals (R3 cut them) | Chapter 5 (`def-rules-existential`, `def-rules-universal`) |
| index, Minimum for fd2 | Chapters 1–6, 8; 7.1–7.2 before fd2 Chapter 3 | — | layout G14 |
| index, Summary | "That is Chapter 4's question." | — | 4.7 `thm-soundness`, `cor-refuting-row` |
| 3.2 Looking ahead | "Chapter 4 calls a list whose members can all be made true at once *satisfiable*, and proves that the satisfiable lists are exactly the consistent ones." | — (**new promise**) | 4.5 `def-satisfiable`; 4.7 "satisfiable ⇒ consistent" (text); 4.8 "consistent ⇔ satisfiable" (text, from `cor-derivable-iff-valid`) |
| 3.2 B4 solution | "Section 4.7 shows that a list made true at once … is consistent." | — | 4.7 (text) |
| 3.2 C2 solution | "Section 4.10 (optional) adds statements to a consistent list one at a time, in exactly this way." | — | 4.10 `lem-lindenbaum` |
| 3.3 Looking ahead | "… Chapter 4 gives each statement a truth value and proves that the rules never lead from true premises to a false conclusion. Then one choice of truth values … proves that no derivation exists." | 3.1's box in R3 (item 12); before D2, 2.6's closing paragraph | 4.7 `thm-soundness`, `cor-refuting-row`; ch04 index:3, 01:3, 07:3, 07:278 |
| 3.1 C2 (b) solution | "Chapter 4 turns such choices into proofs" | "Chapter 4 turns such rows into proofs, @cor-refuting-row" | 4.7 `cor-refuting-row` |
| 3.3 R3 solution (moved) | "Chapter 4 proves that such a choice rules out every derivation, so that a search for it can only stall" | "… such a row … (@cor-refuting-row)" | 4.7 `cor-refuting-row` |
| 3.3 C2 solution | "Section 5.6 meets the same shape with 'for every', in the barber and Russell's theorem." | — (**new**) | 5.6 `thm-russell` |

**Backward pointers** (no promise; each to a delivered or planned label):
- Section 1.1 (`def-counterexample-set`; "Where to look first"; the phrase book; B5's key);
- Section 1.3 B5 (d) (a missing implication written and checked; compared, not attributed);
- Section 1.4 C4 (b) (copying);
- Section 1.5 ("Derive it or break it");
- Section 1.6 (affirming a disjunct; `exm-constructive-dilemma`; the chart 07:936);
- Section 2.1 (convention box);
- Section 2.3 (`lem-weakening-cut`, after ch02-deepen; `def-derived-rule`);
- Section 2.4 (`lem-not-iff-own-negation`, after ch02-deepen; `def-provable-equivalence`);
- Section 2.5 (RAA, LEM, `prp-peirce`).

If ch02-deepen does not deliver `lem-weakening-cut` in 2.3, the proofs of F3.2-a cite @lem-weakening-cut wherever it stands only if that is earlier. Otherwise they inline the two-line copying argument; S3 checks the label's section before drafting. The same applies to `lem-not-iff-own-negation`: the gallery sentence and C2 (c) are dropped if it is absent.

**STATUS.md promise table** (coordinator, S4). Rows by atlas id; Chapter 3's pointers are written in the final numbering.
- Row "F1.7 §01 | soundness (`thm-soundness`, `cor-refuting-row`) …" becomes "**F1.7 §01, §02, §03** | soundness and completeness for the propositional rules":
  - §01: C2 (b)'s plain pointer; the failed search, without a box;
  - §02: the Looking-ahead box, consistent ⇔ satisfiable, and B4's plain pointer;
  - §03: the Looking-ahead box, the chapter's question, and R3's plain pointer (moved from §01).

  Paid by F1.3: `thm-soundness`, `cor-refuting-row`; "satisfiable ⇒ consistent" in 4.7's text, "consistent ⇔ satisfiable" in 4.8's text.
- Row "F1.7 §01 | quantifier steps: 'there exists' …" becomes "**F1.7 index** (the quantifier note), §01 (`exm-skeleton-odd-product`'s 'say \( m = 2k \)', A1 (b))". Paid by F1.4.
- **New row:** "F1.7 §02 | `exr-four-kinds-of-task-b3`, used later: the four breaking claims are recalled as refuting rows | F1.3 (4.6 recalls them by label; 4.7's retroactive paragraph certifies 3.2's withheld verdicts, layout G5)". This is a promise for the **ch04 S1**.
- **New row:** "F1.7 §02 | `exr-four-kinds-of-task-c2`, used later: splitting an inconsistency | F1.3 §10 (4.10 `lem-lindenbaum`'s step recalls it and proves the fact itself; optional section)". A promise for the ch04 S1.
- **New row:** "F1.7 §03 | C2's pointer: the barber and Russell's theorem | F1.4 (5.6 `thm-russell`)".
- **Paid by Chapter 3**, recorded in the existing rows:
  - "F1.1 §07 | the method … is the subject of Chapter 3": paid by F1.7 §01;
  - "F1.2 §03, §04, §05 | the search method … 'Section 3.1'": paid by F1.7 §01;
  - `ch01-deepen.md` §6 seams: 3.2 recalls 1.5's "Derive it or break it" (paid: 3.2 item 8); 3.3 reuses 1.1 B5's key (paid: 3.3 item 2).

  For 1.1 B5, the coordinator adds ", used later" to `exr-statements-and-connectives-b5`'s title at the S8 seam pass, the one ch01 file change this plan causes. The S8 seam referee records it. It is a title change only, so no hash change for the block's content; if the hash covers the title, B5 is re-reviewed.

**Seams recorded for later S1 units (not promises):**
- 6.3 mirrors 3.1 and 3.2: the four tasks with quantifiers, a first-order library citing 3.3's heading id, and the "propositional core" move.
- 6.1 mirrors 3.3 (translate, then derive) and may reuse the two-column format.
- 8.4 recalls 3.3's extraction (layout §1.3 row 8.4).
- 8.7 may cite 3.2 B1 (a)'s RAA-free derivation of \( \neg\neg(P \vee \neg P) \).
- 4.7's G9 "test the subgoal" looks back to 3.1's refinements and the failed search.
- 4.5 pairs `def-satisfiable` with `def-inconsistent-set` in a box (layout §1.3 row 4.5).
- 4.8's Challenge "closed tree ⇒ Fitch derivation" may recall 3.2's heuristic "a forced failed attempt is usually a derivation read backwards" as the informal idea it makes exact. Chapter 3 states it only as a heuristic.

---

## 7. What later chapters hold, so that Chapter 3 does not pre-empt them

| Chapter (new number) | Holds | So Chapter 3 does not |
|---|---|---|
| 4 Truth, Soundness and Completeness | formulas as objects, induction, valuations, truth tables, rows, ⊨, `def-satisfiable`, contingent/contrary, the refuting-row search tree (4.6, `prp-search-decides`), soundness (4.7, the G9 move "test the subgoal", the retroactive paragraph), completeness and TAUT (4.8), normal forms (4.9), infinite Γ and compactness (4.10) | draw a truth table or a search tree; say "row", "valid", "satisfiable" on the main line (except 3.2's box, which names Chapter 4's word); write ⊨; assert that something is not derivable or that a list is consistent (G10); use `\taut`; name "test the subgoal" (G9); define ⊢ or consistency for infinite lists |
| 5 Predicate Logic and the Quantifier Rules | ∀, ∃, =, ∃!, `thm-russell` (5.6), definitional extension (5.8) | use quantifier rules (the index note), translate quantified sentences (the key's sentences are about one fixed \( n \)) |
| 6 Working with Quantifiers | translation with quantifiers (6.1), `prp-replacement` (6.2), first-order search, `def-propositional-skeleton`, `prp-taut-skeleton`, a first-order library and battery (6.3) | replace a part of a line by an equivalent; call a step "propositional core" |
| 7 Models and Theories | structures, counter-models, `def-inconsistent-theory` (T ⊢ ⊥ from finitely many axioms), consistency and independence by a model (7.4) | speak of theories or of infinite lists of axioms; claim consistency by exhibiting a structure |
| 8 From Derivations to Mathematical Prose | the dictionaries, levels of proof, self-explanation (8.4, which recalls 3.3's extraction), the catalogue (N1)–(N14), the dispute over excluded middle (8.7) | teach self-explanation (STYLE §11.1); cite the catalogue; discuss which classical laws survive without RAA (3.2 B2 (c) and B1 (a) say only what *our* derivations used) |

---

## 8. What stays exactly as it is

- Everything that `ch02-revision.md` §7 lists for 2.6 (now 3.1): the faded triple (`exm-search-distribute`, B2, C1), the "What the method did" debriefs, the failed search's honest "a search that fails proves nothing", the schemas and the derived-rules table, the exit check (C3) with its marking scheme, the hint ladders.
- Every passage of `01-finding-derivations.md` not named in §4.1 or in R3 §4.6.
- The statements and proofs of all 17 labels of §3.1, except the solution wording of C2 (b), and R3's solution and stem, named there.
- The R items' content (R1, R2 verbatim).
- `exr-finding-derivations-b1` (frozen) is untouched, including its parenthetical "(That no derivation of \( P \) from the premise avoids \( \rulename{RAA} \) is true, but we do not prove it.)". S2 is asked to rule on it under G10 (§9, item 5).

---

## 9. S2a: every new claim, derivation and answer that needs blueprint verification

**The chapter-wide rules:**
1. **G10 audit.** No sentence of the main line, folds or solutions asserts that a particular claim is not derivable or that a particular list is consistent, except in the two Looking-ahead boxes and the plain Chapter 4 pointers listed in §6. In particular:
   - 3.2's "To show one consistent … nothing in this chapter can do that";
   - the gallery's look-alike paragraph;
   - the Not-allowed entries 2 and 4;
   - A2 (g), (i);
   - B4's "true at once" verdicts;
   - C2 (c);
   - 3.1 C2 (b) and R3 as reworded (solution and stem);
   - `exm-derive-or-break-search`'s closing sentence ("On (b) the method of Section 3.1 could only search, and a stall is not a verdict; the break is"; reworded at S2 round 2, since the S2 round 1 wording, "a search would only have stalled for as long as it ran", drew "every search stalls" from the break);
   - B4 (d)'s "is not itself a clash … breaks" (reworded at S2 round 1);
   - the Named move "Try to break it first" and 3.2 item 8's lead, now heuristic ("usually", "suggests").
   Every sentence that draws "no derivation" or "every search stalls" from a break, rather than citing Chapter 4 for it, is a violation.
2. **No truth tables, rows, ⊨, "valid", "satisfiable"** on the main line of Chapter 3 (except 3.2's box), and **no TAUT** anywhere. Every derived rule cited (DS, MT, VI, DM, ¬¬I, ¬¬E, LEM, CP) is proved earlier. No step replaces a part of a line.
3. **No detours** in any derivation of Chapter 3, old or new: check every typeset derivation, the delivered 3.1 ones included, against the detour paragraph. A manufactured clash (∨I, then ¬E) is not a detour. **¬I followed by ¬E on the negation it built counts** (ruling of S2 round 1; the paragraph now says so); a ¬I or →I line used as the non-negation premise of ¬E does not (3.2 B4 (c), line 7). Gallery row 2 (8 lines) and 3.3 C2 (a) (8 lines) are written detour-free; C2's solution shows the 7-line detour version as a remark only, as an instance of "advice, not a theorem". The S1 Curry and gallery derivations each contained one such detour; S2 should re-check every other derivation of §4 for the ¬I/¬E pattern.

**Changed wording of existing blocks:**

4. 3.1 C2 (b): "neither side follows from no premises" and "Chapter 4 turns such choices into proofs" keep the solution's claim, which says only that the **method** needs step 5. Ch04 08:13 and 08:510 still describe the 13-line derivation correctly.
5. 3.1 B1 (frozen): S2 rules whether its parenthetical on RAA-free derivations is compatible with G10. The claim concerns derivations without RAA, not ⊢. If S2 rules it must change, the minimal fix appends "(Section 4.7 proves a claim of this kind for \( \neg\neg P \vdash P \).)", and ch06 02 and ch07 02, which cite B1, are re-read.
6. 3.3 R3's reworded paragraph and stem. The stem's second question is now "Derive or break its converse"; the solution's "so that a search for it can only stall" sits inside the Chapter 4 pointer. "The converse breaks": check that \( P \), \( R \) false makes \( P \to (Q \to R) \) true and \( (P \to Q) \to R \) false, for either value of \( Q \). It does: \( P \to Q \) is true when \( P \) is false.
7. R3's items, re-run on the delivered 3.1: its S2a items 30–38 and 44. Also: the moved Peirce passage in fold F3.1-c is verbatim from R3 item 8, and the main line keeps one sentence pointing to it. The moved sentences of F3.1-d are verbatim. 01:466 plus its new sentence has no forward chapter in it.

**New main-line claims and examples:**

8. 3.1 refinements:
   - (i) the "three lines where none is needed" example (a goal \( P \to Q \) that is a premise: box, →E, →I, against citing it);
   - (ii) lines outside the boxes are available inside them (scope rule);
   - (iii) the clash-partner advice;
   - `exm-search-free-lines` (rebuilt at S2 round 1, premises \( P \wedge (P \to Q), \ Q \to R \)): only ∧E and →E lines above the boxes, no ∨E; the 13-line derivation (passes `check_fitch.py`, checked while revising) and its two snapshots; "16 lines" for the boxes-first version (box of \( S \): 5 lines, box of \( T \): 6 lines, plus 2 premises, 2 →I lines and the ∧I line);
   - its Quick check (line 8 finds the goal among the resources; lines 3–6 need nothing new);
   - fold F3.1-f's four copying claims (∧: the line is \( i \) or \( j \); →: the box copied with line \( \varphi \) for its assumption gives \( \psi \); ¬: likewise gives \( \bot \); ∨: the first case copied likewise; every copied citation stays legal), the main line's ¬I/¬E sentence, and that a manufactured clash is not a detour;
   - the fold test for F3.1-f and F3.1-g (no A or B item needs either);
   - the detour Quick check.
9. 3.1 Figure 3.1-F: each test and action matches the algorithm's steps 2–5 and R3's step-2 wording (∨ postponed: "no" at t1); following it writes no illegal line; the terminal node says "try to break the claim", not "not derivable"; the termination rules of §4.1 item 3 (decided at S2 round 2) are on the page. **The run on \( P \to Q \vdash Q \to P \)** (gaps written goal | resources; G0 is \( Q \to P \mid P \to Q \)):
   - G0: t1, b1: a box on \( Q \), making G1 \( = P \mid P \to Q, Q \).
   - G1: t0, t1 no. t2: →E on \( P \to Q \) would make the gap \( P \mid P \to Q, Q \), which is G1 itself: skipped. t3 no. t4: RAA, making G2 \( = \bot \mid P \to Q, Q, \neg P \).
   - G2: t2: →E makes G3 \( = P \mid P \to Q, Q, \neg P \) (new: the resources differ from G1's by \( \neg P \)).
   - G3: t2: →E would make G3 again: skipped. t3: the goal is not \( \bot \), nothing clashes. t4: RAA would make G2, open above: skipped; LEM on \( P \) (the only statement a resource waits for): its case \( \neg P \) is G3: skipped. e4: back to G2, →E tried.
   - G2: t3: aiming at \( P \) against \( \neg P \) makes G3's gap again (not open above, so it is tried, and fails as before). t4: RAA on \( \bot \) is not a move; LEM on \( P \): its case \( \neg P \) is G2: skipped. e4: back to G1, RAA tried.
   - G1: t4: LEM on \( P \). The case \( P \) closes at t0; the case \( \neg P \) is G3's gap, which fails as before. e4: back to G0, b1 tried.
   - G0: t2 (→E, making \( P \mid P \to Q \)), t4 (RAA on \( Q \to P \); LEM on \( P \)) open further gaps; each route fails the same way, every \( P \) wanted being wanted from resources that hold \( P \to Q \) and maybe \( Q \) or \( \neg P \), never \( P \). e4 at the first gap: stop.
   That the run ends is the finiteness argument of §4.1 item 3; that it ends at e4 is guaranteed only by soundness (Section 4.7), and the text claims neither, only that the chart is followed. A script following the rules in one fixed order (scratch, not committed) ran this claim to e4 at the first gap after 94 gaps, and found derivations of Peirce's law, \( \vdash P \vee \neg P \), \( \neg\neg P \vdash P \), \( \neg(P \wedge Q) \vdash \neg P \vee \neg Q \), \( P \to (Q \vee R) \vdash (P \to Q) \vee (P \to R) \) and 3.2 B3 (c), (i); on B3 (d) it ends at e4. S2a checks the bullets above by hand and that each node's wording matches the rules.
10. 3.1 fold F3.1-e: no claim beyond "a derivation commits whoever accepts \( \Gamma \) to \( \varphi \)", and "the rules permit more lines than a search writes".
11. 3.2 `exm-theorem-search`: the 8-line derivation; the snapshots; the aftermath's "a theorem is a derived rule with nothing above the line" (consistent with `def-derived-rule` for \( n = 0 \), as \( \rulename{LEM} \) is used).
12. 3.2 `exm-equivalence-search`: both derivations (7 and 11 lines); the reading (\( ab = 0 \), \( a \ne 0 \Rightarrow b = 0 \)); the two snapshots now written for (⇒) (S2 round 1 withdrew the exemption).
13. 3.2 `def-inconsistent-set`: finite lists, \( n \ge 0 \) as in `def-derivable`; matches NOTATION's *consistent* row (syntactic). The empty list is a list. No claim is made that it is consistent.
14. 3.2 `prp-inconsistent-derives-everything` and `prp-derivable-iff-negation-inconsistent`:
    - the statements;
    - fold F3.2-a's proofs, in particular the copying argument for (⇐): premises outside, \( D \)'s boxes nested inside the new box, citations of \( \neg\varphi \) redirected to the assumption, the last line of \( D \) a line of the new box itself, and the case where \( D \)'s last line is a premise belonging to \( \Gamma \) (\( \bot \in \Gamma \)); only non-premise lines are copied; in (a), the case where \( D \)'s last line is the premise \( \varphi = \bot \) itself (a one-line box);
    - (a) needs no RAA;
    - the reliance on `lem-weakening-cut` (a), (c) as stated at ch04 08:30 (to be in 2.3);
    - "the same move as Section 1.4, Exercise C4 (b), run backwards" (C4 (b) turns open assumptions into premises).
15. 3.2 `exm-inconsistency-search`:
    - the 10-line derivation, with a one-line case box 5–5 (as in 1.6's gallery);
    - no integer meets (1)–(4);
    - \( n = 6 \) fails only (1), \( n = 1 \) only (2), \( n = 3 \) only (3), \( n = 12 \) only (4);
    - Quick check: \( 3 \), \( 9 \) are the integers in \( [1, 10] \) meeting (1), (2), (4), each failing (3). (Of the others, \( 1 \), \( 5 \), \( 7 \) fail (2); \( 2 \), \( 6 \), \( 10 \) fail (1); \( 4 \), \( 8 \) fail (4); the sidecar checks.)
16. 3.2 gallery: each list's derivation of \( \bot \) (7, 8, 4 lines; row 2 detour-free, passes `check_fitch.py`, and marked in the plan as a recall of the 2.4 lemma); every member compound; the look-alike true at once with \( P \) false; the look-alike derives \( \neg P \) (a 5-line ¬I box); the gallery sentence equating row 2 with `lem-not-iff-own-negation` via the proposition (a) with \( \Gamma \) empty and \( \varphi = P \leftrightarrow \neg P \).
17. 3.2 Not-allowed entries and their tags.
18. 3.2 "One task in four costumes":
    - the table's entries;
    - the claim \( \varphi \dashv\vdash \psi \iff \vdash \varphi \leftrightarrow \psi \), argued by copying into boxes for ↔I, and by weakening plus ↔E;
    - the "it breaks when" column: each is the counterexample set of the row's claim made true. For the equivalence, "one true and the other false" is the union of the two claims' counterexample sets.
19. 3.2 `exm-derive-or-break-search`:
    - (a) the forced attempt (each step forced) and the 10-line derivation;
    - (b) the break at \( P \), \( Q \) true, \( R \) false, and at \( x = 2 \) with \( x > 0 \), \( x > 1 \), \( x > 3 \);
    - the Quick check's "For example" repairs, each a replacement of one symbol: → for ∨ gives (a); ∧ for ∨, the 9-line derivation with ⊥E (passes `check_fitch.py`); and the two further replacements named in the last sentence, ↔ for ∨ and \( R \) for \( Q \) (truth-table checked while revising); no row proved only in an exercise is cited;
    - the closing sentence ("the method of Section 3.1 could only search … the break is") against G10 (item 1): it says what this chapter's method can do with (b), not what any search can do.
20. 3.2 Figure 3.2-F: the loop is drawn and not claimed to terminate; no node asserts non-derivability.
21. 3.2 Looking-ahead wording against 4.5/4.7/4.8 as layout §1.3 plans them ("satisfiable ⇒ consistent" in 4.7's text; "consistent ⇔ satisfiable" in 4.8's).
22. 3.3 the key (identical to 1.1 B5's four letters and readings); F1–F3 true for every integer, with their reasons; the definition of prime used ("greater than \( 1 \)"); the Quick check's translation and reading back.
23. 3.3 the extraction method's five steps; `exm-extract-argument`: the reading of the paragraph, the facts F1, F2, the 16-line derivation and snapshots, the aftermath's box version.
24. 3.3 Figure 3.3-F: arrows match the derivation's dependencies (\( \neg E \) from \( P \wedge G \) and F1; \( \neg T \) from \( P \wedge G \) and F2); the lead says it omits the boxes.
25. 3.3 Not-allowed entries (step tags; "every prime is odd" fails at \( 2 \)); `exm-two-columns`: the 10-line derivation, the table's row matches, "silent on lines 3–4 and 10"; its Quick check (F1 replaces F3; the ¬I box disappears: \( P \wedge E \) by ∧I from lines 4, 3 and one →E).
26. 3.3 library:
    - every row's sequent matches its label's statement exactly, including one-directional rows: `prp-and-associative` and `exm-disjunction-regroup` are one direction only and are listed so; `prp-implication-as-disjunction` (a), (b) as stated; DM (a)–(d) by letter;
    - every cited label precedes 3.3;
    - the grouping is fd1's own (by the method's steps 3 and 2), with no Lemmon or LB order (Critic small correction 7);
    - the lead's "applied to whole lines".
27. 3.3 Looking-ahead wording (R3 item 12 verbatim, except "the failed search above" → "the failed search of Section 3.1").

**New and changed exercise answers:**

28. 3.1 A2: all twelve parts; (i)'s detour and its one-line replacement. (No new part prints an answer given on the main line or in another item: (i) is not B4's derivation or the Quick check's.)
29. 3.1 B4: the 11-line derivation passes `check_fitch.py`; the two detours; the 6-line rewrite; (d)'s copy.
30. 3.2 A1 (a)–(e); A2 (a)–(l), in particular (f) (two readings, and \( Q \) not a negated conclusion).
31. 3.2 B1: three theorems (14, 8, 10 lines); which step opens each box (in (b), box 1 by step 2 and the two case boxes by step 3); (a)'s second conjunct without RAA. (b) was replaced at S2 round 1 (the S1 (b) was the main-line claim (a) curried); the new (b) is checked against the text's derivations and against Chapter 1's ∨E items, and passes `check_fitch.py`.
32. 3.2 B2: the scaffold; both derivations (10 lines each); (c).
33. 3.2 B3: nine verdicts (five derive, four break); the derivations of (b), (c), (e), (h), (i); the breaks of (a), (d), (f), (g) at the stated numbers; the closing pairs. (A truth-table check of all nine was run while writing this blueprint, and of the replaced (c), (d), (i) at S2 rounds 1 and 2: (b), (c), (e), (h), (i) valid; (a), (d), (f), (g) invalid; (d)'s break at \( x = 1 \) with \( x > 5 \), \( x > 0 \), \( x > 10 \) checked; the round 2 (c) (10 lines, LEM and DS) and (i) (6 lines) pass `check_fitch.py`, checked while revising.) The round 2 (c), (d), (i) are fd1's own, and none is a textbook item plus a trivial step (item 40's standard): (c)'s two cases end by different rules, and (c) is not 3.1's `exm-search-postpone-or` (whose goal is a disjunction and whose split is on \( Q \)); (i)'s premise has a consequent that is neither the goal nor the RAA assumption's negation, so the clash is manufactured (Lemmon's \( \neg P \to P \vdash P \) closes by a direct clash). Checked against the LPL and Lemmon exercise lists for these shapes. The (c)/(d) look-alike pair shares its premises, so B3's closing sentence stays true.
34. 3.2 B4: three derivations of \( \bot \) ((a), (c), (e)); three lists true at once ((b), (d), (f)) with their statements; (f) with the fourth member derives \( \bot \) (LEM twice, four cases). Truth-table check run: (a), (c), (e), (f) + fourth member unsatisfiable; (b), (d), (f) satisfiable.
35. 3.2 C1: the counterexample set; the 13-line derivation of \( \bot \); the 11-line direct derivation; (d)'s break at \( x = 1 \) (all four members of the new counterexample set checked); the marking scheme.
36. 3.2 C2: (a)–(c) from the two propositions; the marking scheme; the "used later" target.
37. 3.3 A1 (a)–(e).
38. 3.3 B1: (a) 6 lines; (b) the fact \( E \to S \) and the tempting wrong supply; (c) the 10-line LEM derivation and the division fact.
39. 3.3 B2: the scaffold; the 8-line derivation; the table; (c) \( G \) idle, \( F3 \vdash P \to \neg(E \wedge T) \).
40. 3.3 B3: all fifteen answers:
    - the derivations of 1–10, 12, 14;
    - the breaks 11 (\( n = 2 \)), 13 (\( n = 15 \)), 15 (\( n = 25 \));
    - 3's remark (the library saves nothing);
    - 9's unused premise.

    None duplicates a derivation in the text or another exercise of Chapters 1–3, nor is one plus a trivial step. Check against `exm-extract-argument`, `exm-two-columns`, B2, C1, B4, 1.1 B5, 1.6 B7, 2.3–2.5's exercises, and the 3.1 items. None matches a Lemmon numbered sequent after renaming letters (Critic small correction 7). Truth-table check run: every derive verdict valid.
41. 3.3 B4: the six-sentence order and its uniqueness; the two distractors' faults (\( a = 0 \), \( b = 3 \)); the 8-line derivation; the matching.
42. 3.3 C1: the 14-line derivation; the table; (e)'s break at \( n = 2 \); the marking scheme. Its derivation is not B3 item 8's or item 9's (checked).
43. 3.3 C2: the 8-line detour-free derivation (passes `check_fitch.py`) and the solution's remark on the 7-line detour version; the marking scheme's line references (box 2–4, line 6; the 7-line ending accepted); (b)'s inconsistency; (c)'s rule list; the name "Curry's paradox" and the remark linking it to @prp-curry's name (the logician Haskell Curry; the book gives the surname only).
44. 3.3 R4: the dialogue's facts (true for all real \( x \) in their ranges); the 10-line derivation with ¬¬I; (d).
45. The index: the Summary's claims (each a labelled result or worked example of the chapter); the Terms glosses; the nine named moves with their sections.

**Originality (for S2's comparison with the twelve books):** every example, drill and exercise above is written for this book. The items with standard names (the detour rule, Harman's remark, Curry's paradox, constructive dilemma) carry fd1's own wording and dress. The library and the battery are fd1's own selection, grouped by fd1's moves. The dialogue and the extraction paragraphs are mathematical and fd1's own.

---

## 10. Notes for S3 and S4

- **Three drafters**:
  - (i) 3.1, editing the existing file: R3 §4.6 first, then §4.1 here;
  - (ii) 3.2, a new file;
  - (iii) 3.3, a new file, including the R move out of 3.1 (coordinate with (i): (i) deletes the `### R. Review` block of 3.1, and (iii) pastes it, with R3's reworded solution and the new R4).

  The index is written last, against the delivered sections (DRAFTING).
- Every new derivation passes `tools/check_fitch.py`. Every snapshot carries `% schema (partial derivations: …)`, and `\purpose{…}` on each assumption whose box no justified line closes yet. B4 of 3.1 is a correct derivation, so it is **not** marked `% expect-invalid`. S4 runs `check_fitch.py --purposes` on the chapter.
- Each new figure (3.1-F, 3.2-F, 3.3-F) is a raw LaTeX block with the `tikzpicture` in full, using only `book-diagrams.sty`'s styles. There are no colours and no white fills. S4 checks the HTML (SVG) and PDF renderings.
- **Coordinator, STYLE and NOTATION (pre-layout numbering):** STYLE §12.5 ("2.6"), §12.6 ("after 1.6, 2.6 and 4.6") and §12.13.4 ("until Chapter 3 … from Section 3.6") still use the old numbering. In the final layout these read "3.1", "after 1.6, 3.1 and 5.6 (the quantifier card)" and "until Chapter 4 … a refuting row once Section 4.7 has proved soundness". NOTATION's *consistent* row names "F1.2's new section"; it should say F1.7 §02. None of these changes Chapter 3's plan.
- **R3 §9 D9 superseded in part**: the method flowchart (Figure 3.1-F) is added. R3 refused a second **decision chart** that duplicated the moves table; this chart draws the algorithm's order, the way 1.6's chart (delivered in the pilot) draws Chapter 1's.
- The layout's index row allows no opening quiz; none is written.
- **Judgment calls made here, for S2 and the author's S9:**
  - (a) 3.1's Looking-ahead box moves to 3.3, so 3.1 has no box.
  - (b) Peirce's search (R3 item 8) goes into a fold, to make room for the refinements under the 5,000 cap.
  - (c) The detour rule is stated as advice with its three copying arguments, and no normalization theorem is claimed.
  - (d) 3.3 reuses 1.1 B5's key and adds three facts.
  - (e) Curry is named in a solution, with a note on the clash with @prp-curry's name.
  - (f) `prp-derivable-iff-negation-inconsistent` has a part (a) for negated conclusions (¬I only) besides the layout's (b).
  - (g) 3.2's look-alike and Not-allowed lines are worded so that "consistent" is never asserted.
  - (h) 3.1 C2 (b) and 3.3 R3 change by a few words for G10; R3's stem also asks "derive or break" for the converse (S2 round 1).
  - (j) (S2 round 1) ¬I followed by ¬E on the negation it built counts as a detour; the detour copying arguments and the odd product's table go into folds to keep 3.1 under 5,000.
  - (i) The battery is 15 graded items (library, translation, derive-or-break), not 15 bare sequents.

---

## 11. S2 replies (round 1)

All findings of S2 round 1 were applied; none is disputed. Where two reviewers raised the same point, one reply covers both.

1. **`exm-search-free-lines` used an unlicensed ∨E above the boxes** (error and gap). Applied option (b): the example is rebuilt on \( P \wedge (P \to Q), \ Q \to R \vdash (S \to R) \wedge (T \to (Q \wedge R)) \), so only ∧E and →E lines go above the boxes. Snapshots, counts (13 against 16) and the Quick check (line 8; lines 3–6) are rewritten; the derivation passes `check_fitch.py`. The clash-partner refinement is no longer illustrated in 3.1's own example; it is illustrated by name in 3.2's `exm-inconsistency-search` and C1 (b), which the plan now says. Option (a), a fifth refinement, was not taken: it would add a named move and ~40 words to a section already at its cap.
2. **`exm-derive-or-break-search` closing sentence (G10)**. Reworded and added to §9 item 1. (The round 1 wording, "a search would only have stalled for as long as it ran", still drew "every search stalls" from the break; S2 round 2 replaced it by "On (b) the method of Section 3.1 could only search, and a stall is not a verdict; the break is". See §11b, reply 1.)
3. **R3's "breaks, so a search can only stall" (G10)**, both reviewers. The stall is now stated inside the Chapter 4 pointer ("Chapter 4 proves that such a choice rules out every derivation, so that a search for it can only stall"), and the stem's second question becomes "Derive or break its converse". R3 re-enters the ledger (§3.3 already had it going stale).
4. **B4 (d) said a particular list is not inconsistent**. Reworded as proposed: the member is not itself a clash, and the claim that the list derives \( \bot \) breaks. Added to §9 item 1.
5. **Quick check repair rested on DS's exercise form; "Two answers" wrong; ¬Q inserts a symbol**, both findings. The \( \neg Q \) answer is dropped. The solution says "For example" and gives → for ∨ (claim (a)) and ∧ for ∨ (a 9-line derivation with ⊥E, no exercise row cited), and names ↔ for ∨ and \( R \) for \( Q \) in one closing sentence. §9 item 19 updated.
6. **Curry's 7-line derivation contains a →I/→E detour; gallery row 2 a ¬I/¬E one**, both reviewers. C2 (a) prints the 8-line detour-free derivation, and the solution adds that the 7-line ending is a detour whose cutting costs a line because line 5 is cited again: "advice, not a theorem". The marking scheme accepts either. Ruling: ¬I followed by ¬E on the negation it built is a detour, and the detour paragraph says so in one sentence; gallery row 2 becomes the 8-line copy. §9 items 3, 16 and 43 updated.
7. **Equivalence (⇒) snapshot exemption did not fit any class**, both reviewers. The exemption is withdrawn and S1/S2 are written as proposed.
8. **F3.2-a's case split missed \( \varphi = \bot \) in (a), and "copy the other lines" copied the premise \( \neg\varphi \)**. The first case now reads "a premise that belongs to \( \Gamma \)"; "copy the lines of \( D \) that are not premises"; and (a)'s sentence names the one-line box when \( D \)'s last line is the premise \( \varphi = \bot \). §9 item 14 updated.
9. **B3 closing sentence wrong for (c)/(d)**, both reviewers. Resolved together with item 10 below: the new (c)/(d) share their premises, so the sentence "each pair has the same premises and differs in the conclusion" is now true of both pairs.
10. **B3 (c) and (i) reproduced textbook exercises; gallery row 2 is a textbook list**. (c) and (i) are replaced by fd1's own claims of the same kinds: (c) \( P \to (Q \wedge R), \ \neg P \to R \vdash R \) (LEM split), its look-alike (d) \( P \to (Q \wedge R), \ \neg P \to R \vdash Q \) (breaks at \( x = -1 \)), and (i) \( \neg P \to (P \wedge Q) \vdash P \). Verdicts truth-table checked; derivations pass `check_fitch.py`. The breaking claims recalled by 4.6 are still (a), (d), (f), (g). Row 2 stays, marked in the plan as a recall of the 2.4 lemma. (Superseded at S2 round 2 for (c), (d), (i): see §11b, reply 4.)
11. **§0 and §5 Time figures disagreed**, both reviewers. Both now say core ≈ 14.5 h and full ≈ 27.3 h. The full figure moves from 27.1 h because the fold budget grew (F3.1-f, F3.1-g); the printed lines are unchanged.
12. **"A forced attempt is a derivation read backwards" stated as fact**. Made heuristic in the Named move, in 3.2 item 8's lead, in Figure 3.2-F's node b1, and in §6's seam for 4.8.
13. **Figure 3.1-F need not terminate**. t2 read "can a resource not yet used be taken apart?", with "used" defined for the drafter. (Superseded at S2 round 2: see §11b, reply 3.)
14. **"Weakest fact" attributed to Section 1.3 B5**. The attribution is dropped: the advice is stated as new, with its reason, and B5 (d) is only compared. §6's backward-pointer list updated.
15. **Library lead's list of sections**, both reviewers. Now "Chapters 1 and 2 and Section 3.2".
16. **Affirming the consequent credited to Section 1.1**, both reviewers. Now "Section 1.3", matching 3.3 B1 (b) and 01:464.
17. **3.1 budget tally summed to 5,045 and omitted two items**. The tally is corrected and itemised (≈ 4,967). It now takes three trims in advance: the card's Lean sentence, 01:186's second sentence, and the odd product's Givens/Goal table, moved verbatim to the new fold F3.1-g. It also moves the detour paragraph's copying arguments to the new fold F3.1-f. The fold budget rises from ≤ 850 to ≤ 975, and a new three-step trim order covers any remaining excess.
18. **3.2 B1 (b) was the main-line claim (a) curried**. Replaced by \( \vdash ((P \to Q) \wedge (P \vee Q)) \to Q \). Its search reaches step 3 on a disjunction (8 lines, passes `check_fitch.py`). §9 item 31 updated.

## 11b. S2 replies (round 2)

All four findings of S2 round 2 were applied; none is disputed.

1. **`exm-derive-or-break-search`'s closing still drew "every search stalls" from the break (G10)**. The clause "a search would only have stalled for as long as it ran" is gone. The sentence now reads "On (b) the method of Section 3.1 could only search, and a stall is not a verdict; the break is." It speaks of this chapter's method and draws nothing about all searches. The quoted text in §9 items 1 and 19 and in §11 reply 2 is updated.
2. **The refinements lead promised "shorter", but C2 (a) and gallery row 2 are longer detour-free**. Both proposed fixes are applied. The lead now says "usually find a shorter or more direct one". The detour paragraph's last sentence carries the length clause on the main line: "a detour is legal, and cutting one need not shorten a derivation, since an introduced line cited elsewhere stays". It replaces the clause "the line it makes was within reach without it", which repeated the paragraph's second sentence. 3.3 C2 (a)'s solution now cites that clause ("This is the case Section 3.1 names"), and so does gallery row 2's note. Recount: refinements 470 → 479.
3. **Figure 3.1-F's termination was left conditional; t4 never answered "no"**. Decided now, with no conditional, in §4.1 item 3. The reviewer's fallback "a goal already being sought is not new" was tested and is **too strong** as worded: it blocks the manufactured clash with an RAA assumption. On \( \vdash P \vee \neg P \) and on the new 3.2 B3 (i), the right move inside the RAA box on \( \neg(P \vee Q) \) is to aim at \( P \vee Q \), which is the goal already being sought. So the rule compares whole gaps: a move is skipped when its gap has the same goal **and the same resources** as a gap open above it. That rule fixes defect (1), since the RAA box differs by its assumption, and it still terminates. Defect (2) is fixed as the reviewer proposed. t4 reads "is RAA on this goal, or LEM on a statement a resource waits for, still untried for this gap?", b4 excludes RAA on \( \bot \), and a LEM case that adds a statement already present is no move. t2 and t3 say "untried for this gap". e4 now backs up to the gap that made the current one, which is step 5's "a goal further out", and stops only at the first gap. Without backing up, the chart stops on Peirce's law, which fold F3.1-c shows the method finds. The lead carries the two rules (≈ 42 words; 3.1 tally 4,993 ≤ 5,000). §9 item 9 gives the run on \( P \to Q \vdash Q \to P \) as fact. A scratch script ran it and the positive cases under the same rules: the run on \( P \to Q \vdash Q \to P \) ends at e4 at the first gap, and the script finds derivations of Peirce, LEM, ¬¬E, De Morgan and B3 (c), (i).
4. **B3 (c) and (i) were textbook items plus one ∧E line**. Both are replaced along the lines proposed. (c) is now \( P \to Q, \ \neg P \to (R \vee Q), \ \neg R \vdash Q \), the reviewer's claim with the disjunction written \( R \vee Q \), because Section 2.3's DS refutes the **left** disjunct only (03-derived-rules 144). It is a LEM split on \( P \) whose cases end by →E and by →E then DS (10 lines). (d) is \( P \to Q, \ \neg P \to (R \vee Q), \ \neg R \vdash P \), with the same premises. It breaks at \( x = 1 \) with \( P \): "\( x > 5 \)", \( Q \): "\( x > 0 \)", \( R \): "\( x > 10 \)", and its trap is affirming the consequent. (i) is \( \neg(P \vee Q) \to P \vdash P \vee Q \) (6 lines: RAA, →E, ∨I, ¬E). Its goal is postponed and its clash is manufactured, unlike Lemmon's direct clash. Truth tables were re-run ((c), (i) valid; (d) invalid; the break checked numerically). Both derivations pass `check_fitch.py`. The (c)/(d) pairing and the closing sentence hold, and 4.6's recalled breaking claims are still (a), (d), (f), (g). §9 item 33 is updated.

