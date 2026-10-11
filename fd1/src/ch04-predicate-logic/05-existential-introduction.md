# Proving "There Exists": Exhibit a Witness

Sections 4.3 and 4.4 gave the two rules for "for every": \( \rulename{\forall E} \) uses a universal statement, and \( \rulename{\forall I} \) proves one. This section starts on the other quantifier. It gives the rule that **proves** an existential statement, \( \rulename{\exists I} \), and the habit that goes with it: when the goal is "there exists", do not guess the object, but wait until a line of the derivation shows it. Section 4.4 left open a sequent that no rule so far could finish, \( \forall x\, P(x) \vdash \exists x\, P(x) \); it is finished here in three lines.

## Showing that something exists

How does a mathematician prove that there is a natural number \( N \) with \( 1/(N + 1) < 1/100 \)? By naming one. "Take \( N = 100 \): then \( 1/(N + 1) = 1/101 \), and \( 1/101 < 1/100 \)." Nobody asks for more, and nobody objects that \( N = 1000 \) would also have done. The proof exhibits a **witness**, checks that it has the property, and stops.

Look at what the proof does with the witness at the end. The statement proved, "there is an \( N \) with \( 1/(N + 1) < 1/100 \)", does not say which \( N \); the \( 100 \) still in it belongs to the bound \( 1/100 \), not to \( N \). The number was needed to establish the claim and is then forgotten: a reader of the conclusion learns that some \( N \) works, not which one.

Chapter 1 used the same pattern from its first page. It recalled that an integer \( n \) is **even** when \( n = 2k \) for **some** integer \( k \), and said that the word "some" has rules of its own, to come in Chapter 4. Here is the first of them. To show that \( 6 \) is even, take \( k = 3 \): then \( 6 = 2 \cdot 3 \). The statement "\( 6 \) is even" is \( \exists k\, (6 = 2 \cdot k) \), and the proof passes from the instance \( 6 = 2 \cdot 3 \) to it. The second rule for "some", how to **use** "\( n = 2k \) for some \( k \)", is the subject of Section 4.6.

There is a helpful way to see the step, which Section 4.1's reading of \( \exists \) suggests. Over a domain with three elements named \( a \), \( b \), \( c \), the sentence \( \exists x\, P(x) \) says what the disjunction
\[
P(a) \vee P(b) \vee P(c)
\]
says (grouped to the right, as in Section 3.4): at least one of the three has \( P \). An existential is a long "or", with one disjunct for each object of the domain. Proving a disjunction from one of its sides is \( \rulename{\vee I} \) (@def-rule-disjunction-introduction), and proving an existential from one instance is the rule of this section. The analogy is only a guide (a domain such as \( \nN \) has infinitely many elements, and a formula cannot be infinitely long), but it predicts the rule's behavior exactly: it throws information away, and it must never be run backwards.

## The rule of existential introduction

*To prove that something has a property, show that one particular thing has it.*

