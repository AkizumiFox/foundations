# Finding First-Order Derivations

Chapter 5 added one step to the search method in each rule section, and Section 6.2 added laws. This section puts the steps into one method, puts in order the moves that do most of the work with quantifiers and names a third, admits the propositional step TAUT into derivations with quantifiers, and runs the four kinds of task of Section 3.2 again. The new difficulty is names: which term to instantiate at, when to open a box for a witness, and which names a line may mention when a box closes.

::: {.remark}
[Looking back]

Section 3.1 assembled the search method for the connectives, and Section 3.2 sorted the tasks it serves. Here both return with flags and witnesses. Backward from the goal and forward from the premises is unchanged; what is new is that a box may carry a name, and a closing line must not mention it.
:::

## The search method, extended

Section 3.1 put the moves for the connectives in order. Each of Sections 5.3–5.7 added a step. Here is the method with all of them.

::: {.algorithm}
**Searching for a derivation of \( \Gamma \vdash \varphi \) in predicate logic.**

1. **Set up.** Write the premises \( \Gamma \) at the top and \( \varphi \) at the bottom, with one gap between. Translate any definition in words into a formula first, as in @exm-translate-limit.
2. **Goal-directed step.** Take the current goal's main symbol and set up its introduction rule:
   - \( \wedge \), \( \to \), \( \neg \), \( \leftrightarrow \): as in Section 3.1;
   - \( \forall x\, \psi \): open a **flagged box** with a fresh name \( x_0 \); the new goal, the box's last line, is \( \psi[x_0/x] \) (Section 5.4). For \( \forall x \in A\; \psi \), the box opens with the assumption \( x_0 \in A \);
   - \( \vee \): **postpone**, as in Section 3.1;
   - \( \exists x\, \psi \): **postpone**; work on the premises until an available line shows a term \( t \) with \( \psi[t/x] \), then use \( \rulename{\exists I} \) (Section 5.5). For \( \exists x \in A\; \psi \), the line \( t \in A \) is needed too.

   Repeat while the goal is \( \wedge \), \( \to \), \( \neg \), \( \leftrightarrow \), or \( \forall \).
3. **Premise-directed step.** Take the main symbol of a resource and apply its elimination rule:
   - \( \wedge \), \( \to \), \( \vee \), \( \leftrightarrow \), and the derived rules: as in Section 3.1;
   - \( \exists x\, \psi \): open the \( \rulename{\exists E} \) box **early**, as soon as the line is available, with a fresh witness \( x_0 \), and make its last line the current goal, which must not mention \( x_0 \) (Section 5.6). An early box lets the witness serve the goals that come later;
   - \( \forall x\, \psi \): do not instantiate blindly; instantiate at the term that the goal, or another resource, mentions (Section 5.3). For \( \forall x \in A\; \psi \), the line \( t \in A \) is needed too;
   - an equation \( t_1 = t_2 \): use \( \rulename{{=}E} \) with a \( \varphi \) chosen so that one substitution turns an available line into the goal, turning the equation round first if needed (Section 5.7).
4. **Clash.** As in Section 3.1: for the goal \( \bot \), find or manufacture a pair \( \chi \), \( \neg\chi \); an impossible case closes itself by \( \rulename{\bot E} \).
5. **Stuck.** As in Section 3.1: \( \rulename{RAA} \) on the current goal, or \( \rulename{LEM} \) on a well-chosen statement.

When no gap is left, number the lines and check the derivation as @def-derivation, extended in Section 5.4, says: every citation is available, and every side condition holds (\( t \) free for \( x \) at \( \rulename{\forall E} \) and \( \rulename{\exists I} \), bounded or not; \( t_1 \) and \( t_2 \) free for \( x \) at \( \rulename{{=}E} \); a fresh name at each line that closes a flagged box).
:::

Two of the new steps deserve a word on their place in the order. The goal step for \( \forall \) is safe in the same way as the goal steps for \( \to \) and \( \neg \) (Section 3.1): if \( \forall x\, \psi \) is derivable at all, then so is \( \psi[x_0/x] \) for a fresh \( x_0 \), by one more \( \rulename{\forall E} \); so opening the box loses nothing. The goal step for \( \exists \) is unsafe in the same way as the one for \( \vee \): a witness chosen too early may be the wrong one, as in @exm-existential-introduction-derivations, where "take \( y = c \)" stalled. That is why \( \exists \) is postponed and the \( \rulename{\exists E} \) boxes of the premises are opened early: the witnesses they supply are often the terms the postponed goal is waiting for, as \( N_0 \) was in the limit derivation of Section 6.1.

## Three moves for quantifiers

Most first-order searches turn on three moves. The first two carry the names Chapter 5 gave them; what is new here is their order, which the method above already follows.

**Name the witness early** (Section 5.6). When an \( \exists \) line is among the resources, open its box at once, with a fresh witness, and make the box's last line the current goal. The witness costs nothing to name, and it is often the very term that a \( \forall \) line or the goal is waiting for.

**Instantiate at the term you need** (Section 5.3), and so not before that term is known. A \( \forall \) line can be instantiated at any term at all, which is exactly why instantiating it before the goal or a witness names the term is a blind choice. Wait for the witnesses, then instantiate at them.

**The propositional core.** Once the boxes are open and the \( \forall \) lines are instantiated, what is left is often a step that holds for propositional reasons alone. The subsection "The propositional core" below names this move and gives it a one-line step.

Two pairs of steps recur: \( \rulename{\forall E} \) followed by \( \rulename{{\to}E} \), which applies a general law at one point, and \( \rulename{\exists E} \) followed, inside its box, by \( \rulename{\exists I} \) with a term built from the names in hand.

The next move, read off the goal and the lines in hand:

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc start] (s) {the current goal\\and the available lines};
  \node[fc test, below=of s] (t1) {goal begins with $\forall$,\\$\wedge$, $\to$, $\neg$ or $\leftrightarrow$?};
  \node[fc test, below=of t1] (t2) {an $\exists$ line available,\\box not yet opened?};
  \node[fc test, below=of t2] (t3) {a $\forall$ line not yet\\instantiated at a term\\the goal or a witness names?};
  \node[fc test, below=of t3] (t4) {goal $\exists x\, \psi$, and a line\\showing $\psi[t/x]$?};
  \node[fc start, below=of t4] (e) {stuck: test the subgoal\\by a counter-reading;\\then RAA or LEM};
  \node[fc step, anchor=west] (a) at ($(t1)+(4.5,0)$) {set up its introduction rule\\(for $\forall$: a fresh flag)};
  \node[fc step, anchor=west] (b) at ($(t2)+(4.5,0)$) {open its $\exists$E box now;\\fresh witness, same goal};
  \node[fc step, anchor=west] (c) at ($(t3)+(4.5,0)$) {$\forall$E at that term};
  \node[fc step, anchor=west] (d) at ($(t4)+(4.5,0)$) {$\exists$I at $t$};
  \coordinate (r) at ($(a.east)+(0.5,0)$);
  \draw[fc arrow] (s) -- (t1);
  \foreach \t/\b in {t1/a, t2/b, t3/c, t4/d}
    \draw[fc arrow] (\t) -- node[above, font=\scriptsize] {yes} (\b);
  \foreach \p/\q in {t1/t2, t2/t3, t3/t4, t4/e}
    \draw[fc arrow] (\p) -- node[right, font=\scriptsize] {no} (\q);
  \draw (b.east) -- (b.east -| r);
  \draw (c.east) -- (c.east -| r);
  \draw (d.east) -- (d.east -| r);
  \draw[fc arrow] (a.east) -- (a.east -| r) |- (s.east);
  \draw (d.east -| r) -- (a.east -| r);
