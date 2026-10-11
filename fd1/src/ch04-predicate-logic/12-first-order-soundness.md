# Soundness for Predicate Logic

This section is optional, and nothing outside it depends on it: Section 4.11 stated soundness for predicate logic without proof, and the rest of the book uses that statement. The results below build on one another, so they carry no optional marker of their own; the section as a whole is the unit a reader may skip. Here is the proof. It is Chapter 3's proof of @thm-soundness with six new cases, one for each quantifier and equality rule, and it is worth reading for one reason above all: each side condition of Sections 4.3 to 4.7 is used in the case of its own rule, and there one can see what would go wrong without it. The section proves a lemma about substitution and its corollary on renaming bound variables, then the theorem, then the corollary that turns every counter-model of Section 4.11 into a proof that no derivation exists.

## What carries over, and what is new

Chapter 3 proved that whatever the rules of Chapters 1 and 2 derive is true in every row where the premises are true. The proof had four steps (Steps 1–4 of the proof of @thm-soundness). It reduced to derivations in the primitive rules; it proved a claim for **every** line, not only the last, namely \( \Gamma_k \models \varphi_k \), where \( \Gamma_k \) is the context of line \( k \); it did so by strong induction on \( k \), one case per rule; and it read off the claim for the last line. We follow the same four steps. Three things change.

**The formulas.** Lines now carry first-order formulas (@def-first-order-formula), and \( \models \) is the entailment of @def-first-order-entailment: \( \Gamma_k \models \varphi_k \) says that every structure \( \fM \) and assignment \( \ell \) with \( \fM, \ell \models \Gamma_k \) satisfy \( \varphi_k \). Assignments are not optional here. Lines inside a flagged box can mention the box's name, a **variable** such as \( x_0 \), free; such a line is then not a sentence, and its truth depends on the value of \( x_0 \). This is why Section 4.4 insisted that fresh names are always variables, never constants: the proof below changes their values.

**The rules.** The primitive rules are the thirteen of Chapter 3's list (Section 3.5) and six new ones: \( \rulename{\forall E} \) (@def-rule-universal-elimination), \( \rulename{\forall I} \) (@def-rules-universal), \( \rulename{\exists I} \) (@def-rule-existential-introduction), \( \rulename{\exists E} \) (@def-rules-existential), \( \rulename{{=}I} \) and \( \rulename{{=}E} \) (@def-rules-equality). Two of the new rules cite a **box**, the flagged box of \( \rulename{\forall I} \) and the \( \rulename{\exists E} \) box, so the box rules are now seven: Chapter 3's five, and \( \rulename{\forall I} \) and \( \rulename{\exists E} \). The other four new rules cite only lines and join the one-step rules.

**Derived rules and "arith".** As in Step 1 of @thm-soundness, a line citing a derived rule abbreviates a pasted derivation in primitive rules. This covers Chapter 2's derived rules (@def-derived-rule), whose derivations have no flagged boxes and apply to first-order formulas as they stand, and the bounded rules of @prp-bounded-quantifier-rules, each of which Section 4.8 expanded into a displayed block of unbounded steps whose side conditions hold whenever the bounded ones do, and the one-line "(sym)" and "(trans)" of Section 4.7 (@prp-equality-symmetric-transitive), each of which abbreviates its three-line derivation from \( \rulename{{=}I} \) and \( \rulename{{=}E} \) with the given terms pasted in. Those derivations have no boxes, and each \( \varphi \) they use is an equation, with no quantifier, so every term is free for its variable and the side conditions of @def-rules-equality hold. A line justified "arith" is not a rule at all: it records an arithmetic fact. Written out, it is a universally quantified arithmetic sentence taken as an extra **premise**, whose bound variables are distinct and appear nowhere else in the derivation, instantiated by \( \rulename{\forall E} \) at the terms on the line and applied by \( \rulename{{\to}E} \), as Section 4.4 did explicitly when it turned the premises of a Chapter 1 derivation into universal statements. That choice of bound variables means that no fresh name of the derivation appears in the new premise, so the side conditions of \( \rulename{\forall I} \) and \( \rulename{\exists E} \) still hold, and that every term on the line is free for the variable it replaces at each \( \rulename{\forall E} \) step. So a derivation with "arith" lines is a derivation in primitive rules from its premises together with those arithmetic sentences, and soundness speaks about that derivation.

**Renaming.** Section 4.2 took, as a convention, that formulas differing only by renaming bound variables say the same thing, so a derivation may write a line, or apply a rule to a cited line, in a renamed form. This is not a rule either. @cor-renaming-bound-variables below shows that a formula and any renamed form of it are satisfied by exactly the same structures and assignments, so such a step changes nothing in the proof, which may take every line in the form its rule displays.

## Contexts, once more

The context \( \Gamma_k \) of line \( k \) is still the list of the premises together with the assumptions of every box containing line \( k \) (Section 1.5, recalled before @lem-context-inclusion). A flagged box of \( \rulename{\forall I} \) has **no** assumption, so it adds nothing to the context of the lines inside it. The \( \rulename{\exists E} \) box opens with its assumption \( \varphi[x_0/x] \), which does join the context.

Section 4.4 extended @def-derivation to flagged boxes and kept its scope rule and its notion of availability word for word; two boxes are still disjoint or one inside the other. So @lem-context-inclusion (a), whose proof uses only the scope rule, holds as it stands: if line \( i \) is available at line \( k \), then \( \Gamma_i \subseteq \Gamma_k \).

Part (b) needs one extension, since its statement names "the assumption of that box". It becomes: *if line \( k \) is justified by a box rule citing the box from line \( a \) to line \( b \), then \( \Gamma_b \) is \( \Gamma_k \) together with the assumption of that box if it has one, and \( \Gamma_b \) is \( \Gamma_k \) if it is a flagged box without an assumption.* The proof of (b) in Section 3.5 is unchanged. It showed that the boxes containing line \( b \) are exactly the cited box and the boxes containing line \( k \), and for that it used one fact about box rules: the last line of the cited box is a line of that box itself, not of a box inside it. The two new box rules demand the same: \( \rulename{\forall I} \) requires \( \varphi[x_0/x] \) to be the last line of the flagged box, a line of that box itself (@def-rules-universal), and \( \rulename{\exists E} \) requires \( \chi \) to be the last line of the box itself (@def-rules-existential). So the boxes containing line \( b \) are the cited box and those containing line \( k \), and the context of line \( b \) adds to \( \Gamma_k \) only the cited box's assumption, if any. When a flagged box immediately contains another box and is cited from the first line of that inner box, as the citation convention of Section 4.4 says, the argument is the same: the cited box runs from that line to its last line, and its last line lies in no box inside it.

Here is the derivation of @prp-exists-forall-swap, with its contexts.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, \forall y\, R(x, y)}
  \open[y_0]
  \open[x_0]
  \hypo {2} {\forall y\, R(x_0, y)}
  \have {3} {R(x_0, y_0)} \Ae{2}
  \have {4} {\exists x\, R(x, y_0)} \Ei{3}
  \close
  \have {5} {\exists x\, R(x, y_0)} \Ee{1,2-4}
  \close
  \have {6} {\forall y\, \exists x\, R(x, y)} \Ai{2-5}
