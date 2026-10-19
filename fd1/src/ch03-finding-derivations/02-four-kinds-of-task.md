# Four Kinds of Task

The method of Section 3.1 answers one kind of question: here are premises, here is a conclusion, find a derivation. Mathematics asks others as well:

- prove a statement from nothing;
- show that two statements say the same thing;
- show that some conditions cannot all be met at once;
- decide whether a conclusion follows at all, when nobody says whether it does.

Each of these changes where a search starts and what counts as its end. This section takes the four tasks in turn. Underneath, it finds, they are one question.

## Four tasks, one method

*Let the task choose the search.* The four tasks use the same rules and the same method. What differs is the first move and the finish line.

| Task | The claim | Where the search starts | What ends it |
|---|---|---|---|
| theorem | \( \vdash \varphi \) | step 2 on the goal; every resource is an assumption the goal asks for | the goal, reached outside every box |
| equivalence | \( \varphi \dashv\vdash \psi \) (@def-provable-equivalence) | two searches, one from each side | two derivations |
| inconsistency | \( \Gamma \vdash \bot \) | step 4: the goal is \( \bot \); look for a clash partner already on a line | \( \bot \), outside every box |
| derive or break | \( \Gamma \vdash \varphi \)? (verdict withheld) | try to break it first | a derivation, or statements that make the counterexample set true |

Only the last task leaves open which way it ends. The other three state their claim: a failed search leaves the question open, as Section 3.1's failed search did, and a break ends the task against the claim.

::: {.check}
Which task is each? (i) \( \vdash P \vee \neg P \). (ii) \( P \wedge Q \dashv\vdash Q \wedge P \). (iii) Show that \( P \), \( \neg P \vee Q \) and \( \neg Q \) cannot all be accepted together. (iv) Does \( P \to Q, \ Q \vdash P \) hold?
:::

::: {.solution}
(i) A theorem. (ii) An equivalence. (iii) An inconsistency: the claim \( P, \ \neg P \vee Q, \ \neg Q \vdash \bot \). (iv) Derive or break; it breaks, since it is affirming the consequent (Section 1.3).
:::

## Theorems

A **theorem** of logic is a statement derivable from no premises, \( \vdash \varphi \) (@def-derivable with the list empty).

::: {#exm-theorem-search}
[A statement that implies a contradiction]

Find a derivation of \( \vdash (P \to (Q \wedge \neg Q)) \to \neg P \).

In words: a statement that implies a contradiction is false. Every proof that begins "suppose \( P \)" and ends "which is impossible" has this shape.
:::

::: {.solution}
There are no premises, so step 1 writes only the goal. Step 2 opens a box on \( P \to (Q \wedge \neg Q) \) with the goal \( \neg P \), and then, inside it, a box on \( P \) with the goal \( \bot \):

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \to (Q \wedge \neg Q)}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {\neg P}
  \close
  \have {8} {(P \to (Q \wedge \neg Q)) \to \neg P} \ii{1-7}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \open
  \hypo {1} {P \to (Q \wedge \neg Q)}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {\bot}
  \close
  \have {7} {\neg P} \ni{2-6}
  \close
  \have {8} {(P \to (Q \wedge \neg Q)) \to \neg P} \ii{1-7}
\end{nd}$
\end{center}
```

Now there are two resources, both assumptions the goal asked for. Step 3 fires the first on the second, giving \( Q \wedge \neg Q \), and splits it by \( \rulename{\wedge E} \). Step 4 finds the clash.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \to (Q \wedge \neg Q)}
  \open
  \hypo {2} {P}
  \have {3} {Q \wedge \neg Q} \ie{1,2}
  \have {4} {Q} \ae{3}
  \have {5} {\neg Q} \ae{3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg P} \ni{2-6}
  \close
  \have {8} {(P \to (Q \wedge \neg Q)) \to \neg P} \ii{1-7}
\end{nd}$
\end{center}
```
:::

A theorem has no premises, so the goal does all the early work. Once proved, it is a derived rule with nothing above the line (@def-derived-rule): any derivation, from any premises, may write an instance of it as a line, as derivations already write \( \rulename{LEM} \).

## Equivalences