\end{tikzpicture}
\end{center}
```

The last edge reads "no", not "impossible": the chart is a guide to the next move, and it makes no claim that every derivable sequent is found by following it. It leaves out the premise-directed connective steps, the clash and the propositional core (TAUT, below); for those, follow the method above.

::: {#exm-search-with-witnesses}
[A search that waits for its witnesses]

Show that \( \forall x\, (P(x) \to \exists y\, R(x, y)), \ \forall x\, \forall y\, (R(x, y) \to Q(y)), \ \exists x\, P(x) \vdash \exists y\, Q(y) \).
:::

::: {.idea}
The goal is an \( \exists \): postpone it. Premise 3 is an \( \exists \): open its box now, with witness \( x_0 \) (left). Premise 1 is a \( \forall \), and \( x_0 \) is now the term it needs: \( \rulename{\forall E} \) then \( \rulename{{\to}E} \) gives an \( \exists y \) line. Open that box at once, with witness \( y_0 \) (right). Premise 2 needs two terms, and both are in hand: \( x_0 \), then \( y_0 \). The postponed goal gets its witness, \( y_0 \).

In the left snapshot the gap's goal is still \( \exists y\, Q(y) \): an \( \rulename{\exists E} \) box keeps the goal it was opened for, and its assumption, line 4, says "\( P(x_0) \)" and nothing more. In the right snapshot the same goal has moved one box further in, and line 7 is now the only line that asserts \( R \) of particular terms.

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to \exists y\, R(x, y))}
  \hypo {2} {\forall x\, \forall y\, (R(x, y) \to Q(y))}
  \hypo {3} {\exists x\, P(x)}
  \open[x_0]
  \hypo {4} {P(x_0)} \purpose{\Ee}
  \have[\ ][0] {} {\vdots}
  \have[][12] {12} {\exists y\, Q(y)} \by{?}{}
  \close
  \have {13} {\exists y\, Q(y)} \by{?}{}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to \exists y\, R(x, y))}
  \hypo {2} {\forall x\, \forall y\, (R(x, y) \to Q(y))}
  \hypo {3} {\exists x\, P(x)}
  \open[x_0]
  \hypo {4} {P(x_0)} \purpose{\Ee}
  \have {5} {P(x_0) \to \exists y\, R(x_0, y)} \Ae{1}
  \have {6} {\exists y\, R(x_0, y)} \ie{5,4}
  \open[y_0]
  \hypo {7} {R(x_0, y_0)} \purpose{\Ee}
  \have[\ ][0] {} {\vdots}
  \have[][11] {11} {\exists y\, Q(y)} \by{?}{}
  \close
  \have {12} {\exists y\, Q(y)} \by{?}{}
  \close
  \have {13} {\exists y\, Q(y)} \by{?}{}
\end{nd}$
\end{center}
```
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to \exists y\, R(x, y))}
  \hypo {2} {\forall x\, \forall y\, (R(x, y) \to Q(y))}
  \hypo {3} {\exists x\, P(x)}
  \open[x_0]
  \hypo {4} {P(x_0)}
  \have {5} {P(x_0) \to \exists y\, R(x_0, y)} \Ae{1}
  \have {6} {\exists y\, R(x_0, y)} \ie{5,4}
  \open[y_0]
  \hypo {7} {R(x_0, y_0)}
  \have {8} {\forall y\, (R(x_0, y) \to Q(y))} \Ae{2}
  \have {9} {R(x_0, y_0) \to Q(y_0)} \Ae{8}
  \have {10} {Q(y_0)} \ie{9,7}
  \have {11} {\exists y\, Q(y)} \Ei{10}
  \close
  \have {12} {\exists y\, Q(y)} \Ee{6,7-11}
  \close
  \have {13} {\exists y\, Q(y)} \Ee{3,4-12}
