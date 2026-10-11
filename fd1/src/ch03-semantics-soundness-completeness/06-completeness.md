# Completeness

Soundness (@thm-soundness) says that the rules of Chapters 1 and 2 never lead from true premises to a false conclusion: whatever can be derived is true in every row where the premises are. That answers half of the chapter's question. The other half is the converse. Could the rules be too **weak**, so that some sequent is true in every row and yet no derivation of it exists? This section proves that they are not: every truth-table consequence has a derivation. The proof reads a derivation off the truth table, one row at a time, and then glues the rows together with excluded middle.

## The question soundness leaves open

Recall the two relations from Section 3.4. \( \Gamma \vdash \psi \) says that **there is** a derivation of \( \psi \) from premises in \( \Gamma \) (@def-derivable). \( \Gamma \models \psi \) says that **every** valuation making all of \( \Gamma \) true makes \( \psi \) true (@def-valid-argument). Soundness is the implication
\[
\Gamma \vdash \psi \ \Rightarrow \ \Gamma \models \psi .
\]
Its converse is not automatic. The rules are a list that people wrote down, and a list can leave something out. Suppose, as a thought experiment, that we struck \( \rulename{RAA} \) (@def-rule-raa) from the list. Every derivation that remains is still a derivation, so soundness still holds. But the tautology \( p \vee \neg p \) would then have no derivation (this is the optional @thm-raa-independent of Section 3.5). So a sound list of rules can be too short. The question is whether **our** list is long enough.

Here is a sequent to keep in mind. The formula \( (p \to q) \vee (q \to p) \) is a tautology: if \( q \) is true then \( p \to q \) is true, and if \( q \) is false then \( q \to p \) is true. Chapter 2 found a derivation of it (@exr-finding-derivations-c2), but only after reaching for \( \rulename{LEM} \), and nothing in Chapter 2 promised that a derivation would be there to find. We want a theorem that promises it in advance, for every tautology and every valid sequent.

We are going to prove:

> If \( \Gamma \) is a list of formulas and \( \Gamma \models \psi \), then \( \Gamma \vdash \psi \).

The plan has two ideas, one per row and one for all the rows together.

1. **One row gives one derivation.** Fix a row of the truth table, that is, a valuation \( v \). Write each atom as it stands in that row: \( p \) if \( v \) makes \( p \) true, \( \neg p \) if \( v \) makes it false. From these signed atoms we will derive the formula \( \psi \) if \( \psi \) is true in the row, and \( \neg\psi \) if it is false. The derivation climbs the parse tree of \( \psi \), one connective at a time.
2. **The rows are glued by excluded middle.** If \( \Gamma \models \psi \), the first idea gives \( \psi \) from \( \Gamma \) and the signed atoms of **each** row. Two rows that differ only at the atom \( p \) have derivations from "\( \ldots, p \)" and from "\( \ldots, \neg p \)". The rule \( \rulename{\vee E} \) applied to \( p \vee \neg p \) merges them into one derivation that no longer mentions \( p \). Removing the atoms one at a time leaves a derivation from \( \Gamma \) alone.

The first idea is known as Kalmár's lemma, and gluing rows by excluded middle is the standard way to finish; the route is the classical one. We keep the premises \( \Gamma \) throughout, and we isolate the two ingredients as lemmas so that each can be checked on its own. Before either, we need a little bookkeeping about derivations.

## Bookkeeping: adding premises and chaining derivations

In Chapter 2 we learned to use a proved sequent as a single line (@def-derived-rule): its derivation could be pasted in, with its letters replaced by formulas. The completeness proof uses this move dozens of times, so we now state exactly what it gives and check that pasting really produces a derivation.

