# From Argument to Derivation

Sections 3.1 and 3.2 started from a sequent: its letters, its premises and its conclusion were given. Mathematics starts from a paragraph. Its premises are scattered among words such as "since" and "so"; some of them are not written at all; and its letters must be chosen. This section turns paragraphs into sequents and derives them. Then it goes the other way, and writes a proof beside the derivation it mirrors. A last page collects the sequents that searches keep needing.

## One key for the section

Section 1.1, Exercise B5, fixed one key for an integer \( n \), and this section keeps it: \( E \): "\( n \) is even", \( P \): "\( n \) is prime", \( T \): "\( n \) is a multiple of \( 3 \)", \( G \): "\( n > 10 \)" (@exr-statements-and-connectives-b5). A **prime** is an integer greater than \( 1 \) whose only positive divisors are \( 1 \) and itself. Three facts about integers will serve as premises:

- **F1** \( (P \wedge E) \to \neg G \): an even prime is at most \( 10 \). The only even prime is \( 2 \), since an even \( n > 2 \) has the divisor \( 2 \).
- **F2** \( (P \wedge T) \to \neg G \): a prime multiple of \( 3 \) is at most \( 10 \). The only one is \( 3 \), since a multiple of \( 3 \) greater than \( 3 \) has the divisor \( 3 \).
- **F3** \( (E \wedge T) \to \neg P \): no even multiple of \( 3 \) is prime. Such an integer is a multiple of \( 6 \). A positive multiple of \( 6 \) has the divisor \( 2 \) and is greater than \( 2 \), and \( 0 \) and the negative integers are not prime.

Each fact is true for every integer \( n \). An argument may use any of them as a premise, and a derivation lists the ones it uses.

A translation is checked by reading it back, letter by letter, as in Section 1.1: F3 reads back as "if \( n \) is even and a multiple of \( 3 \), then \( n \) is not prime".

::: {.check}
On the key, translate "\( n \) is an odd prime greater than \( 10 \)". Then read back \( G \to \neg(P \wedge E) \).
:::

::: {.solution}
\( (\neg E \wedge P) \wedge G \). And \( G \to \neg(P \wedge E) \) reads back as "if \( n > 10 \), then \( n \) is not an even prime".
:::

## Extracting an argument

To turn a paragraph into a sequent, work through five steps.

1. *Find the conclusion.* Words such as *so*, *hence*, *therefore*, *thus* and *it follows that* introduce it.
2. *Find the stated premises.* Words such as *since*, *because*, *for* and *given that* introduce them. A supposition ("suppose …", "let \( n \) be …") is a premise, or the assumption of a box.
3. *Name the unstated facts.* Wherever a step does not follow by a rule from the lines before it, write the fact that would make it follow, as an implication, and check that the fact is true. Supply the weakest fact that closes the gap: a stronger one may prove more than the paragraph claims, or be false. (Compare Section 1.3, Exercise B5 (d), where a missing implication was written and checked.)
4. *Translate on a key*, with Section 1.1's phrase book.
5. *Derive the sequent, or break it.*

Steps 1–4 are reading. Step 5 is the rest of this book.

::: {#exm-extract-argument}
[An argument about a prime, extracted]

Extract the argument of this paragraph and derive it.

> Let \( n \) be an integer, and suppose that \( n \) is a prime greater than \( 10 \). Then \( n \) is odd, since the only even prime is \( 2 \). Nor is \( n \) a multiple of \( 3 \), because the only prime that is a multiple of \( 3 \) is \( 3 \) itself. So \( n \) is neither even nor a multiple of \( 3 \).
:::

::: {.solution}
We take the five steps in order.

1. The conclusion follows "So": \( n \) is neither even nor a multiple of \( 3 \), that is, \( \neg E \wedge \neg T \) ("neither … nor" in the phrase book).
2. The stated premise is the supposition, "\( n \) is a prime greater than \( 10 \)": \( P \wedge G \), since "a prime greater than \( 10 \)" is a conjunction. "\( n \) is odd" and "nor is \( n \) a multiple of \( 3 \)" are not premises. They are steps, each with a reason after "since" or "because".
3. The reasons are facts about numbers, but not in a form a rule can use. "The only even prime is \( 2 \)" is used as "an even prime is not greater than \( 10 \)", which is F1. The second reason is used as F2.
4. The sequent is
   \[
   P \wedge G, \ (P \wedge E) \to \neg G, \ (P \wedge T) \to \neg G \vdash \neg E \wedge \neg T.
   \]
5. We read the derivation off the goal. It is a conjunction of two negations: two \( \rulename{\neg I} \) boxes joined by \( \rulename{\wedge I} \), as in Section 3.1.

In the first picture, the premise is taken apart and the two conjuncts stand as subgoals. In the second, each subgoal has its box, with goal \( \bot \).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge G}
  \hypo {2} {(P \wedge E) \to \neg G}
  \hypo {3} {(P \wedge T) \to \neg G}
  \have {4} {P} \ae{1}
  \have {5} {G} \ae{1}
  \have[\ ][0] {} {\vdots}
  \have[][10] {10} {\neg E}
  \have[\ ][0] {} {\vdots}
  \have[][15] {15} {\neg T}
  \have {16} {\neg E \wedge \neg T} \ai{10,15}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {P \wedge G}
  \hypo {2} {(P \wedge E) \to \neg G}
  \hypo {3} {(P \wedge T) \to \neg G}
  \have {4} {P} \ae{1}
  \have {5} {G} \ae{1}
  \open
  \hypo {6} {E}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {\bot}
  \close
  \have {10} {\neg E} \ni{6-9}
  \open
  \hypo {11} {T}
  \have[\ ][0] {} {\vdots}
  \have[][14] {14} {\bot}
  \close
  \have {15} {\neg T} \ni{11-14}
  \have {16} {\neg E \wedge \neg T} \ai{10,15}
\end{nd}$
\end{center}
```

Inside each box, the fact fires once the box's assumption is joined to \( P \), and its conclusion \( \neg G \) clashes with line 5.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge G}
  \hypo {2} {(P \wedge E) \to \neg G}
  \hypo {3} {(P \wedge T) \to \neg G}
  \have {4} {P} \ae{1}
  \have {5} {G} \ae{1}
  \open
  \hypo {6} {E}
  \have {7} {P \wedge E} \ai{4,6}
  \have {8} {\neg G} \ie{2,7}
  \have {9} {\bot} \ne{5,8}
  \close
  \have {10} {\neg E} \ni{6-9}
  \open
  \hypo {11} {T}
  \have {12} {P \wedge T} \ai{4,11}
  \have {13} {\neg G} \ie{3,12}
  \have {14} {\bot} \ne{5,13}
  \close
  \have {15} {\neg T} \ni{11-14}
  \have {16} {\neg E \wedge \neg T} \ai{10,15}
\end{nd}$
\end{center}
```

Lines 4–5 need nothing new, so they are written before the boxes (Section 3.1). Had the supposition been kept as a supposition, the claim would be \( (P \wedge E) \to \neg G, \ (P \wedge T) \to \neg G \vdash (P \wedge G) \to (\neg E \wedge \neg T) \): the same lines inside one more box, closed by \( \rulename{{\to}I} \).
:::

