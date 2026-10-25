# Connectives and Derivations

Section 1.1 opens with two arguments that every integer with an even square is even. Every claim in both is true, and yet only one is a proof. The other, Argument B, starts from "\( n \) is even", reaches "\( n^2 \) is even", and then announces the reverse. Spotting the flaw once it is pointed out is easy. Naming it, so that the same flaw can be caught in an argument we have never seen, needs an answer to a harder question: when is a list of true claims a proof? The motivating problem of this chapter is to *name exactly what is wrong with Argument B*, and the answer arrives in Section 1.4.

This chapter builds the calculus that answers it: a proof is a chain in which every line is a premise, an assumption, or one application of a rule. It gives the rules for "and", "implies" and "or", one at a time; Chapter 2 adds "not", "iff" and proof by contradiction.

**Before you start: five tempting misreadings.** Each is a misreading that this chapter corrects; decide each now, and check again when you reach the section named.

::: {.check}
1. Let \( x \) be a real number. "If \( x > 3 \), then \( x^2 > 9 \)" is false at \( x = 1 \), since \( x > 3 \) fails there.
2. Let \( n \) be an integer. "\( n \) is divisible by \( 4 \) only if \( n \) is even" says that every even number is divisible by \( 4 \).
3. In a proof that begins "Suppose \( x > 2 \)" and derives \( x^2 > 4 \), the line \( x^2 > 4 \) may be used anywhere later.
4. "\( 5 \ge 0 \)" is false, because \( 5 \ne 0 \).
5. Let \( x \) be a real number. From "\( x \ge 1 \) or \( x \le 2 \)" and "\( x \ge 1 \)" it follows that \( x \le 2 \) fails.
:::

::: {.solution}
1. No. An implication breaks only when its hypothesis holds and its conclusion fails; at \( x = 1 \) it promises nothing (Section 1.1, "When is an implication broken?").
2. No. "\( P \) only if \( Q \)" is \( P \to Q \): divisible by \( 4 \) implies even, which is true. The claim reads the converse, false at \( n = 2 \) (Section 1.1).
3. No. It holds only inside the supposition's box. Outside it, only "if \( x > 2 \), then \( x^2 > 4 \)" may be used, and \( x^2 > 4 \) fails at \( x = 0 \) (Section 1.4).
4. No. \( 5 \ge 0 \) is \( (5 > 0) \vee (5 = 0) \), and an inclusive "or" needs one true side: \( 5 > 0 \) is true (Section 1.5).
5. No. At \( x = \tfrac32 \) both sides hold. The form "from \( P \vee Q \) and \( P \), conclude not \( Q \)" is affirming a disjunct, a bad form (Sections 1.1 and 1.6).
:::

**What you need.** School algebra only: the rules of signs, adding and multiplying inequalities, and the facts that every integer is even or odd and every real number is non-negative or negative. They are used as facts in examples; *Analysis on the Real Line*, Chapter 1 proves the order facts from the axioms for the real numbers. No earlier chapter is needed.

**Time.** About 40 hours on the core track (all of A, one B and one C per section, the exit checks); about 65 hours for everything.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, core; Sections 7.1–7.2 before its Section 2.5.

## Roadmap

- **Statements, Arguments and How to Break One.** Statements and the connectives, a phrase book for the English that hides them, the promise reading of "if … then", and how to break a bad argument form by making its counterexample set true.
- **Derivations, Starting with And.** The format of a derivation, with numbered lines, premises and a justification on every line, and the first two rules of logic, \( \rulename{\wedge I} \) and \( \rulename{\wedge E} \).
- **Using an Implication: Modus Ponens.** The rule \( \rulename{{\to}E} \), and chains of implications found forwards and backwards.
- **Proving an Implication: the Rule of the Box.** The rule \( \rulename{{\to}I} \), the box and the scope rule for citing lines, and a diagnosis of exactly what Argument B did wrong.
- **Or, Introduced.** The rule \( \rulename{\vee I} \), and the habit of postponing a disjunctive goal until one side is in hand.
- **Using Or: Proof by Cases.** The rule \( \rulename{\vee E} \), the laws of "or" and the constructive dilemma, case proofs about absolute values, and the whole chapter's rule card.

