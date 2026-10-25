<!-- hand-written -->
# Revision blueprint: F2.3 Cardinality (fd2 Chapter 4) and F2.5 Relations, Section 5.2 (fd2 Chapter 5), stage S1

**Frozen after S2 (2026-10-26).** S1 2026-10-26; S2 round 1 (two blind referees) applied, replies in "S2 replies (round 1)" at the end. Next: S2a, then S3.

**What this is.** This is the S1 blueprint for the Chapter 4 and Chapter 5 work of the approved six-chapter layout, `fd2/authoring/design/layout-six-chapters.md` (§0, §1 Ch4 and Ch5 rows, §3, §4 R9–R12, §7). It covers:
- the hand edits to 4.3 and 4.4;
- the rebuilt 4.5, which keeps only choice-free results (author, §0 Q2: 「移到 6.1」);
- 5.2, with the fibres and the canonical factorization merged in;
- the forced small edits to 4.1 and 5.3;
- the two chapter indexes.

It is complete on its own. A drafter works from this file, the current `fd2/src/ch04-cardinality/` and `fd2/src/ch05-relations/` files at commit `09cf1f1`, `authoring/STYLE.md` (§1 house manner, §2 item 6, §4 item 3, §11.4, §12.0, §12.1, §12.5, §12.13.4, §12.14), `DRAFTING.md` and `NOTATION.md`. The format follows `ch01-deepen.md`, leaner.

**Line references** are to the files at `09cf1f1`. Prefixes:
- `41:` `01-finite-sets.md`, `42:` `02-countable-sets.md`, `43:` `03-diagonal-arguments.md`, `44:` `04-comparing-cardinalities.md`, `45:` `05-cardinal-arithmetic.md`, `ix4:` `ch04-cardinality/index.md`;
- `52:` `ch05-relations/02-equivalence-relations.md`, `53:` `03-orders.md`, `ix5:` `ch05-relations/index.md`;
- `61:` `ch06-axiom-of-choice/01-countable-unions-and-choice.md`. This file is read only, as a source of verbatim text; it is not edited here.

**Word counts** are main-line prose words as `tools/check_structure.py` counts them: a math span is one word, and folds are excluded. They are measured from the top of the file to `## Exercises`, as in the Chapter 1 blueprint. Layout §1's "Now" column counted whole files with the parked material still in them. That is why 4.5 is already under the cap here.

| File | Main line now | Folded now | Budget |
|---|---|---|---|
| 41 | 4,930 | 219 | as is (M+) |
| 43 | 3,406 | 0 | as is (M+) |
| 44 | 2,348 | 0 | ≤ 5,000 (M+) |
| 45 | 3,354 | 156 | ≤ 5,000 (F) |
| 52 | 6,619 | 583 | ≤ 5,000, folds ≤ 1,900 (F) |

**Inputs and manner.** The moves are the Cummings structural moves only: motivation before a new statement, scratch work kept apart from the proof, hooks and payoffs. There are no footnotes, no jokes, no history beyond one line and no first person. Nothing is copied from `/home/akizumi/book`. Every new example, item and answer below is the book's own.

**Binding rules.**
1. **No label is lost or renamed.** Exercise titles may change; labels never do. Moving a passage verbatim into a fold is not a change. No statement that a later proof cites goes into a fold.
2. **No choice in Chapters 4 and 5.** No proof, idea, claim or solution in 41–45, 52 or 53 cites `ax-choice`, `thm-countable-union`, `thm-surjection-right-inverse`, `prp-card-le-surjection`, `thm-infinite-countable-subset`, `thm-infinite-iff-proper-subset` or any `exr-infinite-sets-*` or `exr-countable-unions-and-choice-*` label. The forward-citation scan at `09cf1f1` finds eight such `@` citations, and §4 removes every one:
   - 43:5, 43:356 (three citations);
   - 44:144, 44:248;
   - 45:562 (`exr-infinite-sets-r4`);
   - 53:246.

   Prose may name the axiom of choice and "Chapter 6", but never as a reason.
3. **Prerequisites are earlier sections in the new order only.** The order is Sets (1), Functions (2), Induction and Recursion (3), Cardinality (4), Relations (5), Axiom of Choice (6). Every label cited below was grepped in `fd2/src` at `09cf1f1`. The new labels are listed in §3.
4. **One forward pointer per section.** It goes in the `[Looking ahead]` box at the end of the main line (STYLE §12.1). A second promise goes into the same box, not into the running text. The only exceptions are the approved prose pointers already standing in the kept text of 4.1 and 4.2, listed in §4.5; no new one is added.

---

## 1. Devices as applied

- **Method sections and boxes.** The boxes are unchanged:
  - `exm-method-pigeonhole` (4.1), `exm-method-list-it` (4.2), `exm-method-diagonal` (4.3), `exm-method-injections-both-ways` (4.4);
  - `exm-method-encode` and `exm-method-laws-by-bijection` (4.5);
  - `exm-method-well-definedness` (5.2).

  No new box is added. The new 4.4 proposition and the new 4.5 proposition reuse the moves of 2.4 (construct and verify) and of 4.1 (the hotel).
- **Scratch work and Givens/Goal tables** already stand at each method's first full appearance: 45:155–167 (`exm-pairing-bijection`), 45:230–240 (`thm-cardinal-laws` (d)) and 52:373–386 (`prp-congruence-arithmetic`). Fading is as follows:
  - well-definedness falls to an **Idea** at `thm-canonical-factorization`, its third use (§4.8 item 9);
  - the new 4.5 proposition gets an **Idea**, since the hotel (the one-room-up Quick check after `exm-hilbert-hotel`) is 4.1's.
- **Prove or disprove** B items exist in every method section: 43 B4, 44 B4, 45 B4 and 52 B4. 52 B4 gains parts (f) and (g) on the new material (§4.8). No new P-or-D item is needed.
- **Quick checks.** New checks: one in 4.4 and one in 4.5. 52 loses one duplicate. Density stays at about one per 800–1,000 main-line words.
- **Threads.**
  - Lattice points: 1.1 → 4.1.
  - The five strings: 2.1 → 4.3.
  - Russell to Cantor: 1.2 → 4.3 → 4.5.
  - Same size: 2.4 → 4.1 → 4.5 → 5.2.
  - Choice: 2.4 → 4.2 → 4.4 → 4.5 → Chapter 6. This one is new.
  - Comparability: 4.4 → Chapter 6.
  - Fractions: 2.1 → 5.2 → *Number Systems*, Chapter 2. This one is new.
  - The clock: 5.2 → *Number Systems*, Section 3.4.

  §4.0 and §4.7 put them in the indexes.

## 2. Section map

| § | File | Main line now → budget (expected) | Changes |
|---|---|---|---|
| ix4 | `ch04-cardinality/index.md` | — | rewritten (§4.0) |
| 4.1 | `01-finite-sets.md` | 4,930 → as is | new exercise C3 (counting injections); gluing C1 retitled C4; 41:428 reworded into the Looking-ahead box; S3 marker removed |
| 4.3 | `03-diagonal-arguments.md` | 3,406 → ~3,400 | opening (R9); a 2.3 pointer; B4 (a) solution without countable unions |
| 4.4 | `04-comparing-cardinalities.md` | 2,348 → ~2,750 | new `prp-injection-gives-surjection` with its Quick check; the gluing paragraph from 2.3 (§4.3 item 1a); 44:144 and 44:245–249 reworded (R10) |
| 4.5 | `05-cardinal-arithmetic.md` | 3,354 → ~3,900 | new subsection "Infinite sets without choice" (`prp-copy-of-naturals-absorbs`, Quick check); hook trimmed; parked pointers repaired; new B5; C2 repaired |
| ix5 | `ch05-relations/index.md` | — | edited (§4.7) |
| 5.2 | `02-equivalence-relations.md` | 6,619 → ≤ 5,000 (~4,965, measured parts), folds ~1,690 | old 5.2 merged in; "Functions on the clock" removed; nine folds (F5.2-a to F5.2-i); Scratch work → Idea; B4 (f), (g); exercises retitled |
| 5.3 | `03-orders.md` | as is | 53:246 remark (R12), ledger 53:494 (§4.6; this pass owns them, as the Ch6 blueprint §6 records) |

## 3. Labels

**New (three):**
- `prp-injection-gives-surjection` (4.4). This is layout §3's "choice-free half of `prp-card-le-surjection`".
- `prp-copy-of-naturals-absorbs` (4.5). This is the choice-free core of old 3.5, layout §1 4.5 row ("Hilbert's hotel revisited").
- `exr-cardinal-arithmetic-b5` (4.5), and `exr-finite-sets-c3` (4.1).

**Kept**, with these retitles:
- 4.1: `exr-finite-sets-c3` is titled `[C3: Counting injections]`, and `exr-restriction-extension-and-gluing-c1` becomes `[C4: Counting extensions]`.
- 5.2: `exr-fibres-and-factorization-a1` → `[A2]`, `exr-fibres-and-factorization-b2` → `[B5: Same fibers]`, `exr-fibres-and-factorization-c1` → `[C3: Equal fibers]`, `exr-restriction-extension-and-gluing-c2` → `[C4: Find the error]`.

