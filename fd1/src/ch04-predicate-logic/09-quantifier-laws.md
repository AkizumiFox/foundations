# Negating and Moving Quantifiers

To prove that a sequence does **not** converge, or that a function is **not** uniformly continuous, we must use the negation of a definition, and a negation is only usable once the \( \neg \) has been pushed all the way in. "It is not the case that for every \( \varepsilon > 0 \) there is an \( N \) …" gives a proof nothing to hold. "There is an \( \varepsilon > 0 \) such that for every \( N \) there is an \( n \ge N \) with …" tells it what to find. Section 4.1 read the step from the first form to the second informally, as the challenger and the defender changing sides. This section derives the laws that make it exact, with the rules of Sections 4.3–4.6. Once they are proved, negating a definition is mechanical: one law per symbol, from the outside in. The section also derives the laws that move a quantifier across a connective, and it ends with a short analysis proof in which a negation and a well-chosen \( \varepsilon \) do the work.

## Not every, and some not

Section 4.1 called the two quantifiers mirror images: a single counterexample refutes a "for every", and a single witness confirms a "there exists". The mirror suggests four sequents. "Not every \( x \) satisfies \( \varphi \)" should say the same as "some \( x \) fails \( \varphi \)", and "no \( x \) satisfies \( \varphi \)" the same as "every \( x \) fails \( \varphi \)". Three of the four directions come straight out of the search method. The fourth does not, and the reason it does not is worth a close look.

*To negate a quantifier, flip it and move the \( \neg \) inside.*

In the derivations of this section, \( \neg\varphi[x_0/x] \) means \( (\neg\varphi)[x_0/x] \), which is \( \neg(\varphi[x_0/x]) \) by @def-substitution; the two readings give the same formula. The fresh name \( x_0 \) is always a variable different from \( x \) that does not appear in \( \varphi \) (or in \( \psi \), when there is one); so it does not appear in \( \forall x\, \varphi \) or \( \exists x\, \varphi \) either. The side conditions of \( \rulename{\forall I} \) and \( \rulename{\exists E} \) need this, and it also makes \( x_0 \) free for \( x \) in \( \varphi \) (Section 4.2).

::: {#prp-quantifier-negation}
[Quantifier Negation]

Let \( \varphi \) be a formula and \( x \) a variable.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg\forall x\, \varphi \vdash \exists x\, \neg\varphi \), by a derivation that uses \( \rulename{RAA} \);
2. \( \exists x\, \neg\varphi \vdash \neg\forall x\, \varphi \), by a derivation that does not;
3. \( \neg\exists x\, \varphi \dashv\vdash \forall x\, \neg\varphi \), both directions by derivations that do not use \( \rulename{RAA} \).
:::
:::

*Try it first (ten minutes): run the search method of Section 4.8 on (a). Which rule should give the last line, and what would that rule need from the premise?*

::: {.idea}
Start with (a), and with the obstacle. The goal \( \exists x\, \neg\varphi \) is an \( \exists \), so the search postpones it until an available line shows an instance \( \neg\varphi[t/x] \). None ever does. The premise \( \neg\forall x\, \varphi \) is a negation, and a negation is used only by clashing it with what it negates, \( \forall x\, \varphi \). It says that a counterexample exists and names none, so \( \rulename{\exists I} \) has nothing to act on. We are stuck, and the last step of the method applies: assume \( \neg\exists x\, \neg\varphi \), "no \( x \) fails \( \varphi \)", and hunt for a clash. The clash will be with the premise, so the new goal is \( \forall x\, \varphi \). Open a flagged box for it, with the goal \( \varphi[x_0/x] \). That goal is again stuck (we know nothing about \( \varphi \)), so a second \( \rulename{RAA} \) assumes \( \neg\varphi[x_0/x] \); and now an instance of \( \neg\varphi \) is on a line, so \( \rulename{\exists I} \) produces \( \exists x\, \neg\varphi \), which clashes with the outer assumption.

For (b) and (c) the method runs without getting stuck. A negated goal opens a \( \rulename{\neg I} \) box (Section 2.2); an \( \exists \) premise opens an \( \rulename{\exists E} \) box early (Section 4.6); a \( \forall \) goal opens a flagged box (Section 4.4). The clash comes in one of two ways. In (b), and in (c) right to left, the instance assumed in the \( \rulename{\exists E} \) box clashes with the matching instance that \( \rulename{\forall E} \) takes from the \( \forall \) line. In (c) left to right, \( \rulename{\exists I} \) turns the instance into \( \exists x\, \varphi \), which meets the premise \( \neg\exists x\, \varphi \).
:::

::: {.proof}
For (a), the derivation:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \forall x\, \varphi}
  \open
  \hypo {2} {\neg \exists x\, \neg \varphi}
  \open[x_0]
  \open
  \hypo {3} {\neg \varphi[x_0/x]}
  \have {4} {\exists x\, \neg \varphi} \Ei{3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\varphi[x_0/x]} \raa{3-5}
  \close
  \have {7} {\forall x\, \varphi} \Ai{3-6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {\exists x\, \neg \varphi} \raa{2-8}
\end{nd}$
\end{center}
```

Line 4 is \( \rulename{\exists I} \) at the term \( x_0 \), which is free for \( x \) in \( \neg\varphi \). At line 7 the side condition of \( \rulename{\forall I} \) holds: \( x_0 \) does not appear in the premise, in the assumption \( \neg\exists x\, \neg\varphi \) still open at line 7, or in \( \forall x\, \varphi \), since it is not \( x \) and does not appear in \( \varphi \); and line 6 is the last line of the flagged box.

For (b):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, \neg \varphi}
  \open
  \hypo {2} {\forall x\, \varphi}
  \open[x_0]
  \hypo {3} {\neg \varphi[x_0/x]}
  \have {4} {\varphi[x_0/x]} \Ae{2}
  \have {5} {\bot} \ne{4,3}
  \close
  \have {6} {\bot} \Ee{1,3-5}
  \close
  \have {7} {\neg \forall x\, \varphi} \ni{2-6}
\end{nd}$
\end{center}
```

At line 6, \( x_0 \) does not appear in \( \bot \), in \( \exists x\, \neg\varphi \), in the premise, or in the assumption \( \forall x\, \varphi \) still open there.

For (c), left to right and right to left:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \exists x\, \varphi}
  \open[x_0]
  \open
  \hypo {2} {\varphi[x_0/x]}
  \have {3} {\exists x\, \varphi} \Ei{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg \varphi[x_0/x]} \ni{2-4}
  \close
  \have {6} {\forall x\, \neg \varphi} \Ai{2-5}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\forall x\, \neg \varphi}
  \open
  \hypo {2} {\exists x\, \varphi}
  \open[x_0]
  \hypo {3} {\varphi[x_0/x]}
  \have {4} {\neg \varphi[x_0/x]} \Ae{1}
  \have {5} {\bot} \ne{3,4}
  \close
  \have {6} {\bot} \Ee{2,3-5}
  \close
  \have {7} {\neg \exists x\, \varphi} \ni{2-6}
