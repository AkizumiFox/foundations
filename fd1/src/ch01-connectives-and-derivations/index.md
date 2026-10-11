# Connectives and Derivations

Section 1.1 opens with two arguments that every integer with an even square is even. Every sentence in both is true, and yet only one is a proof. The other, Argument B, starts from "\( n \) is even", reaches "\( n^2 \) is even", and then announces the reverse. Spotting the flaw once it is pointed out is easy. Naming it, so that the same flaw can be caught in an argument we have never seen, needs an answer to a harder question: when is a list of true sentences a proof? The motivating problem of this chapter is to *name exactly what is wrong with Argument B*, and the answer arrives in Section 1.4.

This chapter builds the calculus that answers it: a proof is a chain in which every line is a premise, an assumption, or one application of a rule. It gives the rules for "and", "implies" and "or", one at a time; Chapter 2 adds "not", "iff" and proof by contradiction.

**What you need.** School algebra only: the rules of signs, adding and multiplying inequalities, and the facts that every integer is even or odd and every real number is non-negative or negative. They are used as facts in examples; *Analysis on the Real Line*, Chapter 1 proves the order facts from the axioms for the real numbers. No earlier chapter is needed.

**Time.** About 35 hours on the core track (all of A, one B and one C per section, the exit checks); about 50 hours for everything.

## Roadmap

- **Statements, Arguments and How to Break One.** Statements and the connectives, the promise reading of "if … then", and how to show that an argument form is bad by breaking it.
- **Derivations, Starting with And.** The format of a derivation, with numbered lines, premises and a justification on every line, and the first two rules of logic, \( \rulename{\wedge I} \) and \( \rulename{\wedge E} \).
- **Using an Implication: Modus Ponens.** The rule \( \rulename{{\to}E} \), and chains of implications found forwards and backwards.
- **Proving an Implication: the Rule of the Box.** The rule \( \rulename{{\to}I} \), the box and the scope rule for citing lines, and a diagnosis of exactly what Argument B did wrong.
- **Or, Introduced.** The rule \( \rulename{\vee I} \), and the habit of postponing a disjunctive goal until one side is in hand.
- **Using Or: Proof by Cases.** The rule \( \rulename{\vee E} \), the laws of "or", case proofs about absolute values, and the whole chapter's rule card.

## Named moves

- **Try to break it.** To test a form, put statements in for the letters that make every premise true and the conclusion false; one such choice shows the form is bad. (Section 1.1)
- **Read the skeleton off the goal.** The goal's main connective chooses the introduction rule: \( \wedge \) gives two subgoals, \( \to \) a box, \( \vee \) a choice to postpone. (Section 1.2)
- **Use a premise by its main connective.** Its elimination rule says what you may do with it: take a conjunction apart, feed an implication its hypothesis, split a disjunction into cases. (Section 1.2)
- **Open a box, close a box.** An assumption lives exactly as long as its box. (Section 1.4)
- **Work from both ends.** Premises at the top, the goal at the bottom; fill the gap from both sides. (Section 1.2)
- **Postpone a disjunction.** Choose a side of a goal \( P \vee Q \) only when that side is in hand. (Section 1.5)
- **Cases end in the current goal.** Both boxes of \( \rulename{\vee E} \) close on the statement you are trying to reach. (Section 1.6)

The chapter's seven moves are collected again at the end of Section 1.6, beside the rules that make them.
