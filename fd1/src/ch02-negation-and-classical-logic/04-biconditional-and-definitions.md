# Iff, Equivalence, and What a Definition Says

One connective is still without rules: "if and only if". Theorems say "\( n \) is odd if and only if \( n^2 \) is odd", and every definition, though written with a plain "if", is used as an "if and only if". Section 1.1 warned that "if" means different things in a theorem and in a definition, and promised an explanation. The one new thing here is the pair of rules for \( \leftrightarrow \); the rest of the section (provable equivalence, the layout of an "iff" proof, the convention about definitions, chains of equivalences) is what the rules are used for.

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

1. **Two boxes.** \( \rulename{{\leftrightarrow}I} \) needs two available boxes: one opened by \( \varphi \) and ending in \( \psi \), the other opened by \( \psi \) and ending in \( \varphi \), each last line a line of its own box. Each is exactly the box \( \rulename{{\to}I} \) would need for one direction. Their order does not matter, but both must be there: a single box from \( \varphi \) to \( \psi \) proves \( \varphi \to \psi \) and nothing more.
2. **Separate boxes.** The boxes are siblings, not nested, so nothing in the second may cite a line of the first (the scope rule of @def-derivation). Each direction is a proof on its own.
3. **Citation.** The justification cites both boxes as ranges, as in \( \rulename{{\leftrightarrow}I}\ \lines{2}{4}, \lines{5}{7} \).
4. **Elimination, either way.** From \( \varphi \leftrightarrow \psi \) and \( \varphi \) on available lines, \( \rulename{{\leftrightarrow}E} \) writes \( \psi \); from \( \varphi \leftrightarrow \psi \) and \( \psi \), it writes \( \varphi \). It is modus ponens in whichever direction we need, citing the biconditional first.

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

So \( \leftrightarrow \) could have been an abbreviation for \( (P \to Q) \wedge (Q \to P) \). We keep it as a connective with its own rules, so that every connective is proved by an introduction rule and used by an elimination rule.

