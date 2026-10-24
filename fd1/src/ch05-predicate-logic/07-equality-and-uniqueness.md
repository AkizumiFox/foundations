# Equality

Sections 5.3 to 5.6 gave the four quantifier rules, and with them every logical symbol of the language of Section 5.2 (the connectives, \( \bot \), the quantifiers, and equality) has rules, except one. So far the equals sign has been treated like a predicate symbol: \( a = b \) was an atomic formula like \( P(a) \), and no rule looked inside it. Yet almost every calculation in mathematics is a chain of equations, and every use of "the" (the limit, the supremum, the inverse) quietly asserts that something is unique. This section adds the two rules for equality, \( \rulename{{=}I} \) and \( \rulename{{=}E} \), which say together that *equals may be replaced by equals*. Section 5.8 applies them to the phrase "there is exactly one", which is an existential statement together with an equation. This section ends by completing the table of rules, phrases, and Lean tactics that Chapter 1 began.

## What the rules so far cannot do with an equation

Here is the first line of a calculation any reader has written:

> Since \( a = b \) and \( a + a = 2a \), we have \( b + b = 2b \).

Nothing could be simpler, and nothing in Sections 5.3–5.6 derives it: so far the rules treat \( = \) as they treat any two-place predicate symbol, and from \( R(a, b) \) and \( P(a) \) no rule gives \( P(b) \). Reading \( R(a, b) \) as \( a < b \) and \( P(x) \) as \( x < 1 \) over \( \nZ \), with \( a = 0 \) and \( b = 5 \), both premises are true and \( P(b) \) is false.

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

**Mark the holes first.** To use \( \rulename{{=}E} \) with \( t_1 = t_2 \), write down the line you have and draw a box round each occurrence of \( t_1 \) you want to replace. The boxes are the holes: \( \varphi \) is the line with a variable in each box, and the new line puts \( t_2 \) in every box. With \( a = b \):
\[
\boxed{a} + \boxed{a} = 2 \cdot \boxed{a} \ \text{ gives } \ b + b = 2 \cdot b, \qquad \boxed{a} + a = 2 \cdot a \ \text{ gives } \ b + a = 2 \cdot a .
\]
Occurrences without a box stay as they are.

Read the definition clause by clause.

1. **\( \rulename{{=}I} \) cites nothing.**
   - *Schema:* the left block above, \( t = t \), citing nothing.
   - *Reading:* every term equals itself, so the line may stand anywhere, even first in a derivation with no premises.
   - *Example:* "\( a + b = a + b \) — \( \rulename{{=}I} \)", the first line of every chain below.
2. **The equation is read from left to right.** The cited equation \( t_1 = t_2 \) licenses replacing \( t_1 \) by \( t_2 \), and not the other way round. From \( a = b \) and \( P(b) \), the rule does **not** give \( P(a) \), because \( P(b) \) is \( \varphi[b/x] \) for \( \varphi = P(x) \), and the equation would have to be \( b = a \). The reverse direction needs one more step, symmetry, which we derive below.
3. **Some or all occurrences.** The choice of \( \varphi \) decides which occurrences of \( t_1 \) are replaced: exactly those that \( \varphi \) marks with \( x \) (the boxes above). Occurrences of \( t_1 \) that \( \varphi \) writes out are left alone. Choosing \( \varphi \) is the whole art of using the rule.
4. **Free for \( x \).** Neither term may have a variable captured by a quantifier of \( \varphi \), the condition of @def-free-for that the rules of Sections 5.3 and 5.5 also carry. The nonexample below shows what goes wrong without it.

**One line, many readings.** Take the equation \( a = b \) and the line \( a + a = 2 \cdot a \). The term \( a \) occurs three times in the line, and \( \varphi \) may mark any of them. Some of the choices:

| \( \varphi \) | \( \varphi[a/x] \) (the cited line) | \( \varphi[b/x] \) (the new line) |
|---|---|---|
| \( x + a = 2 \cdot a \) | \( a + a = 2 \cdot a \) | \( b + a = 2 \cdot a \) |
| \( a + x = 2 \cdot a \) | \( a + a = 2 \cdot a \) | \( a + b = 2 \cdot a \) |
| \( a + a = 2 \cdot x \) | \( a + a = 2 \cdot a \) | \( a + a = 2 \cdot b \) |
| \( x + x = 2 \cdot x \) | \( a + a = 2 \cdot a \) | \( b + b = 2 \cdot b \) |

Each of the three occurrences is marked or not, so there are \( 2^3 = 8 \) choices in all, and each is a legal step. The fourth row is the step of the opening calculation.

::: {.second-reading title="Degenerate choices"}
One more row belongs to the table:

| \( \varphi \) | \( \varphi[a/x] \) (the cited line) | \( \varphi[b/x] \) (the new line) |
|---|---|---|
| \( a + a = 2 \cdot a \) | \( a + a = 2 \cdot a \) | \( a + a = 2 \cdot a \) |

This row is the **degenerate** choice: \( \varphi \) contains no \( x \), so \( \varphi[a/x] \) and \( \varphi[b/x] \) are both \( \varphi \), and the rule copies the line unchanged. It is legal and useless, and it shows that "some occurrences" includes "none". Another degenerate case: the equation may be \( t = t \) itself, and then \( \rulename{{=}E} \) again returns the cited line.
:::

::: {.check}
From the equation \( x_0 = 3 \) and the line \( x_0 \cdot x_0 > x_0 \), which formula \( \varphi \) makes \( \rulename{{=}E} \) give \( 3 \cdot 3 > x_0 \)? Which gives \( x_0 \cdot 3 > 3 \)?
:::

