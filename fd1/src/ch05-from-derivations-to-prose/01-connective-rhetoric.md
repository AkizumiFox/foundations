# The Connective Rules in Prose

Chapters 1–4 built a calculus in which every step of a proof is one rule applied to lines that are available. Mathematicians do not write Fitch boxes, and from Part I on neither does this book; yet every proof in it is a derivation underneath, written in sentences. This section and the next compile the dictionary between the two: for each rule, the phrases that carry it in written mathematics, a sentence of analysis in which it does its work, and whether a writer may leave it unsaid. This section covers the connectives and the classical rules; Section 5.2 covers the quantifiers, equality and induction.

## The same proof, twice

Section 2.1 proved @thm-square-even-implies-even ("if \( n^2 \) is even, then \( n \) is even") by cases, and printed a table that matched each line of its derivation with one sentence of the proof. Section 2.3 proved the same theorem a second way, in @exm-square-even-via-contrapositive, with the derived rules \( \rulename{CP} \) and \( \rulename{DS} \) doing the work. Here is that second derivation again, with \( E \): "\( n \) is even", \( O \): "\( n \) is odd", \( S \): "\( n^2 \) is even", \( T \): "\( n^2 \) is odd", and the facts (E1)–(E3) of Section 2.1 (every integer is even or odd; no integer is both; the square of an odd integer is odd) as its premises.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \vee O}
  \hypo {2} {\neg (S \wedge T)}
  \hypo {3} {O \to T}
  \open
  \hypo {4} {S}
  \open
  \hypo {5} {T}
  \have {6} {S \wedge T} \ai{4,5}
  \have {7} {\bot} \ne{6,2}
  \close
  \have {8} {\neg T} \ni{5-7}
  \have {9} {\neg T \to \neg O} \ctp{3}
  \have {10} {\neg O} \ie{9,8}
  \have {11} {O \vee E} \by{or commutes}{1}
  \have {12} {E} \ds{11,10}
  \close
  \have {13} {S \to E} \ii{4-12}
