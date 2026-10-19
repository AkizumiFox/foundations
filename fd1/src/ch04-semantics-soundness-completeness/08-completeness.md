# Completeness

Soundness (@thm-soundness) says that the rules of Chapters 1 and 2 never lead from true premises to a false conclusion: whatever can be derived is true in every row where the premises are. That answers half of the chapter's question. The other half is the converse. Could the rules be too **weak**, so that some sequent is true in every row and yet no derivation of it exists? This section proves that they are not: every truth-table consequence has a derivation. The proof reads a derivation off the truth table, one row at a time, and then glues the rows together with excluded middle.

## The question soundness leaves open

Recall the two relations from Section 4.5. \( \Gamma \vdash \psi \) says that **there is** a derivation of \( \psi \) from premises in \( \Gamma \) (@def-derivable). \( \Gamma \models \psi \) says that **every** valuation making all of \( \Gamma \) true makes \( \psi \) true (@def-valid-argument). Soundness is the implication
\[
\Gamma \vdash \psi \ \Rightarrow \ \Gamma \models \psi .
\]
Its converse is not automatic. The rules are a list that people wrote down, and a list can leave something out. Suppose, as a thought experiment, that we struck \( \rulename{RAA} \) (@def-rule-raa) from the list. Every derivation that remains is still a derivation, so soundness still holds. But the tautology \( p \vee \neg p \) would then have no derivation (this is the optional @thm-raa-independent of Section 4.7). So a sound list of rules can be too short. The question is whether **our** list is long enough.

Here is a sequent to keep in mind. The formula \( (p \to q) \vee (q \to p) \) is a tautology: if \( q \) is true then \( p \to q \) is true, and if \( q \) is false then \( q \to p \) is true. Chapter 3 found a derivation of it (@exr-finding-derivations-c2), but only after reaching for \( \rulename{LEM} \), and nothing in Chapter 3 promised that a derivation would be there to find. We want a theorem that promises it in advance, for every tautology and every valid sequent.

We are going to prove:

> If \( \Gamma \) is a list of formulas and \( \Gamma \models \psi \), then \( \Gamma \vdash \psi \).

The plan has two ideas, one per row and one for all the rows together.

1. **One row gives one derivation.** Fix a row of the truth table, that is, a valuation \( v \). Write each atom as it stands in that row: \( p \) if \( v \) makes \( p \) true, \( \neg p \) if \( v \) makes it false. From these signed atoms we will derive the formula \( \psi \) if \( \psi \) is true in the row, and \( \neg\psi \) if it is false. The derivation climbs the parse tree of \( \psi \), one connective at a time.
2. **The rows are glued by excluded middle.** If \( \Gamma \models \psi \), the first idea gives \( \psi \) from \( \Gamma \) and the signed atoms of **each** row. Two rows that differ only at the atom \( p \) have derivations from "\( \ldots, p \)" and from "\( \ldots, \neg p \)". The rule \( \rulename{\vee E} \) applied to \( p \vee \neg p \) merges them into one derivation that no longer mentions \( p \). Removing the atoms one at a time leaves a derivation from \( \Gamma \) alone.

We keep the premises \( \Gamma \) throughout, and we isolate the two ingredients as lemmas so that each can be checked on its own. Before either, we need a little bookkeeping about derivations.

::: {.second-reading title="Where the route comes from"}
The first idea is known as Kalmár's lemma, and gluing rows by excluded middle is the standard way to finish; the route is the classical one.
:::

## Bookkeeping: adding premises and chaining derivations

In Chapter 2 we learned to use a proved sequent as a single line (@def-derived-rule), and Section 2.3 proved what that gives, @lem-weakening-cut: (a) extra premises never hurt; (b) a statement already derived may be used as a premise; (c) a sequent already proved may be applied to statements already derived. The completeness proof uses (a) and (c) dozens of times. They also made Step 1 of the proof of @thm-soundness honest: for whole derivations, part (c) is the precise form of "abbreviates".

::: {.check}
Suppose \( \Gamma \vdash \alpha \) and \( \Gamma \vdash \neg\alpha \). Which part of @lem-weakening-cut, applied to which proved sequent, gives \( \Gamma \vdash \chi \) for every formula \( \chi \)?
:::

::: {.solution}
Part (c) with \( m = 2 \), \( \alpha_1 = \alpha \), \( \alpha_2 = \neg\alpha \) and \( \beta = \chi \), applied to @prp-ex-falso, \( P, \neg P \vdash Q \), with \( \alpha \) for \( P \) and \( \chi \) for \( Q \).
:::

## The rules prove their own truth tables

Each line of the truth table of a connective says something like "with \( \alpha \) true and \( \beta \) false, \( \alpha \to \beta \) comes out false". Read with signs, that line is a sequent: from \( \alpha \) and \( \neg\beta \), conclude \( \neg(\alpha \to \beta) \). If every such sequent is derivable, then the rules know the truth tables. This is the key to the first idea of the plan. Section 4.4 began by reading the tables off the rules; the lemma below makes that reading exact: every line of every table is a derivable sequent.

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

Here are the tables of @def-truth-value again, with each row tagged by the sequent of the lemma that derives it from the signed parts. Where two sequents fit a row, the tag is the one the proof of the next lemma uses.

| \( \alpha \) | \( \beta \) | \( \alpha \wedge \beta \) | \( \alpha \vee \beta \) | \( \alpha \to \beta \) | \( \alpha \leftrightarrow \beta \) |
|---|---|---|---|---|---|
| T | T | T \( (\wedge 1) \) | T \( (\vee 1) \) | T \( ({\to}2) \) | T \( ({\leftrightarrow}1) \) |
| T | F | F \( (\wedge 3) \) | T \( (\vee 1) \) | F \( ({\to}3) \) | F \( ({\leftrightarrow}3) \) |
| F | T | F \( (\wedge 2) \) | T \( (\vee 2) \) | T \( ({\to}1) \) | F \( ({\leftrightarrow}4) \) |
| F | F | F \( (\wedge 2) \) | F \( (\vee 3) \) | T \( ({\to}1) \) | T \( ({\leftrightarrow}2) \) |

Beside it: \( \alpha \) T gives \( \neg\alpha \) F, tagged \( (\neg 1) \); \( \alpha \) F gives \( \neg\alpha \) T, and no sequent is needed, since the signed part \( \neg\alpha \) is already the signed whole; \( \bot \) is always F, tagged \( (\bot 1) \).

Each sequent has as premises **only the parts it needs**, each as itself or negated. For instance, \( \alpha \wedge \beta \) is false as soon as \( \alpha \) is false, whatever \( \beta \) is, and \( (\wedge 2) \) has the single premise \( \neg\alpha \). This economy will matter: when the proof of the next lemma uses a row, it needs to know something only about the parts the row mentions.

::: {.idea}
Most of the sequents are already in the book: rules of Chapter 1, or results of Chapter 2 with \( \alpha \) and \( \beta \) put in for the letters. The others are short derivations of the kinds Chapter 2 practiced: a box that repeats a premise, or a \( \rulename{\neg I} \) box that reaches a clash. The only thing to watch is that no step, and no cited result, uses \( \rulename{RAA} \).
:::

The derivations, with a check that none uses \( \rulename{RAA} \), are in the fold below.

::: {.second-reading title="The fifteen derivations"}
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
:::

