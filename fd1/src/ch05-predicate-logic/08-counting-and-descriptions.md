# Unique Existence, Counting and Descriptions

Mathematics says "the limit", "the maximum", "the inverse", and it defines new words all the time: "we define \( \abs{x} \) to be …", "call \( n \) even if …". This section is about the logic behind both habits. It starts with "there is exactly one", which licenses "the". Then it counts with equality, turns "the \( x \) such that \( \varphi \)" into a name that may be used only after uniqueness is proved, and sets a function symbol beside its graph. Last, it shows why introducing a new symbol by a definition never proves anything new about the old ones. No new rule is needed: equality and the quantifiers do all the work.

## Unique existence

Mathematics says "**the** limit of the sequence", "**the** supremum of \( A \)", "**the** additive inverse of \( a \)". Each "the" makes two claims. There is such an object, and there is only one, so that the name picks it out. The second claim is the one that is easy to forget, and the one the claim at the start of Section 5.7 was about.

*"There is exactly one \( x \) with \( \varphi \)": there is one, and any other is it.*

::: {#def-unique-existence}
[Unique Existence]

Let \( \varphi \) be a formula, \( x \) a variable, and \( y \) a variable **other than \( x \) that does not appear in \( \varphi \)** (Section 5.2). Then
\[
\exists! x\, \varphi \quad \text{abbreviates} \quad \exists x\, \bigl( \varphi \wedge \forall y\, (\varphi[y/x] \to y = x) \bigr).
\]
We read \( \exists! x\, \varphi \) as "there is **exactly one** \( x \) such that \( \varphi \)", or "there is a **unique** \( x \) with \( \varphi \)".
:::

In words: there is an \( x \) that satisfies \( \varphi \), and every \( y \) that satisfies \( \varphi \) (that is, satisfies \( \varphi \) with \( y \) in place of \( x \)) is equal to that \( x \). The first conjunct is existence. The second is uniqueness, and it is a statement about the \( x \) already found: any other candidate coincides with it. Like the bounded quantifiers of @def-bounded-quantifier, \( \exists! \) is not a new symbol of the language but shorthand, and every rule applies to the formula it abbreviates.

**Well-definedness.** The abbreviation does not depend on the choice of \( y \), up to renaming a bound variable. The argument, in the fold below, rests on one fact about substitution that the proof of @prp-unique-existence-use uses again: *if \( y \) does not appear in \( \varphi \), then \( (\varphi[y/x])[t/y] \) is \( \varphi[t/x] \).*

::: {.second-reading title="Well-definedness, proved"}
This is a structural induction on \( \varphi \) of the kind in Section 5.2. In a term, the \( y \)'s of \( s[y/x] \) are exactly the former \( x \)'s, so \( (s[y/x])[t/y] = s[t/x] \); atomic formulas, \( \bot \) and the connectives follow clause by clause. For \( \forall x\, \psi \), both sides are \( \forall x\, \psi \), since substitution for \( x \) stops at \( \forall x \) and \( y \) does not appear in \( \psi \) (the second fact of Section 5.2). For \( \forall z\, \psi \) with \( z \) not \( x \), also \( z \) is not \( y \), because \( y \) does not appear in \( \varphi \); so both substitutions pass under the quantifier and the induction hypothesis applies, and \( \exists \) is the same. Now let \( y \) and \( y' \) be two admissible choices. If they are the same variable there is nothing to show. Otherwise \( y' \) does not appear in \( \varphi[y/x] \to y = x \), since it is neither \( x \) nor \( y \) and does not appear in \( \varphi \); so the bound \( y \) of \( \forall y\, (\varphi[y/x] \to y = x) \) may be renamed \( y' \), which gives \( \forall y'\, \bigl( (\varphi[y/x])[y'/y] \to y' = x \bigr) \). By the fact with \( t = y' \), this is \( \forall y'\, (\varphi[y'/x] \to y' = x) \), the formula written with \( y' \).
:::

**Examples.** Simplest first; each is read over the domain named, with the informal truth of Section 5.1.

1. Over \( \nR \), \( \exists! x\, (x + 2 = 5) \) is true. *Existence:* \( 3 + 2 = 5 \). *Uniqueness:* if \( y + 2 = 5 \), then subtracting \( 2 \) gives \( y = 3 \), so \( y \) is the \( x \) already found.
2. Over \( \nN \), \( \exists! x\, (x \cdot x = 4) \) is true. *Existence:* \( 2 \cdot 2 = 4 \). *Uniqueness:* for a natural number \( y \), if \( y \le 1 \) then \( y \cdot y \le 1 \), and if \( y \ge 3 \) then \( y \cdot y \ge 9 \); so \( y \cdot y = 4 \) forces \( y = 2 \).
3. Over \( \nR \), \( \exists! x\, \forall y\, (x + y = y) \) is true: \( 0 \) is the **unique** additive identity. *Existence:* \( 0 + y = y \) for every \( y \). *Uniqueness:* suppose \( z + y = y \) for every \( y \). Apply this to the one instance \( y = 0 \) (by \( \rulename{\forall E} \)): \( z + 0 = 0 \). Since also \( z + 0 = z \), symmetry and transitivity give \( z = 0 \). The whole uniqueness proof is the choice of the instance \( y = 0 \).

**Nonexample by minimal change.** Keep example 2 and change the domain to \( \nZ \). Existence still holds, with the same witness \( 2 \). Uniqueness fails: \( y = -2 \) also satisfies \( y \cdot y = 4 \), and \( -2 \ne 2 \). So over \( \nZ \), \( \exists! x\, (x \cdot x = 4) \) is false, and the failing clause is exactly the second conjunct.

::: {.check}
Is \( \exists! x\, (x < 1) \) true over \( \nN \)? Over \( \nZ \)?
:::

::: {.solution}
Over \( \nN \), yes: \( 0 < 1 \), and every natural number below \( 1 \) is \( 0 \). Over \( \nZ \), no: existence holds, and uniqueness fails, since \( 0 \) and \( -1 \) are both below \( 1 \).
:::

::: {.second-reading title="Why y must not appear, and a degenerate case"}
**Why \( y \) must not appear in \( \varphi \).** The condition keeps the new quantifier \( \forall y \) from capturing anything of \( \varphi \)'s own. Take \( \varphi = (x \le y) \), in which \( y \) is free, and read over \( \nN \) with \( y \) naming \( 0 \). "There is exactly one natural number \( x \) with \( x \le 0 \)" is true: \( x = 0 \). The formula written with the forbidden bound variable \( y \) is
\[
\exists x\, \bigl( x \le y \wedge \forall y\, (y \le y \to y = x) \bigr),
\]
because \( (x \le y)[y/x] \) is \( y \le y \). Its second conjunct says that **every** natural number equals \( x \), which is false. The free \( y \) of \( \varphi \), which was to name \( 0 \), has been captured by \( \forall y \). With an admissible variable, say \( z \), the formula is \( \exists x\, \bigl( x \le y \wedge \forall z\, (z \le y \to z = x) \bigr) \), which is true.

**Degenerate.** For any constant \( c \), \( \exists! x\, (x = c) \) holds in every domain, and it is derivable from no premises (the derivation follows). By contrast, \( \exists! x\, (x = x) \) says that the domain has exactly one element, which is false in \( \nN \), \( \nZ \) and \( \nR \): existence holds and uniqueness fails.

The derivation of \( \exists! x\, (x = c) \), with the abbreviation written out, shows that \( \exists! \) needs no rules of its own:

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {c = c} \eqi{}
  \open[y_0]
  \open
  \hypo {2} {y_0 = c}
  \close
  \have {3} {y_0 = c \to y_0 = c} \ii{2-2}
  \close
  \have {4} {\forall y\, (y = c \to y = c)} \Ai{2-3}
  \have {5} {c = c \wedge \forall y\, (y = c \to y = c)} \ai{1,4}
  \have {6} {\exists x\, (x = c \wedge \forall y\, (y = c \to y = x))} \Ei{5}
\end{nd}$
\end{center}
```

Line 3 closes a box whose only line is its assumption: the box shows \( y_0 = c \to y_0 = c \), as \( P \to P \) is shown in Chapter 1. Line 6 is \( \rulename{\exists I} \) with the witness \( c \), and it reads line 5 as \( \psi[c/x] \) for \( \psi = \bigl( x = c \wedge \forall y\, (y = c \to y = x) \bigr) \), which marks with \( x \) the first \( c \) and the last one, and keeps the other two. The choice of which occurrences to mark is the one discussed with @def-rule-existential-introduction.
:::

::: {.warning}
**Uniqueness is not existence.** A uniqueness argument ("suppose \( y \) also satisfies \( \varphi \); then \( y = x \)") proves nothing about whether anything satisfies \( \varphi \). Over \( \nR \), every two solutions of \( x^2 = -1 \) are equal, vacuously, because there are none; yet no real number is "the" square root of \( -1 \). Conversely, an existence proof does not give uniqueness: \( x^2 = 1 \) has the solution \( 1 \), and "the solution" would be wrong, since \( -1 \) is another. Before writing "the", check both halves.
:::

## How uniqueness is used and proved

A proof of "exactly one" rarely follows the shape of @def-unique-existence, which ties the uniqueness clause to the witness just found. It proves two separate statements: there is at least one, and there is at most one. The second is "any two objects with the property are equal", and it makes no mention of a witness. The next result says that the two shapes say the same thing.

::: {#prp-unique-existence-use}
[Two Halves of Unique Existence]

Let \( \varphi \) be a formula, \( x \) a variable, and \( y \) a variable other than \( x \) that does not appear in \( \varphi \). Then
\[
\exists! x\, \varphi \;\dashv\vdash\; \exists x\, \varphi \wedge \forall x\, \forall y\, \bigl( \varphi \wedge \varphi[y/x] \to x = y \bigr).
\]
:::

The right-hand side is "existence and at most one". Its second conjunct is what a mathematician proves under the heading "uniqueness": take two objects \( x \) and \( y \) with the property, and show \( x = y \).

::: {.idea}
Both directions are searches in the style of Section 3.1 with the quantifier steps. For \( \vdash \), the premise is an \( \exists \), so open its \( \rulename{\exists E} \) box first, with a witness \( x_0 \): inside it, \( \varphi[x_0/x] \) gives existence at once by \( \rulename{\exists I} \), and "at most one" is a \( \forall\forall \) goal, which opens two flagged boxes \( u_0 \), \( v_0 \). Two objects \( u_0 \), \( v_0 \) with the property are each equal to the witness \( x_0 \), by the uniqueness clause, and so equal to each other: the witness is the "third point" that links them. For \( \dashv \), open the \( \rulename{\exists E} \) box on \( \exists x\, \varphi \) with a witness \( x_0 \); the goal inside is \( \exists! x\, \varphi \), whose witness will be \( x_0 \) again, and the uniqueness clause for \( x_0 \) comes from "at most one" applied to the pair \( x_0 \), \( y_0 \).
:::

The two derivations that carry this out are in the fold below.

::: {.second-reading title="The proof of the two halves"}
::: {.proof}
Choose four distinct variables \( x_0 \), \( u_0 \), \( v_0 \), \( y_0 \) that do not appear in \( \varphi \), and none of which is \( x \) or \( y \). Three facts about substitution are used throughout. First, since \( y \) does not appear in \( \varphi \), \( (\varphi[y/x])[t/y] \) is \( \varphi[t/x] \) for every term \( t \), the fact proved for the well-definedness of @def-unique-existence. Second, \( \varphi[y/x] \) has no free \( x \) (every free \( x \) became \( y \)), so it is unchanged by a substitution for \( x \). Third, for a term \( t \) that does not contain \( y \), \( \varphi[t/x] \) contains no \( y \), so it is unchanged by a substitution for \( y \).

\( (\vdash) \) The following is a derivation with premise \( \exists! x\, \varphi \), written out.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, (\varphi \wedge \forall y\, (\varphi[y/x] \to y = x))}
  \open[x_0]
  \hypo {2} {\varphi[x_0/x] \wedge \forall y\, (\varphi[y/x] \to y = x_0)}
  \have {3} {\varphi[x_0/x]} \ae{2}
  \have {4} {\forall y\, (\varphi[y/x] \to y = x_0)} \ae{2}
  \have {5} {\exists x\, \varphi} \Ei{3}
  \open[u_0]
  \open[v_0]
  \open
  \hypo {6} {\varphi[u_0/x] \wedge \varphi[v_0/x]}
  \have {7} {\varphi[u_0/x]} \ae{6}
  \have {8} {\varphi[v_0/x]} \ae{6}
  \have {9} {\varphi[u_0/x] \to u_0 = x_0} \Ae{4}
  \have {10} {u_0 = x_0} \ie{9,7}
  \have {11} {\varphi[v_0/x] \to v_0 = x_0} \Ae{4}
  \have {12} {v_0 = x_0} \ie{11,8}
  \have {13} {v_0 = v_0} \eqi{}
  \have {14} {x_0 = v_0} \eqe{12,13}
  \have {15} {u_0 = v_0} \eqe{14,10}
  \close
  \have {16} {\varphi[u_0/x] \wedge \varphi[v_0/x] \to u_0 = v_0} \ii{6-15}
  \close
  \have {17} {\forall y\, (\varphi[u_0/x] \wedge \varphi[y/x] \to u_0 = y)} \Ai{6-16}
  \close
  \have {18} {\forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)} \Ai{6-17}
  \have {19} {\exists x\, \varphi \wedge \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)} \ai{5,18}
  \close
  \have {20} {\exists x\, \varphi \wedge \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)} \Ee{1,2-19}
\end{nd}$
\end{center}
```

Lines 9 and 11 are \( \rulename{\forall E} \) on line 4 at \( u_0 \) and at \( v_0 \), by the first substitution fact; each term is a variable not bound in \( \varphi[y/x] \to y = x_0 \), so it is free for \( y \) there. Lines 13 and 14 are the symmetry of @prp-equality-symmetric-transitive (a), written out; line 15 is \( \rulename{{=}E} \) with the equation \( x_0 = v_0 \) and \( \psi = (u_0 = z) \), which turns line 10 into \( u_0 = v_0 \). Line 17 is \( \rulename{\forall I} \) with the flag \( v_0 \): line 16 is its instance at \( v_0 \) (by the third and first substitution facts), and \( v_0 \) appears in no premise, in no assumption still open at line 17 (only line 2 is, and \( v_0 \) is not in it), and not in line 17. Line 18 is \( \rulename{\forall I} \) with the flag \( u_0 \) in the same way; its instance at \( u_0 \) is line 17, by the second substitution fact. Finally, line 20 closes the \( \rulename{\exists E} \) box: its last line 19 does not contain \( x_0 \), and \( x_0 \) is in neither line 1 nor any open assumption.

\( (\dashv) \) The following is a derivation with the right-hand side as premise.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\exists x\, \varphi \wedge \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)}
  \have {2} {\exists x\, \varphi} \ae{1}
  \have {3} {\forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y)} \ae{1}
  \open[x_0]
  \hypo {4} {\varphi[x_0/x]}
  \open[y_0]
  \open
  \hypo {5} {\varphi[y_0/x]}
  \have {6} {\forall y\, (\varphi[x_0/x] \wedge \varphi[y/x] \to x_0 = y)} \Ae{3}
  \have {7} {\varphi[x_0/x] \wedge \varphi[y_0/x] \to x_0 = y_0} \Ae{6}
  \have {8} {\varphi[x_0/x] \wedge \varphi[y_0/x]} \ai{4,5}
  \have {9} {x_0 = y_0} \ie{7,8}
  \have {10} {x_0 = x_0} \eqi{}
  \have {11} {y_0 = x_0} \eqe{9,10}
  \close
  \have {12} {\varphi[y_0/x] \to y_0 = x_0} \ii{5-11}
  \close
  \have {13} {\forall y\, (\varphi[y/x] \to y = x_0)} \Ai{5-12}
  \have {14} {\varphi[x_0/x] \wedge \forall y\, (\varphi[y/x] \to y = x_0)} \ai{4,13}
  \have {15} {\exists x\, (\varphi \wedge \forall y\, (\varphi[y/x] \to y = x))} \Ei{14}
  \close
  \have {16} {\exists x\, (\varphi \wedge \forall y\, (\varphi[y/x] \to y = x))} \Ee{2,4-15}
\end{nd}$
\end{center}
```

Line 6 is \( \rulename{\forall E} \) at \( x_0 \) on line 3, by the second substitution fact, and line 7 is \( \rulename{\forall E} \) at \( y_0 \) on line 6, by the third and first. Lines 10 and 11 are symmetry, written out. Line 13 is \( \rulename{\forall I} \) with the flag \( y_0 \): line 12 is its instance at \( y_0 \), by the first substitution fact; at line 13 the open assumptions are line 4, which does not contain \( y_0 \), the premise does not contain it either, and neither does line 13. Line 15 is \( \rulename{\exists I} \) with the witness \( x_0 \), which is free for \( x \) since it does not appear in \( \varphi \); line 14 is its instance at \( x_0 \), by the second substitution fact. Line 16 closes the \( \rulename{\exists E} \) box: line 15 does not contain \( x_0 \), and \( x_0 \) is in neither line 2 nor the premise, which is the only assumption open outside the box. This proves both directions.
:::
:::

In practice this is how "there is exactly one" is proved: an existence proof, then a separate "suppose \( x \) and \( y \) both satisfy \( \varphi \); then \( x = y \)".

**One more instance: "the maximum".** A **maximum** of a set \( A \) of reals is an element \( m \in A \) with \( a \le m \) for every \( a \in A \). If \( m \) and \( m' \) are both maxima, then \( m' \le m \) (apply the property of \( m \) to the element \( m' \in A \)) and \( m \le m' \) (apply the property of \( m' \) to \( m \in A \)), so \( m = m' \) by the order fact that \( a \le b \) and \( b \le a \) give \( a = b \). That is "at most one"; a set may have no maximum at all, such as \( (0, 1) \), so existence is a separate question. Only when both halves are known may we write "the maximum of \( A \)".

## Counting with equality

"At least one" is \( \exists \), and "at most one" is the second half of @prp-unique-existence-use. Beyond one, counting needs the sign \( \ne \).

::: {#def-counting-with-equality}
[Counting with Equality]

Let \( \varphi \) be a formula, \( x \) a variable, and \( y \), \( z \) two different variables, other than \( x \), that do not appear in \( \varphi \).

- "**At least two** \( x \) satisfy \( \varphi \)" abbreviates \( \exists x\, \exists y\, (x \ne y \wedge \varphi \wedge \varphi[y/x]) \).
- "**At most one** \( x \) satisfies \( \varphi \)" abbreviates \( \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y) \).
- "**At most two** \( x \) satisfy \( \varphi \)" abbreviates \( \forall x\, \forall y\, \forall z\, (\varphi \wedge \varphi[y/x] \wedge \varphi[z/x] \to x = y \vee x = z \vee y = z) \).
- "**Exactly two** \( x \) satisfy \( \varphi \)" abbreviates the conjunction of "at least two" and "at most two".

For a number \( n \ge 2 \), "at least \( n \)" uses \( n \) different variables \( x_1, \dots, x_n \) that do not appear in \( \varphi \), and asks for all \( n(n - 1)/2 \) inequalities \( x_i \ne x_j \) together with \( \varphi \) at each; "at most \( n \)" says that among any \( n + 1 \) objects satisfying \( \varphi \), two are equal; "exactly \( n \)" is both.
:::

In words: two letters count two objects only when the formula says that they differ, and "at most two" says that three letters satisfying \( \varphi \) cannot name three different objects. As with \( \exists! \), these are abbreviations, not new symbols, and \( \exists! \) stays the only counting shorthand.

::: {#exm-exactly-two-solutions}
[Exactly Two Square Roots of One]

Over \( \nR \), show that exactly two \( x \) satisfy \( x \cdot x = 1 \).
:::

::: {.solution}
*At least two:* the witnesses \( 1 \) and \( -1 \): \( 1 \ne -1 \), \( 1 \cdot 1 = 1 \) and \( (-1) \cdot (-1) = 1 \).

*At most two:* let \( u \), \( v \), \( w \) be real numbers with \( u \cdot u = v \cdot v = w \cdot w = 1 \). Each is \( 1 \) or \( -1 \), since \( y \cdot y = 1 \) gives \( (y - 1)(y + 1) = 0 \). If \( u = v \), the disjunction \( u = v \vee u = w \vee v = w \) holds. Otherwise one of \( u \), \( v \) is \( 1 \) and the other \( -1 \), and \( w \), being \( 1 \) or \( -1 \), equals one of them. Three letters, at most two objects: that is what "at most two" means.
:::

::: {.warning}
**Different letters, perhaps the same object.** \( \exists x\, \exists y\, (x \cdot x = 1 \wedge y \cdot y = 1) \) is true over \( \nR \) with \( x \) and \( y \) both naming \( 1 \): it says no more than \( \exists x\, (x \cdot x = 1) \). Two letters count two objects only when the formula says \( x \ne y \). The same holds in derivations: two \( \rulename{\exists E} \) boxes with the names \( x_0 \) and \( y_0 \) may have named the same object, and nothing gives \( x_0 \ne y_0 \).
:::

::: {.check}
Write "at least two primes are even" with \( \mathrm{Prime} \) and \( \mathrm{Even} \), and decide it over \( \nN \).
:::

::: {.solution}
\( \exists x\, \exists y\, \bigl( x \ne y \wedge (\mathrm{Prime}(x) \wedge \mathrm{Even}(x)) \wedge (\mathrm{Prime}(y) \wedge \mathrm{Even}(y)) \bigr) \). It is false: an even prime is divisible by \( 2 \), so it is \( 2 \), and any two even primes are equal.
:::

*Only*, *except* and *the smallest* are counting words too; the drill at the end of the section translates them.

## The \( x \) such that \( \varphi \)

Once there is exactly one \( x \) with \( \varphi \), mathematics names it: "the maximum of \( A \)", "the additive inverse of \( a \)", "\( \sqrt 2 \)". The name is then used like a constant, because the proof has earned it.

::: {#def-definite-description}
[Definite Description]

Let \( \Gamma \) be a list of formulas and \( \varphi \) a formula whose only free variable is \( x \), and suppose \( \Gamma \vdash \exists! x\, \varphi \). **Introducing a name for the \( x \) such that \( \varphi \)** means taking a constant \( c \) that appears neither in \( \Gamma \) nor in \( \varphi \), and letting derivations from \( \Gamma \) use the **defining line** \( \varphi[c/x] \) as one more premise. The phrase "the \( x \) such that \( \varphi \)" names \( c \).
:::

In words, and why both halves are needed: existence is what makes the defining line safe, and the proposition at the end of this section shows that it proves nothing new about the old symbols. Uniqueness is what makes the word "the" honest. If \( c \) and \( c' \) are both introduced for \( \varphi \), then \( \Gamma, \varphi[c/x], \varphi[c'/x] \vdash c = c' \): take the "at most one" half of @prp-unique-existence-use, instantiate it at \( c \) and at \( c' \) (\( \rulename{\forall E} \) twice, with the substitution facts used in the proof of @prp-unique-existence-use), and fire it by \( \rulename{\wedge I} \) and \( \rulename{{\to}E} \). So every proof that names the \( x \) such that \( \varphi \) names the same object.

**Russell's unpacking.** A sentence about the \( x \) such that \( \varphi \) can be unpacked into one that names nothing. Write \( \mathrm{Max}(A, m) \) for "\( m \) is a maximum of \( A \)", that is, \( m \in A \wedge \forall a \in A\; (a \le m) \) (the paragraph "One more instance" above). "The maximum of \( A \) is less than \( 2 \)" unpacks to
\[
\exists m\, \bigl( \mathrm{Max}(A, m) \wedge \forall y\, (\mathrm{Max}(A, y) \to y = m) \wedge m < 2 \bigr):
\]
there is exactly one maximum, and it is less than \( 2 \).

**Two readings of a negation.** When nothing satisfies \( \varphi \), the unpacked sentence is false, and a negation can be read two ways. The interval \( A = (0, 1) \) has no maximum: an \( m \in A \) is exceeded by \( (m + 1)/2 \), which is also in \( A \). Read "the maximum of \( A \) is not \( 1 \)" with the negation inside, \( \exists m\, (\mathrm{Max}(A, m) \wedge \forall y\, (\mathrm{Max}(A, y) \to y = m) \wedge m \ne 1) \): it is false, since there is no \( m \). Read it with the negation outside, \( \neg\exists m\, (\mathrm{Max}(A, m) \wedge \forall y\, (\mathrm{Max}(A, y) \to y = m) \wedge m = 1) \): it is true. The two readings agree whenever there is exactly one maximum, which is why "the" waits for \( \exists! \). The same trap sits in "\( \lim a_n \ne 0 \)" for a sequence with no limit, and analysis writes instead "the sequence converges, and its limit is not \( 0 \)".

::: {.check}
Over \( \nR \), may a proof speak of "the \( x \) with \( x \cdot x = 2 \)"? Of "the \( x \ge 0 \) with \( x \cdot x = 2 \)"?
:::

::: {.solution}
The first, no: \( \sqrt 2 \) and \( -\sqrt 2 \) both have square \( 2 \), so uniqueness fails. The second, yes: existence is the school fact of Section 5.1 (\( \sqrt 2 \) exists), and uniqueness holds, since two non-negative numbers with the same square are equal (if \( 0 \le u < v \), then \( u \cdot u < v \cdot v \)).
:::

## A function symbol and its graph

A function symbol gives every object exactly one value, since every term names an object (Section 5.2). A two-place predicate \( G(x, y) \) may or may not behave like that. Call \( G \) the **graph of a function** when \( \forall x\, \exists! y\, G(x, y) \): every \( x \) has exactly one partner. Then a new function symbol \( f \) may be introduced with the defining line \( \forall x\, G(x, f(x)) \), and \( f(t) \) is "the \( y \) such that \( G(t, y) \)": the name of the last subsection, with \( x \) as a parameter.

Over \( \nR \), \( G(x, y) \): \( y = x \cdot x + 1 \) is the graph of a function (existence: \( y = x \cdot x + 1 \) itself; uniqueness: two numbers equal to \( x \cdot x + 1 \) are equal). \( G(x, y) \): \( y \cdot y = x \) is not: \( x = -1 \) has no partner, and \( x = 4 \) has two, \( 2 \) and \( -2 \). For \( x \ge 0 \), the predicate \( y \ge 0 \wedge y \cdot y = x \) gives exactly one partner, and the function it defines is \( \sqrt{x} \), written only under the hypothesis \( x \ge 0 \) (the fold on partial terms in Section 5.2).

So "a function" and "a relation in which every object has exactly one partner" are two ways of saying the same thing; the function symbol is the shorter.

::: {.check}
Over \( \nZ \), is \( x = 2 \cdot y \) the graph of a function, with \( y \) as the value at \( x \)? Is \( y = 2 \cdot x \)?
:::

::: {.solution}
The first is not: \( x = 1 \) has no partner, since no integer \( y \) has \( 2y = 1 \). The second is: each \( x \) has exactly one partner, \( 2x \); the function is \( f(x) = 2x \).
:::

## Definitions add words, not facts

"An integer \( n \) is **even** if \( n = 2k \) for some integer \( k \)" adds a predicate symbol with its **definition** \( \forall x\, (\mathrm{Even}(x) \leftrightarrow \exists k\, (x = 2 \cdot k)) \). "We define \( \abs{x} \) to be \( x \) if \( x \ge 0 \) and \( -x \) otherwise" adds a function symbol. Its graph \( G(x, y) \): \( (x \ge 0 \wedge y = x) \vee (x < 0 \wedge y = -x) \) gives each \( x \) exactly one partner (one of \( x \ge 0 \), \( x < 0 \) holds and gives its \( y \), and the two cases exclude each other), and \( \abs{\cdot} \) is introduced by \( \forall x\, G(x, \abs{x}) \). A definition is a new premise, and premises prove things. The next result says what a definition can prove: nothing new about the old symbols.

::: {#prp-definitional-extension}
[Definitions Prove Nothing New]

Let \( \Gamma \) be a list of formulas and \( \psi \) a formula.

::: {.enumerate options="label=(\alph*)"}
1. Let \( P \) be a one-place predicate symbol that appears neither in \( \Gamma \) nor in \( \psi \), and \( \varphi \) a formula in which \( P \) does not appear and whose only free variable is \( x \). If \( \Gamma, \forall x\, (P(x) \leftrightarrow \varphi) \vdash \psi \), then \( \Gamma \vdash \psi \).
2. Let \( \varphi \) be a formula whose only free variable is \( x \), and \( c \) a constant that appears in none of \( \Gamma \), \( \varphi \), \( \psi \). If \( \Gamma \vdash \exists x\, \varphi \) and \( \Gamma, \varphi[c/x] \vdash \psi \), then \( \Gamma \vdash \psi \).
:::
:::

*In words: whatever is proved with a defined symbol, about symbols that were there before it, could have been proved without it. A definition makes proofs shorter, never stronger.*

Part (b) asks only for existence; uniqueness, as the subsection on "the \( x \) such that \( \varphi \)" said, is what makes "the" name one object. The same holds for predicates with several places, and for a function symbol \( f \) introduced by \( \forall x\, G(x, f(x)) \) once \( \forall x\, \exists! y\, G(x, y) \) is proved; we do not prove those cases, and nothing later depends on them.

::: {.idea}
For (b), rename \( c \) everywhere into a variable that appears nowhere, and put the whole derivation inside an \( \rulename{\exists E} \) box on \( \exists x\, \varphi \). For (a), replace every atomic formula \( P(t) \) by \( \varphi[t/x] \); the definition becomes \( \forall x\, (\varphi \leftrightarrow \varphi) \), which needs no premise. The fold below carries both out.
:::

::: {.second-reading title="Why definitions prove nothing new"}
::: {.proof}
(b) Let \( D \) be a derivation of \( \psi \) from \( \Gamma \) and \( \varphi[c/x] \). Choose a variable \( x_0 \) that appears nowhere in \( D \), \( \Gamma \), \( \varphi \) or \( \psi \) (a derivation from \( \Gamma \) need not write every member of \( \Gamma \)), and replace \( c \) by \( x_0 \) everywhere in \( D \). Every line stays a correct line: the rules treat constants and variables alike as terms; \( x_0 \) is not a flag or a witness name of \( D \), since it appears nowhere there; and it is bound nowhere, so every "free for" condition still holds. \( \Gamma \) and \( \psi \) do not contain \( c \) and do not change, and the premise \( \varphi[c/x] \) becomes \( \varphi[x_0/x] \), since \( c \) is not in \( \varphi \). Now take a derivation of \( \exists x\, \varphi \) from \( \Gamma \), open an \( \rulename{\exists E} \) box (@def-rules-existential) with the name \( x_0 \) and the assumption \( \varphi[x_0/x] \), copy the changed \( D \) inside it, and close the box on \( \psi \): by the choice of \( x_0 \), it is not in \( \psi \), not in \( \exists x\, \varphi \), and not in \( \Gamma \), which holds the only premises.

(a) Let \( D \) be a derivation of \( \psi \) from \( \Gamma \) and \( \forall x\, (P(x) \leftrightarrow \varphi) \). Rename the bound variables of \( \varphi \) to letters that appear nowhere in \( D \) (the convention of Section 5.2), and replace every atomic formula \( P(t) \) in \( D \) by \( \varphi[t/x] \). Because \( x \) is the only free variable of \( \varphi \) and its bound letters are new, the replacement commutes with every substitution a rule makes and changes no free variable of any line; so every line stays a correct line, and every side condition still holds. \( \Gamma \) and \( \psi \) do not contain \( P \) and do not change; the definition becomes \( \forall x\, (\varphi \leftrightarrow \varphi) \), which is derived from no premises by a flagged box, with a flag \( x_0 \) that appears nowhere in \( \Gamma \), \( \varphi \) or \( D \), ending in \( \varphi[x_0/x] \leftrightarrow \varphi[x_0/x] \), got by \( \rulename{{\leftrightarrow}I} \) from two one-line boxes. Writing that derivation in front of the changed \( D \) derives \( \psi \) from \( \Gamma \). (After the renaming the defining premise is \( \forall x\, (\varphi' \leftrightarrow \varphi) \), with \( \varphi' \) the renamed \( \varphi \), which the convention of Section 5.2 treats as \( \forall x\, (\varphi \leftrightarrow \varphi) \).)
:::
:::

**What a definition sounds like.** "We define …" and "call \( n \) even if …" introduce a symbol with its defining line; the right-hand side must not mention the new symbol, and a function needs exactly one value for each argument. "Let \( L \) be the limit of \( (a_n) \)" introduces a name by a description, and may be written only after it has been proved that there is exactly one such \( L \). Every "the" carries that debt; "a limit" does not.

::: {.remark}
[Looking ahead]

Chapter 8 collects "we define …" and "the …" with the other phrases of written proof.
:::

## Exercises

### A. Check your understanding

::: {#exr-counting-and-descriptions-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Write \( \exists! x\, (x \cdot x = 9) \) without the symbol \( \exists! \), and decide whether it is true over \( \nN \) and over \( \nZ \).
2. Write "exactly two integers \( x \) satisfy \( x \cdot x = 9 \)" by @def-counting-with-equality, and decide it over \( \nZ \).
3. When may a proof write "the \( x \) such that \( \varphi \)", and what may it then use about that object?
4. State in words the two parts of @prp-definitional-extension.
5. Exercise B1 of Section 5.7 showed that any two identities of an operation are equal. Explain how to turn its derivation into the second conjunct of @prp-unique-existence-use for \( \varphi = \forall z\, (x \cdot z = z \wedge z \cdot x = z) \).
:::
:::

::: {.solution}
*(a)* \( \exists x\, \bigl( x \cdot x = 9 \wedge \forall y\, (y \cdot y = 9 \to y = x) \bigr) \). Over \( \nN \) it is true: \( x = 3 \) works, and a natural number \( y \) with \( y \cdot y = 9 \) is \( 3 \), since \( y \le 2 \) gives \( y \cdot y \le 4 \) and \( y \ge 4 \) gives \( y \cdot y \ge 16 \). Over \( \nZ \) it is false: whatever \( x \) is proposed, \( 3 \) and \( -3 \) both satisfy \( y \cdot y = 9 \), and they cannot both equal \( x \).

*(b)* \( \exists x\, \exists y\, (x \ne y \wedge x \cdot x = 9 \wedge y \cdot y = 9) \wedge \forall x\, \forall y\, \forall z\, (x \cdot x = 9 \wedge y \cdot y = 9 \wedge z \cdot z = 9 \to x = y \vee x = z \vee y = z) \). True: \( 3 \ne -3 \) are two solutions, and every solution is \( 3 \) or \( -3 \) (since \( (y - 3)(y + 3) = 0 \)), so among three solutions two are equal.

*(c)* After \( \exists! x\, \varphi \) has been proved from the premises in hand. It may use the defining line \( \varphi[c/x] \), and only what follows from it with the premises.

*(d)* Part (a): adding a predicate symbol by a definition \( \forall x\, (P(x) \leftrightarrow \varphi) \) proves nothing new that does not mention \( P \). Part (b): naming a witness of a proved existential by a new constant proves nothing new that does not mention the constant.

*(e)* Take \( \varphi = \forall z\, (x \cdot z = z \wedge z \cdot x = z) \), and run lines 3–7 again with variables \( u_0 \), \( v_0 \) in place of \( e \), \( e' \): inside flagged boxes for \( u_0 \) and \( v_0 \) and a \( \rulename{{\to}I} \) box on \( \varphi[u_0/x] \wedge \varphi[v_0/x] \), the two premises (with \( z \) as their bound variable) come from that assumption by \( \rulename{\wedge E} \), and the same steps give \( u_0 = v_0 \). Then \( \rulename{{\to}I} \) and \( \rulename{\forall I} \) twice give \( \forall x\, \forall y\, (\varphi \wedge \varphi[y/x] \to x = y) \), the second conjunct of the proposition. With the existence of one identity as well, @prp-unique-existence-use gives "there is exactly one".
:::

::: {#exr-counting-and-descriptions-a2}
[A2: Drill]

Each part takes a line or two. The parts run from writing counting statements, through judging them and the counting words, to descriptions and graphs.

::: {.enumerate options="label=(\alph*)"}
1. Write \( \exists! x\, (x + 1 = 3) \) without \( \exists! \).
2. Write "at least two elements of \( A \) are negative".
3. Write "at most two \( x \) satisfy \( P(x) \)".
4. Write "exactly two \( x \) satisfy \( P(x) \)" as one formula of the shape \( \exists x\, \exists y\, (\dots \wedge \forall z\, (\dots)) \).
5. Does \( \exists x\, \exists y\, (P(x) \wedge P(y)) \) say "at least two \( x \) satisfy \( P(x) \)"?
6. Over \( \nN \), translate "\( 0 \) is the only natural number \( n \) with \( n + n = n \)", and decide it.
7. Translate "every prime except \( 2 \) is odd". Does your formula say that \( 2 \) is not odd?
8. Write "\( m \) is the smallest element of \( A \)", and say what must be proved before writing "the smallest element of \( A \)".
9. In \( A = \{2, 3, 4\} \), ordered by divisibility, which elements are maximal (no other element of \( A \) is a multiple of them), and is there a maximum (an element that is a multiple of every element of \( A \))?
10. \( A = (0, 1] \) has no smallest element. Read "the smallest element of \( A \) is not positive" both ways, and decide each.
11. Over \( \nR \), does \( x \cdot y = 1 \) give each \( x \) exactly one partner \( y \)? Over the non-zero reals?
12. A proof says "let \( c \) be the real number with \( c + 3 = 5 \)". What must have been proved, and what may be used about \( c \)?
:::
:::

::: {.solution}
(a) \( \exists x\, (x + 1 = 3 \wedge \forall y\, (y + 1 = 3 \to y = x)) \).

(b) \( \exists x\, \exists y\, (x \ne y \wedge (x \in A \wedge x < 0) \wedge (y \in A \wedge y < 0)) \).

(c) \( \forall x\, \forall y\, \forall z\, (P(x) \wedge P(y) \wedge P(z) \to x = y \vee x = z \vee y = z) \).

(d) \( \exists x\, \exists y\, (x \ne y \wedge P(x) \wedge P(y) \wedge \forall z\, (P(z) \to z = x \vee z = y)) \).

(e) No: \( x \) and \( y \) may name the same object; it says only \( \exists x\, P(x) \).

(f) \( 0 + 0 = 0 \wedge \forall x\, (x + x = x \to x = 0) \). True: \( x + x = x \) gives \( x = 0 \) by cancelling \( x \).

(g) \( \forall x\, (\mathrm{Prime}(x) \wedge x \ne 2 \to \mathrm{Odd}(x)) \). It says nothing about \( 2 \). If "except" is meant to say that \( 2 \) is not odd as well, add \( \wedge \neg\mathrm{Odd}(2) \).

(h) \( m \in A \wedge \forall a \in A\; (m \le a) \). Existence only: two smallest elements are each \( \le \) the other, hence equal, so uniqueness is automatic.

(i) \( 3 \) and \( 4 \) are maximal; \( 2 \) is not, since \( 4 \) is a multiple of \( 2 \). There is no maximum: \( 3 \) is not a multiple of \( 2 \) or of \( 4 \), and \( 4 \) is not a multiple of \( 3 \); and \( 2 \) is not a multiple of \( 3 \) either. Maximal and maximum differ.

(j) With \( \mathrm{Min}(A, m) \) the formula of (h): negation inside, \( \exists m\, (\mathrm{Min}(A, m) \wedge \forall y\, (\mathrm{Min}(A, y) \to y = m) \wedge \neg(m > 0)) \), false, since there is no \( m \). Negation outside, \( \neg\exists m\, (\mathrm{Min}(A, m) \wedge \forall y\, (\mathrm{Min}(A, y) \to y = m) \wedge m > 0) \), true. (For \( m \in A \), \( m/2 \in A \) is smaller.)

(k) No: \( x = 0 \) has none, since \( 0 \cdot y = 0 \). Over \( x \ne 0 \), yes: the partner is \( 1/x \), and \( x \cdot y = x \cdot y' = 1 \) gives \( y = y' \).

(l) \( \exists! x\, (x + 3 = 5) \): existence makes the name safe, uniqueness makes "the" right. It may use the defining line \( c + 3 = 5 \), and what follows from it, such as \( c = 2 \).
:::

### B. Practice

::: {#exr-counting-and-descriptions-b1}
[B1: Exactly two, by halves]

Over \( \nN \), show that exactly two natural numbers \( x \) satisfy \( x \cdot x < 3 \): write the statement by @def-counting-with-equality, then prove "at least two" and "at most two" separately.
:::

::: {.solution}
The statement is
\[
\exists x\, \exists y\, (x \ne y \wedge x \cdot x < 3 \wedge y \cdot y < 3) \wedge \forall x\, \forall y\, \forall z\, (x \cdot x < 3 \wedge y \cdot y < 3 \wedge z \cdot z < 3 \to x = y \vee x = z \vee y = z).
\]

*At least two:* \( 0 \) and \( 1 \): \( 0 \ne 1 \), \( 0 \cdot 0 = 0 < 3 \) and \( 1 \cdot 1 = 1 < 3 \).

*At most two:* if \( x \cdot x < 3 \) then \( x \le 1 \), since \( x \ge 2 \) gives \( x \cdot x \ge 4 \); so \( x \in \{0, 1\} \). Three natural numbers \( u \), \( v \), \( w \) with squares below \( 3 \) take values in \( \{0, 1\} \), so two of them are equal. Worked example type: @exm-exactly-two-solutions.

**Marking scheme.** (10 points) 3: the formula, with \( x \ne y \) and the three-way disjunction. 3: "at least two", with both witnesses and their difference. 4: "at most two", with \( x \le 1 \) justified and the pigeonhole step stated. Fatal error (0 for the half): "at least two" written without \( x \ne y \).
:::

::: {#exr-equality-and-uniqueness-b2}
[B2: A unique square root of zero]

Over \( \nR \), write \( \exists! x\, (x \cdot x = 0) \) without \( \exists! \), and prove it: existence, then uniqueness in the form "suppose \( y \) also satisfies …".

*Hint: a product of two non-zero reals is non-zero.*
:::

::: {.solution}
Written out, the statement is \( \exists x\, \bigl( x \cdot x = 0 \wedge \forall y\, (y \cdot y = 0 \to y = x) \bigr) \). We take the witness \( x = 0 \) and prove the two conjuncts.

*Existence.* \( 0 \cdot 0 = 0 \).

*Uniqueness.* Let \( y \) be a real number, and suppose \( y \cdot y = 0 \). If \( y \ne 0 \), then \( y \cdot y \) is a product of two non-zero reals and so is non-zero, which contradicts \( y \cdot y = 0 \). Hence \( y = 0 \), which is the witness. Since \( y \) was arbitrary, every \( y \) with \( y \cdot y = 0 \) equals \( 0 \).

So \( 0 \) witnesses the existential, and \( \exists! x\, (x \cdot x = 0) \) holds. The rules behind the words: "we take the witness \( x = 0 \)" is \( \rulename{\exists I} \), postponed to the end as usual; "let \( y \) be a real number" is a flagged box for \( \rulename{\forall I} \); "suppose \( y \cdot y = 0 \)" is a \( \rulename{{\to}I} \) box; "if \( y \ne 0 \) … contradicts" is an \( \rulename{RAA} \) box on \( y \ne 0 \). (That box gives \( y = 0 \) directly; \( \rulename{\neg I} \) would give only \( \neg(y \ne 0) \). Since for reals \( y = 0 \) or \( y \ne 0 \) is also a school fact, a proof by cases would do as well.)
:::

::: {#exr-equality-and-uniqueness-b3}
[B3: Exactly one fixed point]

A **fixed point** of a function \( f \colon \nR \to \nR \) is a real \( x \) with \( f(x) = x \).

::: {.enumerate options="label=(\alph*)"}
1. Formalize "\( f \) has exactly one fixed point" over \( \nR \), first with \( \exists! \) and then without it.
2. Write a formula without \( \exists! \) that says "\( f \) does **not** have exactly one fixed point", in the form "there is none, or there are two different ones".
3. Decide the statement of (a) for \( f(x) = x \cdot x \), for \( f(x) = x + 1 \) and for \( f(x) = 2 \cdot x \), and check your answer against the formula of (b).
:::
:::

::: {.solution}
*(a)* With \( \exists! \): \( \exists! x\, (f(x) = x) \). Written out, with \( y \) as the new variable: \( \exists x\, \bigl( f(x) = x \wedge \forall y\, (f(y) = y \to y = x) \bigr) \).

*(b)* \( \neg\exists x\, (f(x) = x) \vee \exists x\, \exists y\, \bigl( f(x) = x \wedge f(y) = y \wedge x \ne y \bigr) \). Read informally over \( \nR \): either no real number is fixed, or two different ones are. That is exactly the failure of "exactly one". If no \( x \) is fixed, the first disjunct holds. If some \( x \) is fixed but the uniqueness clause fails for it, then some \( y \) is fixed and differs from \( x \). Conversely, either disjunct rules out a unique fixed point: with none there is no witness, and two different fixed points \( x \ne y \) would both have to equal any proposed witness \( w \), giving \( x = y \). (Section 6.2 derives such negations mechanically, one quantifier at a time.)

*(c)* For \( f(x) = x \cdot x \): \( x \cdot x = x \) holds for \( x = 0 \) and for \( x = 1 \), so there are two different fixed points; (a) is false, and the second disjunct of (b) is true with \( x = 0 \), \( y = 1 \). For \( f(x) = x + 1 \): \( x + 1 = x \) has no solution, so (a) is false and the first disjunct of (b) is true. For \( f(x) = 2 \cdot x \): \( 2x = x \) gives \( x = 0 \), and \( 0 \) is fixed; so (a) is true with the witness \( 0 \), and both disjuncts of (b) are false.
:::

::: {#exr-counting-and-descriptions-b4}
[B4: The empty set is unique]

Read the domain as consisting of sets, and let \( E \) be the axiom of extensionality, \( \forall x\, \forall y\, (\forall z\, (z \in x \leftrightarrow z \in y) \to x = y) \).

::: {.enumerate options="label=(\alph*)"}
1. Derive \( E, \ \forall z\, \neg(z \in a), \ \forall z\, \neg(z \in b) \vdash a = b \).
2. Which half of "there is exactly one set with no elements" does (a) prove, and what would give the other half?
3. Suppose also \( \exists x\, \forall z\, \neg(z \in x) \). Which result of this section gives \( \exists! x\, \forall z\, \neg(z \in x) \), and what may a proof then write?
:::
:::

::: {.solution}
(a) The goal \( a = b \) is the consequent of an instance of \( E \); its hypothesis \( \forall z\, (z \in a \leftrightarrow z \in b) \) is built in a flagged box, each direction of the biconditional by \( \rulename{\bot E} \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (\forall z\, (z \in x \leftrightarrow z \in y) \to x = y)}
  \hypo {2} {\forall z\, \neg (z \in a)}
  \hypo {3} {\forall z\, \neg (z \in b)}
  \open[z_0]
  \open
  \hypo {4} {z_0 \in a}
  \have {5} {\neg (z_0 \in a)} \Ae{2}
  \have {6} {\bot} \ne{4,5}
  \have {7} {z_0 \in b} \be{6}
  \close
  \open
  \hypo {8} {z_0 \in b}
  \have {9} {\neg (z_0 \in b)} \Ae{3}
  \have {10} {\bot} \ne{8,9}
  \have {11} {z_0 \in a} \be{10}
  \close
  \have {12} {z_0 \in a \leftrightarrow z_0 \in b} \bi{4-7,8-11}
  \close
  \have {13} {\forall z\, (z \in a \leftrightarrow z \in b)} \Ai{4-12}
  \have {14} {\forall y\, (\forall z\, (z \in a \leftrightarrow z \in y) \to a = y)} \Ae{1}
  \have {15} {\forall z\, (z \in a \leftrightarrow z \in b) \to a = b} \Ae{14}
  \have {16} {a = b} \ie{15,13}
\end{nd}$
\end{center}
```

(b) "At most one": any two sets without elements are equal. The other half, "at least one", needs a premise of its own, an axiom saying that a set without elements exists: from \( E \) alone the claim \( \exists x\, \forall z\, \neg(z \in x) \) breaks. Counter-reading: the domain \( \{0\} \), with \( 0 \in 0 \). \( E \) is true, since there is only one object and so \( x = y \) holds for every \( x \), \( y \); and \( \exists x\, \forall z\, \neg(z \in x) \) is false, since the only object, \( 0 \), has the element \( 0 \).

(c) Run (a) with flags \( x_0 \), \( y_0 \) in place of \( a \), \( b \), inside a \( \rulename{{\to}I} \) box on \( \forall z\, \neg(z \in x_0) \wedge \forall z\, \neg(z \in y_0) \) (\( \rulename{\wedge E} \) gives the two premises), and close with \( \rulename{{\to}I} \) and \( \rulename{\forall I} \) twice: that is the second conjunct of @prp-unique-existence-use for \( \varphi = \forall z\, \neg(z \in x) \). With the existence premise, the direction \( \dashv \) of @prp-unique-existence-use gives \( \exists! x\, \forall z\, \neg(z \in x) \), and by @def-definite-description a proof may now say "**the** empty set" and name it \( \emptyset \). Worked example types: @exm-extensionality-logical-half (Section 5.7); the two halves of @prp-unique-existence-use.

**Marking scheme.** (10 points) 4: (a), the biconditional built by \( \rulename{{\leftrightarrow}I} \) from two boxes, each closed by \( \rulename{\bot E} \), then \( \rulename{\forall I} \), two \( \rulename{\forall E} \) on \( E \) and \( \rulename{{\to}E} \). 3: (b), "at most one" (1), existence as a separate premise (1), and the counter-reading with \( E \) checked true and the existence claim false (1). 3: (c), the flags and the \( \rulename{{\to}I} \) box, the right direction of @prp-unique-existence-use, and the license to write "the". Fatal error (0 for (a)): \( a = b \) "by extensionality" with no instance of \( E \) written.
:::

::: {#exr-counting-and-descriptions-b5}
[B5: Composites of one-to-one maps]

A function symbol \( f \) is **one-to-one** if \( \forall x\, \forall y\, (f(x) = f(y) \to x = y) \). Derive
\[
\forall x\, \forall y\, (f(x) = f(y) \to x = y), \;\; \forall x\, \forall y\, (g(x) = g(y) \to x = y) \;\vdash\; \forall x\, \forall y\, (f(g(x)) = f(g(y)) \to x = y),
\]
then write the proof in two sentences.
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (f(x) = f(y) \to x = y)}
  \hypo {2} {\forall x\, \forall y\, (g(x) = g(y) \to x = y)}
  \open[x_0]
  \open[y_0]
  \open
  \hypo {3} {f(g(x_0)) = f(g(y_0))}
  \have {4} {\forall y\, (f(g(x_0)) = f(y) \to g(x_0) = y)} \Ae{1}
  \have {5} {f(g(x_0)) = f(g(y_0)) \to g(x_0) = g(y_0)} \Ae{4}
  \have {6} {g(x_0) = g(y_0)} \ie{5,3}
  \have {7} {\forall y\, (g(x_0) = g(y) \to x_0 = y)} \Ae{2}
  \have {8} {g(x_0) = g(y_0) \to x_0 = y_0} \Ae{7}
  \have {9} {x_0 = y_0} \ie{8,6}
  \close
  \have {10} {f(g(x_0)) = f(g(y_0)) \to x_0 = y_0} \ii{3-9}
  \close
  \have {11} {\forall y\, (f(g(x_0)) = f(g(y)) \to x_0 = y)} \Ai{3-10}
  \close
  \have {12} {\forall x\, \forall y\, (f(g(x)) = f(g(y)) \to x = y)} \Ai{3-11}
\end{nd}$
\end{center}
```

Lines 4 and 5 instantiate the premise for \( f \) at the compound terms \( g(x_0) \) and \( g(y_0) \): the move *instantiate at the term you need*. In prose: "Let \( x \) and \( y \) satisfy \( f(g(x)) = f(g(y)) \). Since \( f \) is one-to-one, \( g(x) = g(y) \), and since \( g \) is one-to-one, \( x = y \)."

**Marking scheme.** (10 points) 2: the two flags and the \( \rulename{{\to}I} \) box. 4: the \( \rulename{\forall E} \) steps at \( g(x_0) \), \( g(y_0) \), then at \( x_0 \), \( y_0 \), each with \( \rulename{{\to}E} \). 2: the closing \( \rulename{\forall I} \) lines with the flag checks. 2: the prose, one sentence per use of one-to-one. Fatal error (0 for the derivation): the premise for \( f \) instantiated at \( x_0 \), \( y_0 \).
:::

### C. Going deeper

::: {#exr-equality-and-uniqueness-c1}
[C1: Two unique quantifiers do not commute]

Show that \( \exists! x\, \exists! y\, R(x, y) \) and \( \exists! y\, \exists! x\, R(x, y) \) can have different truth values, by giving a finite domain \( D \) and a two-place relation \( R \) on it for which the first is true and the second false. Check both, reading \( \exists! \) informally.

*Hint: first say in words what each sentence claims about the rows and columns of a table of \( R \).*
:::

::: {.solution}
**What any answer must satisfy.** Call \( x \) *single* if exactly one \( y \) has \( R(x, y) \), and call \( y \) *co-single* if exactly one \( x \) has \( R(x, y) \). The first sentence says that **exactly one** element is single. The second says that exactly one element is co-single. So an answer needs exactly one single element and a number of co-single elements other than one: none, or two or more.

**An example.** Take \( D = \{0, 1, 2\} \) and \( R = \{(1, 2), (2, 0), (2, 1)\} \).

- Single elements: \( 0 \) has no partner, \( 1 \) has exactly one (\( 2 \)), and \( 2 \) has two (\( 0 \) and \( 1 \)). So \( 1 \) is the only single element, and \( \exists! x\, \exists! y\, R(x, y) \) is true, with the witness \( 1 \).
- Co-single elements: \( y = 0 \) is reached only from \( x = 2 \); \( y = 1 \) only from \( x = 2 \); \( y = 2 \) only from \( x = 1 \). All three are co-single, so there is not exactly one, and \( \exists! y\, \exists! x\, R(x, y) \) is false.

No example exists on one or two elements (there are only \( 2 + 16 = 18 \) relations on such domains). On one element, \( 0 \) is single and co-single exactly when \( R(0, 0) \) holds, so the two sentences agree. On two elements, suppose exactly one element is single; after relabeling, call it \( 0 \), and let \( c \) be its only partner. Then \( 1 \) is not single, so it has no partners or two. If it has none, column \( c \) has one entry and the other column has none. If it has two, column \( c \) has two entries and the other column has one. Either way exactly one element is co-single. Exchanging the roles of rows and columns gives the converse, so the two sentences have the same truth value. Three elements is therefore the smallest possible domain.

The moral: \( \exists! \) is not a quantifier that commutes with its own kind, as two \( \exists \)'s do. "Exactly one" hides a \( \forall \) (the uniqueness clause), and the order of a \( \forall \) and an \( \exists \) matters.
:::

::: {#exr-equality-and-uniqueness-c2}
[C2: "At most one", two ways]

Let \( P \) be a one-place predicate symbol. Derive both directions of
\[
\forall x\, \forall y\, \bigl( P(x) \wedge P(y) \to x = y \bigr) \;\dashv\vdash\; \neg\exists x\, \exists y\, \bigl( (P(x) \wedge P(y)) \wedge x \ne y \bigr),
\]
and say which of your two derivations uses \( \rulename{RAA} \), and at which line.
:::

::: {.solution}
[Hint 1]

The right-hand side is a negation: for \( \vdash \), open a \( \rulename{\neg I} \) box, and inside it two \( \rulename{\exists E} \) boxes. For \( \dashv \), the goal is \( \forall\forall \), then an implication, then an equation.
:::

::: {.solution}
[Hint 2]

In the \( \dashv \) direction, open flagged boxes for \( x_0 \) and \( y_0 \) and a \( \rulename{{\to}I} \) box on \( P(x_0) \wedge P(y_0) \). The goal is now the atomic formula \( x_0 = y_0 \). Which resources can give it?
:::

::: {.solution}
\( (\vdash) \) The goal is a negation, so a \( \rulename{\neg I} \) box opens on \( \exists x\, \exists y\, (\dots) \); inside, the premise-directed step opens an \( \rulename{\exists E} \) box for each \( \exists \), with the goal \( \bot \) as each box's last line. The premise, instantiated at the two witnesses, gives \( x_0 = y_0 \), which clashes with \( x_0 \ne y_0 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (P(x) \wedge P(y) \to x = y)}
  \open
  \hypo {2} {\exists x\, \exists y\, ((P(x) \wedge P(y)) \wedge x \neq y)}
  \open[x_0]
  \hypo {3} {\exists y\, ((P(x_0) \wedge P(y)) \wedge x_0 \neq y)}
  \open[y_0]
  \hypo {4} {(P(x_0) \wedge P(y_0)) \wedge x_0 \neq y_0}
  \have {5} {P(x_0) \wedge P(y_0)} \ae{4}
  \have {6} {x_0 \neq y_0} \ae{4}
  \have {7} {\forall y\, (P(x_0) \wedge P(y) \to x_0 = y)} \Ae{1}
  \have {8} {P(x_0) \wedge P(y_0) \to x_0 = y_0} \Ae{7}
  \have {9} {x_0 = y_0} \ie{8,5}
  \have {10} {\bot} \ne{9,6}
  \close
  \have {11} {\bot} \Ee{3,4-10}
  \close
  \have {12} {\bot} \Ee{2,3-11}
  \close
  \have {13} {\neg \exists x\, \exists y\, ((P(x) \wedge P(y)) \wedge x \neq y)} \ni{2-12}
\end{nd}$
\end{center}
```

The brackets in the statement are written out because the default groups a longer conjunction to the right (Section 4.5); with the grouping \( (P(x_0) \wedge P(y_0)) \wedge x_0 \ne y_0 \) on line 4, \( \rulename{\wedge E} \) takes out its two halves on lines 5 and 6. At line 11, \( y_0 \) is not in \( \bot \), not in line 3, not in the premise, and not in the assumptions still open (lines 2 and 3). At line 12 the same holds for \( x_0 \), with line 2 the only open assumption.

\( (\dashv) \) The goal-directed steps open flagged boxes for \( x_0 \) and \( y_0 \) and a \( \rulename{{\to}I} \) box on \( P(x_0) \wedge P(y_0) \), leaving the goal \( x_0 = y_0 \). No resource gives an equation, so the search is stuck, and step 5 of the method applies: an \( \rulename{RAA} \) box on \( x_0 \ne y_0 \). Inside, \( \rulename{\wedge I} \) and two \( \rulename{\exists I} \) steps rebuild the formula that the premise denies.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \exists x\, \exists y\, ((P(x) \wedge P(y)) \wedge x \neq y)}
  \open[x_0]
  \open[y_0]
  \open
  \hypo {2} {P(x_0) \wedge P(y_0)}
  \open
  \hypo {3} {x_0 \neq y_0}
  \have {4} {(P(x_0) \wedge P(y_0)) \wedge x_0 \neq y_0} \ai{2,3}
  \have {5} {\exists y\, ((P(x_0) \wedge P(y)) \wedge x_0 \neq y)} \Ei{4}
  \have {6} {\exists x\, \exists y\, ((P(x) \wedge P(y)) \wedge x \neq y)} \Ei{5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {x_0 = y_0} \raa{3-7}
  \close
  \have {9} {P(x_0) \wedge P(y_0) \to x_0 = y_0} \ii{2-8}
  \close
  \have {10} {\forall y\, (P(x_0) \wedge P(y) \to x_0 = y)} \Ai{2-9}
  \close
  \have {11} {\forall x\, \forall y\, (P(x) \wedge P(y) \to x = y)} \Ai{2-10}
\end{nd}$
\end{center}
```

**The \( \dashv \) derivation uses \( \rulename{RAA} \), at line 8**: the box opens with \( x_0 \ne y_0 \), that is \( \neg(x_0 = y_0) \), and closes with \( x_0 = y_0 \). Closing it by \( \rulename{\neg I} \) instead would give \( \neg\neg(x_0 = y_0) \), and no rule of Chapter 1 or Sections 2.1–2.4 removes the double negation. (With the derived rule \( \rulename{\neg\neg E} \) of Section 2.5, that \( \rulename{\neg I} \) box followed by \( \rulename{\neg\neg E} \) is an equally good derivation; its classical step is the \( \rulename{\neg\neg E} \) line, which hides an \( \rulename{RAA} \).) The \( \vdash \) derivation uses no classical rule.

**Marking scheme.** (10 points)
- 2: \( \vdash \): opens a \( \rulename{\neg I} \) box on the existential, with the goal \( \bot \).
- 2: \( \vdash \): two \( \rulename{\exists E} \) boxes with **fresh** witnesses, each ending in \( \bot \), and the premise instantiated at those witnesses.
- 2: \( \dashv \): two flagged boxes and a \( \rulename{{\to}I} \) box, in the order read off the goal.
- 2: \( \dashv \): an \( \rulename{RAA} \) box on \( x_0 \ne y_0 \), with the clash obtained by \( \rulename{\wedge I} \) and two \( \rulename{\exists I} \) steps.
- 2: names the \( \dashv \) direction as the one using \( \rulename{RAA} \), and the line.
- A \( \rulename{\neg I} \) box on \( x_0 \ne y_0 \) followed by \( \rulename{\neg\neg E} \), or an \( \rulename{LEM} \) split on \( x_0 = y_0 \) whose second case reaches \( \bot \) the same way (then \( \rulename{\bot E} \)), earns the 2 points of the \( \rulename{RAA} \)-box line; for the naming line, the reader names the \( \rulename{\neg\neg E} \) or \( \rulename{LEM} \) line as the classical step, a derived rule whose derivation uses \( \rulename{RAA} \) (Section 2.5).
Fatal errors (0 for the step): an \( \rulename{\exists E} \) box closing on a line that contains its witness; a \( \rulename{\forall I} \) over a name in an open assumption; \( \rulename{\neg I} \) claimed to give \( x_0 = y_0 \).
:::

::: {#exr-counting-and-descriptions-c3}
[C3: One and one make two]

Let \( P \) and \( Q \) be one-place predicate symbols. Show that from \( \exists! x\, P(x) \), \( \exists! x\, Q(x) \) and \( \neg\exists x\, (P(x) \wedge Q(x)) \) it follows that exactly two \( x \) satisfy \( P(x) \vee Q(x) \), in the form
\[
\exists x\, \exists y\, \bigl( x \ne y \wedge (P(x) \vee Q(x)) \wedge (P(y) \vee Q(y)) \wedge \forall z\, (P(z) \vee Q(z) \to z = x \vee z = y) \bigr).
\]
Give the proof in numbered steps, naming the rule behind each; a full derivation is not required. Which premise does the conjunct \( x \ne y \) need, and what happens without it?
:::

::: {.solution}
1. By @prp-unique-existence-use, the first premise gives \( \exists x\, P(x) \) and "at most one \( P \)", and the second gives \( \exists x\, Q(x) \) and "at most one \( Q \)" (\( \rulename{\wedge E} \)).
2. Open two \( \rulename{\exists E} \) boxes early, with different names: \( P(a_0) \) and \( Q(b_0) \), both aimed at the goal.
3. \( a_0 \ne b_0 \): in a \( \rulename{\neg I} \) box on \( a_0 = b_0 \), \( \rulename{{=}E} \) turns \( P(a_0) \) into \( P(b_0) \); \( \rulename{\wedge I} \) with \( Q(b_0) \) and \( \rulename{\exists I} \) give \( \exists x\, (P(x) \wedge Q(x)) \), which \( \rulename{\neg E} \) clashes with the third premise.
4. \( P(a_0) \vee Q(a_0) \) and \( P(b_0) \vee Q(b_0) \) by \( \rulename{\vee I} \).
5. Let \( z_0 \) be arbitrary (a flagged box) with \( P(z_0) \vee Q(z_0) \) (a \( \rulename{{\to}I} \) box), and split by \( \rulename{\vee E} \). If \( P(z_0) \): "at most one \( P \)" at \( z_0 \) and \( a_0 \) (\( \rulename{\forall E} \) twice, \( \rulename{\wedge I} \), \( \rulename{{\to}E} \)) gives \( z_0 = a_0 \), and \( \rulename{\vee I} \) gives \( z_0 = a_0 \vee z_0 = b_0 \). If \( Q(z_0) \): "at most one \( Q \)" at \( z_0 \) and \( b \) gives \( z_0 = b_0 \), and \( \rulename{\vee I} \) again.
6. \( \rulename{{\to}I} \) and \( \rulename{\forall I} \) give the last conjunct; \( \rulename{\wedge I} \) joins the four; \( \rulename{\exists I} \) with the witness \( b_0 \) for \( y \), then \( a_0 \) for \( x \). Both \( \rulename{\exists E} \) boxes close, since the goal mentions neither name.

The third premise is used only in step 3. Without it the conclusion breaks: the domain \( \{0\} \) with \( P \) and \( Q \) both true of \( 0 \) makes the first two premises true, and only one object satisfies \( P(x) \vee Q(x) \).

**Marking scheme.** (10 points) 2: the two halves of each premise by @prp-unique-existence-use. 1: two \( \rulename{\exists E} \) boxes with different names. 2: \( a_0 \ne b_0 \) by \( \rulename{\neg I} \), \( \rulename{{=}E} \) and the third premise. 3: the last conjunct by the flagged box, the \( \rulename{{\to}I} \) box and \( \rulename{\vee E} \), each case using the right "at most one". 1: the closing \( \rulename{\exists I} \) order and the box conditions. 1: the counter-reading without the third premise. Fatal errors (0 for the step): \( a_0 \ne b_0 \) asserted because the names differ (the warning "Different letters, perhaps the same object"); an \( \rulename{\exists E} \) box closed on a line that mentions \( a_0 \) or \( b_0 \).
:::

### R. Review

::: {#exr-counting-and-descriptions-r1}
[R1]

Consider the terms built from variables, the constant \( 0 \) and the two-place function symbol \( + \). Show that in every such term the number of occurrences of \( + \) is one less than the number of occurrences of variables and constants, counted together. Check it on \( (x + 0) + (y + x) \).
:::

::: {.solution}
For a term \( t \), let \( a(t) \) count the occurrences of variables and constants in \( t \), and \( p(t) \) those of \( + \). We show \( p(t) = a(t) - 1 \) for every \( t \), by induction on the clauses of @def-term, the method of @thm-structural-induction (Section 4.3).

*Base:* \( t \) is a variable or \( 0 \). Then \( p(t) = 0 \) and \( a(t) = 1 \).

*Step:* \( t \) is \( t_1 + t_2 \), and the claim holds for \( t_1 \) and \( t_2 \). Then
\[
p(t) = p(t_1) + p(t_2) + 1 = (a(t_1) - 1) + (a(t_2) - 1) + 1 = a(t_1) + a(t_2) - 1 = a(t) - 1.
\]

The term \( (x + 0) + (y + x) \) has four occurrences of variables and constants and three of \( + \). This is the counting argument of @lem-parenthesis-count (Section 4.3), on new data. About 10 minutes.

**Marking scheme.** (10 points) 2: \( a \) and \( p \) defined. 3: the base case, both kinds of atomic term. 4: the step, with the hypothesis used for both \( t_1 \) and \( t_2 \) and the \( +1 \) for the new symbol. 1: the check. Fatal error (0 for the step): induction on the length of the term with no case for \( t_1 + t_2 \).
:::

::: {#exr-counting-and-descriptions-r2}
[R2]

Derive \( \forall x\, (\neg Q(x) \to \neg P(x)) \vdash \forall x\, (P(x) \to Q(x)) \), and name the line that uses a classical rule.
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (\neg Q(x) \to \neg P(x))}
  \open[x_0]
  \open
  \hypo {2} {P(x_0)}
  \have {3} {\neg Q(x_0) \to \neg P(x_0)} \Ae{1}
  \open
  \hypo {4} {\neg Q(x_0)}
  \have {5} {\neg P(x_0)} \ie{3,4}
  \have {6} {\bot} \ne{2,5}
  \close
  \have {7} {Q(x_0)} \raa{4-6}
  \close
  \have {8} {P(x_0) \to Q(x_0)} \ii{2-7}
  \close
  \have {9} {\forall x\, (P(x) \to Q(x))} \Ai{2-8}
\end{nd}$
\end{center}
```

Line 9 cites the flagged box from line 2, the convention for a flagged box that immediately contains another; \( x_0 \) is in no premise, in no open assumption, and not in line 9. Lines 2 and 4–8 are the derivation of @prp-contrapositive-converse (Section 2.5) at \( P(x_0) \), \( Q(x_0) \), with line 3 as its premise. The classical line is line 7, \( \rulename{RAA} \) (@def-rule-raa). About 10 minutes.

**Marking scheme.** (10 points) 2: the flagged box opened first and closed by \( \rulename{\forall I} \) with the flag checked. 2: \( \rulename{\forall E} \) at the flag. 4: the \( \rulename{{\to}I} \) box and, inside it, the \( \rulename{RAA} \) box on \( \neg Q(x_0) \). 2: line 7 named as the classical line. A \( \rulename{\neg I} \) box on \( \neg Q(x_0) \) followed by \( \rulename{\neg\neg E} \), or @prp-contrapositive-converse used as a derived rule on line 3, earns the 4 points of the box line; its classical line (the \( \rulename{\neg\neg E} \) line, or the derived-rule line, whose derivation uses \( \rulename{RAA} \)) earns the naming 2. Fatal error (0): \( \rulename{\forall E} \) outside the flagged box at a constant, then \( \rulename{\forall I} \) over that constant.
:::

::: {#exr-counting-and-descriptions-r3}
[R3]

You have derived \( (P \wedge Q) \to R \vdash P \to (Q \to R) \). Derive \( \forall x\, ((P(x) \wedge Q(x)) \to R(x)) \vdash \forall x\, (P(x) \to (Q(x) \to R(x))) \), and say which lines are the propositional derivation and what the quantifier adds.
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, ((P(x) \wedge Q(x)) \to R(x))}
  \open[x_0]
  \have {2} {(P(x_0) \wedge Q(x_0)) \to R(x_0)} \Ae{1}
  \open
  \hypo {3} {P(x_0)}
  \open
  \hypo {4} {Q(x_0)}
  \have {5} {P(x_0) \wedge Q(x_0)} \ai{3,4}
  \have {6} {R(x_0)} \ie{2,5}
  \close
  \have {7} {Q(x_0) \to R(x_0)} \ii{4-6}
  \close
  \have {8} {P(x_0) \to (Q(x_0) \to R(x_0))} \ii{3-7}
  \close
  \have {9} {\forall x\, (P(x) \to (Q(x) \to R(x)))} \Ai{2-8}
\end{nd}$
\end{center}
```

Lines 3–8 are the first derivation of @prp-curry (Section 1.4) at the statements \( P(x_0) \), \( Q(x_0) \), \( R(x_0) \), with line 2 as its premise. The quantifier adds line 2 (\( \rulename{\forall E} \) at the flag) and line 9 (\( \rulename{\forall I} \)), whose side condition holds because the boxes of lines 3 and 4 have closed. About 10 minutes.

**Marking scheme.** (10 points) 3: the flagged box with \( \rulename{\forall E} \) at the flag. 4: the two \( \rulename{{\to}I} \) boxes in the order of @prp-curry. 3: the propositional lines named and the side condition of line 9 checked. Fatal error (0): \( \rulename{\forall I} \) written while the box of line 3 or 4 is open.
:::

::: {#exr-counting-and-descriptions-r4}
[R4]

Derive \( \forall x\, \forall y\, (f(x) = y \to g(y) = x) \vdash \forall x\, (g(f(x)) = x) \).
:::

::: {.solution}
```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, (f(x) = y \to g(y) = x)}
  \open[x_0]
  \have {2} {\forall y\, (f(x_0) = y \to g(y) = x_0)} \Ae{1}
  \have {3} {f(x_0) = f(x_0) \to g(f(x_0)) = x_0} \Ae{2}
  \have {4} {f(x_0) = f(x_0)} \eqi{}
  \have {5} {g(f(x_0)) = x_0} \ie{3,4}
  \close
  \have {6} {\forall x\, (g(f(x)) = x)} \Ai{2-5}
