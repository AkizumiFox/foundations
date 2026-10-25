# Truth, Soundness and Completeness

Chapter 3 ended on a question: we show that something is derivable by exhibiting a derivation, but how could we ever show that something is **not** derivable? Section 3.1 searched for a derivation of \( P \to Q \vdash Q \to P \), and every route stalled. A search that fails proves nothing: a cleverer derivation might exist. Here is something that does prove it.

| \( p \) | \( q \) | \( p \to q \) | \( q \to p \) | |
|---|---|---|---|---|
| T | T | T | T | |
| T | F | F | T | |
| **F** | **T** | **T** | **F** | **this row** |
| F | F | T | T | |

In the third row the premise \( p \to q \) (Section 4.1 says why the letters are now lower-case) is true, because its hypothesis is false (the promise reading of Section 1.1), and the conclusion \( q \to p \) is false. By the end of this chapter this one row is a **proof** that no derivation of \( q \to p \) from \( p \to q \) exists, however long.

The answer is to give formulas a **meaning**. **Soundness** says that whatever can be derived is true in every row where the premises are true; so one such row with a false conclusion proves that no derivation exists. **Completeness** says that whatever is true in every such row can be derived. To prove them, formulas become objects and **induction** arrives. Between the two theorems sits a search (Section 4.6) that, for any finite list of premises and any conclusion, finds a refuting row or shows that there is none. The core ends with completeness; normal forms, the constructive content of completeness (second pass), and compactness (optional) follow.

**What you need.** Chapters 1–3: the rules for every connective, the definition of a derivation with its boxes and its scope rule (@def-derivation), derived rules and @lem-weakening-cut (Section 2.3), the classical rules of Section 2.5, above all @prp-excluded-middle, the search method of Section 3.1, and the four kinds of task of Section 3.2 with its word *consistent* (@def-inconsistent-set). The arithmetic and order of the natural numbers are school facts.

**Time.** About 45 hours on the core track (Sections 4.1–4.8: all of A, one B and one C per section, the exit checks); about 90 hours for everything.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, core; Sections 7.1–7.2 before its Section 4.1.

**How to read this chapter.** A first reading takes Sections 4.1–4.8 with every second-reading fold closed. Each section's main line teaches the section, and every A and B exercise can be done from it. The folds hold the proofs of structural induction, the parenthesis count and structural recursion, the bookkeeping lemmas, the proof that the search of Section 4.6 decides, and the descent in the completeness proof. They are not optional: later proofs use those results, and the proofs are complete. Section 4.9, on normal forms, is a second-pass section; nothing in Chapters 5–8 uses it. Section 4.10, on compactness, is optional; nothing outside it depends on it.

## Roadmap

- **Formulas as Objects.** The exact definition of a formula, parse trees, the object language and the metalanguage, and substitution into a derivation.
- **Induction on the Natural Numbers.** The principle, strong induction, a checklist for every induction, and proving more in order to prove less.
- **Induction and Recursion on Formulas.** Structural induction, a count of parentheses, the proof that every formula is read in only one way, and definitions by recursion, which fail without it.
- **Valuations and Truth Tables.** The value of every formula computed from its atoms, \( 2^n \) rows for \( n \) atoms, truth-functional connectives, and a game for the clauses.
- **Tautologies, Entailment and Equivalence.** \( \Gamma \models \psi \), satisfiable and contingent formulas, contradictory and contrary pairs, replacement and substitution, and every question reduced to one: is this list unsatisfiable?
- **Hunting for a Refuting Row.** Forced moves, splits, the search drawn as a tree, and why a closed tree proves an entailment.
- **Soundness.** Every rule checked against the tables, by induction on the lines of a derivation, so that one refuting row rules out every derivation; and the move *test the subgoal*.
- **Completeness.** The rules prove their own truth tables row by row, and excluded middle glues the rows; consistent and satisfiable coincide; a truth-table step, TAUT.
- **Normal Forms and Adequate Connectives** (second pass). Normal forms, adequate connectives, calculating with equivalences, and why a stronger hypothesis gives a weaker theorem.
- **Compactness and Maximal Consistent Sets** (optional). Infinitely many premises, Lindenbaum's construction, and why every finite part satisfiable means the whole is.

## Named moves