The argument can also be drawn as a map: each statement a dot, each step an arrow into what it gives. The unstated facts are the dots nobody wrote. The map shows what supports what; it is not a derivation, and it leaves out the boxes.

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=above:{F1 (unstated)}] (f1) at (0,2.4) {};
  \node[elt, label=above:{$P \wedge G$ (given)}] (g) at (2,2.4) {};
  \node[elt, label=above:{F2 (unstated)}] (f2) at (4,2.4) {};
  \node[elt, label=left:{$\neg E$}] (e) at (1,1.2) {};
  \node[elt, label=right:{$\neg T$}] (t) at (3,1.2) {};
  \node[elt, label=below:{$\neg E \wedge \neg T$}] (c) at (2,0) {};
  \draw[rel] (f1) -- (e);
  \draw[rel] (g) -- (e);
  \draw[rel] (g) -- (t);
  \draw[rel] (f2) -- (t);
  \draw[rel] (e) -- (c);
  \draw[rel] (t) -- (c);
\end{tikzpicture}
\end{center}
```

::: {.check}
Which line of the derivation in @exm-extract-argument is the paragraph's sentence "Then \( n \) is odd", and which lines does the paragraph leave silent?
:::

::: {.solution}
Line 10. The paragraph is silent on lines 4–9, the box that shows it, apart from the reason F1 behind line 8.
:::

::: {.warning}
[Not allowed: extracting an argument]

Each entry names the step of the method it breaks.

- "Writing '\( n \) is odd' among the premises": a step taken as a premise. The derivation then proves nothing about whether \( n \) is odd (step 2).
- "Reading '\( n \) is odd, since \( n \) is a prime greater than \( 10 \)' with '\( n \) is odd' as the premise": *since* introduces the premise, not the conclusion (steps 1–2).
- "Supplying 'every prime is odd' for the first step": the supplied fact must be true, and this one fails at \( n = 2 \) (step 3).
- "Supplying \( \neg E \wedge \neg T \) itself as the unstated fact": the derivation is legal and proves nothing. Supply the weakest fact that closes the gap (step 3).
- "Translating '\( n \) is a prime greater than \( 10 \)' as \( P \to G \)": a noun with an adjective is a conjunction, \( P \wedge G \), as "an even prime" was \( E \wedge P \) in Section 1.1 (step 4).
:::

## Two columns

Now the other direction: a proof is written, and its derivation is wanted. Write the proof in the left column and the derivation in the right, each sentence on the row of the lines it says. A line that no sentence says is a **silent step**. A sentence that matches no line is a gap in the proof, or a step this book's rules cannot take.

::: {#exm-two-columns}
[A proof and its derivation, side by side]

Let \( n \) be an integer. Claim: if \( n \) is even and prime, then \( n \) is not a multiple of \( 3 \).

> *Proof.* Suppose \( n \) is even and prime. If \( n \) were a multiple of \( 3 \), it would be an even multiple of \( 3 \), and no even multiple of \( 3 \) is prime; but \( n \) is prime. So \( n \) is not a multiple of \( 3 \).

Write the derivation the proof mirrors, in two columns.
:::

::: {.solution}
The proof uses one fact, F3, and the claim is an implication. The sequent is \( (E \wedge T) \to \neg P \vdash (E \wedge P) \to \neg T \). The goal gives a box on \( E \wedge P \) (left). Inside it the goal \( \neg T \) is a negation, so a \( \rulename{\neg I} \) box on \( T \) opens, after the assumption has been taken apart (right).

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {(E \wedge T) \to \neg P}
  \open
  \hypo {2} {E \wedge P}
  \have[\ ][0] {} {\vdots}
  \have[][9] {9} {\neg T}
  \close
  \have {10} {(E \wedge P) \to \neg T} \ii{2-9}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {(E \wedge T) \to \neg P}
  \open
  \hypo {2} {E \wedge P}
  \have {3} {E} \ae{2}
  \have {4} {P} \ae{2}
  \open
  \hypo {5} {T}
  \have[\ ][0] {} {\vdots}
  \have[][8] {8} {\bot}
  \close
  \have {9} {\neg T} \ni{5-8}
  \close
  \have {10} {(E \wedge P) \to \neg T} \ii{2-9}
\end{nd}$
\end{center}
```

The two columns finish the derivation.

| The proof | The derivation |
|---|---|
| "Suppose \( n \) is even and prime." | 2 \( E \wedge P \), asm, for \( \rulename{{\to}I} \) |
| (silent) | 3 \( E \), 4 \( P \), \( \rulename{\wedge E} \) 2 |
| "If \( n \) were a multiple of \( 3 \)," | 5 \( T \), asm, for \( \rulename{\neg I} \) |
| "it would be an even multiple of \( 3 \)," | 6 \( E \wedge T \), \( \rulename{\wedge I} \) 3, 5 |
| "and no even multiple of \( 3 \) is prime;" | 1 \( (E \wedge T) \to \neg P \), F3; 7 \( \neg P \), \( \rulename{{\to}E} \) 1, 6 |
| "but \( n \) is prime." | 8 \( \bot \), \( \rulename{\neg E} \) 4, 7 |
| "So \( n \) is not a multiple of \( 3 \)." | 9 \( \neg T \), \( \rulename{\neg I} \) 5–8 |
| (the claim) | 10 \( (E \wedge P) \to \neg T \), \( \rulename{{\to}I} \) 2–9 |

The finished derivation, read down the right column:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(E \wedge T) \to \neg P}
  \open
  \hypo {2} {E \wedge P}
  \have {3} {E} \ae{2}
  \have {4} {P} \ae{2}
  \open
  \hypo {5} {T}
  \have {6} {E \wedge T} \ai{3,5}
  \have {7} {\neg P} \ie{1,6}
  \have {8} {\bot} \ne{4,7}
  \close
  \have {9} {\neg T} \ni{5-8}
  \close
  \have {10} {(E \wedge P) \to \neg T} \ii{2-9}
