# Preface

This volume is for a reader who knows school algebra and has never been asked to write a proof. It teaches one skill: to read a mathematical statement exactly, and to prove it in sentences that a reader can check line by line.

It teaches logic as the grammar of proof. A proof is first written as a **derivation**, a chain in which every line is a premise, an assumption, or one application of a rule, so that checking it needs no idea: for each line we ask which rule produced it and from which lines. Each rule is introduced beside the sentence a mathematician writes when using it, and it is practiced at once, in short derivations and in proofs about numbers. The last chapter turns derivations back into ordinary mathematical prose, and shows that the rules are still there underneath.

**What it covers.** Eight chapters, in three parts.

| Part | Chapter | What it does |
|---|---|---|
| I. Propositional logic | 1 | The format of a derivation, with its boxes and scope rule, and the rules for "and", "implies" and "or" |
| | 2 | The rules for "not" and "if and only if", derived rules, and proof by contradiction with the other classical rules |
| | 3 | How to find a derivation: a search method, four kinds of task, and turning a written argument into a derivation |
| | 4 | Formulas as objects, induction, truth tables, and the theorems that the rules are sound and complete; then normal forms, and compactness (optional) |
| II. First-order logic | 5 | "For every" and "there exists": terms, formulas and substitution, the four quantifier rules and their side conditions, equality, unique existence and counting |
| | 6 | Translating mathematics into formulas, the laws for negating and moving quantifiers, searching for first-order derivations, and one theorem of analysis derived rule by rule |
| | 7 | Structures and counter-models, theories and their models, definability and isomorphism; first-order soundness and the limits of first-order logic (both optional) |
| III. Proof in prose | 8 | From derivations to mathematical prose: the rules in sentences, four levels of one proof, habits for reading, writing and checking proofs, a catalogue of the errors that recur, and the dispute over excluded middle |

**How to read it.** Read the chapters in order: each uses the ones before it. A first reading takes Chapters 1–3, Sections 4.1–4.8, Chapters 5 and 6, Sections 7.1, 7.2 and 7.4 with Section 7.5 up to its isomorphisms, and Sections 8.1–8.7. Section 4.9 and the rest of Section 7.5 wait for a second pass. Sections 4.10, 7.3, 7.6 and 8.8 are optional. Before *Sets, Relations, and Cardinality*, a reader needs the core of Chapters 1–6 and 8, and Sections 7.1–7.2 before its Chapter 3; Sections 7.4–7.5 are recommended.

Every section has Quick checks with folded answers; answer each one before you unfold it. The exercises of a section come in three groups, A to check understanding, B for practice and C to go deeper, and the last core sections of each chapter add R items that reach back to earlier chapters. Do the derivations on paper, line by line, before reading the solution. A chapter's opening page lists what it needs, with links, and the time it takes. Second-reading folds hold edge cases and longer justifications; they can be left closed on a first reading, but they are not optional, since later proofs may use what they contain. Sections and results marked optional can be skipped, and nothing outside them depends on them.

**How long it takes.** The core track, as each chapter's opening page counts it (the first-reading sections with all of A, one B and one C per section, and the exit checks), takes about 250 hours in all. Everything, folds and optional sections included, takes about 440 hours.

**Why rules before truth tables.** Many logic books begin with truth tables, where the row "a false hypothesis makes \( P \to Q \) true" has to be accepted as a convention. This book starts from the rules. Section 1.1 reads that row informally, as a promise that is not broken; Section 2.1 derives it from the rules, as vacuous truth; and Chapter 4 brings in the tables and proves that rules and tables agree: what the rules derive is true in every row (Section 4.7), and what is true in every row the rules derive (Section 4.8). The quantifiers take the same road. Chapters 5 and 6 give their rules and use them; Chapter 7 gives them their meaning in structures, where a counter-model shows that a derivation cannot exist.

**What comes next.** *Sets, Relations, and Cardinality* puts the logic to work on sets, functions, relations, induction and the sizes of infinite sets. Its first three chapters are what *Analysis on the Real Line* assumes. *Number Systems: From \(\nN\) to \(\nR\)* builds the numbers themselves out of sets.
