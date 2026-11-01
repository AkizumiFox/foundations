# Chapter Review

## Summary

A written proof is a derivation in sentences. Every rule has its phrases, and "let", "suppose", "choose" and "in either case" are the boxes, spoken (Sections 8.1–8.2). The chapter named four levels of one proof (@def-levels-of-proof). One principle fixed which steps plain prose may leave unsaid (@def-silent-steps), and a doubtful sentence is checked by expanding it to a skeleton. For reading, the chapter gave a habit, self-explanation. For writing, it gave a procedure. For checking, it gave two questions and a catalogue of fourteen errors (@exm-not-allowed-catalogue).

It ended with the one rule mathematicians have disputed. Without \( \rulename{RAA} \), excluded middle has no derivation, by the optional @thm-raa-independent. Yet excluded middle cannot be refuted (@prp-not-not-excluded-middle). An irrational number raised to an irrational power can be rational. One proof of this names no witness (@thm-irrational-power-rational), and another names one, using @prp-log2-9-irrational. The optional Section 8.8 proves, with stages of knowledge, which classical laws need the rule.

What is open is what the logic is for. *Sets and Functions* writes its proofs at levels 2 and 3 with these tools, and its first question is what a set is.

## Proof methods in this chapter

- **Hear the rule in the phrase.** "Let \( x \in A \)" opens a \( \rulename{\forall I} \) box, and "suppose" opens an assumption. "Choose" is \( \rulename{\exists E} \), and "take" and "let \( \delta \coloneqq \dots \)" are \( \rulename{\exists I} \). "Suppose, for contradiction" is \( \rulename{RAA} \) or \( \rulename{\neg I} \). Both boxes end in \( \bot \), and what the box assumes and the line written after it tell which. (Sections 8.1 and 8.2)
- **Expand to check.** When a sentence is doubtful, rewrite that stretch, and only that stretch, as a skeleton, and look for the line that breaks a rule. (Section 8.3)
- **Skeleton first.** Write the first and the last sentence of every box before filling any. (Section 8.3)
- **Explain each line to yourself** by earlier lines, definitions and named results, and the rule that combines them, never by restating it. (Section 8.4)
- **Two columns when checking:** *is the line true?* and *does it follow, and by which rule?* The first column finds where to look, and the second decides. (Section 8.6)
- **Say what depends on what.** Every chosen object carries its dependencies: the names in the line it comes from, among the boxes open when it was chosen. (Section 8.2)
- **Write the reductions as a column.** Each "it suffices to show" is one row with its reason. Read upwards, the column is the proof. (Section 8.3)
- **Generalize by a new name.** Replace the particular object by a new letter, and keep only the lines that still hold for it. (Section 8.5)

## Terms

- **BHK reading**: a proof as a construction of what it claims (Section 8.7).
- **catalogue of errors**, (N1)–(N14): recurring errors, each with the rule it breaks (@exm-not-allowed-catalogue).
- **costume**: a direct or contrapositive proof dressed as a proof by contradiction (@exm-costume-direct).
- **double inclusion**: \( A = B \) shown as \( A \subseteq B \) and \( B \subseteq A \) (@exm-rhetoric-double-inclusion).
- **forcing** (optional): what a stage of knowledge makes true (@def-forcing).
- **heredity** (optional): what a stage forces, every later stage forces (@lem-heredity).
- **intuitionistic logic**: the rules of this book without \( \rulename{RAA} \) (Section 8.7).
- **Kripke model** (optional): stages of knowledge, with atoms that stay known (@def-kripke-model).
- **levels of proof**: derivation, skeleton, annotated prose, plain prose (@def-levels-of-proof).
- **self-explanation**: naming what makes each line true, never restating it (@exm-self-explanation).
- **silent step**: a step plain prose may leave unwritten (@def-silent-steps).
- **skeleton**: level 1, the boxes and the logical lines (@def-levels-of-proof).
- **TFAE by a cycle** ("the following are equivalent"): several conditions shown equivalent by a loop of implications (@exm-rhetoric-cycle).

## Results used from earlier chapters

This is the first volume, so every result the chapter uses comes from Chapters 1–7.

*Chapters 1 and 2*:

- the rules for every connective, and derivations with their boxes and scope rule (@def-derivation);
- derived rules (@def-derived-rule) and the cut rule (@lem-weakening-cut);
- the classical rules of Section 2.5 and how each derives the others (@thm-classical-rules-interderivable);
- the two running examples, @thm-square-even-implies-even and @thm-sqrt2-irrational.

*Chapter 3*:

- the search for a derivation (Section 3.1) and the extraction of an argument (Section 3.3);
- @prp-derivable-iff-negation-inconsistent.

*Chapter 4*:

- induction and strong induction (@ax-induction, @thm-strong-induction);
- truth tables and refuting rows (@exm-backwards-from-f, @def-valid-argument, @cor-refuting-row);
- soundness (@thm-soundness) and completeness (@thm-completeness, @cor-derivable-iff-valid);
- the rule TAUT (@def-rule-taut);
- the proof of @lem-atom-splitting, for a Challenge exercise of Section 8.4;
- for Section 8.7 only, the optional @thm-raa-independent.

*Chapters 5 and 6*:

- the quantifier rules and their side conditions (@def-rules-universal, @def-rules-existential), and the bounded rules (@prp-bounded-quantifier-rules);
- definitions of analysis translated into formulas (Section 6.1);
- the laws for negating quantifiers (@prp-quantifier-negation);
- the propositional skeleton (@def-propositional-skeleton, @prp-taut-skeleton);
- the derivation that uniform continuity implies continuity (@exm-uniform-implies-continuous), the place where its converse breaks down (@exm-converse-fails), and the counter-model @exm-square-not-uniform.

*Chapter 7*: the soundness statement for predicate logic in Section 7.2. Its proof is the optional Section 7.3.

*For the optional Section 8.8*: structural induction and recursion (@thm-structural-induction, @thm-structural-recursion), and the proof of @thm-soundness with its context lemma (@lem-context-inclusion).

School arithmetic and the order of \( \nR \) are used in examples as facts.