\end{nd}$
\end{center}
```

At line 12, \( y_0 \) is not in line 12, in line 6, in the premises, or in the open assumption on line 4. At line 13, \( x_0 \) is not in line 13, in line 3, or in the premises, and no assumption is open.

Read over \( \nZ \), with \( P(x) \) as "\( x > 0 \)", \( R(x, y) \) as "\( y = 2x + 1 \)" and \( Q(y) \) as "\( y \) is odd": every positive integer has a \( 2x + 1 \); every number of the form \( 2x + 1 \) is odd; some integer is positive; so some integer is odd.

Compare a search that starts with premise 1, before any witness is named. It must instantiate at some term, a variable or a constant that nothing mentions, say \( c \); the line \( P(c) \to \exists y\, R(c, y) \) then waits for \( P(c) \), which no premise gives. The box of premise 3 supplies the term that makes premise 1 usable.
:::

::: {.check}
Why is line 8 an instance at \( x_0 \), and not at some other term?
:::

::: {.solution}
Line 7, the only line that asserts \( R \) of particular terms, mentions \( x_0 \) and \( y_0 \). Premise 2 is useful only at the terms that line names. This is the move "instantiate at the term you need": the terms were known only once the witnesses were named.
:::

## Steps that are right for propositional reasons

Inside the boxes of a first-order derivation, many steps are propositional: \( \rulename{\wedge E} \), \( \rulename{{\to}E} \), a contrapositive, a case split. Section 4.8 let a propositional derivation take such steps in one line, as TAUT. With quantifiers the step must not look inside a quantifier, and the next definition says exactly what it may look at.

::: {#def-propositional-skeleton}
[Propositional Skeleton]

Call a first-order formula **prime** if it is atomic and not \( \bot \), or begins with a
quantifier, bounded or not. Assign to each prime formula a propositional atom, the **same** atom to two prime
formulas exactly when one can be turned into the other by finitely many renamings of bound variables (Section 5.2), in either direction; this is an equivalence relation, so the assignment is well defined. The
**propositional skeleton** \( \mathrm{sk}(\varphi) \) of a formula \( \varphi \) is defined by
recursion: \( \mathrm{sk}(\bot) = \bot \); \( \mathrm{sk}(\pi) \) is the atom of \( \pi \) for a
prime formula \( \pi \); \( \mathrm{sk}(\neg\varphi) = \neg\,\mathrm{sk}(\varphi) \); and
\( \mathrm{sk}(\varphi \circ \psi) = \mathrm{sk}(\varphi) \circ \mathrm{sk}(\psi) \) for each of
\( \wedge \), \( \vee \), \( \to \), \( \leftrightarrow \). The formulas of one list take their
skeletons from one assignment.
:::

The skeleton keeps the connectives outside every quantifier and hides everything else; this is not the skeleton of a derivation that Section 3.1 reads off the goal, and wherever the two could be confused, the book says "propositional skeleton" for this one. For example,
\[
\mathrm{sk}\bigl( \forall x\, P(x) \to (\exists y\, R(y, c) \vee \neg\forall z\, P(z)) \bigr) = p \to (q \vee \neg p),
\]
since \( \forall x\, P(x) \) and \( \forall z\, P(z) \) differ only by renaming and so share the atom \( p \).

Why only renaming? The formulas \( \forall x\, (P(x) \wedge Q(x)) \) and \( \forall x\, P(x) \wedge \forall x\, Q(x) \) are provably equivalent (@prp-quantifier-distribution (a)), yet the first is prime and the second is a conjunction of two prime formulas. If provable equivalence were allowed to merge atoms, the skeleton would depend on what has been derived, and a TAUT line could hide a quantifier step inside a table. Renaming is different: whether two formulas differ only by renaming bound variables can be seen by comparing them symbol by symbol, so anyone can compute the skeleton without a derivation. And \( \bot \) is kept as itself, not given an atom, so that \( \neg\bot \) is a tautology and a cited line \( \bot \) entails every skeleton, as \( \rulename{\bot E} \) says it should; an atom would have neither property.

::: {#prp-taut-skeleton}
[Tautological Steps on the Skeleton]

Let \( \Gamma \) be a list of first-order formulas and \( \psi \) a formula, with skeletons taken
from one assignment. If the skeletons of \( \Gamma \) semantically entail \( \mathrm{sk}(\psi) \)
(@def-valid-argument), then \( \Gamma \vdash \psi \). If no two different prime
formulas occurring outside all quantifiers in \( \Gamma \) and \( \psi \) share an atom, the derivation uses only the rules of
Chapters 1 and 2.
:::

*In words: a step that is right for propositional reasons alone is derivable, with the quantified parts carried along untouched.*

The proof takes the propositional derivation that completeness provides and puts the prime formulas back in place of their atoms; it is in the fold below.

::: {.second-reading title="The proof: completeness on the skeleton, then substitution"}
::: {.proof}
*Step 1: no two different prime formulas outside all quantifiers share an atom.* By @cor-derivable-iff-valid (completeness, Section 4.8) there is a derivation \( D \) of \( \mathrm{sk}(\Gamma) \vdash \mathrm{sk}(\psi) \) with the rules of Chapters 1 and 2; its lines are propositional formulas. Replace, in every line of \( D \), each atom of \( \mathrm{sk}(\Gamma) \), \( \mathrm{sk}(\psi) \) by the prime formula of \( \Gamma \), \( \psi \) to which it was assigned, and any other atom by \( \bot \). This is the substitution of formulas for atoms that @def-derived-rule makes for letters, and that @lem-substitution makes for meaning. Every rule of Chapters 1 and 2 is a schema in formulas, and the replacement commutes with each connective and leaves \( \bot \) alone. So each line keeps its rule and its citations, and each box keeps its extent and its assumption; this holds for \( \rulename{RAA} \), \( \rulename{LEM} \) and \( \rulename{\bot E} \) as for the others. \( D \) has no flagged box, so no side condition about names arises. Each premise \( \mathrm{sk}(\gamma) \) becomes \( \gamma \), and the last line becomes \( \psi \). So the result is a first-order derivation of \( \Gamma \vdash \psi \) (@def-derivation, as Section 5.4 extended it), and it uses only the rules of Chapters 1 and 2. This is the second sentence of the statement.

*Step 2: the general case.* Choose one prime formula for each atom, and let \( \gamma^* \) be \( \gamma \) with every prime formula occurring outside all quantifiers (the occurrences the skeleton sees) replaced by the chosen one of its atom. Prime formulas with one atom differ only by renaming. A renaming is a provable equivalence whose closure is derivable (the renaming sentence after @prp-replacement), so @prp-replacement, applied one occurrence and one renaming step at a time (through a letter new to the formula where needed), with the steps chained by @lem-weakening-cut (c), gives \( \gamma \dashv\vdash \gamma^* \) for each formula \( \gamma \) of the list, and \( \psi \dashv\vdash \psi^* \). The formulas \( \Gamma^* \) and \( \psi^* \) have the same skeletons as \( \Gamma \) and \( \psi \), and in them no two different prime formulas outside all quantifiers share an atom, so Step 1 gives \( \Gamma^* \vdash \psi^* \). Now @lem-weakening-cut (Section 2.3) chains \( \Gamma \vdash \gamma^* \) for each \( \gamma \), then \( \Gamma^* \vdash \psi^* \), then \( \psi^* \vdash \psi \). Each pasted block's flags are first renamed to names new to the whole derivation, as "The laws as one line" (Section 6.2) argues. Then no flag of a pasted block occurs in a premise or an open assumption of the derivation it is pasted into, so every \( \rulename{\forall I} \) and \( \rulename{\exists E} \) side condition of the block still holds, and @lem-weakening-cut (c) holds for these first-order derivations by the same pasting. So \( \Gamma \vdash \psi \).
:::
:::

**TAUT on the skeleton.** From now on, a line of a derivation may be justified \( \rulename{TAUT} \), citing available lines, when their skeletons semantically entail its skeleton (@def-valid-argument), all from one assignment; with no cited lines, when its skeleton is a tautology. This is @def-rule-taut of Section 4.8, applied to skeletons. By @prp-taut-skeleton the line abbreviates a block of primitive steps, pasted in with any flags renamed to names new to the whole derivation, as "The laws as one line" (Section 6.2) allows. As in Section 4.8, use TAUT only for a step a written proof would leave unsaid.

These are TAUT steps:

- from \( \neg(\exists x\, P(x) \wedge Q(c)) \) and \( Q(c) \) to \( \neg\exists x\, P(x) \), since \( \neg(p \wedge q), q \models \neg p \);
- from \( \forall x\, (P(x) \to Q(x)) \to R \) and \( \neg R \) to \( \neg\forall x\, (P(x) \to Q(x)) \): modus tollens on the skeleton, \( p \to r, \neg r \models \neg p \).

These are not:

- from \( \forall x\, \forall y\, R(x, y) \) to \( \forall y\, \forall x\, R(x, y) \): the two prime formulas do not differ by renaming, so the skeletons are \( p \) and \( q \), and \( p \not\models q \). The step is derivable, by @exm-universal-introduction-derivations (c), and that derivation looks inside the quantifiers;
- from \( \forall x\, P(x) \) to \( P(c) \): the skeletons are \( p \) and \( q \); this is \( \rulename{\forall E} \);
- \( x = x \): the skeleton is one atom, not a tautology; this is \( \rulename{{=}I} \).

::: {.check}
Which are TAUT steps? (a) From \( \exists x\, P(x) \wedge \forall y\, Q(y) \) to \( \forall y\, Q(y) \wedge \exists x\, P(x) \). (b) From \( \forall x\, (P(x) \wedge Q(x)) \) to \( \forall x\, P(x) \). (c) From \( \neg\forall x\, P(x) \) to \( \exists x\, \neg P(x) \).
:::

::: {.solution}
(a) Yes: \( p \wedge q \models q \wedge p \). (b) No: the skeletons are two different atoms; the step is @prp-quantifier-distribution (a), which looks inside \( \forall x \). (c) No: the skeletons are \( \neg p \) and \( q \); the step is QN (a) of Section 6.2, which needs the quantifier rules and \( \rulename{RAA} \).
:::

::: {.warning}
[Not allowed: TAUT]

- From \( \forall x\, (P(x) \wedge Q(x)) \) to \( \forall x\, Q(x) \). *Looks inside a quantifier; needs a flagged box.*
- From \( \forall x\, P(x) \) to \( P(f(c)) \). *An instance, not an entailment of skeletons; needs \( \rulename{\forall E} \).*
- From \( P(c) \) to \( \exists x\, P(x) \). *Needs \( \rulename{\exists I} \).*
- From \( s = t \) and \( P(s) \) to \( P(t) \). *The skeleton is \( p, q \models r \), which fails; needs \( \rulename{{=}E} \).*
- Citing a line inside a box that has closed. *Not available, whatever the table says (@def-derivation).*
:::

## The propositional core {#the-propositional-core}

Many first-order derivations have the same shape. Open the boxes the goal asks for, instantiate every \( \forall \) line at the names in play, then finish with a step that is propositional. The quantifiers frame the derivation, and its core is a truth-table fact.

::: {#exm-propositional-core}
[A propositional core inside a flagged box]

Show that \( \forall x\, (P(x) \to (Q(x) \vee R(x))), \ \forall x\, \neg Q(x) \vdash \forall x\, (P(x) \to R(x)) \).
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to (Q(x) \vee R(x)))}
  \hypo {2} {\forall x\, \neg Q(x)}
  \open[x_0]
  \have {3} {P(x_0) \to (Q(x_0) \vee R(x_0))} \Ae{1}
  \have {4} {\neg Q(x_0)} \Ae{2}
  \have {5} {P(x_0) \to R(x_0)} \taut{3,4}
  \close
  \have {6} {\forall x\, (P(x) \to R(x))} \Ai{3-5}
\end{nd}$
\end{center}
```

The skeleton of line 5's step is \( p \to (q \vee r), \neg q \models p \to r \). At line 6, \( x_0 \) is not in a premise or in line 6, and no assumption is open.

Read over \( \nZ \), with \( P(n) \) as "\( n > 1 \)", \( Q(n) \) as "\( n^2 = 2 \)" and \( R(n) \) as "\( n > 0 \)". The first premise says "if \( n > 1 \), then \( n^2 = 2 \) or \( n > 0 \)", true since \( n > 1 \) gives \( n > 0 \); the second says that no integer squares to \( 2 \). Both premises are true under this reading, and so is the conclusion, which says that every integer greater than \( 1 \) is positive. The quantifier part of the derivation is two instantiations and one generalization, and its core is propositional.
:::