::: {#def-rule-existential-introduction}
[Existential Introduction]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {\varphi[t/x]}
  \have {k} {\exists x\, \varphi} \Ei{i}
\end{nd}$
\end{center}
```

The rule given by this schema is called \( \rulename{\exists I} \) (**existential introduction**). Here \( \varphi \) is **any** formula, \( x \) any variable, and \( t \) **any** term, subject to one side condition: **\( t \) is free for \( x \) in \( \varphi \)** (@def-free-for). Line \( i \) must be available at line \( k \) (@def-derivation).
:::

In words, clause by clause.

1. **One given line, no box.** The rule cites one available line, as \( \rulename{\vee I} \) does. Like \( \rulename{\forall E} \) of Section 4.3, it opens no box and introduces no fresh name.
2. **The cited line is an instance.** Line \( i \) must have the form \( \varphi[t/x] \): the formula \( \varphi \) with the term \( t \) put in for every free occurrence of \( x \) (@def-substitution). The term \( t \) is the **witness**.
3. **The rule reads the cited line backwards.** The line \( \varphi[t/x] \) is given, and \( \varphi \) is not: we choose it. In practice we look at the cited line, choose a variable \( x \) that does not appear in it (Section 4.2), and replace some of the occurrences of \( t \) by \( x \); the result is \( \varphi \), and \( \varphi[t/x] \) is then the cited line. If \( x \) does appear in the line, this recipe can fail (from \( R(x, c) \), marking \( c \) gives \( \varphi = R(x, x) \), and \( \varphi[c/x] = R(c, c) \) is not the line), so check directly that \( \varphi[t/x] \) is exactly the cited line. In every case check clause 5. One line is an instance of many formulas, so one line has many existential conclusions. The table below shows this.
4. **Any term.** The witness may be a constant (\( 3 \), \( c \)), a compound term (\( f(c) \), \( 2k + 1 \)), or a **variable**: a variable that appears elsewhere in the derivation, a fresh name of a flagged box such as \( x_0 \), or even the variable \( x \) itself. No box is needed for any of these. The rule never asks where \( t \) came from.
5. **Free for \( x \).** The only restriction is the condition of @def-free-for, the same one that \( \rulename{\forall E} \) carries. Its job is shown by the nonexample below.

**One line, several readings.** Let line \( i \) be \( R(c, c) \), with \( R \) a two-place predicate symbol and \( c \) a constant. The witness is \( c \), and \( c \) occurs twice. Each occurrence may be marked with \( x \) or left alone, and each choice is a different \( \varphi \):

| \( \varphi \) | \( \varphi[c/x] \) (the cited line) | the new line \( \exists x\, \varphi \) |
|---|---|---|
| \( R(x, c) \) | \( R(c, c) \) | \( \exists x\, R(x, c) \) |
| \( R(c, x) \) | \( R(c, c) \) | \( \exists x\, R(c, x) \) |
| \( R(x, x) \) | \( R(c, c) \) | \( \exists x\, R(x, x) \) |
| \( R(c, c) \) | \( R(c, c) \) | \( \exists x\, R(c, c) \) |

All four are legal steps. Read over \( \nN \) with \( R(x, y) \) as "\( x \le y \)" and \( c \) as \( 5 \): the cited line says \( 5 \le 5 \), and the three useful conclusions say that something is at most \( 5 \), that \( 5 \) is at most something, and that something is at most itself. Each is a true and weaker statement. The last row is the **degenerate** choice: \( \varphi \) has no free \( x \), so \( \varphi[c/x] \) is \( \varphi \) (Section 4.2) and the new line \( \exists x\, R(c, c) \) quantifies over nothing. It is legal, and it says nothing that line \( i \) did not.

**Why this rule.** Under the reading of Section 4.1, \( \exists x\, \varphi \) is true when at least one element of the domain, put in for \( x \), makes \( \varphi \) true. If \( \varphi[t/x] \) is true, then the object that \( t \) names is such an element, so \( \exists x\, \varphi \) is true. The side condition is what makes "\( \varphi[t/x] \) says about \( t \) what \( \varphi \) says about \( x \)" correct: that was the content of "free for" in Section 4.2. Section 4.12 turns this sentence into a proof.

*\( \rulename{\exists I} \) forgets the witness, and keeps the truth.*

**A nonexample: capture.** Let line 1 be \( \forall y\, R(y, y) \). With \( \varphi = \forall y\, R(x, y) \) and \( t = y \), the definition of substitution gives \( \varphi[y/x] = \forall y\, R(y, y) \), which is line 1. So it is tempting to write \( \exists x\, \forall y\, R(x, y) \) by \( \rulename{\exists I} \).

```{=latex}
\begin{center}
% expect-invalid
$\begin{nd}
  \hypo {1} {\forall y\, R(y, y)}
  \have {2} {\exists x\, \forall y\, R(x, y)} \Ei{1}
\end{nd}$
\end{center}
```

Line 2 breaks the side condition: the free occurrence of \( x \) in \( \varphi \) lies in the scope of \( \forall y \), and \( y \) is the variable of the term \( t \), so \( y \) is **not** free for \( x \) in \( \varphi \). The step would be wrong. Read over \( \nZ \) with \( R(x, y) \) as "\( x \le y \)": line 1 says that every integer is at most itself, which is true, and line 2 says that some integer is at most every integer, that is, that there is a least integer, which is false. The \( y \) put in for \( x \) was meant to name one object, and it was captured by \( \forall y \) and made to range over all of them.

::: {.warning}
The witness must be **written on a line**. "There is an \( N \) with \( 1/(N + 1) < 1/100 \): take \( N \) large enough" is not an application of \( \rulename{\exists I} \), because "large enough" is not a term, and the rule asks for an instance \( \varphi[t/x] \) on an available line. In a written proof, "large enough" is a promise to name the witness, and the promise is kept by a term such as \( N = 100 \), followed by the check that it works (\( 1/101 < 1/100 \)). Until then nothing has been proved.
:::

::: {.check}
Let line 1 be \( 2 + 2 = 4 \). Which of
\[
\exists x\, (x + x = 4), \qquad \exists x\, (x + 2 = 4), \qquad \exists x\, (2 + 2 = x)
\]
may line 2 be, justified by one application of \( \rulename{\exists I} \) to line 1? For each that may, name \( \varphi \) and the witness \( t \).
:::

::: {.solution}
All three. For \( \exists x\, (x + x = 4) \), take \( \varphi = (x + x = 4) \) and \( t = 2 \): both \( 2 \)'s of line 1 are marked. For \( \exists x\, (x + 2 = 4) \), take \( \varphi = (x + 2 = 4) \) and \( t = 2 \): only the first \( 2 \) is marked, and the second is written out in \( \varphi \). For \( \exists x\, (2 + 2 = x) \), take \( \varphi = (2 + 2 = x) \) and \( t = 4 \): the witness is a different term. In each case \( \varphi[t/x] \) is exactly line 1, and \( \varphi \) has no quantifier, so \( t \) is free for \( x \).
:::

## From "for every" to "there exists"

Section 4.4 left \( \forall x\, P(x) \vdash \exists x\, P(x) \) open. It looks like the easiest sequent in the chapter, and it has a small puzzle in it. To use \( \rulename{\exists I} \), the goal needs an instance \( P(t) \) on a line. The premise gives an instance for every term, by \( \rulename{\forall E} \). But the sequent mentions no constant, so which term?

::: {#prp-forall-implies-exists}
[Every Implies Some]

\( \forall x\, P(x) \vdash \exists x\, P(x) \).
:::

::: {.proof}
The following is a derivation.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, P(x)}
  \have {2} {P(x)} \Ae{1}
  \have {3} {\exists x\, P(x)} \Ei{2}
\end{nd}$
\end{center}
```

Line 2 is \( \rulename{\forall E} \) at the term \( x \): with \( \varphi = P(x) \), the instance \( \varphi[x/x] \) is \( P(x) \), and the variable \( x \) is free for \( x \) in every formula (Section 4.2). Line 3 is \( \rulename{\exists I} \) with the same \( \varphi \) and the witness \( x \). This proves the proposition.
:::

The puzzle is answered by clause 4 of the reading of @def-rule-existential-introduction: a variable is a term, so no constant is needed. The line \( P(x) \) has \( x \) free; it says that \( P \) holds of whatever \( x \) names. Nothing in the derivation says what that is, and nothing needs to. The same three lines prove \( \forall x\, \varphi \vdash \exists x\, \varphi \) for every formula \( \varphi \), since \( \varphi[x/x] = \varphi \) (Section 4.2).

::: {.remark}
The rules accept this derivation in any case; it leads from a true premise to a true conclusion only because every domain has **at least one** element, the convention of Section 4.1. Over an empty domain, \( \forall x\, P(x) \) would be true with nothing to check and \( \exists x\, P(x) \) false with no witness; the convention enters at line 2, where \( P(x) \) treats \( x \) as naming an object, and there must be one to name. Section 4.11 explains why the book keeps the convention.
:::

This does not clash with the empty set of Section 4.1, where \( \forall x \in \emptyset\; \varphi \) is true and \( \exists x \in \emptyset\; \varphi \) is false. A bounded quantifier is an abbreviation (@def-bounded-quantifier): \( \forall x \in \emptyset\; \varphi \) is \( \forall x\, (x \in \emptyset \to \varphi) \), and \( \exists x \in \emptyset\; \varphi \) is \( \exists x\, (x \in \emptyset \wedge \varphi) \). The domain is still non-empty; it is the set \( \emptyset \) that has no elements. Running the three lines on the bounded premise gives \( \rulename{\forall E} \) at \( x \), the line \( x \in \emptyset \to \varphi \), and then \( \rulename{\exists I} \) gives only \( \exists x\, (x \in \emptyset \to \varphi) \), an existential with \( \to \) inside. No line \( x \in \emptyset \) is available to fire the implication, so the bounded "every implies some" is not derived, and it should not be.

## An existential goal: postpone the witness

The search method of Section 2.6 asks two questions at each gap: what is the goal, and what are the resources? Sections 4.3 and 4.4 added a step for each side of \( \forall \). Now \( \exists \) can be a goal.

If the goal is \( \exists x\, \varphi \), its last line can be \( \rulename{\exists I} \), and then the new goal is \( \varphi[t/x] \) for a term \( t \) **of our choosing**. That is the same situation as a goal \( \varphi \vee \psi \), where \( \rulename{\vee I} \) left us to choose a side, and the danger is the same. A wrong \( t \) can leave a goal that does not follow from the resources, although the existential does. Section 2.6 met the danger for \( \vee \) and answered it by postponing; the answer here is the same.

*Postpone the witness: choose the term \( t \) of a goal \( \exists x\, \varphi \) only when an available line shows an instance \( \varphi[t/x] \).*

Until then, work on the premises and on the other goals, and watch what terms appear. Often the witness is a term that only appears late, built by \( \rulename{\forall E} \) or \( \rulename{{\to}E} \) from the premises. Here are four derivations, in order of difficulty, each with an Idea that says why each rule was chosen.

::: {#exm-existential-introduction-derivations}
[Derivations with existential introduction]

Show that:

::: {.enumerate options="label=(\alph*)"}
1. \( P(c) \wedge Q(c) \vdash \exists x\, \bigl( P(x) \wedge Q(x) \bigr) \);
2. \( R(c, c) \vdash \exists x\, R(x, c) \wedge \exists x\, R(x, x) \); and decide whether one \( \rulename{\exists I} \) step leads from \( \exists x\, R(x, x) \) to \( \exists x\, R(x, c) \);
3. \( \forall x\, R(x, x) \vdash \forall x\, \exists y\, R(x, y) \);
4. \( \forall x\, \bigl( P(x) \to Q(f(x)) \bigr), \ P(c) \vdash \exists y\, Q(y) \).
:::
:::

::: {.solution}
(a) *Idea.* The goal is an existential, and the premise already is an instance of a suitable \( \varphi \): mark both occurrences of \( c \). One goal-directed step finishes.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P(c) \wedge Q(c)}
  \have {2} {\exists x\, (P(x) \wedge Q(x))} \Ei{1}
\end{nd}$
\end{center}
```

Here \( \varphi = P(x) \wedge Q(x) \) and \( t = c \). Marking only the first \( c \), with \( \varphi = P(x) \wedge Q(c) \), would give the legal but weaker line \( \exists x\, (P(x) \wedge Q(c)) \), which is not the goal.

(b) *Idea.* The goal is a conjunction, so it splits into two goals (Section 1.3), and each is an existential with the line \( R(c, c) \) as an instance, read in two different ways (the first and third rows of the table above).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {R(c, c)}
  \have {2} {\exists x\, R(x, c)} \Ei{1}
  \have {3} {\exists x\, R(x, x)} \Ei{1}
  \have {4} {\exists x\, R(x, c) \wedge \exists x\, R(x, x)} \ai{2,3}
\end{nd}$
\end{center}
```

Line 2 uses \( \varphi = R(x, c) \) and line 3 uses \( \varphi = R(x, x) \), both with the witness \( c \).

Now the second question. From the line \( \exists x\, R(x, x) \), the step to \( \exists x\, R(x, c) \) is **not** an \( \rulename{\exists I} \) step. The new line is \( \exists x\, \varphi \) with \( \varphi = R(x, c) \), so the cited line would have to be \( R(t, c) \) for some term \( t \). The line \( \exists x\, R(x, x) \) is not of that form: its main symbol is \( \exists x \), not \( R \). The rule passes from an **instance** to an existential, never from one existential to another. Nor is the step safe by any other route: read over \( \nZ \) with \( R(x, y) \) as "\( x \cdot y = 1 \)" and \( c \) as \( 0 \), the line \( \exists x\, R(x, x) \) is true (take \( x = 1 \)), and \( \exists x\, R(x, c) \), "some integer times \( 0 \) is \( 1 \)", is false.

(c) *Idea.* The goal is a \( \forall \), so the step of Section 4.4 opens a flagged box with a fresh name \( x_0 \), and the new goal is \( \exists y\, R(x_0, y) \). That is an existential: postpone it and look at the premise. The premise is a \( \forall \); instantiate it at the term the goal mentions, \( x_0 \). The result, \( R(x_0, x_0) \), shows the witness: it is \( x_0 \) itself, a variable used as a term, as \( x \) was in @prp-forall-implies-exists.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, R(x, x)}
  \open[x_0]
  \have {2} {R(x_0, x_0)} \Ae{1}
  \have {3} {\exists y\, R(x_0, y)} \Ei{2}
  \close
  \have {4} {\forall x\, \exists y\, R(x, y)} \Ai{2-3}
