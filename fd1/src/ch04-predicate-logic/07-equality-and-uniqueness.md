# Equality and Unique Existence

Sections 4.3 to 4.6 gave the four quantifier rules, and with them every logical symbol of the language of Section 4.2 (the connectives, \( \bot \), the quantifiers, and equality) has rules, except one. So far the equals sign has been treated like a predicate symbol: \( a = b \) was an atomic formula like \( P(a) \), and no rule looked inside it. Yet almost every calculation in mathematics is a chain of equations, and every use of "the" (the limit, the supremum, the inverse) quietly asserts that something is unique. This section adds the two rules for equality, \( \rulename{{=}I} \) and \( \rulename{{=}E} \), which say together that *equals may be replaced by equals*. Its first application is the phrase "there is exactly one", which is an existential statement together with an equation. The section ends by completing the table of rules, phrases, and Lean tactics that Chapter 1 began.

## What the rules so far cannot do with an equation

Here is the first line of a calculation any reader has written:

> Since \( a = b \) and \( a + a = 2a \), we have \( b + b = 2b \).

Nothing could be simpler, and nothing in Sections 4.3–4.6 derives it. The line \( a = b \) is an atomic formula, and so far the rules have treated \( = \) exactly as they treat a two-place predicate symbol written between its terms, like the \( R \) in front of \( R(a, b) \). From the premises \( R(a, b) \) and \( P(a) \) no rule gives \( P(b) \): a relation between \( a \) and \( b \) says nothing, by itself, about the properties of either. The quantifier rules do not help either, since neither premise begins with a quantifier. As far as the rules of Chapters 1–2 and Sections 4.3–4.6 are concerned, \( a = b \) could mean "\( a \) is less than \( b \)" or "\( a \) and \( b \) are coprime", and under those readings the general pattern behind the step, from \( R(a, b) \) and \( P(a) \) to \( P(b) \), fails: reading \( R(a, b) \) as \( a < b \) and \( P(x) \) as \( x < 1 \) over \( \nZ \), with \( a = 0 \) and \( b = 5 \), both premises are true and \( P(b) \) is false.

What makes the step correct is what \( = \) means: \( a \) and \( b \) are names of **the same object**. Any statement true of the object is true of it whichever name is used. Two things follow, and they are the two rules of this section.

1. Every term names the same object as itself. Nothing needs to be assumed to write \( t = t \).
2. If \( t_1 \) and \( t_2 \) name the same object, then a statement about \( t_1 \) may be rewritten as the same statement about \( t_2 \).

The first rule is unusual: it cites no earlier line at all. Chapter 1 anticipated this when it defined rules (Section 1.2): the definition of a rule schema (@def-rule-schema) was worded so that a rule of Chapter 4 could have no given lines at all. This is that rule.

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
4. **Free for \( x \).** Neither term may have a variable captured by a quantifier of \( \varphi \), the condition of @def-free-for that the rules of Sections 4.3 and 4.5 also carry. The nonexample below shows what goes wrong without it.

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

Line 3 breaks the side condition of @def-rules-equality. What the argument meant to say needs a different name for the bound variable: \( \exists z\, (z < a) \), which is the same sentence up to renaming (Section 4.2), becomes \( \exists z\, (z < y) \), which is true when \( y \) names \( 0 \).

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

*Finding it.* The goal is \( \forall x \), so the search method of Section 2.6, with the step of Section 4.4, opens a flagged box for \( x_0 \); the new goal \( \forall y\, (\dots) \) opens a second flagged box, for \( y_0 \). The goal \( x_0 = y_0 \to (P(x_0) \to P(y_0)) \) is an implication, so a box opens with \( x_0 = y_0 \), and the new goal \( P(x_0) \to P(y_0) \) opens another, with \( P(x_0) \). Now the goal is \( P(y_0) \), the resources are \( x_0 = y_0 \) and \( P(x_0) \), and one \( \rulename{{=}E} \) with \( \varphi = P(x) \) finishes. Every line but one was written by a goal-directed step.

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

The two \( \rulename{\forall I} \) lines cite the flagged boxes as \( \lines{1}{5} \) and \( \lines{1}{6} \): each flagged box immediately contains another box, so its range starts at that box's first line (the convention of Section 4.4). At line 6 the name \( y_0 \) appears in no premise (there are none), in no open assumption (the boxes on lines 1 and 2 have closed), and not in the conclusion; at line 7 the same holds for \( x_0 \). The derivation has 7 lines.

The claim is one of the classical "axioms of equality", often taken as a starting point in place of \( \rulename{{=}E} \). Here it is a consequence. Conversely, with the claim as a premise, \( \rulename{\forall E} \) twice and \( \rulename{{\to}E} \) twice would do the work of \( \rulename{{=}E} \) for the formula \( P(x) \); the rule does it for every formula at once.

## Calculations are chains of substitutions

A calculation in a proof looks like this:

\[
a + b = 2 \cdot b + b = 2 \cdot 3 + 3 = 9,
\]

written under the premises \( a = 2 \cdot b \) and \( b = 3 \). The chain is a single statement to the eye, but logically it is several equations, each obtained from the last. Here is the derivation it abbreviates, with one line of arithmetic, justified "arith" as in Section 4.3.

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

