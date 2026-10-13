# Equality

Sections 5.3 to 5.6 gave the four quantifier rules, and with them every logical symbol of the language of Section 5.2 (the connectives, \( \bot \), the quantifiers, and equality) has rules, except one. So far the equals sign has been treated like a predicate symbol: \( a = b \) was an atomic formula like \( P(a) \), and no rule looked inside it. Yet almost every calculation in mathematics is a chain of equations, and every use of "the" (the limit, the supremum, the inverse) quietly asserts that something is unique. This section adds the two rules for equality, \( \rulename{{=}I} \) and \( \rulename{{=}E} \), which say together that *equals may be replaced by equals*. Section 5.8 applies them to the phrase "there is exactly one", which is an existential statement together with an equation. This section ends by completing the table of rules, phrases, and Lean tactics that Chapter 1 began.

## What the rules so far cannot do with an equation

Here is the first line of a calculation any reader has written:

> Since \( a = b \) and \( a + a = 2a \), we have \( b + b = 2b \).

Nothing could be simpler, and nothing in Sections 5.3–5.6 derives it. The line \( a = b \) is an atomic formula, and so far the rules have treated \( = \) exactly as they treat a two-place predicate symbol written between its terms, like the \( R \) in front of \( R(a, b) \). From the premises \( R(a, b) \) and \( P(a) \) no rule gives \( P(b) \): a relation between \( a \) and \( b \) says nothing, by itself, about the properties of either. The quantifier rules do not help either, since neither premise begins with a quantifier. As far as the rules of Chapters 1–2 and Sections 5.3–5.6 are concerned, \( a = b \) could mean "\( a \) is less than \( b \)" or "\( a \) and \( b \) are coprime", and under those readings the general pattern behind the step, from \( R(a, b) \) and \( P(a) \) to \( P(b) \), fails: reading \( R(a, b) \) as \( a < b \) and \( P(x) \) as \( x < 1 \) over \( \nZ \), with \( a = 0 \) and \( b = 5 \), both premises are true and \( P(b) \) is false.

What makes the step correct is what \( = \) means: \( a \) and \( b \) are names of **the same object**. Any statement true of the object is true of it whichever name is used. Two things follow, and they are the two rules of this section.

1. Every term names the same object as itself. Nothing needs to be assumed to write \( t = t \).
2. If \( t_1 \) and \( t_2 \) name the same object, then a statement about \( t_1 \) may be rewritten as the same statement about \( t_2 \).

The first rule is unusual: it cites no earlier line at all. Chapter 1 anticipated this when it defined rules (Section 1.2): the definition of a rule schema (@def-rule-schema) was worded so that a rule of Chapter 5 could have no given lines at all. This is that rule.

## The rules for equality

*Everything is equal to itself, and equals may be replaced by equals.*