::: {#lem-weakening-cut}
[Weakening and Cut]

Let \( \Gamma \) and \( \Delta \) be lists of formulas, and let \( \varphi \), \( \psi \), \( \alpha_1, \dots, \alpha_m \) (\( m \ge 1 \)), and \( \beta \) be formulas.

::: {.enumerate options="label=(\alph*)"}
1. **Weakening.** If \( \Gamma \vdash \psi \) and every member of \( \Gamma \) is a member of \( \Delta \), then \( \Delta \vdash \psi \). In particular, \( \Gamma \vdash \psi \) implies \( \Gamma, \varphi \vdash \psi \).
2. **Cut.** If \( \Gamma \vdash \varphi \) and \( \Gamma, \varphi \vdash \psi \), then \( \Gamma \vdash \psi \).
3. **Chaining.** If \( \Gamma \vdash \alpha_i \) for **every** \( i = 1, \dots, m \), and \( \alpha_1, \dots, \alpha_m \vdash \beta \), then \( \Gamma \vdash \beta \).
:::
:::

In words: (a) extra premises never hurt; (b) a formula that has been derived may be used as a premise; (c) a sequent already proved can be applied to formulas already derived. Part (c) is @def-derived-rule for sequents: applying a proved sequent to formulas already derived, outside every box. Inside a box, Section 2.3's expansion does the same job.

::: {.idea}
Part (a) is read off @def-derivable, which asks only that the premises of the derivation **belong to** the list. For (b) and (c), write the derivations one after another and let the last one cite, instead of its premise \( \alpha_i \), the last line of the derivation of \( \alpha_i \). The only thing to check is the scope rule of @def-derivation: the last line of a derivation lies in no box, so it stays available to everything written after it.
:::

::: {.proof}
*(a)* A derivation witnessing \( \Gamma \vdash \psi \) has premises that belong to \( \Gamma \), hence to \( \Delta \), and its last line is \( \psi \). By @def-derivable it witnesses \( \Delta \vdash \psi \). The second sentence is the case where \( \Delta \) is \( \Gamma, \varphi \).

For (b) and (c) we prove one statement that contains both:

\( (\ast) \) If \( \Gamma \vdash \alpha_i \) for every \( i = 1, \dots, m \), and \( \Gamma, \alpha_1, \dots, \alpha_m \vdash \beta \), then \( \Gamma \vdash \beta \).

Part (b) is \( (\ast) \) with \( m = 1 \), \( \alpha_1 = \varphi \) and \( \beta = \psi \). Part (c) follows from \( (\ast) \), since \( \alpha_1, \dots, \alpha_m \vdash \beta \) gives \( \Gamma, \alpha_1, \dots, \alpha_m \vdash \beta \) by (a).

To prove \( (\ast) \), let \( D_i \) be a derivation of \( \alpha_i \) with premises in \( \Gamma \), for each \( i \), and let \( E \) be a derivation of \( \beta \) with premises in \( \Gamma, \alpha_1, \dots, \alpha_m \). If the last line of \( E \) is one of its premises, then \( \beta \) is a member of \( \Gamma \), and the one-line derivation whose only line is the premise \( \beta \) shows \( \Gamma \vdash \beta \); or \( \beta \) is some \( \alpha_i \), and \( D_i \) shows \( \Gamma \vdash \beta \). Otherwise, build a list of lines \( F \) as follows.

1. First, as premises, every premise of \( D_1, \dots, D_m \), and every premise of \( E \) that is a member of \( \Gamma \).
2. Then the lines of \( D_1 \) that are not premises, then those of \( D_2 \), and so on up to \( D_m \), each with its boxes.
3. Then the lines of \( E \) that are not premises, with its boxes.

Renumber the lines, and change each citation as follows. A citation of a premise that is in \( \Gamma \) now cites the premise line of step 1 carrying that formula. A citation in \( E \) of a premise \( \alpha_i \) that is not in \( \Gamma \) now cites the last line of \( D_i \); that line is not a premise of \( D_i \), because the premises of \( D_i \) are in \( \Gamma \) and \( \alpha_i \) is not, so it was copied in step 2. Every other citation follows its line to its new number.

We check that \( F \) is a derivation (@def-derivation). The premises come first and lie in no box. The boxes are those of the \( D_i \) and of \( E \), moved as blocks, so two boxes are still disjoint or nested, each still begins with its assumption, and each line lies in exactly the boxes it lay in before. Hence a line and a box that were available at a citing line are still available there, since the boxes containing each are unchanged. A premise line of step 1 lies in no box and comes first, so it is available at every later line. The last line of \( D_i \) lies in no box (it was the last line of a derivation) and comes before every line of \( E \), so it is available at every line of \( E \). Each line carries the same formula and the same justification as before, citing lines with the same formulas, so it is an instance of the same rule. Finally, the last line of \( F \) is the last line of \( E \), namely \( \beta \), and it lies in no box. The premises of \( F \) are all in \( \Gamma \). Therefore \( \Gamma \vdash \beta \), which proves \( (\ast) \).
:::

The lemma is pure bookkeeping, but it is what makes "cite a proved sequent as one line" honest. From now on, when a derivation cites a sequent proved earlier as a single line, the lemma (for a line in no box) or @def-derived-rule (for a line inside a box, where the cited lines are repeated inside the box first) is the reason the result is a derivation in the primitive rules. As Section 3.5 said, soundness was proved for the primitive rules, and a line citing a derived rule abbreviates a pasted derivation; for whole derivations, part (c) is the precise form of "abbreviates", and inside a box the pasting of @def-derived-rule is the same bookkeeping.

::: {.check}
Suppose \( \Gamma \vdash \alpha \) and \( \Gamma \vdash \neg\alpha \). Which part of @lem-weakening-cut, applied to which proved sequent, gives \( \Gamma \vdash \chi \) for every formula \( \chi \)?
:::

::: {.solution}
Part (c) with \( m = 2 \), \( \alpha_1 = \alpha \), \( \alpha_2 = \neg\alpha \) and \( \beta = \chi \), applied to @prp-ex-falso, \( P, \neg P \vdash Q \), with \( \alpha \) for \( P \) and \( \chi \) for \( Q \).
:::

## The rules prove their own truth tables

Each line of the truth table of a connective says something like "with \( \alpha \) true and \( \beta \) false, \( \alpha \to \beta \) comes out false". Read with signs, that line is a sequent: from \( \alpha \) and \( \neg\beta \), conclude \( \neg(\alpha \to \beta) \). If every such sequent is derivable, then the rules know the truth tables. This is the key to the first idea of the plan. Section 3.3 began by reading the tables off the rules; the lemma below makes that reading exact: every line of every table is a derivable sequent.

::: {#lem-connective-rows}
[The Rules Prove the Truth Tables]

For all formulas \( \alpha \) and \( \beta \), the following sequents are derivable, by derivations that do not use \( \rulename{RAA} \).

::: {.enumerate options="label=(\roman*)"}
1. \( (\neg 1) \) \( \alpha \vdash \neg\neg\alpha \), and \( (\bot 1) \) \( \vdash \neg\bot \).
2. \( (\wedge 1) \) \( \alpha, \beta \vdash \alpha \wedge \beta \); \( (\wedge 2) \) \( \neg\alpha \vdash \neg(\alpha \wedge \beta) \); \( (\wedge 3) \) \( \neg\beta \vdash \neg(\alpha \wedge \beta) \).
3. \( (\vee 1) \) \( \alpha \vdash \alpha \vee \beta \); \( (\vee 2) \) \( \beta \vdash \alpha \vee \beta \); \( (\vee 3) \) \( \neg\alpha, \neg\beta \vdash \neg(\alpha \vee \beta) \).
4. \( ({\to}1) \) \( \neg\alpha \vdash \alpha \to \beta \); \( ({\to}2) \) \( \beta \vdash \alpha \to \beta \); \( ({\to}3) \) \( \alpha, \neg\beta \vdash \neg(\alpha \to \beta) \).
5. \( ({\leftrightarrow}1) \) \( \alpha, \beta \vdash \alpha \leftrightarrow \beta \); \( ({\leftrightarrow}2) \) \( \neg\alpha, \neg\beta \vdash \alpha \leftrightarrow \beta \); \( ({\leftrightarrow}3) \) \( \alpha, \neg\beta \vdash \neg(\alpha \leftrightarrow \beta) \); \( ({\leftrightarrow}4) \) \( \neg\alpha, \beta \vdash \neg(\alpha \leftrightarrow \beta) \).
:::
:::

Each sequent has as premises **only the parts it needs**, each as itself or negated. For instance, \( \alpha \wedge \beta \) is false as soon as \( \alpha \) is false, whatever \( \beta \) is, and \( (\wedge 2) \) has the single premise \( \neg\alpha \). This economy will matter: when the proof of the next lemma uses a row, it needs to know something only about the parts the row mentions.

::: {.idea}
Most of the sequents are already in the book: rules of Chapter 1, or results of Chapter 2 with \( \alpha \) and \( \beta \) put in for the letters. The others are short derivations of the kinds Chapter 2 practiced: a box that repeats a premise, or a \( \rulename{\neg I} \) box that reaches a clash. The only thing to watch is that no step, and no cited result, uses \( \rulename{RAA} \).
:::

::: {.proof}
The table lists, for each sequent, the rows of the truth table it covers (by @def-truth-value) and where its derivation comes from. The letters of the Chapter 2 results are replaced by \( \alpha \) and \( \beta \), as @def-derived-rule allows.

| Tag | Rows covered | Sequent | Derivation |
|---|---|---|---|
| \( (\neg 1) \) | \( \alpha \) T, so \( \neg\alpha \) F | \( \alpha \vdash \neg\neg\alpha \) | @exm-double-negation-introduction (a) |
| \( (\bot 1) \) | \( \bot \) is always F | \( \vdash \neg\bot \) | printed below |
| \( (\wedge 1) \) | T, T give T | \( \alpha, \beta \vdash \alpha \wedge \beta \) | \( \rulename{\wedge I} \) (@def-rules-conjunction) |
| \( (\wedge 2) \) | F, anything give F | \( \neg\alpha \vdash \neg(\alpha \wedge \beta) \) | \( \rulename{\vee I} \) gives \( \neg\alpha \vee \neg\beta \), then @prp-de-morgan (c) |
| \( (\wedge 3) \) | anything, F give F | \( \neg\beta \vdash \neg(\alpha \wedge \beta) \) | \( \rulename{\vee I} \) gives \( \neg\alpha \vee \neg\beta \), then @prp-de-morgan (c) |
| \( (\vee 1) \) | T, anything give T | \( \alpha \vdash \alpha \vee \beta \) | \( \rulename{\vee I} \) (@def-rule-disjunction-introduction) |
| \( (\vee 2) \) | anything, T give T | \( \beta \vdash \alpha \vee \beta \) | \( \rulename{\vee I} \) |
| \( (\vee 3) \) | F, F give F | \( \neg\alpha, \neg\beta \vdash \neg(\alpha \vee \beta) \) | \( \rulename{\wedge I} \) gives \( \neg\alpha \wedge \neg\beta \), then @prp-de-morgan (b) |
| \( ({\to}1) \) | F, anything give T | \( \neg\alpha \vdash \alpha \to \beta \) | @prp-vacuous-implication |
| \( ({\to}2) \) | anything, T give T | \( \beta \vdash \alpha \to \beta \) | printed below |
| \( ({\to}3) \) | T, F give F | \( \alpha, \neg\beta \vdash \neg(\alpha \to \beta) \) | printed below |
| \( ({\leftrightarrow}1) \) | T, T give T | \( \alpha, \beta \vdash \alpha \leftrightarrow \beta \) | printed below |
| \( ({\leftrightarrow}2) \) | F, F give T | \( \neg\alpha, \neg\beta \vdash \alpha \leftrightarrow \beta \) | printed below |
| \( ({\leftrightarrow}3) \) | T, F give F | \( \alpha, \neg\beta \vdash \neg(\alpha \leftrightarrow \beta) \) | printed below |
| \( ({\leftrightarrow}4) \) | F, T give F | \( \neg\alpha, \beta \vdash \neg(\alpha \leftrightarrow \beta) \) | printed below |

In the second column, "F, anything give F" means: if \( \alpha \) is F, then \( \alpha \wedge \beta \) is F whatever the value of \( \beta \).

The seven printed derivations follow. First \( ({\to}2) \) and \( ({\to}3) \) (the first is the derivation of @exr-proving-an-implication-b2 (a), printed again because a proof does not rest on an exercise): an implication whose conclusion we already have, and the refutation of an implication by a true hypothesis with a false conclusion.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\beta}
  \open
  \hypo {2} {\alpha}
  \have {3} {\beta} \r{1}
  \close
  \have {4} {\alpha \to \beta} \ii{2-3}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\alpha}
  \hypo {2} {\neg \beta}
  \open
  \hypo {3} {\alpha \to \beta}
  \have {4} {\beta} \ie{3,1}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg (\alpha \to \beta)} \ni{3-5}
\end{nd}$
\end{center}
```

Next \( ({\leftrightarrow}1) \) and \( ({\leftrightarrow}2) \). In the first, each box repeats the premise it needs; in the second, each box reaches a clash and closes by \( \rulename{\bot E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\alpha}
  \hypo {2} {\beta}
  \open
  \hypo {3} {\alpha}
  \have {4} {\beta} \r{2}
  \close
  \open
  \hypo {5} {\beta}
  \have {6} {\alpha} \r{1}
  \close
  \have {7} {\alpha \leftrightarrow \beta} \bi{3-4,5-6}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\neg \alpha}
  \hypo {2} {\neg \beta}
  \open
  \hypo {3} {\alpha}
  \have {4} {\bot} \ne{3,1}
  \have {5} {\beta} \be{4}
  \close
  \open
  \hypo {6} {\beta}
  \have {7} {\bot} \ne{6,2}
  \have {8} {\alpha} \be{7}
  \close
  \have {9} {\alpha \leftrightarrow \beta} \bi{3-5,6-8}
\end{nd}$
\end{center}
```

