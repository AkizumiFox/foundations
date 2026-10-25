<!-- hand-written -->
# Revision blueprint: F2.3 Cardinality (fd2 Chapter 4) and F2.5 Relations, Section 5.2 (fd2 Chapter 5), stage S1

**Status: S1, 2026-10-26.** Next: S2 (lean: one blind referee, hand round 2), S2a, then S3.

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
4. **One forward pointer per section.** It goes in the `[Looking ahead]` box at the end of the main line (STYLE §12.1). A second promise goes into the same box, not into the running text.

---

## 1. Devices as applied

- **Method sections and boxes.** The boxes are unchanged:
  - `exm-method-pigeonhole` (4.1), `exm-method-list-it` (4.2), `exm-method-diagonal` (4.3), `exm-method-injections-both-ways` (4.4);
  - `exm-method-encode` and `exm-method-laws-by-bijection` (4.5);
  - `exm-method-well-definedness` (5.2).

  No new box is added. The new 4.4 proposition and the new 4.5 proposition reuse the moves of 2.4 (construct and verify) and of 4.1 (the hotel).
- **Scratch work and Givens/Goal tables** already stand at each method's first full appearance: 45:155–167 (`exm-pairing-bijection`), 45:230–240 (`thm-cardinal-laws` (d)) and 52:373–386 (`prp-congruence-arithmetic`). Fading is as follows:
  - well-definedness falls to an **Idea** at `thm-canonical-factorization`, its third use (§4.8 item 9);
  - the new 4.5 proposition gets an **Idea**, since the hotel is 4.1's.
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
| 4.1 | `01-finite-sets.md` | 4,930 → as is | new exercise C3 (counting injections); C1–C4 retitled; S3 marker removed |
| 4.3 | `03-diagonal-arguments.md` | 3,406 → ~3,400 | opening (R9); a 2.3 pointer; B4 (a) solution without countable unions |
| 4.4 | `04-comparing-cardinalities.md` | 2,348 → ~2,650 | new `prp-injection-gives-surjection` with its Quick check; 44:144 and 44:245–249 reworded (R10) |
| 4.5 | `05-cardinal-arithmetic.md` | 3,354 → ~3,900 | new subsection "Infinite sets without choice" (`prp-copy-of-naturals-absorbs`, Quick check); hook trimmed; parked pointers repaired; new B5; C2 repaired |
| ix5 | `ch05-relations/index.md` | — | edited (§4.7) |
| 5.2 | `02-equivalence-relations.md` | 6,619 → ≤ 5,000 (~4,990), folds ~1,840 | old 5.2 merged in; "Functions on the clock" removed; nine folds; Scratch work → Idea; B4 (f), (g); exercises retitled |
| 5.3 | `03-orders.md` | as is | 53:246 remark (R12), ledger 53:494 |

## 3. Labels

**New (three):**
- `prp-injection-gives-surjection` (4.4). This is layout §3's "choice-free half of `prp-card-le-surjection`".
- `prp-copy-of-naturals-absorbs` (4.5). This is the choice-free core of old 3.5, layout §1 4.5 row ("Hilbert's hotel revisited").
- `exr-cardinal-arithmetic-b5` (4.5), and `exr-finite-sets-c3` (4.1).

**Kept**, with these retitles:
- 4.1: `exr-finite-sets-c3` is titled `[C3: Counting injections]`, and `exr-restriction-extension-and-gluing-c1` becomes `[C4: Counting extensions]`.
- 5.2: `exr-fibres-and-factorization-a1` → `[A2]`, `exr-fibres-and-factorization-b2` → `[B5: Same fibers]`, `exr-fibres-and-factorization-c1` → `[C3: Equal fibers]`, `exr-restriction-extension-and-gluing-c2` → `[C4: Find the error]`.

**Moved within 5.2:** `exm-fibres-of-function` and `exm-same-size-subsets` move to the new subsection "The fibers of a function". `exm-same-size-subsets` goes inside a fold.

**Deviation from layout §1 (4.1 row).** The counting of injections is an **exercise**, not a worked example. Its count of \( \{1, \dots, n\} \times I(k, n - 1) \) needs the product count, which is only an exercise (`exr-finite-sets-c2` (a)). A main-line example may not use an exercise as a reason. An exercise may cite an earlier one. 2.2's Looking-ahead line (Ch2 blueprint) should read "Section 4.1, Exercise C3".

---

## 4. Per-section plans

### 4.0 `ch04-cardinality/index.md`

Rewrite the page; remove the S3 marker. The title stays `# Cardinality`.

