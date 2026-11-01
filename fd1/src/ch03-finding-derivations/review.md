# Chapter Review

## Summary

The search method reads the boxes off the goal and the elimination rules off the premises. Its goal-directed steps and its last-resort classical step never turn a gap that can be filled into one that cannot (Section 3.1, "Why the order loses nothing"). Postponing a disjunction, and four refinements, make the search shorter. Every task of Section 3.2 is a question about derivability. Every question about derivability is in turn a question about whether a list is **inconsistent**, that is, whether it derives \( \bot \) (@prp-derivable-iff-negation-inconsistent). So deriving \( \varphi \) from \( \Gamma \) is the same as showing that the counterexample set \( \Gamma, \neg\varphi \) is inconsistent. An inconsistent list derives every statement (@prp-inconsistent-derives-everything). An argument in prose becomes a sequent once its unstated facts are written down, and the library of Section 3.3 sorts the standard sequents by what they are for.

What is left open: every method of the chapter can show that something **is** derivable, and none can show that something is **not**. A claim that breaks, or a search that stalls, has not been shown underivable. Chapter 4 answers that question.

## Proof methods in this chapter

- **Work from both ends.** Let the goal choose the boxes, let the premises choose the elimination rules, and keep the classical rules for when nothing else works. Introduced in Section 3.1.
- **Find the goal among the resources.** If the current goal is already on an available line, cite it, or copy it by \( \rulename{R} \). Introduced in Section 3.1.
- **Derive what needs nothing new before opening a box.** A line written outside the boxes is available inside all of them. Introduced in Section 3.1.
- **Look first for a clash partner already on a line.** When the goal is \( \bot \), aim at a statement whose negation you already have. Introduced in Section 3.1.
- **No detours.** Never build a line by an introduction rule and then take it apart at once by the matching elimination rule. Introduced in Section 3.1.
- **Let the task choose the search.** A theorem starts from the goal alone, an equivalence needs two derivations, and an inconsistent list needs a clash. Introduced in Section 3.2.
- **Try to break it first.** Before searching, try to make every statement of the counterexample set true. If every attempt is forced into a clash, the attempt is usually a derivation read backwards. The statements it was forced to accept suggest the boxes, and its clash suggests the line \( \bot \). Introduced in Section 3.2.
- **Name the unstated fact.** An argument in prose leaves some premises unsaid. Write each one down and check that it is true. Introduced in Section 3.3.
- **Two columns.** Write the proof beside the derivation it follows, and see which lines the prose leaves out. Introduced in Section 3.3.

## Terms

- **consistent list**: a list from which \( \bot \) is not derivable (@def-inconsistent-set).
- **counterexample set** (from Section 1.1): the premises together with the negated conclusion (@def-counterexample-set).
- **current goal**: the written line below a gap (@def-partial-derivation).
- **gap**: a stretch of a partial derivation still missing (@def-partial-derivation).
- **inconsistent list**: a list from which \( \bot \) is derivable (@def-inconsistent-set).
- **partial derivation**: a derivation with gaps still to fill (@def-partial-derivation).
- **provably equivalent** (from Section 2.4): each derivable from the other (@def-provable-equivalence).
- **resources**: the lines available at a gap's current goal (@def-partial-derivation).
- **theorem (of logic)**: a statement derivable from no premises, \( \vdash \varphi \) (@def-derivable).

## Results used from earlier volumes

None. *Logic and Proof* is the first volume, and this chapter uses only Chapters 1 and 2.