**Moved within 5.2:** `exm-fibres-of-function` and `exm-same-size-subsets` move to the new subsection "The fibers of a function". `exm-same-size-subsets` goes inside a fold.

**Deviation from layout §1 (4.1 row).** The counting of injections is an **exercise**, not a worked example. Its count of \( \{1, \dots, n\} \times I(k, n - 1) \) needs the product count, which is only an exercise (`exr-finite-sets-c2` (a)). A main-line example may not use an exercise as a reason. An exercise may cite an earlier one. 2.2's Looking-ahead box (Ch2 blueprint, item 12) says "counts the injections between finite sets", naming no number; that wording is accepted and nothing is changed there.

---

## 4. Per-section plans

### 4.0 `ch04-cardinality/index.md`

Rewrite the page; remove the S3 marker. The title stays `# Cardinality`.

1. **ix4:5, the story.** Keep the first six sentences, from "Are there more rational numbers …" to "… than the set itself.", and keep the decimal sentences ("A second motivating question … by that definition."). Replace the rest of the paragraph with: "It starts from finite sets: Section 4.1 defines 'same size' by bijections, proves the pigeonhole principle and finishes the lattice-point puzzle of Section 1.1. Sections 4.1–4.4 teach one method of proof each: pigeonhole, list a set, run a diagonal, and compare sizes by injections both ways. The last section adds, multiplies and raises sizes to powers, absorbs a countable set into any set that contains a copy of \( \nN \), and finds that the plane and the subsets of \( \nN \) have exactly as many elements as the line. It teaches two more methods: encode and decode, and prove a law of sizes by a bijection."
2. **ix4:7, replaced:** "Every map in this chapter is given by a rule: a formula, a least element, a recursion with an explicit step. Some natural arguments would have to pick one element from each of infinitely many sets, with no rule to say which: a right inverse for every surjection, a copy of \( \nN \) inside every infinite set, one listing for each of countably many countable sets. Where that happens, the chapter says so and leaves the statement open. Chapter 6 adds the principle that settles these statements, the axiom of choice."
3. **What you need (ix4:9).**
   - Change the first sentence to "*Logic and Proof*, Chapters 1–8, and *Sets and Functions*, Chapters 1–3."
   - The ∃E clause becomes "the rule ∃E (@fd1:def-rules-existential), which names one object at a time".
   - In the Chapters 1 and 2 list, replace "the indicator function of a subset (Section 2.1, @exm-first-functions (d))" with "indicator functions and \( \powerset{X} \approx \{0,1\}^X \) (@def-indicator, @thm-power-set-two-power); restriction, extension and gluing, and injectivity across the pieces (@def-restriction-extension, @thm-gluing, @prp-injective-across-pieces)".
   - The Chapter 3 list ends at "(@prp-finite-max)". Delete from "; equinumerous, finite and infinite sets" to "(@exm-method-least-element, @exm-method-pigeonhole)". These are now Section 4.1's own; keep `@exm-method-least-element` in the Chapter 3 list.
   - Keep "(D1)–(D3) … without proof".
   - Delete "Section 6.1 uses one fact from school algebra … real roots."
   - Keep the √2 sentence, extended to "used in Sections 4.2 and 4.5".
4. **Time.** The target is about 30 h core and 45 h full (layout §1). The coordinator recomputes it with `check_structure.py --words` after S3.
5. **Roadmap.** Replace the six old bullets with these five; the old bullets "Countable unions and the axiom of choice" and "Infinite sets" are deleted, and "Cardinal arithmetic" is replaced by the last bullet below:
   - **Finite sets.** "Equinumerous sets, finite and infinite sets, the pigeonhole principle and the lattice points of Section 1.1, subsets and disjoint unions of finite sets, \( 2^n \) subsets, and no finite set the size of a proper subset; the method: pigeonhole."
   - **Countable sets.** Keep the old bullet.
   - **Diagonal arguments.** Keep the old bullet, deleting ", and the existence of transcendental numbers".
   - **Comparing sizes.** Keep the old bullet, replacing "its exchange with surjections at the price of choice" with "an injection gives a surjection back".
   - **Infinite sets and cardinal arithmetic.** "A copy of \( \nN \) absorbs any countable set, with no choice made; sums as disjoint unions, products and powers compared by size; the laws \( \card{X^{Y \sqcup Z}} = \card{X^Y \times X^Z} \) and \( \card{(X^Y)^Z} = \card{X^{Y \times Z}} \) proved by bijections; no set is the size of its 0–1 functions; no set of all sets, once more; \( \nR \), \( \nR \times \nR \), \( \{0,1\}^{\nN} \) and \( \powerset{\nN} \) all of one size; the methods: encode and decode, and prove a law of sizes by a bijection. The review exercises reach back across this volume and *Logic and Proof*."
6. **Named moves.** Delete the "Name the choice" line and add, first:
   - "**Pigeonhole** (@exm-method-pigeonhole). Choose pigeons and fewer holes, define 'the hole of a pigeon', and conclude that two pigeons share a hole. (Section 4.1)"

   The other five lines are kept.
7. **Threads.**
   - Add first: "**Lattice points.** Section 1.1 left a puzzle about five lattice points half solved; Section 4.1 finishes it with the pigeonhole principle (@exm-five-lattice-points)."
   - Keep "The five strings" and "Russell to Cantor".
   - **Choice**, replaced: "Section 2.4 could not build a right inverse of an arbitrary surjection. Section 4.2 avoids choice with least preimages, Section 4.4 turns an injection into a surjection and leaves the converse open, and Section 4.5 absorbs countable sets only into sets that come with a copy of \( \nN \). Chapter 6 adds the axiom of choice and settles all three."
   - **Comparability**: "… Chapter 6 answers it" (no section number).
   - **Same size**: "The bijections of Section 2.4 say when two sets have the same size; Section 4.1 makes this a definition, Section 4.5 makes it arithmetic, and Section 5.2 names the requirement that arithmetic of sizes not depend on representatives: well-definedness."
8. **Summary**, replaced: "Two sets have the same size when there is a bijection between them (@def-equinumerous). A finite set has one number of elements (@cor-finite-size-unique), and there is no injection from a finite set into one with fewer elements (@cor-pigeonhole-finite-sets). Countable means listable (@def-countable), in three equivalent forms (@thm-countable-characterizations). Countable sets are closed under subsets, images, unions of two sets and finite products, so \( \nZ \) and \( \nQ \) are countable (@thm-integers-rationals-countable). The diagonal shows that the 0–1 sequences, \( \powerset{\nN} \) and \( \nR \) are too big to be listed, and that no set maps onto its power set (@thm-binary-sequences-uncountable, @cor-powerset-naturals-uncountable, @thm-reals-uncountable-decimal, @thm-cantor). Sizes are compared by injections. An injection from a non-empty set gives a surjection back (@prp-injection-gives-surjection), and injections both ways give a bijection (@thm-schroder-bernstein). A copy of \( \nN \) absorbs any countable set (@prp-copy-of-naturals-absorbs). Sizes add, multiply and exponentiate, with the laws of exponents proved by bijections (@thm-cardinal-laws); so \( \card{\nR} = \card{\powerset{\nN}} \), and the plane is the size of the line (@thm-reals-power-set-naturals, @thm-plane-equinumerous-line). No proof in the chapter uses the axiom of choice.

   What is open: does every infinite set contain a copy of \( \nN \)? Does a surjection give an injection back? Are any two sets comparable? Chapter 6 answers all three with the axiom of choice. Next, Chapter 5 studies relations, and 'same size' returns there as an example."
9. **Terms.**
   - Delete "choice function".
   - Add, in alphabetical order:
     - "**equinumerous**: there is a bijection \( A \to B \), written \( \card{A} = \card{B} \) (@def-equinumerous)";
     - "**finite**: equinumerous with \( \{1, \dots, n\} \) for some \( n \in \nN \) (@def-finite)";
     - "**infinite**: not finite (@def-infinite)".

### 4.1 Section 4.1 (`01-finite-sets.md`): one exercise, titles, one pointer moved