1. **ix4:5, the story.** Keep the first five sentences, from "Are there more rational numbers …" to "… than the set itself.", and keep the decimal sentences ("A second motivating question … by that definition."). Replace the rest of the paragraph with: "It starts from finite sets: Section 4.1 defines 'same size' by bijections, proves the pigeonhole principle and finishes the lattice-point puzzle of Section 1.1. Sections 4.1–4.4 teach one method of proof each: pigeonhole, list a set, run a diagonal, and compare sizes by injections both ways. The last section adds, multiplies and raises sizes to powers, absorbs a countable set into any set that contains a copy of \( \nN \), and finds that the plane and the subsets of \( \nN \) have exactly as many elements as the line. It teaches two more methods: encode and decode, and prove a law of sizes by a bijection."
2. **ix4:7, replaced:** "Every map in this chapter is given by a rule: a formula, a least element, a recursion with an explicit step. Some natural arguments would have to pick one element from each of infinitely many sets, with no rule to say which: a right inverse for every surjection, a copy of \( \nN \) inside every infinite set, one listing for each of countably many countable sets. Where that happens, the chapter says so and leaves the statement open. Chapter 6 adds the principle that settles these statements, the axiom of choice."
3. **What you need (ix4:9).**
   - Change the first sentence to "*Logic and Proof*, Chapters 1–8, and *Sets and Functions*, Chapters 1–3."
   - The ∃E clause becomes "the rule ∃E (@fd1:def-rules-existential), which names one object at a time".
   - In the Chapters 1 and 2 list, replace "the indicator function of a subset (Section 2.1, @exm-first-functions (d))" with "indicator functions and \( \powerset{X} \approx \{0,1\}^X \) (@def-indicator, @thm-power-set-two-power); restriction, extension and gluing (@def-restriction-extension, @thm-gluing)".
   - The Chapter 3 list ends at "(@prp-finite-max)". Delete from "; equinumerous, finite and infinite sets" to "(@exm-method-least-element, @exm-method-pigeonhole)". These are now Section 4.1's own; keep `@exm-method-least-element` in the Chapter 3 list.
   - Keep "(D1)–(D3) … without proof".
   - Delete "Section 6.1 uses one fact from school algebra … real roots."
   - Keep the √2 sentence, extended to "used in Sections 4.2 and 4.5".
4. **Time.** The target is about 30 h core and 45 h full (layout §1). The coordinator recomputes it with `check_structure.py --words` after S3.
5. **Roadmap**, five bullets:
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
8. **Summary**, replaced: "Two sets have the same size when there is a bijection between them (@def-equinumerous). A finite set has one number of elements (@cor-finite-size-unique), and there is no injection from a finite set into one with fewer elements (@cor-pigeonhole-finite-sets). Countable means listable (@def-countable), in three equivalent forms (@thm-countable-characterizations). Countable sets are closed under subsets, images, unions of two sets and finite products, so \( \nZ \) and \( \nQ \) are countable (@thm-integers-rationals-countable). The diagonal shows that the 0–1 sequences, \( \nR \) and every power set are too big to be listed (@thm-binary-sequences-uncountable, @thm-reals-uncountable-decimal, @thm-cantor). Sizes are compared by injections. An injection gives a surjection back (@prp-injection-gives-surjection), and injections both ways give a bijection (@thm-schroder-bernstein). A copy of \( \nN \) absorbs any countable set (@prp-copy-of-naturals-absorbs). Sizes add, multiply and exponentiate, with the laws of exponents proved by bijections (@thm-cardinal-laws); so \( \card{\nR} = \card{\powerset{\nN}} \), and the plane is the size of the line (@thm-reals-power-set-naturals, @thm-plane-equinumerous-line). No proof in the chapter uses the axiom of choice.

   What is open: does every infinite set contain a copy of \( \nN \)? Does a surjection give an injection back? Are any two sets comparable? Chapter 6 answers all three with the axiom of choice. Next, Chapter 5 studies relations, and 'same size' returns there as an example."
9. **Terms.**
   - Delete "choice function".
   - Add, in alphabetical order:
     - "**equinumerous**: there is a bijection \( A \to B \), written \( \card{A} = \card{B} \) (@def-equinumerous)";
     - "**finite**: equinumerous with \( \{1, \dots, n\} \) for some \( n \in \nN \) (@def-finite)";
     - "**infinite**: not finite (@def-infinite)".

### 4.1 Section 4.1 (`01-finite-sets.md`): one exercise, titles

