# Negation, Classical Logic and Finding Derivations

Chapter 1 could prove that things are so. It could not prove that something is **not** so. No rule of Chapter 1 shows that no rational number has square \( 2 \), or that \( x^2 + 1 \) is never \( 0 \); none lets a proof by cases say "this case cannot occur" and move on; and none explains why the sentence "if \( x^2 < 0 \), then \( x = 7 \)" should count as true, when its hypothesis never holds and its conclusion has nothing to do with it. All three are questions about negation and contradiction, and ordinary proofs are full of them: "suppose not", "which is absurd", "we prove the contrapositive".

This chapter adds the rules for "not" and for contradiction one at a time, first the rules that use a negation, then the rule that proves one. It shows that a sequent, once proved, can be used as a rule of its own; gives "if and only if" its rules, and with them what a definition's "if" means; and then meets the one rule that is different in kind, proof by contradiction, together with the reason why it, double-negation elimination, and the law of excluded middle stand or fall together. It ends with a method for **finding** derivations, which collects the moves the chapter has met one section at a time, and with a question the method cannot answer: we show that something is derivable by exhibiting a derivation, but how could we ever show that something is **not** derivable? Chapter 3 answers it (@cor-refuting-row).

**What you need.** All of Chapter 1: the rules for "and", "implies", and "or", and above all the definition of a derivation, with its boxes and its scope rule (@def-derivation). School algebra about integers and real numbers is used in examples, as facts.

**Time.** About 30 hours on the core track (all of A, one B and one C per section, the exit checks); about 45 hours for everything.

## Roadmap

- **Contradiction: using a negation.** The rules \( \rulename{\neg E} \) and \( \rulename{\bot E} \): what a clash is, what it buys, why an impossible case closes itself, and why an implication with an impossible hypothesis is true.
- **Proving a negation.** The rule \( \rulename{\neg I} \), assume and reach a contradiction, and with it the proof that \( \sqrt 2 \) is irrational.
- **Derived rules.** A sequent, once proved, may be used as a single line; modus tollens, the contrapositive, and disjunctive syllogism become rules.
- **Iff, equivalence, and what a definition says.** The rules for \( \leftrightarrow \), provable equivalence, chains of equivalences, and why a definition's "if" means "if and only if".
- **Proof by contradiction and the classical rules.** The rule \( \rulename{RAA} \), the classical laws it gives (double negation, excluded middle, De Morgan, Peirce), and why three of them are one principle.
- **How to find a derivation.** The search method, assembled from the moves of the chapter, with worked searches, one search that fails, and all the rules in one place.

## Named moves

- **Goal \( \bot \): find a clash.** Look for \( \varphi \) and \( \neg\varphi \) among the available lines, or make \( \varphi \) a subgoal for some \( \neg\varphi \) you have.
- **An impossible case closes itself.** In a proof by cases, a case that reaches \( \bot \) ends by \( \rulename{\bot E} \) on the current goal.
- **To prove "not \( \varphi \)", assume \( \varphi \).** The box opens with the unnegated statement and ends on \( \bot \).
- **Use a derived rule as one line.** A proved sequent is a new rule.
- **Two boxes for an iff.** One box for each direction, each ending on the other side.
- **When stuck, assume the negation of the goal.** Proof by contradiction, and then hunt for a clash.
- **Work from both ends.** The full method: read the skeleton off the goal, use the premises by their main connectives, and keep the classical step for last.
