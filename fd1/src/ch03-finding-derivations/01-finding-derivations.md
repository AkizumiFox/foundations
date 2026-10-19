# How to Find a Derivation

We now have every rule for the connectives. Checking a derivation is mechanical, as @def-derivation makes it: for each line, which rule, which lines, and are they available. Finding one is not, since an assumption may be any statement at all. Yet every Idea in Chapters 1 and 2 found its derivation with the same handful of moves. This section introduces no new rule. It collects those moves into one method, puts them in order, says why the order is right, and then watches the method work: on five searches that succeed, one that fails, and one mathematical goal. It ends with every rule in one place.

## The moves so far

Each section since Section 1.2 has added a move, either to the list read off the **goal** (goal-directed: which introduction rule builds the goal's main connective?) or to the list read off the **premises** (premise-directed: which elimination rule uses an available line's main connective?). Here they are together, with the section where each first appeared.

| The situation | The move | First met |
|---|---|---|
| goal \( \varphi \wedge \psi \) | two subgoals, \( \varphi \) and \( \psi \), joined by \( \rulename{\wedge I} \) | Section 1.2 |
| resource \( \varphi \wedge \psi \) | take it apart by \( \rulename{\wedge E} \) | Section 1.2 |
| resource \( \varphi \to \psi \) | fire it on \( \varphi \) by \( \rulename{{\to}E} \); if \( \varphi \) is missing, make it a subgoal | Section 1.3 |
| goal \( \varphi \to \psi \) | a box opened with \( \varphi \), with the new goal \( \psi \) | Section 1.4 |
| goal \( \varphi \vee \psi \) | postpone; choose a side only when it is in hand | Section 1.5 |
| resource \( \varphi \vee \psi \) | two cases, each ending in the current goal | Section 1.6 |
| goal \( \bot \) | find a clash, or manufacture one; an impossible case closes itself by \( \rulename{\bot E} \) | Section 2.1 |
| resource \( \neg\varphi \) | clash it by \( \rulename{\neg E} \): make \( \varphi \) a subgoal | Section 2.1 |
| goal \( \neg\varphi \) | a box opened with \( \varphi \), with the new goal \( \bot \) | Section 2.2 |
| a pattern with a name | use the derived rule as one line (\( \rulename{MT} \), \( \rulename{DS} \), …) | Section 2.3 |
| goal \( \varphi \leftrightarrow \psi \) | two boxes, one for each direction | Section 2.4 |
| resource \( \varphi \leftrightarrow \psi \) | cross it by \( \rulename{{\leftrightarrow}E} \) once one side is on a line | Section 2.4 |
| stuck | assume the negation of the goal (\( \rulename{RAA} \)), or split on \( \chi \vee \neg\chi \) (\( \rulename{LEM} \)) | Section 2.5 |

Thirteen moves is a lot to hold in mind at a blank page. The method below turns them into an order of attack. Every assumption a search opens says, in its justification column, which move opened it: "asm, for \( \rulename{{\to}I} \)" is the goal step for \( \to \), "asm, for \( \rulename{\vee E} \)" the resource step for \( \vee \), "asm, for \( \rulename{RAA} \)" step 5. To state it we need a name for a derivation that is only half written.

## Partial derivations

Here is the first snapshot of the first search below, for \( P \to \neg Q \vdash \neg(P \wedge Q) \wedge (Q \to \neg P) \), drawn as in every section since Section 1.2:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \to \neg Q}
  \have {} {\vdots}
  \have {7} {\neg (P \wedge Q)}
  \have {} {\vdots}
  \have {13} {Q \to \neg P}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
\end{nd}$
\end{center}
```

Each row \( \vdots \) is a **gap**. The written line just below a gap, here line 7 or line 13, is the gap's **current goal**; it has no justification yet. The lines available at that goal, here the premise for the first gap and the premise and line 7 for the second, are the gap's **resources**. The definition says the same thing exactly.

::: {#def-partial-derivation}
[Partial Derivation]

A **partial derivation** is a list of lines laid out as a derivation (@def-derivation), except that some stretches of lines are still missing. Each missing stretch is a **gap**, drawn as a row \( \vdots \). The line just below a gap is its **current goal**; it is already written, but it has no justification yet, since the lines of the gap are to supply one. The lines available at the current goal, in the sense of @def-derivation, are the gap's **resources**.
:::

In words: every line that has been written is a premise, an assumption, a current goal, or a line justified by a rule from lines and boxes available to it; the boxes are nested and closed as in any derivation; only the gaps are missing. A search starts with a single gap, below the premises and above the conclusion, and each step replaces a gap by lines, boxes, and smaller gaps. It ends when no gap is left, and then the partial derivation is a derivation.

The snapshots in the worked searches below are all partial derivations; a line carries the number it will have in the finished derivation, and a line whose place is not yet fixed carries no number. On paper you would number the lines at the end.

::: {.second-reading title="A snapshot that is not a partial derivation"}
**Nonexample.** Take a snapshot and leave one of its boxes open at the bottom, so that the conclusion sits inside the box. That is not a partial derivation, even though every line is correct so far: @def-derivation asks that every box close and that the last line lie outside every box, and a gap cannot repair that, since filling a gap adds lines only above its current goal.
:::

## The method

*Work from both ends: let the goal choose the boxes, let the premises choose the eliminations, and meet in the middle.*

::: {.algorithm}
**Searching for a derivation of \( \Gamma \vdash \varphi \).**

1. **Set up.** Write the premises \( \Gamma \) at the top and \( \varphi \) at the bottom, with one gap between.
2. **Goal-directed step.** Take the main connective of the current goal (@def-main-connective) and set up its introduction rule:
   - \( \psi \wedge \chi \): two gaps, with goals \( \psi \) and \( \chi \) (Section 1.2);
   - \( \psi \to \chi \): a box opened with \( \psi \); inside it, the new goal is \( \chi \) (Section 1.4);
   - \( \neg\psi \): a box opened with \( \psi \); inside it, the new goal is \( \bot \) (Section 2.2);
   - \( \psi \leftrightarrow \chi \): two boxes, one from \( \psi \) to \( \chi \) and one from \( \chi \) to \( \psi \) (Section 2.4);
   - \( \psi \vee \chi \): **postpone**; do not choose a side yet (Section 1.5).

   Repeat while the current goal is a \( \wedge \), \( \to \), \( \neg \), or \( \leftrightarrow \).
3. **Premise-directed step.** Take the main connective of a resource and apply its elimination rule: \( \rulename{\wedge E} \) freely (Section 1.2); \( \rulename{{\to}E} \) and \( \rulename{{\leftrightarrow}E} \) when the other statement they need is a resource, or can be made a new goal (Sections 1.3 and 2.4); \( \rulename{\vee E} \) by opening two boxes, one per disjunct, **each ending in the current goal** (Section 1.6). A derived rule may do the work of several lines (Section 2.3): a resource \( \psi \to \chi \) with \( \neg\chi \) available gives \( \neg\psi \) by \( \rulename{MT} \); a resource \( \psi \vee \chi \) with \( \neg\psi \) available gives \( \chi \) by \( \rulename{DS} \).
4. **Clash.** If the current goal is \( \bot \), look for a pair \( \chi \), \( \neg\chi \) among the resources, or make \( \chi \) the new goal for some resource \( \neg\chi \) and manufacture it, starting again at step 2 for that goal. Whatever the current goal, if the resources clash, or a clash with a resource \( \neg\chi \) can be manufactured, write \( \bot \) and then the goal by \( \rulename{\bot E} \): an impossible case closes itself (Section 2.1). When the clash needs a disjunction whose negation is a resource, either side may be chosen to build it: once the disjunction is written, \( \bot \) follows.
5. **Stuck.** Use \( \rulename{RAA} \): open a box with the negation of the current goal, whose new goal is \( \bot \); if that gives nothing, try the same with a goal further out whose box contains the stalled gap. Or use \( \rulename{LEM} \) on a well-chosen statement \( \chi \), and split on \( \chi \vee \neg\chi \) by \( \rulename{\vee E} \). Then return to step 3 (Section 2.5).

When no gap is left, number the lines and check the derivation as @def-derivation says.
:::

The steps are listed in the order in which to try them, and the order has reasons.

- **Step 2 loses nothing.** If a gap with the goal \( \psi \to \chi \) can be filled at all, so can the gap inside a box on \( \psi \) with the goal \( \chi \).
- **Choosing a side of \( \vee \) can leave a goal that does not follow.** From \( P \vee Q \), with \( P \) true and \( Q \) false, the step to \( Q \) breaks.
- **Step 5 loses nothing either, and still comes last.** The goal \( \bot \) gives step 2 nothing to work with, and a good statement to split on must be chosen.

::: {.second-reading title="Why the order loses nothing"}
**The goal-directed steps lose nothing.** Suppose the goal \( \psi \to \chi \) is derivable from the resources \( \Gamma \) at all, by some derivation \( D \). Then \( \chi \) is derivable from \( \Gamma \) together with \( \psi \): add \( \psi \) to the premises of \( D \) (@def-derivable asks only that the premises belong to the list), and append the line \( \chi \) by \( \rulename{{\to}E} \), citing the last line of \( D \) and the premise \( \psi \). A derivation from \( \Gamma \) and \( \psi \) can be written inside the box, its premises from \( \Gamma \) cited as available lines and \( \psi \) as the box's assumption (the pasting of @lem-weakening-cut). So opening a box on \( \psi \) never turns a derivable gap into an underivable one. With \( \rulename{\wedge E} \), \( \rulename{\neg E} \), or \( \rulename{{\leftrightarrow}E} \) as the appended line, the same argument covers \( \wedge \), \( \neg \), and \( \leftrightarrow \). That is why step 2 may be applied without thinking.

**Choosing a side of \( \vee \) can leave a goal that does not follow.** A disjunction can be derivable when neither side follows from the resources. From \( P \vee Q \) the goal \( Q \vee P \) is derivable (@exm-disjunction-first-derivations), but \( P \vee Q \) does not say which side holds, so a last line \( \rulename{\vee I} \) from \( Q \), or from \( P \), leaves a gap whose goal does not follow from its resources: \( P \) true and \( Q \) false makes \( P \vee Q \) true and \( Q \) false. Choosing a side is safe only once the resources decide it, typically inside a case of \( \rulename{\vee E} \), or when the disjunction is being manufactured for a clash (step 4) with a resource that is its negation: then the resources derive \( \bot \) as soon as they derive the disjunction, and from \( \bot \) every statement, either side included, by \( \rulename{\bot E} \).

**Step 5 also loses nothing, and still comes last.** If \( \varphi \) is derivable from the resources, then \( \bot \) is derivable from them together with \( \neg\varphi \), by one appended \( \rulename{\neg E} \); so an \( \rulename{RAA} \) box is always safe. A split on \( \chi \vee \neg\chi \) is safe too, since each case only adds a resource. Step 5 comes last because the goal \( \bot \) gives step 2 nothing to work with, because a good \( \chi \) must be chosen, and because a derivation that did not need the classical step reads worse with it (the costume of Section 2.5).
:::

The same method as a chart. A move counts only if the gap it makes is not already open above it, with the same goal and resources. When no move is left, go back to the gap that made this one.

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc start] (s) {a gap: its goal\\and its resources};
  \node[fc test, below=of s] (t0) {is the goal\\a resource?};
  \node[fc test, below=of t0] (t1) {is the goal a $\wedge$, $\to$,\\$\neg$ or $\leftrightarrow$?};
  \node[fc test, below=of t1] (t2) {can a resource be taken\\apart by a move untried\\for this gap?};
  \node[fc test, below=of t2] (t3) {is the goal $\bot$, or do the\\resources clash, with a clash\\untried for this gap?};
  \node[fc test, below=of t3] (t4) {is RAA on this goal, or LEM on\\a well-chosen statement,\\still untried for this gap?};
  \node[fc start, below=of t4] (e4) {no move left: back to the gap\\that made this one; at the first\\gap, stop and try to break the claim};
  \node[fc start, anchor=west] (e0) at ($(t0)+(4.5,0)$) {done: cite it,\\or copy it by R};
  \node[fc step, anchor=west] (b1) at ($(t1)+(4.5,0)$) {step 2: its introduction\\rule (boxes or two gaps)};
  \node[fc step, anchor=west] (b2) at ($(t2)+(4.5,0)$) {step 3: its elimination rule\\($\vee$E: both boxes end in the goal)};
  \node[fc step, anchor=west] (b3) at ($(t3)+(4.5,0)$) {step 4: find or build\\the clash; $\bot$E if needed};
  \node[fc step, anchor=west] (b4) at ($(t4)+(4.5,0)$) {step 5: RAA on the goal\\(not $\bot$), or LEM\\on that statement};
  \coordinate (m) at ($(s.south)!0.5!(t0.north)$);
  \coordinate (r) at ($(b2.east)+(0.5,0)$);
  \draw[fc arrow] (s) -- (t0);
  \foreach \t/\b in {t0/e0, t1/b1, t2/b2, t3/b3, t4/b4}
    \draw[fc arrow] (\t) -- node[above, font=\scriptsize] {yes} (\b);
  \foreach \a/\b in {t0/t1, t1/t2, t2/t3, t3/t4, t4/e4}
    \draw[fc arrow] (\a) -- node[right, font=\scriptsize] {no} (\b);
  \draw (b1.east) -- (b1.east -| r);
  \draw (b2.east) -- (b2.east -| r);
  \draw (b3.east) -- (b3.east -| r);
  \draw[fc arrow] (b4.east) -- (b4.east -| r) -- (m -| r) -- (m);
\end{tikzpicture}
\end{center}
```