\end{nd}$
\end{center}
```

| Line | Boxes containing it | Context |
|---|---|---|
| 1 | none | \( \exists x\, \forall y\, R(x, y) \) |
| 2, 3, 4 | flagged \( y_0 \) (\( \lines{2}{5} \)); \( \rulename{\exists E} \) box \( x_0 \) (\( \lines{2}{4} \)) | \( \exists x\, \forall y\, R(x, y), \ \forall y\, R(x_0, y) \) |
| 5 | flagged \( y_0 \) (\( \lines{2}{5} \)) | \( \exists x\, \forall y\, R(x, y) \) |
| 6 | none | \( \exists x\, \forall y\, R(x, y) \) |

Line 6 cites the flagged box \( \lines{2}{5} \), which has no assumption, and indeed \( \Gamma_5 = \Gamma_6 \). Line 5 cites the \( \rulename{\exists E} \) box \( \lines{2}{4} \), and \( \Gamma_4 \) is \( \Gamma_5 \) with its assumption \( \forall y\, R(x_0, y) \) added. Line 3 mentions \( x_0 \) and \( y_0 \) free, and line 4 mentions \( y_0 \) free, while its context mentions \( x_0 \) free, through the assumption \( \forall y\, R(x_0, y) \): the claim \( \Gamma_4 \models \exists x\, R(x, y_0) \) is about every structure **and every value** of \( x_0 \) and \( y_0 \) that makes the context true.

## Substitution and satisfaction

Five of the six new rules write a substitution: \( \rulename{\forall E} \) and \( \rulename{\exists I} \) write \( \varphi[t/x] \) for a term \( t \), in their conclusion or premise; \( \rulename{{=}E} \) writes one in both; and \( \rulename{\forall I} \) and \( \rulename{\exists E} \) write \( \varphi[x_0/x] \) for the fresh name. To handle them we need to know what \( \varphi[t/x] \) **means** in a structure. The natural guess is that substituting the term \( t \) for \( x \) has the same effect as giving \( x \) the value of \( t \). Section 4.2 showed that this can fail: in \( \exists y\, (y > x) \), putting \( y + 1 \) for \( x \) blindly gives \( \exists y\, (y > y + 1) \), which is false in \( \nZ \), while giving \( x \) the value of \( y + 1 \), whatever it is, leaves \( \exists y\, (y > x) \) true. The \( y \) of the term was captured. The lemma says that capture is the only thing that can go wrong.

::: {#lem-term-substitution}
[Substitution Lemma]

Let \( \fM \) be a structure, \( \ell \) an assignment in \( \fM \), \( \varphi \) a formula, \( x \) a variable, and \( t \) a term that is free for \( x \) in \( \varphi \) (@def-free-for). Write \( a \coloneqq t^{\fM, \ell} \). Then
\[
\fM, \ell \models \varphi[t/x] \quad \text{if and only if} \quad \fM, \ell[x \mapsto a] \models \varphi .
\]
:::

::: {.idea}
First terms: substituting \( t \) for \( x \) in a term \( s \) and then evaluating is the same as evaluating \( s \) with \( x \) set to the value of \( t \). Then structural induction on \( \varphi \), for all assignments at once, since the quantifier clauses change the assignment. Atomic formulas follow from the claim for terms, and connectives pass straight through. The only real case is \( \forall y\, \varphi \) with \( x \) free in it. The substitution goes inside, and (S6) sets \( y \) to each \( d \) in turn. For the induction hypothesis to help, the value of \( t \) must not change when \( y \) does, and that is exactly what "free for" guarantees: \( y \) does not occur in \( t \).
:::

::: {.proof}
Fix \( \fM \), \( x \) and \( t \). For an assignment \( \ell \), write \( a_\ell \coloneqq t^{\fM, \ell} \).

*Terms.* We show, for every term \( s \) and every assignment \( \ell \), that \( (s[t/x])^{\fM, \ell} = s^{\fM, \ell[x \mapsto a_\ell]} \), by structural induction on \( s \) (@def-term). If \( s \) is the variable \( x \), then \( s[t/x] \) is \( t \), with value \( a_\ell \), and \( s^{\fM, \ell[x \mapsto a_\ell]} = \ell[x \mapsto a_\ell](x) = a_\ell \) (@def-assignment). If \( s \) is another variable \( y \), then \( s[t/x] \) is \( y \), and both sides are \( \ell(y) \), since \( \ell[x \mapsto a_\ell] \) changes only \( x \). If \( s \) is a constant \( c \), both sides are \( c^{\fM} \). If \( s \) is \( f(s_1, \dots, s_n) \), then \( s[t/x] \) is \( f(s_1[t/x], \dots, s_n[t/x]) \) (@def-substitution), and applying \( f^{\fM} \) to the values, which agree by the hypothesis for \( s_1, \dots, s_n \), gives equal results.

*Formulas.* We prove, by structural induction on \( \varphi \), the property \( B(\varphi) \): *if \( t \) is free for \( x \) in \( \varphi \), then for every assignment \( \ell \), \( \fM, \ell \models \varphi[t/x] \) if and only if \( \fM, \ell[x \mapsto a_\ell] \models \varphi \).* Two facts are used throughout. If \( t \) is free for \( x \) in \( \neg\varphi \) or in \( \varphi \circ \psi \), it is free for \( x \) in the parts, by the recursive description of "free for" after @def-free-for in Section 4.2. And by @def-substitution, substitution passes through connectives: \( (\neg\varphi)[t/x] \) is \( \neg(\varphi[t/x]) \), and \( (\varphi \circ \psi)[t/x] \) is \( \varphi[t/x] \circ \psi[t/x] \).

*Atomic formulas.* \( R(s_1, \dots, s_n)[t/x] \) is \( R(s_1[t/x], \dots, s_n[t/x]) \). By the claim for terms, the tuple of values of the \( s_i[t/x] \) under \( \ell \) is the tuple of values of the \( s_i \) under \( \ell[x \mapsto a_\ell] \), so (S1) of @def-satisfaction gives the same answer on both sides. Equations \( s_1 = s_2 \) are the same with (S2). For \( \bot \), \( \bot[t/x] \) is \( \bot \), and neither side holds (S3).

*Connectives.* For \( \varphi \wedge \psi \): by \( B(\varphi) \) and \( B(\psi) \), \( \fM, \ell \models \varphi[t/x] \) if and only if \( \fM, \ell[x \mapsto a_\ell] \models \varphi \), and likewise for \( \psi \); (S5) combines the two answers in the same way on both sides. The cases \( \neg \), \( \vee \), \( \to \), \( \leftrightarrow \) are the same with (S4) and the other parts of (S5).

*Universal quantifier, \( x \) not free in \( \forall y\, \varphi \).* This happens when \( y \) is the variable \( x \), or when \( x \) is not free in \( \varphi \). Then \( (\forall y\, \varphi)[t/x] \) is \( \forall y\, \varphi \) itself, since there is no free occurrence of \( x \) to replace (Section 4.2 proved that \( \psi[t/x] = \psi \) whenever \( x \) is not free in \( \psi \)). The assignments \( \ell \) and \( \ell[x \mapsto a_\ell] \) differ at most at \( x \), which is not free in \( \forall y\, \varphi \); so by @lem-free-coincidence, \( \fM, \ell \models \forall y\, \varphi \) if and only if \( \fM, \ell[x \mapsto a_\ell] \models \forall y\, \varphi \), which is \( B(\forall y\, \varphi) \).

*Universal quantifier, \( x \) free in \( \forall y\, \varphi \).* Then \( y \) is not \( x \), and \( x \) is free in \( \varphi \). Every free occurrence of \( x \) in \( \forall y\, \varphi \) lies in the scope of \( \forall y \), so, as \( t \) is free for \( x \) in \( \forall y\, \varphi \), **the variable \( y \) does not occur in \( t \)**, and \( t \) is free for \( x \) in \( \varphi \) (@def-free-for, and its recursive description in Section 4.2). By @def-substitution, \( (\forall y\, \varphi)[t/x] \) is \( \forall y\, (\varphi[t/x]) \). Let \( d \in D \). Since \( y \) does not occur in \( t \), the assignments \( \ell \) and \( \ell[y \mapsto d] \) agree on every variable of \( t \), so \( a_{\ell[y \mapsto d]} = a_\ell \), by the claim for terms in the proof of @lem-free-coincidence. Since \( x \) and \( y \) are different variables, \( \ell[y \mapsto d][x \mapsto a_\ell] = \ell[x \mapsto a_\ell][y \mapsto d] \). Hence, using \( B(\varphi) \) for the assignment \( \ell[y \mapsto d] \) in the second step,
\[
\begin{aligned}
\fM, \ell \models \forall y\, (\varphi[t/x])
&\iff \text{for every } d \in D, \ \fM, \ell[y \mapsto d] \models \varphi[t/x] \\
&\iff \text{for every } d \in D, \ \fM, \ell[y \mapsto d][x \mapsto a_\ell] \models \varphi \\
&\iff \text{for every } d \in D, \ \fM, \ell[x \mapsto a_\ell][y \mapsto d] \models \varphi \\
&\iff \fM, \ell[x \mapsto a_\ell] \models \forall y\, \varphi ,
\end{aligned}
\]
where the first and last steps are (S6). This is \( B(\forall y\, \varphi) \).

*Existential quantifier.* The same two subcases, with (S7) in place of (S6) and "for some \( d \)" in place of "for every \( d \)".

Every clause of @def-first-order-formula is covered, so \( B(\varphi) \) holds for every formula. This proves the lemma.
:::

The hypothesis "free for" was used once, in the second quantifier case, to get \( a_{\ell[y \mapsto d]} = a_\ell \). The capture example shows what happens without it. In the structure on \( \nZ \) with \( > \), \( + \), and \( 1 \) as usual, take \( \varphi = \exists y\, (y > x) \) and \( t = y + 1 \), which is **not** free for \( x \) in \( \varphi \). The blind substitution is \( \exists y\, (y > y + 1) \), false under every assignment. But \( \fM, \ell[x \mapsto a] \models \exists y\, (y > x) \) holds for every \( a \in \nZ \), with witness \( a + 1 \). The two sides of the lemma disagree, and the reason is visible in the displayed chain: when (S7) sets \( y \) to a new value, the value of \( y + 1 \) moves with it.

::: {.check}
Let \( \fM \) be the structure on \( \nZ \) with \( < \), \( + \), and \( 1 \) as usual, \( \varphi = \forall z\, (x < z \to y < z) \), \( t = y + 1 \), and let \( \ell(x) = 3 \), \( \ell(y) = 5 \). Is \( t \) free for \( x \) in \( \varphi \)? Compute both sides of @lem-term-substitution.
:::

::: {.solution}
Yes: the only quantifier in \( \varphi \) is \( \forall z \), and \( z \) does not occur in \( y + 1 \). Here \( a = t^{\fM, \ell} = 6 \). The right side asks whether \( \fM, \ell[x \mapsto 6] \models \varphi \): every \( z > 6 \) is \( > 5 \), so yes. The left side is \( \varphi[t/x] = \forall z\, (y + 1 < z \to y < z) \) under \( \ell \): every \( z > 6 \) is \( > 5 \), so yes. Both sides hold, as the lemma says. (Under \( \ell \) itself, \( \varphi \) is false: \( z = 4 \) has \( 3 < 4 \) and not \( 5 < 4 \). The lemma compares \( \varphi[t/x] \) with \( \varphi \) at the **new** value of \( x \), not at the old one.)
:::

The lemma also pays a debt of Section 4.2, which took renaming of bound variables inside a formula as a convention and left its justification in terms of meaning to this section.

::: {#cor-renaming-bound-variables}
[Renaming Keeps Meaning]

Let \( \varphi \) be a formula and \( y, z \) variables, with \( z \) not appearing in \( \varphi \) (Section 4.2). Let \( \fM \) be a structure for the symbols of \( \varphi \), with domain \( D \).

::: {.enumerate options="label=(\alph*)"}
1. For every assignment \( \ell \), \( \fM, \ell \models \forall y\, \varphi \) if and only if \( \fM, \ell \models \forall z\, \varphi[z/y] \), and \( \fM, \ell \models \exists y\, \varphi \) if and only if \( \fM, \ell \models \exists z\, \varphi[z/y] \).
2. If \( \psi' \) arises from a formula \( \psi \) by such a renaming of one quantifier anywhere inside \( \psi \) (Section 4.2), then for every structure \( \fM \) for the symbols of \( \psi \) and every assignment \( \ell \) in it, \( \fM, \ell \models \psi \) if and only if \( \fM, \ell \models \psi' \).
:::
:::

::: {.proof}
*(a)* If \( z \) is \( y \), then \( \varphi[y/y] \) is \( \varphi \) and there is nothing to prove. Let \( z \) be a variable other than \( y \). Since \( z \) does not appear in \( \varphi \), no quantifier of \( \varphi \) is on \( z \), so \( z \) is free for \( y \) in \( \varphi \) (@def-free-for). Let \( d \in D \). Under \( \ell[z \mapsto d] \) the term \( z \) has value \( d \), so @lem-term-substitution gives: \( \fM, \ell[z \mapsto d] \models \varphi[z/y] \) if and only if \( \fM, \ell[z \mapsto d][y \mapsto d] \models \varphi \). The assignments \( \ell[z \mapsto d][y \mapsto d] \) and \( \ell[y \mapsto d] \) differ at most at \( z \), which does not appear in \( \varphi \); by @lem-free-coincidence, the last statement holds if and only if \( \fM, \ell[y \mapsto d] \models \varphi \). So \( \fM, \ell[z \mapsto d] \models \varphi[z/y] \) if and only if \( \fM, \ell[y \mapsto d] \models \varphi \), for every \( d \in D \). Now (S6) gives the statement for \( \forall \), and (S7) the statement for \( \exists \).

*(b)* By structural induction on \( \psi \), for all assignments at once, since the quantifier clauses change the assignment. If the renamed quantifier is the outermost symbol of \( \psi \), this is (a). Otherwise \( \psi \) is not atomic, and the renaming takes place inside one immediate part of \( \psi \), which it turns into a formula satisfied by the same assignments, by the induction hypothesis; the other parts are unchanged. If \( \psi \) is \( \neg\alpha \) or \( \alpha \circ \beta \), (S4) or (S5) then gives the same answer for \( \psi \) and \( \psi' \) under every \( \ell \). If \( \psi \) is \( \forall w\, \alpha \) or \( \exists w\, \alpha \), with the renaming inside \( \alpha \), then \( \psi' \) is \( \forall w\, \alpha' \) or \( \exists w\, \alpha' \), and \( \alpha \), \( \alpha' \) are satisfied by the same assignments \( \ell[w \mapsto d] \), so (S6) or (S7) gives the same answer for \( \psi \) and \( \psi' \).
:::

Several renamings one after another are covered by applying (b) once for each.

## The soundness theorem

We can now state the theorem that Section 4.11 took on trust.

::: {#thm-first-order-soundness}
[Soundness for Predicate Logic]

Let \( \Gamma \) be a list of formulas and \( \psi \) a formula. If \( \Gamma \vdash \psi \) with the rules of Chapters 1 and 2 and the quantifier and equality rules of Sections 4.3 to 4.7, then \( \Gamma \models \psi \) (@def-first-order-entailment).
:::

::: {.idea}
The steps are those of Chapter 3's proof (Steps 1–4 of @thm-soundness).

① Reduce to derivations in the primitive rules.

② Prove \( \Gamma_k \models \varphi_k \) for every line \( k \), by strong induction on \( k \) (@thm-strong-induction): fix a structure \( \fM \) and an assignment \( \ell \) satisfying \( \Gamma_k \), and show that they satisfy \( \varphi_k \).

③ The cases. Premises, assumptions, and the thirteen propositional rules go through word for word, because (S3)–(S5) are Chapter 3's clauses. \( \rulename{\forall E} \), \( \rulename{\exists I} \), and \( \rulename{{=}E} \) are @lem-term-substitution, used once or twice. \( \rulename{{=}I} \) is (S2). The two box rules are the heart of the proof, and they both use the same trick: **change the value of the fresh name**. In \( \rulename{\forall I} \), to show \( \forall x\, \varphi \) under \( \ell \), take any \( d \), and set \( x_0 \) to \( d \); the context does not notice, because \( x_0 \) is not in it, so the box's last line \( \varphi[x_0/x] \) holds there, and moving \( d \) from \( x_0 \) to \( x \) gives \( \varphi \) under \( \ell[x \mapsto d] \). In \( \rulename{\exists E} \), set \( x_0 \) to the witness \( d \) that \( \exists x\, \varphi \) provides; the box's assumption holds there, so its last line \( \chi \) holds there, and since \( \chi \) does not mention \( x_0 \), it holds under \( \ell \) as well.

④ The last line lies in no box, so its context is the premises.

*Before reading on: in the \( \rulename{\forall I} \) case below, the assignment \( \ell[x_0 \mapsto d] \) must still satisfy the context \( \Gamma_k \), and at the end the conclusion must come back from \( \ell[x_0 \mapsto d][x \mapsto d] \) to \( \ell[x \mapsto d] \). Which clause of the side condition of \( \rulename{\forall I} \) does each step use?*
:::

::: {.proof}
**Step 1 (reduction).** Suppose \( \Gamma \vdash \psi \). By the subsection "What carries over, and what is new", there is a derivation of \( \psi \) in the primitive rules whose premises all belong to \( \Gamma \). (A derivation with "arith" lines is of this kind only for the list of its premises together with the arithmetic sentences \( A \) those lines stand for, as explained there. The theorem applies to it with the list \( \Gamma, A \) in place of \( \Gamma \), and gives \( \Gamma, A \models \psi \): truth in every structure that satisfies \( \Gamma \) and \( A \). The sentences \( A \) hold, for instance, when the arithmetic symbols have their usual meaning on \( \nR \), as in Section 4.11.) Fix one, with lines \( 1, \dots, n \), formulas \( \varphi_k \), and contexts \( \Gamma_k \). Let \( \Sigma \) be the finite set of constants, function symbols and predicate symbols that occur in some line of it. A line may contain symbols that occur neither in \( \Gamma \) nor in \( \psi \), as \( c \) does in the line \( P(c) \) between \( \forall x\, P(x) \) and \( \exists x\, P(x) \); so the induction is run over structures that interpret every symbol of \( \Sigma \), and Step 4 returns to the structures of @def-first-order-entailment.

**Step 2 (the induction).** For \( k \in \nN \), let \( S(k) \) be: *if \( 1 \le k \le n \), then every structure \( \fM \) that interprets every symbol of \( \Sigma \) and every assignment \( \ell \) in \( \fM \) with \( \fM, \ell \models \Gamma_k \) satisfy \( \fM, \ell \models \varphi_k \).* In Steps 2 and 3, "structure" means a structure that interprets every symbol of \( \Sigma \), and possibly more. We prove \( S(k) \) for all \( k \) by @thm-strong-induction. For \( k = 0 \) and \( k > n \), \( S(k) \) holds vacuously. Let \( 1 \le k \le n \) and assume \( S(j) \) for every \( j < k \). Every line and box that line \( k \) cites is available at line \( k \), so lies before it (@def-derivation); hence the hypothesis holds for every cited line and for the last line of every cited box. Let \( \fM \) be a structure, with domain \( D \), and \( \ell \) an assignment with \( \fM, \ell \models \Gamma_k \). We show \( \fM, \ell \models \varphi_k \). Two consequences of the hypothesis do the bookkeeping, as in the proof of @thm-soundness. If line \( k \) cites line \( i \), then \( \Gamma_i \subseteq \Gamma_k \) by @lem-context-inclusion (a), so \( \fM, \ell \models \Gamma_i \), and \( S(i) \) gives
\[
\fM, \ell \models \varphi_i \quad \text{for every line } i \text{ cited by line } k . \tag{$\ast$}
\]
If line \( k \) cites, by a box rule, the box from line \( a \) to line \( b \), then by @lem-context-inclusion (b), extended in the subsection "Contexts, once more", and \( S(b) \):
\[
\text{every structure and assignment satisfying } \Gamma_k \text{ and the box's assumption, if any, satisfy } \varphi_b . \tag{$\ast\ast$}
\]

**Step 3 (the cases).**

::: {.claim}
If line \( k \) is a premise, an assumption, or justified by one of the thirteen primitive rules of Chapters 1 and 2, then \( \fM, \ell \models \varphi_k \).
:::

::: {.proofofclaim}
Claims 1–3 in the proof of @thm-soundness treat these cases. Each step there uses only \( (\ast) \), \( (\ast\ast) \), the fact that a premise or an assumption belongs to its own context, and the clauses (V1)–(V6) of @def-truth-value. Clauses (S3)–(S5) of @def-satisfaction are (V1)–(V6) with "\( v \) makes \( \varphi \) true" replaced by "\( \fM, \ell \models \varphi \)". Making that replacement throughout, the proofs of those claims prove this one, case by case.
:::

::: {.claim}
If line \( k \) is justified by \( \rulename{\forall E} \), \( \rulename{\exists I} \), \( \rulename{{=}I} \), or \( \rulename{{=}E} \), then \( \fM, \ell \models \varphi_k \).
:::

::: {.proofofclaim}
*\( \rulename{\forall E} \).* Line \( k \) is \( \varphi[t/x] \), citing a line holding \( \forall x\, \varphi \), with \( t \) free for \( x \) in \( \varphi \). By \( (\ast) \), \( \fM, \ell \models \forall x\, \varphi \), so by (S6), \( \fM, \ell[x \mapsto d] \models \varphi \) for every \( d \in D \), in particular for \( d = t^{\fM, \ell} \). By @lem-term-substitution, which applies because \( t \) is free for \( x \) in \( \varphi \), \( \fM, \ell \models \varphi[t/x] \).

*\( \rulename{\exists I} \).* Line \( k \) is \( \exists x\, \varphi \), citing a line holding \( \varphi[t/x] \), with \( t \) free for \( x \) in \( \varphi \). By \( (\ast) \), \( \fM, \ell \models \varphi[t/x] \). By @lem-term-substitution, \( \fM, \ell[x \mapsto d] \models \varphi \) with \( d = t^{\fM, \ell} \in D \). So \( d \) is the element (S7) asks for, and \( \fM, \ell \models \exists x\, \varphi \).

*\( \rulename{{=}I} \).* Line \( k \) is \( t = t \). The two sides have the same value \( t^{\fM, \ell} \), so (S2) holds.

*\( \rulename{{=}E} \).* Line \( k \) is \( \varphi[t_2/x] \), citing lines holding \( t_1 = t_2 \) and \( \varphi[t_1/x] \), with \( t_1 \) and \( t_2 \) free for \( x \) in \( \varphi \). By \( (\ast) \) and (S2), \( t_1^{\fM, \ell} \) and \( t_2^{\fM, \ell} \) are the same element \( d \); and \( \fM, \ell \models \varphi[t_1/x] \). By @lem-term-substitution for \( t_1 \), \( \fM, \ell[x \mapsto d] \models \varphi \). By @lem-term-substitution for \( t_2 \), read from right to left, \( \fM, \ell \models \varphi[t_2/x] \).
:::

::: {.claim}
If line \( k \) is justified by \( \rulename{\forall I} \) or \( \rulename{\exists E} \), then \( \fM, \ell \models \varphi_k \).
:::

::: {.proofofclaim}
*\( \rulename{\forall I} \).* Line \( k \) is \( \forall x\, \varphi \), citing a flagged box with name \( x_0 \) and no assumption, whose last line \( b \) holds \( \varphi[x_0/x] \). The side condition of @def-rules-universal says that at line \( k \) the name \( x_0 \) appears in no premise and in no assumption of a box still open at line \( k \), and not in \( \forall x\, \varphi \). The premises and the assumptions of the boxes open at line \( k \) are exactly the formulas of \( \Gamma_k \), so

(i) \( x_0 \) appears in no formula of \( \Gamma_k \); and

(ii) \( x_0 \) does not appear in \( \forall x\, \varphi \), so \( x_0 \) is not the variable \( x \), and \( x_0 \) does not appear in \( \varphi \).

The flagged box has no assumption, so \( (\ast\ast) \) says: every structure and assignment satisfying \( \Gamma_k \) satisfy \( \varphi[x_0/x] \).

Let \( d \in D \); we show \( \fM, \ell[x \mapsto d] \models \varphi \). Put \( \ell' \coloneqq \ell[x_0 \mapsto d] \). It differs from \( \ell \) at most at \( x_0 \), which by (i) is free in no formula of \( \Gamma_k \); so by @lem-free-coincidence, \( \fM, \ell' \models \Gamma_k \). **This is where the fresh-name condition is used:** changing the value of \( x_0 \) cannot disturb anything we assumed. By \( (\ast\ast) \), \( \fM, \ell' \models \varphi[x_0/x] \). By (ii), \( x_0 \) does not appear in \( \varphi \), so no quantifier of \( \varphi \) is on \( x_0 \), and the term \( x_0 \) is free for \( x \) in \( \varphi \) (@def-free-for). Its value under \( \ell' \) is \( d \), so @lem-term-substitution gives
\[
\fM, \ell[x_0 \mapsto d][x \mapsto d] \models \varphi .
\]
The assignments \( \ell[x_0 \mapsto d][x \mapsto d] \) and \( \ell[x \mapsto d] \) agree at \( x \), where both give \( d \), and at every variable other than \( x \) and \( x_0 \), where both give the value \( \ell \) gives. They can differ only at \( x_0 \), which by (ii) does not appear in \( \varphi \). By @lem-free-coincidence, \( \fM, \ell[x \mapsto d] \models \varphi \). Since \( d \in D \) was arbitrary, (S6) gives \( \fM, \ell \models \forall x\, \varphi \).

*\( \rulename{\exists E} \).* Line \( k \) is \( \chi \), citing a line \( h \) holding \( \exists x\, \varphi \) and a box with name \( x_0 \) that opens with the assumption \( \varphi[x_0/x] \) and ends with \( \chi \). The side condition of @def-rules-existential says that \( x_0 \) appears neither in \( \chi \), nor in \( \exists x\, \varphi \), nor in any premise, nor in any assumption of a box still open at line \( k \). So

(i) \( x_0 \) appears in no formula of \( \Gamma_k \);

(ii) \( x_0 \) is not \( x \), and does not appear in \( \varphi \);

(iii) \( x_0 \) does not appear in \( \chi \).

By \( (\ast\ast) \), every structure and assignment satisfying \( \Gamma_k \) and \( \varphi[x_0/x] \) satisfy \( \chi \).

By \( (\ast) \) for line \( h \), \( \fM, \ell \models \exists x\, \varphi \); by (S7), choose \( d \in D \) with \( \fM, \ell[x \mapsto d] \models \varphi \). Put \( \ell' \coloneqq \ell[x_0 \mapsto d] \). First, \( \fM, \ell' \models \Gamma_k \), by (i) and @lem-free-coincidence, as in the \( \rulename{\forall I} \) case. Second, \( \fM, \ell' \models \varphi[x_0/x] \). Indeed, \( \ell'[x \mapsto d] = \ell[x_0 \mapsto d][x \mapsto d] \) and \( \ell[x \mapsto d] \) differ at most at \( x_0 \), which by (ii) does not appear in \( \varphi \), so \( \fM, \ell'[x \mapsto d] \models \varphi \) by @lem-free-coincidence; the term \( x_0 \) is free for \( x \) in \( \varphi \) by (ii), and has value \( d \) under \( \ell' \), so @lem-term-substitution gives \( \fM, \ell' \models \varphi[x_0/x] \). **This is where "\( x_0 \) not in \( \exists x\, \varphi \)" is used.** By \( (\ast\ast) \), \( \fM, \ell' \models \chi \). Finally, \( \ell' \) and \( \ell \) differ at most at \( x_0 \), which by (iii) does not appear in \( \chi \), so \( \fM, \ell \models \chi \) by @lem-free-coincidence. **This is where "\( x_0 \) not in \( \chi \)" is used.**
:::

The three claims cover every way a line can be justified, so \( S(k) \) holds, and by @thm-strong-induction \( S(k) \) holds for every line \( k \) of the derivation.

**Step 4 (the last line).** The last line \( n \) lies in no box (@def-derivation), so \( \Gamma_n \) consists of premises only, and \( \varphi_n = \psi \). Let \( \fM \) be a structure for the symbols occurring in \( \Gamma \) and \( \psi \), with domain \( D \), and \( \ell \) an assignment with \( \fM, \ell \models \Gamma \). Expand \( \fM \) to a structure \( \fM' \) with the same domain and the same meanings, which also interprets the symbols of \( \Sigma \) that \( \fM \) does not, so that \( \fM' \) interprets every symbol of \( \Sigma \): fix some \( e \in D \), which exists because \( D \) is non-empty (M1), and give each new constant the value \( e \), each new function symbol, of arity \( m \) say, the function \( D^m \to D \) with constant value \( e \), and each new predicate symbol the empty relation. Then \( \ell \) is an assignment in \( \fM' \), and by the remark after @def-first-order-entailment (the clauses of @def-satisfaction consult only the symbols of the formula at hand), each formula of \( \Gamma \), and \( \psi \), is satisfied by \( \fM', \ell \) exactly when it is satisfied by \( \fM, \ell \). Every premise belongs to \( \Gamma \), so \( \fM', \ell \models \Gamma_n \); by \( S(n) \), \( \fM', \ell \models \psi \); and so \( \fM, \ell \models \psi \). This proves \( \Gamma \models \psi \).
:::

The answer to the prompt: the first step uses the clauses "no premise" and "no open assumption", which together say that \( x_0 \) is not in \( \Gamma_k \); the second uses "not in \( \forall x\, \varphi \)". The last line \( \varphi[x_0/x] \) of the box, which may mention \( x_0 \) as often as it likes, plays no part in either. That is the precise sense in which "let \( x_0 \) be arbitrary" works: whatever value \( x_0 \) is given, what we know still holds, so what we proved about \( x_0 \) holds at that value.

The \( \rulename{\exists E} \) case uses the same move with the opposite purpose. There the value of \( x_0 \) is **not** arbitrary; it is set to the witness \( d \). What makes that legitimate is that nothing else knows about \( x_0 \) (condition (i)), that the assumption \( \varphi[x_0/x] \) then holds at the witness (condition (ii)), and that the result \( \chi \) forgets it again (condition (iii)).

## Counter-models prove nonderivability {#counter-models-prove-non-derivability}

The corollary is the one Section 4.11 used, now with a proof.

::: {#cor-counter-model}
[Counter-models]

Let \( \Gamma \) be a list of formulas and \( \psi \) a formula. If some structure \( \fM \) and assignment \( \ell \) satisfy every formula of \( \Gamma \) and do not satisfy \( \psi \), then \( \Gamma \nvdash \psi \).
:::

::: {.proof}
The pair \( \fM, \ell \) shows that \( \Gamma \models \psi \) fails (@def-first-order-entailment). If \( \Gamma \vdash \psi \) held, @thm-first-order-soundness would give \( \Gamma \models \psi \). So \( \Gamma \vdash \psi \) does not hold.
:::

If the derivations in question may use "arith" lines, a counter-model must also satisfy the arithmetic sentences those lines stand for (Step 1 of the proof of @thm-first-order-soundness), for instance by giving the arithmetic symbols their usual meaning.

Every counter-model of Section 4.11 is now a proof that no derivation exists.

- By @exm-counter-model-swap, \( \forall y\, \exists x\, R(x, y) \nvdash \exists x\, \forall y\, R(x, y) \). The converse search of @prp-exists-forall-swap stalled at two lines, a \( \rulename{\forall I} \) blocked by an open assumption and an \( \rulename{\exists E} \) blocked by its conclusion; now we know that no other route could have succeeded.
- The two-element structure with \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \) gives \( \exists x\, P(x) \wedge \exists x\, Q(x) \nvdash \exists x\, (P(x) \wedge Q(x)) \) and \( \forall x\, (P(x) \vee Q(x)) \nvdash \forall x\, P(x) \vee \forall x\, Q(x) \): the one-way laws of @prp-quantifier-distribution are one-way.
- \( \exists x\, P(x) \nvdash P(c) \), which @exr-existential-introduction-c2 could only explain informally.
- \( P(x_0) \nvdash \forall x\, P(x) \), by the structure on \( \nZ \) with \( P^{\fM} \) the even integers and \( \ell(x_0) = 2 \): generalizing over a name in a premise is not merely forbidden, it would be unsound.
- The passage laws of @prp-quantifier-passage need \( x \) not free in \( \psi \): with \( x \) free, \( \nvdash \exists x\, P(x) \to P(x) \), by the counter-model of @exr-models-b1 (iii), which names an assignment.

::: {.remark}
The converse of @thm-first-order-soundness is also true: if \( \Gamma \models \psi \), then \( \Gamma \vdash \psi \). This is the **completeness theorem** for predicate logic, proved by Gödel in 1929. Its proof needs to build a structure out of the formulas themselves, and it is beyond this book; nothing here depends on it.
:::

::: {.remark}
One difference from Chapter 3 remains even with completeness: there is no truth table to check. Whether a sentence of predicate logic is derivable cannot, in general, be decided by any mechanical procedure (Church and Turing, 1936). A failed search and a missing counter-model can both go on for ever.
:::

## Every side condition is a case of the proof

The side conditions of Sections 4.3 to 4.7 were introduced one at a time, each with a counterexample. The proof above shows that they are all the same kind of thing: each is used in the case of its own rule, and dropping it breaks a step of that case. Each counterexample of Sections 4.3 to 4.7 can be read as a failed case:

- generalizing over a name in a premise, as in "\( P(x_0) \vdash \forall x\, P(x) \)" (Section 4.4): the \( \rulename{\forall I} \) case fails at "\( \fM, \ell[x_0 \mapsto d] \models \Gamma_k \)", since changing \( x_0 \) changes the premise \( P(x_0) \);
- generalizing over a name in an open assumption, as in "from \( x_0 > 0 \), \( \forall x\, (x > 0) \)" (Section 4.4): the same step, with the assumption \( x_0 > 0 \) in \( \Gamma_k \);
- a name that leaks into the conclusion of \( \rulename{\forall I} \), as in @exr-existential-introduction-c1: the last step of the \( \rulename{\forall I} \) case, since \( x_0 \) now occurs in \( \varphi \);
- treating the witness as arbitrary, by \( \rulename{\forall I} \) over its name inside its \( \rulename{\exists E} \) box (Section 4.6): the \( \rulename{\forall I} \) case again, since the box's assumption is in \( \Gamma_k \);
- letting the witness escape its box, or giving a second witness a name already in an open assumption (Section 4.6): the \( \rulename{\exists E} \) case, at condition (iii) or (i);
- a capture in \( \rulename{\forall E} \) (Section 4.3) or \( \rulename{\exists I} \) (Section 4.5): the \( \rulename{\forall E} \) or \( \rulename{\exists I} \) case, where @lem-term-substitution does not apply; Exercise C2 and the solution to Exercise B1 give false conclusions;
- a capture in \( \rulename{{=}E} \), as in \( a = y, \ \exists y\, (y < a) \vdash \exists y\, (y < y) \) (Section 4.7): the \( \rulename{{=}E} \) case, where @lem-term-substitution does not apply to \( t_2 \).

::: {.warning}
A side condition is not mere bookkeeping: a derivation that breaks one is not covered by @thm-first-order-soundness, and it can reach a false line, as the counter-model to \( P(x_0) \vdash \forall x\, P(x) \) in the previous subsection shows for the first item of the list.
:::

::: {.check}
@exr-existential-elimination-c2 gives a derivation of \( \exists x\, (P(x) \wedge Q(x)) \vdash \exists x\, P(x) \) whose \( \rulename{\exists E} \) box ends in \( P(x_0) \); the line after the box is \( P(x_0) \) by \( \rulename{\exists E} \), and the last line is \( \exists x\, P(x) \) by \( \rulename{\exists I} \). Which case of the proof of @thm-first-order-soundness fails, at which step, and for which line? Give a structure and an assignment showing that the claim \( \Gamma_k \models \varphi_k \) is false for that line.
:::

::: {.solution}
The \( \rulename{\exists E} \) case fails, at its last step: \( \chi = P(x_0) \) contains \( x_0 \), so condition (iii) is false, and "\( \fM, \ell' \models \chi \)" cannot be carried back from \( \ell' = \ell[x_0 \mapsto d] \) to \( \ell \). The line concerned is the illegal \( \rulename{\exists E} \) line \( P(x_0) \), whose context is the premise alone. Take \( D = \{ a, b \} \), \( P^{\fM} = Q^{\fM} = \{ a \} \) and \( \ell(x_0) = b \): the premise \( \exists x\, (P(x) \wedge Q(x)) \) holds (witness \( a \)), and \( P(x_0) \) fails, since \( b \notin P^{\fM} \). The final conclusion \( \exists x\, P(x) \) is still true in this structure, as it is in every structure satisfying the premise; the fault is in the line before it.
:::

## Exercises

### A. Check your understanding

::: {#exr-first-order-soundness-a1}
[A1]

These parts are about the proof of @thm-first-order-soundness.

::: {.enumerate options="label=(\alph*)"}
1. In the \( \rulename{\forall I} \) case, name the two places where the side condition of \( \rulename{\forall I} \) is used, and say which clause each uses.
2. The derivation below breaks the side condition of \( \rulename{\exists E} \): its conclusion \( P(x_0) \) contains the fresh name. Which step of the \( \rulename{\exists E} \) case fails? Give a structure and an assignment in which the premise holds and line 3 does not.
3. Give the idea of the proof in two sentences.
4. Why does the claim \( \Gamma_k \models \varphi_k \) quantify over assignments, and not only over structures? Point to a line of the derivation of @prp-exists-forall-swap printed in this section.
:::

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, P(x)}
  \open[x_0]
  \hypo {2} {P(x_0)}
  \close
  \have {3} {P(x_0)} \Ee{1,2-2}
\end{nd}$
\end{center}
```
:::

