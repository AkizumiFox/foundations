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

Words such as "let", "choose", "suppose" and "in either case" are the boxes, spoken. This chapter makes that correspondence exact in both directions. If you can hear the boxes in a written proof, you can check it alone: wherever a step is in doubt, you restore the derivation underneath. If you can speak them, someone else can check your proof.

Words can also deceive. Here is a proof whose every sentence is true and which is still wrong.

> **Claim.** For an integer \( n \), if \( n^2 \) is even, then \( n \) is even.
>
> (1) Suppose \( n \) is even. (2) Then \( n = 2k \) for some integer \( k \). (3) So \( n^2 = 4k^2 = 2(2k^2) \). (4) Hence \( n^2 \) is even. (5) Therefore, if \( n^2 \) is even, then \( n \) is even.

Every sentence is true, and so is the claim. But the box opens with "\( n \) is even", so what the lines prove is the converse, "if \( n \) is even, then \( n^2 \) is even". Section 8.6 checks this proof line by line. By the end of the chapter you will see the error at a glance.

*The question of this chapter: when a proof is written in sentences, where did its boxes go, and how does a reader find them again?*

The chapter first builds a dictionary from rules to phrases. It then writes one proof at four levels, from a full derivation to plain prose, and fixes which steps plain prose may leave unsaid. All of this becomes habits for reading, writing and checking proofs, with a list of the errors that recur. The chapter ends with the one rule mathematicians have seriously argued about: reductio ad absurdum, the rule \( \rulename{RAA} \).

**What you need.**

- **Derivations and their boxes**, from Chapters 1 and 2. An assumption opens a box, the line written after it closes it, and a line may use only lines and boxes available to it (@def-derivation).
- **The rules for every connective and quantifier**, from Chapters 1, 2 and 5. Section 8.1 collects them on one card.
- **Choosing a name**, from Sections 5.6 and 6.4. "Choose" needs a new name, and a chosen object may depend only on the names of the boxes around it.
- **The classical rule \( \rulename{RAA} \)**, from Section 2.5, the one rule that belongs to no connective, with its other two forms \( \rulename{\neg\neg E} \) and \( \rulename{LEM} \).
- **One fact from Chapter 7**: a derivation with the quantifier rules never leads from true premises to a false conclusion. Section 7.2 states it under "From counter-models to non-derivability", and Sections 8.5, 8.6 and 8.7 use it.

**Time.** About 35 hours if you read the main text and do every A exercise and one B and one C exercise per section; about 65 hours for everything.

**Minimum before *Sets and Functions*.** Chapters 1–6 and 8, without the optional sections; Sections 7.1–7.2 before its Section 4.1.

## Roadmap

- **The connective rules in prose.** A card of all the rules, and which steps may go unsaid. Each connective and classical rule gets its phrases, with a short proof annotated phrase by phrase. Then come the purpose of a box said in words, the constructive dilemma, and conditions proved equivalent by a cycle. The section ends with the three meanings of "proof by contradiction" and with proofs that only look like contradiction.
- **The quantifier rules in prose.** The phrases for "for every", "there exists", equality and unique existence, and for definitions, "the" and proving two sets equal. What a chosen object depends on, in a picture and in numbers. Then "it suffices to show", induction, "without loss of generality", and the quantifiers that English leaves unwritten or puts in the wrong place.
- **Four levels of one proof.** One short proof written four times, and the four levels named. The rule on which steps may stay silent, tested on the irrationality of \( \sqrt 2 \) and on "uniformly continuous implies continuous". How to check a doubtful sentence by expanding it.
- **Reading a proof: self-explanation.** The habit of saying, at each line, what makes it true. Four questions to ask of every line, how to name a fact the proof leaves unstated, and five strategies that good readers apply to a proof as a whole.
- **Writing a proof.** A seven-step procedure, run at once on one example. Scratch paper against the page, the conventions of written mathematics, two more examples, and how to generalize a proof.
- **Checking proofs, and what is not allowed.** Two questions for every line, a list of fourteen errors in seven families, and four student proofs checked line by line.
- **The dispute over excluded middle.** A proof of existence that names nothing, and what some mathematicians ask a proof to provide. Reductio as the one extra rule, why excluded middle cannot be refuted, and which laws survive without the rule. A short history, what analysis would lose, proofs as programs, and the book's position.
- **Stages of knowledge: Kripke models** (optional). A meaning for formulas in which knowledge grows by stages. The rules without \( \rulename{RAA} \) are sound for it, and two or three stages show which laws need \( \rulename{RAA} \).