1. Delete the comment at 41:666.
2. Insert **`exr-finite-sets-c3`** `[C3: Counting injections]` after the end of `exr-finite-sets-c2`, before 41:666. Retitle `exr-restriction-extension-and-gluing-c1` as `[C4: Counting extensions]`.

   **Stem.** "Let \( k, n \in \nN \), and let \( I(k, n) \) be the set of injections \( \{1, \dots, k\} \to \{1, \dots, n\} \). For \( n \ge 1 \) and \( v \in \{1, \dots, n\} \), let \( s_v \colon \{1, \dots, n - 1\} \to \{1, \dots, n\} \setminus \{v\} \) send \( x \) to \( x \) if \( x < v \) and to \( x + 1 \) if \( x \ge v \). One checks that \( s_v \) is a bijection, with inverse \( t_v \) given by \( t_v(y) = y \) for \( y < v \) and \( t_v(y) = y - 1 \) for \( y > v \); you may use this.
   - (a) Show that \( I(k, n) = \emptyset \) if \( k > n \).
   - (b) Let \( k + 1 \le n \). Show that \( \varphi \mapsto \bigl(\varphi(k + 1),\ t_v \circ \varphi|_{\{1, \dots, k\}}\bigr) \), where \( v = \varphi(k + 1) \), is a bijection \( I(k + 1, n) \to \{1, \dots, n\} \times I(k, n - 1) \).
   - (c) Deduce that \( I(k, n) \) has \( n!/(n - k)! \) elements when \( k \le n \). How many injections \( \{1, 2\} \to \{1, 2, 3\} \) are there? List them."

   **Hint 1.** "For (b), the inverse sends \( (v, \psi) \) to the function equal to \( s_v \circ \psi \) on \( \{1, \dots, k\} \) and to \( v \) at \( k + 1 \). To check the facts about \( s_v \) and \( t_v \) of the stem, treat \( x < v \) and \( x \ge v \) (and \( y < v \), \( y > v \)) separately; \( y - 1 \in \nN \) for \( y > v \ge 1 \)."

   **Solution.**
   - (a) \( \{1, \dots, k\} \) has \( k \) elements and \( \{1, \dots, n\} \) has \( n < k \) (@def-finite), so there is no injection by @cor-pigeonhole-finite-sets (a).
   - (b) Write \( \Phi(\varphi) \) for the pair. Since \( \varphi \) is injective, \( \varphi(i) \ne \varphi(k + 1) = v \) for \( i \le k \). So \( \varphi|_{\{1, \dots, k\}} \) takes values in \( \{1, \dots, n\} \setminus \{v\} \); with its codomain shrunk to \( \{1, \dots, n\} \setminus \{v\} \) (same rule, @def-function) it is still injective, and \( t_v \circ \varphi|_{\{1, \dots, k\}} \in I(k, n - 1) \), as a composite of injections (@prp-restriction-properties (d), @thm-composition-injective-surjective (a)). For \( (v, \psi) \) in the target, let \( \Psi(v, \psi) \) be \( s_v \circ \psi \) on \( \{1, \dots, k\} \) and \( v \) at \( k + 1 \). This is a function by @thm-gluing, since the two pieces are disjoint and cover \( \{1, \dots, k + 1\} \). It is injective by @prp-injective-across-pieces: \( s_v \circ \psi \) is injective, a map on one point is injective, and the values of \( s_v \) differ from \( v \). Round trips: \( \Psi(\Phi(\varphi)) \) takes the value \( v = \varphi(k + 1) \) at \( k + 1 \) and \( s_v(t_v(\varphi(i))) = \varphi(i) \) at \( i \le k \), so it is \( \varphi \) (@prp-function-equality). And \( \Phi(\Psi(v, \psi)) = (v, t_v \circ s_v \circ \psi) = (v, \psi) \). By @thm-bijection-iff-inverse, \( \Phi \) is a bijection.
   - (c) Induction on \( k \) (@fd1:ax-induction), with the statement "for every \( n \ge k \), \( I(k, n) \) has \( n!/(n - k)! \) elements".
     - *Base.* \( I(0, n) \) has one element, the empty function, which is injective (@prp-empty-function (a)); and \( n!/n! = 1 \).
     - *Step.* Let \( k + 1 \le n \). Then \( n \ge 1 \) and \( k \le n - 1 \), so \( I(k, n - 1) \) has \( (n - 1)!/(n - 1 - k)! \) elements. By (b) and @exr-finite-sets-c2 (a), \( I(k + 1, n) \) has \( n \cdot (n - 1)!/(n - 1 - k)! = n!/(n - (k + 1))! \) elements, using \( n! = (n - 1)! \, n \) (@def-sum-product) and @prp-equinumerous-properties with @cor-finite-size-unique to carry the count across \( \Phi \).

     So \( I(2, 3) \) has \( 3!/1! = 6 \) elements. Written as value pairs \( (\varphi(1), \varphi(2)) \), they are \( (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2) \).

   **Marking scheme (10).** (a) 2: the two sizes 1, pigeonhole 1; (b) 5: the codomain shrunk and lands in \( I(k, n - 1) \) 1, \( \Psi \) by gluing 1, \( \Psi \) injective across the pieces 1, the round trips 2; (c) 3: base 1, step with C2 (a) 2.
   **Fatal errors** (0 for the step): "\( n \) choices for the first value, \( n - 1 \) for the next, …", with no bijection behind it.

   **Ledger:** "exr-finite-sets-c3 (stem): s_v is a bijection with inverse t_v (stated as a fact) | lem-naturals-arithmetic (c) for y - 1 in N; verify/ch04/exr-finite-sets-c3.py" and "exr-finite-sets-c3 (solution): n! = (n-1)! n; I(2,3) has 6 elements | def-sum-product (cited); exr-finite-sets-c2 (an exercise cited by an exercise); verify/ch04/exr-finite-sets-c3.py". The sidecar also checks the range and round trips of \( s_v \), \( t_v \) for \( n \le 6 \).