::: {.solution}
*(a)* First, to show that \( \ell[x_0 \mapsto d] \) still satisfies \( \Gamma_k \): this uses "\( x_0 \) appears in no premise and in no assumption of a box open at line \( k \)", which together say that \( x_0 \) is in no formula of \( \Gamma_k \), so @lem-free-coincidence applies. Second, to pass from \( \ell[x_0 \mapsto d][x \mapsto d] \) to \( \ell[x \mapsto d] \) (and, before that, to know that \( x_0 \) is free for \( x \) in \( \varphi \)): this uses "\( x_0 \) does not appear in \( \forall x\, \varphi \)".

*(b)* The last step: from \( \fM, \ell[x_0 \mapsto d] \models \chi \) to \( \fM, \ell \models \chi \), which needs \( x_0 \) not in \( \chi \). Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( \ell(x_0) = b \). The premise \( \exists x\, P(x) \) holds, with witness \( a \); line 3, \( P(x_0) \), fails, since \( \ell(x_0) = b \notin P^{\fM} \). Inside the box, under \( \ell[x_0 \mapsto a] \), line 2 holds; the proof would carry it back to \( \ell \), and that is exactly what fails.

*(c)* Every line of a derivation is satisfied by every structure and assignment that satisfy its context, by strong induction on the line, with one case per rule. The quantifier box rules are handled by changing the value of the fresh name, which the side conditions guarantee the context and the conclusion cannot notice.

