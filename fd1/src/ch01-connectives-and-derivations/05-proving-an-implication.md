# Proving an Implication: the Rule of the Box

Sections 1.2 and 1.3 gave three rules. \( \rulename{\wedge I} \) builds a conjunction; \( \rulename{\wedge E} \) and \( \rulename{{\to}E} \) take a line apart or use it. With them we can **use** an implication, but we cannot **prove** one. This section fills that gap with the rule \( \rulename{{\to}I} \). The rule asks us to do something new: to assume a statement we do not know, inside a boundary that says where the assumption holds. The boundary is a **box**. With the box we can name the error of Argument B, and say exactly which earlier lines a line may cite.

## Supposing something we do not know

Here is a small theorem about a real number \( x \).

> If \( x > 2 \), then \( x^2 > 4 \).

The proof everyone would write goes like this. *Suppose \( x > 2 \). Then \( x > 0 \), so multiplying \( x > 2 \) by \( x \) gives \( x^2 > 2x \). Also \( 2x > 4 \). Hence \( x^2 > 4 \).* Then, often without saying it: *this proves that if \( x > 2 \), then \( x^2 > 4 \).*

Look at the first sentence. We do not know that \( x > 2 \). The number \( x \) is arbitrary, and it may well be \( 0 \). So "suppose \( x > 2 \)" asserts nothing. It opens a **temporary world**, one in which \( x > 2 \) holds, and asks what else holds there.

Inside that world, the sentences "\( x^2 > 2x \)", "\( 2x > 4 \)", and "\( x^2 > 4 \)" are true. Outside it they are not: at \( x = 0 \) all three are false. Only the last sentence of the proof leaves the temporary world. What it carries out is not "\( x^2 > 4 \)" but the implication "if \( x > 2 \), then \( x^2 > 4 \)", and that is true for every real \( x \).

None of the rules so far can do this: \( \rulename{\wedge I} \) writes a conjunction, and \( \rulename{\wedge E} \) and \( \rulename{{\to}E} \) write a piece of a line that is already there. To prove "if \( x > 2 \), then \( x^2 > 4 \)" from nothing, we must be allowed to suppose.

A supposition is only safe if it has a boundary. Without one, the proof above could go on: "… Hence \( x^2 > 4 \). So \( x^2 > 4 \) for every real \( x \)." That is false at \( x = 0 \). The error is not in any computation; it is that a sentence from inside the temporary world was used outside it.

A derivation draws the boundary as a **box**. The assumption opens the box: it is written with a vertical bar to its left and a short horizontal rule under it. Every line derived under the assumption carries the same bar. When the box closes, the bar stops, and exactly one thing leaves: the implication from the assumption to the box's last line.

*To prove "if \( \varphi \), then \( \psi \)", assume \( \varphi \) in a box, reach \( \psi \) inside it, and close the box.*

## The introduction rule for implication

From now on the given part of a schema may also be a **box**, cited as a range of lines from its first line to its last; nothing else in @def-rule-schema changes.

Here is the rule, as a pattern. Beside it, for reference, is the rule \( \rulename{{\to}E} \) of @def-rule-implication-elimination, so that the two rules for "implies" stand in one place.

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

As in every schema (@def-rule-schema), \( \varphi \) and \( \psi \) stand for any statements, replaced consistently, and \( i, j, k \) for line numbers. This rule has conditions that matter; read each one.

1. **Open a box** whose first line is the assumption \( \varphi \). The assumption may be **any** statement: true or false, related to the premises or not. Its justification is "assumption", printed **"asm, for \( \rulename{{\to}I} \)"**: the annotation names the rule that will close the box. The price of assuming anything we like is the box.
2. **Inside the box**, work as usual. Every rule may be used. A line inside may cite the assumption and every earlier line that is not inside a box that has already closed: the premises, the lines above the box that are still in force, and the lines derived inside the box so far.
3. **The last line** of the box is \( \psi \). It must be a line of this box itself, not a line of some further box opened inside it. (The drawing cannot show this, which is why the definition says it in words.)
4. **Close the box**, and write \( \varphi \to \psi \) on a later line outside it, in practice the very next line. The justification cites the **whole box** as the range \( \lines{i}{j} \), from its assumption to its last line, not its lines one by one.
5. **After the box closes**, nothing inside it may be cited again. The assumption is discharged, and everything derived under it goes with it. Only the implication leaves.

Clause 5 is the boundary of the temporary world. The subsection "Which lines a line may cite" below turns clause 5 into an exact rule.

**What each box is for.** From now on every assumption says, in its justification column, what its box is for. "asm, for \( \rulename{{\to}I} \)" says that the box was opened to prove an implication, and that a \( \rulename{{\to}I} \) line will close it. In a written proof the same line is the word "suppose". While a derivation is still growing and its closing line is not yet written, the annotation records the plan.

::: {.second-reading title="A box of one line"}
The **degenerate case** is \( i = j \): a box of one line, whose assumption is also its last line. Then \( \psi \) is \( \varphi \), and the rule writes \( \varphi \to \varphi \). Nothing in the rule asks the box to contain more than its assumption.
:::

*Why the rule is right.* The implication \( \varphi \to \psi \) claims only that \( \psi \) holds whenever \( \varphi \) does. The box shows exactly that: starting from \( \varphi \), and from facts that hold anyway, the rules lead to \( \psi \).

*Why the box closes.* The lines inside hold only under the assumption. If the assumption is false, as \( x > 2 \) is at \( x = 0 \), they may be false too. Closing the box is what stops them being used where the assumption is not in force.

## A first box: implication is transitive

The first result proved with a box is the chaining of implications. Section 1.3 used chains of implications forwards, firing each on a hypothesis already in hand. Here the hypothesis is not in hand, and we still want the chain.