Then \( ({\leftrightarrow}3) \), \( ({\leftrightarrow}4) \) and \( (\bot 1) \). The first two assume the biconditional and use it in the direction that clashes with a premise; the last is a box whose assumption \( \bot \) is already the \( \bot \) that \( \rulename{\neg I} \) asks for, the degenerate box of Section 2.2.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\alpha}
  \hypo {2} {\neg \beta}
  \open
  \hypo {3} {\alpha \leftrightarrow \beta}
  \have {4} {\beta} \bie{3,1}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg (\alpha \leftrightarrow \beta)} \ni{3-5}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\neg \alpha}
  \hypo {2} {\beta}
  \open
  \hypo {3} {\alpha \leftrightarrow \beta}
  \have {4} {\alpha} \bie{3,2}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg (\alpha \leftrightarrow \beta)} \ni{3-5}
\end{nd}$
\end{center}
```

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\bot}
  \close
  \have {2} {\neg \bot} \ni{1-1}
\end{nd}$
\end{center}
```

None of these derivations uses \( \rulename{RAA} \): their boxes close by \( \rulename{{\to}I} \), \( \rulename{\neg I} \) and \( \rulename{{\leftrightarrow}I} \). Nor do the cited results: @prp-vacuous-implication and @exm-double-negation-introduction come from Sections 2.1 and 2.2, before \( \rulename{RAA} \) was introduced, and Chapter 2 derived De Morgan's laws (b) and (c) without it (it says so right after the derivations of @prp-de-morgan). This proves the lemma.
:::

The \( \neg \) connective needs only one sequent. When \( \alpha \) is false, \( \neg\alpha \) is true, and the "sequent" \( \neg\alpha \vdash \neg\alpha \) is a one-line derivation; only the other row, \( (\neg 1) \), needs a proof.

::: {.warning}
The sequents of @lem-connective-rows go **from the parts to the whole**. Read backwards they are false. For instance \( \alpha \vee \beta \vdash \alpha \) is not derivable in general: the row \( p = \mathrm{F} \), \( q = \mathrm{T} \) makes \( p \vee q \) true and \( p \) false, so \( p \vee q \nvdash p \) by @cor-refuting-row. A row of a table tells us the value of the whole from the values of the parts, never the other way round.
:::

## One row, one derivation

We now name the formulas that "write down a row".

*A signed formula is a formula as it stands in one row: itself if the row makes it true, its negation if the row makes it false.*

For a valuation \( v \) and a formula \( \varphi \), the **signed formula** \( \varphi^{v} \) is
\[
\varphi^{v} \coloneqq
\begin{cases}
\varphi & \text{if } v(\varphi) = \mathrm{T}, \\
\neg\varphi & \text{if } v(\varphi) = \mathrm{F}.
\end{cases}
\]
In particular, for an atom \( p \), the **signed atom** \( p^{v} \) is \( p \) or \( \neg p \). For example, if \( v(p) = \mathrm{T} \) and \( v(q) = \mathrm{F} \), then \( p^{v} = p \), \( q^{v} = \neg q \), \( (p \to q)^{v} = \neg(p \to q) \) and \( (q \to p)^{v} = q \to p \). Whatever \( v \) is, \( v(\varphi^{v}) = \mathrm{T} \): the signed formula is always the true one of \( \varphi \) and \( \neg\varphi \), by the clause for \( \neg \) in @def-truth-value.

The signed atoms \( p_1^{v}, \dots, p_n^{v} \) describe the row of \( v \) completely, as far as \( p_1, \dots, p_n \) go. The next lemma says they are enough premises to derive the signed version of any formula built from these atoms.

