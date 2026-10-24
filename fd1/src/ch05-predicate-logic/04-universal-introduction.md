# Proving "For Every": Let x Be Arbitrary

Section 5.3 gave the rule for using a universal statement, and ended at a stall: from \( \forall x\, (P(x) \wedge Q(x)) \) it could derive \( P(c) \) for every term \( c \) we cared to name, but never \( \forall x\, P(x) \) itself. No list of instances is a statement about everything. This section gives the rule that proves a universal statement, \( \rulename{\forall I} \). It needs one new device, a box that carries a **name** instead of an assumption, and one new side condition, which turns the mathematician's "let \( x \) be arbitrary" into something a reader can check line by line.

## One number we know nothing about

Here is a fact of school algebra.

> For every real number \( x \), \( x^2 - 2x + 1 \ge 0 \).

We cannot check it number by number; there are too many numbers. The proof everyone writes takes **one** real number and argues about it: *Let \( x \in \nR \). Then \( x^2 - 2x + 1 = (x - 1)^2 \), and a square is never negative. So \( x^2 - 2x + 1 \ge 0 \).* Then, often without saying so: *since \( x \) was arbitrary, this holds for every real \( x \).*

Chapter 1 adopted a convention for sentences like "let \( x \) be a real number": the letter names **one fixed** number, not further specified (Section 1.1). It promised that Chapter 5 would explain why an argument of that kind proves a statement about every \( x \) at once. Section 2.2 met the same step at the end of the proof of @thm-sqrt2-irrational, passing from an arbitrary rational \( r \) to every rational; Section 4.2 met it in induction, passing from "let \( n \in \nN \)" to "for every \( n \)". Each time the step was taken on trust. Here is why it is correct, and when it is not.

The argument about \( x \) used **nothing** about \( x \) except that it is a real number. It never said "suppose \( x > 0 \)" or "take \( x = 3 \)". So it could be repeated word for word with \( 0 \), with \( -7 \), with \( \pi \), with any real number in place of \( x \), and it would prove the claim for that number. One argument about a number we know nothing about is a recipe for an argument about each number, and that is what "for every" asks for.

Everything depends on "nothing". If the argument had used a fact about \( x \) that not every number has, the recipe would break for some numbers. "Let \( x \) be a real number with \( x > 0 \). Then \( x > 0 \). Since \( x \) was arbitrary, every real number is positive" is the same shape, and its conclusion is false. The step "since \( x \) was arbitrary" is legitimate only when \( x \) **was** arbitrary: when no premise and no assumption still in force says anything about it. The rule of this section makes that condition exact.

## The flagged box

*To prove "for every \( x \)", take a fresh name that nothing is known about, prove the statement for that name, and generalize.*

In a derivation the argument about the arbitrary \( x \) is drawn as a box, as Chapter 1 drew the argument under an assumption. The box opens with no assumption at all. Instead it carries the arbitrary name, written at its top left, and is called a **flagged box**; the name is its **flag**.