\end{nd}$
\end{center}
```

The proof says lines 2 and 5–9. It is silent on lines 3–4, taking the conjunction apart, and on line 10, since closing the outer box is the claim itself. Its "Suppose" is line 2's "asm, for \( \rulename{{\to}I} \)", and its "If \( n \) were" is line 5's "asm, for \( \rulename{\neg I} \)". The proof hides the fact F3 in a clause; the derivation lists it.
:::

::: {.check}
If the claim in @exm-two-columns were "if \( n \) is even and prime, then \( n \) is at most \( 10 \)", which fact would replace F3, and what would happen to the box of line 5?
:::

::: {.solution}
F1 replaces F3. The box of line 5 disappears: the goal \( \neg G \) is F1's conclusion, so after \( \rulename{\wedge E} \) and \( \rulename{\wedge I} \) give \( P \wedge E \), one \( \rulename{{\to}E} \) line reaches it.
:::

## A library of standard sequents

Chapters 1 and 2 and Section 3.2 proved sequents that searches keep needing. Here they are grouped by what they are for: a searcher with a resource or a goal of a given shape looks up its row. Each row is a derived rule (@def-derived-rule). It is applied to **whole** available lines, never to a part of a line, and it is cited by the name in its middle column. "The rules in one place" in Section 3.1 lists the same rules by the chapter that proved them; this page lists them by use. The last group is different: it holds facts about derivations, which change the task rather than add a line.

| Sequent | In a justification | Proved in |
|---|---|---|
| **To use an implication** | | |
| \( P \to Q, \ \neg Q \vdash \neg P \) | \( \rulename{MT} \) | @prp-modus-tollens |
| \( P \to Q, \ Q \to R \vdash P \to R \) | (implication is transitive) | @prp-implication-transitive |
| \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \) | (curry) | @prp-curry |
| \( P \to Q \vdash \neg P \vee Q \) | (implication as disjunction) | @prp-implication-as-disjunction (b) |
| **To use a disjunction** | | |
| \( P \vee Q, \ \neg P \vdash Q \); \( P \vee Q, \ \neg Q \vdash P \) | \( \rulename{DS} \) | @prp-disjunctive-syllogism; @exr-derived-rules-b1 (a) |
| \( (P \to R) \wedge (Q \to R) \dashv\vdash (P \vee Q) \to R \) | (cases on a hypothesis) | @exm-cases-on-hypothesis; @exm-or-hypothesis-split |
| \( (P \to R) \wedge (Q \to S), \ P \vee Q \vdash R \vee S \) | (constructive dilemma) | @exm-constructive-dilemma |
| \( (P \to R) \wedge (Q \to S), \ \neg R \vee \neg S \vdash \neg P \vee \neg Q \) | (destructive dilemma) | @exr-derived-rules-b4 (b) |
| \( \neg(P \wedge Q) \vdash P \to \neg Q \) | (*modus ponendo tollens*) | @exr-derived-rules-b4 (c) |
| **To use a negation or a clash** | | |
| \( P, \ \neg P \vdash Q \) | (ex falso) | @prp-ex-falso |
| \( \neg P \vdash P \to Q \) | VI | @prp-vacuous-implication |
| \( \neg\neg P \vdash P \) | \( \rulename{\neg\neg E} \) | @prp-double-negation (b) |
| \( \neg(P \vee Q) \vdash \neg P \wedge \neg Q \); \( \neg(P \wedge Q) \vdash \neg P \vee \neg Q \) | \( \rulename{DM} \) | @prp-de-morgan (a), (d) |
| **To reach a negation** | | |
| \( P \to Q \vdash \neg Q \to \neg P \) | \( \rulename{CP} \) | @prp-contrapositive |
| \( \vdash (P \to (Q \wedge \neg Q)) \to \neg P \) | (implies a contradiction) | @exm-theorem-search |
| \( \neg P \wedge \neg Q \vdash \neg(P \vee Q) \); \( \neg P \vee \neg Q \vdash \neg(P \wedge Q) \) | \( \rulename{DM} \) | @prp-de-morgan (b), (c) |
| \( P \vdash \neg\neg P \) | \( \rulename{\neg\neg I} \) | @prp-double-negation (a) |
| **To reach an implication** | | |
| \( \neg P \vee Q \vdash P \to Q \) | (implication as disjunction) | @prp-implication-as-disjunction (a) |
| \( \neg Q \to \neg P \vdash P \to Q \) | (\( \rulename{CP} \), converse) | @prp-contrapositive-converse |
| **To reach a disjunction** | | |
| \( \vdash P \vee \neg P \) | \( \rulename{LEM} \) | @prp-excluded-middle |
| \( (P \wedge \neg Q) \to R \dashv\vdash P \to (Q \vee R) \) | (refute one side) | @exm-equivalence-search |
| **To rearrange** | | |
| \( P \wedge Q \vdash Q \wedge P \); \( P \vee Q \vdash Q \vee P \) | (and commutes); (or commutes) | @prp-and-commutes; @exm-disjunction-first-derivations |
| \( (P \wedge Q) \wedge R \vdash P \wedge (Q \wedge R) \); \( P \vee (Q \vee R) \vdash (P \vee Q) \vee R \) | (and regroups); (or regroups) | @prp-and-associative; @exm-disjunction-regroup |
| \( P \wedge (Q \vee R) \dashv\vdash (P \wedge Q) \vee (P \wedge R) \) | (distributivity) | @prp-distributivity |
| \( P \leftrightarrow Q \vdash Q \leftrightarrow P \) | (iff symmetric) | @exm-iff-symmetric |
| \( P \leftrightarrow Q \dashv\vdash (P \to Q) \wedge (Q \to P) \) | (iff as two implications) | @prp-iff-two-implications |
| \( P \to Q, \ Q \to R, \ R \to P \vdash P \leftrightarrow Q \) | (equivalence cycle) | @prp-equivalence-cycle |
| **To change the task** (facts about derivations, not lines) | | |
| more premises never hurt; a derived statement may be used as a premise | (weakening, cut) | @lem-weakening-cut |
| \( \Gamma \vdash \varphi \) exactly when \( \Gamma, \neg\varphi \) is inconsistent | — | @prp-derivable-iff-negation-inconsistent |
| an inconsistent list derives every statement | — | @prp-inconsistent-derives-everything |

Rows proved in exercises (the second form of \( \rulename{DS} \), the two dilemma rows of @exr-derived-rules-b4) may be used by exercises, as in Section 3.1; the text's own derivations use only rows proved in the text.

::: {.check}
Which row would you look up first? (i) The goal is \( \neg(P \vee Q) \). (ii) A resource is \( \neg(P \wedge Q) \), and the goal is \( \neg P \vee \neg Q \). (iii) The resources include \( P \to Q \) and \( \neg Q \).
:::

::: {.solution}
(i) \( \rulename{DM} \) (b), under "To reach a negation". (ii) \( \rulename{DM} \) (d), which gives the goal in one line. (iii) \( \rulename{MT} \).
:::

::: {.remark}
[Looking ahead]

We show that something is derivable by exhibiting a derivation; how could we ever show that something is not? Chapter 4 gives each statement a truth value and proves that the rules never lead from true premises to a false conclusion. Then one choice of truth values, such as \( P \) false and \( Q \) true for the failed search of Section 3.1, proves that no derivation exists.
:::

## Exercises

### A. Check your understanding

::: {#exr-from-argument-to-derivation-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. In "Since \( n^2 \) is even, \( n \) is even", which is the premise and which the conclusion?
2. Find the conclusion: "\( n \) is odd, for \( n \) is prime and greater than \( 10 \)."
3. Name the unstated fact: "\( n \) is a multiple of \( 6 \), so \( n \) is even."
4. On the key of this section, translate "\( n \) is an odd prime at most \( 10 \)."
5. In @exm-two-columns, which sentence of the proof is line 5, and what does line 5's annotation read?
:::
:::

::: {.solution}
(a) The premise is "\( n^2 \) is even"; the conclusion is "\( n \) is even".

(b) "\( n \) is odd". *For* introduces the premise.

(c) Every multiple of \( 6 \) is even: if \( 6 \mid n \), then \( 2 \mid n \).

(d) \( (\neg E \wedge P) \wedge \neg G \).

(e) "If \( n \) were a multiple of \( 3 \)"; the annotation reads "asm, for \( \rulename{\neg I} \)".
:::

### B. Practice

::: {#exr-from-argument-to-derivation-b1}
[B1: Extract, then derive]

For each paragraph, find the conclusion, the stated premises and any unstated fact; choose letters; write the sequent; derive it.

::: {.enumerate options="label=(\alph*)"}
1. Let \( x \) be a real number with \( x^2 \le x \). If \( x \) were greater than \( 1 \), then \( x^2 = x \cdot x \) would be greater than \( x \). If \( x \) were negative, \( x^2 \) would be positive, hence greater than \( x \). So \( x \) is at least \( 0 \) and at most \( 1 \).
2. Let \( n \) be an integer. Since \( n^2 \) is odd, \( n \) is odd.
3. Let \( a \) and \( b \) be real numbers with \( ab = 0 \). If \( a \ne 0 \), we may divide by \( a \) and find \( b = 0 \). So \( a = 0 \) or \( b = 0 \).
:::
:::

::: {.solution}
(a) Take \( A \): "\( x > 1 \)", \( B \): "\( x < 0 \)", \( C \): "\( x^2 > x \)". The paragraph states two facts, each with its reason: \( A \to C \) and \( B \to C \). The premise "\( x^2 \le x \)" is \( \neg C \), by the convention of Section 2.1. The conclusion "at least \( 0 \) and at most \( 1 \)" is \( \neg B \wedge \neg A \), by the same convention. The sequent is \( A \to C, \ B \to C, \ \neg C \vdash \neg B \wedge \neg A \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A \to C}
  \hypo {2} {B \to C}
  \hypo {3} {\neg C}
  \have {4} {\neg A} \mt{1,3}
  \have {5} {\neg B} \mt{2,3}
  \have {6} {\neg B \wedge \neg A} \ai{5,4}
\end{nd}$
\end{center}
```