\end{nd}$
\end{center}
```

In the first, line 5 is the instance of \( \neg\varphi \) at \( x_0 \), as \( \rulename{\forall I} \) requires, and \( x_0 \) appears neither in the premise nor in \( \forall x\, \neg\varphi \); no assumption is open at line 6. In the second, the side condition of \( \rulename{\exists E} \) at line 6 is checked as in (b). No line of the derivations of (b) and (c) is justified by \( \rulename{RAA} \), and the derivation of (a) uses it twice, at lines 6 and 9. This proves the proposition.
:::

So "not every" and "some not" are interderivable, and so are "none" and "every not". The direction that cost two \( \rulename{RAA} \) boxes is the one that **produces** an existential statement from a negative one. That is not an accident of our derivation: no derivation of (a) avoids \( \rulename{RAA} \). This is a claim about all derivations, which no search can establish, and we state it without proof (Chapter 3's optional @thm-raa-independent proves the propositional analogue for \( \neg\neg P \vdash P \)). Chapter 5 returns to what is at stake: the conclusion of (a) asserts that something fails \( \varphi \), and the derivation never says what. This is the law that Chapter 11 uses at the end of the proof of the Archimedean property, where "not every \( n \) satisfies \( n \le x \)" becomes "some \( n \) satisfies \( n > x \)".

::: {.check}
From the line \( \neg\forall x\, P(x) \), may a derivation write \( \neg P(c) \) for a constant \( c \)? If not, what may it write, and what does a derivation do next to use it?
:::

::: {.solution}
No. \( \neg\forall x\, P(x) \) says that **some** element fails \( P \), not that the element named \( c \) does: over \( \nZ \), with \( P \) read as "is even" and \( c \) as \( 0 \), \( \neg\forall x\, P(x) \) is true and \( \neg P(0) \) is false. By (a) the derivation may write \( \exists x\, \neg P(x) \). To use that line it opens an \( \rulename{\exists E} \) box with a **fresh** witness \( x_0 \) and the assumption \( \neg P(x_0) \) (Section 4.6), and nothing about \( c \) follows.
:::

**The laws as one line.** From now on a derivation may use any law of this section as one line, citing it, in the way @prp-bounded-quantifier-rules allows a bounded rule: the line abbreviates the derivation printed here, with \( \varphi \) (and \( \psi \)) replaced by the formulas at hand and the fresh name chosen so that it appears nowhere in the larger derivation. Then every side condition inside the pasted block still holds, since the block's premises become lines of the larger derivation and the name is new to all of them. In a derivation the justification is a short tag: QN (a) for @prp-quantifier-negation (a), NIm for @prp-negated-implication below, and VI for @prp-vacuous-implication.

## The negation of an implication

Every definition with a bounded \( \forall \) contains an implication, \( \forall x\, (x \in A \to \varphi) \), so negating it means negating an implication. The answer is the one Section 4.1 found for the wrong translation of a bounded \( \exists \): an implication fails exactly when its hypothesis holds and its conclusion does not. Chapter 2 met this law only as an exercise (@exr-finding-derivations-b1 (b)), and a proof in the text may not rest on an exercise, so we prove it here.

::: {#prp-negated-implication}
[Negated Implication]

For all formulas \( \varphi \) and \( \psi \),
\[
\neg(\varphi \to \psi) \dashv\vdash \varphi \wedge \neg\psi .
\]
The direction \( \vdash \) is derived with \( \rulename{RAA} \), and the direction \( \dashv \) without it.
:::

::: {.idea}
For \( \vdash \) the goal is a conjunction, so \( \rulename{\wedge I} \) asks for \( \varphi \) and \( \neg\psi \) separately. The premise is a negation, usable only to clash with \( \varphi \to \psi \), so in each part we manufacture \( \varphi \to \psi \). For \( \neg\psi \): open a \( \rulename{\neg I} \) box on \( \psi \); then \( \varphi \to \psi \) follows by \( \rulename{{\to}I} \), whose box repeats \( \psi \). For \( \varphi \) we are stuck, since \( \varphi \) has no known main connective; so \( \rulename{RAA} \) assumes \( \neg\varphi \), and \( \neg\varphi \) gives \( \varphi \to \psi \) by @prp-vacuous-implication. For \( \dashv \), the goal is a negation: assume \( \varphi \to \psi \) and clash \( \psi \) with \( \neg\psi \).
:::

::: {.proof}
The two derivations:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\varphi \to \psi)}
  \open
  \hypo {2} {\neg \varphi}
  \have {3} {\varphi \to \psi} \by{VI}{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\varphi} \raa{2-4}
  \open
  \hypo {6} {\psi}
  \open
  \hypo {7} {\varphi}
  \have {8} {\psi} \r{6}
  \close
  \have {9} {\varphi \to \psi} \ii{7-8}
  \have {10} {\bot} \ne{9,1}
  \close
  \have {11} {\neg \psi} \ni{6-10}
  \have {12} {\varphi \wedge \neg \psi} \ai{5,11}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\varphi \wedge \neg \psi}
  \open
  \hypo {2} {\varphi \to \psi}
  \have {3} {\varphi} \ae{1}
  \have {4} {\psi} \ie{2,3}
  \have {5} {\neg \psi} \ae{1}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg (\varphi \to \psi)} \ni{2-6}
\end{nd}$
\end{center}
```

Line 3 of the first derivation uses @prp-vacuous-implication as a derived rule (@def-derived-rule), and line 8 repeats line 6 into the box, since \( \rulename{{\to}I} \) needs \( \psi \) as a line of its own box. The only \( \rulename{RAA} \) is at line 5.
:::

The derivations use only the rules of Chapters 1 and 2, so the law holds for statements as well as formulas, and it may be used as a derived rule in the sense of @def-derived-rule. Over the real numbers: "if \( x > 2 \) then \( x^2 > 4 \)" fails for a given \( x \) exactly when \( x > 2 \) and \( x^2 \le 4 \).

## Bounded quantifiers keep their bounds

Analysis negates bounded quantifiers: \( \neg\forall \varepsilon > 0 \), \( \neg\exists N \in \nN \). The two laws so far combine into laws for them, and the combination has one surprise in it, which is no surprise once the bound is unfolded: **the bound stays as it is**.

*Negating a bounded quantifier flips the quantifier and keeps the bound.*

::: {#prp-bounded-quantifier-negation}
[Negating Bounded Quantifiers]

Let \( A \) be a fixed set, so that \( \in A \) is a one-place predicate symbol, let \( x \) be a variable and \( \varphi \) a formula. Then

::: {.enumerate options="label=(\alph*)"}
1. \( \neg\forall x \in A \; \varphi \dashv\vdash \exists x \in A \; \neg\varphi \), where \( \vdash \) is derived with \( \rulename{RAA} \) and \( \dashv \) without;
2. \( \neg\exists x \in A \; \varphi \dashv\vdash \forall x \in A \; \neg\varphi \), both directions without \( \rulename{RAA} \).
:::

The same holds with \( x \in A \) replaced by \( x > a \), or by \( x \ge a \), \( x < a \), \( x \le a \), for a term \( a \) in which \( x \) does not occur.
:::

So \( \neg\forall \varepsilon > 0\; \varphi \) becomes \( \exists \varepsilon > 0\; \neg\varphi \), and never \( \exists \varepsilon \le 0\; \neg\varphi \).

::: {.idea}
Unfold the bounds (@def-bounded-quantifier): (a) is \( \neg\forall x\, (x \in A \to \varphi) \dashv\vdash \exists x\, (x \in A \wedge \neg\varphi) \). Push the \( \neg \) through the quantifier by @prp-quantifier-negation, and then through the implication by @prp-negated-implication; the second step must happen under the \( \exists \), so it happens inside an \( \rulename{\exists E} \) box. The negation lands on \( \varphi \), and the bound \( x \in A \) comes out of the implication unnegated. For (b), the derivations of @prp-quantifier-negation (c) go through with the bounded rules of @prp-bounded-quantifier-rules in place of the unbounded ones.
:::

::: {.proof}
For (a), \( \vdash \) and \( \dashv \), with the bounds unfolded:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \forall x\, (x \in A \to \varphi)}
  \have {2} {\exists x\, \neg (x \in A \to \varphi)} \by{QN (a)}{1}
  \open[x_0]
  \hypo {3} {\neg (x_0 \in A \to \varphi[x_0/x])}
  \have {4} {x_0 \in A \wedge \neg \varphi[x_0/x]} \by{NIm}{3}
  \have {5} {\exists x\, (x \in A \wedge \neg \varphi)} \Ei{4}
  \close
  \have {6} {\exists x\, (x \in A \wedge \neg \varphi)} \Ee{2,3-5}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\exists x\, (x \in A \wedge \neg \varphi)}
  \open[x_0]
  \hypo {2} {x_0 \in A \wedge \neg \varphi[x_0/x]}
  \have {3} {\neg (x_0 \in A \to \varphi[x_0/x])} \by{NIm}{2}
  \have {4} {\exists x\, \neg (x \in A \to \varphi)} \Ei{3}
  \close
  \have {5} {\exists x\, \neg (x \in A \to \varphi)} \Ee{1,2-4}
  \have {6} {\neg \forall x\, (x \in A \to \varphi)} \by{QN (b)}{5}
\end{nd}$
\end{center}
```

Line 3 on the left is the instance at \( x_0 \) of \( \neg(x \in A \to \varphi) \), since \( A \) is not a variable; line 4 is @prp-negated-implication with \( x_0 \in A \) and \( \varphi[x_0/x] \) for \( \varphi \) and \( \psi \). At line 6, \( x_0 \) does not appear in the conclusion, in line 2 or in the premise, and no assumption is open. The right-hand derivation is checked the same way. The only use of \( \rulename{RAA} \) is inside the two cited laws on the left: in QN (a) and in the direction \( \vdash \) of NIm.

For (b), with the bounded rules:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \exists x \in A \; \varphi}
  \open[x_0]
  \hypo {2} {x_0 \in A}
  \open
  \hypo {3} {\varphi[x_0/x]}
  \have {4} {\exists x \in A \; \varphi} \Ei{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg \varphi[x_0/x]} \ni{3-5}
  \close
  \have {7} {\forall x \in A \; \neg \varphi} \Ai{2-6}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\forall x \in A \; \neg \varphi}
  \open
  \hypo {2} {\exists x \in A \; \varphi}
  \open[x_0]
  \hypo {3} {x_0 \in A}
  \hypo {4} {\varphi[x_0/x]}
  \have {5} {\neg \varphi[x_0/x]} \Ae{1,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\bot} \Ee{2,3-6}
  \close
  \have {8} {\neg \exists x \in A \; \varphi} \ni{2-7}
\end{nd}$
\end{center}
```

At line 7 on the left, the box's own assumption \( x_0 \in A \) has closed, and \( x_0 \) is in neither the premise nor the conclusion; at line 7 on the right, \( x_0 \) is not in \( \bot \), in line 2, in the premise, or in the open assumption on line 2. Neither derivation uses \( \rulename{RAA} \).

For the bounds \( x > a \) and the others, the same four derivations work with \( x > a \) and \( x_0 > a \) in place of \( x \in A \) and \( x_0 \in A \), choosing \( x_0 \) not to appear in \( a \); since \( x \) does not occur in \( a \), \( (x > a)[x_0/x] \) is \( x_0 > a \). This proves the proposition.
:::

::: {.warning}
**Negate the quantifier, not the bound** (Chapter 5 lists this among the wrong negations it catalogues). The negation of "\( a_n \to L \)" begins \( \exists \varepsilon > 0 \), not \( \exists \varepsilon \le 0 \). The wrong form, \( \exists \varepsilon \le 0\; \forall N \in \nN\; \exists n \in \nN\; (n \ge N \wedge \abs{a_n - L} \ge \varepsilon) \), is true for **every** sequence: \( \varepsilon = 0 \) works, since \( \abs{a_n - L} \ge 0 \) always. So it would "prove" that the constant sequence \( a_n = 0 \) does not converge to \( 0 \).
:::