::: {#exm-equivalence-search}
[Proving a disjunction by refuting one side]

Show that \( P \to (Q \vee R) \dashv\vdash (P \wedge \neg Q) \to R \).

This is how mathematics proves a disjunction: to show that \( ab = 0 \) implies \( a = 0 \) or \( b = 0 \), assume \( ab = 0 \) and \( a \ne 0 \), and show \( b = 0 \) (divide by \( a \)). The equivalence says that this changes nothing.
:::

::: {.solution}
\( (\Rightarrow) \) The goal is an implication, so a box on \( P \wedge \neg Q \). \( \rulename{\wedge E} \) splits it, the premise fires on \( P \), and \( \rulename{DS} \) removes the refuted side.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \open
  \hypo {2} {P \wedge \neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {R}
  \close
  \have {7} {(P \wedge \neg Q) \to R} \ii{2-6}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \open
  \hypo {2} {P \wedge \neg Q}
  \have {3} {P} \ae{2}
  \have {4} {\neg Q} \ae{2}
  \have {5} {Q \vee R} \ie{1,3}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {R}
  \close
  \have {7} {(P \wedge \neg Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \open
  \hypo {2} {P \wedge \neg Q}
  \have {3} {P} \ae{2}
  \have {4} {\neg Q} \ae{2}
  \have {5} {Q \vee R} \ie{1,3}
  \have {6} {R} \ds{5,4}
  \close
  \have {7} {(P \wedge \neg Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```

\( (\Leftarrow) \) The goal is an implication: a box on \( P \), with the goal \( Q \vee R \). That goal is a disjunction, so it is postponed (step 2). The premise waits for \( P \wedge \neg Q \): \( P \) is in hand, \( \neg Q \) is not, and nothing clashes. That is step 5, and the well-chosen statement is \( Q \), whose negation the premise waits for: \( \rulename{LEM} \) on \( Q \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge \neg Q) \to R}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][10] {10} {Q \vee R}
  \close
  \have {11} {P \to (Q \vee R)} \ii{2-10}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {(P \wedge \neg Q) \to R}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee \neg Q} \lem{}
  \open
  \hypo {4} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {Q \vee R}
  \close
  \open
  \hypo {6} {\neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {Q \vee R}
  \close
  \have {10} {Q \vee R} \oe{3,4-5,6-9}
  \close
  \have {11} {P \to (Q \vee R)} \ii{2-10}
\end{nd}$
\end{center}
```

In the case \( Q \), \( \rulename{\vee I} \) gives the left side. In the case \( \neg Q \), \( \rulename{\wedge I} \) builds \( P \wedge \neg Q \), the premise gives \( R \), and \( \rulename{\vee I} \) gives the right side.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge \neg Q) \to R}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee \neg Q} \lem{}
  \open
  \hypo {4} {Q}
  \have {5} {Q \vee R} \oi{4}
  \close
  \open
  \hypo {6} {\neg Q}
  \have {7} {P \wedge \neg Q} \ai{2,6}
  \have {8} {R} \ie{1,7}
  \have {9} {Q \vee R} \oi{8}
  \close
  \have {10} {Q \vee R} \oe{3,4-5,6-9}
  \close
  \have {11} {P \to (Q \vee R)} \ii{2-10}
\end{nd}$
\end{center}
```
:::

An equivalence is two searches, and they need not be alike. The direction \( (\Rightarrow) \) used a derived rule and no classical step. The direction \( (\Leftarrow) \) reached step 5, because its goal was a disjunction with no side in hand. When one direction is easy, do it first: it checks that the statements are worth comparing, and its lines often suggest the other direction's split.

## Inconsistent lists

Sometimes the task is not to reach a conclusion but to show that some statements cannot be accepted together: a puzzle's conditions that no number meets, the hypotheses of a lemma that contradict each other, or the assumption of a proof by contradiction together with what is given. Section 2.5 (@exr-reductio-and-classical-rules-b5) already read an \( \rulename{RAA} \) derivation as a derivation of \( \bot \) from the counterexample set. A derivation of \( \bot \) does this job, and the list it starts from gets a name.

::: {#def-inconsistent-set}
[Inconsistent and Consistent Lists]

Let \( \Gamma \) be a list of statements \( \varphi_1, \dots, \varphi_n \), where \( n \ge 0 \). The list
\( \Gamma \) is **inconsistent** if \( \Gamma \vdash \bot \): some derivation whose premises all belong to
\( \Gamma \) has \( \bot \) as its last line. It is **consistent** if it is not inconsistent, that is,
if **no** derivation with premises in \( \Gamma \) ends with \( \bot \).
:::

In words: a list is inconsistent when a derivation from it reaches \( \bot \) outside every box. The definition speaks only of derivations, and says nothing about whether the statements are true. The list \( P, \neg P \) is inconsistent, by one \( \rulename{\neg E} \) line, and so is any list with \( \bot \) as a member. To show a list inconsistent, exhibit a derivation. To show one consistent, one would have to rule out every derivation, and nothing in this chapter can do that.

::: {#prp-inconsistent-derives-everything}
[An Inconsistent List Proves Everything]

For a list of statements \( \Gamma \), the following are equivalent:

::: {.enumerate options="label=(\roman*)"}
1. \( \Gamma \) is inconsistent;
2. \( \Gamma \vdash \psi \) for **every** statement \( \psi \);
3. \( \Gamma \vdash \chi \) and \( \Gamma \vdash \neg\chi \) for **some** statement \( \chi \).
:::
:::

*In words: an inconsistent list proves every statement, and a list that proves some statement and its negation is inconsistent.* This is @prp-ex-falso grown from two premises to any inconsistent list. Its proof is in the fold of the next subsection.

::: {.check}
Without writing a derivation, explain why \( P, \ \neg P \vdash Q \wedge \neg Q \).
:::

::: {.solution}
The list \( P, \neg P \) is inconsistent (one \( \rulename{\neg E} \) line), so by @prp-inconsistent-derives-everything, (i) \( \Rightarrow \) (ii), it derives every statement, \( Q \wedge \neg Q \) included.
:::

::: {#exm-inconsistency-search}
[Four conditions that no integer meets]

Let \( n \) be an integer. A puzzle asks for an \( n \) such that:

::: {.enumerate options="label=(\arabic*)"}
1. if \( n \) is even, then \( n \) is a multiple of \( 4 \);
2. \( n \) is even or a multiple of \( 3 \);
3. if \( n \) is a multiple of \( 3 \), then \( n \) is even;
4. \( n \) is not a multiple of \( 4 \).
:::

With \( E \): "\( n \) is even", \( F \): "\( n \) is a multiple of \( 4 \)" and \( T \): "\( n \) is a multiple of \( 3 \)", show that the list \( E \to F, \ E \vee T, \ T \to E, \ \neg F \) is inconsistent.
:::

::: {.solution}
The goal is \( \bot \). Look first for a clash partner already on a line (Section 3.1): line 4 is \( \neg F \), so aim at \( F \).

\( F \) is the conclusion of line 1, so the new goal is \( E \), a letter. Line 3 gives \( E \) from \( T \), but \( T \) is not in hand, and \( E \vee T \) does not say which side holds. So use line 2 by \( \rulename{\vee E} \), with both cases ending in \( E \). The case \( E \) is a one-line box; the case \( T \) fires line 3.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {E \to F}
  \hypo {2} {E \vee T}
  \hypo {3} {T \to E}
  \hypo {4} {\neg F}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {F}
  \have {10} {\bot} \ne{9,4}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {E \to F}
  \hypo {2} {E \vee T}
  \hypo {3} {T \to E}
  \hypo {4} {\neg F}
  \open
  \hypo {5} {E}
  \close
  \open
  \hypo {6} {T}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {E}
  \close
  \have {8} {E} \oe{2,5-5,6-7}
  \have {9} {F} \ie{1,8}
  \have {10} {\bot} \ne{9,4}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \to F}
  \hypo {2} {E \vee T}
  \hypo {3} {T \to E}
  \hypo {4} {\neg F}
  \open
  \hypo {5} {E}
  \close
  \open
  \hypo {6} {T}
  \have {7} {E} \ie{3,6}
  \close
  \have {8} {E} \oe{2,5-5,6-7}
  \have {9} {F} \ie{1,8}
  \have {10} {\bot} \ne{9,4}
\end{nd}$
\end{center}
```

Read as a proof about \( n \), the derivation shows that no integer meets all four conditions: by (2) and (3), \( n \) is even in either case; by (1) it is a multiple of \( 4 \); and (4) says it is not. Yet any three of the conditions can be met together: \( n = 6 \) meets all but (1), \( n = 1 \) all but (2), \( n = 3 \) all but (3), and \( n = 12 \) all but (4). The inconsistency belongs to the four together. The derivation does not say which condition to drop (the fold "Logic permits; it does not choose" in Section 3.1).
:::

::: {.check}
Which integers between \( 1 \) and \( 10 \) meet conditions (1), (2) and (4) of @exm-inconsistency-search, and which condition does each break?
:::

::: {.solution}
\( 3 \) and \( 9 \): they are odd, so (1) promises nothing; they are multiples of \( 3 \), so (2) holds; and they are not multiples of \( 4 \). Each breaks (3).
:::

Here are three more inconsistent lists, each with compound members, and one list that only looks inconsistent.

::: {#exm-inconsistent-lists}
[Three inconsistent lists, and a look-alike]

| The list | The clash it reaches | The derivation of \( \bot \), in brief |
|---|---|---|
| \( (P \vee Q) \to R, \ P \wedge \neg R \) | \( R \), \( \neg R \) | \( P \) by \( \rulename{\wedge E} \); \( P \vee Q \) by \( \rulename{\vee I} \); \( R \) by \( \rulename{{\to}E} \); \( \neg R \) by \( \rulename{\wedge E} \); \( \bot \) by \( \rulename{\neg E} \) (7 lines) |
| \( P \leftrightarrow \neg P \) | \( P \), \( \neg P \) | a box on \( P \): \( \neg P \) by \( \rulename{{\leftrightarrow}E} \), \( \bot \) by \( \rulename{\neg E} \); \( \neg P \) by \( \rulename{\neg I} \); then \( P \) by \( \rulename{{\leftrightarrow}E} \), and \( \neg P \) by \( \rulename{{\leftrightarrow}E} \) again from that \( P \); \( \bot \) by \( \rulename{\neg E} \) (8 lines) |
| \( \neg(P \to Q), \ \neg P \) | \( P \to Q \), \( \neg(P \to Q) \) | \( P \to Q \) by VI from \( \neg P \) (@prp-vacuous-implication); \( \bot \) by \( \rulename{\neg E} \) (4 lines) |

**Not an instance.** \( P \to Q, \ P \to \neg Q \). The two members look opposed. But with \( P \) false (say \( P \): "\( 0 = 1 \)") both are true, whatever \( Q \) says, so the claim \( P \to Q, \ P \to \neg Q \vdash \bot \) breaks. What the list does derive is \( \neg P \): from \( P \) it would give \( Q \) and \( \neg Q \). This chapter does not call the list inconsistent, and it does not call it consistent either. Whether a break rules out every derivation of \( \bot \) is the question the chapter ends on (Section 3.3).
:::

The second row's derivation is written without a detour: the line \( \neg P \) built by \( \rulename{\neg I} \) is cited by \( \rulename{{\leftrightarrow}E} \), never taken apart at once by \( \rulename{\neg E} \), so it stays, as Section 3.1's detour paragraph allows ("an introduced line cited elsewhere stays").

::: {.warning}
[Not allowed: claims about inconsistency]

Each claim below is wrong; the tag names what it misreads.

- "The list is inconsistent because one of its members is false." *Truth for derivation*: inconsistency is a derivation of \( \bot \) (@def-inconsistent-set), not a false member. The one-member list "\( 2 > 3 \)" has a false member, and no derivation of \( \bot \) is offered.
- "\( P \to Q \) and \( P \to \neg Q \) contradict each other, so the list is inconsistent." *Looks for derivation*: nothing has been derived. Both members are true when \( P \) is false, and the claim of inconsistency breaks.
- "Line 7, inside the box of the assumption \( P \), is \( \bot \); so the premises are inconsistent." *A boxed line*: that \( \bot \) depends on \( P \). It shows the list \( \Gamma, P \) inconsistent, and so \( \Gamma \vdash \neg P \). The last line must lie outside every box (@def-derivation).
- "A search for \( \bot \) stalled, so the list is consistent." *A stall for a proof*: a stalled search proves nothing (Section 3.1). Consistency is the absence of **every** derivation of \( \bot \).
- "The list is inconsistent, so its first member is false." *The list for a member*: inconsistency belongs to the list. It says that the members cannot all be accepted together, not which one fails (compare the four conditions above).
:::

## The counterexample set, derived

Proving and refuting meet in one list. The counterexample set of a claim \( \Gamma \vdash \varphi \) is the list \( \Gamma, \neg\varphi \) (@def-counterexample-set). Breaking the claim makes that list true. Deriving the claim, it turns out, is showing that list inconsistent.

::: {#prp-derivable-iff-negation-inconsistent}
[Derivable Exactly When the Counterexample Set Is Inconsistent]

Let \( \Gamma \) be a list of statements and \( \varphi \) a statement.

::: {.enumerate options="label=(\alph*)"}
1. \( \Gamma \vdash \neg\varphi \) if and only if the list \( \Gamma, \varphi \) is inconsistent.
2. \( \Gamma \vdash \varphi \) if and only if the list \( \Gamma, \neg\varphi \) is inconsistent.
:::
:::

*In words: (b) says that a claim is derivable exactly when its counterexample set is inconsistent, and (a) says the same for a negated conclusion.* In the proofs, the box of (a) closes by \( \rulename{\neg I} \) and that of (b) by \( \rulename{RAA} \): Section 2.5's distinction between the two rules, stated about whole derivations. Section 1.1's test of a form, try to break it, now has a partner on the same list: make the counterexample set true, or derive \( \bot \) from it.

With \( \Gamma \) empty and \( \varphi \) the statement \( P \leftrightarrow \neg P \), part (a) says that the second row of @exm-inconsistent-lists and @lem-not-iff-own-negation, \( \vdash \neg(P \leftrightarrow \neg P) \), are the same fact.

::: {.second-reading title="The proofs: append a line, or copy a derivation into a box"}
::: {.proof}
*Proof of @prp-inconsistent-derives-everything.* (i) \( \Rightarrow \) (ii): a derivation of \( \bot \) with premises in \( \Gamma \), followed by the line \( \psi \) by \( \rulename{\bot E} \), is a derivation of \( \psi \). Its last line lies in no box. (ii) \( \Rightarrow \) (iii): apply (ii) to any \( \chi \) and to \( \neg\chi \). (iii) \( \Rightarrow \) (i): the sequent \( \chi, \neg\chi \vdash \bot \) has a one-step derivation (\( \rulename{\neg E} \)), so by @lem-weakening-cut (c), \( \Gamma \vdash \bot \).
:::

::: {.proof}
*Proof of @prp-derivable-iff-negation-inconsistent.* (b), \( (\Rightarrow) \): from \( \Gamma \vdash \varphi \), @lem-weakening-cut (a) gives \( \Gamma, \neg\varphi \vdash \varphi \). The one-line derivation of the premise \( \neg\varphi \) gives \( \Gamma, \neg\varphi \vdash \neg\varphi \). By @lem-weakening-cut (c) with \( \varphi, \neg\varphi \vdash \bot \), we get \( \Gamma, \neg\varphi \vdash \bot \).

(b), \( (\Leftarrow) \): let \( D \) be a derivation of \( \bot \) with premises in \( \Gamma, \neg\varphi \). If the last line of \( D \) is a premise in \( \Gamma \), then \( \bot \) is a member of \( \Gamma \), and \( \rulename{\bot E} \) gives \( \varphi \). (The last line cannot be the premise \( \neg\varphi \), since \( \neg\varphi \) is not \( \bot \).) Otherwise, write as premises those premises of \( D \) that belong to \( \Gamma \). Open a box with the assumption \( \neg\varphi \). Inside it, copy the lines of \( D \) that are not premises, in order, with their boxes, renumbering citations; a citation of the premise \( \neg\varphi \) now cites the assumption. Close the box after the copy of the last line of \( D \), and write \( \varphi \) by \( \rulename{RAA} \).

Every copied citation is legal. A cited premise of \( \Gamma \) lies above the box, in no box. The assumption is available throughout the box. The boxes of \( D \) sit inside the new box as they sat in \( D \), so every line and every box that was available at a citing line stays available (the scope rule of @def-derivation). The last line of \( D \) lies in no box of \( D \), so its copy is a line of the new box itself, as \( \rulename{RAA} \) requires. If \( D \) never cites \( \neg\varphi \), nothing changes.

Part (a) is the same, with \( \varphi \) in place of \( \neg\varphi \) and \( \rulename{\neg I} \) in place of \( \rulename{RAA} \). If the last line of \( D \) is the premise \( \varphi \) itself (possible only when \( \varphi \) is \( \bot \)), nothing is copied: the box is its one assumption line, and \( \rulename{\neg I} \) closes it at once. In \( (\Rightarrow) \), \( \Gamma, \varphi \vdash \varphi \) and, by weakening, \( \Gamma, \varphi \vdash \neg\varphi \); chaining with \( \rulename{\neg E} \) finishes.
:::

The copying is the move of Section 1.4's @exr-proving-an-implication-c4 (b), which turns open assumptions into premises, run backwards.
:::

::: {.check}
By @prp-derivable-iff-negation-inconsistent, which list must be shown inconsistent to prove \( \vdash \neg(P \wedge \neg P) \)? Show it.
:::

::: {.solution}
By (a), with \( \Gamma \) empty and \( \varphi \) the statement \( P \wedge \neg P \), the list is \( P \wedge \neg P \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge \neg P}
  \have {2} {P} \ae{1}
  \have {3} {\neg P} \ae{1}
  \have {4} {\bot} \ne{2,3}
\end{nd}$
\end{center}
```
:::

## One task in four costumes

Every task of this section is a claim that something is derivable, and by @prp-derivable-iff-negation-inconsistent every such claim is a claim that a list is inconsistent.

| Task | As a claim of derivability | As a claim of inconsistency | It breaks when some choice of statements makes |
|---|---|---|---|
| theorem | \( \vdash \varphi \) | the list \( \neg\varphi \) | \( \varphi \) false |
| equivalence | \( \varphi \vdash \psi \) and \( \psi \vdash \varphi \) | the lists \( \varphi, \neg\psi \) and \( \psi, \neg\varphi \) | one of \( \varphi \), \( \psi \) true and the other false |
| inconsistency | \( \Gamma \vdash \bot \) | the list \( \Gamma \) | every member of \( \Gamma \) true |
| derive or break | \( \Gamma \vdash \varphi \) | the list \( \Gamma, \neg\varphi \) | every member of \( \Gamma, \neg\varphi \) true |

An equivalence is also a theorem: \( \varphi \dashv\vdash \psi \) holds exactly when \( \vdash \varphi \leftrightarrow \psi \). Copy each of the two derivations into a box, as in the fold above, and close both boxes by \( \rulename{{\leftrightarrow}I} \). Conversely, add the premise \( \varphi \) to a derivation of \( \varphi \leftrightarrow \psi \) and write \( \psi \) by \( \rulename{{\leftrightarrow}E} \), and likewise for \( \psi \).

So the four tasks are one: is this list inconsistent? Each costume starts the search in a different place, which is why the task chooses the search. And each row has a second half, the last column: what to do when the list might instead be made true. That is the fourth task.

## Derive or break

Section 1.5 listed claims without a verdict ("Derive it or break it"). Here the format becomes a task with its own first move: **decide before you search**.

*Try to break it first.* Spend a few minutes trying to make the counterexample set true, starting where the conclusion is false (Section 1.1, "Where to look first"). Either some choice of statements works, and the claim breaks; or every attempt is forced into a clash. Then search for a derivation. The forced attempt usually suggests a plan for it: the statements the attempt had to make true suggest the assumptions of the derivation's boxes, and the clash it met suggests the derivation's \( \bot \).

::: {#exm-derive-or-break-search}
[Two claims, one connective apart]

Derive or break each claim.

::: {.enumerate options="label=(\alph*)"}
1. \( P \to (Q \to R), \ P \to \neg R \vdash P \to \neg Q \).
2. \( P \to (Q \vee R), \ P \to \neg R \vdash P \to \neg Q \).
:::
:::

::: {.solution}
*(a), trying to break it.* The conclusion is false only with \( P \) true and \( \neg Q \) false, that is, \( Q \) true. Then the first premise needs \( Q \to R \) true, so \( R \) true. The second needs \( \neg R \) true, so \( R \) false. Every choice was forced, and the forcing ends in a clash. So we search.

*(a), the derivation.* The attempt's plan: a box on \( P \) (the conclusion's hypothesis), a box on \( Q \) (the statement whose negation is wanted), and the clash \( R \), \( \neg R \). Before the box on \( Q \) opens, both premises fire on \( P \): lines that need nothing new (Section 3.1).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {P \to \neg R}
  \open
  \hypo {3} {P}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {\neg Q}
  \close
  \have {10} {P \to \neg Q} \ii{3-9}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {P \to \neg R}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \ie{1,3}
  \have {5} {\neg R} \ie{2,3}
  \open
  \hypo {6} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][8] {8} {\bot}
  \close
  \have {9} {\neg Q} \ni{6-8}
  \close
  \have {10} {P \to \neg Q} \ii{3-9}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {P \to \neg R}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \ie{1,3}
  \have {5} {\neg R} \ie{2,3}
  \open
  \hypo {6} {Q}
  \have {7} {R} \ie{4,6}
  \have {8} {\bot} \ne{7,5}
  \close
  \have {9} {\neg Q} \ni{6-8}
  \close
  \have {10} {P \to \neg Q} \ii{3-9}
\end{nd}$
\end{center}
```

*(b), trying to break it.* The same start: \( P \) true, \( Q \) true. Now the first premise asks only that \( Q \vee R \) be true, and \( Q \) already makes it so. \( R \) is free, and the second premise asks for \( R \) false. Nothing clashes: with \( P \) and \( Q \) true and \( R \) false, every member of the counterexample set \( P \to (Q \vee R), \ P \to \neg R, \ \neg(P \to \neg Q) \) is true. With statements about a real number \( x \), take \( P \): "\( x > 0 \)", \( Q \): "\( x > 1 \)", \( R \): "\( x > 3 \)", at \( x = 2 \). The claim breaks.

The two claims differ in one connective. Trying to break each found its verdict, and for (a) it also found the derivation. The method of Section 3.1 would have found (a) without the attempt. On (b) the method of Section 3.1 could only search, and a stall is not a verdict; the break is.
:::

The task as a chart. The loop at the bottom is honest: nothing in this chapter promises that it ends.

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc start] (s) {a claim $\Gamma \vdash \varphi$,\\verdict withheld};
  \node[fc test, below=of s] (t1) {can the counterexample set\\be made true? (start where\\the conclusion is false)};
  \node[fc start, right=of t1] (e1) {it breaks:\\give the statements};
  \node[fc step, below=of t1] (b1) {search for a derivation\\(Section 3.1): the forced\\clash suggests a plan};
  \node[fc test, below=of b1] (t2) {has the search\\finished?};
  \node[fc start, right=of t2] (e2) {derived};
  \draw[fc arrow] (s) -- (t1);
  \draw[fc arrow] (t1) -- node[above, font=\scriptsize] {yes} (e1);
  \draw[fc arrow] (t1) -- node[right, font=\scriptsize] {every try is forced into a clash} (b1);
  \draw[fc arrow] (b1) -- (t2);
  \draw[fc arrow] (t2) -- node[above, font=\scriptsize] {yes} (e2);
  \draw[fc arrow] (t2.west) -- ++(-0.6,0) |- node[pos=0.25, left, font=\scriptsize] {stalled} (t1.west);
\end{tikzpicture}
\end{center}
```

::: {.check}
Change one symbol of the first premise of claim (b) in @exm-derive-or-break-search so that the claim can be derived, and derive it.
:::

::: {.solution}
For example, replace \( \vee \) by \( \to \): that is claim (a), derived above. Or replace \( \vee \) by \( \wedge \): from \( P \), the premises give \( Q \wedge R \) and \( \neg R \), which clash.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \wedge R)}
  \hypo {2} {P \to \neg R}
  \open
  \hypo {3} {P}
  \have {4} {Q \wedge R} \ie{1,3}
  \have {5} {R} \ae{4}
  \have {6} {\neg R} \ie{2,3}
  \have {7} {\bot} \ne{5,6}
  \have {8} {\neg Q} \be{7}
  \close
  \have {9} {P \to \neg Q} \ii{3-8}
\end{nd}$
\end{center}
```

Replacing \( \vee \) by \( \leftrightarrow \), or \( Q \) by \( R \), works too. For \( \leftrightarrow \): from \( P \), the premises give \( Q \leftrightarrow R \) and \( \neg R \); a box on \( Q \) gives \( R \) by \( \rulename{{\leftrightarrow}E} \), which clashes with \( \neg R \), so \( \neg Q \) by \( \rulename{\neg I} \). For \( Q \) replaced by \( R \): from \( P \), \( R \vee R \) gives \( R \) by \( \rulename{\vee E} \), which clashes with \( \neg R \), so \( \neg Q \) by \( \rulename{\bot E} \).
:::

::: {.remark}
[Looking ahead]

Chapter 4 calls a list whose members can all be made true at once *satisfiable*, and proves that the satisfiable lists are exactly the consistent ones.
:::

## Exercises

### A. Check your understanding

::: {#exr-four-kinds-of-task-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. When is a list of statements inconsistent?
2. By @prp-derivable-iff-negation-inconsistent, which list is inconsistent exactly when \( P \to Q, \ Q \to R \vdash P \to R \)?
3. True or false: every list that has \( \bot \) as a member is inconsistent.
4. True or false: if \( \Gamma \) is inconsistent, so is every list \( \Gamma, \psi \).
5. Name the task and the first move: "show that \( P \wedge Q \dashv\vdash Q \wedge P \)".
:::
:::

::: {.solution}
(a) When \( \bot \) is derivable from it (@def-inconsistent-set).

(b) The counterexample set \( P \to Q, \ Q \to R, \ \neg(P \to R) \).

(c) True: the one-line derivation whose only line is the premise \( \bot \) ends with \( \bot \).

(d) True, by @lem-weakening-cut (a): the derivation of \( \bot \) from \( \Gamma \) has its premises in \( \Gamma, \psi \).

(e) An equivalence: two derivations, each starting with \( \rulename{\wedge E} \) on its premise. Each is @prp-and-commutes, with the letters exchanged for the second.
:::

::: {#exr-four-kinds-of-task-a2}
[A2: Drill]

The parts run from naming the task, through one step and a missing piece, to claims to judge and short derivations.

::: {.enumerate options="label=(\alph*)"}
1. Which task is "show \( \vdash (P \wedge Q) \to P \)"?
2. "Show that \( P \to \neg Q \) and \( Q \to \neg P \) are provably equivalent." Which two derivations does this ask for?
3. Write "\( P \), \( P \to Q \) and \( \neg Q \) cannot all be accepted together" as a sequent.
4. A search for \( \bot \) from \( P \wedge \neg Q, \ P \to Q \) begins. Write its first three lines after the premises.
5. Which list must be shown inconsistent to prove \( P \to Q \vdash \neg Q \to \neg P \) by @prp-derivable-iff-negation-inconsistent (b)?
6. The list \( Q, \ \neg P, \ \neg\neg R \) is the counterexample set of which claims?
7. "\( P \to Q, \ P \to \neg Q \) is inconsistent, since its members contradict each other." Is this correct?
8. "Inside the box of the assumption \( P \), line 6 is \( \bot \); so the premises are inconsistent." Is this correct?
9. "A search for \( \bot \) from \( P \vee Q, \ \neg P \) stalled; so the list is consistent." Is this correct?
10. "Since \( P, \neg P \vdash \bot \), the list \( P, \neg P \) derives both \( Q \) and \( \neg Q \)." Is this correct?
11. Derive \( \bot \) from \( P \to Q, \ Q \to R, \ P, \ \neg R \).
12. Derive \( \bot \) from \( P \vee Q, \ \neg P, \ \neg Q \).
:::
:::

::: {.solution}
(a) A theorem.

(b) \( P \to \neg Q \vdash Q \to \neg P \) and \( Q \to \neg P \vdash P \to \neg Q \).

(c) \( P, \ P \to Q, \ \neg Q \vdash \bot \).

(d) 3 \( P \), \( \rulename{\wedge E} \) 1; 4 \( Q \), \( \rulename{{\to}E} \) 2, 3; 5 \( \neg Q \), \( \rulename{\wedge E} \) 1. (Then 6 \( \bot \), \( \rulename{\neg E} \) 4, 5.)

(e) \( P \to Q, \ \neg(\neg Q \to \neg P) \).

(f) Of \( Q, \neg P \vdash \neg R \), with \( \neg\neg R \) the negated conclusion, and of \( Q, \neg\neg R \vdash P \), with \( \neg P \) the negated conclusion. \( Q \) is not a negation, so it is not the negated conclusion of any claim.

(g) No. Both members are true when \( P \) is false, and nothing has been derived.

(h) No. It shows the premises together with \( P \) inconsistent, so the premises derive \( \neg P \).

(i) No: a stalled search proves nothing.

(j) Yes: @prp-inconsistent-derives-everything, (i) \( \Rightarrow \) (ii).

(k) 5 \( Q \), \( \rulename{{\to}E} \) 1, 3; 6 \( R \), \( \rulename{{\to}E} \) 2, 5; 7 \( \bot \), \( \rulename{\neg E} \) 6, 4.

(l) 4 \( P \), assumption; 5 \( \bot \), \( \rulename{\neg E} \) 4, 2; 6 \( Q \), assumption; 7 \( \bot \), \( \rulename{\neg E} \) 6, 3; 8 \( \bot \), \( \rulename{\vee E} \) 1, 4–5, 6–7.
:::

### B. Practice

::: {#exr-four-kinds-of-task-b1}
[B1: Three theorems]

Derive each theorem, and say which step of Section 3.1's method opens each box.

::: {.enumerate options="label=(\alph*)"}
1. \( \vdash \neg(P \wedge \neg P) \wedge \neg\neg(P \vee \neg P) \).
2. \( \vdash ((P \to Q) \wedge (P \vee Q)) \to Q \).
3. \( \vdash ((P \to Q) \to Q) \to ((Q \to P) \to P) \).
:::
:::

::: {.solution}
(a)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge \neg P}
  \have {2} {P} \ae{1}
  \have {3} {\neg P} \ae{1}
  \have {4} {\bot} \ne{2,3}
  \close
  \have {5} {\neg (P \wedge \neg P)} \ni{1-4}
  \open
  \hypo {6} {\neg (P \vee \neg P)}
  \open
  \hypo {7} {P}
  \have {8} {P \vee \neg P} \oi{7}
  \have {9} {\bot} \ne{8,6}
  \close
  \have {10} {\neg P} \ni{7-9}
  \have {11} {P \vee \neg P} \oi{10}
  \have {12} {\bot} \ne{11,6}
  \close
  \have {13} {\neg\neg (P \vee \neg P)} \ni{6-12}
  \have {14} {\neg (P \wedge \neg P) \wedge \neg\neg (P \vee \neg P)} \ai{5,13}
\end{nd}$
\end{center}
```

Boxes 1 and 6 come from step 2: each goal is a negation. Box 7 comes from step 2 inside step 4: step 4 chooses to manufacture \( P \vee \neg P \) from its side \( \neg P \), so that it clashes with line 6, and the goal \( \neg P \), a negation, opens the box. The second conjunct needed no classical rule, although \( P \vee \neg P \) itself does in this book's derivation (@prp-excluded-middle).

(b)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {(P \to Q) \wedge (P \vee Q)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {P \vee Q} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{2,4}
  \close
  \open
  \hypo {6} {Q}
  \close
  \have {7} {Q} \oe{3,4-5,6-6}
  \close
  \have {8} {((P \to Q) \wedge (P \vee Q)) \to Q} \ii{1-7}
\end{nd}$
\end{center}
```

Box 1 comes from step 2. Boxes 4 and 6 come from step 3: the resource \( P \vee Q \) is split by \( \rulename{\vee E} \), both cases ending in the goal \( Q \) (the case \( Q \) is a one-line box). Lines 2 and 3 need nothing new. Read aloud: if \( P \) implies \( Q \), and \( P \) or \( Q \) holds, then \( Q \) holds.

(c)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {(P \to Q) \to Q}
  \open
  \hypo {2} {Q \to P}
  \open
  \hypo {3} {\neg P}
  \have {4} {P \to Q} \by{VI}{3}
  \have {5} {Q} \ie{1,4}
  \have {6} {P} \ie{2,5}
  \have {7} {\bot} \ne{6,3}
  \close
  \have {8} {P} \raa{3-7}
  \close
  \have {9} {(Q \to P) \to P} \ii{2-8}
  \close
  \have {10} {((P \to Q) \to Q) \to ((Q \to P) \to P)} \ii{1-9}
\end{nd}$
\end{center}
```

Boxes 1 and 2 come from step 2. Box 3 comes from step 5: the goal \( P \) is a letter, and the resources wait for \( P \to Q \), which nothing in hand gives.
:::

::: {#exr-four-kinds-of-task-b2}
[B2: Two directions]

Show that \( (P \wedge Q) \to R \dashv\vdash (P \wedge \neg R) \to \neg Q \).

::: {.enumerate options="label=(\alph*)"}
1. The search for \( (\Leftarrow) \) has reached the stage below. *Name the move, then complete it.*
2. Derive \( (\Rightarrow) \).
3. Which direction used a classical rule, and why did the other not need one?
:::

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge \neg R) \to \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {R}
  \close
  \have {10} {(P \wedge Q) \to R} \ii{2-9}
\end{nd}$
\end{center}
```
:::

::: {.solution}
(a) First the lines that need nothing new, \( P \) and \( Q \) by \( \rulename{\wedge E} \). Then the move is step 5: the current goal \( R \) is a letter, no resource gives it, and nothing clashes, so assume \( \neg R \) for \( \rulename{RAA} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge \neg R) \to \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \open
  \hypo {5} {\neg R}
  \have {6} {P \wedge \neg R} \ai{3,5}
  \have {7} {\neg Q} \ie{1,6}
  \have {8} {\bot} \ne{4,7}
  \close
  \have {9} {R} \raa{5-8}
  \close
  \have {10} {(P \wedge Q) \to R} \ii{2-9}
\end{nd}$
\end{center}
```

(b)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P \wedge \neg R}
  \have {3} {P} \ae{2}
  \have {4} {\neg R} \ae{2}
  \open
  \hypo {5} {Q}
  \have {6} {P \wedge Q} \ai{3,5}
  \have {7} {R} \ie{1,6}
  \have {8} {\bot} \ne{7,4}
  \close
  \have {9} {\neg Q} \ni{5-8}
  \close
  \have {10} {(P \wedge \neg R) \to \neg Q} \ii{2-9}
\end{nd}$
\end{center}
```

(c) \( (\Leftarrow) \) used \( \rulename{RAA} \) at line 9, because its goal \( R \) is a letter. \( (\Rightarrow) \) needed none, because its goal \( \neg Q \) is a negation, which \( \rulename{\neg I} \) builds. This is a claim about our two derivations only.

In words: to prove "if \( P \) and \( Q \), then \( R \)", it is enough to prove "if \( P \) and not \( R \), then not \( Q \)", a contrapositive in one hypothesis.
:::

::: {#exr-four-kinds-of-task-b3}
[B3: Derive or break, used later]

For each claim, derive it or break it. Try to break it first. To break a claim, give statements that make its counterexample set true.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg P \vee \neg Q \vdash \neg(P \vee Q) \)
2. \( \neg(P \leftrightarrow Q), \ P \vdash \neg Q \)
3. \( P \to Q, \ \neg P \to (R \vee Q), \ \neg R \vdash Q \)
4. \( P \to Q, \ \neg P \to (R \vee Q), \ \neg R \vdash P \)
5. \( (P \to Q) \to R, \ \neg R \vdash P \)
6. \( (P \to Q) \to R, \ \neg R \vdash Q \)
7. \( P \vee Q, \ P \vdash \neg Q \)
8. \( P \vee Q, \ \neg(P \wedge Q), \ P \vdash \neg Q \)
9. \( \neg(P \vee Q) \to P \vdash P \vee Q \)
:::
:::

::: {.solution}
The verdict comes first, then the derivation or the break. In every break, \( x \) is a real number.

(a) Breaks. Take \( P \): "\( x > 2 \)", \( Q \): "\( x > 0 \)", at \( x = 1 \). \( \neg P \) is true, so \( \neg P \vee \neg Q \) is true; \( Q \) is true, so \( P \vee Q \) is true and \( \neg(P \vee Q) \) is false. (The De Morgan law with this premise is \( \neg P \vee \neg Q \vdash \neg(P \wedge Q) \), @prp-de-morgan (c); here the wrong connective sits inside the negation.)

(b) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {P} \r{2}
  \close
  \have {8} {P \leftrightarrow Q} \bi{4-5,6-7}
  \have {9} {\bot} \ne{8,1}
  \close
  \have {10} {\neg Q} \ni{3-9}
\end{nd}$
\end{center}
```

This is the first box of @exr-reductio-and-classical-rules-b5 (f).

(c) Derive. Step 5: the goal \( Q \) is a letter, and the first two premises wait for \( P \) and for \( \neg P \), so \( \rulename{LEM} \) on \( P \). \( \rulename{DS} \) matches as stated in Section 2.3, refuting the **left** disjunct \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg P \to (R \vee Q)}
  \hypo {3} {\neg R}
  \have {4} {P \vee \neg P} \lem{}
  \open
  \hypo {5} {P}
  \have {6} {Q} \ie{1,5}
  \close
  \open
  \hypo {7} {\neg P}
  \have {8} {R \vee Q} \ie{2,7}
  \have {9} {Q} \ds{8,3}
  \close
  \have {10} {Q} \oe{4,5-6,7-9}
\end{nd}$
\end{center}
```

(d) Breaks. Take \( P \): "\( x > 5 \)", \( Q \): "\( x > 0 \)", \( R \): "\( x > 10 \)", at \( x = 1 \). \( P \) is false, so \( P \to Q \) is true; \( \neg P \) and \( Q \) are true, so \( \neg P \to (R \vee Q) \) is true; \( \neg R \) is true; and \( P \) is false. Trying to break it first: with \( P \) false, the premises force \( Q \) true and \( R \) false, and nothing clashes. The tempting step from "\( P \) gives \( Q \)" and "\( Q \) holds", which (c) derives, to \( P \) is affirming the consequent (Section 1.3).

(e) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to R}
  \hypo {2} {\neg R}
  \have {3} {\neg (P \to Q)} \mt{1,2}
  \open
  \hypo {4} {\neg P}
  \have {5} {P \to Q} \by{VI}{4}
  \have {6} {\bot} \ne{5,3}
  \close
  \have {7} {P} \raa{4-6}
\end{nd}$
\end{center}
```

(f) Breaks. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 2 \)", \( R \): "\( x > 3 \)", at \( x = 1 \). \( P \to Q \) is false, so \( (P \to Q) \to R \) is true; \( \neg R \) is true; and \( Q \) is false.

(g) Breaks; it is affirming a disjunct (Section 1.6). Take \( P \): "\( x > 1 \)", \( Q \): "\( x > 2 \)", at \( x = 3 \): \( P \vee Q \) and \( P \) are true, and \( \neg Q \) is false.

(h) Derive. The premise \( P \vee Q \) is not needed.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg (P \wedge Q)}
  \hypo {3} {P}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{3,4}
  \have {6} {\bot} \ne{5,2}
  \close
  \have {7} {\neg Q} \ni{4-6}
\end{nd}$
\end{center}
```

(i) Derive. Step 2 postpones the disjunction. The premise waits for \( \neg(P \vee Q) \), which \( \rulename{RAA} \) on the goal supplies; step 4 then manufactures the clash partner \( P \vee Q \) from line 3 by \( \rulename{\vee I} \), a manufactured clash and not a detour.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q) \to P}
  \open
  \hypo {2} {\neg (P \vee Q)}
  \have {3} {P} \ie{1,2}
  \have {4} {P \vee Q} \oi{3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {P \vee Q} \raa{2-5}
\end{nd}$
\end{center}
```

Read aloud: a statement whose failure would force one of its own sides holds.

(c) and (d), and (e) and (f), are look-alike pairs: each pair has the same premises and differs in the conclusion. (h) is (g) repaired by "not both". (a) is a De Morgan look-alike with the wrong connective inside.
:::

::: {#exr-four-kinds-of-task-b4}
[B4: Derive ⊥, or make every member true, used later]

For each list, either derive \( \bot \) from it, or give statements that make every member true at once.

::: {.enumerate options="label=(\alph*)"}
1. \( P \to Q, \ Q \to \neg P, \ P \)
2. \( P \vee Q, \ P \to \neg Q, \ Q \to \neg P \)
3. \( \neg(P \to Q), \ Q \vee \neg P \)
4. \( P \to (Q \wedge \neg Q) \)
5. \( \neg(P \vee Q), \ P \vee (Q \wedge R) \)
6. \( \neg(P \wedge Q), \ \neg(P \wedge \neg Q), \ \neg(\neg P \wedge Q) \)
:::
:::

::: {.solution}
(a) Derive \( \bot \): 4 \( Q \), \( \rulename{{\to}E} \) 1, 3; 5 \( \neg P \), \( \rulename{{\to}E} \) 2, 4; 6 \( \bot \), \( \rulename{\neg E} \) 3, 5.

(b) True at once. Take \( P \): "\( x > 0 \)", \( Q \): "\( x < 0 \)", at \( x = 1 \): \( P \vee Q \) is true; \( \neg Q \) is true, so \( P \to \neg Q \) is true; and \( Q \to \neg P \) is true, since \( Q \) is false.

(c) Derive \( \bot \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \to Q)}
  \hypo {2} {Q \vee \neg P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \open
  \hypo {8} {\neg P}
  \have {9} {P \to Q} \by{VI}{8}
  \have {10} {\bot} \ne{9,1}
  \close
  \have {11} {\bot} \oe{2,3-7,8-10}
\end{nd}$
\end{center}
```

(d) True at once, with \( P \) false (\( P \): "\( 0 = 1 \)", any \( Q \)). A member that mentions a contradiction is not itself a clash: with \( P \) false every member is true, so the claim that the list derives \( \bot \) breaks.

(e) Derive \( \bot \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \hypo {2} {P \vee (Q \wedge R)}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \have {5} {\bot} \ne{4,1}
  \close
  \open
  \hypo {6} {Q \wedge R}
  \have {7} {Q} \ae{6}
  \have {8} {P \vee Q} \oi{7}
  \have {9} {\bot} \ne{8,1}
  \close
  \have {10} {\bot} \oe{2,3-5,6-9}
\end{nd}$
\end{center}
```

(f) True at once, with \( P \) and \( Q \) both false (\( P \): "\( 1 > 2 \)", \( Q \): "\( 2 > 3 \)"): each conjunction has a false member, so each negation is true. Adding a fourth member \( \neg(\neg P \wedge \neg Q) \) gives a list from which \( \bot \) can be derived: the four exclude every way for \( P \) and \( Q \) to be. Use \( \rulename{LEM} \) on \( P \) and, inside each case, on \( Q \); each of the four cases builds the conjunction that one member negates, by \( \rulename{\wedge I} \), and clashes with it.

Section 4.7 shows that a list made true at once, as in (b), (d) and (f), is consistent.
:::

### C. Going deeper

::: {#exr-four-kinds-of-task-c1}
[C1: Exit check: the counterexample set, used later]

Let \( \Gamma \) be the list \( P \to (Q \vee R), \ Q \to S, \ R \to S \).

::: {.enumerate options="label=(\alph*)"}
1. Write the counterexample set of \( \Gamma \vdash P \to S \).
2. Show that it is inconsistent.
3. What does @prp-derivable-iff-negation-inconsistent conclude? Give also a direct derivation of \( \Gamma \vdash P \to S \), and compare the two.
4. Replace one premise so that the claim breaks, and break it.
:::
:::

::: {.solution}
(a) \( P \to (Q \vee R), \ Q \to S, \ R \to S, \ \neg(P \to S) \).

(b) The goal is \( \bot \), and the clash partner \( \neg(P \to S) \) is already on a line (Section 3.1), so aim at \( P \to S \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \hypo {2} {Q \to S}
  \hypo {3} {R \to S}
  \hypo {4} {\neg (P \to S)}
  \open
  \hypo {5} {P}
  \have {6} {Q \vee R} \ie{1,5}
  \open
  \hypo {7} {Q}
  \have {8} {S} \ie{2,7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {S} \ie{3,9}
  \close
  \have {11} {S} \oe{6,7-8,9-10}
  \close
  \have {12} {P \to S} \ii{5-11}
  \have {13} {\bot} \ne{12,4}
\end{nd}$
\end{center}
```

(c) By part (b) of the proposition, \( \Gamma \vdash P \to S \). The direct derivation is lines 1–3 and 5–12 of (b), renumbered: 11 lines. The route through the counterexample set adds the premise \( \neg(P \to S) \) and one \( \rulename{\neg E} \) line, and gains nothing here. It pays when the goal gives step 2 nothing (a letter, or a disjunction with no side in hand), and then it is step 5.

(d) For instance, replace \( R \to S \) by \( R \to T \). Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)", \( R \): "\( x < 2 \)", \( S \): "\( x > 3 \)", \( T \): "\( x < 10 \)", at \( x = 1 \). \( P \) and \( R \) are true, so \( Q \vee R \) and \( P \to (Q \vee R) \) are true; \( Q \to S \) is true, since \( Q \) is false; \( R \to T \) is true, since \( T \) is true; and \( P \to S \) is false, since \( S \) is false. So every member of the new counterexample set is true. Any replacement that a choice of statements breaks is accepted.

**Marking scheme.** (10 points)

- 2: the counterexample set, with \( \neg(P \to S) \), not \( \neg P \to S \) or \( P \to \neg S \).
- 3: the derivation of \( \bot \): \( P \to S \) derived (by a box whose cases of \( Q \vee R \) both end in \( S \), or by @exm-cases-on-hypothesis and @prp-implication-transitive), and \( \rulename{\neg E} \) outside every box.
- 2: the conclusion drawn by the proposition, and the direct derivation.
- 3: (d), a changed premise, with statements checked against all four members of the new counterexample set.

Fatal errors (0 for the step): \( \bot \) written inside the box of \( P \) and taken as the end; a "break" in (d) that leaves a premise false.
:::

::: {#exr-four-kinds-of-task-c2}
[C2: Challenge: Splitting an inconsistency, used later]

Let \( \Gamma \) be a list and \( \varphi \) a statement.

::: {.enumerate options="label=(\alph*)"}
1. Prove that if \( \Gamma, \varphi \) and \( \Gamma, \neg\varphi \) are both inconsistent, then so is \( \Gamma \).
2. Deduce: if \( \Gamma \) is consistent, then at least one of \( \Gamma, \varphi \) and \( \Gamma, \neg\varphi \) is consistent.
3. Does (b) say which one?
:::
:::

::: {.solution}
(a) Since \( \Gamma, \varphi \) is inconsistent, @prp-derivable-iff-negation-inconsistent (a) gives \( \Gamma \vdash \neg\varphi \). Since \( \Gamma, \neg\varphi \) is inconsistent, part (b) gives \( \Gamma \vdash \varphi \). So (iii) of @prp-inconsistent-derives-everything holds with \( \chi \) the statement \( \varphi \), and \( \Gamma \) is inconsistent.

(b) This is the contrapositive of (a): if both lists were inconsistent, \( \Gamma \) would be.

(c) No. It says that one of the two lists is consistent and gives no way to tell which. Deciding that would need a way to show a list consistent, which this chapter does not have.

Section 4.10 (optional) adds statements to a consistent list one at a time, in exactly this way.

**Marking scheme.** (10 points)

- 4: (a) obtains \( \Gamma \vdash \neg\varphi \) by part (a) of the proposition or \( \Gamma \vdash \varphi \) by part (b), and combines it with the other inconsistency, directly (by Cut, @lem-weakening-cut (b)) or by the other part.
- 3: (a) concludes by @prp-inconsistent-derives-everything, by @lem-weakening-cut (c) with one \( \rulename{\neg E} \), or by Cut (@lem-weakening-cut (b)).
- 2: (b) as the contrapositive.
- 1: (c) "no".

Fatal error: (b) claimed to show that a particular list is consistent.
:::

<!-- dependency ledger
exm-equivalence-search (example): ab = 0 and a != 0 give b = 0 (divide by a) | school algebra, AN1.1 (promised); a reading only, the derivations do not use it
exm-inconsistency-search (example): parity and divisibility of 1, 3, 6, 12 (6 is even, a multiple of 3, not of 4; 12 a multiple of 4 and 3; 1, 3 odd; 3 a multiple of 3) | arithmetic; checked by verify/ch03/exm-inconsistency-search.py
exm-inconsistency-search (example): the reading "no integer meets all four" follows the derivation line by line | inline (the derivation, read with the key)
exm-inconsistency-search (claim): in the Quick check after it, 3 and 9 are the integers in 1..10 meeting (1), (2), (4) | arithmetic; checked by verify/ch03/exm-inconsistency-search.py
exm-inconsistent-lists (example): with P "0 = 1" false, P -> Q and P -> not-Q are both true | an implication with a false hypothesis is true (the reading of -> in F1.1); 0 = 1 is false
exm-inconsistent-lists (example): the line counts 7, 8 and 4 of the table rows | inline (each row's derivation given in brief; row 3 cites prp-vacuous-implication)
exm-derive-or-break-search (example): (b) at x = 2 with x > 0, x > 1, x > 3 | arithmetic; checked by verify/ch03/exm-derive-or-break-search.py
exm-derive-or-break-search (claim): in the Quick check after it, replacing or by iff, or Q by R, in the first premise of (b) gives a derivable claim | derivation sketched inline in the solution; checked by truth table in verify/ch03/exm-derive-or-break-search.py; nothing depends on it
exr-four-kinds-of-task-b3 (solution): the breaks (a), (d), (f), (g) at the stated x | arithmetic; checked by verify/ch03/exr-four-kinds-of-task-b3.py
exr-four-kinds-of-task-b4 (solution): the lists (b), (d), (f) made true at the stated statements; (f) with the fourth member derives bot by LEM on P and Q | arithmetic; the derivation described inline; checked by truth table in verify/ch03/exr-four-kinds-of-task-b4.py
exr-four-kinds-of-task-b4 (solution): Section 4.7 shows that a list made true at once is consistent | plain pointer in a solution (F1.3 s07, text); nothing depends on it
exr-four-kinds-of-task-c1 (solution): (d) at x = 1 with x > 0, x > 5, x < 2, x > 3, x < 10 | arithmetic; checked by verify/ch03/exr-four-kinds-of-task-c1.py
exr-four-kinds-of-task-c2 (solution): Section 4.10 adds statements to a consistent list one at a time | plain pointer in a solution (F1.3 s10, lem-lindenbaum); nothing depends on it
-->
