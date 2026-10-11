# Using "For Every": Instantiation

Section 4.2 made the language exact and defined the operation \( \varphi[t/x] \), "put the term \( t \) in for the variable \( x \)", with its one hazard, capture. We can now give the first quantifier rule. It is the rule for **using** a universal statement: whatever holds for every object holds for the object named by any term we care to write. The rule is called \( \rulename{\forall E} \). It is the rule behind every "by the theorem, applied to \( x = 2 \)". With it alone, universal statements can be used but not proved, and the section ends at exactly that gap, which Section 4.4 fills.

## Applying a statement about everything

Every application of a general fact to a particular case is one step of logic, and so far that step has been taken on trust. Three earlier places took it.

- Section 1.4 used the theorem "if \( a < b \) and \( b < c \), then \( a < c \)" at \( a = \sqrt{2} \), \( b = 1.5 \), \( c = 2 \), and said that passing from "for all \( a, b, c \)" to one instance is a rule of its own, still to be stated.
- In @exm-raa-zero (Section 2.5) the hypothesis was "\( x \le \varepsilon \) for every \( \varepsilon > 0 \)", and the proof applied it to the one number \( \varepsilon = x/2 \).
- Section 4.1 opened with the argument "every positive real has a square root; \( 2 \) is positive; so \( 2 \) has a square root", which a truth table calls invalid because it sees only three unrelated atoms.

The same step happens in each: a statement about **every** object is applied to **one** object, named by a term. In the language of Section 4.2, the first premise of the square-root argument is \( \forall x\, (P(x) \to S(x)) \), and applying it to \( 2 \) gives
\[
\bigl( P(x) \to S(x) \bigr)[2/x] \ = \ P(2) \to S(2),
\]
which is part (a) of @exm-computing-substitutions. From there \( \rulename{{\to}E} \) finishes. All that is missing is a rule that licenses the first step.

## The rule

*A universal statement may be applied to any term: remove the quantifier and put the term in for the variable.*

::: {#def-rule-universal-elimination}
[Universal Elimination]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\forall x\, \varphi}
  \have {k} {\varphi[t/x]} \Ae{i}
\end{nd}$
\end{center}
```

Here \( \varphi \) is a formula, \( x \) a variable, and \( t \) **any** term, subject to one side condition: **\( t \) is free for \( x \) in \( \varphi \)** (@def-free-for). Line \( i \) must be available at line \( k \) (the scope rule of @def-derivation). This rule is called \( \rulename{\forall E} \) (**universal elimination**, or **instantiation**), and \( \varphi[t/x] \) is an **instance** of \( \forall x\, \varphi \).
:::

In words: if a line says that \( \varphi \) holds for every \( x \), then any later line, where that line is still available, may write what \( \varphi \) says about \( t \). The rule cites one line and no box.

Read the definition clause by clause.

1. **The cited line begins with \( \forall x \).** Its main symbol must be the quantifier, with the whole of \( \varphi \) as its scope. By shorthand rule 2 of Section 4.2, \( \forall x\, P(x) \to Q(c) \) is an implication whose hypothesis is \( \forall x\, P(x) \); its main symbol is \( \to \), so \( \rulename{\forall E} \) does not apply to it. A \( \forall \) buried inside another connective is not available to the rule until the rules for that connective have dug it out.
2. **Any term.** The term may be a constant (\( c \), \( 2 \)), a variable (\( y \), or \( x \) itself), or a compound term (\( f(c) \), \( a - 1 \), \( \varepsilon/2 \)). It may be a variable that already occurs elsewhere in the derivation. Nothing about the term has to be established first: \( \rulename{\forall E} \) needs no line saying that \( t \) "exists" or "is in the domain", because every term names an element of the domain.
3. **Every free occurrence, by the same term.** The new line is \( \varphi[t/x] \), so by @def-substitution every free occurrence of \( x \) in \( \varphi \) is replaced, and all of them by the same \( t \). We do not choose which occurrences change.
4. **Free for \( x \).** This is the condition of @def-free-for, and it is the rule's only restriction. It forbids exactly the substitutions in which a variable of \( t \) would be captured by a quantifier of \( \varphi \).
5. **Line \( i \) is available.** Line \( i \) must be available at line \( k \) (the scope rule of @def-derivation). Every rule asks this; it is not a restriction special to \( \rulename{\forall E} \).

**A degenerate case.** If \( x \) is not free in \( \varphi \), then \( \varphi[t/x] = \varphi \) for every term \( t \) (the claim proved in Section 4.2), and \( \rulename{\forall E} \) simply removes a quantifier that bound nothing: from \( \forall x\, P(c) \) it writes \( P(c) \). Legal, and dull.

**One line, many uses.** The cited line stays where it is, available as before. A derivation may instantiate the same universal line as often as it likes, at different terms or the same one. Worked derivation (d) below uses one premise twice.

*Why this rule.* It says no more than the word "every". If every object in the domain satisfies \( \varphi \), then so does the object that \( t \) names, whichever object that is. A term always names something, since the domain is never empty (Section 4.1), so the instance always has something to be about.

*Why "free for".* The instance must say about \( t \) what \( \varphi \) says about \( x \). Section 4.2 showed that when a variable of \( t \) is captured, \( \varphi[t/x] \) can say something quite different. The condition rules capture out, and the subsection on common errors below shows the rule going wrong without it. Section 4.11 states that the rule, with its condition, never leads from true premises to a false line, and the optional Section 4.12 proves it.

::: {.check}
Line 1 of a derivation is \( \forall x\, \exists z\, (z > x + y) \). For which terms \( t \) may \( \rulename{\forall E} \) write \( (\exists z\, (z > x + y))[t/x] \) on line 2? Is \( t = y \) allowed? Is \( t = z + 1 \)?
:::

::: {.solution}
The only free occurrence of \( x \) in \( \exists z\, (z > x + y) \) lies in the scope of \( \exists z \), and that is the only quantifier above it. So \( t \) is free for \( x \) exactly when \( z \) is not a variable of \( t \): **any term not containing \( z \)** is allowed. The term \( y \) is allowed, and gives \( \exists z\, (z > y + y) \); the variable \( y \) already occurs free in the line, and that does no harm. The term \( z + 1 \) is not allowed: it would give \( \exists z\, (z > z + 1 + y) \), where the \( z \) of the term has been captured. Nor is \( z \) itself. To instantiate at \( z \), rename the bound \( z \) first (Section 4.2), say to \( w \): from \( \forall x\, \exists w\, (w > x + y) \), \( \rulename{\forall E} \) at \( z \) gives \( \exists w\, (w > z + y) \).
:::

## Four derivations

The worked derivations below use \( \rulename{\forall E} \) and the rules of Chapter 1. Each has an Idea that says why each rule was chosen, continuing the search method of Section 2.6: a goal-directed step looks at the goal's main symbol, a premise-directed step at a resource's. The new question is the one that \( \rulename{\forall E} \) raises every time: **at which term?**

::: {#exm-universal-elimination-derivations}
[Instantiation at work]

Give a derivation of each sequent.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, (P(x) \to Q(x)), \ P(c) \vdash Q(c) \).
2. \( \forall x\, \forall y\, R(x, y) \vdash R(c, c) \).
3. \( \forall x\, \forall y\, (R(x, y) \to R(y, x)), \ R(a, b) \vdash R(b, a) \).
4. \( \forall x\, (P(x) \to P(f(x))), \ P(c) \vdash P(f(f(c))) \).
:::
:::

::: {.solution}
(a) *Idea.* The goal \( Q(c) \) has no connective or quantifier, so no introduction rule produces it, and the search turns to the premises. The premise \( P(c) \) cannot be taken apart. The premise \( \forall x\, (\dots) \) begins with \( \forall \), so it can be used only by \( \rulename{\forall E} \). At which term? The goal mentions the term \( c \), so instantiate at \( c \). That gives an implication whose hypothesis is a premise and whose conclusion is the goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {P(c)}
  \have {3} {P(c) \to Q(c)} \Ae{1}
  \have {4} {Q(c)} \ie{3,2}
\end{nd}$
\end{center}
```