## Named moves

- **Try to break it.** To test a form, put statements in for the letters that make every premise true and the conclusion false; one such choice shows the form is bad. (Section 1.1)
- **Two ways to attack an argument.** Show a premise false, or show a step's form bad; the two attacks are independent. (Section 1.1)
- **Read the skeleton off the goal.** The goal's main connective chooses the introduction rule: \( \wedge \) gives two subgoals, \( \to \) a box, \( \vee \) a choice to postpone. (Section 1.2)
- **Use a premise by its main connective.** Its elimination rule says what you may do with it: take a conjunction apart, feed an implication its hypothesis, split a disjunction into cases. (Section 1.2)
- **Open a box, close a box.** An assumption lives exactly as long as its box. (Section 1.4)
- **Work from both ends.** Premises at the top, the goal at the bottom; fill the gap from both sides. (Section 1.2)
- **Postpone a disjunction.** Choose a side of a goal \( P \vee Q \) only when that side is in hand. (Section 1.5)
- **Cases end in the current goal.** Both boxes of \( \rulename{\vee E} \) close on the statement you are trying to reach. (Section 1.6)

The chapter's eight moves are collected again at the end of Section 1.6, beside the rules that make them.

## Summary

A proof is a chain in which every line is a premise, an assumption, or one step of a rule, and checking one needs no idea. The chapter gave the six rules for "and", "implies" and "or", with repetition, and with them derived that "and" commutes and regroups (@prp-and-commutes, @prp-and-associative), that implications chain (@prp-implication-transitive), that two hypotheses may be taken at once or one at a time (@prp-curry), that "or" commutes and regroups (@exm-disjunction-first-derivations, @exm-disjunction-regroup), that "and" distributes over "or" (@prp-distributivity) and the constructive dilemma (@exm-constructive-dilemma). It named Argument B's error: a box opened at the wrong end proves the converse. A form is bad when some choice of statements makes its counterexample set true, and breaking a form is how a bad step is shown bad. Still open: the chapter has no rules for "not" or for contradiction, and the fact Argument B set out to prove waits for them. That is Chapter 2's question.

## Terms

- **argument form, good and bad**: bad if some choice of statements breaks it (@def-counterexample-set).
- **assumption, discharged**: an assumption whose box has closed (@def-rules-implication).
- **available**: citable at a line, by the scope rule (@def-derivation).
- **box**: a block of lines opened by an assumption (@def-derivation).
- **box-free derivation**: premises, then one rule step per line (@def-box-free-derivation).
- **conjunction rules** \( \rulename{\wedge I} \), \( \rulename{\wedge E} \): build from both sides; take apart (@def-rules-conjunction).
- **counterexample set**: the premises together with the negated conclusion (@def-counterexample-set).
- **derivable**, \( \Gamma \vdash \psi \): some derivation from premises in \( \Gamma \) ends with \( \psi \) (@def-derivable).
- **derivation**: each line a premise, assumption, repetition or rule step (@def-derivation).
- **disjunction rules** \( \rulename{\vee I} \), \( \rulename{\vee E} \), **proof by cases**: weaken to a disjunction; split one into cases (@def-rules-disjunction).
- **implication rules** \( \rulename{{\to}I} \), \( \rulename{{\to}E} \): prove by a box; use by modus ponens (@def-rules-implication).
- **main connective**: the connective applied last in building a statement (@def-main-connective).
- **modus ponens**: from \( \varphi \to \psi \) and \( \varphi \), conclude \( \psi \) (@def-rule-implication-elimination).
- **or-introduction**: from one side, conclude the disjunction (@def-rule-disjunction-introduction).
- **repetition** \( \rulename{R} \): copy the statement of an available line (@def-derivation).
- **rule schema**: given lines above, one new line below (@def-rule-schema).
- **sequent**, turnstile: \( P_1, \dots, P_n \vdash Q \), the claim that \( Q \) is derivable (@def-sequent).
- **statement**: a declarative sentence, either true or false (@def-statement).
