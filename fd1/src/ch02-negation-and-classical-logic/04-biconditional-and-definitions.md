# Iff, Equivalence, and What a Definition Says

One connective is still without rules: "if and only if". Theorems say "\( n \) is odd if and only if \( n^2 \) is odd", and every definition, though written with a plain "if", is used as an "if and only if". Section 1.1 warned that "if" means different things in a theorem and in a definition; this section explains why. The one new thing here is the pair of rules for \( \leftrightarrow \); the rest of the section (provable equivalence, the layout of an "iff" proof, the convention about definitions, chains of equivalences) is what the rules are used for.

## The rules for "if and only if"

"\( P \) if and only if \( Q \)" combines "\( P \) if \( Q \)", which is \( Q \to P \), with "\( P \) only if \( Q \)", which is \( P \to Q \), as @exr-statements-and-connectives-c1 explains. A proof of it travels both ways; a use of it, either way. An implication is proved by a box, opened on the hypothesis and closed on the conclusion (@def-rules-implication); an "if and only if" needs two such boxes.

*An "if and only if" is two implications, and proving it takes two proofs.*

::: {#def-rules-biconditional}
[Rules for the Biconditional]

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
\\[2ex]
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

The first schema is the rule \( \rulename{{\leftrightarrow}I} \) (**iff-introduction**); its two assumptions are discharged when their boxes close, and each box's last line (\( \psi \) in the first, \( \varphi \) in the second) is a line **of that box itself**, not of a box inside it. The two schemas below it are the two forms of \( \rulename{{\leftrightarrow}E} \) (**iff-elimination**).
:::

As in every schema (@def-rule-schema), \( \varphi \) and \( \psi \) stand for any statements, replaced consistently, and \( i, j, k, l, m \) for line numbers. Read the rules clause by clause.

1. **Two boxes.** \( \rulename{{\leftrightarrow}I} \) needs two available boxes: one opened by \( \varphi \) and ending in \( \psi \), the other opened by \( \psi \) and ending in \( \varphi \), each last line a line of its own box. Each is exactly the box \( \rulename{{\to}I} \) would need for one direction. Their order does not matter, but both must be there: a single box from \( \varphi \) to \( \psi \) proves \( \varphi \to \psi \) and nothing more. Each box's assumption is printed "asm, for \( \rulename{{\leftrightarrow}I} \)"; in a written proof the two boxes are the paragraphs \( (\Rightarrow) \) and \( (\Leftarrow) \).
2. **Separate boxes.** The boxes are siblings, not nested, so nothing in the second may cite a line of the first (the scope rule of @def-derivation). Each direction is a proof on its own.
3. **Citation.** The justification cites both boxes as ranges, as in \( \rulename{{\leftrightarrow}I}\ \lines{2}{4}, \lines{5}{7} \).
4. **Elimination, either way.** From \( \varphi \leftrightarrow \psi \) and \( \varphi \) on available lines, \( \rulename{{\leftrightarrow}E} \) writes \( \psi \); from \( \varphi \leftrightarrow \psi \) and \( \psi \), it writes \( \varphi \). It is modus ponens in whichever direction we need, citing the biconditional first.

In the Givens/Goal table, \( \rulename{{\leftrightarrow}I} \) splits a row in two: \( \varphi \) added to the Givens with the goal \( \psi \), and \( \psi \) added with the goal \( \varphi \).

## First derivations with iff

The section's goal-directed move: **a goal \( \varphi \leftrightarrow \psi \) opens two boxes**, one on each side, and each box's goal is the other side.

::: {#exm-iff-symmetric}
[An iff read both ways]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( P \leftrightarrow Q \vdash Q \leftrightarrow P \).
2. Show that \( P \leftrightarrow Q, \; \neg Q \vdash \neg P \).
:::
:::

::: {.solution}
(a) *Idea.* The goal is an iff, so the last line is \( \rulename{{\leftrightarrow}I} \), and we need a box from \( Q \) to \( P \) and a box from \( P \) to \( Q \). Each box's goal is one \( \rulename{{\leftrightarrow}E} \) away: the premise crosses from its assumption to the other side.

The goal at the foot (left), then its two boxes (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {Q \leftrightarrow P}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {P}
  \close
  \open
  \hypo {4} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {Q}
  \close
  \have {6} {Q \leftrightarrow P} \bi{2-3,4-5}
\end{nd}$
\end{center}
```

The finished derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {Q}
  \have {3} {P} \bie{1,2}
  \close
  \open
  \hypo {4} {P}
  \have {5} {Q} \bie{1,4}
  \close
  \have {6} {Q \leftrightarrow P} \bi{2-3,4-5}
\end{nd}$
\end{center}
```

Line 3 uses the second form of \( \rulename{{\leftrightarrow}E} \) (right to left), line 5 the first.

(b) *Idea.* The goal \( \neg P \) is a negation, so open a box on \( P \) and aim at \( \bot \) (Section 2.2). Inside, the premise \( P \leftrightarrow Q \) turns \( P \) into \( Q \), and \( Q \) clashes with \( \neg Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \bie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
\end{nd}$
\end{center}
```

This is the derivation of @prp-modus-tollens with \( \rulename{{\leftrightarrow}E} \) on line 4: if two statements are equivalent and one fails, so does the other.
:::

The rules say nothing that the two implications do not say. The next result makes this exact.

::: {#prp-iff-two-implications}
[An Iff Is Two Implications]

\( P \leftrightarrow Q \vdash (P \to Q) \wedge (Q \to P) \), and \( (P \to Q) \wedge (Q \to P) \vdash P \leftrightarrow Q \).
:::

::: {.idea}
Each goal chooses its rule. For the first, the goal is a conjunction of two implications: \( \rulename{\wedge I} \) needs both, and each is built in its own \( \rulename{{\to}I} \) box, crossing the premise with \( \rulename{{\leftrightarrow}E} \) inside. For the second, the goal is an iff: open its two boxes. The premise is a conjunction, so take it apart first (premise-directed), and cross each box with one of its halves by \( \rulename{{\to}E} \).

First claim: the two implications as goals (left), then their boxes (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {P \to Q}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {Q \to P}
  \have {8} {(P \to Q) \wedge (Q \to P)} \ai{4,7}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {P}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {Q}
  \close
  \have {4} {P \to Q} \ii{2-3}
  \open
  \hypo {5} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {P}
  \close
  \have {7} {Q \to P} \ii{5-6}
  \have {8} {(P \to Q) \wedge (Q \to P)} \ai{4,7}
\end{nd}$
\end{center}
```

Second claim: the premise taken apart (left), then the two boxes (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to P)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {Q \to P} \ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][8] {8} {P \leftrightarrow Q}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to P)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {Q \to P} \ae{1}
  \open
  \hypo {4} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {Q}
  \close
  \open
  \hypo {6} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {P}
  \close
  \have {8} {P \leftrightarrow Q} \bi{4-5,6-7}
\end{nd}$
\end{center}
```
:::

::: {.proof}
For the first claim, the following is a derivation with premise \( P \leftrightarrow Q \) and last line \( (P \to Q) \wedge (Q \to P) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \bie{1,2}
  \close
  \have {4} {P \to Q} \ii{2-3}
  \open
  \hypo {5} {Q}
  \have {6} {P} \bie{1,5}
  \close
  \have {7} {Q \to P} \ii{5-6}
  \have {8} {(P \to Q) \wedge (Q \to P)} \ai{4,7}
\end{nd}$
\end{center}
```

For the second claim, the following is a derivation with premise \( (P \to Q) \wedge (Q \to P) \) and last line \( P \leftrightarrow Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to P)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {Q \to P} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{2,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {P} \ie{3,6}
  \close
  \have {8} {P \leftrightarrow Q} \bi{4-5,6-7}
\end{nd}$
\end{center}
```

Lines 2 and 3 lie in no box, so both boxes may cite them. This proves both claims.
:::

::: {.second-reading title="Why iff keeps its own rules"}
So \( \leftrightarrow \) could have been an abbreviation for \( (P \to Q) \wedge (Q \to P) \). We keep it as a connective with its own rules, so that every connective is proved by an introduction rule and used by an elimination rule.
:::

::: {#exm-iff-negations}
[Negating both sides of an iff]

Show that \( P \leftrightarrow Q \vdash \neg P \leftrightarrow \neg Q \).
:::

::: {.solution}
*Idea.* The goal is an iff, so there are two boxes, one opened by \( \neg P \) and reaching \( \neg Q \), the other the reverse. Each box's goal is a negation, so each contains a \( \rulename{\neg I} \) box: the goal-directed move applied twice, one inside the other. Inside the inner box, \( \rulename{{\leftrightarrow}E} \) crosses from one side of the premise to the other, and the result clashes with the outer assumption. Each half is part (b) of @exm-iff-symmetric, run inside a box.

The outer boxes (left), then a \( \rulename{\neg I} \) box inside each (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {\neg P}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {\neg Q}
  \close
  \open
  \hypo {7} {\neg Q}
  \have[\ ][0] {} {\vdots}
  \have[][11] {11} {\neg P}
  \close
  \have {12} {\neg P \leftrightarrow \neg Q} \bi{2-6,7-11}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {\bot}
  \close
  \have {6} {\neg Q} \ni{3-5}
  \close
  \open
  \hypo {7} {\neg Q}
  \open
  \hypo {8} {P}
  \have[\ ][0] {} {\vdots}
  \have[][10] {10} {\bot}
  \close
  \have {11} {\neg P} \ni{8-10}
  \close
  \have {12} {\neg P \leftrightarrow \neg Q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

The finished derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {Q}
  \have {4} {P} \bie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg Q} \ni{3-5}
  \close
  \open
  \hypo {7} {\neg Q}
  \open
  \hypo {8} {P}
  \have {9} {Q} \bie{1,8}
  \have {10} {\bot} \ne{9,7}
  \close
  \have {11} {\neg P} \ni{8-10}
  \close
  \have {12} {\neg P \leftrightarrow \neg Q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

The two halves are mirror images.
:::

::: {.check}
In the derivation of @exm-iff-negations, which line does line 5 cite as \( \neg\varphi \), and why may it?
:::

::: {.solution}
Line 2, \( \neg P \), the assumption of the outer box \( \lines{2}{6} \), which is still open at line 5.
:::

The derivation uses only the rules of this section and of Sections 2.1–2.2. Its converse, \( \neg P \leftrightarrow \neg Q \vdash P \leftrightarrow Q \), is also derivable, with the rule of Section 2.5: in the box of \( P \) it must produce the **positive** statement \( Q \), and the natural box, on \( \neg Q \), closes to \( \neg\neg Q \), not \( Q \).

@exm-iff-negations negated both sides of an iff. Can one side be the negation of the other, a statement equivalent to its own negation?

::: {#lem-not-iff-own-negation}
[No Statement Is Equivalent to Its Negation]

\( \vdash \neg(P \leftrightarrow \neg P) \).
:::

::: {.idea}
The goal is a negation: open a \( \rulename{\neg I} \) box on \( P \leftrightarrow \neg P \), with goal \( \bot \). \( \rulename{{\leftrightarrow}E} \) needs one side of the iff on a line, and neither is. So make \( \neg P \) a subgoal, by a \( \rulename{\neg I} \) box on \( P \): inside it \( \rulename{{\leftrightarrow}E} \) gives \( \neg P \), which clashes with \( P \). With \( \neg P \) in hand, \( \rulename{{\leftrightarrow}E} \) the other way gives \( P \), and the two clash again.

The outer box (left), then the subgoal \( \neg P \) with its box (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \leftrightarrow \neg P} \purpose{\ni}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {\bot}
  \close
  \have {8} {\neg(P \leftrightarrow \neg P)} \ni{1-7}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \open
  \hypo {1} {P \leftrightarrow \neg P} \purpose{\ni}
  \open
  \hypo {2} {P} \purpose{\ni}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {\bot}
  \close
  \have {5} {\neg P} \ni{2-4}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {\bot}
  \close
  \have {8} {\neg(P \leftrightarrow \neg P)} \ni{1-7}
\end{nd}$
\end{center}
```
:::

::: {.proof}
The following is a derivation with no premises and last line \( \neg(P \leftrightarrow \neg P) \).

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \leftrightarrow \neg P}
  \open
  \hypo {2} {P}
  \have {3} {\neg P} \bie{1,2}
  \have {4} {\bot} \ne{2,3}
  \close
  \have {5} {\neg P} \ni{2-4}
  \have {6} {P} \bie{1,5}
  \have {7} {\bot} \ne{6,5}
  \close
  \have {8} {\neg(P \leftrightarrow \neg P)} \ni{1-7}
\end{nd}$
\end{center}
```

Line 5 may be cited at lines 6 and 7: it lies in the box \( \lines{1}{7} \), as they do. No rule of Section 2.5 is used.
:::

*In words: no statement is equivalent to its own negation; a definition that made a term mean the failure of that very term would define nothing.*

For an instance, let \( x \) be a real number. The sentence "\( x > 0 \) if and only if \( x \le 0 \)" is false whatever \( x \) is: by the convention of Section 2.1, \( x \le 0 \) is \( \neg(x > 0) \), so the sentence is an instance of \( P \leftrightarrow \neg P \), and the lemma, used as a derived rule, refutes every instance.

::: {.check}
In the proof of @lem-not-iff-own-negation, which two lines use the biconditional, and in which direction?
:::

::: {.solution}
Line 3, from the left side \( P \) (line 2) to the right side \( \neg P \); and line 6, from the right side \( \neg P \) (line 5) back to the left side \( P \).
:::

## Provable equivalence

@prp-iff-two-implications is a pair of sequents, one in each direction. It is not the first such pair: @prp-curry and @prp-distributivity are pairs too. When two statements can each be derived from the other, either may stand in for the other in any derivation, and the situation deserves a name.

*Two statements are provably equivalent when each can be derived from the other.*

::: {#def-provable-equivalence}
[Provable Equivalence]

Statements \( P \) and \( Q \) are **provably equivalent**, written \( P \dashv\vdash Q \), if \( P \vdash Q \) **and** \( Q \vdash P \).
:::

In words: there is a derivation with premise \( P \) and last line \( Q \), and **another** with premise \( Q \) and last line \( P \). The symbol is the turnstile of @def-derivable written twice, back to back; two derivations prove the claim.

A first example is \( P \wedge Q \dashv\vdash Q \wedge P \): @prp-and-commutes derives \( Q \wedge P \) from \( P \wedge Q \), and the same derivation with \( P \) and \( Q \) exchanged derives \( P \wedge Q \) from \( Q \wedge P \). By the same exchange, @exm-disjunction-first-derivations gives \( P \vee Q \dashv\vdash Q \vee P \), and part (a) of @exm-iff-symmetric gives \( P \leftrightarrow Q \dashv\vdash Q \leftrightarrow P \).

::: {.second-reading title="Edge cases of provable equivalence"}
The degenerate example is \( P \dashv\vdash P \): the one-line derivation of part (a) of @exm-derivations serves in both directions.

A minimal change gives a one-way street. @exm-double-negation-introduction derived \( P \vdash \neg\neg P \), but the converse, \( \neg\neg P \vdash P \), would have to remove two negations, and no rule met so far removes one. So we cannot claim \( P \dashv\vdash \neg\neg P \): the clause "\( Q \vdash P \)" is the one missing. (It holds once Section 2.5 adds its rule.) Likewise @prp-contrapositive derives \( \neg Q \to \neg P \) from \( P \to Q \), but not yet the reverse.
:::

The connective \( \leftrightarrow \) and the relation \( \dashv\vdash \) are two sides of one idea; the next result makes the link exact, and shows that \( \dashv\vdash \) behaves as an equivalence should.

::: {#prp-provable-equivalence-basics}
[Provable Equivalence and the Biconditional]

For all statements \( P \), \( Q \), \( R \):

::: {.enumerate options="label=(\alph*)"}
1. \( P \dashv\vdash Q \) if and only if \( \vdash P \leftrightarrow Q \);
2. \( P \dashv\vdash P \); if \( P \dashv\vdash Q \), then \( Q \dashv\vdash P \); and if \( P \dashv\vdash Q \) and \( Q \dashv\vdash R \), then \( P \dashv\vdash R \).
:::
:::

*In words: one derivation of \( P \leftrightarrow Q \) from no premises is worth two derivations, one each way; and \( \dashv\vdash \) can be used like \( = \) in a calculation.*

::: {.second-reading title="The proof: copying derivations"}
::: {.idea}
Everything here moves whole derivations around. To prove \( \vdash P \leftrightarrow Q \), the two boxes of \( \rulename{{\leftrightarrow}I} \) are the two given derivations, with their premises turned into the boxes' assumptions. To use \( \vdash P \leftrightarrow Q \), write out its derivation and apply \( \rulename{{\leftrightarrow}E} \). For transitivity, run one derivation into the next: the last line of the first is the premise of the second.
:::

::: {.proof}
We use one observation twice. Let \( D \) be a derivation, and copy its lines, in order and with their numbers shifted, to some place in another derivation, with every line of the copy inside the same boxes as that place. Then every citation inside the copy is still available: if line \( i \) of \( D \) is available at line \( k \) of \( D \), every box of \( D \) containing line \( i \) contains line \( k \), and the boxes added around the copy contain both lines. Closed boxes cited in \( D \) are handled the same way. So each copied line is justified by the same rule as before.

\( (\Rightarrow) \) in (a). Suppose \( P \vdash Q \) and \( Q \vdash P \), by derivations \( D_1 \) and \( D_2 \). Build a derivation with no premises as follows. Open a box with the assumption \( P \) and, below it, copy \( D_1 \), turning each of its premise lines \( P \) into a repetition of the assumption by (D3) of @def-derivation. By the observation, the copy is justified, and its last line \( Q \) is a line of the box itself, since the last line of \( D_1 \) lies in none of \( D_1 \)'s boxes. Close the box. Open a second box with \( Q \), copy \( D_2 \) in the same way, and close it on \( P \). Then \( \rulename{{\leftrightarrow}I} \) on the two boxes gives \( P \leftrightarrow Q \). So \( \vdash P \leftrightarrow Q \).

\( (\Leftarrow) \) in (a). Suppose \( \vdash P \leftrightarrow Q \), by a derivation \( D \) with no premises. For \( P \vdash Q \), start with the premise \( P \), copy \( D \) below it, and write \( Q \) by \( \rulename{{\leftrightarrow}E} \) from the last line of the copy, \( P \leftrightarrow Q \), and line 1. Both cited lines lie in no box, so both are available. For \( Q \vdash P \), do the same with premise \( Q \), using the other form of \( \rulename{{\leftrightarrow}E} \). So \( P \dashv\vdash Q \).

(b) The one-line derivation consisting of the premise \( P \) shows \( P \vdash P \), in both directions, so \( P \dashv\vdash P \). Symmetry holds because @def-provable-equivalence says the same thing about \( P, Q \) as about \( Q, P \). For transitivity it is enough to show that \( P \vdash Q \) and \( Q \vdash R \) give \( P \vdash R \), since the reverse direction is the same statement with \( P \) and \( R \) exchanged. Take a derivation \( D_1 \) of \( Q \) from \( P \), and below its last line copy a derivation \( D_2 \) of \( R \) from \( Q \), turning each premise line \( Q \) of \( D_2 \) into a repetition of the last line of \( D_1 \). That line lies in no box, so it is available everywhere below it, and by the observation the rest of the copy is justified. The result has premise \( P \) and last line \( R \). This proves the proposition.
:::
:::

Here are equivalences derived so far. Each row gives two derived rules (@def-derived-rule), one in each direction.

| Provable equivalence | Derived in |
|---|---|
| \( P \wedge Q \dashv\vdash Q \wedge P \) | @prp-and-commutes, with the letters exchanged for the converse |
| \( P \vee Q \dashv\vdash Q \vee P \) | @exm-disjunction-first-derivations, likewise |
| \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \) | @prp-curry |
| \( P \wedge (Q \vee R) \dashv\vdash (P \wedge Q) \vee (P \wedge R) \) | @prp-distributivity |
| \( (P \to R) \wedge (Q \to R) \dashv\vdash (P \vee Q) \to R \) | @exm-cases-on-hypothesis and @exm-or-hypothesis-split |
| \( P \leftrightarrow Q \dashv\vdash (P \to Q) \wedge (Q \to P) \) | @prp-iff-two-implications |
| \( P \leftrightarrow Q \dashv\vdash Q \leftrightarrow P \) | @exm-iff-symmetric (a), with the letters exchanged |

The fourth row is distributivity of \( \wedge \) over \( \vee \) as a provable equivalence. Some familiar laws are not in the table, because the text has derived them in one direction only; associativity of \( \vee \) is one (@exm-disjunction-regroup).

::: {.warning}
A sequent in one direction is not an equivalence. \( P \wedge Q \vdash P \) holds by \( \rulename{\wedge E} \), but the form "from \( P \) conclude \( P \wedge Q \)" breaks: take \( P \): "\( 2 > 1 \)" and \( Q \): "\( 1 > 2 \)", and the premise is true while the conclusion is false. Before writing \( \dashv\vdash \), check that **both** derivations exist.
:::

## Proving an iff: two directions

In a written proof, the two boxes of \( \rulename{{\leftrightarrow}I} \) become two paragraphs: \( (\Rightarrow) \) assumes the left side and reaches the right, \( (\Leftarrow) \) the reverse. Neither may borrow the other's assumption: they are two separate boxes.

The first example completes the story of parity. We use the facts (E1)–(E3) of Section 2.1: every integer is even or odd; no integer is both even and odd; the square of an odd integer is odd.

::: {#thm-odd-iff-square-odd}
[Odd Square, Odd Number]

Let \( n \) be an integer. Then \( n \) is odd if and only if \( n^2 \) is odd.
:::

::: {.idea}
Two boxes. Forwards is (E3). Backwards, "\( n^2 \) is odd" gives nothing to compute with, so split on (E1) and show the even case impossible, as in @exm-impossible-case.
:::

::: {.proof}
\( (\Rightarrow) \) This is (E3).

\( (\Leftarrow) \) Suppose \( n^2 \) is odd \( [\text{assumption for the second box}] \). By (E1), \( n \) is even or odd, and we argue by cases \( [\rulename{\vee E}] \). If \( n \) is odd, we are done. If \( n \) is even, say \( n = 2k \) with \( k \) an integer, then \( n^2 = 2(2k^2) \) is even; so \( n^2 \) is both even and odd \( [\rulename{\wedge I}] \), which contradicts (E2) \( [\rulename{\neg E}] \). So this case cannot occur, and \( n \) is odd in it too \( [\rulename{\bot E}] \). In both cases \( n \) is odd.

This proves the theorem \( [\rulename{{\leftrightarrow}I}] \).
:::

With the derived rules of Section 2.3, \( (\Leftarrow) \) fits in one breath, "\( n \) cannot be even, since then \( n^2 \) would be even; so \( n \) is odd": \( \rulename{\neg I} \) with (E2), then \( \rulename{MT} \), then \( \rulename{DS} \) on (E1).

The next example is about real numbers, and its two directions do different work. Each hypothesis is needed: dropping either one breaks one of the two directions, as the remark after the proof shows.

::: {#thm-squares-order}
[Squaring Preserves Order]

Let \( x \) and \( y \) be real numbers with \( x \ge 0 \) and \( y \ge 0 \). Then
\[
x \le y \iff x^2 \le y^2 .
\]
:::

::: {.idea}
Forwards, multiply \( x \le y \) by \( x \ge 0 \) and by \( y \ge 0 \), and chain. Backwards, nothing undoes squaring without square roots, so we split instead: either \( x \le y \), which is the goal, or \( y < x \). In the second case the forward argument, run with a strict inequality, gives \( y^2 < x^2 \), which clashes with the hypothesis: an impossible case, closed by \( \rulename{\bot E} \).
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( x \le y \). Multiplying by \( x \ge 0 \) gives \( x^2 \le xy \), and multiplying by \( y \ge 0 \) gives \( xy \le y^2 \). Hence \( x^2 \le y^2 \).

\( (\Leftarrow) \) Suppose \( x^2 \le y^2 \). For real numbers, \( x \le y \) or \( y < x \), and we argue by cases \( [\rulename{\vee E}] \). If \( x \le y \), we are done. If \( y < x \), then \( x > y \ge 0 \), so \( x > 0 \). Multiplying \( y < x \) by \( x > 0 \) gives \( xy < x^2 \), and multiplying \( y < x \) by \( y \ge 0 \) gives \( y^2 \le xy \). Hence \( y^2 < x^2 \), which contradicts \( x^2 \le y^2 \) \( [\rulename{\neg E}] \); so this case cannot occur, and \( x \le y \) holds in it \( [\rulename{\bot E}] \). In both cases \( x \le y \).

This proves the theorem \( [\rulename{{\leftrightarrow}I}] \).
:::

::: {.remark}
Each hypothesis has a job. The direction \( (\Rightarrow) \) needs \( x \ge 0 \), and fails without it: \( x = -2 \), \( y = 1 \) gives \( x \le y \) but \( x^2 = 4 > 1 = y^2 \). (Its proof also multiplied by \( y \ge 0 \), but there \( y \ge 0 \) already follows from \( y \ge x \ge 0 \).) The direction \( (\Leftarrow) \) used only \( y \ge 0 \), and fails without it: \( x = 1 \), \( y = -2 \) gives \( x^2 = 1 \le 4 = y^2 \) but \( x > y \).
:::

A payoff comes at once. For \( a, b \ge 0 \), apply @thm-squares-order to \( x = \sqrt{a} \) and \( y = \sqrt{b} \): \( \sqrt{a} \le \sqrt{b} \) if and only if \( a \le b \). Taking square roots preserves order, a fact used constantly in estimates. (That square roots of non-negative numbers exist is a school fact here.)

::: {.check}
Here is a proof of the statement "for a real number \( x \), \( x^2 = 1 \) if and only if \( x = 1 \) or \( x = -1 \)".

> If \( x = 1 \), then \( x^2 = 1 \cdot 1 = 1 \). If \( x = -1 \), then \( x^2 = (-1)(-1) = 1 \). This proves the claim.

Which direction has been proved, and which is missing? Supply the missing one.
:::

::: {.solution}
The proof assumes the right side, "\( x = 1 \) or \( x = -1 \)", splits it into its two cases, and reaches \( x^2 = 1 \) in both. So it proves \( (\Leftarrow) \), by \( \rulename{\vee E} \). The direction \( (\Rightarrow) \) is missing.

\( (\Rightarrow) \) Suppose \( x^2 = 1 \). Then \( (x - 1)(x + 1) = x^2 - 1 = 0 \). A product of real numbers is zero only if one of the factors is zero, so \( x - 1 = 0 \) or \( x + 1 = 0 \), that is, \( x = 1 \) or \( x = -1 \).
:::

::: {.warning}
A proof of an iff can prove one direction twice and look complete. For "\( n \) is odd if and only if \( n^2 \) is odd", a proof that shows "if \( n \) is odd, then \( n^2 \) is odd" and then "if \( n^2 \) is not odd, then \( n \) is not odd" has proved \( (\Rightarrow) \) and its contrapositive (@prp-contrapositive), which is \( (\Rightarrow) \) again. The direction \( (\Leftarrow) \), "if \( n^2 \) is odd, then \( n \) is odd", is still missing; its contrapositive would be "if \( n \) is not odd, then \( n^2 \) is not odd". Before writing "this proves the theorem", check that one paragraph assumes each side.
:::

## What a definition says

Here is a definition written the way this book and most others write definitions.

> A function \( f \colon \nR \to \nR \) is **strictly increasing** if, for all real numbers \( x \) and \( y \), \( x < y \) implies \( f(x) < f(y) \).

Grammatically the sentence is an implication, "\( f \) is strictly increasing **if** [condition]", and read as a theorem it would allow only one move, from the condition to the term. But a definition is not a theorem. It introduces a new term, and the new term means **exactly** the condition: no more, since nothing else was said about the term, and no less, since the condition is all the term was made to express. So the definition is used in both directions, as an \( \leftrightarrow \) between the term and the condition, and \( \rulename{{\leftrightarrow}E} \) is how it is used.

*In a definition, "if" means "if and only if".*

This is a convention of mathematical language, not a rule of logic. Some books write "iff" or \( :\Leftrightarrow \) in definitions; this book, like most, writes "if" and puts the term defined in **bold**, which signals that the "if" is an "iff". Here it is used three ways.

::: {#exm-strictly-increasing-both-ways}
[A definition used in both directions]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( f(x) = 3x - 5 \) defines a strictly increasing function \( f \colon \nR \to \nR \).
2. Suppose \( g \colon \nR \to \nR \) is strictly increasing. Show that \( g(1) < g(2) \).
3. Show that \( h(x) = x^2 \) does not define a strictly increasing function \( h \colon \nR \to \nR \).
:::
:::

::: {.solution}
(a) Let \( x \) and \( y \) be real numbers with \( x < y \). Multiplying by \( 3 > 0 \) gives \( 3x < 3y \), and subtracting \( 5 \) gives \( 3x - 5 < 3y - 5 \), that is, \( f(x) < f(y) \). So \( f \) satisfies the condition, and by the definition, read from right to left, \( f \) is strictly increasing \( [\rulename{{\leftrightarrow}E}] \).

(b) Since \( g \) is strictly increasing, the definition, read from left to right, says that \( x < y \) implies \( g(x) < g(y) \) for all real \( x \) and \( y \) \( [\rulename{{\leftrightarrow}E}] \). Taking \( x = 1 \) and \( y = 2 \), and using \( 1 < 2 \), we get \( g(1) < g(2) \) \( [\rulename{{\to}E}] \).

(c) Suppose \( h \) were strictly increasing \( [\text{assumption for } \rulename{\neg I}] \). By the definition read from left to right, as in (b), \( -1 < 0 \) would give \( h(-1) < h(0) \), that is, \( 1 < 0 \), which is false \( [\rulename{\neg E}] \). So \( h \) is not strictly increasing \( [\rulename{\neg I}] \).
:::

Part (a) uses the definition from the condition to the term; parts (b) and (c) use it from the term to the condition. A definition read only as an "if" would permit (a) and nothing else.

::: {.warning}
The convention is for **definitions only**. In a theorem, "if" means "if", one direction. The theorem "if \( 6 \mid n \), then \( n \) is even" is true for every integer \( n \): \( n = 6k = 2(3k) \). Its converse, "if \( n \) is even, then \( 6 \mid n \)", breaks at \( n = 4 \). Reading a theorem's "if" as "iff" means proving its converse without a proof, which is the error of Argument B in Section 1.1.
:::

::: {.second-reading title="The same slip in calculus"}
A familiar theorem of calculus says: if \( f \) is differentiable at \( a \), then \( f \) is continuous at \( a \). Its converse is false. The function \( f(x) = \abs{x} \) is continuous at \( 0 \), but it is not differentiable there, since its graph has a corner: the quotient \( \abs{h}/h \) is \( 1 \) for \( h > 0 \) and \( -1 \) for \( h < 0 \).
:::

::: {.check}
Write the converse of "if a real number \( x \) satisfies \( x > 2 \), then \( x^2 > 4 \)", and break it.
:::

::: {.solution}
The converse is "if \( x^2 > 4 \), then \( x > 2 \)". The value \( x = -3 \) breaks it: \( (-3)^2 = 9 > 4 \), and \( -3 > 2 \) fails.
:::

## Chains of equivalences

"The following are equivalent: (a), (b), (c)" means that any two of the three are equivalent: three iff statements, or six implications. Three implications suffice, if they go round in a cycle:
\[
\text{(a)} \Rightarrow \text{(b)} \Rightarrow \text{(c)} \Rightarrow \text{(a)} .
\]
Once the cycle is proved, any condition leads to any other by following the arrows round. Here is the derivation behind that sentence.

::: {#prp-equivalence-cycle}
[Proving Equivalence by a Cycle]

\( P \to Q, \; Q \to R, \; R \to P \vdash P \leftrightarrow Q \). Likewise, from the same three premises, \( Q \leftrightarrow R \) and \( R \leftrightarrow P \) are derivable.
:::

::: {.idea}
The goal is an iff, so there are two boxes. From \( P \), one step along the cycle reaches \( Q \). From \( Q \), the cycle reaches \( P \) the long way round, through \( R \): a backward chain of \( \rulename{{\to}E} \), as in Section 1.3. The other two equivalences need no new work, because the three premises do not change when the letters are rotated.

The goal at the foot (left), then its two boxes (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {R \to P}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {P \leftrightarrow Q}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {R \to P}
  \open
  \hypo {4} {P}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {Q}
  \close
  \open
  \hypo {6} {Q}
  \have[\ ][0] {} {\vdots}
  \have[][8] {8} {P}
  \close
  \have {9} {P \leftrightarrow Q} \bi{4-5,6-8}
\end{nd}$
\end{center}
```
:::

::: {.proof}
The following is a derivation with the three premises and last line \( P \leftrightarrow Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {R \to P}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{1,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {R} \ie{2,6}
  \have {8} {P} \ie{3,7}
  \close
  \have {9} {P \leftrightarrow Q} \bi{4-5,6-8}
\end{nd}$
\end{center}
```

Now replace \( P \), \( Q \), \( R \) throughout by \( Q \), \( R \), \( P \) respectively. The premises \( P \to Q \), \( Q \to R \), \( R \to P \) become \( Q \to R \), \( R \to P \), \( P \to Q \), the same three statements in a different order, and every line remains justified by the same rule. So the renamed derivation derives \( Q \leftrightarrow R \) from the same premises. Rotating once more gives \( R \leftrightarrow P \). This proves the proposition.
:::

In a cycle every condition reaches every other along the arrows; longer cycles work the same way.

::: {.warning}
Two arrows back and forth are not a cycle through three conditions. Proving (a) \( \Rightarrow \) (b) and (b) \( \Rightarrow \) (a) shows that (a) and (b) are equivalent and says nothing about (c): no arrow enters or leaves it. For a real number \( x \), take (a) "\( x > 0 \)", (b) "\( 2x > 0 \)", and (c) "\( x > 1 \)". Both arrows between (a) and (b) are true, and (c) is not equivalent to them: \( x = \frac{1}{2} \) satisfies (a) and (b) but not (c). Every condition in the list must lie on the cycle.
:::

::: {#exm-unit-interval-tfae}
[Three descriptions of the unit interval]

Let \( x \) be a real number. Prove that the following are equivalent.

::: {.enumerate options="label=(\alph*)"}
1. \( 0 < x < 1 \).
2. \( x^2 < x \).
3. \( x > 0 \) and \( 1/x > 1 \).
:::
:::

::: {.solution}
By @prp-equivalence-cycle it suffices to prove (a) \( \Rightarrow \) (b) \( \Rightarrow \) (c) \( \Rightarrow \) (a).

*(a) \( \Rightarrow \) (b).* Suppose \( 0 < x < 1 \). Multiplying \( x < 1 \) by \( x > 0 \) gives \( x^2 < x \).

*(b) \( \Rightarrow \) (c).* Suppose \( x^2 < x \). First, \( x > 0 \): otherwise \( x \le 0 \), and then \( x \le 0 \le x^2 \), so \( x \le x^2 \), which contradicts \( x^2 < x \). (In rules: we have \( x \le 0 \) or \( x > 0 \); the first is refuted by a \( \rulename{\neg I} \) box, and \( \rulename{DS} \) (@prp-disjunctive-syllogism) leaves the second.) Since \( x > 0 \), we may divide \( x^2 < x \) by \( x \), which gives \( x < 1 \), and then divide \( x < 1 \) by \( x \), which gives \( 1 < 1/x \). So \( x > 0 \) and \( 1/x > 1 \).

*(c) \( \Rightarrow \) (a).* Suppose \( x > 0 \) and \( 1/x > 1 \). Multiplying \( 1 < 1/x \) by \( x > 0 \) gives \( x < 1 \). So \( 0 < x < 1 \).
:::

The order of the cycle was a choice, made so that each arrow was short: (b) \( \Rightarrow \) (c) carried the only case split. The reverse cycle would also do, with different arrows to prove.

## The rule card

Before the card, the two rules at work on large statements.

::: {#exm-biconditional-and-definitions-instances}
[Instances of \( \rulename{{\leftrightarrow}I} \) and \( \rulename{{\leftrightarrow}E} \)]

| Rule | Letters replaced | Cited | New line |
|---|---|---|---|
| \( \rulename{{\leftrightarrow}I} \) | \( \varphi \coloneqq P \wedge Q \), \( \psi \coloneqq Q \wedge P \) | box \( P \wedge Q \) … \( Q \wedge P \), box \( Q \wedge P \) … \( P \wedge Q \) | \( (P \wedge Q) \leftrightarrow (Q \wedge P) \) |
| \( \rulename{{\leftrightarrow}E} \) | \( \varphi \coloneqq \neg P \), \( \psi \coloneqq Q \to R \) | \( \neg P \leftrightarrow (Q \to R) \), \( Q \to R \) | \( \neg P \) (the second form) |
| \( \rulename{{\leftrightarrow}E} \) | \( \varphi \coloneqq P \vee Q \), \( \psi \coloneqq \neg R \) | \( (P \vee Q) \leftrightarrow \neg R \), \( P \vee Q \) | \( \neg R \) |

**Not an instance.** From two lines \( P \to Q \) and \( Q \to P \), the line "\( P \leftrightarrow Q \) — \( \rulename{{\leftrightarrow}I} \)" is not an instance: \( \rulename{{\leftrightarrow}I} \) cites two boxes, not two implications. The two lines give the iff through @prp-iff-two-implications used as a derived rule (after \( \rulename{\wedge I} \)), or by opening the two boxes.
:::

Chapter 1's seven rules are on the card at the end of Section 1.6; here are this chapter's so far.

| Rule | Shape | You write | Lean |
|---|---|---|---|
| \( \rulename{\neg E} \) | \( \varphi \), \( \neg\varphi \) \( \Longrightarrow \) \( \bot \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
| \( \rulename{\bot E} \) | \( \bot \) \( \Longrightarrow \) any \( \varphi \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |
| \( \rulename{\neg I} \) | box \( \varphi \) … \( \bot \) \( \Longrightarrow \) \( \neg\varphi \) | "Suppose \( P \). … This is a contradiction. Hence not \( P \)." | `intro hp` (goal `False`) |
| \( \rulename{MT} \) | \( \varphi \to \psi \), \( \neg\psi \) \( \Longrightarrow \) \( \neg\varphi \) (derived) | "Since \( Q \) fails, so does \( P \)." | `mt h hnq` |
| \( \rulename{CP} \) | \( \varphi \to \psi \) \( \Longrightarrow \) \( \neg\psi \to \neg\varphi \) (derived) | "We prove the contrapositive: suppose not \( Q \); … so not \( P \)." | `mt` |
| \( \rulename{DS} \) | \( \varphi \vee \psi \), \( \neg\varphi \) \( \Longrightarrow \) \( \psi \) (derived) | "\( P \) is impossible, so \( Q \)." | `h.resolve_left hnp` |
| \( \rulename{{\leftrightarrow}I} \) | box \( \varphi \) … \( \psi \), box \( \psi \) … \( \varphi \) \( \Longrightarrow \) \( \varphi \leftrightarrow \psi \) | "\( (\Rightarrow) \) Suppose \( P \). … so \( Q \). \( (\Leftarrow) \) Suppose \( Q \). … so \( P \)." | `constructor` |
| \( \rulename{{\leftrightarrow}E} \) | \( \varphi \leftrightarrow \psi \), \( \varphi \) \( \Longrightarrow \) \( \psi \) (or with \( \psi \), \( \varphi \)) | "Since \( P \) holds if and only if \( Q \) does, and \( P \) holds, so does \( Q \)." | `h.mp hp` / `h.mpr hq` |

The rows for this section's rules complete the table for the connectives. The Lean names in the last column come from the two fields of an iff, `mp` ("modus ponens", left to right) and `mpr` (right to left).

::: {.warning}
[Not allowed: \( \rulename{{\leftrightarrow}I} \) and \( \rulename{{\leftrightarrow}E} \)]

Each step below is wrong; the tag names the clause it breaks.

- Close \( \rulename{{\leftrightarrow}I} \) with one box: clause 1, two boxes (a single box proves \( \varphi \to \psi \) only).
- In the second box, cite a line of the first: clause 2, the boxes are siblings (the pair below).
- Write \( \neg\psi \) by \( \rulename{{\leftrightarrow}E} \) from \( \varphi \leftrightarrow \psi \) and \( \neg\varphi \): clause 4, \( \rulename{{\leftrightarrow}E} \) needs one side itself; \( \neg\psi \) takes a \( \rulename{\neg I} \) box.
- Write \( \varphi \leftrightarrow \psi \) by \( \rulename{{\leftrightarrow}I} \) citing two implication lines: clause 3, the rule cites boxes, as ranges (the look-alike of @exm-biconditional-and-definitions-instances).

Clause 2 is where the rule bites: WRONG beside RIGHT, with premises \( P \to Q \), \( R \) and \( (Q \wedge R) \to P \). On the left, line 7 copies \( P \) from the closed first box.

```{=latex}
\begin{center}
% expect-invalid: line 7 repeats line 4, a line of the closed sibling box 4-5
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {R}
  \hypo {3} {(Q \wedge R) \to P}
  \open
  \hypo {4} {P} \purpose{\bi}
  \have {5} {Q} \ie{1,4}
  \close
  \open
  \hypo {6} {Q} \purpose{\bi}
  \have {7} {P} \r{4}
  \close
  \have {8} {P \leftrightarrow Q} \bi{4-5,6-7}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {R}
  \hypo {3} {(Q \wedge R) \to P}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{1,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {Q \wedge R} \ai{6,2}
  \have {8} {P} \ie{3,7}
  \close
  \have {9} {P \leftrightarrow Q} \bi{4-5,6-8}
\end{nd}$
\end{center}
```

The left list never cites premises 2 and 3, so it would show \( P \to Q \vdash P \leftrightarrow Q \), which breaks: with \( P \): "\( x > 5 \)" and \( Q \): "\( x > 3 \)", at \( x = 4 \) the premise is true and \( P \leftrightarrow Q \) is false.
:::

::: {.remark}
[Looking ahead]

Chapter 5 uses the lemma \( \neg(P \leftrightarrow \neg P) \) to show that no barber can shave exactly those who do not shave themselves, and in what sense no set can contain exactly the sets that do not contain themselves. *Analysis on the Real Line*, Chapter 1 proves from its axioms that every non-negative real number has a square root, the school fact behind the square-root payoff above.
:::

## Exercises

### A. Check your understanding

::: {#exr-biconditional-and-definitions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the rules \( \rulename{{\leftrightarrow}I} \) and \( \rulename{{\leftrightarrow}E} \), and the definition of \( P \dashv\vdash Q \).
2. For a real number \( x \ge 0 \), consider "\( x^2 = x \) if and only if \( x = 0 \) or \( x = 1 \)". Write the directions \( (\Rightarrow) \) and \( (\Leftarrow) \) as implications. Which one would a proof begin with "Suppose \( x^2 = x \)"?
3. True or false, with a reason: from the definition "an integer \( n \) is **even** if there is an integer \( k \) with \( n = 2k \)" and the fact that \( 10 \) is even, we may conclude that \( 10 = 2k \) for some integer \( k \).
4. True or false, with a reason: from the theorem "if \( x > 1 \), then \( x^2 > 1 \)" and the fact that \( x^2 > 1 \), we may conclude that \( x > 1 \).
:::
:::

::: {.solution}
(a) \( \rulename{{\leftrightarrow}I} \): from a box \( \varphi \dots \psi \) and a box \( \psi \dots \varphi \), both available, write \( \varphi \leftrightarrow \psi \). \( \rulename{{\leftrightarrow}E} \): from \( \varphi \leftrightarrow \psi \) and either side, write the other (@def-rules-biconditional). \( P \dashv\vdash Q \) means \( P \vdash Q \) and \( Q \vdash P \) (@def-provable-equivalence).

(b) \( (\Rightarrow) \): if \( x^2 = x \), then \( x = 0 \) or \( x = 1 \). \( (\Leftarrow) \): if \( x = 0 \) or \( x = 1 \), then \( x^2 = x \). The direction \( (\Rightarrow) \) begins "Suppose \( x^2 = x \)", since it assumes the left side.

(c) True. A definition's "if" means "if and only if", so the definition may be used from the term "even" to the condition, by \( \rulename{{\leftrightarrow}E} \). (Indeed \( k = 5 \).)

(d) False. A theorem's "if" is one direction only, and the conclusion would be its converse. The converse fails at \( x = -2 \): \( x^2 = 4 > 1 \) but \( x < 1 \).
:::

::: {#exr-biconditional-and-definitions-a2}
[A2: Drill]

The parts run from one step, through a missing line, a justification column and steps to judge, to short derivations.

::: {.enumerate options="label=(\alph*)"}
1. Lines 1 \( P \leftrightarrow Q \), 2 \( Q \). What does "\( \rulename{{\leftrightarrow}E} \) 1, 2" write?
2. A box \( \lines{3}{6} \) runs from \( P \vee Q \) to \( \neg R \), and a box \( \lines{7}{9} \) from \( \neg R \) to \( P \vee Q \). What does "\( \rulename{{\leftrightarrow}I} \) 3–6, 7–9" write?
3. Write "\( x^2 = 4 \) if and only if \( x = 2 \) or \( x = -2 \)" as two implications. Which begins "Suppose \( x^2 = 4 \)"?
4. Definition: "an integer \( n \) is a **multiple of 3** if \( n = 3k \) for some integer \( k \)". From \( 12 = 3 \cdot 4 \), what follows, reading the definition which way?
5. Line 6 is \( Q \wedge R \), justified "\( \rulename{{\leftrightarrow}E} \) 2, 5", and line 2 is \( P \leftrightarrow (Q \wedge R) \). What is line 5?
6. Line 12 is \( \neg P \leftrightarrow Q \), justified "\( \rulename{{\leftrightarrow}I} \) 4–7, 8–11". What are lines 4, 7, 8 and 11?
7. Fill in the justifications (i)–(iv).

    ```{=latex}
    \begin{center}
    $\begin{nd}
      \hypo {1} {P \leftrightarrow \neg Q}
      \hypo {2} {Q}
      \open
      \hypo {3} {P} \by{(i)}{}
      \have {4} {\neg Q} \by{(ii)}{}
      \have {5} {\bot} \by{(iii)}{}
      \close
      \have {6} {\neg P} \by{(iv)}{}
    \end{nd}$
    \end{center}
    ```

8. Lines 1 \( P \leftrightarrow Q \), 2 \( \neg P \). Does \( \rulename{{\leftrightarrow}E} \) give anything?
9. A box \( \lines{2}{4} \) runs from \( P \) to \( Q \); a box \( \lines{5}{7} \) from \( Q \) to \( P \), and line 6 cites line 3. Is "\( P \leftrightarrow Q \) — \( \rulename{{\leftrightarrow}I} \) 2–4, 5–7" correct?
10. One box runs from \( P \) to \( Q \). What does it prove?
11. True or false: \( P \dashv\vdash Q \) says that \( \vdash P \to Q \).
12. A proof that (a), (b), (c) are equivalent proves (a) \( \Rightarrow \) (b), (b) \( \Rightarrow \) (a) and (b) \( \Rightarrow \) (c). Is it complete?
13. Derive \( P \leftrightarrow Q, \ P \vdash Q \wedge P \).
14. Derive \( P \leftrightarrow Q, \ Q \leftrightarrow R, \ R \vdash P \).
15. Derive \( P \leftrightarrow Q, \ \neg P \vdash \neg Q \).
:::
:::

::: {.solution}
(a) \( P \), by the second form.

(b) \( (P \vee Q) \leftrightarrow \neg R \): the first box's assumption on the left, its last line on the right.

(c) \( (\Rightarrow) \) if \( x^2 = 4 \), then \( x = 2 \) or \( x = -2 \); \( (\Leftarrow) \) the converse. The direction \( (\Rightarrow) \) begins "Suppose \( x^2 = 4 \)".

(d) \( 12 \) is a multiple of \( 3 \), reading the definition from the condition to the term (\( \rulename{{\leftrightarrow}E} \)).

(e) \( P \), the left side, so that the first form writes the right side \( Q \wedge R \).

(f) Line 4 is \( \neg P \) and line 7 is \( Q \) (the first box); line 8 is \( Q \) and line 11 is \( \neg P \) (the second).

(g) (i) assumption, for \( \rulename{\neg I} \); (ii) \( \rulename{{\leftrightarrow}E} \) 1, 3; (iii) \( \rulename{\neg E} \) 2, 4; (iv) \( \rulename{\neg I} \) \( \lines{3}{5} \).

(h) No: \( \rulename{{\leftrightarrow}E} \) needs \( P \) or \( Q \) itself. \( \neg Q \) comes by a \( \rulename{\neg I} \) box, as in part (o).

(i) No: line 6 cites line 3, inside the closed sibling box \( \lines{2}{4} \).

(j) \( P \to Q \), by \( \rulename{{\to}I} \); not \( P \leftrightarrow Q \).

(k) False: it says \( P \vdash Q \) and \( Q \vdash P \), two derivations (equivalently \( \vdash P \leftrightarrow Q \)).

(l) No: no arrow leaves (c). Add (c) \( \Rightarrow \) (a) or (c) \( \Rightarrow \) (b).

(m) 3 \( Q \), \( \rulename{{\leftrightarrow}E} \) 1, 2; 4 \( Q \wedge P \), \( \rulename{\wedge I} \) 3, 2.

(n) 4 \( Q \), \( \rulename{{\leftrightarrow}E} \) 2, 3; 5 \( P \), \( \rulename{{\leftrightarrow}E} \) 1, 4.

(o) 3 \( Q \), assumption, for \( \rulename{\neg I} \); 4 \( P \), \( \rulename{{\leftrightarrow}E} \) 1, 3; 5 \( \bot \), \( \rulename{\neg E} \) 4, 2; 6 \( \neg Q \), \( \rulename{\neg I} \) \( \lines{3}{5} \).
:::

### B. Practice

::: {#exr-biconditional-and-definitions-b1}
[B1: Iff is transitive]

Show that \( P \leftrightarrow Q, \; Q \leftrightarrow R \vdash P \leftrightarrow R \).
:::

::: {.solution}
The goal is an iff, so we open two boxes: \( P \) to \( R \), and \( R \) to \( P \). In each, the premises are used as bridges, one after the other, by \( \rulename{{\leftrightarrow}E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \hypo {2} {Q \leftrightarrow R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \bie{1,3}
  \have {5} {R} \bie{2,4}
  \close
  \open
  \hypo {6} {R}
  \have {7} {Q} \bie{2,6}
  \have {8} {P} \bie{1,7}
  \close
  \have {9} {P \leftrightarrow R} \bi{3-5,6-8}
\end{nd}$
\end{center}
```

Lines 4 and 8 use \( P \leftrightarrow Q \) in opposite directions, as do lines 5 and 7 with \( Q \leftrightarrow R \).
:::

::: {#exr-biconditional-and-definitions-b2}
[B2: A parity equivalence]

Let \( n \) be an integer. Prove that \( n \) is even if and only if \( n + 3 \) is odd.
:::

::: {.solution}
\( (\Rightarrow) \) Suppose \( n \) is even, say \( n = 2k \) with \( k \) an integer. Then \( n + 3 = 2k + 2 + 1 = 2(k + 1) + 1 \), and \( k + 1 \) is an integer, so \( n + 3 \) is odd.

\( (\Leftarrow) \) Suppose \( n + 3 \) is odd, say \( n + 3 = 2j + 1 \) with \( j \) an integer. Then \( n = 2j - 2 = 2(j - 1) \), and \( j - 1 \) is an integer, so \( n \) is even.

This proves the equivalence.
:::

::: {#exr-biconditional-and-definitions-b3}
[B3: Strict inequalities]

Let \( x \) and \( y \) be real numbers with \( x \ge 0 \) and \( y \ge 0 \). Deduce from @thm-squares-order and @exm-iff-negations that \( x < y \) if and only if \( x^2 < y^2 \). You may use that, for real numbers \( a \) and \( b \), \( a < b \) holds exactly when \( b \le a \) fails.

::: {.enumerate options="label=(\alph*)"}
1. Apply @thm-squares-order with the roles of \( x \) and \( y \) exchanged. What does it say?
2. Use @exm-iff-negations as a derived rule on (a): with which statements in place of \( P \) and \( Q \), and what does it give?
3. Translate both sides of (b) with the fact quoted.
4. What have you proved?
:::
:::

::: {.solution}
(a) The exchange is allowed, since both numbers are non-negative: \( y \le x \) if and only if \( y^2 \le x^2 \).

(b) With \( P \): "\( y \le x \)" and \( Q \): "\( y^2 \le x^2 \)", @exm-iff-negations, used as a derived rule (@def-derived-rule), gives: \( y \le x \) fails if and only if \( y^2 \le x^2 \) fails.

(c) By the fact quoted, the left side says \( x < y \) and the right side says \( x^2 < y^2 \).

(d) That \( x < y \) if and only if \( x^2 < y^2 \).
:::

::: {#exr-biconditional-and-definitions-b4}
[B4: Both directions]

A search for \( P \leftrightarrow Q \vdash (P \wedge R) \leftrightarrow (Q \wedge R) \) has reached the stage below. *Name the move, then complete it.*

```{=latex}
% schema (partial derivation: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \have[\ ][0] {} {\vdots}
  \have[][12] {12} {(P \wedge R) \leftrightarrow (Q \wedge R)} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The move is *two boxes for an iff*: the goal's main connective is \( \leftrightarrow \), so line 12 will be \( \rulename{{\leftrightarrow}I} \), with a box from \( P \wedge R \) to \( Q \wedge R \) and a box back. Inside each, take the conjunction apart, cross with \( \rulename{{\leftrightarrow}E} \), and rebuild.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {P \wedge R}
  \have {3} {P} \ae{2}
  \have {4} {R} \ae{2}
  \have {5} {Q} \bie{1,3}
  \have {6} {Q \wedge R} \ai{5,4}
  \close
  \open
  \hypo {7} {Q \wedge R}
  \have {8} {Q} \ae{7}
  \have {9} {R} \ae{7}
  \have {10} {P} \bie{1,8}
  \have {11} {P \wedge R} \ai{10,9}
  \close
  \have {12} {(P \wedge R) \leftrightarrow (Q \wedge R)} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

The second box never cites a line of the first: line 10 gets \( P \) afresh from line 8.
:::

::: {#exr-biconditional-and-definitions-b5}
[B5: Criticize the definition]

For real numbers \( a \), \( b \), \( x \), we want to define "\( x \) lies **strictly between** \( a \) and \( b \)", meaning that one of \( a \), \( b \) is less than \( x \) and \( x \) is less than the other. Here are five candidate conditions.

::: {.enumerate options="label=(\roman*)"}
1. \( a < x \) and \( x < b \).
2. \( a < x \) or \( x < b \).
3. (\( a < x \) and \( x < b \)) or (\( b < x \) and \( x < a \)).
4. \( (x - a)(x - b) < 0 \).
5. \( x \le a \) fails and \( b \le x \) fails.
:::

::: {.enumerate options="label=(\alph*)"}
1. For each, say whether it is too broad (it admits a triple \( a, b, x \) that should be excluded), too narrow (it excludes one that should be admitted), or right, giving a triple for each fault.
2. A definition is read as an iff. Prove that (iii) and (iv) are equivalent.
3. Which candidates would make "if \( x \) lies strictly between \( a \) and \( b \), then \( x \) lies strictly between \( b \) and \( a \)" false? Give one triple that shows it for all of them.
:::
:::

::: {.solution}
(a) (i) Too narrow: \( a = 5 \), \( b = 2 \), \( x = 3 \) lies between and fails (i). It is not too broad: (i) gives one of the wanted orders.

(ii) Too broad: \( a = 2 \), \( b = 5 \), \( x = 100 \) satisfies \( 2 < 100 \) but does not lie between. And too narrow: \( a = 5 \), \( b = 2 \), \( x = 3 \) lies between, but \( 5 < 3 \) and \( 3 < 2 \) both fail (the triple of (c)).

(iii) Right: it lists the two possible orders.

(iv) Right, by (b).

(v) This is (i) in negative dress: by the convention of Section 2.1, "\( x \le a \) fails" is \( a < x \) and "\( b \le x \) fails" is \( x < b \). So it is too narrow, by the same triple as (i), and needlessly negative.

(b) \( (\Rightarrow) \) In the case \( a < x < b \), \( x - a > 0 \) and \( x - b < 0 \), so the product is negative. In the case \( b < x < a \), \( x - a < 0 \) and \( x - b > 0 \), so again the product is negative. The two cases are \( \rulename{\vee E} \) on (iii).

\( (\Leftarrow) \) Suppose the product is negative. Then neither factor is \( 0 \), and the two factors cannot have the same sign, since a product of two positive or of two negative numbers is positive. So \( x - a > 0 > x - b \), that is \( a < x < b \), or \( x - a < 0 < x - b \), that is \( b < x < a \).

(c) (i), (ii) and (v). With \( a = 2 \), \( b = 5 \), \( x = 3 \), each holds for the ends \( 2, 5 \) and fails for the ends \( 5, 2 \) (for (ii): \( 2 < 3 \), while neither \( 5 < 3 \) nor \( 3 < 2 \)). A definition of "between" should not depend on the order of the two ends; (iii) and (iv) do not, since exchanging \( a \) and \( b \) exchanges the two disjuncts of (iii) and the two factors of (iv).

**Marking scheme.** (10 points)
- 4: (a), one point each for (i) and (v) with a correct triple, one for (ii) with **both** triples (too broad and too narrow), and one for calling (iii) and (iv) right.
- 4: (b), each direction 2; the second must say why the factors have opposite signs.
- 2: (c), (i), (ii) and (v) with one triple.

Fatal error (0 for (b)): proving only one direction and calling the conditions equivalent.
:::

::: {#exr-biconditional-and-definitions-b6}
[B6: Four conditions, one cycle]

Let \( n \) be an integer. Prove by one cycle of four implications that the following are equivalent.

::: {.enumerate options="label=(\roman*)"}
1. \( n \) is odd.
2. \( n + 1 \) is even.
3. \( 8 \mid n^2 - 1 \).
4. \( n^2 \) is odd.
:::

You may use @thm-odd-iff-square-odd and the fact that \( k(k - 1) \) is even for every integer \( k \). Then: a proof that proved only (i) \( \Leftrightarrow \) (ii) and (iii) \( \Leftrightarrow \) (iv) would be incomplete; which two implications would complete it most cheaply?
:::

::: {.solution}
We prove the cycle (i) \( \Rightarrow \) (ii) \( \Rightarrow \) (iii) \( \Rightarrow \) (iv) \( \Rightarrow \) (i). It suffices by @prp-equivalence-cycle: a cycle of four works as the cycle of three does, since every condition reaches every other along the arrows.

*(i) \( \Rightarrow \) (ii).* If \( n = 2k + 1 \), then \( n + 1 = 2(k + 1) \).

*(ii) \( \Rightarrow \) (iii).* If \( n + 1 = 2j \), then \( n - 1 = 2(j - 1) \), so \( n^2 - 1 = (n - 1)(n + 1) = 4j(j - 1) \). By the fact quoted, \( j(j - 1) = 2m \) for an integer \( m \), so \( n^2 - 1 = 8m \).

*(iii) \( \Rightarrow \) (iv).* If \( n^2 - 1 = 8m \), then \( n^2 = 2(4m) + 1 \), which is odd.

*(iv) \( \Rightarrow \) (i).* This is @thm-odd-iff-square-odd, read from right to left.

(Exercise B3 of Section 1.6 met the fact (i) \( \Rightarrow \) (iii) by another route.)

For the second question: any two implications joining the two pairs, one in each direction, for instance (ii) \( \Rightarrow \) (iii) and (iv) \( \Rightarrow \) (i), the two arrows above that cross between the pairs. With them every condition reaches every other.

**Marking scheme.** (10 points)
- 1: a cycle through all four conditions, citing @prp-equivalence-cycle or arguing that it suffices.
- 8: 2 for each of the four arrows.
- 1: the completion question.

Fatal errors (0 for the step): a "cycle" that omits a condition; (iii) \( \Rightarrow \) (iv) or (iv) \( \Rightarrow \) (i) argued by examples.
:::

::: {#exr-biconditional-and-definitions-b7}
[B7: Derive or break]

For each claim, derive it with the rules of Chapter 1 and Sections 2.1–2.4, or break it by statements about a real number \( x \) that make its counterexample set true.

::: {.enumerate options="label=(\alph*)"}
1. \( P \leftrightarrow Q \vdash (P \vee R) \leftrightarrow (Q \vee R) \).
2. \( (P \vee R) \leftrightarrow (Q \vee R) \vdash P \leftrightarrow Q \).
3. \( P \leftrightarrow (Q \wedge R) \vdash P \to Q \).
4. \( P \leftrightarrow (Q \wedge R) \vdash Q \to P \).
5. \( P \leftrightarrow Q, \ Q \leftrightarrow \neg R \vdash \neg(P \wedge R) \).
6. \( P \leftrightarrow Q \vdash \neg(P \wedge \neg Q) \).
7. \( \neg(P \wedge \neg Q) \vdash P \leftrightarrow Q \).
8. \( P \leftrightarrow Q, \ P \vee Q \vdash P \wedge Q \).
:::
:::

::: {.solution}
(a) Derive. Two boxes for the iff, and a case split inside each.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {P \vee R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \bie{1,3}
  \have {5} {Q \vee R} \oi{4}
  \close
  \open
  \hypo {6} {R}
  \have {7} {Q \vee R} \oi{6}
  \close
  \have {8} {Q \vee R} \oe{2,3-5,6-7}
  \close
  \open
  \hypo {9} {Q \vee R}
  \open
  \hypo {10} {Q}
  \have {11} {P} \bie{1,10}
  \have {12} {P \vee R} \oi{11}
  \close
  \open
  \hypo {13} {R}
  \have {14} {P \vee R} \oi{13}
  \close
  \have {15} {P \vee R} \oe{9,10-12,13-14}
  \close
  \have {16} {(P \vee R) \leftrightarrow (Q \vee R)} \bi{2-8,9-15}
\end{nd}$
\end{center}
```

(b) Break. Take \( P \): "\( x > 0 \)", \( Q \): "\( x > 5 \)", \( R \): "\( x > -1 \)". At \( x = 1 \), \( P \vee R \) and \( Q \vee R \) are both true, so the premise is true; \( P \) is true and \( Q \) false, so \( P \leftrightarrow Q \) is false. The counterexample set (@def-counterexample-set) \( (P \vee R) \leftrightarrow (Q \vee R) \), \( \neg(P \leftrightarrow Q) \) is true at \( x = 1 \).

(c) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow (Q \wedge R)}
  \open
  \hypo {2} {P}
  \have {3} {Q \wedge R} \bie{1,2}
  \have {4} {Q} \ae{3}
  \close
  \have {5} {P \to Q} \ii{2-4}
\end{nd}$
\end{center}
```

(d) Break. Take \( P \): "\( x > 5 \)", \( Q \): "\( x > 0 \)", \( R \): "\( x > 3 \)". At \( x = 1 \), \( Q \wedge R \) and \( P \) are both false, so the premise is true, while \( Q \to P \) is false, since \( Q \) is true and \( P \) false. The counterexample set is true at \( x = 1 \).

(e) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \hypo {2} {Q \leftrightarrow \neg R}
  \open
  \hypo {3} {P \wedge R}
  \have {4} {P} \ae{3}
  \have {5} {Q} \bie{1,4}
  \have {6} {\neg R} \bie{2,5}
  \have {7} {R} \ae{3}
  \have {8} {\bot} \ne{7,6}
  \close
  \have {9} {\neg(P \wedge R)} \ni{3-8}
\end{nd}$
\end{center}
```

(f) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {P \wedge \neg Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \bie{1,3}
  \have {5} {\neg Q} \ae{2}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg(P \wedge \neg Q)} \ni{2-6}
\end{nd}$
\end{center}
```

(g) Break. Take \( P \): "\( x > 5 \)", \( Q \): "\( x > 0 \)". At \( x = 1 \), \( P \wedge \neg Q \) is false, since \( P \) is, so the premise is true; \( P \) is false and \( Q \) true, so \( P \leftrightarrow Q \) is false. The counterexample set is true at \( x = 1 \).

(h) Derive. Split on the second premise; in each case \( \rulename{{\leftrightarrow}E} \) supplies the other letter.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \hypo {2} {P \vee Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \bie{1,3}
  \have {5} {P \wedge Q} \ai{3,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {P} \bie{1,6}
  \have {8} {P \wedge Q} \ai{7,6}
  \close
  \have {9} {P \wedge Q} \oe{2,3-5,6-8}
\end{nd}$
\end{center}
```

(b), (d) and (g) are the converses of (a), (c) and (f), and each breaks. (a) is the \( \vee \)-twin of @exr-biconditional-and-definitions-b4, with a case split inside each box.

**Marking scheme.** (16 points) For each claim: 1 for the verdict; 1 for a derivation every line of which checks, or for a choice of statements and one value of \( x \) at which every member of the counterexample set is true. Fatal errors (0 for the claim): a "break" at which a premise fails; RAA in a derivation; a box of \( \rulename{{\leftrightarrow}I} \) citing its sibling.
:::

### C. Going deeper

::: {#exr-biconditional-and-definitions-c1}
[C1: Divisibility by six]

For integers \( d \) and \( n \), write \( d \mid n \) if \( n = dk \) for some integer \( k \). Let \( n \) be an integer. Prove that the following three conditions are equivalent, by a single cycle of three implications.

::: {.enumerate options="label=(\roman*)"}
1. \( 6 \mid n \);
2. \( 2 \mid n \) and \( 3 \mid n \);
3. \( 6 \mid n^2 \).
:::

You may use @thm-square-even-implies-even and part (a) of @exr-negation-and-contradiction-b3.
:::

::: {.solution}
[Hint 1]

Choose the order of the cycle so that each arrow is short. The two results you may use both pass from a square to the number itself.
:::

::: {.solution}
[Hint 2]

Try (i) \( \Rightarrow \) (iii) \( \Rightarrow \) (ii) \( \Rightarrow \) (i). The last arrow is the one that needs an idea: the two halves of (ii) must be used together, not one at a time.
:::

::: {.solution}
We prove (i) \( \Rightarrow \) (iii) \( \Rightarrow \) (ii) \( \Rightarrow \) (i), which suffices by @prp-equivalence-cycle.

*(i) \( \Rightarrow \) (iii).* Suppose \( n = 6k \). Then \( n^2 = 36k^2 = 6(6k^2) \), so \( 6 \mid n^2 \).

*(iii) \( \Rightarrow \) (ii).* Suppose \( n^2 = 6j \). Then \( n^2 = 2(3j) \) is even, so \( n \) is even by @thm-square-even-implies-even, that is, \( 2 \mid n \). Also \( n^2 = 3(2j) \), so \( 3 \mid n^2 \), and by part (a) of @exr-negation-and-contradiction-b3, \( 3 \mid n \). Hence \( 2 \mid n \) and \( 3 \mid n \) \( [\rulename{\wedge I}] \).

*(ii) \( \Rightarrow \) (i).* Suppose \( 2 \mid n \) and \( 3 \mid n \), and write \( n = 3b \) with \( b \) an integer. The integer \( b \) is odd or even. If \( b \) were odd, then \( n = 3b \) would be odd: writing \( b = 2c + 1 \) gives \( 3b = 6c + 3 = 2(3c + 1) + 1 \). But \( n \) is even, and no integer is both, so this case cannot occur \( [\rulename{\neg E}, \rulename{\bot E}] \). Hence \( b \) is even, say \( b = 2c \), and \( n = 6c \), so \( 6 \mid n \).

**Marking scheme.** (10 points)
- 1: names a cycle through all three conditions and cites @prp-equivalence-cycle (or proves the needed implications explicitly).
- 2: (i) \( \Rightarrow \) (iii) by computation.
- 3: (iii) \( \Rightarrow \) (ii), citing @thm-square-even-implies-even for the factor \( 2 \) and part (a) of @exr-negation-and-contradiction-b3 for the factor \( 3 \).
- 4: (ii) \( \Rightarrow \) (i), combining the two factors correctly (ruling out \( b \) odd, or \( n = 3n - 2n \), or otherwise).

Fatal errors (0 for the step): a "cycle" that omits a condition; using "\( 2 \mid n \) and \( 3 \mid n \) gives \( 6 \mid n \)" without proof; using "\( 6 \mid n^2 \) implies \( 6 \mid n \)" as known.
Any other cycle through the three conditions earns full marks if each of its arrows is proved: 1 point for the cycle and its citation, and 3 points for each of its three arrows.
:::

::: {#exr-biconditional-and-definitions-c2}
[C2: Dropping a hypothesis, and repairing the statement]

::: {.enumerate options="label=(\alph*)"}
1. Suppose only \( y \ge 0 \) is assumed in @thm-squares-order, and \( x \) is an arbitrary real number. The remark after it says that \( (\Leftarrow) \) survives. Which steps of its proof use \( y \ge 0 \), and why is \( x \ge 0 \) never needed? Refute \( (\Rightarrow) \) with a new pair.
2. Prove that for **all** real numbers \( x \) and \( y \), \( \abs{x} \le \abs{y} \) if and only if \( x^2 \le y^2 \).
:::

*Hint: for (b), apply @thm-squares-order to the right pair of numbers.*
:::

::: {.solution}
(a) The proof of \( (\Leftarrow) \) uses \( y \ge 0 \) twice: for \( x > 0 \) from \( x > y \), and for \( y^2 \le xy \). Its other multiplication is by the derived \( x > 0 \), so \( x \ge 0 \) is never used. For \( (\Rightarrow) \), take \( x = -3 \), \( y = 1 \): \( x \le y \) and \( y \ge 0 \), but \( x^2 = 9 > 1 = y^2 \).

(b) Let \( x \) and \( y \) be real numbers. Then \( \abs{x} \ge 0 \) and \( \abs{y} \ge 0 \), so @thm-squares-order applies to the pair \( \abs{x} \), \( \abs{y} \) and gives \( \abs{x} \le \abs{y} \) if and only if \( \abs{x}^2 \le \abs{y}^2 \). Finally \( \abs{x}^2 = x^2 \), since \( \abs{x} \) is \( x \) or \( -x \) and \( (-x)^2 = x^2 \), and likewise \( \abs{y}^2 = y^2 \). This proves that \( \abs{x} \le \abs{y} \) if and only if \( x^2 \le y^2 \).
:::

<!-- dependency ledger
prp-provable-equivalence-basics (proof): copying a derivation into a new place (inside extra boxes, numbers shifted) keeps every citation available | inline (the "observation" in the proof), from def-derivation's scope rule and (D3)
prp-provable-equivalence-basics (proof): a one-line derivation consisting of a premise is a derivation | exm-derivations (cited in the fold before the proposition); def-derivation
def-provable-equivalence (claim): (warning) the form "from P conclude P and Q" breaks at P: "2 > 1", Q: "1 > 2" | arithmetic; a break by a choice of statements (def-counterexample-set), no soundness claim
def-provable-equivalence (claim): (fold "Edge cases") not-not-P |- P holds once F1.2 §05 adds its rule | F1.2 §05 (prp-double-negation, a later section of this chapter); nothing here depends on it
exm-iff-negations (claim): the converse is derivable with the rule of F1.2 §05 | F1.2 §05 (a later section of this chapter); nothing depends on it
lem-not-iff-own-negation (claim): the instance "x > 0 iff x <= 0" is false for every real x, x <= 0 being not(x > 0) | the order convention of F1.2 §01 (convention box); checked by verify/ch02/lem-not-iff-own-negation.py
thm-odd-iff-square-odd (proof): (E1)-(E3); n = 2k gives n^2 = 2(2k^2) | school facts stated in F1.2 §01 (thm-square-even-implies-even); computation inline
thm-squares-order (proof): multiplying an inequality by a non-negative (positive) number; x <= y or y < x; transitivity of <= and < | school algebra, taken as known; AN1.1 (promised)
thm-squares-order (claim): (aftermath) existence of square roots of non-negative reals | school fact, taken as known; AN1.1 (promised, in the Looking-ahead box); nothing depends on it
thm-squares-order (solution): (the quick check after this theorem) a product of reals is zero only if a factor is zero | school algebra, taken as known
exm-strictly-increasing-both-ways (example): 3 > 0; multiplying/adding inequalities; the quantifier "for all x, y" used informally | school algebra; quantifier steps as ordinary reasoning (the note in this chapter's index)
exm-strictly-increasing-both-ways (claim): (warning) 6 | n implies n even (n = 6k = 2(3k)); 4 is even and 6 does not divide 4; (quick check) x = -3 has x^2 = 9 > 4 and x < 2 | arithmetic; checked by verify/ch02/exm-strictly-increasing-both-ways.py
exm-unit-interval-tfae (example): x <= 0 or x > 0; x^2 >= 0; dividing an inequality by x > 0 | school algebra, taken as known
def-rules-biconditional (claim): (fold "The same slip in calculus") differentiable at a implies continuous at a; |h|/h = 1 for h > 0 and -1 for h < 0 | AN1.7 (promised; the fold names no volume); the corner computation inline; nothing depends on it
exm-biconditional-and-definitions-instances (example): the Not-allowed WRONG/RIGHT pair: at x = 4, x > 5 implies x > 3 is true and (x > 5 iff x > 3) is false | arithmetic; checked by verify/ch02/exm-biconditional-and-definitions-instances.py
exr-biconditional-and-definitions-a1 (solution): 10 = 2*5; (-2)^2 = 4 > 1 | arithmetic
exr-biconditional-and-definitions-a2 (solution): (c) x^2 = 4 exactly at x = 2 and x = -2; (d) 12 = 3 * 4 | arithmetic; checked by verify/ch02/exr-biconditional-and-definitions-a2.py
exr-biconditional-and-definitions-b3 (solution): a < b exactly when b <= a fails | stated in the item
exr-biconditional-and-definitions-b5 (solution): a product of two real numbers is negative exactly when the factors are non-zero and of opposite signs; the triples (5, 2, 3), (2, 5, 100), (2, 5, 3); (v) read through the order convention | school algebra (sign rule), taken as known; AN1.1 (promised); the order convention of F1.2 §01; checked by verify/ch02/exr-biconditional-and-definitions-b5.py
exr-biconditional-and-definitions-b6 (solution): k(k - 1) is even for every integer k; n + 1 = 2j gives n^2 - 1 = 4j(j - 1) | stated in the item; computation inline; thm-odd-iff-square-odd (cited); checked by verify/ch02/exr-biconditional-and-definitions-b6.py
exr-biconditional-and-definitions-b7 (solution): the three breaks at x = 1 | arithmetic; checked by verify/ch02/exr-biconditional-and-definitions-b7.py (verdicts and breaks)
exr-biconditional-and-definitions-c1 (solution): every integer is odd or even, not both | (E1), (E2) of F1.2 §01
exr-biconditional-and-definitions-c2 (solution): |x| >= 0; |x|^2 = x^2 | school algebra; the second shown inline
-->