Line 3 is \( (P(x) \to Q(x))[c/x] \); the constant \( c \) has no variables, so it is free for \( x \). Read \( c \) as \( 2 \), \( P(x) \) as "\( x \) is positive", and \( Q(x) \) as "\( x \) has a square root" (Section 4.1 wrote \( S \) for this predicate), and the derivation is the square-root argument of Section 4.1, in the four lines promised there. The argument that truth tables rejected is derivable once the rules can see inside its sentences.

(b) *Idea.* The premise has two quantifiers, and \( \rulename{\forall E} \) removes one at a time, the outermost first: the main symbol of the premise is \( \forall x \), and only after it is gone is \( \forall y \) the main symbol. The goal \( R(c, c) \) shows the term for both.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \have {2} {\forall y\, R(c, y)} \Ae{1}
  \have {3} {R(c, c)} \Ae{2}
\end{nd}$
\end{center}
```

Line 2 is \( (\forall y\, R(x, y))[c/x] \): the quantifier \( \forall y \) is on a variable other than \( x \), so the substitution passes through it (@def-substitution). Line 3 instantiates \( y \) at \( c \) as well. Nothing forbids putting the same term in for two different variables; "for all \( x \) and \( y \)" includes the case \( x = y \).

(c) *Idea.* Work backwards from the goal \( R(b, a) \). The only line that can produce it is the first premise, through an instance of its inside, \( R(x, y) \to R(y, x) \), followed by \( \rulename{{\to}E} \). Which instance has conclusion \( R(b, a) \)? Matching \( R(y, x) \) with \( R(b, a) \) gives \( y \coloneqq b \) and \( x \coloneqq a \). Then the hypothesis of that instance is \( R(a, b) \), which is the second premise. So the terms are read off the goal: \( a \) for \( x \) first (the outer quantifier), then \( b \) for \( y \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (R(x, y) \to R(y, x))}
  \hypo {2} {R(a, b)}
  \have {3} {\forall y\, (R(a, y) \to R(y, a))} \Ae{1}
  \have {4} {R(a, b) \to R(b, a)} \Ae{3}
  \have {5} {R(b, a)} \ie{4,2}
\end{nd}$
\end{center}
```

A reader who matches the goal \( R(b, a) \) against the hypothesis \( R(x, y) \) instead of the conclusion \( R(y, x) \) puts \( b \) for \( x \) and \( a \) for \( y \), and gets \( R(b, a) \to R(a, b) \). That is a legal line, but its hypothesis is the goal itself, so \( \rulename{{\to}E} \) cannot fire. Match the goal against the conclusion of the implication, since that is the part \( \rulename{{\to}E} \) delivers.

(d) *Idea, forwards.* The premise \( P(c) \) is the hypothesis of the instance of the first premise at \( c \), so instantiating at \( c \) and firing gives \( P(f(c)) \). Now \( P(f(c)) \) is the hypothesis of the instance at \( f(c) \), so the same premise, instantiated again, fires again and gives \( P(f(f(c))) \), the goal.