\end{nd}$
\end{center}
```

The tools: instantiate at the term you need (@def-rule-universal-elimination, Section 5.3), here the compound term \( f(x_0) \) at line 3, and \( \rulename{{=}I} \) (@def-rules-equality, Section 5.7), which makes the hypothesis of line 3 at no cost. Why the look-alikes fail: \( \rulename{{=}E} \) has no equation to cite, since no line is an equation until \( \rulename{{=}I} \) writes one; \( \rulename{\forall E} \) at a fresh variable \( y_0 \) leaves the hypothesis \( f(x_0) = y_0 \), which nothing proves; and there is no existential, so \( \rulename{\exists E} \) has nothing to open. About 15 minutes.

**Marking scheme.** (10 points) 2: the flagged box. 4: the second \( \rulename{\forall E} \), at \( f(x_0) \). 3: \( \rulename{{=}I} \) and \( \rulename{{\to}E} \). 1: the closing \( \rulename{\forall I} \) with the flag checked. Fatal error (0): \( \rulename{\forall E} \) at a variable \( y_0 \) followed by a step that treats \( f(x_0) = y_0 \) as proved.
:::

<!-- dependency ledger
def-unique-existence (claim): well-definedness: two admissible choices of y differ by renaming a bound variable | F1.4 §02 (renaming bound variables)
def-unique-existence (claim): well-definedness: (phi[y/x])[t/y] = phi[t/x] for y not in phi | def-substitution (cited); structural induction proved in the text, using the F1.4 §02 claim that x not free gives phi[t/x] = phi
def-unique-existence (example): 3 + 2 = 5 and y + 2 = 5 gives y = 3; y <= 1 gives y*y <= 1, y >= 3 gives y*y >= 9; 0 + y = y; z + 0 = z | school arithmetic
def-unique-existence (claim): example 3: the uniqueness step z + 0 = 0 and z + 0 = z give z = 0 | prp-equality-symmetric-transitive (cited in the text by name "symmetry and transitivity")
def-unique-existence (claim): Quick check: over N every number below 1 is 0; over Z, 0 and -1 are below 1 | school arithmetic
prp-unique-existence-use (proof): (phi[y/x])[t/y] = phi[t/x] for y not in phi; phi[y/x] has no free x; phi[t/x] has no y for t without y | first fact: def-unique-existence (well-definedness paragraph, cited); def-substitution (cited); second and third read off def-substitution
prp-unique-existence-use (proof): lines 13-14 and 10-11 are symmetry written out | prp-equality-symmetric-transitive (cited)
prp-unique-existence-use (example): the maximum: a <= b and b <= a give a = b; (0, 1) has no maximum | school algebra (order); AN1.1 (index, Where this goes)
def-counting-with-equality (claim): "at most one" is the second conjunct of prp-unique-existence-use | prp-unique-existence-use (cited)
exm-exactly-two-solutions (solution): y*y = 1 gives (y - 1)(y + 1) = 0, so y = 1 or y = -1; 1 != -1 | school algebra; checked by verify/ch05/exm-exactly-two-solutions.py
def-counting-with-equality (claim): Quick check: an even prime is divisible by 2, so it is 2 | school arithmetic
def-definite-description (claim): Gamma, phi[c/x], phi[c'/x] |- c = c' | prp-unique-existence-use (cited), def-rule-universal-elimination; the three substitution facts of the proof of prp-unique-existence-use (cited)
def-definite-description (claim): the proposition at the end of the section shows the defining line proves nothing new | prp-definitional-extension (same section, later; cited forward within the section)
def-definite-description (claim): two readings: (0, 1) has no maximum, m < (m + 1)/2 < 1 for m in (0, 1) | school algebra; checked by verify/ch05/def-definite-description.py
def-definite-description (claim): Quick check: sqrt 2 exists; 0 <= u < v gives u*u < v*v | school fact, F1.4 §01 (stated as such); AN1.1 (index, Where this goes); school algebra
def-definite-description (claim): graph: y = x*x + 1 has one partner per x; y*y = x has none at -1 and two at 4; y >= 0 and y*y = x has one for x >= 0 | school algebra; sqrt x exists for x >= 0: school fact, AN1.1 (index, Where this goes)
def-definite-description (claim): graph Quick check: 2y = 1 has no integer solution | school arithmetic
def-definite-description (claim): remark: a function symbol is the same as a graph with one partner per object | not proved; nothing depends on it
prp-definitional-extension (claim): text: the graph of |x| gives exactly one partner per x | school algebra (trichotomy of x >= 0, x < 0)
prp-definitional-extension (proof): fold: (b) constant to fresh variable keeps a derivation, then an exists-E box; (a) replacing P(t) by phi[t/x] commutes with substitution | def-rules-existential (cited); F1.4 §02 (renaming bound variables, the convention); def-rules-universal, iff-I for forall x (phi <-> phi)
prp-definitional-extension (claim): remark: the several-place and function-symbol cases | not proved; nothing later depends on them
exr-counting-and-descriptions-a1 (solution): y <= 2 gives y*y <= 4, y >= 4 gives y*y >= 16; (y - 3)(y + 3) = 0 | school arithmetic
exr-counting-and-descriptions-a2 (solution): divisibility on {2, 3, 4}; m/2 in (0, m) for m in (0, 1]; x + x = x gives x = 0 in N; 0 * y = 0; a <= b and b <= a give a = b; x*y = x*y' with x != 0 gives y = y' | school arithmetic; checked by verify/ch05/exr-counting-and-descriptions-a2.py
exr-counting-and-descriptions-b1 (solution): x*x < 3 iff x in {0, 1} over N | school arithmetic; checked by verify/ch05/exr-counting-and-descriptions-b1.py
exr-equality-and-uniqueness-b2 (solution): a product of two non-zero reals is non-zero; for reals y = 0 or y != 0 | school algebra (stated in the hint); AN1.1 (index, Where this goes)
exr-equality-and-uniqueness-b3 (solution): x*x = x iff x in {0, 1}; x + 1 = x has no solution; 2x = x iff x = 0 | school algebra
exr-equality-and-uniqueness-b3 (solution): not exactly one x has phi iff no x has phi or two different x have phi, read informally | informal truth over a domain, F1.4 §01 (the mirror-image remark on the two quantifiers), argued both ways in the solution; F1.8 §02 pointed at only, nothing depends on it
exr-counting-and-descriptions-b4 (solution): the 16-line derivation; (b)'s counter-reading on {0} with 0 in 0 | sets used informally, F2.1 (index, Where this goes); finite counter-reading, checked by verify/ch05/exr-counting-and-descriptions-b4.py; prp-unique-existence-use, def-definite-description (cited)
exr-equality-and-uniqueness-c1 (solution): no separating relation on 1 or 2 elements (18 relations) | case argument in the solution (rows and columns of a 2-element table)
exr-equality-and-uniqueness-c2 (solution): no rule of F1.1 or F1.2 §01-F1.2 §04 removes a double negation | F1.2 §05's discussion (thm-raa-independent, F1.3, optional; pointed at only, nothing depends on it)
exr-equality-and-uniqueness-c2 (solution): a longer conjunction groups to the right by default, so the brackets are written | F1.3 §05 (grouping convention)
exr-equality-and-uniqueness-c2 (solution): the alternative routes by the derived rules not-not-E and LEM | F1.2 §05 (derived rules)
exr-counting-and-descriptions-c3 (solution): the two halves of each premise; the counter-reading on {0} without the third premise | prp-unique-existence-use (cited); finite counter-reading
exr-counting-and-descriptions-r1 (solution): p(t) = a(t) - 1 by structural induction on terms | def-term, thm-structural-induction, lem-parenthesis-count (cited); checked by verify/ch05/exr-counting-and-descriptions-r1.py
exr-counting-and-descriptions-r2 (solution): lines 2, 4-8 are the derivation of prp-contrapositive-converse | prp-contrapositive-converse, def-rule-raa (cited)
exr-counting-and-descriptions-r3 (solution): lines 3-8 are the derivation of prp-curry | prp-curry (cited)
exr-counting-and-descriptions-r4 (solution): forall-E at the compound term f(x_0) and =I | def-rule-universal-elimination, def-rules-equality (cited)
-->
