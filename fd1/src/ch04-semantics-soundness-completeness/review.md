# Chapter Review

## Summary

Formulas are strings built by the clauses of @def-formula. Each formula is read in only one way (@thm-unique-readability), so a function on formulas can be defined by one clause per connective. Induction, on the numbers and on formulas, proves statements about all of them. Two habits make it work: the checklist of Section 4.2, and strengthening the claim until the step goes through. A valuation gives every formula a truth value, and entailment, *satisfiable*, *contingent* and the relations between pairs of formulas are all defined from rows. Every such question reduces to whether some list of formulas is unsatisfiable, and a search tree decides it (@prp-search-decides).

Soundness (@thm-soundness) says that a refuting row rules out every derivation. Completeness (@thm-completeness) says that every valid sequent has a derivation. So \( \vdash \) and \( \models \) coincide, *consistent* and *satisfiable* coincide, and a finite table decides whether a derivation exists. TAUT records a truth-table step as one line.

All of this is proved for propositional formulas and finitely many premises, and for infinitely many premises in the optional Section 4.10. What is open is the inside of an atom. "For every \( \varepsilon > 0 \) there is an \( N \)" is one letter to a truth table, and how to reason inside it is the question of Chapter 5. Two more questions stay open: which tautologies need reductio, of which the optional @thm-raa-independent settles two, and how short a derivation can be.

## Proof methods in this chapter

- **Induction on the shape of a formula.** Prove the claim for atoms and \( \bot \), then for each connective from its parts. Section 4.3.
- **Check the induction.** Name the objects, the property, the base cases, the steps and the principle used. Section 4.2.
- **Prove more to prove less.** Strengthen the claim until the step goes through. Sections 4.2 and 4.3.
- **Define by recursion on formulas.** Give one clause for each way of building a formula. Section 4.3.
- **Work backwards from F.** Assume the formula false and follow what is forced. Section 4.4.
- **Reduce to unsatisfiability.** Turn every question about rows into the question whether some list of formulas is unsatisfiable. Section 4.5.
- **Search for a refuting row.** Make the forced choices first, split only when nothing is forced, and close branches early. Section 4.6.
- **Refute with one row.** One refuting row proves \( \Gamma \nvdash \psi \), by soundness. Section 4.7.
- **Test the subgoal.** Before working towards a subgoal, look for a row that refutes it. Section 4.7.
- **Induction on the lines of a derivation.** Show that every rule keeps the property. Section 4.7.
- **Split on an atom.** With \( p \vee \neg p \) and \( \rulename{\vee E} \), prove the goal once assuming \( p \) and once assuming \( \neg p \). Section 4.8.

## Terms

- **adequate set of connectives**: expresses every truth function (@def-adequate).
- **atom**: one letter such as \( p, q, p_1 \), a formula on its own (@def-formula).
- **conjunctive normal form**: an "and" of "or"s of literals (@def-cnf).
- **contingent formula**: true in some row and false in another (@def-tautology).
- **contradiction**: a formula false in every row (@def-tautology).
- **contradictory, contrary, subcontrary**: exactly one of the two is true, the two are never both true, the two are never both false (@def-pair-relations).
- **disjunctive normal form**: an "or" of "and"s of literals (@def-dnf).
- **entailment**, \( \Gamma \models \psi \): there is no refuting row (@def-valid-argument).
- **formula**: a string built from atoms and \( \bot \) by the connectives (@def-formula).
- **height**: the number of nodes on a longest branch of the parse tree (@def-height).
- **induction**: from \( P(0) \) and each step from \( P(n) \) to \( P(n+1) \), conclude \( P(n) \) for every \( n \) (@ax-induction).
- **literal**: an atom or the negation of an atom (@def-literal).
- **parse tree**: the tree showing how a formula is built (@def-parse-tree).
- **positive, negative occurrence**: the sign of a part of a formula, flipped by \( \neg \) and by the hypothesis of an implication (@def-occurrence-polarity).
- **premises, infinitely many**: \( \vdash \) and \( \models \) for a collection of premises (@def-infinite-entailment).
- **refuting row**: a row where the premises are true and the conclusion is false (@def-valid-argument).
- **satisfiable**: some row makes every member true (@def-satisfiable).
- **search tree**: the search for a refuting row, drawn as a tree (@def-search-tree).
- **semantic equivalence**, \( \equiv \): the same value in every row (@def-semantic-equivalence).
- **subformula**: a formula met while building another (@def-subformula).
- **TAUT**: one line that records a truth-table step (@def-rule-taut).
- **tautology**: a formula true in every row (@def-tautology).
- **truth function**: a truth value for each list of truth values (@def-truth-function).
- **truth table**: a formula's value in each of the \( 2^n \) rows (@def-truth-table).
- **truth value**: T or F, computed from the atoms (@def-truth-value).
- **valuation**: a choice of T or F for each atom (@def-valuation).

## Results used from earlier volumes

None. *Logic and Proof* is the first volume, and this chapter uses only Chapters 1–3 and the arithmetic of the natural numbers from school.

## Threads

- **Inside the atoms.** Chapter 5 gives "every" and "some" their rules and their meaning.
- **Reductio.** Chapter 8 says what reductio asserts that the other rules do not, and who objected to it.
- **Models.** Chapter 7 gives the formulas of predicate logic structures in place of rows. It shows a theory consistent, and an axiom independent, by exhibiting a model (Section 7.4). It asks which sets a formula can define (Section 7.5), and it states completeness and compactness for predicate logic in the optional Section 7.6.
- **Later volumes.** *Sets and Functions*, Chapter 1 makes exact "the smallest collection of strings closed under the building steps", and the word "function". Its Chapter 2 proves induction equivalent to the well-ordering principle, and shows a famous false induction that breaks at its first step. *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 1 derives induction from the axioms of set theory. *Analysis on the Real Line*, Chapter 1 takes the least upper bound axiom as given, as this chapter takes induction.
- **Before *Sets and Functions*.** The least to read first is the main line of Chapters 1–6 and 8, and Sections 7.1–7.2 before Section 4.1 of *Sets and Functions*.