1. Delete the comment at 41:666.
2. Insert **`exr-finite-sets-c3`** `[C3: Counting injections]` after the end of `exr-finite-sets-c2`, before 41:666. Retitle `exr-restriction-extension-and-gluing-c1` as `[C4: Counting extensions]`.

   **Stem.** "Let \( k, n \in \nN \), and let \( I(k, n) \) be the set of injections \( \{1, \dots, k\} \to \{1, \dots, n\} \).
   - (a) Show that \( I(k, n) = \emptyset \) if \( k > n \).
   - (b) For \( n \ge 1 \) and \( v \in \{1, \dots, n\} \), let \( s_v \colon \{1, \dots, n - 1\} \to \{1, \dots, n\} \setminus \{v\} \) send \( x \) to \( x \) if \( x < v \) and to \( x + 1 \) if \( x \ge v \). Show that \( s_v \) is a bijection.
   - (c) Let \( k + 1 \le n \). Show that \( \varphi \mapsto \bigl(\varphi(k + 1),\ s_v^{-1} \circ \varphi|_{\{1, \dots, k\}}\bigr) \), where \( v = \varphi(k + 1) \), is a bijection \( I(k + 1, n) \to \{1, \dots, n\} \times I(k, n - 1) \).
   - (d) Deduce that \( I(k, n) \) has \( n!/(n - k)! \) elements when \( k \le n \). How many injections \( \{1, 2\} \to \{1, 2, 3\} \) are there? List them."

   **Hint 1.** "For (c), the inverse sends \( (v, \psi) \) to the function equal to \( s_v \circ \psi \) on \( \{1, \dots, k\} \) and to \( v \) at \( k + 1 \)."

   **Solution.**
   - (a) \( \{1, \dots, k\} \) has \( k \) elements and \( \{1, \dots, n\} \) has \( n < k \) (@def-finite), so there is no injection by @cor-pigeonhole-finite-sets (a).
   - (b) Let \( t_v(y) \coloneqq y \) if \( y < v \) and \( t_v(y) \coloneqq y - 1 \) if \( y > v \), for \( y \in \{1, \dots, n\} \setminus \{v\} \). Its values lie in \( \{1, \dots, n - 1\} \): if \( y < v \), then \( y \le v - 1 \le n - 1 \); if \( y > v \), then \( 1 \le v \le y - 1 \le n - 1 \). The values of \( s_v \) avoid \( v \): \( x < v \) gives \( x \ne v \), and \( x \ge v \) gives \( x + 1 > v \), with \( x + 1 \le n \). Round trips: for \( x < v \), \( t_v(s_v(x)) = x \); for \( x \ge v \), \( s_v(x) = x + 1 > v \), so \( t_v(s_v(x)) = x \). For \( y < v \), \( s_v(t_v(y)) = y \); for \( y > v \), \( t_v(y) = y - 1 \ge v \), so \( s_v(t_v(y)) = y \). By @thm-bijection-iff-inverse, \( s_v \) is a bijection with inverse \( t_v \).
   - (c) Write \( \Phi(\varphi) \) for the pair. Since \( \varphi \) is injective, \( \varphi(i) \ne \varphi(k + 1) = v \) for \( i \le k \). So \( \varphi|_{\{1, \dots, k\}} \) takes values in \( \{1, \dots, n\} \setminus \{v\} \), and \( t_v \circ \varphi|_{\{1, \dots, k\}} \in I(k, n - 1) \), as a composite of injections (@thm-composition-injective-surjective (a)). For \( (v, \psi) \) in the target, let \( \Psi(v, \psi) \) be \( s_v \circ \psi \) on \( \{1, \dots, k\} \) and \( v \) at \( k + 1 \). This is a function by @thm-gluing, since the two pieces are disjoint and cover \( \{1, \dots, k + 1\} \). It is injective: \( s_v \circ \psi \) is injective, and its values differ from \( v \) by (b). Round trips: \( \Psi(\Phi(\varphi)) \) takes the value \( v = \varphi(k + 1) \) at \( k + 1 \) and \( s_v(t_v(\varphi(i))) = \varphi(i) \) at \( i \le k \), so it is \( \varphi \) (@prp-function-equality). And \( \Phi(\Psi(v, \psi)) = (v, t_v \circ s_v \circ \psi) = (v, \psi) \). By @thm-bijection-iff-inverse, \( \Phi \) is a bijection.
   - (d) Induction on \( k \) (@fd1:ax-induction), with the statement "for every \( n \ge k \), \( I(k, n) \) has \( n!/(n - k)! \) elements".
     - *Base.* \( I(0, n) \) has one element, the empty function, which is injective (@prp-empty-function (a)); and \( n!/n! = 1 \).
     - *Step.* Let \( k + 1 \le n \). Then \( n \ge 1 \) and \( k \le n - 1 \), so \( I(k, n - 1) \) has \( (n - 1)!/(n - 1 - k)! \) elements. By (c) and @exr-finite-sets-c2 (a), \( I(k + 1, n) \) has \( n \cdot (n - 1)!/(n - 1 - k)! = n!/(n - (k + 1))! \) elements, using \( n! = (n - 1)! \, n \) (@def-sum-product) and @prp-equinumerous-properties with @cor-finite-size-unique to carry the count across \( \Phi \).

     So \( I(2, 3) \) has \( 3!/1! = 6 \) elements. Written as value pairs \( (\varphi(1), \varphi(2)) \), they are \( (1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2) \).

   **Marking scheme (10).** (a) 1; (b) 2; (c) 4: lands in \( I(k, n - 1) \) 1, \( \Psi \) by gluing and injective 1, the round trips 2; (d) 3: base 1, step with C2 (a) 2.
   **Fatal errors** (0 for the step): "\( n \) choices for the first value, \( n - 1 \) for the next, …", with no bijection behind it.

   **Ledger:** "exr-finite-sets-c3 (solution): t_v values; n! = (n-1)! n; I(2,3) has 6 elements | lem-naturals-arithmetic, def-sum-product (cited); exr-finite-sets-c2 (an exercise cited by an exercise); verify/ch04/exr-finite-sets-c3.py".

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
   - Lead sentence: "Before the theorem, one exchange: an injection can be turned around into a surjection, with no choice made."
   - **`prp-injection-gives-surjection`** `[An Injection Gives a Surjection Back]`: "Let \( A \) and \( B \) be sets with \( A \ne \emptyset \). If \( \card{A} \le \card{B} \), then there is a surjection \( B \to A \)."
   - **Proof**, verbatim from the \( (\Rightarrow) \) paragraph of 61:150, without its "\( (\Rightarrow) \)" tag: "Let \( f \colon A \to B \) be an injection. Since \( A \ne \emptyset \), @thm-left-inverse-iff-injective (b) gives a left inverse \( g \colon B \to A \), so \( g \circ f = \id_A \). This says that \( f \) is a right inverse of \( g \) (@def-left-right-inverse), so \( g \) is surjective by @prp-right-inverse-surjective."
   - Paragraph (≤ 120 words): "The hypothesis \( A \ne \emptyset \) is needed. For \( A = \emptyset \) and \( B = \{b\} \), the empty function is an injection \( \emptyset \to \{b\} \), but there is no function \( \{b\} \to \emptyset \) at all (@prp-empty-function (b)), let alone a surjection. The converse would turn a surjection \( g \colon B \to A \) into an injection \( A \to B \) by sending each \( a \) to one of its preimages. When \( B = \nN \), 'the least preimage' is a rule, and that is how @thm-countable-characterizations went from (i) to (ii). For an arbitrary \( B \) there is no such rule, and nothing in this chapter decides the converse. The remark at the end of the section says where it is settled."
   - **Quick check:** "The inclusion \( \nN \to \nZ \) is an injection. Which surjection \( \nZ \to \nN \) does the proof produce if the left inverse sends every point outside the image to \( 0 \)?"

     *Solution:* "\( g(n) = n \) for \( n \ge 0 \) and \( g(n) = 0 \) for \( n < 0 \). It is onto, since \( g(n) = n \) for every \( n \in \nN \), and \( g \circ \iota = \id_{\nN} \)."
