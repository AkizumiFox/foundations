# Chapter Review

## Summary

The chapter added the rules for \( \neg \), \( \bot \) and \( \leftrightarrow \), and the rule \( \rulename{RAA} \). Together with Chapter 1's seven rules they make the thirteen rules of the book's logic. A clash gives anything (@prp-ex-falso), and an implication whose hypothesis cannot hold is true (@prp-vacuous-implication). The chapter proved that if \( n^2 \) is even, then \( n \) is even (@thm-square-even-implies-even), and that \( \sqrt 2 \) is irrational (@thm-sqrt2-irrational). It showed that a result already proved may be used as one line of a later derivation, and why that is safe (@lem-weakening-cut). An iff is two implications, the "if" of a definition is an iff, and no statement is equivalent to its own negation (@lem-not-iff-own-negation). With \( \rulename{RAA} \) the chapter derived double negation, excluded middle, De Morgan's laws and Peirce's law, and showed that \( \rulename{RAA} \), \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \) are one principle in three forms (@thm-classical-rules-interderivable).

What is left open: a method for **finding** derivations (Chapter 3), and a way to show that a sequent has **no** derivation (Chapter 4). Chapter 4 also settles whether the classical rule could be done without.

## Proof methods in this chapter

- **When the goal is \( \bot \), find a clash.** Look for a statement and its negation among the available lines. Or, if a negation \( \neg\varphi \) is available, make \( \varphi \) the next goal. Introduced in Section 2.1.
- **An impossible case closes itself.** In a proof by cases, a case that reaches \( \bot \) ends by \( \rulename{\bot E} \) on the current goal. Introduced in Section 2.1.
- **To prove "not \( \varphi \)", assume \( \varphi \).** The box opens with \( \varphi \) itself, without the "not", and ends on \( \bot \). Introduced in Section 2.2.
- **Use a derived rule as one line.** A sequent already derived can be used like a rule. Introduced in Section 2.3.
- **Two boxes for an iff.** Open one box for each direction. Each box opens with one side and ends with the other. Introduced in Section 2.4.
- **When stuck, assume the negation of the goal.** This is proof by contradiction. Then look for a clash. Introduced in Section 2.5.
- **A disjunction with neither side within reach: expect the classical step.** Suppose the goal is a disjunction, and each side, as a goal on its own, can be broken. Then aim at the whole disjunction by \( \rulename{RAA} \). Introduced in Section 2.5.

Section 3.1 gathers these methods and Chapter 1's into one table, and all thirteen rules onto one card.

## Terms

- **biconditional rules** \( \rulename{{\leftrightarrow}I} \), \( \rulename{{\leftrightarrow}E} \): prove an iff by two boxes, and use it in either direction (@def-rules-biconditional).
- **classical rules** \( \rulename{RAA} \), \( \rulename{\neg\neg E} \), \( \rulename{LEM} \): each can be derived from each other one, so they are one principle (@thm-classical-rules-interderivable).
- **contradiction** \( \bot \): the line a clash produces (@def-rules-contradiction).
- **contradiction rules** \( \rulename{\neg E} \), \( \rulename{\bot E} \): a clash gives \( \bot \), and \( \bot \) gives anything (@def-rules-contradiction).
- **contrapositive**: \( \neg\psi \to \neg\varphi \), derivable from \( \varphi \to \psi \) (@prp-contrapositive).
- **cut**: a result already proved may be pasted into a derivation (@lem-weakening-cut).
- **De Morgan's laws**: how negation passes through "and" and "or" (@prp-de-morgan).
- **derived rule**: a sequent already derived, used as one line (@def-derived-rule).
- **disjunctive syllogism** \( \rulename{DS} \): from \( \varphi \vee \psi \) and \( \neg\varphi \), conclude \( \psi \) (@prp-disjunctive-syllogism).
- **double negation**: \( \neg\neg\varphi \) and \( \varphi \), each derivable from the other (@prp-double-negation).
- **ex falso**: from a clash, anything follows (@prp-ex-falso).
- **excluded middle** \( \rulename{LEM} \): \( \varphi \vee \neg\varphi \), with no premises (@prp-excluded-middle).
- **modus tollens** \( \rulename{MT} \): from \( \varphi \to \psi \) and \( \neg\psi \), conclude \( \neg\varphi \) (@prp-modus-tollens).
- **negation rule** \( \rulename{\neg I} \): assume \( \varphi \), reach \( \bot \), conclude \( \neg\varphi \) (@def-rules-negation).
- **Peirce's law**: \( ((\varphi \to \psi) \to \varphi) \to \varphi \) (@prp-peirce).
- **provably equivalent**, \( \dashv\vdash \): each derivable from the other (@def-provable-equivalence).
- **reductio ad absurdum** \( \rulename{RAA} \): assume \( \neg\varphi \), reach \( \bot \), conclude \( \varphi \) (@def-rule-raa).
- **vacuously true**: said of an implication whose hypothesis cannot hold (@prp-vacuous-implication).
- **weakening**: extra premises never spoil a derivation (@lem-weakening-cut).

## Results used from earlier volumes

None. *Logic and Proof* is the first volume, and this chapter uses only Chapter 1.
