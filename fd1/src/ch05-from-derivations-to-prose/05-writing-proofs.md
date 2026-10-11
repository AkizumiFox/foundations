# Writing a Proof

Section 5.4 trained a reader to say what licenses each line of a proof, as @exm-self-explanation did line by line. This section turns to the writer. A proof is written for a reader who will check it in exactly that way, so the writer's job is to make each line's warrant visible. The section gives a procedure that leads from a statement to plain prose, the conventions of written mathematics, each a rule of Chapters 1–4 made audible, and three worked examples.

## A procedure

A reader checks a proof forwards, one line at a time. A writer finds a proof mostly backwards, from the goal. The two directions are not in conflict: Section 2.6 showed that the search for a derivation is goal-directed, and @def-derivation says that the derivation found is a list in which each line cites only lines above it. The procedure below keeps both, the search in scratch work and the derivation on the page. Its steps 3 and 6 use the levels of @def-levels-of-proof and the convention of @def-silent-steps from Section 5.3.

::: {.algorithm}
**Writing a proof of a statement.**

1. **Write the goal in symbols.** Translate the statement, its hypotheses and its conclusion into a formula, as in Section 4.8, with every quantifier and its bound. Read a letter that is not introduced as universally quantified (Section 4.1).
2. **Unwind the definitions.** Replace each defined word ("bounded", "converges", "irrational", "\( \subseteq \)") by its definition, in the hypotheses and in the goal. This is \( \rulename{{\leftrightarrow}E} \) on a definition.
3. **Read the skeleton off the goal** (Section 2.6, extended in Section 4.8), and write it at level 1: the boxes, their first lines and their last lines. Open the \( \rulename{\exists E} \) boxes of existential hypotheses early.
4. **Fill the boxes:** backwards in scratch, forwards on the page. The search runs from the goal; the written proof runs from the hypotheses, each line citing lines above it. What the search found goes into the Idea, not into the Proof.
5. **Choose constants last in the search, and write them first on the page,** each with what it depends on.
6. **Write level 3,** leaving silent exactly the steps that @def-silent-steps allows, and no others.
7. **Reread as a checker:** for each line, is it true, and by which rule does it follow from which available lines? (Section 5.6 makes this a two-column check.)
:::

Steps 1–3 involve no mathematics, only logical form, and they fix the first and last sentence of every box before anything is invented ("skeleton first"). Steps 4 and 5 need a remark each.

**Step 4 as a logical fact.** The search of Section 2.6 opens a box for the goal before it knows how the box will be filled, and it postpones an existential goal until a witness appears; that is why it works backwards. But a derivation is a list in which line \( k \) cites only lines available at \( k \) (@def-derivation), and a written proof is that list in sentences. So the order of the page is forced by the rules, not by taste: "\( \abs{f(x) - f(a)} < \varepsilon \) holds if \( \abs{x - a} < \varepsilon/2 \)" points from a later line to an earlier one. The backward reasoning lives in the Idea block.

**Step 5 as a logical fact.** A chosen constant, such as "let \( \delta \coloneqq \varepsilon/2 \)", is the witness of an \( \rulename{\exists I} \) line. The search finds it last, because only the end of the search shows what it must do. On the page it comes first, right after the names it is built from, because later lines use it. Those names are its dependencies; they must be among the names of the boxes open where it is chosen (Section 4.10).

::: {.check}
Which step of the procedure produces the sentence "Let \( \varepsilon > 0 \)" at the start of a proof that \( a_n \to L \), and which step keeps it at level 3?
:::

::: {.solution}
Step 3. Unwound in step 2, the goal begins \( \forall \varepsilon > 0 \), so its skeleton is a bounded \( \rulename{\forall I} \) box whose assumption is \( \varepsilon_0 > 0 \); "Let \( \varepsilon > 0 \)" is the first line of that box. Step 6 keeps it, because the opening of a \( \rulename{\forall I} \) box is never silent (@def-silent-steps). The closing "since \( \varepsilon \) was arbitrary" may be silent.
:::

## Conventions of written mathematics

A handful of conventions make a proof checkable. Each is a rule of Chapters 1–4 heard in a sentence.

- **Announce the skeleton.** "We prove the contrapositive", "by induction on \( n \)", "we consider two cases", "suppose, for a contradiction, that …". An announcement tells the reader which box is opening, and so what its last line must be.
- **Name every object when it is introduced,** by "let" (an arbitrary object, \( \rulename{\forall I} \)), "choose" (a witness, \( \rulename{\exists E} \), with a fresh name), or "let … \( \coloneqq \) …" (a constant, the witness of \( \rulename{\exists I} \)), and say what a chosen object depends on.
- **One claim per sentence.** A sentence carries one line, or a short chain of lines joined by "so", each step of which the reader can name. Two unrelated claims joined by "and" hide which one is used later.
- **End with what was shown.** The last sentence of a proof is the last line of the derivation, outside every box. If it is not the statement to be proved, the reader should be told how the two are related.
- **Label displayed claims that will be cited,** \( (\ast) \) or (1), and cite them by the label. A citation is a line number in prose.

None of these is a matter of style. An object used without being introduced is a line citing nothing, and an announcement that does not match its box (assuming the conclusion of an implication) proves the converse; these are entries (N9) and (N5) of the catalogue in Section 5.6.

## Matching sentences and rules

The first two examples go in opposite directions.