::: {#prp-implication-transitive}
[Implication Is Transitive]

\( P \to Q, \ Q \to R \vdash P \to R \).
:::

::: {.idea}
Start from the goal. Its main connective is \( \to \), so the last line will be \( \rulename{{\to}I} \), and that needs a box that opens with \( P \) and ends with \( R \). Inside the box, the new goal is \( R \). Reason backwards: \( R \) is the conclusion of the premise \( Q \to R \), so \( \rulename{{\to}E} \) gives it once \( Q \) is on a line. And \( Q \) is the conclusion of \( P \to Q \), so \( \rulename{{\to}E} \) gives it from \( P \), which the box has just assumed.

In the Givens/Goal table, \( \rulename{{\to}I} \) moves the hypothesis into the Givens and makes the conclusion the goal.

| Givens | Goal |
|---|---|
| \( P \to Q \), \( Q \to R \) | \( P \to R \) |
| \( P \to Q \), \( Q \to R \), \( P \) (box opened) | \( R \) |
| \( P \to Q \), \( Q \to R \), \( P \), \( Q \) (\( \rulename{{\to}E} \)) | \( R \) |
| \( P \to Q \), \( Q \to R \), \( P \), \( Q \), \( R \) (\( \rulename{{\to}E} \)) | \( R \) ✓ |

The same search as a growing derivation: the box opened, its goal \( R \) at the bottom (left); then line 4 written forwards (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {R}
  \close
  \have {6} {P \to R} \ii{3-5}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {R}
  \close
  \have {6} {P \to R} \ii{3-5}
\end{nd}$
\end{center}
```
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

## Argument B, diagnosed

Section 1.1 broke the form of Argument B's last step. Here is the rule B misused. With \( E \): "\( n \) is even" and \( S \): "\( n^2 \) is even", B's prose is this derivation.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {E}
  \have {2} {S} \by{algebra}{1}
  \close
  \have {3} {E \to S} \ii{1-2}
\end{nd}$
\end{center}
```

Line 1 is B's "Suppose \( n \) is even, say \( n = 2k \)". Line 2 is its computation \( n^2 = 4k^2 = 2(2k^2) \), a step of algebra, as in @exm-product-in-unit-interval. Line 3 is what the box earns; set it beside what B claimed.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=1cm, every node/.style={font=\normalsize}]
  \node[font=\small\itshape] at (0,0.75) {what B's box earns};
  \draw (-0.6,0.3) -- (-0.6,-0.75);
  \draw (-0.6,-0.24) -- (0.1,-0.24);
  \node[right] at (-0.55,0) {$E$};
  \node[right] at (-0.55,-0.5) {$S$};
  \node[right] at (-0.85,-1.15) {$E \to S$};
  \node at (2.1,-1.15) {$\neq$};
  \node[font=\small\itshape] at (4,0.75) {what B claimed};
  \node at (4,-1.15) {$S \to E$};
\end{tikzpicture}
\end{center}
```

B's box opens with \( E \) and closes on \( S \), so \( \rulename{{\to}I} \) lets it write \( E \to S \): the converse of the claim. B's last sentence wrote \( S \to E \). The rule asks the box to open with the **hypothesis** of the implication being proved, here \( S \), and B never opened that box.

**The repair fails.** Keep \( E \to S \), open a box with \( S \), and inside it use \( S \) to reach \( E \): that step goes from \( E \to S \) and \( S \) to \( E \). It is affirming the consequent, the bad form of Section 1.3. Try to break it. Take "if \( x > 2 \), then \( x^2 > 4 \)" and "\( x^2 > 4 \)". At \( x = -3 \) both are true, since \( 9 > 4 \), and "\( x > 2 \)" is false. So B cannot be saved by moving its lines around: a \( \rulename{{\to}I} \) proof of \( S \to E \) opens its box with \( S \).

::: {.warning}
The box of \( \rulename{{\to}I} \) opens with the **hypothesis** of the implication to be proved, never with its conclusion: Argument B used \( \rulename{{\to}I} \) with the box opened at the wrong end.
:::

::: {.check}
A proof of "if \( x^3 > 8 \), then \( x > 2 \)" begins "Suppose \( x > 2 \)." and ends "Hence \( x^3 > 8 \)." What does its box earn? Is the claim it was meant to prove true?
:::

::: {.solution}
Its box opens with \( x > 2 \) and closes on \( x^3 > 8 \), so it earns \( (x > 2) \to (x^3 > 8) \), the converse of the claim. The claim itself is true: if \( x \le 2 \), then \( x^3 \le 2^3 = 8 \), since a larger real number has a larger cube, so \( x^3 > 8 \) forces \( x > 2 \). But this box does not prove it.
:::

::: {.second-reading title="Two errors that cancel"}
::: {#exm-errors-that-cancel}
[Two errors that cancel]

Let \( x \) be a real number. Here is a "proof" that if \( x > 3 \), then \( x^2 > 9 \): *Suppose \( x^2 > 9 \). Then \( x > 3 \). Hence, if \( x > 3 \), then \( x^2 > 9 \).* Is the conclusion true? Is it proved?
:::

::: {.solution}
As a derivation, the "proof" reads as follows.

```{=latex}
\begin{center}
% expect-invalid: line 2 is no fact about numbers, and line 3 writes the converse of what the box earns
$\begin{nd}
  \open
  \hypo {1} {x^2 > 9}
  \have {2} {x > 3} \by{algebra}{1}
  \close
  \have {3} {(x > 3) \to (x^2 > 9)} \ii{1-2}
\end{nd}$
\end{center}
```

Two lines fail. Line 2 is no fact about numbers: at \( x = -4 \) we have \( x^2 = 16 > 9 \), and \( x > 3 \) fails. Line 3 writes the converse of what the box earns. The box opens with \( x^2 > 9 \) and ends with \( x > 3 \), so \( \rulename{{\to}I} \) would write \( (x^2 > 9) \to (x > 3) \).

The two errors cancel. The implication the box would earn is false, and reversed it is the true claim: if \( x > 3 \), then \( x > 0 \), so \( x^2 = x \cdot x > 3x > 9 \). A reader who compares only the last line with the claim sees nothing wrong; a checker who reads every line finds both errors. A correct conclusion is no evidence that the lines above it are correct.
:::
:::

## A box must end on a line of its own

Try to derive \( \vdash P \to (Q \to P) \). The goal is an implication, so open a box with \( P \); the new goal \( Q \to P \) is again an implication, so open a box with \( Q \) inside the first. The statement \( P \) is already on line 1, so it is tempting to close the inner box at once.

```{=latex}
\begin{center}
% expect-invalid: line 3 cites a box whose last line is Q, so ->I may write only Q -> Q
$\begin{nd}
  \open
  \hypo {1} {P}
  \open
  \hypo {2} {Q}
  \close
  \have {3} {Q \to P} \ii{2-2}
  \close
  \have {4} {P \to (Q \to P)} \ii{1-3}
\end{nd}$
\end{center}
```

A checker reads the box \( \lines{2}{2} \): its assumption is \( Q \), and its last line is \( Q \). So \( \rulename{{\to}I} \) may write only \( Q \to Q \) from it, and line 3 is rejected. The statement \( P \) stands on line 1, outside the inner box, and clause 3 asks for \( \psi \) as a line **of the box itself**.

The fix is bookkeeping: copy \( P \) into the inner box. Copying an available line is the rule \( \rulename{R} \) (**repetition**), made official as clause (D3) of the definition below. The copy "\( P \), R 1" then ends the inner box.

Some books let a box end on any line available inside it. This book copies the line in, so that every \( \rulename{{\to}I} \) line can be checked by looking only at the box it cites. The corrected derivation is @exm-first-boxes (b) below.

## Which lines a line may cite

In a derivation without boxes (@def-box-free-derivation), a line may cite any **earlier** line. With boxes that is no longer enough: after the derivation of @prp-implication-transitive, a line 7 citing line 5 would write \( R \) outside the box, the "\( x^2 > 4 \) for every \( x \)" error of the first subsection. What matters is which earlier lines are still **available**, and the bars show it.

**A line inside a box may be cited only from inside that box. Once a box has closed above you, nothing inside it can be cited; the boxes you are in may be left across their tops, and passing beside a closed box is fine.**

*Open a box, close a box: an assumption lives exactly as long as its box.*

A **whole box**, cited by \( \rulename{{\to}I} \), has its own condition: the citing line must stand in exactly the boxes that the cited box stands in, other than the cited box itself. For single lines:

- a line in no box is available at every later line;
- a line inside a box is available further down that box, and inside every box opened within it;
- once its box closes, the line is available nowhere.

The figure shows eleven lines without statements: box A is lines 2–4, box B lines 6–10, and box C, lines 7–8, sits inside B. An arrow runs from a citing line up to the line it cites, solid and marked \( \checkmark \) if legal, dashed and marked \( \times \) if not. A bracket on the left marks a whole box cited.

```{=latex}
\begin{center}
\begin{tikzpicture}[x=1cm, y=0.62cm, every node/.style={font=\normalsize}, >={Stealth[length=2mm]}]
  \foreach \k in {1,...,11} \node[left] at (0.15,-\k) {\k};
  \draw (0.35,-0.6) -- (0.35,-11.4);
  \draw (0.35,-1.42) -- (1.15,-1.42);
  \draw (0.85,-1.65) -- (0.85,-4.4);
  \draw (0.85,-2.42) -- (1.65,-2.42);
  \draw (0.85,-5.65) -- (0.85,-10.4);
  \draw (0.85,-6.42) -- (1.65,-6.42);
  \draw (1.25,-6.65) -- (1.25,-8.4);
  \draw (1.25,-7.42) -- (1.9,-7.42);
  \node[font=\small] at (0.6,-3) {A};
  \node[font=\small] at (0.6,-8.5) {B};
  \node[font=\small] at (1.05,-7.5) {C};
  \foreach \k in {1,5,11} \node[right] at (0.4,-\k) {$\cdots$};
  \foreach \k in {2,3,4,6,9,10} \node[right] at (0.9,-\k) {$\cdots$};
  \foreach \k in {7,8} \node[right] at (1.3,-\k) {$\cdots$};
  % legal citations: solid, marked with a check
  \draw[->] (2.1,-4) -- (2.6,-4) -- (2.6,-2) -- (2.1,-2);
  \node[fill=white, inner sep=1pt, font=\small] at (2.6,-2.5) {$\checkmark$};
  \draw[->] (2.1,-7.82) -- (2.6,-7.82) -- (2.6,-5.82) -- (2.1,-5.82);
  \node[fill=white, inner sep=1pt, font=\small] at (2.6,-6.6) {$\checkmark$};
  \draw[->] (2.1,-8.18) -- (4.7,-8.18) -- (4.7,-1) -- (2.1,-1);
  \node[fill=white, inner sep=1pt, font=\small] at (4.7,-4.6) {$\checkmark$};
  \draw[->] (2.1,-11.18) -- (4.0,-11.18) -- (4.0,-5) -- (2.1,-5);
  \node[fill=white, inner sep=1pt, font=\small] at (4.0,-9.6) {$\checkmark$};
  % illegal citations: dashed, marked with a cross
  \draw[->, dashed] (2.1,-6.18) -- (3.3,-6.18) -- (3.3,-3) -- (2.1,-3);
  \node[fill=white, inner sep=1pt, font=\small] at (3.3,-4.0) {$\times$};
  \draw[->, dashed] (2.1,-8.82) -- (3.3,-8.82) -- (3.3,-7) -- (2.1,-7);
  \node[fill=white, inner sep=1pt, font=\small] at (3.3,-7.5) {$\times$};
  \draw[->, dashed] (2.1,-10.82) -- (2.6,-10.82) -- (2.6,-9.18) -- (2.1,-9.18);
  \node[fill=white, inner sep=1pt, font=\small] at (2.6,-10) {$\times$};
  % whole boxes cited: brackets on the left
  \draw (-0.4,-1.7) -- (-0.55,-1.7) -- (-0.55,-4.3) -- (-0.4,-4.3);
  \draw[->] (-0.35,-5) -- (-0.95,-5) -- (-0.95,-3) -- (-0.55,-3);
  \node[fill=white, inner sep=1pt, font=\small] at (-0.95,-4) {$\checkmark$};
  \draw (-0.4,-5.7) -- (-0.55,-5.7) -- (-0.55,-10.3) -- (-0.4,-10.3);
  \draw[->] (-0.35,-11) -- (-0.95,-11) -- (-0.95,-8) -- (-0.55,-8);
  \node[fill=white, inner sep=1pt, font=\small] at (-0.95,-9.5) {$\checkmark$};
\end{tikzpicture}
\end{center}
```

*A line can be cited from below only while every box containing it is still open.* Line 8 leaves box C across its top to cite line 6, and line 11 passes beside the closed box B to cite line 5. Lines 5 and 11 stand in no box, and neither do the boxes A and B they cite whole.

::: {.check}
In the figure, which of lines 1–9 may line 10 cite?
:::

::: {.solution}
Lines 1, 5, 6 and 9. Lines 1 and 5 are in no box; lines 6 and 9 are in box B, which contains line 10. Lines 2–4 are not available (box A has closed), and neither are lines 7–8 (box C has closed). It may also cite the whole box 7–8, which, like line 10, stands in box B alone.
:::

Here is the official version, the one a checker uses.

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

(D1)–(D4) say: given, assumed, copied, or one step of one rule, always from what is still available.

The scope rule is the definition's real content: line \( i \) is available at line \( k \) when every assumption that line \( i \) was derived under is still in force at line \( k \): the picture rule above, in words a checker can apply.

::: {.second-reading title="Why checking stays mechanical"}
*Well defined.* Whether a line is available is decided by looking at the boxes; nothing about the meaning of the statements enters. Checking a derivation stays mechanical.
:::

*Nothing earlier changes.* A derivation with no boxes is a box-free derivation of @def-box-free-derivation for the same rules with \( \rulename{R} \) added: with no boxes, "available" means just "earlier". So every derivation of Sections 1.2 and 1.3 is a derivation in the new sense, and @def-derivable is read from now on with this definition. The sequent \( \Gamma \vdash \psi \) still means: **there is** a derivation whose premises all belong to \( \Gamma \) and whose last line is \( \psi \). Its last line lies in no box, so it depends on the premises and on nothing that was merely assumed.

::: {.second-reading title="More on repetition"}
The typical use of \( \rulename{R} \) copies a line into a box opened below it.

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi}
  \have {} {\vdots}
  \open
  \hypo {j} {\psi} \purpose{\ii}
  \have {} {\vdots}
  \have {k} {\varphi} \r{i}
  \close
\end{nd}$
\end{center}
```

Line \( i \) is available at line \( k \) exactly when every box containing line \( i \) contains line \( k \); in this drawing, line \( i \) is in no box that has closed, so the copy is legal. The worked example @exm-first-boxes below uses it.
:::

::: {.warning}
A box that is never closed cannot end a derivation. If the last line of a list is still inside a box, it depends on an assumption that was never discharged, and @def-derivation does not count the list as a derivation at all. "Suppose \( x > 2 \). Then \( x^2 > 4 \)", with nothing after it, proves nothing about \( x \): the implication is the only thing the supposition was allowed to produce, and it was never written.
:::

## How to check a derivation

Section 1.2 checked a line by asking which rule it uses, which lines it cites, and whether they are earlier. With boxes the third question becomes: **are they available here?** For each line after the premises, ask:

1. **Which rule?** Name it. An assumption opens a box; \( \rulename{R} \) repeats; every other line applies one rule.
2. **Which lines or boxes does it cite, and do they form an instance of the rule's schema?** \( \rulename{{\to}E} \) cites an implication and exactly its hypothesis; \( \rulename{{\to}I} \) cites one box, whose assumption and last line must be the two sides of the implication written.
3. **Are they available here?** Apply the scope rule to each cited line and box.

*Finding a derivation may need an idea; checking one never does.* Here is the check run on the derivation of @prp-implication-transitive.

| Line | Which rule? | Cites | Available? |
|---|---|---|---|
| 1, 2 | premises (D1) | — | — |
| 3 | assumption (D2); opens the box 3–5 | — | — |
| 4 | \( \rulename{{\to}E} \): \( Q \) from \( P \to Q \) and \( P \) | 1, 3 | 1 is in no box; 3 is in box 3–5, which contains 4 |
| 5 | \( \rulename{{\to}E} \): \( R \) from \( Q \to R \) and \( Q \) | 2, 4 | 2 is in no box; 4 is in box 3–5, which contains 5 |
| 6 | \( \rulename{{\to}I} \): \( P \to R \) from the box | box 3–5 | the box ended at 5; neither it nor 6 lies in another box |

Every line passes, and the last line lies in no box. The bar shows the temporary world: it starts at line 3 and stops after line 5.

## An assumption used outside its box

Now watch the scope rule catch an error. Take the derivation of @prp-implication-transitive and add one careless line.

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
(a) *Idea.* The goal is an implication, so open a box with its hypothesis \( P \); the box must end with \( P \). The assumption is already \( P \), so the box can end at once: a box of one line, whose assumption is also its last line. Nothing in \( \rulename{{\to}I} \) asks a box to contain more than its assumption.

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

Line 1 is an assumption (D2) and opens the box \( \lines{1}{1} \), whose last line is \( P \). Line 2 cites that box, which ended before line 2 and, like line 2, lies in no other box. There are no premises, so this shows \( \vdash P \to P \). It is the first statement in the book derivable from **no** premises by the rules of logic alone. Argument B's box in "Argument B, diagnosed" also began without premises, but it used a step of algebra. Every other rule so far (@def-rules-conjunction, @def-rule-implication-elimination, and \( \rulename{R} \) of @def-derivation) cites at least one earlier line, so without a box a derivation must start with a premise. A box is what escapes: its first line is an assumption, and the assumption is discharged before the end.

(b) *Idea.* This is the derivation the checker accepted after the fix in "A box must end on a line of its own": line 3 copies \( P \) into the inner box.

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

Both boxes opened, goals at their feet (left); then the inner lines written, and only line 7 still to justify (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {Q} \purpose{\ii}
  \open
  \hypo {3} {P} \purpose{\ii}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {R}
  \close
  \have {6} {P \to R}
  \close
  \have {7} {Q \to (P \to R)}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {Q} \purpose{\ii}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \ie{1,3}
  \have {5} {R} \ie{4,2}
  \close
  \have {6} {P \to R} \ii{3-5}
  \close
  \have {7} {Q \to (P \to R)} \by{?}{}
\end{nd}$
\end{center}
```

The finished derivation:

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

The first claim: the outer box opened (left), then the inner one, with goal \( R \) (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {Q \to R}
  \close
  \have {7} {P \to (Q \to R)} \ii{2-6}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {R}
  \close
  \have {6} {Q \to R} \ii{3-5}
  \close
  \have {7} {P \to (Q \to R)} \ii{2-6}
\end{nd}$
\end{center}
```

The second claim: the box opened (left), then the assumption taken apart (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {P \wedge Q}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {R}
  \close
  \have {7} {(P \wedge Q) \to R} \ii{2-6}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {R}
  \close
  \have {7} {(P \wedge Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```

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

Lines 3–6 cite line 1, which lies in no box, or earlier lines of the box \( \lines{2}{6} \), from inside that box. Line 7 cites the box \( \lines{2}{6} \), which has ended, and neither that box nor line 7 lies in any other box. By @def-derivable, the two derivations prove the two claims.
:::

::: {.check}
In the second derivation of @prp-curry, what does the annotation of line 2 say, and which line closes its box?
:::

::: {.solution}
"asm, for \( \rulename{{\to}I} \)": the box was opened to prove an implication. Line 7 closes it, citing the box \( \lines{2}{6} \).
:::

In the first derivation the boxes are nested, and the inner one closes first: an assumption made later is discharged earlier. That is the general pattern, forced by @def-derivation, since two boxes are either disjoint or one inside the other.

Read mathematically, the first claim turns "if \( x > 0 \) and \( y > 0 \), then \( xy > 0 \)" into "if \( x > 0 \), then (if \( y > 0 \), then \( xy > 0 \))", and the second turns it back. The two forms say the same thing, one hypothesis at a time or both at once.

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

## The rule card

Before the card, the rule at work on large statements. Each row is one use of \( \rulename{{\to}I} \): the box, and the line it writes.

::: {#exm-proving-an-implication-instances}
[Instances of \( \rulename{{\to}I} \)]

| \( \varphi \) | \( \psi \) | The box | New line |
|------------|----------------|------------------------|----------------------------|
| \( P \wedge \neg Q \) | \( P \wedge (P \wedge \neg Q) \) | from \( P \wedge \neg Q \) (asm) to \( P \wedge (P \wedge \neg Q) \), by \( \rulename{\wedge E} \) and then \( \rulename{\wedge I} \) | \( (P \wedge \neg Q) \to (P \wedge (P \wedge \neg Q)) \) |
| \( Q \to R \) | \( (P \to Q) \to (P \to R) \) | from \( Q \to R \) (asm) to \( (P \to Q) \to (P \to R) \), with two boxes inside it | \( (Q \to R) \to ((P \to Q) \to (P \to R)) \) |
| \( (P \vee Q) \wedge R \) | \( (P \vee Q) \wedge R \) | a box of one line | \( ((P \vee Q) \wedge R) \to ((P \vee Q) \wedge R) \) |

**Not an instance.** A box opens with \( Q \) and ends with \( P \), copied in by \( \rulename{R} \). The line "\( P \to Q \) — \( \rulename{{\to}I} \)" is not an instance: \( \rulename{{\to}I} \) writes the assumption first, \( Q \to P \). This is Argument B's step.
:::

The card grows by two rows. In *Shape*, "box \( \varphi \) … \( \psi \)" is a closed box from the assumption \( \varphi \) to its last line \( \psi \).

| Rule | Shape | You write | Lean |
|---|---|---|---|
| \( \rulename{\wedge I} \) | \( \varphi \), \( \psi \) \( \Longrightarrow \) \( \varphi \wedge \psi \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | \( \varphi \wedge \psi \) \( \Longrightarrow \) \( \varphi \) (or \( \psi \)) | "In particular, \( P \)." | `h.1` (and `h.2`) |
| \( \rulename{{\to}E} \) | \( \varphi \to \psi \), \( \varphi \) \( \Longrightarrow \) \( \psi \) | "Since \( P \) implies \( Q \), and \( P \) holds, \( Q \)." | `exact h hp` |
| \( \rulename{{\to}I} \) | box \( \varphi \) … \( \psi \) \( \Longrightarrow \) \( \varphi \to \psi \) | "Assume \( P \). … Hence \( Q \)." | `intro hp` |
| \( \rulename{R} \) | \( \varphi \) (available) \( \Longrightarrow \) \( \varphi \), copied | "As shown above, \( P \)." | `exact hp` |

In the Lean column, `intro hp` opens the box and names its assumption `hp`.

::: {.warning}
[Not allowed: \( \rulename{{\to}I} \)]

Each step below is wrong; the tag names the clause of the rule's reading that it breaks.

- Close the box on a line of a box inside it: clause 3, the last line must be a line of the box itself ("A box must end on a line of its own").
- Write \( \psi \to \varphi \) from a box that runs from \( \varphi \) to \( \psi \): clause 4, the box opens with the hypothesis (Argument B).
- Cite a line inside a closed box: clause 5 (@exm-illegal-citation).
- End the derivation inside an open box: clause 4, the box must close (the warning on a box that is never closed).
- Cite the box's lines one by one: clause 4, the box is cited whole, as a range.

The discharge is where the rule bites, so here is one wrong step beside the right one, with premises \( (P \wedge R) \to Q \) and \( R \). On the left, line 6 carries \( Q \) out of the box by repetition, as if \( P \) had been proved. On the right, line 6 closes the box with \( \rulename{{\to}I} \).

```{=latex}
\begin{center}
% expect-invalid: line 6 repeats line 5, a line of the closed box 3-5
$\begin{nd}
  \hypo {1} {(P \wedge R) \to Q}
  \hypo {2} {R}
  \open
  \hypo {3} {P} \purpose{\ii}
  \have {4} {P \wedge R} \ai{3,2}
  \have {5} {Q} \ie{1,4}
  \close
  \have {6} {Q} \r{5}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {(P \wedge R) \to Q}
  \hypo {2} {R}
  \open
  \hypo {3} {P}
  \have {4} {P \wedge R} \ai{3,2}
  \have {5} {Q} \ie{1,4}
  \close
  \have {6} {P \to Q} \ii{3-5}
\end{nd}$
\end{center}
```

The left list would show \( (P \wedge R) \to Q, \ R \vdash Q \). Let \( x \) be a real number, with \( P \): "\( x > 5 \)", \( R \): "\( x > 0 \)", \( Q \): "\( x > 3 \)". The first premise holds for every \( x \), and at \( x = 1 \) both premises are true and \( Q \) is false.
:::

The sentence for \( \rulename{{\to}I} \) is the one to watch. "Assume \( P \)" opens a box, and "hence \( Q \)" is its last line. The closing line, "so \( P \) implies \( Q \)", is usually left unsaid in written mathematics. It is still there: the box closes whether or not anyone says so. It is also the line Argument B got wrong.

::: {.remark}
[Looking ahead]

Chapter 2 proves the claim Argument B wanted, with the rules for "not".
:::

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
  \hypo {3} {P} \purpose{\ii}
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
3. Which of lines 1–5 are available at line 6, and which boxes?
4. Someone extends the derivation by a line 7, the statement \( R \) justified by \( \rulename{{\to}E} \) 6, 3. Is the result a derivation? If not, name the clause of @def-derivation that line 7 breaks.
5. In the first derivation in the proof of @prp-curry, why is line 4 available at line 5? And why is the inner box closed before the outer one?
6. In the same derivation, which rule produces line 5, and which lines does it cite?
:::
:::

::: {.solution}
(a) The schema is the left one in @def-rules-implication: a box from an assumption \( \varphi \) on line \( i \) to a line \( \psi \) on line \( j \), and then \( \varphi \to \psi \) on line \( k \), justified \( \rulename{{\to}I} \) \( \lines{i}{j} \). The condition the drawing cannot show: \( \psi \) is a line of that box itself, not of a box inside it.

(b) (i) \( \rulename{{\to}E} \) 1, 3; (ii) \( \rulename{{\to}E} \) 4, 2; (iii) \( \rulename{{\to}I} \) \( \lines{3}{5} \). The derivation shows \( P \to (Q \to R), \ Q \vdash P \to R \).

(c) Lines 1 and 2, and the box \( \lines{3}{5} \). Lines 3, 4, and 5 lie in the box \( \lines{3}{5} \), which does not contain line 6, so none of them is available there one by one. The box as a whole is available at line 6: it has ended, and neither it nor line 6 lies in another box. That is why (iii) may cite it.

(d) No. Line 6 is available at line 7, but line 3 is not: it lies in the box \( \lines{3}{5} \), which does not contain line 7. So line 7 applies a rule to a line that is not available, which (D4) forbids.

(e) Line 4 lies in two boxes, \( \lines{2}{6} \) and \( \lines{3}{5} \), and both contain line 5; so by the scope rule line 4 is available at line 5. The inner box \( \lines{3}{5} \) lies inside the outer box \( \lines{2}{6} \), and two boxes are either disjoint or one inside the other, so the inner box must end first. Read off the goal: the inner box proves \( Q \to R \), which is the last line the outer box needs.

(f) \( \rulename{{\to}E} \), citing line 1, the implication \( (P \wedge Q) \to R \), and line 4, its hypothesis \( P \wedge Q \).
:::

::: {#exr-proving-an-implication-a2}
[A2: Drill]

The parts run from one step, through a missing line, a justification column and steps to judge, to short derivations. Parts (e)–(g) refer to the eleven-line figure in "Which lines a line may cite".

::: {.enumerate options="label=(\alph*)"}
1. A box runs from line 3, \( (P \vee Q) \wedge R \), to line 6, \( S \to P \), a line of that box itself. What does "\( \rulename{{\to}I} \) 3–6" write?
2. Line 7 is \( (P \to Q) \to R \), justified "\( \rulename{{\to}I} \) 2–6". What is line 2, and what does its annotation read?
3. Line 9 is \( (P \wedge Q) \to (R \vee S) \), justified "\( \rulename{{\to}I} \) 4–8". What are lines 4 and 8?
4. Say which lines below are premises and which are assumptions, and fill in (i) and (ii).

    ```{=latex}
    \begin{center}
    $\begin{nd}
      \hypo {1} {P}
      \open
      \hypo {2} {Q} \purpose{\ii}
      \have {3} {P \wedge Q} \by{(i)}{}
      \close
      \have {4} {Q \to (P \wedge Q)} \by{(ii)}{}
    \end{nd}$
    \end{center}
    ```

5. May line 8 cite line 5?
6. May line 9 cite the whole box 2–4?
7. May line 11 cite line 6?
8. A box runs from line 3, \( P \) (an assumption), to line 6, \( R \); line 4, inside it, is \( Q \). Is "7. \( P \to Q \) — \( \rulename{{\to}I} \) 3–4" correct?
9. Find the illegal line, and say why it is illegal.

    ```{=latex}
    \begin{center}
    % expect-invalid: line 5 cites line 2, inside the closed box 2-3
    $\begin{nd}
      \hypo {1} {P \to Q}
      \open
      \hypo {2} {P}
      \have {3} {Q} \ie{1,2}
      \close
      \have {4} {P \to Q} \ii{2-3}
      \have {5} {Q} \ie{4,2}
    \end{nd}$
    \end{center}
    ```

10. Let \( x \) be a real number. Is "Suppose \( x > 3 \). Then \( x^2 > 9 \).", with nothing after it, a proof that \( x^2 > 9 \)?
11. Show \( \vdash (P \wedge Q) \to (Q \wedge P) \) by a derivation. Then write the argument as a paragraph of prose, one sentence per line.
12. Derive \( P \to Q \vdash (P \wedge R) \to Q \).
13. Derive \( Q \vdash (P \wedge R) \to (Q \wedge R) \).
14. Derive \( \vdash (P \wedge Q) \to (R \to P) \). Which box opens first?
15. Derive \( (P \to Q) \wedge R \vdash P \to (Q \wedge R) \).
:::
:::

::: {.solution}
(a) \( ((P \vee Q) \wedge R) \to (S \to P) \): the assumption on the left, the box's last line on the right.

(b) Line 2 is \( P \to Q \), the hypothesis of line 7, and its annotation reads "asm, for \( \rulename{{\to}I} \)".

(c) Line 4 is the assumption \( P \wedge Q \), which opens the box; line 8 is \( R \vee S \), the last line of that box.

(d) Line 1 is a premise and line 2 an assumption; (i) \( \rulename{\wedge I} \) 1, 2; (ii) \( \rulename{{\to}I} \) \( \lines{2}{3} \).

(e) Yes: line 5 lies in no box.

(f) No: box 2–4 stands in no box, and line 9 stands in box B, so the two do not stand in exactly the same boxes.

(g) No: line 6 is inside box B, which closed after line 10.

(h) No: lines 3–4 are not a box, since the box runs on to line 6. \( \rulename{{\to}I} \) cites the whole box \( \lines{3}{6} \) and writes \( P \to R \). (\( P \to Q \) is earned by a box of its own that ends on \( Q \).)

(i) Line 5: it cites line 2, which lies inside the box \( \lines{2}{3} \), closed before line 5.

(j) No. The box opened by "suppose" never closes, so nothing has left it; and at \( x = 0 \) the sentence \( x^2 > 9 \) is false. What the two sentences can prove, once the box closes, is "if \( x > 3 \), then \( x^2 > 9 \)".

(k) The goal is an implication, so open a box with \( P \wedge Q \); inside, \( \rulename{\wedge E} \) gives both halves, and \( \rulename{\wedge I} \) rebuilds them in the other order.

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

In prose: *Assume \( P \) and \( Q \). In particular, \( P \) holds. In particular, \( Q \) holds. Hence \( Q \) and \( P \) both hold. This proves that if \( P \) and \( Q \), then \( Q \) and \( P \).* Compared with @prp-and-commutes, the premise \( P \wedge Q \) has become an assumption, and the conclusion has become an implication that depends on nothing.

(l) 2 \( P \wedge R \), assumption, for \( \rulename{{\to}I} \); 3 \( P \), \( \rulename{\wedge E} \) 2; 4 \( Q \), \( \rulename{{\to}E} \) 1, 3; 5 \( (P \wedge R) \to Q \), \( \rulename{{\to}I} \) \( \lines{2}{4} \).

(m) 2 \( P \wedge R \), assumption, for \( \rulename{{\to}I} \); 3 \( R \), \( \rulename{\wedge E} \) 2; 4 \( Q \wedge R \), \( \rulename{\wedge I} \) 1, 3; 5 \( (P \wedge R) \to (Q \wedge R) \), \( \rulename{{\to}I} \) \( \lines{2}{4} \).

(n) The box of \( P \wedge Q \) opens first, since the goal's main connective is its first \( \to \): 1 \( P \wedge Q \), assumption, for \( \rulename{{\to}I} \); 2 \( R \), assumption, for \( \rulename{{\to}I} \), opening a box inside the first; 3 \( P \), \( \rulename{\wedge E} \) 1; 4 \( R \to P \), \( \rulename{{\to}I} \) \( \lines{2}{3} \); 5 \( (P \wedge Q) \to (R \to P) \), \( \rulename{{\to}I} \) \( \lines{1}{4} \).

(o) 2 \( P \), assumption, for \( \rulename{{\to}I} \); 3 \( P \to Q \), \( \rulename{\wedge E} \) 1; 4 \( Q \), \( \rulename{{\to}E} \) 3, 2; 5 \( R \), \( \rulename{\wedge E} \) 1; 6 \( Q \wedge R \), \( \rulename{\wedge I} \) 4, 5; 7 \( P \to (Q \wedge R) \), \( \rulename{{\to}I} \) \( \lines{2}{6} \).
:::

### B. Practice

::: {#exr-proving-an-implication-b1}
[B1: Two boxes, one inside the other]

A search for \( (P \wedge Q) \to R, \ S \to Q \vdash S \to (P \to R) \) has reached the stage below. *Name the move, then complete it.*

```{=latex}
% schema (partial derivation: the gaps are unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {S \to Q}
  \open
  \hypo {3} {S} \purpose{\ii}
  \open
  \hypo {4} {P} \purpose{\ii}
  \have[\ ][0] {} {\vdots}
  \close
  \have[\ ][0] {} {\vdots}
  \close
  \have[][9] {9} {S \to (P \to R)} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The move is goal-directed, twice: an implication goal opens a box with its hypothesis, and the new goal is its conclusion. The goal \( S \to (P \to R) \) gave the outer box, with \( S \), and its conclusion \( P \to R \) gave the inner box, with \( P \); the inner goal is \( R \). Inside both boxes, work backwards from the first premise: \( R \) is its conclusion, so it suffices to build its hypothesis \( P \wedge Q \) exactly. \( P \) is line 4, and \( Q \) comes from the second premise and the assumption \( S \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {S \to Q}
  \open
  \hypo {3} {S}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{2,3}
  \have {6} {P \wedge Q} \ai{4,5}
  \have {7} {R} \ie{1,6}
  \close
  \have {8} {P \to R} \ii{4-7}
  \close
  \have {9} {S \to (P \to R)} \ii{3-8}
\end{nd}$
\end{center}
```

Every citation is available. Lines 1 and 2 lie in no box. Line 3 lies only in the box \( \lines{3}{8} \), which contains line 5. Lines 4, 5 and 6 lie in both boxes, which contain lines 6 and 7. Line 8 cites the box \( \lines{4}{7} \), which has ended and stands, like line 8, in the box \( \lines{3}{8} \) and no other. Line 9 cites the box \( \lines{3}{8} \), which has ended and, like line 9, lies in no other box.
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
2. Let \( x \) be a real number. Use (a) to deduce "if \( \abs{x - 2} < 1 \), then \( 1 < x < 3 \)" from the two facts "if \( \abs{x - 2} < 1 \), then \( 1 < x \)" and "if \( \abs{x - 2} < 1 \), then \( x < 3 \)". Write the resulting argument as prose.
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

(b) Take \( P \): "\( \abs{x - 2} < 1 \)", \( Q \): "\( 1 < x \)" and \( R \): "\( x < 3 \)". The two facts are the premises \( P \to Q \) and \( P \to R \), and \( Q \wedge R \) is \( (1 < x) \wedge (x < 3) \), which \( 1 < x < 3 \) abbreviates (Section 1.1). The derivation in (a), with these statements put in for the letters, is a derivation of \( P \to (Q \wedge R) \) from the two facts.

In prose: *Suppose \( \abs{x - 2} < 1 \). Then \( 1 < x \) by the first fact, and \( x < 3 \) by the second. Hence \( 1 < x < 3 \). This proves that \( \abs{x - 2} < 1 \) implies \( 1 < x < 3 \).*
:::

::: {#exr-proving-an-implication-b4}
[B4: Putting a derivation in order]

Here are nine lines, each a statement with its justification. Seven of them, in the right order and with the right boxes, form a derivation of \( P \to (Q \to R) \vdash Q \to (P \to R) \). Give the order, and say where each box opens and closes. Then say why each of the other two lines cannot be used.

::: {.enumerate options="label=(\roman*)"}
1. \( P \to R \), by \( \rulename{{\to}I} \) on the box from \( P \) to \( R \).
2. \( Q \), assumption, for \( \rulename{{\to}I} \).
3. \( R \), by \( \rulename{{\to}E} \) from \( Q \to R \) and \( Q \).
4. \( R \), by \( \rulename{R} \), repeating the line \( R \) of (iii), written directly below (i).
5. \( P \to (Q \to R) \), premise.
6. \( Q \to (P \to R) \), by \( \rulename{{\to}I} \) on the box from \( Q \) to \( P \to R \).
7. \( R \), assumption, opening the box for the \( \rulename{{\to}I} \) that proves \( P \to R \).
8. \( Q \to R \), by \( \rulename{{\to}E} \) from \( P \to (Q \to R) \) and \( P \).
9. \( P \), assumption, for \( \rulename{{\to}I} \).
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

Start: line 2 assumes \( P \) and line 3 assumes \( Q \), read off the goal. The last line of the box of \( Q \) must be \( R \), and line 1 gives \( P \to R \) only once \( P \to Q \) is on an available line.
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

The sentence: the premise fires only on an available line \( P \to Q \), and no available line is \( P \to Q \) or has it as a conjunct or as the conclusion of an implication, so it can come only from \( \rulename{{\to}I} \), which needs a box of its own.

Line 1 does not help, since \( \rulename{{\to}E} \) on it would need \( P \to Q \) already. The third box assumes \( P \) again although line 2 already did: \( \rulename{{\to}I} \) needs the box, not new information.

**Marking scheme.** (10 points)

- 2: opens a box with \( P \) and inside it a box with \( Q \), read off the goal.
- 3: derives \( P \to Q \) inside the box of \( Q \) by a box whose last line is \( Q \).
- 2: obtains \( P \to R \), then \( R \), by \( \rulename{{\to}E} \) on available lines.
- 2: closes the boxes inner first, each \( \rulename{{\to}I} \) citing an available box.
- 1: the sentence says \( P \to Q \) must be a line that no elimination rule can supply, hence needs a box.

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

In prose: *We know that \( x > 5 \) implies \( x > 4 \), and that \( x > 4 \) implies \( x^2 > 16 \) and \( x^2 > 16 \) implies \( x^2 > 9 \). In particular, \( x > 4 \) implies \( x^2 > 16 \). In particular, \( x^2 > 16 \) implies \( x^2 > 9 \). Suppose \( x > 5 \). Then \( x > 4 \). Hence \( x^2 > 16 \). So \( x^2 > 9 \). This proves that if \( x > 5 \), then \( x^2 > 9 \).*

**Marking scheme.** (10 points)

- 2: takes the conjunctive premise apart by two \( \rulename{\wedge E} \) lines (inside or outside the box).
- 2: opens a box with \( P \) (not \( S \)) and closes it on \( S \), a line of that box.
- 2: reaches \( S \) inside the box of \( P \) by \( \rulename{{\to}E} \) steps, each citing an implication and exactly its hypothesis, every cited line available.
- 1: each closing \( \rulename{{\to}I} \) cites its box as a range.
- 3: prose with one sentence per step, "suppose" for the assumption, and a closing sentence stating the implication.

A route that first derives \( Q \to S \) in a box of \( Q \) (as in @prp-implication-transitive) and then uses it in the box of \( P \) earns the same points: its \( \rulename{{\to}E} \) steps in both boxes count for the third line, and its two \( \rulename{{\to}I} \) steps for the fourth.

Fatal errors (0 for the step): a box opened with the conclusion \( S \) (the converse error); citing a line of the box after it has closed.
:::

::: {#exr-proving-an-implication-c4}
[C4: The assumptions a line depends on, used later]

Each line of a derivation depends on the premises and on the assumptions of the boxes it sits in. Take the first derivation in the proof of @prp-curry (lines 1–7).

::: {.enumerate options="label=(\alph*)"}
1. Beside each line, write the set of line numbers of the premises and assumptions it depends on.
2. For line 5 and for line 6, write the sequent whose premises are the statements on the lines of that set and whose conclusion is the statement of the line. Show that each is derivable, by turning the open assumptions into premises.
3. *(Challenge.)* Show that, in any derivation, the set of a line cited by an \( \rulename{\wedge I} \), \( \rulename{\wedge E} \) or \( \rulename{{\to}E} \) line is contained in the set of the citing line. Then say how the set of a \( \rulename{{\to}I} \) line compares with the set of the last line of the box it cites.
:::
:::

::: {.solution}
(a) Line 1: \( \{1\} \). Line 2: \( \{1, 2\} \). Lines 3, 4 and 5: \( \{1, 2, 3\} \). Line 6: \( \{1, 2\} \). Line 7: \( \{1\} \). The premise is in every set; the assumption of line 3 only in the sets of lines 3–5, the lines of its box; the assumption of line 2 in the sets of lines 2–6.

(b) Line 5 gives \( (P \wedge Q) \to R, \ P, \ Q \vdash R \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {P}
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
\end{nd}$
\end{center}
```

Line 6 gives \( (P \wedge Q) \to R, \ P \vdash Q \to R \); here the box of \( Q \) is kept, since line 6 lies outside it:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {Q \to R} \ii{3-5}
\end{nd}$
\end{center}
```

In each, the lines down to the chosen one, with the assumptions of the boxes still open there made premises, form a derivation.

(c) A line's set consists of the premises and the assumptions of the boxes containing it. Let line \( k \) cite line \( i \) by \( \rulename{\wedge I} \), \( \rulename{\wedge E} \) or \( \rulename{{\to}E} \). Then line \( i \) is available at line \( k \), so by the scope rule of @def-derivation every box containing line \( i \) also contains line \( k \). Hence the assumption of every such box is in the set of line \( k \), and the premises are in both sets: the set of \( i \) is contained in the set of \( k \).

For \( \rulename{{\to}I} \): the box's last line is a line of the box itself, so it lies in the cited box and in the boxes around it. The \( \rulename{{\to}I} \) line lies in exactly the boxes around the cited box (the condition for a box to be available). So the set of the \( \rulename{{\to}I} \) line is the set of the box's last line with one member removed: the line number of the box's assumption. That is the discharge, seen as a set.

**Marking scheme.** (10 points)

- 3: all seven sets correct (the premise in every set; line 3's assumption only in the sets of lines 3–5).
- 2: line 5's sequent, with a correct derivation.
- 2: line 6's sequent, with the box of \( Q \) kept.
- 3: (c) uses the scope rule for the containment, and names the one assumption that a \( \rulename{{\to}I} \) line drops.

Fatal errors (0 for the step): putting line 3 in the set of line 6 or line 7; treating an assumption as a premise of the whole derivation.
:::

<!-- dependency ledger
def-rules-implication (example): x > 2 gives x > 0, x^2 > 2x, 2x > 4 and x^2 > 4; all three fail at x = 0 | school algebra, AN1.1 (promised); checked by verify/ch01/def-rules-implication.py
def-rules-implication (example): each of and-I, and-E, ->E writes a conjunction or a piece of an earlier line, so without ->I an implication cannot be proved from nothing | inline (read off the schemas of def-rules-conjunction and def-rule-implication-elimination; not used in a proof)
prp-implication-transitive (example): x > 3 implies x^2 > 9 (x > 0, x^2 > 3x > 9); x^2 > 9 implies x^2 > 4 since 4 < 9 | school algebra, AN1.1 (promised); checked by verify/ch01/prp-implication-transitive.py
prp-implication-transitive (claim): "Argument B, diagnosed": n = 2k gives n^2 = 4k^2 = 2(2k^2) with 2k^2 an integer (line 2, "algebra") | inline school algebra (F1.1 §01's Argument B; the step from "n is even" to a k is used as school algebra, as F1.1 §01 says); checked by verify/ch01/prp-implication-transitive.py
prp-implication-transitive (claim): "Argument B, diagnosed": affirming the consequent ("from P -> Q and Q, conclude P") is a bad form | F1.1 §01 ("Try to break it", prose, no label) and F1.1 §04 ("Why nothing more", prose, no label), recalled in prose; broken again inline at x = -3 (x > 2 implies x^2 > 4 for every real x; 9 > 4; -3 > 2 false); checked by verify/ch01/prp-implication-transitive.py
prp-implication-transitive (claim): Quick check after "Argument B, diagnosed": x > 2 implies x^3 > 8 (a larger real number has a larger cube), and x^3 > 8 implies x > 2 (if x <= 2 then x^3 <= 2^3 = 8, by the same fact) | school algebra, AN1.1 (promised); checked by verify/ch01/prp-implication-transitive.py
def-derivation (example): the scope figure: each arrow and bracket legal or illegal as marked, and line 10 may cite lines 1, 5, 6, 9 and the box 7-8 | inline (read off def-derivation's scope rule); checked by verify/ch01/exr-proving-an-implication-a2.py
exm-illegal-citation (solution): x > 3 implies x > 2 and x > 2 implies x > 1 for every real x; 0 > 1 is false | school algebra, AN1.1 (promised); checked by verify/ch01/exm-illegal-citation.py
exm-illegal-citation (example): the warning's slip: x > 1 implies x^2 > 1; x^3 > 1 fails at x = 0 | school algebra, AN1.1 (promised); checked by verify/ch01/exm-illegal-citation.py
exm-first-boxes (solution): if a > 0 and x > 1 then ax > a (the reading of (c), not used in a derivation) | school algebra, AN1.1 (promised); checked by verify/ch01/exm-first-boxes.py
prp-curry (example): if x > 0 and y > 0 then xy > 0 (the reading, not used in a derivation) | school algebra, AN1.1 (promised); checked by verify/ch01/exm-first-boxes.py
exr-proving-an-implication-a2 (solution): (e)-(g) read off the scope rule on the figure; (h) lines 3-4 are not a box (the box runs to line 6); (j) at x = 0, x^2 > 9 is false | inline (def-derivation's scope rule and def-rules-implication, cited in the section); checked by verify/ch01/exr-proving-an-implication-a2.py
def-rules-implication (claim): "What each box is for": the printed annotation "asm, for ->I" names the rule whose line closes the box | the book's printing convention (read off the derivations of the section), not a fact used in any proof
exm-errors-that-cancel (solution): x = -4 gives x^2 = 16 > 9 and x > 3 false; x > 3 implies x^2 > 9 (x > 0, x^2 = x * x > 3x > 9) | school algebra, AN1.1 (promised); checked by verify/ch01/exm-errors-that-cancel.py
exm-proving-an-implication-instances (example): row 1's box reaches P and (P and not Q) by and-E, then and-I; row 2's box holds two nested boxes (P -> Q, then P) and is a derivation of its line; row 3 is a box of one line | read off def-rules-implication and def-derivation (cited in the section); each box written out as a derivation and checked mechanically by verify/ch01/exm-proving-an-implication-instances.py
exm-proving-an-implication-instances (example): the Not-allowed WRONG/RIGHT pair: (x > 5 and x > 0) implies x > 3 for every real x; at x = 1, x > 0 is true and x > 3 false | school algebra, AN1.1 (promised); checked by verify/ch01/exm-proving-an-implication-instances.py
exr-proving-an-implication-c4 (solution): (c) the scope rule of def-derivation (cited); a line's set is the premises with the assumptions of the boxes containing it | def-derivation (cited); the definition of the set is the exercise's own; (a) and (c) on this derivation checked by verify/ch01/exr-proving-an-implication-c4.py
exr-proving-an-implication-b2 (solution): x^2 >= 0 for every real x | school algebra, AN1.1 (promised)
exr-proving-an-implication-c1 (solution): (x > 2 and x > 3) implies x > 1 for every real x; 0 > 1 is false | school algebra, AN1.1 (promised)
exr-proving-an-implication-c3 (solution): x > 5 implies x > 4; x > 4 implies x^2 > 16 (x > 0, x^2 > 4x > 16); x^2 > 16 implies x^2 > 9 | school algebra, AN1.1 (promised); checked by verify/ch01/exr-proving-an-implication-c3.py
-->