::: {#lem-truth-table-line}
[One Row of the Truth Table Is Derivable]

Let \( \varphi \) be a formula, let \( p_1, \dots, p_n \) (\( n \ge 0 \)) be atoms among which are **all** the atoms of \( \varphi \), and let \( v \) be a valuation. Then
\[
p_1^{v}, \dots, p_n^{v} \vdash \varphi^{v} .
\]
:::

In words: in each row of the truth table of \( \varphi \), the value of \( \varphi \) can be derived from the values of its atoms, where "value T" is written as the formula and "value F" as its negation.

::: {.idea}
Climb the parse tree. At an atom, \( \varphi^{v} \) is one of the premises. At a connective, the induction hypothesis gives the signed parts \( \alpha^{v} \), \( \beta^{v} \), and @lem-connective-rows has a sequent from exactly those signed parts to the signed whole. So structural induction (@thm-structural-induction), with @lem-weakening-cut (c) to chain, does the whole job. The only care is to pick, for each pair of values, the row whose premises are the signs we actually have.
:::

::: {.proof}
Fix the atoms \( p_1, \dots, p_n \) and the valuation \( v \), and write \( \Sigma \) for the list \( p_1^{v}, \dots, p_n^{v} \). We prove, by structural induction (@thm-structural-induction), that every formula \( \varphi \) has the property

> if every atom of \( \varphi \) is among \( p_1, \dots, p_n \), then \( \Sigma \vdash \varphi^{v} \).

Every atom of an immediate part \( \alpha \) or \( \beta \) of a formula is an atom of the formula itself, so when \( \varphi \) satisfies the "if", so do its immediate parts, and the induction hypothesis applies to them.

*Atoms.* Let \( \varphi \) be an atom among \( p_1, \dots, p_n \), say \( \varphi = p_i \). Then \( \varphi^{v} = p_i^{v} \) is a member of \( \Sigma \), and the one-line derivation whose only line is the premise \( p_i^{v} \) shows \( \Sigma \vdash \varphi^{v} \).

*The formula \( \bot \).* By @def-truth-value, \( v(\bot) = \mathrm{F} \), so \( \bot^{v} = \neg\bot \). By \( (\bot 1) \) of @lem-connective-rows, \( \vdash \neg\bot \), and weakening (@lem-weakening-cut (a)) gives \( \Sigma \vdash \neg\bot \).

*Negation.* Let \( \varphi = \neg\alpha \), and assume \( \Sigma \vdash \alpha^{v} \).

- *Case \( v(\alpha) = \mathrm{T} \).* Then \( \alpha^{v} = \alpha \), and \( v(\neg\alpha) = \mathrm{F} \), so \( \varphi^{v} = \neg\neg\alpha \). From \( \Sigma \vdash \alpha \) and \( (\neg 1) \), \( \alpha \vdash \neg\neg\alpha \), chaining (@lem-weakening-cut (c)) gives \( \Sigma \vdash \neg\neg\alpha \).
- *Case \( v(\alpha) = \mathrm{F} \).* Then \( \alpha^{v} = \neg\alpha \), and \( v(\neg\alpha) = \mathrm{T} \), so \( \varphi^{v} = \neg\alpha = \alpha^{v} \). The hypothesis is already the claim.

*Conjunction.* Let \( \varphi = \alpha \wedge \beta \), and assume \( \Sigma \vdash \alpha^{v} \) and \( \Sigma \vdash \beta^{v} \). By @def-truth-value, \( v(\alpha \wedge \beta) = \mathrm{T} \) exactly when \( v(\alpha) = v(\beta) = \mathrm{T} \).

- *Case \( v(\alpha) = v(\beta) = \mathrm{T} \).* Then \( \varphi^{v} = \alpha \wedge \beta \), \( \alpha^{v} = \alpha \), \( \beta^{v} = \beta \). Chaining \( \Sigma \vdash \alpha \) and \( \Sigma \vdash \beta \) with \( (\wedge 1) \), \( \alpha, \beta \vdash \alpha \wedge \beta \), gives \( \Sigma \vdash \alpha \wedge \beta \).
- *Case \( v(\alpha) = \mathrm{F} \).* Then \( \varphi^{v} = \neg(\alpha \wedge \beta) \) and \( \alpha^{v} = \neg\alpha \). Chaining \( \Sigma \vdash \neg\alpha \) with \( (\wedge 2) \), \( \neg\alpha \vdash \neg(\alpha \wedge \beta) \), gives \( \Sigma \vdash \neg(\alpha \wedge \beta) \). The hypothesis for \( \beta \) is not used.
- *Case \( v(\alpha) = \mathrm{T} \), \( v(\beta) = \mathrm{F} \).* Then \( \varphi^{v} = \neg(\alpha \wedge \beta) \) and \( \beta^{v} = \neg\beta \), and chaining \( \Sigma \vdash \neg\beta \) with \( (\wedge 3) \) gives \( \Sigma \vdash \neg(\alpha \wedge \beta) \).

*Implication.* Let \( \varphi = \alpha \to \beta \), and assume \( \Sigma \vdash \alpha^{v} \) and \( \Sigma \vdash \beta^{v} \). By @def-truth-value, \( v(\alpha \to \beta) = \mathrm{F} \) exactly when \( v(\alpha) = \mathrm{T} \) and \( v(\beta) = \mathrm{F} \).

- *Case \( v(\alpha) = \mathrm{F} \).* Then \( \varphi^{v} = \alpha \to \beta \) and \( \alpha^{v} = \neg\alpha \). Chaining \( \Sigma \vdash \neg\alpha \) with \( ({\to}1) \), \( \neg\alpha \vdash \alpha \to \beta \), gives \( \Sigma \vdash \alpha \to \beta \).
- *Case \( v(\alpha) = \mathrm{T} \), \( v(\beta) = \mathrm{T} \).* Then \( \varphi^{v} = \alpha \to \beta \) and \( \beta^{v} = \beta \). Chaining \( \Sigma \vdash \beta \) with \( ({\to}2) \), \( \beta \vdash \alpha \to \beta \), gives \( \Sigma \vdash \alpha \to \beta \).
- *Case \( v(\alpha) = \mathrm{T} \), \( v(\beta) = \mathrm{F} \).* Then \( \varphi^{v} = \neg(\alpha \to \beta) \), \( \alpha^{v} = \alpha \) and \( \beta^{v} = \neg\beta \). Chaining \( \Sigma \vdash \alpha \) and \( \Sigma \vdash \neg\beta \) with \( ({\to}3) \), \( \alpha, \neg\beta \vdash \neg(\alpha \to \beta) \), gives \( \Sigma \vdash \neg(\alpha \to \beta) \).

*Disjunction and biconditional.* These go as for implication. For each pair of values of \( \alpha \) and \( \beta \), the table in the proof of @lem-connective-rows names a sequent whose premises are among \( \alpha^{v} \), \( \beta^{v} \) and whose conclusion is \( \varphi^{v} \): for \( \vee \), \( (\vee 1) \) if \( v(\alpha) = \mathrm{T} \), \( (\vee 2) \) if \( v(\alpha) = \mathrm{F} \) and \( v(\beta) = \mathrm{T} \), \( (\vee 3) \) if both are F; for \( \leftrightarrow \), \( ({\leftrightarrow}1) \) to \( ({\leftrightarrow}4) \) for the value pairs T T, F F, T F, F T. Chaining the induction hypotheses for those premises with that sequent gives \( \Sigma \vdash \varphi^{v} \).

The atoms and \( \bot \) have the property, and each formation clause preserves it, so by @thm-structural-induction every formula has it. This proves the lemma.
:::

Each case used the induction hypothesis only for the parts named in the premises of its sequent: the conjunction case with \( \alpha \) false never looked at \( \beta \). That is the economy of @lem-connective-rows at work. The disjunction and biconditional cases are written out in @exr-completeness-c1.

Here is the lemma run on one formula, with every chained sequent written as a line.

::: {#exm-truth-table-line-run}
[Deriving one row]

Let \( \varphi = p \to (q \wedge \neg p) \) and let \( v(p) = v(q) = \mathrm{T} \). Find \( \varphi^{v} \), and write the derivation of \( p^{v}, q^{v} \vdash \varphi^{v} \) that the proof of @lem-truth-table-line produces.
:::

::: {.solution}
Compute up the parse tree: \( v(\neg p) = \mathrm{F} \), so \( v(q \wedge \neg p) = \mathrm{F} \), and since \( v(p) = \mathrm{T} \), \( v(\varphi) = \mathrm{F} \). So \( \varphi^{v} = \neg(p \to (q \wedge \neg p)) \), and the premises are \( p^{v} = p \) and \( q^{v} = q \).

The proof climbs the same tree. At \( \neg p \) with \( v(p) = \mathrm{T} \), it is the negation case with \( \alpha \) true: \( (\neg 1) \) gives \( \neg\neg p \). At \( q \wedge \neg p \), the values are T and F: \( (\wedge 3) \) gives \( \neg(q \wedge \neg p) \) from \( (\neg p)^{v} = \neg\neg p \). At the root, the values are T and F: \( ({\to}3) \) gives the goal from \( p \) and \( \neg(q \wedge \neg p) \). Written as a derivation, with each sequent of @lem-connective-rows cited as a derived rule:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p}
  \hypo {2} {q}
  \have {3} {\neg\neg p} \by{$(\neg 1)$}{1}
  \have {4} {\neg (q \wedge \neg p)} \by{$(\wedge 3)$}{3}
  \have {5} {\neg (p \to (q \wedge \neg p))} \by{$({\to}3)$}{1,4}
\end{nd}$
\end{center}
```

The premise \( q \) is never cited. It was used only in computing which case applies: the \( \wedge \) case with \( \beta = \neg p \) false needs only \( \beta \)'s sign, not \( q \)'s. A derivation need not use every premise (@def-derivable).
:::

::: {.check}
Let \( \varphi = p \to \neg q \) and \( v(p) = v(q) = \mathrm{T} \). What sequent does @lem-truth-table-line provide, and which sequent of @lem-connective-rows does the proof use at the root?
:::

::: {.solution}
Here \( v(\neg q) = \mathrm{F} \), so \( v(\varphi) = \mathrm{F} \), and the lemma gives \( p, q \vdash \neg(p \to \neg q) \). At the root the values are T and F, so the proof uses \( ({\to}3) \), \( \alpha, \neg\beta \vdash \neg(\alpha \to \beta) \), with \( \alpha = p \) and \( \beta = \neg q \). Its premise \( \neg\beta = \neg\neg q \) comes from the negation case below it: \( q \vdash \neg\neg q \), by \( (\neg 1) \).
:::

## Gluing the rows: splitting on an atom

@lem-truth-table-line derives a formula from the signed atoms of **one** row. A sequent \( \Gamma \vdash \psi \) mentions no row at all. The signed atoms must be removed, and the tool for that is excluded middle.

::: {#lem-atom-splitting}
[Splitting on an Atom]

Let \( \Delta \) be a list of formulas, \( p \) an atom and \( \psi \) a formula. If \( \Delta, p \vdash \psi \) and \( \Delta, \neg p \vdash \psi \), then \( \Delta \vdash \psi \).
:::

::: {.idea}
This is proof by cases on \( p \vee \neg p \). @prp-excluded-middle gives \( p \vee \neg p \) with no premises, and \( \rulename{\vee E} \) (@def-rules-disjunction) needs a box that reaches \( \psi \) from \( p \) and a box that reaches \( \psi \) from \( \neg p \). The two given derivations are exactly the contents of those boxes, once their premise \( p \) (or \( \neg p \)) is replaced by the box's assumption.

*Before reading on: this is the only place in the completeness proof where a classical rule enters. Where exactly, and why could the \( \rulename{\neg I} \) of Chapter 2 not do the job?*
:::

::: {.proof}
Let \( D \) be a derivation of \( \psi \) with premises in \( \Delta, p \), and \( E \) one with premises in \( \Delta, \neg p \). Build a list of lines as follows.

1. As premises, every premise of \( D \) or of \( E \) that is a member of \( \Delta \).
2. The line \( p \vee \neg p \), justified by @prp-excluded-middle (\( \rulename{LEM} \)) with \( p \) for \( P \); it cites nothing.
3. A box that opens with the assumption \( p \), followed by the lines of \( D \) that are not premises, with their boxes. A citation of a premise of \( D \) that is in \( \Delta \) now cites the premise line of step 1; a citation of the premise \( p \) now cites the assumption. If the last line of \( D \) is itself a premise, the box is shorter: if that premise is \( p \), the box is the assumption alone, which is then its last line; otherwise the box is the assumption followed by \( \psi \), by \( \rulename{R} \), citing the premise line carrying \( \psi \).
4. A second box, built from \( E \) in the same way, opening with the assumption \( \neg p \).
5. The line \( \psi \), by \( \rulename{\vee E} \), citing line 2 of this list and the two boxes.

This is a derivation (@def-derivation). The premises lie in no box and come first, so they are available everywhere. Inside the first box, the lines of \( D \) keep their boxes, which now sit inside the new box, and they cite the same lines and boxes as before, or a premise line, or the assumption, which is available at every line of its own box. As in the proof of @lem-weakening-cut, each line is still an instance of its rule. The last line of the first box is \( \psi \), and it is a line of that box itself and not of a box inside it: it was the last line of \( D \), which lies in no box of \( D \) (or it is the assumption itself, or the repetition line). The same holds for the second box. Both boxes and the line \( p \vee \neg p \) lie in no box, and neither does the last line, so they are available at it. Hence the last line is an instance of \( \rulename{\vee E} \), and the list is a derivation of \( \psi \) whose premises are all in \( \Delta \). So \( \Delta \vdash \psi \).
:::

Here is its shape, with \( \Delta \) standing for the premise lines:

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \hypo {h} {\Delta}
  \have {i} {p \vee \neg p} \lem{}
  \open
  \hypo {a} {p}
  \have {} {\vdots}
  \have {b} {\psi}
  \close
  \open
  \hypo {c} {\neg p}
  \have {} {\vdots}
  \have {d} {\psi}
  \close
  \have {k} {\psi} \oe{i,a-b,c-d}
\end{nd}$
\end{center}
```

The answer to the prompt: the classical rule enters at line \( i \). @prp-excluded-middle was derived in Chapter 2 with \( \rulename{RAA} \), and nothing else in the proof of this lemma is classical. \( \rulename{\neg I} \) could not replace it: \( \rulename{\neg I} \) produces a negation, and here we need a disjunction with no premises to split on. Nothing in the proof uses that \( p \) is an atom; the lemma holds for any formula in place of \( p \), but atoms are all we shall split on.

## The completeness theorem

Now the plan of the opening can be carried out.

::: {#thm-completeness}
[Completeness]

Let \( \Gamma \) be a list of formulas and \( \psi \) a formula. If \( \Gamma \models \psi \), then \( \Gamma \vdash \psi \).
:::

A list is finite, as in @def-derivable. That matters: the proof works with the atoms that occur in \( \Gamma \) and \( \psi \), and it needs them to be finitely many.

::: {.idea}
**Step roadmap.** ① List the atoms \( p_1, \dots, p_n \) of \( \Gamma \) and \( \psi \). ② **Claim:** for **every** valuation \( v \), \( \Gamma, p_1^{v}, \dots, p_n^{v} \vdash \psi \). If \( v \) makes all of \( \Gamma \) true, then \( \psi \) is true in that row, and @lem-truth-table-line derives it. If \( v \) makes some premise \( \gamma \) false, the lemma derives \( \neg\gamma \), which clashes with the premise \( \gamma \). ③ Remove the signed atoms, last first, by @lem-atom-splitting. To remove \( p_j \) we need derivations from both \( p_j \) and \( \neg p_j \) with the same other signed atoms: two rows that differ only at \( p_j \). That is why the Claim must hold for every valuation, not just one.
:::

::: {.proof}
**Step 1.** The list \( \Gamma \) is finite and each formula has finitely many symbols, so only finitely many atoms occur in \( \Gamma \) or \( \psi \). List them without repetition as \( p_1, \dots, p_n \), where \( n \ge 0 \).

**Step 2.**

::: {.claim}
For every valuation \( v \), \( \ \Gamma, p_1^{v}, \dots, p_n^{v} \vdash \psi \).
:::

::: {.proofofclaim}
Let \( v \) be a valuation, and write \( \Sigma \) for \( p_1^{v}, \dots, p_n^{v} \).

*Case 1: \( v(\gamma) = \mathrm{T} \) for every member \( \gamma \) of \( \Gamma \).* Since \( \Gamma \models \psi \), by @def-valid-argument \( v(\psi) = \mathrm{T} \), so \( \psi^{v} = \psi \). Every atom of \( \psi \) is among \( p_1, \dots, p_n \), so @lem-truth-table-line gives \( \Sigma \vdash \psi \), and weakening (@lem-weakening-cut (a)) gives \( \Gamma, \Sigma \vdash \psi \).

*Case 2: \( v(\gamma) = \mathrm{F} \) for some member \( \gamma \) of \( \Gamma \).* Then \( \gamma^{v} = \neg\gamma \). Every atom of \( \gamma \) is among \( p_1, \dots, p_n \), so @lem-truth-table-line gives \( \Sigma \vdash \neg\gamma \), and by weakening \( \Gamma, \Sigma \vdash \neg\gamma \). Also \( \Gamma, \Sigma \vdash \gamma \), by the one-line derivation whose only line is the premise \( \gamma \). By @prp-ex-falso, \( \gamma, \neg\gamma \vdash \psi \). Chaining (@lem-weakening-cut (c)) gives \( \Gamma, \Sigma \vdash \psi \).
:::

**Step 3.** For each integer \( j \) with \( 0 \le j \le n \), let \( S(j) \) be the statement
\[
\text{for every valuation } v, \quad \Gamma, p_1^{v}, \dots, p_j^{v} \vdash \psi ,
\]
where for \( j = 0 \) the list of signed atoms is empty. The Claim is \( S(n) \).

::: {.claim}
If \( 1 \le j \le n \) and \( S(j) \) holds, then \( S(j - 1) \) holds.
:::

::: {.proofofclaim}
Let \( v \) be a valuation. Let \( v^{+} \) be the valuation that agrees with \( v \) at every atom except that \( v^{+}(p_j) = \mathrm{T} \), and \( v^{-} \) the one that agrees with \( v \) except that \( v^{-}(p_j) = \mathrm{F} \); by @def-valuation, a valuation may assign any value to each atom, so both exist. The atoms \( p_1, \dots, p_{j-1} \) are different from \( p_j \), so \( v^{+} \) and \( v^{-} \) agree with \( v \) on them, and \( p_i^{v^{+}} = p_i^{v^{-}} = p_i^{v} \) for \( i < j \). Also \( p_j^{v^{+}} = p_j \) and \( p_j^{v^{-}} = \neg p_j \). Applying \( S(j) \) to \( v^{+} \) and to \( v^{-} \) gives, with \( \Delta \) standing for the list \( \Gamma, p_1^{v}, \dots, p_{j-1}^{v} \),
\[
\Delta, p_j \vdash \psi
\quad\text{and}\quad
\Delta, \neg p_j \vdash \psi .
\]
By @lem-atom-splitting, \( \Delta \vdash \psi \). Since \( v \) was arbitrary, this is \( S(j - 1) \).
:::

It remains to go down from \( S(n) \) to \( S(0) \), which takes \( n \) applications of the Claim. We count the applications made: for \( m \in \nN \), let \( T(m) \) say "if \( m \le n \), then \( S(n - m) \) holds". \( T(0) \) says that \( S(n) \) holds, which is Step 2. Suppose \( T(m) \) holds, and let \( m + 1 \le n \). Then \( m \le n \), so \( S(n - m) \) holds by \( T(m) \); and \( j \coloneqq n - m \) satisfies \( 1 \le j \le n \), because \( 0 \le m \le n - 1 \). The Claim gives \( S(j - 1) = S(n - (m + 1)) \), which is \( T(m + 1) \). By @ax-induction, \( T(m) \) holds for every \( m \in \nN \), and \( T(n) \) is \( S(0) \).

**Step 4.** \( S(0) \) says that \( \Gamma \vdash \psi \), for every valuation \( v \); there is at least one valuation (for instance the one making every atom true), so \( \Gamma \vdash \psi \). This proves the theorem.
:::

If \( n = 0 \), the formulas of \( \Gamma \) and \( \psi \) are built from \( \bot \) alone, and Step 3 does nothing: \( S(0) \) is the Claim itself.

A common alternative route first turns \( \Gamma \models \psi \) into a single tautology, \( \models \gamma_1 \to (\gamma_2 \to \cdots \to (\gamma_k \to \psi)) \), proves completeness for tautologies, and then unpacks the implications with \( \rulename{{\to}E} \). Keeping \( \Gamma \) as premises, as Step 2 does, costs one extra case (a false premise) and saves that detour.

Let us run the proof on the tautology of the opening.

::: {#exm-completeness-run}
[The method on a tautology]

Run the proof of @thm-completeness on \( \models (p \to q) \vee (q \to p) \), and write the derivation it produces, citing the sequents of @lem-connective-rows as derived rules.
:::

::: {.solution}
Write \( \chi \) for \( (p \to q) \vee (q \to p) \). The list \( \Gamma \) is empty and the atoms are \( p_1 = p \), \( p_2 = q \). Every valuation makes \( \chi \) true (if \( v(q) = \mathrm{T} \) the left side is true; otherwise the right side is), so Step 2 is always Case 1, and @lem-truth-table-line produces four short derivations, one per row:

- \( p, q \vdash \chi \): \( p \to q \) by \( ({\to}2) \) from \( q \), then \( \rulename{\vee I} \);
- \( p, \neg q \vdash \chi \): \( q \to p \) by \( ({\to}1) \) from \( \neg q \), then \( \rulename{\vee I} \);
- \( \neg p, q \vdash \chi \) and \( \neg p, \neg q \vdash \chi \): \( p \to q \) by \( ({\to}1) \) from \( \neg p \), then \( \rulename{\vee I} \).

(In the row \( p = \mathrm{F} \), \( q = \mathrm{T} \), both \( ({\to}1) \) and \( ({\to}2) \) would do; the proof of @lem-truth-table-line uses \( ({\to}1) \) whenever \( \alpha \) is false.) Step 3 first splits on \( q = p_2 \), twice: once with \( p \) and once with \( \neg p \) among the premises. Then it splits on \( p = p_1 \), once. Three uses of @lem-atom-splitting in two rounds. Pasting as in its proof, the last split is the outermost:

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {p \vee \neg p} \lem{}
  \open
  \hypo {2} {p}
  \have {3} {q \vee \neg q} \lem{}
  \open
  \hypo {4} {q}
  \have {5} {p \to q} \by{$({\to}2)$}{4}
  \have {6} {(p \to q) \vee (q \to p)} \oi{5}
  \close
  \open
  \hypo {7} {\neg q}
  \have {8} {q \to p} \by{$({\to}1)$}{7}
  \have {9} {(p \to q) \vee (q \to p)} \oi{8}
  \close
  \have {10} {(p \to q) \vee (q \to p)} \oe{3,4-6,7-9}
  \close
  \open
  \hypo {11} {\neg p}
  \have {12} {q \vee \neg q} \lem{}
  \open
  \hypo {13} {q}
  \have {14} {p \to q} \by{$({\to}1)$}{11}
  \have {15} {(p \to q) \vee (q \to p)} \oi{14}
  \close
  \open
  \hypo {16} {\neg q}
  \have {17} {p \to q} \by{$({\to}1)$}{11}
  \have {18} {(p \to q) \vee (q \to p)} \oi{17}
  \close
  \have {19} {(p \to q) \vee (q \to p)} \oe{12,13-15,16-18}
  \close
  \have {20} {(p \to q) \vee (q \to p)} \oe{1,2-10,11-19}
\end{nd}$
\end{center}
```

The derivation has 20 lines. The one found by search in @exr-finding-derivations-c2 has 13, and splits only once. Here the split on \( q \) inside the box of \( \neg p \) (lines 12–19) is wasted: both of its boxes do the same thing, because in the rows with \( p \) false the value of \( q \) does not matter. The proof is a **method** that always works, not a recipe for short derivations; to find a short one, search as in Section 2.6.
:::

::: {.warning}
Completeness promises a derivation, not a short one. For a sequent with \( n \) atoms, the proof builds \( 2^n \) row derivations and glues them with \( 2^n - 1 \) splittings: with \( n = 10 \) atoms, that is 1024 row derivations and 1023 uses of \( \rulename{LEM} \). The theorem answers "is there a derivation?", not "how short is the shortest?".
:::

With soundness, completeness closes the circle.

::: {#cor-derivable-iff-valid}
[Derivable Means Valid]

For every list of formulas \( \Gamma \) and every formula \( \psi \),
\[
\Gamma \vdash \psi \iff \Gamma \models \psi .
\]
In particular, whether \( \Gamma \vdash \psi \) holds can be decided by checking the \( 2^n \) rows of a truth table, where \( n \) is the number of atoms occurring in \( \Gamma \) and \( \psi \).
:::

::: {.proof}
\( (\Rightarrow) \) is @thm-soundness and \( (\Leftarrow) \) is @thm-completeness. For the second sentence, let \( p_1, \dots, p_n \) be the atoms occurring in \( \Gamma \) and \( \psi \). By @lem-coincidence, the values of the members of \( \Gamma \) and of \( \psi \) under a valuation depend only on its values at \( p_1, \dots, p_n \), so \( \Gamma \models \psi \) holds exactly when it holds in each of the \( 2^n \) rows of the joint truth table. That is a finite check, and by the first sentence it decides \( \Gamma \vdash \psi \).
:::

So a question that looks as if it needs a search through infinitely many possible derivations can be settled by a finite table. The search for a derivation may still be the quicker way to a **yes**, and one row is the quickest way to a **no** (@cor-refuting-row), but neither is needed.

::: {.remark}
We defined \( \Gamma \vdash \psi \) only for a list, that is, for finitely many premises. One may allow an infinite collection \( \Gamma \) of premises and say \( \Gamma \vdash \psi \) when \( \psi \) is derivable from finitely many members of \( \Gamma \) (a derivation has finitely many lines, so it can only use finitely many). The equivalence with \( \Gamma \models \psi \) still holds for infinite \( \Gamma \); this is the compactness theorem of propositional logic. We do not prove it, and nothing in the book depends on it. Our proof does not reach it: Step 1 needs finitely many atoms.
:::

## Two roads to every answer

We now have two independent ways to settle any question "is \( \Gamma \vdash \psi \)?". One is to **search** for a derivation, as in Section 2.6. The other is to **check a table**, and @cor-derivable-iff-valid says the two always agree. Here are two of Chapter 2's classical laws settled by the table first.

**De Morgan's law (d).** Is \( \neg(p \wedge q) \models \neg p \vee \neg q \)? The four rows:
\[
\begin{array}{cc|c|c}
p & q & \neg(p \wedge q) & \neg p \vee \neg q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T}
\end{array}
\]
In every row where the premise is T, so is the conclusion. So \( \neg(p \wedge q) \models \neg p \vee \neg q \), and by @thm-completeness, \( \neg(p \wedge q) \vdash \neg p \vee \neg q \).

**Peirce's law.** Is \( (p \to q) \to p \models p \)? Work backwards from F (Section 3.3). A refuting row would need \( p \) false. Then \( p \to q \) is true, so \( (p \to q) \to p \) is "true implies false", which is false. So no row makes the premise true and the conclusion false: \( (p \to q) \to p \models p \), and by @thm-completeness, \( (p \to q) \to p \vdash p \).

Both answers came before anyone found a derivation. Chapter 2 found both by hand (@prp-de-morgan (d), and @prp-peirce, whose \( \vdash ((P \to Q) \to P) \to P \) gives the sequent by \( \rulename{{\to}E} \)), and the derivations there use \( \rulename{RAA} \). Completeness explains why a search had to succeed; it does not say how.

Section 3.4 remarked that the tables do not see which of Chapter 2's laws needed \( \rulename{RAA} \). Now we can say why they cannot. A table decides \( \Gamma \models \psi \), and by @cor-derivable-iff-valid that is the same as derivability with **all** the rules, \( \rulename{RAA} \) included. A table has no column recording which rules a derivation uses. Whether a sequent can be derived without \( \rulename{RAA} \) is a question about a shorter list of rules, and for that list the completeness theorem is false, as the next paragraph explains. So no truth-table check can tell the laws that need \( \rulename{RAA} \) from those that do not.

Which rules did the proof of completeness itself use? @lem-weakening-cut only pastes derivations. @lem-connective-rows uses no \( \rulename{RAA} \), as its proof checks. @lem-truth-table-line and the Claim chain those sequents, together with @prp-ex-falso, which Chapter 2 derived before \( \rulename{RAA} \) appeared. The one classical step is the line \( p \vee \neg p \) of @lem-atom-splitting. So the theorem is really about the full list of rules, \( \rulename{RAA} \) included. Without \( \rulename{RAA} \) the list is sound but not complete, as the optional @thm-raa-independent shows for \( \vdash p \vee \neg p \) and \( \neg\neg p \vdash p \); the proof above breaks exactly at the splitting.

::: {.warning}
Completeness does not say that a tautology has a derivation **without** \( \rulename{RAA} \). It says there is a derivation from the rules of Chapters 1 and 2, all of them. The formula \( (p \to q) \vee (q \to p) \) is a tautology, and every derivation found for it so far uses \( \rulename{LEM} \) or \( \rulename{RAA} \). Whether a particular tautology can do without them is a different question, and a table cannot answer it.
:::

## Exercises

### A. Check your understanding

::: {#exr-completeness-a1}
[A1]

These questions are about @lem-truth-table-line and @thm-completeness.

::: {.enumerate options="label=(\alph*)"}
1. In the conjunction case of the proof of @lem-truth-table-line, suppose \( v(\alpha) = \mathrm{F} \) and \( v(\beta) = \mathrm{T} \). Which sequent of @lem-connective-rows is used, and which induction hypotheses?
2. Where is \( \rulename{RAA} \) used in the proof of @thm-completeness, including inside the results it cites?
3. State the idea of the proof of @thm-completeness in two sentences.
4. Run Step 2 of the proof for \( \Gamma = p \), \( \psi = p \vee q \) and the valuation with \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{T} \): which case applies, and which sequent does it prove?
5. Step 1 lists the atoms **without repetition**. Where in the proof is that used?
6. Which step of the proof fails if \( \Gamma \) is allowed to be an infinite collection of formulas, each with its own atoms?
:::
:::

::: {.solution}
*(a)* \( (\wedge 2) \), \( \neg\alpha \vdash \neg(\alpha \wedge \beta) \), and only the hypothesis for \( \alpha \), \( \Sigma \vdash \neg\alpha \). The hypothesis for \( \beta \) is not needed, because \( \alpha \wedge \beta \) is false once \( \alpha \) is.

*(b)* Only inside @lem-atom-splitting, at the line \( p \vee \neg p \): @prp-excluded-middle was derived with \( \rulename{RAA} \). The sequents of @lem-connective-rows are derived without it, @lem-weakening-cut only pastes derivations, and @prp-ex-falso comes before \( \rulename{RAA} \) in Chapter 2.

*(c)* Each row of the truth table gives a derivation of the conclusion from the premises and that row's signed atoms: by @lem-truth-table-line if the row makes every premise true, and from a clash with a false premise otherwise. Two rows that differ at one atom are merged by excluded middle and proof by cases, and after all the atoms are merged the signed atoms are gone.

*(d)* The valuation makes the premise \( p \) false, so Case 2 applies with \( \gamma = p \). @lem-truth-table-line gives \( \neg p, q \vdash \neg p \) (the atom case), the premise gives \( p \), and @prp-ex-falso gives \( p \vee q \). The sequent proved is \( p, \neg p, q \vdash p \vee q \).

*(e)* In the Claim of Step 3: \( v^{+} \) and \( v^{-} \) change only the value at \( p_j \), and they agree with \( v \) on \( p_1, \dots, p_{j-1} \) only because those atoms differ from \( p_j \). If \( p_j \) also appeared as some \( p_i \) with \( i < j \), then \( p_i^{v^{+}} = p_j \) and \( p_i^{v^{-}} = \neg p_j \) would differ, and the two sequents would not share the list \( \Delta \) that @lem-atom-splitting needs.

*(f)* Step 1. Infinitely many atoms may occur, so there is no finite list \( p_1, \dots, p_n \): the Claim would need infinitely many signed atoms as premises, which is not a list, and Step 3's descent from \( S(n) \) has no \( n \) to start from.
:::

### B. Practice

::: {#exr-completeness-b1}
[B1: Three rows from the primitive rules]

The table in the proof of @lem-connective-rows obtains \( (\wedge 2) \), \( (\wedge 3) \) and \( (\vee 3) \) from De Morgan's laws. Derive
\[
\neg\alpha \vdash \neg(\alpha \wedge \beta), \qquad
\neg\beta \vdash \neg(\alpha \wedge \beta), \qquad
\neg\alpha, \neg\beta \vdash \neg(\alpha \vee \beta)
\]
directly from the primitive rules, and say which of your derivations use \( \rulename{RAA} \).
:::

::: {.solution}
Each goal is a negation, so each derivation opens a \( \rulename{\neg I} \) box on the unnegated formula and hunts for a clash.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \alpha}
  \open
  \hypo {2} {\alpha \wedge \beta}
  \have {3} {\alpha} \ae{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg (\alpha \wedge \beta)} \ni{2-4}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\neg \beta}
  \open
  \hypo {2} {\alpha \wedge \beta}
  \have {3} {\beta} \ae{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg (\alpha \wedge \beta)} \ni{2-4}
\end{nd}$
\end{center}
```

For the disjunction, the assumption \( \alpha \vee \beta \) is used by \( \rulename{\vee E} \) with the goal \( \bot \), and each case clashes with one premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \alpha}
  \hypo {2} {\neg \beta}
  \open
  \hypo {3} {\alpha \vee \beta}
  \open
  \hypo {4} {\alpha}
  \have {5} {\bot} \ne{4,1}
  \close
  \open
  \hypo {6} {\beta}
  \have {7} {\bot} \ne{6,2}
  \close
  \have {8} {\bot} \oe{3,4-5,6-7}
  \close
  \have {9} {\neg (\alpha \vee \beta)} \ni{3-8}
\end{nd}$
\end{center}
```

The three derivations have 5, 5 and 9 lines, and none uses \( \rulename{RAA} \): every box closes by \( \rulename{\neg I} \) or \( \rulename{\vee E} \).
:::

::: {#exr-completeness-b2}
[B2: The method on modus ponens]

Apply the method of @thm-completeness to \( p, \ p \to q \models q \): list the four rows and the case of Step 2 that each falls under, and write the derivation that the proof produces, citing \( \rulename{LEM} \) and the sequents of @lem-connective-rows as single lines. (It is long; that is expected, and the usual length of an exercise answer does not apply.) Compare it with the derivation by \( \rulename{{\to}E} \).
:::

::: {.solution}
The atoms are \( p_1 = p \) and \( p_2 = q \). The rows:

- \( p = \mathrm{T} \), \( q = \mathrm{T} \): both premises true, Case 1; \( q^{v} = q \) is itself a premise.
- \( p = \mathrm{T} \), \( q = \mathrm{F} \): the premise \( p \to q \) is false, Case 2 with \( \gamma = p \to q \); @lem-truth-table-line gives \( p, \neg q \vdash \neg(p \to q) \) by \( ({\to}3) \).
- \( p = \mathrm{F} \), \( q \) either value: the premise \( p \) is false, Case 2 with \( \gamma = p \); the lemma gives \( \neg p \) (an atom case).

In Case 2, the clash is \( \rulename{\neg E} \) followed by \( \rulename{\bot E} \), which is the derivation of @prp-ex-falso written out. Splitting on \( q \) inside each case of a split on \( p \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p}
  \hypo {2} {p \to q}
  \have {3} {p \vee \neg p} \lem{}
  \open
  \hypo {4} {p}
  \have {5} {q \vee \neg q} \lem{}
  \open
  \hypo {6} {q}
  \close
  \open
  \hypo {7} {\neg q}
  \have {8} {\neg (p \to q)} \by{$({\to}3)$}{4,7}
  \have {9} {\bot} \ne{2,8}
  \have {10} {q} \be{9}
  \close
  \have {11} {q} \oe{5,6-6,7-10}
  \close
  \open
  \hypo {12} {\neg p}
  \have {13} {q \vee \neg q} \lem{}
  \open
  \hypo {14} {q}
  \have {15} {\bot} \ne{1,12}
  \have {16} {q} \be{15}
  \close
  \open
  \hypo {17} {\neg q}
  \have {18} {\bot} \ne{1,12}
  \have {19} {q} \be{18}
  \close
  \have {20} {q} \oe{13,14-16,17-19}
  \close
  \have {21} {q} \oe{3,4-11,12-20}
\end{nd}$
\end{center}
```

The box at line 6 has one line: in the row \( p = q = \mathrm{T} \) the goal \( q \) is the signed atom itself, so, as in the proof of @lem-atom-splitting, the box is its assumption alone. The result has 21 lines. The derivation by \( \rulename{{\to}E} \) has 3: the two premises and \( q \) by \( \rulename{{\to}E} \) citing lines 2 and 1. The method is uniform, not short: it does the same thing for every valid sequent, and pays for that with a split on every atom.
:::

::: {#exr-completeness-b3}
[B3: Table first, then a derivation]

Decide by a truth table whether \( \neg(p \leftrightarrow q) \models \neg p \leftrightarrow q \). If it holds, find a derivation of \( \neg(p \leftrightarrow q) \vdash \neg p \leftrightarrow q \) by search, where you may cite the sequents of @lem-connective-rows as derived rules. Which rule of your derivation is classical?
:::

::: {.solution}
The table:
\[
\begin{array}{cc|c|c}
p & q & \neg(p \leftrightarrow q) & \neg p \leftrightarrow q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F}
\end{array}
\]
The premise is true in rows 2 and 3, and so is the conclusion. So the entailment holds, and by @thm-completeness a derivation exists.

The search: the goal is a biconditional, so two boxes, one from \( \neg p \) to \( q \) and one from \( q \) to \( \neg p \). In the second, the goal \( \neg p \) is a negation: a box on \( p \), and \( p \), \( q \) give \( p \leftrightarrow q \) by \( ({\leftrightarrow}1) \), which clashes with the premise. In the first, the goal \( q \) is an atom, the only premise is a negation, and nothing else applies: we are stuck, and assume \( \neg q \). Then \( \neg p \), \( \neg q \) give \( p \leftrightarrow q \) by \( ({\leftrightarrow}2) \), which clashes with the premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (p \leftrightarrow q)}
  \open
  \hypo {2} {\neg p}
  \open
  \hypo {3} {\neg q}
  \have {4} {p \leftrightarrow q} \by{$({\leftrightarrow}2)$}{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {q} \raa{3-5}
  \close
  \open
  \hypo {7} {q}
  \open
  \hypo {8} {p}
  \have {9} {p \leftrightarrow q} \by{$({\leftrightarrow}1)$}{8,7}
  \have {10} {\bot} \ne{9,1}
  \close
  \have {11} {\neg p} \ni{8-10}
  \close
  \have {12} {\neg p \leftrightarrow q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

The classical rule is the \( \rulename{RAA} \) at line 6. (Pasting in the derivations of the two cited sequents gives a derivation in the primitive rules of 22 lines.) Whether some other derivation could avoid \( \rulename{RAA} \) is a question the table cannot answer. In fact none can; we state that without proof, as Chapter 2 did for similar sequents, and nothing depends on it.
:::

### C. Going deeper

::: {#exr-completeness-c1}
[C1: The remaining cases]

Write out in full the disjunction case and the biconditional case of the proof of @lem-truth-table-line, in the style of the implication case.
:::

::: {.solution}
Throughout, \( \Sigma \) is \( p_1^{v}, \dots, p_n^{v} \), and the induction hypotheses are \( \Sigma \vdash \alpha^{v} \) and \( \Sigma \vdash \beta^{v} \). "Chaining" is @lem-weakening-cut (c).

*Disjunction,* \( \varphi = \alpha \vee \beta \). By @def-truth-value, \( v(\alpha \vee \beta) = \mathrm{F} \) exactly when \( v(\alpha) = v(\beta) = \mathrm{F} \).

- *Case \( v(\alpha) = \mathrm{T} \).* Then \( \varphi^{v} = \alpha \vee \beta \) and \( \alpha^{v} = \alpha \). Chaining \( \Sigma \vdash \alpha \) with \( (\vee 1) \), \( \alpha \vdash \alpha \vee \beta \), gives \( \Sigma \vdash \alpha \vee \beta \).
- *Case \( v(\alpha) = \mathrm{F} \), \( v(\beta) = \mathrm{T} \).* Then \( \varphi^{v} = \alpha \vee \beta \) and \( \beta^{v} = \beta \). Chaining \( \Sigma \vdash \beta \) with \( (\vee 2) \) gives \( \Sigma \vdash \alpha \vee \beta \).
- *Case \( v(\alpha) = v(\beta) = \mathrm{F} \).* Then \( \varphi^{v} = \neg(\alpha \vee \beta) \), \( \alpha^{v} = \neg\alpha \) and \( \beta^{v} = \neg\beta \). Chaining both hypotheses with \( (\vee 3) \), \( \neg\alpha, \neg\beta \vdash \neg(\alpha \vee \beta) \), gives \( \Sigma \vdash \neg(\alpha \vee \beta) \).

*Biconditional,* \( \varphi = \alpha \leftrightarrow \beta \). By @def-truth-value, \( v(\alpha \leftrightarrow \beta) = \mathrm{T} \) exactly when \( v(\alpha) = v(\beta) \). Each case uses both hypotheses.

- *Case T, T.* \( \varphi^{v} = \alpha \leftrightarrow \beta \); chain \( \Sigma \vdash \alpha \), \( \Sigma \vdash \beta \) with \( ({\leftrightarrow}1) \).
- *Case F, F.* \( \varphi^{v} = \alpha \leftrightarrow \beta \); chain \( \Sigma \vdash \neg\alpha \), \( \Sigma \vdash \neg\beta \) with \( ({\leftrightarrow}2) \).
- *Case T, F.* \( \varphi^{v} = \neg(\alpha \leftrightarrow \beta) \); chain \( \Sigma \vdash \alpha \), \( \Sigma \vdash \neg\beta \) with \( ({\leftrightarrow}3) \).
- *Case F, T.* \( \varphi^{v} = \neg(\alpha \leftrightarrow \beta) \); chain \( \Sigma \vdash \neg\alpha \), \( \Sigma \vdash \beta \) with \( ({\leftrightarrow}4) \).

The cases cover all four pairs of values, so in each the property holds for \( \varphi \).

**Marking scheme.** (10 points)

- 4: the \( \vee \) case: the three value cases, each with the right sequent of @lem-connective-rows and only the hypotheses its premises need.
- 4: the \( \leftrightarrow \) case: the four value cases, each with the right sequent and both hypotheses.
- 1: names chaining (@lem-weakening-cut (c)) as the step that combines the hypotheses with the sequent.
- 1: says that the cases cover every pair of values.

Fatal errors (0 for the step): using a sequent whose premises are not the signed parts \( \alpha^{v} \), \( \beta^{v} \) of that case.
:::

::: {#exr-completeness-c2}
[C2: Exit check: completeness]

*Close the section first, and write from memory.*

::: {.enumerate options="label=(\alph*)"}
1. Prove @lem-atom-splitting: if \( \Delta, p \vdash \psi \) and \( \Delta, \neg p \vdash \psi \), then \( \Delta \vdash \psi \).
2. Prove Step 3 of the proof of @thm-completeness in full: from the Claim of Step 2, for every valuation \( v \), \( \Gamma, p_1^{v}, \dots, p_n^{v} \vdash \psi \), deduce \( \Gamma \vdash \psi \). State the statement you prove by induction, and say which principle of induction you use.
:::
:::

::: {.solution}
[Hint 1]

For (a): excluded middle and proof by cases. For (b): remove the signed atoms from the end of the list, one at a time.
:::

::: {.solution}
[Hint 2]

For (b): let \( S(j) \) say "for every valuation \( v \), \( \Gamma, p_1^{v}, \dots, p_j^{v} \vdash \psi \)", and show that \( S(j) \) implies \( S(j - 1) \) for \( 1 \le j \le n \).
:::

::: {.solution}
*(a)* Let \( D \) derive \( \psi \) from premises in \( \Delta, p \), and \( E \) from premises in \( \Delta, \neg p \). Write, as premises, those of \( D \) and \( E \) that lie in \( \Delta \); then \( p \vee \neg p \) by \( \rulename{LEM} \) (@prp-excluded-middle, a derived rule with no premises); then a box opening with \( p \) containing the nonpremise lines of \( D \), in which citations of the premise \( p \) now cite the assumption and citations of premises in \( \Delta \) cite the premise lines; then a box opening with \( \neg p \), built from \( E \) in the same way; then \( \psi \) by \( \rulename{\vee E} \), citing the line \( p \vee \neg p \) and the two boxes. (If \( D \) or \( E \) ends on a premise, its box is the assumption alone when that premise is the assumption's formula, and otherwise the assumption followed by \( \psi \) by \( \rulename{R} \).) Every copied line keeps its boxes, now inside the new box, and cites lines still available to it. The last line of each box is \( \psi \), as a line of that box itself, because the last line of \( D \) or \( E \) lay in no box. The two boxes and the \( \rulename{LEM} \) line lie in no box, so they are available at the final line. So the result is a derivation of \( \psi \) from premises in \( \Delta \), and \( \Delta \vdash \psi \).

*(b)* For \( 0 \le j \le n \), let \( S(j) \) be: for every valuation \( v \), \( \Gamma, p_1^{v}, \dots, p_j^{v} \vdash \psi \). The Claim of Step 2 is \( S(n) \).

*The step.* Let \( 1 \le j \le n \) and assume \( S(j) \). Let \( v \) be any valuation, and let \( v^{+} \), \( v^{-} \) agree with \( v \) except that \( v^{+}(p_j) = \mathrm{T} \) and \( v^{-}(p_j) = \mathrm{F} \). Since the \( p_i \) are distinct, both agree with \( v \) on \( p_1, \dots, p_{j-1} \). By \( S(j) \) for \( v^{+} \) and for \( v^{-} \), with \( \Delta \coloneqq \Gamma, p_1^{v}, \dots, p_{j-1}^{v} \): \( \Delta, p_j \vdash \psi \) and \( \Delta, \neg p_j \vdash \psi \). By (a), \( \Delta \vdash \psi \). As \( v \) was arbitrary, \( S(j - 1) \) holds.

*The induction.* We use @ax-induction on \( m \in \nN \) with the statement \( T(m) \): "if \( m \le n \), then \( S(n - m) \)". \( T(0) \) is \( S(n) \). If \( T(m) \) holds and \( m + 1 \le n \), then \( S(n - m) \) holds and \( j = n - m \) lies between \( 1 \) and \( n \), so the step gives \( S(n - m - 1) \), which is \( T(m + 1) \). Hence \( T(n) \), which is \( S(0) \): for every valuation, \( \Gamma \vdash \psi \). Valuations exist, so \( \Gamma \vdash \psi \).

(Inducting downwards on \( j \), or on the number of atoms removed, is the same argument; either earns full marks.)

**Marking scheme.** (10 points)

- 3: (a) pastes both derivations into the two boxes of a \( \rulename{\vee E} \) on \( p \vee \neg p \), with the premise \( p \) (or \( \neg p \)) redirected to the box's assumption, and says why every citation is still available.
- 1: (a) cites \( \rulename{LEM} \) (@prp-excluded-middle) as a derived rule.
- 3: (b) sets up an induction on the number of atoms removed (or downward on \( j \)) with a statement quantified over **every** valuation, and names the induction principle.
- 2: (b) in the step, applies the hypothesis to **both** valuations that differ at \( p_j \), and notes that they agree with \( v \) on the other atoms.
- 1: (b) concludes \( \Gamma \vdash \psi \) from \( S(0) \).

Fatal errors (0 for the step): splitting on an atom using the Claim for a single valuation only; an induction statement that fixes \( v \) before the induction, so that the two valuations of the step are not covered by the hypothesis.
:::

<!-- dependency ledger
lem-weakening-cut (proof): renumbering lines and moving boxes as blocks preserves nesting, availability and rule instances | inline (checked clause by clause against def-derivation)
lem-weakening-cut (proof): a one-line derivation whose only line is a premise is a derivation | def-derivation, def-derivable (a premise line; the last line lies in no box)
lem-connective-rows (proof): De Morgan (b) and (c) are derived without RAA | ch02 prp-de-morgan (the sentence after its derivations says so; cited in the proof)
lem-connective-rows (proof): prp-vacuous-implication and exm-double-negation-introduction come before RAA (Sections 2.1, 2.2) | ch02 section order
lem-truth-table-line (proof): every atom of an immediate part is an atom of the whole formula | the recursive definition of the set of atoms, Section 3.2 (after thm-structural-recursion)
lem-truth-table-line (proof): v(phi^v) = T; the value clauses of each connective | def-truth-value (cited)
lem-atom-splitting (proof): pasted lines keep availability inside a new box | inline, as in lem-weakening-cut
thm-completeness (proof): a finite list of formulas contains only finitely many atoms | inline (each formula has finitely many symbols)
thm-completeness (proof): integer arithmetic 1 <= n - m <= n from 0 <= m <= n - 1 | school arithmetic
thm-completeness (proof): a valuation may be changed at one atom and stays a valuation; at least one valuation exists | def-valuation (cited)
cor-derivable-iff-valid (proof): 2^n rows for n atoms | def-truth-table, lem-coincidence (Section 3.3)
exm-completeness-run (example): the search derivation of Chapter 2 has 13 lines | exr-finding-derivations-c2 solution (cited)
exr-completeness-b3 (solution): no derivation of the sequent avoids RAA | stated without proof and marked so; nothing depends on it
exr-completeness-b3 (solution): pasting the two cited rows gives 22 lines in primitive rules | inline count: the non-premise lines of the (<->2) and (<->1) derivations, 7 and 5, replace lines 4 and 9, so 12 + 6 + 4 = 22
cor-derivable-iff-valid (claim): the remark after it, compactness for infinite premise sets | stated without proof and marked so; nothing depends on it
-->