## Moving a quantifier across a connective

Negation is not the only thing that needs moving. A formula such as \( \exists x\, P(x) \to \psi \) has its quantifier buried in a hypothesis, and proofs often want it outside, or the reverse. Two groups of laws do this. The **distribution** laws move a quantifier across \( \wedge \) or \( \vee \) when both sides mention \( x \); the **passage** laws move it across a connective when one side does not.

::: {#prp-quantifier-distribution}
[Distribution of Quantifiers]

For all formulas \( \varphi \), \( \psi \) and every variable \( x \):

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, (\varphi \wedge \psi) \dashv\vdash \forall x\, \varphi \wedge \forall x\, \psi \);
2. \( \exists x\, (\varphi \vee \psi) \dashv\vdash \exists x\, \varphi \vee \exists x\, \psi \);
3. \( \forall x\, \varphi \vee \forall x\, \psi \vdash \forall x\, (\varphi \vee \psi) \);
4. \( \exists x\, (\varphi \wedge \psi) \vdash \exists x\, \varphi \wedge \exists x\, \psi \).
:::

All four are derived without \( \rulename{RAA} \).
:::

The proposition collects laws that are mostly proved already. Its point is the comparison: \( \forall \) goes across \( \wedge \) and \( \exists \) across \( \vee \) in both directions, while \( \forall \) across \( \vee \) and \( \exists \) across \( \wedge \) go one way only.

::: {.idea}
Three of the four laws were derived in Sections 4.4 and 4.6 for \( P(x) \) and \( Q(x) \); only the fresh name's instances were used there, so formulas can take their place. For (c), the goal is a \( \forall \) and the premise a disjunction: open the flagged box first, then split on the premise inside it.
:::

::: {.proof}
(a) is @prp-forall-and, (d) is @prp-exists-and, and (b) is the derivation of \( \exists \) over \( \vee \) in @exm-existential-elimination-derivations. Those derivations are written with \( P(x) \) and \( Q(x) \); they work word for word with \( \varphi \) and \( \psi \) in their place, because they use nothing about \( P(x) \) and \( Q(x) \) beyond the instances at the fresh name, which is chosen different from \( x \) and not appearing in \( \varphi \) or \( \psi \).

For (c), the goal is a \( \forall \): open a flagged box. Inside it the premise is a disjunction, so split on it; in each case one \( \rulename{\forall E} \) at \( x_0 \) and one \( \rulename{\vee I} \) reach the instance of \( \varphi \vee \psi \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \varphi \vee \forall x\, \psi}
  \open[x_0]
  \open
  \hypo {2} {\forall x\, \varphi}
  \have {3} {\varphi[x_0/x]} \Ae{2}
  \have {4} {\varphi[x_0/x] \vee \psi[x_0/x]} \oi{3}
  \close
  \open
  \hypo {5} {\forall x\, \psi}
  \have {6} {\psi[x_0/x]} \Ae{5}
  \have {7} {\varphi[x_0/x] \vee \psi[x_0/x]} \oi{6}
  \close
  \have {8} {\varphi[x_0/x] \vee \psi[x_0/x]} \oe{1,2-4,5-7}
  \close
  \have {9} {\forall x\, (\varphi \vee \psi)} \Ai{2-8}
\end{nd}$
\end{center}
```

Line 8 is the instance of \( \varphi \vee \psi \) at \( x_0 \) and the last line of the flagged box; at line 9, \( x_0 \) is in neither the premise nor the conclusion, and no assumption is open. This proves the proposition.
:::

The converses of (c) and (d) are false. Over \( \nZ \), every integer is even or odd, but neither "every integer is even" nor "every integer is odd" holds; some integer is even and some integer is odd, but none is both. Section 4.11 turns these two observations into proofs that the converses are not derivable.

The passage laws need a condition: the quantified variable must not be free in the formula that the quantifier moves away from. Section 4.2 proved the fact that makes this work: if \( x \) is not free in \( \psi \), then \( \psi[t/x] = \psi \) for every term \( t \). So an instance of \( \psi \to \varphi \) at \( x_0 \) is \( \psi \to \varphi[x_0/x] \), with \( \psi \) untouched.

::: {#prp-quantifier-passage}
[Passage Laws]

Let \( \varphi \) and \( \psi \) be formulas and \( x \) a variable that is **not free in \( \psi \)**. Then

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, (\psi \to \varphi) \dashv\vdash \psi \to \forall x\, \varphi \);
2. \( \forall x\, (\varphi \to \psi) \dashv\vdash \exists x\, \varphi \to \psi \);
3. \( \exists x\, (\varphi \wedge \psi) \dashv\vdash \exists x\, \varphi \wedge \psi \);
4. \( \exists x\, (\varphi \to \psi) \dashv\vdash \forall x\, \varphi \to \psi \);
5. \( \exists x\, (\psi \to \varphi) \dashv\vdash \psi \to \exists x\, \varphi \).
:::

Of the ten directions, two are derived here with \( \rulename{RAA} \): \( \dashv \) in (d), through \( \rulename{LEM} \) and the cited QN (a), and \( \dashv \) in (e), through \( \rulename{LEM} \). The other eight are derived without it.
:::

Read (b) aloud: "everything with \( \varphi \) has \( \psi \)" says the same as "if something has \( \varphi \), then \( \psi \)". In (b) and (d) the quantifier changes from \( \forall \) to \( \exists \) or back as it leaves the hypothesis of an implication. That is the game reading of Section 4.1 once more: a quantifier in a hypothesis changes sides.

::: {.idea}
Each intuitionistic direction is a short run of the search method. A goal \( \to \) opens a \( \rulename{{\to}I} \) box; a goal \( \forall \) a flagged box; a premise \( \exists \) an \( \rulename{\exists E} \) box, early; a premise \( \forall \) is instantiated at \( x_0 \), where the condition on \( \psi \) keeps \( \psi \) unchanged; and the \( \exists \) goal waits for its witness \( x_0 \). The two classical directions get stuck. In (d), the premise \( \forall x\, \varphi \to \psi \) is usable only once \( \forall x\, \varphi \) is in hand, and it may not be; so decide it, by \( \rulename{LEM} \). If \( \forall x\, \varphi \) holds, then \( \psi \) holds, and \( \varphi \to \psi \) holds at every \( x \). If not, (a) of @prp-quantifier-negation supplies an \( x_0 \) with \( \neg\varphi[x_0/x] \), and \( \varphi[x_0/x] \to \psi \) is vacuously true. In (e), decide \( \psi \): if \( \psi \) holds, the premise supplies a witness; if not, \( \psi \to \varphi \) is vacuously true at every \( x \).
:::

::: {.proof}
In every derivation below, \( x_0 \) is a variable other than \( x \) that does not appear in \( \varphi \) or \( \psi \), and \( \psi[x_0/x] = \psi \) because \( x \) is not free in \( \psi \) (Section 4.2). So the instance at \( x_0 \) of \( \psi \to \varphi \) is \( \psi \to \varphi[x_0/x] \), and likewise for the other combinations.

(a), \( \vdash \) and \( \dashv \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (\psi \to \varphi)}
  \open
  \hypo {2} {\psi}
  \open[x_0]
  \have {3} {\psi \to \varphi[x_0/x]} \Ae{1}
  \have {4} {\varphi[x_0/x]} \ie{3,2}
  \close
  \have {5} {\forall x\, \varphi} \Ai{3-4}
  \close
  \have {6} {\psi \to \forall x\, \varphi} \ii{2-5}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\psi \to \forall x\, \varphi}
  \open[x_0]
  \open
  \hypo {2} {\psi}
  \have {3} {\forall x\, \varphi} \ie{1,2}
  \have {4} {\varphi[x_0/x]} \Ae{3}
  \close
  \have {5} {\psi \to \varphi[x_0/x]} \ii{2-4}
  \close
  \have {6} {\forall x\, (\psi \to \varphi)} \Ai{2-5}
\end{nd}$
\end{center}
```

At line 5 on the left the assumption \( \psi \) is open, and \( x_0 \) does not appear in it: this is where the fresh name must avoid \( \psi \).

(b), \( \vdash \) and \( \dashv \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (\varphi \to \psi)}
  \open
  \hypo {2} {\exists x\, \varphi}
  \open[x_0]
  \hypo {3} {\varphi[x_0/x]}
  \have {4} {\varphi[x_0/x] \to \psi} \Ae{1}
  \have {5} {\psi} \ie{4,3}
  \close
  \have {6} {\psi} \Ee{2,3-5}
  \close
  \have {7} {\exists x\, \varphi \to \psi} \ii{2-6}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\exists x\, \varphi \to \psi}
  \open[x_0]
  \open
  \hypo {2} {\varphi[x_0/x]}
  \have {3} {\exists x\, \varphi} \Ei{2}
  \have {4} {\psi} \ie{1,3}
  \close
  \have {5} {\varphi[x_0/x] \to \psi} \ii{2-4}
  \close
  \have {6} {\forall x\, (\varphi \to \psi)} \Ai{2-5}
