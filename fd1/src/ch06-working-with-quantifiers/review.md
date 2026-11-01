# Chapter Review

## Summary

The bounded rules are shortcuts: they prove nothing that the four quantifier rules cannot prove (@prp-bounded-quantifier-rules). "Not every" is "some not", and "none" is "every not" (@prp-quantifier-negation). A negated implication is a conjunction (@prp-negated-implication), and when a bounded quantifier is negated, its bound stays the same (@prp-bounded-quantifier-negation). A part of a formula may be replaced by a provably equivalent part, even under quantifiers (@prp-replacement). A step that is right for propositional reasons alone may be written as one line (@prp-taut-skeleton). With these, the chapter translated and negated the definitions of analysis, and ran the search method and the four kinds of task with quantifiers. Its last section derived "uniformly continuous implies continuous" line by line (@exm-uniform-implies-continuous), and found the lines that stop the converse.

What is open: every "break" in this chapter was shown by a counter-reading. Does a counter-reading really rule out every derivation? Chapter 7 answers this.

## Proof methods in this chapter

- **Read it back.** Before you use a translation, read it back into words and compare it with the original sentence. Introduced in Section 6.1.
- **Negate one quantifier at a time.** Push \( \neg \) inward from the outside, changing \( \forall \) to \( \exists \) and \( \exists \) to \( \forall \), and keep every bound as it is. Introduced in Section 6.2.
- **Name the witness early, then instantiate at the term you need.** Open the box for each \( \exists \) premise as soon as it appears. Then use each \( \forall \) line at the names those boxes give. Introduced in Section 6.3.
- **Reduce to propositional reasoning.** Open the boxes, instantiate the \( \forall \) lines at the names in play, and finish with one TAUT line. Then close the boxes. Introduced in Section 6.3.
- **Test a subgoal by a counter-reading.** Before chasing a subgoal, look for a reading that makes the available lines true and the subgoal false. If there is one, go back and choose differently. Introduced in Section 6.3.
- **Read the dependence off the boxes.** A chosen constant may depend only on the names whose boxes are open where it is chosen. Introduced in Section 6.4.

## Terms

- **A, E, I, O forms**: "every \( P \) is \( Q \)", "no \( P \) is \( Q \)", "some \( P \) is \( Q \)", "some \( P \) is not \( Q \)", in [Section 6.2](#the-square-of-opposition).
- **alternation**: a change from \( \forall \) to \( \exists \), or back, in a row of quantifiers, in [Section 6.2](#prenex-form).
- **bounded rules**: one-line rules for \( \forall x > 0 \), \( \exists x \in A \) and the like, which add no power (@prp-bounded-quantifier-rules).
- **contradictory**, **contrary**: exactly one of the two is true; the two are never both true, in [Section 6.2](#the-square-of-opposition).
- **negated implication**: \( \neg(\varphi \to \psi) \) is equivalent to \( \varphi \wedge \neg\psi \) (@prp-negated-implication).
- **passage laws**: laws that move a quantifier across a connective (@prp-quantifier-passage).
- **prenex form**: every quantifier stands at the front of the formula, in [Section 6.2](#prenex-form).
- **propositional core**: instantiate, reason propositionally, then close the boxes, in [Section 6.3](#the-propositional-core).
- **propositional skeleton**: the formula read with each atomic part and each part that begins with a quantifier as a letter (@def-propositional-skeleton).
- **quantifier distribution**: \( \forall \) over \( \wedge \), and \( \exists \) over \( \vee \) (@prp-quantifier-distribution).
- **quantifier negation**: "not every" is "some not", and "none" is "every not" (@prp-quantifier-negation).
- **replacement of provable equivalents**: a part of a formula may be swapped for an equivalent part (@prp-replacement).
- **TAUT step on the skeleton**: a line justified because the skeletons make a valid propositional argument (@prp-taut-skeleton).
- **uniformly continuous**: one \( \delta \) works at every point, in [Section 6.4](#two-definitions-that-differ-in-one-place).
- **witness function**: a witness written as a function of the names it may depend on, in [Section 6.4](#witness-functions).

## Threads

- **Before *Sets and Functions*.** That volume uses Chapters 1–6 and 8 of this one, read with every A exercise and one B and one C exercise per section. It needs Sections 7.1–7.2 before its own Section 4.1.
- **Facts used here as school facts.** *Analysis on the Real Line*, Chapter 1, proves from the axioms for the real numbers the facts about \( \nN \) inside \( \nR \) and about absolute value that Sections 6.1 and 6.2 used as known. Its proof of the Archimedean property uses "not every" gives "some not" (Section 6.2).
- **Continuity.** *Analysis on the Real Line*, Chapters 5 and 6, define continuity and uniform continuity. Section 6.4 used them only as patterns of quantifiers.
- **Choosing many witnesses at once.** Picking a witness for every \( \varepsilon \) at once, as one function (Section 6.4), in general makes infinitely many choices at once. *Sets and Functions*, Chapter 6, states the axiom that allows this, the axiom of choice.