::: {#def-rules-universal}
[Rules for the Universal Quantifier]

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open[x_0]
  \have {i} {\vdots}
  \have {j} {\varphi[x_0/x]}
  \close
  \have {k} {\forall x\, \varphi} \Ai{i-j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {\forall x\, \varphi}
  \have {k} {\varphi[t/x]} \Ae{i}
\end{nd}$
\end{center}
```

The rule on the left is \( \rulename{\forall I} \) (**universal introduction**, or **generalization**). It cites a flagged box, with flag \( x_0 \), from its first line \( i \) to its last line \( j \), and writes \( \forall x\, \varphi \) on line \( k \). The flag \( x_0 \) is a **variable**. The box's last line \( j \) is \( \varphi[x_0/x] \), and it is a line of the flagged box **itself**, not of a box inside it. The side condition is on the name: at line \( k \),

- \( x_0 \) appears in **no premise**,
- \( x_0 \) appears in **no assumption of a box still open at line \( k \)**, and
- \( x_0 \) does **not** appear in \( \forall x\, \varphi \).

The rule on the right is \( \rulename{\forall E} \), as in @def-rule-universal-elimination: \( t \) is any term free for \( x \) in \( \varphi \).
:::

In words: to prove that \( \varphi \) holds for every \( x \), open a box flagged with a new name \( x_0 \), prove \( \varphi[x_0/x] \), "\( \varphi \) holds of \( x_0 \)", as the box's last line, close the box, and write \( \forall x\, \varphi \). The side condition says that \( x_0 \) really was arbitrary.

### A first flagged box: how the rule looks in a mathematical proof

Here is the opening proof as a derivation, with the general fact about squares as a premise and the algebra as one line justified "arith" (Section 5.3).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall y\, (y^2 \ge 0)}
  \open[x_0]
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {x_0^2 - 2 \cdot x_0 + 1 \ge 0}
  \close
  \have {4} {\forall x\, (x^2 - 2 \cdot x + 1 \ge 0)}
\end{nd}$
\end{center}
```

The goal is universal, so the box opens first, with the goal's instance at \( x_0 \) as its last line; then the premise is instantiated at the term that last line needs, \( x_0 - 1 \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall y\, (y^2 \ge 0)}
  \open[x_0]
  \have {2} {(x_0 - 1)^2 \ge 0} \Ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {x_0^2 - 2 \cdot x_0 + 1 \ge 0}
  \close
  \have {4} {\forall x\, (x^2 - 2 \cdot x + 1 \ge 0)}
\end{nd}$
\end{center}
```

The finished derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall y\, (y^2 \ge 0)}
  \open[x_0]
  \have {2} {(x_0 - 1)^2 \ge 0} \Ae{1}
  \have {3} {x_0^2 - 2 \cdot x_0 + 1 \ge 0} \by{arith}{2}
  \close
  \have {4} {\forall x\, (x^2 - 2 \cdot x + 1 \ge 0)} \Ai{2-3}
\end{nd}$
\end{center}
```

| Line | Sentence |
|---|---|
| box \( x_0 \) | "Let \( x \in \nR \)." |
| 2 | "Then \( (x - 1)^2 \ge 0 \), since a square is never negative." (\( \rulename{\forall E} \) at \( x_0 - 1 \)) |
| 3 | "That is, \( x^2 - 2x + 1 \ge 0 \)." (arith) |
| 4 | "Since \( x \) was arbitrary, \( x^2 - 2x + 1 \ge 0 \) for every real \( x \)." (\( \rulename{\forall I} \)) |

Lines 2 and 3 are the derivation of Section 5.3 with the flag \( x_0 \) in place of the constant \( a \). What changed is only the name: \( a \) was a constant that the language fixed, so nothing could be generalized over it; \( x_0 \) is a variable that no premise mentions, so line 4 may generalize. The written proof uses the same letter \( x \) for the flag and for the bound variable, and says "let \( x \in \nR \)" where the derivation opens the box. Readers of mathematics are expected to supply the box.

Since the domain is \( \nR \), "let \( x \in \nR \)" asks nothing of \( x \). A proof that says "let \( \varepsilon > 0 \)" does ask something, and its box opens with the assumption \( \varepsilon_0 > 0 \).

### Reading the rule

Here are the two boxes side by side: the box of \( \rulename{{\to}I} \) from @def-rules-implication, and the flagged box.

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
\qquad\qquad
$\begin{nd}[schema]
  \open[x_0]
  \have {i} {\vdots}
  \have {j} {\varphi[x_0/x]}
  \close
  \have {k} {\forall x\, \varphi} \Ai{i-j}
\end{nd}$
\end{center}
```

Both draw a boundary and both are cited as a range \( i \)–\( j \). The \( \rulename{{\to}I} \) box opens with what we suppose; the flagged box opens with the name we have fixed. In the schema the flagged box begins with a gap \( \vdots \) on line \( i \), only so that the range has a first line; in a real derivation line \( i \) is whatever the box's first line is.

*This rule has conditions that matter; read each one.* Read the rule part by part: the flag, the three clauses of the side condition, and the last line.

- **The flag.** Opening the box is the written "let \( x_0 \) be arbitrary". The flag is always a variable, never a constant: a constant has a fixed meaning, while the whole point of \( x_0 \) is that it may stand for anything. The book writes flags with a subscript \( 0 \), \( x_0 \), \( y_0 \), \( \varepsilon_0 \), so that they stand out.
- **No premise, no open assumption** (the first and second clauses). This is "we know nothing about \( x_0 \)". What is known at line \( k \) is the premises and the assumptions of the boxes still open there. If none of them mentions \( x_0 \), then nothing that was used about \( x_0 \) inside the box is special to \( x_0 \).
- **Not in the conclusion** (the third clause). The name must not leak out. Inside the box it stood for an arbitrary object, and \( \forall x\, \varphi \) is meant to speak about all objects through the bound \( x \). A conclusion that still mentions \( x_0 \) ties what it says to the one object \( x_0 \) names, while claiming it of everything.
- **The last line.** \( \varphi[x_0/x] \) is what was proved about \( x_0 \), and it must be a line of the flagged box itself, just as the last line of a \( \rulename{{\to}I} \) box must be (Section 1.4). A line inside a further box would still depend on that box's assumption.

"Appear" is the word of Section 5.2: written anywhere in the formula, including just after a quantifier symbol. So a box flagged \( x \) can never end in \( \forall x\, \varphi \), since \( x \) appears in \( \forall x\, \varphi \). That is one more reason the book never uses the quantified letter itself as the flag.

**In practice:** choose as flag a letter written nowhere in the derivation so far, and when the box closes, put \( x \) in place of **every** occurrence of the flag in its last line. Then all three clauses hold at once: no premise or open assumption can contain a letter written nowhere, and the conclusion no longer contains the flag. The clauses are what a checker tests, and they allow a little more than this habit does (the fold below).

::: {.second-reading title="Fresh is not the same as new"}
The condition asks about three places only: the premises, the open assumptions, and the conclusion. Lines **outside** the box may mention \( x_0 \), before it or after it. An earlier line \( \forall y\, R(x_0, y) \), obtained by \( \rulename{\forall E} \) from a premise, is harmless; Exercise C1 builds a derivation with such a line. And once a flagged box has closed, its name may flag a later box. A name that satisfies the side condition at the line that closes its box is called **fresh** there. It need not be new to the whole derivation.
:::

::: {.check}
A derivation has used the letters \( x_0 \), \( y_0 \) and \( u_0 \) so far, and \( u_0 \) appears in an open assumption. Which flag can a new \( \rulename{\forall I} \) box take without checking anything?
:::

::: {.solution}
Any letter written nowhere yet, for example \( z_0 \). (\( x_0 \) or \( y_0 \) may also be allowed, but only after checking the three clauses; \( u_0 \) is not, while its assumption is open.)
:::

### Why each clause

Each clause stops a derivation of a false conclusion from true premises. Here is one failure for each.

*A name in a premise.* If \( \rulename{\forall I} \) could generalize over a name in a premise, then \( P(x_0) \vdash \forall x\, P(x) \):

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (forall-I over a name in a premise)
$\begin{nd}
  \hypo {1} {P(x_0)}
  \open[x_0]
  \have {2} {P(x_0)} \r{1}
  \close
  \have {3} {\forall x\, P(x)} \Ai{2-2}
\end{nd}$
\end{center}
```

Over \( \nZ \), read \( P(x) \) as "\( x \) is even" and let \( x_0 \) name \( 2 \). The premise is true and line 3, "every integer is even", is false. Line 3 breaks the first clause: \( x_0 \) appears in the premise on line 1. The premise **does** say something about \( x_0 \), so \( x_0 \) is not arbitrary.

*A name in an open assumption.* Suppose \( x_0 > 0 \), and inside that supposition generalize over \( x_0 \) (left):

```{=latex}
\begin{center}
% expect-invalid: line 3 generalizes over x_0 while the assumption x_0 > 0 on line 1 is open
$\begin{nd}
  \open
  \hypo {1} {x_0 > 0} \purpose{\ii}
  \open[x_0]
  \have {2} {x_0 > 0} \r{1}
  \close
  \have {3} {\forall x\, (x > 0)} \Ai{2-2}
  \close
  \have {4} {x_0 > 0 \to \forall x\, (x > 0)} \ii{1-3}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \open[x_0]
  \open
  \hypo {1} {x_0 > 0}
  \have {2} {x_0 + 1 > 0} \by{arith}{1}
  \close
  \have {3} {x_0 > 0 \to x_0 + 1 > 0} \ii{1-2}
  \close
  \have {4} {\forall x\, (x > 0 \to x + 1 > 0)} \Ai{1-3}
\end{nd}$
\end{center}
```

On the left, line 3 breaks the second clause, since \( x_0 \) appears in the assumption of line 1, whose box is still open at line 3. Read over \( \nZ \) with \( x_0 \) naming \( 1 \): line 4 says "if \( 1 > 0 \), then every integer is positive", which is false at \( 0 \), and it rests on no premise at all. This is the "let \( x \) be a real number with \( x > 0 \) … since \( x \) was arbitrary" of the opening, made into lines. One more legal flagged box around everything turns line 4 into a false sentence; the fold shows it. On the right the boxes are nested the other way: the flagged box opens first, the supposition inside it, and \( \rulename{\forall I} \) generalizes an implication that carries its hypothesis with it.

::: {.second-reading title="The same error, as a false sentence"}
With one more flagged box, the error of the minimal derivation becomes a false **sentence**:

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (forall-I over a name in an open assumption)
$\begin{nd}
  \open[x_0]
  \open
  \hypo {1} {x_0 > 0}
  \open[x_0]
  \have {2} {x_0 > 0} \r{1}
  \close
  \have {3} {\forall x\, (x > 0)} \Ai{2-2}
  \close
  \have {4} {x_0 > 0 \to \forall x\, (x > 0)} \ii{1-3}
  \close
  \have {5} {\forall y\, (y > 0 \to \forall x\, (x > 0))} \Ai{1-4}
\end{nd}$
\end{center}
```

Line 3 breaks the second clause: \( x_0 \) appears in the assumption on line 1, whose box is still open at line 3. Every other line is legal, including line 5, where the box of line 1 has closed. The inner box on line 2 is flagged \( x_0 \) while the outer box flagged \( x_0 \) is still open; the definition allows this, since its side condition asks only about premises, open assumptions and the conclusion. And line 5 says "every positive number makes every number positive", which over \( \nZ \) is false: at \( y = 1 \) the hypothesis \( 1 > 0 \) holds and \( \forall x\, (x > 0) \) fails at \( x = 0 \). This is the "let \( x \) be a real number with \( x > 0 \) … since \( x \) was arbitrary" of the opening, made into lines.
:::

*A name in the conclusion.* From the premise \( \forall x\, (x \le x) \), true over \( \nN \), open a box flagged \( y_0 \):

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (the flag appears in the conclusion)
$\begin{nd}
  \hypo {1} {\forall x\, (x \le x)}
  \open[y_0]
  \have {2} {y_0 \le y_0} \Ae{1}
  \close
  \have {3} {\forall x\, (x \le y_0)} \Ai{2-2}
\end{nd}$
\end{center}
```

Line 2 is \( (x \le y_0)[y_0/x] \), so line 3 has the shape of \( \rulename{\forall I} \) with \( \varphi = (x \le y_0) \). But \( y_0 \) appears in the conclusion, which breaks the third clause. Line 3 says "every natural number is at most \( y_0 \)", and that is false whatever \( y_0 \) names: \( y_0 + 1 \) is a counterexample. (Exercise C1 of Section 5.5 turns this into a sentence, "there is a largest natural number".)

The requirement on the last line is the one Chapter 1 already imposed on every box rule, for the same reason.

## Derivations with flagged boxes

The search method of Section 3.1 gets a new goal-directed step: when the goal is \( \forall x\, \varphi \), open a flagged box with a fresh name \( x_0 \), and make \( \varphi[x_0/x] \) the box's last line, the new goal. The examples below use it, each with an Idea.

::: {#exm-universal-introduction-derivations}
[Flagged boxes at work]

Give a derivation of each sequent.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, \forall y\, R(x, y) \vdash \forall x\, R(x, x) \).
2. \( \forall x\, (P(x) \to Q(x)), \ \forall x\, P(x) \vdash \forall x\, Q(x) \).
3. \( \forall x\, \forall y\, R(x, y) \vdash \forall y\, \forall x\, R(x, y) \).
:::
:::

::: {.solution}
(a) *Idea.* The goal begins with \( \forall x \), so the goal-directed step opens a box flagged \( x_0 \), and the new goal is \( R(x, x)[x_0/x] = R(x_0, x_0) \). That goal names the term for \( \rulename{\forall E} \) (Section 5.3's step): instantiate the premise at \( x_0 \), twice.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \open[x_0]
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {R(x_0, x_0)}
  \close
  \have {4} {\forall x\, R(x, x)}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \open[x_0]
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {R(x_0, x_0)}
  \close
  \have {4} {\forall x\, R(x, x)}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \open[x_0]
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \have {3} {R(x_0, x_0)} \Ae{2}
  \close
  \have {4} {\forall x\, R(x, x)} \Ai{2-3}
\end{nd}$
\end{center}
```

The side condition at line 4: \( x_0 \) does not appear in the premise, no box is open at line 4, and \( x_0 \) does not appear in \( \forall x\, R(x, x) \). Lines 2 and 3 instantiate at the variable \( x_0 \), which is free for \( x \) and for \( y \), since the formulas contain no quantifier on \( x_0 \). Compare Section 5.3, (b), which reached only \( R(c, c) \): there the term was a constant, a name fixed by the language, and nothing can be generalized over a constant; here it is a flag, a variable that no premise mentions.

(b) *Idea.* The goal is universal: a box flagged \( x_0 \), whose last line must be \( Q(x_0) \). Both premises are universal; instantiate each at the term the box's goal names, \( x_0 \), and \( \rulename{{\to}E} \) finishes.

| Givens | Goal |
|---|---|
| \( \forall x\, (P(x) \to Q(x)) \), \( \forall x\, P(x) \) | \( \forall x\, Q(x) \) |
| the same, and the fresh name \( x_0 \) (\( \rulename{\forall I} \) opens a box) | \( Q(x_0) \) |
| + \( P(x_0) \to Q(x_0) \), \( P(x_0) \) (\( \rulename{\forall E} \) at \( x_0 \), twice) | \( Q(x_0) \) |
| + \( Q(x_0) \) (\( \rulename{{\to}E} \)) | \( Q(x_0) \) ✓ |

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, P(x)}
  \open[x_0]
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {Q(x_0)}
  \close
  \have {6} {\forall x\, Q(x)}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, P(x)}
  \open[x_0]
  \have {3} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {4} {P(x_0)} \Ae{2}
  \have[\ ][0] {} {\vdots}
  \have[][5] {5} {Q(x_0)}
  \close
  \have {6} {\forall x\, Q(x)}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, P(x)}
  \open[x_0]
  \have {3} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {4} {P(x_0)} \Ae{2}
  \have {5} {Q(x_0)} \ie{3,4}
  \close
  \have {6} {\forall x\, Q(x)} \Ai{3-5}
\end{nd}$
\end{center}
```

At line 6, \( x_0 \) appears in neither premise nor in \( \forall x\, Q(x) \), and no box is open.

(c) *Idea.* Read the goal's quantifiers from the outside: \( \forall y \) first, so open a box flagged \( y_0 \); the new goal \( \forall x\, R(x, y_0) \) is again universal, so open a box flagged \( x_0 \) inside it; the innermost goal is \( R(x_0, y_0) \). Two boxes, opened in the goal's order. Now the premise's quantifiers are removed in **its** order: \( \rulename{\forall E} \) at \( x_0 \), then at \( y_0 \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \open[y_0]
  \open[x_0]
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {R(x_0, y_0)}
  \close
  \have {4} {\forall x\, R(x, y_0)}
  \close
  \have {5} {\forall y\, \forall x\, R(x, y)}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \open[y_0]
  \open[x_0]
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {R(x_0, y_0)}
  \close
  \have {4} {\forall x\, R(x, y_0)}
  \close
  \have {5} {\forall y\, \forall x\, R(x, y)}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \open[y_0]
  \open[x_0]
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \have {3} {R(x_0, y_0)} \Ae{2}
  \close
  \have {4} {\forall x\, R(x, y_0)} \Ai{2-3}
  \close
  \have {5} {\forall y\, \forall x\, R(x, y)} \Ai{2-4}
\end{nd}$
\end{center}
```

The box flagged \( y_0 \) immediately contains the box flagged \( x_0 \), so it has no line of its own before the inner box; following the convention for a flagged box that immediately contains another box (the fine print below), line 5 cites it as \( \lines{2}{4} \), from the first line of the inner box. Its last line is line 4, a line of the outer box itself. At line 4, \( x_0 \) is in no premise, the only open box (flagged \( y_0 \)) has no assumption, and \( x_0 \) does not appear in \( \forall x\, R(x, y_0) \). At line 5 the same holds for \( y_0 \).

Nothing in (c) used that the formula under the quantifiers is \( R(x, y) \). For any formula \( \psi \) and different variables \( x \) and \( y \), with flags \( x_0 \) and \( y_0 \) that are different from each other and from \( x \) and \( y \) and that do not appear in \( \psi \), the same five lines derive \( \forall x\, \forall y\, \psi \vdash \forall y\, \forall x\, \psi \): line 3 becomes \( (\psi[x_0/x])[y_0/y] \), which equals \( (\psi[y_0/y])[x_0/x] \), since the two substitutions put two different fresh names in for two different variables and so do not interfere. Exchanging the letters \( x \) and \( y \) gives the other direction. So **two adjacent universal quantifiers may always be swapped**: \( \forall x\, \forall y\, \psi \dashv\vdash \forall y\, \forall x\, \psi \). Section 5.1 read this off the game, where the challenger makes both moves; here it is derived.
:::

::: {.check}
Suppose premise 2 of (b) were \( P(x_0) \) in place of \( \forall x\, P(x) \). The box still reaches \( Q(x_0) \), by \( \rulename{\forall E} \) 1 and \( \rulename{{\to}E} \). May line 6 be written?
:::

::: {.solution}
No: \( x_0 \) appears in a premise, so the first clause fails. A counter-reading shows the step is unsafe: over \( \nZ \), with \( P \) and \( Q \) both read as "even" and \( x_0 \) naming \( 2 \), both premises are true and \( \forall x\, Q(x) \) is false.
:::

::: {.check}
Could both boxes of (c) be flagged \( x_0 \), the outer one standing for \( y \)?
:::

::: {.solution}
No. The inner box would end in \( R(x_0, x_0) \), and the \( \rulename{\forall I} \) line that closes it must be \( \forall x\, R(x, x_0) \), the instance at \( x_0 \) of the outer goal; that line contains the inner flag \( x_0 \), so the third clause fails. Nested flagged boxes need two names.
:::

::: {.second-reading title="The front renaming, derived"}
Section 5.2 took renaming of a bound variable as a convention and promised to derive it at the front of a formula. For a formula \( \varphi \) and variables \( y \), \( z \) with \( z \) not appearing in \( \varphi \), \( \forall y\, \varphi \dashv\vdash \forall z\, \varphi[z/y] \):

```{=latex}
% schema (phi is a metavariable; the side conditions are checked in the text)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall y\, \varphi}
  \open[z_0]
  \have {2} {\varphi[z_0/y]} \Ae{1}
  \close
  \have {3} {\forall z\, \varphi[z/y]} \Ai{2-2}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\forall z\, \varphi[z/y]}
  \open[z_0]
  \have {2} {\varphi[z_0/y]} \Ae{1}
  \close
  \have {3} {\forall y\, \varphi} \Ai{2-2}
\end{nd}$
\end{center}
```

Take \( z_0 \) to be a variable that does not appear in \( \varphi \) and is different from \( y \) and \( z \). Since \( z \) does not appear in \( \varphi \), the formula \( \varphi[z/y] \) is \( \varphi \) with each free \( y \) changed to \( z \), and changing those \( z \)'s on to \( z_0 \) gives the same result as changing each free \( y \) to \( z_0 \) at once: \( (\varphi[z/y])[z_0/z] = \varphi[z_0/y] \). So in the left derivation, line 2 is a legal \( \rulename{\forall E} \) (\( z_0 \) does not appear in \( \varphi \), so it is free for \( y \)), and it is the instance \( (\varphi[z/y])[z_0/z] \) that the \( \rulename{\forall I} \) on line 3 needs. In the right derivation, line 2 is \( (\varphi[z/y])[z_0/z] \), a legal \( \rulename{\forall E} \) for the same reason, and it is \( \varphi[z_0/y] \), the instance that \( \forall y\, \varphi \) needs. At line 3 of each, \( z_0 \) appears neither in the premise nor in the conclusion, and no box is open. Each direction has three lines.
:::

Now the sequent at which Section 5.3 stalled, together with its converse. "For every \( x \), \( P(x) \) and \( Q(x) \)" says the same as "\( P(x) \) for every \( x \), and \( Q(x) \) for every \( x \)":

::: {#prp-forall-and}
[Universal Quantifier and Conjunction]

\[
\forall x\, (P(x) \wedge Q(x)) \dashv\vdash \forall x\, P(x) \wedge \forall x\, Q(x) .
\]
:::

::: {.idea}
\( (\vdash) \) The goal is a conjunction, so (Section 1.2) two subgoals, \( \forall x\, P(x) \) and \( \forall x\, Q(x) \). Each is universal, so each gets its own flagged box, and inside each, \( \rulename{\forall E} \) at the flag and \( \rulename{\wedge E} \) give the box's last line. \( (\dashv) \) The goal is universal, so one flagged box, with the goal \( P(x_0) \wedge Q(x_0) \); take the premise apart by \( \rulename{\wedge E} \) and instantiate each half at \( x_0 \).

The search, for \( (\vdash) \):

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \wedge Q(x))}
  \open[x_0]
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {P(x_0)}
  \close
  \have {4} {\forall x\, P(x)}
  \open[x_0]
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {Q(x_0)}
  \close
  \have {7} {\forall x\, Q(x)}
  \have {8} {\forall x\, P(x) \wedge \forall x\, Q(x)} \ai{4,7}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \wedge Q(x))}
  \open[x_0]
  \have {2} {P(x_0) \wedge Q(x_0)} \Ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {P(x_0)}
  \close
  \have {4} {\forall x\, P(x)}
  \open[x_0]
  \have {5} {P(x_0) \wedge Q(x_0)} \Ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {Q(x_0)}
  \close
  \have {7} {\forall x\, Q(x)}
  \have {8} {\forall x\, P(x) \wedge \forall x\, Q(x)} \ai{4,7}
\end{nd}$
\end{center}
```

For \( (\dashv) \):

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, P(x) \wedge \forall x\, Q(x)}
  \have {2} {\forall x\, P(x)} \ae{1}
  \have {3} {\forall x\, Q(x)} \ae{1}
  \open[x_0]
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {P(x_0) \wedge Q(x_0)}
  \close
  \have {7} {\forall x\, (P(x) \wedge Q(x))}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\forall x\, P(x) \wedge \forall x\, Q(x)}
  \have {2} {\forall x\, P(x)} \ae{1}
  \have {3} {\forall x\, Q(x)} \ae{1}
  \open[x_0]
  \have {4} {P(x_0)} \Ae{2}
  \have {5} {Q(x_0)} \Ae{3}
  \have[\ ][0] {} {\vdots}
  \have[][6] {6} {P(x_0) \wedge Q(x_0)}
  \close
  \have {7} {\forall x\, (P(x) \wedge Q(x))}