\end{nd}$
\end{center}
```

A mathematician would write the same proof in four sentences:

> Suppose \( n^2 \) is even. If \( n^2 \) were odd, it would be both even and odd, which (E2) forbids; so \( n^2 \) is not odd. By (E3), read contrapositively, \( n \) is not odd. Since \( n \) is even or odd, by (E1), \( n \) is even.

The paragraph accounts for every line of the derivation, though some lines have no words of their own.

| Lines | Words that carry them | Rule |
|---|---|---|
| 4 | "Suppose \( n^2 \) is even." | \( \rulename{{\to}I} \), the box opens |
| 5 | "If \( n^2 \) were odd" | \( \rulename{\neg I} \), the box opens |
| 6 | "it would be both even and odd" | \( \rulename{\wedge I} \) |
| 7 | "which (E2) forbids" | \( \rulename{\neg E} \), citing premise 2 |
| 8 | "so \( n^2 \) is not odd" | \( \rulename{\neg I} \), the box closes |
| 9 | "By (E3), read contrapositively" | \( \rulename{CP} \), citing premise 3 |
| 10 | "\( n \) is not odd" | \( \rulename{{\to}E} \) |
| 11–12 | "Since \( n \) is even or odd, by (E1), \( n \) is even." | \( \rulename{DS} \), citing premise 1 |
| 13 | nothing | \( \rulename{{\to}I} \), the box closes |

Three features of the table recur through the whole dictionary. The **openings** of boxes always have words, which name what is assumed: "suppose", "if … were". Some lines have **no words**: line 13 closes the box of line 4, and the paragraph simply stops; line 11 only reorders the disjuncts of (E1) for the schema of @prp-disjunctive-syllogism, and prose does not see the order of a disjunction (the convention on silent steps of Section 5.3 lets the exchange be silent). And a **premise** is never a sentence of its own: it enters through its name, "(E2)" or "by (E1)", at the step that uses it.

::: {.check}
Which word of the paragraph tells the reader that line 5 is an assumption and not a claim, and what would the sentence assert if that word were replaced by "is"?
:::

::: {.solution}
The word "were" (with "if"): "if \( n^2 \) were odd" supposes something in order to refute it, which is the opening of a \( \rulename{\neg I} \) box. With "is", the sentence "\( n^2 \) is odd, so it is both even and odd" would assert \( T \) as a claim rather than an assumption: it would sit, unjustified, directly in the box of line 4, where it is in fact false (\( n^2 \) is even there), and the proof would be wrong.
:::

## How to read the dictionary

The dictionary is a set of rows, one per rule, grouped by connective. Each row has four entries.

- **The rule**, as Chapters 1, 2 and 4 named it, primitive or derived.
- **Phrases**, in the order a writer should prefer them; the later ones are variants a reader must recognize. They are not a fixed vocabulary: any wording that does the same job is correct.
- **An analysis sentence**, from a proof the reader has met or will meet in Part I, with the premises of the rule visible.
- **Whether the rule may be silent in plain prose.** Section 5.3 names four levels of writing, from the full derivation down to the plain prose of Part I onward, and turns this column into a convention. "Never" means that a proof which leaves the step out is incomplete, however obvious the step looks.

Readers who use the Lean proof assistant will find the Lean command for each primitive rule in the rule, phrase and Lean table that ends Section 4.7; nothing in this chapter depends on it.

Each group of rows is followed by a worked example, a short proof annotated phrase by phrase. A rule tag such as [\( \rulename{\wedge E} \)] after a phrase says which rule the phrase carries; proofs in Part 0 may carry such tags, and from Part I on they are dropped.

## Conjunction

| Rule | Phrases | Silent in plain prose? |
|---|---|---|
| \( \rulename{\wedge I} \) | "…, and …"; "we show (a) … and (b) …"; "both … hold" | often, when both conjuncts are displayed |
| \( \rulename{\wedge E} \) | "in particular"; "so \( a > 0 \)"; using one clause of a hypothesis without comment | yes |

In analysis, \( \rulename{\wedge I} \) is the shape of every definition with two clauses. "\( s \) is a least upper bound of \( A \)" will mean that \( s \) is an upper bound of \( A \) **and** no smaller number is an upper bound of \( A \); a proof of it has two parts, labeled (a) and (b), and ends by putting them together. (Chapter 11 states the second clause as "\( s \le M \) for every upper bound \( M \) of \( A \)", which says the same: by trichotomy, \( s \le M \) holds exactly when \( M < s \) fails, and an upper bound \( M \) with \( M < s \) would be a smaller one.) \( \rulename{\wedge E} \) is the step from a chain to one of its links: "since \( x \in (0, 1) \), in particular \( x > 0 \)" takes the left conjunct of \( 0 < x \wedge x < 1 \).

::: {#exm-rhetoric-conjunction}
[Two clauses of a least upper bound]

Let \( A \coloneqq \{ x \in \nR : 0 < x < 2 \} \). Prove that \( 2 \) is an upper bound of \( A \), and that no real number \( t < 2 \) is an upper bound of \( A \). Tag each step with its rule.
:::

::: {.solution}
*(a)* Let \( a \in A \) [\( \rulename{\forall I} \)]. Then \( 0 < a < 2 \), by the definition of \( A \); in particular \( a < 2 \) [\( \rulename{\wedge E} \)], so \( a \le 2 \) [\( \rulename{\vee I} \)]. So \( 2 \) is an upper bound of \( A \).

*(b)* Let \( t \) be a real number with \( t < 2 \) [\( \rulename{\forall I} \), \( \rulename{{\to}I} \)], and suppose \( t \) is an upper bound of \( A \) [assumption for \( \rulename{\neg I} \)]. Let \( m \coloneqq \max\{t, 0\} \) and \( a \coloneqq (m + 2)/2 \). We have \( t \ge 0 \) or \( t < 0 \), and by the definition of the maximum we consider the two cases [\( \rulename{\vee E} \)]: if \( t \ge 0 \), then \( m = t \), so \( m \ge t \), \( m \ge 0 \) and \( m < 2 \); if \( t < 0 \), then \( m = 0 \), so \( m > t \), \( m \ge 0 \) and \( m < 2 \). So in either case \( m \ge t \) and \( 0 \le m < 2 \). Hence \( 1 \le a < 2 \); thus \( 0 < a \) and \( a < 2 \), that is, \( a \in A \) [\( \rulename{\wedge I} \)]. As \( t \) is an upper bound of \( A \), \( a \le t \) [\( \rulename{\forall E} \) at \( a \)]. But \( a - m = (2 - m)/2 > 0 \), so \( a > m \ge t \), and \( a > t \). This contradicts \( a \le t \) [\( \rulename{\neg E} \)]. Hence \( t \) is not an upper bound of \( A \) [\( \rulename{\neg I} \)].

So \( 2 \) is an upper bound of \( A \), and no smaller number is [\( \rulename{\wedge I} \)].

The \( \rulename{\wedge E} \) of (a) could have been silent ("then \( a < 2 \), so \( a \le 2 \)"); the \( \rulename{\vee I} \) after it weakened a strict inequality, since \( a \le 2 \) means \( a < 2 \vee a = 2 \). In (b), the two conjuncts \( 0 < a \) and \( a < 2 \) were displayed and then merged by "that is, \( a \in A \)". The bound \( m < 2 \) needed the case split hidden in \( \max \), and it is written out, as the warning below requires. The final sentence is the \( \rulename{\wedge I} \) of the two clauses. And the clashing lines \( a \le t \) and \( a > t \) are both named before "contradicts", as the \( \rulename{\neg E} \) row below requires.
:::

## Implication

| Rule | Phrases | Silent in plain prose? |
|---|---|---|
| \( \rulename{{\to}I} \) | "assume …; then …; hence if … then …"; "suppose …"; "if …, then …" as the frame of a whole proof | never the assumption; the closing "hence" may be silent |
| \( \rulename{{\to}E} \) | "since …, …"; "by (hypothesis, lemma), …"; "hence" | the citation, never |
| \( \rulename{R} \) | "recall that"; "as noted above" | yes |
| \( \rulename{MT} \), \( \rulename{CP} \) | "…; so \( P \) cannot hold"; "we prove the contrapositive"; "equivalently, if not \( Q \) then not \( P \)" | the announcement "we prove the contrapositive", never |

In analysis, \( \rulename{{\to}I} \) is a proof that begins "Suppose \( \abs{x - 1} < 1 \)" and ends "so \( x > 0 \)"; the example below writes it out. \( \rulename{{\to}E} \) is every citation of a theorem: "since \( f \) is continuous at \( a \) and \( a_n \to a \), we have \( f(a_n) \to f(a) \)" applies an implication proved in Chapter 15 to two facts in hand, and the word "since" introduces those facts. For \( \rulename{CP} \), Section 2.3's @exm-square-even-via-contrapositive is the model, as the opening of this section showed. (@thm-square-even-implies-even itself is proved by cases, with no contraposition.)

::: {#exm-rhetoric-implication}
[A hypothesis assumed, a lemma cited, a contrapositive announced]

Let \( x \) be a real number. (a) Prove that if \( \abs{x - 1} < 1 \), then \( x > 0 \). (b) Deduce that if \( x \le 0 \), then \( \abs{x - 1} \ge 1 \). Tag each step with its rule.
:::

::: {.solution}
We use the school fact that, for real \( u \) and \( r \), \( \abs{u} < r \) holds exactly when \( -r < u < r \).

*(a)* Suppose \( \abs{x - 1} < 1 \) [assumption for \( \rulename{{\to}I} \)]. By the school fact, \( -1 < x - 1 < 1 \) [\( \rulename{{\leftrightarrow}E} \)], in particular \( -1 < x - 1 \) [\( \rulename{\wedge E} \)], so \( x > 0 \) [arith].

*(b)* Suppose \( x \le 0 \) [assumption for \( \rulename{{\to}I} \)]. Recall from (a) that \( \abs{x - 1} < 1 \) implies \( x > 0 \) [\( \rulename{R} \)]. Since \( x \le 0 \), that is, \( x > 0 \) fails, \( \abs{x - 1} < 1 \) cannot hold [\( \rulename{MT} \)], so \( \abs{x - 1} \ge 1 \).

Part (a) ends at "\( x > 0 \)": the closing line of \( \rulename{{\to}I} \), "hence, if \( \abs{x - 1} < 1 \), then \( x > 0 \)", is silent. The assumption could not be: without "suppose", the sentence "\( \abs{x - 1} < 1 \)" would be a claim about every real \( x \), and a false one.

In (b), "recall" is \( \rulename{R} \), and it could be dropped. "Cannot hold" is \( \rulename{MT} \), with \( P \) the statement \( \abs{x - 1} < 1 \) and \( Q \) the statement \( x > 0 \); the last step reads \( \neg(\abs{x - 1} < 1) \) as \( \abs{x - 1} \ge 1 \), by the order fact of Section 2.1. An equivalent (b) announces the derived rule instead: "This is the contrapositive of (a)", which is \( \rulename{CP} \) applied to (a), followed by \( \rulename{{\to}E} \). That announcement may never be silent: a reader who sees "suppose \( x \le 0 \)" and then a citation of (a) must be told that (a) is being used backwards.
:::

## Disjunction and cases

| Rule | Phrases | Silent in plain prose? |
|---|---|---|
| \( \rulename{\vee I} \) | "…, so certainly \( P \) or \( Q \)"; "in particular \( x \ne 0 \) or …" | yes |
| \( \rulename{\vee E} \) | "we consider two cases"; "Case 1 … Case 2 …"; "in either case"; "otherwise" | never the split; the "in either case" may be silent |
| \( \rulename{DS} \) | "since \( x \ne 0 \), the first case is impossible, so …" | the rule's name, yes; the fact \( x \ne 0 \) it uses, never |
| "or" and "and" commute (@exm-disjunction-first-derivations, @prp-and-commutes) | "\( P \) or \( Q \)" read as "\( Q \) or \( P \)", with no words of its own | yes |

In analysis, \( \rulename{\vee I} \) hides inside every weakening of a strict inequality: "\( x > 0 \), so \( x \ge 0 \)". \( \rulename{\vee E} \) is the proof of the triangle inequality in Section 1.7 (@exm-triangle-inequality-cases), which splits on the sign of \( x + y \) and reaches \( \abs{x + y} \le \abs{x} + \abs{y} \) in both cases. \( \rulename{DS} \) is the step "\( x^2 = x \), so \( x = 0 \) or \( x = 1 \); since \( x \ne 0 \), \( x = 1 \)".

::: {#exm-rhetoric-cases}
[Two cases, a weakening, a refuted disjunct]

Let \( x \) be a real number. (a) Prove that \( \abs{x} + x \ge 0 \). (b) Prove that if \( x^2 = x \) and \( x \ne 0 \), then \( x = 1 \). Tag each step with its rule.
:::

::: {.solution}
*(a)* Every real number satisfies \( x \ge 0 \) or \( x < 0 \), and we consider the two cases [\( \rulename{\vee E} \)].

*Case \( x \ge 0 \).* Then \( \abs{x} = x \), so \( \abs{x} + x = 2x \ge 0 \).

*Case \( x < 0 \).* Then \( \abs{x} = -x \), so \( \abs{x} + x = 0 \), and certainly \( \abs{x} + x \ge 0 \) [\( \rulename{\vee I} \)].

So \( \abs{x} + x \ge 0 \) in either case [\( \rulename{\vee E} \), closing].

*(b)* Suppose \( x^2 = x \) and \( x \ne 0 \) [assumption for \( \rulename{{\to}I} \)]. Then \( x(x - 1) = x^2 - x = 0 \), and a product of two real numbers is \( 0 \) only if one factor is, so \( x = 0 \) or \( x - 1 = 0 \) [\( \rulename{{\to}E} \)]. Since \( x \ne 0 \), the first case is impossible, so \( x - 1 = 0 \) [\( \rulename{DS} \)], that is, \( x = 1 \).

In (a), the split was announced with the disjunction that makes it exhaust; \( \rulename{\vee E} \) needs that disjunction on a line, and a split without it is the missing-case error that Section 5.6 catalogues. The second case weakened \( \abs{x} + x = 0 \) to \( \abs{x} + x \ge 0 \), which is \( \rulename{\vee I} \). The closing "in either case" could be silent. In (b), the words "the first case is impossible" carry the fact \( x \ne 0 \) that \( \rulename{DS} \) uses: the rule's name is not needed, but that fact is.
:::

::: {.warning}
"Clearly" often hides a case split. "Clearly \( \max\{a, b\} \ge (a + b)/2 \)" is true for all real \( a, b \), but its proof is \( \rulename{\vee E} \) on "\( a \le b \) or \( b \le a \)": if \( a \le b \), then \( \max\{a, b\} = b = (b + b)/2 \ge (a + b)/2 \), and the other case is the same with the letters exchanged. The case split is never silent; write it, or write "by cases on whether \( a \le b \)" and the one computation.
:::

## Negation and contradiction

| Rule | Phrases | Silent in plain prose? |
|---|---|---|
| \( \rulename{\neg I} \) | "suppose \( P \); … a contradiction; hence \( \neg P \)"; "\( P \) is impossible, since …" | never |
| \( \rulename{\neg E} \) | "this contradicts …"; "which is impossible"; "but …" | never: the clashing pair is named |
| \( \rulename{\bot E} \) | "this case cannot occur"; "vacuously"; "there is nothing to prove" | yes, once the contradiction or the empty case is stated |
| \( \rulename{DM} \), quantifier negation | "not all … so some … fails"; "it is not the case that …, so …" | the negated form must be written |

In analysis, \( \rulename{\neg I} \) is the proof of @thm-sqrt2-irrational: "suppose some rational \( r \) has \( r^2 = 2 \); …; this is a contradiction; hence no rational number has square \( 2 \)". \( \rulename{\neg E} \) is a sentence such as "then \( n \le 1/\varepsilon < n \), a contradiction": the chain gives \( n < n \), which clashes with the fact that no number is less than itself. One strict link is essential, since \( n \le 1/\varepsilon \le n \) gives only \( n \le n \), which clashes with nothing. \( \rulename{\bot E} \) is "if \( A = \emptyset \), there is nothing to prove", said of a claim about every element of \( A \): with no element to check, the claim is vacuously true (Section 4.4).

The last row needs more room. To negate "\( s \) is an upper bound of \( A \)", that is, \( \forall a \in A\; (a \le s) \), a proof writes the negated form: **some** \( a \in A \) has \( a > s \). The passage uses @prp-bounded-quantifier-negation (a), derived with \( \rulename{RAA} \), and the order fact that \( \neg(a \le s) \) says \( a > s \). Chapter 11's proof that \( \nN \) is not bounded above is the instructive case. It opens "suppose, for contradiction, that \( \nN \) is bounded above" and closes with "therefore \( \nN \) is not bounded above"; that is \( \rulename{\neg I} \), despite the phrase. Its one classical step comes after the box: from "not every \( n \in \nN \) has \( n \le x \)" it passes to "some \( n \in \nN \) has \( n > x \)", by @prp-bounded-quantifier-negation (a), which Section 4.9 derives with \( \rulename{RAA} \) through @prp-quantifier-negation (a) and @prp-negated-implication, and then by trichotomy for \( \neg(n \le x) \), giving \( n > x \). That step produces an \( n \) without naming it, and the proof needs no name.

::: {#exm-rhetoric-negation}
[A negative claim, its positive form, and an empty case]

(a) Prove that no real number is an upper bound of \( \nR \). (b) Prove the positive form: for every real \( s \) there is a real \( x \) with \( x > s \). (c) Let \( A \) be an empty set of real numbers. Prove that every real number is an upper bound of \( A \). Tag each step with its rule.
:::

::: {.solution}
*(a)* Let \( s \) be a real number [\( \rulename{\forall I} \)], and suppose \( s \) is an upper bound of \( \nR \) [assumption for \( \rulename{\neg I} \)]. Since \( s + 1 \) is a real number, \( s + 1 \le s \) [\( \rulename{\forall E} \) at \( s + 1 \)], that is, \( 1 \le 0 \). This contradicts \( 0 < 1 \) [\( \rulename{\neg E} \)]. Hence \( s \) is not an upper bound of \( \nR \) [\( \rulename{\neg I} \)].

*(b)* Let \( s \) be a real number [\( \rulename{\forall I} \)]. Take \( x \coloneqq s + 1 \) [\( \rulename{\exists I} \)]; then \( x - s = 1 > 0 \), so \( x > s \).

*(c)* Let \( s \) be a real number and \( a \in A \) [\( \rulename{\forall I} \), \( \rulename{{\to}I} \)]. Since \( A \) has no elements, \( a \in A \) is impossible [\( \rulename{\neg E} \), against "\( a \notin A \)"], so there is nothing to prove: \( a \le s \) [\( \rulename{\bot E} \)]. Hence \( s \) is an upper bound of \( A \).

Claim (a) is \( \forall s\, \neg\forall x\; (x \le s) \), and its proof writes the \( \rulename{\neg I} \) box in full: the assumption, the named clash, the conclusion. The positive form (b), \( \forall s\, \exists x\; (x > s) \), says more: it hands over the number that beats \( s \). Given (b) as a premise, (a) follows with no classical step: if \( s \) were an upper bound of \( \nR \), the \( x \) that (b) provides for \( s \) would satisfy \( x > s \) and \( x \le s \). The general passage from the shape of (a) to the shape of (b), with no witness in hand, goes through @prp-quantifier-negation (a), derived with \( \rulename{RAA} \), and trichotomy. So when both forms are within reach, prove the positive one. In (c), once the clash and the empty set are named, the \( \rulename{\bot E} \) line itself may be silent. Part (c) is the prose form of the derivation in Section 4.4 that concludes \( \forall u\, \forall x\; (x \in A \to x \le u) \) from \( \forall x\, \neg(x \in A) \), with its vacuous step unpacked into the \( \rulename{\neg E} \) and \( \rulename{\bot E} \) lines.
:::

## Proof by contradiction

| Rule | Phrases | Silent in plain prose? |
|---|---|---|
| \( \rulename{RAA} \) | "suppose, for contradiction, that \( \neg P \)"; "suppose not"; "assume the contrary" | never |
| \( \rulename{\neg\neg E} \), \( \rulename{LEM} \) | "either \( P \) or not"; "\( P \) must hold, since …"; "otherwise" | never: written as an explicit case split or an explicit removal of a double negation ("\( P \) must hold, since …") |

In analysis, \( \rulename{RAA} \) is the proof of @prp-arbitrarily-close-equal: "suppose, for a contradiction, that \( a \ne b \); then \( \abs{a - b} > 0 \), so the hypothesis gives \( \abs{a - b} < \abs{a - b} \), a contradiction; hence \( a = b \)". The box assumes \( \neg(a = b) \) and concludes \( a = b \), so it is genuine \( \rulename{RAA} \); \( \rulename{\neg I} \) would give only \( \neg\neg(a = b) \). \( \rulename{LEM} \) is a split such as "either the sequence has infinitely many terms in the left half of the interval, or it does not", the step of the bisection proof of the Bolzano–Weierstrass theorem (Chapter 12 proves the theorem). That split is genuinely non-constructive: nobody can decide in general which case holds. Section 5.7 explains why that matters, and a proof that makes such a step says so in one clause. A split such as "\( x \ge 0 \) or \( x < 0 \)" is also excluded middle in logical form, but it is an instance of the trichotomy of the order of \( \nR \), which Chapter 11 takes as an axiom, and it is never flagged.

::: {#exm-rhetoric-contradiction}
[One proof by contradiction, read three ways]

Let \( a \) and \( b \) be real numbers with \( a \le b + \varepsilon \) for every \( \varepsilon > 0 \). Prove that \( a \le b \), first by \( \rulename{RAA} \); then rewrite the proof with \( \rulename{\neg I} \) and \( \rulename{\neg\neg E} \), and with a case split.
:::

::: {.solution}
*By \( \rulename{RAA} \).* Suppose, for a contradiction, that \( a > b \) [assumption for \( \rulename{RAA} \)]. Then \( \varepsilon \coloneqq (a - b)/2 \) is positive, so the hypothesis gives \( a \le b + (a - b)/2 \) [\( \rulename{\forall E} \) at \( (a - b)/2 \)], that is, \( 2a \le a + b \), so \( a \le b \). This contradicts \( a > b \) [\( \rulename{\neg E} \)]. Hence \( a \le b \) [\( \rulename{RAA} \)].

The box assumes \( a > b \), which is \( \neg(a \le b) \) by the order fact of Section 2.1, and the proof concludes \( a \le b \): a negation goes **out**.

*By \( \rulename{\neg I} \) and \( \rulename{\neg\neg E} \).* Close the same box with "hence \( a > b \) is impossible" [\( \rulename{\neg I} \)], the line \( \neg(a > b) \), which is \( \neg\neg(a \le b) \) under the same reading of \( a > b \) as \( \neg(a \le b) \); then "so \( a \le b \) must hold" [\( \rulename{\neg\neg E} \)]. The two steps do what \( \rulename{RAA} \) did in one, and show that the box itself uses no classical rule.

*By cases.* By trichotomy, \( a \le b \) or \( a > b \) [\( \rulename{\vee E} \)]. In the first case we are done. In the second, the lines of the box above reach \( a \le b \) against \( a > b \), so this case cannot occur, and in it \( a \le b \) [\( \rulename{\neg E} \), \( \rulename{\bot E} \)]. In either case \( a \le b \).

The three proofs share their mathematics, the instance \( \varepsilon = (a - b)/2 \), and differ only in how the classical step is written: as \( \rulename{RAA} \), as \( \rulename{\neg\neg E} \), or as a case split. All three also read \( a > b \) as \( \neg(a \le b) \) by the order fact of Section 2.1, itself an instance of trichotomy; read the other way, that fact gives \( a \le b \) from \( \neg(a > b) \) directly, so the first two put an excluded-middle step on top of it. Over \( \nR \) trichotomy is an axiom, so no step here is flagged.
:::

## The biconditional

| Rule | Phrases | Silent in plain prose? |
|---|---|---|
| \( \rulename{{\leftrightarrow}I} \) | "\( (\Rightarrow) \) … \( (\Leftarrow) \) …"; "conversely"; "we prove both directions" | never either direction |
| \( \rulename{{\leftrightarrow}E} \) | "by definition"; "that is"; "i.e."; "equivalently" | yes, for a definitional "if and only if" |

In analysis, @thm-squares-order of Section 2.4 (for \( x, y \ge 0 \), \( x \le y \iff x^2 \le y^2 \)) is the model of \( \rulename{{\leftrightarrow}I} \): two labeled directions, each a \( \rulename{{\to}I} \) box. \( \rulename{{\leftrightarrow}E} \) is every unwinding of a definition: "\( f \) is strictly increasing, that is, \( x < y \) implies \( f(x) < f(y) \)" (@exm-strictly-increasing-both-ways). A definition is an "if and only if" (Section 2.4), and the words "that is" use it in one direction or the other.

::: {#exm-rhetoric-biconditional}
[Both directions, the second by cases]

Let \( x \) be a real number with \( x \ge 0 \). Prove that \( x \le 1 \) if and only if \( x^2 \le x \). Tag each step with its rule.
:::

::: {.solution}
\( (\Rightarrow) \) Suppose \( x \le 1 \) [assumption for \( \rulename{{\to}I} \)]. Multiplying by \( x \ge 0 \) gives \( x^2 \le x \).

\( (\Leftarrow) \) Conversely, suppose \( x^2 \le x \) [assumption for \( \rulename{{\to}I} \)]. Since \( x \ge 0 \), either \( x = 0 \) or \( x > 0 \) [\( \rulename{\vee E} \)]. If \( x = 0 \), then \( x \le 1 \). If \( x > 0 \), dividing \( x^2 \le x \) by \( x \) gives \( x \le 1 \).

So \( x \le 1 \) if and only if \( x^2 \le x \) [\( \rulename{{\leftrightarrow}I} \)].

The labels \( (\Rightarrow) \) and \( (\Leftarrow) \) are the two boxes of \( \rulename{{\leftrightarrow}I} \), and "conversely" opens the second. The hypothesis \( x \ge 0 \) does a job in each: it keeps the inequality's direction when we multiply, and it reduces the cases to \( x = 0 \) and \( x > 0 \), by \( \rulename{{\leftrightarrow}E} \) on the definition of \( \ge \). Without it, \( (\Leftarrow) \) still holds, since a negative \( x \) has \( x^2 \ge 0 > x \), so \( x^2 \le x \) forces \( x \ge 0 \) and the proof above applies; but \( (\Rightarrow) \) fails: \( x = -1 \) has \( x \le 1 \) and \( x^2 = 1 > x \).
:::

## The three faces of "by contradiction"

"Proof by contradiction" is used in practice for three different arguments. Each opens a box and finds \( \bot \) inside it; they differ in what the box assumes and what the proof concludes, and only face (i) is free of a classical step: face (iii) ends with \( \rulename{RAA} \), and face (ii) ends with @prp-contrapositive-converse, which uses \( \rulename{RAA} \) unless \( Q \) is itself a negation.

| Face | The box assumes | The proof concludes | Last step |
|---|---|---|---|
| (i) refuting | \( P \) | \( \neg P \) | \( \rulename{\neg I} \) |
| (ii) contrapositive | \( \neg Q \), inside "suppose \( P \)" | \( P \to Q \), from \( \neg Q \to \neg P \) | @prp-contrapositive-converse |
| (iii) genuine | \( \neg P \) | \( P \) | \( \rulename{RAA} \) |

**(i) Refuting a statement.** The claim is negative: irrational, "no largest", \( x \ne 5 \). The box assumes the positive statement, as the proof of @thm-sqrt2-irrational assumes \( r^2 = 2 \), and no classical rule is used.

**(ii) The contrapositive.** The claim is \( P \to Q \), and the proof derives \( \neg P \) from \( \neg Q \), with \( P \) playing no part until the end. The passage back to \( P \to Q \) is @prp-contrapositive-converse, which Section 2.5 derives with \( \rulename{RAA} \) (avoidable when \( Q \) is itself a negation, as Section 2.5 notes after the proof). Written as "suppose \( P \); suppose, for contradiction, \( \neg Q \); … \( \neg P \), a contradiction", it is that derivation done inline.

**(iii) Genuine reductio.** The claim \( P \) is positive, and \( \neg P \) is used throughout the box, typically because it hands over an object: \( a \ne b \) makes \( \abs{a - b} \) a positive number to feed to a hypothesis about every \( \varepsilon > 0 \).

*To tell them apart, read the first sentence of the box and the sentence after it:* what does it assume, and what does the proof write after it closes? The words "for contradiction" do not decide it; Chapter 11 uses them for a face (i) proof.

*The style rule: use the weakest form that works, and say which one you use.* A direct proof, when one exists, beats all three. A negative claim is proved by face (i). Face (ii) is announced as "we prove the contrapositive", which tells the reader the goal \( \neg Q \to \neg P \) at once. Face (iii) is for a positive claim that resists the other routes, with its classical step made visible as in @exm-rhetoric-contradiction.

## Costumes

A proof written as "suppose, for contradiction, …" sometimes uses its assumption for nothing except the final clash. It is then a direct proof or a contrapositive proof **in costume**, and it reads better with the costume off. Section 2.5 met the smallest case; here are the two costumes as they appear in prose, each with a test to run on a finished proof.

::: {#exm-costume-direct}
[A direct proof in costume]

Here is a proof that \( x^2 - 2x > 3 \) for every real \( x > 3 \). Decide what it really uses, and rewrite it.

> Let \( x > 3 \). Suppose, for a contradiction, that \( x^2 - 2x \le 3 \). Since \( x > 3 \), both \( x - 3 \) and \( x + 1 \) are positive, so \( (x - 3)(x + 1) > 0 \), that is, \( x^2 - 2x - 3 > 0 \). So \( x^2 - 2x > 3 \). This contradicts our assumption. Hence \( x^2 - 2x > 3 \).
:::

::: {.solution}
The assumption "\( x^2 - 2x \le 3 \)" is cited exactly once, in "This contradicts our assumption". The sentences before it prove \( x^2 - 2x > 3 \) from \( x > 3 \) alone, so the \( \rulename{RAA} \) box contains a complete derivation of the goal. Deleting the box leaves a direct proof:

> Let \( x > 3 \). Then \( x - 3 > 0 \) and \( x + 1 > 0 \), so \( x^2 - 2x - 3 = (x - 3)(x + 1) > 0 \), that is, \( x^2 - 2x > 3 \).

Nothing is lost, the \( \rulename{RAA} \) is gone, and the reader no longer holds a false assumption in mind for three sentences.
:::

*The test:* if the assumption of the box is cited only in the line that produces \( \bot \), the box proved the goal without it. Delete the box.

::: {#exm-costume-contrapositive}
[A contrapositive in costume]

Here is a proof that, for an integer \( n \), if \( n^2 \) is even then \( n \) is even. Decide what it really uses, and rewrite it.

> Suppose \( n^2 \) is even. Suppose, for a contradiction, that \( n \) is not even. Then \( n \) is odd, say \( n = 2k + 1 \) with \( k \) an integer. Then \( n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 \) is odd, so \( n^2 \) is not even. This contradicts the fact that \( n^2 \) is even. Hence \( n \) is even.
:::

::: {.solution}
Here the assumption of the box, "\( n \) is not even", is used heavily; what is used only once is the **hypothesis** "\( n^2 \) is even", in "This contradicts …". The sentences between derive "\( n^2 \) is not even" from "\( n \) is not even" alone. So the real content is \( \neg Q \to \neg P \), with \( P \) the statement "\( n^2 \) is even" and \( Q \) the statement "\( n \) is even", and the frame around it is @prp-contrapositive-converse done inline: face (ii). Written openly:

> We prove the contrapositive: if \( n \) is not even, then \( n^2 \) is not even. Suppose \( n \) is not even. Then \( n \) is odd, say \( n = 2k + 1 \) with \( k \) an integer, and \( n^2 = 2(2k^2 + 2k) + 1 \) is odd, so it is not even.

The rewrite tells the reader at the start what will be shown, and the final clash disappears. The classical step has not: it is now inside the announcement, which uses @prp-contrapositive-converse. (The proof by cases of @thm-square-even-implies-even in Section 2.1 needs no \( \rulename{RAA} \) at all.)
:::

*The test:* if everything inside the box follows from its assumption \( \neg Q \) alone, and the hypothesis \( P \) of the theorem enters only in the line that produces \( \bot \), then the box proved \( \neg Q \to \neg P \). Present it as a contrapositive.

The two tests share one smell: *the clash at the end is with a statement the proof already had, or would have had without the box.* A genuine reductio uses its assumed negation throughout, and the clash comes somewhere the reader did not see coming; in @exm-rhetoric-contradiction, the assumption \( a > b \) was what made \( (a - b)/2 \) positive.

::: {.warning}
"Assume \( P \)" means different things at the top of different proofs. At the top of a proof of \( P \to Q \), it is the opening of the \( \rulename{{\to}I} \) box, and it is exactly right. At the top of a proof of \( P \) itself, it assumes the goal, and everything after it is circular: the last line "hence \( P \)" cites a line that is not available outside the box. For instance, "assume \( \sqrt 2 \) is irrational; then … ; hence \( \sqrt 2 \) is irrational" proves nothing, however correct the middle: it is entry (N9) of the catalogue in Section 5.6.
:::

## Exercises

### A. Check your understanding

::: {#exr-connective-rhetoric-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Name the rule that each phrase most often carries: (i) "in particular"; (ii) "conversely"; (iii) "in either case"; (iv) "this case cannot occur"; (v) "suppose, for contradiction, that \( x \) is not positive"; (vi) "we prove the contrapositive"; (vii) "that is"; (viii) "since \( x \ne 0 \), the first case is impossible"; (ix) "so \( x \ge 0 \)", after "\( x > 0 \)"; (x) "which contradicts \( x^2 \ge 0 \)".
2. Which of the phrases in (a) carry steps that may be silent in plain prose?
3. A proof ends "Suppose \( 7 = 2k \) for an integer \( k \). Then \( k = 7/2 \), which is not an integer. Hence \( 7 \) is not even." Which face of "by contradiction" is this?
4. True or false, with a reason: a proof that begins "suppose, for contradiction" always uses \( \rulename{RAA} \).
:::
:::

::: {.solution}
*(a)* (i) \( \rulename{\wedge E} \). (ii) \( \rulename{{\leftrightarrow}I} \), opening the second direction. (iii) \( \rulename{\vee E} \), closing. (iv) \( \rulename{\bot E} \). (v) \( \rulename{RAA} \), opening its box (the goal is "\( x \) is positive", and the box assumes its negation). (vi) \( \rulename{CP} \), or, as the frame of a whole proof, @prp-contrapositive-converse. (vii) \( \rulename{{\leftrightarrow}E} \), on a definition. (viii) \( \rulename{DS} \). (ix) \( \rulename{\vee I} \). (x) \( \rulename{\neg E} \).

*(b)* (i), (iii) (the closing "in either case"), (iv) (once the contradiction is stated), (vii) (for a definition), and (ix). In (viii) the name of \( \rulename{DS} \) may be dropped, but not the fact \( x \ne 0 \). The openings (ii), (v), (vi) and the clash (x) are never silent.

*(c)* Face (i), refuting: the box assumes the positive statement "\( 7 \) is even", that is, \( 7 = 2k \) for some integer \( k \), and the proof concludes its negation, by \( \rulename{\neg I} \). (The value \( 7/2 \) is not an integer because \( 3 < 7/2 < 4 \).)

*(d)* False. The phrase also opens \( \rulename{\neg I} \) boxes. Chapter 11's proof that \( \nN \) is not bounded above begins "suppose, for contradiction, that \( \nN \) is bounded above" and concludes the negation, by \( \rulename{\neg I} \). What decides is what the box assumes and what the proof concludes.
:::

### B. Practice

::: {#exr-connective-rhetoric-b1}
[B1: Take off the costume]

Here is a proof that \( \frac{a + b}{2} \ge \sqrt{ab} \) for all real \( a > 0 \) and \( b > 0 \).

> Let \( a, b > 0 \). Suppose, for a contradiction, that \( \frac{a+b}{2} < \sqrt{ab} \). Since \( (\sqrt a - \sqrt b)^2 \ge 0 \), expanding gives \( a - 2\sqrt{ab} + b \ge 0 \), so \( \frac{a+b}{2} \ge \sqrt{ab} \). This contradicts our assumption. Hence \( \frac{a+b}{2} \ge \sqrt{ab} \).

::: {.enumerate options="label=(\alph*)"}
1. Which costume is this? Justify your answer by saying where the assumption of the box is cited.
2. Rewrite the proof without the contradiction.
:::
:::

::: {.solution}
*(a)* A direct proof in costume (@exm-costume-direct). The assumption \( \frac{a+b}{2} < \sqrt{ab} \) is cited only in "This contradicts our assumption", the line that produces \( \bot \). The sentence beginning "Since" proves the goal from \( a, b > 0 \) alone, without using the assumption.

*(b)* Let \( a, b > 0 \), so that \( \sqrt a \) and \( \sqrt b \) are defined and \( \sqrt a \sqrt b = \sqrt{ab} \). Since \( (\sqrt a - \sqrt b)^2 \ge 0 \), expanding gives \( a - 2\sqrt{ab} + b \ge 0 \). Adding \( 2\sqrt{ab} \) to both sides and dividing by \( 2 \) gives \( \frac{a+b}{2} \ge \sqrt{ab} \), as claimed.
:::

::: {#exr-connective-rhetoric-b2}
[B2: Where the classical step sits]

Here is a proof that if \( x \) is a real number with \( \abs{x} \le \abs{y} \) for every real \( y \ne 0 \), then \( x = 0 \).

> Suppose \( \abs{x} \le \abs{y} \) for every real \( y \ne 0 \). Suppose, for a contradiction, that \( x \ne 0 \). Then \( y \coloneqq x/2 \) is a non-zero real number, so the hypothesis gives \( \abs{x} \le \abs{x/2} = \abs{x}/2 \), and hence \( \abs{x} \le 0 \). But \( \abs{x} > 0 \), since \( x \ne 0 \). This is a contradiction. Hence \( x = 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Is the last step \( \rulename{RAA} \) or \( \rulename{\neg I} \)? Is the proof in costume?
2. Rewrite it so that the box closes by \( \rulename{\neg I} \) and one further step removes a double negation. Tag the two steps.
3. Which of the two versions tells the reader more, and what?
:::
:::

::: {.solution}
*(a)* \( \rulename{RAA} \): the box assumes \( \neg(x = 0) \), written \( x \ne 0 \), and the proof concludes the positive statement \( x = 0 \). It is not in costume. The assumption does work inside the box (it makes \( x/2 \) non-zero, so that the hypothesis applies to it), and the hypothesis is used in the middle of the box, not only at the clash; neither test of this section is met.

*(b)* Suppose \( \abs{x} \le \abs{y} \) for every real \( y \ne 0 \). If \( x \ne 0 \), then \( x/2 \ne 0 \), so the hypothesis gives \( \abs{x} \le \abs{x}/2 \), that is, \( \abs{x} \le 0 \), against \( \abs{x} > 0 \). Hence \( x \ne 0 \) is impossible [\( \rulename{\neg I} \)], so \( x = 0 \) must hold [\( \rulename{\neg\neg E} \)].

*(c)* The second. It shows that the box uses no classical rule: without one, the argument proves \( \neg\neg(x = 0) \), "\( x \) cannot be non-zero", and the classical rule enters only in the final step, "so \( x = 0 \) must hold" [\( \rulename{\neg\neg E} \)]. The first version does both steps at once in the single \( \rulename{RAA} \), and so hides where the classical rule enters.
:::

### C. Going deeper

::: {#exr-connective-rhetoric-c1}
[C1: Euclid without the contradiction]

Here is a common proof that there are infinitely many primes. It uses two facts about integers that we take as known here: every integer \( m \ge 2 \) has a prime divisor (Chapter 7 proves it); and if an integer \( d \) divides two integers, it divides their difference (if \( u = dk \) and \( v = dl \), then \( u - v = d(k - l) \)).

> Suppose, for a contradiction, that there are only finitely many primes, say \( p_1, \dots, p_k \). Let \( N \coloneqq p_1 p_2 \cdots p_k + 1 \). Then \( N \ge 2 \), so \( N \) has a prime divisor \( p \). Since \( p_1, \dots, p_k \) are all the primes, \( p = p_i \) for some \( i \). Then \( p_i \) divides both \( N \) and \( p_1 p_2 \cdots p_k \), so it divides their difference \( 1 \), which is impossible for a prime. This is a contradiction. Hence there are infinitely many primes.

::: {.enumerate options="label=(\alph*)"}
1. "There are infinitely many primes" means "the set of primes is **not** finite". Is the last step of the proof \( \rulename{RAA} \) or \( \rulename{\neg I} \)?
2. Where is the assumption "\( p_1, \dots, p_k \) are all the primes" used? Which smell from this section does that suggest?
3. Rewrite the argument as a direct proof of: *for every finite list \( p_1, \dots, p_k \) of primes, with \( k \ge 1 \), there is a prime not in the list.*
4. Say what the rewrite gains over the original.
:::
:::

::: {.solution}
*(a)* \( \rulename{\neg I} \). The box opens with "the set of primes is finite", the positive statement, and the conclusion is its negation: face (i). No \( \rulename{RAA} \) is used.

*(b)* Once, in "\( p = p_i \) for some \( i \)", where the clash is manufactured. Everything else holds for **any** finite list of primes, complete or not: the smell of a costume.

*(c)* Let \( p_1, \dots, p_k \) be a finite list of primes, \( k \ge 1 \), and let \( N \coloneqq p_1 p_2 \cdots p_k + 1 \). Each \( p_i \ge 2 \), so \( N \ge 3 \), and \( N \) has a prime divisor \( p \). Let \( i \) be an index with \( 1 \le i \le k \) [\( \rulename{\forall I} \), opening], and suppose \( p = p_i \) [assumption for \( \rulename{\neg I} \)]. Then \( p \) divides \( N \) and \( p_1 p_2 \cdots p_k \), so it divides their difference \( 1 \), say \( 1 = pm \) with \( m \) an integer. Since \( p > 0 \), \( m > 0 \), so \( m \ge 1 \) and \( 1 = pm \ge p \ge 2 \), a contradiction [\( \rulename{\neg E} \)]. Hence \( p \ne p_i \) [\( \rulename{\neg I} \)]. Since \( i \) was arbitrary, \( p \ne p_i \) for every \( i \) [\( \rulename{\forall I} \), closing], and \( p \) is a prime not in the list.

*(d)* The rewrite proves a stronger statement: given any finite list of primes, it **produces** a prime outside it, any prime divisor of \( N \); the original shows only that a list of all the primes is impossible. Its one \( \rulename{\neg I} \) box, for the negative claim \( p \ne p_i \), is honest, since its assumption is what the clash uses. The original theorem follows at once: a finite list of all the primes is non-empty, since \( 2 \) is prime, so by (c) it would miss a prime.

**Marking scheme.** (10 points)
- 2: (a) \( \rulename{\neg I} \), with the reason (the box assumes the positive statement and the proof concludes its negation).
- 2: (b) locates the single use of the assumption and names the costume smell.
- 4: (c) a proof for an arbitrary finite list: \( N \) defined, \( N \ge 2 \) justified, a prime divisor \( p \) taken, \( p \ne p_i \) for every \( i \) shown.
- 2: (d) names the gain: a prime outside any given list is produced.
Fatal errors (0 for the step): in (c), a proof that still assumes the list contains all the primes; in (a), calling the step \( \rulename{RAA} \) because of the words "for a contradiction".
:::

::: {#exr-connective-rhetoric-c2}
[C2: Which face, and the weakest form]

Here is a proof that if \( x \) is a real number with \( x^2 < \varepsilon \) for every \( \varepsilon > 0 \), then \( x = 0 \).

> Suppose \( x^2 < \varepsilon \) for every \( \varepsilon > 0 \). Suppose, for a contradiction, that \( x \ne 0 \). Then \( x^2 > 0 \), so we may take \( \varepsilon = x^2 \), and the hypothesis gives \( x^2 < x^2 \), which is impossible. Hence \( x = 0 \).

::: {.enumerate options="label=(\alph*)"}
1. Which face of "by contradiction" is this, as written?
2. Rewrite the proof in the weakest form you can, and say which rules it uses at its logical steps, and which school fact.
:::
:::

::: {.solution}
[Hint 1]

The goal \( x = 0 \) is positive. Look for a school fact about \( x^2 \) that is a disjunction: one case leads to the goal through another school fact, and the hypothesis rules out the other.
:::

::: {.solution}
[Hint 2]

Start: "Since \( x^2 \ge 0 \), either \( x^2 > 0 \) or \( x^2 = 0 \)."
:::

::: {.solution}
*(a)* Face (iii), genuine reductio. The box assumes \( \neg(x = 0) \), written \( x \ne 0 \), uses it to make \( x^2 \) a positive number to which the hypothesis applies, and concludes the positive statement \( x = 0 \). The last step is \( \rulename{RAA} \). It is not in costume: the assumption does work inside the box.

*(b)* Suppose \( x^2 < \varepsilon \) for every \( \varepsilon > 0 \) [assumption for \( \rulename{{\to}I} \)]. Since \( x^2 \ge 0 \), either \( x^2 > 0 \) or \( x^2 = 0 \), and we consider the two cases [\( \rulename{\vee E} \)].

*Case \( x^2 > 0 \).* Then the hypothesis applies to \( \varepsilon = x^2 \) [\( \rulename{\forall E} \)] and gives \( x^2 < x^2 \), which contradicts the fact that no number is less than itself [\( \rulename{\neg E} \)]. So this case cannot occur, and in it \( x = 0 \) [\( \rulename{\bot E} \)].

*Case \( x^2 = 0 \).* Then \( x \cdot x = 0 \), so \( x = 0 \) [\( \rulename{{\to}E} \)], since a product of two real numbers is \( 0 \) only if a factor is.

In either case \( x = 0 \) [\( \rulename{\vee E} \)].

The logical steps are \( \rulename{{\to}I} \), \( \rulename{\vee E} \), \( \rulename{\forall E} \), \( \rulename{\neg E} \), \( \rulename{{\to}E} \) (citing the second school fact, that a product is \( 0 \) only if a factor is) and \( \rulename{\bot E} \); no classical rule is used. The classical content has moved into the school fact "\( x^2 > 0 \) or \( x^2 = 0 \)", which rests on the trichotomy of the order, an axiom of Chapter 11; Section 5.7 explains why that axiom is where the book makes its classical commitment.

**Marking scheme.** (10 points)
- 3: (a) identifies \( \rulename{RAA} \) (face (iii)), with the reason: the assumption is a negation and the conclusion is positive.
- 2: (b) splits on a disjunction that is justified (from \( x^2 \ge 0 \), or from trichotomy).
- 3: (b) closes the case \( x^2 > 0 \) by the instance \( \varepsilon = x^2 \), a named clash, and \( \rulename{\bot E} \).
- 2: (b) settles the case \( x^2 = 0 \) with its reason and concludes "in either case".
A rewrite with \( \rulename{\neg I} \) and \( \rulename{\neg\neg E} \) in place of the case split earns the points of (b) except the 2 for the split, provided it names \( \rulename{\neg\neg E} \) as its one classical step.
Fatal errors (0 for the step): calling (a) face (i) because the word "contradiction" appears; splitting on "\( x^2 > 0 \) or \( x^2 < 0 \)", which does not exhaust.
:::

<!-- dependency ledger
exm-square-even-via-contrapositive (example): the derivation reprinted in the hook; (E1)-(E3) | exm-square-even-via-contrapositive (cited); school facts of Section 2.1
exm-square-even-via-contrapositive (claim): line 11 (or commutes) has no words; the Disjunction table's row: exchanging the members of a disjunction or conjunction may be silent | exm-disjunction-first-derivations, prp-and-commutes (cited); def-silent-steps (Section 5.3, prose pointer)
exm-rhetoric-conjunction (solution): t >= 0 or t < 0; max{t, 0} = t if t >= 0 and 0 if t < 0, so max{t, 0} >= t, >= 0 and < 2 for t < 2, in each case; a = (m + 2)/2 in [1, 2), a - m = (2 - m)/2 > 0 | trichotomy; max of two numbers, a school notion (max{a, b} is a if a >= b and b otherwise, as Ch 3 05 (the three-valued table before thm-raa-independent) and Ch 11 exr-ordered-fields-a1 (3) treat it; Ch 1 exr-disjunction-and-cases-b2 is a pointer only, nothing rests on it); school algebra; verify/ch05/exm-rhetoric-conjunction.py
exm-rhetoric-conjunction (claim): Ch 11's (S2) says the same as "no t < s is an upper bound" | trichotomy; prose remark, nothing rests on it
exm-rhetoric-implication (solution): |u| < r iff -r < u < r; a >= b iff not(a < b) | school fact stated in the solution; order fact of Section 2.1
exm-rhetoric-implication (claim): the continuity sentence is a theorem of Ch 15 | prose pointer (ch15 blueprint, sequential criterion); sample sentence only
exm-rhetoric-cases (solution): x >= 0 or x < 0; |x| by cases; ab = 0 implies a = 0 or b = 0; max{a, b} >= (a + b)/2 | school facts; verify/ch05/exm-rhetoric-cases.py
exm-rhetoric-negation (solution): s + 1 <= s gives 1 <= 0; 0 < 1; claims about every element of the empty set; (c) is the prose form of Section 4.4's upper-bound derivation | school algebra; Section 4.4 (prose)
exm-rhetoric-negation (claim): Ch 11's unboundedness proof is neg-I, then one classical step | prose pointer (Ch 11 thm-naturals-unbounded and its remark)
exm-rhetoric-negation (claim): the general passage from the shape of (a) to the shape of (b), with no witness, goes through prp-quantifier-negation (a) and trichotomy | prp-quantifier-negation (cited); trichotomy school fact
exm-rhetoric-contradiction (solution): (a - b)/2 > 0 for a > b; a <= b + (a - b)/2 iff a <= b; a <= b or a > b | school algebra; trichotomy; verify/ch05/exm-rhetoric-contradiction.py
exm-rhetoric-contradiction (claim): Bolzano-Weierstrass proved in Ch 12; its bisection split is non-constructive | prose pointers (ch12 blueprint; Section 5.7)
exm-rhetoric-biconditional (solution): multiply by x >= 0; divide by x > 0; x = -1 | school algebra; verify/ch05/exm-rhetoric-biconditional.py
exm-rhetoric-biconditional (claim): x < 0 gives x^2 >= 0 > x, so (<=) needs no hypothesis | school algebra; prose remark, nothing rests on it; verify/ch05/exm-rhetoric-biconditional.py
exm-costume-direct (solution): (x - 3)(x + 1) = x^2 - 2x - 3 > 0 for x > 3 | school algebra; verify/ch05/exm-costume-direct.py
exm-costume-contrapositive (solution): not even implies odd; odd implies not even; (2k + 1)^2 = 2(2k^2 + 2k) + 1 | (E1), (E2) of Section 2.1 (ch07 promised, STATUS parity row); inline
exr-connective-rhetoric-a1 (solution): 3 < 7/2 < 4, and no integer lies strictly between 3 and 4 | school arithmetic of Z (ch07 promised in STATUS: "nothing between n and n + 1"); verify/ch05/exr-connective-rhetoric-a1.py
exr-connective-rhetoric-b1 (solution): sqrt a sqrt b = sqrt(ab); (sqrt a - sqrt b)^2 expanded | school facts (Ch 11 thm-nth-root, prose); verify/ch05/exr-connective-rhetoric-b1.py
exr-connective-rhetoric-b2 (solution): x != 0 gives x/2 != 0 and |x| > 0; |x/2| = |x|/2; |x| <= |x|/2 gives |x| <= 0 | school algebra; verify/ch05/exr-connective-rhetoric-b2.py
exr-connective-rhetoric-c1 (solution): every integer m >= 2 has a prime divisor | ch07 (promised): thm-prime-factor; stated in the item
exr-connective-rhetoric-c1 (solution): d | u, d | v give d | u - v; a positive divisor of 1 is at most 1 | proved in the item, using m > 0 gives m >= 1, i.e. no integer strictly between 0 and 1: school arithmetic of Z (ch07 promised in STATUS: "nothing between n and n + 1")
exr-connective-rhetoric-c1 (solution): 2 is prime, so a list of all the primes has k >= 1 | arithmetic (its only positive divisors are 1 and 2); inline
exr-connective-rhetoric-c2 (solution): x^2 >= 0 gives x^2 > 0 or x^2 = 0; xx = 0 gives x = 0; no number is less than itself | school facts; trichotomy (Ch 11 axiom); verify/ch05/exr-connective-rhetoric-c2.py
-->
