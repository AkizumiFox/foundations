# Stages of Knowledge: Kripke Models

This section is optional, and nothing outside it depends on it. Section 8.7 named several classical laws that have no derivation without \( \rulename{RAA} \). For two of them, excluded middle and double-negation elimination, Chapter 4's optional @thm-raa-independent gave a proof by a three-valued reading; for the rest, Section 8.7 states the fact and points here. Truth tables cannot show it: every row makes \( p \vee \neg p \) true. Here is a reading that covers them all. A statement is not true or false once and for all, but *known* or *not yet known* at a stage of an inquiry that grows. The rules without \( \rulename{RAA} \) are sound for this reading, and \( \rulename{RAA} \) is not; two or three stages then suffice to show which laws need it.

## Stages of knowledge

An inquiry passes through stages. At each stage some atomic statements are known: established, never to be withdrawn. From a stage, the inquiry may go on in several ways, to later stages where more is known. Nobody knows which way it will go. The atomic statements are the letters of Chapter 4's formulas (@def-formula), its atoms, and the formulas of this section are those formulas: letters, \( \bot \), and the connectives \( \neg \), \( \wedge \), \( \vee \), \( \to \), \( \leftrightarrow \).

::: {#def-kripke-model}
[Kripke Model]

A **Kripke model** consists of:

- a finite non-empty set of **stages**;
- for each stage \( w \), a set of stages **reachable** from \( w \) (written \( w \le w' \)), such that \( w \le w \) for every stage, and \( w \le w' \) and \( w' \le w'' \) give \( w \le w'' \);
- for each stage \( w \), a set of letters **known at** \( w \), such that a letter known at \( w \) is known at every stage reachable from \( w \).
:::

We draw a model as dots for the stages, with an arrow from a stage to each stage that comes directly after it. A stage is reachable from \( w \) when it can be reached by following arrows, none or several; so \( w \) reaches itself, and arrows are never drawn for that. Beside each dot stands the set of letters known there.

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=below:$w_0$, label=right:$\emptyset$] (a) at (0,0) {};
  \node[elt, label=above:$w_1$, label=right:$\{p\}$] (b) at (0,1.6) {};
  \draw[rel] (a) -- (b);
\end{tikzpicture}
\end{center}
```

The model \( M_1 \): at \( w_0 \) nothing is known yet; at the later stage \( w_1 \), \( p \) is known.

## Forcing

What a stage knows about a compound formula is computed from its parts, as a row computes a truth value, except that some connectives look ahead to later stages.

::: {#def-forcing}
[Forcing]

Let \( w \) be a stage of a Kripke model. **\( w \) forces** a formula \( \varphi \), written \( w \Vdash \varphi \), as follows; \( w \nVdash \varphi \) says that it does not. The definition is a recursion on \( \varphi \) (@thm-structural-recursion) that defines, for each formula, the set of stages that force it; clauses (K5) and (K6) need the sets of its parts, at other stages.

::: {.enumerate options="label=(K\arabic*)"}
1. \( w \Vdash p \), for a letter \( p \), if \( p \) is known at \( w \);
2. \( w \Vdash \bot \) never;
3. \( w \Vdash \varphi \wedge \psi \) if \( w \Vdash \varphi \) and \( w \Vdash \psi \);
4. \( w \Vdash \varphi \vee \psi \) if \( w \Vdash \varphi \) or \( w \Vdash \psi \);
5. \( w \Vdash \varphi \to \psi \) if every stage \( w' \) reachable from \( w \) with \( w' \Vdash \varphi \) has \( w' \Vdash \psi \);
6. \( w \Vdash \neg\varphi \) if no stage reachable from \( w \) forces \( \varphi \);
7. \( w \Vdash \varphi \leftrightarrow \psi \) if \( w \Vdash \varphi \to \psi \) and \( w \Vdash \psi \to \varphi \).
:::

A stage **refutes** a sequent \( \Gamma \vdash \psi \) if it forces every formula of \( \Gamma \) and does not force \( \psi \).
:::

*In words:* a conjunction or a disjunction is decided at the stage itself, and a disjunction is forced only when one of its sides is: the inquiry must already know which. An implication and a negation look ahead. To force \( \varphi \to \psi \) is to know that, however the inquiry goes on, \( \psi \) will be known whenever \( \varphi \) is. To force \( \neg\varphi \) is to know that \( \varphi \) will never be known. Not forcing \( \varphi \) is weaker than forcing \( \neg\varphi \).

A model with **one stage** is a row of a truth table. With one stage, the stages reachable from \( w \) are \( w \) alone, so (K5) says "\( \varphi \) is not forced, or \( \psi \) is", and (K6) says "\( \varphi \) is not forced": forcing becomes Chapter 4's truth (@def-truth-value). Kripke models are rows that can grow.

A stage that refutes \( \Gamma \vdash \psi \) forces every member of \( \Gamma \) and not \( \psi \), which is weaker than forcing \( \neg\psi \). It is Section 1.1's counterexample set, read at a stage: where truth tables make \( \neg\psi \) true, a stage only fails to know \( \psi \).

::: {.check}
In a one-stage model in which \( p \) is not known, does the stage force \( \neg p \)? Does it force \( p \vee \neg p \)?
:::

::: {.solution}
Yes to both. The only stage reachable is the stage itself, which does not force \( p \), so (K6) gives \( \neg p \), and (K4) gives \( p \vee \neg p \). One stage is one row.
:::

## A first countermodel

::: {#exm-two-stage-model}
[Two stages refute excluded middle]

In \( M_1 \), decide whether \( w_0 \) forces \( p \), \( \neg p \), \( p \vee \neg p \), \( \neg\neg p \) and \( \neg\neg p \to p \).
:::

::: {.solution}
- \( p \) is not known at \( w_0 \), so \( w_0 \nVdash p \) (K1).
- \( w_1 \) is reachable from \( w_0 \) and forces \( p \), so \( w_0 \nVdash \neg p \) (K6).
- Hence \( w_0 \nVdash p \vee \neg p \) (K4): \( w_0 \) refutes \( \vdash p \vee \neg p \).
- Next, \( \neg\neg p \). No stage reachable from \( w_0 \) forces \( \neg p \): not \( w_0 \), as just shown, and not \( w_1 \), which forces \( p \). So \( w_0 \Vdash \neg\neg p \) (K6).
- So \( w_0 \) forces \( \neg\neg p \) and not \( p \): it refutes \( \neg\neg p \vdash p \), and by (K5), applied with \( w' = w_0 \), \( w_0 \nVdash \neg\neg p \to p \).

At \( w_0 \) the inquiry knows that \( p \) cannot be refuted, since \( p \) becomes known later on every way it can go, but it does not yet know \( p \). Excluded middle asks it to know now which of \( p \) and \( \neg p \) holds.
:::

## Knowledge persists

Letters stay known by the definition of a Kripke model. The same holds for every formula.

::: {#lem-heredity}
[Heredity]

In every Kripke model, if \( w \Vdash \varphi \) and \( w \le w' \), then \( w' \Vdash \varphi \).
:::

*In words: what a stage forces, every later stage forces.* The proof is a structural induction on \( \varphi \) (@thm-structural-induction); it is in the fold.

::: {.second-reading title="The proof of heredity"}
::: {.proof}
We prove, by @thm-structural-induction, that every formula \( \varphi \) has the property: for all stages \( w \le w' \) of every Kripke model, \( w \Vdash \varphi \) gives \( w' \Vdash \varphi \).

*Letters.* A letter forced at \( w \) is known at \( w \) (K1), hence known at \( w' \) by the condition on known letters in @def-kripke-model, hence forced at \( w' \).

*\( \bot \).* No stage forces it (K2), so there is nothing to show.

*\( \wedge \) and \( \vee \).* If \( w \Vdash \varphi \wedge \psi \), then \( w \) forces both parts (K3), so \( w' \) forces both by the induction hypothesis, and \( w' \Vdash \varphi \wedge \psi \). For \( \vee \), \( w \) forces one part (K4), and \( w' \) forces the same part by the induction hypothesis.

*\( \to \).* Let \( w \Vdash \varphi \to \psi \), and let \( w'' \) be reachable from \( w' \) with \( w'' \Vdash \varphi \). Since \( w \le w' \) and \( w' \le w'' \), transitivity gives \( w \le w'' \), so \( w'' \Vdash \psi \) by (K5) at \( w \). Hence \( w' \Vdash \varphi \to \psi \) by (K5). No induction hypothesis is used.

*\( \neg \).* The same: every stage reachable from \( w' \) is reachable from \( w \), and none of those forces \( \varphi \) (K6), so \( w' \Vdash \neg\varphi \).

*\( \leftrightarrow \).* By (K7), \( w \) forces the two implications, so \( w' \) forces both by the case \( \to \), and \( w' \Vdash \varphi \leftrightarrow \psi \).

Every clause of @def-formula is covered, so every formula has the property. This proves the lemma.
:::
:::

::: {.check}
A stage \( w \) forces \( \neg\varphi \), and \( w' \) is reachable from \( w \). Why does \( w' \) force \( \neg\varphi \), whatever \( \varphi \) is?
:::

::: {.solution}
\( w \Vdash \neg\varphi \) says that no stage reachable from \( w \) forces \( \varphi \). The stages reachable from \( w' \) are among those, by transitivity, so none of them forces \( \varphi \) either. Nothing is assumed about \( \varphi \) itself.
:::

## The rules without RAA are sound for stages

::: {#thm-kripke-soundness}
[Soundness without RAA]

Let \( \Gamma \) be a list of formulas and \( \psi \) a formula. If \( \Gamma \vdash \psi \) by a derivation every line of which is a formula of @def-formula, in which no line uses \( \rulename{RAA} \) or TAUT, nor a derived rule or cited result whose derivation uses one of them or a line outside @def-formula, then every stage of every Kripke model that forces every formula of \( \Gamma \) forces \( \psi \).
:::

*In words: a derivation without \( \rulename{RAA} \) never leads from what a stage knows to what it does not know.*

TAUT (Section 4.8) is not among the rules here: it is licensed by completeness, whose proof uses \( \rulename{LEM} \) (Section 8.7), so a derivation with a TAUT line is not a derivation without \( \rulename{RAA} \).

The proof is Chapter 4's proof of @thm-soundness, Steps 1–4, with "every valuation making the context true" replaced by "every stage forcing the context". Each rule's case, in one line:

| Rule | Why its case holds at a stage \( w \) that forces the context |
|---|---|
| \( \rulename{R} \) | the cited line itself, forced at \( w \) |
| \( \rulename{\wedge I} \), \( \rulename{\wedge E} \), \( \rulename{\vee I} \), \( \rulename{{\leftrightarrow}E} \) | the clause (K3), (K4) or (K7) at \( w \) itself, with (K5) at \( w' = w \) for \( \rulename{{\leftrightarrow}E} \) |
| \( \rulename{{\to}E} \), \( \rulename{\neg E} \) | (K5) or (K6), applied at \( w' = w \), which is reachable from \( w \); for \( \rulename{\neg E} \) no stage forces both cited lines, so there is nothing to show |
| \( \rulename{\bot E} \) | no stage forces \( \bot \), so there is nothing to show |
| \( \rulename{\vee E} \) | \( w \) forces one side, by (K4); the box of that side ends in its last line, forced at \( w \) |
| \( \rulename{{\to}I} \), \( \rulename{\neg I} \), \( \rulename{{\leftrightarrow}I} \) | a later stage \( w' \) forces the context too, **by heredity**, so the box applies at \( w' \) |
| \( \rulename{RAA} \) | **fails**: its box on \( \neg\varphi \) shows only that no stage reachable from \( w \) forces \( \neg\varphi \), that is, \( w \Vdash \neg\neg\varphi \); in \( M_1 \), \( w_0 \) forces \( \neg\neg p \) and not \( p \) |

::: {.second-reading title="The proof, case by case"}
::: {.proof}
**Step 1 (reduction to primitive rules).** As in Step 1 of the proof of @thm-soundness, a derived rule or cited result derived without \( \rulename{RAA} \) and TAUT abbreviates a pasted derivation in the propositional primitive rules (Chapters 1 and 2) other than \( \rulename{RAA} \). So fix a derivation of \( \psi \) whose premises all belong to \( \Gamma \) and which uses only those rules, with lines \( 1, \dots, n \); let \( \varphi_k \) be the formula on line \( k \) and \( \Gamma_k \) its context.

**Step 2 (the induction).** For \( k \in \nN \), let \( S(k) \) be the statement: *if \( 1 \le k \le n \), then every stage of every Kripke model that forces every formula of \( \Gamma_k \) forces \( \varphi_k \).* We prove \( S(k) \) for every \( k \) by @thm-strong-induction. Let \( 1 \le k \le n \) (otherwise there is nothing to prove), assume \( S(j) \) for every \( j < k \), and let \( w \) force every formula of \( \Gamma_k \). Every line and box that line \( k \) cites lies before it (@def-derivation), so the induction hypothesis holds for each cited line and for the last line of each cited box.

**Step 3 (the cases).** *Premises and assumptions:* \( \varphi_k \) belongs to \( \Gamma_k \), so \( w \) forces it. *One-step rules:* a cited line \( i \) is available at line \( k \), so \( \Gamma_i \subseteq \Gamma_k \) (@lem-context-inclusion (a)), and the hypothesis gives \( w \Vdash \varphi_i \). Then \( \rulename{R} \) is the hypothesis for the cited line, and \( \rulename{\wedge I} \), \( \rulename{\wedge E} \) and \( \rulename{\vee I} \) follow from (K3) and (K4) at \( w \). For \( \rulename{{\to}E} \), \( w \Vdash \varphi \to \psi \) and \( w \Vdash \varphi \), and (K5) with \( w' = w \) gives \( w \Vdash \psi \); \( \rulename{{\leftrightarrow}E} \) is the same after (K7). For \( \rulename{\neg E} \), \( w \Vdash \neg\varphi \) would say by (K6) that \( w \), reachable from itself, does not force \( \varphi \), against \( w \Vdash \varphi \); so no stage forces \( \Gamma_k \), and there is nothing to show. For \( \rulename{\bot E} \), \( w \Vdash \bot \) is impossible by (K2), and again there is nothing to show.

*Box rules:* if line \( k \) cites the box from line \( a \) to line \( b \), then \( \Gamma_b = \Gamma_k, \varphi_a \) (@lem-context-inclusion (b)), so the hypothesis for line \( b \) says that every stage forcing \( \Gamma_k \) and \( \varphi_a \) forces \( \varphi_b \). For \( \rulename{{\to}I} \), line \( k \) is \( \varphi \to \psi \). Let \( w' \) be reachable from \( w \) with \( w' \Vdash \varphi \). By @lem-heredity, \( w' \) forces every formula of \( \Gamma_k \), so it forces \( \Gamma_k \) and \( \varphi \), and hence \( \psi \). So \( w \Vdash \varphi \to \psi \) by (K5). \( \rulename{\neg I} \) is the same with \( \psi = \bot \): a stage \( w' \) reachable from \( w \) that forced \( \varphi \) would force \( \bot \), against (K2), so none does, and \( w \Vdash \neg\varphi \) by (K6). \( \rulename{{\leftrightarrow}I} \) is two cases of \( \rulename{{\to}I} \), joined by (K7). For \( \rulename{\vee E} \), \( w \Vdash \varphi \vee \psi \) by the hypothesis for the cited line, so \( w \) forces \( \varphi \) or \( \psi \) (K4); if \( \varphi \), then \( w \) forces \( \Gamma_k \) and \( \varphi \), and the first box gives \( w \Vdash \chi \); if \( \psi \), the second box does. For \( \rulename{RAA} \) the case fails, as the table says, and no derivation here uses it.

So \( S(k) \) holds, and by @thm-strong-induction every line \( k \) satisfies it.

**Step 4 (the last line).** The last line lies in no box (@def-derivation), so its context \( \Gamma_n \) consists of premises only, each of which belongs to \( \Gamma \) (@def-derivable). A stage forcing every formula of \( \Gamma \) forces every formula of \( \Gamma_n \), so by Steps 2 and 3 it forces \( \varphi_n = \psi \). This proves the theorem.
:::
:::

::: {#cor-kripke-countermodel}
[Kripke Countermodel]

If some stage of some Kripke model refutes \( \Gamma \vdash \psi \), then \( \Gamma \vdash \psi \) has no derivation without \( \rulename{RAA} \) in the propositional rules.
:::

::: {.proof}
Suppose it had one. By @thm-kripke-soundness the stage would force \( \psi \), and it does not; so it has none.
:::

::: {.check}
Which case of the proof fails for \( \rulename{RAA} \), and which stage of \( M_1 \) shows that it must?
:::

::: {.solution}
\( \rulename{RAA} \)'s own case: its box assumes \( \neg\varphi \) and the rule writes \( \varphi \). \( w_0 \) forces \( \neg\neg p \) and not \( p \). If \( \rulename{RAA} \) were sound for stages, the derivation of \( \neg\neg p \vdash p \) (@prp-double-negation (b)) would make \( w_0 \) force \( p \).
:::

## Two branches

::: {#exm-three-stage-model}
[A fork]

In the model \( M_2 \) the inquiry can go two ways: one learns \( p \), the other \( q \).

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=below:$w_0$, label=right:$\emptyset$] (a) at (0,0) {};
  \node[elt, label=above:$w_1$, label=left:$\{p\}$] (b) at (-1.2,1.6) {};
  \node[elt, label=above:$w_2$, label=right:$\{q\}$] (c) at (1.2,1.6) {};
  \draw[rel] (a) -- (b);
  \draw[rel] (a) -- (c);
\end{tikzpicture}
\end{center}
```

Show that \( w_0 \) refutes \( \vdash (p \to q) \vee (q \to p) \) and \( \neg(p \wedge q) \vdash \neg p \vee \neg q \).
:::

::: {.solution}
- \( w_1 \) is reachable from \( w_0 \), forces \( p \) and does not force \( q \), so \( w_0 \nVdash p \to q \) (K5). Likewise \( w_2 \) gives \( w_0 \nVdash q \to p \). By (K4), \( w_0 \) does not force the disjunction.
- No stage forces both \( p \) and \( q \), so \( w_0 \Vdash \neg(p \wedge q) \) (K6).
- \( w_1 \) forces \( p \), so \( w_0 \nVdash \neg p \); \( w_2 \) forces \( q \), so \( w_0 \nVdash \neg q \). Hence \( w_0 \nVdash \neg p \vee \neg q \).
- By @cor-kripke-countermodel, neither \( \vdash (p \to q) \vee (q \to p) \) nor \( \neg(p \wedge q) \vdash \neg p \vee \neg q \) has a derivation without \( \rulename{RAA} \).
:::

Classically each is derivable (Section 2.5, and @cor-derivable-iff-valid for the first, a tautology). The branch is what defeats them. At \( w_0 \) the inquiry knows that \( p \) and \( q \) will never both be known, but not which one will fail.

## What two or three stages settle

Here is the propositional right column of the table in Section 8.7, "Which laws survive without RAA", each sequent with a stage that refutes it. Two more models are described in words: \( M_3 \) has stages \( w_0 \to w_1 \), nothing known at \( w_0 \), and \( p \) and \( q \) known at \( w_1 \); \( M_4 \) has stages \( w_0 \to w_1 \), \( p \) known at both, and \( q \) known at \( w_1 \) only.

| Sequent (letters \( p \), \( q \)) | A refuting stage |
|---|---|
| \( \vdash p \vee \neg p \); \( \neg\neg p \vdash p \); \( \vdash \neg\neg p \to p \) | \( w_0 \) of \( M_1 \) (@exm-two-stage-model) |
| \( \vdash ((p \to q) \to p) \to p \) | \( w_0 \) of \( M_1 \): no stage forces \( p \to q \), so both stages force \( (p \to q) \to p \); \( w_0 \nVdash p \) |
| \( \neg(p \to q) \vdash p \wedge \neg q \) | \( w_0 \) of \( M_1 \): no stage forces \( p \to q \), so \( w_0 \Vdash \neg(p \to q) \); \( w_0 \nVdash p \) |
| \( (p \to q) \to q \vdash p \vee q \) (Section 8.7, R3) | \( w_0 \) of \( M_1 \): as above, both stages force \( (p \to q) \to q \); \( w_0 \) forces neither \( p \) nor \( q \) |
| \( p \to q \vdash \neg p \vee q \) | \( w_0 \) of \( M_3 \): \( w_0 \Vdash p \to q \); \( w_0 \nVdash \neg p \) since \( w_1 \Vdash p \), and \( w_0 \nVdash q \) |
| \( \neg q \to \neg p \vdash p \to q \) | \( w_0 \) of \( M_4 \): no stage forces \( \neg q \), so \( w_0 \Vdash \neg q \to \neg p \); \( w_0 \) forces \( p \) and not \( q \) |
| \( \vdash (p \to q) \vee (q \to p) \); \( \neg(p \wedge q) \vdash \neg p \vee \neg q \) | \( w_0 \) of \( M_2 \) (@exm-three-stage-model) |

With @cor-kripke-countermodel, each row proves that the sequent has no derivation without \( \rulename{RAA} \) in the propositional rules; that the rules for \( \forall \), \( \exists \) and \( = \) do not change this is stated without proof (Section 8.7). This covers every propositional entry of Section 8.7's right column, and the claims stated without proof in its Exercises B1 and R3.

## Searching for a countermodel

How were these models found? Here is the search for \( (p \to q) \to q \vdash p \vee q \), run backwards from what must fail, in the manner of Section 4.6's search for a refuting row.

- Start with a stage \( w_0 \) that must not force \( p \vee q \). So neither \( p \) nor \( q \) is known there.
- It must force \( (p \to q) \to q \): every later stage that forces \( p \to q \) must force \( q \). The cheapest way is to make sure no stage forces \( p \to q \).
- \( w_0 \) itself must then fail \( p \to q \), so some stage reachable from it forces \( p \) and not \( q \). Add \( w_1 \) after \( w_0 \), with \( p \) known.
- Check every clause at both stages: this is \( M_1 \).

In general:

- to refute a disjunction at \( w \), refute both sides at \( w \) itself;
- to refute \( \varphi \to \psi \) or \( \neg\varphi \) at \( w \), add a later stage that forces \( \varphi \) (and, for \( \to \), not \( \psi \));
- keep letters known once known.

The search is a guide, not a decision procedure as stated here.

::: {.remark}
Three facts, stated without proof.

- The converse of @thm-kripke-soundness holds: a sequent forced at every stage of every Kripke model that forces its premises has a derivation without \( \rulename{RAA} \). This is completeness for this semantics.
- From it, by placing a new first stage below two countermodels, follows the **disjunction property**: if \( \vdash \varphi \vee \psi \) without \( \rulename{RAA} \), then \( \vdash \varphi \) or \( \vdash \psi \) without \( \rulename{RAA} \), the BHK clause for "or" made a theorem about derivations.
- Kripke models extend to the quantifiers, with a domain at each stage that may grow. In them \( \neg\forall x\, \varphi \vdash \exists x\, \neg\varphi \) and the two passage directions of Section 8.7's table can be refuted.

Nothing in this book depends on these facts.
:::

::: {.warning}
[Not allowed: misreadings of forcing]

Each sentence below is wrong; the tag names the clause it misreads.

- "\( w \nVdash p \), so \( w \Vdash \neg p \)": (K6) looks at every stage reachable from \( w \); in \( M_1 \), \( w_0 \) forces neither \( p \) nor \( \neg p \).
- "\( w \Vdash \varphi \to \psi \), because \( w \nVdash \varphi \)": (K5) looks at every later stage, not only at \( w \).
- "\( w \Vdash \varphi \vee \psi \), because every stage reachable from \( w \), other than \( w \) itself, forces \( \varphi \) or \( \psi \)": (K4) is decided at \( w \) itself; in \( M_2 \), every stage reachable from \( w_0 \) other than \( w_0 \) forces \( p \) or \( q \), and \( w_0 \) forces neither.
- "A picture with \( p \) known at \( w_0 \) and not at a later \( w_1 \)": it is not a Kripke model, since a known letter stays known (@def-kripke-model).
:::

## Exercises

### A. Check your understanding

::: {#exr-kripke-models-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. In \( M_1 \), does \( w_1 \) force \( \neg\neg p \to p \)?
2. Why is a one-stage Kripke model a row of a truth table?
3. True or false: if \( w \) does not force \( \varphi \), then \( w \) forces \( \neg\varphi \).
4. Which rule's case fails in the proof of @thm-kripke-soundness, and how does \( M_1 \) show that it must fail?
:::
:::

::: {.solution}
(a) Yes. The only stage reachable from \( w_1 \) is \( w_1 \), which forces \( p \), so it forces the implication by (K5).

(b) With one stage, (K5) and (K6) look only at that stage, so the clauses become those of @def-truth-value, with "forced" for "true".

(c) False: \( w_0 \) of \( M_1 \), with \( \varphi = p \), forces neither \( p \) nor \( \neg p \).

(d) \( \rulename{RAA} \)'s. \( w_0 \) forces \( \neg\neg p \) and not \( p \), but \( \neg\neg p \vdash p \) is derived with \( \rulename{RAA} \); if \( \rulename{RAA} \)'s case held, \( w_0 \) would force \( p \).
:::

::: {#exr-kripke-models-a2}
[A2: Drill]

Decide each in a line, with the clause you use. \( M_1 \) and \( M_2 \) are the models of the text. \( M_5 \) is the chain \( w_0 \to w_1 \to w_2 \), with nothing known at \( w_0 \), \( p \) known at \( w_1 \), and \( p \), \( q \) known at \( w_2 \).

::: {.enumerate options="label=(\alph*)"}
1. \( M_1 \): does \( w_1 \) force \( \neg p \)?
2. \( M_1 \), with \( q \) known nowhere: does \( w_0 \) force \( \neg q \)?
3. \( M_2 \): does \( w_0 \) force \( p \vee q \)?
4. \( M_2 \): does \( w_1 \) force \( \neg q \)?
5. \( M_5 \): does \( w_0 \) force \( p \to q \)?
6. \( M_5 \): does \( w_1 \) force \( \neg\neg q \)?
7. Is this a Kripke model: \( w_0 \to w_1 \), with \( p \) known at \( w_0 \) and not at \( w_1 \)?
8. In \( M_1 \), a student says "\( w_0 \) forces \( \neg p \), because \( p \) is not known at \( w_0 \)". What is wrong?
9. \( M_2 \): does \( w_0 \) force \( \neg p \to q \)?
10. \( M_5 \): does \( w_0 \) force \( q \vee \neg q \)?
11. \( M_5 \): does \( w_0 \) force \( q \to p \)?
12. Can a one-stage model refute \( \neg\neg p \vdash p \)?
:::
:::

::: {.solution}
(a) No: \( w_1 \) is reachable from itself and forces \( p \) (K6).

(b) Yes: no stage reachable from \( w_0 \) forces \( q \) (K6).

(c) No: neither letter is known at \( w_0 \) (K4).

(d) Yes: the only stage reachable from \( w_1 \) is \( w_1 \), where \( q \) is not known (K6).

(e) No: \( w_1 \) is reachable, forces \( p \), and does not force \( q \) (K5).

(f) Yes. The stages reachable from \( w_1 \) are \( w_1 \) and \( w_2 \); neither forces \( \neg q \), since \( w_2 \) forces \( q \) and is reachable from both (K6). And \( w_1 \nVdash q \), so \( \neg\neg q \) is forced where \( q \) is not.

(g) No: a letter known at \( w_0 \) must be known at every stage reachable from it (@def-kripke-model).

(h) (K6) needs \( p \) to fail at every reachable stage, and \( w_1 \) forces \( p \).

(i) Yes (K5). Of the stages reachable from \( w_0 \), only \( w_2 \) forces \( \neg p \) (\( w_0 \) and \( w_1 \) reach \( w_1 \), which knows \( p \)), and \( w_2 \) forces \( q \).

(j) No: \( q \) is not known at \( w_0 \), and \( w_2 \), reachable from \( w_0 \), forces \( q \), so \( w_0 \nVdash \neg q \) (K4, K6).

(k) Yes: the only stage that forces \( q \) is \( w_2 \), which forces \( p \) (K5).

(l) No. At a single stage forcing is truth, and \( \neg\neg p \) is true exactly when \( p \) is. A refutation needs a later stage.
:::

### B. Practice

::: {#exr-kripke-models-b1}
[B1: A chain of three stages]

Let \( M_6 \) be the chain \( w_0 \to w_1 \to w_2 \), with nothing known at \( w_0 \), \( q \) known at \( w_1 \), and \( p \) and \( q \) known at \( w_2 \).

::: {.enumerate options="label=(\alph*)"}
1. Decide whether \( w_0 \) forces \( \neg\neg p \), \( p \vee \neg p \), \( q \to p \), \( (q \to p) \vee (p \to q) \) and \( \neg p \to \neg q \).
2. Which sequents among \( \vdash p \vee \neg p \), \( \neg\neg p \vdash p \) and \( \vdash (p \to q) \vee (q \to p) \) does \( w_0 \) refute?
3. A **chain** is a Kripke model whose stages can be listed \( u_0, \dots, u_m \) so that \( u_i \le u_j \) exactly when \( i \le j \). Show that no stage of a chain refutes \( \vdash (p \to q) \vee (q \to p) \).
:::
:::

::: {.solution}
(a)

- \( \neg\neg p \): yes. Every stage reachable from \( w_0 \) reaches \( w_2 \), which forces \( p \), so none forces \( \neg p \) (K6).
- \( p \vee \neg p \): no. \( p \) is not known at \( w_0 \), and \( w_0 \nVdash \neg p \) because of \( w_2 \) (K4).
- \( q \to p \): no. \( w_1 \) forces \( q \) and not \( p \) (K5).
- \( (q \to p) \vee (p \to q) \): yes. The only stage forcing \( p \) is \( w_2 \), which forces \( q \), so \( w_0 \Vdash p \to q \) (K5), and (K4) gives the disjunction.
- \( \neg p \to \neg q \): yes. No stage reachable from \( w_0 \) forces \( \neg p \), so the implication holds with nothing to check (K5).

(b) \( \vdash p \vee \neg p \) and \( \neg\neg p \vdash p \), since \( w_0 \) forces \( \neg\neg p \) and not \( p \). Not \( \vdash (p \to q) \vee (q \to p) \), by (a).

(c) Suppose some stage \( w \) of a chain refuted it, that is, forced neither \( p \to q \) nor \( q \to p \). By (K5), some \( u \) reachable from \( w \) forces \( p \) and not \( q \), and some \( v \) reachable from \( w \) forces \( q \) and not \( p \). In a chain, \( u \le v \) or \( v \le u \). If \( u \le v \), then \( v \) forces \( p \), since letters stay known, a contradiction. If \( v \le u \), then \( u \) forces \( q \), a contradiction. So no stage of a chain refutes it, and the branch of \( M_2 \) is needed.

**Marking scheme.** (10 points)
- 5: (a), one per formula, each with its clause.
- 2: (b).
- 3: (c), the two orders of \( u \), \( v \), each with persistence of letters.

Fatal errors (0 for the step): deciding (K5) or (K6) at \( w_0 \) alone; in (c), checking one chain only.
:::

::: {#exr-kripke-models-b2}
[B2: Derive without RAA, or break with a Kripke model]

For each claim, either derive it without \( \rulename{RAA} \) and without TAUT (and without results derived with \( \rulename{RAA} \)), or give a stage of a Kripke model that refutes it.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg\neg(p \wedge q) \vdash \neg\neg p \wedge \neg\neg q \).
2. \( \neg\neg p \wedge \neg\neg q \vdash \neg\neg(p \wedge q) \).
3. \( \neg\neg(p \vee q) \vdash \neg\neg p \vee \neg\neg q \).
4. \( (p \to q) \to p \vdash \neg\neg p \).
5. \( \neg p \to p \vdash p \).
6. \( (p \vee q) \wedge \neg p \vdash q \).
7. \( (p \to q) \wedge (\neg p \to q) \vdash q \).
:::
:::

::: {.solution}
The verdict comes first in each part.

(a) **Derive.** Each conjunct is a negation, so each takes a \( \rulename{\neg I} \) box, whose clash builds \( \neg(p \wedge q) \) against the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg (p \wedge q)}
  \open
  \hypo {2} {\neg p}
  \open
  \hypo {3} {p \wedge q}
  \have {4} {p} \ae{3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg (p \wedge q)} \ni{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {\neg\neg p} \ni{2-7}
  \open
  \hypo {9} {\neg q}
  \open
  \hypo {10} {p \wedge q}
  \have {11} {q} \ae{10}
  \have {12} {\bot} \ne{11,9}
  \close
  \have {13} {\neg (p \wedge q)} \ni{10-12}
  \have {14} {\bot} \ne{13,1}
  \close
  \have {15} {\neg\neg q} \ni{9-14}
  \have {16} {\neg\neg p \wedge \neg\neg q} \ai{8,15}
\end{nd}$
\end{center}
```

(b) **Derive.** A \( \rulename{\neg I} \) box on \( \neg(p \wedge q) \); inside it, \( \neg q \) and then \( \neg p \) are built, each clashing with a conjunct of the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg p \wedge \neg\neg q}
  \have {2} {\neg\neg p} \ae{1}
  \have {3} {\neg\neg q} \ae{1}
  \open
  \hypo {4} {\neg (p \wedge q)}
  \open
  \hypo {5} {p}
  \open
  \hypo {6} {q}
  \have {7} {p \wedge q} \ai{5,6}
  \have {8} {\bot} \ne{7,4}
  \close
  \have {9} {\neg q} \ni{6-8}
  \have {10} {\bot} \ne{9,3}
  \close
  \have {11} {\neg p} \ni{5-10}
  \have {12} {\bot} \ne{11,2}
  \close
  \have {13} {\neg\neg (p \wedge q)} \ni{4-12}
\end{nd}$
\end{center}
```

(c) **Break**, at \( w_0 \) of \( M_2 \). Every stage reachable from \( w_0 \) is, or reaches, \( w_1 \) or \( w_2 \), each of which forces \( p \vee q \), so none forces \( \neg(p \vee q) \): \( w_0 \Vdash \neg\neg(p \vee q) \). But \( w_2 \Vdash \neg p \) (only \( w_2 \) is reachable from it, and \( p \) is not known there), so \( w_0 \nVdash \neg\neg p \). Likewise \( w_1 \Vdash \neg q \), so \( w_0 \nVdash \neg\neg q \), and \( w_0 \) does not force the disjunction (K4).

(d) **Derive.** A \( \rulename{\neg I} \) box on \( \neg p \), in which \( p \to q \) is built by \( \rulename{\bot E} \) and fed to the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(p \to q) \to p}
  \open
  \hypo {2} {\neg p}
  \open
  \hypo {3} {p}
  \have {4} {\bot} \ne{3,2}
  \have {5} {q} \be{4}
  \close
  \have {6} {p \to q} \ii{3-5}
  \have {7} {p} \ie{1,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {\neg\neg p} \ni{2-8}
\end{nd}$
\end{center}
```

(e) **Break**, at \( w_0 \) of \( M_1 \). No stage forces \( \neg p \), so \( w_0 \Vdash \neg p \to p \) with nothing to check, and \( w_0 \nVdash p \).

(f) **Derive.** The disjunction is used by cases; the case \( p \) clashes with \( \neg p \):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(p \vee q) \wedge \neg p}
  \have {2} {p \vee q} \ae{1}
  \have {3} {\neg p} \ae{1}
  \open
  \hypo {4} {p}
  \have {5} {\bot} \ne{4,3}
  \have {6} {q} \be{5}
  \close
  \open
  \hypo {7} {q}
  \have {8} {q} \r{7}
  \close
  \have {9} {q} \oe{2,4-6,7-8}
\end{nd}$
\end{center}
```

(g) **Break**, at \( w_0 \) of \( M_3 \) (stages \( w_0 \to w_1 \), nothing known at \( w_0 \), \( p \) and \( q \) known at \( w_1 \)). The only stage forcing \( p \) is \( w_1 \), which forces \( q \), so \( w_0 \Vdash p \to q \). No stage forces \( \neg p \), since both reach \( w_1 \), which forces \( p \); so \( w_0 \Vdash \neg p \to q \) with nothing to check. Hence \( w_0 \) forces the conjunction (K3), and \( w_0 \nVdash q \).

The look-alikes: (a) and (b) are converses, and both derivable. (c) is (a)'s look-alike with \( \vee \) for \( \wedge \), and it breaks. (e) is (d)'s look-alike and breaks: from \( \neg p \to p \) one derives only \( \neg\neg p \) (a box on \( \neg p \), then \( \rulename{{\to}E} \), \( \rulename{\neg E} \) and \( \rulename{\neg I} \)). (g) is (f)'s look-alike: a proof by cases on \( p \) and \( \neg p \) with no disjunction to split, which needs \( p \vee \neg p \). It is the pattern of @lem-atom-splitting (Section 4.8) with no further premises, which is why completeness, and with it TAUT, rests on \( \rulename{LEM} \).

**Marking scheme.** (10 points)
- 6: the four derivations, 1.5 each.
- 3: the three countermodels, 1 each, every clause checked.
- 1: one correct remark on a look-alike pair.

A wrong verdict scores 0 for that item. Fatal errors (0 for that item): a derivation that uses \( \rulename{RAA} \), \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \), or cites a result derived with one; a TAUT line (every claim is a tautology, so a TAUT line would "derive" each, the breakable (c), (e) and (g) included; TAUT rests on completeness); a "model" with a known letter lost at a later stage.
:::

### C. Going deeper

::: {#exr-kripke-models-c1}
[C1: Peirce's law and one instance of excluded middle]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( ((p \to q) \to p) \to p \) from the premise \( p \vee \neg p \) without \( \rulename{RAA} \) or TAUT.
2. Derive without \( \rulename{RAA} \) or TAUT, or refute with a Kripke model: \( \vdash \bigl( ((p \to q) \to p) \to p \bigr) \to (p \vee \neg p) \).
3. Compare (a), (b) and @exr-excluded-middle-b5 (c) with @thm-classical-rules-interderivable, in one sentence.
:::
:::

::: {.solution}
(a) A \( \rulename{{\to}I} \) box on \( (p \to q) \to p \), and inside it the premise used by cases. In the case \( \neg p \), the implication \( p \to q \) is built by \( \rulename{\bot E} \) and fed to the box's assumption:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {p \vee \neg p}
  \open
  \hypo {2} {(p \to q) \to p}
  \open
  \hypo {3} {p}
  \have {4} {p} \r{3}
  \close
  \open
  \hypo {5} {\neg p}
  \open
  \hypo {6} {p}
  \have {7} {\bot} \ne{6,5}
  \have {8} {q} \be{7}
  \close
  \have {9} {p \to q} \ii{6-8}
  \have {10} {p} \ie{2,9}
  \close
  \have {11} {p} \oe{1,3-4,5-10}
  \close
  \have {12} {((p \to q) \to p) \to p} \ii{2-11}
\end{nd}$
\end{center}
```

(b) **Refute**, at \( w_0 \) of the fork \( M_7 \): stages \( w_0 \to w_1 \) and \( w_0 \to w_2 \), with \( p \) known at \( w_1 \) only, and \( q \) known nowhere.

- At \( w_2 \) no stage reachable forces \( p \), so \( w_2 \Vdash p \to q \), and \( w_2 \nVdash p \). So \( w_2 \nVdash (p \to q) \to p \), and neither does \( w_0 \), which reaches \( w_2 \). \( w_1 \) forces \( p \), hence \( (p \to q) \to p \). The only stage forcing \( (p \to q) \to p \) is \( w_1 \), and it forces \( p \): so \( w_0 \Vdash ((p \to q) \to p) \to p \) (K5).
- \( w_0 \nVdash p \), and \( w_0 \nVdash \neg p \) because of \( w_1 \). So \( w_0 \nVdash p \vee \neg p \). Since \( w_0 \) is reachable from itself, forces \( ((p \to q) \to p) \to p \) and does not force \( p \vee \neg p \), (K5) gives \( w_0 \nVdash \bigl( ((p \to q) \to p) \to p \bigr) \to (p \vee \neg p) \), so \( w_0 \) refutes the claim; by @cor-kripke-countermodel it has no derivation without \( \rulename{RAA} \).
- \( M_1 \) would not do: there no stage forces \( p \to q \), so \( w_0 \) forces \( (p \to q) \to p \) and not \( p \), and so does not force Peirce's law; the only stage that does, \( w_1 \), forces \( p \vee \neg p \). So the second branch is needed.

(c) @thm-classical-rules-interderivable compares rules, which act on every statement at once. Instance by instance the three differ: one instance of excluded middle gives Peirce's law (a) and double-negation elimination (@exr-excluded-middle-b5 (c)) for that letter, while that instance of Peirce's law does not give the instance of excluded middle back (b).

**Marking scheme.** (10 points)
- 5: (a). The \( \rulename{\vee E} \) on the premise, with both cases inside the box of line 2 (2); the case \( \neg p \) reaching \( p \) without \( \rulename{RAA} \) (2), for instance by building \( p \to q \) with \( \rulename{\bot E} \), or via \( \neg\neg p \) as in B2 (d) (citing B2 (d) and @exr-excluded-middle-b5 (c) is allowed); the closing \( \rulename{{\to}I} \) (1).
- 4: (b). A model whose stage forces \( ((p \to q) \to p) \to p \) and not \( p \vee \neg p \), every clause checked.
- 1: (c).

Fatal errors (0 for the step): using \( M_1 \) in (b), where the formula is forced; using \( \rulename{RAA} \) or TAUT in (a).
:::

::: {#exr-kripke-models-c2}
[C2: Challenge: three negations are one]

Prove that in every Kripke model, for every stage \( w \) and every formula \( \varphi \): \( w \Vdash \neg\neg\neg\varphi \) if and only if \( w \Vdash \neg\varphi \). Compare with @exm-triple-negation.
:::

::: {.solution}
\( (\Leftarrow) \) Let \( w \Vdash \neg\varphi \), and let \( w' \) be reachable from \( w \). By @lem-heredity, \( w' \Vdash \neg\varphi \). Since \( w' \) is reachable from itself, \( w' \nVdash \neg\neg\varphi \) (K6). So no stage reachable from \( w \) forces \( \neg\neg\varphi \), and \( w \Vdash \neg\neg\neg\varphi \).

\( (\Rightarrow) \) Let \( w \Vdash \neg\neg\neg\varphi \), and suppose some \( w' \) reachable from \( w \) forces \( \varphi \). Every \( w'' \) reachable from \( w' \) forces \( \varphi \) by @lem-heredity, so no such \( w'' \) forces \( \neg\varphi \) (K6, with \( w'' \) reachable from itself), and \( w' \Vdash \neg\neg\varphi \). But \( w' \) is reachable from \( w \), and \( w \Vdash \neg\neg\neg\varphi \) says no such stage forces \( \neg\neg\varphi \): a contradiction. So no stage reachable from \( w \) forces \( \varphi \), and \( w \Vdash \neg\varphi \).

The comparison: @exm-triple-negation derives \( \neg\neg\neg P \vdash \neg P \) without \( \rulename{RAA} \), and \( \neg P \vdash \neg\neg\neg P \) is @prp-double-negation (a) for \( \neg P \). By @thm-kripke-soundness both directions hold at every stage. The exercise proves the same fact directly, from the clauses.

**Marking scheme.** (10 points)
- 4: \( (\Leftarrow) \), with heredity and reflexivity named.
- 5: \( (\Rightarrow) \), with heredity of \( \varphi \) used to get \( w' \Vdash \neg\neg\varphi \).
- 1: the comparison.
- Second route: both directions from @thm-kripke-soundness, applied to the derivations without \( \rulename{RAA} \) of @exm-triple-negation and @prp-double-negation (a) with \( \varphi \) for \( P \), earn the 9 points for the two directions; the 1 point for the comparison then goes to naming where the direct proof uses heredity.

Fatal errors (0 for the step): "not forced, so the negation is forced"; heredity used without being cited.
:::

<!-- dependency ledger
kripke-models-opening (claim): Section 8.7 names the laws; thm-raa-independent proves the non-derivability of LEM and not-not-E by a three-valued reading; 8.7 states the rest and points to this section; every row makes p or not p true | F1.5 §07 (earlier section, prose); thm-raa-independent (optional, cited in prose only); def-truth-value (inline)
def-forcing (claim): the recursion defines, for each formula, the set of stages forcing it | thm-structural-recursion (cited; its values may be sets of stages)
def-forcing (claim): with one stage, forcing is Chapter 4's truth | def-truth-value (cited); inline comparison of (K5), (K6) with (V5), (V2)
def-forcing (claim): a refuting stage is the counterexample set read at a stage | def-counterexample-set, F1.1 §01 (prose pointer); inline
exm-two-stage-model (solution): w0 does not force p, not p, p or not p, not-not p -> p; w0 forces not-not p | inline; verify/ch08/def-kripke-model.py
lem-heredity (proof): structural induction on formulas | thm-structural-induction (cited); def-formula (cited)
thm-kripke-soundness (proof): Steps 1-4 of the proof of thm-soundness, with stages for valuations; derived rules abbreviate propositional primitive ones; lines restricted to def-formula | def-formula (cited), thm-soundness (cited), lem-context-inclusion (a), (b) (cited), def-derivation, def-derivable (cited), thm-strong-induction (cited), lem-heredity (cited)
thm-kripke-soundness (claim): TAUT is licensed by completeness, whose proof uses LEM | def-rule-taut, F1.3 §08 (prose pointer "Section 4.8"); F1.5 §07's sentence on TAUT (earlier section, prose pointer)
thm-kripke-soundness (claim): the rule table, row by row | inline (each row is the matching case of the folded proof)
cor-kripke-countermodel (proof): inline not-I | thm-kripke-soundness (cited)
kripke-models-raa-check (solution): not-not p |- p is derived with RAA | prp-double-negation (b) (cited)
exm-three-stage-model (solution): w0 of M2 refutes both sequents | inline; verify/ch08/def-kripke-model.py
exm-three-stage-model (claim): both sequents are classically derivable | prp-de-morgan (d), Section 2.5 (prose); cor-derivable-iff-valid (cited) for the tautology (p -> q) or (q -> p)
kripke-models-settle (claim): every row of the table; M3 and M4 are Kripke models; the table covers the propositional right column of 8.7's table and 8.7 B1, R3 | inline; verify/ch08/def-kripke-model.py; F1.5 §07 table (earlier section, prose)
kripke-models-search (example): the backwards search for (p -> q) -> q |- p or q ends at M1 | inline; Section 4.6's search named as the model (prose)
kripke-models-remark (claim): Kripke completeness; the disjunction property; quantifier Kripke models refute not-forall |- exists-not and the two passage directions | stated without proof and marked so; nothing depends on them
kripke-models-not-allowed (claim): the four misreadings fail at the stated stages | inline; verify/ch08/def-kripke-model.py
exr-kripke-models-a1 (solution): (a), (c), (d) on M1; (b) one stage is a row | inline; verify/ch08/def-kripke-model.py; def-truth-value (cited)
exr-kripke-models-a2 (solution): every part on M1, M2, M5 | inline; verify/ch08/def-kripke-model.py
exr-kripke-models-b1 (solution): the five verdicts on M6; the chain argument | inline; verify/ch08/def-kripke-model.py (verdicts, and every chain of up to four stages over p, q checked)
exr-kripke-models-b2 (solution): the four derivations and three countermodels; every claim classically valid | tools/check_fitch.py; verify/ch08/exr-kripke-models-b2.py; verify/ch08/def-kripke-model.py; lem-atom-splitting (cited in the look-alike note only)
exr-kripke-models-c1 (solution): the derivation from p or not p; M7 refutes the claim and M1 does not | tools/check_fitch.py; verify/ch08/def-kripke-model.py; verify/ch08/exr-kripke-models-b2.py (classical validity); thm-classical-rules-interderivable, exr-excluded-middle-b5 (cited)
exr-kripke-models-c2 (solution): both directions from the clauses | lem-heredity (cited); exm-triple-negation, prp-double-negation, thm-kripke-soundness (cited) for the comparison
-->
