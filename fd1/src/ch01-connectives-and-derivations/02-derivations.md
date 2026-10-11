# Derivations: Premises, Lines and Justifications

The previous section stated a slogan: a proof is a chain in which every line is a premise, an assumption, or one application of a rule. This section makes part of that slogan exact, the premises and the lines that apply a rule; assumptions wait until Section 1.5. It says what such a chain looks like on the page, how each line carries its reason, and how anyone can check the chain without understanding its subject. It introduces no rule of logic. Its only rules are two facts about inequalities, borrowed for practice, so that the **format** of a derivation can be learned on its own.

## Checking a chain without understanding it

Here is a chain of inequalities between fractions:
\[
0 < \tfrac{1}{3} < \tfrac{1}{2} < 1 .
\]
It is read as three claims, \( 0 < \tfrac13 \), \( \tfrac13 < \tfrac12 \), and \( \tfrac12 < 1 \), and a reader who accepts them concludes \( 0 < 1 \). What justifies that conclusion? Not a picture of the number line, and not a feeling that the numbers go up. The justification is one fact, used twice:

> if \( a < b \) and \( b < c \), then \( a < c \).

From \( 0 < \tfrac13 \) and \( \tfrac13 < \tfrac12 \) it gives \( 0 < \tfrac12 \). From \( 0 < \tfrac12 \) and \( \tfrac12 < 1 \) it gives \( 0 < 1 \).

What must a reader know to check those two steps? Nothing about fractions, and nothing about what \( < \) means. It is enough to see that the two inequalities used in each step have the **same** expression in the middle, and that the new inequality joins the outer two. A clerk who had never seen a number could do it, provided the clerk can compare symbols. That is the sense in which a proof can be checked without being understood: a proof is correct when every step matches its pattern, and matching is mechanical.

The rest of this section writes such chains in the format that the whole of Part 0 uses, with every reason on the page. Everything here is about the format. The logic starts in Section 1.3.

## Two rules about numbers, for practice

We borrow two facts about real numbers and use them as rules. Every reader knows them, so attention can go entirely to the format.

- **Tr** (for "transitivity", or chaining): from \( a < b \) and \( b < c \), write \( a < c \).
- **Sh** (for "shift"): from \( a < b \), write \( a + c < b + c \), for any number \( c \).

These are facts about numbers, not rules of logic. They are used as rules in this section and its exercises only. When a later proof adds \( 1 \) to both sides of an inequality, that is a step of school algebra, and Chapter 11 proves the facts behind such steps from the axioms for the real numbers.

## Rule schemas

A rule is applied by matching, and to match we need something to match against. That something is a small picture of the lines the rule needs and the line it writes.

*A rule is a pattern: given these lines, you may write that line.*

