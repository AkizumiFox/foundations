# Soundness

Chapter 2 ended on a question it could not answer. Section 2.6 searched for a derivation of \( P \to Q \vdash Q \to P \), and every route came back to the same gap; but a search that fails proves nothing, since a cleverer derivation might exist. The row that refutes affirming the consequent in Section 3.4, \( p = \mathrm{F} \) and \( q = \mathrm{T} \), finds what the search could not: it makes \( p \to q \) true and \( q \to p \) false. This section proves the theorem that turns such a row into a proof that **no** derivation exists. It is called soundness: whatever the rules derive is true in every row where the premises are true. The proof is the book's first long proof about proofs, and it is an induction on the lines of a derivation.

## What must be proved, and why it is not obvious

Chapters 1 and 2 checked each rule as it arrived. \( \rulename{\wedge I} \) is safe because two true statements make a true conjunction (Section 1.3); \( \rulename{{\to}E} \) is safe because that is what "if … then" asserts (Section 1.4). Each time, the book said that Chapter 3 would prove it "for every rule at once". Why is that more than collecting the separate checks?

The first attempt at a proof is: go down a derivation, line by line, and show that each line is true in every row in which the premises are true. For a derivation without boxes this works. Each line is a premise, or comes from earlier lines by a rule, and the rule turns true lines into a true line. But it fails at the first box. Here is the derivation of @prp-contrapositive, written with atoms:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \to q}
  \open
  \hypo {2} {\neg q}
  \open
  \hypo {3} {p}
  \have {4} {q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg p} \ni{3-5}
  \close
  \have {7} {\neg q \to \neg p} \ii{2-6}
\end{nd}$
\end{center}
```

Line 3 is \( p \), and the row \( p = \mathrm{F} \), \( q = \mathrm{F} \) makes the premise \( p \to q \) true and line 3 false. Line 5 is \( \bot \), which is false in **every** row. So the lines inside a box are not true in the rows where the premises are true, and the first attempt collapses. Yet the derivation is correct, and its last line \( \neg q \to \neg p \) is true in every row making \( p \to q \) true (@exm-table-contrapositive).

What goes wrong is that a line inside a box is not claimed on the strength of the premises alone. Line 4 says: *if* \( p \to q \), \( \neg q \) and \( p \) all hold, then \( q \) holds. That is a true claim about rows. Every line depends on the premises **and** on the assumptions of the boxes around it, and a correct statement about each line must mention both. Chapter 1 gave this list a name.

## Derivations of formulas

From now on the lines of a derivation carry **formulas** in the sense of @def-formula, with atoms \( p, q, r, \dots \). Nothing in the rules changes. Every rule was stated as a schema, whose letters \( \varphi, \psi, \chi \) stand for arbitrary statements (@def-rule-schema), so it applies to formulas as it stands, and @def-derivation and @def-derivable read the same with "formula" for "statement". As Section 3.1 said, a derivation written with Chapter 2's letters \( P, Q \) is a pattern, and reading its letters as atoms, or as any formulas, gives a derivation of formulas.

Two conventions for the rest of the section. The **primitive rules** are those of Chapters 1 and 2 collected in Section 2.6: \( \rulename{R} \), \( \rulename{\wedge I} \), \( \rulename{\wedge E} \), \( \rulename{{\to}I} \), \( \rulename{{\to}E} \), \( \rulename{\vee I} \), \( \rulename{\vee E} \), \( \rulename{\neg I} \), \( \rulename{\neg E} \), \( \rulename{\bot E} \), \( \rulename{RAA} \), \( \rulename{{\leftrightarrow}I} \) and \( \rulename{{\leftrightarrow}E} \). The **box rules** among them are the five that cite a box: \( \rulename{{\to}I} \), \( \rulename{\neg I} \), \( \rulename{RAA} \), \( \rulename{\vee E} \) and \( \rulename{{\leftrightarrow}I} \). The other eight, \( \rulename{R} \) included, cite only lines; we call them the **one-step rules**.

A derivation may also use derived rules such as \( \rulename{MT} \) and \( \rulename{LEM} \). A line citing one abbreviates a stretch of derivation in rules proved earlier, with the letters replaced by formulas (@def-derived-rule), and Section 2.3 showed how to write it out: repeat the cited lines, then paste the derivation of the derived rule below them. Every chain of derived rules ends in primitive rules. So whenever \( \Gamma \vdash \psi \), there is also a derivation of \( \psi \) from premises in \( \Gamma \) that uses **primitive rules only**. That is the only kind of derivation the proof below has to consider.

## The context of a line

Let a derivation have lines \( 1, \dots, n \). We write \( \varphi_k \) for the formula on line \( k \). Recall from Section 1.5, just after @def-derivation, that the **context** of line \( k \) is the list of the premises together with the assumptions of every box containing line \( k \); we write it \( \Gamma_k \). For lists of formulas \( \Delta \) and \( \Delta' \), we write \( \Delta \subseteq \Delta' \) when every formula of \( \Delta \) occurs in \( \Delta' \).

*The context of a line is everything that line depends on: the premises, and every assumption still open where the line stands.*

In the derivation of @prp-contrapositive above, the boxes are \( \lines{2}{6} \) and \( \lines{3}{5} \), and the contexts are:

| Line | Formula | Boxes containing it | Context |
|---|---|---|---|
| 1 | \( p \to q \) | none | \( p \to q \) |
| 2 | \( \neg q \) | \( \lines{2}{6} \) | \( p \to q, \ \neg q \) |
| 3, 4, 5 | \( p \), \( q \), \( \bot \) | \( \lines{2}{6} \), \( \lines{3}{5} \) | \( p \to q, \ \neg q, \ p \) |
| 6 | \( \neg p \) | \( \lines{2}{6} \) | \( p \to q, \ \neg q \) |
| 7 | \( \neg q \to \neg p \) | none | \( p \to q \) |

Now look at each line through its context. Line 3 is one of the formulas in its own context, so every row making the context true makes line 3 true. Line 4: every row making \( p \to q \) and \( p \) true makes \( q \) true. Line 5: no row makes \( p \to q \), \( \neg q \), and \( p \) all true (the first and third force \( q \)), so the context is unsatisfiable and it entails even \( \bot \) (Section 3.4). Line 6: every row making \( p \to q \) and \( \neg q \) true makes \( p \) false. Line 7: its context is the premise, and we know \( p \to q \models \neg q \to \neg p \). So on this derivation, every line \( k \) satisfies
\[
\Gamma_k \models \varphi_k .
\]
This is the statement that survives the boxes, and it is the one we shall prove for every line of every derivation.

Two facts about contexts, read off the scope rule, do the bookkeeping. The first says that citing an available line never involves an assumption the citing line does not have. The second says exactly what the context of a box's last line is, when the box is cited by a box rule.

::: {#lem-context-inclusion}
[Contexts in a Derivation]

Let lines \( i \), \( k \) and \( a \le b \) belong to a derivation, and let \( \Gamma_j \) denote the context of line \( j \).

::: {.enumerate options="label=(\alph*)"}
1. If line \( i \) is available at line \( k \), then \( \Gamma_i \subseteq \Gamma_k \).
2. If line \( k \) is justified by a box rule citing the box whose first line is \( a \) and whose last line is \( b \), then the formulas of \( \Gamma_b \) are exactly those of \( \Gamma_k \) together with \( \varphi_a \), the assumption of that box. We write this \( \Gamma_b = \Gamma_k, \varphi_a \).
:::
:::

::: {.idea}
Both parts compare two sets of boxes, since contexts differ only in the assumptions of the boxes around a line. For (a), the scope rule says that the boxes around line \( i \) are among the boxes around line \( k \). For (b), the boxes around line \( b \) should be the cited box itself and the boxes around line \( k \); the danger is a further box inside the cited box that also ends on line \( b \), and the box rules forbid exactly that.
:::

::: {.proof}
*(a)* The premises belong to every context. Any other formula of \( \Gamma_i \) is the assumption of a box containing line \( i \). Since line \( i \) is available at line \( k \), every box containing line \( i \) also contains line \( k \), by the scope rule of @def-derivation. So that assumption belongs to \( \Gamma_k \).

*(b)* Let \( B \) be the box from line \( a \) to line \( b \). Since line \( k \) cites \( B \), the box \( B \) is available at line \( k \). By the scope rule, it ends before line \( k \), and the boxes containing \( B \) are exactly the boxes containing line \( k \).

We find the boxes containing line \( b \). Every box containing line \( k \) contains \( B \), and so contains line \( b \); and \( B \) contains line \( b \). Conversely, let \( C \) be a box containing line \( b \). By @def-derivation, two boxes are either disjoint or one inside the other; \( C \) and \( B \) share line \( b \), so \( C = B \), or \( C \) contains \( B \), or \( C \) lies inside \( B \). The last is impossible: then line \( b \), the last line of \( B \), would be a line of a box inside \( B \), and every box rule requires the last line of its box to be a line of that box itself, not of a box inside it (@def-rules-implication, @def-rules-negation, @def-rule-raa, @def-rules-disjunction, @def-rules-biconditional). So \( C = B \), or \( C \) is one of the boxes containing \( B \), which are the boxes containing line \( k \).

Hence the boxes containing line \( b \) are \( B \) and the boxes containing line \( k \). The assumption of \( B \) is \( \varphi_a \), so \( \Gamma_b \) consists of the premises, the assumptions of the boxes containing line \( k \), and \( \varphi_a \), which is \( \Gamma_k \) together with \( \varphi_a \).
:::

In the derivation of @prp-contrapositive, line 6 cites the box \( \lines{3}{5} \) by \( \rulename{\neg I} \), and \( \Gamma_5 = p \to q, \ \neg q, \ p \) is \( \Gamma_6 = p \to q, \ \neg q \) with the assumption \( p \) added, as (b) says. Line 5 cites lines 4 and 2, both available there, and \( \Gamma_4 \) and \( \Gamma_2 \) are contained in \( \Gamma_5 \), as (a) says.

::: {.warning}
Part (b) needs the box to be **cited by a box rule**. @def-derivation allows a box to end on the same line as a box inside it, and then its last line has a larger context. In the derivation below, the box \( \lines{2}{4} \) is available at line 5, but \( \Gamma_4 = p, \ q, \ r \) contains \( r \), the assumption of the inner box, as well as \( q \). No box rule may cite \( \lines{2}{4} \): its last line lies inside the box \( \lines{3}{4} \), not in \( \lines{2}{4} \) itself. (This is why the derivation of @exm-disjunction-regroup needs its line 11.)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p}
  \open
  \hypo {2} {q}
  \open
  \hypo {3} {r}
  \have {4} {p} \r{1}
  \close
  \close
  \have {5} {p} \r{1}
\end{nd}$
\end{center}
```
:::