Nothing is unstated here except the order convention.

(b) Take \( E \): "\( n \) is even", \( S \): "\( n^2 \) is even". The premise is \( \neg S \) and the conclusion \( \neg E \). The unstated fact is \( E \to S \), "the square of an even integer is even", which is true since \( (2k)^2 = 4k^2 = 2(2k^2) \). The sequent is \( E \to S, \ \neg S \vdash \neg E \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \to S}
  \hypo {2} {\neg S}
  \have {3} {\neg E} \mt{1,2}
\end{nd}$
\end{center}
```

The tempting wrong supply is "the square of an odd integer is odd", \( \neg E \to \neg S \). It is true, but with the premise \( \neg S \) it gives nothing: concluding \( \neg E \) from it would be affirming the consequent (Section 1.3).

(c) Take \( A \): "\( a = 0 \)", \( B \): "\( b = 0 \)", \( Z \): "\( ab = 0 \)". The stated fact is \( (Z \wedge \neg A) \to B \), dividing by \( a \): \( b = a^{-1}(ab) = 0 \). The premise is \( Z \) and the conclusion \( A \vee B \). Neither side of the goal is in hand, so we split on \( A \) by \( \rulename{LEM} \), Section 3.1's step 5, as in @exm-equivalence-search.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(Z \wedge \neg A) \to B}
  \hypo {2} {Z}
  \have {3} {A \vee \neg A} \lem{}
  \open
  \hypo {4} {A}
  \have {5} {A \vee B} \oi{4}
  \close
  \open
  \hypo {6} {\neg A}
  \have {7} {Z \wedge \neg A} \ai{2,6}
  \have {8} {B} \ie{1,7}
  \have {9} {A \vee B} \oi{8}
  \close
  \have {10} {A \vee B} \oe{3,4-5,6-9}
\end{nd}$
\end{center}
```
:::

::: {#exr-from-argument-to-derivation-b2}
[B2: Two columns]

Let \( n \) be an integer. Claim: if \( n \) is prime and \( n > 10 \), then \( n \) is not a multiple of \( 6 \).

> *Proof.* Suppose \( n \) is prime and \( n > 10 \). If \( n \) were a multiple of \( 6 \), it would be an even multiple of \( 3 \), and no even multiple of \( 3 \) is prime; but \( n \) is prime. So \( n \) is not a multiple of \( 6 \).

::: {.enumerate options="label=(\alph*)"}
1. On the key, "\( n \) is a multiple of \( 6 \)" is \( E \wedge T \). The derivation the proof mirrors has reached the stage below. *Name the move, then complete it.*

    ```{=latex}
    % schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
    \begin{center}
    $\begin{nd}
      \hypo {1} {(E \wedge T) \to \neg P}
      \open
      \hypo {2} {P \wedge G} \purpose{\ii}
      \have[\ ][0] {} {\vdots}
      \have[][7] {7} {\neg (E \wedge T)}
      \close
      \have {8} {(P \wedge G) \to \neg (E \wedge T)} \ii{2-7}
    \end{nd}$
    \end{center}
    ```
2. Write the two-column table.
3. Which hypothesis does the derivation never cite? What claim does that show, and is it true?
:::
:::

::: {.solution}
(a) The goal \( \neg(E \wedge T) \) is a negation, so step 2 of the method opens a \( \rulename{\neg I} \) box on \( E \wedge T \). F3 fires on it, and the clash partner \( P \) comes from line 2.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(E \wedge T) \to \neg P}
  \open
  \hypo {2} {P \wedge G}
  \have {3} {P} \ae{2}
  \open
  \hypo {4} {E \wedge T}
  \have {5} {\neg P} \ie{1,4}
  \have {6} {\bot} \ne{3,5}
  \close
  \have {7} {\neg (E \wedge T)} \ni{4-6}
  \close
  \have {8} {(P \wedge G) \to \neg (E \wedge T)} \ii{2-7}