*(d)* Lines inside boxes contain free variables, the fresh names, and their truth depends on the values of those variables. Line 3, \( R(x_0, y_0) \), is not a sentence: in the structure on \( \nZ \) with \( R \) read as \( < \), it is satisfied when \( \ell(x_0) = 1 \), \( \ell(y_0) = 2 \), and not when \( \ell(x_0) = 2 \), \( \ell(y_0) = 1 \). The \( \rulename{\forall I} \) and \( \rulename{\exists E} \) cases work precisely by changing such values.
:::

### B. Practice

::: {#exr-first-order-soundness-b1}
[B1: The \( \rulename{\exists I} \) case]

Write out the \( \rulename{\exists I} \) case of the proof of @thm-first-order-soundness in full: state what is known about the cited line, and show \( \fM, \ell \models \exists x\, \varphi \), naming the reason for each step. Where is "\( t \) free for \( x \) in \( \varphi \)" used?
:::

::: {.solution}
Line \( k \) is \( \exists x\, \varphi \), by \( \rulename{\exists I} \) citing a line \( i \) holding \( \varphi[t/x] \), where \( t \) is free for \( x \) in \( \varphi \) (@def-rule-existential-introduction). Let \( \fM \) be a structure interpreting every symbol of the derivation (as in Step 2), with domain \( D \), and \( \ell \) an assignment with \( \fM, \ell \models \Gamma_k \). Line \( i \) is available at line \( k \), so \( \Gamma_i \subseteq \Gamma_k \) by @lem-context-inclusion (a), and \( \fM, \ell \models \Gamma_i \). Since \( i < k \), the induction hypothesis \( S(i) \) gives \( \fM, \ell \models \varphi[t/x] \). Let \( d \coloneqq t^{\fM, \ell} \), an element of \( D \). Because \( t \) is free for \( x \) in \( \varphi \), @lem-term-substitution applies and gives \( \fM, \ell[x \mapsto d] \models \varphi \). By (S7) of @def-satisfaction, with the element \( d \), \( \fM, \ell \models \exists x\, \varphi \).

"Free for" is used exactly once, to apply @lem-term-substitution. Without it the step fails: from \( \forall y\, R(y, y) \), read as \( (\forall y\, R(x, y))[y/x] \), an "\( \rulename{\exists I} \)" would give \( \exists x\, \forall y\, R(x, y) \), and in the structure on \( \nZ \) with \( R \) read as \( \le \) the first is true and the second ("there is a least integer") false.
:::

::: {#exr-first-order-soundness-b2}
[B2: Three nonderivability results]

Use the following counter-models from Section 4.11 to state three nonderivability results, citing @cor-counter-model, and check in each case that the structure (and assignment) satisfy every premise and not the conclusion.

::: {.enumerate options="label=(\alph*)"}
1. The two-element structure of @exm-counter-model-swap.
2. The counter-model of @exr-models-b3.
3. The counter-model of @exr-models-b1 (iii).
:::
:::

::: {.solution}
*(a)* \( D = \{ a, b \} \), \( R^{\fM} = \{ (a, a), (b, b) \} \). The premise \( \forall y\, \exists x\, R(x, y) \) holds (for \( y = a \) take \( x = a \), for \( y = b \) take \( x = b \)); the conclusion \( \exists x\, \forall y\, R(x, y) \) fails (\( x = a \) fails at \( y = b \), \( x = b \) at \( y = a \)). Both are sentences, so any assignment will do. By @cor-counter-model, \( \forall y\, \exists x\, R(x, y) \nvdash \exists x\, \forall y\, R(x, y) \).

*(b)* \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \). The premise \( \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \) holds, since its hypothesis fails at \( b \); the conclusion \( \forall x\, (P(x) \to Q(x)) \) fails at \( a \). By @cor-counter-model, \( \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \nvdash \forall x\, (P(x) \to Q(x)) \).

*(c)* \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), with an assignment \( \ell(x) = b \). There are no premises, so the condition on premises holds trivially. The formula \( \exists x\, P(x) \to P(x) \) fails under \( \ell \): its hypothesis holds (witness \( a \)) and its conclusion, with \( x \) free, has value \( b \notin P^{\fM} \). By @cor-counter-model, with \( \Gamma \) empty, \( \nvdash \exists x\, P(x) \to P(x) \). Here the assignment is essential: under \( \ell(x) = a \) the formula holds, and the structure alone would not have been a counter-model.
:::