2. **44:144**, first sentence: "Every value of \( h \) is given by a rule, so nothing in the proof is chosen: Step 1 is a recursion with an explicit step, and Step 2 picks the unique preimage, where there is nothing to choose." The rest is kept.
3. **44:245–249**, the Looking-ahead box. Keep the first two sentences. Replace "Section 6.3 proves … @ax-choice. Nothing in this chapter needs comparability." with: "Chapter 6 adds the axiom of choice, proves with it the converse of @prp-injection-gives-surjection, and shows from Zorn's lemma that any two sets are comparable. Nothing in this chapter needs either fact."
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
   - **Lead (≤ 90):** "Section 4.1 moved every guest of Hilbert's hotel one room up (@exm-hilbert-hotel) and so found \( \nN \) equinumerous with a proper subset. The same move works inside any set that comes with a copy of \( \nN \), that is, with an injection \( s \colon \nN \to X \): move \( s(n) \) to \( s(n + 1) \), and leave every other point where it is. The copy is given, so every value of the new map is given by a rule, and nothing is chosen. The move also absorbs a countable set added from outside."
   - **`prp-copy-of-naturals-absorbs`** `[A Copy of ℕ Absorbs Countable Sets]`: "Let \( X \) be a set, and let \( s \colon \nN \to X \) be an injection. (a) \( \card{X \setminus \{s(0)\}} = \card{X} \). (b) If \( C \) is countable and \( C \cap X = \emptyset \), then \( \card{X \cup C} = \card{X} \)."
   - **Idea (≤ 60):** "(a) is the hotel, run on \( S \coloneqq s(\nN) \). For (b), \( S \cup C \) is countable and infinite, hence the same size as \( S \). A bijection \( S \cup C \to S \), glued to the identity off \( S \), absorbs \( C \)."
   - **Proof (a).** Take 61:307–321 verbatim, with these changes:
     - its first sentence becomes "Let \( x_n \coloneqq s(n) \) and \( S \coloneqq \{ x_n : n \in \nN \} \)";
     - "Let \( X \) be infinite. By @thm-infinite-countable-subset there is an injection …" is dropped;
     - the last paragraph ends "… with \( \card{X} = \card{Y} \)."

     It keeps the case definition of \( h \), "*\( h \) is injective.*" and "*\( h \) is onto \( X \setminus \{x_0\} \).*", with @lem-naturals-arithmetic (c).
   - **Proof (b)**, new: "The set \( S \) is countable, as the image of \( \nN \) (@prp-countable-image), so \( S \cup C \) is countable (@prp-union-two-countable). It is infinite. \( S \) is equinumerous with \( \nN \) via \( s \), and \( \nN \) is infinite (@exm-hilbert-hotel); if \( S \cup C \) were finite, so would be its subset \( S \) (@prp-subset-finite), and then \( \nN \) (@prp-equinumerous-properties, @def-finite). By @thm-countable-characterizations (iii), \( S \cup C \) is countably infinite, so there is a bijection \( \psi \colon S \cup C \to S \) (@prp-equinumerous-properties). Now \( X \cup C \) is the union of the disjoint sets \( X \setminus S \) and \( S \cup C \) (disjoint because \( C \cap X = \emptyset \)), and \( X \) is the union of the disjoint sets \( X \setminus S \) and \( S \). Let \( h \) be the identity on \( X \setminus S \) and \( \psi \) on \( S \cup C \), a function by @thm-gluing. Each piece is a bijection onto the matching piece of \( X \), and the two target pieces are disjoint and cover \( X \). So \( h \) is injective and onto, and \( \card{X \cup C} = \card{X} \)."
   - **Aftermath (≤ 80):** "By @thm-finite-no-proper-copy, (a) shows again that a set with a copy of \( \nN \) is infinite. For the disjoint union just defined: in \( \nR \sqcup \nN \), the part \( \nR \times \{0\} \) has the copy \( n \mapsto (n, 0) \), and \( \nN \times \{1\} \) is countable and disjoint from it, so \( \card{\nR \sqcup \nN} = \card{\nR \times \{0\}} = \card{\nR} \). The proposition says nothing about a set that is merely known to be infinite: finding a copy of \( \nN \) inside it would mean picking new points one at a time, with no rule."
   - **Quick check:** "For \( X = \nR \) and \( s(n) = n \), write down the bijection \( h \colon \nR \to \nR \setminus \{0\} \) of the proof of (a), and compute \( h(3) \), \( h(-3) \) and \( h(\tfrac12) \)."

     *Solution:* "\( h(x) = x + 1 \) for \( x \in \nN \), and \( h(x) = x \) otherwise. So \( h(3) = 4 \), \( h(-3) = -3 \) and \( h(\tfrac12) = \tfrac12 \). No point is sent to \( 0 \), and every \( m \in \nN \setminus \{0\} \) is \( h(m - 1) \)."
