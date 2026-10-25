# Structures and Satisfaction

Sections 5.3 to 6.4 derived a good deal, and some searches stalled. The converse of @prp-exists-forall-swap could not be finished: every attempt ran into a side condition. The converse of @prp-exists-and stalled in the same way, and so did the search for \( \exists x\, P(x) \vdash P(c) \) in @exr-existential-introduction-c2. But a search that fails proves nothing, since a cleverer derivation might exist. Chapter 4 met the same problem for the connectives and solved it with meaning: a row of a truth table that makes the premises true and the conclusion false rules out every derivation at once (@cor-refuting-row). This section builds the meaning of a quantified formula: a **model**, a domain of objects with a meaning for every symbol. A model that makes the premises true and the conclusion false is a **counter-model**, the exact form of the counter-readings used since Section 5.3, and Section 7.2 uses it to settle the stalled searches.

::: {.remark}
[Looking back]

Section 4.4 gave each formula of Chapter 4 a truth value by recursion on the formula, one clause per connective, under a row. This section does the same for first-order formulas, with a structure and an assignment in place of a row. Clauses (S3)–(S5) below are Chapter 4's clauses word for word; (S6) and (S7), for the quantifiers, are the new ones.
:::

## Why a row is not enough

Chapter 4's semantics gave each atom a truth value and computed the rest. Try it on the stalled sequent of @prp-exists-forall-swap's converse,
\[
\forall y\, \exists x\, R(x, y) \vdash \exists x\, \forall y\, R(x, y) .
\]
Neither side has a main connective among \( \neg, \wedge, \vee, \to, \leftrightarrow \): each is a quantified formula, and a truth table would have to treat each as one atom. The sequent would become \( p \vdash q \), refuted by the row \( p = \mathrm{T} \), \( q = \mathrm{F} \). That "refutation" is worthless. The same reading refutes \( \forall x\, P(x) \vdash \exists x\, P(x) \), which is derivable (@prp-forall-implies-exists). Treating a quantified formula as an atom throws away exactly the structure that the quantifier rules use.

So what does make \( \forall y\, \exists x\, R(x, y) \) true or false? Section 5.1 read such sentences informally, **over a domain**: "for every \( y \) in the domain there is an \( x \) in the domain with \( R(x, y) \)". To decide it we need three things.

- **A domain**: the objects the variables range over. Over \( \nZ \) the sentence may be true and over a three-element set false.
- **A meaning for each symbol.** \( R \) is a predicate symbol, a name with two slots and no meaning of its own (Section 5.2). Read as \( > \) on \( \nZ \), the sentence says "every integer has an integer above it", which is true; read as \( < \) on \( \nN \), it says "every natural number has a natural number below it", which is false at \( y = 0 \).
- **Values for the free variables**, if there are any. The formula \( \exists y\, (y < x) \) is neither true nor false on \( \nN \) until we know which number \( x \) is.

The first two together are a **structure**; the third is an **assignment**. A structure with an assignment decides every formula, by clauses that read the quantifiers as Section 5.1 read them. That is all this section does; Section 7.2 uses the result.

## Structures

Situate the notion first. A formula is built from **symbols**: constants such as \( c \) and \( 0 \), function symbols such as \( f \) and \( + \), predicate symbols such as \( P \), \( R \) and \( < \), each function and predicate symbol with its number of argument places, its **arity** (Section 5.2, @def-term and @def-first-order-formula). The symbol \( = \) is special: it is part of the logic, with rules of its own (@def-rules-equality), and it will always mean the same thing. A structure gives every other symbol a meaning.

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

In words. (M1) says what the variables range over, and insists that there is at least one object. (M2) says which object each name names; two constants may name the same object. (M3) makes each function symbol an operation that can be applied to **any** objects of the domain and always returns an object of the domain. (M4) makes each predicate symbol a relation: \( R^{\fM} \) is the set of tuples for which \( R \) "holds". A one-place predicate symbol \( P \) becomes a subset \( P^{\fM} \subseteq D \), a two-place one a set of ordered pairs, and so on. Here \( D^n \) is the set of \( n \)-tuples \( (d_1, \dots, d_n) \) of elements of \( D \); this section uses only their everyday meaning.

We usually describe a structure in one line, naming the domain and the meaning of each symbol, and write "\( \fM = (\nZ, <) \)" for the structure with domain \( \nZ \) in which the symbol \( < \) means the usual order. When a symbol has its usual meaning on a familiar set, we say so and do not write \( <^{\fM} \).

**Examples**, simplest first.

- *One element.* \( D = \{ a \} \), with \( P^{\fM} = \{ a \} \). This is the degenerate structure. Every variable must take the value \( a \), so "for every element" and "there is an element" both mean "\( a \)". It will reappear as a test case: a sentence true here and false in some other structure cannot be derivable (by the soundness statement in Section 7.2), and some of the chapter's non-derivable sequents need at least two elements to refute.
- *Two elements, one relation.* \( D = \{ a, b \} \), with \( R^{\fM} = \{ (a, a), (b, b) \} \): the relation "is the same as", written out as a set of pairs. A finite structure can be given completely by listing.
- *The integers with their order.* \( D = \nZ \), with \( R^{\fM} = \{ (x, y) \in \nZ^2 : x > y \} \). Here the relation is described by a condition rather than a list.
- *Arithmetic.* \( D = \nR \), with the constants \( 0 \) and \( 1 \) naming zero and one, the function symbols \( + \), \( \cdot \) and two-place \( - \) meaning addition, multiplication and subtraction, the one-place symbols \( - \), \( (\cdot)^2 \) and \( \abs{\cdot} \) meaning negation, squaring and absolute value, and \( < \), \( \le \), \( > \), \( \ge \) the usual order. Extended by the other familiar symbols with their usual meanings (numerals, halving, the predicates \( \in A \), division with its value at a zero denominator fixed arbitrarily as in the non-example below, and a function symbol for each sequence or function an example uses), this is the structure in which the analysis examples of Chapters 5 and 6 have been read all along.

::: {.second-reading title="A non-example, and the repair used for 1/n"}
*Non-example by minimal change.* Take the arithmetic structure and add a one-place function symbol \( g \), meant to be read as \( x \mapsto 1/x \). This is **not** a structure: (M3) asks for a function defined at every element of \( D \), and \( 1/0 \) is not defined. Everything else in the description is fine; exactly clause (M3) fails, at the single point \( 0 \). There are two repairs. Shrink the domain to \( (0, \infty) \), where \( 1/x \) is always defined; or keep \( \nR \) and give \( g \) any value at \( 0 \), say \( g^{\fM}(0) \coloneqq 0 \). The second repair is the one this book uses for terms such as \( 1/n \): the value at \( 0 \) is fixed arbitrarily and is never looked at, because such terms are used only under a bound \( n \in \nZ_{>0} \) (as in @exr-models-c3), exactly as a sequence \( a_n \) was read in Section 5.1 as a function symbol whose values off \( \nN \) are never used.
:::

