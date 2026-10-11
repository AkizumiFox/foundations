# Models and Counter-models

Sections 4.3 to 4.10 derived a good deal, and some searches stalled. The converse of @prp-exists-forall-swap could not be finished: every attempt ran into a side condition. The converse of @prp-exists-and stalled in the same way, and so did the search for \( \exists x\, P(x) \vdash P(c) \) in @exr-existential-introduction-c2. But a search that fails proves nothing, since a cleverer derivation might exist. Chapter 3 met the same problem for the connectives and solved it with meaning: a row of a truth table that makes the premises true and the conclusion false rules out every derivation at once (@cor-refuting-row). This section builds the meaning of a quantified formula. A row of \( \mathrm{T} \) and \( \mathrm{F} \) is replaced by a **model**: a domain of objects, with a meaning for every symbol. A model that makes the premises true and the conclusion false is a **counter-model**, and it is the tool that settles the stalled searches.

## Why a row is not enough

Chapter 3's semantics gave each atom a truth value and computed the rest. Try it on the stalled sequent of @prp-exists-forall-swap's converse,
\[
\forall y\, \exists x\, R(x, y) \vdash \exists x\, \forall y\, R(x, y) .
\]
Neither side has a main connective among \( \neg, \wedge, \vee, \to, \leftrightarrow \): each is a quantified formula, and a truth table would have to treat each as one atom. The sequent would become \( p \vdash q \), refuted by the row \( p = \mathrm{T} \), \( q = \mathrm{F} \). That "refutation" is worthless. The same reading refutes \( \forall x\, P(x) \vdash \exists x\, P(x) \), which is derivable (@prp-forall-implies-exists). Treating a quantified formula as an atom throws away exactly the structure that the quantifier rules use.

So what does make \( \forall y\, \exists x\, R(x, y) \) true or false? Section 4.1 read such sentences informally, **over a domain**: "for every \( y \) in the domain there is an \( x \) in the domain with \( R(x, y) \)". To decide it we need three things.

- **A domain**: the objects the variables range over. Over \( \nZ \) the sentence may be true and over a three-element set false.
- **A meaning for each symbol.** \( R \) is a predicate symbol, a name with two slots and no meaning of its own (Section 4.2). Read as \( > \) on \( \nZ \), the sentence says "every integer has an integer above it", which is true; read as \( < \) on \( \nN \), it says "every natural number has a natural number below it", which is false at \( y = 0 \).
- **Values for the free variables**, if there are any. The formula \( \exists y\, (y < x) \) is neither true nor false on \( \nN \) until we know which number \( x \) is.

The first two together are a **structure**; the third is an **assignment**. A structure with an assignment decides every formula, by clauses that read the quantifiers as Section 4.1 read them. That is all this section does, and then it uses the result.

## Structures

Situate the notion first. A formula is built from **symbols**: constants such as \( c \) and \( 0 \), function symbols such as \( f \) and \( + \), predicate symbols such as \( P \), \( R \) and \( < \), each function and predicate symbol with its number of argument places, its **arity** (Section 4.2, @def-term and @def-first-order-formula). The symbol \( = \) is special: it is part of the logic, with rules of its own (@def-rules-equality), and it will always mean the same thing. A structure gives every other symbol a meaning.

*A structure is a non-empty set of objects together with a meaning for each symbol: an object for each constant, an operation for each function symbol, and a relation for each predicate symbol.*