4. **45:145.** "The Quick check before 3.4's Looking-ahead remark" becomes "The Quick check before the Looking-ahead remark of Section 4.4".
5. **45:196**, the usual failure of `exm-method-encode`. "(the interleaving of decimals, later in this section)" becomes "(reading a decimal as a code, when \( 0.0999\ldots \) and \( 0.1000\ldots \) are two codes for one number, Section 4.3)".
6. **45:290–301.** Keep the heading. The new first line (≤ 40): "Section 2.3 proved that \( A \mapsto \ind_A \) is a bijection \( \powerset{X} \to \{0, 1\}^X \) (@thm-power-set-two-power). With Cantor's theorem it gives one more strict inequality." In the Idea of `cor-cantor-two-power`, "with the theorem just proved" becomes "with @thm-power-set-two-power". The proof is unchanged.
7. **45:380**, rewritten: "So the guess of the hook was wrong: the plane is no bigger than the line. Neither is \( \nN^{\nN} \): Exercise B4 (d) of Section 4.4 gives \( \card{\nN^{\nN}} = \card{\{0, 1\}^{\nN}} \), which is \( \card{\nR} \) by @thm-reals-power-set-naturals. For every infinite set \( X \) it is in fact true that \( \card{X \times X} = \card{X} \) and \( \card{X \sqcup X} = \card{X} \). In general these cannot be proved without the axiom of choice (the first is equivalent to it), and this book does not prove them."
8. **Looking-ahead box (45:382–386).** Keep its text, and add a second sentence: "Chapter 6 shows, with the axiom of choice, that every infinite set has an injection from \( \nN \), so that @prp-copy-of-naturals-absorbs applies to every infinite set."
9. **C2, "What survives" (45:562).** Replace the paragraph with: "*What survives.* On the sequences that are eventually \( 0 \), the sum is finite (\( \sum_{k < K} b(k) 2^k \) for any \( K \) past the last \( 1 \)), and \( N \) is defined there. That set is countable, and binary digits are not needed to see it. The map \( b \mapsto \{ k \in \nN : b(k) = 1 \} \) is injective, since two sequences with the same \( 1 \)-places are equal (@prp-function-equality). It sends an eventually zero sequence to a finite subset of \( \nN \) (@prp-subset-finite), and the finite subsets of \( \nN \) form a countable set (@exr-countable-sets-c1). Compose with an injection of that set into \( \nN \) (@thm-countable-characterizations, @thm-composition-injective-surjective (a)). The injectivity of \( N \) itself needs the uniqueness of binary digits, which is Step 3 of the solution of @exr-countable-sets-c1." In the marking scheme, the last line becomes "1: notes that the injectivity of \( N \) needs the uniqueness of binary digits (Exercise C1 of Section 4.2)." Ledger 45:676 becomes "exr-cardinal-arithmetic-c2 (solution): eventually zero sequences inject into the finite subsets of N | exr-countable-sets-c1 (an exercise cited by an exercise), prp-subset-finite (cited)".
10. **New B5** after B4: **`exr-cardinal-arithmetic-b5`** `[B5: Absorbing without choice]`.

    **Stem.** "Use @prp-copy-of-naturals-absorbs to show:
    - (a) \( \card{\nR \setminus \nQ} = \card{\nR} \);
    - (b) \( \card{\nR \setminus \{0, 1\}} = \card{\nR} \);
    - (c) \( \card{\{0, 1\}^{\nN} \setminus E} = \card{\{0, 1\}^{\nN}} \), where \( E \) is the set of eventually zero sequences (Exercise C2).

    In each part, name \( X \), \( s \) and, where used, \( C \)."

    **Solution.**
    - (a) \( X \coloneqq \nR \setminus \nQ \), \( s(n) \coloneqq \sqrt 2 + n \). Each \( s(n) \in X \): if \( \sqrt 2 + n = q \in \nQ \), then \( \sqrt 2 = q - n \in \nQ \), against @fd1:thm-sqrt2-irrational. And \( s \) is injective, by cancelling \( \sqrt 2 \). Take \( C \coloneqq \nQ \), which is countable (@thm-integers-rationals-countable) and disjoint from \( X \), with \( X \cup C = \nR \). By (b) of the proposition, \( \card{\nR} = \card{X} \), and @prp-equinumerous-properties gives the claim.
    - (b) \( X \coloneqq \nR \setminus \{0, 1\} \), \( s(n) \coloneqq n + 2 \), injective with values in \( X \); \( C \coloneqq \{0, 1\} \), finite, hence countable (@thm-countable-characterizations), and disjoint from \( X \). Then \( X \cup C = \nR \). (Or apply (a) of the proposition twice: to \( \nR \) with \( s(n) = n \), then to \( \nR \setminus \{0\} \) with \( s(n) = n + 1 \).)
    - (c) \( X \coloneqq \{0, 1\}^{\nN} \setminus E \), with \( s(n) \) the sequence that is \( 0 \) before place \( n \) and \( 1 \) from place \( n \) on. It is not eventually zero, so \( s(n) \in X \). Different \( n \) give sequences that differ at the smaller index, so \( s \) is injective. \( C \coloneqq E \) is countable by Exercise C2's "what survives", and \( X \cup E = \{0, 1\}^{\nN} \).

    **Ledger:** "exr-cardinal-arithmetic-b5 (solution): sqrt 2 + n irrational | thm-sqrt2-irrational (F1, cited); Q arithmetic, school fact".