::: {.solution}
For \( 3 \cdot 3 > x_0 \), take \( \varphi = (z \cdot z > x_0) \), with a variable \( z \) that appears nowhere else: \( \varphi[x_0/z] \) is the cited line and \( \varphi[3/z] \) is \( 3 \cdot 3 > x_0 \). For \( x_0 \cdot 3 > 3 \), take \( \varphi = (x_0 \cdot z > z) \). The hole has to be a variable other than \( x_0 \), since the occurrences of \( x_0 \) that stay must be written out in \( \varphi \).
:::

::: {.check}
From \( a = b \) and the line \( a \cdot a = a + 1 \), which occurrences do you box to get \( a \cdot b = b + 1 \)?
:::

::: {.solution}
The second and the third \( a \): \( \varphi = (a \cdot z = z + 1) \), and \( \varphi[a/z] \) is the given line, \( \varphi[b/z] \) the new one.
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

*Why these two rules.* They are exactly the two facts about "same object" listed above, and nothing else about equality needs to be assumed. Symmetry (\( s = t \) gives \( t = s \)), transitivity (\( s = t \) and \( t = u \) give \( s = u \)), and "applying the same function to both sides" are all derived below. So the two rules play for \( = \) the part that the introduction and elimination rules played for each connective: one builds an equation, one uses it.

::: {.warning}
**A bound variable is not a place to substitute.** From \( x = 0 \) and \( \forall x\, (x = x) \), the line \( \forall x\, (0 = x) \) does **not** follow: the \( x \)'s of \( \forall x\, (x = x) \) are bound, and \( \rulename{{=}E} \) replaces only free occurrences. Over \( \nZ \), with \( x \) naming \( 0 \), the premises are true and \( \forall x\, (0 = x) \) is false.
:::

::: {.second-reading title="Why no choice of the hole works"}
To write \( \forall x\, (x = x) \) as \( \varphi[x/z] \), either \( z \) does not occur free in \( \varphi \), and then \( \varphi[0/z] \) is the unchanged line, or \( z \) occurs free in \( \varphi \) (for instance, \( \varphi \) is \( \forall x\, (z = x) \)), and then every free \( z \) lies inside \( \forall x \), so \( x \) is not free for \( z \) in \( \varphi \) and the side condition fails.
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

The last result of this group has no premises. It says that equals share every property, and it is called **Leibniz's Law**.