::: {.check}
In the derivation of @prp-contrapositive above, which case of the soundness claim handles line 5? Which lines' contexts are involved, and why does \( \Gamma_5 \models \bot \) hold?
:::

::: {.solution}
Line 5 is \( \bot \), by \( \rulename{\neg E} \) citing lines 4 and 2: a one-step rule. Lines 4 and 2 are available at line 5, so by @lem-context-inclusion (a), \( \Gamma_4 = p \to q, \ \neg q, \ p \) and \( \Gamma_2 = p \to q, \ \neg q \) are contained in \( \Gamma_5 = p \to q, \ \neg q, \ p \). The claim for the earlier lines gives \( \Gamma_4 \models q \) and \( \Gamma_2 \models \neg q \). So a valuation making \( \Gamma_5 \) true would make both \( q \) and \( \neg q \) true, which clause (V2) of @def-truth-value forbids. No valuation makes \( \Gamma_5 \) true, and \( \Gamma_5 \models \bot \) holds because there is no row to check.
:::

## The soundness theorem

We can now state the theorem that Chapters 1 and 2 kept pointing to.

::: {#thm-soundness}
[Soundness]

Let \( \Gamma \) be a list of formulas and \( \psi \) a formula. If \( \Gamma \vdash \psi \), then \( \Gamma \models \psi \).
:::

*Try it first (ten minutes): suppose line \( k \) is \( \varphi \to \psi \), by \( \rulename{{\to}I} \) from a box that opens with \( \varphi \) and ends with \( \psi \). Suppose you already know that every row making the context of line \( k \) and \( \varphi \) true makes \( \psi \) true. Why is \( \varphi \to \psi \) true in every row making the context of line \( k \) true? What happens in the rows where \( \varphi \) is false?*

::: {.idea}
An attempt at the \( \rulename{{\to}I} \) case runs into two things. First, knowledge about the box's last line is knowledge about rows making its **own** context true, which contains the assumption \( \varphi \); that is why the claim must carry contexts, and why @lem-context-inclusion (b) is needed. Second, the rows in which \( \varphi \) is false are not covered by the box at all, and they need nothing: there \( \varphi \to \psi \) is true by (V5). The same two moves handle every box rule. The Step roadmap:

① Prove the stronger claim \( \Gamma_k \models \varphi_k \) for **every** line \( k \) of a derivation in primitive rules.

② Use strong induction on \( k \) (@thm-strong-induction): a rule may cite **any** earlier line, not only the line just above, so the hypothesis must be available for all earlier lines at once.

③ Split on how line \( k \) is justified. A premise or an assumption belongs to its own context. A one-step rule: apply the hypothesis to the cited lines, move their contexts into \( \Gamma_k \) by @lem-context-inclusion (a), and use one clause of @def-truth-value. A box rule: apply the hypothesis to each box's last line, whose context is \( \Gamma_k \) plus the box's assumption by @lem-context-inclusion (b), and argue about the rows where that assumption is true or false.

④ The last line lies in no box, so its context is the premises, all in \( \Gamma \); adding the other formulas of \( \Gamma \) keeps the entailment.

*Before reading on: in the case of \( \rulename{RAA} \) (Claim 3 below), where does the proof use that \( v(\neg\varphi) \) is \( \mathrm{F} \) exactly when \( v(\varphi) \) is \( \mathrm{T} \), and which half of that fact does it use?*
:::

::: {.proof}
**Step 1 (reduction to primitive rules).** Suppose \( \Gamma \vdash \psi \). As shown in the subsection on derivations of formulas, there is a derivation of \( \psi \) whose premises all belong to \( \Gamma \) and which uses primitive rules only. Fix one, with lines \( 1, \dots, n \); let \( \varphi_k \) be the formula on line \( k \) and \( \Gamma_k \) its context.

**Step 2 (the induction).** For \( k \in \nN \), let \( S(k) \) be the statement: *if \( 1 \le k \le n \), then \( \Gamma_k \models \varphi_k \).* We prove \( S(k) \) for every \( k \) by @thm-strong-induction. So let \( k \in \nN \), and assume \( S(j) \) for every \( j < k \). If \( k = 0 \) or \( k > n \), there is nothing to prove, so let \( 1 \le k \le n \). Every line and every box that line \( k \) cites is available at line \( k \), and so lies before line \( k \) (@def-derivation). Hence the induction hypothesis \( \Gamma_j \models \varphi_j \) holds for every line \( j \) that line \( k \) cites, and for the last line of every box it cites.

Let \( v \) be a valuation that makes every formula of \( \Gamma_k \) true. We show \( v(\varphi_k) = \mathrm{T} \); since \( v \) is arbitrary, this proves \( \Gamma_k \models \varphi_k \). By @def-derivation, line \( k \) is a premise, an assumption, or the conclusion of one primitive rule, and the three claims below treat these cases.

**Step 3 (the cases).**

::: {.claim}
If line \( k \) is a premise or an assumption, then \( v(\varphi_k) = \mathrm{T} \).
:::

::: {.proofofclaim}
A premise belongs to every context. An assumption opens a box, that box contains line \( k \), and so its assumption \( \varphi_k \) belongs to \( \Gamma_k \). In both cases \( \varphi_k \) is one of the formulas that \( v \) makes true.
:::

For the one-step rules we first record what the hypothesis gives for a cited line. If line \( k \) cites line \( i \), then line \( i \) is available at line \( k \), so \( \Gamma_i \subseteq \Gamma_k \) by @lem-context-inclusion (a). Hence \( v \) makes every formula of \( \Gamma_i \) true, and the induction hypothesis \( \Gamma_i \models \varphi_i \) gives
\[
v(\varphi_i) = \mathrm{T} \quad \text{for every line } i \text{ cited by line } k . \tag{$\ast$}
\]

::: {.claim}
If line \( k \) is justified by a one-step rule, then \( v(\varphi_k) = \mathrm{T} \).
:::

::: {.proofofclaim}
We take the rules one at a time; in each, the cited lines are true under \( v \) by \( (\ast) \).

*\( \rulename{R} \).* Line \( k \) repeats a line \( i \), so \( \varphi_k = \varphi_i \), and \( v(\varphi_k) = \mathrm{T} \).

*\( \rulename{\wedge I} \).* Line \( k \) is \( \varphi \wedge \psi \), citing lines holding \( \varphi \) and \( \psi \). Both are true under \( v \), so \( \varphi \wedge \psi \) is true by (V3).

*\( \rulename{\wedge E} \).* Line \( k \) is \( \varphi \), citing a line holding \( \varphi \wedge \psi \). That line is true under \( v \), so by (V3) both conjuncts are true, and in particular \( \varphi \). The second form, which writes \( \psi \), is the same with the other conjunct, and we skip it.

*\( \rulename{{\to}E} \).* Line \( k \) is \( \psi \), citing lines holding \( \varphi \to \psi \) and \( \varphi \). Both are true under \( v \). By (V5), an implication with a true hypothesis and a false conclusion is false; since \( \varphi \to \psi \) is true and \( \varphi \) is true, \( \psi \) is true.

*\( \rulename{\vee I} \).* Line \( k \) is \( \varphi \vee \psi \) or \( \psi \vee \varphi \), citing a line holding \( \varphi \). That line is true under \( v \), so both disjunctions are true by (V4).

*\( \rulename{\neg E} \).* Line \( k \) is \( \bot \), citing lines holding \( \varphi \) and \( \neg\varphi \). By \( (\ast) \) both would be true under \( v \), and by (V2) \( \neg\varphi \) is false whenever \( \varphi \) is true. So no valuation makes every formula of \( \Gamma_k \) true, and there is no \( v \) to consider: \( \Gamma_k \models \bot \) holds because there is no row to check.

*\( \rulename{\bot E} \).* Line \( k \) is any formula \( \varphi \), citing a line holding \( \bot \). By \( (\ast) \), \( v(\bot) = \mathrm{T} \), which (V1) forbids. So again no valuation makes every formula of \( \Gamma_k \) true, and \( \Gamma_k \models \varphi \) holds.

*\( \rulename{{\leftrightarrow}E} \).* Line \( k \) is \( \psi \), citing lines holding \( \varphi \leftrightarrow \psi \) and \( \varphi \). Both are true under \( v \); by (V6), \( v(\psi) = v(\varphi) = \mathrm{T} \). The second form, which writes \( \varphi \) from \( \varphi \leftrightarrow \psi \) and \( \psi \), is the same with the sides exchanged, and we skip it.
:::

For the box rules we record what the hypothesis gives for a cited box. If line \( k \) cites, by a box rule, the box from line \( a \) to line \( b \), then \( \Gamma_b = \Gamma_k, \varphi_a \) by @lem-context-inclusion (b), and the induction hypothesis for line \( b \) says
\[
\Gamma_k, \varphi_a \models \varphi_b : \quad \text{every valuation making } \Gamma_k \text{ and } \varphi_a \text{ true makes } \varphi_b \text{ true.} \tag{$\ast\ast$}
\]

::: {.claim}
If line \( k \) is justified by a box rule, then \( v(\varphi_k) = \mathrm{T} \).
:::

::: {.proofofclaim}
Recall that \( v \) makes every formula of \( \Gamma_k \) true.

*\( \rulename{{\to}I} \).* Line \( k \) is \( \varphi \to \psi \), citing a box that opens with \( \varphi \) and ends with \( \psi \). By \( (\ast\ast) \), every valuation making \( \Gamma_k \) and \( \varphi \) true makes \( \psi \) true. If \( v(\varphi) = \mathrm{F} \), then \( v(\varphi \to \psi) = \mathrm{T} \) by (V5). If \( v(\varphi) = \mathrm{T} \), then \( v \) makes \( \Gamma_k \) and \( \varphi \) true, so \( v(\psi) = \mathrm{T} \), and again \( v(\varphi \to \psi) = \mathrm{T} \) by (V5).

*\( \rulename{\neg I} \).* Line \( k \) is \( \neg\varphi \), citing a box that opens with \( \varphi \) and ends with \( \bot \). By \( (\ast\ast) \), every valuation making \( \Gamma_k \) and \( \varphi \) true makes \( \bot \) true; since (V1) makes \( \bot \) false under every valuation, no valuation makes \( \Gamma_k \) and \( \varphi \) true. As \( v \) makes \( \Gamma_k \) true, it must make \( \varphi \) false, and then \( v(\neg\varphi) = \mathrm{T} \) by (V2).

*\( \rulename{RAA} \).* Line \( k \) is \( \varphi \), citing a box that opens with \( \neg\varphi \) and ends with \( \bot \). By \( (\ast\ast) \) and (V1), as in the previous case, no valuation makes \( \Gamma_k \) and \( \neg\varphi \) true. Suppose \( v(\varphi) = \mathrm{F} \). Then \( v(\neg\varphi) = \mathrm{T} \) by (V2), so \( v \) makes \( \Gamma_k \) and \( \neg\varphi \) true, which is impossible. Hence \( v(\varphi) = \mathrm{T} \).

*\( \rulename{\vee E} \).* Line \( k \) is \( \chi \), citing a line \( i \) holding \( \varphi \vee \psi \), a box that opens with \( \varphi \) and ends with \( \chi \), and a box that opens with \( \psi \) and ends with \( \chi \). By \( (\ast) \), \( v(\varphi \vee \psi) = \mathrm{T} \), so by (V4), \( v(\varphi) = \mathrm{T} \) or \( v(\psi) = \mathrm{T} \). By \( (\ast\ast) \) for the first box, every valuation making \( \Gamma_k \) and \( \varphi \) true makes \( \chi \) true; for the second, every valuation making \( \Gamma_k \) and \( \psi \) true makes \( \chi \) true. If \( v(\varphi) = \mathrm{T} \), then \( v \) makes \( \Gamma_k \) and \( \varphi \) true, so \( v(\chi) = \mathrm{T} \). If \( v(\psi) = \mathrm{T} \), the second box gives \( v(\chi) = \mathrm{T} \) in the same way.

*\( \rulename{{\leftrightarrow}I} \).* Line \( k \) is \( \varphi \leftrightarrow \psi \), citing a box that opens with \( \varphi \) and ends with \( \psi \), and one that opens with \( \psi \) and ends with \( \varphi \). By \( (\ast\ast) \), every valuation making \( \Gamma_k \) and \( \varphi \) true makes \( \psi \) true, and every valuation making \( \Gamma_k \) and \( \psi \) true makes \( \varphi \) true. If \( v(\varphi) = \mathrm{T} \), the first box gives \( v(\psi) = \mathrm{T} \). If \( v(\varphi) = \mathrm{F} \), then \( v(\psi) = \mathrm{F} \) too, since \( v(\psi) = \mathrm{T} \) would give \( v(\varphi) = \mathrm{T} \) by the second box. In both cases \( v(\varphi) = v(\psi) \), so \( v(\varphi \leftrightarrow \psi) = \mathrm{T} \) by (V6).
:::

The three claims cover every way line \( k \) can be justified, so \( S(k) \) holds. By @thm-strong-induction, \( S(k) \) holds for every \( k \in \nN \): every line \( k \) of the derivation satisfies \( \Gamma_k \models \varphi_k \).

**Step 4 (the last line).** The last line \( n \) of a derivation lies in no box (@def-derivation), so its context \( \Gamma_n \) consists of the premises alone, and \( \varphi_n = \psi \). By Step 3, \( \Gamma_n \models \psi \). Every premise belongs to \( \Gamma \) (@def-derivable), so a valuation making every formula of \( \Gamma \) true makes every formula of \( \Gamma_n \) true, and hence makes \( \psi \) true. This proves \( \Gamma \models \psi \).
:::

The proof is long, but each case is one step of the truth-table reasoning of Section 3.3, placed in the right context. Every primitive rule has passed. So has every derived rule, since each abbreviates primitive ones. *The rules never lead from truth to falsehood*, not merely line by line but for every derivation that can ever be written.

Why strong induction and the position \( k \) of a line? A rule may cite any available line, however far back: line 7 of the derivation of @prp-contrapositive cites the box that begins at line 2. So the hypothesis is needed for all earlier lines at once. A different route would induct on the length of the whole derivation, removing its last line. But the lines above the last line need not form a derivation, since a box may still be open there (in the derivation of @prp-contrapositive, lines 1–6 end inside the box \( \lines{2}{6} \)), and that route has to cut boxes open. Carrying the context of every line avoids the surgery.

::: {#exm-soundness-run}
[Running the claim on a case split]

Here is a derivation of \( p \vee q \vdash q \vee p \). List the context of each line, and check \( \Gamma_k \models \varphi_k \) for each \( k \), naming the case of the proof that handles it.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \vee q}
  \open
  \hypo {2} {p}
  \have {3} {q \vee p} \oi{2}
  \close
  \open
  \hypo {4} {q}
  \have {5} {q \vee p} \oi{4}
  \close
  \have {6} {q \vee p} \oe{1,2-3,4-5}
\end{nd}$
\end{center}
```
:::

::: {.solution}
The boxes are \( \lines{2}{3} \) and \( \lines{4}{5} \).

| Line | Context \( \Gamma_k \) | Case | Why \( \Gamma_k \models \varphi_k \) |
|---|---|---|---|
| 1 | \( p \vee q \) | premise | \( \varphi_1 \) is in its context |
| 2 | \( p \vee q, \ p \) | assumption | \( \varphi_2 \) is in its context |
| 3 | \( p \vee q, \ p \) | \( \rulename{\vee I} \) citing 2 | \( \Gamma_2 \subseteq \Gamma_3 \); a row making \( p \) true makes \( q \vee p \) true |
| 4 | \( p \vee q, \ q \) | assumption | \( \varphi_4 \) is in its context |
| 5 | \( p \vee q, \ q \) | \( \rulename{\vee I} \) citing 4 | as for line 3, with \( q \) |
| 6 | \( p \vee q \) | \( \rulename{\vee E} \) citing 1 and both boxes | see below |

For line 6: by @lem-context-inclusion (b), \( \Gamma_3 = \Gamma_6, p \) and \( \Gamma_5 = \Gamma_6, q \), and the claim for lines 3 and 5 says that rows making \( p \vee q \) and \( p \) true, and rows making \( p \vee q \) and \( q \) true, make \( q \vee p \) true. A row making \( \Gamma_6 \) true makes \( p \vee q \) true, so it makes \( p \) or \( q \) true, and one of the two boxes applies. Line 6 is the last line, and its context is the premise: so \( p \vee q \models q \vee p \), as soundness promises.
:::

## Refuting with one row

Soundness is most often used backwards. If the conclusion can be false while the premises are true, no derivation can exist.

::: {#cor-refuting-row}
[Refuting Row]

Let \( \Gamma \) be a list of formulas and \( \psi \) a formula. If some valuation makes every formula of \( \Gamma \) true and \( \psi \) false, then \( \Gamma \nvdash \psi \).
:::

::: {.proof}
Let \( v \) make every formula of \( \Gamma \) true and \( \psi \) false. Then \( \Gamma \models \psi \) fails (@def-valid-argument). If \( \Gamma \vdash \psi \) held, @thm-soundness would give \( \Gamma \models \psi \). So \( \Gamma \vdash \psi \) does not hold.
:::

Here \( \Gamma \nvdash \psi \) means that there is **no** derivation of \( \psi \) from premises in \( \Gamma \): not with the primitive rules, not with any derived rule, not in a thousand lines. One row has settled a question about infinitely many derivations.

**Chapter 2's question.** Section 2.6 searched for a derivation of \( P \to Q \vdash Q \to P \) and stalled. The row \( p = \mathrm{F} \), \( q = \mathrm{T} \) makes \( p \to q \) true (false hypothesis) and \( q \to p \) false (true hypothesis, false conclusion). By @cor-refuting-row,
\[
p \to q \nvdash q \to p .
\]
The letters of Chapter 2 stood for arbitrary statements, and the search asked for a derivation of the **pattern**: one derivation, written with \( P \) and \( Q \), that works whatever they are. Such a derivation, with \( P \) and \( Q \) read as the atoms \( p \) and \( q \), would derive \( p \to q \vdash q \to p \), which we have just ruled out. So the pattern has no derivation, and the search was right to fail. (Particular instances can be derivable: with \( P \) and \( Q \) the same statement, \( P \to P \vdash P \to P \) takes one line. A refuting row for atoms speaks about the pattern, as the warning after @lem-substitution said.)

**Affirming the consequent.** Chapter 1 promised, in Sections 1.1 and 1.4, that no derivation leads from \( P \to Q \) and \( Q \) to \( P \), whichever rules of Chapters 1 and 2 it uses. The refuting row of @exm-affirming-the-consequent, \( p = \mathrm{F} \) and \( q = \mathrm{T} \), makes \( p \to q \) and \( q \) true and \( p \) false, so by @cor-refuting-row,
\[
p \to q, \ q \nvdash p .
\]
Chapter 1 could already see that the step "from \( \varphi \to \psi \) and \( \psi \), infer \( \varphi \)" is not an instance of \( \rulename{{\to}E} \). That did not exclude a longer derivation reaching \( p \) some other way. The row excludes every derivation at once. So the repair of Argument B that Section 1.1 considered is not merely unjustified: it is impossible.

**A stall in Chapter 2.** Section 2.5 found that the De Morgan direction \( \neg(P \wedge Q) \vdash \neg P \vee \neg Q \) cannot end with \( \rulename{\vee I} \), because neither \( \neg P \) nor \( \neg Q \) follows from the premise alone, and it said "the rules never lead from true premises to a false conclusion" as its reason. Now that reason is a theorem: the row \( p = \mathrm{T} \), \( q = \mathrm{F} \) makes \( \neg(p \wedge q) \) true and \( \neg p \) false, so \( \neg(p \wedge q) \nvdash \neg p \), and the row \( p = \mathrm{F} \), \( q = \mathrm{T} \) gives \( \neg(p \wedge q) \nvdash \neg q \).

::: {.warning}
A refuting row must make **every** premise true. For \( p \to q, \ p \vdash q \), the row \( p = \mathrm{F} \), \( q = \mathrm{F} \) makes the conclusion false, but it also makes the premise \( p \) false, so it refutes nothing; and the sequent is derivable, by one line of \( \rulename{{\to}E} \). A row in which some premise fails is simply not one of the rows @def-valid-argument looks at.
:::

::: {.warning}
Soundness goes one way. It says that derivable sequents are valid; it does not say that a formula true in the row you happened to check is derivable. The atom \( p \) is true under the all-T valuation, but \( \nvdash p \): the all-F valuation makes it false, so @cor-refuting-row (with \( \Gamma \) empty) applies. Whether **every** valid sequent is derivable is a separate question, answered in Section 3.6.
:::

::: {.check}
Give a row showing \( p \to r \nvdash (p \vee q) \to r \).
:::

::: {.solution}
Take \( p = \mathrm{F} \), \( q = \mathrm{T} \), \( r = \mathrm{F} \). The premise \( p \to r \) is true, since \( p \) is false. The conclusion has hypothesis \( p \vee q \), which is true, and conclusion \( r \), which is false, so it is false. By @cor-refuting-row, no derivation exists. (The rows with \( p \) true fail: they make the premise force \( r \) true, or make the premise false.)
:::

## Reductio says something new

Chapter 2 introduced \( \rulename{RAA} \) in Section 2.5 because the rules before it stalled on \( \neg\neg P \vdash P \), and said that Chapter 3 would prove that no derivation of \( P \) from \( \neg\neg P \) avoids \( \rulename{RAA} \). Truth tables cannot do it. The row method only proves nonderivability from **all** the rules, and with \( \rulename{RAA} \) the sequent is derivable, so no two-valued row refutes it. The trick is to run the proof of @thm-soundness with a different notion of truth, one with three values, under which every rule except \( \rulename{RAA} \) still passes. This result is optional: it answers a question Chapter 2 raised, and nothing later uses it.

A **three-valued valuation** \( u \) assigns to each atom one of the values \( 0 \), \( \frac12 \), \( 1 \), ordered \( 0 < \frac12 < 1 \). Think of \( 1 \) as "true", \( 0 \) as "false", and \( \frac12 \) as "not yet settled". It is extended to all formulas by recursion (@thm-structural-recursion):
\[
\begin{aligned}
u(\bot) &= 0, \qquad u(\neg\varphi) = u(\varphi \to \bot), \\
u(\varphi \wedge \psi) &= \min\{ u(\varphi), u(\psi) \}, \qquad u(\varphi \vee \psi) = \max\{ u(\varphi), u(\psi) \}, \\
u(\varphi \to \psi) &= \begin{cases} 1 & \text{if } u(\varphi) \le u(\psi), \\ u(\psi) & \text{otherwise,} \end{cases} \\
u(\varphi \leftrightarrow \psi) &= \min\{ u(\varphi \to \psi), u(\psi \to \varphi) \} .
\end{aligned}
\]
So \( u(\neg\varphi) = 1 \) if \( u(\varphi) = 0 \), and \( u(\neg\varphi) = 0 \) otherwise. On the values \( 0 \) and \( 1 \) alone these are exactly the tables of @def-truth-value, with \( 1 \) for \( \mathrm{T} \) and \( 0 \) for \( \mathrm{F} \). For a list \( \Gamma \), let \( u(\Gamma) \) be the least of the values \( u(\gamma) \) for \( \gamma \) in \( \Gamma \), and \( u(\Gamma) = 1 \) if \( \Gamma \) is empty. Write \( \Gamma \models_3 \psi \) if \( u(\Gamma) \le u(\psi) \) for every three-valued valuation \( u \): the conclusion is at least as true as the weakest premise.

::: {#thm-raa-independent .optional}
[Reductio Is Not Derivable from the Other Rules]

Neither \( \neg\neg p \vdash p \) nor \( \vdash p \vee \neg p \) has a derivation that uses only the primitive rules other than \( \rulename{RAA} \) (and derived rules derived from those).
:::

::: {.idea}
Repeat the proof of @thm-soundness with \( \models_3 \) in place of \( \models \): every line of a derivation without \( \rulename{RAA} \) satisfies \( \Gamma_k \models_3 \varphi_k \). Then show that both sequents fail for \( \models_3 \), at \( u(p) = \frac12 \). The one case that breaks is \( \rulename{RAA} \), and that is the point.
:::

::: {.proof}
As in Step 1 of the proof of @thm-soundness, a derived rule derived without \( \rulename{RAA} \) abbreviates a pasted derivation in the primitive rules other than \( \rulename{RAA} \), so it is enough to consider those. Fix a derivation that uses only the primitive rules other than \( \rulename{RAA} \), with lines \( 1, \dots, n \), formulas \( \varphi_k \) and contexts \( \Gamma_k \). We show \( \Gamma_k \models_3 \varphi_k \) for every \( k \) with \( 1 \le k \le n \), by @thm-strong-induction exactly as in Step 2 of the proof of @thm-soundness, the cases \( k = 0 \) and \( k > n \) being vacuous. Fix \( k \), assume the claim for all earlier lines, and fix a three-valued valuation \( u \); write \( m = u(\Gamma_k) \). We must show \( m \le u(\varphi_k) \). Two facts do the bookkeeping. If line \( k \) cites line \( i \), then \( \Gamma_i \subseteq \Gamma_k \) (@lem-context-inclusion (a)), and the least value over a longer list is at most the least over a shorter one, so \( m \le u(\Gamma_i) \le u(\varphi_i) \). If line \( k \) cites a box from line \( a \) to line \( b \) by a box rule, then \( \Gamma_b = \Gamma_k, \varphi_a \) (@lem-context-inclusion (b)), so the hypothesis for line \( b \) says \( \min\{ m, u(\varphi_a) \} \le u(\varphi_b) \). Below, \( x = u(\varphi) \), \( y = u(\psi) \), \( z = u(\chi) \).

*Premises and assumptions:* \( \varphi_k \) is in \( \Gamma_k \), so \( m \le u(\varphi_k) \). *\( \rulename{R} \):* \( m \le u(\varphi_i) = u(\varphi_k) \). *\( \rulename{\wedge I} \):* \( m \le x \) and \( m \le y \), so \( m \le \min\{x, y\} \). *\( \rulename{\wedge E} \):* \( m \le \min\{x, y\} \le x \), and likewise \( \le y \). *\( \rulename{\vee I} \):* \( m \le x \le \max\{x, y\} \).

*\( \rulename{{\to}E} \):* \( m \le u(\varphi \to \psi) \) and \( m \le x \). If \( x \le y \), then \( m \le x \le y \). Otherwise \( u(\varphi \to \psi) = y \), so \( m \le y \). *\( \rulename{{\leftrightarrow}E} \):* \( m \le u(\varphi \leftrightarrow \psi) \le u(\varphi \to \psi) \) and \( m \le x \), so \( m \le y \) as for \( \rulename{{\to}E} \); the second form is symmetric.

*\( \rulename{\neg E} \):* \( m \le x \) and \( m \le u(\neg\varphi) \). If \( x = 0 \), then \( m \le 0 \); if \( x > 0 \), then \( u(\neg\varphi) = 0 \) and \( m \le 0 \). So \( m = 0 = u(\bot) \). *\( \rulename{\bot E} \):* \( m \le u(\bot) = 0 \), so \( m = 0 \le u(\varphi_k) \).

*\( \rulename{{\to}I} \):* the hypothesis gives \( \min\{m, x\} \le y \). If \( x \le y \), then \( u(\varphi \to \psi) = 1 \ge m \). Otherwise \( y < x \) and \( u(\varphi \to \psi) = y \); since \( \min\{m, x\} \le y < x \), the minimum is not \( x \), so it is \( m \), and \( m \le y \). *\( \rulename{{\leftrightarrow}I} \):* the same argument for each box gives \( m \le u(\varphi \to \psi) \) and \( m \le u(\psi \to \varphi) \), so \( m \) is at most their minimum.

*\( \rulename{\neg I} \):* the hypothesis gives \( \min\{m, x\} \le u(\bot) = 0 \). If \( x = 0 \), then \( u(\neg\varphi) = 1 \ge m \). If \( x > 0 \), the minimum is \( 0 \) and is not \( x \), so \( m = 0 \le u(\neg\varphi) \).

*\( \rulename{\vee E} \):* \( m \le \max\{x, y\} \), and the boxes give \( \min\{m, x\} \le z \) and \( \min\{m, y\} \le z \). If \( x \ge y \), then \( m \le x \), so \( \min\{m, x\} = m \) and \( m \le z \). If \( y > x \), then \( m \le y \) and \( m \le z \) from the second box.

This covers every rule used, so \( \Gamma_k \models_3 \varphi_k \) for every line, and in particular for the last line, whose context is the premises. As in Step 4 of the proof of @thm-soundness, a list containing all the premises has least value at most theirs, so every sequent \( \Gamma \vdash \psi \) derived without \( \rulename{RAA} \) satisfies \( \Gamma \models_3 \psi \).

Now let \( u(p) = \frac12 \). Then \( u(\neg p) = 0 \), since \( \frac12 > 0 \), and \( u(\neg\neg p) = 1 \), since \( u(\neg p) = 0 \). So \( u(\neg\neg p) = 1 > \frac12 = u(p) \), and \( \neg\neg p \models_3 p \) fails. Also \( u(p \vee \neg p) = \max\{ \frac12, 0 \} = \frac12 < 1 \), the value of the empty list, so \( \models_3 p \vee \neg p \) fails. Hence neither sequent is derivable without \( \rulename{RAA} \).
:::

The case that was not written is \( \rulename{RAA} \) itself. Its box would give \( \min\{m, u(\neg\varphi)\} \le 0 \), and we would need \( m \le x \). At \( u(\varphi) = \frac12 \) the box gives nothing, since \( u(\neg\varphi) = 0 \) already, while \( m \) may be \( 1 \). This is the three-valued face of the question asked in the Idea of @thm-soundness: the two-valued \( \rulename{RAA} \) case used that \( v(\varphi) = \mathrm{F} \) forces \( v(\neg\varphi) = \mathrm{T} \), and with a third value, \( \varphi \) and \( \neg\varphi \) can both fail to be true.

::: {.remark}
The same values settle Peirce's law, \( ((p \to q) \to p) \to p \), which Section 2.5 derived with \( \rulename{RAA} \) (@prp-peirce): at \( u(p) = \frac12 \), \( u(q) = 0 \), we get \( u(p \to q) = 0 \), \( u((p \to q) \to p) = 1 \), and the whole formula has value \( \frac12 \), so it too needs \( \rulename{RAA} \). The values do not refute everything Chapter 2 derived with \( \rulename{RAA} \): the De Morgan direction \( \neg(p \wedge q) \vdash \neg p \vee \neg q \) passes this test, and so does \( \vdash (p \to q) \vee (q \to p) \). Neither of these is derivable without \( \rulename{RAA} \) either, but showing that needs a different kind of model, and this book states it without proof, as Chapter 2 did for De Morgan's law. \( \rulename{RAA} \) says something the other rules cannot, and Chapter 5 says what it is and who objected to it.
:::

## Exercises

### A. Check your understanding

::: {#exr-soundness-a1}
[A1]

These parts are about the proof of @thm-soundness. Part (c) uses the derivation of @prp-vacuous-implication, written with atoms:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg p}
  \open
  \hypo {2} {p}
  \have {3} {\bot} \ne{2,1}
  \have {4} {q} \be{3}
  \close
  \have {5} {p \to q} \ii{2-4}
\end{nd}$
\end{center}
```

::: {.enumerate options="label=(\alph*)"}
1. Why does the proof use strong induction on \( k \), rather than ordinary induction from line \( k \) to line \( k + 1 \)?
2. In the \( \rulename{\vee E} \) case, the induction hypothesis is applied to the last lines \( b \) and \( d \) of the two boxes. What does it say about each, and which part of @lem-context-inclusion identifies the contexts?
3. List the context of each of the five lines of the derivation above, and check \( \Gamma_k \models \varphi_k \) for each.
4. Suppose a rule "from \( \varphi \to \psi \) and \( \psi \), infer \( \varphi \)" were added to the primitive rules. Which part of the proof would fail? Give a valuation showing it.
5. Where does Step 4 use that the last line of a derivation lies in no box?
:::
:::

::: {.solution}
*(a)* A rule may cite any available line, however far back, and the last line of a box that closed long ago. The hypothesis must therefore be available for every earlier line, not just for line \( k - 1 \). For example, line 7 of the derivation of @prp-contrapositive uses the claim for line 6, and line 6 uses it for line 5; but line 5 uses it for line 2, three lines back.

*(b)* It says \( \Gamma_b \models \chi \) and \( \Gamma_d \models \chi \). By @lem-context-inclusion (b), \( \Gamma_b = \Gamma_k, \varphi \) and \( \Gamma_d = \Gamma_k, \psi \): every row making \( \Gamma_k \) and \( \varphi \) true makes \( \chi \) true, and every row making \( \Gamma_k \) and \( \psi \) true makes \( \chi \) true. It is **not** \( \Gamma_k \models \chi \), which is what we are trying to prove.

*(c)* The box is \( \lines{2}{4} \).

| Line | Context | Check |
|---|---|---|
| 1 | \( \neg p \) | premise, in its context |
| 2 | \( \neg p, \ p \) | assumption, in its context |
| 3 | \( \neg p, \ p \) | no row makes \( \neg p \) and \( p \) true, so it entails \( \bot \) |
| 4 | \( \neg p, \ p \) | the same unsatisfiable context entails \( q \) |
| 5 | \( \neg p \) | a row making \( \neg p \) true makes \( p \) false, so \( p \to q \) true |

Line 3 is the \( \rulename{\neg E} \) case, line 4 the \( \rulename{\bot E} \) case, and line 5 the \( \rulename{{\to}I} \) case, with \( \Gamma_4 = \Gamma_5, p \) by @lem-context-inclusion (b).

*(d)* Claim 2, the one-step rules: it would need a new case, and the case is false. From \( v(\varphi \to \psi) = \mathrm{T} \) and \( v(\psi) = \mathrm{T} \) nothing follows about \( v(\varphi) \). The valuation with \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{T} \) makes \( p \to q \) and \( q \) true and \( p \) false; with the new rule, the three-line derivation of \( p \) from \( p \to q \) and \( q \) would have a last line whose context does not entail it.

