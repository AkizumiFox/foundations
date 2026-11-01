# Truth, Soundness and Completeness

Chapter 3 ended on a question: we show that something is derivable by exhibiting a derivation, but how could we ever show that something is **not** derivable? Section 3.1 searched for a derivation of \( P \to Q \vdash Q \to P \), and every route stalled. A search that fails proves nothing: a cleverer derivation might exist. Here is something that does prove it.

| \( p \) | \( q \) | \( p \to q \) | \( q \to p \) | |
|---|---|---|---|---|
| T | T | T | T | |
| T | F | F | T | |
| **F** | **T** | **T** | **F** | **this row** |
| F | F | T | T | |

In the third row the premise \( p \to q \) is true, because its hypothesis is false: a promise whose condition fails is not broken (Section 1.1). The conclusion \( q \to p \) is false in that row. Section 4.1 explains why the letters are now lower-case. By the end of this chapter this one row is a **proof** that no derivation of \( q \to p \) from \( p \to q \) exists, however long.

The answer is to give every formula a **meaning**: a truth value, true or false, in each row of a table like the one above. **Soundness** says that whatever can be derived is true in every row where the premises are true. So one row with true premises and a false conclusion proves that no derivation exists. **Completeness** says the converse: whatever is true in every such row can be derived. To prove the two theorems, the chapter treats formulas as objects. It proves facts about all of them by **induction**, a way to prove a statement for every natural number one step at a time. Between the two theorems comes a search. For finitely many premises and a conclusion, it either finds a row with true premises and a false conclusion or shows that there is none. After completeness come normal forms, which you can skip on a first reading, and compactness, which is optional.

**What you need.**

- The rules for every connective, and what a derivation is, with its boxes and its scope rule, from Chapter 1 (@def-derivation).
- Derived rules, and weakening and cut, from Chapter 2 (@lem-weakening-cut).
- The classical rules of Chapter 2, above all excluded middle, \( P \vee \neg P \) (@prp-excluded-middle).
- How to search for a derivation, and what a consistent list of premises is, from Chapter 3 (@def-inconsistent-set).
- The arithmetic and the order of the natural numbers, as in school.

**Time.** About 45 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 90 hours for everything.

## Roadmap

- **Formulas as Objects.** The exact definition of a formula, the tree that shows how a formula is built, and the difference between the formulas we study and the language we use to talk about them.
- **Induction on the Natural Numbers.** The principle of induction, strong induction, a checklist for every proof by induction, and why proving more can be easier than proving less.
- **Induction and Recursion on Formulas.** Induction on the way a formula is built, a count of parentheses, the proof that every formula can be read in only one way, and definitions that follow the way a formula is built.
- **Valuations and Truth Tables.** A choice of true or false for each letter fixes the value of every formula, and \( n \) letters give \( 2^n \) rows.
- **Tautologies, Entailment and Equivalence.** Formulas true in every row, conclusions true in every row where the premises are true, and formulas with the same value in every row. Every such question becomes one question: can these formulas all be true at once?
- **Hunting for a Refuting Row.** A search, drawn as a tree, for a row with true premises and a false conclusion, which either finds one or shows there is none.
- **Soundness.** Every rule is checked against the tables, so one row with true premises and a false conclusion rules out every derivation. Before working towards a subgoal, look for such a row.
- **Completeness.** The rules prove their own truth tables row by row, and excluded middle joins the rows. So whatever is true in every row where the premises are true can be derived.
- **Normal Forms and Adequate Connectives.** Every formula has an equivalent of a standard shape, and a few connectives can express all the others. You can skip this section on a first reading: nothing in Chapters 5–8 uses it.
- **Compactness and Maximal Consistent Sets.** Infinitely many premises, and why they can all be true at once when every finite part of them can. This section is optional: nothing outside it depends on it.

Sections 4.1–4.8 are the main line. Some proofs in them are in closed panels, which you can skip on a first reading. They hold:

- the proofs of induction on formulas, of the parenthesis count, of the one-way reading and of definitions on formulas;
- the bookkeeping lemmas;
- the proof that the search of Section 4.6 always gives an answer;
- one step of the completeness proof.

Every A and B exercise can be done without opening them. They are not optional, though: later proofs use those results.