::: {.check}
For each goal, with no premises, name the first rule the method aims for and the box or gaps it sets up.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg(P \wedge \neg P) \)
2. \( (P \vee Q) \to (Q \vee P) \)
3. \( (P \to Q) \wedge (Q \to (P \to Q)) \)
4. \( P \vee \neg(P \wedge Q) \)
:::
:::

::: {.solution}
(a) \( \rulename{\neg I} \): a box opened with \( P \wedge \neg P \), goal \( \bot \). (b) \( \rulename{{\to}I} \): a box opened with \( P \vee Q \), goal \( Q \vee P \); that goal is a disjunction, so it is postponed, and step 3 uses the new resource \( P \vee Q \) by \( \rulename{\vee E} \). (c) \( \rulename{\wedge I} \): two gaps, with goals \( P \to Q \) and \( Q \to (P \to Q) \), each then a box. (d) Step 2 postpones the disjunction, and with no premises steps 3 and 4 have nothing to use, so the search is at step 5 at once. \( \rulename{LEM} \) on \( P \) works: in the case \( P \), \( \rulename{\vee I} \) gives the left side; in the case \( \neg P \), a \( \rulename{\neg I} \) box on \( P \wedge Q \) clashes (its \( \rulename{\wedge E} \) gives \( P \)) and gives \( \neg(P \wedge Q) \), and \( \rulename{\vee I} \) gives the right side.
:::

## Splitting the goal

We now run the method. The first search uses only steps 2, 3, and 4. It is the full version of the chapter's main move, *read the skeleton off the goal, then work from both ends*, which comes back twice in the exercises with parts left blank.

::: {#exm-search-distribute}
[Splitting the goal, then using the premise]

Find a derivation of \( P \to \neg Q \vdash \neg(P \wedge Q) \wedge (Q \to \neg P) \).
:::

::: {.solution}
*Step 1.* The premise on top, the goal at the bottom, one gap. The resources of the gap are the premise alone.

*Step 2, first pass.* The goal's main connective is \( \wedge \), so it splits into two gaps, with goals \( \neg(P \wedge Q) \) and \( Q \to \neg P \), joined at the end by \( \rulename{\wedge I} \):

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \to \neg Q}
  \have {} {\vdots}
  \have {7} {\neg (P \wedge Q)}
  \have {} {\vdots}
  \have {13} {Q \to \neg P}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
\end{nd}$
\end{center}
```

*Step 2, again.* Both new goals have a connective, so step 2 applies to each. The goal \( \neg(P \wedge Q) \) asks for a \( \rulename{\neg I} \) box opened with \( P \wedge Q \) and ending in \( \bot \). The goal \( Q \to \neg P \) asks for a \( \rulename{{\to}I} \) box opened with \( Q \); inside it the goal \( \neg P \) asks, in turn, for a \( \rulename{\neg I} \) box opened with \( P \). Every gap now has the goal \( \bot \), and step 2 has nothing more to do:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \to \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have {} {\vdots}
  \have {6} {\bot}
  \close
  \have {7} {\neg (P \wedge Q)} \ni{2-6}
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {} {\vdots}
  \have {11} {\bot}
  \close
  \have {12} {\neg P} \ni{9-11}
  \close
  \have {13} {Q \to \neg P} \ii{8-12}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
\end{nd}$
\end{center}
```

*Steps 3 and 4, first gap.* The resources are lines 1 and 2. Step 3 splits line 2 into \( P \) and \( Q \) by \( \rulename{\wedge E} \). Now \( P \) is the hypothesis of line 1, so \( \rulename{{\to}E} \) gives \( \neg Q \). Step 4 finds the pair \( Q \), \( \neg Q \).

*Steps 3 and 4, second gap.* The resources are lines 1, 7, 8, and 9, and line 7 is not needed.

| Givens | Goal |
|---|---|
| \( P \to \neg Q \), \( \neg(P \wedge Q) \), \( Q \), \( P \) | \( \bot \) |
| … and \( \neg Q \) (→E 1, 9) | \( \bot \) ✓ (\( Q \) and \( \neg Q \) clash) |

\( \rulename{{\to}E} \) on lines 1 and 9 gives \( \neg Q \), which clashes with line 8. Both gaps close:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {\neg Q} \ie{1,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg (P \wedge Q)} \ni{2-6}
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {\neg Q} \ie{1,9}
  \have {11} {\bot} \ne{8,10}
  \close
  \have {12} {\neg P} \ni{9-11}
  \close
  \have {13} {Q \to \neg P} \ii{8-12}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
\end{nd}$
\end{center}
```

*What the method did.* The goal-directed steps wrote nine of the fourteen lines, every box among them, before the premise was used; the premise-directed steps wrote four, lines 3, 4, 5, and 10. The premise itself was used once in each gap, by the same \( \rulename{{\to}E} \). Line 10 cites line 1 from inside two boxes, which is legal because line 1 is a premise and so is available everywhere below it.
:::

Notice how little thinking the search needed. That is the typical shape of a successful search: **the goal fixes the skeleton, and the premises fill in the flesh.**

::: {.check}
In the second snapshot of @exm-search-distribute above, the second gap has the current goal \( \bot \) on line 11, and line 7 is one of its resources, though the gap never uses it. Why is line 7 available there, and why are lines 2–6 not?
:::

::: {.solution}
Line 7 lies in no box and above the gap, so it is available, though this gap will not need it. Lines 2–6 are not resources: they lie in a box that has closed.
:::

## Cases must end in the goal

When the goal gives nothing, the premises must. The next search is driven by a disjunction among the premises.

::: {#exm-search-cases}
[Proof by cases, found by the method]

Find a derivation of \( P \vee Q, \ P \to R, \ Q \to R \vdash R \).
:::

::: {.solution}
*Step 1.* The premises, one gap, the goal:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to R}
  \have {} {\vdots}
  \have {8} {R}
\end{nd}$
\end{center}
```

The goal \( R \) is a letter, so step 2 has nothing to do. Step 3 looks at the resources. \( \rulename{{\to}E} \) on \( P \to R \) needs \( P \), and making \( P \) a new goal is hopeless: from \( P \vee Q \) we know that one of \( P \), \( Q \) holds, not which. The disjunction itself is the resource to use, by \( \rulename{\vee E} \), with two boxes that each end in the current goal \( R \):

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to R}
  \open
  \hypo {4} {P}
  \have {} {\vdots}
  \have {5} {R}
  \close
  \open
  \hypo {6} {Q}
  \have {} {\vdots}
  \have {7} {R}
  \close
  \have {8} {R} \oe{1,4-5,6-7}
\end{nd}$
\end{center}
```

Inside the first box, \( P \) is a resource, so \( \rulename{{\to}E} \) on line 2 closes the gap at once; the second box is the same with line 3:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to R}
  \open
  \hypo {4} {P}
  \have {5} {R} \ie{2,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {R} \ie{3,6}
  \close
  \have {8} {R} \oe{1,4-5,6-7}
\end{nd}$
\end{center}
```

This is the pattern that Section 1.6 called the skeleton of almost every proof by cases (compare @exm-cases-on-hypothesis, which packages the same two boxes into one implication). The method found it without being told.

*Why the boxes end in the current goal.* \( \rulename{\vee E} \) (@def-rules-disjunction) gives, after the two boxes, their common last line and nothing else. A box that ends in anything but the current goal leaves that goal still to be reached, and two boxes that end in different statements cannot be combined at all.
:::

## Postponing a disjunction

The third search has a disjunction as its goal. It shows why step 2 postpones one, and how a dead end can name the statement to split on.