A **mixed chain**, such as \( a^2 + 1 = 10 \le 10 + b^2 \) with \( a = 3 \), is not made of \( \rulename{{=}E} \) alone. Its \( = \) links are \( \rulename{{=}E} \) steps as above, and a \( \le \) link needs a fact about \( \le \): here that \( b^2 \ge 0 \), so that adding \( b^2 \) does not decrease a number. The \( = \) link before it then carries over by one more \( \rulename{{=}E} \), with \( \varphi = (z \le 10 + b^2) \) and the equation \( a^2 + 1 = 10 \) turned round by symmetry (@prp-equality-symmetric-transitive (a)); transitivity of \( \le \) is needed only where two \( \le \) links meet, as in \( x \le y \le z \). Those are facts about order, not about equality. Chapter 11 derives them from the axioms of an ordered field; until then they enter derivations as "arith" lines, one per link.

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

The first link is the fact \( y + 0 = y \) for every \( y \), applied at \( y = b \) (an instance by \( \rulename{\forall E} \)) and read from right to left: the chain needs \( b = b + 0 \), which is the instance \( b + 0 = b \) turned round by symmetry. The second link rewrites the \( 0 \) by the premise \( a + c = 0 \), again turned round, since the chain needs \( 0 \) to become \( a + c \). The third and fourth are instances of associativity and commutativity. The fifth rewrites \( a + b \) by the premise \( a + b = 0 \) in the direction written. The last is the instance \( 0 + c = c \). So the claim says that a number has **at most one** additive inverse; the facts it uses are the field axioms, which Chapter 11 states as axioms and which here are school algebra.

## Unique existence

Mathematics says "**the** limit of the sequence", "**the** supremum of \( A \)", "**the** additive inverse of \( a \)". Each "the" makes two claims. There is such an object, and there is only one, so that the name picks it out. The second claim is the one that is easy to forget, and the one the claim above was about.

*"There is exactly one \( x \) with \( \varphi \)": there is one, and any other is it.*