*(e)* It concludes that the context of the last line is just the premises. Without that, the last line could depend on an undischarged assumption, and \( \Gamma_n \models \psi \) would say nothing about the rows making the premises true.
:::

### B. Practice

::: {#exr-soundness-b1}
[B1: Derivable or not]

Determine which of the following are derivable. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (p \wedge q) \to r \vdash p \to r \).
2. \( \neg(p \wedge q) \vdash \neg p \).
3. \( p \leftrightarrow q, \ q \vee r \vdash p \).
4. \( p \to (q \vee r) \vdash (p \to q) \vee (p \to r) \).
:::
:::

::: {.solution}
*(a)* Not derivable. The row \( p = \mathrm{T} \), \( q = \mathrm{F} \), \( r = \mathrm{F} \) makes the premise true (its hypothesis \( p \wedge q \) is false) and the conclusion \( p \to r \) false. By @cor-refuting-row there is no derivation.

*(b)* Not derivable. The row \( p = \mathrm{T} \), \( q = \mathrm{F} \) makes \( p \wedge q \) false, so \( \neg(p \wedge q) \) true, and \( \neg p \) false. By @cor-refuting-row there is no derivation.

*(c)* Not derivable. The row \( p = \mathrm{F} \), \( q = \mathrm{F} \), \( r = \mathrm{T} \) makes \( p \leftrightarrow q \) true (both sides false) and \( q \vee r \) true, and \( p \) false.