::: {#exm-search-postpone-or}
[Choosing a side too early]

Find a derivation of \( P \to (Q \vee R) \vdash (P \to Q) \vee (P \to R) \).
:::

::: {.solution}
*The tempting start.* The goal is a disjunction, and it is tempting to choose a side at once, say \( P \to Q \), and finish with \( \rulename{\vee I} \). The new goal is an implication, so we open a box on \( P \); then \( \rulename{{\to}E} \) gives \( Q \vee R \), and \( \rulename{\vee E} \) splits into the cases \( Q \) and \( R \), each to end in the current goal \( Q \). The first case ends at once. The second is a dead end:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \to (Q \vee R)}
  \open
  \hypo {2} {P} \purpose{\ii}
  \have {3} {Q \vee R} \ie{1,2}
  \open
  \hypo {4} {Q} \purpose{\oe}
  \close
  \open
  \hypo {5} {R} \purpose{\oe}
  \have {} {\vdots}
  \have {} {Q}
  \close
  \have {} {Q} \oe{}
  \close
  \have {} {P \to Q} \ii{}
  \have {} {(P \to Q) \vee (P \to R)} \oi{}
\end{nd}$
\end{center}
```

In the case \( R \) the resources are \( P \to (Q \vee R) \), \( P \), \( Q \vee R \), and \( R \), and none of them yields \( Q \): no resource has \( Q \) as a conclusion except \( Q \vee R \), which is already split, and nothing clashes. Choosing the right side instead fails in the mirror image, in the case \( Q \). In fact neither side follows from the premise alone: with \( P \) and \( Q \) true and \( R \) false the premise is true and \( P \to R \) is false, and with \( P \) and \( R \) true and \( Q \) false the premise is true and \( P \to Q \) is false.

*The diagnosis.* Each case of the dead end knew which side it wanted: the case \( Q \) wanted \( P \to Q \), and the case \( R \) wanted \( P \to R \). But those cases were opened inside the box of \( P \), too late to choose the side of a disjunction that stands outside it. The side must be decided **before** any box is opened, and the premise does not decide it. Steps 2–4 are used up: we are at step 5.

The dead end also names the statement to split on. If \( Q \) holds, the left side is easy. If \( Q \) fails, then from \( P \) the premise gives \( Q \vee R \) with its left side refuted, and \( \rulename{DS} \) gives \( R \). So we use \( \rulename{LEM} \) on \( Q \), and each case gets the whole goal:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \to (Q \vee R)}
  \have {2} {Q \vee \neg Q} \lem{}
  \open
  \hypo {3} {Q}
  \have {} {\vdots}
  \have {7} {(P \to Q) \vee (P \to R)}
  \close
  \open
  \hypo {8} {\neg Q}
  \have {} {\vdots}
  \have {13} {(P \to Q) \vee (P \to R)}
  \close
  \have {14} {(P \to Q) \vee (P \to R)} \oe{2,3-7,8-13}
\end{nd}$
\end{center}
```

Now each case decides the side. In the case \( Q \), the goal is \( P \to Q \): a box on \( P \) whose last line repeats \( Q \). In the case \( \neg Q \), the goal is \( P \to R \): a box on \( P \), then \( Q \vee R \) by \( \rulename{{\to}E} \), then \( R \) by @prp-disjunctive-syllogism used as a derived rule, citing \( Q \vee R \) and \( \neg Q \). Then \( \rulename{\vee I} \), on the correct side each time:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \have {2} {Q \vee \neg Q} \lem{}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {(P \to Q) \vee (P \to R)} \oi{6}
  \close
  \open
  \hypo {8} {\neg Q}
  \open
  \hypo {9} {P}
  \have {10} {Q \vee R} \ie{1,9}
  \have {11} {R} \ds{10,8}
  \close
  \have {12} {P \to R} \ii{9-11}
  \have {13} {(P \to Q) \vee (P \to R)} \oi{12}
  \close
  \have {14} {(P \to Q) \vee (P \to R)} \oe{2,3-7,8-13}
\end{nd}$
\end{center}
```

*What the method did.* Step 2 postponed the goal, the tempting start broke that rule, and its dead end showed both why the rule exists and what to do instead. Line 5 repeats line 3 because \( \rulename{{\to}I} \) needs \( Q \) as a line of the box of line 4 itself.
:::

::: {.warning}
**Do not choose a disjunct early.** A goal \( \psi \vee \chi \) tempts us to pick a side and prove it, and the choice usually fails, as the first attempt above did: neither \( P \to Q \) nor \( P \to R \) follows from the premise. Postpone the \( \vee \) goal, use the resources first, and choose a side only inside a case that decides it.
:::

## When nothing else works

The fourth search reaches step 5 in the other form, \( \rulename{RAA} \), and then needs steps 2 and 4 inside the box.

::: {#exm-search-raa}
[A search that reaches step 5 at once]

Find a derivation of \( \neg(P \leftrightarrow Q) \vdash P \vee Q \).
:::

::: {.solution}
*Steps 1–4.* The goal is a disjunction, so step 2 postpones it. The one resource is a negation, and a negation can be used only in a clash (step 4), and here no clash can be found or manufactured. Neither side is in hand: the premise says only that \( P \) and \( Q \) differ, not which one holds. Steps 2–4 have nothing to offer.

*Step 5.* We assume the negation of the goal. The new goal is \( \bot \), and the gap has one more resource:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
  \hypo {2} {\neg (P \vee Q)}
  \have {} {\vdots}
  \have {12} {\bot}
  \close
  \have {13} {P \vee Q} \raa{2-12}
\end{nd}$
\end{center}
```

*Step 4 inside the box.* The resources are two negations, \( \neg(P \leftrightarrow Q) \) and \( \neg(P \vee Q) \), and no pair clashes yet. So we choose a statement to manufacture: \( P \leftrightarrow Q \), to clash with line 1, or \( P \vee Q \), to clash with line 2. The second is the goal we started from, a disjunction of two letters with no side in hand, so aiming at it leads back to the start. So we choose \( P \leftrightarrow Q \), and it is a biconditional, so step 2 sets up two boxes:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
  \hypo {2} {\neg (P \vee Q)}
  \open
  \hypo {3} {P}
  \have {} {\vdots}
  \have {6} {Q}
  \close
  \open
  \hypo {7} {Q}
  \have {} {\vdots}
  \have {10} {P}
  \close
  \have {11} {P \leftrightarrow Q} \bi{3-6,7-10}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {P \vee Q} \raa{2-12}
\end{nd}$
\end{center}
```

*The two small gaps.* In the first, the resources are lines 1, 2, and 3, and the goal \( Q \) is a letter that no resource produces. But the resources clash once a line is manufactured: \( \rulename{\vee I} \) builds \( P \vee Q \) from line 3, which clashes with line 2, and \( \rulename{\bot E} \) writes \( Q \) (step 4: an impossible case closes itself). The second gap is the mirror image:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
  \hypo {2} {\neg (P \vee Q)}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \have {5} {\bot} \ne{4,2}
  \have {6} {Q} \be{5}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {P \vee Q} \oi{7}
  \have {9} {\bot} \ne{8,2}
  \have {10} {P} \be{9}
  \close
  \have {11} {P \leftrightarrow Q} \bi{3-6,7-10}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {P \vee Q} \raa{2-12}
\end{nd}$
\end{center}
```

*What the method did.* Step 5 came first, because nothing else applied, and after it steps 2 and 4 did the rest: step 4 chose which clash to aim for, step 2 read the two boxes off \( P \leftrightarrow Q \), and step 4 closed each box with a manufactured clash and \( \rulename{\bot E} \). In words: *suppose neither \( P \) nor \( Q \) holds; then each of them implies the other, since neither can hold at all; so \( P \leftrightarrow Q \), against the premise.* The assumption of line 2 is used twice, at lines 5 and 9.
:::

::: {.second-reading title="Other splits that also work"}
**In @exm-search-postpone-or.** \( \rulename{LEM} \) on \( P \), the first split one thinks of, also succeeds, but less well: in the case \( P \) the premise gives \( Q \vee R \), and a second \( \rulename{\vee E} \), with two more implication boxes, is needed inside it; the finished derivation has 22 lines against these 14.

**In @exm-search-raa.** A split by \( \rulename{LEM} \) on \( P \) also works, but less well: in the case \( \neg P \) the goal side \( Q \) is a letter that the resources do not give, and the search is stuck there a second time.
:::

Step 5's advice to try a goal further out is shown on Peirce's law in the fold below.

::: {.second-reading title="Step 5 one level out: the search for Peirce's law"}
The derivation of Peirce's law (@prp-peirce, in the fold of Section 2.5) adds one detail to step 5.

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {1} {(P \to Q) \to P} \purpose{\ii}
  \open
  \hypo {} {P} \purpose{\ii}
  \have {} {\vdots}
  \have {} {Q}
  \close
  \have {} {P \to Q} \ii{}
  \have {} {P} \ie{}
  \close
  \have {} {((P \to Q) \to P) \to P} \ii{}
\end{nd}$
\end{center}
```

In the box on \( P \) with the goal \( Q \), the search stalls: assuming \( \neg Q \) gives nothing new, since a clash with \( \neg Q \) needs \( Q \) itself. One level out, the search assumes \( \neg P \):

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {1} {(P \to Q) \to P}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P} \purpose{\ii}
  \have {} {\vdots}
  \have {5} {Q}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \have {7} {P} \ie{1,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {P} \raa{2-8}
  \close
  \have {10} {((P \to Q) \to P) \to P} \ii{1-9}
\end{nd}$
\end{center}
```

The new resource \( \neg P \) is available in every gap inside its box, including the stalled one, where it clashes with line 3. That is why step 5 says to try a goal further out.

::: {.check}
In the second snapshot, which two resources of the gap clash, and what does \( \rulename{\bot E} \) then write?
:::

::: {.solution}
Lines 3 (\( P \)) and 2 (\( \neg P \)) give \( \bot \) by \( \rulename{\neg E} \) 3, 2 at line 4, and \( \rulename{\bot E} \) 4 writes \( Q \), line 5.
:::
:::

## Four refinements

The method finds a derivation; these four refinements usually find a shorter or more direct one.

- **Find the goal among the resources.** Before step 2, ask whether the current goal is already available; if so, cite it, or copy it into the current box by \( \rulename{R} \).
- **Derive what needs nothing new before opening a box.** \( \rulename{\wedge E} \) on a resource, and \( \rulename{{\to}E} \) or \( \rulename{{\leftrightarrow}E} \) when both of their lines stand, may be written at once, above the boxes the goal asks for: a line outside the boxes is available inside all of them, so it is written once instead of once per box. (\( \rulename{\vee E} \) is not such a step: it opens boxes.)
- **Look first for a clash partner already on a line.** When the goal is \( \bot \), scan the resources for a negation \( \neg\chi \) whose \( \chi \) is cheap, or for \( \chi \) and \( \neg\chi \) both in reach, before manufacturing anything (step 4).