\end{nd}$
\end{center}
```
:::

::: {.proof}
\( (\vdash) \)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \wedge Q(x))}
  \open[x_0]
  \have {2} {P(x_0) \wedge Q(x_0)} \Ae{1}
  \have {3} {P(x_0)} \ae{2}
  \close
  \have {4} {\forall x\, P(x)} \Ai{2-3}
  \open[x_0]
  \have {5} {P(x_0) \wedge Q(x_0)} \Ae{1}
  \have {6} {Q(x_0)} \ae{5}
  \close
  \have {7} {\forall x\, Q(x)} \Ai{5-6}
  \have {8} {\forall x\, P(x) \wedge \forall x\, Q(x)} \ai{4,7}
\end{nd}$
\end{center}
```

At lines 4 and 7, \( x_0 \) appears neither in the premise nor in the conclusion of that line, and no box is open. The second flagged box reuses the name \( x_0 \). That is allowed: the side condition at line 7 asks only about the premise, the open assumptions, and \( \forall x\, Q(x) \), and the earlier box, with its lines 2 and 3, closed at line 3 and is not available at line 7. (A fresh \( y_0 \) would do equally well.)

\( (\dashv) \)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, P(x) \wedge \forall x\, Q(x)}
  \have {2} {\forall x\, P(x)} \ae{1}
  \have {3} {\forall x\, Q(x)} \ae{1}
  \open[x_0]
  \have {4} {P(x_0)} \Ae{2}
  \have {5} {Q(x_0)} \Ae{3}
  \have {6} {P(x_0) \wedge Q(x_0)} \ai{4,5}
  \close
  \have {7} {\forall x\, (P(x) \wedge Q(x))} \Ai{4-6}
\end{nd}$
\end{center}
```

At line 7, \( x_0 \) is in neither the premise nor the conclusion, and no box is open. The two derivations prove the two sequents, as claimed.
:::

The first derivation is the answer to Section 5.3's stall: its lines 1–4 derive \( \forall x\, P(x) \) from \( \forall x\, (P(x) \wedge Q(x)) \). The proposition says that \( \forall \) distributes over \( \wedge \).

**Fine print: flagged boxes in a derivation.** @def-derivation (Section 1.4) said that a box is a block of consecutive lines whose first line is an assumption. We now extend that definition, and two things change. First, a box may be **flagged**: it carries a name, a variable written at its top, and a flagged box need **not** open with an assumption. The box of \( \rulename{\forall I} \) has none; the box of the rule for using "there exists" in Section 5.6 is flagged and has one. Second, the rules that close a flagged box carry side conditions about its name, such as the one above. Everything else in @def-derivation stays word for word: two boxes are disjoint or one is inside the other, a box ends at one of its lines, and the scope rule decides which lines and boxes are available where. A flagged box with no assumption adds nothing to what is assumed; it only marks where the name is in use. When a flagged box immediately contains another box, as in the swap of two quantifiers in the examples above, the range starts at the first line of that inner box. The right-hand derivation of "Why each clause", derivation (c) above and Exercise B1 below use the convention.

## Every element of the empty set {#every-element-of-the-empty-set}

Section 5.1 read \( \forall x \in \emptyset \; \varphi \) as true whatever \( \varphi \) says, because there is no element to test, and promised a derivation. Section 2.1 met the same phenomenon for implications: \( \neg P \vdash P \to Q \) (@prp-vacuous-implication, the derived rule written VI). With \( \rulename{\forall I} \) the two meet.

Let \( A \) be a set with no elements. What that means is the premise \( \forall x\, \neg(x \in A) \): no object is in \( A \). From it, "every element of \( A \) is greater than \( 5 \)", which by @def-bounded-quantifier is \( \forall x\, (x \in A \to x > 5) \), has a four-line derivation:

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \neg (x \in A)}
  \open[x_0]
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {x_0 \in A \to x_0 > 5}
  \close
  \have {4} {\forall x\, (x \in A \to x > 5)}
\end{nd}$
\qquad\qquad
$\begin{nd}
  \hypo {1} {\forall x\, \neg (x \in A)}
  \open[x_0]
  \have {2} {\neg (x_0 \in A)} \Ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][3] {3} {x_0 \in A \to x_0 > 5}
  \close
  \have {4} {\forall x\, (x \in A \to x > 5)}
\end{nd}$
\end{center}
```