\end{nd}$
\end{center}
```

At line 6 on the left, the conclusion \( \psi \) does not mention the witness \( x_0 \): this is where \( \rulename{\exists E} \)'s side condition meets the condition on \( \psi \).

(c), \( \vdash \) and \( \dashv \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, (\varphi \wedge \psi)}
  \open[x_0]
  \hypo {2} {\varphi[x_0/x] \wedge \psi}
  \have {3} {\varphi[x_0/x]} \ae{2}
  \have {4} {\exists x\, \varphi} \Ei{3}
  \have {5} {\psi} \ae{2}
  \have {6} {\exists x\, \varphi \wedge \psi} \ai{4,5}
  \close
  \have {7} {\exists x\, \varphi \wedge \psi} \Ee{1,2-6}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\exists x\, \varphi \wedge \psi}
  \have {2} {\exists x\, \varphi} \ae{1}
  \have {3} {\psi} \ae{1}
  \open[x_0]
  \hypo {4} {\varphi[x_0/x]}
  \have {5} {\varphi[x_0/x] \wedge \psi} \ai{4,3}
  \have {6} {\exists x\, (\varphi \wedge \psi)} \Ei{5}
  \close
  \have {7} {\exists x\, (\varphi \wedge \psi)} \Ee{2,4-6}
\end{nd}$
\end{center}
```

(d), \( \vdash \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, (\varphi \to \psi)}
  \open
  \hypo {2} {\forall x\, \varphi}
  \open[x_0]
  \hypo {3} {\varphi[x_0/x] \to \psi}
  \have {4} {\varphi[x_0/x]} \Ae{2}
  \have {5} {\psi} \ie{3,4}
  \close
  \have {6} {\psi} \Ee{1,3-5}
  \close
  \have {7} {\forall x\, \varphi \to \psi} \ii{2-6}
\end{nd}$
\end{center}
```

(d), \( \dashv \), with \( \rulename{LEM} \) on \( \forall x\, \varphi \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \varphi \to \psi}
  \have {2} {\forall x\, \varphi \vee \neg \forall x\, \varphi} \lem{}
  \open
  \hypo {3} {\forall x\, \varphi}
  \have {4} {\psi} \ie{1,3}
  \open
  \hypo {5} {\varphi}
  \have {6} {\psi} \r{4}
  \close
  \have {7} {\varphi \to \psi} \ii{5-6}
  \have {8} {\exists x\, (\varphi \to \psi)} \Ei{7}
  \close
  \open
  \hypo {9} {\neg \forall x\, \varphi}
  \have {10} {\exists x\, \neg \varphi} \by{QN (a)}{9}
  \open[x_0]
  \hypo {11} {\neg \varphi[x_0/x]}
  \have {12} {\varphi[x_0/x] \to \psi} \by{VI}{11}
  \have {13} {\exists x\, (\varphi \to \psi)} \Ei{12}
  \close
  \have {14} {\exists x\, (\varphi \to \psi)} \Ee{10,11-13}
  \close
  \have {15} {\exists x\, (\varphi \to \psi)} \oe{2,3-8,9-14}
\end{nd}$
\end{center}
```

Line 8 is \( \rulename{\exists I} \) at the term \( x \) itself: \( (\varphi \to \psi)[x/x] \) is \( \varphi \to \psi \), as in @prp-forall-implies-exists, and as there the step is sound because every domain is non-empty (Section 4.11). At line 14, \( x_0 \) is in neither the conclusion nor line 10, nor in the premise or the open assumption \( \neg\forall x\, \varphi \).

(e), \( \vdash \) and \( \dashv \), the second with \( \rulename{LEM} \) on \( \psi \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, (\psi \to \varphi)}
  \open
  \hypo {2} {\psi}
  \open[x_0]
  \hypo {3} {\psi \to \varphi[x_0/x]}
  \have {4} {\varphi[x_0/x]} \ie{3,2}
  \have {5} {\exists x\, \varphi} \Ei{4}
  \close
  \have {6} {\exists x\, \varphi} \Ee{1,3-5}
  \close
  \have {7} {\psi \to \exists x\, \varphi} \ii{2-6}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\psi \to \exists x\, \varphi}
  \have {2} {\psi \vee \neg \psi} \lem{}
  \open
  \hypo {3} {\psi}
  \have {4} {\exists x\, \varphi} \ie{1,3}
  \open[x_0]
  \hypo {5} {\varphi[x_0/x]}
  \open
  \hypo {6} {\psi}
  \have {7} {\varphi[x_0/x]} \r{5}
  \close
  \have {8} {\psi \to \varphi[x_0/x]} \ii{6-7}
  \have {9} {\exists x\, (\psi \to \varphi)} \Ei{8}
  \close
  \have {10} {\exists x\, (\psi \to \varphi)} \Ee{4,5-9}
  \close
  \open
  \hypo {11} {\neg \psi}
  \have {12} {\psi \to \varphi} \by{VI}{11}
  \have {13} {\exists x\, (\psi \to \varphi)} \Ei{12}
  \close
  \have {14} {\exists x\, (\psi \to \varphi)} \oe{2,3-10,11-13}
