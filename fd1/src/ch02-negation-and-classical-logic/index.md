# Negation and Classical Logic

Is there a rational number whose square is \( 2 \)? Is \( x^2 + 1 \) ever \( 0 \) for a real number \( x \)? Is "if \( x^2 < 0 \), then \( x = 7 \)" true? Chapter 1 could prove that things are so, but not that something is **not** so, and it read the third sentence only informally, as a promise not broken: no rule yet derives it. By the end of this chapter you will be able to prove that something is not so; you will know when "suppose not" is a different kind of step from the others, and why that one step is all that classical logic adds. Two questions stay open at the end. How do you find a derivation when none comes to mind? Chapter 3 answers it. And how could you ever show that something is **not** derivable? Chapter 4 answers that.

**Steps about "every" and "some".** Proofs in this chapter apply facts about every integer to one integer, pass from an arbitrary rational number to all of them, and name the \( k \) in "\( n = 2k + 1 \)". These are steps about "every" and "some". Here they are used as ordinary reasoning, as in school algebra; Chapter 5 gives them rules.

**What you need.** All of Chapter 1: the rules for "and", "implies", and "or", and above all the definition of a derivation, with its boxes and its scope rule (@def-derivation). School algebra about integers and real numbers is used in examples, as facts.

**Time.** About 30 hours on the core track (all of A, one B and one C per section, the exit checks); about 50 hours for everything.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, core; Sections 7.1–7.2 before its Section 2.5.

## Roadmap

- **Contradiction: Using a Negation.** The rules \( \rulename{\neg E} \) and \( \rulename{\bot E} \): what a clash is, what it buys, why an impossible case closes itself and an implication with an impossible hypothesis is true, and the two sequents called the paradoxes of material implication.
- **Proving a Negation.** The rule \( \rulename{\neg I} \), and with it the irrationality of \( \sqrt 2 \), then of \( \sqrt p \) for a prime \( p \).
- **Derived Rules: Proved Sequents as New Rules.** A proved sequent used as one line; modus tollens, the contrapositive and disjunctive syllogism; and why pasting a proved sequent into a derivation is safe (weakening and cut).
- **Iff, Equivalence, and What a Definition Says.** The rules for \( \leftrightarrow \), provable equivalence, why a definition's "if" means "if and only if", chains of equivalences, and why no statement is equivalent to its own negation.
- **Proof by Contradiction and the Classical Rules.** The rule \( \rulename{RAA} \), the classical laws it gives (double-negation elimination, excluded middle, De Morgan, Peirce), where the classical step is needed, and why three of its forms stand or fall together.

## Named moves

- **Goal \( \bot \): find a clash.** Look for \( \varphi \) and \( \neg\varphi \) among the available lines, or make \( \varphi \) a subgoal for some \( \neg\varphi \) you have. (Section 2.1)
- **An impossible case closes itself.** In a proof by cases, a case that reaches \( \bot \) ends by \( \rulename{\bot E} \) on the current goal. (Section 2.1)
- **To prove "not \( \varphi \)", assume \( \varphi \).** The box opens with the unnegated statement and ends on \( \bot \). (Section 2.2)
- **Use a derived rule as one line.** A proved sequent is a new rule. (Section 2.3)
- **Two boxes for an iff.** One box for each direction, each ending on the other side. (Section 2.4)
- **When stuck, assume the negation of the goal.** Proof by contradiction, and then hunt for a clash. (Section 2.5)
- **A disjunction with neither side within reach: expect the classical step.** When each side of a disjunctive goal breaks on its own, aim at the disjunction by \( \rulename{RAA} \). (Section 2.5)

Section 3.1 gathers these moves and Chapter 1's into one table, and all thirteen rules onto one card.

## Summary

The chapter added the rules for \( \neg \), \( \bot \) and \( \leftrightarrow \) and the rule \( \rulename{RAA} \), which with Chapter 1's seven make the thirteen primitive rules. It proved that a clash gives anything (@prp-ex-falso) and that an impossible hypothesis makes an implication true (@prp-vacuous-implication); it proved the theorem Argument B set out to prove (@thm-square-even-implies-even) and that \( \sqrt 2 \) is irrational (@thm-sqrt2-irrational). It turned proved sequents into rules, with weakening and cut as the reason pasting is safe (@lem-weakening-cut). It showed that an iff is two implications, that a definition's "if" is an iff, and that no statement is equivalent to its own negation (@lem-not-iff-own-negation). With \( \rulename{RAA} \) it derived double negation, excluded middle, De Morgan's laws and Peirce's law, and showed \( \rulename{RAA} \), \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \) to be one principle (@thm-classical-rules-interderivable). Still open: a method for **finding** derivations (Chapter 3), and a way to show that a sequent has **no** derivation (Chapter 4), which also settles whether the classical rule could be done without.

## Terms

- **biconditional rules** \( \rulename{{\leftrightarrow}I} \), \( \rulename{{\leftrightarrow}E} \): prove by two boxes; use either direction (@def-rules-biconditional).
- **classical rules** \( \rulename{RAA} \), \( \rulename{\neg\neg E} \), \( \rulename{LEM} \): interderivable; one principle (@thm-classical-rules-interderivable).
- **contradiction** \( \bot \): the line a clash produces (@def-rules-contradiction).
- **contradiction rules** \( \rulename{\neg E} \), \( \rulename{\bot E} \): a clash gives \( \bot \); \( \bot \) gives anything (@def-rules-contradiction).
- **contrapositive**: \( \neg\psi \to \neg\varphi \), derivable from \( \varphi \to \psi \) (@prp-contrapositive).
- **cut**: a proved lemma may be pasted in (@lem-weakening-cut).
- **De Morgan's laws**: how negation passes through "and" and "or" (@prp-de-morgan).
- **derived rule**: a proved sequent used as one line (@def-derived-rule).
- **disjunctive syllogism** \( \rulename{DS} \): from \( \varphi \vee \psi \) and \( \neg\varphi \), conclude \( \psi \) (@prp-disjunctive-syllogism).
- **double negation**: \( \neg\neg\varphi \) and \( \varphi \), each from the other (@prp-double-negation).
- **ex falso**: from a clash, anything follows (@prp-ex-falso).
- **excluded middle** \( \rulename{LEM} \): \( \varphi \vee \neg\varphi \), with no premises (@prp-excluded-middle).
- **modus tollens** \( \rulename{MT} \): from \( \varphi \to \psi \) and \( \neg\psi \), conclude \( \neg\varphi \) (@prp-modus-tollens).
- **negation rule** \( \rulename{\neg I} \): assume \( \varphi \), reach \( \bot \), conclude \( \neg\varphi \) (@def-rules-negation).
- **Peirce's law**: \( ((\varphi \to \psi) \to \varphi) \to \varphi \) (@prp-peirce).
- **provably equivalent**, \( \dashv\vdash \): each derivable from the other (@def-provable-equivalence).
- **reductio ad absurdum** \( \rulename{RAA} \): assume \( \neg\varphi \), reach \( \bot \), conclude \( \varphi \) (@def-rule-raa).
- **vacuously true**: an implication whose hypothesis cannot hold (@prp-vacuous-implication).
- **weakening**: extra premises never spoil a derivation (@lem-weakening-cut).
