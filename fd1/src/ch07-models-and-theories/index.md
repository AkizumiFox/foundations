# Models and Theories

The axioms of a partial order say that \( \le \) is reflexive, antisymmetric and transitive. Do they prove that any two elements are comparable, \( \forall x\, \forall y\, (x \le y \vee y \le x) \)? A search for a derivation stalls, and a stalled search proves nothing. Two dots settle it. Take two objects \( a \) and \( b \), and let each be \( \le \) itself and nothing else. All three axioms are true there and comparability is false. By a statement of Section 7.2, that rules out every derivation.

*What does "true there" mean, and why does one picture rule out every derivation?* This chapter answers both questions. Then it uses such pictures on whole lists of axioms. The axioms of a group are a few rules that addition of integers obeys. In Section 7.4, the six symmetries of a triangle show that these rules do not force \( x \cdot y = y \cdot x \).

**What you need.**

- **The meaning of the connectives**, from Chapter 4: rows of a truth table, entailment \( \models \), and soundness, which says that a derivation never leads from true premises to a false conclusion (@thm-soundness).
- **Induction on the way a formula is built**, from Chapter 4 (@thm-structural-induction). Sections 7.1, 7.3 and 7.5 prove facts about every formula this way.
- **Terms, formulas and substitution**, from Section 5.2 (@def-first-order-formula).
- **The quantifier rules and their side conditions**, from Chapter 5, and the searches for derivations in Chapters 5 and 6 that stalled. This chapter settles several of them.
- **Sets, pairs and functions in their everyday sense.** Section 7.5 also uses one-to-one and onto functions in that sense.

**Time.** About 25 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 50 hours for everything.

**Minimum before *Sets and Functions*.** Sections 7.1 and 7.2 before its Section 4.1; Sections 7.4 and 7.5 are recommended.

## Roadmap

On a first reading, take Sections 7.1, 7.2 and 7.4, and Section 7.5 up to "Isomorphic structures"; the rest of Section 7.5 is for a second pass. Sections 7.3 and 7.6 are optional, and nothing on the first-reading list uses them.

- **Structures and Satisfaction.** A set of objects with a meaning for every symbol, values for the free variables, and seven rules that decide every formula. Small examples are drawn as dots and arrows, and a claim is proved by what it means.
- **Counter-models.** Pictures in which the premises are true and the conclusion is false. How to find one, how to test every picture with two or three objects, and why each side condition of Chapter 5 is needed. The section states that such a picture rules out every derivation.
- **Soundness for Predicate Logic** (optional). The proof of that statement, by the induction of Chapter 4.
- **Theories and Their Models.** Axioms written as sentences. One picture in which all of them are true shows that they never lead to a contradiction, and two pictures show that a sentence is neither provable nor refutable from them.
- **Definability and Isomorphism.** A formula picks out a set of objects. On the second pass: two pictures that match object for object and arrow for arrow satisfy the same sentences, and a matching of a picture with itself can move only what no formula picks out.
- **What First-Order Logic Can and Cannot Say** (optional). Completeness, compactness, numbers beyond all the natural numbers, and problems no procedure can decide, all stated without proof.
