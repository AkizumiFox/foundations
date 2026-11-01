# Chapter Review

## Summary

A proof is a chain in which every line is a premise, an assumption, or one step of a rule, and checking one needs no idea. The chapter gave six rules, two each for "and", "implies" and "or", together with repetition. With them it derived the following:

- "and" commutes and regroups (@prp-and-commutes, @prp-and-associative);
- implications chain (@prp-implication-transitive);
- two hypotheses may be taken at once or one at a time (@prp-curry);
- "or" commutes and regroups (@exm-disjunction-first-derivations, @exm-disjunction-regroup);
- "and" distributes over "or" (@prp-distributivity);
- from "\( P \) or \( Q \)", "\( P \) implies \( R \)" and "\( Q \) implies \( S \)" follows "\( R \) or \( S \)", the constructive dilemma (@exm-constructive-dilemma).

It named Argument B's error: a box opened at the wrong end proves the converse. A form is bad when some choice of statements makes its counterexample set true. Breaking a form in this way is how a bad step is shown to be bad.

Still open: the chapter has no rules for "not" or for contradiction, and the fact Argument B set out to prove waits for them. That is Chapter 2's question.

## Proof methods in this chapter

Section 1.6 lists the same methods beside the rules that carry them out.

- **Try to break it.** To test a form, put statements in for the letters that make every premise true and the conclusion false. One such choice shows that the form is bad. (Section 1.1)
- **Two ways to attack an argument.** Show a premise false, or show that a step's form is bad. Either attack works without the other. (Section 1.1)
- **Read the skeleton off the goal.** The goal's main connective chooses the introduction rule: \( \wedge \) gives two subgoals, \( \to \) a box, \( \vee \) a choice to postpone. (Section 1.2)
- **Use a premise by its main connective.** Its elimination rule says what you may do with it: take a conjunction apart, feed an implication its hypothesis, split a disjunction into cases. (Section 1.2)
- **Work from both ends.** Premises at the top, the goal at the bottom; fill the gap from both sides. (Section 1.2)
- **Open a box, close a box.** An assumption may be used exactly as long as its box is open. (Section 1.4)
- **Postpone a disjunction.** Choose a side of a goal \( P \vee Q \) only when that side is in hand. (Section 1.5)
- **Cases end in the current goal.** Both boxes of \( \rulename{\vee E} \) close on the statement you are trying to reach. (Section 1.6)

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

## Results used from earlier volumes

None: this is the first volume. Examples use school algebra as facts: the rules of signs, adding and multiplying inequalities, and that every integer is even or odd.

## Five tempting misreadings

Each claim below is a misreading that this chapter corrects. Decide whether each one is right, then check the answer.

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

## What comes next

Chapter 2 gives the rules for "not", for "if and only if" and for proof by contradiction.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, the main text with every A exercise and one B and one C exercise per section; Sections 7.1–7.2 before its Section 4.1.
