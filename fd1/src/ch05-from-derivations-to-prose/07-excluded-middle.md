# The Dispute over Excluded Middle

Chapter 2 found that one rule stands apart. \( \rulename{RAA} \) belongs to no connective, and over the other primitive rules it derives \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \) and is derived by each of them (@thm-classical-rules-interderivable). Chapter 3's optional @thm-raa-independent showed that the other propositional rules cannot derive it. Some mathematicians have refused to use it, for a century now and for reasons that are mathematical rather than merely fussy. This section asks what those reasons are, what can still be proved without the rule, and what analysis would lose.

## One extra rule {#one-extra-rule}

Recall what Section 2.5 established. Over the primitive rules other than \( \rulename{RAA} \), the three rules \( \rulename{RAA} \), \( \rulename{\neg\neg E} \), and \( \rulename{LEM} \) each derive the other two, so adding any one of them gives the same derivable sequents. There is one classical principle, and it has three faces. Nothing needs re-proving here; what is new is the decision to leave the principle out and see what remains.

Call a derivation **intuitionistic** if no line is justified by \( \rulename{RAA} \) and no line uses a derived rule or a cited result whose own derivation uses \( \rulename{RAA} \). **Intuitionistic logic** is the system of these derivations. Its rules are the introduction and elimination rules for \( \wedge \), \( \to \), and \( \vee \) (Chapter 1); \( \rulename{\neg I} \), \( \rulename{\neg E} \), \( \rulename{\bot E} \), \( \rulename{{\leftrightarrow}I} \), and \( \rulename{{\leftrightarrow}E} \) (Chapter 2); the rules for \( \forall \), \( \exists \), and \( = \) (Chapter 4); and repetition. **Classical logic**, the logic of Chapters 1–4, is the same list with \( \rulename{RAA} \) added.

This is why Chapter 2 kept \( \rulename{\bot E} \) as a primitive rule although \( \rulename{RAA} \) and repetition derive it (the remark after @thm-classical-rules-interderivable). Had \( \rulename{\bot E} \) been dropped, striking \( \rulename{RAA} \) would have taken it away too, and the remaining system would be weaker than the one intuitionists actually use: it could no longer derive \( \bot \vdash P \). That is a claim about all derivations, and we state it without proof; nothing depends on it. With \( \rulename{\bot E} \) kept, the rules without \( \rulename{RAA} \) are exactly intuitionistic logic.

| System | Rules | \( \vdash P \vee \neg P \)? |
|---|---|---|
| intuitionistic | the primitive rules other than \( \rulename{RAA} \) | not derivable (@thm-raa-independent for the propositional rules; the rules for \( \forall \), \( \exists \) and \( = \) do not change this, stated without proof) |
| classical | the same rules and \( \rulename{RAA} \) | derivable (@prp-excluded-middle) |

Every intuitionistic derivation is a derivation, so everything intuitionistic logic derives, classical logic derives too, and soundness applies to it: @thm-soundness, and, for derivations whose lines contain quantifiers or equations, the soundness statement for predicate logic in Section 4.11. The difference is a list of sequents that only the classical system reaches. Chapters 2–4 flag the derivations that use \( \rulename{RAA} \) as they go, so the results on that list can be read off the text; the Quick check asks for them.

::: {.check}
(a) Which labeled results of Chapter 2 (propositions and theorems) were derived with \( \rulename{RAA} \), directly or through \( \rulename{\neg\neg E} \), \( \rulename{LEM} \), or a cited result that uses one of them? (b) The same question for Chapters 3 and 4.
:::

::: {.solution}
(a) Seven: @prp-double-negation (b); @prp-contrapositive-converse; @prp-excluded-middle; @prp-de-morgan (d); @prp-implication-as-disjunction (b), through \( \rulename{LEM} \); @thm-classical-rules-interderivable, whose proof uses all three: \( \rulename{RAA} \) in ①, \( \rulename{\neg\neg E} \) in ②, \( \rulename{LEM} \) in ③; and @prp-peirce. Every other proposition and theorem of Chapter 2 uses no classical rule, including @thm-sqrt2-irrational, whose box closes by \( \rulename{\neg I} \).

(b) In Chapter 3: @lem-atom-splitting, through \( \rulename{LEM} \), and with it @thm-completeness and the direction \( (\Leftarrow) \) of @cor-derivable-iff-valid. In Chapter 4: @prp-quantifier-negation (a); the direction \( \vdash \) of @prp-negated-implication; the direction \( \vdash \) of @prp-bounded-quantifier-negation (a); the two directions \( \dashv \) of @prp-quantifier-passage, in (d) and in (e), both through \( \rulename{LEM} \); and @prp-arbitrarily-close-equal, as proved, since its box assumes \( a \ne b \) and concludes \( a = b \).
:::

## Excluded middle cannot be refuted

If intuitionists do not assert \( P \vee \neg P \), perhaps they deny it. They do not, and they could not: its double negation needs no classical rule at all.

