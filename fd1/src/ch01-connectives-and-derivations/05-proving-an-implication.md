# Proving an Implication: the Rule of the Box

Sections 1.3 and 1.4 gave three rules. \( \rulename{\wedge I} \) builds a conjunction; \( \rulename{\wedge E} \) and \( \rulename{{\to}E} \) take a line apart or use it. With them we can **use** an implication, but we cannot **prove** one. Most theorems are implications, so this is the gap that matters most. This section fills it with the rule \( \rulename{{\to}I} \). The rule asks us to do something new: to assume a statement we do not know, inside a boundary that says where the assumption holds. The boundary is a **box**. Boxes change what an earlier line may cite, so at the end of the section we can say exactly what a derivation is.

## Supposing something we do not know

Here is a small theorem about a real number \( x \).

> If \( x > 2 \), then \( x^2 > 4 \).

The proof everyone would write goes like this. *Suppose \( x > 2 \). Then \( x > 0 \), so multiplying \( x > 2 \) by \( x \) gives \( x^2 > 2x \). Also \( 2x > 4 \). Hence \( x^2 > 4 \).* Then, often without saying it: *this proves that if \( x > 2 \), then \( x^2 > 4 \).*

Look at the first sentence. We do not know that \( x > 2 \). The number \( x \) is arbitrary, and it may well be \( 0 \). So "suppose \( x > 2 \)" asserts nothing. It opens a **temporary world**, one in which \( x > 2 \) holds, and asks what else holds there.

Inside that world, the sentences "\( x^2 > 2x \)", "\( 2x > 4 \)", and "\( x^2 > 4 \)" are true. Outside it they are not: at \( x = 0 \) all three are false. Only the last sentence of the proof leaves the temporary world. What it carries out is not "\( x^2 > 4 \)" but the implication "if \( x > 2 \), then \( x^2 > 4 \)", and that is true for every real \( x \).

None of the rules so far can do this. \( \rulename{\wedge I} \) writes a conjunction, and \( \rulename{\wedge E} \) and \( \rulename{{\to}E} \) write a piece of a line that is already there. So with those three rules, an implication can stand on a line only as a premise or as a piece of an earlier line. To prove "if \( x > 2 \), then \( x^2 > 4 \)" from nothing, we must be allowed to suppose.

A supposition is only safe if it has a boundary. Without one, the proof above could go on: "… Hence \( x^2 > 4 \). So \( x^2 > 4 \) for every real \( x \)." That is false at \( x = 0 \). The error is not in any computation; it is that a sentence from inside the temporary world was used outside it.

A derivation draws the boundary as a **box**. The assumption opens the box: it is written with a vertical bar to its left and a short horizontal rule under it. Every line derived under the assumption carries the same bar. When the box closes, the bar stops, and exactly one thing leaves: the implication from the assumption to the box's last line.

*To prove "if \( \varphi \), then \( \psi \)", assume \( \varphi \) in a box, reach \( \psi \) inside it, and close the box.*

## The introduction rule for implication

Here is the rule, as a pattern. The given part is now a **box**, not a line, and the rule cites it as a range of lines. Beside it, for reference, is the rule \( \rulename{{\to}E} \) of @def-rule-implication-elimination, so that the two rules for "implies" stand in one place.