\end{nd}$
\end{center}
```

Line 13 is again \( \rulename{\exists I} \) at the variable \( x \). At line 10, \( x_0 \) is in neither the conclusion \( \exists x\, (\psi \to \varphi) \) nor line 4, \( \exists x\, \varphi \), nor in the premise or the open assumption \( \psi \) of line 3. In each of the eight other derivations, the side conditions are checked as in @prp-quantifier-negation, and \( \rulename{LEM} \) and \( \rulename{RAA} \) do not occur. This proves the proposition.
:::

**Why the condition on \( \psi \).** Drop it, and (b) fails. Take \( \varphi \) and \( \psi \) both to be \( P(x) \). Then \( \forall x\, (P(x) \to P(x)) \) is true in every domain, while \( \exists x\, P(x) \to P(x) \), over \( \nZ \) with \( P \) read as "is even" and \( x \) read as \( 1 \), says "if some integer is even, then \( 1 \) is even", which is false. The derivation of (b) shows where the condition was used. Without it, line 4 would be \( P(x_0) \to P(x_0) \), line 5 would be \( P(x_0) \), and the \( \rulename{\exists E} \) box could not close on a line that mentions its witness.

::: {.check}
A student writes \( \forall x\, (x > 0 \to \exists y\, (y \cdot y = x)) \) as \( \forall x\, \exists y\, (x > 0 \to y \cdot y = x) \), citing a passage law. Which law, and is the condition met?
:::

::: {.solution}
Law (e) of @prp-quantifier-passage, applied under \( \forall x \) (a law may be used on a part under a quantifier; the next subsection says why), with \( \psi \) the formula \( x > 0 \), \( \varphi \) the formula \( y \cdot y = x \), and \( y \) as the moving variable. The condition asks that \( y \) not be free in \( \psi \), and \( y \) does not occur in \( x > 0 \); so the step is correct. It is the classical direction of (e), the one derived with \( \rulename{LEM} \).
:::

## Negating a definition, mechanically

With the laws in hand, negating a definition is a procedure.

::: {.algorithm}
**Negating a formula.**

1. **Rewrite \( \leftrightarrow \)** as two implications, by @prp-iff-two-implications.
2. **Push \( \neg \) inward**, one symbol at a time, from the outside, citing a law at each step:
   - \( \neg\forall x \) becomes \( \exists x\, \neg \), and \( \neg\exists x \) becomes \( \forall x\, \neg \) (@prp-quantifier-negation); a bounded quantifier keeps its bound (@prp-bounded-quantifier-negation);
   - \( \neg(\alpha \to \beta) \) becomes \( \alpha \wedge \neg\beta \) (@prp-negated-implication);
   - \( \neg(\alpha \wedge \beta) \) becomes \( \neg\alpha \vee \neg\beta \), and \( \neg(\alpha \vee \beta) \) becomes \( \neg\alpha \wedge \neg\beta \) (De Morgan, @prp-de-morgan);
   - \( \neg\neg\alpha \) becomes \( \alpha \) (@prp-double-negation).
3. **Stop at atomic formulas.** In an ordered domain, replace \( \neg(s < t) \) by \( s \ge t \) and \( \neg(s \le t) \) by \( s > t \); these are facts about the order, not laws of logic.

Each step of 1 and 2 replaces a part of the formula by a part provably equivalent to it. Write that chain with \( \dashv\vdash \) between the stages, not \( \equiv \). Step 3 is not a law of logic: make its replacements after the chain, citing the order fact.
:::

Why may a step act on a part buried inside the formula? Because provable equivalence passes through every symbol. If \( \alpha \dashv\vdash \beta \), then \( \neg\alpha \dashv\vdash \neg\beta \): from \( \neg\alpha \), a \( \rulename{\neg I} \) box on \( \beta \) derives \( \alpha \) from \( \beta \) and clashes it with \( \neg\alpha \), and the other direction is the same with the letters exchanged. Also \( \alpha \wedge \gamma \dashv\vdash \beta \wedge \gamma \), and the same holds for the other connectives, with the part on either side, by pasting the given derivations into the boxes of the connective's rules. Under a quantifier, \( \forall x\, \alpha \vdash \forall x\, \beta \) by a flagged box: \( \rulename{\forall E} \) at \( x_0 \), the derivation of \( \alpha[x_0/x] \vdash \beta[x_0/x] \), and \( \rulename{\forall I} \); and \( \exists x\, \alpha \vdash \exists x\, \beta \) by an \( \rulename{\exists E} \) box ending in \( \rulename{\exists I} \). Here \( x_0 \) is fresh: a variable other than \( x \) that appears in neither \( \alpha \) nor \( \beta \). The derivation of \( \alpha[x_0/x] \vdash \beta[x_0/x] \) is available because each law used holds for **every** formula that meets its condition, in particular for the instances at \( x_0 \). The laws this book applies to parts have only two kinds of condition, and both survive, for the same reason. A passage law of @prp-quantifier-passage asks that its moving variable \( y \) not be free in \( \psi \); since \( y \) appears in \( \beta \), the fresh \( x_0 \) is not \( y \). If \( y \) is \( x \) itself, substitution stops at the quantifier on \( x \), and \( \psi[x_0/x] \) is \( \psi \) because \( x \) is not free in \( \psi \); the pair is then the law's own instance, unchanged. Otherwise substituting \( x_0 \) for \( x \) passes the quantifier on \( y \) unchanged, and \( \psi[x_0/x] \) has no free variable that \( \psi \) lacks except \( x_0 \), and \( y \) is not free in it either. A law of @prp-bounded-quantifier-negation with a bound such as \( z > a \) asks that its bound variable \( z \) not occur in the term \( a \); since \( z \) appears in \( \beta \), again \( x_0 \) is not \( z \). If \( z \) is \( x \), substitution stops at the quantifier on \( x \) and the pair is unchanged; otherwise it passes the quantifier on \( z \), and \( a[x_0/x] \) contains no variable that \( a \) lacks except \( x_0 \), so \( z \) does not occur in it. So the pair \( \alpha[x_0/x] \), \( \beta[x_0/x] \) is again an instance of the same law, with its condition met. A part sitting under several symbols is reached one symbol at a time.

::: {#exm-negating-definitions}
[Three negations from analysis]

Negate each statement into positive form: no \( \neg \) in front of a quantifier, a connective or an inequality. Work over \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. \( a_n \to L \): \( \forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; \bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr) \).
2. \( s \) is the supremum of \( A \), in the two-clause form "\( s \) is an upper bound of \( A \), and for every \( \varepsilon > 0 \) some element of \( A \) exceeds \( s - \varepsilon \)":
\[
\forall x \in A \; (x \le s) \;\wedge\; \forall \varepsilon > 0 \; \exists x \in A \; (s - \varepsilon < x) .
\]
3. \( f \) is uniformly continuous on \( A \): \( \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; \bigl( \abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon \bigr) \).
:::
:::

::: {.solution}
*(a)* Three quantifiers, then an implication, then an inequality:
\[
\begin{aligned}
&\neg \forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; \bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr) \\
\dashv\vdash\; &\exists \varepsilon > 0 \; \neg \exists N \in \nN \; \forall n \in \nN \; \bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr) \\
\dashv\vdash\; &\exists \varepsilon > 0 \; \forall N \in \nN \; \neg \forall n \in \nN \; \bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr) \\
\dashv\vdash\; &\exists \varepsilon > 0 \; \forall N \in \nN \; \exists n \in \nN \; \neg \bigl( n \ge N \to \abs{a_n - L} < \varepsilon \bigr) \\
\dashv\vdash\; &\exists \varepsilon > 0 \; \forall N \in \nN \; \exists n \in \nN \; \bigl( n \ge N \wedge \neg (\abs{a_n - L} < \varepsilon) \bigr).
\end{aligned}
\]
The first three steps are @prp-bounded-quantifier-negation, the fourth is @prp-negated-implication. Last, the order fact turns \( \neg(\abs{a_n - L} < \varepsilon) \) into \( \abs{a_n - L} \ge \varepsilon \):
\[
\exists \varepsilon > 0 \; \forall N \in \nN \; \exists n \in \nN \; \bigl( n \ge N \wedge \abs{a_n - L} \ge \varepsilon \bigr).
\]
In words: some \( \varepsilon > 0 \) is such that, however far out we start, some later term is at least \( \varepsilon \) away from \( L \). Every bound stayed, and the order of the quantifiers stayed: \( \varepsilon \), then \( N \), then \( n \).

*(b)* The outer symbol is \( \wedge \). By De Morgan the negation becomes a disjunction, and each side is negated on its own:
\[
\begin{aligned}
&\neg \bigl( \forall x \in A \; (x \le s) \;\wedge\; \forall \varepsilon > 0 \; \exists x \in A \; (s - \varepsilon < x) \bigr) \\
\dashv\vdash\; &\neg \forall x \in A \; (x \le s) \;\vee\; \neg \forall \varepsilon > 0 \; \exists x \in A \; (s - \varepsilon < x) \\
\dashv\vdash\; &\exists x \in A \; \neg (x \le s) \;\vee\; \exists \varepsilon > 0 \; \forall x \in A \; \neg (s - \varepsilon < x).
\end{aligned}
\]
The first step is @prp-de-morgan, (d) for \( \vdash \) and (c) for \( \dashv \); the second is @prp-bounded-quantifier-negation, (a) on the left and (a) then (b) on the right. Last, the order facts turn \( \neg(x \le s) \) into \( s < x \) and \( \neg(s - \varepsilon < x) \) into \( x \le s - \varepsilon \):
\[
\exists x \in A \; (s < x) \;\vee\; \exists \varepsilon > 0 \; \forall x \in A \; (x \le s - \varepsilon).
\]
In words: \( s \) fails to be the supremum when some element of \( A \) lies above it (it is not an upper bound), or when some \( s - \varepsilon \) with \( \varepsilon > 0 \) is still an upper bound (it is not the least).

*(c)* Four quantifiers and an implication:
\[
\begin{aligned}
&\neg \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \in A \; \forall y \in A \; \bigl( \abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon \bigr) \\
\dashv\vdash\; &\exists \varepsilon > 0 \; \forall \delta > 0 \; \exists x \in A \; \exists y \in A \; \neg \bigl( \abs{x - y} < \delta \to \abs{f(x) - f(y)} < \varepsilon \bigr) \\
\dashv\vdash\; &\exists \varepsilon > 0 \; \forall \delta > 0 \; \exists x \in A \; \exists y \in A \; \bigl( \abs{x - y} < \delta \wedge \neg (\abs{f(x) - f(y)} < \varepsilon) \bigr),
\end{aligned}
\]
where the first step is four uses of @prp-bounded-quantifier-negation, and the second is @prp-negated-implication. Last, the order fact turns \( \neg(\abs{f(x) - f(y)} < \varepsilon) \) into \( \abs{f(x) - f(y)} \ge \varepsilon \):
\[
\exists \varepsilon > 0 \; \forall \delta > 0 \; \exists x \in A \; \exists y \in A \; \bigl( \abs{x - y} < \delta \wedge \abs{f(x) - f(y)} \ge \varepsilon \bigr).
\]
In words: one \( \varepsilon > 0 \) defeats every \( \delta \): however small \( \delta > 0 \) is, two points of \( A \) closer than \( \delta \) have values at least \( \varepsilon \) apart. To prove that a function is **not** uniformly continuous, this is the statement to prove, and it says exactly what to exhibit: first \( \varepsilon \); then, for an arbitrary \( \delta \), the two points \( x \) and \( y \), which may depend on \( \delta \). Section 4.10 does this for \( x^2 \) on \( \nR \).
:::

The same procedure finishes the rewriting promised in Section 4.8 for "there is no largest prime". By @prp-quantifier-negation (c),
\[
\begin{aligned}
&\neg \exists p \; \bigl( \mathrm{Prime}(p) \wedge \forall q \; (\mathrm{Prime}(q) \to q \le p) \bigr) \\
\dashv\vdash\; &\forall p \; \neg \bigl( \mathrm{Prime}(p) \wedge \forall q \; (\mathrm{Prime}(q) \to q \le p) \bigr).
\end{aligned}
\]
A negated conjunction \( \neg(\alpha \wedge \beta) \) is interderivable with \( \alpha \to \neg\beta \): De Morgan's law (@prp-de-morgan (d)) and @prp-implication-as-disjunction (a) give one direction, and (b) of the latter with @prp-de-morgan (c) the other. Then @prp-quantifier-negation (a) and (b) turn \( \neg\forall q\, (\mathrm{Prime}(q) \to q \le p) \) into \( \exists q\, \neg(\mathrm{Prime}(q) \to q \le p) \), and @prp-negated-implication, used under \( \exists q \), pushes the last \( \neg \) in; both steps act on a part, as the paragraph before @exm-negating-definitions allows:
\[
\forall p \; \Bigl( \mathrm{Prime}(p) \to \exists q \; \bigl( \mathrm{Prime}(q) \wedge \neg(q \le p) \bigr) \Bigr).
\]
The quantifier \( \forall q\, (\mathrm{Prime}(q) \to \dots) \) works like a bounded one, with the bound \( \mathrm{Prime}(q) \). That bound is not one that @prp-bounded-quantifier-negation covers, but the same two steps work for it, and the bound stays unnegated.

::: {.check}
Negate "every non-empty set of reals that is bounded above has a supremum", writing \( E(A) \) for "\( A \) is non-empty", \( B(A) \) for "\( A \) is bounded above" and \( S(A) \) for "\( A \) has a supremum", with the variable \( A \) ranging over sets of reals.
:::

::: {.solution}
The statement is \( \forall A\, \bigl( (E(A) \wedge B(A)) \to S(A) \bigr) \). By @prp-quantifier-negation (a) and (b) and then @prp-negated-implication, its negation is
\[
\exists A \; \bigl( (E(A) \wedge B(A)) \wedge \neg S(A) \bigr):
\]
there is a non-empty set of reals, bounded above, with no supremum. The two conditions are not negated: they stay as conditions on the counterexample, just as a bound stays with its quantifier.
:::

::: {.warning}
**The negation of an implication is not an implication.** "If \( x > 2 \), then \( x^2 > 4 \)" is not negated by "if \( x > 2 \), then \( x^2 \le 4 \)", nor by "if \( x \le 2 \), then \( x^2 \le 4 \)". For \( x = 0 \) the original is true (its hypothesis fails), and so is the second candidate, so the candidate cannot be its negation. The negation is \( x > 2 \wedge x^2 \le 4 \) (@prp-negated-implication), and it is false for every real \( x \). Chapter 5 catalogues this slip among the wrong negations.
:::

## How the laws look in a mathematical proof

Chapter 2 proved, in @exm-raa-zero, that a number \( x \ge 0 \) below every positive number is \( 0 \). Its key step chose \( \varepsilon \coloneqq x/2 \), and the reading after it said that "the hypothesis applies to it" is a rule for "every" that Chapter 4 would make precise. The rule is \( \rulename{\forall E} \), in its bounded form (@prp-bounded-quantifier-rules), at a term built from the data. Here is the same move once more, the way it appears in analysis.

*Two real numbers that are closer than every positive number are equal.*

::: {#prp-arbitrarily-close-equal}
[Arbitrarily Close Numbers Are Equal]

Let \( a \) and \( b \) be real numbers. If \( \abs{a - b} < \varepsilon \) for every \( \varepsilon > 0 \), then \( a = b \).
:::

::: {.idea}
The goal \( a = b \) is atomic, so no introduction rule applies, and the hypothesis is a \( \forall \) whose instances are all inequalities, never an equation. We are stuck, so suppose \( a \ne b \). The hypothesis may be instantiated at any positive term, so choose the term that makes the numbers collide: \( \varepsilon \coloneqq \abs{a - b} \), which is positive exactly because \( a \ne b \).
:::

::: {.proof}
Suppose that \( \abs{a - b} < \varepsilon \) for every \( \varepsilon > 0 \), and suppose, for a contradiction, that \( a \ne b \) [an \( \rulename{RAA} \) box]. Then \( a - b \ne 0 \), so \( \abs{a - b} > 0 \), by the school fact that \( \abs{u} > 0 \) for every real \( u \ne 0 \). So the hypothesis applies to the term \( \abs{a - b} \) [bounded \( \rulename{\forall E} \), citing the line \( \abs{a - b} > 0 \)] and gives \( \abs{a - b} < \abs{a - b} \). No real number is less than itself, so this is a contradiction [\( \rulename{\neg E} \)]. Hence \( a = b \) [\( \rulename{RAA} \)].
:::

The last step is a genuine \( \rulename{RAA} \): the box assumed \( \neg(a = b) \), written \( a \ne b \), and concluded \( a = b \); \( \rulename{\neg I} \) would only have given \( \neg\neg(a = b) \). The hypothesis cannot be weakened to "for **some** \( \varepsilon > 0 \)": \( a = 0 \), \( b = \frac12 \), \( \varepsilon = 1 \) satisfy \( \abs{a - b} < \varepsilon \) and \( a \ne b \). The facts about \( \abs{\cdot} \) used here are school algebra; Chapter 11 proves them from the axioms of \( \nR \).

Read the result through the negation laws. Its contrapositive says: if \( a \ne b \), then \( \neg\forall \varepsilon > 0\, (\abs{a - b} < \varepsilon) \), which by @prp-bounded-quantifier-negation is interderivable with \( \exists \varepsilon > 0\, \neg(\abs{a - b} < \varepsilon) \), that is, by the order fact, \( \exists \varepsilon > 0\, (\abs{a - b} \ge \varepsilon) \). The proof did not search for that \( \varepsilon \): it named it, \( \abs{a - b} \), from the data. A proof by contradiction in analysis is usually this shape. Negate the goal; the negation hands over an object (here the positive number \( \abs{a - b} \)); feed it to a hypothesis that holds for **every** object of its kind.

## Exercises

### A. Check your understanding

::: {#exr-quantifier-laws-a1}
[A1]

These parts are about the derivation of @prp-quantifier-negation (a).

::: {.enumerate options="label=(\alph*)"}
1. Which lines are justified by \( \rulename{RAA} \), and what does each of the two boxes assume and conclude?
2. Why can the derivation not reach \( \exists x\, \neg\varphi \) by one \( \rulename{\exists I} \) directly from the premise?
3. Line 4 is an \( \rulename{\exists I} \) at \( x_0 \). Why is its conclusion not the conclusion of the derivation, although the two formulas are the same?
4. Run the derivation with \( \varphi \) the formula \( x \cdot x \ne 2 \), over \( \nR \). Write lines 1 and 9 in words. Does any line name the number \( \sqrt 2 \)? What more would be needed to reach \( \exists x\, (x \cdot x = 2) \)?
5. True or false, with a reason: \( \exists \varepsilon \le 0\; \neg\varphi \) is a correct way to write the negation of \( \forall \varepsilon > 0\; \varphi \).
:::
:::

::: {.solution}
*(a)* Lines 6 and 9. The inner box (lines 3–5) assumes \( \neg\varphi[x_0/x] \), reaches \( \bot \), and line 6 concludes \( \varphi[x_0/x] \). The outer box (lines 2–8) assumes \( \neg\exists x\, \neg\varphi \), reaches \( \bot \), and line 9 concludes \( \exists x\, \neg\varphi \).

*(b)* \( \rulename{\exists I} \) needs a line holding an instance \( \neg\varphi[t/x] \). The premise \( \neg\forall x\, \varphi \) is not such an instance (its main symbol is \( \neg \) followed by \( \forall \)), and no rule takes it apart except \( \rulename{\neg E} \), which needs \( \forall x\, \varphi \). The premise says a counterexample exists without naming one.

*(c)* Line 4 lies inside three boxes: the box opened at line 2, and the flagged box of \( x_0 \) and the inner box, both opened at line 3. It depends on the assumptions on lines 2 and 3, so it is not available at the end. It is used only to clash with line 2. The conclusion on line 9 is reached by closing the outer box with \( \rulename{RAA} \).

*(d)* Line 1: "not every real number has a square different from \( 2 \)". Line 9: "some real number does not have a square different from \( 2 \)", that is, \( \exists x\, \neg(x \cdot x \ne 2) \). No line names \( \sqrt 2 \): the only witness on any line is the fresh name \( x_0 \), inside boxes that closed, and line 9 comes from \( \rulename{RAA} \), not from \( \rulename{\exists I} \). To reach \( \exists x\, (x \cdot x = 2) \), open an \( \rulename{\exists E} \) box on line 9 with the assumption \( \neg(x_1 \cdot x_1 \ne 2) \), apply \( \rulename{\neg\neg E} \) (the formula \( x_1 \cdot x_1 \ne 2 \) is \( \neg(x_1 \cdot x_1 = 2) \)) to get \( x_1 \cdot x_1 = 2 \), and close with \( \rulename{\exists I} \).

*(e)* False. By @prp-bounded-quantifier-negation the negation is \( \exists \varepsilon > 0\; \neg\varphi \): the bound stays. The wrong form can be true together with the statement it claims to negate. Over \( \nR \), take \( \varphi \) to be \( \varepsilon > 0 \): then \( \forall \varepsilon > 0\, (\varepsilon > 0) \) is true, and \( \exists \varepsilon \le 0\; \neg(\varepsilon > 0) \) is true as well, with the witness \( \varepsilon = 0 \). A statement and its negation are never both true.
:::

### B. Practice

::: {#exr-quantifier-laws-b1}
[B1: Four negations]

Negate each definition into positive form, citing the law used at each step. Work over \( \nR \), with \( (a_n) \) a sequence and \( f \) a function.

::: {.enumerate options="label=(\alph*)"}
1. \( (a_n) \) is bounded: \( \exists M \; \forall n \in \nN \; (\abs{a_n} \le M) \).
2. \( f \) is increasing on \( A \): \( \forall x \in A \; \forall y \in A \; \bigl( x < y \to f(x) \le f(y) \bigr) \).
3. \( \lim_{x \to a} f(x) = L \): \( \forall \varepsilon > 0 \; \exists \delta > 0 \; \forall x \; \bigl( (0 < \abs{x - a} \wedge \abs{x - a} < \delta) \to \abs{f(x) - L} < \varepsilon \bigr) \).
4. \( (a_n) \) is a Cauchy sequence: \( \forall \varepsilon > 0 \; \exists N \in \nN \; \forall m \in \nN \; \forall n \in \nN \; \bigl( (m \ge N \wedge n \ge N) \to \abs{a_m - a_n} < \varepsilon \bigr) \).
:::
:::

::: {.solution}
*(a)* By @prp-quantifier-negation (c) (the \( \exists M \) has no bound), then @prp-bounded-quantifier-negation (a) under \( \forall M \):
\[
\neg \exists M \; \forall n \in \nN \; (\abs{a_n} \le M)
\dashv\vdash
\forall M \; \neg \forall n \in \nN \; (\abs{a_n} \le M)
\dashv\vdash
\forall M \; \exists n \in \nN \; \neg (\abs{a_n} \le M),
\]
and the order fact turns \( \neg(\abs{a_n} \le M) \) into \( \abs{a_n} > M \):
\[
\forall M \; \exists n \in \nN \; (\abs{a_n} > M).
\]
Every real number is exceeded by the size of some term.

*(b)* Two uses of @prp-bounded-quantifier-negation, then @prp-negated-implication and the order fact:
\[
\exists x \in A \; \exists y \in A \; \bigl( x < y \wedge f(x) > f(y) \bigr).
\]
Two points of \( A \), in increasing order, whose values are in decreasing order.

*(c)* @prp-bounded-quantifier-negation twice, @prp-quantifier-negation (a) and (b) for the unbounded \( \forall x \), @prp-negated-implication, and the order fact:
\[
\exists \varepsilon > 0 \; \forall \delta > 0 \; \exists x \; \bigl( (0 < \abs{x - a} \wedge \abs{x - a} < \delta) \wedge \abs{f(x) - L} \ge \varepsilon \bigr).
\]
The hypothesis \( 0 < \abs{x - a} < \delta \) is not negated: it moves, unchanged, into a conjunction.

*(d)* @prp-bounded-quantifier-negation four times, @prp-negated-implication, the order fact:
\[
\exists \varepsilon > 0 \; \forall N \in \nN \; \exists m \in \nN \; \exists n \in \nN \; \bigl( (m \ge N \wedge n \ge N) \wedge \abs{a_m - a_n} \ge \varepsilon \bigr).
\]
For some \( \varepsilon > 0 \), however far out we start, two later terms are at least \( \varepsilon \) apart.
:::

::: {#exr-quantifier-laws-b2}
[B2: Two passage laws in one derivation]

Derive \( \exists x\, P(x) \to \forall y\, Q(y) \vdash \forall x\, \forall y\, \bigl( P(x) \to Q(y) \bigr) \) without \( \rulename{RAA} \). Then name the two laws of @prp-quantifier-passage that the sequent combines, and say how.
:::

::: {.solution}
The goal is \( \forall x \), then \( \forall y \), then \( \to \): open two flagged boxes and a \( \rulename{{\to}I} \) box, in the goal's order. Inside, the premise is an implication whose hypothesis \( \exists x\, P(x) \) comes from the assumption \( P(x_0) \) by \( \rulename{\exists I} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, P(x) \to \forall y\, Q(y)}
  \open[x_0]
  \open[y_0]
  \open
  \hypo {2} {P(x_0)}
  \have {3} {\exists x\, P(x)} \Ei{2}
  \have {4} {\forall y\, Q(y)} \ie{1,3}
  \have {5} {Q(y_0)} \Ae{4}
  \close
  \have {6} {P(x_0) \to Q(y_0)} \ii{2-5}
  \close
  \have {7} {\forall y\, (P(x_0) \to Q(y))} \Ai{2-6}
  \close
  \have {8} {\forall x\, \forall y\, (P(x) \to Q(y))} \Ai{2-7}
\end{nd}$
\end{center}
```

