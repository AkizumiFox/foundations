# Working with Quantifiers: Translation, Laws and Search

A first course in analysis defines "\( a_n \to L \)" with three quantifiers and two bounds, then asks for a proof that a sequence does **not** converge, which starts from its negation. Chapter 5 gave the rules one per section; this chapter puts them to work: turning a definition into a formula, negating and rearranging it by laws, and finding the derivation a claim needs. *You know every quantifier rule. Can you turn a definition from analysis into a formula, negate it without error, and find the derivation it needs?* It ends where Chapter 5 began: why "uniformly continuous implies continuous" has a short derivation and a false converse.

::: {.remark}
[Looking back]

Chapter 3 did for the connectives what this chapter does for the quantifiers. Section 3.3 turned arguments in words into derivations; Section 6.1 does the same for definitions with quantifiers. Section 3.2 sorted the tasks, and Section 3.1 gave the search method; Section 6.3 does both again, with flags and witnesses. Section 6.2 collects the equivalences the tasks keep using. Section 6.4 has no twin: it is the chapter's capstone.
:::

**What you need.** Chapters 1–5. From Chapter 3: the search method (Section 3.1) and the four kinds of task (Section 3.2). From Chapter 4: truth tables and semantic entailment (@def-valid-argument), completeness (@thm-completeness), the move *test the subgoal* (Section 4.7) and the TAUT step for propositional formulas (@def-rule-taut). From Chapter 5: the four quantifier rules with their side conditions (@def-rules-universal, @def-rules-existential), bounded quantifiers and the convention for mixing kinds of number (@def-bounded-quantifier), substitution, free-for and renaming (Section 5.2), equality (Section 5.7), and counter-readings ([Section 5.3](#counter-readings)). School arithmetic and the order of \( \nN \), \( \nZ \), \( \nR \) are used in examples as facts.

**Time.** About 20 hours on the core track (all of A, one B and one C per section, the exit checks); about 35 hours for everything.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, core; Sections 7.1–7.2 before its Section 2.5.

**How to read this chapter.** Every section is on the first reading, with its folds closed. The folds hold the proofs of the bounded rules, of the replacement rule and of TAUT on the skeleton, the derivations of the distribution and passage laws, and short remarks on edge cases. They are not optional: later proofs may use them.

## Roadmap

- **Translating mathematics.** Definitions from analysis as formulas, worked from the outside in; the bounded rules; five traps, each shown wrong by a reading; "infinitely many" against "eventually".
- **Negating and moving quantifiers.** "Not every" is "some not"; negation pushed inward by the replacement rule; the four forms A, E, I, O and their square; the laws that move a quantifier across a connective, and prenex form.
- **Finding first-order derivations.** The search method with flags and witnesses; TAUT on the skeleton; the propositional core; the four kinds of task; a library of sequents and a battery.
- **Uniformly continuous implies continuous, rule by rule.** The capstone derivation, the lines where the converse breaks, \( x^2 \) as the counter-reading, and witness functions \( \delta(\varepsilon) \) against \( \delta(x, \varepsilon) \).

## Named moves

- **Read it back.** Read a translation back into words before using it. (Section 6.1)
- **Negate quantifier by quantifier.** Push \( \neg \) inward, swapping \( \forall \) and \( \exists \), keeping the bounds. (Section 6.2)
- **Name the witness early, then instantiate at the term you need.** Chapter 5's two moves, in that order. (Section 6.3)
- **The propositional core.** Instantiate at the names in play, reason propositionally, with TAUT, then close the boxes. (Section 6.3)
- **Test the subgoal by a counter-reading.** Section 4.7's move, with quantifiers. (Section 6.3)
- **Read the dependency off the boxes.** A witness may depend only on the flags whose boxes enclose it. (Section 6.4)

**Where this goes.** *Analysis on the Real Line*, Chapter 1 proves from the real-number axioms the facts about \( \nN \) in \( \nR \) and absolute value that Sections 6.1 and 6.2 use as school facts, and it uses "not every" gives "some not" (Section 6.2) in its proof of the Archimedean property. Its Chapters 5 and 6 define continuity and uniform continuity, which Section 6.4 uses only as quantifier patterns. Picking a witness for every \( \varepsilon \) at once, as one function (Section 6.4), in general appeals to the axiom of choice, which *Sets and Functions*, Chapter 3 states.

## Summary

The bounded rules add no power (@prp-bounded-quantifier-rules). "Not every" is "some not", with one direction classical (@prp-quantifier-negation); a negated implication is a conjunction (@prp-negated-implication); a bound stays with its quantifier (@prp-bounded-quantifier-negation). A part may be replaced anywhere by a provably equivalent part, by a syntactic induction (@prp-replacement); a step right for propositional reasons alone is derivable (@prp-taut-skeleton). The chapter translated and negated the definitions of analysis, and took the search method and the four tasks to quantifiers. The capstone derived "uniformly continuous implies continuous" (@exm-uniform-implies-continuous) and located the side conditions that stop the converse.

What is open: every "break" here was a counter-reading. Does one rule out every derivation? Chapter 7 asks.

## Terms

- **A, E, I, O forms**: every, no, some, some not ([Section 6.2](#the-square-of-opposition)).
- **alternation**: a \( \forall \)/\( \exists \) change in a prefix ([Section 6.2](#prenex-form)).
- **bounded rules**: abbreviations, no new power (@prp-bounded-quantifier-rules).
- **contradictory, contrary**: exactly one true; never both true ([Section 6.2](#the-square-of-opposition)).
- **negated implication**: \( \neg(\varphi \to \psi) \) is \( \varphi \wedge \neg\psi \) (@prp-negated-implication).
- **passage laws**: move a quantifier across a connective (@prp-quantifier-passage).
- **prenex form**: every quantifier at the front ([Section 6.2](#prenex-form)).
- **propositional core**: instantiate, reason propositionally, close ([Section 6.3](#the-propositional-core)).
- **propositional skeleton**: prime parts read as letters (@def-propositional-skeleton).
- **quantifier distribution**: \( \forall \) over \( \wedge \), \( \exists \) over \( \vee \) (@prp-quantifier-distribution).
- **quantifier negation**: "not every" is "some not" (@prp-quantifier-negation).
- **replacement of provable equivalents**: swap a part for an equivalent (@prp-replacement).
- **TAUT step, on the skeleton**: propositionally right (@prp-taut-skeleton).
- **uniformly continuous**: one \( \delta \) for all points ([Section 6.4](#two-definitions-that-differ-in-one-place)).
- **witness function**: a witness depending on flags ([Section 6.4](#witness-functions)).