Here is how the search grows it, and the result:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \neg (x \in A)}
  \open[x_0]
  \have {2} {\neg (x_0 \in A)} \Ae{1}
  \have {3} {x_0 \in A \to x_0 > 5} \by{VI}{2}
  \close
  \have {4} {\forall x\, (x \in A \to x > 5)} \Ai{2-3}
\end{nd}$
\end{center}
```

Line 3 uses VI (@prp-vacuous-implication) as one line, with the formulas \( x_0 \in A \) and \( x_0 > 5 \) for \( P \) and \( Q \); every derived rule of Chapter 2 may be used in this way on first-order formulas. Nothing in the derivation used \( x > 5 \): with any formula in place of \( x > 5 \) in which \( x_0 \) does not appear, the same four lines go through, so "every element of an empty set has property \( \varphi \)" is derivable for every \( \varphi \), as Section 5.1 said.

::: {.second-reading title="Why a derived rule may stand in a flagged box"}
Using VI inside the box is allowed because the derivation of @prp-vacuous-implication uses only \( \rulename{\neg E} \), \( \rulename{\bot E} \) and \( \rulename{{\to}I} \), whose schemas apply to any formulas (@def-rule-schema), and it has no flagged box, so pasting it into the box flagged \( x_0 \) gives a derivation in the rules themselves. From now on, any derived rule of Chapter 2 is used in this way on first-order formulas.
:::

One more flagged box gives a statement about upper bounds:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \neg (x \in A)}
  \open[u_0]
  \open[x_0]
  \have {2} {\neg (x_0 \in A)} \Ae{1}
  \have {3} {x_0 \in A \to x_0 \le u_0} \by{VI}{2}
  \close
  \have {4} {\forall x\, (x \in A \to x \le u_0)} \Ai{2-3}
  \close
  \have {5} {\forall u\, \forall x\, (x \in A \to x \le u)} \Ai{2-4}
\end{nd}$
\end{center}
```

Over \( \nR \), line 5 says that every real number \( u \) is an upper bound of \( A \): every element of \( A \) is at most \( u \). For an empty set this holds for every \( u \), because there are no elements to check. At line 4, \( x_0 \) appears in neither the premise nor \( \forall x\, (x \in A \to x \le u_0) \), and the only open box (flagged \( u_0 \)) has no assumption. The name \( u_0 \) does appear in that conclusion, which is allowed, since the condition at line 4 is about \( x_0 \) only. At line 5, \( u_0 \) appears in neither the premise nor \( \forall u\, \forall x\, (x \in A \to x \le u) \), and no box is open.

## Common errors

Three errors with \( \rulename{\forall I} \) are common enough to name now.

- **Checking instances.** Verifying \( \varphi \) at \( x = 0, 1, 2 \), or at a thousand values, proves \( \varphi[0/x] \), \( \varphi[1/x] \), \( \varphi[2/x] \), and so on, and not \( \forall x\, \varphi \). The rule needs one proof about a fresh name, not many proofs about particular terms. Exercise C2 shows how plausible this error can look.
- **Generalizing over a name in an open assumption.** Inside "suppose \( x_0 > 0 \)", the name \( x_0 \) is not arbitrary. The left-hand derivation of the pair in "Why each clause" shows where this leads.
- **Generalizing over a name in a premise.** A premise about \( x_0 \), such as "\( x_0 \) is even", makes \( x_0 \) special. The first derivation of "Why each clause" shows it.

::: {.warning}
"Let \( x \) be arbitrary" is a promise about every line that follows, and the most common way to break it is an assumption made on the way. "Let \( n \in \nN \) and suppose \( n \) is even. Then \( n^2 \) is even. Since \( n \) was arbitrary, every \( n^2 \) is even" is false at \( n = 1 \). What the argument proves is "for every \( n \), **if** \( n \) is even, then \( n^2 \) is even": the \( \rulename{{\to}I} \) box on "\( n \) is even" must close **before** the \( \rulename{\forall I} \) step, so that the assumption is no longer open.
:::

::: {.check}
In the derivation below, line 6 is justified by \( \rulename{\forall I} \). Is it legal? If not, which clause of the side condition fails, and can you find a reading in which the premises are true and line 6 is false?

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (the quick check)
$\begin{nd}
  \hypo {1} {R(c, y_0)}
  \hypo {2} {\forall x\, \forall y\, (R(x, y) \to R(y, x))}
  \open[y_0]
  \have {3} {\forall y\, (R(c, y) \to R(y, c))} \Ae{2}
  \have {4} {R(c, y_0) \to R(y_0, c)} \Ae{3}
  \have {5} {R(y_0, c)} \ie{4,1}
  \close
  \have {6} {\forall y\, R(y, c)} \Ai{3-5}
\end{nd}$
\end{center}
```
:::

::: {.solution}
No. Lines 1–5 are legal; in particular line 5 may cite line 1, which lies in no box. But at line 6 the flag \( y_0 \) appears in the premise on line 1, so the first clause fails: line 5 was proved about \( y_0 \) using a fact about \( y_0 \), and \( y_0 \) was not arbitrary. A reading: over \( \nZ \), let \( R(x, y) \) be \( x \ne y \), which is symmetric, so premise 2 is true; let \( c \) name \( 0 \) and \( y_0 \) name \( 1 \), so premise 1, \( 0 \ne 1 \), is true. Line 6 says that every integer differs from \( 0 \), which is false at \( y = 0 \).
:::

::: {#exm-universal-introduction-critique}
[A Proof to Check]

Here is a proof. Is its claim true? Which step fails?

> *Claim.* Some real number is at least as large as every real number.
>
> *Proof.* Let \( x \) be a real number, and put \( M = x + 1 \). Then \( x \le M \). Since \( x \) was arbitrary, \( x \le M \) for every real \( x \), so \( M \) is such a number.
:::

::: {.solution}
The claim is false: whatever \( M \) is proposed, \( M + 1 \) is a larger real number. The faulty step is "since \( x \) was arbitrary". As a derivation, the box is flagged \( x_0 \) and ends in \( x_0 \le x_0 + 1 \), a line of arithmetic; the proof then writes \( \forall x\, (x \le M) \), and \( M \) stands for \( x_0 + 1 \):

```{=latex}
\begin{center}
% expect-invalid: line 2 keeps the flag x_0 in its conclusion
$\begin{nd}
  \open[x_0]
  \have {1} {x_0 \le x_0 + 1} \by{arith}{}
  \close
  \have {2} {\forall x\, (x \le x_0 + 1)} \Ai{1-1}
\end{nd}$
\end{center}
```

Line 2 breaks the third clause: the flag is still in the conclusion. The box earns \( \forall x\, (x \le x + 1) \), with **every** occurrence of the flag replaced: true, and about no single \( M \). The name \( M \) was chosen after \( x \), so it may depend on \( x \), which is the dependence Section 5.1 read off the order of quantifiers. With Section 5.5's rule, \( \rulename{\exists I} \) inside the box and then \( \rulename{\forall I} \) give "every real number has one at least as large", with the quantifiers in the safe order.
:::

## The rule card

::: {#exm-universal-introduction-instances}
[Instances of \( \rulename{\forall I} \)]

In each row the box's flag is in no premise and no open assumption.

| *flag* | *the box's last line* | *the new line* |
|---|---|---|
| \( x_0 \) | \( P(f(x_0)) \vee \neg R(x_0, c) \) | \( \forall x\, (P(f(x)) \vee \neg R(x, c)) \) |
| \( \varepsilon_0 \) | \( \varepsilon_0 > 0 \to \exists \delta\, (\delta > 0 \wedge \delta < \varepsilon_0) \) | \( \forall \varepsilon\, (\varepsilon > 0 \to \exists \delta\, (\delta > 0 \wedge \delta < \varepsilon)) \) |
| \( y_0 \) | \( \forall x\, (R(x, y_0) \to R(x, g(y_0))) \) | \( \forall y\, \forall x\, (R(x, y) \to R(x, g(y))) \) |

**Not an instance.** A box flagged \( x_0 \) ends in \( R(x_0, x_0) \). The line \( \forall x\, R(x, x_0) \) is not written by \( \rulename{\forall I} \): it keeps the flag in its conclusion (the third clause). The rule puts \( x \) in place of **every** occurrence of the flag: \( \forall x\, R(x, x) \).
:::

Chapters 1 and 2's thirteen rules are on the card at the end of Section 3.1; here are this chapter's so far.

| Rule | Shape | Side condition | You write | Lean |
|---|---|---|---|---|
| \( \rulename{\forall E} \) | \( \forall x\, \varphi \) \( \Longrightarrow \) \( \varphi[t/x] \) | \( t \) free for \( x \) in \( \varphi \) | "In particular, for \( x = t \), …"; "applying the hypothesis to \( t \), …" | `h t` (or `specialize h t`) |
| \( \rulename{\forall I} \) | box \( [x_0] \) … \( \varphi[x_0/x] \) \( \Longrightarrow \) \( \forall x\, \varphi \) | \( x_0 \) in no premise, in no open assumption, not in \( \forall x\, \varphi \) | "Let \( x \) be arbitrary. … Since \( x \) was arbitrary, …" | `intro x` |

Other forms of the opening phrase are "let \( x \in \nR \)", "fix \( \varepsilon > 0 \)", "take any \( n \in \nN \)"; the closing phrase is often left out, since the reader knows that a proof which began by fixing \( x \) proves a statement about every \( x \). In Lean, `intro x` turns the goal `forall x, P x` into the goal `P x` with a new name `x` in context, about which nothing is assumed: Lean's version of opening the flagged box. The same tactic opened the \( \rulename{{\to}I} \) box in Section 1.4, and the two boxes are, to Lean, one kind of thing.

In the Givens/Goal table, \( \rulename{\forall I} \) puts a fresh name among the Givens and makes \( \varphi[x_0/x] \) the goal.

::: {.warning}
[Not allowed: \( \rulename{\forall I} \)]

Each step below is wrong; the tag names the clause of the side condition of @def-rules-universal that it breaks.

- Generalize over a flag that a premise mentions: the first clause.
- Generalize over a flag that an open assumption mentions: the second clause (the pair in "Why each clause").
- Write a conclusion that still mentions the flag: the third clause (@exm-universal-introduction-critique).
- Cite a line inside a flagged box that has closed: the scope rule of @def-derivation, as for every box.
:::

## The search method: one more step

- **A goal \( \forall x\, \varphi \).** Open a flagged box with a fresh name \( x_0 \), one that appears in no premise, in no open assumption, and not in the goal. The new goal, the box's last line, is \( \varphi[x_0/x] \).

This step is **safe**, in the sense of Section 3.1. If \( \forall x\, \varphi \) can be derived at all, then so can \( \varphi[x_0/x] \), by one more \( \rulename{\forall E} \) at \( x_0 \); so opening the box never closes off a derivation that would otherwise exist. Take the step as soon as the goal is universal, and choose a flag that appears nowhere yet, so that the side condition cannot fail.

::: {.remark}
[Looking ahead]

Chapter 8 collects the errors of this section, with others, in a catalogue of steps a proof may not take.
:::

## Exercises

### A. Check your understanding

::: {#exr-universal-introduction-a1}
[A1]

Three derivations, D1, D2 and D3, are used in part (b).

D1:

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (exercise A1, D1)
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {P(x_0)}
  \open[x_0]
  \have {3} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {4} {Q(x_0)} \ie{3,2}
  \close
  \have {5} {\forall x\, Q(x)} \Ai{3-4}
\end{nd}$
\end{center}
```