::: {#def-rule-schema}
[Rule Schema]

A **rule schema** is a pattern of lines: **given** lines and boxes at the top, possibly none, and exactly **one new** line at the bottom, whose justification names the rule and cites the given lines and boxes. Line numbers in a schema are written \( i, j, k \). The letters in the pattern stand for arbitrary **expressions** of the right kind, and a use of the rule replaces them **consistently**: the same letter by the same expression, **symbol for symbol**, everywhere it occurs. A line is **justified by the rule** when it and the lines it cites, with their numbers, are an **instance** of a schema of the rule: the pattern with every letter replaced in this way. The schema of \( \mathrm{Tr} \) is

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

In words, clause by clause.

- *Given lines at the top, one new line at the bottom.* The schema of \( \mathrm{Tr} \) has two given lines, \( i \) and \( j \), and one new line, \( k \). The given lines may sit anywhere above line \( k \), in either order, and need not be next to each other or to line \( k \). The drawing puts them together only because a drawing has to put them somewhere.
- *The justification cites the given lines.* "\( \mathrm{Tr} \ i, j \)" says that line \( i \) plays the part \( a < b \) and line \( j \) plays the part \( b < c \). The **order** of the citation assigns the parts, not the order of the lines on the page.
- *Letters are replaced consistently, symbol for symbol.* The middle letter \( b \) occurs in both given lines, so it must be replaced by the **same** expression in both: the same string of symbols, not merely the same number. This is the clause a careless step breaks.
- *Nothing else is required.* There is no condition on what the expressions mean, how large they are, or whether the given lines are true.

An instance first. Take \( i = 3 \), \( j = 5 \), \( k = 6 \), and replace \( a \) by \( 0 \), \( b \) by \( \tfrac12 \), and \( c \) by \( 1 \). The pattern becomes: line 3 is \( 0 < \tfrac12 \), line 5 is \( \tfrac12 < 1 \), and line 6 is \( 0 < 1 \), justified "\( \mathrm{Tr} \ 3, 5 \)". So if lines 3 and 5 of some list say exactly those things, line 6 may say \( 0 < 1 \) with that justification.

Now a noninstance, by a minimal change. Keep line 3 as \( 0 < \tfrac12 \), and let line 5 be \( \tfrac13 < 1 \). Is "6. \( 0 < 1 \), \( \mathrm{Tr} \ 3, 5 \)" justified? Line 3 forces \( b \) to be \( \tfrac12 \), and line 5 forces \( b \) to be \( \tfrac13 \). The letter \( b \) cannot be both, so these lines are not an instance of the schema. Line 6 is true, but \( \mathrm{Tr} \) was not applied, so the line has no justification.

The schema of \( \mathrm{Sh} \) has one given line:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {a < b}
  \have {k} {a + c < b + c} \by{Sh}{i}
\end{nd}$
\end{center}
```

Its letter \( c \) occurs only in the new line, so it may be replaced by **any** expression; consistency asks only that the **same** expression is added on both sides. From \( y < 5 \) the rule may write \( y + 1 < 5 + 1 \) or \( y + x < 5 + x \), but not \( y + 1 < 5 + 2 \). Nor does it write \( y + 1 < 6 \): that is a different string of symbols. A logical rule with a letter that occurs only in its new line appears in Section 1.6.

*Why define rules this way?* Because a rule applied by matching can be checked by someone who knows nothing about the subject. The schema turns "this step is obviously fine" into "this step matches that pattern", a claim anyone can test. Every rule of logic in the following sections is given in this form, and the definition was worded so that none of them needs a new one: Section 1.5 adds given **boxes**, cited as ranges of lines, and a rule of Chapter 4 has no given lines at all.

From the next section on, the letters in a schema are Greek: \( \varphi \), \( \psi \), \( \chi \) (phi, psi, chi) stand for arbitrary **statements**, just as \( a \), \( b \), \( c \) stand for expressions for numbers here. Replacing them works the same way, with parentheses put around a compound statement where it is needed. For example, if a schema has the given lines \( \varphi \) and \( \psi \) and the new line \( \varphi \wedge \psi \), then the three lines \( P \to Q \), \( R \), and \( (P \to Q) \wedge R \) are an instance of it, with \( \varphi \) replaced by \( P \to Q \) and \( \psi \) by \( R \).

::: {.warning}
The middle expression must match **exactly**, symbol for symbol. The step "\( 0 < \tfrac24 \) and \( \tfrac12 < 1 \), so \( 0 < 1 \)" is tempting, because \( \tfrac24 = \tfrac12 \) and every line in it is true, but it is not an application of \( \mathrm{Tr} \): the two middle expressions are different strings. A checker who had to notice that they are equal would need arithmetic, and the point of a schema is that a checker needs nothing. Compare symbols, not values.
:::

## Derivations without boxes

A single application of a rule is one step. A proof strings steps together, and each step may use what earlier steps produced. The next definition says exactly how.

::: {#def-box-free-derivation}
[Box-Free Derivation]

Fix a list of rules, each given by schemas. A **box-free derivation** is a finite list of numbered lines \( 1, 2, \dots, n \), where \( n \ge 1 \), each carrying one statement and a justification, such that:

::: {.enumerate options="label=(\roman*)"}
1. the first lines, possibly none and possibly all, are **premises**, justified by nothing; a short horizontal rule is drawn under the last premise;
2. every later line is justified by **one** rule of the list, citing **earlier** lines, and it and the cited lines form an instance of a schema of that rule.
:::

The **premises** of the derivation are its premise lines, and its **conclusion** is its last line.
:::

In words. Clause (i) says where a derivation starts: with the statements it is given. They are not proved, and they need no reason; they are the assumptions the whole derivation works under. Clause (ii) says how it goes on: each further line is one step of one rule, and the only lines it may use are ones already written. The word "earlier" is the only condition on which lines may be cited **for now**. Section 1.5 adds assumptions made inside boxes, and then "earlier" is refined to "available": an earlier line may become unusable once the box it sits in has closed.

The layout is always the same. Line numbers run down the left, statements sit in the middle, and each justification is on the right: the rule's name, then the cited line numbers, in the order the schema assigns them. A vertical bar runs down the left of the statements, and a short horizontal rule under the last premise separates what is given from what is derived. The bar does no work yet. From Section 1.5 on, a box draws a second, shorter bar, and the bars beside a line show which assumptions it depends on.

The degenerate case is worth a look. A single premise line, with nothing after it, satisfies both clauses: clause (i) holds, and clause (ii) has no lines to speak about. So it is a derivation, and its premise is its conclusion.

## First derivations

Here are three derivations with \( \mathrm{Tr} \), each with the reasoning that found it. The reasoning is the part to watch: a derivation on the page runs from the top down, but it is rarely found that way.

::: {#exm-chaining-derivation}
[Chaining]

Let \( x \), \( y \), \( u \), \( v \), \( w \), \( z \) be real numbers. Using the rule \( \mathrm{Tr} \) only, write a box-free derivation of each conclusion from the given premises.

::: {.enumerate options="label=(\alph*)"}
1. Premises \( 0 < x \), \( x < y \), \( y < 1 \); conclusion \( 0 < 1 \).
2. The same premises in the order \( y < 1 \), \( 0 < x \), \( x < y \); the same conclusion.
3. Premises \( u < v \), \( w < z \), \( v < w \); conclusion \( u < z \).
:::
:::

::: {.solution}
**(a)** *Idea.* The premises form a chain \( 0 < x < y < 1 \), in which each link shares its right end with the next link's left end. So we work **forwards**, from what we have: chain the first two links at their shared middle \( x \), then chain the result with the third link at the shared middle \( y \).

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

Read it back line by line. Lines 1–3 are the premises. Line 4 says: lines 1 and 2 are an instance of \( \mathrm{Tr} \), line 1 as \( a < b \) and line 2 as \( b < c \), with \( a \), \( b \), \( c \) replaced by \( 0 \), \( x \), \( y \); so we may write \( 0 < y \). Line 5 says the same of lines 4 and 3, with \( a \), \( b \), \( c \) replaced by \( 0 \), \( y \), \( 1 \). The letters are replaced afresh at each use: the \( b \) of line 4 has nothing to do with the \( b \) of line 5.

**(b)** *Idea.* The same chain, found the same way. Only the line numbers change.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {y < 1}
  \hypo {2} {0 < x}
  \hypo {3} {x < y}
  \have {4} {0 < y} \by{Tr}{2,3}
  \have {5} {0 < 1} \by{Tr}{4,1}
\end{nd}$
\end{center}
```

Line 5 is justified "\( \mathrm{Tr} \ 4, 1 \)": line 4 is cited first because it plays the part \( a < b \), although line 1 comes first on the page. The justification, not the position, says which line plays which part.

**(c)** *Idea.* This time the chain is scrambled, so we work **backwards**, from what we want. The goal \( u < z \) can come from \( \mathrm{Tr} \) only if we have some \( u < m \) and \( m < z \) for a single expression \( m \). Which \( m \)? The only premise starting with \( u \) is \( u < v \), so try \( m = v \). Then \( u < v \) is a premise, and the remaining need is \( v < z \): a new, smaller goal. Ask the same question of it. It can come from \( \mathrm{Tr} \) with some \( v < m' \) and \( m' < z \); the only premise starting with \( v \) is \( v < w \), and with \( m' = w \) the second need, \( w < z \), is a premise too. The search has reached the premises, and the derivation is its record, written **forwards**.

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

The search could have started instead from \( w < z \), the premise ending in \( z \): with \( m = w \) it needs \( u < w \), which is \( \mathrm{Tr} \ 1, 3 \), and then \( u < z \) is \( \mathrm{Tr} \ 4, 2 \). That is a different correct derivation. A sequent usually has many, and any one of them establishes it.
:::

Part (c) is the first goal-directed search in the book: we asked what the goal needs, turned the need into smaller goals, and stopped when every goal was a premise. Parts (a) and (b) went forwards from the premises instead. From Section 1.3 on, the Ideas do both with the rules of logic, and name the two directions.

::: {.check}
Line 1 of a derivation is \( 0 < x \) and line 3 is \( x < 1 \). Which is correct: "4. \( 0 < 1 \), \( \mathrm{Tr} \ 1, 3 \)" or "4. \( 0 < 1 \), \( \mathrm{Tr} \ 3, 1 \)"?
:::

::: {.solution}
The first. With the citation "1, 3", line 1 plays \( a < b \) and line 3 plays \( b < c \): \( a \) is \( 0 \), \( b \) is \( x \) in both lines, and \( c \) is \( 1 \), so the new line \( a < c \) is \( 0 < 1 \). With "3, 1", line 3 would play \( a < b \) and line 1 would play \( b < c \), so \( b \) would have to be \( 1 \) (from line 3) and \( 0 \) (from line 1) at once.
:::

## What a derivation proves

A derivation shows that its conclusion follows from its premises. This is exactly what the sequent of @def-sequent claimed, so the claim can now be made exact.

::: {#def-derivable}
[Derivable]

Let \( \Gamma \) be a list of statements \( \varphi_1, \dots, \varphi_n \), where \( n \ge 0 \), and let \( \psi \) be a statement. We say \( \psi \) is **derivable** from \( \Gamma \), and write
\[
\Gamma \vdash \psi ,
\]
if **there is** a derivation, using the rules of logic, whose premises **all belong to** \( \Gamma \) and whose last line is \( \psi \). We write \( \varphi_1, \dots, \varphi_n \vdash \psi \) for \( \Gamma \vdash \psi \), and \( \vdash \psi \) when \( \Gamma \) is empty.
:::

In words, four remarks.

1. *The sequent is now an exact claim.* \( \varphi_1, \dots, \varphi_n \vdash \psi \) is the sequent of @def-sequent, and it holds exactly when a derivation of the required kind exists. It is proved by exhibiting one.
2. *Which derivations?* Until Section 1.5, "derivation" means a box-free derivation (@def-box-free-derivation). Section 1.5 widens the word to allow boxes, and the definition is then read with the wider notion. Nothing proved before changes: a box-free derivation is still a derivation.
3. *Not every premise must be used.* A derivation may ignore some statements of \( \Gamma \), and it may even have no premise lines at all. It may not use a premise that is **not** in \( \Gamma \).
4. *Relative to a list of rules.* The symbol \( \vdash \) always refers to a list of rules. From Section 1.3 on, it is the rules of logic introduced so far; adding a rule never destroys a derivation, so a sequent once derived stays derived. Here there are no rules of logic yet, so we name the rules we mean: "\( \Gamma \vdash \psi \) **with** \( \mathrm{Tr} \)", or "with \( \mathrm{Tr} \) and \( \mathrm{Sh} \)".

For instance, part (a) of @exm-chaining-derivation shows \( 0 < x, \ x < y, \ y < 1 \vdash 0 < 1 \) with \( \mathrm{Tr} \).

In the derivations of the next sections, the capital letters \( P \), \( Q \), \( R \), \( S \) stand for arbitrary statements, as in Section 1.1. A derivation written with them proves not one sequent but infinitely many at once, one for each way of putting statements in for the letters. Chapter 3 makes this precise.

::: {.check}
What sequent "with \( \mathrm{Tr} \)" does part (c) of @exm-chaining-derivation show?
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

(b) No. The definition asks for \( n \ge 1 \) lines, and a derivation must have a last line to be its conclusion. So the empty list derives nothing. In the same way, a list with no premises can never get started with \( \mathrm{Tr} \), \( \mathrm{Sh} \), or any rule that cites at least one line: its first line would have to cite an earlier line, and there is none. Every rule met before Section 1.5 cites at least one line, so until then \( \vdash \psi \) holds for no \( \psi \). Section 1.5 changes that.

(c) Yes. Lines 1–3 are premises, with the rule drawn under line 3: clause (i). Line 4 cites lines 1 and 2, which are earlier, and lines 1, 2, 4 are an instance of \( \mathrm{Tr} \) with \( a \), \( b \), \( c \) replaced by \( 0 \), \( x \), \( y \). Line 5 cites lines 4 and 3, which are earlier, and lines 4, 3, 5 are an instance with \( a \), \( b \), \( c \) replaced by \( 0 \), \( y \), \( 1 \). So clause (ii) holds for both later lines. The premises are the three premise lines and the conclusion is \( 0 < 1 \).
:::

::: {.warning}
A premise is **given**, not proved. A derivation shows that its conclusion follows *from* its premises, and \( \Gamma \vdash \psi \) says nothing about whether the statements in \( \Gamma \) are true. From the false premises \( 1 < 0 \) and \( 0 < -1 \), the rule \( \mathrm{Tr} \) gives \( 1 < -1 \). That is a correct derivation with a false conclusion. What a correct derivation guarantees is conditional: **if** the premises are true, and the rules never lead from true lines to a false one, **then** the conclusion is true.
:::

## Reading a derivation

Finding a derivation may need an idea, as part (c) of @exm-chaining-derivation did. Checking one never does. For each line after the premises, ask three questions.

1. **Which rule?** Name the rule the justification cites, and check that it is on the list of rules.
2. **Do the cited lines and this line form an instance of that rule's schema?** Find the replacement of the letters: read it off the cited lines in the order the citation gives them, and check that every letter gets the same expression each time it occurs, and that the new line is what the pattern then says.
3. **Are the cited lines earlier?** Each cited number must be smaller than the number of the line doing the citing.

A line that passes all three is correct, whatever it says and whether or not it is true. Here is the check run on part (a) of @exm-chaining-derivation.

| Line | Rule | Cites | Instance (the letters' values) | Earlier? |
|---|---|---|---|---|
| 1–3 | premises | — | — | — |
| 4 | \( \mathrm{Tr} \) | 1, 2 | \( a \): \( 0 \); \( b \): \( x \); \( c \): \( y \) | 1, 2 < 4: yes |
| 5 | \( \mathrm{Tr} \) | 4, 3 | \( a \): \( 0 \); \( b \): \( y \); \( c \): \( 1 \) | 4, 3 < 5: yes |

Every line passes, so the list is a derivation. Section 1.5 extends this table, when "earlier" becomes "available".

*Finding a derivation may need an idea; checking one never does.*

A line can fail one question and pass the others. The next example breaks a correct derivation in two ways, each time with the smallest change that does it.

::: {#exm-not-a-derivation}
[Not a derivation]

Each list below is the derivation of part (a) of @exm-chaining-derivation with one change. Say which of the three questions of "Reading a derivation" fails, and at which line.

::: {.enumerate options="label=(\alph*)"}
1. The statements of lines 4 and 5 are swapped, and each keeps its justification.
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

## How this looks in a mathematical proof

A proof about sequences might contain the line
\[
0 < \frac{1}{n+1} < \frac{1}{n} \le 1 \qquad \text{for } n \in \nZ_{>0} .
\]
It asserts three links: \( 0 < \frac{1}{n+1} \), \( \frac{1}{n+1} < \frac1n \), and \( \frac1n \le 1 \). A reader who takes from it a claim about its two ends, \( 0 < 1 \), performs two steps in silence. The first is one application of chaining: \( 0 < \frac{1}{n+1} \) and \( \frac{1}{n+1} < \frac1n \) give \( 0 < \frac1n \). The second joins \( 0 < \frac1n \) with \( \frac1n \le 1 \), and it is **not** \( \mathrm{Tr} \): the line \( \frac1n \le 1 \) has \( \le \), not \( < \), so the lines do not match the schema. It is a different pattern, "from \( a < b \) and \( b \le c \), write \( a < c \)", another true fact about numbers. That is exactly why a justification must name the pattern it uses. "By the chain" does not say which one.

Written chains like this one are everywhere in analysis, and they are derivations with the justifications left off. Nobody writes the justifications out in a real proof about numbers. But a reader checking a hard chain does what the table of "Reading a derivation" does: for each step, which fact, applied to which earlier lines.

## Exercises

### A. Check your understanding

::: {#exr-derivations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of a box-free derivation, and of \( \Gamma \vdash \psi \).
2. Fill in the justifications of the following derivation, which uses \( \mathrm{Tr} \) and \( \mathrm{Sh} \).

   ```{=latex}
   % schema
   \begin{center}
   $\begin{nd}
     \hypo {1} {1 < x}
     \hypo {2} {x < y}
     \hypo {3} {y < 5}
     \have {4} {x < 5}
     \have {5} {1 < 5}
     \have {6} {1 + 2 < 5 + 2}
   \end{nd}$
   \end{center}
   ```

3. Is the following list a derivation with \( \mathrm{Tr} \) and \( \mathrm{Sh} \)? If not, name the line and the clause of @def-box-free-derivation that fails. "1. \( 0 < x \), premise. 2. \( x < 1 \), premise. 3. \( 0 + 1 < 1 + 1 \), \( \mathrm{Sh} \ 4 \). 4. \( 0 < 1 \), \( \mathrm{Tr} \ 1, 2 \)."
4. What sequent "with \( \mathrm{Tr} \) and \( \mathrm{Sh} \)" does the derivation of (b) show?
5. True or false, with a reason: if \( \Gamma \vdash \psi \) with \( \mathrm{Tr} \) and \( \mathrm{Sh} \), and every statement in \( \Gamma \) is true, then \( \psi \) is true.
:::
:::

::: {.solution}
(a) A box-free derivation, relative to a list of rules, is a finite list of numbered lines, at least one, each with a statement and a justification, in which the first lines are premises, justified by nothing, and every later line is justified by one rule of the list, citing earlier lines, so that it and the cited lines form an instance of a schema of that rule (@def-box-free-derivation). And \( \Gamma \vdash \psi \) means that there is a derivation whose premises all belong to \( \Gamma \) and whose last line is \( \psi \) (@def-derivable).

(b) Line 4: \( \mathrm{Tr} \ 2, 3 \), with \( a \), \( b \), \( c \) replaced by \( x \), \( y \), \( 5 \). Line 5: \( \mathrm{Tr} \ 1, 4 \), with \( a \), \( b \), \( c \) replaced by \( 1 \), \( x \), \( 5 \). Line 6: \( \mathrm{Sh} \ 5 \), with \( a \), \( b \) replaced by \( 1 \), \( 5 \) and \( c \) by \( 2 \). No other justification works: for line 5, the only earlier lines of the form \( 1 < \dots \) and \( \dots < 5 \) that share a middle are lines 1 and 4.

(c) No. Line 3 cites line 4, which is not earlier, so clause (ii) fails at line 3. Every line is an instance of its rule: lines 4, 3 form an instance of \( \mathrm{Sh} \) with \( c \) replaced by \( 1 \), and lines 1, 2, 4 an instance of \( \mathrm{Tr} \). The only fault is the order.

(d) \( 1 < x, \ x < y, \ y < 5 \vdash 1 + 2 < 5 + 2 \) with \( \mathrm{Tr} \) and \( \mathrm{Sh} \).

(e) True. Both rules lead from true lines to true lines: if \( a < b \) and \( b < c \) are true, so is \( a < c \), and if \( a < b \) is true, so is \( a + c < b + c \). Go down the derivation: the premises are in \( \Gamma \), so they are true, and each later line comes from earlier, true lines by one of the two rules, so it is true too. Hence the last line, \( \psi \), is true. This is soundness in miniature: Chapter 3 proves it for the rules of logic (@thm-soundness), and makes "go down the derivation" a proof by induction.
:::

### B. Practice

::: {#exr-derivations-b1}
[B1: Shift, then chain]

Let \( x \), \( y \), \( z \) be real numbers. Using \( \mathrm{Tr} \) and \( \mathrm{Sh} \), derive \( x + 1 < z \) from the premises \( x < y \) and \( y + 1 < z \). Remember that \( \mathrm{Sh} \) writes \( a + c < b + c \) literally: no simplification of an expression is a step of the derivation. Then say in one sentence how you found the step that uses \( \mathrm{Sh} \).
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {x < y}
  \hypo {2} {y + 1 < z}
  \have {3} {x + 1 < y + 1} \by{Sh}{1}
  \have {4} {x + 1 < z} \by{Tr}{3,2}
\end{nd}$
\end{center}
```

Line 3 is \( \mathrm{Sh} \) on line 1 with \( a \), \( b \), \( c \) replaced by \( x \), \( y \), \( 1 \). Line 4 is \( \mathrm{Tr} \) on lines 3 and 2 with \( a \), \( b \), \( c \) replaced by \( x + 1 \), \( y + 1 \), \( z \); the middle \( y + 1 \) is the same string in both cited lines.

The step was found backwards: the goal needs a middle expression, premise 2 ends in \( z \) and suggests \( y + 1 \), and the missing link \( x + 1 < y + 1 \) is premise 1 shifted by \( 1 \).
:::

::: {#exr-derivations-b2}
[B2: Instances]

A derivation begins with the premises
\[
1.\ \ 0 < x, \qquad 2.\ \ x < 3, \qquad 3.\ \ 3 < y .
\]
Determine which of the following candidate lines 4 are justified. Justify your answer: for each justified one, give the replacement of the letters; for each other one, say which clause of @def-rule-schema fails.

::: {.enumerate options="label=(\alph*)"}
1. \( 0 < 3 \), \( \mathrm{Tr} \ 1, 2 \).
2. \( x < y \), \( \mathrm{Tr} \ 2, 3 \).
3. \( 0 < y \), \( \mathrm{Tr} \ 1, 3 \).
4. \( 0 + 2 < x + 2 \), \( \mathrm{Sh} \ 1 \).
5. \( x + 1 < 3 + 2 \), \( \mathrm{Sh} \ 2 \).
6. \( x + y < 3 + y \), \( \mathrm{Sh} \ 2 \).
:::
:::

::: {.solution}
(a) Justified: \( a \), \( b \), \( c \) are \( 0 \), \( x \), \( 3 \).

(b) Justified: \( a \), \( b \), \( c \) are \( x \), \( 3 \), \( y \).

(c) Not justified. Line 1 makes \( b \) the expression \( x \), and line 3 makes it \( 3 \): the middle letter is not replaced consistently. The line can be derived in two steps (\( 0 < 3 \) by \( \mathrm{Tr} \ 1, 2 \), then \( 0 < y \) from that line and line 3), but not in this one.

(d) Justified: \( a \), \( b \), \( c \) are \( 0 \), \( x \), \( 2 \). The rule writes \( 0 + 2 \), not \( 2 \).

(e) Not justified. The left side forces \( c \) to be \( 1 \) and the right side forces \( c \) to be \( 2 \); the letter \( c \) is not replaced consistently. The statement \( x + 1 < 3 + 2 \) is even true whenever line 2 is, but \( \mathrm{Sh} \) does not write it.

(f) Justified: \( a \), \( b \), \( c \) are \( x \), \( 3 \), \( y \). The letter \( c \) may be replaced by any expression, including one with a letter in it.
:::

::: {#exr-derivations-b3}
[B3: How many steps a chain takes]

::: {.enumerate options="label=(\alph*)"}
1. Write the chain \( 0 < \tfrac14 < \tfrac13 < \tfrac12 \) as a derivation, with its three links as premises and the conclusion \( 0 < \tfrac12 \), using \( \mathrm{Tr} \), forwards from the first link as in part (a) of @exm-chaining-derivation.
2. A chain \( e_0 < e_1 < \dots < e_m \) has \( m \ge 1 \) links. Forward chaining, as in (a), writes the links as premises and then joins the first link with the next, again and again. How many applications of \( \mathrm{Tr} \) does it use to reach \( e_0 < e_m \)?
:::
:::

::: {.solution}
(a)
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {0 < \tfrac14}
  \hypo {2} {\tfrac14 < \tfrac13}
  \hypo {3} {\tfrac13 < \tfrac12}
  \have {4} {0 < \tfrac13} \by{Tr}{1,2}
  \have {5} {0 < \tfrac12} \by{Tr}{4,3}
\end{nd}$
\end{center}
```

(b) \( m - 1 \). Each application takes the line \( e_0 < e_k \) reached so far and the next link \( e_k < e_{k+1} \), and writes \( e_0 < e_{k+1} \), so it absorbs one more link. The first link needs no application, and each of the other \( m - 1 \) links needs one. In (a), \( m = 3 \) and there are \( 2 \) applications; when \( m = 1 \), the single premise is already the conclusion.

No cleverer derivation does better: every derivation of \( e_0 < e_m \) from the links with \( \mathrm{Tr} \) uses at least \( m - 1 \) applications. We do not prove this here; the proof is an induction, the method of Chapter 3 (@ax-induction), and nothing in the book depends on it.
:::

### C. Going deeper

::: {#exr-derivations-c1}
[C1: A bad rule]

Add to \( \mathrm{Tr} \) and \( \mathrm{Sh} \) a third rule, \( \mathrm{Flip} \): from \( a < b \), write \( b < a \).

::: {.enumerate options="label=(\alph*)"}
1. Derive \( 1 < 0 \) from the premise \( 0 < 1 \), using \( \mathrm{Flip} \).
2. Explain why a checker following "Reading a derivation" would accept your derivation.
3. What property do \( \mathrm{Tr} \) and \( \mathrm{Sh} \) have that \( \mathrm{Flip} \) lacks?
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

(c) \( \mathrm{Tr} \) and \( \mathrm{Sh} \) never lead from true lines to a false one (A1(e)). \( \mathrm{Flip} \) does: from the true line \( 0 < 1 \) it writes the false line \( 1 < 0 \). With such a rule, a derivation from true premises could end anywhere, so checking is only as good as the rules checked against. Chapter 3 proves that the rules of logic have the good property, and calls it **soundness** (@thm-soundness).
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
3. The two lines "1. \( 0 < 0 \), \( \mathrm{Tr} \ 2, 2 \)" and "2. \( 0 < 0 \), \( \mathrm{Tr} \ 1, 1 \)" would each pass the first two questions of "Reading a derivation". Use them to explain why a line may cite only earlier lines.
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

<!-- dependency ledger
def-rule-schema (example): Tr and Sh are true facts about < on the real numbers (transitivity; adding a number to both sides) | school algebra, used as toy rules by the blueprint's design; ch11 (promised)
def-rule-schema (example): 2/4 = 1/2 | inline arithmetic
exm-chaining-derivation (example): none beyond the toy rule Tr | inline; checked by verify/ch01/exm-chaining-derivation.py
exm-derivations (solution): every rule met before boxes cites at least one line (and-I, and-E, ->E) | the third and fourth sections of this chapter (later sections, stated as a meta-claim, not used in a proof; blueprint ch01.md, Rule system)
exm-not-a-derivation (solution): the instance and earlier-line claims for both changes | inline; checked by verify/ch01/exm-not-a-derivation.py
exm-not-a-derivation (example): the "How this looks" chain after it: 0 < 1/(n+1) < 1/n <= 1 for integers n >= 1; from a < b and b <= c infer a < c | school algebra; ch11 (promised)
exr-derivations-a1 (solution): Tr and Sh lead from true lines to true lines; going down the derivation line by line is an induction | school algebra, ch11 (promised); the induction is ch03 (promised)
exr-derivations-b3 (solution): 0 < 1/4 < 1/3 < 1/2; m - 1 joins; the lower bound m - 1 is stated, not proved or used | inline arithmetic, checked by verify/ch01/exr-derivations-b3.py (which also confirms the lower bound for m <= 5); proof by induction ch03 (promised)
exr-derivations-c1 (solution): 0 < 1 is true and 1 < 0 is false | inline arithmetic
exr-derivations-c2 (solution): following citations backwards the line numbers strictly decrease, so the chain of citations ends | inline: the numbers lie among 1, ..., n, so a strictly decreasing chain of them has at most n terms
-->