\end{nd}$
\end{center}
```

Line 3 uses \( \varphi = R(x_0, y) \), the variable \( y \), and the witness \( x_0 \); it marks the second occurrence of \( x_0 \) and keeps the first. Line 4 is \( \rulename{\forall I} \) with the flag \( x_0 \) (@def-rules-universal): \( x_0 \) appears in no premise, there is no open assumption, and \( x_0 \) does not appear in line 4. The \( \rulename{\exists I} \) inside the box needed no box of its own, although its witness is a fresh name. Read over \( \nN \) with \( R(x, y) \) as "\( x \le y \)": every number is at most itself, so every number is at most something.

(d) *Idea.* The goal \( \exists y\, Q(y) \) is an existential, and no line yet has the form \( Q(t) \). Postpone, and work forwards. The premise \( \forall x\, (\dots) \) is a \( \forall \); the only term in sight is \( c \), so instantiate at \( c \) (Section 4.3), and \( \rulename{{\to}E} \) with the premise \( P(c) \) fires. The result \( Q(f(c)) \) shows the witness: the compound term \( f(c) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(f(x)))}
  \hypo {2} {P(c)}
  \have {3} {P(c) \to Q(f(c))} \Ae{1}
  \have {4} {Q(f(c))} \ie{3,2}
  \have {5} {\exists y\, Q(y)} \Ei{4}
\end{nd}$
\end{center}
```