D2:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \open[x_0]
  \have {3} {R(x_0, x_0)} \Ae{2}
  \close
  \have {4} {\forall x\, R(x, x)} \Ai{3-3}
\end{nd}$
\end{center}
```

D3:

```{=latex}
\begin{center}
% expect-invalid: a deliberately flawed derivation (exercise A1, D3)
$\begin{nd}
  \open
  \hypo {1} {R(x_0, c)} \purpose{\ii}
  \open[x_0]
  \have {2} {R(x_0, c)} \r{1}
  \close
  \have {3} {\forall x\, R(x, c)} \Ai{2-2}
  \close
  \have {4} {R(x_0, c) \to \forall x\, R(x, c)} \ii{1-3}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Write the schema of \( \rulename{\forall I} \) with its side condition.
2. For each of D1, D2, D3, decide whether its \( \rulename{\forall I} \) line is legal. If not, name the clause of the side condition that fails.
3. True or false, with a reason: "fresh" means that \( x_0 \) appears nowhere in the derivation outside its flagged box.
4. In the derivation of the \( (\vdash) \) half of @prp-forall-and, the name \( x_0 \) flags two boxes. Why does the side condition allow this?
:::
:::

::: {.solution}
(a) A box flagged \( x_0 \), with no assumption, from line \( i \) to line \( j \), whose last line \( j \) is \( \varphi[x_0/x] \), a line of the flagged box itself; then line \( k \): \( \forall x\, \varphi \), justified "\( \rulename{\forall I} \) \( i \)–\( j \)". At line \( k \) the name \( x_0 \) appears in no premise, in no assumption of a box still open at line \( k \), and not in \( \forall x\, \varphi \) (@def-rules-universal).

(b) *D1:* not legal. At line 5 the flag \( x_0 \) appears in the premise on line 2 (the first clause). Over \( \nZ \), with \( P(x) \) and \( Q(x) \) both read as "\( x \) is even" and \( x_0 \) naming \( 2 \), both premises are true and line 5, "every integer is even", is false.

*D2:* legal. Line 2 mentions \( x_0 \) outside the box, and that is allowed: it is neither a premise nor an assumption, and the conclusion \( \forall x\, R(x, x) \) does not contain \( x_0 \). Line 3 cites line 2, which is available, since no box contains it. (It is also correct in meaning: line 2 came from a premise that says nothing about \( x_0 \), so it holds whatever \( x_0 \) names.)

*D3:* not legal. At line 3 the assumption \( R(x_0, c) \) on line 1 is still open, and \( x_0 \) appears in it (the second clause). Line 4, which closes the box legally, then says "if \( x_0 \) is below \( c \), everything is below \( c \)": false over \( \nZ \) with \( R \) read as \( < \), \( c \) as \( 5 \) and \( x_0 \) as \( 1 \).

(c) False. The side condition asks about the premises, the assumptions of boxes still open at the \( \rulename{\forall I} \) line, and the conclusion of that line. Other lines may mention \( x_0 \), as line 2 of D2 does, and a closed flagged box may share its name with a later one.

(d) At line 7, which closes the second box, the side condition asks whether \( x_0 \) appears in the premise (no), in an assumption of an open box (no box is open), and in \( \forall x\, Q(x) \) (no). The first box's lines mention \( x_0 \), but they are neither premises nor open assumptions, and the box closed at line 3, so its lines are not even available at line 7.
:::

