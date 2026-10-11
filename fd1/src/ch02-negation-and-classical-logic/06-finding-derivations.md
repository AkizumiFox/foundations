# How to Find a Derivation

We now have every rule for the connectives. Checking a derivation is mechanical, as @def-derivation makes it: for each line, which rule, which lines, and are they available. Finding one is not, since an assumption may be any statement at all. Yet every Idea in Chapters 1 and 2 found its derivation with the same handful of moves. This section introduces no new rule. It collects those moves into one method, puts them in order, says why the order is right, and then watches the method work: on four searches that succeed, one that fails, and one mathematical goal. It ends with every rule in one place.

## The moves so far

Each section since Section 1.3 has added a move, either to the list read off the **goal** (goal-directed: which introduction rule builds the goal's main connective?) or to the list read off the **premises** (premise-directed: which elimination rule uses an available line's main connective?). Here they are together, with the section where each first appeared.

| The situation | The move | First met |
|---|---|---|
| goal \( \varphi \wedge \psi \) | two subgoals, \( \varphi \) and \( \psi \), joined by \( \rulename{\wedge I} \) | Section 1.3 |
| resource \( \varphi \wedge \psi \) | take it apart by \( \rulename{\wedge E} \) | Section 1.3 |
| resource \( \varphi \to \psi \) | fire it on \( \varphi \) by \( \rulename{{\to}E} \); if \( \varphi \) is missing, make it a subgoal | Section 1.4 |
| goal \( \varphi \to \psi \) | a box opened with \( \varphi \), with the new goal \( \psi \) | Section 1.5 |
| goal \( \varphi \vee \psi \) | postpone; choose a side only when it is in hand | Section 1.6 |
| resource \( \varphi \vee \psi \) | two cases, each ending in the current goal | Section 1.7 |
| goal \( \bot \) | find a clash, or manufacture one; an impossible case closes itself by \( \rulename{\bot E} \) | Section 2.1 |
| goal \( \neg\varphi \) | a box opened with \( \varphi \), with the new goal \( \bot \) | Section 2.2 |
| a pattern with a name | use the derived rule as one line (\( \rulename{MT} \), \( \rulename{DS} \), …) | Section 2.3 |
| goal \( \varphi \leftrightarrow \psi \) | two boxes, one for each direction | Section 2.4 |
| stuck | assume the negation of the goal (\( \rulename{RAA} \)), or split on \( \chi \vee \neg\chi \) (\( \rulename{LEM} \)) | Section 2.5 |

Eleven moves is a lot to hold in mind at a blank page. The method below turns them into an order of attack. To state it we need a name for a derivation that is only half written.

## Partial derivations

A search builds a derivation from the outside in: the last line first, then the boxes the goal asks for, then the lines in between. What exists halfway is not yet a derivation, but it is close to one.

