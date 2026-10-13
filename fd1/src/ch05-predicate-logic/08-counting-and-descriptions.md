# Unique Existence, Counting and Descriptions

*S3-PLACEHOLDER: opening frame of Section 5.8, split off in D2.*

## Unique existence

Mathematics says "**the** limit of the sequence", "**the** supremum of \( A \)", "**the** additive inverse of \( a \)". Each "the" makes two claims. There is such an object, and there is only one, so that the name picks it out. The second claim is the one that is easy to forget, and the one the claim at the end of Section 5.7 was about.

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

**Well-definedness.** The abbreviation seems to depend on the choice of \( y \). It does not, up to renaming a bound variable (Section 5.2). The argument rests on one fact about substitution, used again below: *if \( y \) does not appear in \( \varphi \), then replacing \( x \) by \( y \) and then \( y \) by a term \( t \) is the same as replacing \( x \) by \( t \)*, that is, \( (\varphi[y/x])[t/y] \) is \( \varphi[t/x] \). This is a structural induction on \( \varphi \) of the kind in Section 5.2. In a term, the \( y \)'s of \( s[y/x] \) are exactly the former \( x \)'s, so \( (s[y/x])[t/y] = s[t/x] \); atomic formulas, \( \bot \) and the connectives follow clause by clause. For \( \forall x\, \psi \), both sides are \( \forall x\, \psi \), since substitution for \( x \) stops at \( \forall x \) and \( y \) does not appear in \( \psi \) (the second fact of Section 5.2). For \( \forall z\, \psi \) with \( z \) not \( x \), also \( z \) is not \( y \), because \( y \) does not appear in \( \varphi \); so both substitutions pass under the quantifier and the induction hypothesis applies, and \( \exists \) is the same. Now let \( y \) and \( y' \) be two admissible choices. If they are the same variable there is nothing to show. Otherwise \( y' \) does not appear in \( \varphi[y/x] \to y = x \), since it is neither \( x \) nor \( y \) and does not appear in \( \varphi \); so the bound \( y \) of \( \forall y\, (\varphi[y/x] \to y = x) \) may be renamed \( y' \), which gives \( \forall y'\, \bigl( (\varphi[y/x])[y'/y] \to y' = x \bigr) \). By the fact with \( t = y' \), this is \( \forall y'\, (\varphi[y'/x] \to y' = x) \), the formula written with \( y' \).

**Why \( y \) must not appear in \( \varphi \).** The condition keeps the new quantifier \( \forall y \) from capturing anything of \( \varphi \)'s own. Take \( \varphi = (x \le y) \), in which \( y \) is free, and read over \( \nN \) with \( y \) naming \( 0 \). "There is exactly one natural number \( x \) with \( x \le 0 \)" is true: \( x = 0 \). The formula written with the forbidden bound variable \( y \) is
\[
\exists x\, \bigl( x \le y \wedge \forall y\, (y \le y \to y = x) \bigr),
\]
because \( (x \le y)[y/x] \) is \( y \le y \). Its second conjunct says that **every** natural number equals \( x \), which is false. The free \( y \) of \( \varphi \), which was to name \( 0 \), has been captured by \( \forall y \). With an admissible variable, say \( z \), the formula is \( \exists x\, \bigl( x \le y \wedge \forall z\, (z \le y \to z = x) \bigr) \), which is true.

**Examples.** Simplest first; each is read over the domain named, with the informal truth of Section 5.1.

1. Over \( \nR \), \( \exists! x\, (x + 2 = 5) \) is true. *Existence:* \( 3 + 2 = 5 \). *Uniqueness:* if \( y + 2 = 5 \), then subtracting \( 2 \) gives \( y = 3 \), so \( y \) is the \( x \) already found.
2. Over \( \nN \), \( \exists! x\, (x \cdot x = 4) \) is true. *Existence:* \( 2 \cdot 2 = 4 \). *Uniqueness:* for a natural number \( y \), if \( y \le 1 \) then \( y \cdot y \le 1 \), and if \( y \ge 3 \) then \( y \cdot y \ge 9 \); so \( y \cdot y = 4 \) forces \( y = 2 \).
3. Over \( \nR \), \( \exists! x\, \forall y\, (x + y = y) \) is true: \( 0 \) is the **unique** additive identity. *Existence:* \( 0 + y = y \) for every \( y \). *Uniqueness:* suppose \( z + y = y \) for every \( y \). Apply this to the one instance \( y = 0 \) (by \( \rulename{\forall E} \)): \( z + 0 = 0 \). Since also \( z + 0 = z \), symmetry and transitivity give \( z = 0 \). The whole uniqueness proof is the choice of the instance \( y = 0 \).
4. **Degenerate.** For any constant \( c \), \( \exists! x\, (x = c) \) holds in every domain, and it is derivable from no premises (the derivation follows). By contrast, \( \exists! x\, (x = x) \) says that the domain has exactly one element, which is false in \( \nN \), \( \nZ \) and \( \nR \): existence holds and uniqueness fails.

**Nonexample by minimal change.** Keep example 2 and change the domain to \( \nZ \). Existence still holds, with the same witness \( 2 \). Uniqueness fails: \( y = -2 \) also satisfies \( y \cdot y = 4 \), and \( -2 \ne 2 \). So over \( \nZ \), \( \exists! x\, (x \cdot x = 4) \) is false, and the failing clause is exactly the second conjunct.

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

In practice this is how "there is exactly one" is proved: an existence proof, then a separate "suppose \( x \) and \( y \) both satisfy \( \varphi \); then \( x = y \)". And it is how it is used: from \( \exists! x\, \varphi \) we may take a witness, and we may identify any two objects with the property. The claim about additive inverses at the end of Section 5.7 was the "at most one" half; existence of an inverse is a field axiom.

**One more instance: "the maximum".** A **maximum** of a set \( A \) of reals is an element \( m \in A \) with \( a \le m \) for every \( a \in A \). If \( m \) and \( m' \) are both maxima, then \( m' \le m \) (apply the property of \( m \) to the element \( m' \in A \)) and \( m \le m' \) (apply the property of \( m' \) to \( m \in A \)), so \( m = m' \) by the order fact that \( a \le b \) and \( b \le a \) give \( a = b \). That is "at most one"; a set may have no maximum at all, such as \( (0, 1) \), so existence is a separate question. Only when both halves are known may we write "the maximum of \( A \)".

## Exercises

### A. Check your understanding

<!-- S3-PLACEHOLDER: items -->

### B. Practice

::: {#exr-equality-and-uniqueness-b2}
[B2: A unique square root of zero]

Over \( \nR \), write \( \exists! x\, (x \cdot x = 0) \) without \( \exists! \), and prove it: existence, then uniqueness in the form "suppose \( y \) also satisfies …".

*Hint: a product of two nonzero reals is nonzero.*
:::

::: {.solution}
Written out, the statement is \( \exists x\, \bigl( x \cdot x = 0 \wedge \forall y\, (y \cdot y = 0 \to y = x) \bigr) \). We take the witness \( x = 0 \) and prove the two conjuncts.

*Existence.* \( 0 \cdot 0 = 0 \).

*Uniqueness.* Let \( y \) be a real number, and suppose \( y \cdot y = 0 \). If \( y \ne 0 \), then \( y \cdot y \) is a product of two nonzero reals and so is nonzero, which contradicts \( y \cdot y = 0 \). Hence \( y = 0 \), which is the witness. Since \( y \) was arbitrary, every \( y \) with \( y \cdot y = 0 \) equals \( 0 \).

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

<!-- dependency ledger
def-unique-existence (well-definedness): two admissible choices of y differ by renaming a bound variable | F1.4 §02 (renaming bound variables)
def-unique-existence (well-definedness): (phi[y/x])[t/y] = phi[t/x] for y not in phi | def-substitution (cited); structural induction proved in the text, using the F1.4 §02 claim that x not free gives phi[t/x] = phi
def-unique-existence (examples): 3 + 2 = 5 and y + 2 = 5 gives y = 3; y <= 1 gives y*y <= 1, y >= 3 gives y*y >= 9; 0 + y = y; z + 0 = z | school arithmetic
def-unique-existence (example 3): the uniqueness step z + 0 = 0 and z + 0 = z give z = 0 | prp-equality-symmetric-transitive (cited in the text by name "symmetry and transitivity")
prp-unique-existence-use (proof): (phi[y/x])[t/y] = phi[t/x] for y not in phi; phi[y/x] has no free x; phi[t/x] has no y for t without y | first fact: def-unique-existence (well-definedness paragraph, cited); def-substitution (cited); second and third read off def-substitution
prp-unique-existence-use (proof): lines 13-14 and 10-11 are symmetry written out | prp-equality-symmetric-transitive (cited)
prp-unique-existence-use (example, the maximum): a <= b and b <= a give a = b; (0, 1) has no maximum | school algebra (order); AN1.1 (prose pointer)
exr-equality-and-uniqueness-b2 (solution): a product of two non-zero reals is non-zero; for reals y = 0 or y != 0 | school algebra (stated in the hint); AN1.1 (prose pointer)
exr-equality-and-uniqueness-b3 (solution): x*x = x iff x in {0, 1}; x + 1 = x has no solution; 2x = x iff x = 0 | school algebra
exr-equality-and-uniqueness-b3 (solution): not exactly one x has phi iff no x has phi or two different x have phi, read informally | informal truth over a domain, F1.4 §01 (the mirror-image remark on the two quantifiers), argued both ways in the solution; F1.8 §02 pointed at only, nothing depends on it
exr-equality-and-uniqueness-c1 (solution): no separating relation on 1 or 2 elements (18 relations) | case argument in the solution (rows and columns of a 2-element table)
exr-equality-and-uniqueness-c2 (solution): no rule of F1.1 or F1.2 §01-F1.2 §04 removes a double negation | F1.2 §05's discussion (thm-raa-independent, F1.3, optional; pointed at only, nothing depends on it)
exr-equality-and-uniqueness-c2 (solution): a longer conjunction groups to the right by default, so the brackets are written | F1.3 §05 (grouping convention)
exr-equality-and-uniqueness-c2 (solution): the alternative routes by the derived rules not-not-E and LEM | F1.2 §05 (derived rules)
-->