::: {#prp-leibniz-law}
[Leibniz's Law]

For every one-place predicate symbol \( P \),
\( \vdash \forall x\, \forall y\, \bigl( x = y \to (P(x) \to P(y)) \bigr) \).
:::

*In words: whatever is true of \( x \) is true of anything equal to it. The rule \( \rulename{{=}E} \) is this law for every formula at once; the seven-line derivation is in the fold below.*

::: {.second-reading title="Leibniz's Law, derived"}
::: {.proof}
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
:::

The claim is one of the classical "axioms of equality", often taken as a starting point in place of \( \rulename{{=}E} \). Here it is a consequence. Conversely, with the claim as a premise, \( \rulename{\forall E} \) twice and \( \rulename{{\to}E} \) twice would do the work of \( \rulename{{=}E} \) for the formula \( P(x) \); the rule does it for every formula at once.
:::

::: {.warning}
**Words about knowledge are not formulas.** \( \rulename{{=}E} \) rewrites formulas of the language, and "it is obvious that …", "the pupil checked that …", "it is known that …" are not among its connectives. A pupil checked that \( 7 \cdot 13 = 91 \), and indeed \( 7 \cdot 13 = 91 \). Replacing \( 7 \cdot 13 \) by \( 91 \) inside the report gives "the pupil checked that \( 91 = 91 \)", a different claim about what the pupil did. Inside a formula every free occurrence of a term may be rewritten; inside words about what someone knows or checked, none may.
:::

### Equal sets have the same elements

::: {#exm-extensionality-logical-half}
[Equal Sets Have the Same Elements]

Read the domain as consisting of sets, with \( \in \) a two-place predicate symbol written between its terms (shorthand rule 1 of Section 5.2). Show that \( \vdash \forall x\, \forall y\, \bigl( x = y \to \forall z\, (z \in x \leftrightarrow z \in y) \bigr) \).
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \open[x_0]
  \open[y_0]
  \open
  \hypo {1} {x_0 = y_0}
  \open[z_0]
  \open
  \hypo {2} {z_0 \in x_0}
  \close
  \open
  \hypo {3} {z_0 \in x_0}
  \close
  \have {4} {z_0 \in x_0 \leftrightarrow z_0 \in x_0} \bi{2-2,3-3}
  \have {5} {z_0 \in x_0 \leftrightarrow z_0 \in y_0} \eqe{1,4}
  \close
  \have {6} {\forall z\, (z \in x_0 \leftrightarrow z \in y_0)} \Ai{2-5}
  \close
  \have {7} {x_0 = y_0 \to \forall z\, (z \in x_0 \leftrightarrow z \in y_0)} \ii{1-6}
  \close
  \have {8} {\forall y\, (x_0 = y \to \forall z\, (z \in x_0 \leftrightarrow z \in y))} \Ai{1-7}
  \close
  \have {9} {\forall x\, \forall y\, (x = y \to \forall z\, (z \in x \leftrightarrow z \in y))} \Ai{1-8}
\end{nd}$
\end{center}
```

The two boxes of line 4 are one-line boxes, as \( P \to P \) is shown, and each flagged box immediately contains another box and is cited from its first line. Line 5 is \( \rulename{{=}E} \) with \( \varphi = (z_0 \in x_0 \leftrightarrow z_0 \in w) \): line 4 is \( \varphi[x_0/w] \), and the equation of line 1 refills the hole with \( y_0 \); as in the proof of symmetry, \( \rulename{{\leftrightarrow}I} \) manufactured a line for \( \rulename{{=}E} \) to rewrite.
:::

The converse, \( \forall z\, (z \in x \leftrightarrow z \in y) \to x = y \), breaks. Here is a counter-reading to it: two dots \( a \) and \( b \), with nothing an element of anything. With \( x \) naming \( a \) and \( y \) naming \( b \), both sides of \( z \in x \leftrightarrow z \in y \) are false for every \( z \), so the hypothesis is true; and \( a = b \) is false. For sets, the converse is taken as an axiom, the axiom of extensionality: a set is determined by its elements.

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

A **mixed chain**, such as \( a^2 + 1 = 10 \le 10 + b^2 \) with \( a = 3 \), is not made of \( \rulename{{=}E} \) alone. Its \( = \) links are \( \rulename{{=}E} \) steps as above, and a \( \le \) link needs a fact about \( \le \): here that \( b^2 \ge 0 \), so that adding \( b^2 \) does not decrease a number. The \( = \) link before it then carries over by one more \( \rulename{{=}E} \), with \( \varphi = (z \le 10 + b^2) \) and the equation \( a^2 + 1 = 10 \) turned round by symmetry (@prp-equality-symmetric-transitive (a)); transitivity of \( \le \) is needed only where two \( \le \) links meet, as in \( x \le y \le z \). Those are facts about order, not about equality. They enter derivations as "arith" lines, one per link.

::: {.check}
Line 5 of the chain rewrites both \( b \)'s on the right of line 4 at once. Which \( \varphi \) would rewrite only the \( b \) inside \( 2 \cdot b \), and what line would it give? How would the chain then reach line 5?
:::

::: {.solution}
Take \( \varphi = (a + b = 2 \cdot z + b) \). Then line 4 is \( \varphi[b/z] \), and \( \rulename{{=}E} \) 1, 4 gives \( \varphi[3/z] \), the line \( a + b = 2 \cdot 3 + b \). One more \( \rulename{{=}E} \) with the same equation \( b = 3 \) and \( \varphi = (a + b = 2 \cdot 3 + z) \) then gives \( a + b = 2 \cdot 3 + 3 \), which is line 5. Marking both occurrences at once saves that line.
:::

::: {.check}
Under the premise \( a = 2 \), the chain \( a + 1 = 2 + 1 = 3 \le 4 \) has three links. Which is an \( \rulename{{=}E} \) step, and which are "arith" lines?
:::

::: {.solution}
The first link is \( \rulename{{=}E} \): from \( a + 1 = a + 1 \) (\( \rulename{{=}I} \)) and \( a = 2 \), with \( \varphi = (a + 1 = z + 1) \), it writes \( a + 1 = 2 + 1 \). The links \( 2 + 1 = 3 \) and \( 3 \le 4 \) are facts of school arithmetic, written as "arith" lines; the last is about order, not equality.
:::

## What equality sounds like in a proof

In a written proof, \( \rulename{{=}E} \) is the word "substituting", or no word at all: the chain \( a + b = 2b + b = 9 \) is read as a sequence of substitutions, and the reader supplies the \( \varphi \) of each link. "By symmetry" or "rewriting the equation as \( t = s \)" is @prp-equality-symmetric-transitive (a). "Applying \( f \) to both sides", "squaring both sides", "adding \( c \) to both sides" are the congruence derivation above. And \( \rulename{{=}I} \) is almost never written, because \( t = t \) goes without saying; it is visible only in the first line of a formal chain, and in a proof assistant, where `rfl` proves \( t = t \).

Here is a proof from school algebra, read link by link.

> **Claim.** If \( a + b = 0 \) and \( a + c = 0 \), then \( b = c \).
>
> *Proof.* \( b = b + 0 = b + (a + c) = (b + a) + c = (a + b) + c = 0 + c = c \).

The first link is the fact \( y + 0 = y \) for every \( y \), applied at \( y = b \) (an instance by \( \rulename{\forall E} \)) and read from right to left: the chain needs \( b = b + 0 \), which is the instance \( b + 0 = b \) turned round by symmetry. The second link rewrites the \( 0 \) by the premise \( a + c = 0 \), again turned round, since the chain needs \( 0 \) to become \( a + c \). The third and fourth are instances of associativity and commutativity. The fifth rewrites \( a + b \) by the premise \( a + b = 0 \) in the direction written. The last is the instance \( 0 + c = c \). So the claim says that a number has **at most one** additive inverse; the facts it uses are the field axioms, here school algebra.

## The search method: one more step

Each of Sections 5.3 to 5.6 added a step to the search method of Section 3.1. Equality adds one.

- **An equation.** When an equation \( t_1 = t_2 \) is available and the goal differs from an available line only in some occurrences of \( t_1 \) and \( t_2 \), look for the \( \varphi \) that makes one \( \rulename{{=}E} \) turn the line into the goal: mark with \( x \) exactly the places where they differ. If the equation points the wrong way, turn it round first (sym). If no available line will do, make one with \( \rulename{{=}I} \), as the proof of @prp-equality-symmetric-transitive did.

In the Givens/Goal table, \( \rulename{{=}E} \) turns a Given into a new Given with some holes refilled, and \( \rulename{{=}I} \) adds \( t = t \) to the Givens at no cost.

::: {#exm-equality-and-uniqueness-instances}
[Instances of \( \rulename{{=}E} \)]

In each row the hole is \( z \); the cited line fills it with the left side of the equation, the new line with the right side.

| Equation \( t_1 = t_2 \) | \( \varphi \) | Cited line \( \varphi[t_1/z] \) | New line \( \varphi[t_2/z] \) |
|---|---|---|---|
| \( f(c) = g(c) + 1 \) | \( P(z) \wedge R(f(c), c) \) | \( P(f(c)) \wedge R(f(c), c) \) | \( P(g(c) + 1) \wedge R(f(c), c) \) |
| \( \varepsilon/2 = \delta \) | \( \abs{x - a} < z \to \abs{h(x) - h(a)} < \varepsilon \) | \( \abs{x - a} < \varepsilon/2 \to \abs{h(x) - h(a)} < \varepsilon \) | \( \abs{x - a} < \delta \to \abs{h(x) - h(a)} < \varepsilon \) |
| \( a + b = b + a \) | \( \forall y\, (z \cdot y = y \cdot (a + b)) \) | \( \forall y\, ((a + b) \cdot y = y \cdot (a + b)) \) | \( \forall y\, ((b + a) \cdot y = y \cdot (a + b)) \) |

In the first row the \( f(c) \) inside \( R(f(c), c) \) is written out in \( \varphi \) and stays; in the third the hole sits under \( \forall y \), and both terms are free for \( z \) because neither contains \( y \).

**Not an instance.** From \( 2 = 1 + 1 \) and the line \( 2^5 = 32 \), the line \( (1 + 1)^5 = 3(1 + 1) \), which treats the digit \( 2 \) of \( 32 \) as an occurrence of the term \( 2 \), is not written by \( \rulename{{=}E} \): the numeral \( 32 \) is one constant, with no occurrence of the term \( 2 \) inside it; \( \varphi = (z^5 = 32) \) gives only \( (1 + 1)^5 = 32 \).
:::

## The rule, phrase and Lean table, completed {#rule-phrase-lean-table}

Chapter 1 began a table that pairs each rule with the sentence that performs it in a written proof and, for readers who use a proof assistant, with the Lean code that does the same (Sections 1.2–1.6), and Chapter 2 added the rows for negation, the biconditional, and the classical rules (Sections 2.1–2.5). Sections 5.3–5.6 added a row for each quantifier rule, and this section adds the two rows for equality. Here is the whole table for the calculus of this volume.

| Rule | Shape | You write |
|---|---|---|
| \( \rulename{\wedge I} \) | \( \varphi \), \( \psi \) \( \Longrightarrow \) \( \varphi \wedge \psi \) | "We show \( P \), and we show \( Q \)." |
| \( \rulename{\wedge E} \) | \( \varphi \wedge \psi \) \( \Longrightarrow \) \( \varphi \) (or \( \psi \)) | "In particular, \( P \)." |
| \( \rulename{{\to}E} \) | \( \varphi \to \psi \), \( \varphi \) \( \Longrightarrow \) \( \psi \) | "Since \( P \) implies \( Q \), and \( P \) holds, \( Q \)." |
| \( \rulename{{\to}I} \) | box \( \varphi \) … \( \psi \) \( \Longrightarrow \) \( \varphi \to \psi \) | "Assume \( P \). … Hence \( Q \)." |
| \( \rulename{R} \) | \( \varphi \) (available) \( \Longrightarrow \) \( \varphi \), copied | "As shown above, \( P \)." |
| \( \rulename{\vee I} \) | \( \varphi \) \( \Longrightarrow \) \( \varphi \vee \psi \) (or \( \psi \vee \varphi \)) | "So \( P \) or \( Q \) holds." |
| \( \rulename{\vee E} \) | \( \varphi \vee \psi \), box \( \varphi \) … \( \chi \), box \( \psi \) … \( \chi \) \( \Longrightarrow \) \( \chi \) | "Case 1: \( P \). … so \( R \). Case 2: \( Q \). … so \( R \). In either case, \( R \)." |
| \( \rulename{\neg E} \) | \( \varphi \), \( \neg\varphi \) \( \Longrightarrow \) \( \bot \) | "…, which contradicts …" |
| \( \rulename{\bot E} \) | \( \bot \) \( \Longrightarrow \) any \( \varphi \) | "This case cannot occur." "So there is nothing to prove." |
| \( \rulename{\neg I} \) | box \( \varphi \) … \( \bot \) \( \Longrightarrow \) \( \neg\varphi \) | "Suppose \( \varphi \). … This is a contradiction. Hence not \( \varphi \)." |
| \( \rulename{{\leftrightarrow}I} \) | box \( \varphi \) … \( \psi \), box \( \psi \) … \( \varphi \) \( \Longrightarrow \) \( \varphi \leftrightarrow \psi \) | "\( (\Rightarrow) \) Suppose \( P \). … so \( Q \). \( (\Leftarrow) \) Suppose \( Q \). … so \( P \)." |
| \( \rulename{{\leftrightarrow}E} \) | \( \varphi \leftrightarrow \psi \), \( \varphi \) \( \Longrightarrow \) \( \psi \) (or with \( \psi \), \( \varphi \)) | "Since \( P \) holds if and only if \( Q \) does, and \( P \) holds, so does \( Q \)." |
| \( \rulename{RAA} \) | box \( \neg\varphi \) … \( \bot \) \( \Longrightarrow \) \( \varphi \) | "Suppose, for a contradiction, that \( \varphi \) fails. … This is impossible. Hence \( \varphi \)." |
| \( \rulename{\forall E} \) | \( \forall x\, \varphi \) \( \Longrightarrow \) \( \varphi[t/x] \) | "In particular, for \( x = t \), …"; "applying the hypothesis to \( t \), …" |
| \( \rulename{\forall I} \) | box \( [x_0] \) … \( \varphi[x_0/x] \) \( \Longrightarrow \) \( \forall x\, \varphi \) | "Let \( x \) be arbitrary. … Since \( x \) was arbitrary, …" |
| \( \rulename{\exists I} \) | \( \varphi[t/x] \) \( \Longrightarrow \) \( \exists x\, \varphi \) | "Take \( x = t \). Then …" |
| \( \rulename{\exists E} \) | \( \exists x\, \varphi \), box \( [x_0] \) \( \varphi[x_0/x] \) … \( \chi \) \( \Longrightarrow \) \( \chi \) | "Choose \( x \) with … . Then …" |
| \( \rulename{{=}I} \) | nothing \( \Longrightarrow \) \( t = t \) | (usually unwritten) "\( t = t \)." |
| \( \rulename{{=}E} \) | \( t_1 = t_2 \), \( \varphi[t_1/x] \) \( \Longrightarrow \) \( \varphi[t_2/x] \) | "Substituting \( t_2 \) for \( t_1 \), …"; a chain \( t_1 = t_2 = \dots = t_n \) |

::: {.remark}
[For Lean users]

∧I `constructor`; ∧E `h.1`, `h.2`; →E `exact h hp`; →I `intro hp`; R `exact hp`; ∨I `left`, `right` (or `Or.inl hp`); ∨E `Or.elim h` (or `cases h`); ¬E `exact hn hp` (goal `False`); ⊥E `exfalso`; ¬I `intro hp` (goal `False`); ↔I `constructor`; ↔E `h.mp hp`, `h.mpr hq`; RAA `by_contra h`; ∀E `h t` (or `specialize h t`); ∀I `intro x`; ∃I `use t` (or `Exists.intro t h`); ∃E `obtain` (or `Exists.elim h`); =I `rfl`; =E `rw [h]`, chains `calc`. Nothing later depends on these.
:::

Of the derived rules of Chapter 2, \( \rulename{MT} \), \( \rulename{CP} \) and \( \rulename{DS} \) have their rows in Section 2.3, and \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \) in Section 2.5; all the derived sequents are collected in Section 3.1. With the two equality rows, every rule of the calculus has its phrase.

::: {.warning}
[Not allowed: \( \rulename{{=}E} \)]

Each step breaks the clause of the reading of @def-rules-equality shown.

- "From \( c = f(b) \) and \( Q(f(b)) \), write \( Q(c) \)": the equation is read left to right and rewrites \( c \) into \( f(b) \); turn it round first, by (sym) (clause 2).
- "From \( x = 0 \) and \( \forall x\, (x \ge x) \), write \( \forall x\, (0 \ge 0) \)": only free occurrences are replaced, and both \( x \)'s of \( x \ge x \) are bound (the warning "A bound variable is not a place to substitute").
- "From \( b = z + 1 \) and \( \forall z\, (z \le b) \), write \( \forall z\, (z \le z + 1) \)": with \( \varphi = \forall z\, (z \le w) \), the \( z \) of \( z + 1 \) is captured (clause 4).
- "Rewrite a term inside 'it is obvious that …'": that is not a formula (the warning "Words about knowledge are not formulas").
:::

::: {.remark}
[Looking ahead]

Chapter 8 turns the "You write" column of this table into a full dictionary of proof phrases.
:::

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
5. True or false, with a reason: from \( a = b \) and the line \( \forall x\, (x = a \to P(x)) \), one application of \( \rulename{{=}E} \) gives \( \forall x\, (x = b \to P(x)) \).
:::
:::

::: {.solution}
*(a)* \( \rulename{{=}I} \): at any line \( k \), write \( t = t \), for any term \( t \), citing nothing. \( \rulename{{=}E} \): from \( t_1 = t_2 \) on line \( i \) and \( \varphi[t_1/x] \) on line \( j \), both available at line \( k \), write \( \varphi[t_2/x] \) on line \( k \); side condition: \( t_1 \) and \( t_2 \) are both free for \( x \) in \( \varphi \).

*(b)* Line 4: \( \rulename{{=}E} \) 1, 3, with \( \varphi = (a \cdot a = z \cdot a) \), which rewrites the first \( a \) on the right. Line 5: \( \rulename{{=}E} \) 1, 4, with \( \varphi = (a \cdot a = (b + 1) \cdot z) \). Line 6: \( \rulename{{=}E} \) 2, 5, with \( \varphi = (a \cdot a = (z + 1) \cdot (z + 1)) \), which rewrites both \( b \)'s at once. Line 8: \( \rulename{{=}E} \) 7, 6, with \( \varphi = (a \cdot a = z) \). In each case the left-hand side \( a \cdot a \) is written out in \( \varphi \), so it is kept.

*(c)* Yes: \( \rulename{{=}E} \) 1, 3 with \( \varphi = (a \cdot a = z \cdot z) \) gives \( a \cdot a = (b + 1) \cdot (b + 1) \) in one step, rewriting both \( a \)'s on the right and keeping the two on the left.

*(d)* False. With the equation \( a = b \), \( \rulename{{=}E} \) passes from \( \varphi[a/x] \) to \( \varphi[b/x] \). The line \( P(b) \) is \( \varphi[b/x] \) for \( \varphi = P(x) \), so the rule would need the equation \( b = a \). One application of symmetry first (@prp-equality-symmetric-transitive (a)) gives \( b = a \), and then \( \rulename{{=}E} \) gives \( P(a) \).

*(e)* True. Take \( \varphi = \forall x\, (x = z \to P(x)) \): the cited line is \( \varphi[a/z] \) and the new line is \( \varphi[b/z] \). The terms \( a \) and \( b \) are constants, so both are free for \( z \), although the hole lies under \( \forall x \).
:::

::: {#exr-equality-and-uniqueness-a2}
[A2: Drill]

Each part takes a line or two. The parts run from single steps, through a missing line and a justification column, to judging steps and short derivations. Letters \( a, b, c, d \) are constants.

::: {.enumerate options="label=(\alph*)"}
1. What does \( \rulename{{=}I} \) cite?
2. From \( a = b \) and \( P(a, a) \), box the holes to get \( P(a, b) \).
3. From \( c = d + 1 \) and the line \( R(c, c \cdot c) \), write the \( \rulename{{=}E} \) line that rewrites only the last \( c \).
4. From \( x_0 = 2 \) and \( x_0 + x_0 = 4 \), which \( \varphi \) gives \( 2 + x_0 = 4 \)?
5. Line 6 is \( f(b) + b = 7 \), justified "\( \rulename{{=}E} \) 2, 5", and line 2 is \( a = b \). Give two possible lines 5.
6. Justify each line: 1 \( a = b \), premise; 2 \( \forall x\, (P(x) \to x = c) \), premise; 3 \( P(a) \), premise; 4 \( P(a) \to a = c \); 5 \( a = c \); 6 \( a = a \); 7 \( b = a \); 8 \( b = c \).
7. From \( a = b \) and \( P(b) \), does one \( \rulename{{=}E} \) give \( P(a) \)?
8. From \( a = y \) and \( \exists y\, (y < a) \), is \( \exists y\, (y < y) \) a legal \( \rulename{{=}E} \) line?
9. From \( x_0 = 0 \) and the line \( \forall y\, (x_0 \le y) \), is \( \forall y\, (0 \le y) \) a legal \( \rulename{{=}E} \) line? From \( y = 0 \) and the same line, is \( \forall y\, (x_0 \le 0) \)?
10. Derive \( a = b \vdash f(b) = f(a) \).
11. Derive \( a = b, \ b = c \vdash a = c \) in one step.
12. Derive \( \forall x\, R(x, x) \vdash \forall x\, \forall y\, (x = y \to R(x, y)) \).
:::
:::

::: {.solution}
(a) Nothing.

(b) Box the second \( a \) only: \( \varphi = P(a, z) \).

(c) \( R(c, c \cdot (d + 1)) \), with \( \varphi = R(c, c \cdot z) \).

(d) \( \varphi = (z + x_0 = 4) \).

(e) Any two of \( f(a) + a = 7 \) (\( \varphi = (f(z) + z = 7) \)), \( f(b) + a = 7 \) (\( \varphi = (f(b) + z = 7) \)), \( f(a) + b = 7 \) (\( \varphi = (f(z) + b = 7) \)); and the degenerate \( f(b) + b = 7 \) itself.

(f) 4 \( \rulename{\forall E} \) 2 (at \( a \)); 5 \( \rulename{{\to}E} \) 4, 3; 6 \( \rulename{{=}I} \); 7 \( \rulename{{=}E} \) 1, 6 (\( \varphi = (z = a) \)); 8 \( \rulename{{=}E} \) 5, 7 (\( \varphi = (b = z) \)).

(g) No, clause 2: the equation rewrites \( a \) into \( b \). Turn it round first (sym), then \( \rulename{{=}E} \).

(h) No, clause 4: the \( y \) put in would be captured by \( \exists y \).

(i) The first is legal: \( \varphi = \forall y\, (z \le y) \), and \( 0 \) is free for \( z \). The second is not: the \( y \) of \( \forall y\, (x_0 \le y) \) is bound, and \( \rulename{{=}E} \) replaces only free occurrences.

(j) 2 \( f(a) = f(a) \), \( \rulename{{=}I} \); 3 \( f(b) = f(a) \), \( \rulename{{=}E} \) 1, 2, with \( \varphi = (f(z) = f(a)) \).

(k) 3 \( a = c \), \( \rulename{{=}E} \) 2, 1, with \( \varphi = (a = z) \).

(l) A flagged box \( x_0 \), inside it a flagged box \( y_0 \): 2 \( x_0 = y_0 \), assumption; 3 \( R(x_0, x_0) \), \( \rulename{\forall E} \) 1; 4 \( R(x_0, y_0) \), \( \rulename{{=}E} \) 2, 3 (\( \varphi = R(x_0, z) \)); 5 \( x_0 = y_0 \to R(x_0, y_0) \), \( \rulename{{\to}I} \) 2–4; 6 \( \forall y\, (x_0 = y \to R(x_0, y)) \), \( \rulename{\forall I} \) 2–5; 7 \( \forall x\, \forall y\, (x = y \to R(x, y)) \), \( \rulename{\forall I} \) 2–6. (A reflexive relation contains equality.)
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

This is the "at most one" half: any two identities are equal. It says nothing about whether an identity exists. Section 5.8 shows how such an argument combines with existence.
:::

::: {#exr-equality-and-uniqueness-b4}
[B2: Rewrite, and turn round]

A search for \( a = b, \ b = c, \ P(a) \vdash P(c) \wedge c = a \) has reached the stage below. *Name the move, then complete it, giving for each \( \rulename{{=}E} \) line its holes.*

```{=latex}
% schema (partial derivation: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {a = b}
  \hypo {2} {b = c}
  \hypo {3} {P(a)}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {P(c) \wedge c = a} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The move is *substitute equals, holes marked*, with an \( \rulename{{=}I} \) line to turn an equation round.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {a = b}
  \hypo {2} {b = c}
  \hypo {3} {P(a)}
  \have {4} {P(b)} \eqe{1,3}
  \have {5} {P(c)} \eqe{2,4}
  \have {6} {a = c} \eqe{2,1}
  \have {7} {a = a} \eqi{}
  \have {8} {c = a} \eqe{6,7}
  \have {9} {P(c) \wedge c = a} \ai{5,8}
\end{nd}$
\end{center}
```

Lines 4 and 5: \( \varphi = P(z) \). Line 6: \( \varphi = (a = z) \), so line 1 is \( \varphi[b/z] \) and the equation \( b = c \) refills the hole with \( c \). Line 8: \( \varphi = (z = a) \); line 7 is \( \varphi[a/z] \), and the equation \( a = c \) refills the box with \( c \). Lines 7–8 are (sym) written out; with the abbreviation of the text, line 8 is "\( c = a \) (sym) 6".
:::

::: {#exr-equality-and-uniqueness-b5}
[B3: Derive or break]

For each claim, derive it with the rules of this chapter, or break it with a counter-reading.

::: {.enumerate options="label=(\alph*)"}
1. \( f(a) = b, \ a = c \vdash f(c) = b \).
2. \( f(a) = f(b) \vdash a = b \).
3. \( \forall x\, (f(x) = x) \vdash f(f(c)) = c \).
4. \( \forall x\, \forall y\, (f(x) = f(y) \to x = y), \ f(a) = f(b) \vdash a = b \).
5. \( a \ne b, \ b \ne c \vdash a \ne c \).
6. \( a = b, \ b \ne c \vdash a \ne c \).
7. \( f(a) = a \vdash f(f(a)) = a \).
8. \( f(f(a)) = a \vdash f(a) = a \).
:::
:::

::: {.solution}
(a) Derive. One \( \rulename{{=}E} \), with \( \varphi = (f(z) = b) \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {f(a) = b}
  \hypo {2} {a = c}
  \have {3} {f(c) = b} \eqe{2,1}
\end{nd}$
\end{center}
```

(b) Break. Counter-reading: the domain \( \{0, 1\} \), \( f \) sending both to \( 0 \), \( a \) naming \( 0 \) and \( b \) naming \( 1 \). Then \( f(a) = 0 = f(b) \), and \( a = b \) is false.

(c) Derive. Instantiate at the compound term \( f(c) \) as well as at \( c \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (f(x) = x)}
  \have {2} {f(f(c)) = f(c)} \Ae{1}
  \have {3} {f(c) = c} \Ae{1}
  \have {4} {f(f(c)) = c} \eqe{3,2}
\end{nd}$
\end{center}
```

Line 4 has \( \varphi = (f(f(c)) = z) \).

(d) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (f(x) = f(y) \to x = y)}
  \hypo {2} {f(a) = f(b)}
  \have {3} {\forall y\, (f(a) = f(y) \to a = y)} \Ae{1}
  \have {4} {f(a) = f(b) \to a = b} \Ae{3}
  \have {5} {a = b} \ie{4,2}
\end{nd}$
\end{center}
```

(e) Break. Counter-reading: the domain \( \{0, 1\} \), \( a \) and \( c \) naming \( 0 \), \( b \) naming \( 1 \). Then \( a \ne b \) and \( b \ne c \) are true, and \( a \ne c \) is false: two different letters, one object.

(f) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {a = b}
  \hypo {2} {b \neq c}
  \open
  \hypo {3} {a = c}
  \have {4} {b = c} \eqe{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {a \neq c} \ni{3-5}
\end{nd}$
\end{center}
```

Line 4 has \( \varphi = (z = c) \).

(g) Derive.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {f(a) = a}
  \have {2} {f(f(a)) = f(f(a))} \eqi{}
  \have {3} {f(f(a)) = f(a)} \eqe{1,2}
  \have {4} {f(f(a)) = a} \eqe{1,3}
\end{nd}$
\end{center}
```

Line 3 has \( \varphi = (f(f(a)) = f(z)) \), and line 4 has \( \varphi = (f(f(a)) = z) \).

(h) Break. Counter-reading: the domain \( \{0, 1\} \), \( f \) exchanging \( 0 \) and \( 1 \), \( a \) naming \( 0 \). Then \( f(f(0)) = f(1) = 0 \), so the premise is true, and \( f(0) = 1 \), so \( f(a) = a \) is false.

(b) and (d) differ by the premise that \( f \) is one-to-one; (e) and (f) look alike, and \( \ne \) is not transitive, since different letters may name one object; (g) and (h) are converses. Worked example types: @prp-equality-symmetric-transitive; the chain derivation of "Calculations are chains of substitutions"; the congruence derivation.

**Marking scheme.** (10 points) 1 for each of the eight claims (a derivation with every \( \varphi \) named, or a counter-reading with the domain and every symbol's value); 2 for the closing comparison, with the point about (e) and (f) stated. Fatal errors (0 for the claim): an \( \rulename{{=}E} \) with the equation read right to left; a counter-reading in which two letters that must differ (by a premise) name one object.
:::

### C. Going deeper

::: {#exr-equality-and-uniqueness-c3}
[C1: Two different objects]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \exists x\, \exists y\, (x \ne y) \vdash \forall x\, \exists y\, (x \ne y) \), and name the line that uses a classical rule.
2. Read both formulas aloud. Derive the converse, or break it.
:::
:::

::: {.solution}
(a) Read off the goal and the premise. The premise is an existential (twice), so both \( \rulename{\exists E} \) boxes open first, with names \( x_0 \) and \( y_0 \). The goal is universal, so a flagged box \( u_0 \) opens inside them. The new goal \( \exists y\, (u_0 \ne y) \) is postponed, and no available line decides whether \( u_0 \) is \( x_0 \), so the search splits by \( \rulename{LEM} \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, \exists y\, (x \neq y)}
  \open[x_0]
  \hypo {2} {\exists y\, (x_0 \neq y)}
  \open[y_0]
  \hypo {3} {x_0 \neq y_0}
  \open[u_0]
  \have {4} {u_0 = x_0 \vee u_0 \neq x_0} \lem{}
  \open
  \hypo {5} {u_0 = x_0}
  \open
  \hypo {6} {u_0 = y_0}
  \have {7} {x_0 = y_0} \eqe{5,6}
  \have {8} {\bot} \ne{7,3}
  \close
  \have {9} {u_0 \neq y_0} \ni{6-8}
  \have {10} {\exists y\, (u_0 \neq y)} \Ei{9}
  \close
  \open
  \hypo {11} {u_0 \neq x_0}
  \have {12} {\exists y\, (u_0 \neq y)} \Ei{11}
  \close
  \have {13} {\exists y\, (u_0 \neq y)} \oe{4,5-10,11-12}
  \close
  \have {14} {\forall x\, \exists y\, (x \neq y)} \Ai{4-13}
  \close
  \have {15} {\forall x\, \exists y\, (x \neq y)} \Ee{2,3-14}
  \close
  \have {16} {\forall x\, \exists y\, (x \neq y)} \Ee{1,2-15}
\end{nd}$
\end{center}
```

Line 7 is \( \rulename{{=}E} \) with \( \varphi = (z = y_0) \): line 6 is \( \varphi[u_0/z] \), and the equation \( u_0 = x_0 \) refills the hole with \( x_0 \). The classical line is line 4, \( \rulename{LEM} \), a derived rule whose derivation uses \( \rulename{RAA} \) (Section 2.5). At line 14, \( u_0 \) appears in no premise, in neither open assumption (lines 2 and 3) and not in line 14. At lines 15 and 16 the witnesses \( y_0 \) and \( x_0 \) appear neither in the last lines, nor in the existentials, nor in the open assumptions.

(b) The premise says "there are two different objects"; the conclusion says "every object has one different from it". The converse derives: 2 \( \exists y\, (x \ne y) \), \( \rulename{\forall E} \) 1 (at \( x \)); 3 \( \exists x\, \exists y\, (x \ne y) \), \( \rulename{\exists I} \) 2 (witness \( x \)). Over a one-element domain both are false; over larger ones both are true.

**Marking scheme.** (10 points) 2: both \( \rulename{\exists E} \) boxes opened first, with different names. 2: the flagged box inside them, and the goal postponed. 3: the split on \( u_0 = x_0 \), with the first case reaching \( u_0 \ne y_0 \) by \( \rulename{\neg I} \) and \( \rulename{{=}E} \), and the second giving the witness \( x_0 \) at once. 1: the classical line named, with the reason. 2: (b), the converse derived, with both readings. An \( \rulename{RAA} \) box on \( \neg\exists y\, (u_0 \ne y) \) in place of the \( \rulename{LEM} \) split earns full marks if correct, its \( \rulename{RAA} \) line then named as the classical one. Fatal errors (0 for the step): the flag \( u_0 \) chosen as \( x_0 \); an \( \rulename{\exists E} \) box closed on a line that mentions its witness.
:::

<!-- dependency ledger
def-rules-equality (claim): the eight readings of a + a = 2 * a: each of three occurrences marked or not | inline (2^3 = 8)
def-rules-equality (claim): over Z with R read as < and P(x) as x < 1, a = 0, b = 5, the premises R(a, b), P(a) are true and P(b) is false | informal truth over a domain, F1.4 §01 (reading only; no derivability claim rests on it)
def-rules-equality (claim): over Z with a and y naming 0, "some integer is less than 0" is true and "some integer is less than itself" is false | informal truth over a domain, F1.4 §01 (reading only; no derivability claim rests on it)
def-rules-equality (claim): exists z (z < a) is the same sentence as exists y (y < a) up to renaming | F1.4 §02 (renaming bound variables)
prp-equality-symmetric-transitive (proof): (x = s)[s/x] is s = s and (x = s)[t/x] is t = s for x not in s, t | def-substitution (cited)
prp-equality-symmetric-transitive (proof): (s = x)[t/x] is s = t and (s = x)[u/x] is s = u for x not in s | def-substitution (cited)
prp-equality-symmetric-transitive (claim): symmetry and transitivity may be used as one line with terms in place of s, t, u | def-derived-rule (cited), extended in the text to terms; the derivations use nothing about s, t, u but that they are terms
prp-leibniz-law (proof): the 7-line derivation; the flagged-box range convention | def-rules-universal, def-rules-equality (cited); F1.4 §04 (range convention for a flagged box that immediately contains another)
prp-leibniz-law (claim): remark: with the law as premise, two forall-E and two ->E do the work of =E for P(x) | def-rule-universal-elimination (cited)
def-rules-equality (claim): warning, opacity: 7 * 13 = 91 | school arithmetic
exm-extensionality-logical-half (solution): the 9-line derivation | def-rules-equality, def-rules-universal (cited); sets used informally, F2.1 (index, Where this goes)
exm-extensionality-logical-half (claim): converse: two dots a, b, no membership: the hypothesis is true and a = b is false | finite counter-reading, checked by verify/ch05/exm-extensionality-logical-half.py
def-rules-equality (example): the chain a + b = 9: 2 * 3 + 3 = 9 | arith line (school arithmetic)
def-rules-equality (example): mixed chains: b^2 >= 0, so adding b^2 does not decrease a number; the = link carries over by =E | school algebra; AN1.1 (index, Where this goes); def-rules-equality and prp-equality-symmetric-transitive (cited)
def-rules-equality (claim): Quick check, mixed chain: 2 + 1 = 3, 3 <= 4 | school arithmetic
prp-equality-symmetric-transitive (example): additive inverse: y + 0 = y, 0 + c = c, associativity and commutativity of + | school algebra (field axioms); AN1.1 (index, Where this goes)
exm-equality-and-uniqueness-instances (claim): look-alike: the numeral 32 is one constant | F1.4 §02 (numerals such as 2 and 32 are constant symbols)
exr-equality-and-uniqueness-a1 (solution): (2+1)(2+1) = 9 | school arithmetic
exr-equality-and-uniqueness-b5 (solution): the counter-readings of (b), (e), (h) on {0, 1} | finite counter-readings, checked by verify/ch05/exr-equality-and-uniqueness-b5.py
exr-equality-and-uniqueness-c3 (solution): LEM is a derived rule whose derivation uses RAA | F1.2 §05 (prp-excluded-middle, cited by section)
-->
