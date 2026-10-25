# Predicate Logic and the Quantifier Rules

*Every lock in this building has a key that opens it.* *Some key opens every lock in this building.* The two sentences use the same words, and the second says far more: it promises a master key. The statements of analysis are made of "for every" and "there exists", and to a truth table each is a single atom: the argument "every positive real has a square root; \( 2 \) is positive; so \( 2 \) has a square root" has the form \( p, q \therefore r \), which a refuting row breaks. This chapter opens the atoms: predicates, terms and the two quantifiers, then their rules and those of equality. Each quantifier rule has a side condition about names, and the side conditions are exactly the rules an analyst breaks when a \( \delta \) secretly depends on an \( x \); continuity and uniform continuity differ only in the order of two quantifiers. *Why does "uniformly continuous implies continuous" have a proof a few lines long, while its converse is false?* Chapter 6 reads the answer off the rules.

The chapter is the first-order twin of Chapters 1 and 2: one rule per section, each with its card, its gallery of instances and its "Not allowed" block.

**What you need.** Chapters 1–4. From Chapters 1–3: the rules of every connective, derivations with boxes and the scope rule (@def-derivation), derived rules (@def-derived-rule), and the search method of Section 3.1, which each rule section here extends by one step. From Chapter 4: formulas as objects (@def-formula), structural induction and recursion (@thm-structural-induction, @thm-structural-recursion), and refuting rows (@cor-refuting-row). School arithmetic and the order of \( \nN \), \( \nZ \), \( \nQ \), \( \nR \) are used in examples as facts.

**Time.** About 45 hours on the core track (all of A, one B and one C per section); about 65 hours for everything.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, core; Sections 7.1–7.2 before its Section 4.1.

**How to read this chapter.** Every section is on the first reading, with its folds closed. The folds hold proofs about the language (substitution, renaming, definitions), longer error analyses and edge cases. They are not optional: later proofs may use them.

## Roadmap

- **Predicates and Quantifiers.** "For every" and "there exists" in a pictured world and over numbers; bounded quantifiers; the order of quantifiers.
- **Terms, Formulas, Free Variables and Substitution.** The exact language, free and bound letters, substitution, and capture.
- **Using "For Every": Instantiation.** \( \rulename{\forall E} \) at the term the goal needs; counter-readings.
- **Proving "For Every": Let x Be Arbitrary.** \( \rulename{\forall I} \) and the flagged box: a fresh name, nothing assumed about it.
- **Proving "There Exists": Exhibit a Witness.** \( \rulename{\exists I} \), with the witness chosen when a line shows it.
- **Using "There Exists": Name a Witness.** \( \rulename{\exists E} \) and its box; moving \( \exists \) past \( \forall \); the barber.
- **Equality.** \( \rulename{{=}I} \) and \( \rulename{{=}E} \), chains, Leibniz's Law, and the table of the whole calculus.
- **Unique Existence, Counting and Descriptions.** "Exactly one", counting with \( \ne \), "the \( x \) such that", graphs of functions, and why a definition proves nothing new.

## Named moves

- **Read the dependency off the order.** A variable depends only on those quantified to its left. (Section 5.1)
- **Instantiate at the term you need** (\( \rulename{\forall E} \)). Read it off the goal. (Section 5.3)
- **Break it with a counter-reading.** Premises true, the line false. (Section 5.3)
- **Let \( x \) be arbitrary** (\( \rulename{\forall I} \)). A fresh name, about which nothing is assumed. (Section 5.4)
- **Postpone the witness** (\( \rulename{\exists I} \)). Choose the term when a line shows it. (Section 5.5)
- **Name the witness early** (\( \rulename{\exists E} \)). "Choose \( x_0 \) with …", and never generalize over it. (Section 5.6)
- **Fix, obtain, choose.** \( \rulename{\forall I} \); \( \rulename{\forall E} \), \( \rulename{\exists E} \) on the hypotheses; \( \rulename{\exists I} \). Most proofs in analysis. (Section 5.6)
- **Existence and uniqueness, separately.** Prove "at least one" and "at most one" apart. (Section 5.8)

The four quantifier rules are on one card at the end of Section 5.6, and the whole calculus on the table at the end of Section 5.7.

**Where this goes.** *Sets and Functions*, Chapters 1 and 2 develop sets, membership, the empty set, pairs and functions, used here in their everyday sense (Sections 5.1, 5.2, 5.7, 5.8). *Analysis on the Real Line*, Chapter 1 proves from the axioms of the real numbers the school facts used in examples: that \( \sqrt 2 \) exists (Sections 5.1, 5.8) and the field and order facts behind mixed chains (Section 5.7).

## Summary

The language and its substitution are exact, capture included. Each quantifier rule has a side condition about names: \( \rulename{\forall E} \) at a term free for the variable, \( \rulename{\forall I} \) over a fresh flag, \( \rulename{\exists I} \) at a witness a line shows, \( \rulename{\exists E} \) with a fresh name kept in its box. With them and the two rules for equality, \( \exists x\, \forall y \) gives \( \forall y\, \exists x \) and a counter-reading breaks the converse, equals share every property (@prp-leibniz-law), no relation has the barber's property (@thm-barber), and a definition proves nothing new about the old words (@prp-definitional-extension).

What is open: a stalled search shows nothing, and the counter-readings are not yet certified (Chapter 7). The definitions of analysis, four quantifiers deep, are still to be translated, negated and derived (Chapter 6).

## Terms

- **bounded quantifier**: \( \forall x \in A \), \( \exists x \in A \) (@def-bounded-quantifier).
- **counter-reading**: premises true, the line false ([Section 5.3](#counter-readings)).
- **counting with equality**: at least, at most, exactly \( n \) (@def-counting-with-equality).
- **definite description**: "the \( x \) such that \( \varphi \)" (@def-definite-description).
- **definitional extension**: a new symbol, nothing new proved (@prp-definitional-extension).
- **equality rules** \( \rulename{{=}I} \), \( \rulename{{=}E} \): \( t = t \); replace equals (@def-rules-equality).
- **existential elimination** \( \rulename{\exists E} \): name a witness, freshly (@def-rules-existential).
- **existential introduction** \( \rulename{\exists I} \): from an instance (@def-rule-existential-introduction).
- **flag, flagged box**: the fresh name of \( \rulename{\forall I} \) (@def-rules-universal).
- **formula**, first-order: connectives and quantifiers over atoms (@def-first-order-formula).
- **free for**: substituting captures no variable (@def-free-for).
- **free variable**: a letter no quantifier binds (@def-free-variable).
- **Leibniz's Law**: equals share every property (@prp-leibniz-law).
- **sentence**: no free variable (@def-sentence).
- **substitution** \( \varphi[t/x] \): \( t \) for free \( x \) (@def-substitution).
- **term**: a name for an object (@def-term).
- **unique existence** \( \exists! \): at least and at most one (@def-unique-existence).
- **universal elimination** \( \rulename{\forall E} \): any instance (@def-rule-universal-elimination).