\end{nd}$
\end{center}
```

(b) The two columns:

| The proof | The derivation |
|---|---|
| "Suppose \( n \) is prime and \( n > 10 \)." | 2 |
| (silent) | 3 |
| "If \( n \) were a multiple of \( 6 \)," | 4 |
| "it would be an even multiple of \( 3 \), and no even multiple of \( 3 \) is prime;" | 1 (F3), 5 |
| "but \( n \) is prime." | 6 |
| "So \( n \) is not a multiple of \( 6 \)." | 7 |
| (the claim) | 8 |

Line 4 already is \( E \wedge T \), so "an even multiple of \( 3 \)" is a rereading, not a step.

(c) \( G \), that is, \( n > 10 \), is never cited: no line uses it. Lines 3–7, with \( P \) as the box's assumption, would derive \( (E \wedge T) \to \neg P \vdash P \to \neg(E \wedge T) \): no prime is a multiple of \( 6 \). That is true for every integer, by F3. The hypothesis \( n > 10 \) was idle.
:::

::: {#exr-from-argument-to-derivation-b3}
[B3: Fifteen items]

Items 1–5: derive each sequent, using a row of the library where it shortens the derivation, and name the row. Items 6–10: translate on the key, using the facts F1–F3 as premises where needed, and derive. Items 11–15: derive or break. The facts may be used as premises. A break is an integer \( n \) at which the premises are true and the conclusion false; since F1–F3 hold at every \( n \), such an \( n \) makes the whole counterexample set true.

*Derive, with the library.*

::: {.enumerate options="label=\arabic*."}
1. \( \neg(P \vee Q) \vdash P \to R \).
2. \( P \vee Q, \ P \to R, \ \neg R \vdash Q \wedge \neg P \).
3. \( \neg(P \wedge \neg Q) \vdash P \to Q \).
4. \( (P \vee Q) \to R \vdash \neg R \to (\neg P \wedge \neg Q) \).
5. \( \neg P \to Q, \ \neg Q \vdash P \wedge (\neg Q \vee R) \).
:::

*Translate on the key, then derive.*

::: {.enumerate options="label=\arabic*."}
6. \( n \) is an even multiple of \( 3 \); so \( n \) is not prime, and \( n \) is not a prime greater than \( 10 \).
7. \( n \) is a prime at most \( 10 \), or \( n \) is odd; so if \( n \) is even, \( n \) is at most \( 10 \).
8. \( n \) is a prime multiple of \( 3 \); so \( n \) is at most \( 10 \), and \( n \) is odd.
9. \( n \) is prime; \( n \) is not a multiple of \( 3 \) or \( n \) is at most \( 10 \); and \( n \) is a multiple of \( 3 \). So \( n \) is at most \( 10 \).
10. If \( n \) is greater than \( 10 \), then \( n \) is not an even prime.
:::

*Derive or break.*

::: {.enumerate options="label=\arabic*."}
11. \( n \) is even but not a multiple of \( 3 \); so \( n \) is not prime.
12. \( n \) is an even prime; so \( n \) is at most \( 10 \).
13. \( n \) is odd and greater than \( 10 \); so \( n \) is prime.
14. \( n \) is odd; so \( n \) is not an even prime.
15. \( n \) is not prime; so \( n \) is even or a multiple of \( 3 \).
:::
:::

::: {.solution}
**1.** \( \rulename{DM} \) (a), then VI.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \have {2} {\neg P \wedge \neg Q} \dm{1}
  \have {3} {\neg P} \ae{2}
  \have {4} {P \to R} \by{VI}{3}
\end{nd}$
\end{center}
```

**2.** \( \rulename{MT} \), then \( \rulename{DS} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {\neg R}
  \have {4} {\neg P} \mt{2,3}
  \have {5} {Q} \ds{1,4}
  \have {6} {Q \wedge \neg P} \ai{5,4}
\end{nd}$
\end{center}
```

**3.** No row helps. The goal is an implication; inside its box the goal \( Q \) is a letter, so \( \rulename{RAA} \) on \( \neg Q \), which clashes with the premise once \( P \wedge \neg Q \) is built.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge \neg Q)}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {P \wedge \neg Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \have {7} {P \to Q} \ii{2-6}
\end{nd}$
\end{center}
```

The library route (\( \rulename{DM} \) (d) on the premise, then \( \rulename{\neg\neg I} \), \( \rulename{DS} \) and \( \rulename{\neg\neg E} \) inside the box) is no shorter. A library row is worth citing only when it saves lines.

**4.** \( \rulename{MT} \), then \( \rulename{DM} \) (a), inside one box.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \open
  \hypo {2} {\neg R}
  \have {3} {\neg (P \vee Q)} \mt{1,2}
  \have {4} {\neg P \wedge \neg Q} \dm{3}
  \close
  \have {5} {\neg R \to (\neg P \wedge \neg Q)} \ii{2-4}
\end{nd}$
\end{center}
```

**5.** \( \rulename{MT} \), then \( \rulename{\neg\neg E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to Q}
  \hypo {2} {\neg Q}
  \have {3} {\neg\neg P} \mt{1,2}
  \have {4} {P} \nne{3}
  \have {5} {\neg Q \vee R} \oi{2}
  \have {6} {P \wedge (\neg Q \vee R)} \ai{4,5}
\end{nd}$
\end{center}
```

**6.** \( E \wedge T, \ (E \wedge T) \to \neg P \vdash \neg P \wedge \neg(P \wedge G) \), with F3.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \wedge T}
  \hypo {2} {(E \wedge T) \to \neg P}
  \have {3} {\neg P} \ie{2,1}
  \open
  \hypo {4} {P \wedge G}
  \have {5} {P} \ae{4}
  \have {6} {\bot} \ne{5,3}
  \close
  \have {7} {\neg (P \wedge G)} \ni{4-6}
  \have {8} {\neg P \wedge \neg (P \wedge G)} \ai{3,7}
\end{nd}$
\end{center}
```

**7.** \( (P \wedge \neg G) \vee \neg E \vdash E \to \neg G \), with no fact needed.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge \neg G) \vee \neg E}
  \open
  \hypo {2} {E}
  \open
  \hypo {3} {P \wedge \neg G}
  \have {4} {\neg G} \ae{3}
  \close
  \open
  \hypo {5} {\neg E}
  \have {6} {\bot} \ne{2,5}
  \have {7} {\neg G} \be{6}
  \close
  \have {8} {\neg G} \oe{1,3-4,5-7}
  \close
  \have {9} {E \to \neg G} \ii{2-8}
\end{nd}$
\end{center}
```

**8.** \( P \wedge T, \ (P \wedge T) \to \neg G, \ (E \wedge T) \to \neg P \vdash \neg G \wedge \neg E \), with F2 and F3.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge T}
  \hypo {2} {(P \wedge T) \to \neg G}
  \hypo {3} {(E \wedge T) \to \neg P}
  \have {4} {\neg G} \ie{2,1}
  \have {5} {P} \ae{1}
  \have {6} {T} \ae{1}
  \open
  \hypo {7} {E}
  \have {8} {E \wedge T} \ai{7,6}
  \have {9} {\neg P} \ie{3,8}
  \have {10} {\bot} \ne{5,9}
  \close
  \have {11} {\neg E} \ni{7-10}
  \have {12} {\neg G \wedge \neg E} \ai{4,11}
\end{nd}$
\end{center}
```

**9.** \( P, \ \neg T \vee \neg G, \ T \vdash \neg G \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {\neg T \vee \neg G}
  \hypo {3} {T}
  \have {4} {\neg\neg T} \nni{3}
  \have {5} {\neg G} \ds{2,4}
\end{nd}$
\end{center}
```

The premise \( P \) is not needed.

**10.** \( (P \wedge E) \to \neg G \vdash G \to \neg(P \wedge E) \), with F1.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge E) \to \neg G}
  \open
  \hypo {2} {G}
  \open
  \hypo {3} {P \wedge E}
  \have {4} {\neg G} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {\neg (P \wedge E)} \ni{3-5}
  \close
  \have {7} {G \to \neg (P \wedge E)} \ii{2-6}
