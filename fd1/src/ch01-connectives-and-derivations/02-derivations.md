# Derivations, Starting with And

The previous section stated a slogan: a proof is a chain in which every line is a premise, an assumption, or one application of a rule. This section makes the premises and the rule steps exact (assumptions wait until Section 1.4): what a derivation is, how each line carries its reason, and how anyone can check one. Then it gives the first two rules of logic, the rules for "and".

## Why check by matching

A proof in a research paper can run to hundreds of steps, too many to hold in mind at once, so it is checked one step at a time. Two careful readers can disagree about whether a step is "obvious"; a rule that says exactly which steps are allowed settles it, since a step matches the rule or does not. And programs that check proofs work in the same spirit: each step must match a pattern.

Here is a small case: the chain
\[
0 < \tfrac{1}{3} < \tfrac{1}{2} < 1
\]
makes three claims, \( 0 < \tfrac13 \), \( \tfrac13 < \tfrac12 \), and \( \tfrac12 < 1 \), and a reader who accepts them concludes \( 0 < 1 \). The justification is one fact, used twice:

> if \( a < b \) and \( b < c \), then \( a < c \).

From \( 0 < \tfrac13 \) and \( \tfrac13 < \tfrac12 \) it gives \( 0 < \tfrac12 \). From \( 0 < \tfrac12 \) and \( \tfrac12 < 1 \) it gives \( 0 < 1 \).

To check those two steps, a reader needs nothing about fractions and nothing about what \( < \) means. It is enough to see that the two inequalities used in each step have the **same** expression in the middle, and that the new inequality joins the outer two. A clerk who had never seen a number could do it. So a proof can be checked without being understood: a proof is correct when every step matches its pattern, and matching is mechanical.

## A rule is a pattern

We borrow one fact about real numbers and use it as a rule.

- **Tr** (for "transitivity", or chaining): from \( a < b \) and \( b < c \), write \( a < c \).

It is a fact about numbers used as a rule, for practice; it is not a rule of logic.

A rule is applied by matching against a small picture of the lines it needs and the line it writes.

*A rule is a pattern: given these lines, you may write that line.*