::: {#exm-annotate-abs}
[Label every sentence]

Here is a short proof. Label each sentence with the rule it uses.

> **Claim.** For a real number \( x \), if \( \abs{x - 1} < 1 \), then \( x > 0 \).
>
> *Proof.* (1) Assume \( \abs{x - 1} < 1 \). (2) Either \( x \ge 1 \) or \( x < 1 \). (3) Suppose first that \( x \ge 1 \). (4) Then \( x \ge 1 > 0 \). (5) Suppose instead that \( x < 1 \). (6) Then \( x - 1 < 0 \), so \( \abs{x - 1} = 1 - x \). (7) Hence \( 1 - x < 1 \), that is, \( x > 0 \). (8) In either case \( x > 0 \), which proves the claim.
:::

::: {.solution}
| Sentence | What it does | Rule |
|---|---|---|
| (1) | opens a box with the hypothesis | assumption for \( \rulename{{\to}I} \) |
| (2) | states a fact about real numbers | a school fact, entered as a line |
| (3) | opens the first case box | assumption for \( \rulename{\vee E} \) |
| (4) | \( x \ge 1 \) and \( 1 > 0 \) give \( x > 0 \) | \( \rulename{{\to}E} \), with the fact "\( a \ge b \) and \( b > c \) imply \( a > c \)" |
| (5) | opens the second case box | assumption for \( \rulename{\vee E} \) |
| (6) | computes \( \abs{x - 1} \) | \( \rulename{{\to}E} \) twice, with the facts "\( x < 1 \) implies \( x - 1 < 0 \)" and "\( a < 0 \) implies \( \abs{a} = -a \)" |
| (7) | uses the assumption of (1) | \( \rulename{{=}E} \), putting (6) into (1), then \( \rulename{{\to}E} \) with "\( 1 - x < 1 \) implies \( x > 0 \)" |
| (8) | combines the cases, then closes the outer box | \( \rulename{\vee E} \) on (2), (3)–(4), (5)–(7); then \( \rulename{{\to}I} \) on (1)–(8) |

Sentence (7) uses the assumption made in (1), and it may: that box is still open. The facts of school algebra enter as implications, each used by \( \rulename{{\to}E} \). Sentence (8) closes two boxes, which is normal.

Measured against @def-silent-steps, the proof leaves out nothing that must be written: the split in (2) is on the page, and the disjunction it splits is a school fact (every real number is at least \( 1 \) or below it), so it covers every case; each case box opens with its assumption; and every step it leaves unwritten is of a kind that may be silent, for instance the \( \rulename{\forall E} \) instances of the school facts at the obvious terms, the conclusion \( x > 0 \) of case 1, which is left to the chain \( x \ge 1 > 0 \) of (4), the \( \rulename{\wedge I} \) behind (4), whose conjuncts are displayed, the \( \rulename{{=}E} \) of (7), and the closing of the \( \rulename{{\to}I} \) box, for which "which proves the claim" stands. Labeling also shows where the work is. The case split exists only because \( \abs{\cdot} \) is defined by cases (Chapter 1); the school fact \( -\abs{u} \le u \), used with \( u = x - 1 \), gives \( -1 < x - 1 \) in one step, and a proof written that way would have no \( \rulename{\vee E} \) at all.
:::

The second direction starts from a derivation whose premises are facts about integers.

::: {#exm-write-from-derivation}
[From a derivation to a paragraph]

Let \( n \) be an integer. Write \( E \) for "\( n \) is even", \( O \) for "\( n \) is odd", \( F \) for "\( n + 1 \) is even", and \( G \) for "\( n(n + 1) \) is even". The derivation below uses four facts about integers as premises. Write the paragraph a mathematician would write for it.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \vee O} \by{(every integer is even or odd)}{}
  \hypo {2} {E \to G} \by{(an even factor makes a product even)}{}
  \hypo {3} {O \to F} \by{(odd plus one is even)}{}
  \hypo {4} {F \to G} \by{(an even factor again)}{}
  \open
  \hypo {5} {E}
  \have {6} {G} \ie{2,5}
  \close
  \open
  \hypo {7} {O}
  \have {8} {F} \ie{3,7}
  \have {9} {G} \ie{4,8}
  \close
  \have {10} {G} \oe{1,5-6,7-9}
\end{nd}$
\end{center}
```
:::

::: {.solution}
> Every integer is even or odd, so we consider two cases. If \( n \) is even, then \( n(n + 1) \) has an even factor, and so it is even. If \( n \) is odd, then \( n + 1 \) is even, since an odd number plus one is even; so again \( n(n + 1) \) has an even factor and is even. In either case \( n(n + 1) \) is even.

Compare the two. The paragraph keeps one sentence for each box and each rule that matters: line 1 becomes "we consider two cases", with its reason; the two boxes become the two "if" sentences; line 10 becomes "in either case". It drops the line numbers and the rule names, and it merges the two \( \rulename{{\to}E} \) steps of lines 8 and 9 into one sentence joined by "so". It never skips a box: the reader still sees both cases and sees them combined.

By @def-silent-steps, the closing "in either case …" could be dropped at level 3; the split of line 1, with the reason it covers every integer, could not. The paragraph leaves the premises unproved. Premises 2–4 are one line of algebra each (for instance, \( n = 2k \) gives \( n(n + 1) = 2\bigl(k(n + 1)\bigr) \)), and a careful write-up includes them; premise 1, that every integer is even or odd, is not, and Chapter 7 proves it.
:::

## From the goal to prose

The third example runs all seven steps on a statement not seen before. Sets of reals are used here as Chapter 4 used them, with "\( a \in A \)" a one-place predicate and \( A \subseteq B \) read as "every element of \( A \) is an element of \( B \)"; Chapter 6 develops sets properly.

::: {#exm-subset-bounded-above}
[A subset of a bounded set]

Let \( A \) and \( B \) be sets of real numbers with \( A \subseteq B \). Prove that if \( B \) is bounded above, then \( A \) is bounded above.
:::

::: {.solution}
*Steps 1 and 2: the goal in symbols, unwound.* Over the domain \( \nR \), "\( B \) is bounded above" is \( \exists M \; \forall b \in B \; (b \le M) \) (Section 4.8), and \( A \subseteq B \) is \( \forall x \in A \; (x \in B) \). The statement is an implication, so the derivation below is the inside of a \( \rulename{{\to}I} \) box: its assumption is the first formula (line 2), the hypothesis is the second, and its goal is \( \exists M \; \forall a \in A \; (a \le M) \).

*Step 3: the skeleton.* The goal is an existential, so it is postponed: no witness is in sight yet. The assumption "\( B \) is bounded above" (line 2) is an existential, so its \( \rulename{\exists E} \) box opens at once, with a fresh name \( M_0 \) and the assumption \( \forall b \in B \; (b \le M_0) \); the box's last line is the goal.

*Step 4: filling the box.* Backwards: the goal needs a witness \( M \) and a proof of \( \forall a \in A \; (a \le M) \). The only bound in sight is \( M_0 \), so try it. Then the new goal is a bounded universal: a box "let \( a_0 \in A \)" whose last line is \( a_0 \le M_0 \). That line comes from the bound on \( B \), instantiated at \( a_0 \), which needs \( a_0 \in B \); and \( a_0 \in B \) comes from \( A \subseteq B \) instantiated at \( a_0 \). Forwards, the same lines in the order of the list are the derivation below (with the bounded rules of @prp-bounded-quantifier-rules; each bounded \( \rulename{\forall E} \) abbreviates a \( \rulename{\forall E} \) and a \( \rulename{{\to}E} \), and the bounded \( \rulename{\forall I} \) box a \( \rulename{\forall I} \) box with a \( \rulename{{\to}I} \) box inside).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x \in A \; x \in B}
  \hypo {2} {\exists M \; \forall b \in B \; b \le M}
  \open[M_0]
  \hypo {3} {\forall b \in B \; b \le M_0}
  \open[a_0]
  \hypo {4} {a_0 \in A}
  \have {5} {a_0 \in B} \Ae{1,4}
  \have {6} {a_0 \le M_0} \Ae{3,5}
  \close
  \have {7} {\forall a \in A \; a \le M_0} \Ai{4-6}
  \have {8} {\exists M \; \forall a \in A \; a \le M} \Ei{7}
  \close
  \have {9} {\exists M \; \forall a \in A \; a \le M} \Ee{2,3-8}
\end{nd}$
\end{center}
```

The side conditions hold: \( a_0 \) appears in neither line 1 nor line 2, not in line 7 and not in the open assumption on line 3; \( M_0 \) appears in none of lines 1, 2 and 9.

*Step 5: the constant.* The witness for the goal is the bound \( M_0 \). The search could choose it only once the \( \rulename{\exists E} \) box supplied \( M_0 \), and confirm it only at line 6; the page writes it first, in the sentence that chooses it. It depends on \( B \) only: its box is opened before the box of \( a_0 \), so it cannot depend on \( a_0 \), and it must not, because a single bound has to serve every element of \( A \).

*Step 6: level 3.*

> Suppose \( B \) is bounded above, and choose an upper bound \( M \) of \( B \) (depending on \( B \) only). Let \( a \in A \). Since \( A \subseteq B \), we have \( a \in B \), and so \( a \le M \). Hence \( M \) is an upper bound of \( A \), and \( A \) is bounded above.

The two instances of \( \rulename{\forall E} \) (lines 5 and 6) are at the obvious term \( a \), and each appears only as the citation that licenses it ("since \( A \subseteq B \)", "so", which cites the choice of \( M \)). The closing of the \( \rulename{\forall I} \) box, "since \( a \) was arbitrary", is silent. Two steps that are never silent are on the page: the \( \rulename{\exists E} \) with its fresh name ("choose an upper bound \( M \)"), and the \( \rulename{\exists I} \) with its witness and dependence ("\( M \) is an upper bound of \( A \)"; "depending on \( B \) only"). "Suppose \( B \) is bounded above" opens the \( \rulename{{\to}I} \) box; its closing is silent.

*Step 7: reread.* The order of the first two sentences matters. With "let \( a \in A \)" first and \( M \) chosen inside, the \( \rulename{\exists I} \) would fall inside the box of \( a_0 \), giving only \( \forall a \in A \; \exists M \; (a \le M) \), which says nothing.
:::

The example used \( A \subseteq B \) once, at line 5, and "\( B \) is bounded above" once, at line 9, by \( \rulename{\exists E} \), whose box assumption is used at line 6. The two warnings below concern steps 4 and 5.

::: {.warning}
**The search is not the proof.** A page that reads "we want \( x^2 < 4 \); this holds if \( x < 2 \); so let \( x < 2 \)" has copied the search, and each "holds if" points backwards. A backward step can be false, and the page hides it: "\( x < 2 \) implies \( x^2 < 4 \)" fails at \( x = -3 \). In scratch work every backward step must be checked as an implication pointing forwards; on the page only the forward chain appears, each line citing lines above it.
:::

::: {.warning}
**A constant without its dependencies is a claim nobody can check.** In a proof that \( x^2 \) is uniformly continuous on \( \nR \), the sentence "let \( \delta \coloneqq \min\{1, \varepsilon/(2\abs{x} + 1)\} \)" looks innocent. Asked "what does \( \delta \) depend on?", the formula answers: on \( \varepsilon \) **and on \( x \)**, so the \( \delta \) was chosen inside the box of \( x \), and the proof shows only continuity at every point. Uniform continuity is false here (@exm-square-not-uniform). Writing "(depending on \( \varepsilon \) only)" after the constant is what lets a reader catch the error.
:::

## Exercises

### A. Check your understanding

::: {#exr-writing-proofs-a1}
[A1]

Here is a proof.

> **Claim.** For real numbers \( x \) and \( y \), if \( x + y > 2 \), then \( x > 1 \) or \( y > 1 \).
>
> (1) Assume \( x + y > 2 \). (2) Suppose, for a contradiction, that it is not the case that \( x > 1 \) or \( y > 1 \). (3) Then \( x > 1 \) fails and \( y > 1 \) fails. (4) So \( x \le 1 \) and \( y \le 1 \). (5) Adding, \( x + y \le 2 \). (6) This contradicts \( x + y > 2 \). (7) Hence \( x > 1 \) or \( y > 1 \), which proves the claim.

::: {.enumerate options="label=(\alph*)"}
1. Label each sentence with the rule it uses, as in @exm-annotate-abs.
2. Which sentence closes an \( \rulename{RAA} \) box, and which uses one of De Morgan's laws (@prp-de-morgan)? Which law?
3. Everything inside the box of (2) follows from (2) alone, until the clash in (6). Which face of "by contradiction" (Section 5.1) does the proof wear, and which face is it really? Write the first sentence of the rewritten proof.
4. Sentence (7) closes two boxes. Which of the two closings may be silent at level 3, by @def-silent-steps?
:::
:::

::: {.solution}
*(a)*

| Sentence | Rule |
|---|---|
| (1) | assumption, opening the \( \rulename{{\to}I} \) box |
| (2) | assumption \( \neg(x > 1 \vee y > 1) \), opening an \( \rulename{RAA} \) box |
| (3) | @prp-de-morgan (a), \( \neg(P \vee Q) \vdash \neg P \wedge \neg Q \), applied to (2) |
| (4) | \( \rulename{\wedge E} \) on (3), twice; \( \rulename{{\to}E} \) with the order fact "\( \neg(a > 1) \) implies \( a \le 1 \)", twice; then \( \rulename{\wedge I} \) |
| (5) | \( \rulename{\wedge E} \) on (4), then \( \rulename{{\to}E} \) with "\( a \le 1 \) and \( b \le 1 \) imply \( a + b \le 2 \)" |
| (6) | \( \rulename{{\to}E} \) with the order fact "\( a \le 2 \) implies \( \neg(a > 2) \)" on (5), then \( \rulename{\neg E} \) on (1) and the result |
| (7) | \( \rulename{RAA} \) on the box (2)–(6); then \( \rulename{{\to}I} \) on (1)–(7) |

*(b)* Sentence (7) closes the \( \rulename{RAA} \) box: the box opened with the negation of the goal \( x > 1 \vee y > 1 \) and closes with the goal itself. Sentence (3) uses De Morgan's law (a), a direction derived without \( \rulename{RAA} \).

*(c)* It wears face (iii), genuine \( \rulename{RAA} \), but it is a contrapositive in costume, as in @exm-costume-contrapositive: the hypothesis (1) is used only at the clash, and everything else derives \( x + y \le 2 \) from \( x \le 1 \) and \( y \le 1 \). The rewrite opens: "We prove the contrapositive: if \( x \le 1 \) and \( y \le 1 \), then \( x + y \le 2 \)." The rewrite is clearer, but it does not remove the classical step: passing from the contrapositive back to the claim is @prp-contrapositive-converse, which uses \( \rulename{RAA} \).

*(d)* The closing of the \( \rulename{{\to}I} \) box ("so if \( x + y > 2 \), then …") may be silent. The conclusion of the \( \rulename{RAA} \) box, "hence \( x > 1 \) or \( y > 1 \)", may not.
:::

### B. Practice

::: {#exr-writing-proofs-b1}
[B1: From skeleton to prose]

Each part gives a statement and a level-1 skeleton of its proof. Write the proof at level 3, keeping every step that @def-silent-steps says is never silent.

::: {.enumerate options="label=(\alph*)"}
1. For every integer \( n \), if \( n \) is odd, then \( 3n + 5 \) is even. (Domain \( \nZ \).)

    ```{=latex}
    \begin{center}
    $\begin{nd}
      \open[n_0]
      \open
      \hypo {1} {\exists k \, (n_0 = 2 \cdot k + 1)}
      \open[k_0]
      \hypo {2} {n_0 = 2 \cdot k_0 + 1}
      \have {3} {3 \cdot n_0 + 5 = 2 \cdot (3 \cdot k_0 + 4)} \by{arith}{2}
      \have {4} {\exists k \, (3 \cdot n_0 + 5 = 2 \cdot k)} \Ei{3}
      \close
      \have {5} {\exists k \, (3 \cdot n_0 + 5 = 2 \cdot k)} \Ee{1,2-4}
      \close
      \have {6} {\exists k \, (n_0 = 2 \cdot k + 1) \to \exists k \, (3 \cdot n_0 + 5 = 2 \cdot k)} \ii{1-5}
      \close
      \have {7} {\forall n \, (\exists k \, (n = 2 \cdot k + 1) \to \exists k \, (3 \cdot n + 5 = 2 \cdot k))} \Ai{1-6}
    \end{nd}$
    \end{center}
    ```

2. No real number \( x \) satisfies \( x^2 + 1 = 2x - 1 \). (Domain \( \nR \).)

    ```{=latex}
    \begin{center}
    $\begin{nd}
      \open
      \hypo {1} {\exists x \, (x^2 + 1 = 2 \cdot x - 1)}
      \open[x_0]
      \hypo {2} {x_0^2 + 1 = 2 \cdot x_0 - 1}
      \have {3} {(x_0 - 1)^2 + 1 = 0} \by{arith}{2}
      \have {4} {(x_0 - 1)^2 \ge 0} \by{arith}{}
      \have {5} {1 \le 0} \by{arith}{3,4}
      \have {6} {\neg (1 \le 0)} \by{arith}{}
      \have {7} {\bot} \ne{5,6}
      \close
      \have {8} {\bot} \Ee{1,2-7}
      \close
      \have {9} {\neg \exists x \, (x^2 + 1 = 2 \cdot x - 1)} \ni{1-8}
    \end{nd}$
    \end{center}
    ```

3. For a real number \( x \): \( x^3 = x \) if and only if \( x = -1 \), \( x = 0 \) or \( x = 1 \). (Here \( x \) is fixed; "or" chains group to the right.)

    ```{=latex}
    \begin{center}
    $\begin{nd}
      \open
      \hypo {1} {x^3 = x}
      \have {2} {(x + 1) \cdot (x \cdot (x - 1)) = 0} \by{arith}{1}
      \have {3} {x = -1 \vee (x = 0 \vee x = 1)} \by{product zero, arith}{2}
      \close
      \open
      \hypo {4} {x = -1 \vee (x = 0 \vee x = 1)}
      \open
      \hypo {5} {x = -1}
      \have {6} {x^3 = x} \by{arith}{5}
      \close
      \open
      \hypo {7} {x = 0 \vee x = 1}
      \open
      \hypo {8} {x = 0}
      \have {9} {x^3 = x} \by{arith}{8}
      \close
      \open
      \hypo {10} {x = 1}
      \have {11} {x^3 = x} \by{arith}{10}
      \close
      \have {12} {x^3 = x} \oe{7,8-9,10-11}
      \close
      \have {13} {x^3 = x} \oe{4,5-6,7-12}
      \close
      \have {14} {x^3 = x \leftrightarrow (x = -1 \vee (x = 0 \vee x = 1))} \bi{1-3,4-13}
    \end{nd}$
    \end{center}
    ```

:::

*Hint: line 3 of (c) uses the school fact that a product of real numbers is zero only if one of its factors is zero.*
:::

::: {.solution}
*(a)* Let \( n \) be an integer, and suppose \( n \) is odd. Choose an integer \( k \) with \( n = 2k + 1 \). Then
\[
3n + 5 = 6k + 3 + 5 = 2(3k + 4),
\]
and \( 3k + 4 \) is an integer, so \( 3n + 5 \) is even.

"Choose an integer \( k \)" is the \( \rulename{\exists E} \) box, with a fresh name; the witness \( 3k + 4 \) of line 4 is on the page, and it depends on \( k \), hence on \( n \). Lines 5, 6 and 7 close boxes and are silent.

*(b)* Suppose, to the contrary, that some real \( x \) satisfies \( x^2 + 1 = 2x - 1 \), and fix such an \( x \). Rearranging, \( x^2 - 2x + 2 = 0 \), that is, \( (x - 1)^2 + 1 = 0 \). But \( (x - 1)^2 \ge 0 \), since a square is non-negative, so \( 1 \le 0 \), which is false. Hence no real \( x \) satisfies the equation.

"Suppose, to the contrary" opens the \( \rulename{\neg I} \) box of line 1 (the goal is a negation, so no classical rule is used), and "fix such an \( x \)" the \( \rulename{\exists E} \) box. The clash of lines 5–7 is named, and the conclusion of the \( \rulename{\neg I} \) box is written; line 8 is silent.

*(c)* Let \( x \) be real.

\( (\Rightarrow) \) Suppose \( x^3 = x \). Then \( (x + 1)\,x\,(x - 1) = x^3 - x = 0 \). A product of real numbers is zero only if a factor is zero, so \( x + 1 = 0 \), \( x = 0 \) or \( x - 1 = 0 \); that is, \( x = -1 \), \( x = 0 \) or \( x = 1 \).

\( (\Leftarrow) \) Suppose \( x = -1 \), \( x = 0 \) or \( x = 1 \). In the three cases, \( x^3 = -1 = x \), \( x^3 = 0 = x \) and \( x^3 = 1 = x \).

This proves the equivalence.

Both directions are written, and the citation in line 3 is visible. The two splits of \( (\Leftarrow) \) are merged into "in the three cases"; the disjunction split is the hypothesis itself, and the closing lines 12 and 13 are silent.
:::

::: {#exr-writing-proofs-b2}
[B2: Put the proof in order]

Let \( (a_n) \) and \( (b_n) \) be sequences of real numbers with \( a_n \to L \) and \( b_n \to M \), where "\( a_n \to L \)" is the pattern of Section 4.8: for every \( \varepsilon > 0 \) there is \( N \in \nN \) such that \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N \). Eight of the ten sentences below, in a suitable order, form a level-3 proof that \( a_n + b_n \to L + M \); two are distractors. Write down an order for the eight, say which other orders are also admissible, and say why each distractor is wrong.

::: {.enumerate options="label=(\roman*)"}
1. Let \( n \in \nN \) with \( n \ge N \).
2. Since \( b_n \to M \) and \( \varepsilon/2 > 0 \), choose \( N_2 \in \nN \) (depending on \( \varepsilon \)) such that \( \abs{b_n - M} < \varepsilon/2 \) for every \( n \ge N_2 \).
3. Let \( N \coloneqq \max\{N_1, N_2\} \), where \( N_1 \) and \( N_2 \) serve every \( \varepsilon \) at once.
4. Then \( n \ge N_1 \) and \( n \ge N_2 \).
5. Let \( \varepsilon > 0 \).
6. Since \( n \ge N \) and \( \varepsilon > 0 \) were arbitrary, \( a_n + b_n \to L + M \).
7. Choose \( N_1 \in \nN \) such that \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N_1 \).
8. Let \( N \coloneqq \max\{N_1, N_2\} \).
9. So \( \abs{(a_n + b_n) - (L + M)} \le \abs{a_n - L} + \abs{b_n - M} < \varepsilon/2 + \varepsilon/2 = \varepsilon \).
10. Since \( a_n \to L \) and \( \varepsilon/2 > 0 \), choose \( N_1 \in \nN \) (depending on \( \varepsilon \)) such that \( \abs{a_n - L} < \varepsilon/2 \) for every \( n \ge N_1 \).
:::
:::

::: {.solution}
An admissible order: (v), (x), (ii), (viii), (i), (iv), (ix), (vi).

The only other admissible order swaps (x) and (ii), which use only \( \varepsilon \) and one hypothesis each. Nothing else moves: (viii) uses \( N_1 \) and \( N_2 \); (i) uses \( N \); (iv) uses \( n \ge N \) and the definition of \( N \); (ix) uses (iv), (x) and (ii) at this \( n \), and the triangle inequality (@exm-triangle-inequality-cases); (vi) closes the boxes of \( n \) and \( \varepsilon \), with the \( \rulename{\exists I} \) of the witness \( N \) inside "\( a_n + b_n \to L + M \)". The maximum exists because there are finitely many numbers.

Distractor (iii) claims that \( N_1 \) and \( N_2 \) serve every \( \varepsilon \) at once. They were chosen from \( \forall \varepsilon \, \exists N \), inside the box of \( \varepsilon \), so they depend on \( \varepsilon \) and serve only the \( \varepsilon \) they were chosen for; a uniform \( N \) would need \( \exists N \, \forall \varepsilon \), which the hypothesis does not give. This is the error that Section 5.6 catalogues as (N2). For \( a_n = 1/(n + 1) \), \( L = 0 \), no single \( N_1 \) serves every \( \varepsilon > 0 \): at \( \varepsilon = 1/(N_1 + 2) \) the term \( a_{N_1} = 1/(N_1 + 1) \) is too far from \( 0 \).

Distractor (vii) applies the hypothesis at \( \varepsilon \) instead of \( \varepsilon/2 \). It is a legal step, but with it in place of (x), the bound in (ix) becomes \( \abs{(a_n + b_n) - (L + M)} < \varepsilon + \varepsilon/2 \), not \( < \varepsilon \), so (ix) would no longer follow. It is an \( \varepsilon \) of the wrong kind for the goal.
:::

::: {#exr-writing-proofs-b3}
[B3: The last step]

Here is a level-1 skeleton for the statement "for real numbers \( x \) and \( y \), if \( x \) is rational and \( y \) is irrational, then \( x + y \) is irrational", with \( x \) and \( y \) fixed:

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {x \in \nQ \wedge \neg (y \in \nQ)}
  \have {2} {x \in \nQ} \ae{1}
  \have {3} {\neg (y \in \nQ)} \ae{1}
  \open
  \hypo {4} {x + y \in \nQ}
  \have {5} {(x + y) - x \in \nQ} \by{difference of rationals}{4,2}
  \have {6} {y \in \nQ} \by{arith}{5}
  \have {7} {\bot} \ne{6,3}
  \close
  \have {8} {\neg (x + y \in \nQ)} \ni{4-7}
  \close
  \have {9} {x \in \nQ \wedge \neg (y \in \nQ) \to \neg (x + y \in \nQ)} \ii{1-8}
\end{nd}$
\end{center}
```

and its level-3 prose, with the closing sentence of the \( \rulename{\neg I} \) box left blank:

> Let \( x \) be rational and \( y \) irrational. Suppose \( x + y \) is rational. Then \( y = (x + y) - x \) is a difference of two rational numbers, so \( y \) is rational. This contradicts the irrationality of \( y \). \( \underline{\qquad\qquad} \)

*Name the move, then complete it.*
:::

::: {.solution}
*The move* is skeleton first: the blank is line 8, the line written after the \( \rulename{\neg I} \) box of lines 4–7 closes, a line the skeleton fixes before any arithmetic. That box assumed "\( x + y \) is rational" and reached \( \bot \) at line 7, so line 8 concludes its negation. It is the first face of "by contradiction" (Section 5.1), proof of a negative statement, and uses no classical rule: "irrational" means "not rational", so the goal of the outer box, line 8, is a negation, and the inner box is opened on \( x + y \in \nQ \) with goal \( \bot \).

*Completion.* "Hence \( x + y \) is not rational, that is, \( x + y \) is irrational."

The conclusion of a \( \rulename{\neg I} \) box is never silent (@def-silent-steps), so this sentence must be written even though the reader can guess it. Line 9, the closing of the \( \rulename{{\to}I} \) box, may stay silent. The sentence before the blank, "this contradicts the irrationality of \( y \)", is line 7, the clash of \( \rulename{\neg E} \), which names both lines it cites.
:::

### C. Going deeper

::: {#exr-writing-proofs-c1}
[C1: A constant found backwards]

Let \( f(x) = 2x + 3 \) and let \( a \) be a fixed real number. Prove that for every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that \( \abs{f(x) - f(a)} < \varepsilon \) for every real \( x \) with \( \abs{x - a} < \delta \). Write your answer as an Idea, which finds \( \delta \) backwards, followed by a Proof, which runs forwards. Say what \( \delta \) depends on.
:::

::: {.solution}
[Hint 1]

Compute \( \abs{f(x) - f(a)} \) in terms of \( \abs{x - a} \) before choosing anything.
:::

::: {.solution}
[Hint 2]

The Proof begins: "Let \( \varepsilon > 0 \), and let \( \delta \coloneqq \) …".
:::

::: {.solution}
*Idea.* We want \( \abs{f(x) - f(a)} < \varepsilon \). Compute: \( f(x) - f(a) = (2x + 3) - (2a + 3) = 2(x - a) \), so \( \abs{f(x) - f(a)} = 2\abs{x - a} \). This is below \( \varepsilon \) exactly when \( \abs{x - a} < \varepsilon/2 \). So \( \delta = \varepsilon/2 \) should work, and it does not involve \( x \) or \( a \).

*Proof.* Let \( \varepsilon > 0 \), and let \( \delta \coloneqq \varepsilon/2 \), which is positive and depends on \( \varepsilon \) only. Let \( x \) be a real number with \( \abs{x - a} < \delta \). Then
\[
\abs{f(x) - f(a)} = \abs{2(x - a)} = 2\abs{x - a} < 2\delta = \varepsilon .
\]
Since \( x \) was arbitrary, \( \delta \) works for \( \varepsilon \); since \( \varepsilon > 0 \) was arbitrary, this proves the claim.

The Idea reads the computation from the goal back to \( \abs{x - a} \); the Proof places \( \delta \) right after \( \varepsilon \), before any \( x \) appears, and justifies it by the final display. Because \( \delta \) does not depend on \( a \) either, the same proof shows that one \( \delta \) serves every point: \( f \) is uniformly continuous on \( \nR \), in the sense of Section 4.10.

**Marking scheme.** (10 points)
- 2: an Idea that computes \( \abs{f(x) - f(a)} = 2\abs{x - a} \) and reads off \( \delta \) from the goal.
- 2: the Proof opens with \( \varepsilon > 0 \) arbitrary and introduces \( \delta \) before any \( x \), with \( \delta > 0 \) checked.
- 2: says what \( \delta \) depends on (\( \varepsilon \) only, or \( \varepsilon \) and \( a \) if the choice involves \( a \)).
- 3: for arbitrary \( x \) with \( \abs{x - a} < \delta \), the forward chain to \( \abs{f(x) - f(a)} < \varepsilon \), each step justified.
- 1: a closing sentence with the quantifiers in the order \( \varepsilon \), \( \delta \), \( x \).
Any \( \delta \) with \( 0 < \delta \le \varepsilon/2 \) earns full marks. Fatal errors (0 for the step): \( \delta \) depending on \( x \); a Proof that runs backwards ("this holds if …").
:::

::: {#exr-writing-proofs-c2}
[C2: Rewrite it properly]

A sequence \( (a_n) \) is **bounded** if there is \( M \in \nR \) with \( \abs{a_n} \le M \) for every \( n \in \nN \) (Section 4.6). The following proof that a sequence \( (a_n) \) with \( a_n \to L \) is bounded is correct in substance but badly written.

> We want some \( M \) with \( \abs{a_n} \le M \). For big \( n \), \( a_n \) is near \( L \), so \( \abs{a_n} \) is less than \( \abs{L} + 1 \) if we use \( 1 \) for \( \varepsilon \). The small \( n \) are only finitely many, so take the biggest. So \( M \) is the max of all of them and it works.

::: {.enumerate options="label=(\alph*)"}
1. Name three faults of the text, each by the convention it breaks (this section) or the step that is not written.
2. Rewrite the proof at level 3.
:::
:::

::: {.solution}
[Hint 1]

Which objects does the text use without introducing them, and what does each depend on?
:::

::: {.solution}
[Hint 2]

The rewrite begins: "Apply the definition of \( a_n \to L \) with \( \varepsilon = 1 \), and choose \( N \in \nN \) such that …".
:::

::: {.solution}
*(a)* (i) It writes the search: "we want some \( M \)" and "if we use \( 1 \) for \( \varepsilon \)" describe what is being looked for, not lines that follow. (ii) It uses objects without introducing them: "big \( n \)" hides an \( N \), obtained from the hypothesis at \( \varepsilon = 1 \) by \( \rulename{\forall E} \) and \( \rulename{\exists E} \), which is never named; "the biggest" does not say of which numbers. (iii) It never says what \( M \) is or what it depends on: \( M \) is built from the finitely many terms before \( N \), so it depends on \( N \). (Also acceptable: the split into small and big \( n \) has no stated reason; the last sentence does not say what was shown.)

*(b)* Apply the definition of \( a_n \to L \) with \( \varepsilon = 1 \), and choose \( N \in \nN \) such that \( \abs{a_n - L} < 1 \) for every \( n \ge N \). Let
\[
M \coloneqq \max\{ \abs{a_0}, \abs{a_1}, \dots, \abs{a_{N-1}}, \abs{L} + 1 \},
\]
the largest of finitely many numbers, so it exists; it depends on \( N \) (when \( N = 0 \) the list is just \( \abs{L} + 1 \)). Let \( n \in \nN \). Either \( n < N \) or \( n \ge N \), since every natural number is one or the other. If \( n < N \), then \( \abs{a_n} \) is in the list, so \( \abs{a_n} \le M \). If \( n \ge N \), then by the triangle inequality (@exm-triangle-inequality-cases)
\[
\abs{a_n} = \abs{(a_n - L) + L} \le \abs{a_n - L} + \abs{L} < 1 + \abs{L} \le M .
\]
In either case \( \abs{a_n} \le M \). Hence \( (a_n) \) is bounded.

The \( \rulename{\forall E} \) instance \( \varepsilon = 1 \) is named, because it is not the obvious one; the witness \( M \) of the final \( \rulename{\exists I} \) is defined before it is used, with its dependence; the split on \( n < N \) or \( n \ge N \) carries its reason (every natural number is one or the other).

**Marking scheme.** (10 points)
- 3: (a) three genuine faults, each tied to a convention or an unwritten step (1 each).
- 2: (b) applies the hypothesis at a named positive \( \varepsilon \) and chooses \( N \) from it.
- 2: defines \( M \) before using it, with its dependence on \( N \), bounding the early terms and \( \abs{L} + \varepsilon \) (a maximum or a sum).
- 2: the two cases \( n < N \) and \( n \ge N \), the second by the triangle inequality (cited) or an equivalent estimate from \( \abs{a_n - L} < \varepsilon \), such as \( L - \varepsilon < a_n < L + \varepsilon \) and a split on the sign of \( a_n \).
- 1: ends with what was shown.
Fatal errors (0 for the step): \( M \) chosen before \( N \) or as a maximum or sum of infinitely many numbers; the early terms omitted.
:::

<!-- dependency ledger
exm-subset-bounded-above (claim): (the procedure, steps 3-4) the search for a derivation is goal-directed and opening the goal's box loses nothing | Section 2.6, "The goal-directed steps lose nothing" (unlabeled)
exm-subset-bounded-above (claim): (the procedure, step 5) a constant may depend only on the names of the boxes open where it is chosen, and depends on the names in the line it comes from | Section 4.10, "Reading dependence off the boxes" (unlabeled)
exm-subset-bounded-above (claim): (the procedure, step 1) a letter not introduced in a theorem is read with "for every" | Section 4.1, "Hidden universal quantifiers" (unlabeled)
exm-annotate-abs (solution): every real number is >= 1 or < 1; a >= b > c gives a > c; x < 1 gives x - 1 < 0; |a| = -a for a < 0; 1 - x < 1 gives x > 0; -|u| <= u | school algebra of order and absolute value (Chapter 1's allowed facts; ch11 prose pointer, nothing rests on it); checked by verify/ch05/exm-annotate-abs.py
exm-write-from-derivation (example): every integer is even or odd; an even factor makes a product even; odd plus one is even | entered as premises of the derivation (school arithmetic; even/odd: ch07 (promised; STATUS row 95)); checked by verify/ch05/exm-write-from-derivation.py
exm-subset-bounded-above (solution): "bounded above" is exists M forall b in B (b <= M); A subseteq B is forall x in A (x in B) | Section 4.8 (exm-translate-limit (b) pattern) and Section 4.1's gloss of subset (prose); sets developed in Ch 6 (prose pointer)
exm-subset-bounded-above (solution): the derivation with the bounded rules and its side conditions | prp-bounded-quantifier-rules (cited), def-rules-existential (Section 4.6); checked by tools/check_fitch.py
exm-subset-bounded-above (claim): (the warning "The search is not the proof") x = -3 has x < 2 and x^2 = 9 >= 4 | arithmetic; checked by verify/ch05/exm-subset-bounded-above.py (warning values)
exm-subset-bounded-above (claim): (the warning "A constant without its dependencies") delta = min(1, eps/(2|x| + 1)) proves only continuity; uniform continuity of x^2 on R is false | exm-square-not-uniform (cited)
exr-writing-proofs-a1 (solution): not(a > 1) implies a <= 1; a <= 2 implies not(a > 2); a <= 1 and b <= 1 give a + b <= 2 | school order facts (trichotomy, Ch 11 axioms; prose); checked by verify/ch05/exr-writing-proofs-a1.py
exr-writing-proofs-a1 (solution): the three faces of "by contradiction" and the costume | Section 5.1 (prose pointer)
exr-writing-proofs-b1 (solution): 3(2k + 1) + 5 = 2(3k + 4); x^2 + 1 = 2x - 1 iff (x - 1)^2 + 1 = 0; squares are non-negative; x^3 - x = (x + 1)x(x - 1); a product is zero only if a factor is zero; (-1)^3 = -1 | school algebra (exm-product-zero gives only the converse direction of the product fact; the direction used is a school fact named in the item's hint); checked by verify/ch05/exr-writing-proofs-b1.py
exr-writing-proofs-b1 (solution): integers closed under + and * (3k + 4 is an integer) | ch07 (promised): prp-integers-closed (STATUS row 95)
exr-writing-proofs-b2 (solution): triangle inequality | exm-triangle-inequality-cases (cited)
exr-writing-proofs-b2 (solution): the maximum of two natural numbers exists, and n >= max{N1, N2} gives n >= N1 and n >= N2; eps/2 + eps/2 = eps; for a_n = 1/(n + 1) no N1 serves eps = 1/(N1 + 2) | school arithmetic; finite max: ch07 (promised; STATUS row 95); checked by verify/ch05/exr-writing-proofs-b2.py
exr-writing-proofs-b2 (solution): the error of distractor (iii) is (N2) of Section 5.6 | prose pointer; nothing rests on it
exr-writing-proofs-b3 (example): a difference of two rational numbers is rational | school algebra, stated in the skeleton as a cited fact
exr-writing-proofs-c1 (solution): (2x + 3) - (2a + 3) = 2(x - a); |2u| = 2|u| | school algebra; exm-abs-product-cases (Ch 1) for |2u| = |2||u|; checked by verify/ch05/exr-writing-proofs-c1.py
exr-writing-proofs-c2 (solution): a maximum of finitely many reals exists; every natural number is < N or >= N; |a_n| <= |a_n - L| + |L| | finite max and the order on N: ch07 (promised; STATUS row 95); exm-triangle-inequality-cases (cited); checked by verify/ch05/exr-writing-proofs-c2.py
-->