At line 7, \( y_0 \) is not in the premise or in line 7, and no assumption is open (the box of line 2 has closed). At line 8 the same holds for \( x_0 \). No \( \rulename{RAA} \) is used.

The sequent combines (b) and (a) of @prp-quantifier-passage. Law (b), with \( \varphi \) the formula \( P(x) \) and \( \psi \) the formula \( \forall y\, Q(y) \) (in which \( x \) is not free), turns the premise into \( \forall x\, \bigl( P(x) \to \forall y\, Q(y) \bigr) \). Then law (a), applied under \( \forall x \) (a provable equivalence may be used under a quantifier, the paragraph after the negation procedure) with \( \psi \) the formula \( P(x) \), \( \varphi \) the formula \( Q(y) \) and \( y \) as the moving variable (\( y \) is not free in \( P(x) \)), turns \( P(x) \to \forall y\, Q(y) \) into \( \forall y\, (P(x) \to Q(y)) \).
:::

::: {#exr-quantifier-laws-b3}
[B3: Choosing \( \varepsilon \) from the data]

Let \( a \) and \( b \) be real numbers with \( a < b + \varepsilon^2 \) for every \( \varepsilon > 0 \). Prove that \( a \le b \), by the method of @prp-arbitrarily-close-equal: suppose not, and choose an \( \varepsilon \) built from the data that makes the numbers collide. Then explain why the choice \( \varepsilon = a - b \) does not work.
:::

::: {.solution}
Suppose \( a < b + \varepsilon^2 \) for every \( \varepsilon > 0 \), and suppose, for a contradiction, that \( a > b \) (the negation of \( a \le b \)). Let \( \varepsilon \coloneqq \min(1, a - b) \). Then \( \varepsilon > 0 \), since \( 1 > 0 \) and \( a - b > 0 \). Since \( 0 < \varepsilon \le 1 \), \( \varepsilon^2 = \varepsilon \cdot \varepsilon \le \varepsilon \cdot 1 = \varepsilon \), and \( \varepsilon \le a - b \). The hypothesis applies to this \( \varepsilon \) and gives
\[
a < b + \varepsilon^2 \le b + \varepsilon \le b + (a - b) = a ,
\]
so \( a < a \), a contradiction. Hence \( a \le b \).

The choice \( \varepsilon = a - b \), copied from the text, gives \( a < b + (a - b)^2 \), that is, \( a - b < (a - b)^2 \). When \( a - b > 1 \) this is true (for \( a - b = 2 \): \( 2 < 4 \)), so there is no contradiction. The square shrinks a number only when it is at most \( 1 \), and the \( \min \) with \( 1 \) is what puts \( \varepsilon \) there.
:::

### C. Going deeper

::: {#exr-quantifier-laws-c1}
[C1: Two prenex forms]

A formula is in **prenex form** when all its quantifiers stand at the front, before a part with no quantifier. Using the laws of @prp-quantifier-passage, bring \( \forall x\, P(x) \to \exists y\, Q(y) \) into prenex form in two ways, ending with \( \exists x\, \exists y\, (P(x) \to Q(y)) \) and with \( \exists y\, \exists x\, (P(x) \to Q(y)) \). Justify each step, and say which directions of the laws are classical.
:::

::: {.solution}
[Hint 1]

The formula is an implication with a quantifier on each side. Law (d) moves the quantifier out of the hypothesis, and law (e) moves it out of the conclusion.
:::

::: {.solution}
[Hint 2]

For the first route, start with law (d), taking \( \psi \) to be the whole conclusion \( \exists y\, Q(y) \).
:::

::: {.solution}
*First route: \( x \) out first.* Law (d) of @prp-quantifier-passage, with \( \varphi \) the formula \( P(x) \) and \( \psi \) the formula \( \exists y\, Q(y) \), in which \( x \) is not free:
\[
\forall x\, P(x) \to \exists y\, Q(y) \;\dashv\vdash\; \exists x\, \bigl( P(x) \to \exists y\, Q(y) \bigr).
\]
Then law (e) under \( \exists x \), with \( \psi \) the formula \( P(x) \), \( \varphi \) the formula \( Q(y) \), and \( y \) as the moving variable (\( y \) is not free in \( P(x) \)): \( P(x) \to \exists y\, Q(y) \dashv\vdash \exists y\, (P(x) \to Q(y)) \). A provable equivalence may be used under a quantifier (the paragraph after the negation procedure), so
\[
\exists x\, \bigl( P(x) \to \exists y\, Q(y) \bigr) \;\dashv\vdash\; \exists x\, \exists y\, \bigl( P(x) \to Q(y) \bigr).
\]

*Second route: \( y \) out first.* Law (e), with \( \psi \) the formula \( \forall x\, P(x) \), \( \varphi \) the formula \( Q(y) \), and \( y \) as the moving variable (\( y \) is not free in \( \forall x\, P(x) \)):
\[
\forall x\, P(x) \to \exists y\, Q(y) \;\dashv\vdash\; \exists y\, \bigl( \forall x\, P(x) \to Q(y) \bigr).
\]
Then law (d) under \( \exists y \), with \( \varphi \) the formula \( P(x) \) and \( \psi \) the formula \( Q(y) \) (\( x \) is not free in \( Q(y) \)):
\[
\exists y\, \bigl( \forall x\, P(x) \to Q(y) \bigr) \;\dashv\vdash\; \exists y\, \exists x\, \bigl( P(x) \to Q(y) \bigr).
\]

*Classical steps.* Going from the given formula towards the prenex form, every step of both routes uses the direction \( \dashv \) of (d) or of (e): the direction from the implication to the \( \exists \). These are exactly the two directions that @prp-quantifier-passage derives with \( \rulename{LEM} \). The way back uses only the intuitionistic directions.

**Marking scheme.** (10 points)
- 3: first route, with law (d) then law (e), each with \( \varphi \), \( \psi \) and the moving variable named, and the "not free" condition checked.
- 3: second route, likewise with (e) then (d).
- 2: says why a law may be applied under \( \exists x \) or \( \exists y \) (an equivalence used under a quantifier, by an \( \rulename{\exists E} \) box closed with \( \rulename{\exists I} \)).
- 2: identifies the \( \dashv \) directions of (d) and (e) as the classical ones, used in every step towards prenex form.
Fatal errors (0 for the step): moving \( \forall x \) out of the hypothesis as \( \forall x \) (it becomes \( \exists x \)); applying a passage law when the moving variable is free in \( \psi \).
:::

::: {#exr-quantifier-laws-c2}
[C2: Exit check: negations]

::: {.enumerate options="label=(\alph*)"}
1. A sequence of functions \( f_n \) converges to \( f \) **uniformly** on \( A \) when
\[
\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; \forall x \in A \; \bigl( n \ge N \to \abs{f_n(x) - f(x)} < \varepsilon \bigr),
\]
where \( f_n(x) \) is a term in the two variables \( n \) and \( x \). Negate this into positive form, citing the laws.
2. Using the negation of uniform continuity in @exm-negating-definitions (c), prove that \( f(x) = 1/x \) is not uniformly continuous on \( (0, 1) \). Give the witnesses that the negation asks for, each as a function of what is chosen before it, and check every condition.
:::
:::

::: {.solution}
[Hint 1]

For (b), the negation asks for one \( \varepsilon \) first. Near \( 0 \), the graph of \( 1/x \) is steep: two points close together have values far apart.
:::

::: {.solution}
[Hint 2]

Take \( \varepsilon = 1 \) and let \( \delta > 0 \) be arbitrary. You must now find \( x, y \in (0, 1) \), depending on \( \delta \), with \( \abs{x - y} < \delta \) and \( \abs{1/x - 1/y} \ge 1 \).
:::

::: {.solution}
*(a)* @prp-bounded-quantifier-negation four times, then @prp-negated-implication and the order fact:
\[
\exists \varepsilon > 0 \; \forall N \in \nN \; \exists n \in \nN \; \exists x \in A \; \bigl( n \ge N \wedge \abs{f_n(x) - f(x)} \ge \varepsilon \bigr).
\]
In words: for some \( \varepsilon > 0 \), however far out we start, some later \( f_n \) is at least \( \varepsilon \) away from \( f \) at some point of \( A \). The point may change with \( n \).

*(b)* By @exm-negating-definitions (c), we must prove
\[
\exists \varepsilon > 0 \; \forall \delta > 0 \; \exists x \in (0, 1) \; \exists y \in (0, 1) \; \Bigl( \abs{x - y} < \delta \wedge \Bigl\lvert \frac1x - \frac1y \Bigr\rvert \ge \varepsilon \Bigr).
\]
Take \( \varepsilon = 1 \), which is positive. Let \( \delta > 0 \) be arbitrary, and let \( t \coloneqq \min(\delta, \tfrac12) \), so \( 0 < t \le \tfrac12 \) and \( t \le \delta \); then take \( x \coloneqq t \) and \( y \coloneqq t/2 \), which depend on \( \delta \). Check:

- \( x, y \in (0, 1) \): \( 0 < t/2 < t \le \tfrac12 < 1 \).
- \( \abs{x - y} = t/2 < t \le \delta \), since \( t > 0 \).
- \( \abs{1/x - 1/y} = \abs{1/t - 2/t} = 1/t \ge 2 \ge 1 = \varepsilon \), since \( t \le \tfrac12 \).

Since \( \delta > 0 \) was arbitrary, the negation of uniform continuity holds, so \( 1/x \) is not uniformly continuous on \( (0, 1) \).

**Marking scheme.** (10 points)
- 3: (a) the negation, with every bound kept, \( \wedge \) in place of \( \to \), and the quantifiers in the order \( \exists \varepsilon\; \forall N\; \exists n\; \exists x \in A \).
- 2: (b) the witness \( \varepsilon \), stated before \( \delta \) is given.
- 2: for an arbitrary \( \delta > 0 \), points \( x \) and \( y \) given as functions of \( \delta \).
- 3: the three checks: \( x, y \in (0, 1) \); \( \abs{x - y} < \delta \); \( \abs{f(x) - f(y)} \ge \varepsilon \).
A different correct choice earns full marks (for instance \( x = t \), \( y = t/3 \)); the scheme rewards the order of the choices and the checks.
Fatal errors (0 for the step): \( \varepsilon \) chosen depending on \( \delta \); points chosen before \( \delta \) is given, or not depending on it where they must; a bound negated instead of the quantifier (\( \exists \varepsilon \le 0 \), \( \exists n < N \)).
:::

<!-- dependency ledger
prp-quantifier-negation (proof): (neg phi)[x_0/x] is neg(phi[x_0/x]); x_0 not appearing in phi is free for x in phi | def-substitution, def-free-for (cited / Section 4.2 special case "a variable that does not appear is free for every variable"), argued inline
prp-quantifier-negation (claim): no derivation of (a) avoids RAA | stated without proof, flagged in the text; propositional analogue thm-raa-independent (optional, cited only as an analogue); Chapter 5 (prose pointer); nothing rests on it
prp-quantifier-negation (claim): Chapter 11 uses (a) at the end of the Archimedean proof | ch11 05-archimedean-property remark (drafted; prose pointer only)
prp-quantifier-negation (claim): in "The laws as one line" after it, a law used as one line abbreviates its pasted derivation with a fresh name new to the larger derivation, keeping all side conditions | argued inline, extending prp-bounded-quantifier-rules' looser sense of derived rule
prp-quantifier-negation (solution): the Quick check after it: over Z, not every integer is even, and 0 is even | school arithmetic, informal truth (Section 4.1)
prp-negated-implication (example): x > 2 and x^2 <= 4 | illustrative reading only
prp-negated-implication (claim): in the warning "The negation of an implication is not an implication", x > 2 implies x^2 > 4 over R, so x > 2 and x^2 <= 4 is false for every real x | school algebra (order facts); ch11 (prose pointer, nothing rests on it)
prp-bounded-quantifier-negation (proof): (x > a)[x_0/x] is x_0 > a when x does not occur in a | def-substitution (cited); def-bounded-quantifier's condition on a
prp-bounded-quantifier-negation (claim): in the warning after it, |a_n - L| >= 0 for every n | school fact (absolute value non-negative); ch11 prp-absolute-value-rules (prose pointer)
prp-quantifier-distribution (proof): prp-forall-and, prp-exists-and and the exists-or derivation of exm-existential-elimination-derivations work with formulas phi, psi in place of P(x), Q(x) | inline argument (they use only the instances at a fresh name not appearing in phi, psi)
prp-quantifier-distribution (claim): over Z every integer is even or odd, not both; the converses are not derivable | school arithmetic, informal truth (Section 4.1); non-derivability is Section 4.11 (prose pointer; nothing here rests on it)
prp-quantifier-passage (proof): psi[t/x] = psi when x is not free in psi | the claim after exm-computing-substitutions in Section 4.2 (unlabelled; cited as "Section 4.2")
prp-quantifier-passage (proof): exists-I at the variable x itself, (phi -> psi)[x/x] = phi -> psi; sound because domains are non-empty | phi[x/x] = phi (Section 4.2, stated after exm-computing-substitutions); non-emptiness explained in Section 4.11 (prose pointer, nothing rests on it)
prp-quantifier-passage (claim): exactly two directions use LEM/RAA here | inspection of the printed derivations (meta-claim, checkable on the page); "cannot be avoided" is not claimed
prp-quantifier-passage (claim): in "Why the condition on psi", over Z with P = even and x read as 1, "if some integer is even then 1 is even" is false | school arithmetic, informal truth (Section 4.1); checked by verify/ch04/prp-quantifier-passage.py
exm-negating-definitions (claim): in the paragraph before it ("Why may a step act on a part"), provable equivalence is preserved under every connective and quantifier, including for a passage law whose condition must survive the instance at x_0 | argued inline (pasting derivations into the rules' boxes; laws hold for every formula meeting their condition, so for instances at x_0; x_0 is a variable other than x, as the closing forall-I needs (ch04 04-universal-introduction side condition); x_0 is not the moving variable y, so the substitution passes the quantifier on y and y stays not free in psi[x_0/x], by def-substitution; if y (or the bound variable z) is x itself, def-substitution stops at that quantifier and psi[x_0/x] = psi since x is not free in psi (Section 4.2 claim after exm-computing-substitutions), so the pair is unchanged)
exm-negating-definitions (solution): not(u < v) iff u >= v and not(u <= v) iff u > v over R | order facts (school algebra), stated as such in the procedure
exm-negating-definitions (claim): not(alpha and beta) -||- alpha -> not beta | prp-de-morgan (c), (d) and prp-implication-as-disjunction (a), (b) (cited)
prp-quantifier-passage (solution): the Quick check after it uses law (e) under forall x | prp-quantifier-passage (e), and the replacement paragraph (inline)
prp-arbitrarily-close-equal (proof): a != b gives a - b != 0 (if a - b = 0 then a = (a - b) + b = b); |u| > 0 for real u != 0; no real is less than itself | school algebra; ch11 prp-absolute-value-rules (prose pointer, "Chapter 11 proves them")
prp-arbitrarily-close-equal (claim): a = 0, b = 1/2, eps = 1 shows "some eps" is not enough | arithmetic; checked by verify/ch04/prp-arbitrarily-close-equal.py
exr-quantifier-laws-a1 (solution): (d) x * x = 2 has a real solution; (e) over R, forall eps > 0 (eps > 0) is true and eps = 0 witnesses exists eps <= 0 not(eps > 0) | informal truth (Section 4.1); school facts; checked by verify/ch04/exr-quantifier-laws-a1.py
exr-quantifier-laws-b1 (solution): order facts not(|a_n| <= M) iff |a_n| > M etc. | school algebra
exr-quantifier-laws-b3 (solution): eps = min(1, a - b) > 0, eps^2 <= eps <= a - b; a - b < (a - b)^2 when a - b > 1 | school algebra; checked by verify/ch04/exr-quantifier-laws-b3.py
exr-quantifier-laws-c1 (solution): passage laws used under exists | prp-quantifier-passage (cited) and the replacement paragraph after the negation procedure (inline)
exr-quantifier-laws-c2 (solution): t = min(delta, 1/2); 0 < t/2 < t <= 1/2 < 1; |1/t - 2/t| = 1/t >= 2 | school algebra; checked by verify/ch04/exr-quantifier-laws-c2.py
-->