::: {#exm-search-free-lines}
[Lines that need nothing new]

Find a derivation of \( P \wedge (P \to Q), \ Q \to R \vdash (S \to R) \wedge (T \to (Q \wedge R)) \).
:::

::: {.solution}
*The search.* The goal is a conjunction of two implications, so step 2 will open a box on \( S \) and a box on \( T \):

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (P \to Q)}
  \hypo {2} {Q \to R}
  \have[\ ][0] {} {\vdots}
  \have[][13] {13} {(S \to R) \wedge (T \to (Q \wedge R))}
\end{nd}$
\end{center}
```

Before it does, the resources give lines that need nothing new: \( P \) and \( P \to Q \) by \( \rulename{\wedge E} \), then \( Q \) by \( \rulename{{\to}E} \), and then \( R \) by \( \rulename{{\to}E} \) on the second premise. With \( Q \) and \( R \) outside every box, the two boxes are short:

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (P \to Q)}
  \hypo {2} {Q \to R}
  \have {3} {P} \ae{1}
  \have {4} {P \to Q} \ae{1}
  \have {5} {Q} \ie{4,3}
  \have {6} {R} \ie{2,5}
  \open
  \hypo {7} {S} \purpose{\ii}
  \have[\ ][0] {} {\vdots}
  \have[][8] {8} {R}
  \close
  \have {9} {S \to R} \ii{7-8}
  \open
  \hypo {10} {T} \purpose{\ii}
  \have[\ ][0] {} {\vdots}
  \have[][11] {11} {Q \wedge R}
  \close
  \have {12} {T \to (Q \wedge R)} \ii{10-11}
  \have {13} {(S \to R) \wedge (T \to (Q \wedge R))} \ai{9,12}
\end{nd}$
\end{center}
```

In the box of \( S \) the goal \( R \) is a resource, copied by \( \rulename{R} \). In the box of \( T \), \( \rulename{\wedge I} \) joins \( Q \) and \( R \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (P \to Q)}
  \hypo {2} {Q \to R}
  \have {3} {P} \ae{1}
  \have {4} {P \to Q} \ae{1}
  \have {5} {Q} \ie{4,3}
  \have {6} {R} \ie{2,5}
  \open
  \hypo {7} {S}
  \have {8} {R} \r{6}
  \close
  \have {9} {S \to R} \ii{7-8}
  \open
  \hypo {10} {T}
  \have {11} {Q \wedge R} \ai{5,6}
  \close
  \have {12} {T \to (Q \wedge R)} \ii{10-11}
  \have {13} {(S \to R) \wedge (T \to (Q \wedge R))} \ai{9,12}
\end{nd}$
\end{center}
```
:::

::: {.check}
In @exm-search-free-lines, which refinement does line 8 use, and which do lines 3–6 use?
:::

::: {.solution}
Line 8 finds the goal \( R \) among the resources (line 6) and copies it into the box of \( S \). Lines 3–6 need nothing new and are written before any box opens, so both boxes can use them.
:::

**No detours.** Never build a line by an introduction rule and then, at once, take that line apart by the matching elimination. The line the pair produces was within reach without it. This includes \( \rulename{\neg I} \) followed by \( \rulename{\neg E} \) on the negation it built. A manufactured clash is not a detour: \( \rulename{\vee I} \) followed by \( \rulename{\neg E} \) against \( \neg(\varphi \vee \psi) \) uses the new line with a different connective. The book uses this as advice, not as a theorem: a detour is legal, and cutting one need not shorten a derivation, since an introduced line cited elsewhere stays.

::: {.second-reading title="Why a detour's line was within reach"}
After \( \rulename{\wedge I} \) joins lines \( i \) and \( j \), \( \rulename{\wedge E} \) on the new line gives back line \( i \) or line \( j \). After \( \rulename{{\to}I} \) closes a box from \( \varphi \) to \( \psi \), \( \rulename{{\to}E} \) on the new implication and a line \( \varphi \) gives \( \psi \); the box's lines, copied with that line in place of the assumption, give \( \psi \) directly. After \( \rulename{\neg I} \) closes a box from \( \varphi \) to \( \bot \), \( \rulename{\neg E} \) on the new negation and a line \( \varphi \) gives \( \bot \); the box's lines, copied likewise, give \( \bot \) directly. After \( \rulename{\vee I} \) builds \( \varphi \vee \psi \) from a line \( \varphi \), \( \rulename{\vee E} \) on it gives what its first case gives, and the first case's lines, copied with the line \( \varphi \) in place of the assumption, give that directly. Every copied citation stays legal by the scope rule of @def-derivation, since the line put in place of the assumption stands above the copy.
:::

::: {.check}
Lines 2 and 3 are \( P \) and \( R \); line 4 is \( P \wedge R \), \( \rulename{\wedge I} \) 2, 3; line 5 is \( R \), \( \rulename{\wedge E} \) 4. Which refinement does this break, and what should line 5 cite instead?
:::

::: {.solution}
No detours. Lines 4–5 build a conjunction and take it apart at once; line 5's statement is line 3, so cite line 3, or copy it by \( \rulename{R} \) where it must lie in the current box.
:::

## A search that fails

The method is not a machine that always succeeds. Here it fails, and the failure is instructive.

Try \( P \to Q \vdash Q \to P \). Step 2 opens a box on \( Q \) with the goal \( P \):

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {Q} \purpose{\ii}
  \have {} {\vdots}
  \have {} {P}
  \close
  \have {} {Q \to P} \ii{}
\end{nd}$
\end{center}
```

Every further move goes round in a circle:

| Attempt | What it needs | Why that goes round in a circle |
|---|---|---|
| step 3: \( \rulename{{\to}E} \) on line 1 | \( P \) | \( P \) is the goal |
| step 4: a clash | a negation among the resources | there is none |
| step 5: \( \rulename{RAA} \), a box on \( \neg P \) | \( P \), to clash with \( \neg P \) | \( P \) is the goal |
| step 5: \( \rulename{LEM} \) on \( P \) | in the case \( \neg P \), the goal \( P \) | the same gap, one resource richer and no closer |
| step 5 further out: \( \rulename{RAA} \) on \( \neg(Q \to P) \) | \( Q \to P \), to clash | step 2 opens the same box on \( Q \) with the same goal \( P \) |

Every row returns to one gap, "\( P \) from \( P \to Q \) and \( Q \)". That is affirming the consequent (Section 1.3).

::: {.check}
Which row of the table would close the gap if affirming the consequent were a rule?
:::

::: {.solution}
The first: the mirror image of \( \rulename{{\to}E} \) would give \( P \) from \( P \to Q \) and the resource \( Q \).
:::

But notice what we have **not** shown. A search that fails proves nothing about derivations in general. An assumption may be any statement at all, by the assumption clause of @def-derivation, so there are infinitely many derivations to consider, and a cleverer one might exist. To show that **no** derivation of \( Q \to P \) from \( P \to Q \) exists, we need a different tool.

*We show that something is derivable by exhibiting a derivation; how could we ever show that something is not?* Section 1.1's move already breaks Argument B's form, from \( P \to Q \) to \( Q \to P \): with \( P \) false and \( Q \) true, the premise is true and the conclusion false. What it cannot yet tell us is that **no derivation** leads from a premise to a conclusion that some choice of statements makes false. Section 3.2 gives this question a sharper form, and the chapter ends on it.

## A mathematical goal

The method reads the frame of a proof off the goal whether the statements are letters or facts about numbers. In ordinary mathematics its payoff is that the first and last sentences of a proof, and its division into parts, are fixed before any mathematics is done.