::: {#prp-not-not-excluded-middle .optional}
[Excluded Middle Cannot Be Refuted]

For every statement \( P \), \( \vdash \neg\neg(P \vee \neg P) \), by a derivation that uses neither \( \rulename{RAA} \) nor \( \rulename{\bot E} \).
:::

*Try it first (ten minutes): the goal is a negation. Open the box that the goal asks for, hunt for a clash, and note which rule closes each box you open.*

::: {.idea}
An attempt that starts from \( P \vee \neg P \) stalls at once: \( \rulename{\vee I} \) needs one side, and neither side is in hand. But the goal is not \( P \vee \neg P \). It is \( \neg(\neg(P \vee \neg P)) \), a negation, so the goal-directed move of Section 2.2 opens a \( \rulename{\neg I} \) box on \( \neg(P \vee \neg P) \) with the goal \( \bot \). That assumption can clash only with \( P \vee \neg P \), which \( \rulename{\vee I} \) builds from either side, so we manufacture a side as in @exm-manufactured-clash. A box on \( P \) gives \( P \vee \neg P \), a clash, and \( \rulename{\neg I} \) closes it with \( \neg P \). Then \( \rulename{\vee I} \) builds \( P \vee \neg P \) from \( \neg P \), and that is the second clash. Every box ends in \( \bot \) and closes by \( \rulename{\neg I} \).

*Before reading on: self-explain lines 5 and 6.*
:::

::: {.proof}
The derivation is:

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\neg (P \vee \neg P)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee \neg P} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
  \have {6} {P \vee \neg P} \oi{5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {\neg\neg (P \vee \neg P)} \ni{1-7}
\end{nd}$
\end{center}
```

The two boxes close by \( \rulename{\neg I} \), at lines 5 and 8. The other rules used are \( \rulename{\vee I} \) (lines 3 and 6) and \( \rulename{\neg E} \) (lines 4 and 7). The derivation has no premises. This proves the proposition.
:::

Set it beside the derivation of @prp-excluded-middle. Lines 1–7 are the same, line for line. Only line 8 differs: there \( \rulename{RAA} \) closed the outer box and wrote \( P \vee \neg P \); here \( \rulename{\neg I} \) closes it and writes the negation of its assumption. So the whole classical content of @prp-excluded-middle sits in its last line.

**Non-example by minimal change.** Keep lines 1–7, and write \( P \vee \neg P \) at line 8 with the justification \( \rulename{\neg I}\ \lines{1}{7} \). The box still checks. What fails is the conclusion of \( \rulename{\neg I} \), which must be the negation of the box's assumption, \( \neg\neg(P \vee \neg P) \). Writing \( P \vee \neg P \) there needs \( \rulename{RAA} \).

What the proposition says is this: **nobody can refute excluded middle**. Suppose some derivation, intuitionistic or not, gave \( \neg(P \vee \neg P) \) from no premises. Then \( \rulename{\neg E} \) against the line \( \neg\neg(P \vee \neg P) \) would give \( \bot \) from no premises, and soundness forbids that: @thm-soundness, or the soundness statement for predicate logic in Section 4.11 when \( P \) or the derivation involves quantifiers or equality, since no valuation, and no structure and assignment, makes \( \bot \) true. The intuitionist does not claim that excluded middle fails. The intuitionist declines to **assert** it, because asserting it would mean having a proof of one side, and for many statements \( P \), an open conjecture for instance, nobody has one.

::: {.remark}
The proposition is one instance of a general fact, due to Glivenko (1929) and stated here without proof: if a statement built from letters by the connectives is derivable with all the rules, then its double negation is derivable without \( \rulename{RAA} \). Classical propositional logic survives inside intuitionistic logic, behind two negations. The fact fails once quantifiers are allowed; \( \neg\neg\forall x\, (\varphi \vee \neg\varphi) \) is in general not derivable without \( \rulename{RAA} \) (also stated without proof).
:::

::: {.warning}
Intuitionistic logic does not say that excluded middle is false. No instance \( P \vee \neg P \) can be refuted, since \( \neg\neg(P \vee \neg P) \) is derivable without \( \rulename{RAA} \); dropping a rule is not adding its negation. (Brouwer's own analysis adds axioms about the real numbers under which the **universal** statement "every real number is \( 0 \) or not \( 0 \)" is refuted, but no single instance is.)
:::

## What a proof provides {#what-a-proof-provides}

Chapter 3 gave the connectives a meaning through truth values: every letter is true or false, and a table computes the rest. That semantics already takes a side, since a row decides every letter. The intuitionist explains a statement instead by saying what counts as a **proof** of it. The resulting clauses are called the **BHK reading**, after Brouwer, Heyting, and Kolmogorov.

*To know a statement is to have a proof of it, and a proof of a compound statement is built from proofs of its parts.*

- There is **no** proof of \( \bot \).
- A proof of \( P \wedge Q \) is a pair: a proof of \( P \) and a proof of \( Q \).
- A proof of \( P \vee Q \) is a proof of \( P \) or a proof of \( Q \), **with a label saying which**.
- A proof of \( P \to Q \) is a method that takes **any** proof of \( P \) and returns a proof of \( Q \).
- A proof of \( \neg P \) is a method that takes any proof of \( P \) and returns a proof of \( \bot \). So \( \neg P \) is read as \( P \to \bot \), exactly the reading that the table in Section 2.2, after @def-rules-negation, found row by row.
- A proof of \( \exists x\, \varphi \) is an object \( t \) **together with** a proof of \( \varphi[t/x] \).
- A proof of \( \forall x\, \varphi \) is a method that produces, for **every** object \( t \), a proof of \( \varphi[t/x] \).

In words: a disjunction must say which side, an existence claim must name the object, and an implication or a universal statement must come with a method that works on every input. A proof of a negation provides no object at all; it is a guarantee that no proof of the negated statement will ever arrive.

Each intuitionistic rule builds exactly what its clause asks for. \( \rulename{\vee I} \) writes \( P \vee Q \) from a line \( P \), so it knows which side it used. \( \rulename{\exists I} \) writes \( \exists x\, \varphi \) from an instance \( \varphi[t/x] \), so the witness \( t \) is on the page. A \( \rulename{{\to}I} \) box is a method: given the assumption, it produces the conclusion. \( \rulename{RAA} \) is the exception. Its box shows that \( \neg\varphi \) leads to \( \bot \), which is a proof of \( \neg\neg\varphi \), and then it writes \( \varphi \). Under the BHK reading a method for refuting every refutation of \( \varphi \) is not a proof of \( \varphi \).

**Excluded middle under BHK.** A proof of \( P \vee \neg P \) for **every** statement \( P \) would be a single method that decides each statement, says which side holds, and proves that side. Nobody has such a method. Take Goldbach's conjecture, that every even integer greater than \( 2 \) is a sum of two primes: nobody has proved it and nobody has refuted it, so nobody can produce a labeled proof of "Goldbach's conjecture or its negation".

**The proposition under BHK.** The derivation of @prp-not-not-excluded-middle is such a method, and it decides nothing. Its conclusion asks for a method that takes any \( f \), a method sending proofs of \( P \vee \neg P \) to proofs of \( \bot \), and returns a proof of \( \bot \). Here is one. Given a proof \( p \) of \( P \), label it "left" and apply \( f \): that turns proofs of \( P \) into proofs of \( \bot \), which is a proof \( g \) of \( \neg P \) (lines 2–5). Now label \( g \) "right" and apply \( f \) once more (lines 6–7). At no point did the method need to know whether \( P \) holds.

**Not every, and some not.** Chapter 4 derived \( \neg\forall x\, \varphi \vdash \exists x\, \neg\varphi \) (@prp-quantifier-negation (a)) with two \( \rulename{RAA} \) boxes, and noted that the derivation never says which \( x \) fails \( \varphi \). The BHK reading says why that matters. A proof of the premise is a method that refutes every proof of \( \forall x\, \varphi \); a proof of the conclusion must name an object. Nothing in the first produces the second, and the derivation does not try: its conclusion comes from \( \rulename{RAA} \), not from an \( \rulename{\exists I} \) applied to an available instance. Classical mathematics accepts the step, and Chapter 11 uses it at the end of its proof of the Archimedean property. A constructive mathematician accepts that conclusion only with an object in hand.

::: {.check}
Describe a BHK proof of \( \neg(P \wedge \neg P) \). Does it decide whether \( P \) holds?
:::

::: {.solution}
We need a method that takes any proof of \( P \wedge \neg P \) and returns a proof of \( \bot \). A proof of \( P \wedge \neg P \) is a pair: a proof \( p \) of \( P \) and a method \( f \) turning proofs of \( P \) into proofs of \( \bot \). Apply \( f \) to \( p \). That is the whole method, and it never decides \( P \): it only uses a pair that someone else supplies. (It is the BHK reading of a \( \rulename{\neg I} \) box on \( P \wedge \neg P \) whose clash is \( \rulename{\neg E} \) on its two halves.)
:::

## Irrational powers, with and without a witness

Here is the standard example of a proof that establishes existence without saying what exists.

::: {#thm-irrational-power-rational .optional}
[An Irrational Power of an Irrational Number Can Be Rational]

There are irrational numbers \( a \) and \( b \) such that \( a^b \) is rational.
:::

*Try it first (ten minutes): find such \( a \) and \( b \) explicitly, and prove that your \( a \) and \( b \) are irrational and that \( a^b \) is rational.*

::: {.idea}
The first candidates anyone tries are \( a = b = \sqrt 2 \). Then the question is whether \( \sqrt 2^{\sqrt 2} \) is rational, and the attempt stalls there: nothing in this book decides it. There are two ways out. The classical one splits on the undecided question with \( \rulename{LEM} \). If \( \sqrt 2^{\sqrt 2} \) is rational, the first candidates work. If not, use it as the new \( a \) and raise it to \( \sqrt 2 \) once more, which turns the exponent into \( \sqrt 2 \cdot \sqrt 2 = 2 \). The proof below takes this way. The other way chooses an exponent that undoes the square root, and the proposition after the proof takes it.
:::

::: {.proof}
Let \( s \coloneqq \sqrt 2^{\sqrt 2} \), a positive real number. By excluded middle, \( s \) is rational or \( s \) is not rational [\( \rulename{LEM} \)], and we argue by cases [\( \rulename{\vee E} \)].

*Case 1: \( s \) is rational.* Take \( a \coloneqq \sqrt 2 \) and \( b \coloneqq \sqrt 2 \). Both are irrational by @thm-sqrt2-irrational, and \( a^b = s \) is rational [\( \rulename{\exists I} \)].

*Case 2: \( s \) is not rational.* Take \( a \coloneqq s \) and \( b \coloneqq \sqrt 2 \). Then \( a \) is irrational by the case assumption and \( b \) by @thm-sqrt2-irrational, and
\[
a^b = \bigl( \sqrt 2^{\sqrt 2} \bigr)^{\sqrt 2} = \sqrt 2^{\sqrt 2 \cdot \sqrt 2} = \sqrt 2^{\,2} = 2,
\]
which is rational [\( \rulename{\exists I} \)].

In either case there are irrational \( a \) and \( b \) with \( a^b \) rational. This proves the theorem.
:::

The classical step is the first line, \( \rulename{LEM} \) on the statement "\( s \) is rational". Every other step is intuitionistic. The proof does **not** tell us which pair works. It hands over two candidate pairs, \( (\sqrt 2, \sqrt 2) \) and \( (\sqrt 2^{\sqrt 2}, \sqrt 2) \), and a guarantee that one of them succeeds. Under the BHK reading a proof of an existence claim must name the object, so this proof is not one. Section 2.5 described excluded middle as making a decision; here the decision about "\( s \) is rational" is made, and nobody learns its outcome.

::: {.remark}
In fact the second case holds: \( \sqrt 2^{\sqrt 2} \) is transcendental, so in particular irrational, by the Gelfond–Schneider theorem, proved independently by Gelfond and by Schneider in 1934. That theorem lies far beyond this book, and nothing here uses it. It also does not repair the proof above, which never needed to know the answer.
:::

The other way out finds the witness. Since \( \sqrt 2^{\,b} = 2^{b/2} \), the exponent \( b = 2\log_2 m = \log_2(m^2) \) gives \( \sqrt 2^{\,b} = m \) for every integer \( m \ge 2 \). The choice \( m = 2 \) gives \( b = 2 \), which is rational, so \( m \) must avoid the powers of \( 2 \); the first choice left is \( m = 3 \).

::: {#prp-log2-9-irrational .optional}
[A Witness for an Irrational Power]

The number \( \log_2 9 \) is irrational. Consequently \( a \coloneqq \sqrt 2 \) and \( b \coloneqq \log_2 9 \) are irrational numbers with \( a^b = 3 \).
:::

::: {.idea}
The irrationality goes as for \( \sqrt 2 \): suppose \( \log_2 9 \) is a fraction \( p/q \), clear the denominator, and look at parity. Here the clash is quicker than for \( \sqrt 2 \): a power of \( 2 \) would equal a power of \( 9 \), and one is even while the other is odd. The positivity of \( \log_2 9 \) is what makes the power of \( 2 \) even.
:::

::: {.proof}
Suppose that \( \log_2 9 = p/q \) for integers \( p \) and \( q \) with \( q \ne 0 \); replacing \( p \), \( q \) by \( -p \), \( -q \) if necessary, we may take \( q \ge 1 \). Since \( 2^0 = 1 < 9 \) and \( t \mapsto 2^t \) is increasing, \( \log_2 9 > 0 \), so \( p > 0 \), that is, \( p \ge 1 \). From \( 2^{p/q} = 9 \), raising both sides to the power \( q \) gives
\[
2^p = 9^q .
\]
The left side is even, since \( 2^p = 2 \cdot 2^{p-1} \) with \( p - 1 \ge 0 \). The right side is odd, being a product of \( q \) odd factors. No integer is both even and odd, by (E2) of Section 2.1, so this is a contradiction. Hence \( \log_2 9 \) is not rational [\( \rulename{\neg I} \)].

For the consequence, \( a = \sqrt 2 \) is irrational by @thm-sqrt2-irrational, and \( b = \log_2 9 \) is irrational by what was just shown. Since \( \log_2 9 = \log_2 (3^2) = 2\log_2 3 \),
\[
a^b = \bigl( 2^{1/2} \bigr)^{\log_2 9} = 2^{(\log_2 9)/2} = 2^{\log_2 3} = 3 .
\]
This proves the proposition.
:::

This proof uses no classical rule. The irrationality of \( \log_2 9 \) is a negative statement, "no fraction equals \( \log_2 9 \)", and its box closes by \( \rulename{\neg I} \), like the proof of @thm-sqrt2-irrational. The witness \( (\sqrt 2, \log_2 9) \) is written down. So @prp-log2-9-irrational gives a second proof of @thm-irrational-power-rational, and this one provides what the BHK reading asks for. (The exponent laws for real exponents are school facts here; Chapter 20 defines \( a^x \) for irrational \( x \) and proves them.)

## A short history

The dispute has dates.

In 1908 L. E. J. Brouwer published "De onbetrouwbaarheid der logische principes" ("The unreliability of the logical principles") in the *Tijdschrift voor Wijsbegeerte*. His point was that excluded middle had been abstracted from reasoning about finite collections, where every case can in principle be checked, and then applied without justification to infinite ones, where it cannot. Over the next two decades he rebuilt parts of analysis on this view, and the movement took the name **intuitionism**.

In 1925 A. N. Kolmogorov showed that classical reasoning can be imitated inside a logic without excluded middle by putting a double negation in front of every subformula: the first **double-negation translation** (Exercise C2 below checks one step of it).

In July 1927 David Hilbert lectured in Hamburg on "Die Grundlagen der Mathematik", printed in 1928. He defended excluded middle in a much-repeated comparison: to take it from the mathematician would be like forbidding the astronomer the telescope or the boxer the use of his fists. The quarrel between his program and Brouwer's became known as the **Grundlagenstreit**, the dispute over foundations. It turned personal in 1928, when Hilbert had Brouwer removed from the editorial board of the *Mathematische Annalen*; the board was then dissolved and re-formed without him.

In 1929 V. Glivenko proved the theorem of the remark above: classical propositional logic sits inside intuitionistic logic behind a double negation. In 1930 Arend Heyting published "Die formalen Regeln der intuitionistischen Logik" in the *Sitzungsberichte der Preußischen Akademie der Wissenschaften*. It wrote down rules for intuitionistic logic, in a format different from ours, and from then on the logic could be studied as a formal system like any other.

In 1933 Kurt Gödel published a double-negation translation of arithmetic, which shows that classical arithmetic is consistent if intuitionistic arithmetic is. Gerhard Gentzen had found an equivalent translation independently and withdrew his paper of 1933 when Gödel's appeared.

In 1967 Errett Bishop published *Foundations of Constructive Analysis*. It developed a large part of analysis without excluded middle, and also without Brouwer's philosophy and his special axioms about the real numbers. Most of what is now called constructive analysis descends from it.

## What analysis would lose

What does analysis look like without the rule? Here are four previews, stated informally and without proof. The book takes the first as an axiom and proves the classical versions of the other three; each is a place where classical reasoning, by the rule or by an axiom, does work that a constructive proof cannot.

- **The supremum.** Chapter 11 takes as an axiom that every non-empty set of real numbers that is bounded above has a supremum. Constructively, a non-empty set \( A \) bounded above has a supremum **if and only if** it is **order-located**: for all real numbers \( x < y \), either \( y \) is an upper bound of \( A \) or some element of \( A \) exceeds \( x \) (Bishop's form of the least upper bound principle). The classical axiom asserts the supremum without requiring anyone to make these decisions.
- **Monotone sequences.** E. Specker (1949) gave an increasing, bounded sequence of rational numbers that a computer program can list term by term, but whose limit is not a computable real number: no program can print its decimal digits. So the convergence of bounded monotone sequences, which Chapter 12 proves from the axiom, cannot come with a method for computing the limit.
- **The intermediate value theorem.** Let \( f \) be continuous on \( [a, b] \) with \( f(a) < 0 < f(b) \). Classically, Chapter 16 proves that \( f(x) = 0 \) for some \( x \in [a, b] \). Constructively, what holds in general is the **approximate** version: for every \( \varepsilon > 0 \) some \( x \in [a, b] \) has \( \abs{f(x)} < \varepsilon \). The exact version holds under extra hypotheses, for example when \( f \) is strictly increasing. A bisection needs the sign of \( f \) at a midpoint \( m \), and finitely many digits of \( f(m) \) cannot always tell whether \( f(m) \) is negative, zero, or positive: the digits of a value equal to \( 0 \) begin like those of a tiny positive or negative one.
- **Bolzano–Weierstrass.** A bisection proof of the theorem (Chapter 12 proves it by another route) says: one of the two halves of an interval contains infinitely many terms of the sequence; continue with that half. That step is \( \rulename{LEM} \) on "the left half contains infinitely many terms", a statement that nobody can decide in general, and the proof does not say which half.

## Proofs as programs

The BHK clauses read like the description of a programming language. A proof of \( P \wedge Q \) is a pair; a proof of \( P \vee Q \) is a value tagged "left" or "right"; a proof of \( P \to Q \) is a function; a proof of \( \exists x\, \varphi \) is a pair of an object and a proof; a proof of \( \forall x\, \varphi \) is a function that accepts any object. This match between propositions and types, and between proofs and programs, is the **Curry–Howard correspondence**. It is what a proof assistant such as Lean is built on: checking a proof is checking that a program has the right type.

Intuitionistic logic fits this picture exactly. \( \rulename{LEM} \) does not, since no program decides every proposition. Lean adds classical logic by an axiom, `Classical.choice`, a form of the axiom of choice. Excluded middle, `Classical.em`, is then a **theorem**, derived from choice together with two extensionality principles by Diaconescu's theorem. Lean draws one line with care. A definition that uses classical logic to produce **data**, for instance a number chosen by deciding an arbitrary proposition, must be marked `noncomputable`, since no program computes it. A proof that uses `Classical.em` needs no mark, because proofs carry no data.

```lean
-- excluded middle is a theorem, proved from the axiom of choice
example (p : Prop) : Or p (Not p) := Classical.em p

-- a number defined by deciding an arbitrary proposition
open Classical in
noncomputable def indicator (p : Prop) : Nat := if p then 1 else 0
```

::: {.warning}
"Constructive" does not mean "computable in practice". A constructive proof provides a method, and the method may be hopeless. Deciding whether a whole number is prime by trying every smaller divisor is constructive, and for a number with a thousand digits no computer could finish it. Constructive mathematics asks whether a method exists, not whether it is fast.
:::

## The book's position

The main line of this book stays classical. The decision is made once, in the axioms. The ordered-field axioms of Chapter 11 include trichotomy: for real numbers \( a \) and \( b \), exactly one of \( a < b \), \( a = b \), \( b < a \) holds. Constructive analysis does not accept trichotomy for real numbers, because it would decide the sign of every real number. So a case split such as "\( x \ge 0 \) or \( x < 0 \)" rests on an axiom, and the book does not flag it.

What the book does flag is a genuinely non-constructive step of the kind discussed above, such as the bisection step of Bolzano–Weierstrass, and every use of the axiom of choice. One clause says so, and nothing more. Such a step is never silent anyway: by @def-silent-steps, a \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \) step is written out as an explicit case split or an explicit removal of a double negation. A reader who wants to know where the classical rule enters a proof can always find the place.

## Exercises

### A. Check your understanding

::: {#exr-excluded-middle-a1}
[A1]

Parts (a)–(d) are about @prp-not-not-excluded-middle and its derivation; part (e) is about the proof of @thm-irrational-power-rational.

::: {.enumerate options="label=(\alph*)"}
1. Which rule closes each of the two boxes, and at which line?
2. The outer box opens with a negation and ends in \( \bot \), the shape of an \( \rulename{RAA} \) box. Why is no \( \rulename{RAA} \) used?
3. Give the BHK reading of the conclusion \( \neg\neg(P \vee \neg P) \).
4. True or false, with a reason: for some statement \( P \), intuitionistic logic derives \( \neg(P \vee \neg P) \) from no premises.
5. Which line of that proof uses \( \rulename{LEM} \), and on which statement? Does the proof say which pair \( (a, b) \) works?
:::
:::

::: {.solution}
(a) The inner box, lines 2–4, opens with \( P \) and closes by \( \rulename{\neg I} \) at line 5, giving \( \neg P \). The outer box, lines 1–7, opens with \( \neg(P \vee \neg P) \) and closes by \( \rulename{\neg I} \) at line 8.

(b) The rule that closes a box is decided by what is written after it, not by the box. Line 8 writes \( \neg\neg(P \vee \neg P) \), the negation of the box's assumption \( \neg(P \vee \neg P) \), and that is what \( \rulename{\neg I} \) writes. \( \rulename{RAA} \) would be needed only to write \( P \vee \neg P \) after the same box.

(c) A method that takes any method \( f \), sending proofs of \( P \vee \neg P \) to proofs of \( \bot \), and returns a proof of \( \bot \). The derivation provides one: label a proof of \( P \) "left" and apply \( f \), which gives a proof of \( \neg P \); label that proof "right" and apply \( f \) again.

(d) False. Such a derivation would also be a derivation with all the rules. Together with the derivation of \( P \vee \neg P \) from no premises (@prp-excluded-middle), \( \rulename{\neg E} \) would derive \( \bot \) from no premises. No derivation does that: by @thm-soundness, or by the soundness statement for predicate logic in Section 4.11 when \( P \) or the derivation involves quantifiers or equality, \( \bot \) would be true under every valuation (in every structure under every assignment), and no valuation, and no structure and assignment, makes \( \bot \) true.

(e) The first line, which splits on "\( \sqrt 2^{\sqrt 2} \) is rational" by \( \rulename{LEM} \). The proof does not say which pair works: it shows that \( (\sqrt 2, \sqrt 2) \) works in the first case and \( (\sqrt 2^{\sqrt 2}, \sqrt 2) \) in the second, and does not decide which case holds.
:::

### B. Practice

::: {#exr-excluded-middle-b1}
[B1: Double negation of double negation elimination]

Derive \( \vdash \neg\neg(\neg\neg P \to P) \) without \( \rulename{RAA} \), and name the rule on every line.

*Hint: the goal is a negation; compare the derivation of the proposition in this section.*
:::

::: {.solution}
The goal is a negation, so we open a \( \rulename{\neg I} \) box on \( \neg(\neg\neg P \to P) \), with the goal \( \bot \). The assumption clashes only with \( \neg\neg P \to P \), an implication, which \( \rulename{{\to}I} \) builds from a box on \( \neg\neg P \) that ends in \( P \). The first way to have \( P \) is to assume it: inside a box on \( P \), the implication holds by \( \rulename{{\to}I} \) with \( P \) repeated, and it clashes with the assumption, so \( \neg P \) follows by \( \rulename{\neg I} \). Now \( \neg P \) clashes with any \( \neg\neg P \), so a second box on \( \neg\neg P \) reaches \( \bot \), \( \rulename{\bot E} \) writes \( P \), and the implication is built a second time.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\neg (\neg\neg P \to P)}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg\neg P}
  \have {4} {P} \r{2}
  \close
  \have {5} {\neg\neg P \to P} \ii{3-4}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg P} \ni{2-6}
  \open
  \hypo {8} {\neg\neg P}
  \have {9} {\bot} \ne{7,8}
  \have {10} {P} \be{9}
  \close
  \have {11} {\neg\neg P \to P} \ii{8-10}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {\neg\neg (\neg\neg P \to P)} \ni{1-12}
\end{nd}$
\end{center}
```

Lines 1, 2, 3, and 8 are assumptions. Line 4 repeats line 2 into the box of line 3, since \( \rulename{{\to}I} \) needs \( P \) as a line of that box itself. Line 9 is \( \rulename{\neg E} \) on \( \neg P \) (line 7) and its negation \( \neg\neg P \) (line 8). Every box closes by \( \rulename{{\to}I} \) or \( \rulename{\neg I} \), so no \( \rulename{RAA} \) is used. Unlike the derivation of the proposition in this section, this one uses \( \rulename{\bot E} \), at line 10. The sequent \( \vdash \neg\neg P \to P \) itself has no derivation without \( \rulename{RAA} \) (we state this without proof); its double negation has one.
:::

::: {#exr-excluded-middle-b2}
[B2: Reading proofs as methods]

::: {.enumerate options="label=(\alph*)"}
1. Give the BHK reading of a proof of \( P \to \neg\neg P \), and describe such a proof.
2. The same for \( (P \to Q) \to (\neg Q \to \neg P) \).
3. The same for \( \forall n \in \nN \; \exists m \in \nN \; (m > n) \), over the natural numbers.
4. A proof of an existence claim \( \exists x\, \varphi \) opens with "suppose that no \( x \) satisfies \( \varphi \)" and reaches a contradiction. Without a classical rule, which of \( \neg\neg\exists x\, \varphi \) and \( \exists x\, \varphi \) does it prove? What does it provide under the BHK reading?
:::
:::

::: {.solution}
(a) A method that takes any proof \( p \) of \( P \) and returns a proof of \( \neg\neg P \), that is, a method that takes any proof \( f \) of \( \neg P \) and returns a proof of \( \bot \). The method: given \( p \), and then given \( f \), apply \( f \) to \( p \). This is the BHK reading of @prp-double-negation (a).

(b) A method that takes any method \( h \) (from proofs of \( P \) to proofs of \( Q \)) and returns a proof of \( \neg Q \to \neg P \): a method that takes any \( g \) (from proofs of \( Q \) to proofs of \( \bot \)) and returns a proof of \( \neg P \), that is, a method from proofs of \( P \) to proofs of \( \bot \). The method: given \( h \), \( g \), and a proof \( p \) of \( P \), compute \( g(h(p)) \). This is the BHK reading of @prp-contrapositive, whose derivation uses no \( \rulename{RAA} \).

(c) Unfolding the bounded quantifiers (@def-bounded-quantifier): a method that takes any object \( n \) and a proof that \( n \in \nN \), and returns an object \( m \) together with a proof of \( m \in \nN \wedge m > n \). The method: given \( n \) and the proof of \( n \in \nN \), output \( m = n + 1 \), with the proofs that \( n + 1 \in \nN \) and \( n + 1 > n \).

(d) The box opens with \( \neg\exists x\, \varphi \) and ends in \( \bot \), so \( \rulename{\neg I} \) closes it with \( \neg\neg\exists x\, \varphi \). Writing \( \exists x\, \varphi \) instead is \( \rulename{RAA} \) (or \( \rulename{\neg\neg E} \) after \( \rulename{\neg I} \)), a classical step. Under the BHK reading the proof provides a method that takes any proof that nothing satisfies \( \varphi \) and returns a proof of \( \bot \). It provides no object: a proof of \( \exists x\, \varphi \) would have to name one.
:::

::: {#exr-excluded-middle-b3}
[B3: Where the witness goes missing]

In the derivation of @prp-quantifier-negation (a), which step makes the existence claim without a witness? Why does no witness appear, although line 4 is an \( \rulename{\exists I} \)?
:::

::: {.solution}
Two lines are classical: line 6, an \( \rulename{RAA} \) that writes the instance \( \varphi[x_0/x] \) after a box on its negation, and line 9, the \( \rulename{RAA} \) that writes the conclusion \( \exists x\, \neg\varphi \). Line 6 produces no existence claim. Line 9 is the step that asserts existence: it closes the box on \( \neg\exists x\, \neg\varphi \), which ends in \( \bot \), and writes \( \exists x\, \neg\varphi \). Closed by \( \rulename{\neg I} \), the same box would give only \( \neg\neg\exists x\, \neg\varphi \).

No witness appears because no \( \rulename{\exists I} \) produces the conclusion. Line 4 does derive \( \exists x\, \neg\varphi \) from the instance \( \neg\varphi[x_0/x] \), but that instance is the assumption of the box \( \lines{3}{5} \), used only to clash with line 2 and discharged at line 6. The name \( x_0 \) is the flagged name of the \( \rulename{\forall I} \) box \( \lines{3}{6} \): an arbitrary object, not a particular one. Line 4 is unavailable at line 9, and the conclusion there is justified by \( \rulename{RAA} \) from the box \( \lines{2}{8} \), which names nothing. Under the BHK reading, line 9 asserts "something fails \( \varphi \)" and hands over no object that fails it.
:::

### C. Going deeper

::: {#exr-excluded-middle-c1}
[C1: More witnesses]

This section proved that \( \log_2 9 \) is irrational; here are variants.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( a = \sqrt 2 \) and \( b = \log_2 25 \) are irrational numbers with \( a^b \) rational.
2. For which integers \( m \ge 2 \) are \( a = \sqrt 2 \) and \( b = \log_2(m^2) \) irrational numbers with \( a^b \) rational? Prove your answer.
:::
:::

::: {.solution}
[Hint 1]

Compute \( a^b \) first; it does not depend on whether \( b \) is rational. Then write \( m = 2^k r \) with \( r \) odd.
:::

::: {.solution}
[Hint 2]

Suppose \( \log_2(m^2) = p/q \) with integers \( p \) and \( q \ge 1 \); then \( 2^p = m^{2q} \).
:::

::: {.solution}
(a) First, \( a^b = (2^{1/2})^{\log_2 25} = 2^{(\log_2 25)/2} = 2^{\log_2 5} = 5 \), since \( \log_2 25 = 2\log_2 5 \); this is rational. Next, \( a = \sqrt 2 \) is irrational by @thm-sqrt2-irrational. Finally, suppose that \( \log_2 25 = p/q \) with integers \( p \) and \( q \ge 1 \). Since \( 25 > 1 = 2^0 \) and \( t \mapsto 2^t \) is increasing, \( \log_2 25 > 0 \), so \( p \ge 1 \). Raising \( 2^{p/q} = 25 \) to the power \( q \) gives \( 2^p = 25^q \). The left side is even because \( p \ge 1 \), and the right side is odd, being a product of odd factors. No integer is both, so \( \log_2 25 \) is irrational.

(b) **Answer:** exactly the integers \( m \ge 2 \) that are not powers of \( 2 \).

For every \( m \ge 2 \), \( a = \sqrt 2 \) is irrational and
\[
a^b = \bigl( 2^{1/2} \bigr)^{\log_2 (m^2)} = 2^{\log_2 m} = m ,
\]
which is rational. So the question is only when \( b = \log_2(m^2) = 2\log_2 m \) is irrational. Write \( m = 2^k r \) with \( k \in \nN \) and \( r \) odd, \( r \ge 1 \).

If \( r = 1 \), then \( m = 2^k \) with \( k \ge 1 \), and \( b = 2k \) is rational: these \( m \) fail.

If \( r \ge 3 \), suppose that \( b = p/q \) with integers \( p \) and \( q \ge 1 \). Since \( m \ge 2 > 1 \), \( b > 0 \), so \( p \ge 1 \). Raising \( 2^{p/q} = m^2 \) to the power \( q \) gives
\[
2^p = m^{2q} = 2^{2kq} r^{2q} .
\]
Since \( r^{2q} \ge 3 > 1 \), the right side exceeds \( 2^{2kq} \), so \( p > 2kq \). Dividing by \( 2^{2kq} \) gives \( r^{2q} = 2^{p - 2kq} \) with \( p - 2kq \ge 1 \). The left side is odd, a product of odd factors, and the right side is even. No integer is both, so \( b \) is irrational: these \( m \) work. The smallest are \( m = 3, 5, 6, 7 \). The cases \( m = 3 \) and \( m = 5 \) are the example of this section and part (a).

**Marking scheme.** (10 points)
- 2: (a) \( a^b = 5 \), with the exponent laws used.
- 2: (a) \( \log_2 25 \) irrational, with \( p \ge 1 \) justified by \( \log_2 25 > 0 \) and the parity clash \( 2^p = 25^q \).
- 2: (b) \( a^b = m \) for every \( m \), so only the rationality of \( b \) matters.
- 1: (b) powers of \( 2 \) excluded, with \( b = 2k \) rational.
- 3: (b) for \( m = 2^k r \), \( r \ge 3 \) odd, the clash \( r^{2q} = 2^{p - 2kq} \) with \( p - 2kq \ge 1 \) (or an equivalent comparison of the odd parts of \( 2^p \) and \( m^{2q} \)).
Fatal errors (0 for the step): concluding irrationality of \( b \) from "\( m \) is irrational" or "\( \log_2 m \) is not an integer"; a parity clash with \( p \) possibly \( 0 \) or negative left unaddressed.
:::

::: {#exr-excluded-middle-c2}
[C2: Modus ponens survives Kolmogorov's translation]

For statements built from letters by \( \wedge \), \( \vee \), \( \to \), and \( \neg \), define the translation \( K \) by putting \( \neg\neg \) in front of every subformula:
\[
KP = \neg\neg P \ \text{for a letter } P, \qquad K(\varphi \circ \psi) = \neg\neg(K\varphi \circ K\psi), \qquad K(\neg\varphi) = \neg\neg\neg K\varphi ,
\]
where \( \circ \) is any of \( \wedge \), \( \vee \), \( \to \). Chapter 2's @exr-reductio-and-classical-rules-b1 (a) derives \( \neg\neg P, \ \neg\neg(P \to Q) \vdash \neg\neg Q \) without \( \rulename{RAA} \) (in its printed solution).

::: {.enumerate options="label=(\alph*)"}
1. Show that every \( K\psi \) has the form \( \neg\neg X \) for some statement \( X \).
2. Deduce that \( K(\varphi \to \psi), \ K\varphi \vdash K\psi \) without \( \rulename{RAA} \), for all statements \( \varphi \) and \( \psi \).
:::
:::

::: {.solution}
[Hint 1]

Put \( K\varphi \) and \( K\psi \) in for \( P \) and \( Q \) in the Chapter 2 sequent. Which of its two premises is \( K(\varphi \to \psi) \)?
:::

::: {.solution}
[Hint 2]

The conclusion you get has two negations too many. Look for a result of Section 2.2 that removes negations without \( \rulename{\neg\neg E} \).
:::

::: {.solution}
(a) By the definition, each of the three clauses produces a statement whose first two symbols are \( \neg\neg \): \( KP = \neg\neg P \), \( K(\varphi \circ \psi) = \neg\neg(K\varphi \circ K\psi) \), and \( K(\neg\varphi) = \neg\neg(\neg K\varphi) \). So \( K\psi = \neg\neg X \), with \( X \) the letter, \( K\varphi \circ K\psi \), or \( \neg K\varphi \), respectively. No induction is needed, since the outermost clause alone decides the first two symbols.

(b) Three steps, each without \( \rulename{RAA} \).

① The derivation of @exr-reductio-and-classical-rules-b1 (a) uses no \( \rulename{RAA} \), so its sequent may be used as a derived rule (@def-derived-rule) with the statements \( K\varphi \) and \( K\psi \) in place of \( P \) and \( Q \):
\[
\neg\neg K\varphi, \ \neg\neg(K\varphi \to K\psi) \vdash \neg\neg K\psi .
\]
Its second premise is \( K(\varphi \to \psi) \) itself, by the clause for \( \to \).

② The first premise follows from \( K\varphi \) by \( \rulename{\neg\neg I} \) (@prp-double-negation (a), derived without \( \rulename{RAA} \)): a box on \( \neg K\varphi \) clashes at once with \( K\varphi \).

③ By (a), \( K\psi = \neg\neg X \), so the conclusion of ① is \( \neg\neg\neg\neg X = \neg\neg\neg(\neg X) \). @exm-triple-negation derives \( \neg\neg\neg P \vdash \neg P \) without \( \rulename{RAA} \); with \( \neg X \) in place of \( P \) it gives \( \neg\neg\neg(\neg X) \vdash \neg(\neg X) \), that is, \( \neg\neg K\psi \vdash K\psi \).

Chaining ②, ①, and ③ gives \( K(\varphi \to \psi), \ K\varphi \vdash K\psi \), and no step is \( \rulename{RAA} \): the derived rules used were all derived without it. In words, modus ponens survives the translation intuitionistically. (This is the translation that puts \( \neg\neg \) in front of every subformula. In the Gödel–Gentzen translation of the history above, \( \varphi \to \psi \) translates without an outer \( \neg\neg \), and modus ponens survives trivially.)

**Marking scheme.** (10 points)
- 2: (a) every clause of \( K \) begins with \( \neg\neg \), read off the outermost clause.
- 3: (b) the Chapter 2 sequent instantiated with \( K\varphi \), \( K\psi \), and its second premise recognized as \( K(\varphi \to \psi) \).
- 2: (b) \( \neg\neg K\varphi \) from \( K\varphi \) by \( \rulename{\neg\neg I} \), named as RAA-free.
- 3: (b) \( \neg\neg K\psi \vdash K\psi \) by the triple-negation result applied to \( \neg X \), using (a).
Fatal errors (0 for the step): removing the extra negations by \( \rulename{\neg\neg E} \) (a classical step); assuming \( K\psi \) is a letter.
:::

### R. Review

::: {#exr-excluded-middle-r1}
[R1]

A set \( A \) of real numbers **has a maximum** if some element \( m \) of \( A \) satisfies \( a \le m \) for every \( a \in A \). Write "\( A \) has no maximum" in positive form, with no \( \neg \) in front of a quantifier, and prove that the interval \( (0, 1) \) has no maximum.
:::

::: {.solution}
This uses the method of Chapter 4, Section 4.9: negate quantifier by quantifier, keeping the bounds (@prp-bounded-quantifier-negation; compare @exm-negating-definitions). In symbols, "\( A \) has a maximum" is \( \exists m \in A \; \forall a \in A \; (a \le m) \). Its negation becomes, step by step,
\[
\begin{aligned}
\neg\exists m \in A \; \forall a \in A \; (a \le m)
&\dashv\vdash \forall m \in A \; \neg\forall a \in A \; (a \le m) \\
&\dashv\vdash \forall m \in A \; \exists a \in A \; \neg(a \le m),
\end{aligned}
\]
by part (b) of @prp-bounded-quantifier-negation and then part (a) under the \( \forall \). For real numbers \( \neg(a \le m) \) says \( a > m \). So the positive form is
\[
\forall m \in A \; \exists a \in A \; (a > m):
\]
every element of \( A \) is exceeded by some element of \( A \).

Now let \( A = (0, 1) \) and let \( m \in (0, 1) \). Take \( a \coloneqq (m + 1)/2 \), which depends on \( m \). Then
\[
a - m = \frac{1 - m}{2} > 0 \quad \text{and} \quad 1 - a = \frac{1 - m}{2} > 0,
\]
since \( m < 1 \), so \( m < a < 1 \); with \( m > 0 \) this gives \( 0 < a < 1 \). So \( a \in (0, 1) \) and \( a > m \). Since \( m \in (0, 1) \) was arbitrary, the positive form holds for \( (0, 1) \), and by the interderivability above, \( (0, 1) \) has no maximum. The directions used to go back from the positive form, \( \dashv \) in (a) and in (b), are derived without \( \rulename{RAA} \), and \( a > m \) gives \( \neg(a \le m) \) by trichotomy; so this half of the argument uses no classical step beyond the order axioms.
:::

::: {#exr-excluded-middle-r2}
[R2]

Give a Fitch derivation of \( P \to (Q \vee R), \ Q \to S, \ R \to S \vdash P \to S \), and write it as one sentence of prose.
:::

::: {.solution}
This uses Chapter 1's rules: \( \rulename{{\to}I} \) (@def-rules-implication), \( \rulename{{\to}E} \) (@def-rule-implication-elimination), and \( \rulename{\vee E} \) (@def-rules-disjunction). The goal is an implication, so a box on \( P \) with the goal \( S \). Inside it, the first premise gives \( Q \vee R \), which we use by cases; each case reaches \( S \) through one of the other premises.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \hypo {2} {Q \to S}
  \hypo {3} {R \to S}
  \open
  \hypo {4} {P}
  \have {5} {Q \vee R} \ie{1,4}
  \open
  \hypo {6} {Q}
  \have {7} {S} \ie{2,6}
  \close
  \open
  \hypo {8} {R}
  \have {9} {S} \ie{3,8}
  \close
  \have {10} {S} \oe{5,6-7,8-9}
  \close
  \have {11} {P \to S} \ii{4-10}
\end{nd}$
\end{center}
```

Line 10 may cite line 5, since both lie in the box of line 4, which is still open; the case boxes end with \( S \) as lines of their own. In prose: "Suppose \( P \); then \( Q \) or \( R \) holds by the first premise, and \( S \) follows in the case \( Q \) by the second premise and in the case \( R \) by the third, so \( P \) implies \( S \)." Each premise is cited where it is used, as @def-silent-steps requires for every \( \rulename{{\to}E} \) on a hypothesis; the first premise is also the reason the two cases exhaust. The closing "so \( P \) implies \( S \)" is the closing line of \( \rulename{{\to}I} \), which @def-silent-steps allows to go unsaid.
:::

::: {#exr-excluded-middle-r3}
[R3]

Decide with a truth table whether \( (P \to Q) \to Q \models P \vee Q \), reading \( P \) and \( Q \) as atoms. If the entailment holds, give a derivation of \( (P \to Q) \to Q \vdash P \vee Q \).
:::

::: {.solution}
This item reaches back within Part 0, since there is no earlier Part: it uses the tables of Chapter 3 and the derivations of Chapter 2.

*The table.* Work backwards from F, as in @exm-backwards-from-f and the entailments of @def-valid-argument. A refuting row needs \( P \vee Q \) false, so \( P \) and \( Q \) are both false. In that row \( P \to Q \) is true, so the premise \( (P \to Q) \to Q \) is "T \( \to \) F", which is false. So no row makes the premise true and the conclusion false, and the entailment holds. The full table agrees:
\[
\begin{array}{cc|ccc}
P & Q & P \to Q & (P \to Q) \to Q & P \vee Q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F}
\end{array}
\]

*The derivation.* The goal is a disjunction with neither side in hand, and the premise gives \( Q \) only once \( P \to Q \) is available. We are stuck, so we open an \( \rulename{RAA} \) box on \( \neg(P \vee Q) \) (@def-rule-raa). Inside it, \( P \to Q \) is built by a box on \( P \): \( \rulename{\vee I} \) gives \( P \vee Q \), which clashes with the assumption, and \( \rulename{\bot E} \) writes \( Q \). Then the premise gives \( Q \), and \( \rulename{\vee I} \) clashes again.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to Q}
  \open
  \hypo {2} {\neg (P \vee Q)}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \have {5} {\bot} \ne{4,2}
  \have {6} {Q} \be{5}
  \close
  \have {7} {P \to Q} \ii{3-6}
  \have {8} {Q} \ie{1,7}
  \have {9} {P \vee Q} \oi{8}
  \have {10} {\bot} \ne{9,2}
  \close
  \have {11} {P \vee Q} \raa{2-10}
\end{nd}$
\end{center}
```

The one classical line is line 11. Closing the same box by \( \rulename{\neg I} \) instead gives \( \neg\neg(P \vee Q) \), and then the derivation is intuitionistic: the premise yields the double negation of its classical conclusion, the pattern of Glivenko's theorem in the remark of this section.

No derivation of this sequent avoids \( \rulename{RAA} \) or one of its equivalents; we state this without proof, as Chapter 2 did for similar sequents. (With \( \bot \) in place of \( Q \), the sequent would turn \( \neg\neg P \) into \( P \) without any further classical step, and Chapter 3's optional theorem in Section 3.5 shows that \( \neg\neg P \vdash P \) needs \( \rulename{RAA} \).)
:::

::: {#exr-excluded-middle-r4}
[R4]

Prove that for every integer \( n \), \( n^3 - n \) is divisible by \( 3 \).
:::

::: {.solution}
*The tool* is proof by cases on the remainder of \( n \) on division by \( 3 \): every integer \( n \) is \( 3k \), \( 3k + 1 \), or \( 3k + 2 \) for some integer \( k \). This is a school fact, of the same kind as "every integer is even or odd" in Chapter 2. It is \( \rulename{\vee E} \) with three cases (@def-rules-disjunction, used twice), and in each case \( \rulename{\exists I} \) (@def-rule-existential-introduction) with an explicit witness. First factor:
\[
n^3 - n = (n - 1)\, n\, (n + 1) .
\]
Let \( n \) be an integer, and let \( k \) be an integer with \( n = 3k \), \( n = 3k + 1 \), or \( n = 3k + 2 \).

*Case \( n = 3k \).* Then \( n^3 - n = 3 \cdot \bigl( (3k - 1)\, k\, (3k + 1) \bigr) \).

*Case \( n = 3k + 1 \).* Then \( n^3 - n = (3k)(3k + 1)(3k + 2) = 3 \cdot \bigl( k\, (3k + 1)(3k + 2) \bigr) \).

*Case \( n = 3k + 2 \).* Then \( n^3 - n = (3k + 1)(3k + 2)(3k + 3) = 3 \cdot \bigl( (3k + 1)(3k + 2)(k + 1) \bigr) \).

In each case \( n^3 - n = 3j \) for the integer \( j \) in brackets, so \( 3 \mid n^3 - n \). Since \( n \) was arbitrary, this holds for every integer \( n \).

*Why the look-alikes are worse.* A proof by contradiction ("suppose \( 3 \nmid n^3 - n \) …") would have to reach exactly this case analysis and then clash with its assumption at the last line: a direct proof in costume (@exm-costume-direct). Induction is closer, but it fits the statement badly: with base case \( P(0) \) and the step from \( n \) to \( n + 1 \) (@ax-induction) it proves the claim only for \( n \in \nN \), and the negative integers \( n = -m \), \( m \in \nZ_{>0} \), need a second argument, for instance \( (-m)^3 - (-m) = -(m^3 - m) \). The case split covers all integers at once.
:::

<!-- dependency ledger
prp-not-not-excluded-middle (claim): Glivenko's theorem (classical propositional theorems become intuitionistically derivable under a double negation) and its failure with quantifiers (not-not-forall-x (phi or not phi)) | stated without proof and marked so; the result is optional and nothing depends on the remark
prp-not-not-excluded-middle (claim): Brouwer's analysis refutes "every real is 0 or not 0" under extra axioms | stated without proof in a warning; nothing depends on it
thm-irrational-power-rational (proof): sqrt 2 exists; sqrt2^sqrt2 is a positive real; (x^y)^z = x^(yz) for x > 0; sqrt2 * sqrt2 = 2; sqrt2^2 = 2 | school facts (square roots: ch11 (promised); real exponents: ch20 (promised)); the result is optional and nothing depends on it
thm-irrational-power-rational (claim): Gelfond-Schneider: sqrt2^sqrt2 is transcendental | stated without proof in a remark, marked so; nothing depends on it
thm-irrational-power-rational (idea): nothing in the book decides whether sqrt2^sqrt2 is rational | meta-claim about the book; the remark after the proof names the theorem that does, not proved here
prp-log2-9-irrational (proof): log2 9 > 0 because 2^0 = 1 < 9 and t -> 2^t is increasing; 2^(p/q) = 9 gives 2^p = 9^q; log2 9 = 2 log2 3; (2^(1/2))^(log2 9) = 2^(log2 3) = 3 | school facts about real exponents and logarithms, ch20 (promised); the result is optional
prp-log2-9-irrational (proof): 2^p is even for p >= 1; a product of odd integers is odd; no integer is both even and odd | (E2) of Section 2.1 (cited in prose) and school arithmetic of Z, ch07 (promised)
prp-log2-9-irrational (proof): p/q = (-p)/(-q), so q may be taken >= 1; p = q log2 9 > 0; an integer p > 0 has p >= 1 (nothing strictly between 0 and 1) | school arithmetic of Z, ch07 (promised; STATUS row 95, "nothing between n and n + 1")
prp-log2-9-irrational (example): sqrt2^b = 2^(b/2), so b = log2(m^2) gives m | school facts about real exponents, ch20 (promised); motivation only
excluded-middle-bhk (claim): Goldbach's conjecture is neither proved nor refuted | external fact, informal; nothing depends on it
excluded-middle-history (claim): dates, titles and events of the history subsection (Brouwer 1908, Kolmogorov 1925, Hilbert 1927/1928, Annalen 1928, Glivenko 1929, Heyting 1930, Goedel and Gentzen 1933, Bishop 1967) | external historical record, no quotation; nothing depends on it
excluded-middle-analysis (claim): constructive sup iff order-located; Specker's sequence (1949); approximate IVT, exact IVT for strictly increasing f; BW bisection step is LEM | stated informally without proof and marked so; previews of ch11, ch12, ch16 (prose pointers); nothing depends on them
excluded-middle-lean (claim): in Lean, Classical.em is derived from Classical.choice via Diaconescu's theorem; data defined by classical decision must be noncomputable | external facts about Lean, stated without proof; nothing depends on them
excluded-middle-position (claim): Chapter 11's ordered-field axioms include trichotomy; constructive analysis rejects trichotomy for reals | ch11 (O1) (prose pointer, later chapter, nothing rests on it); the constructive fact stated without proof
excluded-middle-check-1 (solution): the lists of results derived with RAA in Chapters 2-4 | inline, read off the cited results, each of which says where RAA enters
excluded-middle-check-2 (solution): BHK proof of not (P and not P) | inline
exr-excluded-middle-a1 (solution): no derivation reaches bot from no premises | thm-soundness (cited); when P or the derivation involves quantifiers or equality, the soundness statement for predicate logic of ch04 Section 4.11 (prose pointer; stated there without proof and taken on trust, as the rest of the book does); prp-excluded-middle (cited)
excluded-middle-one-rule (claim): soundness applies to every intuitionistic derivation, and "nobody can refute excluded middle" | thm-soundness (cited); ch04 Section 4.11 soundness statement for predicate logic (prose pointer, stated there without proof)
excluded-middle-one-rule (claim): without bot-E (and without RAA), bot |- P is not derivable | stated without proof and marked so; nothing depends on it
excluded-middle-one-rule (claim): adding the rules for forall, exists and = does not make |- P or not P derivable without RAA | stated without proof and marked so; ch03 optional thm-raa-independent pointed at for the propositional rules; nothing depends on it
exr-excluded-middle-b1 (solution): not-not-P -> P is not derivable without RAA | stated without proof and marked so; nothing depends on it
exr-excluded-middle-b2 (solution): n + 1 in N and n + 1 > n for n in N | school arithmetic, ch07 (promised; STATUS row 95)
exr-excluded-middle-c1 (solution): log2 25 = 2 log2 5; (2^(1/2))^(log2 x) = 2^(log2 sqrt x); log2 25 > 0; 2^(p/q) = x gives 2^p = x^q | school facts about real exponents, ch20 (promised)
exr-excluded-middle-c1 (solution): every integer m >= 2 is 2^k r with k in N and r odd; products of odd integers are odd; 2^p > 2^(2kq) implies p > 2kq; 2^p = 2^(2kq) 2^(p-2kq) for 2kq <= p | school arithmetic of Z, ch07 (promised; STATUS row 95)
exr-excluded-middle-c2 (solution): a derived sequent may be used with statements substituted for its letters | def-derived-rule (cited)
exr-excluded-middle-r1 (solution): (m+1)/2 - m = (1-m)/2 > 0 and 1 - (m+1)/2 = (1-m)/2 > 0 for m < 1; not (a <= m) iff a > m | school algebra (order and trichotomy), ch11 (promised)
exr-excluded-middle-r3 (solution): no derivation of (P -> Q) -> Q |- P or Q avoids RAA | stated without proof and marked so; ch03 optional thm-raa-independent pointed at in prose, outside the argument; nothing depends on it
exr-excluded-middle-r4 (solution): every integer is 3k, 3k+1 or 3k+2 for some integer k | school fact (division with remainder by 3), ch07 (promised): thm-division-algorithm
exr-excluded-middle-r4 (solution): integers closed under +, - and * (the bracketed j, including 3k - 1) | school algebra, ch07 (promised): prp-integers-closed (STATUS row 95)
exr-excluded-middle-r4 (solution): n^3 - n = (n-1)n(n+1) and the three case factorizations | inline (polynomial algebra)
-->