The order of the steps is the point. TAUT could not have been applied to the premises themselves: their skeletons are two atoms \( p \) and \( q \), and the goal's is a third, \( r \), and \( p, q \not\models r \). Only after the flagged box is open and both premises are instantiated at its flag do the lines show the connectives that the table needs. So the move reads: boxes first, instances at the flag second, and the table last.

::: {.check}
Write out what line 5 abbreviates, with the rules of Chapters 1 and 2.
:::

::: {.solution}
Lines 5–13 below replace the one TAUT line:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to (Q(x) \vee R(x)))}
  \hypo {2} {\forall x\, \neg Q(x)}
  \open[x_0]
  \have {3} {P(x_0) \to (Q(x_0) \vee R(x_0))} \Ae{1}
  \have {4} {\neg Q(x_0)} \Ae{2}
  \open
  \hypo {5} {P(x_0)}
  \have {6} {Q(x_0) \vee R(x_0)} \ie{3,5}
  \open
  \hypo {7} {Q(x_0)}
  \have {8} {\bot} \ne{7,4}
  \have {9} {R(x_0)} \be{8}
  \close
  \open
  \hypo {10} {R(x_0)}
  \have {11} {R(x_0)} \r{10}
  \close
  \have {12} {R(x_0)} \oe{6,7-9,10-11}
  \close
  \have {13} {P(x_0) \to R(x_0)} \ii{5-12}
  \close
  \have {14} {\forall x\, (P(x) \to R(x))} \Ai{3-13}
\end{nd}$
\end{center}
```

That is nine lines in place of one. A written proof would say "so \( R(x_0) \), since \( \neg Q(x_0) \)".
:::

## Four kinds of task, with quantifiers

Section 3.2 sorted propositional problems into four kinds, and the kind decides how the search begins. The same four come back. A **theorem** \( \vdash \varphi \) has no premises; an **equivalence** \( \varphi \dashv\vdash \psi \) needs two derivations; **inconsistency** of a list is a derivation of \( \bot \) from it (Section 3.2's definition reads the same for first-order formulas, now with all the rules); and **derive or break** withholds the verdict. A claim is broken by a counter-reading, which makes every member of its counterexample set true (Section 7.2).

::: {#exm-four-tasks-with-quantifiers}
[One pair of predicates, four tasks]

::: {.enumerate options="label=(\alph*)"}
1. *Theorem.* Show that \( \vdash \forall x\, P(x) \to \exists x\, (P(x) \vee Q(x)) \).
2. *Equivalence.* Show that \( \forall x\, (P(x) \to \neg Q(x)) \dashv\vdash \forall x\, (Q(x) \to \neg P(x)) \).
3. *Inconsistency.* Show that the list \( \forall x\, (P(x) \to Q(x)), \ \exists x\, (P(x) \wedge \neg Q(x)) \) is inconsistent.
4. *Derive or break.* Decide \( \forall x\, (P(x) \to Q(x)) \vdash \forall x\, P(x) \to \forall x\, Q(x) \) and its converse.
:::
:::

::: {.solution}
*(a)* With no premises the search starts from the goal alone: an \( \rulename{{\to}I} \) box, then the \( \exists \) goal waits for a line that shows an instance.

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\forall x\, P(x)}
  \have {2} {P(x)} \Ae{1}
  \have {3} {P(x) \vee Q(x)} \oi{2}
  \have {4} {\exists x\, (P(x) \vee Q(x))} \Ei{3}
  \close
  \have {5} {\forall x\, P(x) \to \exists x\, (P(x) \vee Q(x))} \ii{1-4}
\end{nd}$
\end{center}
```

Line 2 instantiates at the variable \( x \) itself, and line 4 uses \( \rulename{\exists I} \) at \( x \), as in @prp-forall-implies-exists. Any term would have done as the witness, since line 1 holds at every term; the variable \( x \) is simply the term at hand, and no constant has to be invented.

*(b)* The E form of Section 6.2 says the same with its two predicates exchanged: "no \( P \) is \( Q \)" is "no \( Q \) is \( P \)". An equivalence is two searches, and here the second is the first with the letters exchanged, so one search does the work of both. Each direction opens a flagged box, instantiates at its flag, takes one TAUT step and generalizes:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to \neg Q(x))}
  \open[x_0]
  \have {2} {P(x_0) \to \neg Q(x_0)} \Ae{1}
  \have {3} {Q(x_0) \to \neg P(x_0)} \taut{2}
  \close
  \have {4} {\forall x\, (Q(x) \to \neg P(x))} \Ai{2-3}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\forall x\, (Q(x) \to \neg P(x))}
  \open[x_0]
  \have {2} {Q(x_0) \to \neg P(x_0)} \Ae{1}
  \have {3} {P(x_0) \to \neg Q(x_0)} \taut{2}
  \close
  \have {4} {\forall x\, (P(x) \to \neg Q(x))} \Ai{2-3}
\end{nd}$
\end{center}
```

The skeletons are \( p \to \neg q \models q \to \neg p \) and the same with \( p \) and \( q \) exchanged.

*(c)* An A form and its O form (Section 6.2). The goal is \( \bot \), so the clash step of the method applies, but no pair \( \chi \), \( \neg\chi \) is in sight among the premises: the clash lives at a witness. The \( \exists \) premise opens its box at once, the \( \forall \) premise is instantiated at the witness, and the clash is propositional:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\exists x\, (P(x) \wedge \neg Q(x))}
  \open[x_0]
  \hypo {3} {P(x_0) \wedge \neg Q(x_0)}
  \have {4} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {5} {\bot} \taut{3,4}
  \close
  \have {6} {\bot} \Ee{2,3-5}
\end{nd}$
\end{center}
```

Line 5's skeleton is \( p \wedge \neg q, p \to q \models \bot \).

*(d)* With the verdict withheld, spend a minute on each side before committing. For the first claim, a reading that makes the premise true and the conclusion false would need every \( P \) to be a \( Q \), every element to be a \( P \), and some element not a \( Q \), which cannot happen; so try to derive it. For the converse, a false hypothesis \( \forall x\, P(x) \) makes the premise true cheaply, which suggests a break.

The first claim derives. Lines 3–6 are @exm-universal-introduction-derivations (b), run inside the box of line 2:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \open
  \hypo {2} {\forall x\, P(x)}
  \open[x_0]
  \have {3} {P(x_0)} \Ae{2}
  \have {4} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {5} {Q(x_0)} \ie{4,3}
  \close
  \have {6} {\forall x\, Q(x)} \Ai{3-5}
  \close
  \have {7} {\forall x\, P(x) \to \forall x\, Q(x)} \ii{2-6}
\end{nd}$
\end{center}
```

At line 6, \( x_0 \) is not in the premise, in line 6, or in the open assumption on line 2.

The converse breaks. Over \( \nZ \), read \( P \) as "even" and \( Q \) as "positive". "Every integer is even" is false, so the premise "if every integer is even, then every integer is positive" is true; the conclusion "every even integer is positive" is false at \( 0 \).
:::

**Test the subgoal by a counter-reading.** Section 4.7 tested a propositional subgoal by a refuting row before chasing it. The first-order form of the move is the same. When a search produces a subgoal, look for a reading that makes the available lines true and the subgoal false before you chase it. If you find one, the subgoal is the wrong one: Section 7.2 states that such a reading rules out every derivation of it from those lines. Return to the step that produced it, and choose differently there: another term for a \( \forall E \), a box opened earlier, or a different case split. A reading takes a minute to find, and it can save the search a long chase.

::: {.check}
A search for the limit derivation of Section 6.1 instantiates the premise at \( \varepsilon_0 \) instead of \( \varepsilon_0/2 \), and reaches the subgoal \( \abs{2 a_{n_0} - 2L} < \varepsilon_0 \) with \( \abs{a_{n_0} - L} < \varepsilon_0 \) available. Find a sequence and numbers that make every available line true and the subgoal false.
:::

::: {.solution}
Take \( \varepsilon_0 = 1 \); \( a_n = L \) for every \( n \) except \( a_{n_0} = L + 0.75 \); and \( N_0 = n_0 \). The premise holds, since the sequence is eventually constant at \( L \). Every term is within \( 0.75 < 1 \) of \( L \), so the instance of the premise at \( \varepsilon_0 \) and the box line \( \forall n \in \nN\; (n \ge N_0 \to \abs{a_n - L} < \varepsilon_0) \) hold; \( n_0 \ge N_0 \) holds; and \( \abs{a_{n_0} - L} = 0.75 < 1 \). But \( \abs{2 a_{n_0} - 2L} = 1.5 \ge 1 \). The subgoal is the wrong one; go back to the choice of term.
:::

::: {.check}
Which task is \( \exists x\, (P(x) \wedge \neg P(x)) \vdash \bot \), and how long is its derivation with TAUT?
:::

::: {.solution}
Inconsistency. Three lines below the premise:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, (P(x) \wedge \neg P(x))}
  \open[x_0]
  \hypo {2} {P(x_0) \wedge \neg P(x_0)}
  \have {3} {\bot} \taut{2}
  \close
  \have {4} {\bot} \Ee{1,2-3}
\end{nd}$
\end{center}
```
:::

