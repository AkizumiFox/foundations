# Truth, Soundness and Completeness

Chapters 1 and 2 built a calculus of derivations, and with it we can show that a sequent holds: write a derivation. What we cannot yet do is show that a sequent does **not** hold. Section 2.6 searched for a derivation of \( P \to Q \vdash Q \to P \), and every route stalled; but a search that fails proves nothing, since a cleverer derivation might exist somewhere. The motivating problem of this chapter is to *prove that no derivation of \( q \to p \) from \( p \to q \) exists*, however long and however clever.

The answer is to give formulas a **meaning**. A valuation makes each atom true or false, a truth table computes the value of every formula from its atoms, and \( \Gamma \models \psi \) says that every valuation making the premises true makes the conclusion true. Two theorems then tie meaning to derivation. **Soundness**: whatever can be derived is true in every row where the premises are true; so a single row with true premises and a false conclusion proves that no derivation exists. **Completeness**: whatever is true in every such row can be derived; so the rules of Chapters 1 and 2 are enough. To state and prove these theorems we first make formulas into mathematical objects, and we meet **induction**, on the natural numbers and on the shape of a formula, because both theorems are proved by it. These are the book's first proofs about proofs, and its first long proofs. The chapter ends with normal forms, the constructive content of completeness.

**What you need.** Chapters 1 and 2: the rules for every connective, the definition of a derivation with its boxes and its scope rule (@def-derivation), derived rules (@def-derived-rule), and the classical rules of Section 2.5, above all the law of excluded middle (@prp-excluded-middle). The arithmetic and order of the natural numbers are used as school facts.

**Time.** About 40 hours on the core track (all of A, one B and one C per section, the exit checks); about 55 hours for everything.

## Roadmap

- **Formulas as objects.** The exact definition of a formula, parse trees, subformulas and height, the shorthand of Chapter 1 as a translation, and why a derivation stays a derivation when formulas are put in for its atoms.
- **Induction on numbers and on formulas.** The principle of induction, strong induction, and structural induction, and with them the proofs that every formula is read in only one way and that a definition by one clause per connective defines exactly one thing.
- **Valuations and truth tables.** Truth values for atoms, the value of every formula computed along its parse tree, and why a table with \( 2^n \) rows tells everything about a formula with \( n \) atoms.
- **Tautologies, entailment, and equivalence.** The semantic counterpart \( \Gamma \models \psi \) of a sequent, tautologies and satisfiability, the standard equivalences, and what may be replaced or substituted without changing truth.
- **Soundness.** The rules never lead from truth to falsehood, proved by induction on the lines of a derivation; so one refuting row shows that a sequent has no derivation.
- **Completeness.** Every truth-table consequence of finitely many premises has a derivation: the rules prove their own truth tables, one row at a time, and excluded middle glues the rows together.
- **Normal forms and adequate connectives.** Every formula is equivalent to one in disjunctive and in conjunctive normal form; validity read off a conjunctive normal form; which sets of connectives can express everything.

## Named moves

- **Induction on the shape of a formula.** Prove it for atoms and \( \bot \); prove it for each connective, assuming it for the parts.
- **Define by recursion on formulas.** One clause per way of building a formula; unique readability makes the definition well defined.
- **Refute with one row.** A valuation making every premise true and the conclusion false proves \( \Gamma \nvdash \psi \), by soundness.
- **Induction on the lines of a derivation.** To prove that every derivable sequent has a property, show that every rule preserves it.
- **Split on an atom.** With \( p \vee \neg p \) and \( \rulename{\vee E} \), prove the goal once assuming \( p \) and once assuming \( \neg p \).
