# Connectives and Derivations

Section 1.1 opens with two arguments that every integer with an even square is even. Every sentence in both is true, and yet only one is a proof. The other, Argument B, starts from "\( n \) is even", reaches "\( n^2 \) is even", and then announces the reverse. Spotting the flaw once it is pointed out is easy. Naming it, so that the same flaw can be caught in an argument we have never seen, needs an answer to a harder question: when is a list of true sentences a proof? The motivating problem of this chapter is to *name exactly what is wrong with Argument B*, and the answer arrives in Section 1.5.

This chapter and the next build the **calculus** that answers the question. A proof is a chain in which every line is a premise, an assumption, or one application of a rule. We first learn to read such chains, with no logic in them at all, and then learn the rules one at a time, for "and", "implies", and "or", each defined by a small pattern of lines and practiced in many short derivations and in proofs about numbers. Chapter 2 does the same for "not", "iff", and proof by contradiction, and shows how to *find* derivations systematically; Chapter 3 asks whether the rules are right (@thm-soundness, @thm-completeness); Chapter 4 adds "for every" and "there exists"; Chapter 5 turns derivations back into the prose mathematicians write.

**What you need.** School algebra only: the rules of signs, adding and multiplying inequalities, and the facts that every integer is even or odd and every real number is nonnegative or negative. They are used as facts in examples; Chapter 11 proves the order facts from the axioms for the real numbers. No earlier chapter is needed.

**Time.** About 35 hours on the core track (all of A, one B and one C per section, the exit checks); about 50 hours for everything.

## Roadmap

- **Statements and connectives.** The language: what a statement is, the five connectives and the constant \( \bot \), the main connective of a statement, and the sequent as a claim about the form of an argument.
- **Derivations.** The format of a derivation, with no logic yet: numbered lines, premises, a justification on every line, and rule schemas, practiced on two borrowed facts about inequalities.
- **Conjunction.** The first two rules of logic, \( \rulename{\wedge I} \) and \( \rulename{\wedge E} \), and the two directions of reasoning: from the goal backwards and from the premises forwards.
- **Using an implication.** The rule \( \rulename{{\to}E} \), modus ponens, and chains of implications found forwards and backwards; why its converse pattern is not a rule.
- **Proving an implication.** The rule \( \rulename{{\to}I} \) and the box: assumptions, their scope, repetition, and the full definition of a derivation.
- **Or, introduced.** The rule \( \rulename{\vee I} \), which loses information but never truth, and the habit of postponing a disjunctive goal.
- **Using or: proof by cases.** The rule \( \rulename{\vee E} \), two boxes ending in the same line, the laws of "or", and case proofs about absolute values.

## Named moves

- **Read the skeleton off the goal.** The goal's main connective chooses the introduction rule: \( \wedge \) gives two subgoals, \( \to \) a box, \( \vee \) a choice to postpone.
- **Use a premise by its main connective.** Its elimination rule says what you may do with it: take a conjunction apart, feed an implication its hypothesis, split a disjunction into cases.
- **Open a box, close a box.** An assumption lives exactly as long as its box.
- **Work from both ends.** Premises at the top, the goal at the bottom; fill the gap from both sides.
- **Postpone a disjunction.** Choose a side of a goal \( P \vee Q \) only when that side is in hand.
- **Cases end in the current goal.** Both boxes of \( \rulename{\vee E} \) close on the statement you are trying to reach.