\end{nd}$
\end{center}
```

With the library, lines 3–6 shrink to two: 3 \( \neg\neg G \), \( \rulename{\neg\neg I} \) 2; 4 \( \neg(P \wedge E) \), \( \rulename{MT} \) 1, 3.

**11.** Breaks. The claim is \( E \wedge \neg T \vdash \neg P \), and at \( n = 2 \) the integer is even, not a multiple of \( 3 \), and prime.

**12.** Derives: \( P \wedge E, \ (P \wedge E) \to \neg G \vdash \neg G \), with F1.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge E}
  \hypo {2} {(P \wedge E) \to \neg G}
  \have {3} {\neg G} \ie{2,1}
\end{nd}$
\end{center}
```

**13.** Breaks. The claim is \( \neg E \wedge G \vdash P \), and at \( n = 15 \) the integer is odd, greater than \( 10 \), and not prime.

**14.** Derives: \( \neg E \vdash \neg(P \wedge E) \). No fact is needed.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg E}
  \open
  \hypo {2} {P \wedge E}
  \have {3} {E} \ae{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg (P \wedge E)} \ni{2-4}
\end{nd}$
\end{center}
```

**15.** Breaks. The claim is \( \neg P \vdash E \vee T \), and at \( n = 25 \) the integer is not prime, odd, and not a multiple of \( 3 \).

Items 11 and 12, and items 13 and 14, pair a break with a derivation on nearby words; item 15 runs F3 the other way, from "not prime" back to "even or a multiple of \( 3 \)", and fails.
:::

::: {#exr-from-argument-to-derivation-b4}
[B4: Put the proof in order]

Let \( a \) and \( b \) be real numbers. Claim: if \( a + b > 2 \), then \( a > 1 \) or \( b > 1 \).

::: {.enumerate options="label=(\roman*)"}
1. This contradicts \( a + b > 2 \).
2. Suppose \( a + b > 2 \).
3. Then \( a > 1 \), since \( a + b > 2 \).
4. Adding, \( a + b \le 2 \).
5. Hence \( a > 1 \) or \( b > 1 \).
6. Suppose, for a contradiction, that neither \( a > 1 \) nor \( b > 1 \).
7. Suppose \( a > 1 \) or \( b > 1 \).
8. Then \( a \le 1 \) and \( b \le 1 \).
:::

::: {.enumerate options="label=(\alph*)"}
1. Put six of these sentences in an order that proves the claim; two do not belong.
2. Match each sentence of your order to a line of the derivation below, with \( A \): "\( a > 1 \)", \( B \): "\( b > 1 \)", \( S \): "\( a + b > 2 \)".
:::

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(\neg A \wedge \neg B) \to \neg S}
  \open
  \hypo {2} {S}
  \open
  \hypo {3} {\neg (A \vee B)}
  \have {4} {\neg A \wedge \neg B} \dm{3}
  \have {5} {\neg S} \ie{1,4}
  \have {6} {\bot} \ne{2,5}
  \close
  \have {7} {A \vee B} \raa{3-6}
  \close
  \have {8} {S \to (A \vee B)} \ii{2-7}
\end{nd}$
\end{center}
```
:::

::: {.solution}
(a) (ii), (vi), (viii), (iv), (i), (v). No other order is admissible: each sentence uses the one before it. The two distractors:

