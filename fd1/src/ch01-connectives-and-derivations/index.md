# Connectives and Derivations

Section 1.1 opens with two arguments that every integer with an even square is even. Every claim in both is true, and yet only one of them is a proof. The other starts from "\( n \) is even", reaches "\( n^2 \) is even", and then announces the reverse. Once the flaw is pointed out, it is easy to see. To catch the same flaw in an argument we have never seen, we need an answer to a harder question: when is a list of true claims a proof?

This chapter answers that question. A proof is a chain of lines. Each line is a claim we were given, a temporary supposition, or one application of a rule. The chapter gives the rules for "and", "if … then" and "or", one word at a time. In Section 1.4 the rules can say exactly what went wrong in the second argument. Chapter 2 adds the rules for "not", for "if and only if" and for proof by contradiction.

**What you need.** Nothing from an earlier chapter, and only school algebra:

- the rules of signs;
- adding and multiplying inequalities;
- every integer is even or odd;
- every real number is non-negative or negative.

Examples use these as facts. A later volume, *Analysis on the Real Line*, proves the facts about order from the axioms for the real numbers.

**Time.** About 40 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 65 hours for everything.

## Roadmap

- **Statements, Arguments and How to Break One.** Statements, and the words "not", "and", "or" and "if … then" that build new statements from old ones. How everyday English hides these words, and how to show that a pattern of argument is bad: find statements that make its starting claims true and its conclusion false.
- **Derivations, Starting with And.** How a proof is written as numbered lines, each with its reason, and the two rules for "and": one builds "\( P \) and \( Q \)", the other takes it apart.
- **Using an Implication: Modus Ponens.** The rule that uses "if \( P \), then \( Q \)": from it and \( P \), conclude \( Q \). Chains of such steps, found forwards from the given claims and backwards from the goal.
- **Proving an Implication: the Rule of the Box.** How to prove "if \( P \), then \( Q \)": suppose \( P \) in a marked-off block of lines, reach \( Q \), and close the block. Which lines may be used where, and exactly what the second argument did wrong.
- **Or, Introduced.** How to prove "\( P \) or \( Q \)" from one of its sides, and why it pays to wait until one side is in hand.
- **Using Or: Proof by Cases.** How to use "\( P \) or \( Q \)": reach the goal once in each case. The laws of "or", proofs about absolute values by cases, and all the rules of the chapter on one page.