Line 5 uses \( \varphi = Q(y) \) and \( t = f(c) \). Now see what choosing the witness first would have done. The term in sight at the start is \( c \), and "take \( y = c \)" leaves the goal \( Q(c) \). Nothing gives it: the premise speaks of \( Q \) only at terms of the form \( f(\dots) \), and \( Q(c) \) need not hold at all. Read over \( \nZ \) with \( P \) as "odd", \( Q \) as "even", \( f(x) \) as \( x + 1 \), and \( c \) as \( 3 \): the premises say that the successor of every odd integer is even and that \( 3 \) is odd, the conclusion says that some integer is even, and the witness the derivation finds is \( f(3) = 4 \), while \( Q(c) \) says that \( 3 \) is even. The search stalls exactly because it chose the witness before the derivation had produced it.
:::

The four Ideas share a pattern. In (a) and (b) the witness stood on a premise line from the start; in (c) and (d) it appeared only after other rules had run, and in (d) it was a term that no line mentioned at the start. Postponing costs nothing in (a) to (c), where the right witness was already a term in sight when the existential goal appeared (in (c) the goal names \( x_0 \)), and it is necessary in (d), where the only term in sight at the start, \( c \), is the wrong witness.

## How this rule looks in a mathematical proof

In a written proof, \( \rulename{\exists I} \) is the word "take", followed by a check. "\( 6 \) is even: take \( k = 3 \); then \( 6 = 2 \cdot 3 \)." Over \( \nZ \), with one line of school arithmetic justified "arith" as in Section 4.3:

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {6 = 2 \cdot 3} \by{arith}{}
  \have {2} {\exists k\, (6 = 2 \cdot k)} \Ei{1}
\end{nd}$
\end{center}
```

Line 2 marks the \( 3 \) with \( k \), and keeps the \( 6 \) and the \( 2 \): \( \varphi = (6 = 2 \cdot k) \). In the same way "\( 7 \) is odd: take \( k = 3 \), since \( 7 = 2 \cdot 3 + 1 \)" is an \( \rulename{\exists I} \) with \( \varphi = (7 = 2 \cdot k + 1) \).

**A bounded witness.** Analysis states its existentials with bounds. "There is an \( N \in \nN \) with \( 1/(N + 1) < 1/100 \)" abbreviates \( \exists N\, \bigl( N \in \nN \wedge 1/(N + 1) < 1/100 \bigr) \) (@def-bounded-quantifier), so the witness must satisfy both conjuncts. Taking \( N = 100 \) is two steps: \( \rulename{\wedge I} \) puts the bound and the inequality together, and \( \rulename{\exists I} \) forgets the witness.

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {100 \in \nN} \by{arith}{}
  \have {2} {1/(100 + 1) < 1/100} \by{arith}{}
  \have {3} {100 \in \nN \wedge 1/(100 + 1) < 1/100} \ai{1,2}
  \have {4} {\exists N\, (N \in \nN \wedge 1/(N + 1) < 1/100)} \Ei{3}
\end{nd}$
\end{center}
```

Line 4 marks two of the three occurrences of \( 100 \) in line 3 and keeps the one on the right. Section 4.8 folds lines 3 and 4 into a single bounded step. The witness \( 100 \) is the least that works, since \( N = 99 \) gives \( 1/100 \), which is not less than \( 1/100 \); but the proof does not need the least witness, only one.