## A library of first-order sequents {#a-library-of-first-order-sequents}

Here is what the book has proved about quantifiers, grouped by use; a search that needs one of these can copy its derivation, with formulas in place of letters, rather than rediscover it.

| Use | Sequent | Where |
|---|---|---|
| exchange two like quantifiers | \( \forall x\, \forall y\, \varphi \dashv\vdash \forall y\, \forall x\, \varphi \) | @exm-universal-introduction-derivations (c) |
| rename a bound variable | \( \forall y\, \varphi \dashv\vdash \forall z\, \varphi[z/y] \), and the same for \( \exists \) | Section 5.4 (the fold after @exm-universal-introduction-derivations); [Section 5.6](#existential-renaming) |
| every gives some | \( \forall x\, \varphi \vdash \exists x\, \varphi \) | @prp-forall-implies-exists |
| some-all gives all-some | \( \exists x\, \forall y\, R(x, y) \vdash \forall y\, \exists x\, R(x, y) \) | @prp-exists-forall-swap |
| distribute | \( \forall \) over \( \wedge \) and \( \exists \) over \( \vee \) both ways; \( \forall \) over \( \vee \) and \( \exists \) over \( \wedge \) one way | @prp-quantifier-distribution (the instances for \( P \), \( Q \) first in @prp-forall-and and @prp-exists-and) |
| negate | "not every" and "some not"; "none" and "every not"; a negated implication; bounded forms | @prp-quantifier-negation, @prp-negated-implication, @prp-bounded-quantifier-negation |
| move across a connective | the passage laws | @prp-quantifier-passage |
| replace a part | a provable equivalence, inside any formula | @prp-replacement |
| equality | symmetric and transitive; equals share every property | @prp-equality-symmetric-transitive, @prp-leibniz-law |
| bounds in one step | the bounded rules | @prp-bounded-quantifier-rules |
| propositional steps | TAUT on the skeleton | @prp-taut-skeleton |

The laws of Section 6.2 may already be used as one line, by "The laws as one line"; the other rows are patterns to copy. Either way, a row is used by matching its shape and then checking its conditions: the passage laws need the moved variable not free in the other side, a renaming needs a letter new to the formula, and an instance of a row's letters must be free for the variables it replaces.

::: {.remark}
[Looking ahead]

Every claim this section broke, it broke by a counter-reading. Chapter 7 gives counter-readings an exact form, the counter-model, and states that a counter-model rules out every derivation.
:::

## Exercises

### A. Check your understanding

::: {#exr-first-order-search-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. What is the propositional skeleton of \( \neg\exists x\, P(x) \vee (Q(c) \wedge \exists y\, P(y)) \)? Is it a tautology?
2. What is the propositional skeleton of \( \exists x\, (P(x) \wedge Q(x)) \wedge \neg\exists x\, (Q(x) \wedge P(x)) \)? Can a TAUT step derive \( \bot \) from this formula?
3. Which are TAUT steps? (i) From \( \forall x\, P(x) \) and \( \forall x\, P(x) \to \exists y\, Q(y) \) to \( \exists y\, Q(y) \). (ii) From \( \forall x\, (P(x) \to Q(x)) \) and \( P(c) \) to \( Q(c) \). (iii) From \( \neg\neg\exists x\, P(x) \) to \( \exists x\, P(x) \).
4. In @exm-search-with-witnesses, why is the box on premise 3 opened before premise 1 is used?
5. A counter-reading makes the premises of a claim true and its conclusion false. What may you say now, and what will Section 7.2 add?
:::
:::

::: {.solution}
*(a)* \( \neg p \vee (q \wedge p) \): \( \exists x\, P(x) \) and \( \exists y\, P(y) \) differ only by renaming, so they share \( p \). It is not a tautology: \( p \) true and \( q \) false make it false.

*(b)* \( p \wedge \neg q \). The two prime formulas are not renamings of each other (\( P(x) \wedge Q(x) \) against \( Q(x) \wedge P(x) \)), so they get different atoms, and \( p \wedge \neg q \) is true in a row: no. \( \bot \) is derivable all the same, by an \( \rulename{\exists E} \) box on the first conjunct, a TAUT step inside it to \( Q(x_0) \wedge P(x_0) \), \( \rulename{\exists I} \), and a clash with the second conjunct.

*(c)* (i) Yes: \( p, p \to q \models q \). (ii) No: \( p, q \not\models r \); it is \( \rulename{\forall E} \) at \( c \), then \( \rulename{{\to}E} \). (iii) Yes: \( \neg\neg p \models p \).

*(d)* Premise 1 is a \( \forall \) whose useful term is not yet known, and the box supplies it, \( x_0 \). These are the moves "name the witness early" and "instantiate at the term you need", in that order.

*(e)* Now: the claim breaks, and a search for it is abandoned. Section 7.2 states that such a claim has no derivation.
:::

### B. Practice

::: {#exr-first-order-search-b1}
[B1: Derive or break, twelve claims]

Derive each claim, with TAUT allowed, or break it by a reading over \( \nZ \) that makes every member of its counterexample set true. The groups say which move to try first; they do not say which claims hold. Claims 1–3: name the witness early. Claims 4 and 5: instantiate at the term you need. Claims 6–8: the propositional core. Claims 9–12: move a quantifier, or derive \( \bot \).

1. \( \exists x\, (P(x) \wedge Q(x)), \ \forall x\, (P(x) \to (Q(x) \to R(f(x)))) \vdash \exists y\, R(y) \).
2. \( \exists x\, R(x, x) \vdash \forall x\, \exists y\, R(x, y) \).
3. \( \exists x\, P(x), \ \forall x\, (P(x) \to \forall y\, R(x, y)) \vdash \forall y\, \exists x\, R(x, y) \).
4. \( \forall x\, \forall y\, (R(x, y) \to R(y, x)), \ \forall x\, R(x, f(x)) \vdash \forall x\, R(f(x), x) \).
5. \( \forall x\, R(x, f(x)) \vdash \forall x\, R(f(x), x) \).
6. \( \forall x\, (P(x) \to Q(x)), \ \forall x\, (Q(x) \to R(x)) \vdash \forall x\, (\neg R(x) \to \neg P(x)) \).
7. \( \forall x\, (P(x) \vee Q(x)), \ \forall x\, \neg P(x) \vdash \forall x\, Q(x) \).
8. \( \forall x\, (P(x) \vee Q(x)), \ \neg\forall x\, P(x) \vdash \forall x\, Q(x) \).
9. \( \forall x\, (P(x) \to Q(x)) \vdash \exists x\, P(x) \to \exists x\, Q(x) \).
10. \( \forall x\, (P(x) \to Q(x)) \vdash \exists x\, P(x) \to \forall x\, Q(x) \).
11. \( \forall x\, (P(x) \leftrightarrow \neg P(f(x))), \ \forall x\, P(x) \vdash \bot \).
12. \( \forall x\, \exists y\, R(x, y), \ \forall x\, \forall y\, (R(x, y) \to \neg R(y, x)) \vdash \bot \).
:::

::: {.solution}
*1. Derive.* The box of the witness opens first; inside it, premise 2 is instantiated at \( x_0 \), and the postponed goal takes the compound witness \( f(x_0) \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, (P(x) \wedge Q(x))}
  \hypo {2} {\forall x\, (P(x) \to (Q(x) \to R(f(x))))}
  \open[x_0]
  \hypo {3} {P(x_0) \wedge Q(x_0)}
  \have {4} {P(x_0) \to (Q(x_0) \to R(f(x_0)))} \Ae{2}
  \have {5} {R(f(x_0))} \taut{3,4}
  \have {6} {\exists y\, R(y)} \Ei{5}
  \close
  \have {7} {\exists y\, R(y)} \Ee{1,3-6}
\end{nd}$
\end{center}
```

Line 5's skeleton is \( p \wedge q, p \to (q \to r) \models r \). At line 7, \( x_0 \) is not in line 7, in line 1, or in a premise.

*2. Breaks.* Read \( R(x, y) \) as "\( x \cdot y = 1 \)". The premise is true, since \( 1 \cdot 1 = 1 \); the conclusion fails at \( x = 0 \), since \( 0 \cdot y = 0 \) for every \( y \).

*3. Derive.*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, P(x)}
  \hypo {2} {\forall x\, (P(x) \to \forall y\, R(x, y))}
  \open[x_0]
  \hypo {3} {P(x_0)}
  \have {4} {P(x_0) \to \forall y\, R(x_0, y)} \Ae{2}
  \have {5} {\forall y\, R(x_0, y)} \ie{4,3}
  \open[y_0]
  \have {6} {R(x_0, y_0)} \Ae{5}
  \have {7} {\exists x\, R(x, y_0)} \Ei{6}
  \close
  \have {8} {\forall y\, \exists x\, R(x, y)} \Ai{6-7}
  \close
  \have {9} {\forall y\, \exists x\, R(x, y)} \Ee{1,3-8}
\end{nd}$
\end{center}
```

At line 8, \( y_0 \) is not in a premise, in the open assumption on line 3, or in line 8. At line 9, \( x_0 \) is not in line 9, in line 1, or in a premise.

*4. Derive.* The term premise 1 needs is \( f(x_0) \), and premise 2 names it.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (R(x, y) \to R(y, x))}
  \hypo {2} {\forall x\, R(x, f(x))}
  \open[x_0]
  \have {3} {R(x_0, f(x_0))} \Ae{2}
  \have {4} {\forall y\, (R(x_0, y) \to R(y, x_0))} \Ae{1}
  \have {5} {R(x_0, f(x_0)) \to R(f(x_0), x_0)} \Ae{4}
  \have {6} {R(f(x_0), x_0)} \ie{5,3}
  \close
  \have {7} {\forall x\, R(f(x), x)} \Ai{3-6}
\end{nd}$
\end{center}
```

Line 5 instantiates at \( f(x_0) \), which is free for \( y \). At line 7, \( x_0 \) is not in a premise or in line 7, and no assumption is open.

*5. Breaks.* Read \( f(x) \) as \( x + 1 \) and \( R \) as \( < \). Every \( x < x + 1 \), so the premise is true; no \( x + 1 < x \), so the conclusion is false.

*6. Derive.*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, (Q(x) \to R(x))}
  \open[x_0]
  \have {3} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {4} {Q(x_0) \to R(x_0)} \Ae{2}
  \have {5} {\neg R(x_0) \to \neg P(x_0)} \taut{3,4}
  \close
  \have {6} {\forall x\, (\neg R(x) \to \neg P(x))} \Ai{3-5}
\end{nd}$
\end{center}
```

Line 5's skeleton is \( p \to q, q \to r \models \neg r \to \neg p \).

*7. Derive.*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \vee Q(x))}
  \hypo {2} {\forall x\, \neg P(x)}
  \open[x_0]
  \have {3} {P(x_0) \vee Q(x_0)} \Ae{1}
  \have {4} {\neg P(x_0)} \Ae{2}
  \have {5} {Q(x_0)} \taut{3,4}
  \close
  \have {6} {\forall x\, Q(x)} \Ai{3-5}