::: {#def-rules-implication}
[Rules for Implication]

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

The left schema is the rule \( \rulename{{\to}I} \) (**implication-introduction**); the right one is \( \rulename{{\to}E} \) (@def-rule-implication-elimination). In \( \rulename{{\to}I} \), the line \( \varphi \) is an **assumption**, which opens the box, and the assumption is **discharged** when the box closes. The line \( \psi \) is a line **of that box itself**, not of a box inside it.
:::

As in every schema (@def-rule-schema), \( \varphi \) and \( \psi \) stand for any statements, replaced consistently, and \( i, j, k \) for line numbers. The drawing says most of the rule. Read it clause by clause.

1. **Open a box** whose first line is the assumption \( \varphi \). The assumption may be **any** statement: true or false, related to the premises or not. Its justification is simply "assumption". The price of assuming anything we like is the box.
2. **Inside the box**, work as usual. Every rule may be used. A line inside may cite the assumption, the lines derived inside the box so far, and the lines above the box that are still in force: the premises, and earlier lines that are not inside a box that has already closed.
3. **The last line** of the box is \( \psi \). It must be a line of this box itself, not a line of some further box opened inside it. (The drawing cannot show this, which is why the definition says it in words.)
4. **Close the box**, and write \( \varphi \to \psi \) on a later line outside it, in practice the very next line. The justification cites the **whole box** as the range \( \lines{i}{j} \), from its assumption to its last line, not its lines one by one.
5. **After the box closes**, nothing inside it may be cited again. The assumption is discharged, and everything derived under it goes with it. Only the implication leaves.

Clause 5 is the boundary of the temporary world. The subsection "Derivations, precisely" below turns it into an exact rule about which lines a line may cite.

The **degenerate case** is \( i = j \): a box of one line, whose assumption is also its last line. Then \( \psi \) is \( \varphi \), and the rule writes \( \varphi \to \varphi \). Nothing in the rule asks the box to contain more than its assumption.

*Why the rule is right.* The implication \( \varphi \to \psi \) claims only that \( \psi \) holds whenever \( \varphi \) does. The box shows exactly that: starting from \( \varphi \), and from facts that hold anyway, the rules lead to \( \psi \). Chapter 3 proves that every rule, \( \rulename{{\to}I} \) included, never leads from true premises to a false conclusion (@thm-soundness).

*Why the box closes.* The lines inside hold only under the assumption. If the assumption is false, as \( x > 2 \) is at \( x = 0 \), they may be false too. Closing the box is what stops them being used where the assumption is not in force.

## A first box: implication is transitive

The first result proved with a box is the chaining of implications. Section 1.4 used chains of implications forwards, firing each on a hypothesis already in hand. Here the hypothesis is not in hand, and we still want the chain.

::: {#prp-implication-transitive}
[Implication Is Transitive]

\( P \to Q, \ Q \to R \vdash P \to R \).
:::

::: {.idea}
Start from the goal. Its main connective is \( \to \), so the last line will be \( \rulename{{\to}I} \), and that needs a box that opens with \( P \) and ends with \( R \). Inside the box, the new goal is \( R \). Reason backwards: \( R \) is the conclusion of the premise \( Q \to R \), so \( \rulename{{\to}E} \) gives it once \( Q \) is on a line. And \( Q \) is the conclusion of \( P \to Q \), so \( \rulename{{\to}E} \) gives it from \( P \), which the box has just assumed.
:::

::: {.proof}
The following derivation has premises \( P \to Q \) and \( Q \to R \), and last line \( P \to R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
\end{nd}$
\end{center}
```

Line 3 opens a box with the assumption \( P \). Lines 4 and 5 apply \( \rulename{{\to}E} \) inside it, each citing a premise and a line of the box. Line 5, \( R \), is the last line of the box. Line 6 closes it and writes \( P \to R \), citing the box \( \lines{3}{5} \). By @def-derivable, this proves the proposition.
:::

Read the drawing once more. The bar that starts at line 3 stops after line 5. The statements \( P \), \( Q \), and \( R \) on lines 3–5 were never established outright; they hold inside the temporary world where \( P \) is assumed. Only \( P \to R \) stands outside, next to the premises.

Now give the letters some content. Let \( x \) be a real number, and let
\[
P : x > 3, \qquad Q : x^2 > 9, \qquad R : x^2 > 4 .
\]
The premise \( P \to Q \) holds: when \( x > 3 \), we have \( x > 0 \), so \( x^2 = x \cdot x > 3x > 9 \). The premise \( Q \to R \) holds because \( 4 < 9 \): if \( x^2 > 9 \), then \( x^2 > 4 \). With the premises in hand, lines 3–6 become a paragraph, one sentence per line.

| Line | Sentence |
|---|---|
| 3 | Suppose \( x > 3 \). |
| 4 | Since \( x > 3 \) implies \( x^2 > 9 \), we get \( x^2 > 9 \). |
| 5 | Since \( x^2 > 9 \) implies \( x^2 > 4 \), we get \( x^2 > 4 \). |
| 6 | Hence, if \( x > 3 \), then \( x^2 > 4 \). |

A practiced writer would compress this to "if \( x > 3 \), then \( x^2 > 9 > 4 \)": the same derivation with its joints hidden. When a proof is hard to follow, expanding it back into this form is how one finds the gap.

::: {.remark}
The same result holds with the two premises joined into one, \( (P \to Q) \wedge (Q \to R) \vdash P \to R \). Two \( \rulename{\wedge E} \) lines take the premise apart first (premise-directed), and the rest is the derivation above, renumbered.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to R)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {Q \to R} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{2,4}
  \have {6} {R} \ie{3,5}
  \close
  \have {7} {P \to R} \ii{4-6}
\end{nd}$
\end{center}
```
:::

The box opens with \( P \), the **hypothesis** of the goal \( P \to R \). That choice is forced, and getting it backwards is the most common misuse of the rule.

::: {.warning}
The box of \( \rulename{{\to}I} \) opens with the **hypothesis** of the implication to be proved, never with its conclusion. Argument B of Section 1.1 had to prove \( Q \to P \), with \( Q \): "\( n^2 \) is even" and \( P \): "\( n \) is even". It opened its box with \( P \), the conclusion, and reached \( Q \). Every line inside that box is correct. But a box from \( P \) to \( Q \) gives \( P \to Q \), the converse, and B's last sentence announced \( Q \to P \).
:::

That names the error of Argument B, as Section 1.1 promised: B used \( \rulename{{\to}I} \) with the box opened at the wrong end. The implication B needed, from the square back to the number, is a genuine theorem, and Chapter 2 proves it.

## Derivations, precisely

Section 1.2 defined a derivation without boxes (@def-box-free-derivation): every line after the premises applies a rule to **earlier** lines. With boxes, "earlier" is no longer enough. In the derivation of @prp-implication-transitive, line 5 is earlier than any line we might add after line 6. If a line 7 could cite line 5, it could write \( R \) outside the box, and the derivation would claim that \( R \) follows from the premises alone. That is the "\( x^2 > 4 \) for every \( x \)" error of the first subsection. So the full definition is mostly about which earlier lines are still **available**.

*A derivation is a list of lines in which every line is a premise, an assumption that opens a box, a repetition of a line still in force, or the result of one rule applied to lines and boxes that are still available.*

::: {#def-derivation}
[Derivation]

Fix a list of rules. A **derivation** is a finite list of numbered lines \( 1, 2, \dots, n \), each carrying one statement and a justification, together with a set of **boxes**. A box is a block of consecutive lines whose first line is an assumption. Any two boxes are either disjoint or **one inside the other**. A box ends at one of its lines and is **closed** after it. The **last line** of the derivation lies outside every box.

**The scope rule.** Line \( i \) is **available** at line \( k \) if \( i < k \) and **every** box containing line \( i \) also contains line \( k \). A box is **available** at line \( k \) if it ends before line \( k \) and the boxes other than itself that contain it are **exactly** the boxes containing line \( k \). A line may cite only lines and boxes available at it.

Every line is exactly one of the following:

::: {.enumerate options="label=(D\arabic*)"}
1. a **premise**; the premises are the first lines, above every box, with a short rule under the last of them;
2. an **assumption**, which may be **any** statement, and opens a new box;
3. a **repetition** of the statement on a line available at this one, justified "R" and the line repeated;
4. the conclusion of **one** rule of the list, applied to lines and boxes available at this one, such that this line and the cited lines and boxes form an instance of the rule's schema.
:::

Clause (D3) is the rule \( \rulename{R} \) (**repetition**), whose schema is

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {} {\vdots}
  \have {k} {\varphi} \r{i}
\end{nd}$
\end{center}
```

where line \( i \) must be available at line \( k \).
:::

In words, clause by clause. (D1) Premises are the givens; they hold throughout, and they are available at every later line, since no box contains them. (D2) We may assume anything, but the assumption opens a box, and that is the price. (D3) A statement already established, and still in force, may be written again. (D4) Everything else is one step of one rule, applied to material that is still in force.

The scope rule is the definition's real content. Line \( i \) is available at line \( k \) when every assumption that line \( i \) was derived under is still in force at line \( k \). So:

- a line in no box is available at every later line;
- a line inside a box is available further down that box, and inside every box opened within it;
- once its box closes, the line is available nowhere.

*Open a box, close a box: an assumption lives exactly as long as its box.*

A closed box, cited as a whole by \( \rulename{{\to}I} \), must sit directly in the part of the derivation where the citing line is. The citing line may not lie outside a box that contains the cited box (that box has closed too), nor inside a further box opened after the cited box ended.

*Well defined.* Whether a line is available is decided by looking at the boxes; nothing about the meaning of the statements enters. Checking a derivation stays mechanical.

*Nothing earlier changes.* A derivation with no boxes is a box-free derivation of @def-box-free-derivation for the same rules with \( \rulename{R} \) added: with no boxes, "available" means just "earlier". So every derivation of Sections 1.2–1.4 is a derivation in the new sense, and @def-derivable is read from now on with this definition. The sequent \( \Gamma \vdash \psi \) still means: **there is** a derivation whose premises all belong to \( \Gamma \) and whose last line is \( \psi \). Its last line lies in no box, so it depends on the premises and on nothing that was merely assumed.

Two more words will be needed in Chapter 3, where the rules are proved trustworthy (@thm-soundness). The **length** of a derivation is its number of lines. The **context** of a line is the list of the premises together with the assumptions of every box containing that line: the statements the line depends on. The context of the last line is just the premises, since the last line lies in no box.

*Repetition.* Most rules may cite an available line directly, so \( \rulename{R} \) is rarely needed. It is needed when a rule wants a statement as a line **of a particular box**: \( \rulename{{\to}I} \) wants its \( \psi \) as a line of the box itself (clause 3 of the reading). The typical use copies a line into a box opened below it.

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {} {\vdots}
  \open
  \hypo {j} {\psi}
  \have {} {\vdots}
  \have {k} {\varphi} \r{i}
  \close
\end{nd}$
\end{center}
```

Line \( i \) is available at line \( k \) exactly when every box containing line \( i \) contains line \( k \); in this drawing, line \( i \) is in no box that has closed, so the copy is legal. The worked example @exm-first-boxes below uses it.

::: {.warning}
A box that is never closed cannot end a derivation. If the last line of a list is still inside a box, it depends on an assumption that was never discharged, and @def-derivation does not count the list as a derivation at all. "Suppose \( x > 2 \). Then \( x^2 > 4 \)", with nothing after it, proves nothing about \( x \): the implication is the only thing the supposition was allowed to produce, and it was never written.
:::

## How to check a derivation

Section 1.2 checked a line by asking which rule it uses, which lines it cites, and whether they are earlier. With boxes the third question becomes: **are they available here?** For each line after the premises, ask:

1. **Which rule?** Name it. An assumption opens a box; \( \rulename{R} \) repeats; every other line applies one rule.
2. **Which lines or boxes does it cite, and do they form an instance of the rule's schema?** \( \rulename{{\to}E} \) cites an implication and exactly its hypothesis; \( \rulename{{\to}I} \) cites one box, whose assumption and last line must be the two sides of the implication written.
3. **Are they available here?** Apply the scope rule to each cited line and box.

*Finding a derivation may need an idea; checking one never does.* Here is the check run on the derivation of @prp-implication-transitive. The last column lists the context of each line.

| Line | Which rule? | Cites | Available? | Context |
|---|---|---|---|---|
| 1, 2 | premises (D1) | — | — | \( P \to Q \), \( Q \to R \) |
| 3 | assumption (D2); opens the box 3–5 | — | — | \( P \to Q \), \( Q \to R \), \( P \) |
| 4 | \( \rulename{{\to}E} \): \( Q \) from \( P \to Q \) and \( P \) | 1, 3 | 1 is in no box; 3 is in box 3–5, which contains 4 | \( P \to Q \), \( Q \to R \), \( P \) |
| 5 | \( \rulename{{\to}E} \): \( R \) from \( Q \to R \) and \( Q \) | 2, 4 | 2 is in no box; 4 is in box 3–5, which contains 5 | \( P \to Q \), \( Q \to R \), \( P \) |
| 6 | \( \rulename{{\to}I} \): \( P \to R \) from the box | box 3–5 | the box ended at 5; neither it nor 6 lies in another box | \( P \to Q \), \( Q \to R \) |

Every line passes, and the last line lies in no box. The context column shows the temporary world: it grows by \( P \) at line 3, and shrinks back at line 6.

## An assumption used outside its box

Now watch the scope rule catch an error. Take the derivation of @prp-implication-transitive and add one line, as a careless writer might.

::: {#exm-illegal-citation}
[A line cited from a closed box]

Is the following a derivation? If it were, what would it show?

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (line 7 repeats a line of a closed box)
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
  \have {7} {R} \r{5}
\end{nd}$
\end{center}
```
:::

::: {.solution}
No. Lines 1–6 are the derivation of @prp-implication-transitive, and line 7 claims to be a repetition (D3). Line 5 lies inside the box \( \lines{3}{5} \), and that box does not contain line 7. By the scope rule, line 5 is not available at line 7, and (D3) repeats only an available line. So line 7 is illegal.

If it were allowed, the list would show \( P \to Q, \ Q \to R \vdash R \), and that would be a disaster. Let \( x \) be a real number, and take \( P \): "\( x > 3 \)", \( Q \): "\( x > 2 \)", \( R \): "\( x > 1 \)". Both premises are true whatever \( x \) is. At \( x = 0 \) the conclusion \( x > 1 \) is false. A step that leads from true premises to a false conclusion cannot be a step of proof.
:::

The error is easy to see in a drawing, where the bar visibly stops after line 5. In prose there is no bar, and the same error hides.

::: {.warning}
The assumption of a closed box is gone, and so is everything derived from it. Here is a typical slip. *"Suppose \( x > 1 \). Then \( x^2 = x \cdot x > 1 \cdot x > 1 \). Hence \( x > 1 \) implies \( x^2 > 1 \). Moreover \( x^3 = x \cdot x^2 > 1 \), so \( x^3 > 1 \)."* The sentence "Hence …" closed the box. The last sentence still uses \( x > 1 \) and \( x^2 > 1 \), and so it asserts \( x^3 > 1 \) with no hypothesis, which fails at \( x = 0 \). The repair is to keep the box open until everything that needs \( x > 1 \) is done, and to conclude "if \( x > 1 \), then \( x^2 > 1 \) and \( x^3 > 1 \)".
:::

::: {.check}
In the derivation below, which of lines 3 to 7 may cite line 2 individually?

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \ie{1,2}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {Q \wedge P} \ai{3,2}
  \close
  \have {6} {P \to (Q \wedge P)} \ii{2-5}
  \have {7} {(P \to Q) \wedge (P \to (Q \wedge P))} \ai{1,6}
\end{nd}$
\end{center}
```
:::

::: {.solution}
Lines 3, 4, and 5. They lie in the box \( \lines{2}{5} \), the only box containing line 2, so line 2 is available to each of them. Line 6 cites the box \( \lines{2}{5} \) as a whole, which is what \( \rulename{{\to}I} \) requires; it does not cite line 2 by itself, and could not, since line 6 is outside the box. Line 7 may not cite line 2 either, for the same reason.
:::

## More boxes: from nothing, and one inside another

The next three derivations are short, and each shows one new feature of boxes.

::: {#exm-first-boxes}
[First boxes]

Find a derivation of each sequent.

::: {.enumerate options="label=(\alph*)"}
1. \( \vdash P \to P \).
2. \( \vdash P \to (Q \to P) \).
3. \( P \to (Q \to R) \vdash Q \to (P \to R) \).
:::
:::

::: {.solution}
(a) *Idea.* The goal is an implication, so open a box with its hypothesis \( P \); the box must end with \( P \). The assumption is already \( P \), so the box can end at once: this is the degenerate case of \( \rulename{{\to}I} \).

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P}
  \close
  \have {2} {P \to P} \ii{1-1}
\end{nd}$
\end{center}
```

Line 1 is an assumption (D2) and opens the box \( \lines{1}{1} \), whose last line is \( P \). Line 2 cites that box, which ended before line 2 and, like line 2, lies in no other box. There are no premises, so this shows \( \vdash P \to P \). It is the first statement in the book derivable from **no** premises. Section 1.2 observed that nothing could be: every rule of Sections 1.3 and 1.4 (@def-rules-conjunction, @def-rule-implication-elimination) cites at least one line, so a derivation using only them needs a first line, and that line must be a premise. A box is what escapes: its first line is an assumption, and the assumption is discharged before the end.

(b) *Idea.* Read the goal from the outside in. Its main connective is the first \( \to \), so open a box with \( P \); the new goal is \( Q \to P \), again an implication, so open a box with \( Q \) inside the first. The inner box must end with \( P \). The statement \( P \) is already available, on line 1, but \( \rulename{{\to}I} \) wants it as a line **of the inner box itself**. That is the job of \( \rulename{R} \).

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P}
  \open
  \hypo {2} {Q}
  \have {3} {P} \r{1}
  \close
  \have {4} {Q \to P} \ii{2-3}
  \close
  \have {5} {P \to (Q \to P)} \ii{1-4}
\end{nd}$
\end{center}
```

Line 3 is legal: the only box containing line 1, the box \( \lines{1}{4} \), also contains line 3. The boxes are nested, and the inner one closes first. No line cites line 2 on its own: the assumption \( Q \) is never used, and nothing in \( \rulename{{\to}I} \) requires it to be. An implication whose conclusion is already known holds whatever its hypothesis.

(c) *Idea.* The goal \( Q \to (P \to R) \) asks for a box with \( Q \) and, inside it, a box with \( P \) ending in \( R \). Inside both boxes, work from the premise: its main connective is the first \( \to \), with hypothesis \( P \), so \( \rulename{{\to}E} \) fires on the assumption \( P \) and gives \( Q \to R \). That implication fires on the assumption \( Q \) and gives \( R \), the inner goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \ie{1,3}
  \have {5} {R} \ie{4,2}
  \close
  \have {6} {P \to R} \ii{3-5}
  \close
  \have {7} {Q \to (P \to R)} \ii{2-6}
\end{nd}$
\end{center}
```

Line 5 cites line 2 from inside the inner box: every box containing line 2 (only \( \lines{2}{6} \)) contains line 5. So the order of two hypotheses does not matter. For real numbers \( a \) and \( x \), the derivation turns "if \( a > 0 \), then (if \( x > 1 \), then \( ax > a \))" into "if \( x > 1 \), then (if \( a > 0 \), then \( ax > a \))".
:::

In (b) and (c) the goal told us which boxes to open, and in which order: the outermost \( \to \) of the goal gives the outermost box. This is the goal-directed move of this section. *An implication goal opens a box with its hypothesis; the new goal is its conclusion.*

## Two hypotheses, or one at a time

A theorem with two hypotheses, "if \( x > 0 \) and \( y > 0 \), then \( xy > 0 \)", is often written with one hypothesis at a time: "let \( x > 0 \); then, if \( y > 0 \), \( xy > 0 \)". The two forms are \( (P \wedge Q) \to R \) and \( P \to (Q \to R) \). Each can be derived from the other, so a writer may use whichever reads better.

::: {#prp-curry}
[Two Hypotheses or One at a Time]

\( (P \wedge Q) \to R \vdash P \to (Q \to R) \), and \( P \to (Q \to R) \vdash (P \wedge Q) \to R \).
:::

*Try it first (ten minutes): for the first claim, which boxes will you open, and in which order?*

::: {.idea}
The tempting first move is premise-directed: use \( (P \wedge Q) \to R \) at once. But \( \rulename{{\to}E} \) needs \( P \wedge Q \) on a line, and at the start nothing is on a line except the premise. So start from the goal. Its main connective is the first \( \to \), so open a box with \( P \); the new goal \( Q \to R \) is again an implication, so open a box with \( Q \) inside the first. Now both \( P \) and \( Q \) are available, \( \rulename{\wedge I} \) builds \( P \wedge Q \), and the premise fires. For the second claim the goal \( (P \wedge Q) \to R \) asks for one box, with \( P \wedge Q \); take the assumption apart and feed the halves to the premise one at a time, \( P \) first because it is the premise's outer hypothesis.

*Before reading on: in the first derivation, which lines may line 4 cite, and why may line 6 cite the box 3–5 but not line 5 on its own?*
:::

::: {.proof}
For the first claim, the following is a derivation with premise \( (P \wedge Q) \to R \) and last line \( P \to (Q \to R) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {Q \to R} \ii{3-5}
  \close
  \have {7} {P \to (Q \to R)} \ii{2-6}
\end{nd}$
\end{center}
```

Line 4 may cite lines 1, 2, and 3: line 1 lies in no box, the only box containing line 2 (the box \( \lines{2}{6} \)) contains line 4, and both boxes containing line 3 contain line 4. Line 6 may cite the box \( \lines{3}{5} \), because that box has ended and both it and line 6 lie in the box \( \lines{2}{6} \) and in no other. Line 6 may not cite line 5 on its own, because the box \( \lines{3}{5} \) contains line 5 and not line 6.

For the second claim, the following is a derivation with premise \( P \to (Q \to R) \) and last line \( (P \wedge Q) \to R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {Q \to R} \ie{1,3}
  \have {6} {R} \ie{5,4}
  \close
  \have {7} {(P \wedge Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```

Every line cites line 1, which lies in no box, or lines of the box \( \lines{2}{6} \) from inside it. By @def-derivable, the two derivations prove the two claims.
:::

In the first derivation the boxes are nested, and the inner one closes first: an assumption made later is discharged earlier. That is the general pattern, forced by @def-derivation, since two boxes are either disjoint or one inside the other.

Read mathematically, the first claim turns "if \( x > 0 \) and \( y > 0 \), then \( xy > 0 \)" into "if \( x > 0 \), then (if \( y > 0 \), then \( xy > 0 \))", and the second turns it back. The two forms say the same thing, one hypothesis at a time or both at once. Section 2.4 gives a name and a symbol to a pair of statements that, like these two, can each be derived from the other.

::: {.check}
To show \( Q \wedge R \vdash (P \to Q) \wedge (S \to R) \), does the derivation need one box or two?
:::

::: {.solution}
Two. The goal's main connective is \( \wedge \), which opens no box, so the goal splits into the two implications \( P \to Q \) and \( S \to R \) (goal-directed \( \rulename{\wedge I} \)). Each is proved by \( \rulename{{\to}I} \), with its own box, opened by its own hypothesis. Inside each box, \( \rulename{\wedge E} \) on the premise gives the half that box needs.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q \wedge R}
  \open
  \hypo {2} {P}
  \have {3} {Q} \ae{1}
  \close
  \have {4} {P \to Q} \ii{2-3}
  \open
  \hypo {5} {S}
  \have {6} {R} \ae{1}
  \close
  \have {7} {S \to R} \ii{5-6}
  \have {8} {(P \to Q) \wedge (S \to R)} \ai{4,7}
\end{nd}$
\end{center}
```

The two boxes are disjoint: the first closes before the second opens. Line 8 may cite lines 4 and 7, which lie in no box.
:::

## What the rule sounds like

Every rule is something mathematicians already say. The table adds the rules of this section to those of Sections 1.3 and 1.4: the sentence that performs the rule in a written proof and, for readers who meet a proof assistant, the Lean code that does the same. Nothing later depends on the last column.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{{\to}I} \) | "Assume \( P \). … Hence \( Q \)." | `intro hp` |
| \( \rulename{R} \) | "As shown above, \( P \)." | `exact hp` |

The sentence for \( \rulename{{\to}I} \) is the one to watch. "Assume \( P \)" opens a box, and "hence \( Q \)" is its last line. The closing line, "so \( P \) implies \( Q \)", is usually left unsaid in written mathematics. It is still there: the box closes whether or not anyone says so. It is also the line Argument B got wrong. Chapter 5 turns sentences like these into a dictionary between derivations and prose.

Every derivation in this section was built from the rules alone, and each repeated in full whatever it needed. Section 2.3 lets a sequent already derived be used as a single line of a later derivation; until then, a derivation that needs an earlier result must repeat its steps.

## Exercises

### A. Check your understanding

::: {#exr-proving-an-implication-a1}
[A1]

Consider the following derivation, whose justifications are missing.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \by{(i)}{}
  \have {5} {R} \by{(ii)}{}
  \close
  \have {6} {P \to R} \by{(iii)}{}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Write the schema of \( \rulename{{\to}I} \) from memory, and state the condition that the drawing cannot show.
2. Fill in the justifications (i), (ii), (iii), and say what the derivation shows, written with \( \vdash \).
3. Which of lines 1–5 are available at line 6? What is the context of line 5?
4. Someone extends the derivation by a line 7, the statement \( R \) justified by \( \rulename{{\to}E} \) 6, 3. Is the result a derivation? If not, name the clause of @def-derivation that line 7 breaks.
5. In the first derivation in the proof of @prp-curry, why is line 4 available at line 5? And why is the inner box closed before the outer one?
6. In the same derivation, which rule produces line 5, and which lines does it cite?
:::
:::

::: {.solution}
(a) The schema is the left one in @def-rules-implication: a box from an assumption \( \varphi \) on line \( i \) to a line \( \psi \) on line \( j \), and then \( \varphi \to \psi \) on line \( k \), justified \( \rulename{{\to}I} \) \( \lines{i}{j} \). The condition the drawing cannot show: \( \psi \) is a line of that box itself, not of a box inside it.

(b) (i) \( \rulename{{\to}E} \) 1, 3; (ii) \( \rulename{{\to}E} \) 4, 2; (iii) \( \rulename{{\to}I} \) \( \lines{3}{5} \). The derivation shows \( P \to (Q \to R), \ Q \vdash P \to R \).

(c) Lines 1 and 2. Lines 3, 4, and 5 lie in the box \( \lines{3}{5} \), which does not contain line 6. (The box \( \lines{3}{5} \) as a whole is available at line 6, which is why (iii) may cite it.) The context of line 5 is \( P \to (Q \to R) \), \( Q \), \( P \): the two premises and the assumption of the one box containing it.

(d) No. Line 6 is available at line 7, but line 3 is not: it lies in the box \( \lines{3}{5} \), which does not contain line 7. So line 7 applies a rule to a line that is not available, which (D4) forbids.

(e) Line 4 lies in two boxes, \( \lines{2}{6} \) and \( \lines{3}{5} \), and both contain line 5; so by the scope rule line 4 is available at line 5. The inner box \( \lines{3}{5} \) lies inside the outer box \( \lines{2}{6} \), and two boxes are either disjoint or one inside the other, so the inner box must end first. Read off the goal: the inner box proves \( Q \to R \), which is the last line the outer box needs.

(f) \( \rulename{{\to}E} \), citing line 1, the implication \( (P \wedge Q) \to R \), and line 4, its hypothesis \( P \wedge Q \).
:::

### B. Practice

::: {#exr-proving-an-implication-b1}
[B1: Swapping inside an implication]

Show that \( \vdash (P \wedge Q) \to (Q \wedge P) \) by a derivation. Then write the argument as a paragraph of prose, one sentence per line.
:::

::: {.solution}
The goal has main connective \( \to \), so the derivation opens a box with \( P \wedge Q \) and must end it with \( Q \wedge P \). Inside, the goal is a conjunction, whose halves \( \rulename{\wedge E} \) supplies from the assumption.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {Q} \ae{1}
  \have {4} {Q \wedge P} \ai{3,2}
  \close
  \have {5} {(P \wedge Q) \to (Q \wedge P)} \ii{1-4}
\end{nd}$
\end{center}
```

It has no premises, and its last line lies outside the box, so it shows \( \vdash (P \wedge Q) \to (Q \wedge P) \).

In prose: *Assume \( P \) and \( Q \). In particular \( P \) holds, and in particular \( Q \) holds. Hence \( Q \) and \( P \) both hold. This proves that if \( P \) and \( Q \), then \( Q \) and \( P \).* Compared with @prp-and-commutes, the premise \( P \wedge Q \) has become an assumption, and the conclusion has become an implication that depends on nothing.
:::

::: {#exr-proving-an-implication-b2}
[B2: An assumption that is not used]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( Q \vdash P \to Q \), and say which line needs repetition.
2. Show that \( \vdash (P \wedge Q) \to (R \to Q) \).
3. Let \( x \) be a real number. Write the instance of (a) with \( Q \): "\( x^2 \ge 0 \)" and \( P \): "\( x > 5 \)" as an English sentence, and say which hypothesis its proof never uses.
:::
:::

::: {.solution}
(a) The goal is an implication, so open a box with \( P \); its last line must be \( Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \r{1}
  \close
  \have {4} {P \to Q} \ii{2-3}
\end{nd}$
\end{center}
```

Line 3 needs repetition: \( \rulename{{\to}I} \) wants \( Q \) as a line of the box \( \lines{2}{3} \) itself. It is legal because line 1 lies in no box.

(b) Two implications, so two nested boxes: one with \( P \wedge Q \), and inside it one with \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge Q}
  \have {2} {Q} \ae{1}
  \open
  \hypo {3} {R}
  \have {4} {Q} \r{2}
  \close
  \have {5} {R \to Q} \ii{3-4}
  \close
  \have {6} {(P \wedge Q) \to (R \to Q)} \ii{1-5}
\end{nd}$
\end{center}
```

Line 4 is legal: the only box containing line 2 also contains line 4. (Applying \( \rulename{\wedge E} \) to line 1 inside the inner box works as well.)

(c) "\( x^2 \ge 0 \); therefore, if \( x > 5 \), then \( x^2 \ge 0 \)." The hypothesis \( x > 5 \) is never used: its box only repeats what was known.
:::

::: {#exr-proving-an-implication-b3}
[B3: Unwinding an absolute value]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \to Q, \ P \to R \vdash P \to (Q \wedge R) \).
2. Let \( x \) be a real number. Use (a) to deduce "if \( \abs{x - 2} < 1 \), then \( 1 < x < 3 \)" from the two facts "if \( \abs{x - 2} < 1 \), then \( x > 1 \)" and "if \( \abs{x - 2} < 1 \), then \( x < 3 \)". Write the resulting argument as prose.
:::
:::

::: {.solution}
(a) The goal is an implication, so assume \( P \), and reach \( Q \wedge R \) by getting each half.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {P \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,3}
  \have {6} {Q \wedge R} \ai{4,5}
  \close
  \have {7} {P \to (Q \wedge R)} \ii{3-6}
\end{nd}$
\end{center}
```

The assumption on line 3 is cited twice, by lines 4 and 5: a line is not used up when it is cited.

(b) Take \( P \): "\( \abs{x - 2} < 1 \)", \( Q \): "\( x > 1 \)" and \( R \): "\( x < 3 \)". The two facts are the premises \( P \to Q \) and \( P \to R \), and \( Q \wedge R \) is \( 1 < x < 3 \). The derivation in (a), with these statements put in for the letters, is a derivation of \( P \to (Q \wedge R) \) from the two facts.

In prose: *Suppose \( \abs{x - 2} < 1 \). Then \( x > 1 \) by the first fact, and \( x < 3 \) by the second. Hence \( 1 < x < 3 \). This proves that \( \abs{x - 2} < 1 \) implies \( 1 < x < 3 \).*
:::

::: {#exr-proving-an-implication-b4}
[B4: Putting a derivation in order]

Here are nine lines, each a statement with its justification. Seven of them, in the right order and with the right boxes, form a derivation of \( P \to (Q \to R) \vdash Q \to (P \to R) \). Give the order, and say where each box opens and closes. Then say why each of the other two lines cannot be used.

::: {.enumerate options="label=(\roman*)"}
1. \( P \to R \), by \( \rulename{{\to}I} \) on the box from \( P \) to \( R \).
2. \( Q \), assumption.
3. \( R \), by \( \rulename{{\to}E} \) from \( Q \to R \) and \( Q \).
4. \( R \), by \( \rulename{R} \), repeating the line \( R \) of (iii), written directly below (i).
5. \( P \to (Q \to R) \), premise.
6. \( Q \to (P \to R) \), by \( \rulename{{\to}I} \) on the box from \( Q \) to \( P \to R \).
7. \( R \), assumption, opening the box for the \( \rulename{{\to}I} \) that proves \( P \to R \).
8. \( Q \to R \), by \( \rulename{{\to}E} \) from \( P \to (Q \to R) \) and \( P \).
9. \( P \), assumption.
:::
:::

::: {.solution}
The order is (v), (ii), (ix), (viii), (iii), (i), (vi), with one box opened by (ii) and closed after (i), and a second box inside it, opened by (ix) and closed after (iii). This is the derivation of @exm-first-boxes (c).

It is the only admissible order. The premise (v) comes first. The last line (vi) needs a box from \( Q \) to \( P \to R \), so (ii) opens a box whose last line is (i). Line (i) needs a box from \( P \) to \( R \), which must lie inside the box of \( Q \), since (i) is a line of that box; so (ix) opens the inner box, whose last line is (iii). Inside it, (viii) needs the premise and (ix), and (iii) needs (viii) and (ii). Opening the box of \( P \) first and the box of \( Q \) inside it would not do: the inner \( \rulename{{\to}I} \) would then give \( Q \to R \), and the outer one \( P \to (Q \to R) \), the premise again.

(iv) cannot be used where it is placed. Directly below (i), the inner box has closed, and line (iii) lies inside it; so (iii) is not available there, and (D3) repeats only an available line (the scope rule of @def-derivation). It is the error of @exm-illegal-citation.

(vii) cannot be used. \( \rulename{{\to}I} \) proves \( P \to R \) from a box opened by \( P \), the **hypothesis**. A box opened by \( R \) would prove an implication with hypothesis \( R \): the converse error of Argument B.
:::

### C. Going deeper

::: {#exr-proving-an-implication-c1}
[C1: Exit check: a line from a closed box]

A student wants to show \( (P \wedge Q) \to R \vdash (P \to (Q \to R)) \wedge (Q \to (P \to R)) \), and offers the following derivation. Lines 1–7 are the first derivation in the proof of @prp-curry.

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (line 10 repeats a line of a closed box)
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {Q \to R} \ii{3-5}
  \close
  \have {7} {P \to (Q \to R)} \ii{2-6}
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {R} \r{5}
  \close
  \have {11} {P \to R} \ii{9-10}
  \close
  \have {12} {Q \to (P \to R)} \ii{8-11}
  \have {13} {(P \to (Q \to R)) \wedge (Q \to (P \to R))} \ai{7,12}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Find the first illegal line, and name the clause of @def-derivation that it breaks.
2. Is the student's conclusion derivable from the premise? Justify your answer.
3. The student defends line 10: "at line 10, both \( P \) and \( Q \) are assumed, exactly as they were at line 5, so \( R \) holds there too." Explain why @def-derivation does not accept this defense, and show by an instance with real numbers that the move "repeat a line of a closed box" cannot be allowed.
:::
:::

::: {.solution}
[Hint 1]

For (a), check each line's citations against the scope rule; for (b), keep the student's idea and change one step.
:::

::: {.solution}
[Hint 2]

For (b), inside the box of \( P \) at line 9, the assumptions \( Q \) (line 8) and \( P \) (line 9) are both available. What did lines 4 and 5 do with such a pair?
:::

::: {.solution}
(a) Line 10 is the first illegal line. It claims to repeat line 5 by (D3), but line 5 lies in the boxes \( \lines{2}{6} \) and \( \lines{3}{5} \), and neither contains line 10. So line 5 is not available at line 10, and (D3) allows repeating only an available line. Lines 1–9 are correct, and lines 11–13 would be correct if line 10 were.

(b) Yes: the sequent is derivable. Replace line 10 by two lines that do inside the new boxes what lines 4 and 5 did inside the old ones.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {Q \to R} \ii{3-5}
  \close
  \have {7} {P \to (Q \to R)} \ii{2-6}
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {P \wedge Q} \ai{9,8}
  \have {11} {R} \ie{1,10}
  \close
  \have {12} {P \to R} \ii{9-11}
  \close
  \have {13} {Q \to (P \to R)} \ii{8-12}
  \have {14} {(P \to (Q \to R)) \wedge (Q \to (P \to R))} \ai{7,13}
\end{nd}$
\end{center}
```

Every box containing line 8 or line 9 contains line 10, and line 1 lies in no box; the other lines check as before. The student's derivation was wrong and its conclusion right: a flawed argument can have a true conclusion.

(c) Availability is about **boxes**, not about which statements happen to be assumed. The boxes \( \lines{8}{11} \) and \( \lines{9}{10} \) of the student's derivation are new boxes; that their assumptions repeat those of the old boxes gives line 10 no access to what was derived inside the old ones. And the move, once allowed, can be used anywhere. Used outside every box, as a line 8 "\( R \), R 5" after lines 1–7, it would derive \( (P \wedge Q) \to R \vdash R \). Let \( x \) be a real number, and take \( P \): "\( x > 2 \)", \( Q \): "\( x > 3 \)" and \( R \): "\( x > 1 \)". The premise "if \( x > 2 \) and \( x > 3 \), then \( x > 1 \)" is true whatever \( x \) is, and at \( x = 0 \) the conclusion \( x > 1 \) is false. A move that leads from a true premise to a false conclusion cannot be a step of proof.

**Marking scheme.** (10 points)

- 3: names line 10, because line 5 lies in boxes that do not contain it.
- 3: gives any correct derivation of the sequent, every citation available.
- 1: says the conclusion is derivable although the argument is wrong.
- 3: explains that availability depends on boxes, not on repeated assumptions, with an instance where the move leads from a true premise to a false conclusion.

Fatal errors (0 for the step): naming line 5 or line 9; claiming the sequent is not derivable; refuting the conclusion instead of the move.
:::

::: {#exr-proving-an-implication-c2}
[C2: A hypothesis inside a hypothesis]

Show that \( (P \to Q) \to (P \to R) \vdash P \to (Q \to R) \). Then say, in one sentence, why the premise cannot be used until a third box is opened.
:::

::: {.solution}
[Hint 1]

Read the boxes off the goal. The premise's hypothesis is \( P \to Q \): what would you need to derive it?
:::

::: {.solution}
[Hint 2]

Which rule proves an implication, and what does that rule need?
:::

::: {.solution}
The goal \( P \to (Q \to R) \) asks for a box with \( P \) and, inside it, a box with \( Q \) whose last line is \( R \). The premise gives \( P \to R \) as soon as we have \( P \to Q \), and \( P \to R \) with the available \( P \) gives \( R \). So the task is to derive \( P \to Q \) inside the box of \( Q \), and that takes a third box.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to (P \to R)}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {P \to R} \ie{1,6}
  \have {8} {R} \ie{7,2}
  \close
  \have {9} {Q \to R} \ii{3-8}
  \close
  \have {10} {P \to (Q \to R)} \ii{2-9}
\end{nd}$
\end{center}
```

Line 5 is a legal repetition: both boxes containing line 3 contain line 5. Line 8 may cite line 2 because the box \( \lines{2}{9} \), the only box containing line 2, contains line 8.

The premise's hypothesis is the implication \( P \to Q \), which \( \rulename{{\to}E} \) needs on an available line, and an implication is derived by \( \rulename{{\to}I} \), which needs a box of its own. (That box assumes \( P \) again although line 2 already did: \( \rulename{{\to}I} \) needs the box, not new information.)

**Marking scheme.** (10 points)

- 2: opens a box with \( P \) and inside it a box with \( Q \), read off the goal.
- 3: derives \( P \to Q \) inside the box of \( Q \) by a box whose last line is \( Q \).
- 2: obtains \( P \to R \), then \( R \), by \( \rulename{{\to}E} \) on available lines.
- 2: closes the boxes inner first, each \( \rulename{{\to}I} \) citing an available box.
- 1: the sentence says \( P \to Q \) must be a line, hence needs a box.

Fatal errors (0 for the step): citing a line outside the box that contains it; writing \( P \to Q \) with no box.
:::

::: {#exr-proving-an-implication-c3}
[C3: Exit check: a derivation and its prose]

::: {.enumerate options="label=(\alph*)"}
1. Write a derivation of \( P \to Q, \ (Q \to R) \wedge (R \to S) \vdash P \to S \), with every line justified.
2. Let \( x \) be a real number, and take \( P \): "\( x > 5 \)", \( Q \): "\( x > 4 \)", \( R \): "\( x^2 > 16 \)", \( S \): "\( x^2 > 9 \)". Say why each premise is true for every real \( x \). Then write your derivation as fluent prose about \( x \), one sentence per step.
:::
:::

::: {.solution}
(a) Premise-directed first: the second premise is a conjunction, so \( \rulename{\wedge E} \) takes it apart. Goal-directed next: the goal is an implication, so open a box with its hypothesis \( P \), and reach \( S \) by firing the three implications in turn.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {(Q \to R) \wedge (R \to S)}
  \have {3} {Q \to R} \ae{2}
  \have {4} {R \to S} \ae{2}
  \open
  \hypo {5} {P}
  \have {6} {Q} \ie{1,5}
  \have {7} {R} \ie{3,6}
  \have {8} {S} \ie{4,7}
  \close
  \have {9} {P \to S} \ii{5-8}
\end{nd}$
\end{center}
```

Lines 1–4 lie in no box, so they are available inside the box \( \lines{5}{8} \); line 9 cites that box, which has ended, and neither it nor line 9 lies in another box.

(b) The premise \( P \to Q \) holds because \( 5 > 4 \): if \( x > 5 \), then \( x > 4 \). For \( Q \to R \): if \( x > 4 \), then \( x > 0 \), so \( x^2 = x \cdot x > 4x > 16 \). For \( R \to S \): if \( x^2 > 16 \), then \( x^2 > 9 \), since \( 16 > 9 \). So both premises (the second a conjunction of two true implications) hold for every real \( x \).

In prose: *We know that \( x > 5 \) implies \( x > 4 \), that \( x > 4 \) implies \( x^2 > 16 \), and that \( x^2 > 16 \) implies \( x^2 > 9 \). Suppose \( x > 5 \). Then \( x > 4 \). Hence \( x^2 > 16 \), and so \( x^2 > 9 \). This proves that if \( x > 5 \), then \( x^2 > 9 \).*

**Marking scheme.** (10 points)

- 2: takes the conjunctive premise apart by two \( \rulename{\wedge E} \) lines (inside or outside the box).
- 2: opens a box with \( P \) (not \( S \)) and closes it on \( S \), a line of that box.
- 2: three \( \rulename{{\to}E} \) steps, each citing an implication and exactly its hypothesis, every cited line available.
- 1: the closing \( \rulename{{\to}I} \) cites the box as a range.
- 3: prose with one sentence per step, "suppose" for the assumption, and a closing sentence stating the implication.

Fatal errors (0 for the step): a box opened with the conclusion \( S \) (the converse error); citing a line of the box after it has closed.
:::

<!-- dependency ledger
def-rules-implication (example): x > 2 gives x > 0, x^2 > 2x, 2x > 4 and x^2 > 4; all three fail at x = 0 | school algebra, ch11 (promised)
def-rules-implication (example): each of and-I, and-E, ->E writes a conjunction or a piece of an earlier line, so without ->I an implication stands on a line only as a premise or as a piece of an earlier line | inline (read off the schemas of def-rules-conjunction and def-rule-implication-elimination; not used in a proof)
def-rules-implication (example): no rule leads from true premises to a false conclusion ("why the rule is right") | ch03 (promised; soundness)
prp-implication-transitive (example): x > 3 implies x^2 > 9 (x > 0, x^2 > 3x > 9); x^2 > 9 implies x^2 > 4 since 4 < 9 | school algebra, ch11 (promised)
exm-illegal-citation (solution): x > 3 implies x > 2 and x > 2 implies x > 1 for every real x; 0 > 1 is false | school algebra, ch11 (promised)
exm-illegal-citation (example): the warning's slip: x > 1 implies x^2 > 1; x^3 > 1 fails at x = 0 | school algebra, ch11 (promised)
exm-first-boxes (solution): if a > 0 and x > 1 then ax > a (the reading of (c), not used in a derivation) | school algebra, ch11 (promised)
prp-curry (example): if x > 0 and y > 0 then xy > 0 (the reading, not used in a derivation) | school algebra, ch11 (promised)
exr-proving-an-implication-b2 (solution): x^2 >= 0 for every real x | school algebra, ch11 (promised)
exr-proving-an-implication-c1 (solution): (x > 2 and x > 3) implies x > 1 for every real x; 0 > 1 is false | school algebra, ch11 (promised)
exr-proving-an-implication-c3 (solution): x > 5 implies x > 4; x > 4 implies x^2 > 16 (x > 0, x^2 > 4x > 16); x^2 > 16 implies x^2 > 9 | school algebra, ch11 (promised)
-->