**A witness built from what is available.** Often the witness is a term made from other names. To show that for every integer \( n \) there is an odd integer greater than \( 2n \), a proof says "let \( n \) be an integer; \( 2n + 1 \) will do, since it is odd and greater than \( 2n \)". The words "let \( n \) be an integer" open the flagged box of Section 4.4, and "\( 2n + 1 \) will do" is \( \rulename{\exists I} \) with the compound witness \( 2n + 1 \), as in (d) above. In general, the witness may be any term the reader can check.

::: {.warning}
\( \rulename{\exists I} \) runs one way only. From \( P(c) \) it gives \( \exists x\, P(x) \); from \( \exists x\, P(x) \) it gives nothing, and in particular not \( P(c) \). "Some integer is even" is true and "\( 3 \) is even" is false: the existential does not say **which** object has the property, so it cannot be read back as a statement about a named one. Using an existential takes a rule of its own, with a box, and that is Section 4.6.
:::

## What the rule sounds like

Here is the row of the rule, phrase and Lean table for \( \rulename{\exists I} \); nothing later depends on the last column, and Section 4.7 collects the whole table.

| Rule | You write | Lean |
|------|--------------------------------------|------------------------|
| \( \rulename{\exists I} \) | "Take \( x = t \). Then …"; "\( 2k + 1 \) will do." | `use t` (or `Exists.intro t h`) |

The phrase names the witness and then checks it. A proof that names the witness without the check ("take \( N = 100 \).") has written the line \( \exists x\, \varphi \) without the instance \( \varphi[t/x] \) it cites; the reader must supply the instance, and should be able to.

**The search method: one more step.** Each rule section adds a step to the method of Section 2.6, and Section 4.8 collects them.

- **Goal \( \exists x\, \varphi \).** Postpone. Work on the premises and on other goals until an available line is an instance \( \varphi[t/x] \), with \( t \) free for \( x \) in \( \varphi \); then \( \rulename{\exists I} \). The witness may be a compound term that appears only after other rules have run, as \( f(c) \) did in (d).

## Exercises

### A. Check your understanding