::: {#def-rule-schema}
[Rule Schema]

A **rule schema** is a pattern of lines: **given** lines at the top, possibly none, and exactly **one new** line at the bottom, whose justification names the rule and cites the given lines. Line numbers in a schema are written \( i, j, k \). The letters in the pattern stand for arbitrary **expressions** of the right kind, and a use of the rule replaces them **consistently**: the same letter by the same expression, **symbol for symbol**, everywhere it occurs. A line is **justified by the rule** when it and the lines it cites, with their numbers, are an **instance** of a schema of the rule: the pattern with every letter replaced in this way. The schema of \( \mathrm{Tr} \) is

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {a < b}
  \have {j} {b < c}
  \have {k} {a < c} \by{Tr}{i,j}
\end{nd}$
\end{center}
```

Here \( a \), \( b \), \( c \) stand for expressions for numbers.
:::

In three points:

- The given lines may stand anywhere above the new line, in any order on the page, and need not be next to each other or to it.
- The citation's order says which line plays which part: "\( \mathrm{Tr} \ i, j \)" makes line \( i \) play \( a < b \) and line \( j \) play \( b < c \), unless the rule says otherwise (\( \rulename{\wedge I} \), below, accepts either order).
- Letters are replaced consistently, symbol for symbol. The middle letter \( b \) occurs in both given lines, so it must be replaced by the **same** string of symbols in both, not merely by the same number.

An instance first. Take \( i = 3 \), \( j = 5 \), \( k = 6 \), and replace \( a \) by \( 0 \), \( b \) by \( \tfrac12 \), and \( c \) by \( 1 \). The pattern becomes: line 3 is \( 0 < \tfrac12 \), line 5 is \( \tfrac12 < 1 \), and line 6 is \( 0 < 1 \), justified "\( \mathrm{Tr} \ 3, 5 \)".

Now a noninstance, by a minimal change. Keep line 3 as \( 0 < \tfrac12 \), and let line 5 be \( \tfrac13 < 1 \). Is "6. \( 0 < 1 \), \( \mathrm{Tr} \ 3, 5 \)" justified? Line 3 forces \( b \) to be \( \tfrac12 \), and line 5 forces it to be \( \tfrac13 \), so these lines are not an instance of the schema. Line 6 is true, but \( \mathrm{Tr} \) was not applied, so the line has no justification.

*Why define rules this way?* Because a rule applied by matching can be checked by someone who knows nothing about the subject. The schema turns "this step is obviously fine" into "this step matches that pattern", a claim anyone can test.

From the rules of logic on, the letters in a schema are Greek: \( \varphi \), \( \psi \), \( \chi \) (phi, psi, chi). A Greek letter is a hole in a rule's pattern; a capital \( P \) is a statement we are reasoning about. A pattern works like the formula \( (a + b)^2 = a^2 + 2ab + b^2 \), whose \( a \) and \( b \) are holes to be filled with any expression, the same one wherever the hole appears. Filling the holes of a schema works the same way, with parentheses put around a compound statement where they are needed. For example, if a schema has the given lines \( \varphi \) and \( \psi \) and the new line \( \varphi \wedge \psi \), then the three lines \( P \to Q \), \( R \), and \( (P \to Q) \wedge R \) are an instance of it, with \( \varphi \) replaced by \( P \to Q \) and \( \psi \) by \( R \).

::: {.warning}
The middle expression must match **exactly**, symbol for symbol. The step "\( 0 < \tfrac24 \) and \( \tfrac12 < 1 \), so \( 0 < 1 \)" is tempting, because \( \tfrac24 = \tfrac12 \) and every line in it is true, but it is not an application of \( \mathrm{Tr} \): the two middle expressions are different strings. A checker who had to notice that they are equal would need arithmetic, and the point of a schema is that a checker needs nothing. Compare symbols, not values.
:::

## Derivations without boxes

A proof strings steps together, each using what earlier steps produced. The next definition says exactly how.

::: {#def-box-free-derivation}
[Box-Free Derivation]

Fix a list of rules, each given by schemas. A **box-free derivation** is a finite list of numbered lines \( 1, 2, \dots, n \), where \( n \ge 1 \), each carrying one statement and a justification, such that:

::: {.enumerate options="label=(\roman*)"}
1. the first lines, possibly none and possibly all, are **premises**, justified by nothing; a short horizontal rule is drawn under the last premise;
2. every later line is justified by **one** rule of the list, citing **earlier** lines, and it and the cited lines form an instance of a schema of that rule.
:::

The **premises** of the derivation are its premise lines, and its **conclusion** is its last line.
:::

In words. Clause (i) says where a derivation starts: with the statements it is given, which are not proved and need no reason. Clause (ii) says how it goes on: each further line is one step of one rule, and the only lines it may use are ones already written. The word "earlier" is the only condition on which lines may be cited **for now**. Section 1.4 adds assumptions made inside boxes, and then "earlier" is refined to "available": an earlier line may become unusable once the box it sits in has closed.

The layout is always the same. Line numbers run down the left, statements sit in the middle, and each justification is on the right: the rule's name, then the cited line numbers. A vertical bar runs down the left, and a short horizontal rule under the last premise separates what is given from what is derived. From Section 1.4 on, a box draws a second, shorter bar, and the bars beside a line show which assumptions it depends on.

## First derivations

Here are two derivations with \( \mathrm{Tr} \), each with the reasoning that found it. The reasoning is the part to watch: a derivation on the page runs from the top down, but it is rarely found that way.

::: {#exm-chaining-derivation}
[Chaining]

Let \( x \), \( y \), \( u \), \( v \), \( w \), \( z \) be real numbers. Using the rule \( \mathrm{Tr} \) only, write a box-free derivation of each conclusion from the given premises.

::: {.enumerate options="label=(\alph*)"}
1. Premises \( 0 < x \), \( x < y \), \( y < 1 \); conclusion \( 0 < 1 \).
2. Premises \( u < v \), \( w < z \), \( v < w \); conclusion \( u < z \).
:::
:::

::: {.solution}
**(a)** *Idea.* The premises form a chain \( 0 < x < y < 1 \), each link sharing its right end with the next link's left end. So we work **forwards**, from what we have: chain the first two links at their shared middle \( x \), then the result with the third link at \( y \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {0 < x}
  \hypo {2} {x < y}
  \hypo {3} {y < 1}
  \have {4} {0 < y} \by{Tr}{1,2}
  \have {5} {0 < 1} \by{Tr}{4,3}
\end{nd}$
\end{center}
```

Read it back. Lines 1–3 are the premises. Line 4: lines 1 and 2 are an instance of \( \mathrm{Tr} \), with \( a \), \( b \), \( c \) replaced by \( 0 \), \( x \), \( y \). Line 5: lines 4 and 3 are one, with \( a \), \( b \), \( c \) replaced by \( 0 \), \( y \), \( 1 \). The letters are replaced afresh at each use: the \( b \) of line 4 has nothing to do with the \( b \) of line 5.

**(b)** *Idea.* This time the chain is scrambled, so we work **backwards**, from what we want. The goal \( u < z \) can come from \( \mathrm{Tr} \) only if we have some \( u < m \) and \( m < z \) for a single expression \( m \). The only premise starting with \( u \) is \( u < v \), so try \( m = v \); the remaining need is \( v < z \), a new, smaller goal. It can come from \( \mathrm{Tr} \) with some \( v < m' \) and \( m' < z \); the only premise starting with \( v \) is \( v < w \), and with \( m' = w \) the second need, \( w < z \), is a premise. The search has reached the premises, and the derivation is its record, written **forwards**.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {u < v}
  \hypo {2} {w < z}
  \hypo {3} {v < w}
  \have {4} {v < z} \by{Tr}{3,2}
  \have {5} {u < z} \by{Tr}{1,4}
\end{nd}$
\end{center}
```

The search could have started instead from \( w < z \), the premise ending in \( z \): with \( m = w \) it needs \( u < w \), which is \( \mathrm{Tr} \ 1, 3 \), and then \( u < z \) is \( \mathrm{Tr} \ 4, 2 \). That is a different correct derivation. The same premises and conclusion usually have many derivations, and any one of them shows that the conclusion follows from the premises.
:::

Part (b) was found backwards, from the goal; part (a) forwards. The rest of this section names the two directions.

::: {.check}
Line 1 of a derivation is \( 0 < x \) and line 3 is \( x < 1 \). Which is correct: "4. \( 0 < 1 \), \( \mathrm{Tr} \ 1, 3 \)" or "4. \( 0 < 1 \), \( \mathrm{Tr} \ 3, 1 \)"?
:::

::: {.solution}
The first. With the citation "1, 3", line 1 plays \( a < b \) and line 3 plays \( b < c \): \( a \) is \( 0 \), \( b \) is \( x \) in both lines, and \( c \) is \( 1 \), so the new line \( a < c \) is \( 0 < 1 \). With "3, 1", line 3 would play \( a < b \) and line 1 would play \( b < c \), so \( b \) would have to be \( 1 \) (from line 3) and \( 0 \) (from line 1) at once.
:::

## Reading a derivation

Finding a derivation may need an idea, as part (b) of @exm-chaining-derivation did. Checking one never does. For each line after the premises, ask three questions.

1. **Which rule?** Name the rule the justification cites, and check that it is on the list of rules.
2. **Do the cited lines and this line form an instance of that rule's schema?** Find the replacement of the letters: read it off the cited lines in the order the citation gives them (or, for a rule whose lines may be cited in either order, try both: the new line decides), and check that every letter gets the same expression each time it occurs, and that the new line is what the pattern then says.
3. **Are the cited lines earlier?** Each cited number must be smaller than the number of the line doing the citing.

A line that passes all three is correct, whatever it says and whether or not it is true. Here is the check run on part (a) of @exm-chaining-derivation.

| Line | Rule | Cites | Instance (the letters' values) | Earlier? |
|---|---|---|---|---|
| 1–3 | premises | — | — | — |
| 4 | \( \mathrm{Tr} \) | 1, 2 | \( a \): \( 0 \); \( b \): \( x \); \( c \): \( y \) | 1, 2 < 4: yes |
| 5 | \( \mathrm{Tr} \) | 4, 3 | \( a \): \( 0 \); \( b \): \( y \); \( c \): \( 1 \) | 4, 3 < 5: yes |

Every line passes, so the list is a derivation. Section 1.4 extends this table, when "earlier" becomes "available".

*Finding a derivation may need an idea; checking one never does.*

::: {.second-reading title="Two ways to break a derivation"}
A line can fail one question and pass the others. The next example breaks a correct derivation in two ways, each time with the smallest change that does it.

::: {#exm-not-a-derivation}
[Not a derivation]

Each list below is the derivation of part (a) of @exm-chaining-derivation with one change. Say which of the three questions of "Reading a derivation" fails, and at which line.

::: {.enumerate options="label=(\alph*)"}
1. The statements of lines 4 and 5 are swapped, each taking its justification with it, so that line 4 is now "\( 0 < 1 \), \( \mathrm{Tr} \ 5, 3 \)" and line 5 is "\( 0 < y \), \( \mathrm{Tr} \ 1, 2 \)".
2. Line 5 is justified "\( \mathrm{Tr} \ 3, 4 \)" instead of "\( \mathrm{Tr} \ 4, 3 \)".
:::
:::

::: {.solution}
(a) The list is the following.

```{=latex}
\begin{center}
% Deliberately invalid: line 4 cites line 5, a later line. The forward citation is written as
% literal text, because fitch.sty resolves line references in one pass and would print ??
% for a later line; so check_fitch cannot see it, and the block carries no expect-invalid marker.
$\begin{nd}
  \hypo {1} {0 < x}
  \hypo {2} {x < y}
  \hypo {3} {y < 1}
  \have {4} {0 < 1} \by{Tr\ 5, 3}{}
  \have {5} {0 < y} \by{Tr}{1,2}
\end{nd}$
\end{center}
```

Line 5 passes all three questions, exactly as line 4 did before. Line 4 passes the first two: lines 5, 3, and 4 are an instance of \( \mathrm{Tr} \) with \( a \), \( b \), \( c \) replaced by \( 0 \), \( y \), \( 1 \). It fails the third, because it cites line 5, which is not earlier. So the list is not a derivation. (It would also be useless if it were one: its last line is now \( 0 < y \), not \( 0 < 1 \).)

(b) Line 5 is now "\( 0 < 1 \), \( \mathrm{Tr} \ 3, 4 \)". Lines 3 and 4 are earlier, so the third question passes, and the rule is named, so the first passes. The second fails. The citation makes line 3, \( y < 1 \), play \( a < b \), so \( a \) is \( y \) and \( b \) is \( 1 \); and it makes line 4, \( 0 < y \), play \( b < c \), so \( b \) is \( 0 \). The letter \( b \) cannot be both \( 1 \) and \( 0 \), so there is no instance. The lines are the right ones in the wrong roles.
:::

Change (b) shows why the citation order is part of the justification, and change (a) why the order of the lines is. Exercise C2 below asks what would go wrong if a line were allowed to cite a later one.
:::

## What a derivation proves

A derivation shows that its conclusion follows from its premises. The symbol \( \vdash \) says that such a derivation exists.

::: {#def-derivable}
[Derivable]

Let \( \Gamma \) be a list of statements \( \varphi_1, \dots, \varphi_n \), where \( n \ge 0 \), and let \( \psi \) be a statement. We say \( \psi \) is **derivable** from \( \Gamma \), and write
\[
\Gamma \vdash \psi ,
\]
if **there is** a derivation, using the rules of logic, whose premises **all belong to** \( \Gamma \) and whose last line is \( \psi \). We write \( \varphi_1, \dots, \varphi_n \vdash \psi \) for \( \Gamma \vdash \psi \), and \( \vdash \psi \) when \( \Gamma \) is empty.
:::

Here \( \Gamma \) (capital gamma) is just a name for a list of statements.

::: {#def-sequent}
[Sequent]

Let \( P_1, \dots, P_n \) and \( Q \) be statements, where \( n \ge 0 \). The expression \( P_1, \dots, P_n \vdash Q \), read "\( P_1 \) to \( P_n \) prove \( Q \)", is a **sequent**. It is the **claim** that \( Q \) is derivable from \( P_1, \dots, P_n \) in the sense of @def-derivable. The statements \( P_1, \dots, P_n \) are its **premises** and \( Q \) is its **conclusion**; when \( n = 0 \) we write \( \vdash Q \).
:::

The symbol \( \vdash \) is called the **turnstile**. A sequent is not true merely because its conclusion is true: it claims that a derivation exists, and it is proved by exhibiting one.

In words, three remarks.

1. *Which derivations?* Until Section 1.4, "derivation" means a box-free derivation (@def-box-free-derivation). Section 1.4 widens the word to allow boxes; nothing proved before changes, since a box-free derivation is still a derivation.
2. *Not every premise must be used.* A derivation may ignore some statements of \( \Gamma \), and it may even have no premise lines at all. It may not use a premise that is **not** in \( \Gamma \).
3. *Relative to a list of rules.* The symbol \( \vdash \) always refers to a list of rules. From "The rules for and" below on, it is the rules of logic introduced so far; adding a rule never destroys a derivation, so a sequent once derived stays derived. Before that, we name the rule: "\( \Gamma \vdash \psi \) **with** \( \mathrm{Tr} \)".

For instance, part (a) of @exm-chaining-derivation shows \( 0 < x, \ x < y, \ y < 1 \vdash 0 < 1 \) with \( \mathrm{Tr} \).

In the derivations from here on, the capital letters \( P \), \( Q \), \( R \), \( S \) stand for arbitrary statements, as in Section 1.1. A derivation written with them proves not one sequent but infinitely many at once, one for each way of putting statements in for the letters.

::: {.check}
What sequent "with \( \mathrm{Tr} \)" does part (b) of @exm-chaining-derivation show?
:::

::: {.solution}
\( u < v, \ w < z, \ v < w \vdash u < z \) with \( \mathrm{Tr} \). The premises of the derivation are lines 1–3, and its last line is \( u < z \).
:::

::: {#exm-derivations}
[Derivations, simplest first]

Decide whether each of the following is a derivation, and if so, what it shows.

::: {.enumerate options="label=(\alph*)"}
1. The single line \( 1 \quad P \quad \text{premise} \).
2. The empty list, with no lines at all.
3. The derivation of part (a) of @exm-chaining-derivation, for the list of rules consisting of \( \mathrm{Tr} \) alone.
:::
:::

::: {.solution}
(a) Yes. Its only line is a premise, so clause (i) of @def-box-free-derivation holds, and clause (ii) has no lines to speak about. Its last line is \( P \). It shows \( P \vdash P \): every statement is derivable from itself. No rule was used, so this holds whatever the list of rules is.

Parts (b) and (c) are answered in the fold below.
:::

::: {.second-reading title="Edge cases"}
**A derivation of one line.** The degenerate case is worth a look. A single premise line, with nothing after it, satisfies both clauses of @def-box-free-derivation: clause (i) holds, and clause (ii) has no lines to speak about. So it is a derivation, and its premise is its conclusion.

**Part (b) of @exm-derivations.** No. The definition asks for \( n \ge 1 \) lines, and a derivation must have a last line to be its conclusion. So the empty list derives nothing. In the same way, a list with no premises can never get started with \( \mathrm{Tr} \), or any rule that cites a line: its first line would have to cite an earlier line, and there is none. Every rule met before Section 1.4 cites at least one line, so until then \( \vdash \psi \) holds for no \( \psi \). Section 1.4 changes that.

**Part (c) of @exm-derivations.** Yes. Lines 1–3 are premises, with the rule drawn under line 3: clause (i). Line 4 cites lines 1 and 2, which are earlier, and lines 1, 2, 4 are an instance of \( \mathrm{Tr} \) with \( a \), \( b \), \( c \) replaced by \( 0 \), \( x \), \( y \). Line 5 cites lines 4 and 3, which are earlier, and lines 4, 3, 5 are an instance with \( a \), \( b \), \( c \) replaced by \( 0 \), \( y \), \( 1 \). So clause (ii) holds for both later lines. The premises are the three premise lines and the conclusion is \( 0 < 1 \).
:::

::: {.warning}
A premise is **given**, not proved: from the false premises \( 1 < 0 \) and \( 0 < -1 \), the rule \( \mathrm{Tr} \) gives the false line \( 1 < -1 \), in a correct derivation. What a correct derivation guarantees is only that **if** the premises are true, so is the conclusion, and even that only for rules that never lead from true lines to a false one.
:::

## The rules for and

Analysis is full of chains such as \( 0 < x < 1 \), which says \( 0 < x \) **and** \( x < 1 \). A proof that **uses** it often needs one half: "in particular \( x > 0 \), so we may divide by \( x \)." A proof that **proves** it must prove both halves; one half is not the whole claim. Section 1.1 previewed these two moves informally. Here they become rules, checked by matching, as \( \mathrm{Tr} \) was.

*To prove "\( \varphi \) and \( \psi \)", prove each; to use it, take either.*

::: {#def-rules-conjunction}
[Rules for Conjunction]

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

The first schema is the rule \( \rulename{\wedge I} \) (**and-introduction**). Its two given lines may be cited in either order: the new line shows which statement is its left conjunct, so question 2 of "Reading a derivation" tries both orders. The second and third are the two forms of the rule \( \rulename{\wedge E} \) (**and-elimination**), one writing the left conjunct and one the right.
:::

**\( \rulename{\wedge I} \).**

- *Schema:* the first one in the block above.
- *Reading:* two lines in hand, anywhere above and cited in either order; write their conjunction.
- *Example:* from line 2, \( P \), and line 5, \( Q \), "\( \rulename{\wedge I} \) 5, 2" (or "2, 5") writes \( Q \wedge P \).

**\( \rulename{\wedge E} \).**

- *Schema:* the other two in the block.
- *Reading:* one line whose **main connective** (@def-main-connective) is \( \wedge \); write either side, one layer at a time.
- *Example:* from \( (P \wedge Q) \wedge R \) it writes \( P \wedge Q \) or \( R \), never \( P \).

If \( \varphi \) and \( \psi \) are true, so is \( \varphi \wedge \psi \); if \( \varphi \wedge \psi \) is true, so is each side.

::: {.warning}
\( \rulename{\wedge E} \) reaches one layer at a time. From line 1, \( (P \wedge Q) \wedge R \), the line "\( Q \) — \( \rulename{\wedge E} \) 1" is not an instance of either \( \rulename{\wedge E} \) schema, because line 1's conjuncts are \( P \wedge Q \) and \( R \). The line is wrong even though \( Q \) does follow; the repair costs one line: \( P \wedge Q \) by \( \rulename{\wedge E} \) 1 first, then \( Q \) from it.
:::

::: {.check}
Which statements can \( \rulename{\wedge E} \) write, in one application each, from the line \( (P \wedge Q) \wedge (R \wedge S) \)?
:::

::: {.solution}
Only \( P \wedge Q \) and \( R \wedge S \). The main connective is the middle \( \wedge \), so \( \varphi \) is \( P \wedge Q \) and \( \psi \) is \( R \wedge S \). Each of \( P, Q, R, S \) needs a second application, to one of those two lines.
:::

::: {.check}
Line 1 is \( (P \wedge Q) \to R \). May "\( P \wedge Q \) — \( \rulename{\wedge E} \) 1" be written?
:::

::: {.solution}
No. Line 1's main connective is \( \to \), so \( \rulename{\wedge E} \) cannot take it apart, although \( \wedge \) occurs in it.
:::

## Two directions of reasoning

A derivation has premises at the top and its goal, the conclusion we want, at the bottom. Between them is a gap, and finding a derivation means filling the gap. There are two places to start.

*From the goal.* Ask: **what is the goal's main connective?** If it is \( \wedge \), the last line can be written by \( \rulename{\wedge I} \), and then the goal \( \varphi \wedge \psi \) splits into two **subgoals**, \( \varphi \) and \( \psi \), each to be reached on some line above. This is **goal-directed** reasoning. It works backwards, up from the bottom of the gap, and asks which **introduction** rule builds the goal's main connective.

*From the premises.* Ask: **what are the main connectives of the lines we already have?** A line whose main connective is \( \wedge \) can be taken apart by \( \rulename{\wedge E} \), and each conjunct becomes a new line to work with. This is **premise-directed** reasoning. It works forwards, down from the top of the gap, and asks which **elimination** rule uses the line's main connective.

*Work from both ends: take the premises apart, and build the goal from its parts.*

The derivation is finished when the two ends meet. Part (b) of @exm-chaining-derivation already worked backwards, with \( \mathrm{Tr} \) in the part that introduction rules play from now on.

Scratch work for a search fits in a two-column table: the **Givens**, what is in hand (premises and lines derived so far), and the **Goal**, what is still needed. A goal-directed step replaces a goal by its subgoals; a premise-directed step adds to the Givens. The search is finished when every goal is among the Givens. The search for \( P \wedge Q \vdash Q \wedge P \), one row per step:

| Givens | Goal |
|---|---|
| \( P \wedge Q \) | \( Q \wedge P \) |
| \( P \wedge Q \) | \( Q \), \( P \) (\( \rulename{\wedge I} \) splits the goal) |
| \( P \wedge Q \), \( P \), \( Q \) (\( \rulename{\wedge E} \)) | \( Q \) \( \checkmark \), \( P \) \( \checkmark \) |

The derivation this search finds is @prp-and-commutes below.

## First derivations with and

::: {#exm-conjunction-warm-ups}
[Two warm-ups]

Give a derivation of each sequent.

::: {.enumerate options="label=(\alph*)"}
1. \( P, \ Q \vdash Q \wedge P \).
2. \( P \wedge Q \vdash Q \).
:::
:::

::: {.solution}
(a) *Idea.* The goal \( Q \wedge P \) has main connective \( \wedge \), so, goal-directed, its last line is \( \rulename{\wedge I} \) with subgoals \( Q \) and \( P \). Both subgoals are premises, so the two ends meet at once.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {Q}
  \have {3} {Q \wedge P} \ai{2,1}
\end{nd}$
\end{center}
```

The citation "2, 1" lists \( Q \)'s line first; "1, 2" would do as well, since the line shows the order.

(b) *Idea.* The goal \( Q \) is a letter, with no main connective, so the goal suggests no rule. The premise has main connective \( \wedge \), so, premise-directed, take it apart; its right conjunct is the goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {Q} \ae{1}
\end{nd}$
\end{center}
```

Line 2 is the second form of \( \rulename{\wedge E} \), with \( \varphi \coloneqq P \) and \( \psi \coloneqq Q \).
:::

The two derivations are box-free derivations in the sense of @def-box-free-derivation, with \( \rulename{\wedge I} \) and \( \rulename{\wedge E} \) as the list of rules: premises first, and every later line an instance of a schema whose given lines are earlier. By @def-derivable they show the two sequents. When the goal is a letter, as in (b), only the premises can suggest a step; when every subgoal is a premise, as in (a), the premises need no taking apart. The first proposition below needs both ends.

::: {.second-reading title="Edge cases for and-introduction"}
**One line cited twice.** Nothing in the schema of \( \rulename{\wedge I} \) says that \( i \) and \( j \) are different lines. With \( i = j \), the letters \( \varphi \) and \( \psi \) are replaced by the same statement, and the rule writes \( \varphi \wedge \varphi \). It is a silly line, and a legal one. For instance, \( P \vdash P \wedge P \): the goal is a conjunction, so \( \rulename{\wedge I} \), with the subgoals \( P \) and \( P \), and the one premise meets both.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have {2} {P \wedge P} \ai{1,1}
\end{nd}$
\end{center}
```
:::

The first result is that the order of a conjunction does not matter.

::: {#prp-and-commutes}
[Conjunction Commutes]

\( P \wedge Q \vdash Q \wedge P \).
:::

::: {.idea}
Write the premise at the top, the goal at the bottom, and leave a gap (left picture; the lines carry the numbers they will have at the end). Start from the goal. Its main connective is \( \wedge \), so the last line will be \( \rulename{\wedge I} \), and we need \( P \) and \( Q \) on earlier lines (right picture: two subgoals, not yet justified). Now start from the premise. Its main connective is \( \wedge \), so \( \rulename{\wedge E} \) gives \( P \) and gives \( Q \). That closes the gap: the pieces the goal asks for are the pieces the premise supplies. (This is the search of the Givens/Goal table above.)

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have[\ ][0] {} {\vdots}
  \have[][4] {4} {Q \wedge P}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have[\ ][0] {} {\vdots}
  \have[][2] {2} {P}
  \have {3} {Q}
  \have {4} {Q \wedge P} \ai{3,2}
\end{nd}$
\end{center}
```
:::

::: {.proof}
The following is a box-free derivation with the single premise \( P \wedge Q \) and last line \( Q \wedge P \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {Q} \ae{1}
  \have {4} {Q \wedge P} \ai{3,2}
\end{nd}$
\end{center}
```

Lines 2 and 3 are the two forms of \( \rulename{\wedge E} \) applied to line 1, and line 4 is \( \rulename{\wedge I} \) applied to lines 3 and 2, and the line shows \( Q \) on the left. By @def-derivable, \( P \wedge Q \vdash Q \wedge P \).
:::

Read back in words, the derivation is a short paragraph: *We are given that \( P \) and \( Q \). In particular \( P \) holds. In particular \( Q \) holds. So \( Q \) and \( P \) both hold.* Each sentence is one line, and each "in particular" is one application of \( \rulename{\wedge E} \).

Nothing in the derivation looks at what \( P \) and \( Q \) say: with \( P \): "\( 0 < x \)" and \( Q \): "\( x < 1 \)" it turns "\( 0 < x \) and \( x < 1 \)" into "\( x < 1 \) and \( 0 < x \)", and it does the same for any two statements. Because the letters stand for arbitrary statements, one derivation written with letters proves every such instance at once.

The second result is that the grouping of a conjunction does not matter either. It needs the premise taken apart in two layers.

::: {#prp-and-associative}
[Conjunction Is Associative]

\( (P \wedge Q) \wedge R \vdash P \wedge (Q \wedge R) \).
:::

::: {.idea}
From the goal: its main connective is the **outer** \( \wedge \), so the last line is \( \rulename{\wedge I} \) with the subgoals \( P \) and \( Q \wedge R \), and the second splits again into \( Q \) and \( R \). From the premise: \( \rulename{\wedge E} \) gives \( P \wedge Q \) and \( R \), and again, on \( P \wedge Q \), gives \( P \) and \( Q \). Both searches stop at the three letters, and the ends meet there. Since \( \rulename{\wedge E} \) reaches one layer at a time, the premise must be peeled in two rounds.

In pictures: the goal below a gap; then the first round of \( \rulename{\wedge E} \) as lines 2–3, a gap for lines 4–5, and the subgoal \( Q \wedge R \) as line 6, lines 6 and 7 not yet justified (line 7 will be \( \rulename{\wedge I} \) 4, 6).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \wedge R}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {P \wedge (Q \wedge R)}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {(P \wedge Q) \wedge R}
  \have {2} {P \wedge Q} \ae{1}
  \have {3} {R} \ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {Q \wedge R}
  \have {7} {P \wedge (Q \wedge R)}
\end{nd}$
\end{center}
```
:::

::: {.proof}
The following is a box-free derivation with the single premise \( (P \wedge Q) \wedge R \) and last line \( P \wedge (Q \wedge R) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \wedge R}
  \have {2} {P \wedge Q} \ae{1}
  \have {3} {R} \ae{1}
  \have {4} {P} \ae{2}
  \have {5} {Q} \ae{2}
  \have {6} {Q \wedge R} \ai{5,3}
  \have {7} {P \wedge (Q \wedge R)} \ai{4,6}
\end{nd}$
\end{center}
```

Lines 2 and 3 apply \( \rulename{\wedge E} \) to line 1, with \( \varphi \coloneqq P \wedge Q \) and \( \psi \coloneqq R \). Lines 4 and 5 apply \( \rulename{\wedge E} \) to line 2, with \( \varphi \coloneqq P \) and \( \psi \coloneqq Q \). Line 6 applies \( \rulename{\wedge I} \) to lines 5 and 3, and line 7 applies \( \rulename{\wedge I} \) to lines 4 and 6, with \( \varphi \coloneqq P \) and \( \psi \coloneqq Q \wedge R \). By @def-derivable, \( (P \wedge Q) \wedge R \vdash P \wedge (Q \wedge R) \).
:::

The lines could come in other orders. Line 3 could come after lines 4 and 5, for instance, since it is used only at line 6. What cannot move is the dependence: every line must come after each line it cites.

::: {.remark}
The converse, \( P \wedge (Q \wedge R) \vdash (P \wedge Q) \wedge R \), is derived the same way, peeling the premise's inner conjunction on the right instead of the left; Exercise B1 asks you to write it out. With both directions, the brackets in a chain of conjunctions carry no information, which is why the chain \( 0 < x < 1 < y \) is written without any.
:::

### A line is not used up

A line of a derivation is a statement that has been established. Citing it does not consume it: it can be cited again, by as many later lines as need it. The derivation of \( P \wedge Q, \ R \vdash (P \wedge R) \wedge (Q \wedge R) \) shows this.

::: {.idea}
From the goal: \( \rulename{\wedge I} \) at the bottom, with subgoals \( P \wedge R \) and \( Q \wedge R \), each split again by \( \rulename{\wedge I} \). From the premises: \( \rulename{\wedge E} \) on line 1 gives \( P \) and \( Q \), and \( R \) is already a premise. Both subgoals that need \( R \) cite the same line 2.

In pictures: the goal below a gap; then the subgoals as lines 5–6, not yet justified.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {R}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {(P \wedge R) \wedge (Q \wedge R)}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {R}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {P \wedge R}
  \have {6} {Q \wedge R}
  \have {7} {(P \wedge R) \wedge (Q \wedge R)} \ai{5,6}
\end{nd}$
\end{center}
```
:::

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {R}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ae{1}
  \have {5} {P \wedge R} \ai{3,2}
  \have {6} {Q \wedge R} \ai{4,2}
  \have {7} {(P \wedge R) \wedge (Q \wedge R)} \ai{5,6}
\end{nd}$
\end{center}
```

Line 2 is cited by lines 5 and 6, and line 1 by lines 3 and 4. In a written proof this is the everyday "we use the hypothesis \( x > 0 \) again".

::: {.second-reading title="Any rearrangement of a conjunction"}
**Take everything apart, rebuild in the new order.** One more derivation rearranges four letters: \( (P \wedge Q) \wedge (R \wedge S) \vdash (S \wedge Q) \wedge (P \wedge R) \).

::: {.idea}
From the premise: two layers of \( \wedge \), so \( \rulename{\wedge E} \) twice on line 1 and then twice on each of the two new lines, which leaves the four letters on lines 4 to 7. From the goal: two layers of \( \wedge \), so \( \rulename{\wedge I} \) builds \( S \wedge Q \) and \( P \wedge R \) from the letters and then joins them. There is nothing to choose; the only care needed is the order of each citation.
:::

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \wedge (R \wedge S)}
  \have {2} {P \wedge Q} \ae{1}
  \have {3} {R \wedge S} \ae{1}
  \have {4} {P} \ae{2}
  \have {5} {Q} \ae{2}
  \have {6} {R} \ae{3}
  \have {7} {S} \ae{3}
  \have {8} {S \wedge Q} \ai{7,5}
  \have {9} {P \wedge R} \ai{4,6}
  \have {10} {(S \wedge Q) \wedge (P \wedge R)} \ai{8,9}
\end{nd}$
\end{center}
```

The recipe visibly does not depend on these particular letters or brackets. Take the premise apart with \( \rulename{\wedge E} \) until only letters remain, then build the goal from the letters with \( \rulename{\wedge I} \), inside out. It works whenever the premise and the goal are both built from letters by \( \wedge \) alone and every letter of the goal occurs in the premise, whatever the bracketing and the order on either side. So "\( \wedge \) is commutative and associative" is, in the end, the observation that \( \rulename{\wedge E} \) can always take a conjunction down to its letters and \( \rulename{\wedge I} \) can always build one back up.
:::

## How this looks in a mathematical proof

Real proofs mix the logical rules with facts about their subject.

::: {#exm-product-in-unit-interval}
[A product of numbers in the unit interval]

Let \( x \) and \( y \) be real numbers with \( 0 < x < 1 \) and \( 0 < y < 1 \). Show that \( 0 < xy < 1 \), and name the rule behind each logical step.
:::

::: {.solution}
The hypothesis \( 0 < x < 1 \) is the conjunction \( (0 < x) \wedge (x < 1) \). By \( \rulename{\wedge E} \) we have \( 0 < x \) and \( x < 1 \) separately, and likewise \( 0 < y \) and \( y < 1 \).

Since \( x > 0 \) and \( y > 0 \), the product \( xy \) is positive. Since \( y < 1 \) and \( x > 0 \), multiplying by \( x \) gives \( xy < x \); together with \( x < 1 \) this gives \( xy < 1 \). These steps are school algebra, not logic.

Finally, from \( 0 < xy \) and \( xy < 1 \), \( \rulename{\wedge I} \) gives \( (0 < xy) \wedge (xy < 1) \), which is \( 0 < xy < 1 \).

As a derivation, the same proof reads as follows.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(0 < x) \wedge (x < 1)}
  \hypo {2} {(0 < y) \wedge (y < 1)}
  \have {3} {0 < x} \ae{1}
  \have {4} {x < 1} \ae{1}
  \have {5} {0 < y} \ae{2}
  \have {6} {y < 1} \ae{2}
  \have {7} {0 < xy} \by{algebra}{3,5}
  \have {8} {xy < 1} \by{algebra}{3,4,6}
  \have {9} {(0 < xy) \wedge (xy < 1)} \ai{7,8}
\end{nd}$
\end{center}
```

Lines 7 and 8 are justified "algebra": each is a step by a fact about numbers used as a rule, exactly as Tr was used above, and not a rule of logic. Line 7 uses "a product of two positive numbers is positive"; line 8 uses "multiplying an inequality by a positive number keeps its direction", then the pattern of Tr.
:::

The facts about numbers supply the content of the solution; the rules supply the joints, taking statements apart and putting the pieces back together. The goal-directed reading is visible in the prose too: "show \( 0 < xy < 1 \)" is a conjunction, so the solution sets itself two subgoals, and it says "finally" when the two meet.

::: {.second-reading title="A chain in an analysis proof"}
A proof about sequences might contain the line
\[
0 < \frac{1}{n+1} < \frac{1}{n} \le 1 \qquad \text{for } n \in \nZ_{>0} .
\]
It asserts three links: \( 0 < \frac{1}{n+1} \), \( \frac{1}{n+1} < \frac1n \), and \( \frac1n \le 1 \). A reader who takes from it a claim about its two ends, \( 0 < 1 \), performs two steps in silence. The first is one application of chaining: \( 0 < \frac{1}{n+1} \) and \( \frac{1}{n+1} < \frac1n \) give \( 0 < \frac1n \). The second joins \( 0 < \frac1n \) with \( \frac1n \le 1 \), and it is **not** \( \mathrm{Tr} \): the line \( \frac1n \le 1 \) has \( \le \), not \( < \), so the lines do not match the schema. It is a different pattern, "from \( a < b \) and \( b \le c \), write \( a < c \)", another true fact about numbers. That is exactly why a justification must name the pattern it uses. "By the chain" does not say which one.

Written chains like this one are everywhere in analysis, and they are derivations with the justifications left off. Nobody writes the justifications out in a real proof about numbers. But a reader checking a hard chain does what the table of "Reading a derivation" does: for each step, which fact, applied to which earlier lines.
:::

## Common errors

Besides \( \rulename{\wedge E} \) applied through a layer, one more error is common.

::: {.warning}
\( \rulename{\wedge E} \) applies only to a line whose **main connective** is \( \wedge \). The line \( (P \wedge Q) \to R \) contains a \( \wedge \), but its main connective is \( \to \), so "\( P \) — \( \rulename{\wedge E} \) 1" is illegal. With \( x \) a real number, \( P \): "\( x > 0 \)", \( Q \): "\( x > 1 \)" and \( R \): "\( x^2 > 1 \)", the premise "if \( x > 0 \) and \( x > 1 \), then \( x^2 > 1 \)" is true for every \( x \), yet at \( x = -1 \) the line \( x > 0 \) is false.
:::

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (and-E applied to an implication)
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \have {2} {P} \ae{1}
\end{nd}$
\end{center}
```

The illegal step leads from a true premise to a false line, so no rule that allowed it could be safe.

## The rule card

The card gives each rule so far, its shape, the sentence that uses it in a written proof and, for readers who meet a proof assistant, the Lean code that performs it (`h.1` names the left half of a hypothesis `h`). Nothing later depends on the last column.

| Rule | Shape | You write | Lean |
|------|------------------|--------------------------------------|------------------------|
| \( \rulename{\wedge I} \) | \( \varphi \), \( \psi \) \( \Longrightarrow \) \( \varphi \wedge \psi \) | "We show \( P \), and we show \( Q \)." | `constructor` |
| \( \rulename{\wedge E} \) | \( \varphi \wedge \psi \) \( \Longrightarrow \) \( \varphi \) (or \( \psi \)) | "In particular, \( P \)." | `h.1` (and `h.2`) |

::: {.remark}
[Looking ahead]

Chapter 3 checks, for every rule of Chapters 1 and 2 at once, that no rule leads from true lines to a false one. Until then each rule comes with the one-sentence reason it is safe, as the sentence after the bullets for "and" did.
:::

## Exercises

### A. Check your understanding

::: {#exr-derivations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of a box-free derivation and of \( \Gamma \vdash \psi \), and write the three schemas of @def-rules-conjunction from memory, naming the rule of each.
2. Which statements does one application of \( \rulename{\wedge E} \) give from the line \( P \wedge (Q \wedge R) \)?
3. In the derivation in the proof of @prp-and-associative, why must line 2 come before line 4?
4. Fill in the justifications (i)–(iv) of the following derivation.

   ```{=latex}
   \begin{center}
   $\begin{nd}
     \hypo {1} {P \wedge (Q \wedge R)}
     \have {2} {P} \by{(i)}{}
     \have {3} {Q \wedge R} \by{(ii)}{}
     \have {4} {R} \by{(iii)}{}
     \have {5} {R \wedge P} \by{(iv)}{}
   \end{nd}$
   \end{center}
   ```

5. True or false, with a reason: if \( \Gamma \vdash \psi \) with \( \mathrm{Tr} \), and every statement in \( \Gamma \) is true, then \( \psi \) is true.
6. What sequent does the derivation in (d) show?
:::
:::

::: {.solution}
(a) A box-free derivation, relative to a list of rules, is a finite list of numbered lines, at least one, each with a statement and a justification, in which the first lines, possibly none and possibly all, are premises, justified by nothing, and every later line is justified by one rule of the list, citing earlier lines, so that it and the cited lines form an instance of a schema of that rule (@def-box-free-derivation). And \( \Gamma \vdash \psi \) means that there is a derivation whose premises all belong to \( \Gamma \) and whose last line is \( \psi \) (@def-derivable). For the schemas see @def-rules-conjunction: \( \rulename{\wedge I} \) has given lines \( i \): \( \varphi \) and \( j \): \( \psi \) and new line \( k \): \( \varphi \wedge \psi \), cited "\( \rulename{\wedge I} \) \( i, j \)" (or \( j, i \)); the two forms of \( \rulename{\wedge E} \) each have the given line \( i \): \( \varphi \wedge \psi \) and the new line \( k \): \( \varphi \), respectively \( \psi \), cited "\( \rulename{\wedge E} \) \( i \)".

(b) \( P \), or \( Q \wedge R \). The main connective is the first \( \wedge \), so \( \varphi \) is \( P \) and \( \psi \) is \( Q \wedge R \).

(c) Line 4 is \( P \), obtained by \( \rulename{\wedge E} \) from line 2, \( P \wedge Q \). A rule may cite only earlier lines (@def-box-free-derivation), and \( P \) cannot be obtained from line 1 in one step, since line 1's conjuncts are \( P \wedge Q \) and \( R \).

(d) (i) \( \rulename{\wedge E} \) 1; (ii) \( \rulename{\wedge E} \) 1; (iii) \( \rulename{\wedge E} \) 3; (iv) \( \rulename{\wedge I} \) 4, 2. "\( \rulename{\wedge I} \) 2, 4" is equally right: the line \( R \wedge P \) shows which conjunct is on the left.

(e) True. \( \mathrm{Tr} \) leads from true lines to a true line: if \( a < b \) and \( b < c \) are true, so is \( a < c \). Go down the derivation: the premises are in \( \Gamma \), so they are true, and each later line comes from earlier, true lines by \( \mathrm{Tr} \), so it is true too. Hence the last line, \( \psi \), is true. This is the property the Looking-ahead box of this section promises for the rules of logic.

(f) \( P \wedge (Q \wedge R) \vdash R \wedge P \): its only premise is line 1, and its last line is \( R \wedge P \).
:::

::: {#exr-derivations-a2}
[A2: Drill]

Answer each part in a line or two.

::: {.enumerate options="label=(\alph*)"}
1. Lines 1 \( 2 < y \) and 2 \( y < z \) are given. What does "\( \mathrm{Tr} \) 1, 2" justify?
2. Lines 1 \( u < 3 \) and 2 \( 4 < v \) are given. Is "\( u < v \) — \( \mathrm{Tr} \) 1, 2" justified?
3. The premises are 1 \( 0 < x \), 2 \( x < 3 \), 3 \( 3 < y \). Is "4. \( 0 < y \) — \( \mathrm{Tr} \) 1, 3" justified?
4. Write \( 0 < \tfrac14 < \tfrac13 < \tfrac12 \) as a derivation of \( 0 < \tfrac12 \) from its three links with \( \mathrm{Tr} \).
5. In the list "1 \( 0 < 1 \), premise; 2 \( 1 < 2 \), premise; 3 \( 0 < 2 \) — \( \mathrm{Tr} \) 2, 1", which of the three questions of "Reading a derivation" fails?
6. May \( \rulename{\wedge E} \) be applied to the line \( \neg P \wedge Q \)?
7. Lines 1 \( P \wedge (Q \wedge R) \), 2 \( S \) and 3 \( Q \wedge R \) (\( \rulename{\wedge E} \) 1) are given. Which of the following can be line 4? (i) \( (Q \wedge R) \wedge S \), \( \rulename{\wedge I} \) 3, 2; (ii) \( Q \wedge S \), \( \rulename{\wedge I} \) 3, 2; (iii) \( R \), \( \rulename{\wedge E} \) 1; (iv) \( R \), \( \rulename{\wedge E} \) 3.
8. Derive \( P \wedge Q, \ R \vdash R \wedge P \).
9. Derive \( (P \wedge Q) \wedge R \vdash Q \).
10. Derive \( P \wedge Q, \ R \wedge S \vdash S \wedge P \).
11. Fill in the Givens/Goal table for \( P \wedge (Q \wedge R) \vdash R \), one row per step.
12. Line 1 is \( (P \wedge Q) \wedge (R \wedge S) \). List every statement \( \rulename{\wedge E} \) can write from line 1 in one step.
:::
:::

::: {.solution}
(a) \( 2 < z \), with \( a \), \( b \), \( c \) replaced by \( 2 \), \( y \), \( z \).

(b) No: the middles \( 3 \) and \( 4 \) differ, so the lines are no instance of \( \mathrm{Tr} \), although \( u < v \) does follow (since \( 3 < 4 \)).

(c) No: line 1 makes \( b \) the expression \( x \), and line 3 makes it \( 3 \).

(d) Premises 1 \( 0 < \tfrac14 \), 2 \( \tfrac14 < \tfrac13 \), 3 \( \tfrac13 < \tfrac12 \); then 4 \( 0 < \tfrac13 \), \( \mathrm{Tr} \) 1, 2; 5 \( 0 < \tfrac12 \), \( \mathrm{Tr} \) 4, 3.

(e) The second: citing line 2 first makes \( b \) be \( 2 \) (from line 2, as \( a < b \)) and \( 0 \) (from line 1, as \( b < c \)). The rule is named and the cited lines are earlier.

(f) Yes: \( \neg \) binds most tightly, so the main connective is \( \wedge \), and \( \rulename{\wedge E} \) writes \( \neg P \) or \( Q \).

(g) (i) Yes. (ii) No: \( \rulename{\wedge I} \) joins the two cited lines whole, and line 3 is \( Q \wedge R \), not \( Q \). (iii) No: \( R \) lies a layer deeper in line 1. (iv) Yes.

(h) 3 \( P \), \( \rulename{\wedge E} \) 1; 4 \( R \wedge P \), \( \rulename{\wedge I} \) 2, 3.

(i) 2 \( P \wedge Q \), \( \rulename{\wedge E} \) 1; 3 \( Q \), \( \rulename{\wedge E} \) 2.

(j) 3 \( P \), \( \rulename{\wedge E} \) 1; 4 \( S \), \( \rulename{\wedge E} \) 2; 5 \( S \wedge P \), \( \rulename{\wedge I} \) 4, 3.

(k)

| Givens | Goal |
|---|---|
| \( P \wedge (Q \wedge R) \) | \( R \) |
| \( P \wedge (Q \wedge R) \), \( P \), \( Q \wedge R \) (\( \rulename{\wedge E} \)) | \( R \) |
| \( P \wedge (Q \wedge R) \), \( P \), \( Q \wedge R \), \( Q \), \( R \) (\( \rulename{\wedge E} \)) | \( R \) \( \checkmark \) |

(l) \( P \wedge Q \) and \( R \wedge S \) only.
:::

### B. Practice

::: {#exr-derivations-b1}
[B1: The other grouping]

Give a derivation of \( P \wedge (Q \wedge R) \vdash (P \wedge Q) \wedge R \). For each line, say whether you found it from the goal or from the premise.
:::

::: {.solution}
From the goal: \( \rulename{\wedge I} \) with subgoals \( P \wedge Q \) and \( R \), and \( P \wedge Q \) by \( \rulename{\wedge I} \) from \( P \) and \( Q \). From the premise: \( \rulename{\wedge E} \) gives \( P \) and \( Q \wedge R \), and \( \rulename{\wedge E} \) on \( Q \wedge R \) gives \( Q \) and \( R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \wedge R} \ae{1}
  \have {4} {Q} \ae{3}
  \have {5} {R} \ae{3}
  \have {6} {P \wedge Q} \ai{2,4}
  \have {7} {(P \wedge Q) \wedge R} \ai{6,5}
\end{nd}$
\end{center}
```

Lines 2–5 were found from the premise, lines 6–7 from the goal. With @prp-and-associative, each of \( (P \wedge Q) \wedge R \) and \( P \wedge (Q \wedge R) \) is derivable from the other.
:::

::: {#exr-derivations-b2}
[B2: Annotating a proof]

Let \( x \) and \( y \) be real numbers. Here is a proof.

> Let \( 1 < x < 2 \) and \( 3 < y < 4 \). Then \( 4 < x + y < 6 \).

Write out the proof in full, naming each use of \( \rulename{\wedge E} \) and \( \rulename{\wedge I} \), and marking the steps that are school algebra rather than logic.
:::

::: {.solution}
The hypotheses are the conjunctions \( (1 < x) \wedge (x < 2) \) and \( (3 < y) \wedge (y < 4) \), and the goal is \( (4 < x + y) \wedge (x + y < 6) \).

By \( \rulename{\wedge E} \), four times, we have \( 1 < x \), \( x < 2 \), \( 3 < y \), and \( y < 4 \) separately. Adding \( 1 < x \) and \( 3 < y \) gives \( 1 + 3 < x + y \), that is, \( 4 < x + y \) (school algebra: two inequalities in the same direction may be added). Adding \( x < 2 \) and \( y < 4 \) gives \( x + y < 6 \) (school algebra again). Finally \( \rulename{\wedge I} \) joins \( 4 < x + y \) and \( x + y < 6 \) into \( 4 < x + y < 6 \).

As a derivation it has the same shape as the one in @exm-product-in-unit-interval: two premises, four \( \rulename{\wedge E} \) lines, two lines justified "algebra", and one \( \rulename{\wedge I} \) line.
:::

::: {#exr-derivations-b3}
[B3: Two layers, then rebuild]

A search for \( P \wedge (Q \wedge R), \ S \vdash (R \wedge P) \wedge S \) has reached the stage below. *Name the move, then complete it.*

```{=latex}
% schema (partial derivation: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \hypo {2} {S}
  \have[\ ][0] {} {\vdots}
  \have[][7] {7} {(R \wedge P) \wedge S} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The move is *work from both ends* ("Two directions of reasoning"). From the goal: its main connective is \( \wedge \), so line 7 is \( \rulename{\wedge I} \) with the subgoals \( R \wedge P \) and \( S \); \( S \) is line 2, and \( R \wedge P \) splits again, by \( \rulename{\wedge I} \), into \( R \) and \( P \). From the premise: \( \rulename{\wedge E} \) in two layers, first \( P \) and \( Q \wedge R \) from line 1, then \( R \) from \( Q \wedge R \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \hypo {2} {S}
  \have {3} {P} \ae{1}
  \have {4} {Q \wedge R} \ae{1}
  \have {5} {R} \ae{4}
  \have {6} {R \wedge P} \ai{5,3}
  \have {7} {(R \wedge P) \wedge S} \ai{6,2}
\end{nd}$
\end{center}
```

The ends meet at line 6: the subgoals \( R \) and \( P \) are lines 5 and 3, which the premise supplied.
:::

### C. Going deeper

::: {#exr-derivations-c1}
[C1: A bad rule]

Add to \( \mathrm{Tr} \) a second rule, \( \mathrm{Flip} \): from \( a < b \), write \( b < a \).

::: {.enumerate options="label=(\alph*)"}
1. Derive \( 1 < 0 \) from the premise \( 0 < 1 \), using \( \mathrm{Flip} \).
2. Explain why a checker following "Reading a derivation" would accept your derivation.
3. What property does \( \mathrm{Tr} \) have that \( \mathrm{Flip} \) lacks?
:::
:::

::: {.solution}
(a)
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {0 < 1}
  \have {2} {1 < 0} \by{Flip}{1}
\end{nd}$
\end{center}
```

(b) Line 1 is a premise. Line 2 names a rule on the list, cites line 1, which is earlier, and lines 1, 2 are an instance of the schema of \( \mathrm{Flip} \) with \( a \) replaced by \( 0 \) and \( b \) by \( 1 \). All three questions pass. The checker never asks whether a line is true, only whether it matches a rule, so a bad rule is invisible to it.

(c) \( \mathrm{Tr} \) never leads from true lines to a false one (A1(e)). \( \mathrm{Flip} \) does: from the true line \( 0 < 1 \) it writes the false line \( 1 < 0 \). With such a rule, a derivation from true premises could end anywhere, so checking is only as good as the rules checked against. The rules of logic are chosen to have it; this section's Looking-ahead box says where that is checked.
:::

::: {#exr-derivations-c2}
[C2: Find the error]

A student offers the following list as a derivation of \( 0 < 4 \) with \( \mathrm{Tr} \).

```{=latex}
\begin{center}
% Deliberately invalid: line 5 cites line 6, a later line, written as literal text (see the
% comment at exm-not-a-derivation); no expect-invalid marker, since check_fitch cannot see it.
$\begin{nd}
  \hypo {1} {0 < 1}
  \hypo {2} {1 < 2}
  \hypo {3} {2 < 3}
  \hypo {4} {3 < 4}
  \have {5} {0 < 3} \by{Tr\ 6, 3}{}
  \have {6} {0 < 2} \by{Tr}{1,2}
  \have {7} {0 < 4} \by{Tr}{5,4}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Is \( 0 < 1, \ 1 < 2, \ 2 < 3, \ 3 < 4 \vdash 0 < 4 \) with \( \mathrm{Tr} \)?
2. Is the list a derivation? If not, name the line that fails and the clause of @def-box-free-derivation it breaks.
3. *(Challenge.)* The two lines "1. \( 0 < 0 \), \( \mathrm{Tr} \ 2, 2 \)" and "2. \( 0 < 0 \), \( \mathrm{Tr} \ 1, 1 \)" would each pass the first two questions of "Reading a derivation". Use them to explain why a line may cite only earlier lines.
:::
:::

::: {.solution}
(a) Yes. Swap lines 5 and 6 and renumber:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {0 < 1}
  \hypo {2} {1 < 2}
  \hypo {3} {2 < 3}
  \hypo {4} {3 < 4}
  \have {5} {0 < 2} \by{Tr}{1,2}
  \have {6} {0 < 3} \by{Tr}{5,3}
  \have {7} {0 < 4} \by{Tr}{6,4}
\end{nd}$
\end{center}
```

Each later line cites earlier lines and is an instance of \( \mathrm{Tr} \), with middles \( 1 \), \( 2 \), \( 3 \). So the student's conclusion is derivable (and true).

(b) No. Line 5 cites line 6, which is not earlier, so clause (ii) fails at line 5. Every line is an instance of \( \mathrm{Tr} \): lines 6, 3, 5 with middle \( 2 \); lines 1, 2, 6 with middle \( 1 \); lines 5, 4, 7 with middle \( 3 \). So the only fault is the order. That the conclusion is true and derivable does not repair the list: a derivation must meet the definition line by line.

(c) Line 1 cites line 2 twice, and line 2 cites line 1 twice. Each is an instance of \( \mathrm{Tr} \) with \( a \), \( b \), \( c \) all replaced by \( 0 \): from \( 0 < 0 \) and \( 0 < 0 \), write \( 0 < 0 \). So if lines could cite later lines, these two lines would justify each other, in a loop that rests on no premise, and the false statement \( 0 < 0 \) would be derivable from nothing. Requiring cited lines to be earlier rules out every such loop: following the citations backwards from any line, the numbers go down, so they must end, and they can end only at premises.

**Marking scheme.** (10 points)
- 3: says the conclusion is derivable and gives a correct derivation (every line an instance, every citation earlier).
- 3: names line 5 as the faulty line and the broken clause: a cited line must be earlier.
- 1: notes that the other lines are instances of \( \mathrm{Tr} \), so the order is the only fault.
- 3: explains with the loop why later citations cannot be allowed: the two lines justify each other, rest on no premise, and give a false line.
Fatal errors (0 for the step): calling the list a derivation because its conclusion is true; blaming line 7, which cites line 5, an earlier line.
:::

::: {#exr-derivations-c3}
[C3: A shortcut through two layers]

A student offers the following derivation of \( P \wedge (Q \wedge R) \vdash Q \wedge P \).

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (and-E through two layers)
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {Q} \ae{1}
  \have {3} {P} \ae{1}
  \have {4} {Q \wedge P} \ai{2,3}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Is line 2 an instance of a schema of \( \rulename{\wedge E} \)? Justify your answer.
2. Is the conclusion derivable from the premise? Justify your answer.
3. The step at line 2 never leads from a true line to a false one. Why must a checker still reject it?
4. *(Challenge.)* State, as a schema, a rule \( \wedge\mathrm{E}^{*} \) that would allow line 2. Show that every use of \( \wedge\mathrm{E}^{*} \) in a derivation can be replaced by two uses of \( \rulename{\wedge E} \).
:::
:::

::: {.solution}
(a) No. To match line 1 with \( \varphi \wedge \psi \), we must read \( \varphi \) and \( \psi \) off line 1's main connective, which is the first \( \wedge \): \( \varphi \) is \( P \) and \( \psi \) is \( Q \wedge R \). So \( \rulename{\wedge E} \) writes \( P \) or \( Q \wedge R \), and \( Q \) is neither.

(b) Yes. Insert the missing layer.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \wedge R} \ae{1}
  \have {4} {Q} \ae{3}
  \have {5} {Q \wedge P} \ai{4,2}
\end{nd}$
\end{center}
```

(c) A derivation is checked by matching each line against the schemas of the rules on the list, and line 2 matches none. A checker that also accepted steps that "obviously follow" would need to understand the statements, and then its verdict would be only as reliable as that understanding. The steps that seem obvious are the ones nobody looks at twice, and they are where unnoticed errors live. (This item is not a find-the-error exercise in the usual sense: the step has no counterexample, since it never leads from truth to falsehood. It is simply not a step of this calculus.)

(d) One such rule, in schema form:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi \wedge (\psi \wedge \chi)}
  \have {k} {\psi} \by{$\wedge$E$^{*}$}{i}
\end{nd}$
\end{center}
```

Suppose line \( k \) of a derivation is \( \psi \), justified "\( \wedge\mathrm{E}^{*} \) \( i \)", with line \( i \) the statement \( \varphi \wedge (\psi \wedge \chi) \). Replace line \( k \) by two lines: first \( \psi \wedge \chi \), justified \( \rulename{\wedge E} \) \( i \) (the second form, with the conjuncts \( \varphi \) and \( \psi \wedge \chi \)), then \( \psi \), justified by \( \rulename{\wedge E} \) citing that new line (the first form, with the conjuncts \( \psi \) and \( \chi \)). Renumber the later lines, and every citation of them, up by one; a later citation of line \( k \) now cites the second new line, which carries the same statement \( \psi \). Every other line is unchanged and still cites earlier lines. Doing this for each \( \wedge\mathrm{E}^{*} \) line, one at a time, gives a derivation with the same premises and last line that uses only \( \rulename{\wedge E} \) and \( \rulename{\wedge I} \). A rule that can always be replaced in this way adds convenience and no new power; Section 2.3 calls such a rule a derived rule.

**Marking scheme.** (10 points)

- 2: (a) no, reading \( \varphi \) and \( \psi \) off the main connective of line 1.
- 2: (b) yes, with a correct derivation.
- 2: (c) checking is by matching the schemas; a step that is not an instance is rejected, whether or not it is true.
- 2: (d) a correct schema, one given line and one new line.
- 2: (d) the replacement by two \( \rulename{\wedge E} \) lines, with the renumbering of later citations.

Fatal errors (0 for the step): claiming the conclusion is not derivable; offering a counterexample to line 2.
:::

::: {#exr-derivations-c4}
[C4: Challenge: What conjunction cannot do]

Show that no box-free derivation whose only premise is \( P \wedge Q \), and whose only rules are \( \rulename{\wedge I} \) and \( \rulename{\wedge E} \), has a line whose statement contains the letter \( R \). Deduce that, with these two rules, \( P \wedge Q \vdash P \wedge R \) cannot be shown.
:::

::: {.solution}
[Hint 1]

Suppose some line does contain \( R \), and look at the **first** such line.
:::

::: {.solution}
[Hint 2]

That first line is not a premise. Which rule wrote it, and which letters can that rule write?
:::

::: {.solution}
Suppose, for a contradiction, that some line of such a derivation contains \( R \). The derivation has finitely many lines, so there is a first such line; call it line \( k \). Every line before line \( k \) is free of \( R \).

Line \( k \) is not a premise, because every premise is \( P \wedge Q \), which does not contain \( R \). So line \( k \) is justified by one of the two rules, citing earlier lines (@def-box-free-derivation).

If it is \( \rulename{\wedge I} \), citing lines \( i \) and \( j \), then its statement is \( \varphi \wedge \psi \), where \( \varphi \) and \( \psi \) are the statements of lines \( i \) and \( j \). Both are earlier than \( k \), so neither contains \( R \), and neither does \( \varphi \wedge \psi \).

If it is \( \rulename{\wedge E} \), citing line \( i \), then its statement is one conjunct of the statement of line \( i \): a part of it. Line \( i \) is earlier than \( k \) and free of \( R \), so the part is free of \( R \) too.

Either way line \( k \) does not contain \( R \), which contradicts the choice of \( k \). So no line contains \( R \). In particular no such derivation has the last line \( P \wedge R \), and \( P \wedge Q \vdash P \wedge R \) cannot be shown with these rules.

The argument, "look at the first bad line; it cannot be a premise, and no rule can create it from good lines", is an induction on the lines of a derivation; Chapter 3 makes such arguments exact.

**Marking scheme.** (10 points)

- 2: considers a first line containing \( R \), and says why a first one exists (finitely many lines); or, equally, goes down the derivation line by line, showing each line free of \( R \) because every line it cites is.
- 2: rules out a premise.
- 2: \( \rulename{\wedge I} \) case: the new line is built from the statements of two earlier, \( R \)-free lines.
- 2: \( \rulename{\wedge E} \) case: the new line is part of an earlier, \( R \)-free line.
- 2: concludes that no line contains \( R \), and so that \( P \wedge R \) is never a last line.

Fatal errors (0 for the step): arguing about one particular derivation instead of every derivation; arguing that \( R \) is "not true" instead of about which symbols the rules can write.
:::

<!-- dependency ledger
def-rule-schema (example): Tr is a true fact about < on the real numbers (transitivity) | school algebra, used as a toy rule by the blueprint's design; AN1.1 (promised)
def-rule-schema (example): 2/4 = 1/2 | inline arithmetic
def-rule-schema (example): the analogy (a + b)^2 = a^2 + 2ab + b^2 | school algebra, used only as an illustration of a pattern
exm-chaining-derivation (example): none beyond the toy rule Tr | inline; checked by verify/ch01/exm-chaining-derivation.py
exm-derivations (solution): every rule met before boxes cites at least one line (and-I, and-E, ->E) | and-I, and-E in this section; ->E in the next section (stated as a meta-claim, not used in a proof; blueprint ch01.md, Rule system)
exm-not-a-derivation (solution): the instance and earlier-line claims for both changes | inline; checked by verify/ch01/exm-not-a-derivation.py
exm-product-in-unit-interval (solution): a product of two positive reals is positive; multiplying an inequality by a positive number keeps its direction; transitivity of < | school algebra (blueprint, Allowed prerequisites) -> AN1.1 (promised); checked by verify/ch01/exm-product-in-unit-interval.py
exm-product-in-unit-interval (example): 0 < 1/(n+1) < 1/n <= 1 for integers n >= 1; from a < b and b <= c infer a < c | school algebra; AN1.1 (promised)
def-rules-conjunction (example): the Common-errors warning's instance: (x > 0 and x > 1) implies x^2 > 1 for every real x, and x > 0 fails at x = -1 | school algebra -> AN1.1 (promised); checked by verify/ch01/exm-product-in-unit-interval.py
def-rules-conjunction (claim): the safety sentence (if phi and psi are true so is phi and psi; if phi and psi is true so is each side) | the reading of "and" in the first section, stated, not used as a reason in a proof; the general proof is the Looking-ahead box's promise
exr-derivations-a1 (solution): Tr leads from true lines to a true line; going down the derivation line by line is an induction | school algebra, AN1.1 (promised); the induction is F1.3 (promised)
exr-derivations-a2 (solution): 0 < 1/4 < 1/3 < 1/2; 3 < 4; the precedence convention (not binds most tightly) | inline arithmetic, checked by verify/ch01/exr-derivations-a2.py; F1.1 (the precedence conventions, before def-main-connective), recalled in prose
exr-derivations-b2 (solution): two inequalities in the same direction may be added | school algebra -> AN1.1 (promised); checked by verify/ch01/exm-product-in-unit-interval.py
exr-derivations-c1 (solution): 0 < 1 is true and 1 < 0 is false | inline arithmetic
exr-derivations-c2 (solution): following citations backwards the line numbers strictly decrease, so the chain of citations ends | inline: the numbers lie among 1, ..., n, so a strictly decreasing chain of them has at most n terms
exr-derivations-c3 (solution): if P and (Q and R) is true then Q and R is true, and then Q is true, so the and-E-through-two-layers step never leads from truth to falsehood | the reading of "and" in Section 1.1 (the safety sentence, as for def-rules-conjunction (claim)), applied twice; stated, not used as a reason in a proof
exr-derivations-c4 (solution): a finite non-empty set of line numbers has a first element (least-number principle, "first bad line") | school fact about finite lists; induction (F1.3) named in prose as the exact version, not used
-->