*Idea, backwards.* The goal \( P(f(f(c))) \) has the shape \( P(f(x)) \), the conclusion of the inside of the first premise, with \( x \coloneqq f(c) \). So the last \( \rulename{\forall E} \) must be at the **compound** term \( f(c) \), and its hypothesis \( P(f(c)) \) becomes the new goal. That has the shape \( P(f(x)) \) with \( x \coloneqq c \), and its hypothesis is the premise \( P(c) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to P(f(x)))}
  \hypo {2} {P(c)}
  \have {3} {P(c) \to P(f(c))} \Ae{1}
  \have {4} {P(f(c))} \ie{3,2}
  \have {5} {P(f(c)) \to P(f(f(c)))} \Ae{1}
  \have {6} {P(f(f(c)))} \ie{5,4}
\end{nd}$
\end{center}
```

Line 5 cites line 1 again: a universal line can be instantiated as often as needed. Its term \( f(c) \) contains no variable, so it is free for \( x \), and \( (P(x) \to P(f(x)))[f(c)/x] \) is \( P(f(c)) \to P(f(f(c))) \): **every** \( x \) is replaced by the whole term \( f(c) \), including the one inside \( f(x) \).

An arithmetic reading: over \( \nN \), let \( f(n) \) be \( n + 2 \), let \( P(n) \) say "\( n \) is even", and let \( c \) be \( 0 \). The first premise says that adding \( 2 \) to an even number gives an even number, the second that \( 0 \) is even, and the derivation concludes that \( f(f(0)) = 4 \) is even. Each further step up the even numbers would cost two more lines. Reaching "every \( n \) of the form \( f(\cdots f(0) \cdots) \)" at once is a job for induction, not for this rule.
:::

In each derivation, the Idea chose the term of every \( \rulename{\forall E} \) by matching: the goal, or a hypothesis still needed, has a definite shape, and the instance is chosen to have that shape. Instantiating at a term that nothing asks for is legal, and it fills a derivation with lines that lead nowhere.

## Checking a line of instantiation

Choosing the term can take thought; checking a line never does. For a line justified "\( \rulename{\forall E} \) \( i \)", ask four questions.

1. Is line \( i \) available here (@def-derivation)?
2. Is the main symbol of line \( i \) a universal quantifier? If so, read off its variable \( x \) and its scope \( \varphi \).
3. Is this line \( \varphi[t/x] \) for some term \( t \)? Find \( t \) by comparing the two lines at a free occurrence of \( x \) in \( \varphi \); then check that **every** free occurrence of \( x \) became that same \( t \), and that nothing else changed.
4. Is \( t \) free for \( x \) in \( \varphi \)?

Run on line 5 of (d): line 1 is available, since no box contains it; its main symbol is \( \forall x \), with scope \( P(x) \to P(f(x)) \); comparing gives \( t = f(c) \), and both occurrences of \( x \) became \( f(c) \); and \( f(c) \) has no variables, so it is free for \( x \). The line passes.

## How this rule looks in a mathematical proof

Let \( a \) be a real number. A proof might say:

> Since \( y^2 \ge 0 \) for every real \( y \), applying this to \( a - 1 \) gives \( (a - 1)^2 \ge 0 \), that is, \( a^2 - 2a + 1 \ge 0 \).

The first half of the sentence is one \( \rulename{\forall E} \), at the compound term \( a - 1 \). The second half rewrites \( (a - 1)^2 \) by school algebra. In a derivation such a step is written as one line justified "arith", for **arithmetic**:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall y\, (y^2 \ge 0)}
  \have {2} {(a - 1)^2 \ge 0} \Ae{1}
  \have {3} {a^2 - 2 \cdot a + 1 \ge 0} \by{arith}{2}
\end{nd}$
\end{center}
```

| Line | Sentence |
|---|---|
| 1 | "Since \( y^2 \ge 0 \) for every real \( y \), …" (the general fact) |
| 2 | "… applying this to \( a - 1 \) gives \( (a - 1)^2 \ge 0 \), …" (\( \rulename{\forall E} \) at \( a - 1 \)) |
| 3 | "… that is, \( a^2 - 2a + 1 \ge 0 \)." (arith) |

A line justified "arith" records a fact of school arithmetic or algebra, used on the lines it cites; here the fact is that \( (u - 1)^2 \) and \( u^2 - 2u + 1 \) are the same number for every real \( u \). It is **not a new rule**. Written out in full, it is a universally quantified arithmetic statement, here
\[
\forall u\, \bigl( (u - 1)^2 \ge 0 \to u^2 - 2 \cdot u + 1 \ge 0 \bigr),
\]
taken as one more premise, instantiated by \( \rulename{\forall E} \) at the term on the line (here \( a \)) and applied by \( \rulename{{\to}E} \) to the cited line. That is exactly the pattern of (a) above. The book writes it as one line because spelling it out every time would bury the logic under algebra; its bound variables are letters that appear nowhere else in the derivation, and that keeps every term free for them. As in the earlier chapters, the facts of school algebra are used here as facts.

Section 4.4 will turn this three-line derivation into a proof of \( x^2 - 2x + 1 \ge 0 \) for **every** real \( x \). That needs a rule this section does not have.

## Common errors

Three mistakes are worth seeing written out, each with a reading in which the premise is true and the offending line false.

**Capture.** The premise \( \forall x\, \exists y\, (y \ne x) \) says, over \( \nN \), that for every number there is a different one; it is true, since \( x + 1 \ne x \). Instantiating "at \( y \)" without looking writes this:

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (forall-E with a captured term)
$\begin{nd}
  \hypo {1} {\forall x\, \exists y\, (y \ne x)}
  \have {2} {\exists y\, (y \ne y)} \Ae{1}