::: {#def-rules-equality}
[Rules for Equality]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {k} {t = t} \eqi{}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {t_1 = t_2}
  \have {j} {\varphi[t_1/x]}
  \have {k} {\varphi[t_2/x]} \eqe{i,j}
\end{nd}$
\end{center}
```

The rule \( \rulename{{=}I} \) (**equality introduction**, or reflexivity) writes \( t = t \) for **any** term \( t \), at any line, citing nothing. The rule \( \rulename{{=}E} \) (**equality elimination**, or substitution of equals) cites an equation \( t_1 = t_2 \) on line \( i \) and a line \( j \) of the form \( \varphi[t_1/x] \), both available at line \( k \), and writes \( \varphi[t_2/x] \) on line \( k \). Here \( \varphi \) is **any** formula and \( x \) any variable, subject to one side condition: **both \( t_1 \) and \( t_2 \) are free for \( x \) in \( \varphi \)** (@def-free-for).
:::

In words: \( \rulename{{=}I} \) says that every term equals itself. \( \rulename{{=}E} \) says that when \( t_1 = t_2 \) is known, a line that says something about \( t_1 \) may be rewritten as the same thing said about \( t_2 \). The formula \( \varphi \) is the "something": a statement with a hole \( x \), which line \( j \) fills with \( t_1 \) and line \( k \) fills with \( t_2 \).

Read the definition clause by clause.

1. **\( \rulename{{=}I} \) cites nothing.** Its justification is "\( \rulename{{=}I} \)" alone. It is the first primitive rule of the book with no given lines (derived rules from results with no premises, such as \( \rulename{LEM} \) of Section 2.5, already cite nothing), and so it may stand anywhere: as the first line of a derivation with no premises, or deep inside a box.
2. **The equation is read from left to right.** The cited equation \( t_1 = t_2 \) licenses replacing \( t_1 \) by \( t_2 \), and not the other way round. From \( a = b \) and \( P(b) \), the rule does **not** give \( P(a) \), because \( P(b) \) is \( \varphi[b/x] \) for \( \varphi = P(x) \), and the equation would have to be \( b = a \). The reverse direction needs one more step, symmetry, which we derive below.
3. **Some or all occurrences.** The choice of \( \varphi \) decides which occurrences of \( t_1 \) are replaced: exactly those that \( \varphi \) marks with \( x \). Occurrences of \( t_1 \) that \( \varphi \) writes out are left alone. Choosing \( \varphi \) is the whole art of using the rule.
4. **Free for \( x \).** Neither term may have a variable captured by a quantifier of \( \varphi \), the condition of @def-free-for that the rules of Sections 5.3 and 5.5 also carry. The nonexample below shows what goes wrong without it.

**One line, many readings.** Take the equation \( a = b \) and the line \( a + a = 2 \cdot a \). The term \( a \) occurs three times in the line, and \( \varphi \) may mark any of them. Some of the choices:

| \( \varphi \) | \( \varphi[a/x] \) (the cited line) | \( \varphi[b/x] \) (the new line) |
|---|---|---|
| \( x + a = 2 \cdot a \) | \( a + a = 2 \cdot a \) | \( b + a = 2 \cdot a \) |
| \( a + x = 2 \cdot a \) | \( a + a = 2 \cdot a \) | \( a + b = 2 \cdot a \) |
| \( a + a = 2 \cdot x \) | \( a + a = 2 \cdot a \) | \( a + a = 2 \cdot b \) |
| \( x + x = 2 \cdot x \) | \( a + a = 2 \cdot a \) | \( b + b = 2 \cdot b \) |
| \( a + a = 2 \cdot a \) | \( a + a = 2 \cdot a \) | \( a + a = 2 \cdot a \) |

Each of the three occurrences is marked or not, so there are \( 2^3 = 8 \) choices in all, and each is a legal step. The fourth row is the step of the opening calculation. The last row is the **degenerate** choice: \( \varphi \) contains no \( x \), so \( \varphi[a/x] \) and \( \varphi[b/x] \) are both \( \varphi \), and the rule copies the line unchanged. It is legal and useless, and it shows that "some occurrences" includes "none". Another degenerate case: the equation may be \( t = t \) itself, and then \( \rulename{{=}E} \) again returns the cited line.

::: {.check}
From the equation \( x_0 = 3 \) and the line \( x_0 \cdot x_0 > x_0 \), which formula \( \varphi \) makes \( \rulename{{=}E} \) give \( 3 \cdot 3 > x_0 \)? Which gives \( x_0 \cdot 3 > 3 \)?
:::

::: {.solution}
For \( 3 \cdot 3 > x_0 \), take \( \varphi = (z \cdot z > x_0) \), with a variable \( z \) that appears nowhere else: \( \varphi[x_0/z] \) is the cited line and \( \varphi[3/z] \) is \( 3 \cdot 3 > x_0 \). For \( x_0 \cdot 3 > 3 \), take \( \varphi = (x_0 \cdot z > z) \). The hole has to be a variable other than \( x_0 \), since the occurrences of \( x_0 \) that stay must be written out in \( \varphi \).
:::

**A nonexample: capture.** Take the equation \( a = y \), with \( y \) a variable, and the line \( \exists y\, (y < a) \). It is tempting to "substitute \( y \) for \( a \)" and write \( \exists y\, (y < y) \). With \( \varphi = \exists y\, (y < x) \), the cited line is \( \varphi[a/x] \), and the new line would be \( \varphi[y/x] \). But \( y \) is **not** free for \( x \) in \( \varphi \): the \( x \) sits inside \( \exists y \), and the \( y \) put there would be captured. The side condition fails, and rightly. Read over \( \nZ \), with \( a \) and \( y \) both naming \( 0 \), the premises say "\( a = y \)" (true) and "some integer is less than \( 0 \)" (true), while \( \exists y\, (y < y) \) says that some integer is less than itself (false).

```{=latex}
\begin{center}
% expect-invalid
$\begin{nd}
  \hypo {1} {a = y}
  \hypo {2} {\exists y\, (y < a)}
  \have {3} {\exists y\, (y < y)} \eqe{1,2}
\end{nd}$
\end{center}
```

Line 3 breaks the side condition of @def-rules-equality. What the argument meant to say needs a different name for the bound variable: \( \exists z\, (z < a) \), which is the same sentence up to renaming (Section 5.2), becomes \( \exists z\, (z < y) \), which is true when \( y \) names \( 0 \).

*Why these two rules.* They are exactly the two facts about "same object" listed above, and nothing else about equality needs to be assumed. Symmetry (\( s = t \) gives \( t = s \)), transitivity (\( s = t \) and \( t = u \) give \( s = u \)), and "applying the same function to both sides" are all derived below. So the two rules play for \( = \) the part that the introduction and elimination rules played for each connective: one builds an equation, one uses it. The name of \( \rulename{{=}E} \) is less natural than the others, since the equation is used to rewrite some **other** line; but "elimination" fits, since the rule takes an equation apart into its use.

::: {.warning}
**A bound variable is not a place to substitute.** From \( x = 0 \) and \( \forall x\, (x = x) \), the line \( \forall x\, (0 = x) \) does **not** follow by \( \rulename{{=}E} \), although it looks like "replace the first \( x \) by \( 0 \)". The \( x \)'s of \( \forall x\, (x = x) \) are bound, and substitution replaces only free occurrences (@def-substitution). To write \( \forall x\, (x = x) \) as \( \varphi[x/z] \), either \( z \) does not occur free in \( \varphi \), and then \( \varphi[0/z] \) is the unchanged line, or \( z \) occurs free in \( \varphi \) (for instance, \( \varphi \) is \( \forall x\, (z = x) \)), and then every free \( z \) lies inside \( \forall x \), so \( x \) is not free for \( z \) in \( \varphi \) and the side condition fails. Over \( \nZ \), with \( x \) naming \( 0 \), the premises are true and \( \forall x\, (0 = x) \) is false.
:::

## Symmetry, transitivity and congruence

Everything we expect of equality now follows from the two rules. Each derivation below is short, and the only thought in each is the choice of \( \varphi \).

It turns out that the equation in \( \rulename{{=}E} \) may be read in either direction after all, at the cost of two extra lines (an \( \rulename{{=}I} \) and an \( \rulename{{=}E} \); after the abbreviation (sym) below, just one), and that equations chain:

::: {#prp-equality-symmetric-transitive}
[Equality Is Symmetric and Transitive]

For all terms \( s \), \( t \), \( u \):

::: {.enumerate options="label=(\alph*)"}
1. \( s = t \vdash t = s \);
2. \( s = t, \; t = u \vdash s = u \).
:::
:::

::: {.idea}
For (a), the goal \( t = s \) must be the last line of an \( \rulename{{=}E} \) that uses the premise \( s = t \) (it is the only equation available), so it has the form \( \varphi[t/x] \), and the cited line \( \varphi[s/x] \) must already be on a line. Try \( \varphi = (x = s) \): then \( \varphi[t/x] \) is \( t = s \), the goal, and \( \varphi[s/x] \) is \( s = s \), which \( \rulename{{=}I} \) supplies for free. For (b), rewrite the \( t \) of the first premise using the second: \( \varphi = (s = x) \).
:::

::: {.proof}
(a) With \( \varphi \coloneqq (x = s) \), for a variable \( x \) that occurs in neither \( s \) nor \( t \), the line \( s = s \) is \( \varphi[s/x] \) and the goal \( t = s \) is \( \varphi[t/x] \). Both terms are free for \( x \) in \( \varphi \), since \( \varphi \) has no quantifier. So the following is a derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {s = t}
  \have {2} {s = s} \eqi{}
  \have {3} {t = s} \eqe{1,2}
\end{nd}$
\end{center}
```

(b) With \( \varphi \coloneqq (s = x) \), for a variable \( x \) that does not occur in \( s \), the first premise \( s = t \) is \( \varphi[t/x] \) and the goal \( s = u \) is \( \varphi[u/x] \); again \( \varphi \) has no quantifier. So the following is a derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {s = t}
  \hypo {2} {t = u}
  \have {3} {s = u} \eqe{2,1}
\end{nd}$
\end{center}
```

Line 3 of (b) cites the equation \( t = u \) on line 2 as the rule's line \( i \), and \( s = t \) on line 1 as its line \( j \). This proves (a) and (b).
:::

Notice where the "reflexivity" line went in (a): the equation \( s = t \) was not rewritten at all. It was the **tool**, and the line it rewrote, \( s = s \), was manufactured for the purpose. This is the typical use of \( \rulename{{=}I} \): it supplies a line for \( \rulename{{=}E} \) to work on.

From now on, symmetry and transitivity may be used as one line, with the justifications "(sym)" and "(trans)": each abbreviates the three-line derivation above with the given terms in place of \( s \), \( t \), \( u \). This is the license of @def-derived-rule, extended from statement letters to terms. The extension is harmless for the same reason: the derivations above used nothing about \( s \), \( t \), \( u \) except that they are terms, so they can be pasted in with any terms.

The next derivation is the rule behind "apply \( f \) to both sides". Let \( f \) be a one-place function symbol, and \( a \), \( b \) constants.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {a = b}
  \have {2} {f(a) = f(a)} \eqi{}
  \have {3} {f(a) = f(b)} \eqe{1,2}
\end{nd}$
\end{center}
```

Here \( \varphi = (f(a) = f(x)) \): it keeps the first \( a \) and marks the second. With \( \varphi = (f(x) = f(x)) \) instead, the same two lines would give \( f(b) = f(b) \), which is true and useless. Nothing is special about \( f \): the same three lines give \( a^2 = b^2 \) from \( a = b \), or \( a + c = b + c \), or \( \abs{a} = \abs{b} \). Every "do the same thing to both sides of an equation" is this derivation.

The last derivation of this group has no premises at all. It says that equals share every property \( P \).

**Claim.** \( \vdash \forall x\, \forall y\, \bigl( x = y \to (P(x) \to P(y)) \bigr) \).

*Finding it.* The goal is \( \forall x \), so the search method of Section 3.1, with the step of Section 5.4, opens a flagged box for \( x_0 \); the new goal \( \forall y\, (\dots) \) opens a second flagged box, for \( y_0 \). The goal \( x_0 = y_0 \to (P(x_0) \to P(y_0)) \) is an implication, so a box opens with \( x_0 = y_0 \), and the new goal \( P(x_0) \to P(y_0) \) opens another, with \( P(x_0) \). Now the goal is \( P(y_0) \), the resources are \( x_0 = y_0 \) and \( P(x_0) \), and one \( \rulename{{=}E} \) with \( \varphi = P(x) \) finishes. Every line but one was written by a goal-directed step.

```{=latex}
\begin{center}
$\begin{nd}
  \open[x_0]
  \open[y_0]
  \open
  \hypo {1} {x_0 = y_0}
  \open
  \hypo {2} {P(x_0)}
  \have {3} {P(y_0)} \eqe{1,2}
  \close
  \have {4} {P(x_0) \to P(y_0)} \ii{2-3}
  \close
  \have {5} {x_0 = y_0 \to (P(x_0) \to P(y_0))} \ii{1-4}
  \close
  \have {6} {\forall y\, (x_0 = y \to (P(x_0) \to P(y)))} \Ai{1-5}
  \close
  \have {7} {\forall x\, \forall y\, (x = y \to (P(x) \to P(y)))} \Ai{1-6}
\end{nd}$
\end{center}
```

The two \( \rulename{\forall I} \) lines cite the flagged boxes as \( \lines{1}{5} \) and \( \lines{1}{6} \): each flagged box immediately contains another box, so its range starts at that box's first line (the convention of Section 5.4). At line 6 the name \( y_0 \) appears in no premise (there are none), in no open assumption (the boxes on lines 1 and 2 have closed), and not in the conclusion; at line 7 the same holds for \( x_0 \). The derivation has 7 lines.

The claim is one of the classical "axioms of equality", often taken as a starting point in place of \( \rulename{{=}E} \). Here it is a consequence. Conversely, with the claim as a premise, \( \rulename{\forall E} \) twice and \( \rulename{{\to}E} \) twice would do the work of \( \rulename{{=}E} \) for the formula \( P(x) \); the rule does it for every formula at once.

## Calculations are chains of substitutions

A calculation in a proof looks like this:

\[
a + b = 2 \cdot b + b = 2 \cdot 3 + 3 = 9,
\]

written under the premises \( a = 2 \cdot b \) and \( b = 3 \). The chain is a single statement to the eye, but logically it is several equations, each obtained from the last. Here is the derivation it abbreviates, with one line of arithmetic, justified "arith" as in Section 5.3.

**A chain as a derivation.** From \( b = 3 \) and \( a = 2 \cdot b \), derive \( a + b = 9 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {b = 3}
  \hypo {2} {a = 2 \cdot b}
  \have {3} {a + b = a + b} \eqi{}
  \have {4} {a + b = 2 \cdot b + b} \eqe{2,3}
  \have {5} {a + b = 2 \cdot 3 + 3} \eqe{1,4}
  \have {6} {2 \cdot 3 + 3 = 9} \by{arith}{}
  \have {7} {a + b = 9} \eqe{6,5}
\end{nd}$
\end{center}
```

The choices of \( \varphi \), with \( z \) a variable not occurring in the terms:

- line 4: \( \varphi = (a + b = z + b) \), rewriting the \( a \) on the **right** of line 3 and keeping the one on the left;
- line 5: \( \varphi = (a + b = 2 \cdot z + z) \), rewriting **both** remaining \( b \)'s on the right at once;
- line 7: \( \varphi = (a + b = z) \), rewriting the whole right-hand side by the equation of line 6.

The pattern is general. A chain \( t_1 = t_2 = \dots = t_n \) starts with \( t_1 = t_1 \) by \( \rulename{{=}I} \), keeps \( t_1 \) fixed on the left, and rewrites the right-hand side once per link, each time by \( \rulename{{=}E} \) with the equation that justifies the link. Each link is either a premise, as on lines 4 and 5, or an arithmetic fact, as on line 7. The last line is \( t_1 = t_n \). Transitivity (@prp-equality-symmetric-transitive (b)) is the same move made once; a chain makes it \( n - 1 \) times.

A **mixed chain**, such as \( a^2 + 1 = 10 \le 10 + b^2 \) with \( a = 3 \), is not made of \( \rulename{{=}E} \) alone. Its \( = \) links are \( \rulename{{=}E} \) steps as above, and a \( \le \) link needs a fact about \( \le \): here that \( b^2 \ge 0 \), so that adding \( b^2 \) does not decrease a number. The \( = \) link before it then carries over by one more \( \rulename{{=}E} \), with \( \varphi = (z \le 10 + b^2) \) and the equation \( a^2 + 1 = 10 \) turned round by symmetry (@prp-equality-symmetric-transitive (a)); transitivity of \( \le \) is needed only where two \( \le \) links meet, as in \( x \le y \le z \). Those are facts about order, not about equality. *Analysis on the Real Line*, Chapter 1 derives them from the axioms of an ordered field; until then they enter derivations as "arith" lines, one per link.

::: {.check}
Line 5 of the chain rewrites both \( b \)'s on the right of line 4 at once. Which \( \varphi \) would rewrite only the \( b \) inside \( 2 \cdot b \), and what line would it give? How would the chain then reach line 5?
:::

::: {.solution}
Take \( \varphi = (a + b = 2 \cdot z + b) \). Then line 4 is \( \varphi[b/z] \), and \( \rulename{{=}E} \) 1, 4 gives \( \varphi[3/z] \), the line \( a + b = 2 \cdot 3 + b \). One more \( \rulename{{=}E} \) with the same equation \( b = 3 \) and \( \varphi = (a + b = 2 \cdot 3 + z) \) then gives \( a + b = 2 \cdot 3 + 3 \), which is line 5. Marking both occurrences at once saves that line.
:::

## What equality sounds like in a proof

In a written proof, \( \rulename{{=}E} \) is the word "substituting", or no word at all: the chain \( a + b = 2b + b = 9 \) is read as a sequence of substitutions, and the reader supplies the \( \varphi \) of each link. "By symmetry" or "rewriting the equation as \( t = s \)" is @prp-equality-symmetric-transitive (a). "Applying \( f \) to both sides", "squaring both sides", "adding \( c \) to both sides" are the congruence derivation above. And \( \rulename{{=}I} \) is almost never written, because \( t = t \) goes without saying; it is visible only in the first line of a formal chain, and in a proof assistant, where `rfl` proves \( t = t \).

Here is a proof from school algebra, read link by link.

> **Claim.** If \( a + b = 0 \) and \( a + c = 0 \), then \( b = c \).
>
> *Proof.* \( b = b + 0 = b + (a + c) = (b + a) + c = (a + b) + c = 0 + c = c \).

The first link is the fact \( y + 0 = y \) for every \( y \), applied at \( y = b \) (an instance by \( \rulename{\forall E} \)) and read from right to left: the chain needs \( b = b + 0 \), which is the instance \( b + 0 = b \) turned round by symmetry. The second link rewrites the \( 0 \) by the premise \( a + c = 0 \), again turned round, since the chain needs \( 0 \) to become \( a + c \). The third and fourth are instances of associativity and commutativity. The fifth rewrites \( a + b \) by the premise \( a + b = 0 \) in the direction written. The last is the instance \( 0 + c = c \). So the claim says that a number has **at most one** additive inverse; the facts it uses are the field axioms, which *Analysis on the Real Line*, Chapter 1 states as axioms and which here are school algebra.

## The search method: one more step

Each of Sections 5.3 to 5.6 added a step to the search method of Section 3.1. Equality adds one.

- **An equation.** When an equation \( t_1 = t_2 \) is available and the goal differs from an available line only in some occurrences of \( t_1 \) and \( t_2 \), look for the \( \varphi \) that makes one \( \rulename{{=}E} \) turn the line into the goal: mark with \( x \) exactly the places where they differ. If the equation points the wrong way, turn it round first (sym). If no available line will do, make one with \( \rulename{{=}I} \), as the proof of @prp-equality-symmetric-transitive did.

Section 6.1 collects all the steps into one method.

## The rule, phrase and Lean table, completed {#rule-phrase-lean-table}

Chapter 1 began a table that pairs each rule with the sentence that performs it in a written proof and, for readers who use a proof assistant, with the Lean code that does the same (Sections 1.2–1.6), and Chapter 2 added the rows for negation, the biconditional, and the classical rules (Sections 2.1–2.5). Sections 5.3–5.6 added a row for each quantifier rule, and this section adds the two rows for equality. Here is the whole table for the calculus of this volume. Nothing later depends on the last column, and Chapter 8 turns the middle column into a full dictionary of proof phrases.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\wedge I} \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | "In particular, \( P \)." | `h.1` (and `h.2`) |
| \( \rulename{{\to}E} \) | "Since \( P \) implies \( Q \), and \( P \) holds, \( Q \)." | `exact h hp` |
| \( \rulename{{\to}I} \) | "Assume \( P \). … Hence \( Q \)." | `intro hp` |
| \( \rulename{R} \) | "As shown above, \( P \)." | `exact hp` |
| \( \rulename{\vee I} \) | "So \( P \) or \( Q \) holds." | `left` (or `Or.inl hp`); `right` |
| \( \rulename{\vee E} \) | "Case 1: \( P \). … so \( R \). Case 2: \( Q \). … so \( R \). In either case, \( R \)." | `Or.elim h` (or `cases h`) |
| \( \rulename{\neg E} \) | "…, which contradicts …" | `exact hn hp` (goal `False`) |
| \( \rulename{\bot E} \) | "This case cannot occur." "So there is nothing to prove." | `exfalso` |
| \( \rulename{\neg I} \) | "Suppose \( \varphi \). … This is a contradiction. Hence not \( \varphi \)." | `intro hp` (goal `False`) |
| \( \rulename{{\leftrightarrow}I} \) | "\( (\Rightarrow) \) Suppose \( P \). … so \( Q \). \( (\Leftarrow) \) Suppose \( Q \). … so \( P \)." | `constructor` |
| \( \rulename{{\leftrightarrow}E} \) | "Since \( P \) holds if and only if \( Q \) does, and \( P \) holds, so does \( Q \)." | `h.mp hp` / `h.mpr hq` |
| \( \rulename{RAA} \) | "Suppose, for a contradiction, that \( \varphi \) fails. … This is impossible. Hence \( \varphi \)." | `by_contra h` |
| \( \rulename{\forall E} \) | "In particular, for \( x = t \), …"; "applying the hypothesis to \( t \), …" | `h t` (or `specialize h t`) |
| \( \rulename{\forall I} \) | "Let \( x \) be arbitrary. … Since \( x \) was arbitrary, …" | `intro x` |
| \( \rulename{\exists I} \) | "Take \( x = t \). Then …" | `use t` (or `Exists.intro t h`) |
| \( \rulename{\exists E} \) | "Choose \( x \) with … . Then …" | `obtain` (or `Exists.elim h`) |
| \( \rulename{{=}I} \) | (usually unwritten) "\( t = t \)." | `rfl` |
| \( \rulename{{=}E} \) | "Substituting \( t_2 \) for \( t_1 \), …"; a chain \( t_1 = t_2 = \dots = t_n \) | `rw [h]`; chains `calc` |

Of the derived rules of Chapter 2, \( \rulename{MT} \), \( \rulename{CP} \) and \( \rulename{DS} \) have their rows in Section 2.3, and \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \) in Section 2.5; all the derived sequents are collected in Section 3.1. With the two equality rows, every rule of the calculus has its phrase.

## Exercises

### A. Check your understanding

::: {#exr-equality-and-uniqueness-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State \( \rulename{{=}I} \) and \( \rulename{{=}E} \) as schemas, with the side condition of \( \rulename{{=}E} \).
2. In the derivation below, name for each of lines 4, 5, 6, and 8 the rule, the cited lines, and the formula \( \varphi \) (with a variable \( z \) as its hole).
   ```{=latex}
   \begin{center}
   $\begin{nd}
     \hypo {1} {a = b + 1}
     \hypo {2} {b = 2}
     \have {3} {a \cdot a = a \cdot a} \eqi{}
     \have {4} {a \cdot a = (b + 1) \cdot a} \eqe{1,3}
     \have {5} {a \cdot a = (b + 1) \cdot (b + 1)} \eqe{1,4}
     \have {6} {a \cdot a = (2 + 1) \cdot (2 + 1)} \eqe{2,5}
     \have {7} {(2 + 1) \cdot (2 + 1) = 9} \by{arith}{}
     \have {8} {a \cdot a = 9} \eqe{7,6}
   \end{nd}$
   \end{center}
   ```
3. In the same derivation, could lines 4 and 5 be replaced by one line? With which \( \varphi \)?
4. True or false, with a reason: from the lines \( a = b \) and \( P(b) \), one application of \( \rulename{{=}E} \) gives \( P(a) \).
5. Write \( \exists! x\, (x \cdot x = 9) \) without the symbol \( \exists! \), and decide whether it is true over \( \nN \) and over \( \nZ \).
:::
:::

::: {.solution}
*(a)* \( \rulename{{=}I} \): at any line \( k \), write \( t = t \), for any term \( t \), citing nothing. \( \rulename{{=}E} \): from \( t_1 = t_2 \) on line \( i \) and \( \varphi[t_1/x] \) on line \( j \), both available at line \( k \), write \( \varphi[t_2/x] \) on line \( k \); side condition: \( t_1 \) and \( t_2 \) are both free for \( x \) in \( \varphi \).

*(b)* Line 4: \( \rulename{{=}E} \) 1, 3, with \( \varphi = (a \cdot a = z \cdot a) \), which rewrites the first \( a \) on the right. Line 5: \( \rulename{{=}E} \) 1, 4, with \( \varphi = (a \cdot a = (b + 1) \cdot z) \). Line 6: \( \rulename{{=}E} \) 2, 5, with \( \varphi = (a \cdot a = (z + 1) \cdot (z + 1)) \), which rewrites both \( b \)'s at once. Line 8: \( \rulename{{=}E} \) 7, 6, with \( \varphi = (a \cdot a = z) \). In each case the left-hand side \( a \cdot a \) is written out in \( \varphi \), so it is kept.

*(c)* Yes: \( \rulename{{=}E} \) 1, 3 with \( \varphi = (a \cdot a = z \cdot z) \) gives \( a \cdot a = (b + 1) \cdot (b + 1) \) in one step, rewriting both \( a \)'s on the right and keeping the two on the left.

*(d)* False. With the equation \( a = b \), \( \rulename{{=}E} \) passes from \( \varphi[a/x] \) to \( \varphi[b/x] \). The line \( P(b) \) is \( \varphi[b/x] \) for \( \varphi = P(x) \), so the rule would need the equation \( b = a \). One application of symmetry first (@prp-equality-symmetric-transitive (a)) gives \( b = a \), and then \( \rulename{{=}E} \) gives \( P(a) \).

*(e)* \( \exists x\, \bigl( x \cdot x = 9 \wedge \forall y\, (y \cdot y = 9 \to y = x) \bigr) \). Over \( \nN \) it is true: \( x = 3 \) works, and a natural number \( y \) with \( y \cdot y = 9 \) is \( 3 \), since \( y \le 2 \) gives \( y \cdot y \le 4 \) and \( y \ge 4 \) gives \( y \cdot y \ge 16 \). Over \( \nZ \) it is false: whatever \( x \) is proposed, \( 3 \) and \( -3 \) both satisfy \( y \cdot y = 9 \), and they cannot both equal \( x \).
:::

### B. Practice

::: {#exr-equality-and-uniqueness-b1}
[B1: The identity is unique]

A set with an operation \( \cdot \) has an **identity** \( e \) if \( e \cdot x = x \) and \( x \cdot e = x \) for every \( x \). Derive
\[
\forall x\, (e \cdot x = x \wedge x \cdot e = x), \;\; \forall x\, (e' \cdot x = x \wedge x \cdot e' = x) \;\vdash\; e = e',
\]
where \( e \) and \( e' \) are constants. Which half of "there is exactly one identity" does this prove?

*Hint: look at the one element that both premises can say something about.*
:::

::: {.solution}
The goal is an equation between \( e \) and \( e' \), and the only term that both premises can connect to both is the product \( e \cdot e' \). Instantiate the first premise at \( e' \) and the second at \( e \) (\( \rulename{\forall E} \), reading the terms off the goal):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (e \cdot x = x \wedge x \cdot e = x)}
  \hypo {2} {\forall x\, (e' \cdot x = x \wedge x \cdot e' = x)}
  \have {3} {e \cdot e' = e' \wedge e' \cdot e = e'} \Ae{1}
  \have {4} {e \cdot e' = e'} \ae{3}
  \have {5} {e' \cdot e = e \wedge e \cdot e' = e} \Ae{2}
  \have {6} {e \cdot e' = e} \ae{5}
  \have {7} {e = e'} \eqe{6,4}
\end{nd}$
\end{center}
```

Line 7 uses the equation \( e \cdot e' = e \) of line 6 to rewrite the left side of line 4, with \( \varphi = (z = e') \): \( \varphi[e \cdot e'/z] \) is line 4, and \( \varphi[e/z] \) is \( e = e' \). In prose: \( e = e \cdot e' = e' \), the first equation because \( e' \) is an identity and the second because \( e \) is.

This is the "at most one" half: any two identities are equal. It says nothing about whether an identity exists. To use it in @prp-unique-existence-use, take \( \varphi = \forall z\, (x \cdot z = z \wedge z \cdot x = z) \), and run lines 3–7 again with variables \( u_0 \), \( v_0 \) in place of \( e \), \( e' \): inside flagged boxes for \( u_0 \) and \( v_0 \) and a \( \rulename{{\to}I} \) box on \( \varphi[u_0/x] \wedge \varphi[v_0/x] \), the two premises (with \( z \) as their bound variable) come from that assumption by \( \rulename{\wedge E} \), and the same steps give \( u_0 = v_0 \). Then \( \rulename{{\to}I} \) and \( \rulename{\forall I} \) twice give \( \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y) \), the second conjunct of the proposition. With the existence of one identity as well, @prp-unique-existence-use gives "there is exactly one".
:::

### C. Going deeper

<!-- S3-PLACEHOLDER: items -->

<!-- dependency ledger
def-rules-equality (claim): the eight readings of a + a = 2 * a: each of three occurrences marked or not | inline (2^3 = 8)
def-rules-equality (claim): over Z with R read as < and P(x) as x < 1, a = 0, b = 5, the premises R(a, b), P(a) are true and P(b) is false | informal truth over a domain, F1.4 §01 (reading only; no derivability claim rests on it)
def-rules-equality (claim): over Z with a and y naming 0, "some integer is less than 0" is true and "some integer is less than itself" is false | informal truth over a domain, F1.4 §01 (reading only; no derivability claim rests on it)
def-rules-equality (claim): exists z (z < a) is the same sentence as exists y (y < a) up to renaming | F1.4 §02 (renaming bound variables)
prp-equality-symmetric-transitive (proof): (x = s)[s/x] is s = s and (x = s)[t/x] is t = s for x not in s, t | def-substitution (cited)
prp-equality-symmetric-transitive (proof): (s = x)[t/x] is s = t and (s = x)[u/x] is s = u for x not in s | def-substitution (cited)
prp-equality-symmetric-transitive (claim): symmetry and transitivity may be used as one line with terms in place of s, t, u | def-derived-rule (cited), extended in the text to terms; the derivations use nothing about s, t, u but that they are terms
def-rules-equality (example, the chain a + b = 9): 2 * 3 + 3 = 9 | arith line (school arithmetic)
def-rules-equality (example, mixed chains): b^2 >= 0, so adding b^2 does not decrease a number; the = link carries over by =E | school algebra; AN1.1 (prose pointer); def-rules-equality and prp-equality-symmetric-transitive (cited)
prp-equality-symmetric-transitive (example, additive inverse): y + 0 = y, 0 + c = c, associativity and commutativity of + | school algebra (field axioms); AN1.1 (prose pointer)
exr-equality-and-uniqueness-a1 (solution): y <= 2 gives y*y <= 4, y >= 4 gives y*y >= 16; (2+1)(2+1) = 9 | school arithmetic
-->