The domain is non-empty because of @prp-forall-implies-exists; the subsection "Why domains are non-empty" explains why.

::: {.second-reading title="Why total functions, and why identity"}
- *Total functions.* Clause (M3) is what makes every term name an object: the term \( g(0) \) must have a value, or the formula \( g(0) = g(0) \), which \( \rulename{{=}I} \) derives from nothing, would have no truth value.
- *Identity for \( = \).* The rule \( \rulename{{=}E} \) replaces equals by equals **everywhere**. If a structure could read \( = \) as some other relation, \( \rulename{{=}E} \) would fail. On \( \nZ \), read \( x = y \) as "\( x \) and \( y \) have the same parity" and \( P \) as "is positive": then \( -2 = 2 \) and \( P(2) \) would both hold, while \( P(-2) \), which \( \rulename{{=}E} \) derives from them, fails. With \( = \) fixed as identity, no such reading exists.
:::

::: {.warning}
A structure must interpret **every** symbol that occurs in the formulas at hand. "Take \( D = \nZ \)" is not yet a structure for \( \forall y\, \exists x\, R(x, y) \): until \( R \) is given a meaning, the sentence has no truth value, and the same domain makes it true with \( R \) read as \( > \) and false with \( R \) read as "\( x \cdot x = y \)" (at \( y = 2 \)). Always write the domain **and** the meaning of each symbol.
:::

## Drawing a finite structure

A finite structure whose symbols are one- and two-place predicate symbols can be drawn, as Section 5.1 drew its worlds. Each element is a dot. Beside a dot stand its name and the one-place predicates it satisfies. For a two-place relation \( R \), an arrow runs from \( d \) to \( e \) for each pair \( (d, e) \) in \( R^{\fM} \), and a loop at \( d \) records the pair \( (d, d) \). Deciding a sentence in a drawn structure is then reading the picture, dot by dot.

When the relation is a partial order \( \le \), arrows crowd the picture, and a lighter drawing is used. Section 7.4 defines partial orders; here it is enough that \( \le \) is reflexive and transitive and never holds both ways between two different elements. The **Hasse diagram** of such a structure puts \( d \) below \( e \) when \( d \le e \) and \( d \ne e \), and draws a line only for the pairs with nothing strictly between them. The loops, and the pairs that follow by chaining lines upwards, are understood. In the right picture below, \( 1 \le 6 \) holds although no line joins \( 1 \) and \( 6 \): the chain \( 1 \), \( 2 \), \( 6 \) runs upwards.

A picture is a structure only when it says what every symbol means: the caption names the domain and each symbol. Figure F draws two structures. Left: \( D = \{ a, b, c \} \), \( P^{\fM} = \{ a \} \), \( R^{\fM} = \{ (a, b), (b, b), (c, a) \} \). Right: \( D = \{ 1, 2, 3, 6 \} \), with \( x \le y \) read as "\( x \) divides \( y \)".

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=below:{$a$ ($P$)}] (a) at (0,0) {};
  \node[elt, label=below:$b$] (b) at (1.6,0) {};
  \node[elt, label=above:$c$] (c) at (0.8,1.3) {};
  \draw[rel] (a) -- (b);
  \draw[rel] (b) to[loop right] (b);
  \draw[rel] (c) -- (a);
  \node[universe, fit=(a)(b)(c)] {};
\end{tikzpicture}
\qquad
\begin{tikzpicture}[hasse]
  \node (n1) at (0,0) {$1$};
  \node (n2) at (-1,1.1) {$2$};
  \node (n3) at (1,1.1) {$3$};
  \node (n6) at (0,2.2) {$6$};
  \path (n1) edge (n2) (n1) edge (n3) (n2) edge (n6) (n3) edge (n6);