\end{nd}$
\end{center}
```

Line 2 says that some number differs from itself, which is false. The step breaks the side condition: the free occurrence of \( x \) in \( \exists y\, (y \ne x) \) lies in the scope of \( \exists y \), and \( y \) is a variable of the term \( y \), so \( y \) is not free for \( x \). This is the capture example of Section 4.2, now inside a derivation. The repair is to rename first: \( \forall x\, \exists z\, (z \ne x) \) is the same premise up to renaming, and \( \rulename{\forall E} \) at \( y \) gives \( \exists z\, (z \ne y) \), "some number differs from \( y \)", which is what was meant.

::: {.warning}
\( \rulename{\forall E} \) at a term that is not free for \( x \) can turn a true premise into a false line, and the definition of \( \varphi[t/x] \) gives no signal: it returns a formula either way. Over \( \nN \), from the true \( \forall x\, \exists y\, (y \ne x) \), the "instance at \( y \)" is \( \exists y\, (y \ne y) \), which is false. Before instantiating at a term with variables, look for quantifiers on those variables inside \( \varphi \).
:::

**A buried quantifier.** From the line \( \forall x\, P(x) \to Q(c) \) one may **not** write \( P(c) \to Q(c) \). The main symbol of the line is \( \to \), and the \( \forall x \) governs only the hypothesis \( \forall x\, P(x) \). The line says "if **every** \( x \) has \( P \), then \( Q(c) \)"; the false step reads it as "if \( c \) has \( P \), then \( Q(c) \)", which is far stronger. Over \( \nN \), read \( P(x) \) as \( x \ge 1 \), \( Q(x) \) as \( x = 0 \), and \( c \) as \( 1 \). The line is true, because its hypothesis "every natural number is at least \( 1 \)" is false (\( 0 \) is not). The false step's result, "if \( 1 \ge 1 \), then \( 1 = 0 \)", is false.

**Replacing only some occurrences.** Over \( \nR \), \( \forall x\, (x \le x^2 \vee x < 1) \) is true: a real \( x \ge 1 \) has \( x^2 = x \cdot x \ge x \), and every other real has \( x < 1 \). Writing \( 2 \le x^2 \vee x < 1 \) from it replaces the first \( x \) and leaves the others. That is not \( \varphi[2/x] \), which is \( 2 \le 2^2 \vee 2 < 1 \): the substitution replaces every free occurrence. The half-replaced line still has \( x \) free, and when \( x \) names \( 1 \) it reads \( 2 \le 1 \vee 1 < 1 \), which is false.

## A stall

Try the sequent
\[
\forall x\, (P(x) \wedge Q(x)) \vdash \forall x\, P(x) .
\]
It is plainly correct: if every \( x \) has both properties, then every \( x \) has the first. Search for a derivation. The goal begins with \( \forall \), and no rule so far is made for proving a \( \forall \). Apart from \( \rulename{\bot E} \) (@def-rules-contradiction) and \( \rulename{RAA} \) (@def-rule-raa), which reach a line only by way of a contradiction, a line beginning with \( \forall \) can only be taken out of a line or box that already contains it. So the goal-directed step has nothing to offer, and we turn to the premise. \( \rulename{\forall E} \) at \( c \) gives \( P(c) \wedge Q(c) \), and \( \rulename{\wedge E} \) gives \( P(c) \). The same works at \( d \), at \( f(c) \), at any term we name. But each line is an instance. No finite list of instances is the statement \( \forall x\, P(x) \), which speaks about every object at once, including all the objects that none of our terms happen to name.

So with \( \rulename{\forall E} \) alone, a universal statement can be **used** but not **proved**. Leaving aside a detour through a contradiction, a derivation can write \( \forall x\, \psi \) only by taking it out of a line or box that already contains it, as line 2 of (b) took \( \forall y\, R(c, y) \) out of the premise. Section 1.4 was in the same position with implications, and Section 1.5 filled the gap with a box. Section 4.4 does the same for \( \forall \): it proves \( P \) of one name about which nothing is known, and that box finishes this derivation in four lines.

## What the rule sounds like

The table of Sections 1.3–1.7 and 2.1–2.5 gains a row for \( \rulename{\forall E} \).

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\forall E} \) | "In particular, for \( x = t \), …"; "applying the hypothesis to \( t \), …" | `h t` (or `specialize h t`) |

Written mathematics has many forms of the phrase: "in particular, for \( x = 3 \), …"; "applying the hypothesis to \( x_0 - 1 \), …"; "by the theorem with \( \varepsilon/2 \) in place of \( \varepsilon \), …". In the Lean column, `h` is the universal statement and `t` the term; applying `h` to `t` gives the instance, just as applying an implication to a proof of its hypothesis gave its conclusion in Section 1.4. In Lean a universal statement behaves like a function that takes a term and returns a proof of the instance.

## The search method: one more step

The search method of Section 2.6 had a goal-directed step and a premise-directed step for each connective. Instantiation adds a premise-directed step.

- **A resource \( \forall x\, \varphi \).** Do not instantiate blindly. Instantiate at the term that the goal, or another resource, asks for: match the shape of the goal (or of a hypothesis still needed) against \( \varphi \), and read off the term. If the term is not free for \( x \) in \( \varphi \), rename the bound variables of \( \varphi \) first.

Instantiating is always **safe**, in the sense of Section 2.6: the new line is added and nothing is lost, since the universal line stays available. What can go wrong is only that the derivation fills with instances nobody needs, as a forward search filled with useless lines in Section 1.4.

## Exercises

### A. Check your understanding

::: {#exr-universal-elimination-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write the schema of \( \rulename{\forall E} \) and its side condition from memory.
2. For each pair, decide whether line 2 follows from line 1 by one application of \( \rulename{\forall E} \). If not, name the clause of @def-rule-universal-elimination that fails.

   - (i) Line 1: \( \forall x\, \exists y\, (y > x) \); line 2: \( \exists y\, (y > y) \).
   - (ii) Line 1: \( \forall x\, (x \cdot x \ge 0) \); line 2: \( 3 \cdot x \ge 0 \).
   - (iii) Line 1: \( \forall x\, P(x) \to P(c) \); line 2: \( P(a) \to P(c) \).
   - (iv) Line 1: \( \forall x\, (P(x) \to P(f(x))) \); line 2: \( P(f(c)) \to P(f(f(c))) \).

3. True or false, with a reason: from \( \forall x\, \forall y\, R(x, y) \), one application of \( \rulename{\forall E} \) gives \( \forall x\, R(x, c) \).
4. Why does \( \rulename{\forall E} \) not need a line saying that the term \( t \) names an element of the domain?
:::
:::

::: {.solution}
(a) From line \( i \): \( \forall x\, \varphi \), line \( k \) may be \( \varphi[t/x] \), justified "\( \rulename{\forall E} \) \( i \)", for any term \( t \) that is free for \( x \) in \( \varphi \), with line \( i \) available at line \( k \).

(b) (i) Not legal: the term \( y \) is not free for \( x \) in \( \exists y\, (y > x) \), since the free \( x \) lies in the scope of \( \exists y \) (clause 4, capture). Over \( \nZ \), line 1 is true and line 2 is false.

(ii) Not legal: only the first \( x \) was replaced, so line 2 is not \( \varphi[t/x] \) for any \( t \) (clause 3). The instance at \( 3 \) is \( 3 \cdot 3 \ge 0 \). Line 2 still has \( x \) free, and over \( \nR \) it is false when \( x \) names \( -1 \).

(iii) Not legal: the main symbol of line 1 is \( \to \), not \( \forall \) (clause 1); the \( \forall x \) governs only \( P(x) \). Over \( \nN \) with \( P(x) \) read as \( x \ge 1 \), \( c \) as \( 0 \), and \( a \) as \( 1 \): line 1 says "if every natural number is at least \( 1 \), then \( 0 \ge 1 \)", true because its hypothesis is false; line 2 says "if \( 1 \ge 1 \), then \( 0 \ge 1 \)", which is false.

(iv) Legal: it is \( \varphi[f(c)/x] \) with \( \varphi = P(x) \to P(f(x)) \), both occurrences of \( x \) replaced by \( f(c) \), and \( f(c) \) has no variables, so it is free for \( x \) (clause 2: any term, compound ones included).

(c) False. The main symbol is \( \forall x \), so one application removes \( \forall x \) and gives \( \forall y\, R(t, y) \) for some term \( t \). The line \( \forall x\, R(x, c) \) would need the inner quantifier removed while the outer one stays, and the rule cannot reach inside the outer quantifier. (The sequent \( \forall x\, \forall y\, R(x, y) \vdash \forall x\, R(x, c) \) is derivable, but it needs the rule of Section 4.4.)

(d) Every term names an element of the domain: once the symbols are interpreted, a constant names one, and a compound term names the value of a function at elements. And the domain is never empty (Section 4.1). So "every element satisfies \( \varphi \)" applies to whatever \( t \) names, with nothing further to check. (Bounded quantifiers are different: to use \( \forall x \in A\; \varphi \) at \( t \) one also needs \( t \in A \), and Section 4.8 builds that into a rule.)
:::

### B. Practice

::: {#exr-universal-elimination-b1}
[B1: Two links]

Give a derivation of
\[
\forall x\, (P(x) \to Q(x)), \ \forall x\, (Q(x) \to R(x)), \ P(a) \vdash R(a),
\]
and say, for each \( \rulename{\forall E} \) line, which line of the search asked for its term.
:::

::: {.solution}
The goal \( R(a) \) is the conclusion of the instance of the second premise at \( a \), so it suffices to reach \( Q(a) \); that is the conclusion of the instance of the first premise at \( a \), so it suffices to reach \( P(a) \), a premise. Both terms come from the goal: the second \( \rulename{\forall E} \) (line 6) from \( R(a) \), the first (line 4) from the subgoal \( Q(a) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, (Q(x) \to R(x))}
  \hypo {3} {P(a)}
  \have {4} {P(a) \to Q(a)} \Ae{1}
  \have {5} {Q(a)} \ie{4,3}
  \have {6} {Q(a) \to R(a)} \Ae{2}
  \have {7} {R(a)} \ie{6,5}
\end{nd}$
\end{center}
```
:::