The \( \neg \) connective needs only one sequent. When \( \alpha \) is false, \( \neg\alpha \) is true, and the "sequent" \( \neg\alpha \vdash \neg\alpha \) is a one-line derivation; only the other row, \( (\neg 1) \), needs a proof.

::: {.warning}
The sequents of @lem-connective-rows go **from the parts to the whole**. Read backwards they are false. For instance \( \alpha \vee \beta \vdash \alpha \) is not derivable in general: the row \( p = \mathrm{F} \), \( q = \mathrm{T} \) makes \( p \vee q \) true and \( p \) false, so \( p \vee q \nvdash p \) by @cor-refuting-row. A row of a table tells us the value of the whole from the values of the parts, never the other way round.
:::

::: {.check}
Which tagged sequent covers \( \alpha \) F, \( \beta \) T for \( \to \)? And for \( \leftrightarrow \)?
:::

::: {.solution}
\( ({\to}1) \), \( \neg\alpha \vdash \alpha \to \beta \). (The row also fits \( ({\to}2) \).) For \( \leftrightarrow \): \( ({\leftrightarrow}4) \), \( \neg\alpha, \beta \vdash \neg(\alpha \leftrightarrow \beta) \).
:::

## One row, one derivation

A row of a truth table can be written as a list of premises: each atom as it stands in the row, itself if true, negated if false.

| \( p \) | \( q \) | \( r \) | the row, as premises |
|---|---|---|---|
| T | F | T | \( p, \ \neg q, \ r \) |

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
The superscript \( v \) is a label naming the row, not an exponent. In particular, for an atom \( p \), the **signed atom** \( p^{v} \) is \( p \) or \( \neg p \). For example, if \( v(p) = \mathrm{T} \) and \( v(q) = \mathrm{F} \), then \( p^{v} = p \), \( q^{v} = \neg q \), \( (p \to q)^{v} = \neg(p \to q) \) and \( (q \to p)^{v} = q \to p \). Whatever \( v \) is, \( v(\varphi^{v}) = \mathrm{T} \): the signed formula is always the true one of \( \varphi \) and \( \neg\varphi \), by the clause for \( \neg \) in @def-truth-value.

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
**Step roadmap.** ① List the atoms \( p_1, \dots, p_n \) of \( \Gamma \) and \( \psi \). ② **Claim:** for **every** valuation \( v \), \( \Gamma, p_1^{v}, \dots, p_n^{v} \vdash \psi \). If \( v \) makes all of \( \Gamma \) true, then \( \psi \) is true in that row, and @lem-truth-table-line derives it. If \( v \) makes some premise \( \gamma \) false, the lemma derives \( \neg\gamma \), which clashes with the premise \( \gamma \). ③ Remove the signed atoms one at a time, the last first, by @lem-atom-splitting: an induction on the number of atoms removed. To remove \( p_j \) we need derivations from both \( p_j \) and \( \neg p_j \) with the same other signed atoms: two rows that differ only at \( p_j \). That is why the Claim must hold for every valuation, not just one.
:::

Let us run the method of the roadmap on the tautology of the opening.