::: {#exm-iff-negations}
[Negating both sides of an iff]

Show that \( P \leftrightarrow Q \vdash \neg P \leftrightarrow \neg Q \).
:::

::: {.solution}
*Idea.* The goal is an iff, so there are two boxes, one opened by \( \neg P \) and reaching \( \neg Q \), the other the reverse. Each box's goal is a negation, so each contains a \( \rulename{\neg I} \) box: the goal-directed move applied twice, one inside the other. Inside the inner box, \( \rulename{{\leftrightarrow}E} \) crosses from one side of the premise to the other, and the result clashes with the outer assumption. Each half is part (b) of @exm-iff-symmetric, run inside a box.

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

Line 5 cites line 2, the assumption of the outer box, still open there. The two halves are mirror images.
:::

The derivation uses only the rules of this section and of Sections 2.1–2.2. Its converse, \( \neg P \leftrightarrow \neg Q \vdash P \leftrightarrow Q \), is also derivable, with the rule of Section 2.5: in the box of \( P \) it must produce the **positive** statement \( Q \), and the natural box, on \( \neg Q \), closes to \( \neg\neg Q \), not \( Q \). That no derivation avoids the new rule is true, but we state it without proof, and nothing depends on it. Section 2.5 sets the converse as an exercise.

## Provable equivalence

@prp-iff-two-implications is a pair of sequents, one in each direction. It is not the first such pair: @prp-curry and @prp-distributivity are pairs too. When two statements can each be derived from the other, either may stand in for the other in any derivation, and the situation deserves a name.

*Two statements are provably equivalent when each can be derived from the other.*

::: {#def-provable-equivalence}
[Provable Equivalence]

Statements \( P \) and \( Q \) are **provably equivalent**, written \( P \dashv\vdash Q \), if \( P \vdash Q \) **and** \( Q \vdash P \).
:::

In words: there is a derivation with premise \( P \) and last line \( Q \), and **another** with premise \( Q \) and last line \( P \). The symbol is the turnstile of @def-derivable written twice, back to back; two derivations prove the claim.

The degenerate example is \( P \dashv\vdash P \): the one-line derivation of part (a) of @exm-derivations serves in both directions. A first real example is \( P \vee Q \dashv\vdash Q \vee P \): @exm-disjunction-first-derivations shows \( P \vee Q \vdash Q \vee P \), and the same derivation with the letters exchanged shows the converse. By the same exchange, part (a) of @exm-iff-symmetric gives \( P \leftrightarrow Q \dashv\vdash Q \leftrightarrow P \).

A minimal change gives a one-way street. @exm-double-negation-introduction derived \( P \vdash \neg\neg P \), but the converse, \( \neg\neg P \vdash P \), would have to remove two negations, and no rule met so far removes one. So we cannot claim \( P \dashv\vdash \neg\neg P \): the clause "\( Q \vdash P \)" is the one missing. (It holds once Section 2.5 adds its rule; that it cannot hold without that rule is true, and Chapter 3 proves it: @thm-raa-independent.) Likewise @prp-contrapositive derives \( \neg Q \to \neg P \) from \( P \to Q \), but not yet the reverse.

The connective \( \leftrightarrow \) and the relation \( \dashv\vdash \) are two sides of one idea; the next result makes the link exact, and shows that \( \dashv\vdash \) behaves as an equivalence should.

::: {#prp-provable-equivalence-basics}
[Provable Equivalence and the Biconditional]

For all statements \( P \), \( Q \), \( R \):

::: {.enumerate options="label=(\alph*)"}
1. \( P \dashv\vdash Q \) if and only if \( \vdash P \leftrightarrow Q \);
2. \( P \dashv\vdash P \); if \( P \dashv\vdash Q \), then \( Q \dashv\vdash P \); and if \( P \dashv\vdash Q \) and \( Q \dashv\vdash R \), then \( P \dashv\vdash R \).
:::
:::

::: {.idea}
Everything here moves whole derivations around. To prove \( \vdash P \leftrightarrow Q \), the two boxes of \( \rulename{{\leftrightarrow}I} \) are the two given derivations, with their premises turned into the boxes' assumptions. To use \( \vdash P \leftrightarrow Q \), write out its derivation and apply \( \rulename{{\leftrightarrow}E} \). For transitivity, run one derivation into the next: the last line of the first is the premise of the second.
:::

::: {.proof}
We use one observation twice. Let \( D \) be a derivation, and copy its lines, in order and with their numbers shifted, to some place in another derivation, with every line of the copy inside the same boxes as that place. Then every citation inside the copy is still available: if line \( i \) of \( D \) is available at line \( k \) of \( D \), every box of \( D \) containing line \( i \) contains line \( k \), and the boxes added around the copy contain both lines. Closed boxes cited in \( D \) are handled the same way. So each copied line is justified by the same rule as before.

\( (\Rightarrow) \) in (a). Suppose \( P \vdash Q \) and \( Q \vdash P \), by derivations \( D_1 \) and \( D_2 \). Build a derivation with no premises as follows. Open a box with the assumption \( P \) and, below it, copy \( D_1 \), turning each of its premise lines \( P \) into a repetition of the assumption by (D3) of @def-derivation. By the observation, the copy is justified, and its last line \( Q \) is a line of the box itself, since the last line of \( D_1 \) lies in none of \( D_1 \)'s boxes. Close the box. Open a second box with \( Q \), copy \( D_2 \) in the same way, and close it on \( P \). Then \( \rulename{{\leftrightarrow}I} \) on the two boxes gives \( P \leftrightarrow Q \). So \( \vdash P \leftrightarrow Q \).

\( (\Leftarrow) \) in (a). Suppose \( \vdash P \leftrightarrow Q \), by a derivation \( D \) with no premises. For \( P \vdash Q \), start with the premise \( P \), copy \( D \) below it, and write \( Q \) by \( \rulename{{\leftrightarrow}E} \) from the last line of the copy, \( P \leftrightarrow Q \), and line 1. Both cited lines lie in no box, so both are available. For \( Q \vdash P \), do the same with premise \( Q \), using the other form of \( \rulename{{\leftrightarrow}E} \). So \( P \dashv\vdash Q \).

(b) The one-line derivation consisting of the premise \( P \) shows \( P \vdash P \), in both directions, so \( P \dashv\vdash P \). Symmetry holds because @def-provable-equivalence says the same thing about \( P, Q \) as about \( Q, P \). For transitivity it is enough to show that \( P \vdash Q \) and \( Q \vdash R \) give \( P \vdash R \), since the reverse direction is the same statement with \( P \) and \( R \) exchanged. Take a derivation \( D_1 \) of \( Q \) from \( P \), and below its last line copy a derivation \( D_2 \) of \( R \) from \( Q \), turning each premise line \( Q \) of \( D_2 \) into a repetition of the last line of \( D_1 \). That line lies in no box, so it is available everywhere below it, and by the observation the rest of the copy is justified. The result has premise \( P \) and last line \( R \). This proves the proposition.
:::

Part (a) says that one derivation of \( P \leftrightarrow Q \) from no premises carries the same information as two derivations, one each way. Part (b) says that \( \dashv\vdash \) can be used like "\( = \)" in a calculation: chains of provable equivalences run either way and join end to end.

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
A sequent in one direction is not an equivalence. \( P \wedge Q \vdash P \) holds by \( \rulename{\wedge E} \), but \( P \vdash P \wedge Q \) does not: take \( P \): "\( 2 > 1 \)" and \( Q \): "\( 1 > 2 \)", and the premise is true while the conclusion is false. (A derivation never leads from true premises to a false conclusion; Chapter 3 proves this, @thm-soundness.) Before writing \( \dashv\vdash \), check that **both** derivations exist.
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

A payoff comes at once. For \( a, b \ge 0 \), apply @thm-squares-order to \( x = \sqrt{a} \) and \( y = \sqrt{b} \): \( \sqrt{a} \le \sqrt{b} \) if and only if \( a \le b \). Taking square roots preserves order, a fact used constantly in estimates. (That square roots of nonnegative numbers exist is a school fact here; Chapter 11 proves it from the least upper bound axiom.)

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

This is a convention of mathematical language, not a rule of logic. Some books write "iff" or \( :\Leftrightarrow \) in definitions; this book, like most, writes "if" and puts the term defined in **bold**, which signals that the "if" is an "iff". Here it is used three ways. The words "for all real numbers \( x \) and \( y \)" are a quantifier, whose rules come in Chapter 4; here we use them informally.

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
The convention is for **definitions only**. In a theorem, "if" means "if", one direction. A familiar theorem of calculus, proved in Chapter 17, says: if \( f \) is differentiable at \( a \), then \( f \) is continuous at \( a \). Its converse is false. The function \( f(x) = \abs{x} \) is continuous at \( 0 \), but it is not differentiable there, since its graph has a corner: the quotient \( \abs{h}/h \) is \( 1 \) for \( h > 0 \) and \( -1 \) for \( h < 0 \). Reading a theorem's "if" as "iff" means proving its converse without a proof, which is the error of Argument B in Section 1.1.
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
The goal is an iff, so there are two boxes. From \( P \), one step along the cycle reaches \( Q \). From \( Q \), the cycle reaches \( P \) the long way round, through \( R \): a backward chain of \( \rulename{{\to}E} \), as in Section 1.4. The other two equivalences need no new work, because the three premises do not change when the letters are rotated.
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

## What the rules sound like

The rows for this section's rules complete the table for the connectives; Section 2.6 collects the rules in one place. The Lean names in the last column come from the two fields of an iff, `mp` ("modus ponens", left to right) and `mpr` (right to left).

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{{\leftrightarrow}I} \) | "\( (\Rightarrow) \) Suppose \( P \). … so \( Q \). \( (\Leftarrow) \) Suppose \( Q \). … so \( P \)." | `constructor` |
| \( \rulename{{\leftrightarrow}E} \) | "Since \( P \) holds if and only if \( Q \) does, and \( P \) holds, so does \( Q \)." | `h.mp hp` / `h.mpr hq` |

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
:::

::: {.solution}
Apply @thm-squares-order with the roles of \( x \) and \( y \) exchanged, which is allowed since both are nonnegative: \( y \le x \) if and only if \( y^2 \le x^2 \). By @exm-iff-negations, with \( P \): "\( y \le x \)" and \( Q \): "\( y^2 \le x^2 \)", used as a derived rule (@def-derived-rule), we get: \( y \le x \) fails if and only if \( y^2 \le x^2 \) fails. By the fact quoted, the left side says \( x < y \) and the right side says \( x^2 < y^2 \). This proves that \( x < y \) if and only if \( x^2 < y^2 \).
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
prp-provable-equivalence-basics (proof): a one-line derivation consisting of a premise is a derivation | exm-derivations (cited in the paragraph before the proposition); def-derivation
def-provable-equivalence (claim): a derivation never leads from true premises to a false conclusion | ch03 (thm-soundness), prose pointer; the warning's example is motivation only
def-provable-equivalence (claim): not-not-P |- P does not hold without RAA | ch03 (thm-raa-independent, optional there), prose pointer; nothing depends on it
exm-iff-negations (claim): the converse needs the rule of Section 2.5 | stated without proof and marked so; nothing depends on it
thm-odd-iff-square-odd (proof): (E1)-(E3); n = 2k gives n^2 = 2(2k^2) | school facts stated in Section 2.1 (thm-square-even-implies-even); computation inline
thm-squares-order (proof): multiplying an inequality by a non-negative (positive) number; x <= y or y < x; transitivity of <= and < | school algebra, taken as known; ch11 (promised)
thm-squares-order (claim): (aftermath) existence of square roots of non-negative reals | school fact, taken as known; ch11 (promised); nothing depends on it
thm-squares-order (solution): (the quick check after this theorem) a product of reals is zero only if a factor is zero | school algebra, taken as known
exm-strictly-increasing-both-ways (example): 3 > 0; multiplying/adding inequalities; the quantifier "for all x, y" used informally | school algebra; quantifier rules in ch04 (prose pointer)
exm-unit-interval-tfae (example): x <= 0 or x > 0; x^2 >= 0; dividing an inequality by x > 0 | school algebra, taken as known
def-rules-biconditional (claim): (warning after "What a definition says") differentiable at a implies continuous at a; |h|/h = 1 for h > 0 and -1 for h < 0 | ch17 (prose pointer); the corner computation inline; nothing depends on it
exr-biconditional-and-definitions-a1 (solution): 10 = 2*5; (-2)^2 = 4 > 1 | arithmetic
exr-biconditional-and-definitions-b3 (solution): a < b exactly when b <= a fails | stated in the item
exr-biconditional-and-definitions-c1 (solution): every integer is odd or even, not both | (E1), (E2) of Section 2.1
exr-biconditional-and-definitions-c2 (solution): |x| >= 0; |x|^2 = x^2 | school algebra; the second shown inline
-->