- (iii) does not follow: \( a = 0 \), \( b = 3 \) has \( a + b > 2 \) and \( a \le 1 \).
- (vii) assumes the conclusion, a box opened on the goal (Section 3.1's warning "Do not assume what you want to prove").

(b) (ii) is line 2, "asm, for \( \rulename{{\to}I} \)". (vi) is line 3, "asm, for \( \rulename{RAA} \)". (viii) is line 4, by \( \rulename{DM} \) and the order convention of Section 2.1 (\( \neg(a > 1) \) is \( a \le 1 \)). (iv) is line 5, with the fact on line 1: adding the two inequalities. (i) is line 6, and (v) is line 7. The claim is line 8. The fact on line 1 is the one step of school algebra: \( a \le 1 \) and \( b \le 1 \) give \( a + b \le 2 \).
:::

### C. Going deeper

::: {#exr-from-argument-to-derivation-c1}
[C1: Exit check: from a paragraph to a derivation]

> Let \( n \) be an integer greater than \( 10 \), and suppose \( n \) is even or a multiple of \( 3 \). Then \( n \) is not prime. Indeed, suppose \( n \) were prime. If \( n \) is even, \( n \) is an even prime, and every even prime is at most \( 10 \). If \( n \) is a multiple of \( 3 \), \( n \) is a prime multiple of \( 3 \), and every such number is at most \( 10 \). Either way \( n \) is at most \( 10 \), which is false. So \( n \) is not prime.

::: {.enumerate options="label=(\alph*)"}
1. Name the conclusion, the stated premises, and the facts the paragraph gives as reasons, each on the key.
2. Write the sequent.
3. Derive it.
4. Write the two-column table.
5. Is the premise "\( n > 10 \)" needed? Break the claim without it.
:::
:::

::: {.solution}
(a) The conclusion is \( \neg P \). The premises are \( G \) and \( E \vee T \). The facts are F1 ("every even prime is at most \( 10 \)") and F2.

(b) \( G, \ E \vee T, \ (P \wedge E) \to \neg G, \ (P \wedge T) \to \neg G \vdash \neg P \).

(c) The goal is a negation: a \( \rulename{\neg I} \) box on \( P \). Inside it, the resource \( E \vee T \) is split, each case reaching \( \neg G \) by its fact, and \( \neg G \) clashes with \( G \) outside the cases.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {G}
  \hypo {2} {E \vee T}
  \hypo {3} {(P \wedge E) \to \neg G}
  \hypo {4} {(P \wedge T) \to \neg G}
  \open
  \hypo {5} {P}
  \open
  \hypo {6} {E}
  \have {7} {P \wedge E} \ai{5,6}
  \have {8} {\neg G} \ie{3,7}
  \close
  \open
  \hypo {9} {T}
  \have {10} {P \wedge T} \ai{5,9}
  \have {11} {\neg G} \ie{4,10}
  \close
  \have {12} {\neg G} \oe{2,6-8,9-11}
  \have {13} {\bot} \ne{1,12}
  \close
  \have {14} {\neg P} \ni{5-13}
\end{nd}$
\end{center}
```

(d) The two columns:

| The proof | The derivation |
|---|---|
| "Let \( n \) … greater than \( 10 \), and suppose \( n \) is even or a multiple of \( 3 \)." | 1, 2 |
| "Then \( n \) is not prime." | the goal, line 14 |
| "suppose \( n \) were prime." | 5 (asm, for \( \rulename{\neg I} \)) |
| "If \( n \) is even, … at most \( 10 \)." | 6–8, with 3 |
| "If \( n \) is a multiple of \( 3 \), … at most \( 10 \)." | 9–11, with 4 |
| "Either way \( n \) is at most \( 10 \)," | 12 |
| "which is false." | 13 |
| "So \( n \) is not prime." | 14 |

(e) It is needed. Without \( G \), the claim \( E \vee T, \ (P \wedge E) \to \neg G, \ (P \wedge T) \to \neg G \vdash \neg P \) breaks at \( n = 2 \): \( 2 \) is even, so \( E \vee T \) holds; F1 and F2 hold, as at every \( n \); and \( 2 \) is prime, so the negated conclusion \( \neg\neg P \) is true too.

**Marking scheme.** (10 points)

- 2: (a)–(b), the sequent, with F1 and F2 named as the facts given as reasons, in implication form.
- 3: (c), the \( \rulename{\neg I} \) box on \( P \), the two cases both ending in \( \neg G \), and the clash with \( G \) outside the cases.
- 2: (d), every sentence placed, the two "suppose"s matched to their annotations.
- 3: (e), "needed", with a break that makes every member of the new counterexample set true.

Fatal errors (0 for the step): \( \neg P \) taken as a premise; the cases of \( \rulename{\vee E} \) ending in different statements; a "break" in (e) at an \( n \) where a premise fails. A derivation that splits \( E \vee T \) first and opens a \( \rulename{\neg I} \) box in each case earns full marks for (c).
:::

::: {#exr-from-argument-to-derivation-c2}
[C2: Challenge: A statement that promises anything]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( C \leftrightarrow (C \to Q) \vdash Q \).
2. Let \( Q \) be "\( 0 = 1 \)". What does (a) say about a statement \( C \) that is equivalent to "if \( C \), then \( 0 = 1 \)"?
3. Which rules does your derivation use? Compare @lem-not-iff-own-negation.
:::
:::

::: {.solution}
(a) The premise gives nothing until one side of the iff is on a line. The side \( C \to Q \) is an implication, and its box can use the premise on its own assumption.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {C \leftrightarrow (C \to Q)}
  \open
  \hypo {2} {C}
  \have {3} {C \to Q} \bie{1,2}
  \have {4} {Q} \ie{3,2}
  \close
  \have {5} {C \to Q} \ii{2-4}
  \have {6} {C} \bie{1,5}
  \have {7} {C \to Q} \bie{1,6}
  \have {8} {Q} \ie{7,6}
\end{nd}$
\end{center}
```

The shorter ending 7 \( Q \), \( \rulename{{\to}E} \) 5, 6 is a detour: line 5 was built by \( \rulename{{\to}I} \) and is taken apart at once. Cutting it costs a line here, because line 5 is cited again at line 6, so it stays. This is the case Section 3.1 names: cutting a detour need not shorten a derivation, and the rule is advice, not a theorem.

(b) Read as an argument, the derivation proves \( 0 = 1 \) from the condition on \( C \). So no statement can meet the condition. In this chapter's words, the list \( C \leftrightarrow (C \to Q), \ \neg Q \) is inconsistent: add the premise \( \neg Q \) and the line 9 \( \bot \), \( \rulename{\neg E} \) 8 and that premise.

(c) Only \( \rulename{{\leftrightarrow}E} \), \( \rulename{{\to}I} \) and \( \rulename{{\to}E} \): no rule for \( \neg \) or \( \bot \), and no \( \rulename{RAA} \). @lem-not-iff-own-negation shows that no statement is equivalent to its own negation. This shows more: it holds for "if \( C \), then \( Q \)" with any \( Q \), and without "not". The trouble is self-reference, not negation. This is known as Curry's paradox, after the logician whose name is also on the law @prp-curry. Section 5.6 meets the same shape with "for every", in the barber and Russell's theorem.

**Marking scheme.** (10 points)

- 4: (a), the box on \( C \) (lines 2–4, with the assumption \( C \) cited twice), \( C \) recovered outside it by \( \rulename{{\leftrightarrow}E} \) (line 6), and \( Q \) reached outside every box. The 7-line ending \( \rulename{{\to}E} \) 5, 6 earns full marks; the detour remark is not required.
- 3: (b), the conclusion that no statement meets the condition, with the inconsistency.
- 3: (c), the rules named, and the point that no negation rule is used.

Fatal error (0 for (a)): \( Q \) obtained inside the box and carried out of it.
:::

### R. Review

::: {#exr-finding-derivations-r1}
[R1]

For real numbers \( a \) and \( b \), let \( \max(a, b) \coloneqq a \) and \( \min(a, b) \coloneqq b \) if \( a \ge b \), and \( \max(a, b) \coloneqq b \) and \( \min(a, b) \coloneqq a \) if \( a < b \). Prove that \( \max(a, b) + \min(a, b) = a + b \).
:::

::: {.solution}
Since \( a \ge b \) or \( a < b \), and these two cases cover every pair of real numbers, we argue by cases (\( \rulename{\vee E} \), @def-rules-disjunction), as in @exm-abs-product-cases.

*Case \( a \ge b \).* Then \( \max(a, b) = a \) and \( \min(a, b) = b \), so \( \max(a, b) + \min(a, b) = a + b \).

*Case \( a < b \).* Then \( \max(a, b) = b \) and \( \min(a, b) = a \), so \( \max(a, b) + \min(a, b) = b + a = a + b \).

In either case the equation holds, which proves it. Both cases end in the same statement, the goal, as \( \rulename{\vee E} \) requires.
:::

::: {#exr-finding-derivations-r2}
[R2]

Let \( x \) be a real number. Write \( N \) for "\( x < 0 \)", \( G \) for "\( x > 1 \)", and \( S \) for "\( x = 7 \)". Translate the argument below into a sequent in these letters, and derive it.

> \( x \) is neither negative nor greater than \( 1 \). Therefore \( x \) is not negative, and if \( x \) is greater than \( 1 \), then \( x = 7 \).
:::

::: {.solution}
"Neither \( N \) nor \( G \)" says that \( N \vee G \) fails, so the premise is \( \neg(N \vee G) \), not \( \neg N \vee G \). The conclusion is a conjunction whose second part is an implication. The sequent (@def-sequent) is
\[
\neg(N \vee G) \vdash \neg N \wedge (G \to S).
\]
The goal is a conjunction; the first conjunct is a negation (a \( \rulename{\neg I} \) box on \( N \)), and the second an implication (a box on \( G \)). In both boxes \( \rulename{\vee I} \) builds \( N \vee G \), which clashes with the premise; in the second box \( \rulename{\bot E} \) then gives \( S \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (N \vee G)}
  \open
  \hypo {2} {N}
  \have {3} {N \vee G} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg N} \ni{2-4}
  \open
  \hypo {6} {G}
  \have {7} {N \vee G} \oi{6}
  \have {8} {\bot} \ne{7,1}
  \have {9} {S} \be{8}
  \close
  \have {10} {G \to S} \ii{6-9}
  \have {11} {\neg N \wedge (G \to S)} \ai{5,10}
\end{nd}$
\end{center}
```

Lines 2–5 are half of @prp-de-morgan (a), which turns "neither … nor" into \( \neg N \wedge \neg G \). The implication \( G \to S \) is vacuously true, as in @prp-vacuous-implication: the premise rules out \( G \), and a promise never tested is never broken, whatever \( S \) says.
:::

::: {#exr-finding-derivations-r3}
[R3]

Is \( (P \to Q) \to R \vdash P \to (Q \to R) \) derivable? Derive or break its converse, \( P \to (Q \to R) \vdash (P \to Q) \to R \).
:::

::: {.solution}
The first is derivable, by the search method of Section 3.1. The goal gives a box on \( P \), then a box on \( Q \), with the goal \( R \). The premise gives \( R \) by \( \rulename{{\to}E} \) once we produce \( P \to Q \), a new goal: a box on \( P \) whose last line repeats \( Q \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {R} \ie{1,6}
  \close
  \have {8} {Q \to R} \ii{3-7}
  \close
  \have {9} {P \to (Q \to R)} \ii{2-8}
\end{nd}$
\end{center}
```

The repetition at line 5 puts \( Q \) inside the box of line 4, as \( \rulename{{\to}I} \) requires (clause (D3) of @def-derivation). Two look-alike tools do not apply. @prp-curry moves a **conjunction** in and out of a hypothesis, \( (P \wedge Q) \to R \dashv\vdash P \to (Q \to R) \), and the premise here has \( P \to Q \), not \( P \wedge Q \), in that place. And @prp-implication-transitive chains two implications, which we do not have.

The converse breaks: with \( P \) and \( R \) false (and \( Q \) either way), the premise \( P \to (Q \to R) \) is true because \( P \) is false, while \( P \to Q \) is true and \( R \) is false, so the conclusion is false. Chapter 4 proves that such a choice rules out every derivation, so that a search for it can only stall: the chapter's open question, in a new place.
:::

::: {#exr-from-argument-to-derivation-r4}
[R4]

Ana and Ben talk about a real number.

> **Ana.** Let \( x \) be a real number with \( x^2 < x \). Then \( x \) is positive.
>
> **Ben.** Why can't it be negative?
>
> **Ana.** A negative number is less than its square.
>
> **Ben.** And zero?
>
> **Ana.** At zero, \( x^2 \) equals \( x \). And \( x \) is less than \( 1 \), because for \( x \ge 1 \) we would have \( x^2 \ge x \).
>
> **Ben.** So \( 0 < x < 1 \). But you never said why \( x^2 \ge x \) when \( x \ge 1 \).
>
> **Ana.** Multiply \( x \ge 1 \) by \( x \), which is positive.

::: {.enumerate options="label=(\alph*)"}
1. What is the conclusion, and who states it?
2. With \( N \): "\( x < 0 \)", \( Z \): "\( x = 0 \)", \( B \): "\( x \ge 1 \)", \( L \): "\( x^2 < x \)", write the premise, the three facts used, and the sequent.
3. Derive it.
4. Is Ana's last answer enough?
:::
:::

::: {.solution}
(a) "\( 0 < x < 1 \)", stated by Ben. Ana's first line, "\( x \) is positive", is an intermediate step.

(b) The premise is \( L \). The facts:

- \( N \to \neg L \) (Ana: a negative \( x \) has \( x^2 > 0 > x \));
- \( Z \to \neg L \) (Ana: \( x^2 = x \) at \( 0 \));
- \( B \to \neg L \) (Ana, then justified at Ben's request).

The conclusion \( (\neg N \wedge \neg Z) \wedge \neg B \) reads as "\( x \ge 0 \), \( x \ne 0 \), \( x < 1 \)", that is, \( 0 < x < 1 \), by the convention of Section 2.1. The sequent is
\[
N \to \neg L, \ Z \to \neg L, \ B \to \neg L, \ L \vdash (\neg N \wedge \neg Z) \wedge \neg B.
\]

(c) \( \rulename{MT} \) (@prp-modus-tollens) needs the negation of each fact's conclusion, and that is \( \neg\neg L \), given by \( \rulename{\neg\neg I} \) (@prp-double-negation (a)); hence line 5.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {N \to \neg L}
  \hypo {2} {Z \to \neg L}
  \hypo {3} {B \to \neg L}
  \hypo {4} {L}
  \have {5} {\neg\neg L} \nni{4}
  \have {6} {\neg N} \mt{1,5}
  \have {7} {\neg Z} \mt{2,5}
  \have {8} {\neg B} \mt{3,5}
  \have {9} {\neg N \wedge \neg Z} \ai{6,7}
  \have {10} {(\neg N \wedge \neg Z) \wedge \neg B} \ai{9,8}
\end{nd}$
\end{center}
```

(d) Yes: \( x \ge 1 \) gives \( x > 0 \), and multiplying \( x \ge 1 \) by the positive \( x \) gives \( x^2 \ge x \).

The method is the extraction of this section (@exm-extract-argument), run on a dialogue; the rules are Chapter 2's.
:::

<!-- dependency ledger
from-argument-to-derivation-key (claim): F1-F3 true for every integer n (the only even prime is 2; the only prime multiple of 3 is 3; a multiple of 6 that is positive exceeds 2 and has divisor 2; 0 and negatives not prime) | school arithmetic, "prime" as defined in the section; checked by verify/ch03/exm-extract-argument.py for |n| <= 500
exm-extract-argument (example): "the only even prime is 2" used as F1, "the only prime multiple of 3 is 3" used as F2 | inline (from the facts' reasons)
exr-from-argument-to-derivation-a1 (solution): (c) 6 | n implies 2 | n | school arithmetic
exr-from-argument-to-derivation-b1 (solution): (a) x > 1 implies x^2 > x; x < 0 implies x^2 > 0 > x; (b) (2k)^2 = 2(2k^2); (c) ab = 0 and a != 0 give b = a^{-1}(ab) = 0 | school algebra, AN1.1 (promised)
exr-from-argument-to-derivation-b3 (solution): breaks at n = 2, 15, 25 (2 prime and even, not a multiple of 3; 15 odd, > 10, not prime; 25 odd, not prime, not a multiple of 3) | school arithmetic; checked by verify/ch03/exr-from-argument-to-derivation-b3.py
exr-from-argument-to-derivation-b4 (solution): a <= 1 and b <= 1 give a + b <= 2; a = 0, b = 3 has a + b > 2 and a <= 1 | school algebra, AN1.1 (promised)
exr-from-argument-to-derivation-c1 (solution): (e) 2 is even and prime and not > 10 | school arithmetic
exr-from-argument-to-derivation-c2 (solution): (b) "no statement can meet the condition" read from the derivation as an argument | inline (the derivation read as an argument, as every example of the book is)
exr-from-argument-to-derivation-r4 (solution): x < 0 gives x^2 > 0 > x; x^2 = x at 0; x >= 1 and x > 0 give x^2 >= x | school algebra, AN1.1 (promised)
exr-finding-derivations-r1 (solution): a >= b or a < b for real numbers; b + a = a + b | school algebra, AN1.1 (promised)
exr-finding-derivations-r3 (solution): the converse breaks (P = R = false); that such a choice rules out every derivation | the break inline; the consequence F1.3 (promised; cor-refuting-row), stated as a plain pointer
-->