::: {#exm-completeness-run}
[The method on a tautology]

Run the roadmap of @thm-completeness on \( \models (p \to q) \vee (q \to p) \), and write the derivation it produces, citing the sequents of @lem-connective-rows as derived rules.
:::

::: {.solution}
Write \( \chi \) for \( (p \to q) \vee (q \to p) \). The list \( \Gamma \) is empty and the atoms are \( p_1 = p \), \( p_2 = q \). Every valuation makes \( \chi \) true (if \( v(q) = \mathrm{T} \) the left side is true; otherwise the right side is), so the Claim ② always falls in its first case (the row makes the premises, here none, true), and @lem-truth-table-line produces four short derivations, one per row:

- \( p, q \vdash \chi \): \( p \to q \) by \( ({\to}2) \) from \( q \), then \( \rulename{\vee I} \);
- \( p, \neg q \vdash \chi \): \( q \to p \) by \( ({\to}1) \) from \( \neg q \), then \( \rulename{\vee I} \);
- \( \neg p, q \vdash \chi \) and \( \neg p, \neg q \vdash \chi \): \( p \to q \) by \( ({\to}1) \) from \( \neg p \), then \( \rulename{\vee I} \).

(In the row \( p = \mathrm{F} \), \( q = \mathrm{T} \), both \( ({\to}1) \) and \( ({\to}2) \) would do; the proof of @lem-truth-table-line uses \( ({\to}1) \) whenever \( \alpha \) is false.) ③ first splits on \( q = p_2 \), twice: once with \( p \) and once with \( \neg p \) among the premises. Then it splits on \( p = p_1 \), once. Three uses of @lem-atom-splitting in two rounds. Pasting as in its proof, the last split is the outermost:

```{=latex}
\begin{center}
\begin{tikzpicture}[tree, level 1/.style={sibling distance=60mm, level distance=14mm}, level 2/.style={sibling distance=30mm, level distance=16mm}]
  \node {$\vdash \chi$: line 20, $\vee$E on line 1}
    child {node {box 2--10}
      child {node {box 4--6:\\ $({\to}2)$, $\vee$I} edge from parent node[tlabel, left] {$q$}}
      child {node {box 7--9:\\ $({\to}1)$, $\vee$I} edge from parent node[tlabel, right] {$\neg q$}}
      edge from parent node[tlabel, left] {$p$}}
    child {node {box 11--19}
      child {node {box 13--15:\\ $({\to}1)$, $\vee$I} edge from parent node[tlabel, left] {$q$}}
      child {node {box 16--18:\\ $({\to}1)$, $\vee$I} edge from parent node[tlabel, right] {$\neg q$}}
      edge from parent node[tlabel, right] {$\neg p$}};
\end{tikzpicture}
\end{center}
```

*Each leaf is one row of the table; each inner node is one use of @lem-atom-splitting.*


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

The derivation has 20 lines. The one found by search in @exr-finding-derivations-c2 has 13, and splits only once. Here the split on \( q \) inside the box of \( \neg p \) (lines 12–19) is wasted: both of its boxes do the same thing, because in the rows with \( p \) false the value of \( q \) does not matter. The proof is a **method** that always works, not a recipe for short derivations; to find a short one, search as in Section 3.1.
:::

::: {.check}
In the tree, which two leaves do the same thing, and why?
:::

::: {.solution}
The boxes 13–15 and 16–18. Both write \( p \to q \) by \( ({\to}1) \) from \( \neg p \) on line 11, because in a row with \( p \) false, \( p \to q \) is true whatever \( q \) is.
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

Step 2 is \( S(n) \). Applying the Claim with \( j = n \), then \( j = n - 1 \), and so on down to \( j = 1 \), removes the signed atoms one at a time and reaches \( S(0) \). This descent is an induction on the number of atoms removed; the fold after the proof writes it out.

**Step 4.** \( S(0) \) says that \( \Gamma \vdash \psi \), for every valuation \( v \); there is at least one valuation (for instance the one making every atom true), so \( \Gamma \vdash \psi \). This proves the theorem.
:::

::: {.second-reading title="The descent, as an induction"}
It remains to go down from \( S(n) \) to \( S(0) \), which takes \( n \) applications of the Claim. We count the applications made: for \( m \in \nN \), let \( T(m) \) say "if \( m \le n \), then \( S(n - m) \) holds". \( T(0) \) says that \( S(n) \) holds, which is Step 2. Suppose \( T(m) \) holds, and let \( m + 1 \le n \). Then \( m \le n \), so \( S(n - m) \) holds by \( T(m) \); and \( j \coloneqq n - m \) satisfies \( 1 \le j \le n \), because \( 0 \le m \le n - 1 \). The Claim gives \( S(j - 1) = S(n - (m + 1)) \), which is \( T(m + 1) \). By @ax-induction, \( T(m) \) holds for every \( m \in \nN \), and \( T(n) \) is \( S(0) \).
:::

If \( n = 0 \), the formulas of \( \Gamma \) and \( \psi \) are built from \( \bot \) alone, and Step 3 does nothing: \( S(0) \) is the Claim itself.

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

**Consistent and satisfiable coincide.** Section 4.7 showed that a satisfiable list is consistent. Completeness gives the converse. If \( \Delta \) is unsatisfiable, no row makes \( \Delta \) true, so \( \Delta \models \bot \) (there is no row to check), and \( \Delta \vdash \bot \) by @thm-completeness: \( \Delta \) is inconsistent. So a finite list is consistent exactly when it is satisfiable. The word of Section 3.2 and the word of Section 4.5 pick out the same lists, though one speaks of derivations and the other of rows; Section 3.2's task "derive \( \bot \)" and Section 4.6's search on a list always give the same answer.

::: {.second-reading title="Why two definitions of 'follows' are enough"}
Before Chapter 1, "\( \psi \) follows from \( \Gamma \)" had only an informal meaning: whatever a careful mathematician accepts as a valid inference, by any means. That is not a definition, but two things about it are clear for propositional forms. If \( \Gamma \vdash \psi \), then \( \psi \) follows informally: each rule is an inference every mathematician accepts, and a chain of accepted inferences is accepted. If \( \psi \) follows informally from \( \Gamma \) by form alone, then \( \Gamma \models \psi \): an inference valid by its form cannot have a row, which is one way of reading the atoms, making the premises true and the conclusion false. So the informal notion is squeezed between \( \vdash \) and \( \models \), and completeness makes the two ends meet: for propositional forms, the informal notion coincides with both. An argument of this shape is due to Georg Kreisel.
:::

::: {.second-reading title="Infinitely many premises"}
We defined \( \Gamma \vdash \psi \) only for a list, that is, for finitely many premises. One may allow an infinite collection \( \Gamma \) of premises and say \( \Gamma \vdash \psi \) when \( \psi \) is derivable from finitely many members of \( \Gamma \) (a derivation has finitely many lines, so it can only use finitely many). The equivalence with \( \Gamma \models \psi \) still holds for infinite \( \Gamma \); this is the compactness theorem of propositional logic. The optional Section 4.10 proves it; nothing in the core depends on it. Our proof does not reach it: Step 1 needs finitely many atoms.
:::

## Two columns that agree

Section 4.5 set the two meanings of "follows" side by side. Here is the full table, now that both theorems are proved: they agree row by row (@cor-derivable-iff-valid and the paragraph on consistency above).

| Notion | In terms of derivations | In terms of rows |
|---|---|---|
| follows | \( \Gamma \vdash \psi \) (@def-derivable, Section 1.2) | \( \Gamma \models \psi \) (@def-valid-argument, Section 4.5) |
| true by form alone | a theorem, \( \vdash \varphi \) | a tautology, \( \models \varphi \) (@def-tautology) |
| say the same | provably equivalent (@def-provable-equivalence, Section 2.4) | semantically equivalent (@def-semantic-equivalence) |
| cannot hold together | inconsistent, \( \Gamma \vdash \bot \) (@def-inconsistent-set, Section 3.2) | unsatisfiable (@def-satisfiable) |
| shown to hold by | one derivation | every row, or a closed search tree (@prp-search-decides) |
| shown to fail by | one refuting row (@cor-refuting-row) | one refuting row |
| more premises, cut | @lem-weakening-cut (Section 2.3): chaining and cut are why a derived rule may be cited | Section 4.5's structural properties: one line about rows each |
| tied together by | soundness, \( \vdash \Rightarrow \models \) (@thm-soundness) | completeness, \( \models \Rightarrow \vdash \) (@thm-completeness) |

## Two roads to every answer

We now have two independent ways to settle any question "is \( \Gamma \vdash \psi \)?". One is to **search** for a derivation, as in Section 3.1. The other is to **check a table**, and @cor-derivable-iff-valid says the two always agree. Here are two of Chapter 2's classical laws settled by the table first.

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

**Peirce's law.** Is \( (p \to q) \to p \models p \)? Work backwards from F (Section 4.4). A refuting row would need \( p \) false. Then \( p \to q \) is true, so \( (p \to q) \to p \) is "true implies false", which is false. So no row makes the premise true and the conclusion false: \( (p \to q) \to p \models p \), and by @thm-completeness, \( (p \to q) \to p \vdash p \).

Both answers came before anyone found a derivation. Chapter 2 found both by hand (@prp-de-morgan (d), and @prp-peirce, whose \( \vdash ((P \to Q) \to P) \to P \) gives the sequent by \( \rulename{{\to}E} \)), and the derivations there use \( \rulename{RAA} \). Completeness explains why a search had to succeed; it does not say how.

::: {.second-reading title="What the proof used"}
A common alternative route first turns \( \Gamma \models \psi \) into a single tautology, \( \models \gamma_1 \to (\gamma_2 \to \cdots \to (\gamma_k \to \psi)) \), proves completeness for tautologies, and then unpacks the implications with \( \rulename{{\to}E} \). Keeping \( \Gamma \) as premises, as Step 2 does, costs one extra case (a false premise) and saves that detour.

Section 4.5 remarked that the tables do not see which of Chapter 2's laws needed \( \rulename{RAA} \). Now we can say why they cannot. A table decides \( \Gamma \models \psi \), and by @cor-derivable-iff-valid that is the same as derivability with **all** the rules, \( \rulename{RAA} \) included. A table has no column recording which rules a derivation uses. Whether a sequent can be derived without \( \rulename{RAA} \) is a question about a shorter list of rules, and for that list the completeness theorem is false, as the next paragraph explains. So no truth-table check can tell the laws that need \( \rulename{RAA} \) from those that do not.

Which rules did the proof of completeness itself use? @lem-weakening-cut only pastes derivations. @lem-connective-rows uses no \( \rulename{RAA} \), as its proof checks. @lem-truth-table-line and the Claim chain those sequents, together with @prp-ex-falso, which Chapter 2 derived before \( \rulename{RAA} \) appeared. The one classical step is the line \( p \vee \neg p \) of @lem-atom-splitting. So the theorem is really about the full list of rules, \( \rulename{RAA} \) included. Without \( \rulename{RAA} \) the list is sound but not complete, as the optional @thm-raa-independent shows for \( \vdash p \vee \neg p \) and \( \neg\neg p \vdash p \); the proof above breaks exactly at the splitting.
:::

::: {.warning}
Completeness does not say that a tautology has a derivation **without** \( \rulename{RAA} \). It says there is a derivation from the rules of Chapters 1 and 2, all of them. The formula \( (p \to q) \vee (q \to p) \) is a tautology, and every derivation found for it so far uses \( \rulename{LEM} \) or \( \rulename{RAA} \). Whether a particular tautology can do without them is a different question, and a table cannot answer it.
:::

## A truth-table step: TAUT

Completeness has a practical consequence. Any step from earlier lines to a new one that a truth table confirms can be filled in by a derivation, so the step may be written as one line and the filling left to the theorem.

::: {#def-rule-taut}
[The Step TAUT]

In a derivation of formulas of @def-formula, a line \( \psi \) may be justified by **TAUT**, citing lines \( i_1, \dots, i_m \) (\( m \ge 0 \)) available at it, if \( \varphi_{i_1}, \dots, \varphi_{i_m} \models \psi \): every row that makes the cited lines true makes \( \psi \) true. For \( m = 0 \), \( \psi \) must be a tautology.
:::

A TAUT line abbreviates a derivation in the rules of Chapters 1 and 2: by @cor-derivable-iff-valid, \( \varphi_{i_1}, \dots, \varphi_{i_m} \vdash \psi \), and that derivation is pasted in as a derived rule's is (@def-derived-rule; @lem-weakening-cut for a line in no box). So TAUT derives nothing new, and @thm-soundness holds for derivations that use it. A TAUT line is checked by a table, not found by a search; its justification reads "TAUT" with the cited lines.

**Convention.** TAUT is a license, not a style. It is used only for a step that a written proof would pass over without comment, such as a rearrangement of connectives ("so if \( p \), then \( q \)"), never to hide the step an argument is about.

::: {#exm-taut-step}
[One line for twelve]

Derive \( \neg(p \to q) \vdash p \wedge \neg q \) with TAUT, and say what the step abbreviates.
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (p \to q)}
  \have {2} {p \wedge \neg q} \taut{1}
\end{nd}$
\end{center}
```

The check: the premise is true only in the row \( p = \mathrm{T} \), \( q = \mathrm{F} \), since an implication is false only there, and \( p \wedge \neg q \) is true in that row. Written out with the rules of Chapter 2, the step takes twelve lines (fold below). It is a step a written proof passes over ("an implication fails only with a true hypothesis and a false conclusion"), so the convention allows it.
:::

::: {.second-reading title="The step written out"}
An \( \rulename{RAA} \) box on \( \neg p \), in which @prp-vacuous-implication (VI) gives \( p \to q \), clashing with line 1, gives \( p \). A \( \rulename{\neg I} \) box on \( q \), in which an inner box gives \( p \to q \) again, gives \( \neg q \). Then \( \rulename{\wedge I} \). The proof that a TAUT line can always be written out builds a longer derivation still, by the method of @thm-completeness; this one was found by search.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (p \to q)}
  \open
  \hypo {2} {\neg p}
  \have {3} {p \to q} \by{VI}{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {p} \raa{2-4}
  \open
  \hypo {6} {q}
  \open
  \hypo {7} {p}
  \have {8} {q} \r{6}
  \close
  \have {9} {p \to q} \ii{7-8}
  \have {10} {\bot} \ne{9,1}
  \close
  \have {11} {\neg q} \ni{6-10}
  \have {12} {p \wedge \neg q} \ai{5,11}
\end{nd}$
\end{center}
```
:::

::: {.check}
May line 3 be justified by TAUT: 1 \( p \vee q \); 2 \( p \to r \); 3 \( r \vee q \), TAUT 1, 2?
:::

::: {.solution}
Yes. In a row making lines 1 and 2 true, either \( p \) is true, and then \( r \) is, or \( p \) is false, and then \( q \) is; either way \( r \vee q \) is true.
:::

::: {.warning}
[Not allowed: TAUT]

The first three steps break a clause of @def-rule-taut, named in the tag; the fourth is legal and breaks the convention.

- "\( q \to p \), TAUT 1", with line 1 \( p \to q \). The row \( p = \mathrm{F} \), \( q = \mathrm{T} \) makes line 1 true and the new line false. *Clause "every row that makes the cited lines true".*
- Citing by TAUT a line inside a box that has closed. *Clause "available"*: the scope rule of @def-derivation.
- TAUT on a line that is not a formula of @def-formula, such as "for every \( x \), \( x^2 \ge 0 \)". *Clause "formulas of @def-formula".*
- "\( \neg p \), TAUT 1, 2", with lines \( p \to q \) and \( \neg q \), in a proof whose point is that contrapositive step. *Convention*: legal by the definition, but it hides the step the argument is about; write \( \rulename{MT} \) (@prp-modus-tollens) or the derivation.
:::

::: {.remark}
[Looking ahead]

Chapter 6 extends TAUT to formulas with quantifiers, reading each quantified part as a letter; Chapter 8 names the steps a written proof passes over without comment.
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

::: {#exr-completeness-a2}
[A2: Drill]

The parts run from signed formulas and the steps of the proof, through consistency and the two columns, to judging TAUT lines.

::: {.enumerate options="label=(\alph*)"}
1. \( v(p) = \mathrm{F} \), \( v(q) = \mathrm{T} \). Write \( p^{v} \), \( q^{v} \), \( (p \to q)^{v} \), \( (q \to p)^{v} \).
2. \( \varphi = \neg p \wedge q \), \( v(p) = v(q) = \mathrm{T} \). Which sequent does @lem-truth-table-line give?
3. In (b), which tagged sequent does the proof use at the root, and where does its premise come from?
4. A sequent has three atoms. How many row derivations and how many uses of @lem-atom-splitting does the method build?
5. In the step from \( S(j) \) to \( S(j - 1) \), which signed atom disappears?
6. \( \Gamma = q \), \( \psi = p \vee q \), \( v(p) = v(q) = \mathrm{F} \). Which case of the Claim of Step 2 applies?
7. Is this TAUT line legal: 2 \( p \vee q \); 3 \( \neg p \); 5 \( q \), TAUT 2, 3?
8. Is this one legal: 1 \( p \to q \); 4 \( q \to p \), TAUT 1?
9. Is the list \( p \vee q, \ \neg p, \ \neg q \) consistent?
10. In the table "Two columns that agree", what is the twin of "a theorem"?
11. May \( \neg(p \wedge \neg p) \) be written by TAUT citing no line?
12. A list is satisfiable. What does completeness add to what soundness already says about it?
:::
:::

::: {.solution}
(a) \( \neg p \), \( q \), \( p \to q \), \( \neg(q \to p) \).

(b) \( p, q \vdash \neg(\neg p \wedge q) \).

(c) \( (\wedge 2) \) with \( \alpha = \neg p \): \( \neg\neg p \vdash \neg(\neg p \wedge q) \). The premise \( \neg\neg p \) comes from \( p \) by \( (\neg 1) \).

(d) \( 8 \) and \( 7 \).

(e) \( p_j^{v} \).

(f) Case 2, with \( \gamma = q \), which \( v \) makes false.

(g) Yes: every row making \( p \vee q \) and \( \neg p \) true makes \( q \) true.

(h) No: the row \( p = \mathrm{F} \), \( q = \mathrm{T} \) makes line 1 true and line 4 false.

(i) No. It is unsatisfiable, so inconsistent ("Consistent and satisfiable coincide"); directly, \( \rulename{\vee E} \) on \( p \vee q \) with \( \rulename{\neg E} \) in each box gives \( \bot \).

(j) A tautology.

(k) Yes: it is a tautology (\( m = 0 \)).

(l) Nothing about this list: soundness already makes it consistent. Completeness speaks of unsatisfiable lists: they are inconsistent.
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

In Case 2, the clash is \( \rulename{\neg E} \) followed by \( \rulename{\bot E} \), which is the derivation of @prp-ex-falso written out. Splitting on \( q \) inside each case of a split on \( p \), the derivation has this shape:

```{=latex}
\begin{center}
\begin{tikzpicture}[tree, level 1/.style={sibling distance=64mm, level distance=14mm}, level 2/.style={sibling distance=32mm, level distance=18mm}]
  \node {line 21, $\vee$E on line 3}
    child {node {box 4--11\\ ($\vee$E at 11 on line 5)}
      child {node {box 6--6:\\ the goal is\\ the assumption} edge from parent node[tlabel, left] {$q$}}
      child {node {box 7--10: $({\to}3)$,\\ clash with line 2,\\ $\bot$E} edge from parent node[tlabel, right] {$\neg q$}}
      edge from parent node[tlabel, left] {$p$}}
    child {node {box 12--20\\ ($\vee$E at 20 on line 13)}
      child {node {box 14--16:\\ clash of lines\\ 1 and 12, $\bot$E} edge from parent node[tlabel, left] {$q$}}
      child {node {box 17--19:\\ the same clash} edge from parent node[tlabel, right] {$\neg q$}}
      edge from parent node[tlabel, right] {$\neg p$}};
\end{tikzpicture}
\end{center}
```

Written out:

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

::: {#exr-completeness-b4}
[B4: When TAUT is welcome]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( p \to (q \wedge r), \ \neg r \vdash \neg p \) twice: once with a single TAUT line, once with primitive rules.
2. By the convention of this section, which is the better proof, and why?
3. In a longer derivation, line 7 holds \( \neg(p \wedge \neg q) \) and line 8 holds \( p \to q \). Justify line 8 by TAUT, and say why the convention allows it.
:::
:::

::: {.solution}
(a) With TAUT, line 3 is justified because a row making both premises true has \( r \) false, so \( q \wedge r \) false, so \( p \) false. With primitive rules, a \( \rulename{\neg I} \) box on \( p \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \to (q \wedge r)}
  \hypo {2} {\neg r}
  \have {3} {\neg p} \taut{1,2}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {p \to (q \wedge r)}
  \hypo {2} {\neg r}
  \open
  \hypo {3} {p}
  \have {4} {q \wedge r} \ie{1,3}
  \have {5} {r} \ae{4}
  \have {6} {\bot} \ne{5,2}
  \close
  \have {7} {\neg p} \ni{3-6}
\end{nd}$
\end{center}
```

(b) The primitive one. The TAUT line hides the only idea of the argument, modus tollens through the conjunction, which is exactly what the convention forbids.

(c) 8 \( p \to q \), TAUT 7. The two formulas are equivalent (each is false exactly at \( p = \mathrm{T} \), \( q = \mathrm{F} \)), and the step is a rearrangement a written proof makes without comment.
:::

::: {#exr-completeness-b5}
[B5: Consistent or not]

Decide whether each list is consistent. Justify "consistent" by a row and the result that makes it a proof; justify "inconsistent" by a derivation of \( \bot \), or by a search and the result that makes it a proof.

::: {.enumerate options="label=(\alph*)"}
1. \( p \to q, \ q \to r, \ p, \ \neg r \).
2. \( p \vee q, \ \neg p \vee \neg q, \ p \leftrightarrow q \).
3. \( p \to \neg q, \ q \to \neg r, \ r \to \neg p \).
:::
:::

::: {.solution}
(a) Inconsistent:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \to q}
  \hypo {2} {q \to r}
  \hypo {3} {p}
  \hypo {4} {\neg r}
  \have {5} {q} \ie{1,3}
  \have {6} {r} \ie{2,5}
  \have {7} {\bot} \ne{6,4}
\end{nd}$
\end{center}
```

(b) Inconsistent. A search closes: \( p \leftrightarrow q \) gives \( p, q \) or \( \neg p, \neg q \); under the first, \( \neg p \vee \neg q \) closes both ways; under the second, \( p \vee q \) closes both ways. So the list is unsatisfiable (@prp-search-decides), hence inconsistent, by @thm-completeness ("Consistent and satisfiable coincide").

(c) Consistent. The row with \( p \), \( q \), \( r \) all false makes all three members true (false hypotheses), so the list is satisfiable, hence consistent (Section 4.7, by @thm-soundness).
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
*(a)* Let \( D \) derive \( \psi \) from premises in \( \Delta, p \), and \( E \) from premises in \( \Delta, \neg p \). Write, as premises, those of \( D \) and \( E \) that lie in \( \Delta \); then \( p \vee \neg p \) by \( \rulename{LEM} \) (@prp-excluded-middle, a derived rule with no premises); then a box opening with \( p \) containing the non-premise lines of \( D \), in which citations of the premise \( p \) now cite the assumption and citations of premises in \( \Delta \) cite the premise lines; then a box opening with \( \neg p \), built from \( E \) in the same way; then \( \psi \) by \( \rulename{\vee E} \), citing the line \( p \vee \neg p \) and the two boxes. (If \( D \) or \( E \) ends on a premise, its box is the assumption alone when that premise is the assumption's formula, and otherwise the assumption followed by \( \psi \) by \( \rulename{R} \).) Every copied line keeps its boxes, now inside the new box, and cites lines still available to it. The last line of each box is \( \psi \), as a line of that box itself, because the last line of \( D \) or \( E \) lay in no box. The two boxes and the \( \rulename{LEM} \) line lie in no box, so they are available at the final line. So the result is a derivation of \( \psi \) from premises in \( \Delta \), and \( \Delta \vdash \psi \).

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

::: {#exr-normal-forms-c3}
[C3: Exit check: deciding sequents]

For each sequent, decide whether it holds. If it does, justify this by a derivation, or by a truth table and the theorem that turns the table into a derivation; if it does not, give a refuting row and say which theorem turns the row into a proof that no derivation exists.

::: {.enumerate options="label=(\alph*)"}
1. \( (p \to q) \vee (p \to r) \vdash p \to (q \vee r) \).
2. \( (p \to q) \to r \vdash p \to r \).
3. \( p \vee (q \wedge r) \vdash (p \vee q) \wedge r \).
4. \( (p \vee q) \wedge \neg p \vdash q \vee r \).
:::
:::

::: {.solution}
*(a)* Derivable. The goal is an implication: a box on \( p \), with the goal \( q \vee r \); the premise is a disjunction, used by \( \rulename{\vee E} \) inside the box; in each case \( \rulename{{\to}E} \) with \( p \) gives one side, and \( \rulename{\vee I} \) gives the goal.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(p \to q) \vee (p \to r)}
  \open
  \hypo {2} {p}
  \open
  \hypo {3} {p \to q}
  \have {4} {q} \ie{3,2}
  \have {5} {q \vee r} \oi{4}
  \close
  \open
  \hypo {6} {p \to r}
  \have {7} {r} \ie{6,2}
  \have {8} {q \vee r} \oi{7}
  \close
  \have {9} {q \vee r} \oe{1,3-5,6-8}
  \close
  \have {10} {p \to (q \vee r)} \ii{2-9}
\end{nd}$
\end{center}
```

*(b)* Not derivable. In the row \( p = \mathrm{T} \), \( q = \mathrm{F} \), \( r = \mathrm{F} \), the premise is true (\( p \to q \) is F, so \( (p \to q) \to r \) is T) and the conclusion \( p \to r \) is F. By @cor-refuting-row, \( (p \to q) \to r \nvdash p \to r \).

*(c)* Not derivable. In the row \( p = \mathrm{T} \), \( q = \mathrm{T} \), \( r = \mathrm{F} \) (the value of \( q \) does not matter), the premise is true because \( p \) is, and the conclusion is false because \( r \) is. By @cor-refuting-row, the sequent fails.

*(d)* Derivable. Split the premise by \( \rulename{\wedge E} \), then use \( p \vee q \) by \( \rulename{\vee E} \): the case \( p \) clashes with \( \neg p \) and closes by \( \rulename{\bot E} \); the case \( q \) gives the goal by \( \rulename{\vee I} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(p \vee q) \wedge \neg p}
  \have {2} {p \vee q} \ae{1}
  \have {3} {\neg p} \ae{1}
  \open
  \hypo {4} {p}
  \have {5} {\bot} \ne{4,3}
  \have {6} {q \vee r} \be{5}
  \close
  \open
  \hypo {7} {q}
  \have {8} {q \vee r} \oi{7}
  \close
  \have {9} {q \vee r} \oe{2,4-6,7-8}
\end{nd}$
\end{center}
```

Neither derivation uses \( \rulename{RAA} \). As the problem allows, (a) and (d) may instead be justified by a table (or backwards from F) showing the entailment, followed by @thm-completeness.

**Marking scheme.** (10 points; 2.5 per sequent)

- 1 per sequent: the correct verdict.
- 1.5 per sequent: its justification: a derivation in which every line is justified and every citation available, or a table check with @thm-completeness; or a row that makes **every** premise true and the conclusion false, checked, with @cor-refuting-row (or @thm-soundness) cited.

Fatal errors (0 for the sequent's justification): a "refuting row" that makes some premise false; a derivation citing a line that is not available.
:::

::: {#exr-completeness-c4}
[C4: Challenge: Strike out ∨I]

Strike \( \rulename{\vee I} \) from the primitive rules.

::: {.enumerate options="label=(\alph*)"}
1. Which sequents of @lem-connective-rows lose the derivations given in its proof (the table of the fold "The fifteen derivations"), and which step of the proof of @thm-completeness also uses \( \rulename{\vee I} \), through a result of Chapter 2?
2. Read \( \vee \) as \( \wedge \): a valuation now makes \( \varphi \vee \psi \) true exactly when it makes both parts true; every other clause stays. Show that every remaining primitive rule is sound for this reading.
3. Deduce that neither \( p \vdash p \vee q \) nor \( \vdash p \vee \neg p \) is derivable without \( \rulename{\vee I} \) (and without derived rules derived with it), although both are valid: the shorter list of rules is sound but not complete.
:::
:::

::: {.solution}
(a) \( (\vee 1) \) and \( (\vee 2) \) are \( \rulename{\vee I} \) itself; \( (\wedge 2) \) and \( (\wedge 3) \) are derived by \( \rulename{\vee I} \) and then @prp-de-morgan (c). And @lem-atom-splitting uses @prp-excluded-middle, whose derivation in Section 2.5 uses \( \rulename{\vee I} \) twice.

(b) Only the cases \( \rulename{\vee I} \) and \( \rulename{\vee E} \) of the proof of @thm-soundness use the clause for \( \vee \), and \( \rulename{\vee I} \) is gone. \( \rulename{\vee E} \): if a valuation makes \( \Gamma_k \) true, it makes \( \varphi \vee \psi \) true, hence, in the new reading, both \( \varphi \) and \( \psi \); by the first box it makes \( \chi \) true. Every other case is unchanged.

(c) The valuation with \( p \) true and \( q \) false makes \( p \) true and, in the new reading, \( p \vee q \) false; every valuation makes \( p \vee \neg p \) false in the new reading, since \( p \) and \( \neg p \) are never both true. By (b), and Step 1 of the proof of @thm-soundness (a derived rule derived without \( \rulename{\vee I} \) expands, by that step, into a pasted derivation in the remaining primitive rules), neither sequent has a derivation without \( \rulename{\vee I} \) and the derived rules that use it, such as @prp-excluded-middle. Both are valid in the ordinary tables.

**Marking scheme.** (10 points)

- 3: (a), all four sequents and the excluded-middle step.
- 4: (b), with the \( \rulename{\vee E} \) case argued and the other cases said to be unchanged.
- 3: (c), both valuations and the conclusion, with Step 1's restriction to derived rules derived without \( \rulename{\vee I} \).

Fatal errors (0 for the step): in (c), using the ordinary tables.
:::

::: {#exr-completeness-c5}
[C5: Challenge: From a closed tree to a derivation]

Let a search tree (Section 4.6) for \( \Gamma, \neg\psi \) have every branch closed. For a node \( X \), let \( \Delta_X \) be the list of formulas on the path from the root down to \( X \), \( X \) included.

::: {.enumerate options="label=(\alph*)"}
1. Prove, by induction on the number of nodes below \( X \), that if every branch through \( X \) is closed, then \( \Delta_X \vdash \bot \). Treat a closed leaf and each rule of the table of search rules, naming the derivable sequents you use.
2. Deduce \( \Gamma \vdash \psi \).
3. Explain why (a), (b) and @prp-search-decides give a second proof of @thm-completeness, and where it uses \( \rulename{RAA} \) or \( \rulename{LEM} \).
:::
:::

::: {.solution}
[Hint 1]

A one-way rule: derive the added formulas from the used one, then chain (@lem-weakening-cut). A two-way rule: join the two derivations of \( \bot \).
:::

::: {.solution}
[Hint 2]

For \( \varphi \to \psi \), split as \( \neg\varphi \) or \( \psi \): from \( \Delta, \neg\varphi \vdash \bot \) get \( \Delta \vdash \varphi \) by \( \rulename{RAA} \).
:::

::: {.solution}
(a) Write \( \Delta \) for \( \Delta_X \).

*A closed leaf.* \( \Delta \) holds \( \varphi \) and \( \neg\varphi \) (one \( \rulename{\neg E} \) line) or \( \bot \) (the premise itself): \( \Delta \vdash \bot \).

*An inner node.* Its children were added by the rule of some \( \chi \) in \( \Delta \). Every branch through each child is closed, and each child has fewer nodes below it, so the hypothesis gives \( \Delta, \alpha_1 \vdash \bot \) (or \( \Delta, \alpha_1, \alpha_2 \vdash \bot \)) for the formulas \( \alpha \) that each child adds.

*One-way rules.* It suffices to show \( \Delta \vdash \alpha \) for each added \( \alpha \), and then chain (@lem-weakening-cut (c), after weakening). \( \varphi \wedge \psi \): \( \rulename{\wedge E} \). \( \neg(\varphi \vee \psi) \vdash \neg\varphi \): a \( \rulename{\neg I} \) box on \( \varphi \), \( \rulename{\vee I} \), \( \rulename{\neg E} \); likewise \( \neg\psi \). \( \neg(\varphi \to \psi) \vdash \varphi \): an \( \rulename{RAA} \) box on \( \neg\varphi \), in which @prp-vacuous-implication gives \( \varphi \to \psi \), then \( \rulename{\neg E} \). \( \neg(\varphi \to \psi) \vdash \neg\psi \): a \( \rulename{\neg I} \) box on \( \psi \), in which an inner box gives \( \varphi \to \psi \) by \( \rulename{R} \) and \( \rulename{{\to}I} \), then \( \rulename{\neg E} \). \( \neg\neg\varphi \vdash \varphi \): @prp-double-negation.

*Two-way rules.* \( \varphi \vee \psi \): \( \rulename{\vee E} \) on the line \( \varphi \vee \psi \), with the two derivations of \( \bot \) pasted into the boxes as in the proof of @lem-atom-splitting. \( \neg(\varphi \wedge \psi) \): from \( \Delta, \neg\varphi \vdash \bot \), \( \Delta \vdash \varphi \) by \( \rulename{RAA} \); likewise \( \Delta \vdash \psi \); then \( \rulename{\wedge I} \), and \( \rulename{\neg E} \) with \( \neg(\varphi \wedge \psi) \). \( \varphi \to \psi \): \( \Delta \vdash \varphi \) by \( \rulename{RAA} \) from the first child; \( \rulename{{\to}E} \) gives \( \psi \); cut with \( \Delta, \psi \vdash \bot \). \( \varphi \leftrightarrow \psi \): from \( \Delta, \varphi, \psi \vdash \bot \) and \( \Delta, \varphi \vdash \psi \) (by \( \rulename{{\leftrightarrow}E} \)), cut gives \( \Delta, \varphi \vdash \bot \); from \( \Delta, \neg\varphi, \neg\psi \vdash \bot \) and \( \Delta, \neg\varphi \vdash \neg\psi \) (a \( \rulename{\neg I} \) box on \( \psi \): \( \varphi \) by \( \rulename{{\leftrightarrow}E} \), clash), cut gives \( \Delta, \neg\varphi \vdash \bot \); join the two by @lem-atom-splitting, which holds for any formula in place of the atom (the remark after its proof). \( \neg(\varphi \leftrightarrow \psi) \): \( \Delta, \varphi \vdash \neg\psi \) (a \( \rulename{\neg I} \) box on \( \psi \): \( \varphi \leftrightarrow \psi \) by \( \rulename{{\leftrightarrow}I} \) with two two-line boxes, each closed by \( \rulename{R} \), then the clash with \( \neg(\varphi \leftrightarrow \psi) \)), so \( \Delta, \varphi \vdash \bot \) by cut with the first child; \( \Delta, \neg\varphi \vdash \psi \) (an \( \rulename{RAA} \) box on \( \neg\psi \): \( \varphi \leftrightarrow \psi \) by \( \rulename{{\leftrightarrow}I} \), each box closing by a clash and \( \rulename{\bot E} \), then the clash with \( \neg(\varphi \leftrightarrow \psi) \)), so \( \Delta, \neg\varphi \vdash \bot \) by cut with the second child; join by @lem-atom-splitting.

(b) At the root, \( \Gamma, \neg\psi \vdash \bot \); an \( \rulename{RAA} \) box on \( \neg\psi \) holding that derivation gives \( \Gamma \vdash \psi \) (@prp-derivable-iff-negation-inconsistent (b)).

(c) If \( \Gamma \models \psi \), a search tree for \( \Gamma, \neg\psi \) can be continued until every branch is closed or finished (@prp-search-decides (a)), and it has no open finished branch, since by (c) of that proposition its row would refute \( \Gamma \models \psi \). So every branch is closed, and (a), (b) give \( \Gamma \vdash \psi \). \( \rulename{RAA} \) enters in the cases \( \neg(\varphi \to \psi) \), \( \neg\neg\varphi \), \( \neg(\varphi \wedge \psi) \), \( \varphi \to \psi \), \( \neg(\varphi \leftrightarrow \psi) \) and at the root; \( \rulename{LEM} \) in the two biconditional cases. The derivation follows the tree, so it is often far shorter than the \( 2^n \) rows of the first proof.

**Marking scheme.** (12 points)

- 1: the closed leaf.
- 3: the four one-way cases.
- 5: the five two-way cases (1 each).
- 1: (b).
- 2: (c), with the classical steps located.

Fatal errors (0 for the step): treating a split by assuming one side only.
:::

### R. Review

::: {#exr-normal-forms-r1}
[R1]

Find a derivation of \( p \vee q, \ \neg(p \wedge r), \ r \vdash q \).
:::

::: {.solution}
The method of Section 3.1 (@exm-search-cases shows it on a proof by cases). The goal \( q \) is an atom, so no introduction rule applies; the premise \( p \vee q \) is a disjunction, so we use it by \( \rulename{\vee E} \), with the goal \( q \) in both boxes. The case \( q \) is the goal. In the case \( p \), nothing gives \( q \) directly, so we look for a clash: \( p \) and the premise \( r \) build \( p \wedge r \) by \( \rulename{\wedge I} \), which clashes with \( \neg(p \wedge r) \), and \( \rulename{\bot E} \) closes the impossible case (@exm-manufactured-clash).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \vee q}
  \hypo {2} {\neg (p \wedge r)}
  \hypo {3} {r}
  \open
  \hypo {4} {p}
  \have {5} {p \wedge r} \ai{4,3}
  \have {6} {\bot} \ne{5,2}
  \have {7} {q} \be{6}
  \close
  \open
  \hypo {8} {q}
  \close
  \have {9} {q} \oe{1,4-7,8-8}
\end{nd}$
\end{center}
```

The second box is its assumption alone, which is already the goal. No \( \rulename{RAA} \) is used.
:::

::: {#exr-normal-forms-r2}
[R2]

Let \( m \) and \( n \) be integers, and consider the argument: "\( m + n \) is even only if \( m \) and \( n \) are both even or both odd. \( m \) is even and \( n \) is odd. Therefore \( m + n \) is not even." Translate it into a sequent, using atoms \( e \): "\( m + n \) is even", \( a \): "\( m \) is even", \( b \): "\( n \) is even", and decide whether the premises entail the conclusion.
:::

::: {.solution}
"\( P \) only if \( Q \)" is \( P \to Q \) (Section 1.1, and @exr-statements-and-connectives-c1). "Both odd" is \( \neg a \wedge \neg b \), since an integer is odd exactly when it is not even. So the sequent is
\[
e \to ((a \wedge b) \vee (\neg a \wedge \neg b)), \ \ a \wedge \neg b \ \models \ \neg e .
\]
Work backwards from F. A refuting row needs \( \neg e \) false, so \( e = \mathrm{T} \), and the second premise true, so \( a = \mathrm{T} \), \( b = \mathrm{F} \). In that row \( a \wedge b \) and \( \neg a \wedge \neg b \) are both F, so the first premise is \( \mathrm{T} \to \mathrm{F} \), which is F. So no row makes both premises true and the conclusion false: the entailment holds. By @thm-completeness, the sequent is also derivable. (The eight-row table gives the same answer; working backwards found the only candidate row at once.)
:::

::: {#exr-normal-forms-r3}
[R3]

Is \( (p \wedge (q \vee r)) \to ((p \wedge q) \vee r) \) a tautology? Is it derivable without \( \rulename{RAA} \)?
:::

::: {.solution}
*A tautology.* Work backwards from F (Section 4.4). The formula is false only if \( p \wedge (q \vee r) \) is true and \( (p \wedge q) \vee r \) is false. The second needs \( r \) false and \( p \wedge q \) false; the first needs \( p \) true and \( q \vee r \) true, so with \( r \) false, \( q \) true. But then \( p \wedge q \) is true. No row makes the formula false, so it is a tautology (@def-tautology).

*Derivable without \( \rulename{RAA} \).* Completeness (@thm-completeness) says it is derivable, but not how, and its proof uses \( \rulename{LEM} \) in @lem-atom-splitting, so it does not answer the second question. A search does: the goal is an implication, so a box on \( p \wedge (q \vee r) \); split it by \( \rulename{\wedge E} \) and use \( q \vee r \) by \( \rulename{\vee E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {p \wedge (q \vee r)}
  \have {2} {p} \ae{1}
  \have {3} {q \vee r} \ae{1}
  \open
  \hypo {4} {q}
  \have {5} {p \wedge q} \ai{2,4}
  \have {6} {(p \wedge q) \vee r} \oi{5}
  \close
  \open
  \hypo {7} {r}
  \have {8} {(p \wedge q) \vee r} \oi{7}
  \close
  \have {9} {(p \wedge q) \vee r} \oe{3,4-6,7-8}
  \close
  \have {10} {(p \wedge (q \vee r)) \to ((p \wedge q) \vee r)} \ii{1-9}
\end{nd}$
\end{center}
```

No \( \rulename{RAA} \) is used: the boxes close by \( \rulename{\vee E} \) and \( \rulename{{\to}I} \). The tools: truth values (@def-truth-value) for the first question, the search of Chapter 3 for the second. The look-alike tool, completeness, answers only "derivable with all the rules".
:::

<!-- dependency ledger
lem-connective-rows (proof): De Morgan (b) and (c) are derived without RAA | F1.2 prp-de-morgan (the sentence after its derivations says so; cited in the proof)
lem-connective-rows (proof): prp-vacuous-implication and exm-double-negation-introduction come before RAA (F1.2 §01, F1.2 §02) | F1.2 section order
lem-truth-table-line (proof): every atom of an immediate part is an atom of the whole formula | the recursive definition of the set of atoms, F1.3 §03 (after thm-structural-recursion)
lem-truth-table-line (proof): v(phi^v) = T; the value clauses of each connective | def-truth-value (cited)
lem-atom-splitting (proof): pasted lines keep availability inside a new box | inline, as in lem-weakening-cut
thm-completeness (proof): a finite list of formulas contains only finitely many atoms | inline (each formula has finitely many symbols)
thm-completeness (proof): integer arithmetic 1 <= n - m <= n from 0 <= m <= n - 1 | school arithmetic
thm-completeness (proof): a valuation may be changed at one atom and stays a valuation; at least one valuation exists | def-valuation (cited)
cor-derivable-iff-valid (proof): 2^n rows for n atoms | def-truth-table, lem-coincidence (F1.3 §04)
exm-completeness-run (example): the search derivation of F1.2 has 13 lines | exr-finding-derivations-c2 solution (cited)
exr-completeness-b3 (solution): no derivation of the sequent avoids RAA | stated without proof and marked so; nothing depends on it
exr-completeness-b3 (solution): pasting the two cited rows gives 22 lines in primitive rules | inline count: the non-premise lines of the (<->2) and (<->1) derivations, 7 and 5, replace lines 4 and 9, so 12 + 6 + 4 = 22
cor-derivable-iff-valid (claim): the fold after it, compactness for infinite premise sets | proved in the optional F1.3 §10 (thm-compactness); nothing in the core depends on it
lem-weakening-cut (claim): the recall: weakening, cut, chaining | lem-weakening-cut (F1.2 §03), cited
lem-connective-rows (claim): the tagged tables: each tag is a sequent of the lemma, and where two fit, the one the proof of lem-truth-table-line uses | inline; checked by verify/ch04/lem-connective-rows.py
exm-completeness-run (example): the case-split tree's line ranges and rules match the printed 20-line derivation | verify/ch04/exm-completeness-run.py
exr-completeness-b2 (solution): the case-split tree's line ranges match the printed 21-line derivation | verify/ch04/exr-completeness-b2.py
thm-completeness (claim): consistent and satisfiable coincide | thm-soundness (F1.3 §07, in prose), thm-completeness (this section); def-inconsistent-set (F1.7 §02), def-satisfiable (F1.3 §05)
thm-completeness (claim): the fold "Why two definitions of 'follows' are enough": informal inference squeezed between |- and |= | an argument about an informal notion, marked as such; nothing depends on it
cor-derivable-iff-valid (claim): the two-columns table: each row's entries | the cited labels; prp-search-decides (F1.3 §06); Section 4.5's structural properties (F1.3 §05, fold), recalled
def-rule-taut (claim): a TAUT line expands into primitive rules; soundness holds for derivations with TAUT | cor-derivable-iff-valid (this section), def-derived-rule, lem-weakening-cut (F1.2 §03)
exm-taut-step (example): the premise is true only at p = T, q = F; the twelve-line derivation | verify/ch04/exm-taut-step.py (truth table; tools/check_fitch.py on a capital-letter copy)
def-rule-taut (example): the TAUT Quick check and the Not-allowed rows | verify/ch04/exm-taut-step.py
exr-completeness-a2 (solution): drill (g), (h), (i), (k) | verify/ch04/exr-completeness-a2.py
exr-completeness-b4 (solution): both derivations; the equivalence of (c) | verify/ch04/exr-completeness-b4.py
exr-completeness-b5 (solution): the verdicts; (a)'s derivation | verify/ch04/exr-completeness-b5.py
exr-completeness-b5 (solution): (b) unsatisfiable by a closed search, hence inconsistent | prp-search-decides (F1.3 §06), thm-completeness (this section), cited
exr-completeness-c4 (solution): the or-as-and reading: every primitive rule except or-I is sound; the two countervaluations | verify/ch04/exr-completeness-c4.py (exhaustive)
exr-completeness-c4 (solution): prp-excluded-middle is derived with or-I; De Morgan (c) gives the (and 2), (and 3) rows | F1.2 §05 (prp-excluded-middle, prp-de-morgan), cited
exr-completeness-c5 (solution): each case's sequents are derivable | verify/ch04/exr-completeness-c5.py (one tools/check_fitch.py derivation per case, schematic letters)
exr-completeness-c5 (solution): the search rules; a finished tree with no open branch has every branch closed | prp-search-decides, the table of search rules (F1.3 §06), cited
exr-normal-forms-c3 (solution): moved here with its label from the normal-forms section; content unchanged | verify/ch04/exr-normal-forms-c3.py
exr-normal-forms-r1 (solution): moved here with its label from the normal-forms section; content unchanged | verify/ch04/exr-normal-forms-r1.py
exr-normal-forms-r2 (solution): an integer is odd exactly when it is not even | school fact about integers (F2.2, promised; STATUS row from F1.1: every integer is even or odd, and not both)
exr-normal-forms-r3 (solution): moved here with its label from the normal-forms section; content unchanged | verify/ch04/exr-normal-forms-r3.py
-->