\end{nd}$
\end{center}
```

Line 5's skeleton is \( p \vee q, \neg p \models q \).

*8. Breaks.* Read \( P \) as "even" and \( Q \) as "odd". Every integer is even or odd; not every integer is even; and \( 0 \) is not odd, so "every integer is odd" is false.

*9. Derive.*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \open
  \hypo {2} {\exists x\, P(x)}
  \open[x_0]
  \hypo {3} {P(x_0)}
  \have {4} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {5} {Q(x_0)} \ie{4,3}
  \have {6} {\exists x\, Q(x)} \Ei{5}
  \close
  \have {7} {\exists x\, Q(x)} \Ee{2,3-6}
  \close
  \have {8} {\exists x\, P(x) \to \exists x\, Q(x)} \ii{2-7}
\end{nd}$
\end{center}
```

At line 7, \( x_0 \) is not in line 7, in line 2, in the premise, or in an open assumption (line 2's box is still open, and line 2 does not mention \( x_0 \)).

*10. Breaks.* Read \( P(x) \) as "\( x = 0 \)" and \( Q(x) \) as "\( x \cdot x = x \)". The premise holds, since the only \( x \) with \( x = 0 \) has \( 0 \cdot 0 = 0 \). In the conclusion, \( \exists x\, (x = 0) \) is true and \( \forall x\, (x \cdot x = x) \) is false, since \( 2 \cdot 2 = 4 \); so the implication is false.

*11. Derive.* Premise 2 is instantiated twice, at \( y \) and at \( f(y) \), the two terms that premise 1 at \( y \) mentions.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \leftrightarrow \neg P(f(x)))}
  \hypo {2} {\forall x\, P(x)}
  \have {3} {P(y) \leftrightarrow \neg P(f(y))} \Ae{1}
  \have {4} {P(y)} \Ae{2}
  \have {5} {P(f(y))} \Ae{2}
  \have {6} {\bot} \taut{3,4,5}
\end{nd}$
\end{center}
```

Line 6's skeleton is \( p \leftrightarrow \neg q, p, q \models \bot \): no row makes all three true.

*12. Breaks.* Read \( R \) as \( < \). Every integer has a larger one, and \( x < y \) excludes \( y < x \). Both premises are true, and \( \neg\bot \) is true, so the whole counterexample set is true: the list is not shown inconsistent.

Seven claims derive and five break. Four breaks sit beside a derivable look-alike: 5 beside 4, 8 beside 7, 10 beside 9, and 12 beside 11. Claim 2 weakens the premise of the derivable \( \forall x\, R(x, x) \vdash \forall x\, \exists y\, R(x, y) \) of @exm-existential-introduction-derivations (c). Every break is a counter-reading (Section 7.2).

**Marking scheme.** (10 points)
- 4: the twelve verdicts, \( \tfrac13 \) point for each correct one, rounded down.
- 3: the seven derivations, each with every closing side condition checked and every TAUT line's skeleton named.
- 3: the five readings, each with every premise and the conclusion evaluated.
Fatal errors (0 for the claim): a TAUT line that looks inside a quantifier; a "break" with a premise false.
:::

::: {#exr-first-order-search-b2}
[B2: Two witnesses in a row]

The premises are 1 \( \forall x\, (P(x) \to \exists y\, R(x, y)) \), 2 \( \forall x\, \forall y\, (R(x, y) \to P(y)) \) and 3 \( P(c) \); the goal is \( \exists y\, \exists z\, (R(c, y) \wedge R(y, z)) \). Here is a partial derivation:

```{=latex}
% schema (partial derivations: the gap is unnumbered, lines carry their final numbers)
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to \exists y\, R(x, y))}
  \hypo {2} {\forall x\, \forall y\, (R(x, y) \to P(y))}
  \hypo {3} {P(c)}
  \have[\ ][0] {} {\vdots}
  \open[y_0]
  \hypo[][6] {6} {R(c, y_0)} \purpose{\Ee}
  \have[\ ][0] {} {\vdots}
  \have[][16] {16} {\exists y\, \exists z\, (R(c, y) \wedge R(y, z))} \by{?}{}
  \close
  \have {17} {\exists y\, \exists z\, (R(c, y) \wedge R(y, z))} \by{?}{}