11. **Ledger, other lines.** Delete the parked-pointer residue. Add:
    - "prp-copy-of-naturals-absorbs (proof): pieces disjoint and covering; a glued map of bijections onto disjoint covering pieces is a bijection | thm-gluing (cited), inline";
    - "prp-copy-of-naturals-absorbs (claim): (Looking ahead) every infinite set has an injection from N, with choice | F2.4 §01 (thm-infinite-countable-subset; prose pointer)";
    - "(45:380) N^N the size of R | exr-comparing-cardinalities-b4 (d) (prose pointer to an exercise), thm-reals-power-set-naturals".
12. **Unchanged:** the R group (R1–R3), the method boxes, the two Scratch works and their tables, and B1–B4.

### 4.5 Note on Chapter 4 and choice

After §4.2–§4.4, the scan of binding rule 2 must return no citation. 41:582–613 (C1's "no infinitely many choices") and 42:125 and 42:331 name Section 6.1 in prose, with no `@`, and stay.

### 4.6 Section 5.3 (`03-orders.md`): R12

**53:246.** Keep the first sentence. Then: "For a non-empty partially ordered set the answer 'yes' is Zorn's lemma, and it cannot be proved from what we have. Chapter 6 adds the axiom of choice, states Zorn's lemma and uses it, and proves from it that every set has a well-order; the proof that the axiom of choice implies Zorn's lemma is left to *Axiomatic Set Theory*, Chapter 4."

Ledger 53:494 becomes "… | F2.4 (choice, Zorn and the well-ordering theorem; prose pointer), ST.4 (AC ⇒ Zorn); nothing depends on them".

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

The new order of the main line is: clock, equivalence relations, classes, partition theorem, partitions to relations, congruence (with the reals mod ℤ folded), operations on classes, **the fibers of a function**, **every function factors**, Looking ahead. The new folds are F5.2-a to F5.2-i, each `::: {.second-reading title="…"}`. Counts in brackets are main-line words saved.

1. **52:3, opening.** Append: "Last, every function sorts its domain into the classes of 'same value', its fibers, and factors through them." (+20)
2. **52:249** goes verbatim into **F5.2-a** `title="Where (P2) does its work"`. [65]
3. **52:239**, "A correspondence, proved both ways", goes verbatim into **F5.2-b** `title="The correspondence as two inverse maps"`. 52:237 and the Quick check 52:241–247 stay on the main line. The check's solution says "by the correspondence", which @thm-partition-equivalence (c) states. [120]
4. **52:301.** Split the paragraph:
   - the main line keeps "So \( \nZ/12 \) … if and only if \( a \) and \( b \) leave the same remainder on division by \( n \).";
   - the sentences "Indeed, … \( [a] = [r] = [b] \)." go verbatim into **F5.2-c** `title="The remainder test, proved"`;
   - "With \( n = 2 \), …" follows the fold as its own paragraph. [45]
5. **52:303–353**, the old "Two more sources".
   - Delete the heading and 52:305.
   - `exm-fibres-of-function` (52:307–329, with the "Two instances" paragraph) moves to item 8.
   - `exm-reals-mod-integers` (52:331–347), the picture paragraph 52:349 and the fold 52:351–353 become **one fold F5.2-d** `title="The reals modulo the integers, and a set with no length"`. It is placed at the end of "Congruence modulo n" and holds, verbatim, the example, 52:349 and 52:352. Its lead is "Congruence identifies integers that differ by a multiple of \( n \); the same idea on the real line, with \( n = 1 \), gives an example that later chapters return to."

   This is allowed: no proof cites the example. 61:154 names it in prose ("Section 5.2 (after exm-reals-mod-integers)"), and B4 (c) restates the relation, so it can be done with the fold closed. The ledger keeps its lines. [≈ 250]
6. **52:443** ("That is the method … with failure.") is deleted. [14]
7. **52:445–461**, the lead "The check is not special …", `exm-same-size-subsets` and 52:461, move into F5.2-e (item 8). The Looking-ahead box 52:463–467 moves to the end of the main line (item 10).
8. **New subsection `## The fibers of a function`** after "Operations on classes". It replaces 52:469–539.
   - Delete the comment at 52:469.
   - Delete "Functions on the clock" (52:471–488). Its (Q1) is the universal property, parked to ST. Append the text verbatim to `fd2/authoring/parked/st/from-5.2-fibres-and-factorization.md` under a bold line "Hook removed from 5.2 at S3 (2026-10-26)". [291]
   - **Lead (≤ 45, new):** "Congruence is one way to manufacture an equivalence relation. Here is the most general way. A function sorts its domain: put two points in one pile when the function gives them the same value."
   - `exm-fibres-of-function`, verbatim, then the "Two instances" paragraph (52:329), verbatim.
   - The 52:490 heading is absorbed into this subsection. 52:492–496 (the recall) is deleted; 52:498, the italic sentence, is kept. [70]
   - `prp-fibres-partition`, verbatim. Its Idea is cut to: "(a) is @exm-fibres-of-function with @thm-classes-partition. For (b), every class is the fiber over the value at its representative, and different values have disjoint, non-empty fibers." The proof is verbatim. [35]
   - 52:521, verbatim. The Quick check 52:523–529, verbatim.
   - The Quick check 52:533–539 is deleted; it repeats the remainder instance of 52:329. [33]
   - **F5.2-e** `title="Same size, revisited"` holds, verbatim, 52:445 (its second sentence becomes "Section 4.1 met the check of well-definedness for the number of elements of a finite set."), `exm-same-size-subsets`, 52:461, and 52:531. In 52:531, "The proposition explains a computation of Section 5.2. In @exm-same-size-subsets, the subsets" becomes "@prp-fibres-partition explains this example: the subsets". [381]
9. **`## Every function factors`** (52:541–631).
   - 52:543: "Now (Q2)." becomes "What does a function look like once its domain has been sorted by value?" The rest of 52:543 and the diagram are kept.
   - The theorem statement and the proof are verbatim.
   - **52:568–581**, the Scratch work and its table, is replaced by an **Idea** (≤ 70): "The candidate is forced: \( \iota \) changes no value, so \( f = \iota \circ \bar f \circ q \) gives \( \bar f([x]) = f(x) \). The rule reads a representative, so the first check is well-definedness (@exm-method-well-definedness): \( [x] = [x'] \) gives \( f(x) = f(x') \). The same line read backwards is injectivity. Surjectivity is the definition of \( f(X) \), and uniqueness holds because \( q \) is onto." [64]
   - **52:603.** Keep through "… sit at the two ends." Then: "The function \( f \) is injective exactly when \( q \) is, and surjective exactly when \( f(X) = Y \), that is, when \( \iota = \id_Y \)." The two-way argument, "if \( f \) is injective and \( q(x) = q(x') \) … and \( x = x' \)", goes verbatim into **F5.2-f** `title="Why f and q are injective together"`. [55]
   - The warning 52:605–607 goes verbatim into **F5.2-g** `title="Onto the image, not the codomain"`. The section keeps its warnings at 52:84 and 52:201. [60]
   - **52:618.** "It is the relation of Exercise B1 in Section 5.2 (@exr-equivalence-relations-b1), now seen as the fiber relation of a function; that it is an equivalence relation is also immediate from @exm-fibres-of-function." becomes "It is the relation of Exercise B1 at the end of this section, now seen as the fiber relation of a function; that it is an equivalence relation is immediate from @exm-fibres-of-function." This removes an `@` to a later block.
   - The rest of the example and the Quick check 52:625–631 are verbatim.
10. **End of the main line:** the Looking-ahead box from 52:463–467, verbatim. It is the section's only forward pointer, and STATUS row 189 stays valid.
11. **Count.** Savings 65 + 120 + 45 + 250 + 14 + 291 + 70 + 35 + 33 + 381 + 64 + 55 + 60 = 1,483; new text ≈ 65. So 6,619 + 65 − 1,483 ≈ **5,200 before the cuts below**, which are therefore part of the plan, not optional:
    - (r1) the solution of `exm-first-equivalences` (d) moves verbatim into the existing fold 52:68 (≈ 45);
    - (r2) 52:405 ("In the language of @def-function …") moves verbatim into **F5.2-h** `title="Well defined means a function"` (≈ 54);
    - (r3) the proof of `prp-fibres-partition` (a) moves into **F5.2-i** `title="Proof of part (a)"`, with the Idea on the main line; the proof of (b) stays (≈ 110).

    Expected after (r1)–(r3): **≈ 4,990** main line, ≈ 1,840 folded. If the measured count is still above 5,000, also fold (r4) the last two sentences of 52:150 ("The quotient map forgets … identified") (≈ 25). The drafter measures with `python3 tools/check_structure.py --book fd2 --words` and the to-Exercises split described in the header.
12. **Exercises.**
    - Retitles as in §3.
    - A1 (e) stays; it cites `exm-fibres-of-function`, which is earlier.
    - **B4** gains two parts, under the same stem ("Prove or disprove: each rule defines a function."):
      - "(f) With \( \sim_f \) for \( f(x) = x^2 \) on \( \nR \), the rule \( \nR/{\sim_f} \to \nR \), \( [x] \mapsto x^3 \)."
      - "(g) With the same relation, the rule \( \nR/{\sim_f} \to \nR \), \( [x] \mapsto \abs{x} \)."

      *Solutions:*
      - "(f) False. \( [1] = [-1] \), since \( 1^2 = (-1)^2 \) (@thm-classes-partition (b)), but \( 1^3 = 1 \ne -1 = (-1)^3 \): one class, two values."
      - "(g) True. If \( [x] = [x'] \), then \( x^2 = x'^2 \), so \( \abs{x}^2 = \abs{x'}^2 \) with \( \abs{x}, \abs{x'} \ge 0 \), and two non-negative reals with equal squares are equal (@fd1:thm-squares-order). By @thm-canonical-factorization the induced map \( [x] \mapsto x^2 \) is a bijection onto \( [0, \infty) \). The rule of (g) is \( x \mapsto \abs{x} \) passed through \( q \), which is possible exactly because \( \abs{x} \) is constant on fibers."

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
| 4.4 | 2,348 | 5,000 | ~2,650 | 0 |
| 4.5 | 3,354 | 5,000 | ~3,900 | 156 |
| 5.2 | 6,619 | 5,000 | ~4,990 | ~1,840 |
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
  - The \( (\Rightarrow) \) proof of `thm-infinite-iff-proper-subset` (61:307–321) and `exr-infinite-sets-b2` can cite `@prp-copy-of-naturals-absorbs` (a), (b) after `thm-infinite-countable-subset`.
  - `exr-infinite-sets-c2` has a choice-free twin in 4.5 B5 (a).
  - The 61:162 pointer "the correspondence of Section 2.1" becomes `@thm-power-set-two-power`.
- **For the Chapter 2 blueprint.** 2.2's Looking-ahead line on counting maps names "Section 4.1, Exercise C3".
- **Parked file.** The 52:471–488 hook is appended to `fd2/authoring/parked/st/from-5.2-fibres-and-factorization.md` (§4.8 item 8).
- **Ledgers** (coordinator, S4, `tools/ledger.py`): `ch04.yaml` and `ch05.yaml` items for the edited passages; the claims of the deleted 52:471–488 and 52:533–539 become stale and are removed.

## 7. S2a: claims to verify

1. The scan of binding rule 2 after S3: no `@` from 41–45, 52 or 53 to a Chapter 6 label or to an `exr-infinite-sets-*` or `exr-countable-unions-and-choice-*` label. `tools/check_forward_deps.py` and `build.py check` are clean.
2. 4.1 C3: \( t_v \) lands in \( \{1, \dots, n - 1\} \); both round trips of \( s_v \); \( \Phi \) lands in \( \{1, \dots, n\} \times I(k, n - 1) \); \( \Psi \) is injective; the step \( n \cdot (n - 1)!/(n - 1 - k)! = n!/(n - k - 1)! \); \( I(2, 3) \) has 6 elements; the citation of C2 (a) is an exercise citing an earlier exercise.
3. 4.3 B4 (a): every periodic \( a \) with period \( p \) equals \( \Lambda(p, F) \) (with \( F \subseteq \{0, \dots, p - 1\} \)); each \( \Lambda(p, F) \) is periodic; \( \nZ_{>0} \times \sF \) is countable from C1 of 4.2, `prp-countable-subset` and `cor-product-countable`; no union over \( p \) is taken.
4. 4.3: 43:5 lists only sets proved countable in 4.2; 43:188 cites `thm-power-set-two-power`, which is earlier (2.3).
5. 4.4: the proof of `prp-injection-gives-surjection` is choice-free (`thm-left-inverse-iff-injective` (b) defines \( g \) by cases with a fixed \( a_0 \)); the \( A = \emptyset \) example; the Quick check's \( g \) is onto with \( g \circ \iota = \id_{\nN} \); the Looking-ahead box holds both promises and nothing else points forward.
6. 4.5 `prp-copy-of-naturals-absorbs`: (a) verbatim from 61 with the copy given; (b) \( S \cup C \) countable and infinite; the gluing pieces are disjoint and cover; the bijection onto disjoint covering pieces; \( \nR \sqcup \nN \) in the aftermath (\( \nR \times \{0\} \) and \( \nN \times \{1\} \) are disjoint, and \( \card{\nR \times \{0\}} = \card{\nR} \)); the Quick check values.
7. 4.5 B5: (a) \( \sqrt 2 + n \notin \nQ \), and \( s \) is injective; (b) \( \{0, 1\} \) is countable; (c) \( s(n) \) is not eventually zero, \( s \) is injective, and \( E \) is countable by C2.
8. 4.5 C2: the injection into finite subsets; 4.2 C1's Step 3 is the uniqueness of binary digits.
9. 4.5: 45:380's citation of 4.4 B4 (d) matches that exercise (\( \card{\{0, 1\}^{\nN}} = \card{\nN^{\nN}} \), choice-free); the hook no longer asks about \( \nN^{\nN} \); no "later in this section" pointer is left at 45:196.
10. 5.2: every fold holds no cited statement and no only check or only warning (main-line warnings 52:84 and 52:201 remain); with folds closed, A1–B5 can be done (B4 (c) restates its relation); the main line is ≤ 5,000 after (r1)–(r3); folds ≤ 1,900.
11. 5.2 order: no forward `@` (fibres after operations, so F5.2-e's use of `exm-method-well-definedness` is backward); 52:618 has no `@` to a later exercise; the moved Looking-ahead box is at the end of the main line.
12. 5.2 B4 (f), (g): \( [1] = [-1] \); `thm-squares-order` gives equal non-negatives from equal squares.
13. 5.3 R12: the remark's claim that Chapter 6 proves the well-ordering theorem matches layout §1's 6.3 row.
14. Indexes: every label in ix4 and ix5 exists and is no later than the chapter (ix4 cites no Chapter 6 label); the Terms are alphabetical.

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