- **Induction on the shape of a formula.** Prove it for atoms and \( \bot \), then for each connective from the parts. (Section 4.3)
- **Check the induction.** Objects, property, base cases, steps, principle. (Section 4.2)
- **Prove more to prove less.** Strengthen the claim until the step goes through. (Sections 4.2, 4.3)
- **Define by recursion on formulas.** One clause per way of building a formula. (Section 4.3)
- **Work backwards from F.** Assume the formula false and follow what is forced. (Section 4.4)
- **Reduce to unsatisfiability.** Every semantic question asks whether some list is unsatisfiable. (Section 4.5)
- **Search for a refuting row.** Forced moves first, split when nothing is forced, close branches early. (Section 4.6)
- **Refute with one row.** One refuting row proves \( \Gamma \nvdash \psi \), by soundness. (Section 4.7)
- **Test the subgoal.** Before chasing a subgoal, look for a row that refutes it. (Section 4.7)
- **Induction on the lines of a derivation.** Show that every rule preserves the property. (Section 4.7)
- **Split on an atom.** With \( p \vee \neg p \) and \( \rulename{\vee E} \), prove the goal under \( p \) and under \( \neg p \). (Section 4.8)

**Where this goes.** Chapter 5 looks inside the atoms: it gives "every" and "some" their rules and their meaning. Chapter 8 says what reductio asserts that the other rules do not, and who objected to it. Chapter 7 gives the formulas of predicate logic structures in place of rows; it shows a theory consistent, and an axiom independent, by exhibiting a model (Section 7.4), asks which sets a formula can define (Section 7.5), and states completeness and compactness for predicate logic (Section 7.6, optional). Three later volumes take up threads of this chapter. *Sets and Functions* makes "the smallest collection of strings closed under the building steps" and "function" exact (Chapter 1). It proves induction equivalent to the well-ordering principle and shows a famous false induction that breaks at its first step (Chapter 2). *Number Systems: From \(\nN\) to \(\nR\)* derives induction from the axioms of set theory (Chapter 1). *Analysis on the Real Line* takes the least upper bound axiom as given, as this chapter takes induction (Chapter 1).

## Summary

Formulas are strings built by the clauses of @def-formula, and each is read in only one way (@thm-unique-readability), so a function on formulas can be defined by one clause per connective. Induction, on the numbers and on formulas, is the tool for statements about all of them; its checklist and its strengthening are the two habits it needs. A valuation gives every formula a truth value, and entailment, *satisfiable*, *contingent* and the pair relations are defined from rows. Every semantic question reduces to whether some list is unsatisfiable, and a search tree decides it (@prp-search-decides). Soundness (@thm-soundness) says that a refuting row rules out every derivation, and completeness (@thm-completeness) that every valid sequent has a derivation; so \( \vdash \) and \( \models \) coincide, and so do *consistent* and *satisfiable*, and derivability is decided by a finite table. TAUT records a truth-table step as one line.

All of this is proved for propositional formulas and finitely many premises (infinitely many in the optional Section 4.10). What is open is the inside of an atom: "for every \( \varepsilon > 0 \) there is an \( N \)" is one letter to a truth table, and how to reason inside it is Chapter 5's question. Also still open: which tautologies need reductio (the optional @thm-raa-independent settles two), and how short a derivation can be.

## Terms

- **adequate set of connectives**: expresses every truth function (@def-adequate).
- **atom**: one letter such as \( p, q, p_1 \), a formula alone (@def-formula).
- **conjunctive, disjunctive normal form**: an "and" of "or"s; an "or" of "and"s (@def-cnf, @def-dnf).
- **contingent formula**: true in some row and false in another (@def-tautology).
- **contradiction**: a formula false in every row (@def-tautology).
- **contradictory, contrary, subcontrary**: exactly one true; never both true; never both false (@def-pair-relations).
- **entailment**, \( \Gamma \models \psi \): no refuting row (@def-valid-argument).
- **formula**: a string built from atoms and \( \bot \) by the connectives (@def-formula).
- **height**: the nodes on a longest branch of the parse tree (@def-height).
- **induction**: from \( P(0) \) and each step, \( P(n) \) for every \( n \) (@ax-induction).
- **literal**: an atom or the negation of an atom (@def-literal).
- **parse tree**: the tree showing how a formula is built (@def-parse-tree).
- **positive, negative occurrence**: a part's sign, flipped by \( \neg \) and by hypotheses (@def-occurrence-polarity).
- **premises, infinitely many**: \( \vdash \) and \( \models \) for a collection (@def-infinite-entailment).
- **refuting row**: premises true and conclusion false (@def-valid-argument).
- **satisfiable**: some row makes every member true (@def-satisfiable).
- **search tree**: the hunt for a refuting row, drawn (@def-search-tree).
- **semantic equivalence**, \( \equiv \): the same value in every row (@def-semantic-equivalence).
- **subformula**: a formula met while building another (@def-subformula).
- **TAUT**: one line for a truth-table step (@def-rule-taut).
- **tautology**: a formula true in every row (@def-tautology).
- **truth function**: a truth value for each list of truth values (@def-truth-function).
- **truth table**: a formula's value in each of the \( 2^n \) rows (@def-truth-table).
- **truth value**: T or F, computed from the atoms (@def-truth-value).
- **valuation**: a choice of T or F for each atom (@def-valuation).