::: {#exr-universal-elimination-b2}
[B2: An increasing function]

Read \( f \) as a function from \( \nR \) to \( \nR \) and \( a, b, c \) as real numbers. Give a derivation of
\[
\forall x\, \forall y\, (x \le y \to f(x) \le f(y)), \ a \le b, \ b \le c \ \vdash \ f(a) \le f(b) \wedge f(b) \le f(c) ,
\]
and then write the argument as one sentence of prose.
:::

::: {.solution}
The goal is a conjunction, so its last line is \( \rulename{\wedge I} \), with subgoals \( f(a) \le f(b) \) and \( f(b) \le f(c) \). Each is the conclusion of an instance of the first premise: matching \( f(x) \le f(y) \) with \( f(a) \le f(b) \) gives \( x \coloneqq a \), \( y \coloneqq b \), and with \( f(b) \le f(c) \) gives \( x \coloneqq b \), \( y \coloneqq c \). The hypotheses of the two instances are the other two premises.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (x \le y \to f(x) \le f(y))}
  \hypo {2} {a \le b}
  \hypo {3} {b \le c}
  \have {4} {\forall y\, (a \le y \to f(a) \le f(y))} \Ae{1}
  \have {5} {a \le b \to f(a) \le f(b)} \Ae{4}
  \have {6} {f(a) \le f(b)} \ie{5,2}
  \have {7} {\forall y\, (b \le y \to f(b) \le f(y))} \Ae{1}
  \have {8} {b \le c \to f(b) \le f(c)} \Ae{7}
  \have {9} {f(b) \le f(c)} \ie{8,3}
  \have {10} {f(a) \le f(b) \wedge f(b) \le f(c)} \ai{6,9}
