# Finding Derivations

Chapters 1 and 2 gave every connective two rules: one for using a statement with that connective, and one for proving it. Once a derivation is written, anyone can check it line by line, with no idea at all. Finding one is harder. An assumption may be any statement whatever, and nothing in the rules says which one to make. Yet every derivation so far was found with a handful of the same strategies. So this chapter asks: *given a sequent, how do you find a derivation, and when should you stop looking?*

The answer comes in three parts. Section 3.1 puts the strategies in order as one method, explains why the order never makes a derivable goal underivable, and shows the method succeeding and failing. Section 3.2 shows that the kind of task changes how a search starts. It also shows that every task comes down to one question: can \( \bot \) be derived from a given list of statements? Section 3.3 starts from a paragraph of ordinary mathematics instead of a sequent. The chapter ends with a question its methods cannot answer. A search that fails proves nothing, so how could anyone show that a statement is **not** derivable?

**What you need.**

- The rules for every connective, from Chapters 1 and 2.
- Derivations with boxes, and which earlier lines a line may cite (@def-derivation).
- Derived rules (@def-derived-rule) and the classical rules of Section 2.5.
- From Section 1.1, the counterexample set (@def-counterexample-set) and the habit of trying to break a claim before proving it.
- Steps about "every" and "some", such as "say \( m = 2k \)", used as ordinary reasoning, as in Chapter 2. Chapter 5 gives them their rules.

**Time.** About 20 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 30 hours for everything.

## Roadmap

- **How to Find a Derivation.** The strategies of Chapters 1 and 2 put in order as one method, with the reason the order is safe. Then four ways to shorten a search, searches that succeed and one that fails, and every rule in one place.
- **Four Kinds of Task.** Theorems, equivalences, lists that derive \( \bot \), and claims to derive or refute: how each kind of task starts its search, and why all four ask whether a list derives \( \bot \).
- **From Argument to Derivation.** Finding the argument inside a paragraph, writing down the facts it leaves unsaid, setting a proof beside its derivation, and a library of standard sequents grouped by what they are for.