::: {#def-partial-derivation}
[Partial Derivation]

A **partial derivation** is a list of lines laid out as a derivation (@def-derivation), except that some stretches of lines are still missing. Each missing stretch is a **gap**, drawn as a row \( \vdots \). The line just below a gap is its **current goal**; it is already written, but it has no justification yet, since the lines of the gap are to supply one. The lines available at the current goal, in the sense of @def-derivation, are the gap's **resources**.
:::

In words: every line that has been written is a premise, an assumption, a current goal, or a line justified by a rule from lines and boxes available to it; the boxes are nested and closed as in any derivation; only the gaps are missing. A search starts with a single gap, below the premises and above the conclusion, and each step replaces a gap by lines, boxes, and smaller gaps. It ends when no gap is left, and then the partial derivation is a derivation.

The **degenerate** partial derivation is the starting point of every search: the premises, one gap, and the goal. Its resources are the premises. The snapshots in the worked searches below are all partial derivations; a line carries the number it will have in the finished derivation, so that snapshots can be compared, and a line whose place is not yet fixed carries no number. On paper you would number the lines at the end.

**Nonexample.** Take a snapshot and leave one of its boxes open at the bottom, so that the conclusion sits inside the box. That is not a partial derivation, even though every line is correct so far: @def-derivation asks that every box close and that the last line lie outside every box, and a gap cannot repair that, since filling a gap adds lines only above its current goal.

::: {.check}
In the second snapshot of @exm-search-distribute below, the second gap has the current goal \( \bot \) on line 11. List its resources.
:::

::: {.solution}
Lines 1, 7, 8, and 9: the premise \( P \to \neg Q \), the line \( \neg(P \wedge Q) \), and the assumptions \( Q \) and \( P \) of the two boxes that contain the gap. Line 7 lies in no box and above the gap, so it is available, though this gap will not need it. Lines 2–6 are not resources: they lie in a box that has closed.
:::

## The method

*Work from both ends: let the goal choose the boxes, let the premises choose the eliminations, and meet in the middle.*

::: {.algorithm}
**Searching for a derivation of \( \Gamma \vdash \varphi \).**

1. **Set up.** Write the premises \( \Gamma \) at the top and \( \varphi \) at the bottom, with one gap between.
2. **Goal-directed step.** Take the main connective of the current goal (@def-main-connective) and set up its introduction rule:
   - \( \psi \wedge \chi \): two gaps, with goals \( \psi \) and \( \chi \) (Section 1.3);
   - \( \psi \to \chi \): a box opened with \( \psi \); inside it, the new goal is \( \chi \) (Section 1.5);
   - \( \neg\psi \): a box opened with \( \psi \); inside it, the new goal is \( \bot \) (Section 2.2);
   - \( \psi \leftrightarrow \chi \): two boxes, one from \( \psi \) to \( \chi \) and one from \( \chi \) to \( \psi \) (Section 2.4);
   - \( \psi \vee \chi \): **postpone**; do not choose a side yet (Section 1.6), unless the disjunction is being manufactured for a clash with its own negation (step 4), when either side may be chosen (see below).

   Repeat while the current goal is a \( \wedge \), \( \to \), \( \neg \), or \( \leftrightarrow \).
3. **Premise-directed step.** Take the main connective of a resource and apply its elimination rule: \( \rulename{\wedge E} \) freely (Section 1.3); \( \rulename{{\to}E} \) and \( \rulename{{\leftrightarrow}E} \) when the other statement they need is a resource, or can be made a new goal (Sections 1.4 and 2.4); \( \rulename{\vee E} \) by opening two boxes, one per disjunct, **each ending in the current goal** (Section 1.7). A derived rule may do the work of several lines (Section 2.3): a resource \( \psi \to \chi \) with \( \neg\chi \) available gives \( \neg\psi \) by \( \rulename{MT} \); a resource \( \psi \vee \chi \) with \( \neg\psi \) available gives \( \chi \) by \( \rulename{DS} \).
4. **Clash.** If the current goal is \( \bot \), look for a pair \( \chi \), \( \neg\chi \) among the resources, or make \( \chi \) the new goal for some resource \( \neg\chi \) and manufacture it, starting again at step 2 for that goal. Whatever the current goal, if the resources clash, write \( \bot \) and then the goal by \( \rulename{\bot E} \): an impossible case closes itself (Section 2.1).
5. **Stuck.** Use \( \rulename{RAA} \): open a box with the negation of the current goal, whose new goal is \( \bot \); if that gives nothing, try the same with a goal further out whose box contains the stalled gap. Or use \( \rulename{LEM} \) on a well-chosen statement \( \chi \), and split on \( \chi \vee \neg\chi \) by \( \rulename{\vee E} \). Then return to step 3 (Section 2.5).

When no gap is left, number the lines and check the derivation as @def-derivation says.
:::

The steps are listed in the order in which to try them, and the order has reasons.

**The goal-directed steps lose nothing.** Suppose the goal \( \psi \to \chi \) is derivable from the resources \( \Gamma \) at all, by some derivation \( D \). Then \( \chi \) is derivable from \( \Gamma \) together with \( \psi \): add \( \psi \) to the premises of \( D \) (@def-derivable asks only that the premises belong to the list), and append the line \( \chi \) by \( \rulename{{\to}E} \), citing the last line of \( D \) and the premise \( \psi \). So opening a box on \( \psi \) never turns a derivable gap into an underivable one. With \( \rulename{\wedge E} \), \( \rulename{\neg E} \), or \( \rulename{{\leftrightarrow}E} \) as the appended line, the same argument covers \( \wedge \), \( \neg \), and \( \leftrightarrow \). That is why step 2 may be applied without thinking.

**Choosing a side of \( \vee \) can lose everything.** A disjunction can be derivable when neither side is. From \( P \vee Q \) the goal \( Q \vee P \) is derivable (@exm-disjunction-first-derivations), but \( P \vee Q \) does not say which side holds, so a last line \( \rulename{\vee I} \) from \( Q \), or from \( P \), leaves a gap that cannot be filled (Chapter 3 makes "cannot" exact, @cor-refuting-row). Choosing a side is safe only once the resources decide it, typically inside a case of \( \rulename{\vee E} \), or when the disjunction is being manufactured for a clash (step 4) with a resource that is its negation: then the resources derive \( \bot \) as soon as they derive the disjunction, and from \( \bot \) every statement, either side included, by \( \rulename{\bot E} \).

**Step 5 also loses nothing, and still comes last.** If \( \varphi \) is derivable from the resources, then \( \bot \) is derivable from them together with \( \neg\varphi \), by one appended \( \rulename{\neg E} \); so an \( \rulename{RAA} \) box is always safe. A split on \( \chi \vee \neg\chi \) is safe too, since each case only adds a resource. Step 5 comes last because the goal \( \bot \) gives step 2 nothing to work with, because a good \( \chi \) must be chosen, and because a derivation that did not need the classical step reads worse with it (the costume of Section 2.5).

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

*Steps 3 and 4, second gap.* The resources are lines 1, 7, 8, and 9, and line 7 is not needed. \( \rulename{{\to}E} \) on lines 1 and 9 gives \( \neg Q \), which clashes with line 8. Both gaps close:

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

Notice how little thinking the search needed. Step 2 is mechanical, and it did most of the work: by the time the premise was consulted, each gap was small, with the goal \( \bot \) and two or three resources. That is the typical shape of a successful search: **the goal fixes the skeleton, and the premises fill in the flesh.**

## Cases must end in the goal

When the goal gives nothing, the premises must. The next search is driven by a disjunction among the premises.

::: {#exm-search-cases}
[Proof by cases, found by the method]

Find a derivation of \( P \vee Q, \ P \to R, \ Q \to R \vdash R \).
:::

::: {.solution}
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

This is the pattern that Section 1.7 called the skeleton of almost every proof by cases (compare @exm-cases-on-hypothesis, which packages the same two boxes into one implication). The method found it without being told.

*Why the boxes end in the current goal.* \( \rulename{\vee E} \) (@def-rules-disjunction) gives, after the two boxes, their common last line and nothing else. A box that ends in anything but the current goal leaves that goal still to be reached, and two boxes that end in different statements cannot be combined at all. The word **current** matters: had the goal been \( S \to R \), step 2 would first open a box on \( S \), the current goal inside it would be \( R \), and the two case boxes, opened inside the box of \( S \), would end in \( R \), not in \( S \to R \).
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
  \hypo {2} {P}
  \have {3} {Q \vee R} \ie{1,2}
  \open
  \hypo {4} {Q}
  \close
  \open
  \hypo {5} {R}
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

In the case \( R \) the resources are \( P \to (Q \vee R) \), \( P \), \( Q \vee R \), and \( R \), and none of them yields \( Q \): no resource has \( Q \) as a conclusion except \( Q \vee R \), which is already split, and nothing clashes. Choosing the right side instead fails in the mirror image, in the case \( Q \). In fact neither side follows from the premise alone: with \( P \) and \( Q \) true and \( R \) false the premise is true and \( P \to R \) is false, and with \( P \) and \( R \) true and \( Q \) false the premise is true and \( P \to Q \) is false. (Chapter 3 turns such rows into proofs that no derivation exists: @cor-refuting-row.)

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

*What the method did.* Step 2 postponed the goal, the tempting start broke that rule, and its dead end showed both why the rule exists and what to do instead. Line 5 repeats line 3 because \( \rulename{{\to}I} \) needs \( Q \) as a line of the box of line 4 itself. \( \rulename{LEM} \) on \( P \), the first split one thinks of, also succeeds, but less well: in the case \( P \) the premise gives \( Q \vee R \), and a second \( \rulename{\vee E} \), with two more implication boxes, is needed inside it; the finished derivation has 22 lines against these 14.
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
*Steps 1–4.* The goal is a disjunction, so step 2 postpones it. The one resource is a negation, and a negation can be used only in a clash (step 4), which needs the goal \( \bot \); the goal is \( P \vee Q \). Neither side is in hand: the premise says only that \( P \) and \( Q \) differ, not which one holds. Steps 2–4 have nothing to offer.

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

*What the method did.* Step 5 came first, because nothing else applied, and after it steps 2 and 4 did the rest: step 4 chose which clash to aim for, step 2 read the two boxes off \( P \leftrightarrow Q \), and step 4 closed each box with a manufactured clash and \( \rulename{\bot E} \). In words: *suppose neither \( P \) nor \( Q \) holds; then each of them implies the other, since neither can hold at all; so \( P \leftrightarrow Q \), against the premise.* The assumption of line 2 is used twice, at lines 5 and 9. A split by \( \rulename{LEM} \) on \( P \) also works, but less well: in the case \( \neg P \) the goal side \( Q \) is a letter that the resources do not give, and the search is stuck there a second time.
:::

The derivation of Peirce's law in Section 2.5 (@prp-peirce) was found by the same method, and it adds one detail to step 5. There, step 2 opened a box with the goal \( P \), step 3 made \( P \to Q \) a subgoal, step 2 opened a box on \( P \) with the goal \( Q \), and the search stalled at \( Q \). Assuming \( \neg Q \) at the stalled gap gives nothing new: a clash with \( \neg Q \) needs \( Q \), the stalled goal itself. Assuming \( \neg P \) one level out does, because the new resource \( \neg P \) is available in every gap inside its box, including the stalled one. That is why step 5 says to try a goal further out when the current one gives nothing.

## A search that fails

The method is not a machine that always succeeds. Here it fails, and the failure is instructive.

Try \( P \to Q \vdash Q \to P \). Step 2 opens a box on \( Q \) with the goal \( P \):

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {Q}
  \have {} {\vdots}
  \have {} {P}
  \close
  \have {} {Q \to P} \ii{}
\end{nd}$
\end{center}
```

The goal \( P \) is a letter. Step 3: \( \rulename{{\to}E} \) on line 1 needs \( P \), the goal itself. Step 4: nothing clashes, and there is no negation among the resources to aim at. Step 5, \( \rulename{RAA} \): assume \( \neg P \); the only negation among the resources is now \( \neg P \), and a clash with it needs \( P \), the goal again. \( \rulename{LEM} \) on \( P \): the case \( \neg P \) needs \( P \) again. \( \rulename{LEM} \) on \( Q \): the case \( \neg Q \) clashes with line 2, and the case \( Q \) is where we started. Step 5 at the goal further out, an \( \rulename{RAA} \) box on \( \neg(Q \to P) \) around the whole search: a clash with it needs \( Q \to P \), the goal again, and step 2 opens the same box on \( Q \) with the same goal \( P \). Every route returns to one gap, "\( P \) from \( P \to Q \) and \( Q \)". That is affirming the consequent (Section 1.4), the step that would repair Argument B.

But notice what we have **not** shown. A search that fails proves nothing about derivations in general. An assumption may be any statement at all, by the assumption clause of @def-derivation, so there are infinitely many derivations to consider, and a cleverer one might exist. To show that **no** derivation of \( Q \to P \) from \( P \to Q \) exists, we need a different tool.

That is the question this chapter leaves open. *We show that something is derivable by exhibiting a derivation; how could we ever show that something is not?* Chapter 3 answers it (@cor-refuting-row). It gives each statement a truth value and proves that the rules never lead from true premises to a false conclusion; the assignment with \( P \) false and \( Q \) true, which makes \( P \to Q \) true and \( Q \to P \) false, then settles this search for good.

## A mathematical goal

The method reads the frame of a proof off the goal whether the statements are letters or facts about numbers. In ordinary mathematics its payoff is that the first and last sentences of a proof, and its division into parts, are fixed before any mathematics is done.

::: {#exm-skeleton-odd-product}
[Building a skeleton]

Let \( m \) and \( n \) be integers. Prove that if \( mn \) is odd, then \( m \) is odd and \( n \) is odd.
:::

::: {.solution}
*The skeleton.* The main connective is "if … then", so step 2 opens a \( \rulename{{\to}I} \) box: "Assume \( mn \) is odd. … Hence \( m \) is odd and \( n \) is odd." The new goal is a conjunction, so step 2 again: two separate proofs, one that \( m \) is odd and one that \( n \) is odd. Each is a letter as far as logic can see, and the one resource, "\( mn \) is odd", cannot be taken apart. So step 3 brings in facts we can compute with: "if \( m \) is even then \( mn \) is even" is one, and \( \rulename{CP} \) (@prp-contrapositive) turns it into "if \( mn \) is not even then \( m \) is not even", which the resource can feed. Then "every integer is even or odd" and \( \rulename{DS} \) finish.

*The proof.* Assume \( mn \) is odd. We show that \( m \) is odd and that \( n \) is odd.

First, if \( m \) is even, say \( m = 2k \) with \( k \) an integer, then \( mn = 2(kn) \) is even. By the contrapositive (@prp-contrapositive), if \( mn \) is not even, then \( m \) is not even. Now \( mn \) is odd, so it is not even, since no integer is both; hence \( m \) is not even. Since every integer is even or odd, \( m \) is odd, by @prp-disjunctive-syllogism.

Exchanging the roles of \( m \) and \( n \) in the previous paragraph shows that \( n \) is odd. Hence \( m \) and \( n \) are both odd.

*What the method did.* It fixed the first sentence, the two paragraphs, and the last sentence; the only computation is \( mn = 2(kn) \). No step uses \( \rulename{RAA} \): the classical-looking move from "\( m \) is not even" to "\( m \) is odd" is disjunctive syllogism on the fact that every integer is even or odd. (The phrase "say \( m = 2k \)" names a witness, which is a rule for "there exists" from Chapter 4.)
:::

::: {.warning}
**Do not assume what you want to prove.** To derive a goal \( \varphi \), it is tempting to open a box with \( \varphi \). The box reaches \( \varphi \) at once, but after it closes it gives \( \varphi \to \varphi \), not \( \varphi \), and its assumption is gone. An assumption is useful when the goal asks for it: the hypothesis of an implication (step 2), the negated goal of \( \rulename{RAA} \) (step 5), a disjunct of a resource (step 3). Opening the box on the conclusion of an implication is the converse error of Argument B in Section 1.1.
:::

## The rules in one place

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

**Derived rules.** Each is a proved sequent, used as one line that cites the lines holding its premises (@def-derived-rule). The table lists every sequent that Chapters 1 and 2 name as a rule or use as one; every other sequent proved in the text may be used in the same way. Where a rule has no short name, the justification names the result, as "(ex falso)" or "VI".

| In a justification | Sequent | Proved in | Our derivation uses \( \rulename{RAA} \) |
|---|---|---|---|
| (and commutes) | \( P \wedge Q \vdash Q \wedge P \) | @prp-and-commutes | no |
| (implication is transitive) | \( P \to Q, \ Q \to R \vdash P \to R \) | @prp-implication-transitive | no |
| (curry) | \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \) | @prp-curry | no |
| (or commutes) | \( P \vee Q \vdash Q \vee P \) | @exm-disjunction-first-derivations | no |
| (distributivity) | \( P \wedge (Q \vee R) \dashv\vdash (P \wedge Q) \vee (P \wedge R) \) | @prp-distributivity | no |
| (cases on a hypothesis) | \( (P \to R) \wedge (Q \to R) \dashv\vdash (P \vee Q) \to R \) | @exm-cases-on-hypothesis; the converse @exm-or-hypothesis-split | no |
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

Two rows are proved in exercises, not in the text: the other form of \( \rulename{DS} \) and the converse of the iff of negations. Exercises may use them as rules; the text's own proofs do not.

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

(b) \( \neg \), since the claim is "not: there is an integer \( n \) with \( 2n = 7 \)"; \( \rulename{\neg I} \): "Suppose \( n \) is an integer with \( 2n = 7 \)." (Naming \( n \) uses a rule for "there exists", from Chapter 4.)

(c) \( \wedge \); \( \rulename{\wedge I} \): "We prove the two statements in turn."

(d) \( \leftrightarrow \); \( \rulename{{\leftrightarrow}I} \): "\( (\Rightarrow) \) Assume \( n \) is odd."

(e) \( \rulename{{\to}E} \), which needs the hypothesis \( P \wedge Q \): make it a new goal, reached by \( \rulename{\wedge I} \) from \( P \) and \( Q \); then \( \rulename{{\to}E} \) gives \( R \).

(f) \( \rulename{\neg E} \), which needs \( P \vee Q \) beside \( \neg(P \vee Q) \): make \( P \vee Q \) the new goal (step 4), reached by \( \rulename{\vee I} \) from \( Q \).
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
  \hypo {3} {P}
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

(b) \( \rulename{LEM} \) is used at line 1, and \( \rulename{RAA} \) only inside it. The method cannot avoid step 5 here. Step 2 postpones the \( \vee \) goal; with no premises, step 3 has nothing to eliminate and step 4 nothing to clash; and \( \rulename{\vee I} \) cannot come first, because neither side is derivable from no premises (with \( P \) true and \( Q \) false, \( P \to Q \) is false; with \( P \) false and \( Q \) true, \( Q \to P \) is false; Chapter 3 turns such rows into proofs, @cor-refuting-row). So a resource must be created from nothing, and only step 5 does that. This shows that the **method** needs step 5; that every derivation of the sequent uses \( \rulename{RAA} \) or an equivalent is a stronger claim, which we do not prove.

**Marking scheme.** (10 points)

- 3: a correct split by \( \rulename{LEM} \) (on \( Q \) or on \( P \)), with two case boxes combined by \( \rulename{\vee E} \), or a correct \( \rulename{RAA} \) box on the negated goal.
- 2: in one case, the implication by a box that repeats the case assumption.
- 2: in the other case, the implication by a box that clashes with the case assumption, then \( \rulename{\bot E} \).
- 1: \( \rulename{\vee I} \) on the correct side in each case, every citation available.
- 2: the paragraph names the \( \rulename{LEM} \) line (or the \( \rulename{RAA} \) line) and explains why no other step of the method applies.

Fatal errors (0 for the step): choosing a side of the goal before the split; citing one case's assumption in the other case.
A correct derivation by \( \rulename{RAA} \) on the negated goal earns full marks: its 2 + 2 + 1 points go to the two implications derived inside the \( \rulename{RAA} \) box (one by a box that repeats an assumption, one by a clash and \( \rulename{\bot E} \)) and to the \( \rulename{\vee I} \) lines that clash with the \( \rulename{RAA} \) assumption.
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
6. *Step 4, inside the box.* The new assumption clashes with \( P \vee \neg Q \), which \( \rulename{\vee I} \) builds from either side. The side \( P \) is a letter that nothing gives; the side \( \neg Q \) is a negation, which step 2 can build. So \( \neg Q \) becomes the goal: a box on \( Q \), with the goal \( \bot \). Choosing a side is safe here, since the disjunction is manufactured for a clash with a resource that is its negation (see the paragraph on choosing a side of \( \vee \), after the method).
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
- 2: step 5 is chosen: \( \rulename{RAA} \) on the whole goal, or \( \rulename{LEM} \) on \( P \). (\( \rulename{LEM} \) on \( Q \) also works; our route with it then uses a second classical step, an \( \rulename{RAA} \) for \( P \) in the case \( Q \); award it.)
- 3: the inner boxes and their clashes are correct, and every citation is available.
- 1: the classical line is named.

Fatal errors (0 for the step): \( \rulename{\vee I} \) as the last line, from a disjunct derived from the premise alone; an \( \rulename{RAA} \) box opened with anything but \( \neg(P \vee \neg Q) \).
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

### R. Review

::: {#exr-finding-derivations-r1}
[R1]

For real numbers \( a \) and \( b \), let \( \max(a, b) \coloneqq a \) and \( \min(a, b) \coloneqq b \) if \( a \ge b \), and \( \max(a, b) \coloneqq b \) and \( \min(a, b) \coloneqq a \) if \( a < b \). Prove that \( \max(a, b) + \min(a, b) = a + b \).
:::

::: {.solution}
Since \( a \ge b \) or \( a < b \), and these two cases cover every pair of real numbers, we argue by cases (\( \rulename{\vee E} \), @def-rules-disjunction), as in @exm-abs-product-cases.

*Case \( a \ge b \).* Then \( \max(a, b) = a \) and \( \min(a, b) = b \), so \( \max(a, b) + \min(a, b) = a + b \).

*Case \( a < b \).* Then \( \max(a, b) = b \) and \( \min(a, b) = a \), so \( \max(a, b) + \min(a, b) = b + a = a + b \).

In either case the equation holds, which proves it. Both cases end in the same statement, the goal, as \( \rulename{\vee E} \) requires.
:::

::: {#exr-finding-derivations-r2}
[R2]

Let \( x \) be a real number. Write \( N \) for "\( x < 0 \)", \( G \) for "\( x > 1 \)", and \( S \) for "\( x = 7 \)". Translate the argument below into a sequent in these letters, and derive it.

> \( x \) is neither negative nor greater than \( 1 \). Therefore \( x \) is not negative, and if \( x \) is greater than \( 1 \), then \( x = 7 \).
:::

::: {.solution}
"Neither \( N \) nor \( G \)" says that \( N \vee G \) fails, so the premise is \( \neg(N \vee G) \), not \( \neg N \vee G \). The conclusion is a conjunction whose second part is an implication. The sequent (@def-sequent) is
\[
\neg(N \vee G) \vdash \neg N \wedge (G \to S).
\]
The goal is a conjunction; the first conjunct is a negation (a \( \rulename{\neg I} \) box on \( N \)), and the second an implication (a box on \( G \)). In both boxes \( \rulename{\vee I} \) builds \( N \vee G \), which clashes with the premise; in the second box \( \rulename{\bot E} \) then gives \( S \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (N \vee G)}
  \open
  \hypo {2} {N}
  \have {3} {N \vee G} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg N} \ni{2-4}
  \open
  \hypo {6} {G}
  \have {7} {N \vee G} \oi{6}
  \have {8} {\bot} \ne{7,1}
  \have {9} {S} \be{8}
  \close
  \have {10} {G \to S} \ii{6-9}
  \have {11} {\neg N \wedge (G \to S)} \ai{5,10}
\end{nd}$
\end{center}
```

Lines 2–5 are half of @prp-de-morgan (a), which turns "neither … nor" into \( \neg N \wedge \neg G \). The implication \( G \to S \) is vacuously true, as in @prp-vacuous-implication: the premise rules out \( G \), and a promise never tested is never broken, whatever \( S \) says.
:::

::: {#exr-finding-derivations-r3}
[R3]

Is \( (P \to Q) \to R \vdash P \to (Q \to R) \) derivable? And is its converse, \( P \to (Q \to R) \vdash (P \to Q) \to R \)?
:::

::: {.solution}
The first is derivable, by the search method of this section. The goal gives a box on \( P \), then a box on \( Q \), with the goal \( R \). The premise gives \( R \) by \( \rulename{{\to}E} \) once we produce \( P \to Q \), a new goal: a box on \( P \) whose last line repeats \( Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {R} \ie{1,6}
  \close
  \have {8} {Q \to R} \ii{3-7}
  \close
  \have {9} {P \to (Q \to R)} \ii{2-8}
\end{nd}$
\end{center}
```

The repetition at line 5 puts \( Q \) inside the box of line 4, as \( \rulename{{\to}I} \) requires (clause (D3) of @def-derivation). Two look-alike tools do not apply. @prp-curry moves a **conjunction** in and out of a hypothesis, \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \), and the premise here has \( P \to Q \), not \( P \wedge Q \), in that place. And @prp-implication-transitive chains two implications, which we do not have.

The converse is not derivable, but a search can only stall, not show it. With \( P \) and \( R \) false (and \( Q \) either way), the premise \( P \to (Q \to R) \) is true because \( P \) is false, while \( P \to Q \) is true and \( R \) is false, so the conclusion is false. Chapter 3 proves that such a row rules out every derivation (@cor-refuting-row): the chapter's open question, in a new place.
:::

<!-- dependency ledger
finding-derivations-method (claim): the goal-directed steps and step 5 never turn a derivable gap into an underivable one | inline (argued in the text from def-derivable and one appended elimination step; LEM split by adding a premise)
finding-derivations-method (claim): P or Q |- Q or P is derivable but neither disjunct follows from P or Q alone | derivability: @exm-disjunction-first-derivations; the non-derivation of the disjuncts: informal, ch03 (promised; soundness) makes it exact; nothing depends on it
def-partial-derivation (example): filling a gap adds lines only above its current goal, so an open box at the bottom cannot be repaired | inline (from the definition)
exm-search-postpone-or (example): neither disjunct follows from the premise (two rows) | informal, ch03 (promised; thm-soundness); the example does not depend on it
exm-search-postpone-or (example): LEM on P also succeeds, with a nested or-E, in 22 lines | inline description; not used
exm-search-raa (example): LEM on P leaves the method stuck again in the case not-P | inline (steps 2-4 read off the resources); not used
exm-search-raa (example): in the paragraph on prp-peirce after it, assuming not-Q at the stalled gap of Peirce's search gives no clash | inline (the resources listed); not used
finding-derivations-failed-search (claim): no derivation of Q -> P from P -> Q exists | not claimed as proved; ch03 (promised; cor-refuting-row), the chapter's closing question
exm-skeleton-odd-product (example): every integer is even or odd, and not both; m = 2k gives mn = 2(kn) | school algebra, ch11 (promised)
exm-skeleton-odd-product (example): "say m = 2k" names a witness | ch04 (promised; rules for "there exists"), flagged in prose
exr-finding-derivations-a1 (solution): (b) naming n uses a rule for "there exists" | ch04 (promised), flagged in prose
exr-finding-derivations-b1 (solution): no derivation of P from not(P -> Q) avoids RAA | stated without proof and marked so; nothing depends on it
exr-finding-derivations-c2 (solution): neither disjunct is derivable from no premises (rows) | informal, ch03 (promised; soundness); the solution says it proves only that the method needs step 5
exr-finding-derivations-c3 (solution): the LEM-on-P route is 11 lines; our route by LEM on Q uses a second classical step in the case Q | inline description (the route is given in words); the second is a remark in the marking scheme about a route, not claimed as a necessity
exr-finding-derivations-r1 (solution): a >= b or a < b for real numbers; b + a = a + b | school algebra, ch11 (promised)
exr-finding-derivations-r3 (solution): the converse is not derivable (row P = R = false) | ch03 (promised; cor-refuting-row), flagged in the solution
-->