::: {#exr-existential-introduction-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State \( \rulename{\exists I} \) as a schema, with its side condition.
2. Line 1 of a derivation is \( R(c, f(c)) \). Which of the following may line 2 be, by one application of \( \rulename{\exists I} \) to line 1? For each that may, give \( \varphi \) and the witness \( t \); for each that may not, say why.
   (i) \( \exists x\, R(x, f(c)) \); (ii) \( \exists x\, R(c, x) \); (iii) \( \exists x\, R(x, f(x)) \); (iv) \( \exists x\, R(x, x) \); (v) \( \exists x\, R(f(c), x) \).
3. Line 1 of a derivation is \( \forall y\, (y \le y \cdot y) \). Is \( \exists x\, \forall y\, (y \le x \cdot x) \) a legal \( \rulename{\exists I} \) step from line 1? Read both lines over \( \nZ \): which is true?
4. True or false, with a reason: from the line \( \exists x\, P(x) \), one application of \( \rulename{\exists I} \) gives \( P(c) \).
5. The current goal of a search is \( \exists x\, \varphi \) and no available line is an instance of \( \varphi \). What does the search method say to do, and why not choose a witness now?
:::
:::

::: {.solution}
*(a)* From \( \varphi[t/x] \) on an available line \( i \), write \( \exists x\, \varphi \) on line \( k \), justified "\( \rulename{\exists I} \) \( i \)". Side condition: \( t \) is free for \( x \) in \( \varphi \).

*(b)* (i) Yes: \( \varphi = R(x, f(c)) \), \( t = c \); only the first \( c \) is marked. (ii) Yes: \( \varphi = R(c, x) \), \( t = f(c) \); the witness is the compound term. (iii) Yes: \( \varphi = R(x, f(x)) \), \( t = c \); both occurrences of \( c \) are marked, and \( \varphi[c/x] \) is \( R(c, f(c)) \). (iv) No: the conclusion fixes \( \varphi = R(x, x) \), whose instances \( R(t, t) \) have equal arguments, while the arguments \( c \) and \( f(c) \) of line 1 differ. (v) No: the conclusion fixes \( \varphi = R(f(c), x) \), whose instances \( R(f(c), t) \) have \( f(c) \) as first argument, while line 1 has \( c \) there. (Read over \( \nN \) with \( R(x, y) \) as "\( x < y \)", \( f(x) \) as \( x + 1 \), and \( c \) as \( 0 \): line 1 says \( 0 < 1 \), and (v) says that something exceeds \( 1 \), true but not by this step; (iv) says that some number is less than itself, which is false.)

*(c)* No. With \( \varphi = \forall y\, (y \le x \cdot x) \), the formula \( \varphi[y/x] \) is line 1, so the witness would be the variable \( y \); but the free occurrences of \( x \) in \( \varphi \) lie in the scope of \( \forall y \), so \( y \) is not free for \( x \) in \( \varphi \). Over \( \nZ \), line 1 is true: for \( y \le 0 \), \( y \le 0 \le y \cdot y \), and for \( y \ge 1 \), \( y \le y \cdot y \) after multiplying \( 1 \le y \) by \( y > 0 \). The other line is false: whatever integer \( x \) is proposed, \( y = x \cdot x + 1 \) gives \( y > x \cdot x \). So the step would lead from a true line to a false one, which is what the side condition prevents.

*(d)* False. \( \rulename{\exists I} \) concludes an existential from an instance; it never concludes an instance. The line \( P(c) \) does not follow from \( \exists x\, P(x) \) at all: over \( \nZ \) with \( P \) as "even" and \( c \) as \( 3 \), the first is true and the second false.

*(e)* Postpone the goal: work on the premises (\( \rulename{\forall E} \) at the terms the goal mentions, \( \rulename{{\to}E} \), and so on) until a line \( \varphi[t/x] \) appears, then use \( \rulename{\exists I} \). A witness chosen now leaves the goal \( \varphi[t/x] \), which may not follow from the resources even when \( \exists x\, \varphi \) does, as "take \( y = c \)" did in @exm-existential-introduction-derivations (d).
:::

### B. Practice

::: {#exr-existential-introduction-b1}
[B1]

Derive \( \forall x\, \bigl( P(x) \to Q(x) \bigr), \ P(a) \vdash \exists x\, \bigl( P(x) \wedge Q(x) \bigr) \). In the Idea, say which rule each line was chosen by: the goal or a premise.
:::

::: {.solution}
*Idea.* The goal is an existential: postpone it. The premise \( \forall x\, (\dots) \) is instantiated at the only term in sight, \( a \), and \( \rulename{{\to}E} \) with \( P(a) \) gives \( Q(a) \); both steps are premise-directed. Now the witness \( a \) is visible, and the instance the goal needs is \( P(a) \wedge Q(a) \), which \( \rulename{\wedge I} \) builds. The last step is the postponed \( \rulename{\exists I} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {P(a)}
  \have {3} {P(a) \to Q(a)} \Ae{1}
  \have {4} {Q(a)} \ie{3,2}
  \have {5} {P(a) \wedge Q(a)} \ai{2,4}
  \have {6} {\exists x\, (P(x) \wedge Q(x))} \Ei{5}
\end{nd}$
\end{center}
```

Line 6 uses \( \varphi = P(x) \wedge Q(x) \) and the witness \( a \).
:::

::: {#exr-existential-introduction-b2}
[B2]

Over \( \nR \), with the premise \( \forall x\, \bigl( x + (-x) = 0 \bigr) \), derive \( \forall x\, \exists y\, (x + y = 0) \), the true sentence (i) of @exm-quantifier-order-sum. Say what the witness is, and what it depends on.
:::

::: {.solution}
*Idea.* The goal is a \( \forall \): open a flagged box with a fresh name \( x_0 \) (Section 4.4); the new goal is \( \exists y\, (x_0 + y = 0) \). Postpone it, and instantiate the premise at the term the goal mentions, \( x_0 \). The line \( x_0 + (-x_0) = 0 \) shows the witness: \( -x_0 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (x + (-x) = 0)}
  \open[x_0]
  \have {2} {x_0 + (-x_0) = 0} \Ae{1}
  \have {3} {\exists y\, (x_0 + y = 0)} \Ei{2}
  \close
  \have {4} {\forall x\, \exists y\, (x + y = 0)} \Ai{2-3}
\end{nd}$
\end{center}
```

Line 3 uses \( \varphi = (x_0 + y = 0) \) and the witness \( -x_0 \), which contains no variable bound in \( \varphi \). At line 4, \( x_0 \) appears in no premise, there is no open assumption, and \( x_0 \) does not appear in the conclusion, so \( \rulename{\forall I} \) applies (@def-rules-universal).

The witness \( -x_0 \) is built from \( x_0 \), so it depends on \( x_0 \): a different number for each \( x \). That is legal, because \( \rulename{\exists I} \) is applied **inside** the box, where \( x_0 \) is available as a term. It is the box picture of the game of Section 4.1: the \( \exists y \) is played after the \( \forall x \), and may use it.
:::

::: {#exr-existential-introduction-b3}
[B3]

Over \( \nZ \), prove "there is an integer \( n \) with \( n^2 = n + 2 \)" as a derivation whose only line not justified by a rule is one line of arithmetic justified "arith"; write \( n^2 \) as \( n \cdot n \). Then write the proof as one sentence.
:::

::: {.solution}
The witness \( 2 \) works, since \( 2 \cdot 2 = 4 = 2 + 2 \).

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {2 \cdot 2 = 2 + 2} \by{arith}{}
  \have {2} {\exists n\, (n \cdot n = n + 2)} \Ei{1}
\end{nd}$
\end{center}
```

Line 2 uses \( \varphi = (n \cdot n = n + 2) \) with the witness \( 2 \). Line 1 contains four \( 2 \)'s, and \( \varphi \) marks three of them: both factors on the left and the first term of the sum on the right. The last \( 2 \) is the constant of the statement and stays. Marking all four would give \( \exists n\, (n \cdot n = n + n) \), a different statement.

In one sentence: *Take \( n = 2 \); then \( n^2 = 4 = n + 2 \).*

The witness \( -1 \) works too, since \( (-1) \cdot (-1) = 1 = -1 + 2 \); a proof needs only one.
:::

### C. Going deeper

::: {#exr-existential-introduction-c1}
[C1: The conclusion clause of for-all-introduction]

The side condition of \( \rulename{\forall I} \) (@def-rules-universal) has three clauses about the flag \( x_0 \): it appears in no premise, in no assumption of a box still open at the \( \rulename{\forall I} \) line, and not in the conclusion \( \forall x\, \varphi \). Show that the third clause is needed: give a "derivation" that breaks **only** that clause, from a premise that is true over \( \nN \) to a sentence (@def-sentence) that is false over \( \nN \). Check that every other step is legal.
:::

::: {.solution}
[Hint 1]

The conclusion of the illegal \( \rulename{\forall I} \) still mentions the flag, so it is not yet a sentence. Which rule of this section can replace a name on a line by a bound variable?
:::

::: {.solution}
[Hint 2]

Start from the premise \( \forall x\, (x \le x) \), and open a flagged box with the name \( y_0 \).
:::

::: {.solution}
```{=latex}
\begin{center}
% expect-invalid
$\begin{nd}
  \hypo {1} {\forall x\, (x \le x)}
  \open[y_0]
  \have {2} {y_0 \le y_0} \Ae{1}
  \close
  \have {3} {\forall x\, (x \le y_0)} \Ai{2-2}
  \have {4} {\exists y\, \forall x\, (x \le y)} \Ei{3}
\end{nd}$
\end{center}
```

*The illegal line.* Line 3 is \( \rulename{\forall I} \) with the flag \( y_0 \) and \( \varphi = (x \le y_0) \): the instance \( \varphi[y_0/x] \) is \( y_0 \le y_0 \), the last line of the box. The flag \( y_0 \) appears in no premise (line 1 has no \( y_0 \)), and there is no open assumption at all. But \( y_0 \) appears in the conclusion \( \forall x\, (x \le y_0) \), so the third clause fails, and only it.

*The other lines are legal.* Line 2 is \( \rulename{\forall E} \) at the term \( y_0 \), which is free for \( x \) in \( x \le x \) since that formula has no quantifier. Line 4 is \( \rulename{\exists I} \) with \( \varphi = \forall x\, (x \le y) \) and the witness \( y_0 \): \( \varphi[y_0/y] \) is line 3, and \( y_0 \) is free for \( y \) in \( \varphi \), since the only quantifier of \( \varphi \) is on \( x \).

*Over \( \nN \).* Line 1 says that every natural number is at most itself: true. Line 4 says that some natural number is at least every natural number, that is, that there is a largest natural number: false, since for any \( y \), \( x = y + 1 \) is larger.

*What the clause prevents.* The box proved \( y_0 \le y_0 \), a fact about \( y_0 \) in which the two sides are the same name. Line 3 generalized only one side and kept the other, so it claimed that **one** fixed \( y_0 \) is at least every \( x \): a claim about \( y_0 \) that the box never proved. The flag is "let \( y_0 \) be arbitrary"; it must not survive into the statement that "since \( y_0 \) was arbitrary" produces. Line 4 then shows the damage, by turning the leaked name into a witness.

**Marking scheme.** (10 points)
- 3: a derivation whose only illegal line is a \( \rulename{\forall I} \) whose flag appears in its conclusion.
- 2: checks the other two clauses at that line (no premise, no open assumption contains the flag).
- 2: checks the remaining lines (here \( \rulename{\forall E} \) and \( \rulename{\exists I} \), with free-for).
- 3: shows the premise true and the conclusion false over \( \nN \), with the witness of the falsity (\( y + 1 \)).
Fatal errors (0 for the step): a second illegal line (for instance a capture in \( \rulename{\exists I} \)); a premise that is false over \( \nN \).
:::

::: {#exr-existential-introduction-c2}
[C2: A witness is not a name]

Explain why the rules so far (Chapters 1–2 and \( \rulename{\forall E} \), \( \rulename{\forall I} \), \( \rulename{\exists I} \)) cannot derive \( \exists x\, P(x) \vdash P(c) \). Go through the rules that could produce the last line \( P(c) \), and say what each would need. Then say, in one sentence, why no rule for using \( \exists \) **should** give \( P(c) \).
:::

::: {.solution}
The argument below is informal: it explains why every search stalls, and it does not by itself prove that no derivation exists. Section 4.11 gives a model in which the premise is true and \( P(c) \) is false. With the soundness theorem stated there (and proved in the optional Section 4.12), that model shows no derivation exists.

*Which rules could write \( P(c) \).* The line \( P(c) \) is atomic, so no introduction rule writes it: \( \rulename{\wedge I} \), \( \rulename{{\to}I} \), \( \rulename{\vee I} \), \( \rulename{\neg I} \), \( \rulename{{\leftrightarrow}I} \), \( \rulename{\forall I} \) and \( \rulename{\exists I} \) all write a line whose main symbol is their own connective or quantifier. The remaining rules take \( P(c) \) out of something larger: \( \rulename{\wedge E} \) needs a conjunction with \( P(c) \) as a side; \( \rulename{{\to}E} \) needs an implication \( \psi \to P(c) \) and \( \psi \); \( \rulename{{\leftrightarrow}E} \) a biconditional with \( P(c) \) as a side; \( \rulename{\vee E} \) a disjunction and two boxes each ending in \( P(c) \); \( \rulename{\forall E} \) a universal \( \forall x\, \psi \) with \( \psi[c/x] = P(c) \); \( \rulename{\bot E} \) the line \( \bot \); \( \rulename{RAA} \) a box from \( \neg P(c) \) to \( \bot \); and \( \rulename{R} \) the line \( P(c) \) itself.

The derived rules of Chapter 2 abbreviate derivations in these rules (@def-derived-rule), so they add no new way to write \( P(c) \).

*What the premise can supply.* The only premise is \( \exists x\, P(x) \), whose main symbol is \( \exists \). No rule so far looks inside an existential: each elimination rule needs a cited line that is \( \bot \) (for \( \rulename{\bot E} \)) or whose main symbol is \( \wedge \), \( \to \), \( \vee \), \( \leftrightarrow \), \( \neg \) or \( \forall \), and \( \rulename{\exists I} \) produces existentials rather than using them. So the premise can enter a derivation only as a whole: copied, built into a larger formula, set against a line \( \neg\exists x\, P(x) \) by \( \rulename{\neg E} \), or cited as the side \( \psi \) beside a line \( \psi \to \chi \) or \( \psi \leftrightarrow \chi \) by \( \rulename{{\to}E} \) or \( \rulename{{\leftrightarrow}E} \). None of these reaches the information inside it, and the lines the rules above need (a conjunction containing \( P(c) \), an implication ending in it, a biconditional with it as a side, a disjunction for \( \rulename{\vee E} \), a universal with it as an instance, a contradiction) have nowhere to come from. A search therefore stalls at once.

*Why it should stall.* The premise says that **something** has \( P \) and does not say what; the conclusion says that the object named \( c \) has \( P \). Over \( \nZ \) with \( P \) as "even" and \( c \) as \( 3 \), the premise is true and the conclusion false. So no rule for using an existential may give \( P(c) \), and the rule of Section 4.6 does not: it names the witness with a **fresh** variable, about which nothing else is known, instead of with \( c \).

**Marking scheme.** (10 points)
- 3: identifies that \( P(c) \) is atomic, so only elimination rules, \( \rulename{\bot E} \), \( \rulename{RAA} \) or \( \rulename{R} \) can write it, and names what each needs.
- 3: observes that no rule so far uses a line whose main symbol is \( \exists \), so the premise cannot supply what those rules need.
- 2: says that this explains the stall but is not a proof of non-derivability (that needs a counter-model together with soundness, Sections 4.11–4.12).
- 2: gives a reading with the premise true and \( P(c) \) false, and the one-sentence reason (the premise does not say which object has \( P \)).
Fatal errors (0 for the step): claiming that \( \rulename{\exists I} \) read backwards gives \( P(c) \); claiming that a failed search proves the sequent underivable.
:::

<!-- dependency ledger
def-rule-existential-introduction (claim): Why this rule: if phi[t/x] is true and t is free for x in phi, then exists x phi is true | informal reading of Section 4.1 (def-free-for's role, Section 4.2); made exact in Section 4.12 (lem-term-substitution; prose pointer only, nothing depends on it)
def-rule-existential-introduction (claim): the degenerate choice: phi without free x gives phi[c/x] = phi | Section 4.2 (claim after def-substitution: x not free gives phi[t/x] = phi)
def-rule-existential-introduction (example): the capture nonexample: over Z, every integer is <= itself, and there is no least integer | school arithmetic (x - 1 < x); informal truth, Section 4.1
def-rule-existential-introduction (example): the table: over N with R as <= and c as 5, the readings are true | school arithmetic; informal truth, Section 4.1
exm-existential-introduction-derivations (solution): b: over Z with R(x, y) as x * y = 1 and c as 0: 1 * 1 = 1, and no integer x has x * 0 = 1 | school arithmetic; informal truth, Section 4.1
exm-existential-introduction-derivations (solution): d: over Z, the successor of an odd integer is even; 3 is odd; f(3) = 4; 3 is not even | school arithmetic
exm-existential-introduction-derivations (solution): c: the side condition of forall-I as quoted (no premise, no open assumption, not in the conclusion) | def-rules-universal (cited)
prp-forall-implies-exists (proof): phi[x/x] = phi, and x is free for x in every formula | Section 4.2 (facts after def-substitution and the special cases after def-free-for)
prp-forall-implies-exists (claim): every domain is non-empty | convention of Section 4.1; explained in Section 4.11 (prose pointer)
prp-forall-implies-exists (claim): bounded case: forall x in A phi and exists x in A phi unfold to -> and /\ | def-bounded-quantifier (cited)
def-rule-existential-introduction (example): How this rule looks: 6 = 2 * 3, 7 = 2 * 3 + 1, 100 in N, 1/101 < 1/100, 1/100 is not < 1/100, 2n + 1 is odd and > 2n | arith lines (school arithmetic)
exr-existential-introduction-a1 (solution): c: over Z, y <= y * y for every y; y = x * x + 1 exceeds x * x | school arithmetic (cases y <= 0 and y >= 1)
exr-existential-introduction-a1 (solution): b: over N with R as <, f(x) = x + 1, c = 0 | school arithmetic
exr-existential-introduction-b2 (solution): the forall-I side condition | def-rules-universal (cited)
exr-existential-introduction-b3 (solution): 2 * 2 = 2 + 2 and (-1) * (-1) = -1 + 2 | arith line (school arithmetic)
exr-existential-introduction-c1 (solution): over N, x <= x, and y + 1 > y | school arithmetic
exr-existential-introduction-c2 (solution): the list of rules of Chapters 1-2 and Sections 4.3-4.4 with the main symbol of each cited line | def-rules-conjunction, def-rules-implication, def-rules-disjunction, def-rules-negation, def-rules-contradiction, def-rules-biconditional, def-rule-raa, def-derivation (R), def-rule-universal-elimination, def-rules-universal (recalled in prose, not cited by @ref)
exr-existential-introduction-c2 (solution): the explanation is informal; non-derivability follows from the counter-model of Section 4.11 and soundness (stated in 4.11, proved in the optional 4.12) | prose pointer; nothing depends on it
exr-existential-introduction-c2 (solution): over Z with P as even and c as 3, exists x P(x) is true (2 is even) and P(3) is false | school arithmetic; informal truth, Section 4.1
exr-existential-introduction-a1 (solution): d: over Z with P as even and c as 3, some integer (2) is even and 3 is not | school arithmetic; informal truth, Section 4.1
def-rule-existential-introduction (example): the one-way warning: some integer is even, 3 is not even | school arithmetic; informal truth, Section 4.1
exm-existential-introduction-derivations (solution): c: over N with R as <=, x <= x for every x | school arithmetic; informal truth, Section 4.1
def-rule-existential-introduction (claim): clause 3's recipe: if x does not appear in the line and phi is the line with some occurrences of t replaced by x, then phi[t/x] is the line; from R(x, c), marking c gives R(x, x), and R(x, x)[c/x] = R(c, c) | def-substitution (Section 4.2; every x of phi is a marked occurrence and none is bound), "appears in" of Section 4.2
exr-existential-introduction-c1 (claim): the problem asks for a sentence as conclusion | def-sentence (cited)
-->