\end{nd}$
\end{center}
```

The premise is instantiated twice, along two different paths: once at \( a \) and \( b \), once at \( b \) and \( c \). In prose: *Since \( f \) is increasing and \( a \le b \), we have \( f(a) \le f(b) \), and likewise \( b \le c \) gives \( f(b) \le f(c) \).* The word "increasing" carries the first premise, and the two applications of it are the two pairs of \( \rulename{\forall E} \) lines.
:::

::: {#exr-universal-elimination-b3}
[B3: Squares are not negative]

Let \( a \) and \( b \) be real numbers. Give a derivation of
\[
\forall x\, (x^2 \ge 0) \vdash (a + b)^2 \ge 0 \wedge (a - b)^2 \ge 0 .
\]
Then extend it by one line justified "arith" to a derivation of \( a^2 + b^2 \ge 2ab \) from the same premise, and say which earlier line the arith line uses.
:::

::: {.solution}
The goal is a conjunction of two instances of the premise, at the compound terms \( a + b \) and \( a - b \). Both terms are free for \( x \) in \( x^2 \ge 0 \), which has no quantifier.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (x^2 \ge 0)}
  \have {2} {(a + b)^2 \ge 0} \Ae{1}
  \have {3} {(a - b)^2 \ge 0} \Ae{1}
  \have {4} {(a + b)^2 \ge 0 \wedge (a - b)^2 \ge 0} \ai{2,3}
  \have {5} {a^2 + b^2 \ge 2 \cdot a \cdot b} \by{arith}{3}
\end{nd}$
\end{center}
```

Lines 1–4 are the first derivation. For the second goal only line 3 is needed: \( (a - b)^2 = a^2 - 2ab + b^2 \), so \( (a - b)^2 \ge 0 \) says \( a^2 - 2ab + b^2 \ge 0 \), and adding \( 2ab \) to both sides gives \( a^2 + b^2 \ge 2ab \). That algebra is the arith line 5. (Lines 2 and 4 are then unused, which is allowed, and deleting them leaves a three-line derivation of \( a^2 + b^2 \ge 2ab \). Line 2 would give \( a^2 + b^2 \ge -2ab \) in the same way.)
:::

### C. Going deeper

::: {#exr-universal-elimination-c1}
[C1: A partner makes a loop]

A relation \( R \) is **symmetric** if \( R(x, y) \) gives \( R(y, x) \), and **transitive** if \( R(x, y) \) and \( R(y, z) \) give \( R(x, z) \). Show that in a symmetric and transitive relation, every element that is related to something is related to itself, by giving a derivation of
\[
\begin{aligned}
&\forall x\, \forall y\, (R(x, y) \to R(y, x)), \\
&\forall x\, \forall y\, \forall z\, ((R(x, y) \wedge R(y, z)) \to R(x, z)), \ R(a, b) \ \vdash \ R(a, a) .
\end{aligned}
\]
Explain how each term of each \( \rulename{\forall E} \) was chosen.
:::

::: {.solution}
[Hint 1]

The goal \( R(a, a) \) can only come from the transitivity premise. Match its conclusion \( R(x, z) \) with the goal.
:::

::: {.solution}
[Hint 2]

The match gives \( x \coloneqq a \) and \( z \coloneqq a \), and leaves \( y \) open. Which \( y \) makes the hypothesis \( R(a, y) \wedge R(y, a) \) reachable from the premises?
:::

::: {.solution}
*The search.* The goal \( R(a, a) \) is atomic, so it must be the conclusion of an instance of a premise. Symmetry ends in \( R(y, x) \), and its instance at \( a, a \) is \( R(a, a) \to R(a, a) \), whose hypothesis is the goal itself: a dead end. Transitivity ends in \( R(x, z) \). Matching gives \( x \coloneqq a \) and \( z \coloneqq a \). The variable \( y \) does not occur in the conclusion, so the goal says nothing about it; the hypothesis \( R(a, y) \wedge R(y, a) \) must decide. The premise \( R(a, b) \) offers \( R(a, y) \) with \( y \coloneqq b \). Then the second conjunct is \( R(b, a) \), which symmetry gives from \( R(a, b) \): the instance of the symmetry premise at \( x \coloneqq a \), \( y \coloneqq b \) (read off its needed conclusion \( R(b, a) \), as in @exm-universal-elimination-derivations (c)).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (R(x, y) \to R(y, x))}
  \hypo {2} {\forall x\, \forall y\, \forall z\, ((R(x, y) \wedge R(y, z)) \to R(x, z))}
  \hypo {3} {R(a, b)}
  \have {4} {\forall y\, (R(a, y) \to R(y, a))} \Ae{1}
  \have {5} {R(a, b) \to R(b, a)} \Ae{4}
  \have {6} {R(b, a)} \ie{5,3}
  \have {7} {\forall y\, \forall z\, ((R(a, y) \wedge R(y, z)) \to R(a, z))} \Ae{2}
  \have {8} {\forall z\, ((R(a, b) \wedge R(b, z)) \to R(a, z))} \Ae{7}
  \have {9} {(R(a, b) \wedge R(b, a)) \to R(a, a)} \Ae{8}
  \have {10} {R(a, b) \wedge R(b, a)} \ai{3,6}
  \have {11} {R(a, a)} \ie{9,10}