::: {#def-structure}
[Structure]

Fix a collection of constants, function symbols and predicate symbols, each function and predicate symbol with its arity \( n \ge 1 \). A **structure** \( \fM \) (also called a **model**) for these symbols consists of

::: {.enumerate options="label=(M\arabic*)"}
1. a **non-empty** set \( D \), the **domain** of \( \fM \);
2. for each constant \( c \), an element \( c^{\fM} \in D \);
3. for each function symbol \( f \) of arity \( n \), a function \( f^{\fM} \colon D^n \to D \), defined at **every** \( n \)-tuple of elements of \( D \);
4. for each predicate symbol \( R \) of arity \( n \), a set \( R^{\fM} \) of \( n \)-tuples of elements of \( D \).
:::

The symbol \( = \) is not interpreted by \( \fM \): in every structure it means **identity**, "is the same element of \( D \) as".
:::

In words. (M1) says what the variables range over, and insists that there is at least one object. (M2) says which object each name names; two constants may name the same object. (M3) makes each function symbol an operation that can be applied to **any** objects of the domain and always returns an object of the domain. (M4) makes each predicate symbol a relation: \( R^{\fM} \) is the set of tuples for which \( R \) "holds". A one-place predicate symbol \( P \) becomes a subset \( P^{\fM} \subseteq D \), a two-place one a set of ordered pairs, and so on. Here \( D^n \) is the set of \( n \)-tuples \( (d_1, \dots, d_n) \) of elements of \( D \); Chapter 6 develops sets, pairs and functions properly, and this section uses only their everyday meaning.

We usually describe a structure in one line, naming the domain and the meaning of each symbol, and write "\( \fM = (\nZ, <) \)" for the structure with domain \( \nZ \) in which the symbol \( < \) means the usual order. When a symbol has its usual meaning on a familiar set, we say so and do not write \( <^{\fM} \).

**Examples**, simplest first.

- *One element.* \( D = \{ a \} \), with \( P^{\fM} = \{ a \} \). This is the degenerate structure. Every variable must take the value \( a \), so "for every element" and "there is an element" both mean "\( a \)". It will reappear as a test case: a sentence true here and false in some other structure cannot be derivable (by the soundness statement at the end of this section), and some of the chapter's non-derivable sequents need at least two elements to refute.
- *Two elements, one relation.* \( D = \{ a, b \} \), with \( R^{\fM} = \{ (a, a), (b, b) \} \): the relation "is the same as", written out as a set of pairs. A finite structure can be given completely by listing.
- *The integers with their order.* \( D = \nZ \), with \( R^{\fM} = \{ (x, y) \in \nZ^2 : x > y \} \). Here the relation is described by a condition rather than a list.
- *Arithmetic.* \( D = \nR \), with the constants \( 0 \) and \( 1 \) naming zero and one, the function symbols \( + \), \( \cdot \) and two-place \( - \) meaning addition, multiplication and subtraction, the one-place symbols \( - \), \( (\cdot)^2 \) and \( \abs{\cdot} \) meaning negation, squaring and absolute value, and \( < \), \( \le \), \( > \), \( \ge \) the usual order. Extended by the other familiar symbols with their usual meanings (numerals, halving, the predicates \( \in A \), division with its value at a zero denominator fixed arbitrarily as in the non-example below, and a function symbol for each sequence or function an example uses), this is the structure in which the analysis examples of this chapter have been read all along.

*Non-example by minimal change.* Take the arithmetic structure and add a one-place function symbol \( g \), meant to be read as \( x \mapsto 1/x \). This is **not** a structure: (M3) asks for a function defined at every element of \( D \), and \( 1/0 \) is not defined. Everything else in the description is fine; exactly clause (M3) fails, at the single point \( 0 \). There are two repairs. Shrink the domain to \( (0, \infty) \), where \( 1/x \) is always defined; or keep \( \nR \) and give \( g \) any value at \( 0 \), say \( g^{\fM}(0) \coloneqq 0 \). The second repair is the one this chapter uses for terms such as \( 1/n \): the value at \( 0 \) is fixed arbitrarily and is never looked at, because such terms are used only under a bound \( n \in \nZ_{>0} \) (as in @exr-models-c3), exactly as a sequence \( a_n \) was read in Section 4.1 as a function symbol whose values off \( \nN \) are never used.

**Why this definition.** Each clause earns its place.

- *Non-empty.* This is a genuine choice, and it is made because of @prp-forall-implies-exists. A later subsection explains it.
- *Total functions.* Clause (M3) is what makes every term name an object: the term \( g(0) \) must have a value, or the formula \( g(0) = g(0) \), which \( \rulename{{=}I} \) derives from nothing, would have no truth value.
- *Identity for \( = \).* The rule \( \rulename{{=}E} \) replaces equals by equals **everywhere**. If a structure could read \( = \) as some other relation, \( \rulename{{=}E} \) would fail. On \( \nZ \), read \( x = y \) as "\( x \) and \( y \) have the same parity" and \( P \) as "is positive": then \( -2 = 2 \) and \( P(2) \) would both hold, while \( P(-2) \), which \( \rulename{{=}E} \) derives from them, fails. With \( = \) fixed as identity, no such reading exists.

::: {.warning}
A structure must interpret **every** symbol that occurs in the formulas at hand. "Take \( D = \nZ \)" is not yet a structure for \( \forall y\, \exists x\, R(x, y) \): until \( R \) is given a meaning, the sentence has no truth value, and the same domain makes it true with \( R \) read as \( > \) and false with \( R \) read as "\( x \cdot x = y \)" (at \( y = 2 \)). Always write the domain **and** the meaning of each symbol.
:::

## Assignments and the value of a term

A structure names the objects that **constants** stand for. Variables are different: their whole purpose is to range over the domain, so a structure gives them no fixed value. A separate object records what they stand for at a given moment.

::: {#def-assignment}
[Assignment]

Let \( \fM \) be a structure with domain \( D \). An **assignment** in \( \fM \) is a function \( \ell \) that gives **every** variable \( x \) a value \( \ell(x) \in D \). For an assignment \( \ell \), a variable \( x \) and an element \( d \in D \), the assignment \( \ell[x \mapsto d] \) is the one that gives \( x \) the value \( d \) and every other variable the value \( \ell \) gives it:
\[
\ell[x \mapsto d](y) \coloneqq
\begin{cases}
d & \text{if } y \text{ is the variable } x, \\
\ell(y) & \text{if } y \text{ is any other variable.}
\end{cases}
\]
:::

In words: an assignment is a choice of value for every variable at once, and \( \ell[x \mapsto d] \) changes that choice at the one variable \( x \), leaving the others alone. The assignment \( \ell[x \mapsto d] \) is what the quantifiers will use: "for every \( x \)" will mean "for every \( d \in D \), with \( x \) set to \( d \)". Changes can be stacked: \( \ell[x \mapsto d][y \mapsto e] \) first sets \( x \) to \( d \) and then \( y \) to \( e \). When \( x \) and \( y \) are different variables the order does not matter, since each change touches only its own variable; when they are the same variable, the later change wins.

There are always assignments, because \( D \) is non-empty: pick any \( d_0 \in D \) and let every variable have the value \( d_0 \). Like a valuation in Chapter 3 (@def-valuation), an assignment fixes infinitely many values, and a formula will only ever look at finitely many of them.

With a structure and an assignment, every term names an element of the domain. Terms are built by the clauses of @def-term, so the value is defined by recursion on terms, in the pattern of @thm-structural-recursion.

*The value of a term is computed from its variables and constants upwards, one function symbol at a time.*

For a structure \( \fM \) and an assignment \( \ell \), the **value** \( t^{\fM, \ell} \in D \) of a term \( t \) is:

- \( x^{\fM, \ell} \coloneqq \ell(x) \) for a variable \( x \);
- \( c^{\fM, \ell} \coloneqq c^{\fM} \) for a constant \( c \);
- \( f(t_1, \dots, t_n)^{\fM, \ell} \coloneqq f^{\fM}\bigl( t_1^{\fM, \ell}, \dots, t_n^{\fM, \ell} \bigr) \) for a function symbol \( f \) of arity \( n \).

The third clause is where (M3) is needed: \( f^{\fM} \) must accept every tuple the terms \( t_1, \dots, t_n \) might produce.

For example, in the arithmetic structure on \( \nR \), let \( \ell(x) = 2 \) and \( \ell(y) = -3 \). The term \( x \cdot x + y \), which is \( +(\cdot(x, x), y) \) written in the usual way, has value \( 2 \cdot 2 + (-3) = 1 \). Under \( \ell[y \mapsto 1] \) it has value \( 2 \cdot 2 + 1 = 5 \), and under \( \ell[x \mapsto 0] \) it has value \( -3 \). The term \( 1 + 1 \) has value \( 2 \) under every assignment, since it contains no variable.

## Satisfaction

Now the central definition. We want to say when a structure and an assignment make a formula true. Formulas are built by the clauses of @def-first-order-formula, so we define it by recursion, one clause per way of building a formula, and each clause reads its connective or quantifier as Chapter 3 and Section 4.1 read it.

*A formula is satisfied when the objects its terms name stand in the relations its predicates name, combined by the connectives as in a truth table, with "for every \( x \)" and "there is an \( x \)" ranging over the domain.*

::: {#def-satisfaction}
[Satisfaction]

Let \( \fM \) be a structure with domain \( D \) and \( \ell \) an assignment in \( \fM \). The relation \( \fM, \ell \models \varphi \), read "\( \fM \) **satisfies** \( \varphi \) under \( \ell \)", is defined by recursion on the formula \( \varphi \):

::: {.enumerate options="label=(S\arabic*)"}
1. \( \fM, \ell \models R(t_1, \dots, t_n) \) if \( \bigl( t_1^{\fM, \ell}, \dots, t_n^{\fM, \ell} \bigr) \in R^{\fM} \);
2. \( \fM, \ell \models t_1 = t_2 \) if \( t_1^{\fM, \ell} \) and \( t_2^{\fM, \ell} \) are the **same** element of \( D \);
3. \( \fM, \ell \models \bot \) **never** holds;
4. \( \fM, \ell \models \neg\varphi \) if \( \fM, \ell \models \varphi \) does not hold;
5. \( \fM, \ell \models \varphi \wedge \psi \) if both \( \fM, \ell \models \varphi \) **and** \( \fM, \ell \models \psi \); \( \fM, \ell \models \varphi \vee \psi \) if at least one of them holds; \( \fM, \ell \models \varphi \to \psi \) unless \( \fM, \ell \models \varphi \) holds and \( \fM, \ell \models \psi \) does not; \( \fM, \ell \models \varphi \leftrightarrow \psi \) if both hold or neither does;
6. \( \fM, \ell \models \forall x\, \varphi \) if \( \fM, \ell[x \mapsto d] \models \varphi \) **for every** \( d \in D \);
7. \( \fM, \ell \models \exists x\, \varphi \) if \( \fM, \ell[x \mapsto d] \models \varphi \) for **at least one** \( d \in D \).
:::

When \( \fM, \ell \models \varphi \) does not hold we write \( \fM, \ell \not\models \varphi \). For a list \( \Gamma \) of formulas, \( \fM, \ell \models \Gamma \) means that \( \fM, \ell \models \gamma \) for **every** formula \( \gamma \) of \( \Gamma \).
:::

Read it clause by clause. (S1): an atomic formula is satisfied exactly when the values of its terms form a tuple in the relation that interprets its predicate symbol. (S2): an equation is satisfied when both sides name the same object; this is where "\( = \) means identity" enters. (S3)–(S5) are the \( \bot \) half of (V1) and clauses (V2)–(V6) of Chapter 3's @def-truth-value, with "is true under \( v \)" replaced by "is satisfied by \( \fM \) under \( \ell \)": \( \bot \) is never satisfied, \( \neg \) flips, \( \wedge \) needs both, \( \vee \) needs one, \( \to \) fails only with a satisfied hypothesis and an unsatisfied conclusion, \( \leftrightarrow \) needs agreement. (S6) and (S7) are the new clauses. To decide \( \forall x\, \varphi \), we run through the elements \( d \) of the domain, set \( x \) to \( d \) and leave every other variable alone, and ask whether \( \varphi \) is satisfied each time. For \( \exists x\, \varphi \) one success is enough. In symbols, for (S6) and (S7):
\[
\begin{aligned}
\fM, \ell \models \forall x\, \varphi \quad &\text{iff} \quad \text{for every } d \in D, \ \ \fM, \ell[x \mapsto d] \models \varphi , \\
\fM, \ell \models \exists x\, \varphi \quad &\text{iff} \quad \text{there is } d \in D \text{ with } \fM, \ell[x \mapsto d] \models \varphi .
\end{aligned}
\]

**Well defined.** The clauses define, for each formula, which pairs \( (\fM, \ell) \) satisfy it, by recursion on the formula: (S1)–(S3) settle the atomic formulas and \( \bot \), and each of (S4)–(S7) settles a compound formula from its immediate parts. One point needs a word. Clauses (S6) and (S7) consult the immediate part \( \varphi \) under **other** assignments \( \ell[x \mapsto d] \), not under \( \ell \). So the recursion must define satisfaction of each formula under **all** assignments at once, and then (S6) reads off the answer for \( \varphi \) at every \( \ell[x \mapsto d] \). The recursion is still on the formula alone, and @thm-structural-recursion, applied to formulas built by the clauses of @def-first-order-formula, gives exactly one such relation.

**A trace, step by step.** Decide \( \forall x\, \exists y\, (x < y) \) in two structures, both with \( < \) the usual order: \( \fM_1 \) with domain \( \nN \), and \( \fM_2 \) with domain \( \{ 1, 2, 3 \} \). Let \( \ell \) be any assignment.

In \( \fM_1 \): by (S6) we must check, for every \( d \in \nN \), that \( \fM_1, \ell[x \mapsto d] \models \exists y\, (x < y) \). Fix \( d \). By (S7) it is enough to find one \( e \in \nN \) with \( \fM_1, \ell[x \mapsto d][y \mapsto e] \models x < y \). Take \( e = d + 1 \). Under \( \ell[x \mapsto d][y \mapsto d + 1] \) the terms \( x \) and \( y \) have the values \( d \) and \( d + 1 \), and \( d < d + 1 \), so (S1) holds. Hence the sentence is satisfied. Notice that the witness \( e = d + 1 \) depends on \( d \): (S7) is checked **inside** (S6), once for each \( d \).

In \( \fM_2 \): (S6) asks the same for \( d = 1, 2, 3 \). At \( d = 1 \) and \( d = 2 \) the witnesses \( e = 2 \) and \( e = 3 \) work. At \( d = 3 \) no \( e \in \{ 1, 2, 3 \} \) has \( 3 < e \), so (S7) fails for \( \ell[x \mapsto 3] \), and (S6) fails. So \( \fM_2 \not\models \forall x\, \exists y\, (x < y) \), and the failure has a name: the element \( 3 \) has nothing above it.

**The assignment matters for free variables.** In \( \fM_1 = (\nN, <) \), with \( \le \) also read as usual, take the formula \( \forall y\, (x \le y) \), in which \( x \) is free. Under an assignment with \( \ell(x) = 0 \) it is satisfied, since every \( e \in \nN \) has \( 0 \le e \) (recall that \( \nN = \{ 0, 1, 2, \dots \} \)). Under an assignment with \( \ell(x) = 1 \) it is not: \( e = 0 \) gives \( 1 \le 0 \), which fails. The same formula in the same structure is satisfied under one assignment and not under another; it is a property of \( x \), "\( x \) is least", not a statement.

**Degenerate cases.** In the one-element structure \( D = \{ a \} \), every assignment gives every variable the value \( a \), so \( \ell[x \mapsto a] = \ell \) and (S6) and (S7) both reduce to "\( \fM, \ell \models \varphi \)". So \( \forall x\, \varphi \) and \( \exists x\, \varphi \) are satisfied together or not at all, and every equation \( x = y \) is satisfied. In any structure, \( \forall x\, (x = x) \) is satisfied, since every \( d \) is the same element as itself; and \( \exists x\, \neg(x = x) \) never is.

::: {.check}
Is \( \forall x\, \exists y\, (y \cdot y = x) \) satisfied in \( \nR \), in \( [0, \infty) \), and in \( \nC \), each with \( \cdot \) the usual product?
:::

::: {.solution}
In \( \nR \), no: at \( d = -1 \), (S7) asks for a real \( e \) with \( e \cdot e = -1 \), and every real square is \( \ge 0 \). In \( [0, \infty) \), yes: for each \( d \ge 0 \), \( e = \sqrt{d} \) is in the domain and \( e \cdot e = d \); and \( [0, \infty) \) with \( \cdot \) is a structure, since a product of non-negative reals is non-negative (M3). In \( \nC \), yes: every complex number has a complex square root (school algebra of complex numbers: \( r(\cos\theta + i\sin\theta) \) with \( r \ge 0 \) has the square root \( \sqrt{r}\,(\cos\frac{\theta}{2} + i\sin\frac{\theta}{2}) \)). The sentence is the same all three times; only the structure changes.
:::

## Only the free variables matter

The example of \( \forall y\, (x \le y) \) above showed \( \ell \) mattering. In the first example it did not: the verdict on \( \forall x\, \exists y\, (x < y) \) was reached for "any assignment \( \ell \)". That is no accident. A sentence has no free variables (@def-sentence), and every variable it contains is bound, so every value \( \ell \) gives is overwritten by (S6) or (S7) before it is looked at. We prove the general fact, which is the first-order version of Chapter 3's @lem-coincidence: satisfaction depends only on the values of the **free** variables.

Say that two assignments \( \ell \) and \( \ell' \) **agree on** a set of variables if \( \ell(y) = \ell'(y) \) for every variable \( y \) in it. We need the free variables of a formula, recursively defined in @def-free-variable: every variable occurring in an atomic formula is free there; \( \neg\varphi \) has the free variables of \( \varphi \); \( \varphi \circ \psi \), for a binary connective \( \circ \), has those of \( \varphi \) and those of \( \psi \); and \( \forall x\, \varphi \) and \( \exists x\, \varphi \) have those of \( \varphi \) other than \( x \).

::: {#lem-free-coincidence}
[Free Variables Coincidence Lemma]

Let \( \fM \) be a structure and \( \varphi \) a formula, and let \( \ell \) and \( \ell' \) be assignments in \( \fM \) that agree on every free variable of \( \varphi \). Then
\[
\fM, \ell \models \varphi \quad \text{if and only if} \quad \fM, \ell' \models \varphi .
\]
:::

::: {.idea}
Structural induction on \( \varphi \), as for @lem-coincidence, after a first induction on terms: a term's value depends only on the values of its variables. The connective cases are Chapter 3's. The quantifier case is the only new one, and it explains why the property must be stated **for all** pairs of assignments: (S6) compares \( \ell[x \mapsto d] \) with \( \ell'[x \mapsto d] \), which are new assignments, so the induction hypothesis must apply to them. They agree at \( x \), since both give it \( d \), and at every other free variable of \( \varphi \), since those are free in \( \forall x\, \varphi \).
:::

::: {.proof}
*Terms first.* We show: if \( \ell \) and \( \ell' \) agree on every variable occurring in a term \( t \), then \( t^{\fM, \ell} = t^{\fM, \ell'} \). We use structural induction on terms (@def-term; the pattern of @thm-structural-induction). For a variable \( x \), the variable \( x \) occurs in \( x \), so \( x^{\fM, \ell} = \ell(x) = \ell'(x) = x^{\fM, \ell'} \). For a constant \( c \), both values are \( c^{\fM} \). For \( f(t_1, \dots, t_n) \), every variable of \( t_i \) occurs in \( f(t_1, \dots, t_n) \), so the hypothesis for \( t_i \) gives \( t_i^{\fM, \ell} = t_i^{\fM, \ell'} \) for each \( i \); applying \( f^{\fM} \) to equal tuples gives equal values.

*Formulas.* We apply structural induction to the property \( C(\varphi) \): *for all assignments \( \ell \), \( \ell' \) in \( \fM \) that agree on the free variables of \( \varphi \), \( \fM, \ell \models \varphi \) if and only if \( \fM, \ell' \models \varphi \).*

*Atomic formulas.* Let \( \varphi \) be \( R(t_1, \dots, t_n) \), and let \( \ell \), \( \ell' \) agree on its free variables. Every variable occurring in \( \varphi \) is free in it (@def-free-variable), so \( \ell \) and \( \ell' \) agree on the variables of each \( t_i \), and by the claim for terms \( t_i^{\fM, \ell} = t_i^{\fM, \ell'} \). The two tuples in (S1) are equal, so one lies in \( R^{\fM} \) exactly when the other does. The case \( t_1 = t_2 \) is the same with (S2). For \( \bot \), neither side holds, by (S3).

*Connectives.* Assume \( C(\varphi) \) and \( C(\psi) \), and let \( \ell \), \( \ell' \) agree on the free variables of \( \varphi \wedge \psi \). These include the free variables of \( \varphi \) and those of \( \psi \), so \( \fM, \ell \models \varphi \) if and only if \( \fM, \ell' \models \varphi \), and likewise for \( \psi \). By (S5), satisfaction of \( \varphi \wedge \psi \) is decided by these two answers through the same rule for \( \ell \) and for \( \ell' \), so \( C(\varphi \wedge \psi) \) holds. The cases \( \neg\varphi \), \( \varphi \vee \psi \), \( \varphi \to \psi \), and \( \varphi \leftrightarrow \psi \) are the same argument with (S4) and the other parts of (S5), as in the proof of @lem-coincidence.

*Universal quantifier.* Assume \( C(\varphi) \), let \( x \) be a variable, and let \( \ell \), \( \ell' \) agree on the free variables of \( \forall x\, \varphi \). Let \( d \in D \). We claim that \( \ell[x \mapsto d] \) and \( \ell'[x \mapsto d] \) agree on the free variables of \( \varphi \). At \( x \), both give \( d \). A free variable \( y \) of \( \varphi \) other than \( x \) is a free variable of \( \forall x\, \varphi \) (@def-free-variable), so \( \ell[x \mapsto d](y) = \ell(y) = \ell'(y) = \ell'[x \mapsto d](y) \). By \( C(\varphi) \), applied to these two assignments,
\[
\fM, \ell[x \mapsto d] \models \varphi \quad \text{iff} \quad \fM, \ell'[x \mapsto d] \models \varphi .
\]
This holds for every \( d \in D \), so by (S6) \( \fM, \ell \models \forall x\, \varphi \) if and only if \( \fM, \ell' \models \forall x\, \varphi \). This proves \( C(\forall x\, \varphi) \).

*Existential quantifier.* The same argument, with (S7) in place of (S6): the displayed equivalence holds for each \( d \), so there is a \( d \) making the left side hold exactly when there is one making the right side hold.

Every clause of @def-first-order-formula has been covered, so \( C(\varphi) \) holds for every formula \( \varphi \). This proves the lemma.
:::

The lemma has a consequence that the rest of the section uses constantly.

*Sentences.* If \( \varphi \) is a sentence, it has no free variables, so **any** two assignments agree on its free variables, and the lemma says that \( \fM, \ell \models \varphi \) either holds for every assignment \( \ell \) or for none. We then write \( \fM \models \varphi \), and say that \( \varphi \) is **true in** \( \fM \) (or that \( \fM \) is a model of \( \varphi \)), in the first case, and \( \fM \not\models \varphi \), \( \varphi \) is **false in** \( \fM \), in the second. At least one assignment exists because \( D \) is non-empty, so a sentence is always exactly one of true and false in \( \fM \). This is the precise form of Section 4.1's informal "true over a domain".

*Only finitely many values matter.* A formula has finitely many free variables. To decide \( \fM, \ell \models \varphi \), it is enough to know \( \ell \) on those. So we describe an assignment by the values that matter ("\( \ell(x) = 2 \)"), exactly as Chapter 3 described a valuation by the values of a few atoms.

::: {.warning}
The same sentence can be true in one structure and false in another, and "true" without a structure means nothing. \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \) and false in \( (\{ 1, 2, 3 \}, <) \), as traced above. A sentence of predicate logic is like a formula of Chapter 3 with atoms: it has a truth value only once the meaning of its symbols has been fixed.
:::

## Semantic entailment

Chapter 3 said that \( \Gamma \) entails \( \psi \) when every row that makes \( \Gamma \) true makes \( \psi \) true (@def-valid-argument). The row is now a structure with an assignment.

*An argument is valid when every structure, under every assignment, that satisfies all the premises also satisfies the conclusion.*

::: {#def-first-order-entailment}
[Semantic Entailment in Predicate Logic]

Let \( \Gamma \) be a list of formulas and \( \varphi \) a formula. We say \( \Gamma \) **semantically entails** \( \varphi \), and write \( \Gamma \models \varphi \), if for **every** structure \( \fM \) for the symbols occurring in \( \Gamma \) and \( \varphi \), and **every** assignment \( \ell \) in \( \fM \),
\[
\fM, \ell \models \Gamma \quad \Rightarrow \quad \fM, \ell \models \varphi .
\]
We write \( \models \varphi \) when \( \Gamma \) is empty. If \( \Gamma \models \varphi \) fails, we write \( \Gamma \not\models \varphi \); a structure \( \fM \) with an assignment \( \ell \) such that \( \fM, \ell \models \Gamma \) and \( \fM, \ell \not\models \varphi \) is a **counter-model** to \( \Gamma \models \varphi \).
:::

In words: "every structure" means every domain and every meaning of the symbols, so an entailment holds for reasons of form and not because of what \( R \) happens to mean. "Every assignment" covers every value of the free variables; when \( \Gamma \) and \( \varphi \) are sentences, the assignment makes no difference, by @lem-free-coincidence. And a counter-model is the analogue of Chapter 3's refuting row: one structure, with one assignment, where the premises hold and the conclusion does not. The symbol \( \models \) is the one of Chapter 3, and the context always shows which is meant: a sequent of formulas with quantifiers or predicate symbols is read with this definition.

A structure may interpret symbols that do not occur in \( \Gamma \) or \( \varphi \). The clauses of @def-satisfaction consult only the symbols of the formula at hand, so such extra meanings change nothing.

*First examples of entailment.* The argument Section 4.1 opened with, "every positive real has a square root; 2 is positive; so 2 has a square root", is \( \forall x\, (P(x) \to Q(x)), \ P(c) \vdash Q(c) \), derived in Section 4.3. Truth tables called it invalid, since they saw three unrelated atoms. It is valid in the new sense:
\[
\forall x\, (P(x) \to Q(x)), \ P(c) \models Q(c) .
\]
Let \( \fM, \ell \) satisfy both premises, and let \( a = c^{\fM} \). By (S6) for the first premise, with \( d = a \), we get \( \fM, \ell[x \mapsto a] \models P(x) \to Q(x) \). Under \( \ell[x \mapsto a] \) the term \( x \) has value \( a \), and under \( \ell \) the term \( c \) has value \( a \); so by (S1), \( \fM, \ell[x \mapsto a] \models P(x) \) holds if and only if \( a \in P^{\fM} \) if and only if \( \fM, \ell \models P(c) \), which is the second premise. So by (S5) \( \fM, \ell[x \mapsto a] \models Q(x) \), that is, \( a \in Q^{\fM} \), and by (S1) again \( \fM, \ell \models Q(c) \). Chapter 3's objection to this argument is gone.

## Why domains are non-empty {#why-domains-are-non-empty}

Clause (M1) of @def-structure demands a non-empty domain. Here is the reason. @prp-forall-implies-exists derives \( \forall x\, P(x) \vdash \exists x\, P(x) \) in three lines: \( \rulename{\forall E} \) at the variable \( x \), then \( \rulename{\exists I} \). The matching entailment holds for our structures:
\[
\forall x\, P(x) \models \exists x\, P(x) .
\]
Let \( \fM, \ell \models \forall x\, P(x) \). Since \( D \) is non-empty, choose some \( d \in D \). By (S6), \( \fM, \ell[x \mapsto d] \models P(x) \), and this \( d \) is the one element (S7) asks for, so \( \fM, \ell \models \exists x\, P(x) \).

Now suppose empty domains were allowed. In a structure with \( D = \emptyset \), (S6) says \( \forall x\, P(x) \) is satisfied, since "for every \( d \in \emptyset \)" has nothing to check; and (S7) says \( \exists x\, P(x) \) is not, since there is no \( d \) at all. So the sequent would be derivable and yet fail in a structure, and the rules would lead from a true premise to a false conclusion. (Worse, no assignment into an empty domain exists, so even the clauses could not be applied as written.) One of two things had to give: the rule \( \rulename{\forall E} \) at a variable, or empty domains. The book, like most of mathematics, keeps the rules and makes domains non-empty.

Nothing is lost. Statements about an empty **set** are handled by the bounded quantifiers of @def-bounded-quantifier, inside a non-empty domain. The bounded forms \( \forall x \in \emptyset\ \varphi \) and \( \exists x \in \emptyset\ \varphi \) abbreviate \( \forall x\, (x \in \emptyset \to \varphi) \) and \( \exists x\, (x \in \emptyset \wedge \varphi) \), and in a structure with domain \( \nR \) in which the one-place predicate symbol \( \in \emptyset \) (Section 4.2) is interpreted, by (M4), as the empty subset of \( \nR \), the first is true (every hypothesis \( d \in \emptyset \) is false) and the second is false (no \( d \) is in \( \emptyset \)). Vacuous truth lives in the bound, not in the domain.

## Counter-models

A counter-model is found the way a refuting row was found in Chapter 3, by working backwards from what must fail. The conclusion must be false, so read off what that demands; the premises must be true, so read off what they demand; and then build the smallest structure meeting both. The worked examples that follow (the swap, the converses of @prp-exists-and and of the \( \forall \)/\( \vee \) law, \( \exists x\, P(x) \vdash P(c) \), and \( P(x_0) \vdash \forall x\, P(x) \)) are sequents whose derivations stalled or were blocked in earlier sections.

::: {#exm-counter-model-swap}
[The swap of \( \exists \) and \( \forall \)]

Show that
\[
\forall y\, \exists x\, R(x, y) \not\models \exists x\, \forall y\, R(x, y) ,
\]
first by a structure on \( \nZ \), then by a structure with two elements.
:::

::: {.solution}
Both formulas are sentences, so by @lem-free-coincidence we need only a structure; any assignment will do.

*A structure on \( \nZ \).* Let \( \fM \) have domain \( \nZ \) and \( R^{\fM} = \{ (x, y) : x > y \} \), so that \( R(x, y) \) says "\( x > y \)". The premise says "every integer has an integer above it". To check it by (S6) and (S7): for each \( e \in \nZ \) we need some \( d \in \nZ \) with \( (d, e) \in R^{\fM} \), that is, \( d > e \); \( d = e + 1 \) works. The conclusion says "some integer is above every integer". By (S7) and (S6) it would need a \( d \in \nZ \) with \( d > e \) for **every** \( e \in \nZ \); but \( e = d \) gives \( d > d \), which is false. So \( \fM \models \forall y\, \exists x\, R(x, y) \) and \( \fM \not\models \exists x\, \forall y\, R(x, y) \).

*A structure with two elements.* Let \( D = \{ a, b \} \) and \( R^{\fM} = \{ (a, a), (b, b) \} \), so that \( R(x, y) \) says "\( x \) is \( y \)". Premise: for \( e = a \) take \( d = a \), and for \( e = b \) take \( d = b \); both pairs are in \( R^{\fM} \). Conclusion: \( d = a \) fails at \( e = b \), since \( (a, b) \notin R^{\fM} \), and \( d = b \) fails at \( e = a \). So the premise is true and the conclusion false.

The pattern is the one Section 4.1 read as a game. In the premise the witness \( x \) is chosen **after** \( y \) and may depend on it (\( x = y + 1 \), or \( x = y \)); the conclusion asks for one \( x \) that works for every \( y \) in advance. A one-element structure cannot separate the two sentences: with \( D = \{ a \} \), both are true if \( (a, a) \in R^{\fM} \) and both false otherwise. Two elements are the least that will do.
:::

The two-element structure is the \( \nZ \) structure's idea at its smallest: each element is related to something, and nothing is related to everything. Finite counter-models are convenient because every clause can be checked by listing. They are not always available: Exercise C1 below gives a sentence that is true in every finite structure and false in an infinite one, and Exercise C2 a sentence with only infinite models.

**The converse of @prp-exists-and.** Section 4.6 derived \( \exists x\, (P(x) \wedge Q(x)) \vdash \exists x\, P(x) \wedge \exists x\, Q(x) \) and asked about the converse. We show
\[
\exists x\, P(x) \wedge \exists x\, Q(x) \not\models \exists x\, (P(x) \wedge Q(x)) .
\]
Backwards from the conclusion: it is false when no element is in both \( P^{\fM} \) and \( Q^{\fM} \). The premise needs \( P^{\fM} \) and \( Q^{\fM} \) non-empty. So take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \). The premise holds by (S5) and (S7), with witnesses \( a \) for \( P \) and \( b \) for \( Q \). The conclusion fails: at \( d = a \), \( a \notin Q^{\fM} \); at \( d = b \), \( b \notin P^{\fM} \). In arithmetic: in \( \nZ \), some integer is even and some integer is odd, but no integer is both. The two witnesses of the premise are different objects, and the conclusion needs one.

**The converse of the \( \forall \)/\( \vee \) law.** The one-way law \( \forall x\, P(x) \vee \forall x\, Q(x) \vdash \forall x\, (P(x) \vee Q(x)) \) of @prp-quantifier-distribution has a false converse, and the same structure shows it:
\[
\forall x\, (P(x) \vee Q(x)) \not\models \forall x\, P(x) \vee \forall x\, Q(x) .
\]
With \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \): each element is in \( P^{\fM} \) or in \( Q^{\fM} \), so the premise holds; \( \forall x\, P(x) \) fails at \( b \) and \( \forall x\, Q(x) \) fails at \( a \), so by (S5) the disjunction fails. In \( \nZ \): every integer is even or odd, but it is false that every integer is even, and false that every integer is odd.

**A witness is not a named constant.** @exr-existential-introduction-c2 asked why \( \exists x\, P(x) \vdash P(c) \) cannot be derived. Take \( D = \{ a, b \} \), \( c^{\fM} = a \) and \( P^{\fM} = \{ b \} \). The premise holds with the witness \( b \); the conclusion \( P(c) \) fails, since the value of \( c \) is \( a \notin P^{\fM} \). So \( \exists x\, P(x) \not\models P(c) \). The premise says that something has \( P \), and nothing says that the object named \( c \) is that something.

**The assignment is part of a counter-model.** Section 4.4 showed why \( \rulename{\forall I} \) may not generalize over a name in a premise: from \( P(x_0) \) one would "derive" \( \forall x\, P(x) \). Here \( x_0 \) is a **variable**, free in the premise, so a counter-model needs an assignment as well as a structure. Let \( \fM \) have domain \( \nZ \) with \( P^{\fM} \) the set of even integers, and let \( \ell(x_0) = 2 \). Then \( \fM, \ell \models P(x_0) \), since \( 2 \) is even, and \( \fM, \ell \not\models \forall x\, P(x) \), since (S6) fails at \( d = 1 \). So \( P(x_0) \not\models \forall x\, P(x) \). Under the assignment with \( \ell(x_0) = 1 \) the premise is false, and that assignment refutes nothing; the counter-model is the structure **with** \( \ell(x_0) = 2 \).

::: {.warning}
A "counter-model" that falsifies a premise refutes nothing. For \( \forall y\, \exists x\, R(x, y) \vdash \exists x\, \forall y\, R(x, y) \), the structure \( (\nN, <) \), with \( R(x, y) \) read as "\( x < y \)", makes the conclusion false, since no natural number is below every natural number; but it also makes the premise false, since nothing in \( \nN \) is below \( y = 0 \). It is not a counter-model, and it proves nothing about the sequent. As with rows in Chapter 3, check the premises **first**.
:::

**A model of a list of sentences.** Counter-models are one use of structures; describing a whole kind of object is another. Consider the three sentences
\[
\begin{aligned}
&\forall x\, \neg(x < x), \\
&\forall x\, \forall y\, \forall z\, \bigl( (x < y \wedge y < z) \to x < z \bigr), \\
&\forall x\, \exists y\, (x < y),
\end{aligned}
\]
which say that \( < \) is a **strict order** (never \( x < x \); \( x < y \) and \( y < z \) give \( x < z \)) **with no largest element**. The structure \( (\nN, <) \) is a model of all three: no number is less than itself, the order is transitive, and \( d + 1 > d \) is a witness for the third sentence. It is the one the sentences were written with in mind, but not the only one: in \( (\nZ, <) \) and \( (\nQ, <) \) all three are true, by the same checks. These models differ in ways the three sentences cannot see: \( \nZ \) has no least element, and \( \nQ \) has a third element between any two. And the one-element structure \( D = \{ a \} \) is not a model of the three sentences: if \( (a, a) \in <^{\fM} \) the first sentence fails, and if not, the third fails at \( d = a \). Exercise C2 shows that no **finite** structure is a model of them.

::: {.check}
Give a counter-model to \( \forall x\, P(x) \to \forall x\, Q(x) \models \forall x\, (P(x) \to Q(x)) \). (Think about what makes an implication with a universal hypothesis true cheaply.)
:::

::: {.solution}
Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \emptyset \). The premise is an implication whose hypothesis \( \forall x\, P(x) \) is false (it fails at \( b \)), so by (S5) the premise is true. The conclusion fails at \( d = a \): \( a \in P^{\fM} \) and \( a \notin Q^{\fM} \), so \( P(x) \to Q(x) \) is not satisfied under \( \ell[x \mapsto a] \). (Any structure with \( P^{\fM} \ne D \) and some element in \( P^{\fM} \) but not in \( Q^{\fM} \) works.)
:::

## From counter-models to non-derivability {#from-counter-models-to-non-derivability}

A counter-model shows \( \Gamma \not\models \varphi \). The stalled searches asked something else: whether \( \Gamma \vdash \varphi \). The bridge is the same as in Chapter 3, where @thm-soundness turned a refuting row into a proof that no derivation exists (@cor-refuting-row). For predicate logic it reads:

*Soundness for predicate logic.* If \( \Gamma \vdash \varphi \) with the rules of Chapters 1 and 2 and the quantifier and equality rules of Sections 4.3 to 4.7, then \( \Gamma \models \varphi \) in the sense of @def-first-order-entailment. Consequently, a counter-model to \( \Gamma \models \varphi \) shows \( \Gamma \nvdash \varphi \).

This statement is **not proved in this section**. Its proof extends Chapter 3's to the new rules, and it is the subject of Section 4.12, which is optional. The proof is where each side condition of the quantifier rules is used: the fresh-name conditions of \( \rulename{\forall I} \) and \( \rulename{\exists E} \), and "free for" in \( \rulename{\forall E} \), \( \rulename{\exists I} \), and \( \rulename{{=}E} \). A reader who skips Section 4.12 may take the statement on trust, as the rest of the book does; a reader who reads it will see why the side conditions are exactly as strict as they are.

With the statement, the examples above become non-derivability results. \( \forall y\, \exists x\, R(x, y) \nvdash \exists x\, \forall y\, R(x, y) \): the converse search of @prp-exists-forall-swap had to stall, and the two lines where it stalled, the blocked \( \rulename{\forall I} \) and the blocked close of the \( \rulename{\exists E} \) box, are not a lack of cleverness. Likewise the converse of @prp-exists-and, the converse of the \( \forall \)/\( \vee \) law, \( \exists x\, P(x) \vdash P(c) \), and \( P(x_0) \vdash \forall x\, P(x) \) have no derivations. And the same reasoning is the semantic side of Section 4.10: there, @exm-square-not-uniform showed that \( x^2 \) on \( \nR \) is continuous and not uniformly continuous, so the arithmetic structure on \( \nR \), with \( f \) read as squaring, is a counter-model to "continuous entails uniformly continuous".

::: {.warning}
A counter-model proves **non**-derivability; it never proves derivability, and a structure in which a sentence is true says nothing about whether the sentence is derivable. \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \), yet it is not derivable: it is false in \( (\{ 1, 2, 3 \}, <) \). To show \( \Gamma \vdash \varphi \), write a derivation.
:::

## Exercises

### A. Check your understanding

::: {#exr-models-a1}
[A1]

Let \( \fM_{\nN} \), \( \fM_{\nZ} \), \( \fM_{\nQ} \) be the structures with domains \( \nN \), \( \nZ \), \( \nQ \), each with \( < \) the usual order. For each sentence in (a)–(d), say in which of the three structures it is true, with a witness or a failing element for each verdict.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, \exists y\, (x < y) \).
2. \( \exists x\, \forall y\, \neg(y < x) \).
3. \( \forall x\, \forall y\, \bigl( x < y \to \exists z\, (x < z \wedge z < y) \bigr) \).
4. \( \forall x\, \exists y\, (y < x) \).
5. True or false: if a sentence is true in some structure, then it is derivable.
6. Why must the domain of a structure be non-empty? Name the derivable sequent that would otherwise fail.
:::
:::

::: {.solution}
*(a)* True in all three: for each \( d \), take \( y = d + 1 \), which lies in the same domain and is larger.

*(b)* This says "there is a least element". True in \( \fM_{\nN} \), with \( x = 0 \): no natural number is below \( 0 \). False in \( \fM_{\nZ} \) and \( \fM_{\nQ} \): for any \( d \), the element \( e = d - 1 \) has \( e < d \), so (S6) fails for \( \neg(y < x) \) under \( \ell[x \mapsto d] \).

*(c)* This says "between any two elements there is a third" (density). False in \( \fM_{\nN} \) and \( \fM_{\nZ} \): at \( x = 1 \), \( y = 2 \) there is no integer strictly between. True in \( \fM_{\nQ} \): for \( d < e \) in \( \nQ \), \( z = (d + e)/2 \) is rational and \( d < z < e \).

*(d)* This says "no element is least". False in \( \fM_{\nN} \), at \( x = 0 \). True in \( \fM_{\nZ} \) and \( \fM_{\nQ} \), with \( y = d - 1 \).

| | \( \nN \) | \( \nZ \) | \( \nQ \) |
|---|---|---|---|
| (a) | true | true | true |
| (b) | true | false | false |
| (c) | false | false | true |
| (d) | false | true | true |

*(e)* False. By the soundness statement, a derivable sentence is true in **every** structure. Sentence (a) is true in \( \fM_{\nN} \) but false in the structure \( (\{ 1, 2, 3 \}, <) \), so it is not derivable.

*(f)* The sequent is \( \forall x\, P(x) \vdash \exists x\, P(x) \), derived in @prp-forall-implies-exists by \( \rulename{\forall E} \) at the variable \( x \) and \( \rulename{\exists I} \). In an empty domain \( \forall x\, P(x) \) would be true, with nothing to check, and \( \exists x\, P(x) \) false, with no witness; so the rules would lead from a true premise to a false conclusion. (There would also be no assignments at all.)
:::

### B. Practice

::: {#exr-models-b1}
[B1: Three counter-models]

Give a counter-model for each of the following, and check each premise and the conclusion against @def-satisfaction.

::: {.enumerate options="label=(\roman*)"}
1. \( \exists x\, P(x) \not\models \forall x\, P(x) \).
2. \( \forall x\, (P(x) \to Q(x)) \not\models \exists x\, P(x) \to \forall x\, Q(x) \).
3. \( \not\models \exists x\, P(x) \to P(x) \). (Here \( x \) is free in the last \( P(x) \); the assignment is part of the answer.)
:::
:::

::: {.solution}
*(i)* Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \). The premise holds by (S7) with \( d = a \). The conclusion fails by (S6) at \( d = b \), since \( b \notin P^{\fM} \).

*(ii)* Take \( D = \{ a, b \} \), \( P^{\fM} = Q^{\fM} = \{ a \} \). Premise: at \( d = a \), \( P(x) \) and \( Q(x) \) are both satisfied, so \( P(x) \to Q(x) \) is; at \( d = b \), \( P(x) \) is not satisfied, so \( P(x) \to Q(x) \) is, by (S5). Hence the premise holds by (S6). Conclusion: \( \exists x\, P(x) \) holds (\( d = a \)) and \( \forall x\, Q(x) \) fails (at \( d = b \)), so by (S5) the implication fails. In words: whatever has \( P \) has \( Q \), and something has \( P \); that does not make everything have \( Q \).

*(iii)* Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), and an assignment with \( \ell(x) = b \). The hypothesis \( \exists x\, P(x) \) holds by (S7) with \( d = a \); its \( x \) is bound, and the value \( \ell(x) \) is overwritten. The conclusion \( P(x) \) has \( x \) free, with value \( \ell(x) = b \notin P^{\fM} \), so it fails. By (S5) the implication fails under \( \ell \). Under an assignment with \( \ell(x) = a \) the implication holds; so the formula is satisfied under some assignments and not others, and a counter-model must name \( \ell \). Now take \( \varphi \) and \( \psi \) both to be \( P(x) \). The formula \( \forall x\, (P(x) \to P(x)) \) is satisfied in every structure under every assignment, since \( P(x) \to P(x) \) is satisfied at every \( d \) by (S5) and (S6). So this structure, with \( \ell \), is a counter-model to \( \forall x\, (P(x) \to P(x)) \models \exists x\, P(x) \to P(x) \), and by the soundness statement of this section that sequent is not derivable. This is why the passage law \( \forall x\, (\varphi \to \psi) \dashv\vdash \exists x\, \varphi \to \psi \) of @prp-quantifier-passage needs \( x \) not free in \( \psi \).
:::

::: {#exr-models-b2}
[B2: A model on three elements]

Give an example of a structure with exactly three elements in which both
\[
\forall x\, \exists y\, R(x, y) \qquad \text{and} \qquad \forall x\, \neg R(x, x)
\]
are true. Check both sentences. Which properties must every such structure have?
:::

::: {.solution}
Take \( D = \{ 0, 1, 2 \} \) and \( R^{\fM} = \{ (0, 1), (1, 2), (2, 0) \} \): each element is related to the next one around a circle. First sentence: for \( d = 0, 1, 2 \), the witnesses \( e = 1, 2, 0 \) give pairs in \( R^{\fM} \). Second sentence: none of \( (0, 0) \), \( (1, 1) \), \( (2, 2) \) is in \( R^{\fM} \), so \( \neg R(x, x) \) is satisfied under \( \ell[x \mapsto d] \) for each \( d \).

The properties every answer must have: the domain has three elements; every element \( d \) has **some** \( e \) with \( (d, e) \in R^{\fM} \); and **no** pair \( (d, d) \) is in \( R^{\fM} \), so that \( e \) is always different from \( d \). Any \( R^{\fM} \) meeting these works, for instance \( \{ (0, 1), (1, 0), (2, 0) \} \) or the set of all pairs \( (d, e) \) with \( d \ne e \).
:::

::: {#exr-models-b3}
[B3: The converse from Section 4.4]

@exr-universal-introduction-b2 derived \( \forall x\, (P(x) \to Q(x)) \vdash \forall x\, \neg Q(x) \to \forall x\, \neg P(x) \), and its search for the converse stalled. Show
\[
\forall x\, \neg Q(x) \to \forall x\, \neg P(x) \not\models \forall x\, (P(x) \to Q(x)) .
\]
:::

::: {.solution}
Work backwards. The conclusion fails when some \( d \) has \( d \in P^{\fM} \) and \( d \notin Q^{\fM} \). The premise is cheapest to make true through a false hypothesis: make \( \forall x\, \neg Q(x) \) false by putting some element in \( Q^{\fM} \). Take \( D = \{ a, b \} \), \( P^{\fM} = \{ a \} \), \( Q^{\fM} = \{ b \} \).

Premise: \( \forall x\, \neg Q(x) \) fails at \( d = b \), since \( b \in Q^{\fM} \); so the implication holds by (S5). Conclusion: at \( d = a \), \( a \in P^{\fM} \) and \( a \notin Q^{\fM} \), so \( P(x) \to Q(x) \) fails under \( \ell[x \mapsto a] \), and (S6) fails. By the soundness statement of this section, the converse is not derivable, and the stalled search could not have succeeded.
:::

### C. Going deeper

::: {#exr-models-c1}
[C1: True in every finite model]

Let \( f \) be a one-place function symbol, and let \( \sigma \) be the sentence
\[
\forall x\, \forall y\, \bigl( f(x) = f(y) \to x = y \bigr) \to \forall y\, \exists x\, \bigl( f(x) = y \bigr) ,
\]
"if \( f \) is injective, then \( f \) is surjective".

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \sigma \) is true in every structure whose domain is finite.
2. Give a structure with an infinite domain in which \( \sigma \) is false.
3. Deduce that \( \sigma \) is not derivable, although no finite structure is a counter-model.
:::
:::

::: {.solution}
[Hint 1]

For (a), suppose \( f^{\fM} \) is injective on a finite \( D \) with \( n \) elements, and count the elements of its image.
:::

::: {.solution}
[Hint 2]

For (b), look for an operation on \( \nN \) that never repeats a value but misses a value.
:::

::: {.solution}
*(a)* Let \( \fM \) have a finite domain \( D \) with \( n \ge 1 \) elements. If the hypothesis of \( \sigma \) is false in \( \fM \), then \( \sigma \) is true by (S5). So suppose it is true: by (S6), (S5) and (S2), for all \( d, e \in D \), \( f^{\fM}(d) = f^{\fM}(e) \) implies \( d = e \); that is, \( f^{\fM} \) takes different values at different elements. Then the \( n \) elements of \( D \) have \( n \) different values, so the set of values \( \{ f^{\fM}(d) : d \in D \} \) is a subset of \( D \) with \( n \) elements. A subset of an \( n \)-element set with \( n \) elements is the whole set (a counting fact from school, proved in Chapter 8). So every \( e \in D \) is \( f^{\fM}(d) \) for some \( d \), which is the conclusion of \( \sigma \) by (S6), (S7) and (S2). Hence \( \sigma \) is true in \( \fM \).

*(b)* Take \( D = \nN \) and \( f^{\fM}(d) = d + 1 \). The hypothesis holds: \( d + 1 = e + 1 \) gives \( d = e \). The conclusion fails at \( y = 0 \): there is no \( d \in \nN \) with \( d + 1 = 0 \), since \( d \ge 0 \) gives \( d + 1 \ge 1 \). So \( \sigma \) is false in \( \fM \).

*(c)* The structure of (b) is a counter-model to \( \models \sigma \) (with \( \Gamma \) empty). By the soundness statement of this section, \( \sigma \) is not derivable. By (a), no finite structure could have shown this: a search for counter-models that lists finite structures of size 1, 2, 3, … would never stop.

**Marking scheme.** (10 points)

- 1: (a) disposes of the case where the hypothesis of \( \sigma \) is false, by the clause for \( \to \).
- 3: (a) reads the hypothesis as injectivity of \( f^{\fM} \) and uses finiteness to get surjectivity, naming the counting fact.
- 3: (b) a structure with infinite domain, with the hypothesis checked and the conclusion refuted at a named element.
- 3: (c) concludes non-derivability through soundness and says why finite structures could not have done it.

Fatal errors (0 for the step): in (b), a "counter-model" in which \( f^{\fM} \) is not injective; in (a), an argument that never uses finiteness.
:::

::: {#exr-models-c2}
[C2: A sentence with no finite model]

Let \( \tau \) be the conjunction of the three sentences of the text saying that \( < \) is a strict order with no largest element:
\[
\forall x\, \neg(x < x) \ \wedge \ \forall x\, \forall y\, \forall z\, \bigl( (x < y \wedge y < z) \to x < z \bigr) \ \wedge \ \forall x\, \exists y\, (x < y) .
\]
Prove that every model of \( \tau \) has an infinite domain. Where does your proof use that domains are non-empty?
:::

::: {.solution}
[Hint 1]

Start from one element and keep climbing with the third conjunct.
:::

::: {.solution}
[Hint 2]

Prove by induction on \( k \) that there are elements \( d_1 < d_2 < \dots < d_k \) of \( D \) with \( d_i < d_j \) whenever \( i < j \).
:::

::: {.solution}
Let \( \fM \) be a model of \( \tau \), with domain \( D \), and write \( d < e \) for \( (d, e) \in <^{\fM} \). We prove, for every \( k \ge 1 \), the statement \( A(k) \): *there are elements \( d_1, \dots, d_k \) of \( D \) with \( d_i < d_j \) whenever \( 1 \le i < j \le k \).* We use @ax-induction, applied to the property \( A(m + 1) \) of \( m \in \nN \), so that the base case is \( A(1) \).

*Base.* \( D \) is non-empty (@def-structure, (M1)), so there is some \( d_1 \in D \), and \( A(1) \) holds, with no pairs \( i < j \) to check. This is the one place the proof uses non-emptiness. If an empty domain were allowed, with "for every \( d \in \emptyset \)" read as having nothing to check, all three conjuncts would hold in it (each begins with \( \forall \)), and it has no elements at all: the statement "every model is infinite" would fail.

*Step.* Suppose \( d_1, \dots, d_k \) are as in \( A(k) \). By the third conjunct and (S6), (S7), there is \( d_{k+1} \in D \) with \( d_k < d_{k+1} \). For \( i < k \), we have \( d_i < d_k \) by \( A(k) \), and then \( d_i < d_{k+1} \) by the second conjunct (transitivity). So \( A(k + 1) \) holds.

Now the elements \( d_1, \dots, d_k \) are all different: if \( d_i = d_j \) with \( i < j \), then \( d_i < d_j \) says \( d_i < d_i \), which the first conjunct forbids. So for every \( k \ge 1 \), the domain contains \( k \) different elements. A finite set with \( n \) elements does not contain \( n + 1 \) different elements, so \( D \) is not finite. Since \( (\nN, <) \) is a model of \( \tau \) (as the text checked), \( \tau \) has models, and all of them are infinite.

**Marking scheme.** (10 points)

- 2: names the non-empty domain as the start of the construction, and says what fails without it.
- 3: an induction producing, for every \( k \), a chain of \( k \) elements, using the third conjunct for the step.
- 2: uses transitivity to keep the whole chain increasing, not only neighbors.
- 3: uses irreflexivity to show the elements are different, and concludes that \( D \) is infinite.

A second route: a proof that every non-empty finite subset of \( D \) has a \( < \)-maximal element (induction on its size, with irreflexivity in the base and transitivity in the step), applied to \( D \), which is non-empty, and contradicted by the third conjunct, earns 2 for using \( D \) non-empty, 3 for the induction, 2 for transitivity in the step, and 3 for irreflexivity plus the contradiction with the third conjunct.

Fatal errors (0 for the step): building the chain without showing its elements are distinct; an "infinite chain" asserted without an induction or a recursion.
:::

::: {#exr-models-c3}
[C3: Exit check: formalize, negate, decide]

Work over the domain \( \nR \), with \( n \in \nZ_{>0} \) as a bound as in Section 4.1, and \( 1/n \) as a term.

::: {.enumerate options="label=(\alph*)"}
1. Formalize, with bounded quantifiers: "for every \( \varepsilon > 0 \) there is \( N \in \nZ_{>0} \) such that \( 1/n < \varepsilon \) for every \( n \in \nZ_{>0} \) with \( n \ge N \)."
2. Formalize the sentence obtained from (a) by moving "there is \( N \in \nZ_{>0} \)" to the front.
3. Negate each of (a) and (b) into positive form: no \( \neg \) left in front of a quantifier or an implication, and \( \neg(s < t) \) written as \( s \ge t \).
4. Decide which of (a) and (b) is true in \( \nR \). For the true sentence give a proof, saying what each chosen number depends on; for the false one, prove its negation, giving the witnesses it asks for.
:::

*You may use that for every real number there is a natural number larger than it.*
:::

::: {.solution}
*A remark on the term \( 1/n \).* In the structure \( \nR \), the symbol \( / \) must be a function on all of \( \nR^2 \) (@def-structure, (M3)); give \( x/0 \) a value for every \( x \in \nR \), say \( x/0 \coloneqq 0 \). The bound \( n \in \nZ_{>0} \) keeps \( n \ge 1 \), so those values are never used.

*(a)* \( \forall \varepsilon > 0\ \exists N \in \nZ_{>0}\ \forall n \in \nZ_{>0}\ \bigl( n \ge N \to 1/n < \varepsilon \bigr) \).

*(b)* \( \exists N \in \nZ_{>0}\ \forall \varepsilon > 0\ \forall n \in \nZ_{>0}\ \bigl( n \ge N \to 1/n < \varepsilon \bigr) \).

*(c)* Push \( \neg \) inward one quantifier at a time, keeping each bound (@prp-bounded-quantifier-negation), then negate the implication (@prp-negated-implication):
\[
\begin{aligned}
\neg(a): &\quad \exists \varepsilon > 0\ \forall N \in \nZ_{>0}\ \exists n \in \nZ_{>0}\ \bigl( n \ge N \wedge 1/n \ge \varepsilon \bigr), \\
\neg(b): &\quad \forall N \in \nZ_{>0}\ \exists \varepsilon > 0\ \exists n \in \nZ_{>0}\ \bigl( n \ge N \wedge 1/n \ge \varepsilon \bigr).
\end{aligned}
\]

*(d)* **(a) is true.** Let \( \varepsilon > 0 \). Choose a natural number \( N \) with \( N > 1/\varepsilon \), by the fact allowed in the problem; since \( 1/\varepsilon > 0 \), \( N \in \nZ_{>0} \), and \( N \) depends on \( \varepsilon \). Let \( n \in \nZ_{>0} \) with \( n \ge N \). Then \( n \ge N > 1/\varepsilon > 0 \), and multiplying \( n > 1/\varepsilon \) by the positive number \( \varepsilon / n \) gives \( \varepsilon > 1/n \). Since \( n \) was arbitrary, and then \( \varepsilon \), (a) holds.

**(b) is false; its negation is true.** Let \( N \in \nZ_{>0} \). Take \( \varepsilon = 1/N \), which is positive, and \( n = N \), which is in \( \nZ_{>0} \) with \( n \ge N \). Then \( 1/n = 1/N \ge 1/N = \varepsilon \). Both witnesses depend on \( N \), as the order \( \forall N\ \exists \varepsilon\ \exists n \) allows. Since \( N \) was arbitrary, \( \neg(b) \) holds, so (b) is false. In words: no single \( N \) works for every \( \varepsilon \), because \( \varepsilon = 1/N \) defeats that \( N \).

The two sentences differ only in the order of \( \forall \varepsilon \) and \( \exists N \). In (a) the \( N \) is chosen after \( \varepsilon \) and may depend on it; in (b) it must be chosen first, which is the swap of @exm-counter-model-swap in an analysis setting.

**Marking scheme.** (10 points)

- 2: both formalizations, with the bounds \( \varepsilon > 0 \), \( N \in \nZ_{>0} \), \( n \in \nZ_{>0} \) attached to the right quantifiers and \( \to \) under the \( \forall n \).
- 3: both negations in positive form, with every bound kept, the quantifier order of each preserved, and \( \wedge \) under the \( \exists n \).
- 2: verdict "true" for (a), with a proof in which \( N \) is chosen after \( \varepsilon \) and said to depend on it.
- 3: verdict "false" for (b), with \( \varepsilon \) and \( n \) given as functions of \( N \) and the three facts \( \varepsilon > 0 \), \( n \ge N \), \( 1/n \ge \varepsilon \) checked.

Fatal errors (0 for the step): in the negation of (b), \( \varepsilon \) chosen before \( N \) (a single \( \varepsilon \) for all \( N \)); a bound negated instead of the quantifier (\( \exists \varepsilon \le 0 \), or \( \exists n < N \)).
:::

### R. Review

::: {#exr-models-r1}
[R1]

Decide whether each sequent is derivable, and justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( (p \to q) \to r \vdash p \to r \).
2. \( (p \to q) \to r \vdash q \to r \).
:::
:::

::: {.solution}
*(a)* Not derivable. Look for a refuting row, backwards from the conclusion: \( p \to r \) is false only when \( p = \mathrm{T} \) and \( r = \mathrm{F} \). The premise must then be true, so its hypothesis \( p \to q \) must be false, which needs \( q = \mathrm{F} \). In the row \( p = \mathrm{T} \), \( q = \mathrm{F} \), \( r = \mathrm{F} \), the premise is \( \mathrm{F} \to \mathrm{F} \), true, and the conclusion is \( \mathrm{T} \to \mathrm{F} \), false. By @cor-refuting-row there is no derivation.

*(b)* Derivable. The goal is an implication, so open a box on \( q \); the premise is waiting for \( p \to q \), which a box on \( p \) produces by repeating \( q \) (the goal-directed and premise-directed steps of the search method of Section 2.6).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(p \to q) \to r}
  \open
  \hypo {2} {q}
  \open
  \hypo {3} {p}
  \have {4} {q} \r{2}
  \close
  \have {5} {p \to q} \ii{3-4}
  \have {6} {r} \ie{1,5}
  \close
  \have {7} {q \to r} \ii{2-6}
\end{nd}$
\end{center}
```

The row method of (a) could not settle (b): no row refutes it, and only a derivation (or @thm-completeness) shows it is derivable.
:::

::: {#exr-models-r2}
[R2]

Derive \( \neg(P \to \neg Q) \vdash \neg\neg P \wedge \neg\neg Q \) without \( \rulename{RAA} \) and without derived rules that use it. Which rule would you need to derive \( P \wedge Q \) itself?
:::

::: {.solution}
The goal is a conjunction, so derive each conjunct. Each is a negation, so each gets a \( \rulename{\neg I} \) box, whose goal is \( \bot \). The only way to use the premise \( \neg(P \to \neg Q) \) is to clash with it, so inside each box we build \( P \to \neg Q \). In the first box, from \( \neg P \): a \( \rulename{{\to}I} \) box on \( P \) clashes \( P \) with \( \neg P \) and uses \( \rulename{\bot E} \) (the pattern of @prp-vacuous-implication). In the second, from \( \neg Q \): a \( \rulename{{\to}I} \) box on \( P \) simply repeats \( \neg Q \). These are the rules of Chapters 1 and 2 (@def-rules-negation, @def-rules-contradiction, @def-rules-implication).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \to \neg Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {\neg Q} \be{4}
  \close
  \have {6} {P \to \neg Q} \ii{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {\neg\neg P} \ni{2-7}
  \open
  \hypo {9} {\neg Q}
  \open
  \hypo {10} {P}
  \have {11} {\neg Q} \r{9}
  \close
  \have {12} {P \to \neg Q} \ii{10-11}
  \have {13} {\bot} \ne{12,1}
  \close
  \have {14} {\neg\neg Q} \ni{9-13}
  \have {15} {\neg\neg P \wedge \neg\neg Q} \ai{8,14}
\end{nd}$
\end{center}
```

No \( \rulename{RAA} \) is used. To reach \( P \wedge Q \) we would need \( P \) from \( \neg\neg P \) and \( Q \) from \( \neg\neg Q \), that is, \( \rulename{\neg\neg E} \), which is derived with \( \rulename{RAA} \) (@prp-double-negation), or an \( \rulename{RAA} \) box directly (@def-rule-raa). The look-alike is @exr-finding-derivations-b1 (b), \( \neg(P \to Q) \vdash P \wedge \neg Q \): there the conjunct \( P \) needed \( \rulename{RAA} \), while \( \neg Q \) came by \( \rulename{\neg I} \) alone. Here both conjuncts stop at a double negation. That no derivation of \( P \) (or of \( P \wedge Q \)) from the premise avoids \( \rulename{RAA} \) is true, but we state it without proof, and nothing depends on it.
:::

::: {#exr-models-r3}
[R3]

Derive \( \neg\exists x\, (P(x) \to \neg Q(x)) \vdash \forall x\, \bigl( \neg\neg P(x) \wedge \neg\neg Q(x) \bigr) \) without \( \rulename{RAA} \).
:::

::: {.solution}
The goal is \( \forall x \), so open a flagged box with a fresh name \( x_0 \) (@def-rules-universal); the new goal is \( \neg\neg P(x_0) \wedge \neg\neg Q(x_0) \). Inside, run the derivation of R2 (@exr-models-r2) with \( P(x_0) \) and \( Q(x_0) \) in place of \( P \) and \( Q \). One change: the premise is now \( \neg\exists x\, (P(x) \to \neg Q(x)) \), not \( \neg(P \to \neg Q) \), so each clash first turns \( P(x_0) \to \neg Q(x_0) \) into \( \exists x\, (P(x) \to \neg Q(x)) \) by \( \rulename{\exists I} \) at \( x_0 \) (@def-rule-existential-introduction).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg \exists x\, (P(x) \to \neg Q(x))}
  \open[x_0]
  \open
  \hypo {2} {\neg P(x_0)}
  \open
  \hypo {3} {P(x_0)}
  \have {4} {\bot} \ne{3,2}
  \have {5} {\neg Q(x_0)} \be{4}
  \close
  \have {6} {P(x_0) \to \neg Q(x_0)} \ii{3-5}
  \have {7} {\exists x\, (P(x) \to \neg Q(x))} \Ei{6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {\neg\neg P(x_0)} \ni{2-8}
  \open
  \hypo {10} {\neg Q(x_0)}
  \open
  \hypo {11} {P(x_0)}
  \have {12} {\neg Q(x_0)} \r{10}
  \close
  \have {13} {P(x_0) \to \neg Q(x_0)} \ii{11-12}
  \have {14} {\exists x\, (P(x) \to \neg Q(x))} \Ei{13}
  \have {15} {\bot} \ne{14,1}
  \close
  \have {16} {\neg\neg Q(x_0)} \ni{10-15}
  \have {17} {\neg\neg P(x_0) \wedge \neg\neg Q(x_0)} \ai{9,16}
  \close
  \have {18} {\forall x\, (\neg\neg P(x) \wedge \neg\neg Q(x))} \Ai{2-17}
\end{nd}$
\end{center}
```

The side condition of \( \rulename{\forall I} \) at line 18: \( x_0 \) does not appear in the premise on line 1, no box is open at line 18, and \( x_0 \) does not appear in the conclusion. The flagged box immediately contains the \( \rulename{\neg I} \) box of line 2, so it is cited from line 2, the first line of that inner box. Lines 7 and 14 are legal \( \rulename{\exists I} \) steps: \( P(x_0) \to \neg Q(x_0) \) is \( (P(x) \to \neg Q(x))[x_0/x] \). The whole derivation is R2's, run inside a flagged box, with an \( \rulename{\exists I} \) before each clash.
:::

::: {#exr-models-r4}
[R4]

Is the sentence \( \forall x\, \exists y\, (x < y) \to \exists y\, \forall x\, (x < y) \) true in \( (\nN, <) \)? Is it derivable?
:::

::: {.solution}
*True in \( (\nN, <) \)?* No. The hypothesis \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \): each \( d \) has \( d + 1 \) above it. The conclusion \( \exists y\, \forall x\, (x < y) \) is false: a candidate \( e \) fails at \( x = e \), since \( e < e \) is false. By (S5) of @def-satisfaction, an implication with a true hypothesis and a false conclusion is false.

*Derivable?* No. By the soundness statement of this section, a derivable sentence is true in every structure; this one is false in \( (\nN, <) \), so no derivation exists.

*Why these tools.* A structure settles the question in two lines, while a derivation search could only fail, and a failed search proves nothing. A truth table is the wrong look-alike: it reads the sentence as \( p \to q \) with two atoms, and a refuting row for \( p \to q \) says nothing here, since the sentence \( \forall x\, P(x) \to \exists x\, P(x) \) has the same shape and is derivable (@prp-forall-implies-exists, then \( \rulename{{\to}I} \)). The soundness statement used here is proved in Section 4.12.
:::

<!-- dependency ledger
def-structure (claim): D^n, subsets, ordered pairs and functions used in their everyday meaning | ch06 (promised), prose pointer "Chapter 6 develops sets, pairs and functions properly"
def-structure (example): with = read as same parity on Z, -2 = 2 and P(2) hold and P(-2) fails | inline
def-structure (example): a sentence false in some structure is not derivable | the soundness statement of this section (not proved here; Section 4.12)
def-assignment (claim): an assignment exists because D is non-empty (a constant assignment) | inline, from def-structure (M1)
def-assignment (claim): the value of a term is well defined by recursion on terms | thm-structural-recursion (pattern), def-term; Section 4.2 says Chapter 3's induction and recursion carry over to terms and first-order formulas
def-assignment (example): values 2*2 + (-3) = 1, 2*2 + 1 = 5, -3, and 1 + 1 = 2 | inline; verify/ch04/def-satisfaction.py
def-satisfaction (claim): satisfaction is well defined by recursion on formulas, for all assignments at once | thm-structural-recursion applied to def-first-order-formula (Section 4.2 remark)
def-satisfaction (example): traces of forall x exists y (x < y) in N and in {1,2,3}; forall y (x <= y) in N under l(x) = 0 and l(x) = 1; one-element domain | inline; verify/ch04/def-satisfaction.py
def-satisfaction (solution): every real square is >= 0; sqrt(d) exists for d >= 0; a product of non-negative reals is non-negative | school algebra; ch11 (thm-nth-root) proves the roots, prose only
def-satisfaction (solution): every complex number has a complex square root (polar form) | school algebra of complex numbers, stated in the solution; not proved in the book before Part V
lem-free-coincidence (proof): structural induction on terms and on first-order formulas | thm-structural-induction (pattern) with the clauses of def-term and def-first-order-formula; Section 4.2 remark
lem-free-coincidence (proof): every variable of an atomic formula is free in it; the free variables of forall x phi are those of phi other than x | def-free-variable
lem-free-coincidence (proof): the cases not, or, ->, <-> repeat the conjunction argument with the other clauses | inline, as in lem-coincidence
def-first-order-entailment (claim): symbols a structure interprets but a formula does not contain never matter | inline, read off the clauses of def-satisfaction
def-first-order-entailment (example): forall x (P(x) -> Q(x)), P(c) |= Q(c) | inline from def-satisfaction
def-first-order-entailment (claim): forall x P(x) |= exists x P(x) in non-empty domains; it would fail for D empty | inline
def-first-order-entailment (claim): bounded quantifiers over the empty set, true and false | def-bounded-quantifier; inline
exm-counter-model-swap (solution): Z with >, the two-element identity; no one-element counter-model | inline; verify/ch04/exm-counter-model-swap.py
exm-counter-model-swap (example): converses of prp-exists-and and of the forall/or law; exists x P(x) |/= P(c); P(x_0) |/= forall x P(x); strict-order models Z, Q and the one-element non-model; the second Quick check | inline; verify/ch04/exm-counter-model-swap.py
exm-counter-model-swap (example): every integer is even or odd, and not both (the Z illustrations of the two converses) | ch07 (promised); STATUS Ch 1 row, as in Ch 1 §01, §07
def-first-order-entailment (claim): Gamma |- phi implies Gamma |= phi (soundness for predicate logic) | stated without proof in this section and marked so; proved in Section 4.12 (optional; thm-first-order-soundness, never cited here)
def-first-order-entailment (claim): x^2 on R is continuous and not uniformly continuous | exm-square-not-uniform (Section 4.10), cited in prose
exr-models-a1 (solution): witnesses and failing elements in N, Z, Q; z = (d + e)/2 is rational and strictly between | inline; verify/ch04/exr-models-a1.py
exr-models-b1 (solution): the three finite counter-models | verify/ch04/exr-models-b1.py
exr-models-b2 (solution): the three-element model and the alternatives | verify/ch04/exr-models-b2.py
exr-models-b3 (solution): the two-element counter-model | verify/ch04/exr-models-b3.py
exr-models-c1 (solution): a subset of an n-element set with n elements is the whole set | school counting fact, named in the solution; ch08 (promised) proves it
exr-models-c1 (solution): successor on N is injective and misses 0 | inline
exr-models-c2 (solution): a finite set with n elements does not contain n + 1 different elements | school counting fact, named in the solution; ch08 (promised)
exr-models-c3 (solution): for every real there is a larger natural number | given in the problem; thm-naturals-unbounded (Ch 11), not cited
exr-models-c3 (solution): n > 1/eps > 0 implies 1/n < eps | school algebra of < (Ch 11 ordered-field rules)
exr-models-a1 (solution): (e) non-derivability from the three-element counter-model | the soundness statement of this section (not proved here; Section 4.12)
exr-models-b1 (solution): (iii) non-derivability from the counter-model with l(x) = b; forall x (P(x) -> P(x)) is satisfied everywhere by (S5), (S6) | the soundness statement of this section (not proved here; Section 4.12); inline
exr-models-b3 (solution): non-derivability from a counter-model | the soundness statement of this section (not proved here; Section 4.12)
exr-models-c1 (solution): non-derivability from a counter-model | the soundness statement of this section (not proved here; Section 4.12)
exr-models-r4 (solution): non-derivability from a false instance | the soundness statement of this section (not proved here; Section 4.12)
exr-models-r1 (solution): refuting row and derivation | cor-refuting-row; verify/ch04/exr-models-r1.py
exr-models-r2 (solution): neg-neg-E is derived with RAA | prp-double-negation (cited)
exr-models-r2 (solution): no RAA-free derivation of P or P and Q from not(P -> not Q) | stated without proof and marked so; nothing depends on it
exr-models-r3 (solution): the derivation of R2 rerun with P(x_0), Q(x_0) inside a flagged box | exr-models-r2 (cited)
-->