### C. Going deeper

::: {#exr-first-order-soundness-c1}
[C1: The \( \rulename{\exists E} \) case]

Write out the \( \rulename{\exists E} \) case of the proof of @thm-first-order-soundness in full, from memory: the data of line \( k \), the side condition, what the induction hypothesis gives for the cited line and the cited box, and the argument, naming at each step which clause of the side condition it uses.
:::

::: {.solution}
[Hint 1]

The tool is the assignment \( \ell[x_0 \mapsto d] \), where \( d \) is a witness for \( \exists x\, \varphi \) under \( \ell \). You will need @lem-free-coincidence three times and @lem-term-substitution once.
:::

::: {.solution}
[Hint 2]

Start: "Let \( \fM \) be a structure interpreting every symbol of the derivation, with domain \( D \), and \( \ell \) an assignment with \( \fM, \ell \models \Gamma_k \). By the induction hypothesis for line \( h \) and @lem-context-inclusion (a), \( \fM, \ell \models \exists x\, \varphi \), so choose \( d \in D \) with \( \fM, \ell[x \mapsto d] \models \varphi \)."
:::

::: {.solution}
*Data.* Line \( k \) is \( \chi \), by \( \rulename{\exists E} \) citing a line \( h \) holding \( \exists x\, \varphi \) and a box with name \( x_0 \), from line \( a \) (the assumption \( \varphi[x_0/x] \)) to line \( b \) (the formula \( \chi \)). Side condition (@def-rules-existential): \( x_0 \) appears neither in \( \chi \), nor in \( \exists x\, \varphi \), nor in a premise, nor in an assumption of a box still open at line \( k \).

*What the hypothesis gives.* Line \( h \) is available at line \( k \), so \( \Gamma_h \subseteq \Gamma_k \) (@lem-context-inclusion (a)), and \( S(h) \) holds: every structure interpreting every symbol of the derivation, and every assignment satisfying \( \Gamma_h \), satisfy \( \exists x\, \varphi \). The box is cited by a box rule, so its last line has context \( \Gamma_k, \varphi[x_0/x] \) (@lem-context-inclusion (b), extended in the subsection "Contexts, once more"), and \( S(b) \) says that every such structure and assignment satisfying \( \Gamma_k \) and \( \varphi[x_0/x] \) satisfy \( \chi \).

*The argument.* Let \( \fM \) be a structure interpreting every symbol of the derivation (as in Step 2), with domain \( D \), and \( \ell \) an assignment with \( \fM, \ell \models \Gamma_k \). Then \( \fM, \ell \models \Gamma_h \), so \( \fM, \ell \models \exists x\, \varphi \); by (S7), choose \( d \in D \) with \( \fM, \ell[x \mapsto d] \models \varphi \). Let \( \ell' \coloneqq \ell[x_0 \mapsto d] \).

1. \( \fM, \ell' \models \Gamma_k \). The formulas of \( \Gamma_k \) are the premises and the assumptions of the boxes open at line \( k \); by the side condition, \( x_0 \) appears in none of them. \( \ell' \) differs from \( \ell \) only at \( x_0 \), so @lem-free-coincidence applies to each formula of \( \Gamma_k \).
2. \( \fM, \ell' \models \varphi[x_0/x] \). Since \( x_0 \) does not appear in \( \exists x\, \varphi \), it is not \( x \) and does not appear in \( \varphi \). So \( \ell'[x \mapsto d] \) and \( \ell[x \mapsto d] \) differ at most at \( x_0 \), which is not in \( \varphi \), and \( \fM, \ell'[x \mapsto d] \models \varphi \) by @lem-free-coincidence. The term \( x_0 \) is free for \( x \) in \( \varphi \), as no quantifier of \( \varphi \) is on \( x_0 \), and \( x_0^{\fM, \ell'} = d \); so @lem-term-substitution gives \( \fM, \ell' \models \varphi[x_0/x] \).
3. By 1, 2 and the hypothesis for the box, \( \fM, \ell' \models \chi \).
4. \( \ell' \) and \( \ell \) differ only at \( x_0 \), which does not appear in \( \chi \); by @lem-free-coincidence, \( \fM, \ell \models \chi \).

Since \( \fM \) and \( \ell \) were arbitrary, this proves \( S(k) \).

**Marking scheme.** (10 points)

- 2: states the data and the full side condition, and the context \( \Gamma_k, \varphi[x_0/x] \) of the box's last line.
- 2: obtains a witness \( d \) from the cited line through the induction hypothesis and (S7), and sets \( x_0 \) to \( d \).
- 2: shows the new assignment still satisfies \( \Gamma_k \), using "\( x_0 \) in no premise and no open assumption".
- 2: shows the new assignment satisfies \( \varphi[x_0/x] \), using "\( x_0 \) not in \( \exists x\, \varphi \)" and the substitution lemma.
- 2: applies the hypothesis for the box, and returns to \( \ell \) using "\( x_0 \) not in \( \chi \)".

A proof that treats the box's assumption and the context in the other order earns the same points. Fatal errors (0 for the step): setting \( x_0 \) to an arbitrary element rather than the witness; concluding \( \fM, \ell \models \chi \) directly from \( \fM, \ell' \models \chi \) without the condition on \( \chi \).
:::

::: {#exr-first-order-soundness-c2}
[C2: "Free for" is needed]

Show that the side condition "\( t \) is free for \( x \) in \( \varphi \)" of \( \rulename{\forall E} \) cannot be dropped. Give a two-line "derivation" that uses \( \rulename{\forall E} \) with a term that is not free for \( x \), a structure in which its premise is true and its conclusion false, and the step of the proof of @lem-term-substitution that fails.
:::

::: {.solution}
[Hint 1]

Look for a premise \( \forall x\, \varphi \) in which \( \varphi \) contains a quantifier \( \forall y \) and \( x \) occurs free inside its scope; instantiate at \( t = y \).
:::

::: {.solution}
[Hint 2]

Try \( \varphi = \neg\forall y\, (y \le x) \), "\( x \) is not an upper bound of everything", in a structure with no largest element.
:::

::: {.solution}
Take \( \varphi = \neg\forall y\, (y \le x) \) and \( t = y \). The free occurrence of \( x \) in \( \varphi \) lies in the scope of \( \forall y \), and \( y \) occurs in \( t \), so \( t \) is **not** free for \( x \) in \( \varphi \). Ignoring this, \( \rulename{\forall E} \) would allow:

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \neg \forall y\, (y \le x)}
  \have {2} {\neg \forall y\, (y \le y)} \Ae{1}
\end{nd}$
\end{center}
```

In \( (\nZ, \le) \), the premise says "for every integer \( x \), not every integer \( y \) is \( \le x \)", that is, no integer is largest: for each \( x \), the integer \( x + 1 \) is not \( \le x \). It is true. The conclusion says "not every integer \( y \) has \( y \le y \)", which is false, since \( \le \) is reflexive. So the premise is true and the conclusion false, and a rule allowing this step would be unsound.

The step of @lem-term-substitution that fails is the second quantifier case, applied to \( \forall y\, (y \le x) \): it needs \( y \) not in \( t \), so that the value of \( t \) does not change when (S6) sets \( y \) to each \( d \). Here \( t = y \), and its value is the new \( d \) each time: \( \forall y\, (y \le y) \) compares each \( d \) with itself, while \( \forall y\, (y \le x) \) at the value \( a \) of \( t \) compares each \( d \) with the fixed \( a \). The legal route renames first (Section 4.2): \( \forall x\, \neg\forall z\, (z \le x) \), and then \( \rulename{\forall E} \) at \( y \) gives \( \neg\forall z\, (z \le y) \), which is true in \( (\nZ, \le) \) under every assignment.

**Marking scheme.** (10 points)

- 3: a premise and a \( \rulename{\forall E} \) step at a term that is not free for \( x \), with the capture identified.
- 4: a structure, with the premise checked true and the conclusion checked false.
- 3: names the quantifier case of @lem-term-substitution and the fact it needs (\( y \) not in \( t \)).

Fatal errors (0 for the step): a "counter-model" in which the premise is false; a step in which \( t \) is in fact free for \( x \).
:::

<!-- dependency ledger
thm-first-order-soundness (claim): the thirteen primitive rules of Chapters 1-2 and the box rules among them | Section 3.5 list (recalled in thm-soundness's section), recalled in prose
thm-first-order-soundness (proof): a derived-rule line abbreviates a pasted primitive derivation; Chapter 2's derived rules have no flagged boxes | def-derived-rule; Step 1 of thm-soundness (cited)
thm-first-order-soundness (proof): bounded rules expand into unbounded steps whose side conditions hold | prp-bounded-quantifier-rules (cited)
thm-first-order-soundness (proof): (sym) and (trans) lines abbreviate pasted three-line =I/=E derivations with quantifier-free phi | prp-equality-symmetric-transitive (cited), def-rules-equality
thm-first-order-soundness (proof): an "arith" line stands for a universally quantified arithmetic premise, forall-E at its terms and ->E | inline convention; Section 4.4 (B3 pattern) recalled in prose, not used as a step
thm-first-order-soundness (proof): the arith premise's bound variables appear nowhere else, so fresh-name conditions and free-for hold; with arith lines the result is Gamma, A |= psi | inline convention
thm-first-order-soundness (proof): lines in renamed form (Section 4.2 convention) are satisfied by the same structures and assignments | cor-renaming-bound-variables (cited)
thm-first-order-soundness (proof): induction over structures interpreting every symbol of the derivation; expansion of a structure for Gamma, psi by arbitrary meanings, using a nonempty domain; extra meanings change nothing | def-structure (M1); remark after def-first-order-entailment (cited in prose)
cor-renaming-bound-variables (proof): front renaming; renaming inside a formula by structural induction for all assignments | lem-term-substitution, lem-free-coincidence, def-free-for, def-satisfaction (S4)-(S7); thm-structural-induction (pattern); renaming as defined in Section 4.2 (no label)
thm-first-order-soundness (proof): scope rule, availability, boxes disjoint or nested, unchanged for flagged boxes | def-derivation as extended in Section 4.4 (def-rules-universal)
thm-first-order-soundness (proof): lem-context-inclusion (b) extended to flagged boxes without an assumption | inline (subsection "Contexts, once more"), re-running the proof of lem-context-inclusion (b)
thm-first-order-soundness (proof): the forall-I box's last line is a line of the box itself; the exists-E box's last line likewise; the side conditions as quoted | def-rules-universal, def-rules-existential
thm-first-order-soundness (proof): the propositional cases carry over from thm-soundness with (S3)-(S5) for (V1)-(V6) | thm-soundness (cited), def-satisfaction
thm-first-order-soundness (proof): a variable not appearing in phi (not even after a quantifier) is free for x in phi | def-free-for, inline
thm-first-order-soundness (proof): l[x0 -> d][x -> d] and l[x -> d] differ at most at x0 when x0 is not x | def-assignment, inline
lem-term-substitution (proof): structural induction on terms and formulas | thm-structural-induction (pattern), def-term, def-first-order-formula; Section 4.2 remark
lem-term-substitution (proof): substitution passes through connectives and atomic formulas, and (forall y phi)[t/x] is forall y (phi[t/x]) for y not x | def-substitution
lem-term-substitution (proof): psi[t/x] = psi when x is not free in psi | Section 4.2, proved in its text (no label), cited as "Section 4.2 proved"
lem-term-substitution (proof): free-for is inherited by immediate parts; for x free in forall y phi, t free for x forces y not in t | def-free-for, inline
lem-term-substitution (proof): terms with the same values of their variables have the same value | the claim for terms in the proof of lem-free-coincidence (cited)
lem-term-substitution (proof): l[y -> d][x -> a] = l[x -> a][y -> d] for different x, y | def-assignment and the remark after it (Section 4.11)
lem-term-substitution (example): the capture example in Z with >, + and 1 and the Quick check values (a = 6; z = 4) | inline; verify/ch04/lem-term-substitution.py
cor-counter-model (example): the non-derivability list, each from a Section 4.11 counter-model | exm-counter-model-swap, exr-models-b1 (cited in prose, not in a proof); verify/ch04/exm-counter-model-swap.py
cor-counter-model (claim): with arith lines a counter-model must also satisfy the arithmetic sentences | thm-first-order-soundness Step 1 (cited)
thm-first-order-soundness (claim): completeness (Goedel 1929) and undecidability (Church, Turing 1936) | stated without proof in a remark; nothing depends on them
exr-first-order-soundness-a1 (solution): the two-element structure for line 3; R(x0, y0) in (Z, <) under the two assignments | inline; verify/ch04/exr-first-order-soundness-a1.py
exr-first-order-soundness-b1 (solution): forall y R(y, y) true and exists x forall y R(x, y) false in (Z, <=) | inline; verify/ch04/exr-first-order-soundness-c2.py checks the (Z, <=) facts on a window
exr-first-order-soundness-b2 (solution): the three counter-models | verify/ch04/exm-counter-model-swap.py, exr-models-b1.py, exr-models-b3.py
exr-first-order-soundness-c2 (solution): no largest integer; <= reflexive | inline; verify/ch04/exr-first-order-soundness-c2.py
-->
