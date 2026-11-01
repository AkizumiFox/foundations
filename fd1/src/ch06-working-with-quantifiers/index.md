# Working with Quantifiers: Translation, Laws and Search

A first course in analysis defines "\( a_n \to L \)" with three quantifiers and two bounds such as \( \varepsilon > 0 \). Then it asks for a proof that a sequence does **not** converge, and that proof starts from the negation of the definition. Chapter 5 gave the quantifier rules one section at a time. This chapter puts them to work. It turns definitions from analysis into formulas, negates and rearranges them by laws, and finds the derivations that claims about them need.

Chapter 3 did the same work for the connectives: it turned arguments in words into derivations, sorted the tasks, and gave a method for finding derivations. This chapter does each of these again with quantifiers, where boxes carry names. It ends where Chapter 5 began, with the question why "uniformly continuous implies continuous" has a short derivation while its converse is false.

**What you need.**

- The four quantifier rules of Chapter 5, with their conditions on names (@def-rules-universal).
- Bounded quantifiers such as \( \forall \varepsilon > 0 \), from Section 5.1 (@def-bounded-quantifier).
- The search method for derivations and the four kinds of task, from Sections 3.1 and 3.2.
- Truth tables and the TAUT step, from Chapter 4 (@def-rule-taut).
- The completeness theorem of Chapter 4 (@thm-completeness).

The examples also use school arithmetic and the order of \( \nN \), \( \nZ \) and \( \nR \) as known facts.

**Time.** About 20 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 35 hours for everything.

## Roadmap

- **Translating Mathematics: Nested and Bounded Quantifiers.** Definitions from analysis written as formulas, from the outside in, with one-line rules for bounded quantifiers and five common translation errors.
- **Negating and Moving Quantifiers.** "Not every" is "some not", negation pushed inward one symbol at a time, and the laws that move a quantifier across a connective.
- **Finding First-Order Derivations.** The search method with boxes that carry names, propositional steps in one line, and the four kinds of task with quantifiers.
- **Uniformly Continuous Implies Continuous, Rule by Rule.** A full derivation of "uniformly continuous implies continuous", the lines where the converse fails, and \( x^2 \) as the function that shows it.