\end{nd}$
\end{center}
```

*The terms.* Lines 7 and 9 put \( a \) in for \( x \) and for \( z \): both read off the goal. Line 8 puts \( b \) in for \( y \): read off the premise \( R(a, b) \), the only available fact of the form \( R(a, \cdot) \). Lines 4 and 5 put in \( a \) and \( b \): read off the needed line \( R(b, a) \). All terms are constants, so every one is free for its variable.

The hypothesis "related to something" is needed. In a symmetric and transitive relation an element related to nothing need not be related to itself: on \( \{0, 1\} \), the relation that holds only between \( 0 \) and \( 0 \) is symmetric and transitive, and \( R(1, 1) \) fails. Without a premise like \( R(a, b) \) the search has no term for \( y \) that makes the hypothesis of line 9 reachable.

**Marking scheme.** (10 points)
- 2: identifies transitivity as the source of the goal and instantiates it with \( a \) for \( x \) and \( z \).
- 2: chooses \( b \) for \( y \), with the reason (the premise \( R(a, b) \)).
- 2: obtains \( R(b, a) \) from symmetry at \( a \), \( b \), with \( \rulename{{\to}E} \).
- 2: builds the conjunction in the right order and fires the transitivity instance.
- 2: every \( \rulename{\forall E} \) removes the outermost quantifier of a cited line and replaces every occurrence of its variable.
Fatal errors (0 for the step): removing an inner quantifier before an outer one; instantiating transitivity at a term for \( y \) for which neither conjunct of the hypothesis is available.
:::

::: {#exr-universal-elimination-c2}
[C2: Instantiating at the variable itself]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \forall x\, P(x) \vdash P(x) \), by a derivation whose one \( \rulename{\forall E} \) line you check against every clause of @def-rule-universal-elimination.
2. The reverse step, from a line \( P(x) \) to \( \forall x\, P(x) \), is an instance of no rule so far. Show that it must not be allowed without restriction: give a reading over \( \nZ \), with \( x \) naming one particular integer, in which \( P(x) \) is true and \( \forall x\, P(x) \) is false.
3. Section 4.4 will allow the step from a line \( P(x_0) \) to \( \forall x\, P(x) \) under conditions on the name \( x_0 \): the line \( P(x_0) \) must close a special box opened for \( x_0 \), and \( x_0 \) must appear in no premise, in no assumption still in force, and not in the conclusion \( \forall x\, P(x) \). Using this description, explain why the route "\( \forall x\, P(x) \), so \( P(x) \), so \( \forall x\, P(x) \)" cannot use the letter \( x \) as the name, what it must do instead, and why no name at all will do when \( P(x) \) is itself the premise.
:::
:::

::: {.solution}
(a)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, P(x)}
  \have {2} {P(x)} \Ae{1}
\end{nd}$
\end{center}
```

Clause 1: the main symbol of line 1 is \( \forall x \), with scope \( P(x) \). Clause 2: the term is the variable \( x \) itself, and any term is allowed. Clause 3: \( P(x)[x/x] = P(x) \), so every free occurrence was replaced, by \( x \). Clause 4: \( x \) is free for \( x \) in every formula (Section 4.2: a free occurrence of \( x \) never lies in the scope of a quantifier on \( x \)). Clause 5: line 1 is a premise and lies in no box, so it is available at line 2. So line 2 is legal. Its \( x \) is now free: line 2 says "\( P \) holds of whatever \( x \) names", which is true whatever \( x \) names, since line 1 says that \( P \) holds of everything.

(b) Read \( P(x) \) as "\( x \) is even" and let \( x \) name \( 2 \). Then \( P(x) \) is true, and \( \forall x\, P(x) \), "every integer is even", is false, since \( 1 \) is odd. A rule allowing the step from \( P(x) \) to \( \forall x\, P(x) \) in general would lead from a true line to a false one.

(c) With the letter \( x \) as the name, the conclusion \( \forall x\, P(x) \) contains \( x \) (the variable after the quantifier counts, which is what "appear" means), so the condition "not in the conclusion" fails, whatever else holds. The route must instantiate at a **different** letter instead: open the box for a new name \( x_0 \), write \( P(x_0) \) by \( \rulename{\forall E} \) at \( x_0 \) from line 1, and close the box with \( \forall x\, P(x) \). Now \( x_0 \) appears nowhere in the premise \( \forall x\, P(x) \), there is no other assumption, and \( x_0 \) is not in the conclusion; every condition holds.

If \( P(x) \) is itself the premise, take any name. If the name is \( x \), the line \( P(x) \) is available but \( x \) appears in the premise and in the conclusion. If the name is some \( x_0 \) other than \( x \), the box needs the line \( P(x_0) \), and the search finds nothing that gives it: the premise is about \( x \), and no line mentions \( x_0 \). A stalled search proves nothing by itself, since a cleverer derivation might exist. By (b), none should exist: \( P(x) \vdash \forall x\, P(x) \) would lead from a true premise to a false conclusion. Section 4.11 turns this reading into a counter-model for the sequent \( P(x_0) \vdash \forall x\, P(x) \), with \( x_0 \) naming \( 2 \); the same reading with \( x \) naming \( 2 \) is a counter-model for \( P(x) \vdash \forall x\, P(x) \), and the soundness statement given there (proved in the optional Section 4.12) then shows that \( P(x) \nvdash \forall x\, P(x) \).

