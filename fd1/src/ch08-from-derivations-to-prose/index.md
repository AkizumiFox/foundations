# From Derivations to Mathematical Prose

Here is a proof that every schoolbook prints: for an integer \( n \), if \( n \) is even, then \( n^2 \) is even.

> Suppose \( n \) is even, say \( n = 2k \). Then \( n^2 = 4k^2 = 2(2k^2) \), so \( n^2 \) is even.

And here is the same proof as a derivation, for one fixed integer \( n \), with "even" written out: \( n \) is even when \( n = 2k \) for some integer \( k \).

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\exists k \, (n = 2 \cdot k)}
  \open[k_0]
  \hypo {2} {n = 2 \cdot k_0}
  \have {3} {n \cdot n = 2 \cdot (2 \cdot k_0 \cdot k_0)} \by{arith}{2}
  \have {4} {\exists j \, (n \cdot n = 2 \cdot j)} \Ei{3}
  \close
  \have {5} {\exists j \, (n \cdot n = 2 \cdot j)} \Ee{1,2-4}
  \close
  \have {6} {\exists k \, (n = 2 \cdot k) \to \exists j \, (n \cdot n = 2 \cdot j)} \ii{1-5}
\end{nd}$
\end{center}
```

At line 5 the side condition holds: \( k_0 \) is not in line 5, not in line 1, and in no other open assumption. The words and the lines match one for one:

| Words | Lines | What they do |
|---|---|---|
| "Suppose \( n \) is even" | 1 | open the \( \rulename{{\to}I} \) box |
| "say \( n = 2k \)" | 2 | open the \( \rulename{\exists E} \) box, with a new name |
| "Then \( n^2 = 4k^2 = 2(2k^2) \)" | 3 | algebra inside both boxes |
| "so \( n^2 \) is even" | 4 | \( \rulename{\exists I} \), with the witness \( 2k^2 \) |
| (the paragraph ends) | 5, 6 | the two boxes close |

Words such as "let", "choose", "suppose" and "in either case" are the boxes, spoken. This chapter makes that correspondence exact in both directions. Learning to hear the boxes is what lets a reader working alone check a proof, by restoring the derivation underneath wherever a step is in doubt; learning to speak them is what makes a proof checkable by someone else.

Words can also deceive. Here is a proof whose every sentence is true and which is still wrong.

> **Claim.** For an integer \( n \), if \( n^2 \) is even, then \( n \) is even.
>
> (1) Suppose \( n \) is even. (2) Then \( n = 2k \) for some integer \( k \). (3) So \( n^2 = 4k^2 = 2(2k^2) \). (4) Hence \( n^2 \) is even. (5) Therefore, if \( n^2 \) is even, then \( n \) is even.

Every sentence is true, and so is the claim. But the box opens with "\( n \) is even", so what the lines prove is the converse, "if \( n \) is even, then \( n^2 \) is even". Section 8.6 checks this proof line by line; by the end of the chapter you will see the error at a glance.

*The question of this chapter: when a proof is written in sentences, where did its boxes go, and how does a reader find them again?*

The chapter builds a dictionary from rules to phrases, writes proofs at four levels from full derivation to plain prose, fixes which steps plain prose may leave unsaid, and turns all of this into habits for reading, writing and checking proofs, with a catalogue of the errors that recur. It ends with the one rule mathematicians have seriously argued about: reductio ad absurdum.

**What you need.** Chapters 1–6, core. From Chapter 7, only the statement in Section 7.2 under "From counter-models to non-derivability", that a derivation with the quantifier rules never leads from true premises to a false conclusion; Sections 8.6 and 8.7, and Exercise C3 of Section 8.5, use it as a fact.

- **Boxes.** An assumption opens a box, the line written after it closes it, and a line may cite only lines and boxes available to it (@def-derivation).
- **The rules.** The introduction and elimination rules of every connective and quantifier, and the derived rules of Chapter 2; Section 8.1 collects them on one card.
- **Choosing.** "Choose" needs a fresh name, and a chosen constant may depend only on the names of the boxes around it (Sections 5.6 and 6.4).
- **The classical rule.** \( \rulename{RAA} \) is the one rule that belongs to no connective; \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \) are its other two forms (Section 2.5).

::: {.second-reading title="The chief earlier results this chapter cites"}
From Chapters 1 and 2: the rules for every connective, derivations with their boxes and scope rule (@def-derivation), derived rules (@def-derived-rule), the classical rules of Section 2.5 and their interderivability (@thm-classical-rules-interderivable), the cut rule (@lem-weakening-cut), and the two running examples @thm-square-even-implies-even and @thm-sqrt2-irrational. From Chapter 3: the search for a derivation (Section 3.1), the extraction of an argument (Section 3.3) and @prp-derivable-iff-negation-inconsistent. From Chapter 4: induction and strong induction (@ax-induction, @thm-strong-induction), truth tables and refuting rows (@exm-backwards-from-f, @def-valid-argument, @cor-refuting-row), soundness (@thm-soundness), completeness (@thm-completeness, @cor-derivable-iff-valid), the rule TAUT (@def-rule-taut) and the proof of @lem-atom-splitting (for a Challenge exercise of Section 8.4), and, for Section 8.7 only, the optional @thm-raa-independent. From Chapters 5 and 6: the quantifier rules and their side conditions (@def-rules-universal, @def-rules-existential), the bounded rules (@prp-bounded-quantifier-rules), definitions of analysis translated into formulas (Section 6.1), the laws for negating quantifiers (@prp-quantifier-negation), the propositional skeleton (@def-propositional-skeleton, @prp-taut-skeleton), and the derivation that uniform continuity implies continuity together with the place where its converse breaks down (@exm-uniform-implies-continuous, @exm-converse-fails, and the counter-model @exm-square-not-uniform). School arithmetic and the order of \( \nR \) are used in examples as facts. From Chapter 7: the statement of Section 7.2 named above (its proof is the optional Section 7.3). For the optional Section 8.8: structural induction and recursion (@thm-structural-induction, @thm-structural-recursion) and the proof of @thm-soundness with its context lemma (@lem-context-inclusion).
:::

**Time.** About 35 hours on the core track (all of A, one B and one C per section, the exit checks); about 65 hours for everything.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, core; Sections 7.1–7.2 before its Section 4.1.

## Roadmap

- **The connective rules in prose.** The rule card for the whole chapter, and which steps may go unsaid; the dictionary rows for the connectives and the classical rules, each with a short proof annotated phrase by phrase; the spoken purpose of a box; the constructive dilemma and equivalent conditions proved by a cycle; why \( \rulename{\neg I} \) and \( \rulename{RAA} \) are told apart; the three faces of "proof by contradiction"; the costumes.
- **The quantifier rules in prose.** The rows for "for every", "there exists", equality and unique existence; definitions, "the" and double inclusion; what a chosen constant depends on, in a picture and in numbers; "it suffices to show", induction and "without loss of generality"; the quantifiers that English leaves unwritten or puts in the wrong place.
- **Four levels of one proof.** One short proof written four times; the levels named; the convention on silent steps; the irrationality of \( \sqrt 2 \) and "uniformly continuous implies continuous" at the levels that show most; which silent steps are truth-functional; "it suffices to show" written as a column; how to check a doubtful sentence by expanding it.
- **Reading a proof: self-explanation.** The book's training passage for the habit of naming, at each line, what makes it true; four questions to ask of every line; naming the unstated fact; and five strategies that good readers apply to a proof as a whole.
- **Writing a proof.** A seven-step procedure, run at once on one example; scratch paper against the page; the conventions of written mathematics; two more examples; generalizing a proof.
- **Checking proofs, and what is not allowed.** Two questions for every line; the catalogue (N1)–(N14) in seven families; four student proofs checked line by line (and, in a fold, the errors' traditional names).
- **The dispute over excluded middle.** A proof of existence that names nothing; what a proof provides under the BHK reading; reductio as the one extra rule; why excluded middle cannot be refuted; which laws survive without the rule; a short history; what analysis would lose; proofs as programs; the book's position.
- **Stages of knowledge: Kripke models** (optional). A semantics in which knowledge grows by stages; the rules without \( \rulename{RAA} \) are sound for it, and two or three stages show which laws need \( \rulename{RAA} \).

## Named moves

- **Hear the rule in the phrase.** "Let \( x \in A \)" opens a \( \rulename{\forall I} \) box and "suppose" an assumption; "choose" is \( \rulename{\exists E} \); "take" and "let \( \delta \coloneqq \dots \)" are \( \rulename{\exists I} \); "suppose, for contradiction" is \( \rulename{RAA} \) or \( \rulename{\neg I} \); both boxes end in \( \bot \), and what the box assumes and the line written after it closes tell which.
- **Expand to check.** When a sentence is doubtful, rewrite that stretch, and only that stretch, as a skeleton, and look for the line that breaks a rule.
- **Skeleton first.** Write the first and the last sentence of every box before filling any.
- **Self-explain each line** by earlier lines, definitions and named results, and the rule that combines them; never by paraphrase.
- **Two columns when checking:** *is the line true?* and *does it follow, and by which rule?* The first column finds where to look; the second decides.
- **Say what depends on what.** Every chosen object carries its dependencies: the names in the line it comes from, among the boxes open when it was chosen.
- **Write the reductions as a column.** Each "it suffices to show" is one row with its reason; read upwards, the column is the proof. (Section 8.3)
- **Generalize by a fresh name.** Replace the particular object by a new letter, and keep only the lines that still hold for it. (Section 8.5)

## Summary

A written proof is a derivation in sentences: every rule has its phrases, and "let", "suppose", "choose" and "in either case" are the boxes, spoken (Sections 8.1–8.2). The chapter named four levels of one proof (@def-levels-of-proof) and fixed by one principle which steps plain prose may leave unsaid (@def-silent-steps); a doubtful sentence is checked by expanding it to a skeleton. It gave a habit for reading (self-explanation), a procedure for writing, and, for checking, two questions and a catalogue of fourteen errors (@exm-not-allowed-catalogue). It ended with the one rule mathematicians have disputed. Without \( \rulename{RAA} \), excluded middle has no derivation (the optional @thm-raa-independent) and yet cannot be refuted (@prp-not-not-excluded-middle). An irrational power of an irrational number can be shown rational with or without a named witness (@thm-irrational-power-rational, @prp-log2-9-irrational). The optional Section 8.8 proves, with stages of knowledge, which classical laws need the rule. What is open is what the logic is for. *Sets and Functions* writes its proofs at levels 2 and 3 with these tools, and its first question is what a set is.

## Terms

- **BHK reading**: a proof as a construction of what it claims ([Section 8.7](07-excluded-middle.html#what-a-proof-provides)).
- **costume**: a direct or contrapositive proof dressed as contradiction (@exm-costume-direct).
- **double inclusion**: \( A = B \) shown as \( A \subseteq B \) and \( B \subseteq A \) (@exm-rhetoric-double-inclusion).
- **forcing** (optional): what a stage of knowledge makes true (@def-forcing).
- **heredity** (optional): what a stage forces, every later stage forces (@lem-heredity).
- **intuitionistic logic**: the rules of this book without \( \rulename{RAA} \) ([Section 8.7](07-excluded-middle.html#one-extra-rule)).
- **Kripke model** (optional): stages of knowledge, with atoms that stay known (@def-kripke-model).
- **levels of proof**: derivation, skeleton, annotated prose, plain prose (@def-levels-of-proof).
- **not-allowed catalogue**, (N1)–(N14): recurring errors, each with the rule broken (@exm-not-allowed-catalogue).
- **self-explanation**: naming each line's warrant, never paraphrasing it (@exm-self-explanation).
- **silent step**: a step plain prose may leave unwritten (@def-silent-steps).
- **skeleton**: level 1, the boxes and the logical lines (@def-levels-of-proof).
- **TFAE by a cycle**: several conditions shown equivalent by a loop of implications (@exm-rhetoric-cycle).