::: {#exm-skeleton-odd-product}
[Building a skeleton]

Let \( m \) and \( n \) be integers. Prove that if \( mn \) is odd, then \( m \) is odd and \( n \) is odd.
:::

::: {.solution}
*The skeleton.* The main connective is "if … then", so step 2 opens a \( \rulename{{\to}I} \) box: "Assume \( mn \) is odd. … Hence \( m \) is odd and \( n \) is odd." The new goal is a conjunction, so step 2 again: two separate proofs, one that \( m \) is odd and one that \( n \) is odd. Each is a letter as far as logic can see, and the one resource, "\( mn \) is odd", cannot be taken apart. So step 3 brings in facts we can compute with: "if \( m \) is even then \( mn \) is even" is one, and \( \rulename{CP} \) (@prp-contrapositive) turns it into "if \( mn \) is not even then \( m \) is not even", which the resource can feed. Then "every integer is even or odd" and \( \rulename{DS} \) finish. The givens and the goal are tabulated in the fold below.

*The proof.* Assume \( mn \) is odd. We show that \( m \) is odd and that \( n \) is odd.

First, if \( m \) is even, say \( m = 2k \) with \( k \) an integer, then \( mn = 2(kn) \) is even. By the contrapositive (@prp-contrapositive), if \( mn \) is not even, then \( m \) is not even. Now \( mn \) is odd, so it is not even, since no integer is both; hence \( m \) is not even. Since every integer is even or odd, \( m \) is odd, by @prp-disjunctive-syllogism.

Exchanging the roles of \( m \) and \( n \) in the previous paragraph shows that \( n \) is odd. Hence \( m \) and \( n \) are both odd.

*What the method did.* It fixed the first sentence, the two paragraphs, and the last sentence; the only computation is \( mn = 2(kn) \). No step uses \( \rulename{RAA} \): the classical-looking move from "\( m \) is not even" to "\( m \) is odd" is disjunctive syllogism on the fact that every integer is even or odd.
:::

::: {.second-reading title="The givens and the goal"}
| Givens | Goal |
|---|---|
| the facts: every integer is even or odd, and not both; if \( m \) is even, then \( mn \) is even; if \( n \) is even, then \( mn \) is even | if \( mn \) is odd, then \( m \) is odd and \( n \) is odd |
| … and \( mn \) odd (→I) | \( m \) odd and \( n \) odd |
| the same | \( m \) odd; \( n \) odd (∧I: two goals) |
| … and \( mn \) not even ("not both"); \( m \) not even (CP, →E) | \( m \) odd ✓ (DS); \( n \) odd by the same steps, with \( m \) and \( n \) exchanged |
:::

::: {.warning}
**Do not assume what you want to prove.** To derive a goal \( \varphi \), it is tempting to open a box with \( \varphi \). The box reaches \( \varphi \) at once, but after it closes it gives \( \varphi \to \varphi \), not \( \varphi \), and its assumption is gone. An assumption is useful when the goal asks for it: the hypothesis of an implication (step 2), the negated goal of \( \rulename{RAA} \) (step 5), a disjunct of a resource (step 3). Opening the box on the conclusion of an implication is the converse error of Argument B, diagnosed in Section 1.4.
:::

::: {.second-reading title="Logic permits; it does not choose"}
A derivation of \( \Gamma \vdash \varphi \) says that whoever accepts every member of \( \Gamma \) is committed to \( \varphi \). It does not say that \( \varphi \) should now be believed. If \( \varphi \) is plainly false, say \( 0 = 1 \), the derivation is a reason to give up a member of \( \Gamma \), and it does not say which. A mathematician who derives \( 0 = 1 \) from the hypotheses of a lemma has learned that those hypotheses cannot hold together; Section 3.2 calls such a list inconsistent, and a proof by contradiction is built to reach exactly that.

In the other direction, at every gap the rules permit far more lines than any search writes: \( \rulename{\wedge E} \) on every conjunction, \( \rulename{\vee I} \) with any statement at all. The rules choose none of them. The method chooses, and the method is advice, not logic: two searchers may find two different derivations, and both are correct.
:::

## The rules in one place

Here are all the primitive rules of Chapters 1 and 2 on one card.

| Rule | Shape | You write | Lean |
|---|---|---|---|
| \( \rulename{\wedge I} \) | \( \varphi \), \( \psi \) \( \Longrightarrow \) \( \varphi \wedge \psi \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | \( \varphi \wedge \psi \) \( \Longrightarrow \) \( \varphi \) (or \( \psi \)) | "In particular, \( P \)." | `h.1` (and `h.2`) |
| \( \rulename{{\to}E} \) | \( \varphi \to \psi \), \( \varphi \) \( \Longrightarrow \) \( \psi \) | "Since \( P \) implies \( Q \), and \( P \) holds, \( Q \)." | `exact h hp` |
| \( \rulename{{\to}I} \) | box \( \varphi \) … \( \psi \) \( \Longrightarrow \) \( \varphi \to \psi \) | "Assume \( P \). … Hence \( Q \)." | `intro hp` |
| \( \rulename{R} \) | \( \varphi \) (available) \( \Longrightarrow \) \( \varphi \), copied | "As shown above, \( P \)." | `exact hp` |
| \( \rulename{\vee I} \) | \( \varphi \) \( \Longrightarrow \) \( \varphi \vee \psi \) (or \( \psi \vee \varphi \)) | "So \( P \) or \( Q \) holds." | `left` (or `Or.inl hp`); `right` |
| \( \rulename{\vee E} \) | \( \varphi \vee \psi \), box \( \varphi \) … \( \chi \), box \( \psi \) … \( \chi \) \( \Longrightarrow \) \( \chi \) | "Case 1: \( P \). … so \( R \). Case 2: \( Q \). … so \( R \). In either case, \( R \)." | `Or.elim h` (or `cases h`) |
| \( \rulename{\neg E} \) | \( \varphi \), \( \neg\varphi \) \( \Longrightarrow \) \( \bot \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
| \( \rulename{\bot E} \) | \( \bot \) \( \Longrightarrow \) any \( \varphi \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |
| \( \rulename{\neg I} \) | box \( \varphi \) … \( \bot \) \( \Longrightarrow \) \( \neg\varphi \) | "Suppose \( P \). … This is a contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |
| \( \rulename{{\leftrightarrow}I} \) | box \( \varphi \) … \( \psi \), box \( \psi \) … \( \varphi \) \( \Longrightarrow \) \( \varphi \leftrightarrow \psi \) | "\( (\Rightarrow) \) Suppose \( P \). … so \( Q \). \( (\Leftarrow) \) Suppose \( Q \). … so \( P \)." | `constructor` |
| \( \rulename{{\leftrightarrow}E} \) | \( \varphi \leftrightarrow \psi \), \( \varphi \) \( \Longrightarrow \) \( \psi \) (or with \( \psi \), \( \varphi \)) | "Since \( P \) holds if and only if \( Q \) does, and \( P \) holds, so does \( Q \)." | `h.mp hp` / `h.mpr hq` |
| \( \rulename{RAA} \) | box \( \neg\varphi \) … \( \bot \) \( \Longrightarrow \) \( \varphi \) | "Suppose, for a contradiction, that \( P \) fails. … This is impossible. Hence \( P \)." | `by_contra h` |

This is the reference sheet for Chapters 1 and 2: every primitive rule as its schema, with the label that defines it. As in every schema (@def-rule-schema), \( \varphi, \psi, \chi \) stand for any statements, replaced consistently, and \( i, j, k, \dots \) for line numbers. Each box rule needs the box's last line as a line of that box itself, not inside a further box, and every cited line or box must be available (@def-derivation).

**Conjunction** (@def-rules-conjunction): \( \rulename{\wedge I} \), and the two forms of \( \rulename{\wedge E} \).

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {j} {\psi}
  \have {k} {\varphi \wedge \psi} \ai{i,j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \wedge \psi}
  \have {k} {\varphi} \ae{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \wedge \psi}
  \have {k} {\psi} \ae{i}
\end{nd}$
\end{center}
```

**Implication** (@def-rules-implication): \( \rulename{{\to}I} \) and \( \rulename{{\to}E} \).

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {i} {\varphi}
  \have {} {\vdots}
  \have {j} {\psi}
  \close
  \have {k} {\varphi \to \psi} \ii{i-j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \to \psi}
  \have {j} {\varphi}
  \have {k} {\psi} \ie{i,j}
\end{nd}$
\end{center}
```

**Disjunction** (@def-rules-disjunction): the two forms of \( \rulename{\vee I} \), and \( \rulename{\vee E} \), whose two boxes end in the same statement \( \chi \).

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {k} {\varphi \vee \psi} \oi{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {k} {\psi \vee \varphi} \oi{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \vee \psi}
  \open
  \hypo {j} {\varphi}
  \have {} {\vdots}
  \have {k} {\chi}
  \close
  \open
  \hypo {l} {\psi}
  \have {} {\vdots}
  \have {m} {\chi}
  \close
  \have {n} {\chi} \oe{i,j-k,l-m}
\end{nd}$
\end{center}
```

**Contradiction and negation** (@def-rules-contradiction, @def-rules-negation): \( \rulename{\neg E} \), \( \rulename{\bot E} \) (which may write **any** statement \( \varphi \)), and \( \rulename{\neg I} \).

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {j} {\neg \varphi}
  \have {k} {\bot} \ne{i,j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\bot}
  \have {k} {\varphi} \be{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \open
  \hypo {i} {\varphi}
  \have {} {\vdots}
  \have {j} {\bot}
  \close
  \have {k} {\neg \varphi} \ni{i-j}
\end{nd}$
\end{center}
```

**Biconditional** (@def-rules-biconditional): \( \rulename{{\leftrightarrow}I} \), and \( \rulename{{\leftrightarrow}E} \), which works in both directions.

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {i} {\varphi}
  \have {} {\vdots}
  \have {j} {\psi}
  \close
  \open
  \hypo {k} {\psi}
  \have {} {\vdots}
  \have {l} {\varphi}
  \close
  \have {m} {\varphi \leftrightarrow \psi} \bi{i-j,k-l}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \leftrightarrow \psi}
  \have {j} {\varphi}
  \have {k} {\psi} \bie{i,j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi \leftrightarrow \psi}
  \have {j} {\psi}
  \have {k} {\varphi} \bie{i,j}
\end{nd}$
\end{center}
```

**Reductio ad absurdum** (@def-rule-raa), the one classical rule, **and repetition**, clause (D3) of @def-derivation, which copies an available line into the current box.

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {i} {\neg \varphi}
  \have {} {\vdots}
  \have {j} {\bot}
  \close
  \have {k} {\varphi} \raa{i-j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {} {\vdots}
  \have {k} {\varphi} \r{i}
\end{nd}$
\end{center}
```

**Derived rules.** Each is a proved sequent, used as one line that cites the lines holding its premises (@def-derived-rule). The table lists the sequents of Chapters 1 and 2 that searches use most; every other sequent proved there may be used in the same way. Where a rule has no short name, the justification names the result, as "(ex falso)" or "VI".

| In a justification | Sequent | Proved in | Our derivation uses \( \rulename{RAA} \) |
|---|---|---|---|
| (and commutes) | \( P \wedge Q \vdash Q \wedge P \) | @prp-and-commutes | no |
| (implication is transitive) | \( P \to Q, \ Q \to R \vdash P \to R \) | @prp-implication-transitive | no |
| (curry) | \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \) | @prp-curry | no |
| (or commutes) | \( P \vee Q \vdash Q \vee P \) | @exm-disjunction-first-derivations | no |
| (or merges) | \( P \vee P \vdash P \) | @exm-disjunction-first-derivations | no |
| (and regroups) | \( (P \wedge Q) \wedge R \vdash P \wedge (Q \wedge R) \) | @prp-and-associative | no |
| (or regroups) | \( P \vee (Q \vee R) \vdash (P \vee Q) \vee R \) | @exm-disjunction-regroup | no |
| (distributivity) | \( P \wedge (Q \vee R) \dashv\vdash (P \wedge Q) \vee (P \wedge R) \) | @prp-distributivity | no |
| (cases on a hypothesis) | \( (P \to R) \wedge (Q \to R) \dashv\vdash (P \vee Q) \to R \) | @exm-cases-on-hypothesis; the converse @exm-or-hypothesis-split | no |
| \( \rulename{CD} \) (constructive dilemma) | \( (P \to R) \wedge (Q \to S), \ P \vee Q \vdash R \vee S \) | @exm-constructive-dilemma | no |
| (destructive dilemma) | \( (P \to R) \wedge (Q \to S), \ \neg R \vee \neg S \vdash \neg P \vee \neg Q \) | @exr-derived-rules-b4 (b) | no |
| (*modus ponendo tollens*) | \( \neg(P \wedge Q) \vdash P \to \neg Q \) | @exr-derived-rules-b4 (c) | no |
| (ex falso) | \( P, \ \neg P \vdash Q \) | @prp-ex-falso | no |
| VI (vacuous implication) | \( \neg P \vdash P \to Q \) | @prp-vacuous-implication | no |
| \( \rulename{MT} \) | \( P \to Q, \ \neg Q \vdash \neg P \) | @prp-modus-tollens | no |
| \( \rulename{CP} \) | \( P \to Q \vdash \neg Q \to \neg P \) | @prp-contrapositive | no |
| \( \rulename{DS} \) | \( P \vee Q, \ \neg P \vdash Q \) | @prp-disjunctive-syllogism | no |
| (\( \rulename{DS} \), other disjunct) | \( P \vee Q, \ \neg Q \vdash P \) | @exr-derived-rules-b1 (a) | no |
| (iff symmetric) | \( P \leftrightarrow Q \vdash Q \leftrightarrow P \) | @exm-iff-symmetric | no |
| (iff as two implications) | \( P \leftrightarrow Q \dashv\vdash (P \to Q) \wedge (Q \to P) \) | @prp-iff-two-implications | no |
| (iff of negations) | \( P \leftrightarrow Q \vdash \neg P \leftrightarrow \neg Q \), and its converse | @exm-iff-negations; the converse @exr-reductio-and-classical-rules-b2 | the converse only |
| (equivalence cycle) | \( P \to Q, \ Q \to R, \ R \to P \vdash P \leftrightarrow Q \) | @prp-equivalence-cycle | no |
| \( \rulename{\neg\neg I} \) | \( P \vdash \neg\neg P \) | @prp-double-negation (a), first in @exm-double-negation-introduction | no |
| \( \rulename{\neg\neg E} \) | \( \neg\neg P \vdash P \) | @prp-double-negation (b) | yes |
| (\( \rulename{CP} \), converse) | \( \neg Q \to \neg P \vdash P \to Q \) | @prp-contrapositive-converse | yes |
| \( \rulename{LEM} \) | \( \vdash P \vee \neg P \) | @prp-excluded-middle | yes |
| (Peirce) | \( \vdash ((P \to Q) \to P) \to P \) | @prp-peirce | yes |
| \( \rulename{DM} \) | the four laws of @prp-de-morgan | @prp-de-morgan | (d) only |
| (implication as disjunction) | \( \neg P \vee Q \vdash P \to Q \), and its converse | @prp-implication-as-disjunction | the converse only, through \( \rulename{LEM} \) |

Four rows are proved in exercises, not in the text: the other form of \( \rulename{DS} \), the destructive dilemma, *modus ponendo tollens*, and the converse of the iff of negations. Exercises may use them as rules; the text's own proofs do not.

Each rule is also a move: the table of moves at the start of this section is the decision chart of Section 1.6, grown to every connective, read by the goal for the introduction rules and by an available line for the elimination rules; the chart after the method's steps draws their order.

::: {.warning}
**Cite only what is already proved.** A derived rule is an abbreviation for its derivation, so it may be used only after that derivation exists, and never inside it. For example, the second route to @prp-de-morgan (d) splits on excluded middle; a proof of excluded middle that used De Morgan's law (d) along that route would be circular. In this book the check is simple: cite only labels that appear earlier.
:::

## Exercises

### A. Check your understanding

::: {#exr-finding-derivations-a1}
[A1]

For (a)–(d), name the goal's main connective, the first rule the method aims for, and the first sentence of a proof. For (e)–(f), name the elimination rule the premise invites, and what it needs.

::: {.enumerate options="label=(\alph*)"}
1. For real \( x \): if \( x^3 < 0 \) then \( x < 0 \).
2. There is no integer \( n \) with \( 2n = 7 \).
3. For real \( x \) and \( y \): \( \abs{xy} = \abs{x}\abs{y} \) and \( \abs{x + y} \le \abs{x} + \abs{y} \).
4. For an integer \( n \): \( n \) is odd if and only if \( n^2 \) is odd.
5. The premise \( (P \wedge Q) \to R \), with the goal \( R \) and the resources \( P \) and \( Q \).
6. The premise \( \neg(P \vee Q) \), with the goal \( \bot \) and the resource \( Q \).
:::
:::

::: {.solution}
(a) \( \to \); \( \rulename{{\to}I} \): "Assume \( x^3 < 0 \)." (Starting "Suppose \( x \ge 0 \)" inside that frame is an \( \rulename{RAA} \) box on the goal \( x < 0 \), not the contrapositive; a proof through the contrapositive replaces the frame, proving "if \( x \ge 0 \) then \( x^3 \ge 0 \)" and then applying \( \rulename{CP} \).)

(b) \( \neg \), since the claim is "not: there is an integer \( n \) with \( 2n = 7 \)"; \( \rulename{\neg I} \): "Suppose \( n \) is an integer with \( 2n = 7 \).\"

(c) \( \wedge \); \( \rulename{\wedge I} \): "We prove the two statements in turn."

(d) \( \leftrightarrow \); \( \rulename{{\leftrightarrow}I} \): "\( (\Rightarrow) \) Assume \( n \) is odd."

(e) \( \rulename{{\to}E} \), which needs the hypothesis \( P \wedge Q \): make it a new goal, reached by \( \rulename{\wedge I} \) from \( P \) and \( Q \); then \( \rulename{{\to}E} \) gives \( R \).

(f) \( \rulename{\neg E} \), which needs \( P \vee Q \) beside \( \neg(P \vee Q) \): make \( P \vee Q \) the new goal (step 4), reached by \( \rulename{\vee I} \) from \( Q \).
:::

::: {#exr-finding-derivations-a2}
[A2: Drill]

The parts run from one step of the method, through available lines and steps to judge, to short derivations.

::: {.enumerate options="label=(\alph*)"}
1. The goal is \( \neg(P \vee Q) \). What does step 2 set up?
2. The goal is \( (P \to Q) \wedge \neg R \). Which gaps does step 2 leave?
3. The goal is \( \bot \), and the resources are \( \neg(P \wedge Q) \), \( P \), \( Q \). What are the next two lines?
4. The goal is \( P \vee Q \), and the one resource is \( \neg P \to Q \). Which step does the work, and how?
5. In a partial derivation the current goal is line 9, inside the boxes opened at lines 3 and 6. Line 1 is a premise, and lines 4–5 form a box inside box 3 that has closed. Which of lines 1, 3, 4, 6 are resources?
6. Which step of the method opens an \( \rulename{RAA} \) box, and when?
7. True or false: a failed search shows that the sequent is not derivable.
8. The goal is \( R \), and the resources are \( P \vee Q \), \( P \to R \), \( Q \to S \). Should the search be expected to succeed?
9. Lines 3 and 4 are \( Q \to R \) (a premise) and \( Q \). A searcher writes 5 \( Q \), assumption; 6 \( R \), \( \rulename{{\to}E} \) 3, 5; 7 \( Q \to R \), \( \rulename{{\to}I} \) 5–6; 8 \( R \), \( \rulename{{\to}E} \) 7, 4. Which refinements of the section does this break, and what single line replaces lines 5–8?
10. Find a derivation of \( P \vee Q, \ \neg P \vdash Q \vee R \).
11. Find a derivation of \( (P \vee Q) \to R \vdash Q \to R \).
12. Find a derivation of \( P \to (Q \to R), \ P \wedge \neg R \vdash \neg Q \).
:::
:::

::: {.solution}
(a) A box opened with \( P \vee Q \), with the goal \( \bot \).

(b) Two boxes: one on \( P \) with the goal \( Q \), and one on \( R \) with the goal \( \bot \).

(c) \( P \wedge Q \) by \( \rulename{\wedge I} \), then \( \bot \) by \( \rulename{\neg E} \).

(d) Step 2 postpones the goal. Step 3 needs \( \neg P \), which is not a resource, and making it a goal stalls. So step 5: \( \rulename{LEM} \) on \( P \), whose negation the resource waits for.

(e) 1, 3 and 6; not 4.

(f) Step 5, when steps 2–4 give nothing.

(g) False: it shows only that this search failed.

(h) No. \( P \) false, \( Q \) true, \( R \) false, \( S \) true makes every resource true and \( R \) false, so the claim breaks. In \( \rulename{\vee E} \), the case \( Q \) gives only \( S \).

(i) Two refinements. Lines 7–8 are a detour (\( \rulename{{\to}I} \), then \( \rulename{{\to}E} \) on its own implication). Line 7 rebuilds a resource, and *find the goal among the resources* would have cited line 3. Replace lines 5–8 by 5 \( R \), \( \rulename{{\to}E} \) 3, 4.

(j) 3 \( Q \), \( \rulename{DS} \) 1, 2; 4 \( Q \vee R \), \( \rulename{\vee I} \) 3.

(k) 2 \( Q \), assumption, for \( \rulename{{\to}I} \); 3 \( P \vee Q \), \( \rulename{\vee I} \) 2; 4 \( R \), \( \rulename{{\to}E} \) 1, 3; 5 \( Q \to R \), \( \rulename{{\to}I} \) \( \lines{2}{4} \).

(l) 3 \( P \), \( \rulename{\wedge E} \) 2; 4 \( \neg R \), \( \rulename{\wedge E} \) 2; 5 \( Q \to R \), \( \rulename{{\to}E} \) 1, 3; 6 \( \neg Q \), \( \rulename{MT} \) 5, 4.
:::

### B. Practice

::: {#exr-finding-derivations-b1}
[B1: Three searches]

For each sequent, name the first goal-directed step, then find a derivation.

::: {.enumerate options="label=(\alph*)"}
1. \( P \wedge (Q \to R) \vdash (P \to Q) \to R \).
2. \( \neg(P \to Q) \vdash P \wedge \neg Q \). Which conjunct does your derivation obtain by \( \rulename{RAA} \), and which by \( \rulename{\neg I} \) alone?
3. \( \neg P \to Q \vdash P \vee Q \).
:::

*Hint: in (c), look at what the premise is waiting for.*
:::

::: {.solution}
(a) The goal is an implication: a box on \( P \to Q \) with the goal \( R \), a letter. Step 3 splits the premise; its half \( Q \to R \) gives \( R \) once we have \( Q \), and the box's assumption gives \( Q \) once we have \( P \), which the premise's other half supplies. So the chain runs backwards from \( R \) to \( Q \) to \( P \), and forwards it reads:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \to R)}
  \open
  \hypo {2} {P \to Q}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ie{2,3}
  \have {5} {Q \to R} \ae{1}
  \have {6} {R} \ie{5,4}
  \close
  \have {7} {(P \to Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```

(b) The goal is a conjunction: two gaps, with goals \( P \) and \( \neg Q \). The premise can be used only by \( \rulename{\neg E} \), against \( P \to Q \), so in each gap we aim to manufacture \( P \to Q \). The goal \( \neg Q \) is a negation: a box on \( Q \), where \( P \to Q \) follows by a box that repeats \( Q \), and it clashes with the premise. The goal \( P \) is a letter, and the resources give nothing, so step 5: \( \rulename{RAA} \) on \( \neg P \). Then \( P \to Q \) follows by vacuous implication (@prp-vacuous-implication, written VI), and it clashes with the premise. **The conjunct \( P \) is the one our derivation obtains by \( \rulename{RAA} \)**; \( \neg Q \) needs only \( \rulename{\neg I} \). (That no derivation of \( P \) from the premise avoids \( \rulename{RAA} \) is true, but we do not prove it.)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \to Q)}
  \open
  \hypo {2} {\neg P}
  \have {3} {P \to Q} \by{VI}{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {P} \raa{2-4}
  \open
  \hypo {6} {Q}
  \open
  \hypo {7} {P}
  \have {8} {Q} \r{6}
  \close
  \have {9} {P \to Q} \ii{7-8}
  \have {10} {\bot} \ne{9,1}
  \close
  \have {11} {\neg Q} \ni{6-10}
  \have {12} {P \wedge \neg Q} \ai{5,11}
\end{nd}$
\end{center}
```

Written with primitive rules only, line 3 becomes the four lines of a box on \( P \) that clashes with \( \neg P \), writes \( Q \) by \( \rulename{\bot E} \), and closes by \( \rulename{{\to}I} \); the derivation then has 15 lines instead of 12.

(c) The goal is a disjunction, so step 2 postpones it; the premise is waiting for \( \neg P \), which is not a resource, and nothing clashes. Step 5, \( \rulename{LEM} \) on \( P \), the statement the premise is waiting for: in the case \( P \), \( \rulename{\vee I} \) gives the left side; in the case \( \neg P \), the premise gives \( Q \) and \( \rulename{\vee I} \) the right side.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to Q}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {Q} \ie{1,5}
  \have {7} {P \vee Q} \oi{6}
  \close
  \have {8} {P \vee Q} \oe{2,3-4,5-7}
\end{nd}$
\end{center}
```

The derivation has 8 lines. An \( \rulename{RAA} \) box on \( \neg(P \vee Q) \) also works, with two manufactured clashes inside it.
:::

::: {#exr-finding-derivations-b2}
[B2: The last step]

A search for \( P \to Q, \ R \to \neg Q \vdash P \to \neg R \) has reached the stage below; only the last line is missing. *Name the move, then complete it.*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {R \to \neg Q}
  \open
  \hypo {3} {P} \purpose{\ii}
  \have {4} {Q} \ie{1,3}
  \open
  \hypo {5} {R}
  \have {6} {\neg Q} \ie{2,5}
  \have {7} {\bot} \ne{4,6}
  \close
  \have {8} {\neg R} \ni{5-7}
  \close
  \have {9} {\;\textbf{?}} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The move is the chapter's main one: the skeleton was read off the goal, and the gap was filled from both ends. The goal \( P \to \neg R \) is an implication, so the outer box opened with \( P \) (line 3); its new goal \( \neg R \) is a negation, so the inner box opened with \( R \) (line 5). The premises then met the goal in the middle: \( \rulename{{\to}E} \) at lines 4 and 6 gave \( Q \) and \( \neg Q \), and the clash at line 7. The inner box was closed at line 8. What remains is to close the outer box on its goal, by \( \rulename{{\to}I}\ \lines{3}{8} \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {R \to \neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \open
  \hypo {5} {R}
  \have {6} {\neg Q} \ie{2,5}
  \have {7} {\bot} \ne{4,6}
  \close
  \have {8} {\neg R} \ni{5-7}
  \close
  \have {9} {P \to \neg R} \ii{3-8}
\end{nd}$
\end{center}
```

The box runs from its assumption \( P \), line 3, to its last line \( \neg R \), line 8, which lies in the outer box itself and not in the inner one, as \( \rulename{{\to}I} \) requires.
:::

::: {#exr-finding-derivations-b3}
[B3: Two boxes and a chain]

Find a derivation of \( P \to (Q \to R), \ P \to (R \to S) \vdash P \to (Q \to S) \), and describe the search in three sentences, naming its goal-directed and premise-directed steps.
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {P \to (R \to S)}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \ie{1,3}
  \have {5} {R \to S} \ie{2,3}
  \open
  \hypo {6} {Q}
  \have {7} {R} \ie{4,6}
  \have {8} {S} \ie{5,7}
  \close
  \have {9} {Q \to S} \ii{6-8}
  \close
  \have {10} {P \to (Q \to S)} \ii{3-9}
\end{nd}$
\end{center}
```

The search: the goal is an implication, so a goal-directed step opens a box on \( P \) with the goal \( Q \to S \), and a second goal-directed step opens a box on \( Q \) with the goal \( S \). With \( P \) a resource, premise-directed steps fire both premises by \( \rulename{{\to}E} \), giving \( Q \to R \) and \( R \to S \). Then a backward chain from the goal \( S \) (it needs \( R \), which needs \( Q \), a resource) is written forwards as two more \( \rulename{{\to}E} \) lines, and the two boxes close in the reverse order of opening. (Lines 4 and 5 may equally be written inside the box of \( Q \).)
:::

::: {#exr-finding-derivations-b4}
[B4: Cut the detours]

The derivation below of \( P \wedge Q, \ Q \to R \vdash R \wedge P \) is correct but contains detours.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {Q \to R}
  \have {3} {Q} \ae{1}
  \open
  \hypo {4} {Q}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {Q \to R} \ii{4-5}
  \have {7} {R} \ie{6,3}
  \have {8} {P} \ae{1}
  \have {9} {R \wedge P} \ai{7,8}
  \have {10} {R} \ae{9}
  \have {11} {R \wedge P} \ai{10,8}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Find each pair of lines in which a line is built by an introduction rule and taken apart at once by the matching elimination.
2. Which line rebuilds a premise?
3. Rewrite the derivation without the detours.
4. To cut the \( \rulename{{\to}I} \)/\( \rulename{{\to}E} \) detour, the box is copied with a line in place of its assumption: which line, and what does the copy give?
:::
:::

::: {.solution}
(a) Lines 6–7: \( \rulename{{\to}I} \), then \( \rulename{{\to}E} \) on line 6. Lines 9–10: \( \rulename{\wedge I} \), then \( \rulename{\wedge E} \) on line 9. (Line 11 then rebuilds line 9.)

(b) Line 6 is premise 2, rebuilt by a box. *Find the goal among the resources* would have cited line 2.

(c) Six lines instead of eleven:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {Q \to R}
  \have {3} {Q} \ae{1}
  \have {4} {R} \ie{2,3}
  \have {5} {P} \ae{1}
  \have {6} {R \wedge P} \ai{4,5}
\end{nd}$
\end{center}
```

(d) Line 3 takes the place of the assumption on line 4. The box's one other line, "\( R \), \( \rulename{{\to}E} \) 2, 4", becomes "\( R \), \( \rulename{{\to}E} \) 2, 3", which is line 4 of (c).
:::

### C. Going deeper

::: {#exr-finding-derivations-c1}
[C1: The second half]

A search for \( P \vee (Q \wedge R) \vdash (P \vee Q) \wedge (P \vee R) \) has used the premise by \( \rulename{\vee E} \) and finished the first case; the second case is blank. *Name the move, then complete it.*

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \vee (Q \wedge R)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {P \vee R} \oi{2}
  \have {5} {(P \vee Q) \wedge (P \vee R)} \ai{3,4}
  \close
  \open
  \hypo {6} {Q \wedge R}
  \have {} {\vdots}
  \have {11} {(P \vee Q) \wedge (P \vee R)}
  \close
  \have {12} {(P \vee Q) \wedge (P \vee R)} \oe{1,2-5,6-11}
\end{nd}$
\end{center}
```
:::

::: {.solution}
[Hint 1]

The current goal of the blank box is a conjunction. What does step 2 do with it, and what does step 3 do with the box's assumption?
:::

::: {.solution}
[Hint 2]

Line 7 is \( Q \), by \( \rulename{\wedge E} \) from line 6.
:::

::: {.solution}
The move is the chapter's main one again: read the skeleton off the goal, then work from both ends. The current goal \( (P \vee Q) \wedge (P \vee R) \) is a conjunction, so step 2 splits it into the goals \( P \vee Q \) and \( P \vee R \), to be joined by \( \rulename{\wedge I} \). Both are disjunctions, so they are postponed, and step 3 turns to the resource \( Q \wedge R \): \( \rulename{\wedge E} \) gives \( Q \) and \( R \). Now each disjunction has a side that is a resource, so \( \rulename{\vee I} \) is safe.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \wedge R)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {P \vee R} \oi{2}
  \have {5} {(P \vee Q) \wedge (P \vee R)} \ai{3,4}
  \close
  \open
  \hypo {6} {Q \wedge R}
  \have {7} {Q} \ae{6}
  \have {8} {R} \ae{6}
  \have {9} {P \vee Q} \oi{7}
  \have {10} {P \vee R} \oi{8}
  \have {11} {(P \vee Q) \wedge (P \vee R)} \ai{9,10}
  \close
  \have {12} {(P \vee Q) \wedge (P \vee R)} \oe{1,2-5,6-11}
\end{nd}$
\end{center}
```

Both boxes end in the current goal of the \( \rulename{\vee E} \), as that rule requires. Here \( \rulename{\vee I} \) adds \( P \) on the left of \( Q \) and of \( R \); in the first case it added \( Q \) and \( R \) on the right of \( P \). Citing line 2 inside the second box would be the sibling-box error of @exr-reductio-and-classical-rules-c2.
:::

::: {#exr-finding-derivations-c2}
[C2: A disjunction from nothing]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \vdash (P \to Q) \vee (Q \to P) \).
2. In a paragraph, say which step of your derivation uses \( \rulename{RAA} \) or \( \rulename{LEM} \), and why the method cannot avoid step 5 on this goal.
:::
:::

::: {.solution}
[Hint 1]

The goal is a disjunction and there are no premises. Which steps of the method does that leave?
:::

::: {.solution}
[Hint 2]

Step 5 has two forms. Which statement would make each side of the goal easy, if you knew whether it held?
:::

::: {.solution}
(a) \( \rulename{LEM} \) on \( Q \). In the case \( Q \), the implication \( P \to Q \) holds by a box that repeats \( Q \). In the case \( \neg Q \), the implication \( Q \to P \) holds by a box on \( Q \) that clashes with \( \neg Q \), followed by \( \rulename{\bot E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {Q \vee \neg Q} \lem{}
  \open
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \r{2}
  \close
  \have {5} {P \to Q} \ii{3-4}
  \have {6} {(P \to Q) \vee (Q \to P)} \oi{5}
  \close
  \open
  \hypo {7} {\neg Q}
  \open
  \hypo {8} {Q}
  \have {9} {\bot} \ne{8,7}
  \have {10} {P} \be{9}
  \close
  \have {11} {Q \to P} \ii{8-10}
  \have {12} {(P \to Q) \vee (Q \to P)} \oi{11}
  \close
  \have {13} {(P \to Q) \vee (Q \to P)} \oe{1,2-6,7-12}
\end{nd}$
\end{center}
```

\( \rulename{LEM} \) on \( P \) works equally well, with the roles of the two sides exchanged.

(b) \( \rulename{LEM} \) is used at line 1; \( \rulename{RAA} \) appears only inside the derivation of \( \rulename{LEM} \) (@prp-excluded-middle) that line 1 abbreviates. The method cannot avoid step 5 here. Step 2 postpones the \( \vee \) goal; with no premises, step 3 has nothing to eliminate and step 4 nothing to clash; and \( \rulename{\vee I} \) cannot come first, because neither side follows from no premises (with \( P \) true and \( Q \) false, \( P \to Q \) is false; with \( P \) false and \( Q \) true, \( Q \to P \) is false; Chapter 4 turns such choices into proofs). So a resource must be created from nothing, and only step 5 does that. This shows that the **method** needs step 5; that every derivation of the sequent uses \( \rulename{RAA} \) or an equivalent is a stronger claim, which we do not prove.

**Marking scheme.** (10 points)

- 3: a correct split by \( \rulename{LEM} \) (on \( Q \) or on \( P \)), with two case boxes combined by \( \rulename{\vee E} \), or a correct \( \rulename{RAA} \) box on the negated goal.
- 2: in one case, the implication by a box that repeats the case assumption.
- 2: in the other case, the implication by a box that clashes with the case assumption, then \( \rulename{\bot E} \), or by VI (@prp-vacuous-implication).
- 1: \( \rulename{\vee I} \) on the correct side in each case, every citation available.
- 2: the paragraph names the \( \rulename{LEM} \) line (or the \( \rulename{RAA} \) line) and explains why no other step of the method applies.

Fatal errors (0 for the step): choosing a side of the goal before the split; citing one case's assumption in the other case.
A correct derivation by \( \rulename{RAA} \) on the negated goal earns full marks: its 2 + 2 + 1 points go to the two implications derived inside the \( \rulename{RAA} \) box (one by a box that repeats an assumption, one by a clash and \( \rulename{\bot E} \), or by VI (@prp-vacuous-implication) once \( \neg Q \) or \( \neg P \) has been derived) and to the \( \rulename{\vee I} \) lines that clash with the \( \rulename{RAA} \) assumption.
:::

::: {#exr-finding-derivations-c3}
[C3: Exit check: search]

Find a derivation of \( \neg(\neg P \wedge Q) \vdash P \vee \neg Q \) by the method of this section. Write one sentence for each step of the method you take, and point to the classical step of your derivation.
:::

::: {.solution}
*The search.*

1. *Step 1.* The premise \( \neg(\neg P \wedge Q) \) on top, the goal \( P \vee \neg Q \) at the bottom, one gap.
2. *Step 2.* The goal is a disjunction, so it is postponed: the premise does not say which side holds.
3. *Step 3.* Nothing can be eliminated. The premise is a negation, so it can be used only in a clash (step 4), against \( \neg P \wedge Q \), and we do not have it.
4. *Step 4.* The goal is not \( \bot \), and nothing clashes. We are stuck.
5. *Step 5.* We assume the negation of the goal, \( \neg(P \vee \neg Q) \), with the new goal \( \bot \).
6. *Step 4, inside the box.* The new assumption clashes with \( P \vee \neg Q \), which \( \rulename{\vee I} \) builds from either side. The side \( P \) is a letter that nothing gives; the side \( \neg Q \) is a negation, which step 2 can build. So \( \neg Q \) becomes the goal: a box on \( Q \), with the goal \( \bot \). Choosing a side is safe here, since the disjunction is manufactured for a clash with a resource that is its negation (step 4 allows either side when the disjunction is built for a clash with its own negation).
7. *Step 4, in the box on \( Q \).* The resources are the premise, the assumption of step 5, and \( Q \). We aim at the premise: \( \neg P \wedge Q \) becomes the goal, and step 2 splits it. Its half \( Q \) is a resource; its half \( \neg P \) is a negation: a box on \( P \), with the goal \( \bot \).
8. *Step 4, in the box on \( P \).* \( \rulename{\vee I} \) builds \( P \vee \neg Q \) from \( P \), which clashes with the assumption of step 5. Now the boxes close from the inside out: \( \neg P \), then \( \neg P \wedge Q \), which clashes with the premise; then \( \neg Q \), then \( P \vee \neg Q \), which clashes with the assumption of step 5; and \( \rulename{RAA} \) closes the outer box.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge Q)}
  \open
  \hypo {2} {\neg (P \vee \neg Q)}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {P \vee \neg Q} \oi{4}
  \have {6} {\bot} \ne{5,2}
  \close
  \have {7} {\neg P} \ni{4-6}
  \have {8} {\neg P \wedge Q} \ai{7,3}
  \have {9} {\bot} \ne{8,1}
  \close
  \have {10} {\neg Q} \ni{3-9}
  \have {11} {P \vee \neg Q} \oi{10}
  \have {12} {\bot} \ne{11,2}
  \close
  \have {13} {P \vee \neg Q} \raa{2-12}
\end{nd}$
\end{center}
```

The classical step is line 13, the \( \rulename{RAA} \) that closes the box of line 2; every other box closes by \( \rulename{\neg I} \). The assumption of line 2 is used twice, at lines 6 and 12, just as in @exm-search-raa.

*A second route.* Step 5 may take its other form: \( \rulename{LEM} \) on \( P \). In the case \( P \), \( \rulename{\vee I} \) gives the goal. In the case \( \neg P \), the goal's side \( \neg Q \) is a negation: a box on \( Q \) builds \( \neg P \wedge Q \), which clashes with the premise, so \( \neg Q \), and \( \rulename{\vee I} \). That derivation has 11 lines, and its classical step is the \( \rulename{LEM} \) line.

**Marking scheme.** (10 points)

- 2: step 2 postpones the disjunctive goal, with the reason (neither side is in hand).
- 2: steps 3 and 4 find that the premise can be used only by producing \( \neg P \wedge Q \) for a clash.
- 2: step 5 is chosen: \( \rulename{RAA} \) on the whole goal, or \( \rulename{LEM} \) on \( P \). (\( \rulename{LEM} \) on \( Q \) also works; our route with it then uses a second classical step, an \( \rulename{RAA} \) for \( P \) in the case \( Q \); award it.) A classical derived rule used at step 3, such as DM (d) on the premise followed by \( \rulename{\neg\neg E} \), is also accepted; its line is the classical line.
- 3: the inner boxes and their clashes are correct, and every citation is available.
- 1: the classical line is named.

Fatal errors (0 for the step): \( \rulename{\vee I} \) as the last line, from a disjunct derived from the premise alone; on the \( \rulename{RAA} \) route, an \( \rulename{RAA} \) box on the whole goal opened with anything but \( \neg(P \vee \neg Q) \).
:::

::: {#exr-finding-derivations-c4}
[C4: Two sequents that look alike]

Derive each sequent, and say which of your two derivations needed the classical rule.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg(P \wedge Q), \ P \vdash \neg Q \).
2. \( \neg(P \wedge \neg Q), \ P \vdash Q \).
:::

Then explain why, in (b), the natural \( \rulename{\neg I} \) box on \( \neg Q \) ends at \( \neg\neg Q \) and not at \( Q \).
:::

::: {.solution}
(a) The goal is a negation: a \( \rulename{\neg I} \) box on \( Q \), in which \( P \wedge Q \) clashes with the first premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg Q} \ni{3-5}
\end{nd}$
\end{center}
```

(b) The goal \( Q \) is a letter, and the resources give nothing directly, so step 5: \( \rulename{RAA} \), a box on \( \neg Q \), in which \( P \wedge \neg Q \) clashes with the first premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge \neg Q)}
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {P \wedge \neg Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {Q} \raa{3-5}
\end{nd}$
\end{center}
```

The derivation of (b) needed the classical rule, at line 6; the derivation of (a) did not. The two have the same shape, and the difference is the goal. In (a) it is a negation, which \( \rulename{\neg I} \) builds. In (b) it is a letter, and the box that reaches \( \bot \) opens with \( \neg Q \); \( \rulename{\neg I} \) writes the negation of a box's assumption, so closing that box by \( \rulename{\neg I} \) gives \( \neg\neg Q \), and our derivation reaches \( Q \) with the classical rule instead: \( \rulename{RAA} \) in place of \( \rulename{\neg I} \) (or \( \rulename{\neg\neg E} \) after it).
:::

<!-- dependency ledger
finding-derivations-method (claim): the goal-directed steps and step 5 never turn a derivable gap into an underivable one | inline (argued in fold "Why the order loses nothing" from def-derivable and one appended elimination step; LEM split by adding a premise)
finding-derivations-method (claim): P or Q |- Q or P is derivable but neither disjunct follows from P or Q alone | derivability: @exm-disjunction-first-derivations; "does not follow": a breaking choice (P true, Q false) on the page; no claim of non-derivability
finding-derivations-chart (claim): following the chart writes no illegal line; a move whose gap repeats an open gap is skipped | inline (each action is a step of the method); termination not claimed in the text
def-partial-derivation (example): filling a gap adds lines only above its current goal, so an open box at the bottom cannot be repaired | inline (from the definition)
exm-search-postpone-or (example): neither disjunct follows from the premise (two breaking choices) | informal, by the choices on the page; no claim of non-derivability
exm-search-postpone-or (example): LEM on P also succeeds, with a nested or-E, in 22 lines | inline description, in fold "Other splits that also work"; not used
exm-search-raa (example): LEM on P leaves the method stuck again in the case not-P | inline (steps 2-4 read off the resources), in fold "Other splits that also work"; not used
finding-derivations-peirce (example): assuming not-Q at the stalled gap of Peirce's search gives no clash | inline (the resources listed), in fold "Step 5 one level out"; not used
exm-search-free-lines (example): lines outside the boxes are available inside them | inline (scope rule of @def-derivation)
finding-derivations-detours (claim): a detour's line was within reach without it | inline (copying argument in fold "Why a detour's line was within reach", from @def-derivation's scope rule); stated as advice, no normalization theorem
finding-derivations-failed-search (claim): no derivation of Q -> P from P -> Q exists | not claimed; the paragraph says only that the form breaks and that "no derivation" cannot yet be shown
exm-skeleton-odd-product (example): every integer is even or odd, and not both | F2.2 (promised; thm-division-algorithm, the case n = 2)
exm-skeleton-odd-product (example): m = 2k gives mn = 2(kn) | school algebra
exm-skeleton-odd-product (example): "say m = 2k" names a witness | F1.4 (promised; rules for "there exists"), carried by the chapter index's quantifier note
exr-finding-derivations-a1 (solution): (b) naming n uses a rule for "there exists" | F1.4 (promised), carried by the chapter index's quantifier note
exr-finding-derivations-a1 (solution): (a) not(x < 0) iff x >= 0; x >= 0 implies x^3 >= 0 | school algebra, AN1.1 (promised)
exr-finding-derivations-a2 (solution): (h) the resources are true and R false at P false, Q true, R false, S true | inline (the choice given)
exr-finding-derivations-b1 (solution): no derivation of P from not(P -> Q) avoids RAA | stated without proof and marked so; nothing depends on it
exr-finding-derivations-c2 (solution): neither disjunct follows from no premises (breaking choices) | informal; plain pointer to Chapter 4; the solution says it proves only that the method needs step 5
exr-finding-derivations-c3 (solution): the LEM-on-P route is 11 lines; our route by LEM on Q uses a second classical step in the case Q | inline description (the route is given in words); the second is a remark in the marking scheme about a route, not claimed as a necessity
-->