\end{nd}$
\end{center}
```

*Name the move, then complete it.*
:::

::: {.solution}
The move is "name the witness early", twice, with each \( \forall \) line instantiated only at the terms in hand: \( c \) (premise 3) first, then the witness \( y_0 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to \exists y\, R(x, y))}
  \hypo {2} {\forall x\, \forall y\, (R(x, y) \to P(y))}
  \hypo {3} {P(c)}
  \have {4} {P(c) \to \exists y\, R(c, y)} \Ae{1}
  \have {5} {\exists y\, R(c, y)} \ie{4,3}
  \open[y_0]
  \hypo {6} {R(c, y_0)}
  \have {7} {\forall y\, (R(c, y) \to P(y))} \Ae{2}
  \have {8} {R(c, y_0) \to P(y_0)} \Ae{7}
  \have {9} {P(y_0)} \ie{8,6}
  \have {10} {P(y_0) \to \exists y\, R(y_0, y)} \Ae{1}
  \have {11} {\exists y\, R(y_0, y)} \ie{10,9}
  \open[z_0]
  \hypo {12} {R(y_0, z_0)}
  \have {13} {R(c, y_0) \wedge R(y_0, z_0)} \ai{6,12}
  \have {14} {\exists z\, (R(c, y_0) \wedge R(y_0, z))} \Ei{13}
  \have {15} {\exists y\, \exists z\, (R(c, y) \wedge R(y, z))} \Ei{14}
  \close
  \have {16} {\exists y\, \exists z\, (R(c, y) \wedge R(y, z))} \Ee{11,12-15}
  \close
  \have {17} {\exists y\, \exists z\, (R(c, y) \wedge R(y, z))} \Ee{5,6-16}
\end{nd}$
\end{center}
```

Lines 4 and 7 instantiate at \( c \), and lines 8 and 10 at \( y_0 \); line 15 is \( \rulename{\exists I} \) at \( y_0 \), which is free for \( y \). At line 16, \( z_0 \) is not in line 16, in line 11, in the premises, or in the open assumption on line 6. At line 17, \( y_0 \) is not in line 17, in line 5, or in the premises.

**Marking scheme.** (10 points)
- 2: names the move.
- 3: opens the two boxes as soon as their \( \exists \) lines exist.
- 3: the \( \rulename{\forall E} \) lines at \( c \), \( c \), \( y_0 \) and \( y_0 \), the terms read off the lines in hand.
- 2: the two side conditions.
Fatal error (0 for the step): \( \rulename{\exists I} \) on line 15 before line 14, so that the witness \( z_0 \) appears in the box's last line.
:::

::: {#exr-first-order-search-b3}
[B3: How much TAUT saves]

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \forall x\, (P(x) \to Q(x)), \ \forall x\, (Q(x) \to \neg P(x)) \vdash \forall x\, \neg P(x) \) twice: once without TAUT, once with exactly one TAUT line. Count the lines.
2. Is the step from \( \forall x\, (P(x) \to Q(x)) \) to \( \forall x\, (\neg Q(x) \to \neg P(x)) \) a TAUT step?
:::
:::

::: {.solution}
*(a)* With TAUT, six lines (left); without it, ten (right):

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, (Q(x) \to \neg P(x))}
  \open[x_0]
  \have {3} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {4} {Q(x_0) \to \neg P(x_0)} \Ae{2}
  \have {5} {\neg P(x_0)} \taut{3,4}
  \close
  \have {6} {\forall x\, \neg P(x)} \Ai{3-5}
\end{nd}$
\qquad
$\begin{nd}
  \hypo {1} {\forall x\, (P(x) \to Q(x))}
  \hypo {2} {\forall x\, (Q(x) \to \neg P(x))}
  \open[x_0]
  \have {3} {P(x_0) \to Q(x_0)} \Ae{1}
  \have {4} {Q(x_0) \to \neg P(x_0)} \Ae{2}
  \open
  \hypo {5} {P(x_0)}
  \have {6} {Q(x_0)} \ie{3,5}
  \have {7} {\neg P(x_0)} \ie{4,6}
  \have {8} {\bot} \ne{5,7}
  \close
  \have {9} {\neg P(x_0)} \ni{5-8}
  \close
  \have {10} {\forall x\, \neg P(x)} \Ai{3-9}
\end{nd}$
\end{center}
```

Line 5 on the left has the skeleton \( p \to q, q \to \neg p \models \neg p \).

*(b)* No: the two formulas are prime and not renamings of each other, so their skeletons are two different atoms. The step is derivable by instantiating, one TAUT line (\( p \to q \models \neg q \to \neg p \)) and generalizing, the pattern of @exm-four-tasks-with-quantifiers (b).

**Marking scheme.** (10 points)
- 3: the TAUT derivation, with the skeleton named.
- 4: the derivation without TAUT.
- 1: the count.
- 2: (b), with the reason.
Fatal error (0 for the step): a TAUT line citing the \( \forall \) lines directly to reach \( \neg P(x_0) \).
:::

### C. Going deeper

::: {#exr-first-order-search-c1}
[C1: Some index decides, used later]

Let \( D(n) \) say "\( a_n > 0 \)" for a sequence \( (a_n) \), over a domain of indices.

::: {.enumerate options="label=(\alph*)"}
1. Derive \( \vdash \exists n\, (D(n) \to \forall m\, D(m)) \), with \( \rulename{LEM} \) on \( \forall m\, D(m) \).
2. Derive it again in two lines, from one TAUT line and one law of Section 6.2.
3. Say in two sentences which index the sentence promises, and why the derivations of (a) and (b) name none.
:::
:::

::: {.solution}
[Hint 1]

For (a): in the case \( \neg\forall m\, D(m) \), which law of Section 6.2 turns the negated \( \forall \) into an \( \exists \)?
:::

::: {.solution}
[Hint 2]

For (b): the formula \( \forall n\, D(n) \to \forall m\, D(m) \) has the skeleton \( p \to p \). Which passage law moves the \( \forall n \) out of the hypothesis of an implication, turning it into \( \exists n \)?
:::

::: {.solution}
*(a)*

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {\forall m\, D(m) \vee \neg\forall m\, D(m)} \lem{}
  \open
  \hypo {2} {\forall m\, D(m)}
  \open
  \hypo {3} {D(n)}
  \have {4} {\forall m\, D(m)} \r{2}
  \close
  \have {5} {D(n) \to \forall m\, D(m)} \ii{3-4}
  \have {6} {\exists n\, (D(n) \to \forall m\, D(m))} \Ei{5}
  \close
  \open
  \hypo {7} {\neg\forall m\, D(m)}
  \have {8} {\exists m\, \neg D(m)} \by{QN (a)}{7}
  \open[m_0]
  \hypo {9} {\neg D(m_0)}
  \have {10} {D(m_0) \to \forall m\, D(m)} \by{VI}{9}
  \have {11} {\exists n\, (D(n) \to \forall m\, D(m))} \Ei{10}
  \close
  \have {12} {\exists n\, (D(n) \to \forall m\, D(m))} \Ee{8,9-11}
  \close
  \have {13} {\exists n\, (D(n) \to \forall m\, D(m))} \oe{1,2-6,7-12}
\end{nd}$
\end{center}
```

Line 6 is \( \rulename{\exists I} \) at the variable \( n \) itself, as in the proof of passage law (d); as there, the step is sound because every domain is non-empty (Section 7.1). Line 11 is \( \rulename{\exists I} \) at \( m_0 \). At line 12, \( m_0 \) is not in line 12, in line 8, or in the open assumption on line 7.

*(b)*

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {\forall n\, D(n) \to \forall m\, D(m)} \taut{}
  \have {2} {\exists n\, (D(n) \to \forall m\, D(m))} \by{passage (d)}{1}