**Marking scheme.** (10 points)
- 3: (a) the derivation, with each of the five clauses checked, including that \( x \) is free for \( x \).
- 2: (b) a reading with \( P(x) \) true and \( \forall x\, P(x) \) false, the value of \( x \) stated.
- 3: (c) the flag \( x \) fails "not in the conclusion"; the fix instantiates at a fresh \( x_0 \) inside the box.
- 2: (c) for the premise \( P(x) \): the name \( x \) fails the side condition, and for a different name the search stalls, with the pointer to Section 4.11 for non-derivability.
Fatal errors (0 for the step): claiming the flag \( x \) is fine because \( x \) is bound in the conclusion; treating \( P(x) \) and \( P(x_0) \) as the same line.
:::

<!-- dependency ledger
def-rule-universal-elimination (claim): the domain is never empty, so every term names an element | Section 4.1 (domain convention, stated there); made exact in Section 4.11, prose pointer only
def-rule-universal-elimination (claim): the rule never leads from true premises to a false line | NOT proved here: stated in Section 4.11, proved in optional Section 4.12; prose pointer only, nothing here rests on it
def-rule-universal-elimination (claim): x not free in phi gives phi[t/x] = phi | Section 4.2 (claim after def-substitution), recalled in prose
def-rule-universal-elimination (example): Section 1.4's instance of "a < b and b < c give a < c" and exm-raa-zero's epsilon = x/2 are forall-E steps | Section 1.4 (def-rule-implication-elimination's example), exm-raa-zero (cited)
exm-universal-elimination-derivations (example): over N, f(n) = n + 2, 0 even, f(f(0)) = 4 | school arithmetic; checked by verify/ch04/exm-universal-elimination-derivations.py
def-rule-universal-elimination (example): in "How this rule looks", (a - 1)^2 = a^2 - 2a + 1; y^2 >= 0 for real y | school algebra, stated as such ("arith"); checked by verify/ch04/def-rule-universal-elimination.py
def-rule-universal-elimination (claim): the arith convention: an arith line abbreviates a universally quantified arithmetic premise, forall-E at the line's terms and ->E | inline convention, stated in the text; the same convention is recalled in Section 4.12
def-rule-universal-elimination (example): in "Common errors", over N, x + 1 != x; not every n >= 1 (0); 1 >= 1 and 1 != 0; over R, x <= x^2 for x >= 1, so x <= x^2 or x < 1 for all x; at x = 1, 2 <= 1 and 1 < 1 fail | school arithmetic; checked by verify/ch04/def-rule-universal-elimination.py
def-rule-universal-elimination (claim): in "A stall", apart from bot-E and RAA a line beginning with forall comes out of a line or box containing it; no finite list of instances derives forall x P(x) with the rules so far | informal remark, not a theorem (bot-E and RAA by @def-rules-contradiction, @def-rule-raa); the stall is resolved in Section 4.4 (prose pointer)
def-rule-universal-elimination (claim): renaming a bound variable to a letter that appears nowhere gives the same statement, so one can rename before substituting (Quick check, "Common errors", search step) | Section 4.2 (renaming convention, after def-free-for; no label), recalled in prose
exm-universal-elimination-derivations (example): a term with no variables (c, f(c)) is free for every variable | Section 4.2 (special cases after def-free-for), recalled
exr-universal-elimination-a1 (solution): f(c) has no variables, so it is free for x | Section 4.2 (special cases after def-free-for), recalled
exr-universal-elimination-b3 (solution): every term is free for x in a formula with no quantifier | def-free-for (recursive description: atomic formulas and connectives), recalled
exr-universal-elimination-c1 (solution): constants are free for every variable | Section 4.2 (special cases after def-free-for), recalled
exr-universal-elimination-a1 (solution): over Z, exists y (y > x) true for all x, exists y (y > y) false; over R, 3 * (-1) < 0; over N, 0 >= 1 false, 1 >= 1 true | school arithmetic; checked by verify/ch04/exr-universal-elimination-a1.py
exr-universal-elimination-b3 (solution): (a - b)^2 = a^2 - 2ab + b^2; (a + b)^2 >= 0 gives a^2 + b^2 >= -2ab | school algebra ("arith"); checked by verify/ch04/exr-universal-elimination-b3.py
exr-universal-elimination-c1 (solution): on {0, 1}, the relation {(0, 0)} is symmetric and transitive, and (1, 1) is not in it | inline (finite check); checked by verify/ch04/exr-universal-elimination-c1.py
exr-universal-elimination-c2 (solution): over Z, 2 is even and 1 is odd | school arithmetic
exr-universal-elimination-c2 (solution): x is free for x in every formula; "appear" includes the variable after a quantifier | Section 4.2 (special cases after def-free-for; the definition of "appear" after def-free-variable), recalled
exr-universal-elimination-c2 (solution): the forall-I side condition, quoted in the item | stated in the item itself; Section 4.4 (prose pointer), not used as a step
exr-universal-elimination-c2 (solution): P(x) does not derive forall x P(x); the search explanation is informal | NOT proved here: Section 4.11 gives the counter-model for P(x0) |- forall x P(x) (Z, evens, x0 names 2) and the soundness statement, proved in optional Section 4.12; the same structure with x naming 2 is the counter-model here (adaptation stated in the solution); prose pointer only, nothing depends on it
-->
