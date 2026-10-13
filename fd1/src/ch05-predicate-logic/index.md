# Predicate Logic and the Quantifier Rules

"\( x^2 \ge 0 \) for every real \( x \)." "There is no largest prime." "For every \( \varepsilon > 0 \) there is an \( N \) such that \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N \)." The statements of analysis are made of the words "for every" and "there exists", and Chapters 1–4 cannot see them: to a truth table, each of these sentences is a single atom, and the argument "every positive real has a square root; \( 2 \) is positive; so \( 2 \) has a square root" has the invalid form \( p, q \therefore r \). This chapter adds the missing grammar (predicates, terms, and the two quantifiers) and then, exactly as Chapters 1 and 2 did for the connectives, gives the rules **one per section**: how to use a "for every", how to prove one, how to prove a "there exists", how to use one, and the rules for equality. Each quantifier rule comes with a side condition about names, and the side conditions turn out to be exactly the rules that analysts break when a \( \delta \) secretly depends on an \( x \), or when a witness is treated as if it were arbitrary.

The motivating problem is this. A function \( f \) is continuous when for every \( x \) and every \( \varepsilon > 0 \) there is a \( \delta > 0 \) that works; it is uniformly continuous when for every \( \varepsilon > 0 \) there is a \( \delta > 0 \) that works for every \( x \). The two definitions differ only in the order of two quantifiers. *Why does "uniformly continuous implies continuous" have a proof a few lines long, while its converse is false?* The answer is a fact about the order in which names are introduced in a derivation, and Section 6.4 reads it off rule by rule. Along the way the chapter translates mathematical definitions into formulas, negates them quantifier by quantifier, gives formulas a meaning in **models**, and uses models to show that some searches for a derivation must fail. The last section, which is optional, proves that the extended rules are sound.

**What you need.** Chapters 1–4. From Chapters 1 and 2: the rules for every connective, the definition of a derivation with its boxes and its scope rule (@def-derivation), derived rules (@def-derived-rule), and the classical rules of Section 2.5. From Chapter 3: the search method of Section 3.1, which each rule section here extends by one step. From Chapter 4: formulas as objects (@def-formula), structural induction and recursion (@thm-structural-induction, @thm-structural-recursion), truth tables, and soundness with its refuting rows (@thm-soundness, @cor-refuting-row). School arithmetic and the order of \( \nN \), \( \nZ \), \( \nQ \), and \( \nR \) are used in examples as facts.

**Time.** About 70 hours on the core track (all of A, one B, and one C per section, the exit checks); about 90 hours for everything.

## Roadmap

- **Predicates and quantifiers.** Predicates, variables, and the domain; how to read "for every" and "there exists", bounded quantifiers, and why the order of two quantifiers can change everything.
- **Terms, formulas, free variables, and substitution.** The exact language, which letters are still holes, the operation "put \( t \) in for \( x \)" that every rule uses, and the one way it goes wrong: capture.
- **Using "for every": instantiation.** The rule \( \rulename{\forall E} \): a universal statement may be applied to any term, and the term is read off the goal.
- **Proving "for every": let \( x \) be arbitrary.** The rule \( \rulename{\forall I} \) and the flagged box: prove the statement for a fresh name about which nothing is assumed.
- **Proving "there exists": exhibit a witness.** The rule \( \rulename{\exists I} \), and why the witness is chosen only when an available line shows it.
- **Using "there exists": name a witness.** The rule \( \rulename{\exists E} \), its box, and its fresh-name condition, and the first derivation that moves an \( \exists \) past a \( \forall \) (and where the reverse move breaks down).
- **Equality and unique existence.** The rules \( \rulename{=I} \) and \( \rulename{=E} \), calculation chains, "there is exactly one", and the completed table of rules, phrases, and proof-assistant commands.

## Named moves

- **Instantiate at the term you need** (\( \rulename{\forall E} \)): read the term off the goal, not off the order of the premises.
- **Let \( x \) be arbitrary** (\( \rulename{\forall I} \)): a fresh name, about which nothing is assumed.
- **Postpone the witness** (\( \rulename{\exists I} \)): choose the term only when an available line shows it.
- **Name the witness early** (\( \rulename{\exists E} \)): "choose \( x_0 \) with …", open the box at once, and never generalize over it.
- **Fix, obtain, choose:** \( \rulename{\forall I} \), then \( \rulename{\forall E} \) and \( \rulename{\exists E} \) on the hypothesis, then \( \rulename{\exists I} \) with a term built from what is available. The shape of most proofs in analysis.