\end{nd}$
\end{center}
```

The two prime formulas of line 1 differ only by renaming, so the skeleton is \( p \to p \), a tautology. Line 2 is @prp-quantifier-passage (d), the direction \( \dashv \), used as one line ("The laws as one line"), with \( \varphi \) the formula \( D(n) \) and \( \psi \) the formula \( \forall m\, D(m) \), in which \( n \) is not free.

*(c)* If every term is positive, any index will do; if not, an index with \( a_n \le 0 \) does, since then the implication is vacuously true. The derivation splits on which case holds without deciding it (\( \rulename{LEM} \) in (a), the classical direction of (d) in (b)), so it never names the index.

**Marking scheme.** (10 points)
- 4: (a), with the \( \rulename{LEM} \) split, both cases closed, with the side condition of every line that closes a flagged box checked.
- 3: (b), with the TAUT line justified by renaming, and law (d) with its condition checked.
- 3: (c).
Fatal errors (0 for the step): giving \( \forall n\, D(n) \) and \( \forall m\, D(m) \) different atoms and then claiming the TAUT line anyway; \( \rulename{\exists I} \) at \( m_0 \) after its box has closed.
:::

::: {#exr-first-order-search-c2}
[C2: Every M is P, every M is S, so some S is P?]

::: {.enumerate options="label=(\alph*)"}
1. Break \( \forall x\, (M(x) \to P(x)), \ \forall x\, (M(x) \to S(x)) \vdash \exists x\, (S(x) \wedge P(x)) \) by a reading over \( \nN \).
2. Add the premise \( \exists x\, M(x) \) and derive the conclusion.
3. Which line of (b) needs the new premise, and what does Section 5.1's existential import have to do with it?
:::
:::

::: {.solution}
*(a) Breaks.* Read \( M(n) \) as "\( n \) is an even prime greater than \( 2 \)", which is true of no \( n \); \( P(n) \) as "\( n \) is odd"; and \( S(n) \) as "\( n \) is even". Both premises are vacuously true, since their hypothesis \( M(n) \) is false for every \( n \), and "some even number is odd" is false (Section 7.2).

*(b)*

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (M(x) \to P(x))}
  \hypo {2} {\forall x\, (M(x) \to S(x))}
  \hypo {3} {\exists x\, M(x)}
  \open[x_0]
  \hypo {4} {M(x_0)}
  \have {5} {M(x_0) \to P(x_0)} \Ae{1}
  \have {6} {M(x_0) \to S(x_0)} \Ae{2}
  \have {7} {S(x_0) \wedge P(x_0)} \taut{4,5,6}
  \have {8} {\exists x\, (S(x) \wedge P(x))} \Ei{7}
  \close
  \have {9} {\exists x\, (S(x) \wedge P(x))} \Ee{3,4-8}
\end{nd}$
\end{center}
```

Line 7's skeleton is \( m, m \to p, m \to s \models s \wedge p \). At line 9, \( x_0 \) is not in line 9, in line 3, or in a premise.

*(c)* Line 7: its TAUT needs \( M(x_0) \), line 4, which only the box of premise 3 supplies. Without it, \( \rulename{\exists I} \) could still be applied at some term, but no line would say that term is \( S \) and \( P \). A "for every" claims no instance, so the old reading of "every \( M \) is \( P \)" as also saying that there are \( M \)s is not the book's reading. With that reading the inference was valid; without it, the premise must be added.

**Marking scheme.** (10 points)
- 3: (a), with all three truth values justified.
- 4: (b).
- 3: (c).
Fatal error (0 for the step): a "break" whose \( M \) is true of some number.
:::

<!-- dependency ledger
exm-search-with-witnesses (claim): the search method: opening a forall box loses nothing: forall-E at a fresh name recovers psi[x_0/x] | inline, as in F1.7 §01's argument for -> (moved with the algorithm from F1.8 §01)
exm-search-with-witnesses (claim): the search method: the moves of Sections 5.3-5.7 assembled; exm-existential-introduction-derivations' "take y = c" stalled | F1.4 §03-§07 (cited by section); exm-existential-introduction-derivations (cited)
exm-search-with-witnesses (claim): the three moves and the flowchart: the flowchart is a guide; no completeness claim | remark; nothing rests on it
exm-search-with-witnesses (solution): over Z, 2x + 1 is odd; positive integers exist | school arithmetic; checked by verify/ch06/exm-search-with-witnesses.py
def-propositional-skeleton (claim): the definition is well defined by recursion on F1.4 §02's formation rules; bot excluded from the prime formulas; renaming is an equivalence on prime formulas | F1.4 §02 (renaming of bound variables, cited by section); inline
prp-taut-skeleton (proof): completeness gives the propositional derivation | cor-derivable-iff-valid (cited)
prp-taut-skeleton (proof): substitution of formulas for atoms preserves every rule instance of Chapters 1-2, with citations and boxes | def-derived-rule, lem-substitution (cited); argued inline
prp-taut-skeleton (proof): the result is a first-order derivation | def-derivation as extended in F1.4 §04 (cited)
prp-taut-skeleton (proof): alike prime formulas are provably equivalent with derivable closure; replacement inside a formula | prp-replacement and the renaming sentence after it (F1.8 §02, cited)
prp-taut-skeleton (proof): lem-weakening-cut (c) for first-order derivations, after each pasted block's flags are renamed to names new to the whole derivation | lem-weakening-cut (cited); argued inline, as "The laws as one line" (F1.8 §02)
prp-taut-skeleton (claim): TAUT on the skeleton: a TAUT line abbreviates a pasted block | prp-taut-skeleton (cited); def-rule-taut (F1.3 §08, cited)
def-propositional-skeleton (claim): TAUT examples and the Quick check: the skeleton verdicts | truth tables; checked by verify/ch06/def-propositional-skeleton.py
exm-propositional-core (solution): n > 1 gives n > 0; no integer squares to 2 | school facts; checked by verify/ch06/exm-propositional-core.py
exm-four-tasks-with-quantifiers (solution): (a) exists-I at the variable x itself | prp-forall-implies-exists (cited); non-empty domains, F1.6 §01 (prose pointer, via that proposition)
exm-four-tasks-with-quantifiers (solution): (d) the converse's reading over Z | school arithmetic; checked by verify/ch06/exm-four-tasks-with-quantifiers.py
exm-four-tasks-with-quantifiers (claim): test the subgoal: a counter-reading rules out every derivation of the subgoal | F1.6 §02 (prose pointer; forward claim, nothing here rests on it); F1.3 §07 (the propositional move, cited by section)
exm-four-tasks-with-quantifiers (solution): the test-the-subgoal Quick check: the reading a_n = L except a_{n_0} = L + 0.75, eps_0 = 1, N_0 = n_0 | arithmetic; checked by verify/ch06/exm-four-tasks-with-quantifiers.py
prp-taut-skeleton (claim): the library table: each row's sequent is the one its label proves | the cited labels (F1.4, F1.8 §01, §02); exm-universal-introduction-derivations' fold (F1.4 §04) and #existential-renaming (F1.4 §06)
exr-first-order-search-b1 (solution): the five readings over Z; the TAUT skeletons of 1, 6, 7, 11 | school arithmetic, truth tables; checked by verify/ch06/exr-first-order-search-b1.py
exr-first-order-search-c1 (solution): exists-I at n itself | non-empty domains, F1.6 §01 (prose pointer, as in prp-quantifier-passage's proof); nothing rests on it
exr-first-order-search-c1 (solution): QN (a), VI and passage (d) as one line | prp-quantifier-negation, prp-vacuous-implication, prp-quantifier-passage (cited, "The laws as one line", F1.8 §02)
exr-first-order-search-c1 (solution): the skeleton p -> p; the case split on which index serves | truth table; checked by verify/ch06/exr-first-order-search-c1.py
exr-first-order-search-c2 (solution): no even prime is greater than 2 | school fact; checked by verify/ch06/exr-first-order-search-c2.py
-->