\end{tikzpicture}
\end{center}
```

**Figure F.** An arrow diagram (left) and a Hasse diagram (right).

::: {.check}
In the left structure of Figure F, decide \( \forall x\, \exists y\, R(x, y) \) and \( \exists y\, \forall x\, R(x, y) \).
:::

::: {.solution}
The first is true: every dot has an arrow out of it (\( a \to b \), \( b \to b \), \( c \to a \)). The second is false: no dot receives an arrow from all three. The dot \( b \) receives none from \( c \), the dot \( a \) none from \( a \) or \( b \), and the dot \( c \) none at all.
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

There are always assignments, because \( D \) is non-empty: pick any \( d_0 \in D \) and let every variable have the value \( d_0 \). Like a valuation in Chapter 4 (@def-valuation), an assignment fixes infinitely many values, and a formula will only ever look at finitely many of them.

With a structure and an assignment, every term names an element of the domain. Terms are built by the clauses of @def-term, so the value is defined by recursion on terms, in the pattern of @thm-structural-recursion.

*The value of a term is computed from its variables and constants upwards, one function symbol at a time.*

For a structure \( \fM \) and an assignment \( \ell \), the **value** \( t^{\fM, \ell} \in D \) of a term \( t \) is:

- \( x^{\fM, \ell} \coloneqq \ell(x) \) for a variable \( x \);
- \( c^{\fM, \ell} \coloneqq c^{\fM} \) for a constant \( c \);
- \( f(t_1, \dots, t_n)^{\fM, \ell} \coloneqq f^{\fM}\bigl( t_1^{\fM, \ell}, \dots, t_n^{\fM, \ell} \bigr) \) for a function symbol \( f \) of arity \( n \).

The third clause is where (M3) is needed: \( f^{\fM} \) must accept every tuple the terms \( t_1, \dots, t_n \) might produce.

For example, in the arithmetic structure on \( \nR \), let \( \ell(x) = 2 \) and \( \ell(y) = -3 \). The term \( x \cdot x + y \), which is \( +(\cdot(x, x), y) \) written in the usual way, has value \( 2 \cdot 2 + (-3) = 1 \). Under \( \ell[y \mapsto 1] \) it has value \( 2 \cdot 2 + 1 = 5 \), and under \( \ell[x \mapsto 0] \) it has value \( -3 \). The term \( 1 + 1 \) has value \( 2 \) under every assignment, since it contains no variable.

## Satisfaction

Now the central definition. We want to say when a structure and an assignment make a formula true. Formulas are built by the clauses of @def-first-order-formula, so we define it by recursion, one clause per way of building a formula, and each clause reads its connective or quantifier as Chapter 4 and Section 5.1 read it.

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

Read it clause by clause. (S1): an atomic formula is satisfied exactly when the values of its terms form a tuple in the relation that interprets its predicate symbol. (S2): an equation is satisfied when both sides name the same object; this is where "\( = \) means identity" enters. (S3)–(S5) are the \( \bot \) half of (V1) and clauses (V2)–(V6) of Chapter 4's @def-truth-value, with "is true under \( v \)" replaced by "is satisfied by \( \fM \) under \( \ell \)": \( \bot \) is never satisfied, \( \neg \) flips, \( \wedge \) needs both, \( \vee \) needs one, \( \to \) fails only with a satisfied hypothesis and an unsatisfied conclusion, \( \leftrightarrow \) needs agreement. (S6) and (S7) are the new clauses. To decide \( \forall x\, \varphi \), we run through the elements \( d \) of the domain, set \( x \) to \( d \) and leave every other variable alone, and ask whether \( \varphi \) is satisfied each time. For \( \exists x\, \varphi \) one success is enough. In symbols, for (S6) and (S7):
\[
\begin{aligned}
\fM, \ell \models \forall x\, \varphi \quad &\text{iff} \quad \text{for every } d \in D, \ \ \fM, \ell[x \mapsto d] \models \varphi , \\
\fM, \ell \models \exists x\, \varphi \quad &\text{iff} \quad \text{there is } d \in D \text{ with } \fM, \ell[x \mapsto d] \models \varphi .
\end{aligned}
\]

**A trace, step by step.** Decide \( \forall x\, \exists y\, (x < y) \) in two structures, both with \( < \) the usual order: \( \fM_1 \) with domain \( \nN \), and \( \fM_2 \) with domain \( \{ 1, 2, 3 \} \). Let \( \ell \) be any assignment.

In \( \fM_1 \): by (S6) we must check, for every \( d \in \nN \), that \( \fM_1, \ell[x \mapsto d] \models \exists y\, (x < y) \). Fix \( d \). By (S7) it is enough to find one \( e \in \nN \) with \( \fM_1, \ell[x \mapsto d][y \mapsto e] \models x < y \). Take \( e = d + 1 \). Under \( \ell[x \mapsto d][y \mapsto d + 1] \) the terms \( x \) and \( y \) have the values \( d \) and \( d + 1 \), and \( d < d + 1 \), so (S1) holds. Hence the sentence is satisfied. Notice that the witness \( e = d + 1 \) depends on \( d \): (S7) is checked **inside** (S6), once for each \( d \).

In \( \fM_2 \): (S6) asks the same for \( d = 1, 2, 3 \). At \( d = 1 \) and \( d = 2 \) the witnesses \( e = 2 \) and \( e = 3 \) work. At \( d = 3 \) no \( e \in \{ 1, 2, 3 \} \) has \( 3 < e \), so (S7) fails for \( \ell[x \mapsto 3] \), and (S6) fails. So \( \fM_2 \not\models \forall x\, \exists y\, (x < y) \), and the failure has a name: the element \( 3 \) has nothing above it.

**The assignment matters for free variables.** In \( \fM_1 = (\nN, <) \), with \( \le \) also read as usual, take the formula \( \forall y\, (x \le y) \), in which \( x \) is free. Under an assignment with \( \ell(x) = 0 \) it is satisfied, since every \( e \in \nN \) has \( 0 \le e \) (recall that \( \nN = \{ 0, 1, 2, \dots \} \)). Under an assignment with \( \ell(x) = 1 \) it is not: \( e = 0 \) gives \( 1 \le 0 \), which fails. The same formula in the same structure is satisfied under one assignment and not under another; it is a property of \( x \), "\( x \) is least", not a statement.

::: {.second-reading title="Satisfaction is well defined; degenerate cases"}
**Well defined.** The clauses define, for each formula, which pairs \( (\fM, \ell) \) satisfy it, by recursion on the formula: (S1)–(S3) settle the atomic formulas and \( \bot \), and each of (S4)–(S7) settles a compound formula from its immediate parts. One point needs a word. Clauses (S6) and (S7) consult the immediate part \( \varphi \) under **other** assignments \( \ell[x \mapsto d] \), not under \( \ell \). So the recursion must define satisfaction of each formula under **all** assignments at once, and then (S6) reads off the answer for \( \varphi \) at every \( \ell[x \mapsto d] \). The recursion is still on the formula alone, and @thm-structural-recursion, applied to formulas built by the clauses of @def-first-order-formula, gives exactly one such relation.

**Degenerate cases.** In the one-element structure \( D = \{ a \} \), every assignment gives every variable the value \( a \), so \( \ell[x \mapsto a] = \ell \) and (S6) and (S7) both reduce to "\( \fM, \ell \models \varphi \)". So \( \forall x\, \varphi \) and \( \exists x\, \varphi \) are satisfied together or not at all, and every equation \( x = y \) is satisfied. In any structure, \( \forall x\, (x = x) \) is satisfied, since every \( d \) is the same element as itself; and \( \exists x\, \neg(x = x) \) never is.
:::

**Satisfaction as a game.** Section 5.1 read a sentence whose quantifiers all stand in front as a game between a challenger, who tries to make it false, and a defender, who tries to make it true. The clauses extend that game to every formula, one move per clause. At \( \forall x\, \varphi \) (S6) the challenger picks an element \( d \in D \) for \( x \); at \( \exists x\, \varphi \) (S7) the defender picks. At \( \varphi \wedge \psi \) the challenger picks the side to be checked, and at \( \varphi \vee \psi \) the defender does; \( \varphi \to \psi \) is played as \( \neg\varphi \vee \psi \), and \( \varphi \leftrightarrow \psi \) as the two implications joined by \( \wedge \). At \( \neg\varphi \) the players change roles (S4), since making \( \neg\varphi \) true is making \( \varphi \) false. At an atomic formula the game ends, and the defender wins exactly when (S1) or (S2) holds; at \( \bot \) the defender never wins (S3). A sentence is true in \( \fM \) exactly when the defender can answer every challenge and win: read clause by clause, that is what (S1)–(S7) say. In the trace above, the defender's answer \( e = d + 1 \) to each challenge \( d \) is such a way of winning on \( \nN \); on \( \{ 1, 2, 3 \} \) the challenge \( d = 3 \) has no answer.

::: {.check}
Play the game for \( \exists y\, \forall x\, (x \le y) \) on \( (\nN, \le) \) and on \( (\{ 1, 2, 3 \}, \le) \). Who moves first, and who wins?
:::

::: {.solution}
The defender moves first, since \( \exists \) comes first: the order of the quantifiers is the order of the moves. On \( \nN \), whatever \( e \) the defender names, the challenger answers \( x = e + 1 \) and wins, so the sentence is false. On \( \{ 1, 2, 3 \} \) the defender names \( 3 \), and every challenge \( x \) has \( x \le 3 \), so the sentence is true.
:::

::: {.check}
Is \( \forall x\, \exists y\, (y \cdot y = x) \) satisfied in \( \nR \), in \( [0, \infty) \), and in \( \nC \), each with \( \cdot \) the usual product?
:::

::: {.solution}
In \( \nR \), no: at \( d = -1 \), (S7) asks for a real \( e \) with \( e \cdot e = -1 \), and every real square is \( \ge 0 \). In \( [0, \infty) \), yes: for each \( d \ge 0 \), \( e = \sqrt{d} \) is in the domain and \( e \cdot e = d \); and \( [0, \infty) \) with \( \cdot \) is a structure, since a product of non-negative reals is non-negative (M3). In \( \nC \), yes: every complex number has a complex square root (school algebra of complex numbers: \( r(\cos\theta + i\sin\theta) \) with \( r \ge 0 \) has the square root \( \sqrt{r}\,(\cos\frac{\theta}{2} + i\sin\frac{\theta}{2}) \)). The sentence is the same all three times; only the structure changes.
:::

## Only the free variables matter

The example of \( \forall y\, (x \le y) \) above showed \( \ell \) mattering. In the first example it did not: the verdict on \( \forall x\, \exists y\, (x < y) \) was reached for "any assignment \( \ell \)". That is no accident. A sentence has no free variables (@def-sentence), and every variable it contains is bound, so every value \( \ell \) gives is overwritten by (S6) or (S7) before it is looked at. We prove the general fact, which is the first-order version of Chapter 4's @lem-coincidence: satisfaction depends only on the values of the **free** variables.

Say that two assignments \( \ell \) and \( \ell' \) **agree on** a set of variables if \( \ell(y) = \ell'(y) \) for every variable \( y \) in it. We need the free variables of a formula, recursively defined in @def-free-variable: every variable occurring in an atomic formula is free there; \( \neg\varphi \) has the free variables of \( \varphi \); \( \varphi \circ \psi \), for a binary connective \( \circ \), has those of \( \varphi \) and those of \( \psi \); and \( \forall x\, \varphi \) and \( \exists x\, \varphi \) have those of \( \varphi \) other than \( x \).

::: {#lem-free-coincidence}
[Free Variables Coincidence Lemma]

Let \( \fM \) be a structure and \( \varphi \) a formula, and let \( \ell \) and \( \ell' \) be assignments in \( \fM \) that agree on every free variable of \( \varphi \). Then
\[
\fM, \ell \models \varphi \quad \text{if and only if} \quad \fM, \ell' \models \varphi .
\]
:::

*In words: to decide a formula, only the values of its free variables matter.*

:::: {.second-reading title="The proof: an induction for all assignments at once"}
::: {.idea}
Structural induction on \( \varphi \), as for @lem-coincidence, after a first induction on terms: a term's value depends only on the values of its variables. The connective cases are Chapter 4's. The quantifier case is the only new one, and it explains why the property must be stated **for all** pairs of assignments: (S6) compares \( \ell[x \mapsto d] \) with \( \ell'[x \mapsto d] \), which are new assignments, so the induction hypothesis must apply to them. They agree at \( x \), since both give it \( d \), and at every other free variable of \( \varphi \), since those are free in \( \forall x\, \varphi \).
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
::::

::: {.check}
In \( (\nN, \le) \), does whether \( \ell \) satisfies \( \forall y\, (x \le y) \) depend on \( \ell(y) \)?
:::

::: {.solution}
No: \( y \) is not free in the formula, so by the lemma only \( \ell(x) \) matters. The formula holds exactly when \( \ell(x) = 0 \).
:::

The lemma has a consequence that the rest of the section uses constantly.

*Sentences.* If \( \varphi \) is a sentence, it has no free variables, so **any** two assignments agree on its free variables, and the lemma says that \( \fM, \ell \models \varphi \) either holds for every assignment \( \ell \) or for none. We then write \( \fM \models \varphi \), and say that \( \varphi \) is **true in** \( \fM \) (or that \( \fM \) is a model of \( \varphi \)), in the first case, and \( \fM \not\models \varphi \), \( \varphi \) is **false in** \( \fM \), in the second. At least one assignment exists because \( D \) is non-empty, so a sentence is always exactly one of true and false in \( \fM \). This is the precise form of Section 5.1's informal "true over a domain".

*Only finitely many values matter.* A formula has finitely many free variables. To decide \( \fM, \ell \models \varphi \), it is enough to know \( \ell \) on those. So we describe an assignment by the values that matter ("\( \ell(x) = 2 \)"), exactly as Chapter 4 described a valuation by the values of a few atoms.

::: {.warning}
The same sentence can be true in one structure and false in another, and "true" without a structure means nothing. \( \forall x\, \exists y\, (x < y) \) is true in \( (\nN, <) \) and false in \( (\{ 1, 2, 3 \}, <) \), as traced above. A sentence of predicate logic is like a formula of Chapter 4 with atoms: it has a truth value only once the meaning of its symbols has been fixed.
:::

## Semantic entailment

Chapter 4 said that \( \Gamma \) entails \( \psi \) when every row that makes \( \Gamma \) true makes \( \psi \) true (@def-valid-argument). The row is now a structure with an assignment.

*An argument is valid when every structure, under every assignment, that satisfies all the premises also satisfies the conclusion.*

::: {#def-first-order-entailment}
[Semantic Entailment in Predicate Logic]

Let \( \Gamma \) be a list of formulas and \( \varphi \) a formula. We say \( \Gamma \) **semantically entails** \( \varphi \), and write \( \Gamma \models \varphi \), if for **every** structure \( \fM \) for the symbols occurring in \( \Gamma \) and \( \varphi \), and **every** assignment \( \ell \) in \( \fM \),
\[
\fM, \ell \models \Gamma \quad \Rightarrow \quad \fM, \ell \models \varphi .
\]
We write \( \models \varphi \) when \( \Gamma \) is empty. If \( \Gamma \models \varphi \) fails, we write \( \Gamma \not\models \varphi \); a structure \( \fM \) with an assignment \( \ell \) such that \( \fM, \ell \models \Gamma \) and \( \fM, \ell \not\models \varphi \) is a **counter-model** to \( \Gamma \models \varphi \).
:::

In words: "every structure" means every domain and every meaning of the symbols, so an entailment holds for reasons of form and not because of what \( R \) happens to mean. "Every assignment" covers every value of the free variables; when \( \Gamma \) and \( \varphi \) are sentences, the assignment makes no difference, by @lem-free-coincidence. And a counter-model is the analogue of Chapter 4's refuting row: one structure, with one assignment, where the premises hold and the conclusion does not. The symbol \( \models \) is the one of Chapter 4, and the context always shows which is meant: a sequent of formulas with quantifiers or predicate symbols is read with this definition.

A structure may interpret symbols that do not occur in \( \Gamma \) or \( \varphi \). The clauses of @def-satisfaction consult only the symbols of the formula at hand, so such extra meanings change nothing.

*First examples of entailment.* The argument Section 5.1 opened with, "every positive real has a square root; 2 is positive; so 2 has a square root", is \( \forall x\, (P(x) \to Q(x)), \ P(c) \vdash Q(c) \), derived in Section 5.3. Truth tables called it invalid, since they saw three unrelated atoms. It is valid in the new sense:
\[
\forall x\, (P(x) \to Q(x)), \ P(c) \models Q(c) .
\]
Let \( \fM, \ell \) satisfy both premises, and let \( a = c^{\fM} \). By (S6) for the first premise, with \( d = a \), we get \( \fM, \ell[x \mapsto a] \models P(x) \to Q(x) \). Under \( \ell[x \mapsto a] \) the term \( x \) has value \( a \), and under \( \ell \) the term \( c \) has value \( a \); so by (S1), \( \fM, \ell[x \mapsto a] \models P(x) \) holds if and only if \( a \in P^{\fM} \) if and only if \( \fM, \ell \models P(c) \), which is the second premise. So by (S5) \( \fM, \ell[x \mapsto a] \models Q(x) \), that is, \( a \in Q^{\fM} \), and by (S1) again \( \fM, \ell \models Q(c) \). Chapter 4's objection to this argument is gone.

## Proving an entailment by meaning

To show \( \Gamma \models \varphi \), fix an arbitrary structure and assignment satisfying \( \Gamma \), and show that they satisfy \( \varphi \). The first proof below writes every step with the clause that licenses it; the second condenses it to what a mathematician writes.

::: {#exm-clause-by-clause}
[A Semantic Proof, Clause by Clause]

Show that \( \exists x\, \forall y\, R(x, y) \models \forall y\, \exists x\, R(x, y) \).
:::

::: {.solution}
Each step ends with the clause that licenses it.

1. Let \( \fM \) be a structure with domain \( D \) and \( \ell \) an assignment with \( \fM, \ell \models \exists x\, \forall y\, R(x, y) \) (@def-first-order-entailment).
2. There is \( d \in D \) with \( \fM, \ell[x \mapsto d] \models \forall y\, R(x, y) \) (S7).
3. To show \( \fM, \ell \models \forall y\, \exists x\, R(x, y) \), let \( e \in D \); we must show \( \fM, \ell[y \mapsto e] \models \exists x\, R(x, y) \) (S6).
4. From item 2, with this \( e \): \( \fM, \ell[x \mapsto d][y \mapsto e] \models R(x, y) \) (S6).
5. Under \( \ell[x \mapsto d][y \mapsto e] \) the terms \( x \), \( y \) have the values \( d \), \( e \), so \( (d, e) \in R^{\fM} \) (S1).
6. Take the witness \( d \) for \( x \): under \( \ell[y \mapsto e][x \mapsto d] \) the values are again \( d \), \( e \), so \( \fM, \ell[y \mapsto e][x \mapsto d] \models R(x, y) \) by item 5 (S1), and so \( \fM, \ell[y \mapsto e] \models \exists x\, R(x, y) \) (S7).
7. Since \( e \) was arbitrary, \( \fM, \ell \models \forall y\, \exists x\, R(x, y) \) (S6).

*Condensed.* Suppose some \( d \) is \( R \)-related to everything. Then for each \( e \), the element \( d \) itself is related to \( e \), so each \( e \) has something related to it.

Section 5.6 derived the same sequent (@prp-exists-forall-swap); this is its meaning. The converse fails, and Section 7.2 draws why.
:::

::: {.check}
In item 6, why are \( \ell[y \mapsto e][x \mapsto d] \) and \( \ell[x \mapsto d][y \mapsto e] \) the same assignment?
:::

::: {.solution}
The variables \( x \) and \( y \) are different, and each change touches only its own variable, so the order of the two changes does not matter (the paragraph after @def-assignment).
:::

::: {#exm-drinker-by-meaning}
[The Drinker Sentence, by Meaning]

Show that \( \models \exists x\, \bigl( P(x) \to \forall y\, P(y) \bigr) \): in every structure, some element has the property that if **it** has \( P \), everything has \( P \).
:::

::: {.solution}
Let \( \fM \) and \( \ell \) be given, with domain \( D \).

*Case 1: \( P^{\fM} = D \).* Choose any \( d \in D \), which exists because \( D \) is non-empty (M1). Under \( \ell[x \mapsto d] \) the formula \( \forall y\, P(y) \) is satisfied, by (S6), so the implication is satisfied, by (S5); hence the sentence holds, by (S7).

*Case 2: some \( d \in D \) is not in \( P^{\fM} \).* Under \( \ell[x \mapsto d] \) the hypothesis \( P(x) \) fails (S1), so the implication is satisfied (S5), and (S7) gives the sentence.

The case split is on a question about the whole structure, whether \( P^{\fM} = D \), and the witness depends on its answer; this is why no witness can be named in advance, and why a derivation needs a detour (Section 6.3 derived it, with \( D \), \( n \), \( m \) in place of \( P \), \( x \), \( y \), @exr-first-order-search-c1). Case 1 is where the non-empty domain is used, as in the next subsection.
:::

## Why domains are non-empty {#why-domains-are-non-empty}

Clause (M1) of @def-structure demands a non-empty domain. Here is the reason. @prp-forall-implies-exists derives \( \forall x\, P(x) \vdash \exists x\, P(x) \) in three lines: \( \rulename{\forall E} \) at the variable \( x \), then \( \rulename{\exists I} \). The matching entailment holds for our structures:
\[
\forall x\, P(x) \models \exists x\, P(x) .
\]
Let \( \fM, \ell \models \forall x\, P(x) \). Since \( D \) is non-empty, choose some \( d \in D \). By (S6), \( \fM, \ell[x \mapsto d] \models P(x) \), and this \( d \) is the one element (S7) asks for, so \( \fM, \ell \models \exists x\, P(x) \).

Now suppose empty domains were allowed. In a structure with \( D = \emptyset \), (S6) says \( \forall x\, P(x) \) is satisfied, since "for every \( d \in \emptyset \)" has nothing to check; and (S7) says \( \exists x\, P(x) \) is not, since there is no \( d \) at all. So the sequent would be derivable and yet fail in a structure, and the rules would lead from a true premise to a false conclusion. (Worse, no assignment into an empty domain exists, so even the clauses could not be applied as written.) One of two things had to give: the rule \( \rulename{\forall E} \) at a variable, or empty domains. The book, like most of mathematics, keeps the rules and makes domains non-empty.

Nothing is lost. Statements about an empty **set** are handled by the bounded quantifiers of @def-bounded-quantifier, inside a non-empty domain. The bounded forms \( \forall x \in \emptyset\ \varphi \) and \( \exists x \in \emptyset\ \varphi \) abbreviate \( \forall x\, (x \in \emptyset \to \varphi) \) and \( \exists x\, (x \in \emptyset \wedge \varphi) \), and in a structure with domain \( \nR \) in which the one-place predicate symbol \( \in \emptyset \) (Section 5.2) is interpreted, by (M4), as the empty subset of \( \nR \), the first is true (every hypothesis \( d \in \emptyset \) is false) and the second is false (no \( d \) is in \( \emptyset \)). Vacuous truth lives in the bound, not in the domain.

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
5. True or false: if a sentence is true in some structure, it is true in every structure for its symbols.
6. Why must the domain of a structure be non-empty? Name the derivable sequent that would otherwise fail.
7. In @exm-clause-by-clause, which clause produces the element \( d \), and why may the same \( d \) serve for every \( e \)?
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

*(e)* False. Sentence (b) is true in \( \fM_{\nN} \) and false in \( \fM_{\nZ} \), as the table shows.

*(f)* The sequent is \( \forall x\, P(x) \vdash \exists x\, P(x) \), derived in @prp-forall-implies-exists by \( \rulename{\forall E} \) at the variable \( x \) and \( \rulename{\exists I} \). In an empty domain \( \forall x\, P(x) \) would be true, with nothing to check, and \( \exists x\, P(x) \) false, with no witness; so the rules would lead from a true premise to a false conclusion. (There would also be no assignments at all.)

*(g)* (S7), applied to the premise in item 2. The element \( d \) is fixed before any \( e \) is chosen, and item 2 says that \( d \) is related to **every** \( e \), by (S6); so item 6 may use \( d \) whatever \( e \) item 3 picked.
:::

::: {#exr-structures-and-satisfaction-a2}
[A2: Drill]

Each part takes a line or two. Parts (a)–(d) read a structure or a clause, (e)–(i) decide a formula in a given structure, with a witness or a failing element, (j) and (k) judge, and (l) builds a structure.

::: {.enumerate options="label=(\alph*)"}
1. Let \( D = \{ a, b \} \) and \( P^{\fM} = \{ a \} \). Is \( \forall x\, P(x) \) true in \( \fM \)?
2. In the same structure, is \( \exists x\, \neg P(x) \) true?
3. In \( (\nR; 1, +, \cdot) \), what is the value of \( x \cdot x + 1 \) under an assignment with \( \ell(x) = -2 \)?
4. By @lem-free-coincidence, the values of which variables **can** matter to the truth of \( \forall y\, (x \le y) \wedge z = z \) in a given structure? Do they all matter?
5. In \( (\{ 0, 1, 2 \}, \le) \), is \( \exists x\, \forall y\, (x \le y) \) true?
6. In \( (\nN, <) \), under an assignment with \( \ell(x) = 3 \), is \( \exists y\, (y < x) \) satisfied? And with \( \ell(x) = 0 \)?
7. In the left structure of Figure F, is \( \forall x\, (P(x) \to \exists y\, R(y, x)) \) true?
8. Decide \( \forall x\, \forall y\, (x \le y \vee y \le x) \) in \( (\nN, \le) \) and in the right structure of Figure F.
9. Decide \( \exists x\, \forall y\, (y \cdot x = y) \) in \( (\nZ, \cdot) \) and in the even integers with \( \cdot \).
10. Is \( \nN \) with the two-place function symbol \( - \) read as subtraction a structure?
11. In a structure with \( D = \{ a \} \) and \( P^{\fM} = \emptyset \), decide \( \forall x\, P(x) \to \exists x\, P(x) \) and \( \forall x\, \neg P(x) \to \neg\exists x\, P(x) \).
12. Give a structure on \( \{ 1, 2 \} \) in which \( \exists x\, R(x, x) \) is false and \( \forall x\, \exists y\, R(x, y) \) is true.
:::
:::

::: {.solution}
(a) No: it fails at \( b \).

(b) Yes, at \( b \).

(c) \( (-2) \cdot (-2) + 1 = 5 \).

(d) At most \( x \) and \( z \), its free variables; not \( y \). In fact only \( x \) matters, since \( z = z \) holds under every assignment: the lemma gives an upper bound, not the exact set.

(e) Yes, with \( x = 0 \).

(f) Yes, with \( y = 0 \). With \( \ell(x) = 0 \), no: nothing in \( \nN \) is below \( 0 \).

(g) Yes: the only element with \( P \) is \( a \), and the arrow \( c \to a \) enters it; at \( b \) and \( c \) the hypothesis fails.

(h) True in \( \nN \); false in the divisibility structure, at \( x = 2 \), \( y = 3 \).

(i) True in \( \nZ \), with \( x = 1 \). False in the even integers: \( y = 2 \) would need \( 2x = 2 \), so \( x = 1 \), which is odd.

(j) No: (M3) fails, since \( 0 - 1 \notin \nN \).

(k) Both true: the first because its hypothesis fails at \( a \); the second because both sides are true.

(l) \( R^{\fM} = \{ (1, 2), (2, 1) \} \): no loops, and each element has an arrow out.
:::

### B. Practice

::: {#exr-structures-and-satisfaction-b1}
[B1: One sentence, two pictures]

Two structures for the one symbol \( \le \) are drawn below. On the left, \( \fM_1 \): the domain \( D_1 = \{ 1, 2, 3, 4, 6, 12 \} \), with \( x \le y \) read as "\( x \) divides \( y \)", as a Hasse diagram. On the right, \( \fM_2 = (\{ 1, 2, 3, 4, 5, 6 \}, \le) \), with the usual order, as a vertical chain.

```{=latex}
\begin{center}
\begin{tikzpicture}[hasse]
  \node (d1) at (0,0) {$1$};
  \node (d2) at (-0.8,1) {$2$};
  \node (d3) at (0.8,1) {$3$};
  \node (d4) at (-1.6,2) {$4$};
  \node (d6) at (0,2) {$6$};
  \node (d12) at (-0.8,3) {$12$};
  \path (d1) edge (d2) (d1) edge (d3) (d2) edge (d4) (d2) edge (d6)
        (d3) edge (d6) (d4) edge (d12) (d6) edge (d12);