::: {#exr-universal-introduction-a2}
[A2: Drill]

Each part takes a line or two. The parts run from single steps, through a missing line, a justification column and a judgement on one step, to whole derivations.

::: {.enumerate options="label=(\alph*)"}
1. What does opening a flagged box say, in the words of a proof?
2. A box flagged \( x_0 \) ends in \( P(x_0) \wedge Q(x_0) \), and \( x_0 \) is in no premise and no open assumption. Which line may \( \rulename{\forall I} \) write?
3. Line 9 is \( \forall x\, (P(x) \vee Q(f(x))) \), justified "\( \rulename{\forall I} \) 4–8", the box flagged \( u_0 \). What is line 8?
4. Justify each line after the premise: 1 \( \forall x\, (P(x) \wedge Q(x)) \), premise; a box flagged \( x_0 \) holding 2 \( P(x_0) \wedge Q(x_0) \), 3 \( Q(x_0) \), 4 \( P(x_0) \), 5 \( Q(x_0) \wedge P(x_0) \); then 6 \( \forall x\, (Q(x) \wedge P(x)) \).
5. The premise is \( R(x_0) \). May a box flagged \( x_0 \) that ends in \( R(x_0) \) be closed with \( \forall x\, R(x) \)? If not, which clause does it break?
6. May a flag be the constant \( c \)?
7. A box flagged \( y_0 \) ends in \( y_0 \le y_0 \). Is \( \forall x\, (x \le y_0) \) a legal \( \rulename{\forall I} \) line? If not, which clause does it break?
8. Inside the box of an assumption \( Q(x_0) \), a box flagged \( x_0 \) ends in \( Q(x_0) \). May \( \rulename{\forall I} \) close it? If not, which clause does it break?
9. Derive \( \forall x\, P(x) \vdash \forall y\, P(y) \).
10. Derive \( \forall x\, (P(x) \wedge Q(x)) \vdash \forall x\, Q(x) \).
11. Derive \( \forall x\, P(x), \ \forall x\, Q(x) \vdash \forall x\, (Q(x) \wedge P(x)) \).
12. Derive \( \vdash \forall x\, (P(x) \to P(x)) \).
:::
:::

::: {.solution}
(a) "Let \( x_0 \) be arbitrary."

(b) \( \forall x\, (P(x) \wedge Q(x)) \).

(c) \( P(u_0) \vee Q(f(u_0)) \), the instance at the flag.

(d) 2 \( \rulename{\forall E} \) 1 (at \( x_0 \)); 3 \( \rulename{\wedge E} \) 2; 4 \( \rulename{\wedge E} \) 2; 5 \( \rulename{\wedge I} \) 3, 4; 6 \( \rulename{\forall I} \) 2–5.

(e) No, the first clause: \( x_0 \) appears in a premise.

(f) No: a flag is always a variable.

(g) No, the third clause: \( y_0 \) appears in the conclusion.

(h) No, the second clause: \( x_0 \) appears in an open assumption.

(i) A box flagged \( y_0 \): 2 \( P(y_0) \), \( \rulename{\forall E} \) 1; then 3 \( \forall y\, P(y) \), \( \rulename{\forall I} \) 2–2.

(j) A box flagged \( x_0 \): 2 \( P(x_0) \wedge Q(x_0) \), \( \rulename{\forall E} \) 1; 3 \( Q(x_0) \), \( \rulename{\wedge E} \) 2; then 4 \( \forall x\, Q(x) \), \( \rulename{\forall I} \) 2–3.

(k) A box flagged \( x_0 \): 3 \( Q(x_0) \), \( \rulename{\forall E} \) 2; 4 \( P(x_0) \), \( \rulename{\forall E} \) 1; 5 \( Q(x_0) \wedge P(x_0) \), \( \rulename{\wedge I} \) 3, 4; then 6 \( \forall x\, (Q(x) \wedge P(x)) \), \( \rulename{\forall I} \) 3–5.

(l) A box flagged \( x_0 \), and inside it the box of 1 \( P(x_0) \); 2 \( P(x_0) \to P(x_0) \), \( \rulename{{\to}I} \) 1–1; then 3 \( \forall x\, (P(x) \to P(x)) \), \( \rulename{\forall I} \) 1–2 (cited from line 1, the convention for a flagged box that immediately contains another).
:::

### B. Practice

::: {#exr-universal-introduction-b1}
[B1: A chain, for every x]

A search for \( \forall x\, (P(x) \to Q(x)), \ \forall x\, (Q(x) \to R(x)) \vdash \forall x\, (P(x) \to R(x)) \) has reached the stage below. *Name the move, then complete it, and check the side condition at line 9.*

```{=latex}
% schema (partial derivation: the gaps are unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, (Q(x) \to R(x))}
  \open[x_0]
  \open
  \hypo {3} {P(x_0)} \purpose{\ii}
  \have[\ ][0] {} {\vdots}
  \close
  \have[][8] {8} {P(x_0) \to R(x_0)} \by{?}{}
  \close
  \have {9} {\forall x\, (P(x) \to R(x))} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The moves are *let \( x \) be arbitrary* and then the \( \rulename{{\to}I} \) box; inside, instantiate both premises at \( x_0 \) and fire twice.

The goal is universal, so open a box flagged \( x_0 \); the new goal \( P(x_0) \to R(x_0) \) is an implication, so open a \( \rulename{{\to}I} \) box on \( P(x_0) \); the new goal is \( R(x_0) \). Now Section 5.3's exercise B1 runs inside the boxes, with \( x_0 \) for \( a \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, (Q(x) \to R(x))}
  \open[x_0]
  \open
  \hypo {3} {P(x_0)}
  \have {4} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {5} {Q(x_0)} \ie{4,3}
  \have {6} {Q(x_0) \to R(x_0)} \Ae{2}
  \have {7} {R(x_0)} \ie{6,5}
  \close
  \have {8} {P(x_0) \to R(x_0)} \ii{3-7}
  \close
  \have {9} {\forall x\, (P(x) \to R(x))} \Ai{3-8}
\end{nd}$
\end{center}
```

The flagged box immediately contains the \( \rulename{{\to}I} \) box, so line 9 cites it from line 3. At line 9: \( x_0 \) appears in neither premise; the assumption \( P(x_0) \) mentions \( x_0 \), but its box closed at line 7, so it is not open at line 9; and \( x_0 \) does not appear in \( \forall x\, (P(x) \to R(x)) \). The order of the boxes matters: the \( \rulename{{\to}I} \) box is inside the flagged box and closes first.
:::

::: {#exr-universal-introduction-b2}
[B2: Contraposition under a quantifier, used later]

::: {.enumerate options="label=(\alph*)"}
1. Give a derivation of \( \forall x\, (P(x) \to Q(x)) \vdash \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \).
2. Try to derive the converse, \( \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \vdash \forall x\, (P(x) \to Q(x)) \). Say where the search stalls, and which side condition stops it.
:::
:::

::: {.solution}
(a) The goal is an implication: a \( \rulename{{\to}I} \) box on \( \forall x\, \neg Q(x) \), with goal \( \forall x\, \neg P(x) \). That is universal: a box flagged \( x_0 \), with goal \( \neg P(x_0) \). That is a negation: a \( \rulename{\neg I} \) box on \( P(x_0) \), with goal \( \bot \). Inside, instantiate both universal lines at \( x_0 \) and look for a clash: \( P(x_0) \) and the instance of the premise give \( Q(x_0) \), and the assumption \( \forall x\, \neg Q(x) \) at \( x_0 \) gives \( \neg Q(x_0) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \open
  \hypo {2} {\forall x\, \neg Q(x)}
  \open[x_0]
  \open
  \hypo {3} {P(x_0)}
  \have {4} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {5} {Q(x_0)} \ie{4,3}
  \have {6} {\neg Q(x_0)} \Ae{2}
  \have {7} {\bot} \ne{5,6}
  \close
  \have {8} {\neg P(x_0)} \ni{3-7}
  \close
  \have {9} {\forall x\, \neg P(x)} \Ai{3-8}
  \close
  \have {10} {\forall x\, \neg Q(x) \to \forall x\, \neg P(x)} \ii{2-9}
\end{nd}$
\end{center}
```

At line 9, the open box is the \( \rulename{{\to}I} \) box of line 2, whose assumption \( \forall x\, \neg Q(x) \) does not contain \( x_0 \); the premise and the conclusion do not contain it either. So the side condition holds, even though the flagged box sits inside an open box.

(b) The goal is universal, so open a box flagged \( x_0 \), then a \( \rulename{{\to}I} \) box on \( P(x_0) \), with goal \( Q(x_0) \). The only premise is an implication, \( \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \). Using it needs its hypothesis \( \forall x\, \neg Q(x) \), which nothing supplies; and its conclusion, \( \forall x\, \neg P(x) \), would clash with \( P(x_0) \) and close the case by \( \rulename{\bot E} \). So everything turns on deriving \( \forall x\, \neg Q(x) \). The goal \( Q(x_0) \) is atomic and nothing produces it, so the method's last resort is an \( \rulename{RAA} \) box on \( \neg Q(x_0) \). Inside, the available facts about \( Q \) are \( \neg Q(x_0) \), and to reach \( \forall x\, \neg Q(x) \) from it we would close a flagged box over \( x_0 \). The side condition forbids it: \( x_0 \) appears in the open assumptions \( P(x_0) \) and \( \neg Q(x_0) \). A fresh name \( y_0 \) does not help either, since nothing tells us anything about \( \neg Q(y_0) \). The search stalls at the second clause of the side condition.

A stalled search proves nothing by itself; a cleverer derivation might exist. Section 7.2 settles the question with a structure in which the premise is true and the conclusion false, and shows that the converse does not follow.
:::

::: {#exr-universal-introduction-b3}
[B3: A number is at most its absolute value, for every number]

@exm-abs-at-least-x (Section 1.6) derived \( \abs{x} > x \vee \abs{x} = x \) for one fixed real \( x \) from three premises about that \( x \): \( x \ge 0 \vee x < 0 \), \( x \ge 0 \to \abs{x} = x \), and \( x < 0 \to \abs{x} > x \). Turn it into a derivation of
\[
\forall x\, (\abs{x} > x \vee \abs{x} = x)
\]
from premises that are universal statements. Explain why the premises of @exm-abs-at-least-x, copied with \( x_0 \) in place of \( x \), will not do.
:::

::: {.solution}
The goal is universal, so the derivation of Section 1.6 must run inside a box flagged \( x_0 \). Its three premises mention the number it is about. So here the premises are the three facts **for every** \( x \), and inside the box \( \rulename{\forall E} \) at \( x_0 \) gives each fact about \( x_0 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (x \ge 0 \vee x < 0)}
  \hypo {2} {\forall x\, (x \ge 0 \to \abs{x} = x)}
  \hypo {3} {\forall x\, (x < 0 \to \abs{x} > x)}
  \open[x_0]
  \have {4} {x_0 \ge 0 \vee x_0 < 0} \Ae{1}
  \have {5} {x_0 \ge 0 \to \abs{x_0} = x_0} \Ae{2}
  \have {6} {x_0 < 0 \to \abs{x_0} > x_0} \Ae{3}
  \open
  \hypo {7} {x_0 \ge 0}
  \have {8} {\abs{x_0} = x_0} \ie{5,7}
  \have {9} {\abs{x_0} > x_0 \vee \abs{x_0} = x_0} \oi{8}
  \close
  \open
  \hypo {10} {x_0 < 0}
  \have {11} {\abs{x_0} > x_0} \ie{6,10}
  \have {12} {\abs{x_0} > x_0 \vee \abs{x_0} = x_0} \oi{11}
  \close
  \have {13} {\abs{x_0} > x_0 \vee \abs{x_0} = x_0} \oe{4,7-9,10-12}
  \close
  \have {14} {\forall x\, (\abs{x} > x \vee \abs{x} = x)} \Ai{4-13}
\end{nd}$
\end{center}
```

Lines 7–13 are the derivation of @exm-abs-at-least-x with \( x_0 \) for \( x \), its premises replaced by lines 4–6. At line 14, \( x_0 \) appears in none of the premises, no box is open (the two case boxes closed at lines 9 and 12), and \( x_0 \) is not in the conclusion. The derivation has 14 lines.

If instead the premises were \( x_0 \ge 0 \vee x_0 < 0 \), \( x_0 \ge 0 \to \abs{x_0} = x_0 \) and \( x_0 < 0 \to \abs{x_0} > x_0 \), the box could reach line 13 just as well, but line 14 would break the first clause: \( x_0 \) would appear in a premise. And rightly so. Premises about \( x_0 \) are facts about one number, and a derivation from them proves something about that number only. The universal premises are true facts about every real number, and that is what entitles the conclusion to speak about every real number.
:::

::: {#exr-universal-introduction-b4}
[B4: Back to the stall of Section 5.3]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \forall x\, P(x) \vdash \forall x\, P(x) \) with \( \rulename{\forall E} \) and \( \rulename{\forall I} \), not \( \rulename{R} \). Why can the flagged box not be flagged \( x \)?
2. Explain why no flag at all gives a derivation of \( P(x) \vdash \forall x\, P(x) \) by this route, and give a counter-reading to the sequent.
:::
:::

::: {.solution}
(a)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, P(x)}
  \open[x_0]
  \have {2} {P(x_0)} \Ae{1}
  \close
  \have {3} {\forall x\, P(x)} \Ai{2-2}
\end{nd}$
\end{center}
```

With the flag \( x \), the conclusion \( \forall x\, P(x) \) contains \( x \) (the letter after the quantifier counts: that is what "appear" means), so the third clause fails, whatever else holds.

(b) With the flag \( x \), the line \( P(x) \) is available, but \( x \) appears in the premise and in the conclusion. With any other flag \( x_0 \), the box needs the line \( P(x_0) \), and the search finds nothing that gives it: the premise is about \( x \), and no line mentions \( x_0 \). A stalled search proves nothing by itself, since a cleverer derivation might exist; the counter-reading settles it. Over \( \nZ \), read \( P \) as "even" and let \( x \) name \( 2 \): the premise is true and \( \forall x\, P(x) \) is false. (Section 7.2 makes this a counter-model.)

**Marking scheme.** (10 points)
- 3: the derivation of (a).
- 3: the flag \( x \) fails "not in the conclusion", with the reason.
- 2: (b) both cases of the flag.
- 2: the counter-reading, with the value of \( x \).
Fatal errors (0 for the step): claiming the flag \( x \) is fine because \( x \) is bound in the conclusion; treating \( P(x) \) and \( P(x_0) \) as the same line.
:::

::: {#exr-universal-introduction-b5}
[B5: Derive or break: properties of a relation, used later]

A two-place predicate \( R \) is **reflexive** if \( \forall x\, R(x, x) \), **irreflexive** if \( \forall x\, \neg R(x, x) \), **symmetric** if \( \forall x\, \forall y\, (R(x, y) \to R(y, x)) \), **asymmetric** if \( \forall x\, \forall y\, (R(x, y) \to \neg R(y, x)) \), and **transitive** if \( \forall x\, \forall y\, \forall z\, ((R(x, y) \wedge R(y, z)) \to R(x, z)) \). Read each claim with these formulas as its premises and conclusion, and derive it, or break it with a counter-reading.

::: {.enumerate options="label=(\alph*)"}
1. asymmetric \( \vdash \) irreflexive.
2. irreflexive \( \vdash \) asymmetric.
3. irreflexive, transitive \( \vdash \) asymmetric.
4. symmetric, transitive \( \vdash \) reflexive.
5. symmetric, transitive, \( \forall x\, R(x, f(x)) \vdash \) reflexive.
6. reflexive \( \vdash \) symmetric.
:::
:::

::: {.solution}
(a) Derive. The goal is universal, so a flagged box; its goal \( \neg R(x_0, x_0) \) is a negation, so a \( \rulename{\neg I} \) box; the premise at \( x_0 \), twice, gives the clash.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (R(x, y) \to \neg R(y, x))}
  \open[x_0]
  \open
  \hypo {2} {R(x_0, x_0)}
  \have {3} {\forall y\, (R(x_0, y) \to \neg R(y, x_0))} \Ae{1}
  \have {4} {R(x_0, x_0) \to \neg R(x_0, x_0)} \Ae{3}
  \have {5} {\neg R(x_0, x_0)} \ie{4,2}
  \have {6} {\bot} \ne{2,5}
  \close
  \have {7} {\neg R(x_0, x_0)} \ni{2-6}
  \close
  \have {8} {\forall x\, \neg R(x, x)} \Ai{2-7}
\end{nd}$
\end{center}
```

(b) Break. The domain \( \{0, 1\} \), \( R \) true of \( (0, 1) \) and \( (1, 0) \) only. No element is related to itself; \( R(0, 1) \) and \( R(1, 0) \) both hold.

(c) Derive: two flags, then an \( \rulename{{\to}I} \) box, then a \( \rulename{\neg I} \) box. Transitivity at \( x_0 \), \( y_0 \), \( x_0 \) turns the two assumptions into \( R(x_0, x_0) \), which irreflexivity refutes.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \neg R(x, x)}
  \hypo {2} {\forall x\, \forall y\, \forall z\, ((R(x, y) \wedge R(y, z)) \to R(x, z))}
  \open[x_0]
  \open[y_0]
  \open
  \hypo {3} {R(x_0, y_0)}
  \open
  \hypo {4} {R(y_0, x_0)}
  \have {5} {\forall y\, \forall z\, ((R(x_0, y) \wedge R(y, z)) \to R(x_0, z))} \Ae{2}
  \have {6} {\forall z\, ((R(x_0, y_0) \wedge R(y_0, z)) \to R(x_0, z))} \Ae{5}
  \have {7} {(R(x_0, y_0) \wedge R(y_0, x_0)) \to R(x_0, x_0)} \Ae{6}
  \have {8} {R(x_0, y_0) \wedge R(y_0, x_0)} \ai{3,4}
  \have {9} {R(x_0, x_0)} \ie{7,8}
  \have {10} {\neg R(x_0, x_0)} \Ae{1}
  \have {11} {\bot} \ne{9,10}
  \close
  \have {12} {\neg R(y_0, x_0)} \ni{4-11}
  \close
  \have {13} {R(x_0, y_0) \to \neg R(y_0, x_0)} \ii{3-12}
  \close
  \have {14} {\forall y\, (R(x_0, y) \to \neg R(y, x_0))} \Ai{3-13}
  \close
  \have {15} {\forall x\, \forall y\, (R(x, y) \to \neg R(y, x))} \Ai{3-14}
\end{nd}$
\end{center}
```

(d) Break. The domain \( \{0, 1\} \), \( R \) true of \( (0, 0) \) only. \( R \) is symmetric and transitive (the only pair is \( (0, 0) \)), and \( R(1, 1) \) fails.

(e) Derive. Inside the box, the partner \( f(x_0) \) plays the part that \( b \) played in Exercise C1 of Section 5.3.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (R(x, y) \to R(y, x))}
  \hypo {2} {\forall x\, \forall y\, \forall z\, ((R(x, y) \wedge R(y, z)) \to R(x, z))}
  \hypo {3} {\forall x\, R(x, f(x))}
  \open[x_0]
  \have {4} {R(x_0, f(x_0))} \Ae{3}
  \have {5} {\forall y\, (R(x_0, y) \to R(y, x_0))} \Ae{1}
  \have {6} {R(x_0, f(x_0)) \to R(f(x_0), x_0)} \Ae{5}
  \have {7} {R(f(x_0), x_0)} \ie{6,4}
  \have {8} {\forall y\, \forall z\, ((R(x_0, y) \wedge R(y, z)) \to R(x_0, z))} \Ae{2}
  \have {9} {\forall z\, ((R(x_0, f(x_0)) \wedge R(f(x_0), z)) \to R(x_0, z))} \Ae{8}
  \have {10} {(R(x_0, f(x_0)) \wedge R(f(x_0), x_0)) \to R(x_0, x_0)} \Ae{9}
  \have {11} {R(x_0, f(x_0)) \wedge R(f(x_0), x_0)} \ai{4,7}
  \have {12} {R(x_0, x_0)} \ie{10,11}
  \close
  \have {13} {\forall x\, R(x, x)} \Ai{4-12}
\end{nd}$
\end{center}
```

(f) Break. The domain \( \{0, 1\} \), \( R \) true of \( (0, 0) \), \( (1, 1) \) and \( (0, 1) \). \( R \) is reflexive; \( R(0, 1) \) holds and \( R(1, 0) \) does not.

(a) and (b) are converses, and only (a) derives. (d) is the trap "symmetric and transitive give reflexive", which breaks at an element related to nothing, and (e) repairs it by giving every element a partner \( f(x) \) (Exercise C1 of Section 5.3 shows the same for one element that has a partner).

**Marking scheme.** (10 points)
- 2 each for (a), (c), (e): flags opened in the order read off the goal, every \( \rulename{\forall E} \) at the flag (or at \( f(x_0) \)) the box needs, the side condition checked once at the last \( \rulename{\forall I} \).
- 1 each for (b), (d), (f): a counter-reading with the domain and every pair of \( R \) listed, each premise and the conclusion checked.
- 1: the closing sentence.
Fatal errors (0 for the claim): a \( \rulename{\forall I} \) over a flag that an open assumption mentions; a counter-reading that is not symmetric (in (d)) or not reflexive (in (f)).
:::

### C. Going deeper

::: {#exr-universal-introduction-c1}
[C1: How fresh is fresh?]

::: {.enumerate options="label=(\alph*)"}
1. Give a derivation of \( \forall x\, \forall y\, R(x, y) \vdash R(x_0, x_0) \wedge \forall x\, R(x, x) \) in which the line \( R(x_0, x_0) \) is written **before** a flagged box that uses the same name \( x_0 \). Check every clause of the side condition at the \( \rulename{\forall I} \) line.
2. A stronger condition is sometimes proposed: "\( x_0 \) occurs nowhere in the derivation outside its box". Does your derivation meet it? Explain why the conclusion of your derivation is nonetheless correct, so that the stronger condition forbids more than it needs to.
3. Could the last line of the flagged box in (a) be obtained by \( \rulename{R} \), repeating the earlier line \( R(x_0, x_0) \)? Is the result a derivation?
:::
:::

::: {.solution}
[Hint 1]

The goal is a conjunction. Derive the left conjunct first, by two \( \rulename{\forall E} \) lines outside any box.
:::

::: {.solution}
[Hint 2]

For the right conjunct, open a box flagged \( x_0 \) and instantiate the premise at \( x_0 \) again inside it. At the \( \rulename{\forall I} \) line, list the premises, the open assumptions and the conclusion, and look for \( x_0 \) in each.
:::

::: {.solution}
(a)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, R(x, y)}
  \have {2} {\forall y\, R(x_0, y)} \Ae{1}
  \have {3} {R(x_0, x_0)} \Ae{2}
  \open[x_0]
  \have {4} {\forall y\, R(x_0, y)} \Ae{1}
  \have {5} {R(x_0, x_0)} \Ae{4}
  \close
  \have {6} {\forall x\, R(x, x)} \Ai{4-5}
  \have {7} {R(x_0, x_0) \wedge \forall x\, R(x, x)} \ai{3,6}
\end{nd}$
\end{center}
```

The side condition at line 6. *Premises:* the only premise is line 1, \( \forall x\, \forall y\, R(x, y) \), and \( x_0 \) does not appear in it. *Open assumptions:* no box is open at line 6, so there are none. *Conclusion:* \( \forall x\, R(x, x) \) does not contain \( x_0 \). The last line of the box, line 5, is \( R(x, x)[x_0/x] \) and is a line of the box itself. So line 6 is legal, and the derivation has 7 lines. Lines 2, 3 and 7 mention \( x_0 \) outside the box, and the side condition does not ask about them.

(b) No: lines 2, 3 and 7 mention \( x_0 \) outside its box. Yet the conclusion is correct. The reason the side condition looks only at premises and open assumptions is that these are the only lines taken without proof, so they are the only lines that can single out what \( x_0 \) names; every other available line is derived from them. Lines 2 and 3 were derived from a premise that does not mention \( x_0 \); they hold whatever \( x_0 \) names. So the argument in the box really is about an arbitrary object, and \( \forall x\, R(x, x) \) follows. The stronger condition would reject this derivation, although renaming the box's flag to a new letter \( z_0 \) (lines 4–5 becoming \( \forall y\, R(z_0, y) \) and \( R(z_0, z_0) \)) gives a derivation that meets it and has the same last line. A condition that rejects a correct derivation for the spelling of a name forbids more than safety needs.

(c) Yes. \( \rulename{R} \) may copy into the box any line available there, and line 3 lies in no box, so it is available at every later line. With line 5 justified "\( \rulename{R} \) 3" (and line 4 deleted), the box is a single line \( R(x_0, x_0) \), and the side condition at the \( \rulename{\forall I} \) line is checked exactly as in (a): nothing in it looks at where the box's last line came from. The derivation is legal, and it is correct for the reason in (b): line 3 was derived from a premise that says nothing about \( x_0 \).

**Marking scheme.** (10 points)
- 2: the left conjunct by two \( \rulename{\forall E} \) lines at \( x_0 \), outside any box.
- 2: a flagged box with \( \rulename{\forall E} \) at the flag and \( \rulename{\forall I} \) citing it.
- 2: the side condition checked clause by clause: premise, open assumptions, conclusion.
- 2: (b) explains that lines outside the box that do not rest on premises or assumptions about \( x_0 \) cannot make \( x_0 \) special. Alternatively, 2 for showing that renaming the box's flag to a new letter gives a derivation that meets the stronger condition and has the same last line.
- 2: (c) correct answer with the availability check for the repeated line.
Fatal errors (0 for the step): claiming that line 3 makes line 6 illegal; checking the side condition against lines that are not premises, open assumptions or the conclusion.
:::

::: {#exr-universal-introduction-c2}
[C2: Find the error]

A student offers this proof.

> **Claim.** For every real number \( x \), \( x^2 - 2x + 1 \ge 0 \).
>
> **Proof.** (1) Let \( x \) be a real number. (2) At \( x = 0 \): \( 0 - 0 + 1 = 1 \ge 0 \). (3) At \( x = 1 \): \( 1 - 2 + 1 = 0 \ge 0 \). (4) At \( x = 2 \): \( 4 - 4 + 1 = 1 \ge 0 \). (5) So \( x^2 - 2x + 1 \ge 0 \), and since \( x \) was arbitrary, the claim holds for every real \( x \).

::: {.enumerate options="label=(\alph*)"}
1. Is the claim true?
2. Does the argument prove it? Name the step that fails and the rule it misuses.
3. Show that the step can lead to a false conclusion: give a polynomial \( g \) for which the same checks at \( x = 0, 1, 2 \) succeed and \( g(x) \ge 0 \) fails for some real \( x \).
4. Point to a correct proof.
:::
:::

::: {.solution}
[Hint 1]

Write lines (2)–(4) as formulas. Which terms do they mention?
:::

::: {.solution}
[Hint 2]

Write the student's proof as a derivation: open a box flagged \( x_0 \) for line (1), and write lines (2)–(4) as lines inside it. What would line (5) have to cite?
:::

::: {.solution}
(a) Yes. For every real \( x \), \( x^2 - 2x + 1 = (x - 1)^2 \ge 0 \), since a square is never negative.

(b) No. Lines (2)–(4) are true, and line (1) opens a flagged box, "let \( x \) be arbitrary". The error is in line (5). With \( \varphi \) the formula \( x^2 - 2 \cdot x + 1 \ge 0 \), lines (2)–(4) establish \( \varphi[0/x] \), \( \varphi[1/x] \) and \( \varphi[2/x] \): statements about the constants \( 0 \), \( 1 \), \( 2 \). None of them is \( \varphi[x_0/x] \) for the flag. Inside the box, nothing about the arbitrary \( x \) was ever proved. The first sentence of (5), "so \( x^2 - 2x + 1 \ge 0 \)", has the right form: it is \( \varphi[x_0/x] \), with the student's \( x \) as the flag. But no rule writes it: it is not a premise, an assumption or a repetition, and no rule takes \( \varphi[0/x] \), \( \varphi[1/x] \) and \( \varphi[2/x] \) to \( \varphi[x_0/x] \). So the closing "since \( x \) was arbitrary" applies \( \rulename{\forall I} \) to a box whose last line was never derived: the lines the box legally derives are all instances at constants, not the instance at the flag. Line (1) was idle: the argument never used the \( x \) it introduced.

(c) Take \( g(x) = x(x - 1)(x - 2) \). The same checks succeed: \( g(0) = 0 \ge 0 \), \( g(1) = 0 \ge 0 \), \( g(2) = 0 \ge 0 \). But \( g(-1) = (-1)(-2)(-3) = -6 < 0 \), so "\( g(x) \ge 0 \) for every real \( x \)" is false. So the pattern of (5), concluding "for every \( x \)" from checks at a few constants, can lead from true checks to a false conclusion. It is not an instance of \( \rulename{\forall I} \), as (b) showed. (A legal step never leads from true premises to a false conclusion; Section 7.2 states this.) The claim in (a) is true for a different reason, one that the argument never gave.

(d) The derivation under "How this rule looks in a mathematical proof": inside the box flagged \( x_0 \), \( \rulename{\forall E} \) applies "squares are not negative" at \( x_0 - 1 \), an arith line rewrites it as \( x_0^2 - 2x_0 + 1 \ge 0 \), and that line **is** \( \varphi[x_0/x] \), so \( \rulename{\forall I} \) applies.

**Marking scheme.** (10 points)
- 2: (a) the claim is true, with a reason (it is a square).
- 3: (b) names step (5) and \( \rulename{\forall I} \); says that lines (2)–(4) are instances at constants, not the instance at the flag.
- 3: (c) a polynomial that passes the three checks and fails somewhere, with both computations shown.
- 2: (d) a correct proof, generalizing over a statement proved about the arbitrary \( x \).
Fatal errors (0 for the step): answering (b) with "the claim is false"; a "counterexample" in (c) that fails one of the three checks or is non-negative everywhere.
:::

<!-- dependency ledger
def-rules-universal (claim): extension of def-derivation to flagged boxes; scope rule and availability unchanged | def-derivation (cited), extended inline in this section
def-rules-universal (example): over Z, 2 is even and 1 is odd; 1 > 0 and 0 > 0 fails; over N, y_0 + 1 > y_0 | school arithmetic; checked by verify/ch05/def-rules-universal.py
def-rules-universal (claim): "appear" includes the variable after a quantifier symbol | F1.4 §02 (after def-free-variable), recalled
def-rules-universal (claim): the box rule's last line must be a line of the box itself, as for ->I | def-derivation and def-rules-implication (F1.1 §05), recalled
exm-universal-introduction-derivations (solution): (phi[z/y])[z_0/z] = phi[z_0/y] when z, z_0 do not appear in phi | inline (both replace exactly the free occurrences of y; argued in the text)
exm-universal-introduction-derivations (solution): (psi[x_0/x])[y_0/y] = (psi[y_0/y])[x_0/x] for different x, y and flags x_0, y_0 different from each other and from x, y and not appearing in psi | inline (stated with its reason in the text)
exm-universal-introduction-derivations (solution): z_0 not appearing in phi is free for y in phi | F1.4 §02 (special cases after def-free-for), recalled
universal-introduction-empty (example): VI is a derived rule usable as one line on first-order formulas | prp-vacuous-implication (cited), def-derived-rule (cited; extended to first-order formulas inline, F1.4 §04), def-rule-schema (cited)
def-rules-universal (example): "A first flagged box": (x - 1)^2 = x^2 - 2x + 1 | school algebra ("arith", as in F1.4 §03); checked by verify/ch05/def-rules-universal.py
universal-introduction-errors (example): the warning's n = 1: 1 is odd and 1^2 = 1 is odd | school arithmetic
universal-introduction-errors (example): quick check reading over Z with R as !=, c = 0, y_0 = 1 | school arithmetic; checked by verify/ch05/def-rules-universal.py
exr-universal-introduction-a1 (solution): readings over Z with P, Q "even" and x_0 = 2 | school arithmetic
exr-universal-introduction-b2 (solution): a stalled search proves nothing; the converse is refuted in F1.6 §02 | F1.6 §02 (prose pointer only, nothing here rests on it)
exr-universal-introduction-b3 (solution): the three universal arithmetic premises are true over R | stated as premises; school facts (as in exm-abs-at-least-x)
exr-universal-introduction-c1 (solution): renaming the box's flag gives a derivation with the same last line | inline (checked line by line in the solution)
exr-universal-introduction-c2 (solution): g(x) = x(x - 1)(x - 2) is 0 at 0, 1, 2 and -6 at -1; x^2 - 2x + 1 = (x - 1)^2 | school arithmetic; checked by verify/ch05/exr-universal-introduction-c2.py
exr-universal-introduction-c2 (solution): a legal step never leads from true premises to a false conclusion | F1.6 §02 (stated); prose pointer only, nothing here rests on it (the illegality of (5) is shown directly in (b))
def-rules-universal (example): the WRONG/RIGHT pair: over Z with x_0 naming 1, 1 > 0 holds and 0 > 0 fails; arith x_0 > 0 gives x_0 + 1 > 0 | school arithmetic; checked by verify/ch05/def-rules-universal.py
def-rules-universal (example): Quick check on a free flag; Quick check on the premise P(x_0): over Z, P and Q "even", x_0 = 2 | school arithmetic
exm-universal-introduction-derivations (solution): part (b), the derivation and its side condition | checked by tools/check_fitch.py
exm-universal-introduction-critique (solution): over R, M + 1 > M, so no real number is at least every real number; x_0 <= x_0 + 1 (arith) | school order; the rejected line checked by tools/check_fitch.py (expect-invalid); exists-I is F1.4 §05 (in-chapter pointer, not used here)
exm-universal-introduction-instances (example): each row's new line replaces every occurrence of the flag; row 2's box immediately contains a ->I box | def-rules-universal, def-substitution (cited); no numbers
exr-universal-introduction-a1 (solution): D3 reading over Z with R as <, c = 5, x_0 = 1: 1 < 5 holds and not every integer is below 5 (6) | school arithmetic; checked by verify/ch05/def-rules-universal.py
exr-universal-introduction-a2 (solution): one-line verdicts and short derivations | def-rules-universal (cited); (d) and (l) checked by tools/check_fitch.py as typed in the blueprint
exr-universal-introduction-b4 (solution): P(x) does not lead to forall x P(x): over Z, P "even", x names 2 | counter-reading (school arithmetic); F1.6 §02 (prose pointer inside a solution, nothing rests on it)
exr-universal-introduction-b5 (solution): counter-readings (b), (d), (f) on {0, 1}: premises true, conclusion false; derivations (a), (c), (e) | counter-readings: informal truth over finite domains; checked by verify/ch05/exr-universal-introduction-b5.py; derivations checked by tools/check_fitch.py
-->
