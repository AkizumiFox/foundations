# Predicate Logic and the Quantifier Rules

*Every lock in this building has a key that opens it.* *Some key opens every lock in this building.* The two sentences use the same words, but the second says far more: it promises a master key. The statements of analysis are built from "for every" and "there exists", and a truth table cannot see inside them. To a truth table, the argument "every positive real has a square root; \( 2 \) is positive; so \( 2 \) has a square root" has the form \( p, q \therefore r \). A refuting row breaks it, although the argument is plainly correct.

This chapter looks inside such statements. It gives "for every" and "there exists" their rules, one rule per section, as Chapters 1 and 2 did for the connectives, and it adds two rules for the equals sign. Each new rule comes with a condition on the names it may use. These conditions are exactly what an analyst breaks when a \( \delta \) quietly depends on an \( x \). Continuity and uniform continuity, two notions of analysis, differ only in the order of a "for every" and a "there exists". *Why does "uniformly continuous implies continuous" have a proof a few lines long, while its converse is false?* Chapter 6 reads the answer off the rules.

**What you need.**

- The rules for the connectives, derivations with boxes and derived rules, from Chapters 1 and 2 (@def-derivation).
- The search method for derivations, from Chapter 3, Section 3.1.
- Formulas as objects, and structural induction and recursion, from Chapter 4 (@thm-structural-induction).
- Refuting rows, from Chapter 4 (@cor-refuting-row).
- School arithmetic and the order of \( \nN \), \( \nZ \), \( \nQ \) and \( \nR \), used in examples as facts.

**Time.** About 45 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 65 hours for everything.

Every section is meant for a first reading. Some passages are shown closed, under a title. They hold proofs about the language, longer analyses of errors and edge cases. You may leave them closed at first, but later proofs may use them.

## Roadmap

- **Predicates and Quantifiers.** How to read "for every" and "there exists", in a small pictured world and over numbers, and why their order matters.
- **Terms, Formulas, Free Variables and Substitution.** The exact language, and how to put a term in for a letter without changing what the other letters mean.
- **Using "For Every": Instantiation.** The rule \( \rulename{\forall E} \): from a statement about every object, conclude it for the object the goal needs.
- **Proving "For Every": Let x Be Arbitrary.** The rule \( \rulename{\forall I} \): prove the statement for a new name about which nothing is assumed.
- **Proving "There Exists": Exhibit a Witness.** The rule \( \rulename{\exists I} \): name an object with the property, chosen once a line of the derivation shows it.
- **Using "There Exists": Name a Witness.** The rule \( \rulename{\exists E} \): give the promised object a new name, and never treat it as arbitrary.
- **Equality.** Two rules for the equals sign, chains of equations, the fact that equal objects share every property, and the table of all the rules.
- **Unique Existence, Counting and Descriptions.** "Exactly one", "at least two", "the \( x \) such that", and why a definition proves nothing new.