::: {#def-unique-existence}
[Unique Existence]

Let \( \varphi \) be a formula, \( x \) a variable, and \( y \) a variable **other than \( x \) that does not appear in \( \varphi \)** (Section 4.2). Then
\[
\exists! x\, \varphi \quad \text{abbreviates} \quad \exists x\, \bigl( \varphi \wedge \forall y\, (\varphi[y/x] \to y = x) \bigr).
\]
We read \( \exists! x\, \varphi \) as "there is **exactly one** \( x \) such that \( \varphi \)", or "there is a **unique** \( x \) with \( \varphi \)".
:::

In words: there is an \( x \) that satisfies \( \varphi \), and every \( y \) that satisfies \( \varphi \) (that is, satisfies \( \varphi \) with \( y \) in place of \( x \)) is equal to that \( x \). The first conjunct is existence. The second is uniqueness, and it is a statement about the \( x \) already found: any other candidate coincides with it. Like the bounded quantifiers of @def-bounded-quantifier, \( \exists! \) is not a new symbol of the language but shorthand, and every rule applies to the formula it abbreviates.

**Well-definedness.** The abbreviation seems to depend on the choice of \( y \). It does not, up to renaming a bound variable (Section 4.2). The argument rests on one fact about substitution, used again below: *if \( y \) does not appear in \( \varphi \), then replacing \( x \) by \( y \) and then \( y \) by a term \( t \) is the same as replacing \( x \) by \( t \)*, that is, \( (\varphi[y/x])[t/y] \) is \( \varphi[t/x] \). This is a structural induction on \( \varphi \) of the kind in Section 4.2. In a term, the \( y \)'s of \( s[y/x] \) are exactly the former \( x \)'s, so \( (s[y/x])[t/y] = s[t/x] \); atomic formulas, \( \bot \) and the connectives follow clause by clause. For \( \forall x\, \psi \), both sides are \( \forall x\, \psi \), since substitution for \( x \) stops at \( \forall x \) and \( y \) does not appear in \( \psi \) (the second fact of Section 4.2). For \( \forall z\, \psi \) with \( z \) not \( x \), also \( z \) is not \( y \), because \( y \) does not appear in \( \varphi \); so both substitutions pass under the quantifier and the induction hypothesis applies, and \( \exists \) is the same. Now let \( y \) and \( y' \) be two admissible choices. If they are the same variable there is nothing to show. Otherwise \( y' \) does not appear in \( \varphi[y/x] \to y = x \), since it is neither \( x \) nor \( y \) and does not appear in \( \varphi \); so the bound \( y \) of \( \forall y\, (\varphi[y/x] \to y = x) \) may be renamed \( y' \), which gives \( \forall y'\, \bigl( (\varphi[y/x])[y'/y] \to y' = x \bigr) \). By the fact with \( t = y' \), this is \( \forall y'\, (\varphi[y'/x] \to y' = x) \), the formula written with \( y' \).

**Why \( y \) must not appear in \( \varphi \).** The condition keeps the new quantifier \( \forall y \) from capturing anything of \( \varphi \)'s own. Take \( \varphi = (x \le y) \), in which \( y \) is free, and read over \( \nN \) with \( y \) naming \( 0 \). "There is exactly one natural number \( x \) with \( x \le 0 \)" is true: \( x = 0 \). The formula written with the forbidden bound variable \( y \) is
\[
\exists x\, \bigl( x \le y \wedge \forall y\, (y \le y \to y = x) \bigr),
\]
because \( (x \le y)[y/x] \) is \( y \le y \). Its second conjunct says that **every** natural number equals \( x \), which is false. The free \( y \) of \( \varphi \), which was to name \( 0 \), has been captured by \( \forall y \). With an admissible variable, say \( z \), the formula is \( \exists x\, \bigl( x \le y \wedge \forall z\, (z \le y \to z = x) \bigr) \), which is true.

**Examples.** Simplest first; each is read over the domain named, with the informal truth of Section 4.1.

1. Over \( \nR \), \( \exists! x\, (x + 2 = 5) \) is true. *Existence:* \( 3 + 2 = 5 \). *Uniqueness:* if \( y + 2 = 5 \), then subtracting \( 2 \) gives \( y = 3 \), so \( y \) is the \( x \) already found.
2. Over \( \nN \), \( \exists! x\, (x \cdot x = 4) \) is true. *Existence:* \( 2 \cdot 2 = 4 \). *Uniqueness:* for a natural number \( y \), if \( y \le 1 \) then \( y \cdot y \le 1 \), and if \( y \ge 3 \) then \( y \cdot y \ge 9 \); so \( y \cdot y = 4 \) forces \( y = 2 \).
3. Over \( \nR \), \( \exists! x\, \forall y\, (x + y = y) \) is true: \( 0 \) is the **unique** additive identity. *Existence:* \( 0 + y = y \) for every \( y \). *Uniqueness:* suppose \( z + y = y \) for every \( y \). Apply this to the one instance \( y = 0 \) (by \( \rulename{\forall E} \)): \( z + 0 = 0 \). Since also \( z + 0 = z \), symmetry and transitivity give \( z = 0 \). The whole uniqueness proof is the choice of the instance \( y = 0 \).
4. **Degenerate.** For any constant \( c \), \( \exists! x\, (x = c) \) holds in every domain, and it is derivable from no premises (the derivation follows). By contrast, \( \exists! x\, (x = x) \) says that the domain has exactly one element, which is false in \( \nN \), \( \nZ \) and \( \nR \): existence holds and uniqueness fails.

**Nonexample by minimal change.** Keep example 2 and change the domain to \( \nZ \). Existence still holds, with the same witness \( 2 \). Uniqueness fails: \( y = -2 \) also satisfies \( y \cdot y = 4 \), and \( -2 \ne 2 \). So over \( \nZ \), \( \exists! x\, (x \cdot x = 4) \) is false, and the failing clause is exactly the second conjunct.

The derivation of \( \exists! x\, (x = c) \), with the abbreviation written out, shows that \( \exists! \) needs no rules of its own:

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {c = c} \eqi{}
  \open[y_0]
  \open
  \hypo {2} {y_0 = c}
  \close
  \have {3} {y_0 = c \to y_0 = c} \ii{2-2}
  \close
  \have {4} {\forall y\, (y = c \to y = c)} \Ai{2-3}
  \have {5} {c = c \wedge \forall y\, (y = c \to y = c)} \ai{1,4}
  \have {6} {\exists x\, (x = c \wedge \forall y\, (y = c \to y = x))} \Ei{5}
\end{nd}$
\end{center}
```

Line 3 closes a box whose only line is its assumption: the box shows \( y_0 = c \to y_0 = c \), as \( P \to P \) is shown in Chapter 1. Line 6 is \( \rulename{\exists I} \) with the witness \( c \), and it reads line 5 as \( \psi[c/x] \) for \( \psi = \bigl( x = c \wedge \forall y\, (y = c \to y = x) \bigr) \), which marks with \( x \) the first \( c \) and the last one, and keeps the other two. The choice of which occurrences to mark is the one discussed with @def-rule-existential-introduction.

::: {.warning}
**Uniqueness is not existence.** A uniqueness argument ("suppose \( y \) also satisfies \( \varphi \); then \( y = x \)") proves nothing about whether anything satisfies \( \varphi \). Over \( \nR \), every two solutions of \( x^2 = -1 \) are equal, vacuously, because there are none; yet no real number is "the" square root of \( -1 \). Conversely, an existence proof does not give uniqueness: \( x^2 = 1 \) has the solution \( 1 \), and "the solution" would be wrong, since \( -1 \) is another. Before writing "the", check both halves.
:::

## How uniqueness is used and proved

A proof of "exactly one" rarely follows the shape of @def-unique-existence, which ties the uniqueness clause to the witness just found. It proves two separate statements: there is at least one, and there is at most one. The second is "any two objects with the property are equal", and it makes no mention of a witness. The next result says that the two shapes say the same thing.

::: {#prp-unique-existence-use}
[Two Halves of Unique Existence]

Let \( \varphi \) be a formula, \( x \) a variable, and \( y \) a variable other than \( x \) that does not appear in \( \varphi \). Then
\[
\exists! x\, \varphi \;\dashv\vdash\; \exists x\, \varphi \wedge \forall x\, \forall y\, \bigl( \varphi \wedge \varphi[y/x] \to x = y \bigr).
\]
:::

The right-hand side is "existence and at most one". Its second conjunct is what a mathematician proves under the heading "uniqueness": take two objects \( x \) and \( y \) with the property, and show \( x = y \).

::: {.idea}
Both directions are searches in the style of Section 2.6 with the quantifier steps. For \( \vdash \), the premise is an \( \exists \), so open its \( \rulename{\exists E} \) box first, with a witness \( x_0 \): inside it, \( \varphi[x_0/x] \) gives existence at once by \( \rulename{\exists I} \), and "at most one" is a \( \forall\forall \) goal, which opens two flagged boxes \( u_0 \), \( v_0 \). Two objects \( u_0 \), \( v_0 \) with the property are each equal to the witness \( x_0 \), by the uniqueness clause, and so equal to each other: the witness is the "third point" that links them. For \( \dashv \), open the \( \rulename{\exists E} \) box on \( \exists x\, \varphi \) with a witness \( x_0 \); the goal inside is \( \exists! x\, \varphi \), whose witness will be \( x_0 \) again, and the uniqueness clause for \( x_0 \) comes from "at most one" applied to the pair \( x_0 \), \( y_0 \).
:::

::: {.proof}
Choose four distinct variables \( x_0 \), \( u_0 \), \( v_0 \), \( y_0 \) that do not appear in \( \varphi \), and none of which is \( x \) or \( y \). Three facts about substitution are used throughout. First, since \( y \) does not appear in \( \varphi \), \( (\varphi[y/x])[t/y] \) is \( \varphi[t/x] \) for every term \( t \), the fact proved for the well-definedness of @def-unique-existence. Second, \( \varphi[y/x] \) has no free \( x \) (every free \( x \) became \( y \)), so it is unchanged by a substitution for \( x \). Third, for a term \( t \) that does not contain \( y \), \( \varphi[t/x] \) contains no \( y \), so it is unchanged by a substitution for \( y \).

\( (\vdash) \) The following is a derivation with premise \( \exists! x\, \varphi \), written out.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, (\varphi \wedge \forall y\, (\varphi[y/x] \to y = x))}
  \open[x_0]
  \hypo {2} {\varphi[x_0/x] \wedge \forall y\, (\varphi[y/x] \to y = x_0)}
  \have {3} {\varphi[x_0/x]} \ae{2}
  \have {4} {\forall y\, (\varphi[y/x] \to y = x_0)} \ae{2}
  \have {5} {\exists x\, \varphi} \Ei{3}
  \open[u_0]
  \open[v_0]
  \open
  \hypo {6} {\varphi[u_0/x] \wedge \varphi[v_0/x]}
  \have {7} {\varphi[u_0/x]} \ae{6}
  \have {8} {\varphi[v_0/x]} \ae{6}
  \have {9} {\varphi[u_0/x] \to u_0 = x_0} \Ae{4}
  \have {10} {u_0 = x_0} \ie{9,7}
  \have {11} {\varphi[v_0/x] \to v_0 = x_0} \Ae{4}
  \have {12} {v_0 = x_0} \ie{11,8}
  \have {13} {v_0 = v_0} \eqi{}
  \have {14} {x_0 = v_0} \eqe{12,13}
  \have {15} {u_0 = v_0} \eqe{14,10}
  \close
  \have {16} {\varphi[u_0/x] \wedge \varphi[v_0/x] \to u_0 = v_0} \ii{6-15}
  \close
  \have {17} {\forall y\, (\varphi[u_0/x] \wedge \varphi[y/x] \to u_0 = y)} \Ai{6-16}
  \close
  \have {18} {\forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)} \Ai{6-17}
  \have {19} {\exists x\, \varphi \wedge \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)} \ai{5,18}
  \close
  \have {20} {\exists x\, \varphi \wedge \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)} \Ee{1,2-19}
\end{nd}$
\end{center}
```

Lines 9 and 11 are \( \rulename{\forall E} \) on line 4 at \( u_0 \) and at \( v_0 \), by the first substitution fact; each term is a variable not bound in \( \varphi[y/x] \to y = x_0 \), so it is free for \( y \) there. Lines 13 and 14 are the symmetry of @prp-equality-symmetric-transitive (a), written out; line 15 is \( \rulename{{=}E} \) with the equation \( x_0 = v_0 \) and \( \psi = (u_0 = z) \), which turns line 10 into \( u_0 = v_0 \). Line 17 is \( \rulename{\forall I} \) with the flag \( v_0 \): line 16 is its instance at \( v_0 \) (by the third and first substitution facts), and \( v_0 \) appears in no premise, in no assumption still open at line 17 (only line 2 is, and \( v_0 \) is not in it), and not in line 17. Line 18 is \( \rulename{\forall I} \) with the flag \( u_0 \) in the same way; its instance at \( u_0 \) is line 17, by the second substitution fact. Finally, line 20 closes the \( \rulename{\exists E} \) box: its last line 19 does not contain \( x_0 \), and \( x_0 \) is in neither line 1 nor any open assumption.

\( (\dashv) \) The following is a derivation with the right-hand side as premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, \varphi \wedge \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)}
  \have {2} {\exists x\, \varphi} \ae{1}
  \have {3} {\forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)} \ae{1}
  \open[x_0]
  \hypo {4} {\varphi[x_0/x]}
  \open[y_0]
  \open
  \hypo {5} {\varphi[y_0/x]}
  \have {6} {\forall y\, (\varphi[x_0/x] \wedge \varphi[y/x] \to x_0 = y)} \Ae{3}
  \have {7} {\varphi[x_0/x] \wedge \varphi[y_0/x] \to x_0 = y_0} \Ae{6}
  \have {8} {\varphi[x_0/x] \wedge \varphi[y_0/x]} \ai{4,5}
  \have {9} {x_0 = y_0} \ie{7,8}
  \have {10} {x_0 = x_0} \eqi{}
  \have {11} {y_0 = x_0} \eqe{9,10}
  \close
  \have {12} {\varphi[y_0/x] \to y_0 = x_0} \ii{5-11}
  \close
  \have {13} {\forall y\, (\varphi[y/x] \to y = x_0)} \Ai{5-12}
  \have {14} {\varphi[x_0/x] \wedge \forall y\, (\varphi[y/x] \to y = x_0)} \ai{4,13}
  \have {15} {\exists x\, (\varphi \wedge \forall y\, (\varphi[y/x] \to y = x))} \Ei{14}
  \close
  \have {16} {\exists x\, (\varphi \wedge \forall y\, (\varphi[y/x] \to y = x))} \Ee{2,4-15}
\end{nd}$
\end{center}
```

Line 6 is \( \rulename{\forall E} \) at \( x_0 \) on line 3, by the second substitution fact, and line 7 is \( \rulename{\forall E} \) at \( y_0 \) on line 6, by the third and first. Lines 10 and 11 are symmetry, written out. Line 13 is \( \rulename{\forall I} \) with the flag \( y_0 \): line 12 is its instance at \( y_0 \), by the first substitution fact; at line 13 the open assumptions are line 4, which does not contain \( y_0 \), the premise does not contain it either, and neither does line 13. Line 15 is \( \rulename{\exists I} \) with the witness \( x_0 \), which is free for \( x \) since it does not appear in \( \varphi \); line 14 is its instance at \( x_0 \), by the second substitution fact. Line 16 closes the \( \rulename{\exists E} \) box: line 15 does not contain \( x_0 \), and \( x_0 \) is in neither line 2 nor the premise, which is the only assumption open outside the box. This proves both directions.
:::

In practice this is how "there is exactly one" is proved: an existence proof, then a separate "suppose \( x \) and \( y \) both satisfy \( \varphi \); then \( x = y \)". And it is how it is used: from \( \exists! x\, \varphi \) we may take a witness, and we may identify any two objects with the property. The claim about additive inverses above was the "at most one" half; existence of an inverse is a field axiom.

**One more instance: "the maximum".** A **maximum** of a set \( A \) of reals is an element \( m \in A \) with \( a \le m \) for every \( a \in A \). If \( m \) and \( m' \) are both maxima, then \( m' \le m \) (apply the property of \( m \) to the element \( m' \in A \)) and \( m \le m' \) (apply the property of \( m' \) to \( m \in A \)), so \( m = m' \) by the order fact that \( a \le b \) and \( b \le a \) give \( a = b \). That is "at most one"; a set may have no maximum at all, such as \( (0, 1) \), so existence is a separate question. Only when both halves are known may we write "the maximum of \( A \)".

## The search method: one more step

Each of Sections 4.3 to 4.6 added a step to the search method of Section 2.6. Equality adds one.

- **An equation.** When an equation \( t_1 = t_2 \) is available and the goal differs from an available line only in some occurrences of \( t_1 \) and \( t_2 \), look for the \( \varphi \) that makes one \( \rulename{{=}E} \) turn the line into the goal: mark with \( x \) exactly the places where they differ. If the equation points the wrong way, turn it round first (sym). If no available line will do, make one with \( \rulename{{=}I} \), as the proof of @prp-equality-symmetric-transitive did.

Section 4.8 collects all the steps into one method.

## The rule, phrase and Lean table, completed {#rule-phrase-lean-table}

Chapter 1 began a table that pairs each rule with the sentence that performs it in a written proof and, for readers who use a proof assistant, with the Lean code that does the same (Sections 1.3–1.7), and Chapter 2 added the rows for negation, the biconditional, and the classical rules (Sections 2.1–2.5). Sections 4.3–4.6 added a row for each quantifier rule, and this section adds the two rows for equality. Here is the whole table for the calculus of Part 0. Nothing later depends on the last column, and Chapter 5 turns the middle column into a full dictionary of proof phrases.

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

Of the derived rules of Chapter 2, \( \rulename{MT} \), \( \rulename{CP} \) and \( \rulename{DS} \) have their rows in Section 2.3, and \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \) in Section 2.5; all the derived sequents are collected in Section 2.6. With the two equality rows, every rule of the calculus has its phrase.

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

::: {#exr-equality-and-uniqueness-b2}
[B2: A unique square root of zero]

Over \( \nR \), write \( \exists! x\, (x \cdot x = 0) \) without \( \exists! \), and prove it: existence, then uniqueness in the form "suppose \( y \) also satisfies …".

*Hint: a product of two nonzero reals is nonzero.*
:::

::: {.solution}
Written out, the statement is \( \exists x\, \bigl( x \cdot x = 0 \wedge \forall y\, (y \cdot y = 0 \to y = x) \bigr) \). We take the witness \( x = 0 \) and prove the two conjuncts.

*Existence.* \( 0 \cdot 0 = 0 \).

*Uniqueness.* Let \( y \) be a real number, and suppose \( y \cdot y = 0 \). If \( y \ne 0 \), then \( y \cdot y \) is a product of two nonzero reals and so is nonzero, which contradicts \( y \cdot y = 0 \). Hence \( y = 0 \), which is the witness. Since \( y \) was arbitrary, every \( y \) with \( y \cdot y = 0 \) equals \( 0 \).

So \( 0 \) witnesses the existential, and \( \exists! x\, (x \cdot x = 0) \) holds. The rules behind the words: "we take the witness \( x = 0 \)" is \( \rulename{\exists I} \), postponed to the end as usual; "let \( y \) be a real number" is a flagged box for \( \rulename{\forall I} \); "suppose \( y \cdot y = 0 \)" is a \( \rulename{{\to}I} \) box; "if \( y \ne 0 \) … contradicts" is an \( \rulename{RAA} \) box on \( y \ne 0 \). (That box gives \( y = 0 \) directly; \( \rulename{\neg I} \) would give only \( \neg(y \ne 0) \). Since for reals \( y = 0 \) or \( y \ne 0 \) is also a school fact, a proof by cases would do as well.)
:::

::: {#exr-equality-and-uniqueness-b3}
[B3: Exactly one fixed point]

A **fixed point** of a function \( f \colon \nR \to \nR \) is a real \( x \) with \( f(x) = x \).

::: {.enumerate options="label=(\alph*)"}
1. Formalize "\( f \) has exactly one fixed point" over \( \nR \), first with \( \exists! \) and then without it.
2. Write a formula without \( \exists! \) that says "\( f \) does **not** have exactly one fixed point", in the form "there is none, or there are two different ones".
3. Decide the statement of (a) for \( f(x) = x \cdot x \), for \( f(x) = x + 1 \) and for \( f(x) = 2 \cdot x \), and check your answer against the formula of (b).
:::
:::

::: {.solution}
*(a)* With \( \exists! \): \( \exists! x\, (f(x) = x) \). Written out, with \( y \) as the new variable: \( \exists x\, \bigl( f(x) = x \wedge \forall y\, (f(y) = y \to y = x) \bigr) \).

*(b)* \( \neg\exists x\, (f(x) = x) \vee \exists x\, \exists y\, \bigl( f(x) = x \wedge f(y) = y \wedge x \ne y \bigr) \). Read informally over \( \nR \): either no real number is fixed, or two different ones are. That is exactly the failure of "exactly one". If no \( x \) is fixed, the first disjunct holds. If some \( x \) is fixed but the uniqueness clause fails for it, then some \( y \) is fixed and differs from \( x \). Conversely, either disjunct rules out a unique fixed point: with none there is no witness, and two different fixed points \( x \ne y \) would both have to equal any proposed witness \( w \), giving \( x = y \). (Section 4.9 derives such negations mechanically, one quantifier at a time.)

*(c)* For \( f(x) = x \cdot x \): \( x \cdot x = x \) holds for \( x = 0 \) and for \( x = 1 \), so there are two different fixed points; (a) is false, and the second disjunct of (b) is true with \( x = 0 \), \( y = 1 \). For \( f(x) = x + 1 \): \( x + 1 = x \) has no solution, so (a) is false and the first disjunct of (b) is true. For \( f(x) = 2 \cdot x \): \( 2x = x \) gives \( x = 0 \), and \( 0 \) is fixed; so (a) is true with the witness \( 0 \), and both disjuncts of (b) are false.
:::

### C. Going deeper

::: {#exr-equality-and-uniqueness-c1}
[C1: Two unique quantifiers do not commute]

Show that \( \exists! x\, \exists! y\, R(x, y) \) and \( \exists! y\, \exists! x\, R(x, y) \) can have different truth values, by giving a finite domain \( D \) and a two-place relation \( R \) on it for which the first is true and the second false. Check both, reading \( \exists! \) informally.

*Hint: first say in words what each sentence claims about the rows and columns of a table of \( R \).*
:::

::: {.solution}
**What any answer must satisfy.** Call \( x \) *single* if exactly one \( y \) has \( R(x, y) \), and call \( y \) *co-single* if exactly one \( x \) has \( R(x, y) \). The first sentence says that **exactly one** element is single. The second says that exactly one element is co-single. So an answer needs exactly one single element and a number of co-single elements other than one: none, or two or more.

**An example.** Take \( D = \{0, 1, 2\} \) and \( R = \{(1, 2), (2, 0), (2, 1)\} \).

- Single elements: \( 0 \) has no partner, \( 1 \) has exactly one (\( 2 \)), and \( 2 \) has two (\( 0 \) and \( 1 \)). So \( 1 \) is the only single element, and \( \exists! x\, \exists! y\, R(x, y) \) is true, with the witness \( 1 \).
- Co-single elements: \( y = 0 \) is reached only from \( x = 2 \); \( y = 1 \) only from \( x = 2 \); \( y = 2 \) only from \( x = 1 \). All three are co-single, so there is not exactly one, and \( \exists! y\, \exists! x\, R(x, y) \) is false.

No example exists on one or two elements (there are only \( 2 + 16 = 18 \) relations on such domains). On one element, \( 0 \) is single and co-single exactly when \( R(0, 0) \) holds, so the two sentences agree. On two elements, suppose exactly one element is single; after relabeling, call it \( 0 \), and let \( c \) be its only partner. Then \( 1 \) is not single, so it has no partners or two. If it has none, column \( c \) has one entry and the other column has none. If it has two, column \( c \) has two entries and the other column has one. Either way exactly one element is co-single. Exchanging the roles of rows and columns gives the converse, so the two sentences have the same truth value. Three elements is therefore the smallest possible domain.

The moral: \( \exists! \) is not a quantifier that commutes with its own kind, as two \( \exists \)'s do. "Exactly one" hides a \( \forall \) (the uniqueness clause), and the order of a \( \forall \) and an \( \exists \) matters.
:::

::: {#exr-equality-and-uniqueness-c2}
[C2: "At most one", two ways]

Let \( P \) be a one-place predicate symbol. Derive both directions of
\[
\forall x\, \forall y\, \bigl( P(x) \wedge P(y) \to x = y \bigr) \;\dashv\vdash\; \neg\exists x\, \exists y\, \bigl( (P(x) \wedge P(y)) \wedge x \ne y \bigr),
\]
and say which of your two derivations uses \( \rulename{RAA} \), and at which line.
:::

::: {.solution}
[Hint 1]

The right-hand side is a negation: for \( \vdash \), open a \( \rulename{\neg I} \) box, and inside it two \( \rulename{\exists E} \) boxes. For \( \dashv \), the goal is \( \forall\forall \), then an implication, then an equation.
:::

::: {.solution}
[Hint 2]

In the \( \dashv \) direction, open flagged boxes for \( x_0 \) and \( y_0 \) and a \( \rulename{{\to}I} \) box on \( P(x_0) \wedge P(y_0) \). The goal is now the atomic formula \( x_0 = y_0 \). Which resources can give it?
:::

::: {.solution}
\( (\vdash) \) The goal is a negation, so a \( \rulename{\neg I} \) box opens on \( \exists x\, \exists y\, (\dots) \); inside, the premise-directed step opens an \( \rulename{\exists E} \) box for each \( \exists \), with the goal \( \bot \) as each box's last line. The premise, instantiated at the two witnesses, gives \( x_0 = y_0 \), which clashes with \( x_0 \ne y_0 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (P(x) \wedge P(y) \to x = y)}
  \open
  \hypo {2} {\exists x\, \exists y\, ((P(x) \wedge P(y)) \wedge x \neq y)}
  \open[x_0]
  \hypo {3} {\exists y\, ((P(x_0) \wedge P(y)) \wedge x_0 \neq y)}
  \open[y_0]
  \hypo {4} {(P(x_0) \wedge P(y_0)) \wedge x_0 \neq y_0}
  \have {5} {P(x_0) \wedge P(y_0)} \ae{4}
  \have {6} {x_0 \neq y_0} \ae{4}
  \have {7} {\forall y\, (P(x_0) \wedge P(y) \to x_0 = y)} \Ae{1}
  \have {8} {P(x_0) \wedge P(y_0) \to x_0 = y_0} \Ae{7}
  \have {9} {x_0 = y_0} \ie{8,5}
  \have {10} {\bot} \ne{9,6}
  \close
  \have {11} {\bot} \Ee{3,4-10}
  \close
  \have {12} {\bot} \Ee{2,3-11}
  \close
  \have {13} {\neg \exists x\, \exists y\, ((P(x) \wedge P(y)) \wedge x \neq y)} \ni{2-12}
\end{nd}$
\end{center}
```

The brackets in the statement are written out because the default groups a longer conjunction to the right (Section 3.4); with the grouping \( (P(x_0) \wedge P(y_0)) \wedge x_0 \ne y_0 \) on line 4, \( \rulename{\wedge E} \) takes out its two halves on lines 5 and 6. At line 11, \( y_0 \) is not in \( \bot \), not in line 3, not in the premise, and not in the assumptions still open (lines 2 and 3). At line 12 the same holds for \( x_0 \), with line 2 the only open assumption.

\( (\dashv) \) The goal-directed steps open flagged boxes for \( x_0 \) and \( y_0 \) and a \( \rulename{{\to}I} \) box on \( P(x_0) \wedge P(y_0) \), leaving the goal \( x_0 = y_0 \). No resource gives an equation, so the search is stuck, and step 5 of the method applies: an \( \rulename{RAA} \) box on \( x_0 \ne y_0 \). Inside, \( \rulename{\wedge I} \) and two \( \rulename{\exists I} \) steps rebuild the formula that the premise denies.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \exists x\, \exists y\, ((P(x) \wedge P(y)) \wedge x \neq y)}
  \open[x_0]
  \open[y_0]
  \open
  \hypo {2} {P(x_0) \wedge P(y_0)}
  \open
  \hypo {3} {x_0 \neq y_0}
  \have {4} {(P(x_0) \wedge P(y_0)) \wedge x_0 \neq y_0} \ai{2,3}
  \have {5} {\exists y\, ((P(x_0) \wedge P(y)) \wedge x_0 \neq y)} \Ei{4}
  \have {6} {\exists x\, \exists y\, ((P(x) \wedge P(y)) \wedge x \neq y)} \Ei{5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {x_0 = y_0} \raa{3-7}
  \close
  \have {9} {P(x_0) \wedge P(y_0) \to x_0 = y_0} \ii{2-8}
  \close
  \have {10} {\forall y\, (P(x_0) \wedge P(y) \to x_0 = y)} \Ai{2-9}
  \close
  \have {11} {\forall x\, \forall y\, (P(x) \wedge P(y) \to x = y)} \Ai{2-10}
\end{nd}$
\end{center}
```

**The \( \dashv \) derivation uses \( \rulename{RAA} \), at line 8**: the box opens with \( x_0 \ne y_0 \), that is \( \neg(x_0 = y_0) \), and closes with \( x_0 = y_0 \). Closing it by \( \rulename{\neg I} \) instead would give \( \neg\neg(x_0 = y_0) \), and no rule of Chapter 1 or Sections 2.1–2.4 removes the double negation. (With the derived rule \( \rulename{\neg\neg E} \) of Section 2.5, that \( \rulename{\neg I} \) box followed by \( \rulename{\neg\neg E} \) is an equally good derivation; its classical step is the \( \rulename{\neg\neg E} \) line, which hides an \( \rulename{RAA} \).) The \( \vdash \) derivation uses no classical rule.

**Marking scheme.** (10 points)
- 2: \( \vdash \): opens a \( \rulename{\neg I} \) box on the existential, with the goal \( \bot \).
- 2: \( \vdash \): two \( \rulename{\exists E} \) boxes with **fresh** witnesses, each ending in \( \bot \), and the premise instantiated at those witnesses.
- 2: \( \dashv \): two flagged boxes and a \( \rulename{{\to}I} \) box, in the order read off the goal.
- 2: \( \dashv \): an \( \rulename{RAA} \) box on \( x_0 \ne y_0 \), with the clash obtained by \( \rulename{\wedge I} \) and two \( \rulename{\exists I} \) steps.
- 2: names the \( \dashv \) direction as the one using \( \rulename{RAA} \), and the line.
- A \( \rulename{\neg I} \) box on \( x_0 \ne y_0 \) followed by \( \rulename{\neg\neg E} \), or an \( \rulename{LEM} \) split on \( x_0 = y_0 \) whose second case reaches \( \bot \) the same way (then \( \rulename{\bot E} \)), earns the 2 points of the \( \rulename{RAA} \)-box line; for the naming line, the reader names the \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \) line as the classical step, a derived rule whose derivation uses \( \rulename{RAA} \) (Section 2.5).
Fatal errors (0 for the step): an \( \rulename{\exists E} \) box closing on a line that contains its witness; a \( \rulename{\forall I} \) over a name in an open assumption; \( \rulename{\neg I} \) claimed to give \( x_0 = y_0 \).
:::

<!-- dependency ledger
def-rules-equality (claim): the eight readings of a + a = 2 * a: each of three occurrences marked or not | inline (2^3 = 8)
def-rules-equality (claim): over Z with R read as < and P(x) as x < 1, a = 0, b = 5, the premises R(a, b), P(a) are true and P(b) is false | informal truth over a domain, Section 4.1 (reading only; no derivability claim rests on it)
def-rules-equality (claim): over Z with a and y naming 0, "some integer is less than 0" is true and "some integer is less than itself" is false | informal truth over a domain, Section 4.1 (reading only; no derivability claim rests on it)
def-rules-equality (claim): exists z (z < a) is the same sentence as exists y (y < a) up to renaming | Section 4.2 (renaming bound variables)
prp-equality-symmetric-transitive (proof): (x = s)[s/x] is s = s and (x = s)[t/x] is t = s for x not in s, t | def-substitution (cited)
prp-equality-symmetric-transitive (proof): (s = x)[t/x] is s = t and (s = x)[u/x] is s = u for x not in s | def-substitution (cited)
prp-equality-symmetric-transitive (claim): symmetry and transitivity may be used as one line with terms in place of s, t, u | def-derived-rule (cited), extended in the text to terms; the derivations use nothing about s, t, u but that they are terms
def-rules-equality (example, the chain a + b = 9): 2 * 3 + 3 = 9 | arith line (school arithmetic)
def-rules-equality (example, mixed chains): b^2 >= 0, so adding b^2 does not decrease a number; the = link carries over by =E | school algebra; ch11 (prose pointer); def-rules-equality and prp-equality-symmetric-transitive (cited)
prp-equality-symmetric-transitive (example, additive inverse): y + 0 = y, 0 + c = c, associativity and commutativity of + | school algebra (field axioms); ch11 (prose pointer)
def-unique-existence (well-definedness): two admissible choices of y differ by renaming a bound variable | Section 4.2 (renaming bound variables)
def-unique-existence (well-definedness): (phi[y/x])[t/y] = phi[t/x] for y not in phi | def-substitution (cited); structural induction proved in the text, using the Section 4.2 claim that x not free gives phi[t/x] = phi
def-unique-existence (examples): 3 + 2 = 5 and y + 2 = 5 gives y = 3; y <= 1 gives y*y <= 1, y >= 3 gives y*y >= 9; 0 + y = y; z + 0 = z | school arithmetic
def-unique-existence (example 3): the uniqueness step z + 0 = 0 and z + 0 = z give z = 0 | prp-equality-symmetric-transitive (cited in the text by name "symmetry and transitivity")
prp-unique-existence-use (proof): (phi[y/x])[t/y] = phi[t/x] for y not in phi; phi[y/x] has no free x; phi[t/x] has no y for t without y | first fact: def-unique-existence (well-definedness paragraph, cited); def-substitution (cited); second and third read off def-substitution
prp-unique-existence-use (proof): lines 13-14 and 10-11 are symmetry written out | prp-equality-symmetric-transitive (cited)
prp-unique-existence-use (example, the maximum): a <= b and b <= a give a = b; (0, 1) has no maximum | school algebra (order); ch11 (prose pointer)
exr-equality-and-uniqueness-a1 (solution): y <= 2 gives y*y <= 4, y >= 4 gives y*y >= 16; (2+1)(2+1) = 9 | school arithmetic
exr-equality-and-uniqueness-b2 (solution): a product of two non-zero reals is non-zero; for reals y = 0 or y != 0 | school algebra (stated in the hint); ch11 (prose pointer)
exr-equality-and-uniqueness-b3 (solution): x*x = x iff x in {0, 1}; x + 1 = x has no solution; 2x = x iff x = 0 | school algebra
exr-equality-and-uniqueness-b3 (solution): not exactly one x has phi iff no x has phi or two different x have phi, read informally | informal truth over a domain, Section 4.1 (the mirror-image remark on the two quantifiers), argued both ways in the solution; Section 4.9 pointed at only, nothing depends on it
exr-equality-and-uniqueness-c1 (solution): no separating relation on 1 or 2 elements (18 relations) | case argument in the solution (rows and columns of a 2-element table)
exr-equality-and-uniqueness-c2 (solution): no rule of Ch 1 or Sections 2.1-2.4 removes a double negation | Section 2.5's discussion (thm-raa-independent, Ch 3, optional; pointed at only, nothing depends on it)
exr-equality-and-uniqueness-c2 (solution): a longer conjunction groups to the right by default, so the brackets are written | Section 3.4 (grouping convention)
exr-equality-and-uniqueness-c2 (solution): the alternative routes by the derived rules not-not-E and LEM | Section 2.5 (derived rules)
-->
