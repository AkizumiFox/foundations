# Chapter Review

## Summary

The chapter made the language of predicate logic exact, including substitution and the one way it goes wrong, capture. Each quantifier rule has a condition about names:

- \( \rulename{\forall E} \) may use any term that is free for the variable;
- \( \rulename{\forall I} \) needs a new name, about which nothing is assumed;
- \( \rulename{\exists I} \) uses a witness that a line already shows;
- \( \rulename{\exists E} \) names the witness with a new letter that stays inside its box.

With these rules and the two rules for equality, \( \exists x\, \forall y \) gives \( \forall y\, \exists x \), and a counter-reading breaks the converse. Equal objects share every property (@prp-leibniz-law). No relation has the barber's property (@thm-barber). And a definition proves nothing new about the old words (@prp-definitional-extension).

What is open: a search that stalls shows nothing, and counter-readings are not yet made exact (Chapter 7). The definitions of analysis, with four quantifiers in a row, are still to be translated, negated and derived (Chapter 6).

## Proof methods in this chapter

- **Read the dependence off the order.** A variable depends only on the variables quantified to its left. (Section 5.1)
- **Instantiate at the term you need** (\( \rulename{\forall E} \)). Read the term off the goal. (Section 5.3)
- **Break a claim with a counter-reading.** Find a reading in which the premises are true and the line is false. (Section 5.3)
- **Let \( x \) be arbitrary** (\( \rulename{\forall I} \)). Use a new name, about which nothing is assumed. (Section 5.4)
- **Postpone the witness** (\( \rulename{\exists I} \)). Choose the term once a line shows it. (Section 5.5)
- **Name the witness early** (\( \rulename{\exists E} \)). Write "choose \( x_0 \) with …", and never generalize over \( x_0 \). (Section 5.6)
- **Fix, obtain, choose.** Fix the arbitrary objects by \( \rulename{\forall I} \), obtain witnesses from the hypotheses by \( \rulename{\forall E} \) and \( \rulename{\exists E} \), and choose the goal's witness by \( \rulename{\exists I} \). Most proofs in analysis have this shape. (Section 5.6)
- **Existence and uniqueness, separately.** Prove "at least one" and "at most one" as two statements. (Section 5.8)

The four quantifier rules are on one card at the end of Section 5.6, and the whole calculus is in the table at the end of Section 5.7.

## Terms

- **bounded quantifier**: \( \forall x \in A \), \( \exists x \in A \) (@def-bounded-quantifier).
- **counter-reading**: a reading with the premises true and the line false, from [Section 5.3](#counter-readings).
- **counting with equality**: at least, at most, exactly \( n \) (@def-counting-with-equality).
- **definite description**: "the \( x \) such that \( \varphi \)" (@def-definite-description).
- **definitional extension**: a new symbol, nothing new proved (@prp-definitional-extension).
- **equality rules** \( \rulename{{=}I} \), \( \rulename{{=}E} \): \( t = t \); replace equals (@def-rules-equality).
- **existential elimination** \( \rulename{\exists E} \): name a witness, with a new name (@def-rules-existential).
- **existential introduction** \( \rulename{\exists I} \): from an instance (@def-rule-existential-introduction).
- **flag, flagged box**: the new name of \( \rulename{\forall I} \) (@def-rules-universal).
- **formula**, first-order: connectives and quantifiers over atoms (@def-first-order-formula).
- **free for**: substituting captures no variable (@def-free-for).
- **free variable**: a letter no quantifier binds (@def-free-variable).
- **Leibniz's Law**: equals share every property (@prp-leibniz-law).
- **sentence**: no free variable (@def-sentence).
- **substitution** \( \varphi[t/x] \): \( t \) for free \( x \) (@def-substitution).
- **term**: a name for an object (@def-term).
- **unique existence** \( \exists! \): at least and at most one (@def-unique-existence).
- **universal elimination** \( \rulename{\forall E} \): any instance (@def-rule-universal-elimination).

## Results used from earlier volumes

None: *Logic and Proof* is the first volume. The chapter uses the earlier chapters of this volume, listed below, and school arithmetic and the order of \( \nN \), \( \nZ \), \( \nQ \) and \( \nR \) in examples.

## Results used from earlier chapters

- Chapter 1: derivations with boxes and the scope rule (@def-derivation), and the rules of the connectives.
- Chapter 2: derived rules (@def-derived-rule).
- Chapter 3: the search method of Section 3.1, which each rule section here extends by one step.
- Chapter 4: formulas as objects (@def-formula).
- Chapter 4: structural induction (@thm-structural-induction) and structural recursion (@thm-structural-recursion).
- Chapter 4: refuting rows (@cor-refuting-row).

## Where this goes

*Sets and Functions*, Chapters 1 and 2, develop sets, membership, the empty set, pairs and functions. This chapter uses them in their everyday sense (Sections 5.1, 5.2, 5.7, 5.8). *Analysis on the Real Line*, Chapter 1, proves from the axioms of the real numbers the school facts used in examples. Among them are that \( \sqrt 2 \) exists (Sections 5.1, 5.8) and the field and order facts behind mixed chains (Section 5.7).

Before starting *Sets and Functions*, read the main text of Chapters 1–6 and 8, and read Sections 7.1–7.2 before its Section 4.1.