3. **41:428**, the second sentence ("Section 6.1 proves that it fails for **every** infinite set.") is deleted from the running text. The Looking-ahead box (41:457–462, "[Looking ahead]" at 41:459) gains a second sentence: "Section 4.5 runs the hotel's move inside any set that contains a copy of \( \nN \)." (Section 4.5's own box carries the Chapter 6 promise.) The ledger key of any claim on 41:428 moves to the box.

### 4.2 Section 4.3 (`03-diagonal-arguments.md`): hand edits (R9)

1. Delete the comment at 43:3.
2. **43:5**, first sentence: "Every infinite set met so far has turned out to be countable: \( \nN \), \( \nZ \), \( \nQ \), and finite products of countable sets." The rest is kept.
3. **43:188**, first sentence: "By @thm-power-set-two-power (Section 2.3), \( S \mapsto \ind_S \) is a bijection \( \powerset{\nN} \to \{0, 1\}^{\nN} \), with inverse \( b \mapsto \{ n \in \nN : b(n) = 1 \} \)." The rest is kept.
4. **B4 (a) solution, 43:356.** Keep from "(a) **False:** the set is countable." to "… determined by \( a(0), \dots, a(p - 1) \)." Replace everything after it with:

   "So \( a = \Lambda(p, F) \) with \( F \coloneqq \{ r < p : a(r) = 1 \} \), where for \( p \in \nZ_{>0} \) and a finite \( F \subseteq \nN \), \( \Lambda(p, F) \) is the sequence \( n \mapsto \ind_F(r) \), with \( r \) the remainder of \( n \) on division by \( p \). Each \( \Lambda(p, F) \) is periodic with period \( p \), so the set of periodic sequences is the image of \( \Lambda \) on \( \nZ_{>0} \times \sF \), where \( \sF \) is the set of finite subsets of \( \nN \). That domain is countable by @exr-countable-sets-c1, @prp-countable-subset and @cor-product-countable, so the image is countable (@prp-countable-image). No choice is made: \( \Lambda \) is a formula. The diagonal fails here because the flipped diagonal of a list of periodic sequences need not be periodic: this is the first usual failure of @exm-method-diagonal."

   Sidecar `verify/ch04/exr-diagonal-arguments-b4.py`: check \( \Lambda(p, F) \) against the \( p \)-patterns for \( p \le 6 \). The ledger line 43:456 becomes "… (a) periodic sequences are Λ(p, F); Z>0 × finite subsets countable; image countable | thm-division-algorithm (F2.2 §02), exr-countable-sets-c1 (an exercise cited by an exercise), prp-countable-subset, cor-product-countable, prp-countable-image (cited); verify/ch04/exr-diagonal-arguments-b4.py".
5. Nothing else changes. `cor-transcendental-exist` is already parked, and no remaining text mentions algebraic or transcendental numbers (grep). 43:254 ("so no choice is involved") cites nothing and stays.

### 4.3 Section 4.4 (`04-comparing-cardinalities.md`): hand edits (R10)

1. **At 44:54**, replacing the comment, add (≈ 280 words):
   - Lead sentence: "Exercise B4 (c) of Section 4.3 turned an injection around into a surjection; here is that move once for all, with no choice made." (Prose, not a reason: the proof below does not lean on the exercise.)
   - **`prp-injection-gives-surjection`** `[An Injection Gives a Surjection Back]`: "Let \( A \) and \( B \) be sets with \( A \ne \emptyset \). If \( \card{A} \le \card{B} \), then there is a surjection \( B \to A \)."
   - **Proof**, verbatim from the \( (\Rightarrow) \) paragraph of 61:150, without its "\( (\Rightarrow) \)" tag: "Let \( f \colon A \to B \) be an injection. Since \( A \ne \emptyset \), @thm-left-inverse-iff-injective (b) gives a left inverse \( g \colon B \to A \), so \( g \circ f = \id_A \). This says that \( f \) is a right inverse of \( g \) (@def-left-right-inverse), so \( g \) is surjective by @prp-right-inverse-surjective."
   - Paragraph (≤ 120 words): "The hypothesis \( A \ne \emptyset \) is needed. For \( A = \emptyset \) and \( B = \{b\} \), the empty function is an injection \( \emptyset \to \{b\} \), but there is no function \( \{b\} \to \emptyset \) at all (@prp-empty-function (b)), let alone a surjection. The converse would turn a surjection \( g \colon B \to A \) into an injection \( A \to B \) by sending each \( a \) to one of its preimages, as the least preimage did for \( B = \nN \) in Section 4.2. For an arbitrary \( B \) there is no such rule, and nothing in this chapter decides the converse. The remark at the end of the section says where it is settled."
   - **Quick check:** "The inclusion \( \nN \to \nZ \) is an injection. Which surjection \( \nZ \to \nN \) does the proof produce if the left inverse sends every point outside the image to \( 0 \)?"

     *Solution:* "\( g(n) = n \) for \( n \ge 0 \) and \( g(n) = 0 \) for \( n < 0 \). It is onto, since \( g(n) = n \) for every \( n \in \nN \), and \( g \circ \iota = \id_{\nN} \)."
1a. **After 44:142** ("The answer to the prompt …"), before 44:144 (added 2026-10-26 by the Chapter 2 blueprint's S2, `ch02-functions.md` §6; layout R4): the paragraph cut from 2.3 (23:163 at `09cf1f1`), ≈ 95 words, retitled and with its references made explicit: "**The definition of h as a gluing.** In the proof above, the pieces were \( C \) and \( A \setminus C \): disjoint, and covering \( A \). So the definition of \( h \) is a gluing in the sense of @exm-method-gluing (Section 2.3), with nothing to check in its step (2), and "each \( a \) falls under exactly one case" is steps (1) and (2) at once: the pieces cover \( A \), and there is no overlap to check. The proof's Case 3 of injectivity, one point in \( C \) and one outside, is step (4)'s comparison across pieces; Cases 1 and 2 are the checks inside each piece." It is part of 4.4's M+ changed-only review.
2. **44:144**, first sentence: "Every value of \( h \) is given by a rule, so nothing in the proof is chosen: Step 1 is a recursion with an explicit step, and Step 2 picks the unique preimage, where there is nothing to choose." The rest is kept.
3. **44:245–249**, the Looking-ahead box. Keep the first three sentences (through "… cannot exhaust an uncountable set."). Replace "Section 6.3 proves … @ax-choice. Nothing in this chapter needs comparability." with: "Chapter 6 adds the axiom of choice, proves with it the converse of @prp-injection-gives-surjection, and shows from Zorn's lemma that any two sets are comparable. Nothing in this chapter needs either fact."
4. **Ledger.**
   - 44:442 is retagged: "… any two sets are comparable, Chapter 6 | F2.4 §03 (thm-cardinal-comparability) …".
   - Add "prp-injection-gives-surjection (claim): (Looking ahead) the converse holds with choice | F2.4 §01 (prp-card-le-surjection; prose pointer; nothing depends on it)".
   - Add "prp-injection-gives-surjection (claim): (Quick check) g o iota = id_N | inline".
5. No new exercise. 44 B4 is the P-or-D item and is unchanged.

### 4.4 Section 4.5 (`05-cardinal-arithmetic.md`): rebuilt, choice-free (F)

Expected main line ~3,900, with folds of 156 unchanged. Edits in file order:

1. Delete the comments at 45:3, 45:292 and 45:378.
2. **Hook (45:9–13).** Delete 45:11, the \( \nN^{\nN} \) question. 45:13 becomes: "Guess the answer before reading on. The plane is a product, and the line will turn out to be a power: a power of \( 2 \)."
3. **New subsection after 45:55**, the "No subtraction" warning, before "## Multiplying …": **`## Infinite sets without choice`** (≈ 520 words).
   - **Lead (≤ 90):** "Section 4.1 moved every guest of Hilbert's hotel one room up (the Quick check after @exm-hilbert-hotel) and so found \( \nN \) equinumerous with the proper subset \( \nN \setminus \{0\} \). The same move works inside any set that comes with a copy of \( \nN \), that is, with an injection \( s \colon \nN \to X \): move \( s(n) \) to \( s(n + 1) \), and leave every other point where it is. The copy is given, so every value of the new map is given by a rule, and nothing is chosen. The move also absorbs a countable set added from outside."
   - **`prp-copy-of-naturals-absorbs`** `[A Copy of ℕ Absorbs Countable Sets]`: "Let \( X \) be a set, and let \( s \colon \nN \to X \) be an injection. (a) \( \card{X \setminus \{s(0)\}} = \card{X} \). (b) If \( C \) is countable and \( C \cap X = \emptyset \), then \( \card{X \cup C} = \card{X} \)."
   - **Idea (≤ 60):** "(a) is the hotel, run on \( S \coloneqq s(\nN) \). For (b), \( S \cup C \) is countable and infinite, hence the same size as \( S \). A bijection \( S \cup C \to S \), glued to the identity off \( S \), absorbs \( C \)."
   - **Proof (a).** Take 61:310–324 verbatim (the \( (\Rightarrow) \) paragraph through "… with \( \card{X} = \card{Y} \)."), without the "\( (\Rightarrow) \)" tag and without 61:308 (the \( (\Leftarrow) \) paragraph), with these changes:
     - "Let \( X \) be infinite. By @thm-infinite-countable-subset there is an injection \( n \mapsto x_n \) from \( \nN \) to \( X \); let \( S \coloneqq \{ x_n : n \in \nN \} \)." becomes "Let \( x_n \coloneqq s(n) \) and \( S \coloneqq \{ x_n : n \in \nN \} \).";
     - the last paragraph (61:324) is replaced by: "So \( h \) is a bijection \( X \to X \setminus \{s(0)\} \), and \( \card{X \setminus \{s(0)\}} = \card{X} \)." ("This proves the theorem" and the proper subset \( Y \) go.)

     It keeps the case definition of \( h \), "*\( h \) is injective.*" and "*\( h \) is onto \( X \setminus \{x_0\} \).*", with @lem-naturals-arithmetic (c).
   - **Proof (b)**, new: "The set \( S \) is countable, as the image of \( \nN \) (@prp-countable-image), so \( S \cup C \) is countable (@prp-union-two-countable). It is infinite. \( S \) is equinumerous with \( \nN \) via \( s \), and \( \nN \) is infinite (@exm-hilbert-hotel); if \( S \cup C \) were finite, so would be its subset \( S \) (@prp-subset-finite), and then \( \nN \) (@prp-equinumerous-properties, @def-finite). By @thm-countable-characterizations (iii), \( S \cup C \) is countably infinite, so there is a bijection \( \psi \colon S \cup C \to S \) (@prp-equinumerous-properties). Now \( X \cup C \) is the union of the disjoint sets \( X \setminus S \) and \( S \cup C \) (disjoint because \( C \cap X = \emptyset \)), and \( X \) is the union of the disjoint sets \( X \setminus S \) and \( S \). Let \( h \colon X \cup C \to X \) be the identity on \( X \setminus S \) and \( \psi \) on \( S \cup C \), a function by @thm-gluing. It is injective by @prp-injective-across-pieces: both pieces are injective, and a value on the first piece lies in \( X \setminus S \), a value on the second in \( S \). It is onto, since the target pieces \( X \setminus S \) and \( S \) cover \( X \) and each is hit. So \( \card{X \cup C} = \card{X} \)."
   - **Aftermath (≤ 80):** "By @thm-finite-no-proper-copy, (a) shows again that a set with a copy of \( \nN \) is infinite. For the disjoint union just defined: in \( \nR \sqcup \nN \), the part \( \nR \times \{0\} \) has the copy \( n \mapsto (n, 0) \), and \( \nN \times \{1\} \) is countable and disjoint from it, so \( \card{\nR \sqcup \nN} = \card{\nR \times \{0\}} = \card{\nR} \). The proposition says nothing about a set that is merely known to be infinite: finding a copy of \( \nN \) inside it would mean picking new points one at a time, with no rule."
   - **Quick check:** "For \( X = \nR \) and \( s(n) = n \), write down the bijection \( h \colon \nR \to \nR \setminus \{0\} \) of the proof of (a), and compute \( h(3) \), \( h(-3) \) and \( h(\tfrac12) \)."

     *Solution:* "\( h(x) = x + 1 \) for \( x \in \nN \), and \( h(x) = x \) otherwise. So \( h(3) = 4 \), \( h(-3) = -3 \) and \( h(\tfrac12) = \tfrac12 \). No point is sent to \( 0 \), and every \( m \in \nN \setminus \{0\} \) is \( h(m - 1) \)."
4. **45:145.** "The Quick check before 3.4's Looking-ahead remark" becomes "The Quick check before the Looking-ahead remark of Section 4.4".
5. **45:196**, the usual failure of `exm-method-encode`. "(the interleaving of decimals, later in this section)" becomes "(reading a decimal as a code, when \( 0.0999\ldots \) and \( 0.1000\ldots \) are two codes for one number, Section 4.3)".
6. **45:290–301.** Keep the heading. The new first line (≤ 40): "Section 2.3 proved that \( A \mapsto \ind_A \) is a bijection \( \powerset{X} \to \{0, 1\}^X \) (@thm-power-set-two-power). With Cantor's theorem it gives one more strict inequality." In the Idea of `cor-cantor-two-power`, "with the theorem just proved" becomes "with @thm-power-set-two-power". The proof is unchanged. The 4.5 drafter checks every citation of `thm-power-set-two-power` (45:305, 45:341, 45:447, 45:533): each reads it as an equality of cardinalities, which still holds, since 2.3's new statement gives a bijection and |A| = |B| abbreviates one (@def-equinumerous); add "(@def-equinumerous)" at 45:341.
7. **45:380**, rewritten: "So the guess of the hook was wrong: the plane is no bigger than the line. For every infinite set \( X \) it is in fact true that \( \card{X \times X} = \card{X} \), but this cannot be proved without the axiom of choice, and this book does not prove it." (\( \nN^{\nN} \) stays an exercise, 4.4 B4 (d); the hook no longer asks about it.)
8. **Looking-ahead box (45:382–386).** Keep its text, and add a second sentence: "Chapter 6 shows, with the axiom of choice, that every infinite set has an injection from \( \nN \), so that @prp-copy-of-naturals-absorbs applies to every infinite set."
9. **C2, "What survives" (45:562).** Replace the paragraph with: "*What survives.* On the sequences that are eventually \( 0 \), the sum is finite (\( \sum_{k < K} b(k) 2^k \) for any \( K \) past the last \( 1 \)), and \( N \) is defined there. That set is countable, and binary digits are not needed to see it. The map \( b \mapsto \{ k \in \nN : b(k) = 1 \} \) is injective, since two sequences with the same \( 1 \)-places are equal (@prp-function-equality). It sends an eventually zero sequence to a finite subset of \( \nN \) (@prp-subset-finite), and the finite subsets of \( \nN \) form a countable set (@exr-countable-sets-c1). Compose with an injection of that set into \( \nN \) (@thm-countable-characterizations, @thm-composition-injective-surjective (a)). The injectivity of \( N \) itself needs the uniqueness of binary digits, which is Step 3 of the solution of @exr-countable-sets-c1." In the marking scheme, the last line becomes "1: notes that the injectivity of \( N \) needs the uniqueness of binary digits (Exercise C1 of Section 4.2)." Ledger 45:676 becomes "exr-cardinal-arithmetic-c2 (solution): eventually zero sequences inject into the finite subsets of N | exr-countable-sets-c1 (an exercise cited by an exercise), prp-subset-finite (cited)".
10. **New B5** after B4: **`exr-cardinal-arithmetic-b5`** `[B5: Absorbing without choice]`.

    **Stem.** "Use @prp-copy-of-naturals-absorbs to show:
    - (a) \( \card{\nR \setminus \nQ} = \card{\nR} \);
    - (b) \( \card{\nR \setminus \{0, 1\}} = \card{\nR} \);
    - (c) \( \card{\{0, 1\}^{\nN} \setminus E} = \card{\{0, 1\}^{\nN}} \), where \( E \) is the set of sequences \( b \) that are eventually zero (there is a \( K \in \nN \) with \( b(k) = 0 \) for all \( k \ge K \)).

    In each part, name \( X \), \( s \) and, where used, \( C \)."

    **Solution.**
    - (a) \( X \coloneqq \nR \setminus \nQ \), \( s(n) \coloneqq \sqrt 2 + n \). Each \( s(n) \in X \): if \( \sqrt 2 + n = q \in \nQ \), then \( \sqrt 2 = q - n \in \nQ \), against @fd1:thm-sqrt2-irrational. And \( s \) is injective, by cancelling \( \sqrt 2 \). Take \( C \coloneqq \nQ \), which is countable (@thm-integers-rationals-countable) and disjoint from \( X \), with \( X \cup C = \nR \). By (b) of the proposition, \( \card{\nR} = \card{X} \), and @prp-equinumerous-properties gives the claim.
    - (b) \( X \coloneqq \nR \setminus \{0, 1\} \), \( s(n) \coloneqq n + 2 \), injective with values in \( X \); \( C \coloneqq \{0, 1\} \), finite, hence countable (@thm-countable-characterizations), and disjoint from \( X \). Then \( X \cup C = \nR \). (Or apply (a) of the proposition twice: to \( \nR \) with \( s(n) = n \), then to \( \nR \setminus \{0\} \) with \( s(n) = n + 1 \).)
    - (c) \( X \coloneqq \{0, 1\}^{\nN} \setminus E \), with \( s(n) \) the sequence that is \( 0 \) before place \( n \) and \( 1 \) from place \( n \) on. It is not eventually zero, so \( s(n) \in X \). Different \( n \) give sequences that differ at the smaller index, so \( s \) is injective. \( C \coloneqq E \) is countable: \( b \mapsto \{ k \in \nN : b(k) = 1 \} \) is injective (@prp-function-equality) and sends \( E \) into the finite subsets of \( \nN \) (each such set lies in some \( \{0, \dots, K - 1\} \), @prp-subset-finite), which form a countable set (@exr-countable-sets-c1); composing with an injection of that set into \( \nN \) gives an injection \( E \to \nN \) (@thm-countable-characterizations, @thm-composition-injective-surjective (a)). It is disjoint from \( X \), and \( X \cup E = \{0, 1\}^{\nN} \). (Compare Exercise C2, which meets \( E \) again.)

    **Ledger:** "exr-cardinal-arithmetic-b5 (solution): sqrt 2 + n irrational | thm-sqrt2-irrational (F1, cited); Q arithmetic, school fact" and "exr-cardinal-arithmetic-b5 (solution): (c) eventually zero sequences inject into the finite subsets of N | exr-countable-sets-c1 (an exercise cited by an exercise), prp-subset-finite (cited)".
11. **Ledger, other lines.** Delete the parked-pointer residue. Add:
    - "prp-copy-of-naturals-absorbs (proof): pieces disjoint and covering; the glued map is injective and onto | thm-gluing, prp-injective-across-pieces (cited)";
    - "prp-copy-of-naturals-absorbs (claim): (Looking ahead) every infinite set has an injection from N, with choice | F2.4 §01 (thm-infinite-countable-subset; prose pointer)";
    - "(45:380) |X x X| = |X| for infinite X needs choice; not proved in this book | prose pointer, nothing depends on it".
12. **Unchanged:** the R group (R1–R3), the method boxes, the two Scratch works and their tables, and B1–B4.

### 4.5 Note on Chapter 4 and choice

After §4.2–§4.4, the scan of binding rule 2 must return no citation. The approved prose pointers in the kept running text of the M+ sections, exempt from binding rule 4, are exactly these, all with no `@`: 41:205 ("Section 6.1 meets surjections …"), 41:582–613 (C1's "no infinitely many choices"), 42:125, 42:303 ("Section 6.1 takes up such unions") and 42:331. 41:428's pointer moves into 4.1's Looking-ahead box (§4.1 item 3), and 41:461 already stands in that box. No other forward pointer in running text is allowed.

### 4.6 Section 5.3 (`03-orders.md`): R12

**53:246.** Keep the first sentence. Then: "For a non-empty partially ordered set the answer 'yes' is Zorn's lemma, and it cannot be proved from what we have. Chapter 6 adds the axiom of choice, states Zorn's lemma and uses it, and proves from Zorn's lemma that every set has a well-order; the proof that the axiom of choice implies Zorn's lemma is left to *Axiomatic Set Theory*, Chapter 4."

Ledger 53:494 becomes "… | F2.4 (choice, Zorn and the well-ordering theorem; prose pointer), ST.4 (AC ⇒ Zorn); nothing depends on them".

**Owner.** This pass (drafter (ii), Sonnet). The Chapter 6 blueprint, frozen after its S2 at commit `99c0cf8`, §6, records the same: the remark and ledger 53:494 belong to the Ch4/5 pass, with this ledger tag, and Chapter 6's drafters do not touch 53. Its quotation of the remark ("… proves from it …") is a paraphrase; the text above, with "from Zorn's lemma", is the one drafted.

### 4.7 `ch05-relations/index.md`

1. Remove the S3 marker.
2. **ix5:5.** After "… does not depend on which integer names a piece.", insert: "Every function gives such a relation, 'same value', and factors through its classes as a surjection, a bijection and an injection."
3. **What you need (ix5:9).**
   - Delete ", and the axiom of choice (@ax-choice), for one remark".
   - Add to the Chapter 2 list: images (@def-image), restriction and inclusion maps (@def-restriction-extension), gluing for one exercise (@thm-gluing, @exm-piecewise-as-gluing), composites of injections and surjections (@thm-composition-injective-surjective), inverse functions (@def-inverse-function) and the empty function (@prp-empty-function).
   - Add to the Chapter 4 list: disjoint unions of finite sets (@prp-disjoint-union-count).
4. **Time (ix5:11).** "the exit check 4.2 C1" becomes "the exit check 5.2 C1". The target is about 22 h core and 28 h full (layout §1); the coordinator recomputes it.
5. **Roadmap**, 5.2 bullet: "sizes of subsets as a last example" becomes "the fibers of a function, and the factorization of every function as a quotient map, a bijection and an inclusion".
6. **Threads.**
   - In "Same size", "Section 2.4" stays, and "(@exm-same-size-subsets)" stays: a link into a fold opens it.
   - Add: "**Fractions.** Section 2.1 found that 'send \( p/q \) to \( p \)' is not a function (@exm-not-a-function). Section 5.2 locates the failure with the factorization (@exm-fraction-map-factorization), and *Number Systems*, Chapter 2 builds \( \nQ \) as these classes."
7. **Summary.** After the \( \nZ/n \) sentence, add: "The fibers of a function are the classes of 'same value', one for each value (@prp-fibres-partition), and every function is a quotient map followed by a bijection and an inclusion (@thm-canonical-factorization)."
8. **Terms.** Add "**fiber**: the preimage \( f^{-1}(\{y\}) \) of one point (@exm-fibres-of-function)".

### 4.8 Section 5.2 (`02-equivalence-relations.md`): merged and cut to 5,000 (F)

The new order of the main line is: clock, equivalence relations, classes, partition theorem, partitions to relations, congruence (with the reals mod ℤ folded), operations on classes, **the fibers of a function**, **every function factors**, Looking ahead. The new folds are F5.2-a to F5.2-i, each `::: {.second-reading title="…"}`. Counts in brackets are main-line words saved, measured with `prose_words` of `tools/check_structure.py` on the `09cf1f1` text (S2 round 1).

1. **52:3, opening.** Append: "Last, every function sorts its domain into the classes of 'same value', its fibers, and factors through them." (+18)
   **52:68 fold**, second paragraph: "as an example later in this section checks" becomes "as the fold on the reals modulo the integers, at the end of 'Congruence modulo n', checks" (prose, no `@`: the example is now in fold F5.2-d).
2. **52:249** goes verbatim into **F5.2-a** `title="Where (P2) does its work"`. [65]
3. **52:239**, "A correspondence, proved both ways", goes verbatim into **F5.2-b** `title="The correspondence as two inverse maps"`. 52:237 and the Quick check 52:241–247 stay on the main line. The check's solution says "by the correspondence", which @thm-partition-equivalence (c) states. [103]
4. **52:301.** Split the paragraph:
   - the main line keeps "So \( \nZ/12 \) … if and only if \( a \) and \( b \) leave the same remainder on division by \( n \).";
   - the sentences "Indeed, … \( [a] = [r] = [b] \)." go verbatim into **F5.2-c** `title="The remainder test, proved"`;
   - "With \( n = 2 \), …" follows the fold as its own paragraph. [26]
5. **52:303–353**, the old "Two more sources".
   - Delete the heading and 52:305.
   - `exm-fibres-of-function` (52:307–329, with the "Two instances" paragraph) moves to item 8.
   - `exm-reals-mod-integers` (52:331–347), the picture paragraph 52:349 and the fold 52:351–353 become **one fold F5.2-d** `title="The reals modulo the integers, and a set with no length"`. It is placed at the end of "Congruence modulo n" and holds, verbatim, the example, 52:349 and 52:352. Its lead is "Congruence identifies integers that differ by a multiple of \( n \); the same idea on the real line, with \( n = 1 \), gives an example that later chapters return to."

   This is allowed: no proof cites the example. 61:154 names it in prose ("Section 5.2 (after exm-reals-mod-integers)"), and B4 (c) restates the relation, so it can be done with the fold closed. The ledger keeps its lines. [295: 52:303–306 deleted, 34; 52:331–349 folded, 261; 52:351–353 was already folded]
6. **52:443** ("That is the method … with failure.") is deleted. [14]
7. **52:445–461**, the lead "The check is not special …", `exm-same-size-subsets` and 52:461, move into F5.2-e (item 8). The Looking-ahead box 52:463–467 moves to the end of the main line (item 10).
8. **New subsection `## The fibers of a function`** after "Operations on classes". It replaces 52:469–539.
   - Delete the comment at 52:469.
   - Delete "Functions on the clock" (52:471–488). Its (Q1) is the universal property, parked to ST. Append the text verbatim to `fd2/authoring/parked/st/from-5.2-fibres-and-factorization.md` under a bold line "Hook removed from 5.2 at S3 (2026-10-26)". [291]
   - **Lead (≤ 45, new):** "Congruence is one way to manufacture an equivalence relation. Here is the most general way. A function sorts its domain: put two points in one pile when the function gives them the same value."
   - `exm-fibres-of-function`, verbatim, then the "Two instances" paragraph (52:329), verbatim.
   - The 52:490 heading is absorbed into this subsection. 52:492–496 (the recall) is deleted; 52:498, the italic sentence, is kept. [57]
   - `prp-fibres-partition`, verbatim. Its Idea (68 words) is cut to: "For (b), every class is the fiber over the value at its representative, and different values have disjoint, non-empty fibers." [50]
   - **Proof (a)** is replaced by one sentence; the old text is deleted, not folded, since it repeats the solution of `exm-fibres-of-function` directly above: "*(a)* By @exm-fibres-of-function the classes of \( \sim_f \) are the fibers over the points of \( f(X) \), and they partition \( X \) by @thm-classes-partition (d)." The proof of (b) is verbatim. [35]
   - 52:521 goes verbatim into **F5.2-i** `title="Values and piles"` (cut (r6) of item 11). The Quick check 52:523–529, verbatim.
   - The Quick check 52:533–539 is deleted; it repeats the remainder instance of 52:329. [33]
   - **F5.2-e** `title="Same size, revisited"` holds, verbatim, 52:445 (its second sentence becomes "Section 4.1 met the check of well-definedness for the number of elements of a finite set."), `exm-same-size-subsets`, 52:461, and 52:531. In 52:531, "The proposition explains a computation of Section 5.2. In @exm-same-size-subsets, the subsets" becomes "@prp-fibres-partition explains this example: the subsets". [381]
9. **`## Every function factors`** (52:541–631).
   - 52:543: "Now (Q2)." becomes "What does a function look like once its domain has been sorted by value?" The rest of 52:543 and the diagram are kept.
   - The theorem statement and the proof are verbatim.
   - **52:568–581**, the Scratch work and its table, is replaced by an **Idea** (≤ 70): "The candidate is forced: \( \iota \) changes no value, so \( f = \iota \circ \bar f \circ q \) gives \( \bar f([x]) = f(x) \). The rule reads a representative, so the first check is well-definedness (@exm-method-well-definedness): \( [x] = [x'] \) gives \( f(x) = f(x') \). The same line read backwards is injectivity. Surjectivity is the definition of \( f(X) \), and uniqueness holds because \( q \) is onto." [87: 134 out, 47 in]
   - **52:603.** Keep through "… sit at the two ends." Then: "The function \( f \) is injective exactly when \( q \) is, and surjective exactly when \( f(X) = Y \), that is, when \( \iota = \id_Y \)." The two-way argument, "if \( f \) is injective and \( q(x) = q(x') \) … and \( x = x' \)", goes verbatim into **F5.2-f** `title="Why f and q are injective together"`. [30]
   - The warning 52:605–607 goes verbatim into **F5.2-g** `title="Onto the image, not the codomain"`. The section keeps its warnings at 52:84 and 52:201. [54]
   - **52:618.** "It is the relation of Exercise B1 in Section 5.2 (@exr-equivalence-relations-b1), now seen as the fiber relation of a function; that it is an equivalence relation is also immediate from @exm-fibres-of-function." becomes "It is the relation of Exercise B1 at the end of this section, now seen as the fiber relation of a function; that it is an equivalence relation is immediate from @exm-fibres-of-function." This removes an `@` to a later block.
   - The rest of the example and the Quick check 52:625–631 are verbatim.
10. **End of the main line:** the Looking-ahead box from 52:463–467, verbatim. It is the section's only forward pointer, and STATUS row 189 stays valid.
11. **Count** (measured at `09cf1f1`; S2 round 1). The main line to `## Exercises` measures 6,652, of which 33 are the comment at 52:469 (deleted in item 8): base **6,619**. Savings of items 2–9: 65 + 103 + 26 + 295 + 14 + 291 + 57 + 50 + 35 + 33 + 381 + 87 + 30 + 54 = 1,521. New text: 18 (item 1) + 34 (lead, item 8) + 11 (item 9, 52:543) = 63. So 6,619 − 1,521 + 63 ≈ **5,160 before the cuts below**, which are part of the plan, not optional. The drafter applies them **in this order** and stops as soon as the measured main line is ≤ 5,000:
    - (r1) the solution of `exm-first-equivalences` (d) (52:63) moves verbatim into the existing fold 52:68, as its first paragraph [29];
    - (r2) 52:405 ("In the language of @def-function …") moves verbatim into **F5.2-h** `title="Well defined means a function"` [54];
    - (r3) the last two sentences of 52:150 ("The quotient map forgets … identified\".") are deleted [28];
    - (r4) the sentence "On the clock: … multiple of \( 12 \)." in 52:195 is deleted; the clock is worked at 52:5–11 [27];
    - (r5) in the "Two instances" paragraph (52:329), "Two instances." and the first instance ("For \( f(x) = \abs{x} \) … the class \( \{-3, 3\} \).") are deleted; "same absolute value" and its class \( \{-3, 3\} \) already stand at `exm-first-equivalences` (c) and 52:106 [20];
    - (r6) 52:521 moves verbatim into **F5.2-i** `title="Values and piles"`, placed right after the proof of `prp-fibres-partition` [42];
    - (r7, reserve) the third sentence of 52:237 ("An equivalence relation and a partition are two descriptions … lists the piles.") is deleted; the named move "*classes from a relation, a relation from classes*" stays on the main line [≈ 25].

    Expected after (r1)–(r6): **≈ 4,960** main line; folded ≈ 583 + 65 + 103 + 26 + 261 + 30 (F5.2-d lead) + 381 + 30 + 54 + 54 + 29 + 42 ≈ **1,660** (≤ 1,900). These are estimates from measured parts; the binding figure is the drafter's measurement with `python3 tools/check_structure.py --book fd2 --words` and the to-Exercises split described in the header. If (r1)–(r7) still leave it above 5,000, the drafter stops and reports the figure to the coordinator; nothing else is folded without a blueprint change.
12. **Exercises.**
    - Retitles as in §3.
    - A1 (e) stays; it cites `exm-fibres-of-function`, which is earlier.
    - **B4** gains two parts, under the same stem ("Prove or disprove: each rule defines a function."):
      - "(f) With \( \sim_f \) for \( f(x) = x^2 \) on \( \nR \), the rule \( \nR/{\sim_f} \to \nR \), \( [x] \mapsto x^3 \)."
      - "(g) With the same relation, the rule \( \nR/{\sim_f} \to \nR \), \( [x] \mapsto \abs{x} \)."

      *Solutions:*
      - "(f) False. \( [1] = [-1] \), since \( 1^2 = (-1)^2 \) (@thm-classes-partition (b)), but \( 1^3 = 1 \ne -1 = (-1)^3 \): one class, two values."
      - "(g) True. If \( [x] = [x'] \), then \( x^2 = x'^2 \), so \( \abs{x}^2 = \abs{x'}^2 \) with \( \abs{x}, \abs{x'} \ge 0 \), and two non-negative reals with equal squares are equal (@fd1:thm-squares-order). So the value does not depend on the representative: one class, one value."

      Sidecar `verify/ch05/exr-equivalence-relations-b4.py`: add (f) and (g) sample checks.
    - **Ledger.**
      - Add "exm-reals-mod-integers (claim): (now in fold F5.2-d) unchanged lines".
      - Add "exr-equivalence-relations-b4 (solution): (f) 1 != -1; (g) equal squares of non-negatives | thm-squares-order (F1, cited)".
      - Any ledger line about 52:471–488 is deleted (there are none at `09cf1f1`).

---

## 5. Budgets and Time

| § | Main now | Budget | Expected | Folds |
|---|---|---|---|---|
| 4.1 | 4,930 | as is | 4,930 | 219 |
| 4.3 | 3,406 | as is | ~3,400 | 0 |
| 4.4 | 2,348 | 5,000 | ~2,750 | 0 |
| 4.5 | 3,354 | 5,000 | ~3,900 | 156 |
| 5.2 | 6,619 | 5,000 | ~4,960 (after (r1)–(r6)) | ~1,660 |
| 5.3 | as is | as is | as is | 0 |

**Exercises added:** 4.1 C3, 4.5 B5, and 52 B4 (f), (g). **Time:** Chapter 4 about 30 h core and 45 h full; Chapter 5 about 22/28 (layout §1). The coordinator recomputes both after S3 and writes them into the indexes.

## 6. Pointers, promises, edits outside the files

- **STATUS promise rows.**
  - Retag 44:442 (comparability) to F2.4 §03.
  - Add "converse of `prp-injection-gives-surjection` (F2.3 §04, Looking ahead) → F2.4 §01 `prp-card-le-surjection`".
  - Add "every infinite set has a copy of ℕ (F2.3 §05, Looking ahead) → F2.4 §01 `thm-infinite-countable-subset`".
  - Retag the F2.5 §03 row for 53:246 to F2.4 §03 (well-ordering theorem) and ST.4 (AC ⇒ Zorn), per layout R12.
  - Rows 186 and 188 (after `exm-reals-mod-integers`) stay; the passage is now in fold F5.2-d.
  - Row 195 stays.
- **NOTATION.** No change. Row 83 (F2.3 §05, `def-disjoint-union`) and rows 247 and 298 (F2.5 §02) stay correct.
- **For the Chapter 6 blueprint** (record only; not edited here).
  - 61:150, the \( (\Rightarrow) \) half of `prp-card-le-surjection`, can cite `@prp-injection-gives-surjection`.
  - The first half of 61:155 now lives in 4.4.
  - The \( (\Rightarrow) \) proof of `thm-infinite-iff-proper-subset` (61:310–324) and `exr-infinite-sets-b2` can cite `@prp-copy-of-naturals-absorbs` (a), (b) after `thm-infinite-countable-subset`.
  - `exr-infinite-sets-c2` has a choice-free twin in 4.5 B5 (a).
  - The 61:162 pointer "the correspondence of Section 2.1" becomes `@thm-power-set-two-power`.
- **For the Chapter 2 blueprint.** Nothing to change: 2.2's Looking-ahead box says "counts the injections between finite sets", naming no number, and that wording is accepted (§3). Chapter 4 cites the Ch2 pass's new `prp-injective-across-pieces` (2.3) in 4.1 C3 and in 4.5 (`prp-copy-of-naturals-absorbs` (b)); the Chapter 4 drafter lands after the Ch2 pass, or checks that the label exists before citing it.
- **Parked file.** The 52:471–488 hook is appended to `fd2/authoring/parked/st/from-5.2-fibres-and-factorization.md` (§4.8 item 8).
- **Ledgers** (coordinator, S4, `tools/ledger.py`): `ch04.yaml` and `ch05.yaml` items for the edited passages; the claims of the deleted 52:471–488 and 52:533–539 become stale and are removed.

## 7. S2a: claims to verify

1. The scan of binding rule 2 after S3: no `@` from 41–45, 52 or 53 to a Chapter 6 label or to an `exr-infinite-sets-*` or `exr-countable-unions-and-choice-*` label. `tools/check_forward_deps.py` and `build.py check` are clean.
2. 4.1 C3: the stem's facts on \( s_v \), \( t_v \) (range, both round trips; sidecar); \( \Phi \) lands in \( \{1, \dots, n\} \times I(k, n - 1) \) after the codomain is shrunk; \( \Psi \) is injective by `prp-injective-across-pieces`; the step \( n \cdot (n - 1)!/(n - 1 - k)! = n!/(n - k - 1)! \); \( I(2, 3) \) has 6 elements; the citation of C2 (a) is an exercise citing an earlier exercise.
3. 4.3 B4 (a): every periodic \( a \) with period \( p \) equals \( \Lambda(p, F) \) (with \( F \subseteq \{0, \dots, p - 1\} \)); each \( \Lambda(p, F) \) is periodic; \( \nZ_{>0} \times \sF \) is countable from C1 of 4.2, `prp-countable-subset` and `cor-product-countable`; no union over \( p \) is taken.
4. 4.3: 43:5 lists only sets proved countable in 4.2; 43:188 cites `thm-power-set-two-power`, which is earlier (2.3).
5. 4.4: the proof of `prp-injection-gives-surjection` is choice-free (`thm-left-inverse-iff-injective` (b) defines \( g \) by cases with a fixed \( a_0 \)); the \( A = \emptyset \) example; the Quick check's \( g \) is onto with \( g \circ \iota = \id_{\nN} \); the Looking-ahead box holds both promises and nothing else points forward.
6. 4.5 `prp-copy-of-naturals-absorbs`: (a) verbatim from 61 with the copy given; (b) \( S \cup C \) countable and infinite; proof (a) is 61:310–324 without the \( (\Leftarrow) \) paragraph and with the new last sentence; the gluing pieces are disjoint and cover; injectivity by `prp-injective-across-pieces`, onto by covering target pieces; the lead cites the one-room-up Quick check, not the \( 2n \) move; \( \nR \sqcup \nN \) in the aftermath (\( \nR \times \{0\} \) and \( \nN \times \{1\} \) are disjoint, and \( \card{\nR \times \{0\}} = \card{\nR} \)); the Quick check values.
7. 4.5 B5: (a) \( \sqrt 2 + n \notin \nQ \), and \( s \) is injective; (b) \( \{0, 1\} \) is countable; (c) \( s(n) \) is not eventually zero, \( s \) is injective, and \( E \) is countable by the inline injection into the finite subsets of \( \nN \) (no citation of the later C2).
8. 4.5 C2: the injection into finite subsets; 4.2 C1's Step 3 is the uniqueness of binary digits.
9. 4.5: 45:380 uses no exercise as a reason and states no unproved equivalence with choice; the hook no longer asks about \( \nN^{\nN} \); no "later in this section" pointer is left at 45:196.
10. 5.2: every fold holds no cited statement and no only check or only warning (main-line warnings 52:84 and 52:201 remain); with folds closed, A1–B5 can be done (B4 (c) restates its relation); the main line is ≤ 5,000 after the cuts of item 11 applied in order; folds ≤ 1,900; proof (a) of `prp-fibres-partition` is one sentence and the 52:68 fold names the reals-mod-ℤ fold in prose.
11. 5.2 order: no forward `@` (fibres after operations, so F5.2-e's use of `exm-method-well-definedness` is backward); 52:618 has no `@` to a later exercise; the moved Looking-ahead box is at the end of the main line.
12. 5.2 B4 (f), (g): \( [1] = [-1] \); `thm-squares-order` gives equal non-negatives from equal squares; (g) claims nothing about the image of \( x \mapsto x^2 \).
13. 5.3 R12: the remark's claim that Chapter 6 proves the well-ordering theorem from Zorn's lemma matches layout §1's 6.3 row and the Chapter 6 blueprint.
14. Indexes: every label in ix4 and ix5 exists and is no later than the chapter (ix4 cites no Chapter 6 label); the Terms are alphabetical.

15. Running-text forward pointers in 41–45 are exactly §4.5's list; 41:428's pointer now stands in 4.1's Looking-ahead box.

## 8. Notes for S3 and S4

- **Drafters** (lean workflow: one at a time).
  - (i) **Chapter 4** (Opus): `fd2/src/ch04-cardinality/05-cardinal-arithmetic.md` and `04-comparing-cardinalities.md`, then the minor edits to `01-finite-sets.md` and `03-diagonal-arguments.md`, which Sonnet may take.
  - (ii) **Chapter 5** (Opus): `fd2/src/ch05-relations/02-equivalence-relations.md`, then `03-orders.md` (Sonnet), and the append to `fd2/authoring/parked/st/from-5.2-fibres-and-factorization.md`.

  The coordinator writes `ch04-cardinality/index.md` and `ch05-relations/index.md` last, against the delivered sections.
- **Sidecars.**
  - New: `fd2/verify/ch04/exr-finite-sets-c3.py` (brute-force \( |I(k, n)| \) for \( n \le 6 \), and \( \Phi \) bijective for small cases); `exr-cardinal-arithmetic-b5.py` (the \( s(n) \) of (c) pairwise different on prefixes); `prp-copy-of-naturals-absorbs.py` (\( h \) on a finite window of the Quick check).
  - Edited: `exr-diagonal-arguments-b4.py` and `fd2/verify/ch05/exr-equivalence-relations-b4.py`.
- **Checkers:** `./build.py check`, `check_structure.py` (0 fatal; main line ≤ 5,000), `check_forward_deps.py`, `check_numbers.py`, `check_notation.py`, the binding-rule-2 grep, and `atlas.py all` before any atlas commit.
- **Review (lean).**
  - 4.5 and 5.2 run S5–S8 with changed-only blind review: the new subsection, B5, C2, and every move and fold of 5.2.
  - 4.1, 4.3, 4.4 and 5.3 get the changed-only blind review of the M+ row (layout §7).
  - Then S7, with the re-referee as S7r. S9 sampling stays with the author.
- **Calls made here, for the author (not blocking).** (1) The injection count is an exercise, not an example (§3). (2) `exm-reals-mod-integers` goes into a fold to meet the cap. (3) The old 5.2 hook ("Functions on the clock") is cut, not condensed, since half of it introduced the parked universal property.

## S2 replies (round 1)

Two blind referees (R1, R2). Every finding applied unless stated. Word counts re-measured with `prose_words` at `09cf1f1`.

**Referee 1**
1. *Hotel citation (error).* Applied: the 4.5 lead cites "the Quick check after @exm-hilbert-hotel" and names \( \nN \setminus \{0\} \); §1 says the same.
2. *B5 (c) cites the later C2 (error).* Applied: \( E \) is defined in the stem and its countability is proved inline (injection into the finite subsets of \( \nN \), `exr-countable-sets-c1`, composition); C2 is "compare" only. Ledger line added.
3. *5.2 budget does not hold (gap).* Applied. Savings corrected to measured values (items 3, 4, 5, 8, 9 and the Idea cut); base 6,652 − 33 = 6,619; before the cuts ≈ 5,160. Item 11 now lists seven cuts, applied in order until ≤ 5,000: (r1) (d) solution into fold 52:68, 29; (r2) 52:405 into F5.2-h, 54; (r3) 52:150's last two sentences deleted, 28; (r4) 52:195's clock sentence deleted, 27; (r5) the \( \abs{x} \) instance of 52:329 deleted, 20; (r6) 52:521 into F5.2-i, 42; (r7, reserve) 52:237's third sentence, ≈ 25. Expected ≈ 4,960. The referee's 52:237 candidate is narrowed to one sentence, so that the named move stays on the main line; the old (r3) fold is replaced by R2's one-sentence proof (R2 item 10).
4. *53:246 text and owner differ between blueprints (gap).* Applied. The Chapter 6 blueprint, as frozen after its S2 (commit `99c0cf8`, §6), hands the remark and ledger 53:494 to this pass, with this blueprint's ledger tag; so the owner is this pass (drafter (ii)) and the tag stays "F2.4 (choice, Zorn and the well-ordering theorem; prose pointer), ST.4 (AC ⇒ Zorn)". The ambiguous "proves from it" now reads "proves from Zorn's lemma". The frozen Chapter 6 blueprint is not edited; §4.6 records that its quotation is a paraphrase.
5. *Proof (a) line range (minor).* Applied: 61:310–324 without the \( (\Leftarrow) \) paragraph and the tag; new last sentence "So \( h \) is a bijection \( X \to X \setminus \{s(0)\} \), and \( \card{X \setminus \{s(0)\}} = \card{X} \)."
6. *44:245–249 drops the recursion sentence (minor).* Applied: keep the first three sentences.
7. *ix4:5 is six sentences (minor).* Applied.
8. *B4 (g) overreach (minor).* Applied: the two sentences are replaced by "So the value does not depend on the representative: one class, one value."
9. *C3 codomain shrink; lem-naturals-arithmetic (minor).* Applied: the codomain is shrunk explicitly (with `prp-restriction-properties` (d)); `lem-naturals-arithmetic` (c) moves to the stem's ledger line (\( y - 1 \in \nN \)), now that the \( t_v \) checks are a stated fact (R2 item 6).
10. *"C1–C4 retitled"; Ch2 Looking-ahead wording (minor).* Applied: "gluing C1 retitled C4". The Ch2 wording, which names no number, is accepted; nothing to change in the Ch2 blueprint (§3, §6).
11. *Running-text forward pointers (minor).* Applied: §4.5 lists the approved prose pointers (41:205, 41:582–613, 42:125, 42:303, 42:331) and rule 4 exempts them; 41:428's pointer is deleted from the running text and 4.1's Looking-ahead box gains "Section 4.5 runs the hotel's move inside any set that contains a copy of \( \nN \)." (4.5's box keeps the Chapter 6 promise, so it is not repeated). 41:461 already stands in the box.

**Referee 2**
1. *"every power set" is uncountable (error).* Applied with the referee's text.
2. *Hotel citation (gap).* Applied (R1 item 1).
3. *B5 (c) cites C2 (gap).* Applied (R1 item 2); part (c) kept.
4. *45:380 rewrite (gap).* Applied with the referee's text; the \( \nN^{\nN} \) and \( X \sqcup X \) clauses and "(the first is equivalent to it)" are gone; ledger line updated.
5. *prp-injective-across-pieces taught twice (gap).* Applied: cited in C3 (b) and in proof (b) of `prp-copy-of-naturals-absorbs`; added to ix4 "What you need"; ledger line changed from "inline" to the citation. §6 notes the dependency on the Ch2 pass.
6. *C3 too fussy (gap).* Applied: \( s_v \) and \( t_v \) are given in the stem as facts; old (b) dropped; parts (a), (b), (c) with marks 2 / 5 / 3; the range checks go to the sidecar and Hint 1.
7. *4.4 repeats (minor).* Applied: lead "Exercise B4 (c) of Section 4.3 turned an injection around into a surjection; here is that move once for all, with no choice made." (marked as prose, not a reason); the least-preimage recap cut to a clause.
8. *Summary drops \( A \ne \emptyset \) (minor).* Applied.
9. *B4 (g) off-task (minor).* Applied (R1 item 8).
10. *Proof (a) of prp-fibres-partition (minor).* Applied: replaced on the main line by the referee's one sentence and deleted, not folded; the Idea keeps only its (b) sentence. F5.2-i now holds 52:521 (cut (r6)). Folded total ≈ 1,660.
11. *Rule 4 and running-text pointers (minor).* Applied (R1 item 11).
12. *53:246 "it" (minor).* Applied (R1 item 4).
13. *Roadmap replacement not explicit (minor).* Applied: "Replace the six old bullets with these five", naming the deleted ones.
14. *52:68 points from fold to fold (minor).* Applied in prose: "as the fold on the reals modulo the integers, at the end of 'Congruence modulo n', checks" (no `@` to a later block, matching 52:618's repair).