*(d)* Derivable: @exm-search-postpone-or in Section 2.6 derives it, with \( \rulename{LEM} \) on \( q \). So no row can refute it: by @thm-soundness it is valid. A search for a refuting row confirms this. The conclusion is false only if both \( p \to q \) and \( p \to r \) are false, that is, \( p = \mathrm{T} \) and \( q = r = \mathrm{F} \); but then \( q \vee r \) is false and the premise is false.

The trap is (d). Its conclusion **looks** stronger than the premise, since it seems to decide in advance which disjunct follows from \( p \); but a derivation exists, and trying to refute it by a row is bound to fail.
:::

::: {#exr-soundness-b2}
[B2: Ordering the \( \vee \)E case]

Here are nine lines. Seven of them, in the right order, form the \( \rulename{\vee E} \) case of the proof of @thm-soundness. Line \( k \) is \( \chi \), by \( \rulename{\vee E} \) citing line \( i \) (holding \( \varphi \vee \psi \)), the box from line \( a \) to line \( b \) (opening with \( \varphi \), ending with \( \chi \)), and the box from line \( c \) to line \( d \) (opening with \( \psi \), ending with \( \chi \)). Give an admissible order, and say why each of the other two lines cannot be used.

*(i)* By the induction hypothesis for lines \( b \) and \( d \), which come before line \( k \), \( \Gamma_b \models \chi \) and \( \Gamma_d \models \chi \).

(ii) Hence \( v(\chi) = \mathrm{T} \) in either case; since \( v \) was arbitrary, \( \Gamma_k \models \chi \).

(iii) Let \( v \) be a valuation making every formula of \( \Gamma_k \) true.

(iv) If \( v(\psi) = \mathrm{T} \), then \( v \) makes every formula of \( \Gamma_d \) true, so \( v(\chi) = \mathrm{T} \).

*(v)* By @lem-context-inclusion (a), \( \Gamma_i \subseteq \Gamma_k \), so \( v \) makes every formula of \( \Gamma_i \) true; by the induction hypothesis for line \( i \), \( v(\varphi \vee \psi) = \mathrm{T} \), so \( v(\varphi) = \mathrm{T} \) or \( v(\psi) = \mathrm{T} \).

(vi) By the induction hypothesis for line \( k \), \( \Gamma_k \models \chi \).

(vii) By @lem-context-inclusion (b), \( \Gamma_b \) is \( \Gamma_k \) with \( \varphi \) added, and \( \Gamma_d \) is \( \Gamma_k \) with \( \psi \) added.

(viii) If \( v(\varphi) = \mathrm{T} \), then \( v \) makes every formula of \( \Gamma_b \) true, so \( v(\chi) = \mathrm{T} \).

(ix) Line \( b \) is inside the box, and the box was cited at line \( k \), so the context of line \( b \) is \( \Gamma_k \); the induction hypothesis for line \( b \) then gives \( \Gamma_k \models \chi \) directly.
:::

::: {.solution}
An admissible order: (iii), (v), (vii), (i), (viii), (iv), (ii).

What each line needs: (v) and (viii), (iv) use the valuation fixed in (iii); (viii) and (iv) use (vii) and (i); (ii) uses the case split of (v) and both of (viii) and (iv). So any order is admissible in which (iii) comes before (v), (viii), and (iv); (vii) and (i) come before (viii) and (iv); (v) comes before (ii); and (viii) and (iv) come before (ii). For instance (vii), (i), (iii), (v), (iv), (viii), (ii) is also admissible: (vii) and (i) do not mention \( v \), and the two cases may be taken in either order.

Line (vi) applies the induction hypothesis to line \( k \) itself. The hypothesis of @thm-strong-induction covers only the lines \( j < k \); (vi) assumes what is to be proved.

Line (ix) uses the context of the citing line for the box's last line. It is false: line \( b \) lies inside the box, whose assumption \( \varphi \) is part of its context, so \( \Gamma_b = \Gamma_k, \varphi \), not \( \Gamma_k \). In the derivation of @exm-soundness-run, line 3 has context \( p \vee q, \ p \), while line 6 has context \( p \vee q \), and \( p \vee q \models q \vee p \) could not be read off from line 3 directly.
:::

### C. Going deeper

::: {#exr-soundness-c1}
[C1: A safe rule and an unsafe one]

::: {.enumerate options="label=(\alph*)"}
1. Add to the primitive rules a one-step rule \( \mathsf{X} \): from a line \( \varphi \wedge \psi \), infer \( \varphi \vee \psi \). Show that @thm-soundness still holds for derivations that may use \( \mathsf{X} \).
2. Add instead a one-step rule \( \mathsf{Y} \): from a line \( \varphi \vee \psi \), infer \( \varphi \wedge \psi \). Show that soundness fails: name the case of the proof that breaks, give a derivation using \( \mathsf{Y} \) of a sequent with a refuting row, and give the row.
:::
:::

::: {.solution}
[Hint 1]

The proof of @thm-soundness treats one rule per case. Adding a rule adds one case to Claim 2 and changes nothing else.
:::

::: {.solution}
[Hint 2]

For (b), start a derivation from the premise \( p \), and look for a way to write \( p \vee q \) first.
:::

::: {.solution}
*(a)* The proof of @thm-soundness goes through with one more case in Claim 2. Every other part is unchanged: Step 1 and Step 4 do not look at the rules, @lem-context-inclusion (a) holds for any cited line, and (b) concerns only box rules, and \( \mathsf{X} \) is not one. *The case \( \mathsf{X} \).* Line \( k \) is \( \varphi \vee \psi \), citing a line \( i \) holding \( \varphi \wedge \psi \). By \( (\ast) \), \( v(\varphi \wedge \psi) = \mathrm{T} \), so \( v(\varphi) = \mathrm{T} \) by (V3), and \( v(\varphi \vee \psi) = \mathrm{T} \) by (V4). So every line of a derivation with \( \mathsf{X} \) still satisfies \( \Gamma_k \models \varphi_k \), and soundness holds.

*(b)* The new case of Claim 2 fails: from \( v(\varphi \vee \psi) = \mathrm{T} \), (V4) gives only that one disjunct is true, and (V3) needs both. With \( \mathsf{Y} \), this is a derivation of \( p \vdash q \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p}
  \have {2} {p \vee q} \oi{1}
  \have {3} {p \wedge q} \by{Y}{2}
  \have {4} {q} \ae{3}
\end{nd}$
\end{center}
```

The row \( p = \mathrm{T} \), \( q = \mathrm{F} \) makes the premise true and the conclusion false, so \( p \not\models q \), although \( p \vdash q \) with \( \mathsf{Y} \). The failure is at line 3: its context is \( p \), and the row makes \( p \) and line 2 true but line 3 false.

**Marking scheme.** (10 points)

- 2: (a) says that only one case is added, and why the rest of the proof (Steps 1 and 4, @lem-context-inclusion) is unaffected.
- 3: (a) the case for \( \mathsf{X} \), using the hypothesis for the cited line through @lem-context-inclusion (a) and the clauses (V3), (V4).
- 2: (b) names the failing case, with the reason (one true disjunct does not give a true conjunction).
- 3: (b) a correct derivation with \( \mathsf{Y} \) and a refuting row for its sequent.

Fatal errors (0 for the step): a "refuting row" that makes a premise false; in (a), checking \( \mathsf{X} \) only on atoms without the context argument.
:::

::: {#exr-soundness-c2}
[C2: Exit check: soundness]

*Close the section first, and write from memory.*

Write out, in full, the \( \rulename{{\to}I} \), \( \rulename{\neg I} \) and \( \rulename{\vee E} \) cases of the proof of @thm-soundness: state the claim being proved for every line, set up the induction, and prove the three cases, naming the reason for each step.
:::

::: {.solution}
*The claim.* Fix a derivation in primitive rules with lines \( 1, \dots, n \), and write \( \varphi_k \) for the formula on line \( k \) and \( \Gamma_k \) for its context (@def-derivation). We prove \( \Gamma_k \models \varphi_k \) for every \( k \) with \( 1 \le k \le n \), by @thm-strong-induction applied to "if \( 1 \le k \le n \), then \( \Gamma_k \models \varphi_k \)" (for \( k = 0 \) it holds vacuously): fix \( k \) with \( 1 \le k \le n \), assume \( \Gamma_j \models \varphi_j \) for every line \( j < k \), and let \( v \) be a valuation making every formula of \( \Gamma_k \) true. Every line and box that line \( k \) cites lies before line \( k \), so the hypothesis applies to the cited lines and to the last lines of the cited boxes. We show \( v(\varphi_k) = \mathrm{T} \).

*\( \rulename{{\to}I} \).* Line \( k \) is \( \varphi \to \psi \), citing the box from line \( a \) (the assumption \( \varphi \)) to line \( b \) (the formula \( \psi \)). By @lem-context-inclusion (b), \( \Gamma_b = \Gamma_k, \varphi \). Since \( b < k \), the hypothesis gives \( \Gamma_k, \varphi \models \psi \). If \( v(\varphi) = \mathrm{F} \), then \( v(\varphi \to \psi) = \mathrm{T} \) by (V5). If \( v(\varphi) = \mathrm{T} \), then \( v \) makes every formula of \( \Gamma_k, \varphi \) true, so \( v(\psi) = \mathrm{T} \), and \( v(\varphi \to \psi) = \mathrm{T} \) by (V5).

*\( \rulename{\neg I} \).* Line \( k \) is \( \neg\varphi \), citing the box from line \( a \) (the assumption \( \varphi \)) to line \( b \) (the formula \( \bot \)). By @lem-context-inclusion (b) and the hypothesis for line \( b \), \( \Gamma_k, \varphi \models \bot \). Since \( v(\bot) = \mathrm{F} \) under every valuation (V1), no valuation makes all of \( \Gamma_k, \varphi \) true. As \( v \) makes \( \Gamma_k \) true, \( v(\varphi) = \mathrm{F} \), so \( v(\neg\varphi) = \mathrm{T} \) by (V2).

*\( \rulename{\vee E} \).* Line \( k \) is \( \chi \), citing line \( i \) (holding \( \varphi \vee \psi \)) and the boxes from \( a \) to \( b \) (\( \varphi \) to \( \chi \)) and from \( c \) to \( d \) (\( \psi \) to \( \chi \)). Line \( i \) is available at line \( k \), so \( \Gamma_i \subseteq \Gamma_k \) by @lem-context-inclusion (a); \( v \) makes \( \Gamma_i \) true, and the hypothesis for line \( i \) gives \( v(\varphi \vee \psi) = \mathrm{T} \), so \( v(\varphi) = \mathrm{T} \) or \( v(\psi) = \mathrm{T} \) by (V4). By @lem-context-inclusion (b), \( \Gamma_b = \Gamma_k, \varphi \) and \( \Gamma_d = \Gamma_k, \psi \), and the hypothesis for lines \( b \) and \( d \) gives \( \Gamma_k, \varphi \models \chi \) and \( \Gamma_k, \psi \models \chi \). If \( v(\varphi) = \mathrm{T} \), then \( v \) makes \( \Gamma_k, \varphi \) true, so \( v(\chi) = \mathrm{T} \); if \( v(\psi) = \mathrm{T} \), likewise by the second box.

*Conclusion.* With the other cases, the induction gives \( \Gamma_k \models \varphi_k \) for every line. The last line lies in no box, so its context is the premises, which all belong to \( \Gamma \); a valuation making \( \Gamma \) true makes the premises true, and so makes the last line \( \psi \) true: \( \Gamma \models \psi \).

**Marking scheme.** (10 points)

- 2: states the claim \( \Gamma_k \models \varphi_k \) for **every** line, with contexts.
- 2: uses the course-of-values hypothesis on earlier lines only, and says why the cited lines and boxes are earlier.
- 2: identifies the context of each box's last line as \( \Gamma_k \) plus the box's assumption, citing @lem-context-inclusion (b) (and (a) for the cited line in \( \vee \)E).
- 1 + 1 + 1: the semantic step in each of the three cases (the rows where the assumption is false for \( \to \)I; no row satisfies the box's context for \( \neg \)I; the split on which disjunct is true for \( \vee \)E).
- 1: the conclusion for the last line.

A proof that inducts on the length of the derivation instead, and handles open boxes correctly, earns the same points step for step. Fatal errors (0 for the step): applying the hypothesis to line \( k \) itself; using \( \Gamma_k \) as the context of a box's last line.
:::

<!-- dependency ledger
thm-soundness (proof): every derived-rule line expands into primitive rules, and chains of derived rules end in primitive rules (Step 1) | def-derived-rule and Section 2.3 ("Convenience, not power"), recalled in prose
thm-soundness (claim): rules stated as schemas apply to formulas; derivations with letters read as atoms are derivations | def-rule-schema; Section 3.1 schema remark
thm-soundness (claim): the list of primitive rules | Section 2.6 reference sheet ("The rules in one place"), recalled in prose
lem-context-inclusion (proof): boxes are disjoint or nested; availability of lines and boxes; the box rules require their box's last line to be a line of that box itself | def-derivation (scope rule), def-rules-implication, def-rules-negation, def-rule-raa, def-rules-disjunction, def-rules-biconditional (the sentence is inside each drafted block)
lem-context-inclusion (example): a box may end on the same line as a box inside it (the warning after the lemma) | def-derivation; exm-disjunction-regroup discussion (Ch 1 §07)
thm-soundness (proof): a context entails any of its own members; an unsatisfiable context entails everything; adding premises keeps |= | def-valid-argument and its paraphrase (Section 3.4)
thm-soundness (proof): every cited line and box lies before line k | def-derivation (available means earlier)
thm-soundness (claim): the lines above the last line need not form a derivation (lines 1-6 of the printed derivation of prp-contrapositive end inside box 2-6) | inline, checkable on the printed derivation
cor-refuting-row (example): the rows for p -> q |/- q -> p; p -> q, q |/- p; not(p and q) |/- not p, and |/- not q; the Quick check row; B1 rows | inline; checked by verify/ch03/cor-refuting-row.py and verify/ch03/exr-soundness-b1.py
cor-refuting-row (claim): a derivation of the pattern with letters, read with atoms, is a derivation of the atom sequent | def-rule-schema; Section 3.1 schema remark
exr-soundness-b1 (solution): (d) is derivable | exm-search-postpone-or (Ch 2 §06), cited
thm-raa-independent (proof): the three-valued recursion is well defined; min over a longer list is at most min over a shorter; every rule except RAA preserves |=_3 | thm-structural-recursion (cited); inline; every case checked exhaustively over all value combinations by verify/ch03/thm-raa-independent.py
thm-raa-independent (claim): Peirce at (1/2, 0) has value 1/2; De Morgan (d) and (p -> q) or (q -> p) are not refuted by these values, and neither is derivable without RAA (remark) | values checked by verify/ch03/thm-raa-independent.py; the non-derivability is stated without proof and marked so; nothing depends on it
exr-soundness-c1 (solution): derivation with Y; row p = T, q = F | checked by verify/ch03/exr-soundness-c1.py
-->