\end{tikzpicture}
\qquad\qquad
\begin{tikzpicture}[hasse]
  \node (c1) at (0,0) {$1$};
  \node (c2) at (0,0.6) {$2$};
  \node (c3) at (0,1.2) {$3$};
  \node (c4) at (0,1.8) {$4$};
  \node (c5) at (0,2.4) {$5$};
  \node (c6) at (0,3) {$6$};
  \path (c1) edge (c2) (c2) edge (c3) (c3) edge (c4) (c4) edge (c5) (c5) edge (c6);
\end{tikzpicture}
\end{center}
```

Decide each sentence in each structure, with a witness or a failing pair:

::: {.enumerate options="label=(\roman*)"}
1. \( \exists x\, \forall y\, (x \le y) \);
2. \( \exists x\, \forall y\, (y \le x) \);
3. \( \forall x\, \forall y\, (x \le y \vee y \le x) \);
4. \( \forall x\, \forall y\, \exists z\, (x \le z \wedge y \le z) \).
:::

Which of them tell the two structures apart?
:::

::: {.solution}
*(i)* True in both: \( x = 1 \) in each, since \( 1 \) divides every element of \( D_1 \) and is the least element of \( \fM_2 \).

*(ii)* True in both: \( x = 12 \) in \( \fM_1 \), since every element of \( D_1 \) divides \( 12 \); \( x = 6 \) in \( \fM_2 \).

*(iii)* False in \( \fM_1 \), at \( x = 2 \), \( y = 3 \): neither divides the other. True in \( \fM_2 \): of two numbers, one is at most the other.

*(iv)* True in both: \( z = 12 \) in \( \fM_1 \), and \( z = 6 \) in \( \fM_2 \) (or \( z \) the larger of \( x \) and \( y \)).

Only (iii) separates them.

**Marking scheme.** (10 points)
- 8: 2 for each of (i)–(iv) in both structures, 1 for the verdicts and 1 for a named witness or failing pair for every verdict.
- 2: naming (iii) as the only separating sentence.
Fatal errors (0 for the part): a verdict on \( \fM_1 \) that reads \( \le \) as the usual order of numbers.
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

::: {#exr-structures-and-satisfaction-b3}
[B3: Is it a structure?]

For each description, say whether it is a structure for the symbols named. If not, name the clause of @def-structure that fails, and repair it with as small a change as you can.

::: {.enumerate options="label=(\roman*)"}
1. \( D = \nQ \), with a one-place function symbol \( f \) read as \( x \mapsto 1/x \) for \( x \ne 0 \) and \( f(0) = 0 \).
2. \( D = \nN \), with \( f \) read as \( x \mapsto x - 1 \).
3. \( D = \emptyset \), with \( P \) read as the empty set.
4. \( D = \nZ \), with a constant \( c \) naming \( \tfrac12 \).
5. \( D = \nR \), with a two-place predicate symbol \( R \) read as \( \{ (x, y) : y = \sqrt{x} \} \).
6. \( D = \nR \), with a one-place function symbol \( g \) read as \( x \mapsto \sqrt{x} \).
:::
:::

::: {.solution}
*(i)* Yes: every element has a value in \( \nQ \).

*(ii)* No: (M3) fails, since \( f(0) = -1 \notin \nN \). Repair: \( f(0) \coloneqq 0 \).

*(iii)* No: (M1) fails. Repair: any non-empty domain.

*(iv)* No: (M2) fails, since \( \tfrac12 \notin \nZ \). Repair: \( D = \nQ \), or let \( c \) name an integer.

*(v)* Yes: (M4) asks only for a set of pairs, and nothing requires a relation to hold for every first element.

*(vi)* No: (M3) fails, since \( \sqrt{-1} \) is not real. Repair: \( D = [0, \infty) \), or fix \( g(x) \coloneqq 0 \) for \( x < 0 \).

Descriptions (v) and (vi) carry the same information, and only the function symbol must be total.

**Marking scheme.** (10 points)
- 6: 1 for each verdict.
- 2: the clause named at each "no" (all four right).
- 2: repairs that are minimal and correct.
Fatal errors (0 for the part): calling (v) a non-structure because \( \sqrt{x} \) is undefined for \( x < 0 \).
:::

### C. Going deeper

::: {#exr-structures-and-satisfaction-c1}
[C1: Proofs by meaning]

::: {.enumerate options="label=(\alph*)"}
1. Prove \( \forall x\, (P(x) \wedge Q(x)) \models \forall x\, P(x) \wedge \forall x\, Q(x) \) clause by clause, as in @exm-clause-by-clause.
2. Prove \( \forall x\, (P(x) \vee Q(x)) \models \forall x\, P(x) \vee \exists x\, Q(x) \), condensed.
3. Prove \( \exists x\, (P(x) \to Q(c)) \models \forall x\, P(x) \to Q(c) \), condensed, and say where your proof uses the existential premise.
:::
:::

::: {.solution}
*(a)* Let \( \fM, \ell \models \forall x\, (P(x) \wedge Q(x)) \). By (S5) it suffices to show each conjunct. For \( \forall x\, P(x) \), let \( d \in D \) (S6). By (S6) for the premise, \( \fM, \ell[x \mapsto d] \models P(x) \wedge Q(x) \); by (S5), \( \fM, \ell[x \mapsto d] \models P(x) \). Since \( d \) was arbitrary, \( \fM, \ell \models \forall x\, P(x) \) (S6). Likewise \( \fM, \ell \models \forall x\, Q(x) \), with the other half of (S5).

*(b)* If \( P^{\fM} = D \), the left disjunct holds. Otherwise some \( d \in D \) is not in \( P^{\fM} \). The premise at \( d \) gives \( d \in P^{\fM} \) or \( d \in Q^{\fM} \), so \( d \in Q^{\fM} \), and \( \exists x\, Q(x) \) holds. Either way the disjunction holds.

*(c)* Let \( d \) be the premise's witness: if \( d \in P^{\fM} \), then \( c^{\fM} \in Q^{\fM} \). Suppose \( \forall x\, P(x) \) holds; then \( d \in P^{\fM} \), so \( Q(c) \) holds. The witness \( d \) is where the existential premise is used: the hypothesis \( \forall x\, P(x) \) is applied at it.

**Marking scheme.** (10 points)
- 4: (a), with every step's clause named, and (S6) used both to fix \( d \) and on the premise.
- 3: (b), split on whether \( P^{\fM} = D \) (or on a failing element), with the premise used at that element.
- 3: (c), fixing the witness first and applying the universal hypothesis at it.
Fatal errors (0 for the part): in (a), a proof that fixes \( d \) before taking the premise's (S6), so that \( d \) is not arbitrary.
:::

::: {#exr-structures-and-satisfaction-c2}
[C2: Challenge: only the symbols that occur matter]

Let \( \fM \) and \( \fN \) be structures with the same domain \( D \) that give the same meaning to every symbol occurring in a formula \( \varphi \). Prove that for every assignment \( \ell \), \( \fM, \ell \models \varphi \) if and only if \( \fN, \ell \models \varphi \). (This is the claim after @def-first-order-entailment that extra meanings change nothing.)
:::

::: {.solution}
[Hint 1]

Terms first, as in the proof of @lem-free-coincidence.
:::

::: {.solution}
[Hint 2]

Prove, by structural induction on \( \varphi \), the property: for **every** assignment \( \ell \), …; the quantifier case needs it at \( \ell[x \mapsto d] \).
:::

::: {.solution}
*Terms.* For every term \( t \) whose symbols \( \fM \) and \( \fN \) interpret alike, \( t^{\fM, \ell} = t^{\fN, \ell} \) for every \( \ell \), by structural induction on \( t \). For a variable \( x \), both values are \( \ell(x) \). For a constant \( c \), they are \( c^{\fM} = c^{\fN} \). For \( f(t_1, \dots, t_n) \), the hypothesis gives equal values of the \( t_i \), and \( f^{\fM} = f^{\fN} \) applied to equal tuples gives equal values.

*Formulas.* Let \( A(\varphi) \) be the property: *for every assignment \( \ell \), \( \fM, \ell \models \varphi \) if and only if \( \fN, \ell \models \varphi \)*, for formulas \( \varphi \) whose symbols \( \fM \) and \( \fN \) interpret alike. Atomic formulas: the tuples of values are equal by the claim for terms, and \( R^{\fM} = R^{\fN} \), so (S1) gives the same answer; equations likewise by (S2); \( \bot \) by (S3). Connectives: (S4) and (S5) combine equal answers into equal answers. For \( \forall x\, \varphi \): the two structures have the same domain, so \( d \) ranges over the same elements in both; for each \( d \), \( A(\varphi) \) at the assignment \( \ell[x \mapsto d] \) gives equal answers, and (S6) gives \( A(\forall x\, \varphi) \). For \( \exists x\, \varphi \), the same with (S7). Every clause of @def-first-order-formula has been covered, so \( A(\varphi) \) holds for every formula.

**Marking scheme.** (10 points)
- 2: the claim for terms, by induction.
- 2: the atomic cases, with (S1) and (S2).
- 2: the connective cases.
- 3: the quantifier case, using the property at the changed assignments and the shared domain.
- 1: naming where "same domain" is used.
Fatal errors (0 for the step): an induction hypothesis stated for one fixed \( \ell \) only.
:::

<!-- dependency ledger
def-structure (claim): D^n, subsets, ordered pairs and functions used in their everyday meaning | F2.1 (promised), prose pointer in the chapter index's Where this goes
def-structure (example): with = read as same parity on Z, -2 = 2 and P(2) hold and P(-2) fails | inline
def-structure (example): a sentence false in some structure is not derivable | the soundness statement of F1.6 §02 (not proved here; F1.6 §03)
def-assignment (claim): an assignment exists because D is non-empty (a constant assignment) | inline, from def-structure (M1)
def-assignment (claim): the value of a term is well defined by recursion on terms | thm-structural-recursion (pattern), def-term; F1.4 §02 says F1.3's induction and recursion carry over to terms and first-order formulas
def-assignment (example): values 2*2 + (-3) = 1, 2*2 + 1 = 5, -3, and 1 + 1 = 2 | inline; verify/ch07/def-satisfaction.py
def-satisfaction (claim): satisfaction is well defined by recursion on formulas, for all assignments at once | thm-structural-recursion applied to def-first-order-formula (F1.4 §02 remark)
def-satisfaction (example): traces of forall x exists y (x < y) in N and in {1,2,3}; forall y (x <= y) in N under l(x) = 0 and l(x) = 1; one-element domain | inline; verify/ch07/def-satisfaction.py
def-satisfaction (solution): every real square is >= 0; sqrt(d) exists for d >= 0; a product of non-negative reals is non-negative | school algebra; AN1.1 (thm-nth-root) proves the roots, prose only
def-satisfaction (solution): every complex number has a complex square root (polar form) | school algebra of complex numbers, stated in the solution; not proved before F4.1 (complex numbers)
lem-free-coincidence (proof): structural induction on terms and on first-order formulas | thm-structural-induction (pattern) with the clauses of def-term and def-first-order-formula; F1.4 §02 remark
lem-free-coincidence (proof): every variable of an atomic formula is free in it; the free variables of forall x phi are those of phi other than x | def-free-variable
lem-free-coincidence (proof): the cases not, or, ->, <-> repeat the conjunction argument with the other clauses | inline, as in lem-coincidence
def-first-order-entailment (claim): symbols a structure interprets but a formula does not contain never matter | inline, read off the clauses of def-satisfaction
def-first-order-entailment (example): forall x (P(x) -> Q(x)), P(c) |= Q(c) | inline from def-satisfaction
def-first-order-entailment (claim): forall x P(x) |= exists x P(x) in non-empty domains; it would fail for D empty | inline
def-first-order-entailment (claim): bounded quantifiers over the empty set, true and false | def-bounded-quantifier; inline
exr-models-a1 (solution): witnesses and failing elements in N, Z, Q; z = (d + e)/2 is rational and strictly between | inline; verify/ch07/exr-models-a1.py
exr-models-b2 (solution): the three-element model and the alternatives | verify/ch07/exr-models-b2.py
exr-models-a1 (solution): (e) sentence (b) true in N and false in Z, from the A1 table | inline; verify/ch07/exr-models-a1.py
exr-models-a1 (solution): (g) the element d comes from (S7) and serves for every e by (S6) | exm-clause-by-clause
def-structure (claim): Hasse convention: loops and the pairs implied by chaining lines upwards are understood | inline convention; partial orders defined in F1.6 §04
def-structure (example): Figure F's two structures and the Quick check (forall-exists true, exists-forall false) | verify/ch07/def-satisfaction.py
def-satisfaction (claim): satisfaction as a game between challenger and defender, one move per clause | informal reading of the clauses, as F1.4 §01's game; no proof rests on it
def-satisfaction (example): the game for exists y forall x (x <= y): challenger wins on N with e + 1, defender names 3 on {1,2,3} | inline; verify/ch07/def-satisfaction.py
lem-free-coincidence (example): the Quick check on l(y) and forall y (x <= y) in (N, <=) | lem-free-coincidence; the l(x) = 0 trace
exm-clause-by-clause (proof): each step licensed by the clause named; the two stacked changes at x and y commute | def-satisfaction, the paragraph after def-assignment; verify/ch07/exm-clause-by-clause.py
exm-clause-by-clause (claim): Section 5.6 derived the same sequent; the converse fails | prp-exists-forall-swap; F1.6 §02 (pointer)
exm-drinker-by-meaning (proof): case split on whether P^M = D; Case 1 uses the non-empty domain | def-structure (M1), def-satisfaction; verify/ch07/def-satisfaction.py
exm-drinker-by-meaning (claim): Section 6.3 derived it | exr-first-order-search-c1 (backward pointer to a used-later item; the proof stands alone)
exr-structures-and-satisfaction-a2 (solution): all twelve answers | verify/ch07/exr-structures-and-satisfaction-a2.py
exr-structures-and-satisfaction-b1 (solution): verdicts and witnesses in the divisors of 12 and the chain 1..6 | verify/ch07/exr-structures-and-satisfaction-b1.py
exr-structures-and-satisfaction-b3 (solution): the failing clauses and values (0 - 1, 1/2, sqrt(-1)) and the repairs | def-structure; verify/ch07/exr-structures-and-satisfaction-b3.py
exr-structures-and-satisfaction-c1 (solution): three entailments by meaning | def-satisfaction; verify/ch07/exr-structures-and-satisfaction-c1.py
exr-structures-and-satisfaction-c2 (solution): structures agreeing on the symbols of phi agree on phi | inline induction; it proves the claim after def-first-order-entailment, which no proof rests on
-->
