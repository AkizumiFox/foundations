# Predicates and Quantifiers

Chapters 1–3 built a complete account of the connectives: rules for using and proving "and", "or", "implies", and "not", a meaning for every formula through truth tables, and the theorems that the rules prove exactly what the tables say. In all of that, an atomic statement was a closed box. The statements of analysis are not boxes. "For every \( \varepsilon > 0 \) there is an \( N \) such that …" has its whole content inside, in the words "for every" and "there is" and in the letters they govern. This section opens the box. It introduces predicates, variables, the domain a statement talks about, and the two quantifiers \( \forall \) and \( \exists \), and it teaches how to **read** a quantified sentence. It proves no theorem and states no rule: the four quantifier rules come one per section, in Sections 4.3 to 4.6.

## An argument the truth table rejects

Here is an argument that nobody would doubt.

> Every positive real number has a square root. The number \( 2 \) is positive. Therefore \( 2 \) has a square root.

It is correct in the plainest sense: if the two premises are true, the conclusion must be. Now try to check it with the tools of Chapters 1–3. The three sentences contain no connective at all, so each is atomic. Give them atoms:

- \( p \): "every positive real number has a square root";
- \( q \): "\( 2 \) is positive";
- \( r \): "\( 2 \) has a square root".

The argument has the form \( p, q \therefore r \). Three different atoms, and nothing connects them. The valuation that makes \( p \) and \( q \) true and \( r \) false makes both premises true and the conclusion false. So by @cor-refuting-row,
\[
p, \ q \nvdash r .
\]
No derivation, with any rule of Chapters 1 and 2, leads from \( p \) and \( q \) to \( r \).

There is no contradiction here, and it is worth seeing exactly why. @cor-refuting-row is about the **form** \( p, q \therefore r \): it says that no derivation leads from two arbitrary statements to a third, unrelated one. That is true. Our argument is correct for a reason that the form cannot see. The first premise speaks about **every** positive real number. The second says that \( 2 \) is **one** of the things the first premise speaks about. The conclusion says of \( 2 \) what the first premise said of all of them. The three statements share parts: a property ("is positive"), another property ("has a square root"), an object (\( 2 \)), and the word "every". Chopped into atoms, the shared parts disappear.

This is the warning of Section 3.3 come true: a truth table sees only the connectives, and everything inside an atom is invisible to it. Section 3.3 ended that warning with the remark that this chapter looks inside atoms. We now do. The first job is a vocabulary for the parts inside: the properties, the objects, and the words "every" and "some". Section 4.3 then gives the rule that makes the argument above a derivation, four lines long.

## Predicates: statements with holes

Chapter 1 met the sentence "\( x > 2 \)" and called it an **open sentence** (item (e) of @exm-statements). It is not a statement, because its truth depends on what \( x \) is: it is true when \( x \) is \( 3 \) and false when \( x \) is \( 0 \). Put a number in for \( x \) and it becomes a statement.

The argument of the last subsection is built from two open sentences of this kind: "\( x \) is positive" and "\( x \) has a square root". Each has one hole, marked by \( x \). The premise "\( 2 \) is positive" is the first open sentence with \( 2 \) put into the hole; the conclusion is the second, with \( 2 \) put into its hole. The first premise does something else with the holes, which we come to in the next subsection. Open sentences are the missing parts, and they deserve a name.

*A predicate is a statement with holes in it; filling every hole with a name of an object gives a statement.*

A **predicate** is an open sentence with one or more marked holes. The number of holes is its **arity**: a predicate with one hole is **one-place** (or unary), with two holes **two-place** (binary), and so on. We write a predicate as a capital letter followed by its holes in parentheses: \( P(x) \) for "\( x \) is positive", \( S(x) \) for "\( x \) has a square root", \( D(x, y) \) for "\( x \) divides \( y \)". The letters that mark the holes are **variables**: \( x, y, z, u \), and in analysis also \( \varepsilon, \delta, N, n \), and for primes and other natural numbers \( p, q \). A **constant** is a name of one particular object: \( 0 \), \( 1 \), \( 2 \), or a letter \( a, b, c \) that has been given a fixed meaning.

In words: a predicate says something **about** objects without saying which objects. The variables are placeholders, not objects. "\( x \) is positive" is about whatever will be put in for \( x \), and until something is, it is neither true nor false.

Many predicates of mathematics are written with a symbol between their two holes rather than a letter in front: \( x < y \), \( x \le y \), \( x = y \), \( x \mid y \). These are two-place predicates like any other; only the way of writing them differs. Membership \( x \in A \), for a fixed set \( A \), is a one-place predicate of \( x \): "\( x \) is an element of \( A \)". Chapter 6 develops sets and membership properly. Until then a set is understood informally, as a collection of objects (usually numbers), and nothing in this section uses more about a set \( A \) than whether a given object is an element of it. For sets \( A \) and \( B \), \( A \subseteq B \) means that every element of \( A \) is an element of \( B \); so \( A \subseteq \nR \) says that \( A \) is a set of real numbers.

Objects can also be built from other objects: \( x + 1 \), \( x^2 \), \( \abs{x} \), \( 2 \cdot y \). The symbols that build them (\( + \), squaring, \( \abs{\cdot} \), \( \cdot \)) are **function symbols**, and an expression such as \( x^2 + 1 \) names an object as soon as \( x \) does. A function symbol may also be a letter, \( f(x) \). Chapter 6 defines functions as sets of pairs; here a function symbol is simply a way of naming one object in terms of others. Section 4.2 makes all of this exact, under the name **term**. For now, a term is any expression that names an object: a variable, a constant, or a function symbol applied to terms.

Filling holes is the first way to turn a predicate into a statement.

- \( P(2) \): "\( 2 \) is positive". A statement, and true.
- \( P(-3) \): "\( -3 \) is positive". A statement, and false.
- \( D(3, 12) \): "\( 3 \) divides \( 12 \)". True.
- \( D(3, y) \): "\( 3 \) divides \( y \)". Still open: one hole is filled and one is not. It is a one-place predicate of \( y \).
- \( P(x^2 + 1) \): "\( x^2 + 1 \) is positive". Still open, in \( x \). (It happens to be true whatever real number \( x \) is, but that is a fact about the numbers, and the sentence still has a hole.)

The last two items show that filling holes is not all or nothing. A predicate with some holes filled is a predicate with fewer holes. Only when **every** hole is filled, or closed in the way described next, do we have a statement.

::: {.remark}
A clash of letters to keep apart. In Chapters 1 and 2, capital letters \( P, Q, R \) stood for whole statements, and Chapter 3 read them as atoms or as arbitrary formulas. In this chapter \( P, Q, R \) are **predicate symbols**, followed by their holes: \( P(x) \), \( R(x, y) \). A bare \( P \) or \( Q \) in this chapter, in a reference back to Chapters 1–3 or in a review exercise, is a statement letter as before. The parentheses tell the two uses apart. The small letters \( p, q, r \) were atoms in the argument that opened this section, which was written in the language of Chapter 3, and they are atoms again wherever a later section reads a formula with a truth table (Section 4.11). A formula of this chapter has no atoms (Section 4.2 replaces them by predicates with their holes), so inside one, \( p \) and \( q \) are variables, used for primes and other natural numbers. A property \( P(n) \) of natural numbers, as in the principle of induction (@ax-induction), was already a one-place predicate in this sense.
:::

## Quantifiers and the domain

There is a second way to turn "\( x \) is positive" into a statement, and the first premise of our argument uses it. The premise does not put a particular number into the hole of "\( x \) has a square root". It says that the open sentence "if \( x \) is positive, then \( x \) has a square root" is true **whatever** real number is put in. The word "every" closes the hole without filling it.

Two questions have to be answered before "whatever is put in" makes sense. What may be put in? And how many of those things must make the sentence true?

The first question is answered by a **domain of discourse**, or **domain**: the collection of objects that the variables range over. For the argument above, the domain is the real numbers, \( \nR \). In number theory it is often \( \nZ \) or \( \nN \) (in this book \( \nN = \{0, 1, 2, \dots\} \), with \( 0 \)). A domain always has at least one element; Section 4.11 explains why the book insists on this, and how it handles the empty set instead.

The second question is answered by the **quantifier**.

*"For every" promises something of each object in the domain; "there exists" promises it of at least one.*

Let \( \varphi \) be an open sentence in which the variable \( x \) marks a hole (it may have other holes too). There are two quantifiers.

- The **universal quantifier**: \( \forall x\, \varphi \), read "**for every** \( x \), \( \varphi \)", "for all \( x \), \( \varphi \)", or "for each \( x \), \( \varphi \)". It is **true** when **every** element of the domain, put in for \( x \), makes \( \varphi \) true.
- The **existential quantifier**: \( \exists x\, \varphi \), read "**there exists** an \( x \) such that \( \varphi \)", "there is an \( x \) with \( \varphi \)", or "for **some** \( x \), \( \varphi \)". It is **true** when **at least one** element of the domain, put in for \( x \), makes \( \varphi \) true.

In words: \( \forall x \) and \( \exists x \) each close the hole marked \( x \), so they remove \( x \) from the list of holes. \( \forall x\, \varphi \) makes one claim about the whole domain at once: no element is an exception. \( \exists x\, \varphi \) claims that there is at least one element for which \( \varphi \) holds, and it does not say which, or how many. "At least one" includes the case of exactly one and the case of all of them. The word "some" in mathematics never means "some but not all".

With these, the first premise of our argument, over the domain \( \nR \), is
\[
\forall x\, \bigl( P(x) \to S(x) \bigr),
\]
"for every \( x \), if \( x \) is positive, then \( x \) has a square root". The second premise is \( P(2) \) and the conclusion is \( S(2) \). Now the shared parts are visible: \( P \) occurs in both premises, \( S \) in the first premise and the conclusion, and \( 2 \) in the second premise and the conclusion. The rule of Section 4.3 uses the first premise with \( x \) replaced by \( 2 \), giving \( P(2) \to S(2) \), and \( \rulename{{\to}E} \) finishes.

Notice the \( \to \) inside the quantifier. The premise does not say that every real number is positive and has a square root; it says that every real number which is positive has one. The subsection on bounded quantifiers below explains why a "for every" restricted to part of the domain always comes with an implication.

::: {.remark}
"True" in this section, and up to Section 4.11, means what it means in ordinary mathematics: we look at the domain and ask whether every element, or some element, makes the sentence true. Section 4.11 turns this reading into a definition, with models. Until then the reading is used only to understand sentences and to decide whether they are true as statements about numbers. Every claim that a sentence can be **derived** from others will be proved by writing a derivation, never by this reading.
:::

### The same sentence over different domains

A quantified sentence is a claim about its domain, so changing the domain can change its truth value. Two examples show how.

Take \( \forall x\, (x \ge 0) \), "every \( x \) is at least \( 0 \)".

- Over \( \nN \) it is **true**: every natural number is at least \( 0 \).
- Over \( \nZ \) it is **false**: the integer \( -1 \) is in the domain, and \( -1 \ge 0 \) is false.

One element of the domain that makes \( \varphi \) false is enough to make \( \forall x\, \varphi \) false. Such an element is a **counterexample**. To show that the sentence is true over \( \nN \), on the other hand, we had to say something about every natural number at once.

Take \( \exists x\, (x^2 = 2) \), "some \( x \) has square \( 2 \)".

- Over \( \nR \) it is **true**: the real number \( \sqrt{2} \) has square \( 2 \). (Its existence is a school fact here; Chapter 11 proves it from the axioms of the real numbers.)
- Over \( \nQ \) it is **false**: that no rational number has square \( 2 \) is exactly @thm-sqrt2-irrational.

One element that makes \( \varphi \) true is enough to make \( \exists x\, \varphi \) true. Such an element is a **witness**. To show that the sentence is false over \( \nQ \), on the other hand, a theorem about every rational number was needed, and Chapter 2 proved it by contradiction.

The two quantifiers are mirror images. For \( \forall \), a single counterexample refutes and a general argument confirms. For \( \exists \), a single witness confirms and a general argument refutes. Section 4.9 makes the mirror exact: "not every \( x \) satisfies \( \varphi \)" says the same as "some \( x \) fails \( \varphi \)".

::: {.check}
Over which of the domains \( \nZ_{>0} = \{1, 2, 3, \dots\} \), \( \nZ \), \( \nR \) is the sentence \( \exists x\, (x + x = x) \) true? Give a witness where it is true, and a reason where it is false.
:::

::: {.solution}
Only \( x = 0 \) satisfies \( x + x = x \), since subtracting \( x \) from both sides gives \( x = 0 \). So the sentence is true over \( \nZ \) and over \( \nR \), with the witness \( 0 \). It is false over \( \nZ_{>0} \), which does not contain \( 0 \): every \( n \in \nZ_{>0} \) has \( n + n > n \), since \( n > 0 \). (Over \( \nN = \{0, 1, 2, \dots\} \) it would be true, again with the witness \( 0 \).)
:::

### Reading a quantified sentence

Quantified sentences are read from the outside in: the first quantifier governs everything after it, and inside it may sit another quantifier, a connective, or a predicate. Reading aloud slowly, one symbol at a time, is the most reliable way to understand one. Here are three, simplest first.

::: {#exm-reading-quantified-sentences}
[Reading three sentences]

Read each sentence aloud, say what it claims, and decide whether it is true over the domain given.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, (x^2 \ge 0) \), over \( \nR \).
2. \( \exists x\, \forall y\, (x \le y) \), over \( \nN \).
3. \( \neg\exists p\, \bigl( \mathrm{Prime}(p) \wedge \forall q\, (\mathrm{Prime}(q) \to q \le p) \bigr) \), over \( \nN \), where \( \mathrm{Prime}(p) \) is the one-place predicate "\( p \) is prime".
:::
:::

::: {.solution}
*(a)* "For every \( x \), \( x^2 \) is at least \( 0 \)." The claim is about every real number, and it is true: the square of a real number is never negative (a school fact about signs: \( x \cdot x \) is a product of two numbers of the same sign, or \( 0 \)).

*(b)* "There is an \( x \) such that for every \( y \), \( x \le y \)." Unpack from the outside. The outer quantifier \( \exists x \) asks for one natural number \( x \). What must be true of it is the inside, \( \forall y\, (x \le y) \): every natural number \( y \) is at least \( x \). So the sentence says that \( \nN \) has a **least element**. It is true, with the witness \( x = 0 \): every natural number is at least \( 0 \).

*(c)* The outer symbol is \( \neg \), so the sentence denies what follows. What follows is \( \exists p\, (\dots) \): there is a \( p \) that is prime and such that every prime \( q \) is at most \( p \). Such a \( p \) would be a **largest prime**. So the sentence says "there is no largest prime". It is true: this is the ancient theorem that there are infinitely many primes. Nothing in this book depends on that theorem; here it is only something to read.

Notice the shape inside (c): \( \forall q\, (\mathrm{Prime}(q) \to q \le p) \), "every prime is at most \( p \)", has an implication under the \( \forall \). It speaks about primes only, and the implication is how a "for every" is restricted to them. The next subsection makes this a rule of writing.
:::

The sentence in (b) has two quantifiers, and they come in a definite order: first \( \exists x \), then \( \forall y \). The order matters, and the subsection "The order of quantifiers" below is about it. First, restricted quantifiers.

## Bounded quantifiers

Mathematics rarely says "for every real number". It says "for every \( \varepsilon > 0 \)", "for every \( x \in A \)", "there is an \( n \ge N \)". The quantifier ranges over a **part** of the domain, described by a condition. There is no new quantifier for this; the condition is written into the sentence with a connective. Which connective turns out to matter.

*A "for every" restricted to a condition is an implication; a "there exists" restricted to a condition is a conjunction.*

::: {#def-bounded-quantifier}
[Bounded Quantifier]

Let \( A \) be a set, \( x \) a variable, and \( \varphi \) an open sentence. The **bounded quantifiers** are the abbreviations
\[
\begin{aligned}
\forall x \in A \; \varphi \quad &\text{stands for} \quad \forall x\, (x \in A \to \varphi), \\
\exists x \in A \; \varphi \quad &\text{stands for} \quad \exists x\, (x \in A \wedge \varphi).
\end{aligned}
\]
In the same way, for a term \( a \) in which \( x \) does not occur, \( \forall x > a \; \varphi \) stands for \( \forall x\, (x > a \to \varphi) \) and \( \exists x > a \; \varphi \) for \( \exists x\, (x > a \wedge \varphi) \), and likewise with \( \ge \), \( < \), \( \le \) in place of \( > \).
:::

In words: "for every \( x \) in \( A \), \( \varphi \)" means "for every \( x \) whatsoever, **if** \( x \) is in \( A \), **then** \( \varphi \)". "There is an \( x \) in \( A \) with \( \varphi \)" means "there is an \( x \) that is in \( A \) **and** satisfies \( \varphi \)". The condition \( x \in A \), or \( x > a \), is the **bound**. A bounded quantifier is not a new symbol of the language: it is shorthand, and every statement about it is a statement about the formula it stands for.

The display after @ax-induction, in Section 3.2, used \( \forall n \in \nN \) as an abbreviation of the words "for every natural number \( n \)". It was already this bounded form: \( \forall n \in \nN\; \bigl( P(n) \to P(n + 1) \bigr) \) stands for \( \forall n\, \bigl( n \in \nN \to (P(n) \to P(n + 1)) \bigr) \).

**Why \( \to \) under \( \forall \), and \( \wedge \) under \( \exists \).** Try the other choices and see what they say. Take the domain \( \nR \), the set \( A = \{1, 2\} \), and the open sentence \( x > 5 \).

- "Every element of \( A \) is greater than \( 5 \)" is false: \( 1 \) is not. The correct form \( \forall x\, (x \in A \to x > 5) \) is false too, with the counterexample \( x = 1 \), which is in \( A \) and not greater than \( 5 \). The wrong form \( \forall x\, (x \in A \wedge x > 5) \) says that **every real number** is in \( A \) and greater than \( 5 \). It is false as well, but for a reason that has nothing to do with \( A \)'s elements: \( x = 0 \) is not in \( A \). Change \( A \) to \( \{6, 7\} \) and the correct form becomes true while the wrong one stays false.
- "Some element of \( A \) is greater than \( 5 \)" is false for \( A = \{1, 2\} \). The correct form \( \exists x\, (x \in A \wedge x > 5) \) is false too: no real number is both in \( A \) and greater than \( 5 \). The wrong form \( \exists x\, (x \in A \to x > 5) \) is **true**, with the witness \( x = 0 \): since \( 0 \notin A \), the implication "if \( 0 \in A \) then \( 0 > 5 \)" has a false hypothesis and is true (vacuous truth, the phenomenon behind @prp-vacuous-implication).

So a \( \forall \) with \( \wedge \) inside claims too much: it says the whole domain lies in \( A \). An \( \exists \) with \( \to \) inside claims too little: anything outside \( A \) is a witness. Neither says what was meant.

::: {.warning}
An existential quantifier with an implication directly inside, \( \exists x\, (\alpha \to \beta) \), is almost always a mistranslation. Over \( \nR \), "some element of \( \{1, 2\} \) exceeds \( 5 \)" is false, but \( \exists x\, (x \in \{1, 2\} \to x > 5) \) is true, because \( x = 0 \) makes the hypothesis false. When you write \( \exists \) and then \( \to \), check whether you meant \( \wedge \).
:::

**One domain per formula.** The logic of this book has a single domain for all the variables of a formula. Mathematics often mixes kinds of objects in one sentence: in "for every \( \varepsilon > 0 \) there is an \( N \in \nN \) such that for every \( n \ge N \), …", the letter \( \varepsilon \) is a real number, while \( N \) and \( n \) are natural numbers. The convention is: **the domain is the larger kind** (here \( \nR \)), and **the smaller kind enters as a bound** (\( \exists N \in \nN \), \( \forall n \in \nN \)). So the sentence begins
\[
\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; \bigl( n \ge N \to \dots \bigr),
\]
and \( n \) ranges over real numbers that happen to be required, by the bound, to be natural numbers. A sequence \( (a_n) \) becomes a function symbol \( a \), with \( a(n) \), written \( a_n \), the \( n \)-th term. Its values at real numbers that are not natural numbers are never used, because \( a \) is only ever applied to variables bounded by \( n \in \nN \). We state this convention once, here; every translation in this chapter follows it.

**The empty set.** Bounded quantifiers make sense even when the bound is never satisfied. Let \( \emptyset \) be the **empty set**, the set with no elements (Chapter 6 introduces it properly), so that \( x \in \emptyset \) is false for every \( x \).

- \( \forall x \in \emptyset \; \varphi \) stands for \( \forall x\, (x \in \emptyset \to \varphi) \). For every \( x \), the hypothesis \( x \in \emptyset \) is false, so the implication is true. The sentence is **true**, whatever \( \varphi \) says. For example, "every element of \( \emptyset \) is greater than \( 5 \)" and "every element of \( \emptyset \) is less than \( 5 \)" are both true.
- \( \exists x \in \emptyset \; \varphi \) stands for \( \exists x\, (x \in \emptyset \wedge \varphi) \). No \( x \) makes the first conjunct true, so the sentence is **false**, whatever \( \varphi \) says.

Section 2.1 met this phenomenon for implications: a statement whose hypothesis never holds is true, and says nothing. A universal statement about the elements of an empty set is true for the same reason, because there is nothing to test. This is the reading; Section 4.4 derives the universal half with the rules.

::: {.warning}
"Every element of \( A \) has property \( \varphi \)" does **not** imply "some element of \( A \) has property \( \varphi \)". It fails when \( A \) is empty: "every element of \( \emptyset \) is greater than \( 5 \)" is true, and "some element of \( \emptyset \) is greater than \( 5 \)" is false. The step from "every" to "some" needs an element, and the bound can remove all of them.
:::

## The order of quantifiers

A sentence with two quantifiers of different kinds can change its meaning completely when they are swapped. This is the single most important fact about reading quantifiers, and the definitions of analysis depend on it.

::: {#exm-quantifier-order-sum}
[Swapping two quantifiers]

Over the domain \( \nR \), compare
\[
\text{(i)} \ \ \forall x\, \exists y\, (x + y = 0)
\qquad \text{and} \qquad
\text{(ii)} \ \ \exists y\, \forall x\, (x + y = 0) .
\]
Read each aloud, and decide which is true.
:::

::: {.solution}
*(i)* "For every \( x \) there is a \( y \) with \( x + y = 0 \)": every real number has an additive inverse. It is **true**. Given any real \( x \), the number \( y = -x \) satisfies \( x + y = x + (-x) = 0 \).

*(ii)* "There is a \( y \) such that for every \( x \), \( x + y = 0 \)": one single number \( y \) is an inverse of every real number at once. It is **false**. Whatever real number \( y \) is proposed, take \( x = 1 - y \); then \( x + y = 1 \ne 0 \). So no \( y \) works.

The two sentences have the same letters, the same quantifiers and the same equation. Only the order differs. In (i), the \( y \) may be chosen **after** \( x \) is known, so it may depend on \( x \): the witness \( -x \) is a different number for each \( x \). In (ii), \( y \) must be chosen **first**, once and for all, and then it must work for every \( x \) that comes after.

What makes the pair work as an example? Two properties, and any other pair with the same shape would do as well. First, for each \( x \) separately there is a suitable \( y \). Second, no one \( y \) is suitable for all \( x \) together, because each \( y \) serves only one \( x \) (here, only \( x = -y \)).
:::

**Quantifiers as a game.** The difference in @exm-quantifier-order-sum can be felt by reading a sentence as a game between two players. The reading applies to a sentence whose quantifiers all stand at the front, unnegated, followed by an inside with no quantifiers, as in (i) and (ii); a bounded quantifier such as \( \forall \varepsilon > 0 \) counts, its bound being checked with the inside. The **challenger** chooses a value for each \( \forall \) variable and tries to make the sentence false. The **defender** chooses a value for each \( \exists \) variable and tries to make it true. They move in the order in which the quantifiers are written, left to right, and each player sees every move made so far. When all variables have values, the inside is checked. The sentence is true exactly when the defender has a way of playing that wins against every choice of the challenger. A quantifier under a \( \neg \), or in the hypothesis of an implication, changes sides: \( \neg \forall x\, \varphi \) is played as \( \exists x\, \neg \varphi \), with the defender moving. Section 4.9 proves the laws that push a \( \neg \) inward in this way.

- In (i), the challenger moves first and picks some \( x \). The defender sees \( x \) and answers \( y = -x \). The defender always wins.
- In (ii), the defender moves first and must commit to some \( y \) without knowing \( x \). The challenger sees \( y \) and answers \( x = 1 - y \). The challenger always wins.

*Read the dependency off the order: a variable may depend on the variables quantified to its left, and only on them.* In (i), \( y \) is to the right of \( x \), so the choice of \( y \) may use \( x \). In (ii), \( y \) is to the left, so it may not. Sections 4.4 to 4.6 will show this same dependence as a fact about the boxes of a derivation, and Section 4.10 shows that it is the whole difference between continuity and uniform continuity.

**When swapping is harmless.** Two quantifiers of the **same** kind may be swapped. \( \forall x\, \forall y\, \varphi \) and \( \forall y\, \forall x\, \varphi \) both say that \( \varphi \) holds for every choice of the pair; in the game, the challenger makes both moves, and the order of the challenger's own moves gives nothing away. Likewise \( \exists x\, \exists y\, \varphi \) and \( \exists y\, \exists x\, \varphi \) both say that some pair works. Section 4.4 derives the first swap with the rules. For quantifiers of **different** kinds, one direction is always safe: if one \( y \) works for every \( x \), then for every \( x \) some \( y \) works (the same one). Section 4.6 derives this, \( \exists y\, \forall x\, \varphi \) to \( \forall x\, \exists y\, \varphi \), and @exm-quantifier-order-sum shows that the other direction fails.

::: {.check}
Over the domain \( \nN \), swap the two quantifiers in "for every \( n \) there is a prime larger than \( n \)", that is, in \( \forall n\, \exists p\, \bigl( \mathrm{Prime}(p) \wedge p > n \bigr) \). Read the result aloud. Is it true?
:::

::: {.solution}
The swapped sentence is \( \exists p\, \forall n\, \bigl( \mathrm{Prime}(p) \wedge p > n \bigr) \): "there is a prime that is larger than every natural number". It is **false**. Whatever \( p \) is proposed, take \( n = p \): then \( p > n \) is false, so the inside fails. (The original sentence is true; it is another form of the theorem that there are infinitely many primes, which we do not use.) As in @exm-quantifier-order-sum, the original lets the prime depend on \( n \), and the swapped sentence demands one prime for all \( n \) at once.
:::

## Words that hide quantifiers

English marks quantifiers loosely, and mathematical English has habits that hide them altogether. Three traps are worth naming now, before they cause trouble in a translation.

::: {.warning}
The word **"any"** can mean "every" or "some", and only the sentence around it decides. "Any \( x \) in \( A \) is positive" means every element of \( A \) is positive: \( \forall x \in A\; (x > 0) \). "If any \( x \) in \( A \) is positive, then \( A \) is nonempty" means if **some** element is positive: \( \exists x \in A\; (x > 0) \to \dots \). When you meet "any", rewrite the sentence with "every" and with "some", and keep the one that says what was meant.
:::

**Hidden universal quantifiers.** A theorem stated as "if \( n \) is even, then \( n^2 \) is even" has no quantifier word in it, and yet it is not about one number. It means: for every integer \( n \), if \( n \) is even, then \( n^2 \) is even. A letter that is not introduced anywhere, in the statement of a theorem, is read with a "for every" in front. Chapter 5 names this convention and lists the others that written mathematics relies on. When translating, put the hidden quantifier back first.

**An implication inside \( \exists \).** This is the warning after @def-bounded-quantifier, and it deserves repeating because it comes up in translations of analysis: "there is an \( N \) such that, if \( n \ge N \), then …" is not the shape of the sentence displayed under **One domain per formula** above, where the implication \( n \ge N \to \dots \) sits under \( \forall n \in \nN \). The implication belongs under a \( \forall \): "there is an \( N \) such that **for every** \( n \), if \( n \ge N \), then …".

## What comes next

We can now read quantified sentences and decide, as mathematicians, whether they are true. We cannot yet **reason** with them in the sense of Chapters 1 and 2: there is no rule for using a "for every", for proving one, for proving a "there exists", or for using one. Section 4.2 first makes the language exact, because the rules will need to say precisely what "put \( 2 \) in for \( x \)" means. Sections 4.3 to 4.6 then give the four rules, one per section, in the same way as Chapters 1 and 2 gave the rules for the connectives.

## Exercises

### A. Check your understanding

::: {#exr-predicates-and-quantifiers-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Read each sentence aloud, and say over which of the domains \( \nN \), \( \nZ \), \( \nR \) it is true: (i) \( \forall x\, (x + 1 > x) \); (ii) \( \exists x\, (x + 1 = 0) \); (iii) \( \forall x\, \exists y\, (y < x) \); (iv) \( \exists x\, (2 \cdot x = 1) \); (v) \( \forall x\, (x \cdot x \ge x) \).
2. With domain \( \nR \), which of the following translates "some element of \( A \) is negative"? (i) \( \exists x\, (x \in A \to x < 0) \); (ii) \( \exists x\, (x \in A \wedge x < 0) \); (iii) \( \forall x\, (x \in A \wedge x < 0) \). For each of the two others, say what it claims instead.
3. What is the arity of the predicate "\( x + y = z \)", and how many holes does "\( 3 + y = z \)" have left?
4. True or false, with a reason: \( \forall x \in \emptyset \; (x \ne x) \) is true.
:::
:::

::: {.solution}
*(a)* (i) "For every \( x \), \( x + 1 \) is greater than \( x \)." True over all three domains: adding \( 1 \) always gives a larger number.

(ii) "There is an \( x \) with \( x + 1 = 0 \)." The only solution is \( x = -1 \). False over \( \nN \), which does not contain \( -1 \); true over \( \nZ \) and \( \nR \), with the witness \( -1 \).

(iii) "For every \( x \) there is a \( y \) smaller than \( x \)." False over \( \nN \): for \( x = 0 \) there is no natural number \( y < 0 \). True over \( \nZ \) and \( \nR \): given \( x \), take \( y = x - 1 \).

(iv) "There is an \( x \) with \( 2x = 1 \)." The only solution is \( x = \frac{1}{2} \). False over \( \nN \) and \( \nZ \), true over \( \nR \) with the witness \( \frac{1}{2} \).

(v) "For every \( x \), \( x \cdot x \) is at least \( x \)." True over \( \nN \): if \( x = 0 \), then \( x \cdot x = 0 = x \); if \( x \ge 1 \), then \( x \cdot x \ge 1 \cdot x = x \). True over \( \nZ \): an integer is either at least \( 1 \), as before, or at most \( 0 \), and then \( x \cdot x \ge 0 \ge x \). False over \( \nR \): the counterexample \( x = \frac{1}{2} \) has \( x \cdot x = \frac{1}{4} < \frac{1}{2} \).

*(b)* (ii) is the translation (@def-bounded-quantifier: \( \wedge \) under \( \exists \)). (i) is true as soon as some real number lies outside \( A \), since that number makes the implication vacuously true; so it can be true when no element of \( A \) is negative (for \( A = \{1\} \), say). (iii) claims that every real number is in \( A \) and negative, which is false whatever \( A \) is (take \( x = 0 \)).

*(c)* It has three holes, \( x \), \( y \), \( z \), so it is three-place. Filling \( x \) with \( 3 \) leaves two holes, \( y \) and \( z \).

*(d)* True. It stands for \( \forall x\, (x \in \emptyset \to x \ne x) \). For every \( x \) the hypothesis \( x \in \emptyset \) is false, so the implication is true, even though its conclusion \( x \ne x \) is false for every \( x \).
:::

### B. Practice

::: {#exr-predicates-and-quantifiers-b1}
[B1: Ordered quantifiers]

Determine which of the following sentences are true over the domain given. Justify your answer: give the witness a true \( \exists \) asks for (as a function of the earlier variables, if there are any), or the counterexample that refutes a \( \forall \).

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, \exists y\, (x < y) \), over \( \nN \).
2. \( \forall x\, \exists y\, (x + y = 1) \), over \( \nN \).
3. \( \exists x\, \forall y\, (x \cdot y = y) \), over \( \nR \).
4. \( \forall x\, \exists y\, (y \cdot y = x) \), over \( \nR \).
:::
:::

::: {.solution}
*(a)* True. Given any natural number \( x \), the natural number \( y = x + 1 \) satisfies \( x < y \). The witness depends on \( x \), which the order \( \forall x\, \exists y \) allows.

*(b)* False. The challenger chooses \( x = 2 \). Then \( x + y = 1 \) forces \( y = -1 \), which is not a natural number; every natural \( y \) gives \( 2 + y \ge 2 \). So for \( x = 2 \) no \( y \) works. (For \( x = 0 \) and \( x = 1 \) the witnesses \( y = 1 \) and \( y = 0 \) do exist, so the challenger must choose with care.) (Over \( \nZ \) the sentence would be true, with \( y = 1 - x \).)

*(c)* True, with the witness \( x = 1 \): for every real \( y \), \( 1 \cdot y = y \). The witness is chosen first and does not depend on \( y \), as the order \( \exists x\, \forall y \) demands.

*(d)* False, with the counterexample \( x = -1 \): for every real \( y \), \( y \cdot y \ge 0 > -1 \), so no \( y \) has \( y \cdot y = -1 \).
:::

::: {#exr-predicates-and-quantifiers-b2}
[B2: Order matters]

Give an example of a two-place predicate \( R(x, y) \) on the domain \( \nN \) such that \( \forall x\, \exists y\, R(x, y) \) is true and \( \exists y\, \forall x\, R(x, y) \) is false. Check both claims.
:::

::: {.solution}
Take \( R(x, y) \): "\( y > x \)".

*\( \forall x\, \exists y\, (y > x) \) is true.* Given any natural number \( x \), the natural number \( y = x + 1 \) satisfies \( y > x \).

*\( \exists y\, \forall x\, (y > x) \) is false.* Whatever natural number \( y \) is proposed, take \( x = y \): then \( y > x \) is false. So no \( y \) is greater than every \( x \).

Any answer must have two properties, and a different answer can be checked against them.

1. **Every \( x \) has a partner:** for each \( x \in \nN \) there is at least one \( y \) with \( R(x, y) \).
2. **No \( y \) is a partner of every \( x \):** for each \( y \in \nN \) there is at least one \( x \) with \( R(x, y) \) false.

For example, "\( y \ne x \)" also works: each \( x \) has the partner \( x + 1 \), and each \( y \) fails to be a partner of \( x = y \). So does "\( y \ge x \)": each \( x \) is its own partner, and each \( y \) fails to be a partner of \( x = y + 1 \). A predicate that does **not** work is "\( y \ge 1 \)": property 1 holds, but property 2 fails, because \( y = 1 \) is a partner of every \( x \), so \( \exists y\, \forall x\, (y \ge 1) \) is true.
:::

### C. Going deeper

::: {#exr-predicates-and-quantifiers-c1}
[C1: A least element]

Decide whether \( \exists x\, \forall y\, (x \le y) \) is true over each of the domains \( \nN \), \( \nZ \), \( [0, 1] \) and \( (0, 1] \). Give the witness where it is true, and where it is false show that every proposed \( x \) is defeated by some \( y \).
:::

::: {.solution}
The sentence says that the domain has a **least element**: one \( x \) that is at most every element \( y \).

*Over \( \nN \): true*, with the witness \( x = 0 \). Every natural number \( y \) satisfies \( 0 \le y \).

*Over \( \nZ \): false.* Let \( x \) be any integer. The integer \( y = x - 1 \) satisfies \( y < x \), so \( x \le y \) fails. No integer is least.

*Over \( [0, 1] \): true*, with the witness \( x = 0 \). Every \( y \in [0, 1] \) satisfies \( 0 \le y \), by the definition of the interval.

*Over \( (0, 1] \): false.* Let \( x \in (0, 1] \), so \( 0 < x \le 1 \). The number \( y = \frac{x}{2} \) satisfies \( 0 < \frac{x}{2} < x \le 1 \), so \( y \in (0, 1] \) and \( y < x \); hence \( x \le y \) fails. The defeating \( y \) depends on the proposed \( x \), which is allowed, because in the game the challenger chooses \( y \) after seeing \( x \).

The last two domains differ by a single point, \( 0 \), and that point is exactly the least element of \( [0, 1] \). Removing it leaves a set with no least element, although every element of \( (0, 1] \) is still at least \( 0 \). Chapter 11 returns to this distinction between a least element and a greatest lower bound.
:::

::: {#exr-predicates-and-quantifiers-c2}
[C2: The wrong connective]

Take the domain \( \nR \).

::: {.enumerate options="label=(\alph*)"}
1. The sentence "every element of \( A \) is positive" is mistranslated as \( \forall x\, (x \in A \wedge x > 0) \), and "some element of \( A \) is positive" as \( \exists x\, (x \in A \to x > 0) \). For each mistranslation, give a set \( A \subseteq \nR \) for which it has a different truth value from the English sentence.
2. Show that the first mistranslation is false for **every** set \( A \subseteq \nR \), and the second is true for **every** set \( A \subseteq \nR \). What does this say about how much each one tells us about \( A \)?
:::
:::

::: {.solution}
*(a)* Take \( A = \{1\} \) for the first. "Every element of \( \{1\} \) is positive" is true. The mistranslation claims that every real \( x \) is in \( \{1\} \) and positive; \( x = 0 \) is neither, so it is false.

Take \( A = \{-1\} \) for the second. "Some element of \( \{-1\} \) is positive" is false, since its only element is negative. The mistranslation is true, with the witness \( x = 0 \): since \( 0 \notin \{-1\} \), the implication "if \( 0 \in A \), then \( 0 > 0 \)" has a false hypothesis and is true.

*(b)* For the first, let \( A \subseteq \nR \) be any set. The real number \( x = 0 \) does not satisfy \( x > 0 \), so it does not satisfy \( x \in A \wedge x > 0 \), whatever \( A \) is. It is a counterexample to the \( \forall \), so the sentence is false.

For the second, let \( A \subseteq \nR \) be any set, and consider the real number \( x = 1 \). The conclusion \( 1 > 0 \) is true, so the implication \( 1 \in A \to 1 > 0 \) is true whether or not \( 1 \in A \). Hence \( x = 1 \) is a witness, whatever \( A \) is, and the sentence is true.

So neither mistranslation tells us anything about \( A \) at all: the first is false and the second is true, whichever set \( A \) is. A sentence whose truth value does not depend on \( A \) cannot express a property of \( A \). This is the precise sense in which the wrong connective "claims too much" under \( \forall \) and "too little" under \( \exists \).

**Marking scheme.** (10 points)
- 2: a set for the first mistranslation, with both truth values checked.
- 2: a set for the second mistranslation, with both truth values checked, and the implication at the witness justified (its hypothesis is false, or its conclusion is true).
- 3: for the first, for an arbitrary \( A \), a real number (the same for every \( A \), or chosen by cases covering every \( A \)) that fails \( x \in A \wedge x > 0 \), with the check.
- 3: for the second, for an arbitrary \( A \), a witness (the same for every \( A \), or chosen by cases covering every \( A \)) at which \( x \in A \to x > 0 \) holds, with a reason that covers every \( A \) (its conclusion is true, or a check in every case).
Fatal errors (0 for the step): a witness or counterexample that depends on \( A \) in (b) without a case split covering every \( A \); reading \( \exists x\, (x \in A \to x > 0) \) as "some element of \( A \) is positive".
:::

<!-- dependency ledger
exm-reading-quantified-sentences (claim): in the subsection "The same sentence over different domains" before it, sqrt 2 exists in R, so exists x (x^2 = 2) is true over R | school fact here, stated as such; Chapter 11 (thm-nth-root) proves it; prose pointer
exm-reading-quantified-sentences (claim): in the subsection "The same sentence over different domains" before it, every natural number is at least 0, so forall x (x >= 0) holds over N | convention N = {0, 1, 2, ...} (NOTATION); school fact
exm-reading-quantified-sentences (solution): the check "exists x (x + x = x)" before it: x + x = x iff x = 0; 0 is in Z, R and N, not in Z_{>0}; n + n > n for n in Z_{>0} | school arithmetic
exm-reading-quantified-sentences (example): x^2 >= 0 for every real x | school fact (signs), stated as such
exm-reading-quantified-sentences (example): there is no largest prime | school fact (infinitude of primes), stated in the text as not used; nothing depends on it
def-bounded-quantifier (claim): an implication with a false hypothesis is true (vacuous truth), used to read the wrong bounded forms and the empty-set cases | informal reading of Chapter 2 (prp-vacuous-implication cited); made exact in Section 4.11; the universal empty-set case is derived in Section 4.4
exm-quantifier-order-sum (example): x + (-x) = 0 and (1 - y) + y = 1 in R | school arithmetic
exm-quantifier-order-sum (claim): the game reading after it; a quantifier under a negation changes sides, not-forall x read as exists x not | informal reading only, stated as such; Section 4.9 (later section of this chapter; prose pointer only, nothing here rests on it)
exm-quantifier-order-sum (claim): "When swapping is harmless" after it: swapping two quantifiers of the same kind is harmless; exists y forall x implies forall x exists y | informal reading only, stated as such; derived in Sections 4.4 and 4.6; the failure of the converse is exm-quantifier-order-sum
exm-quantifier-order-sum (solution): the check on the swapped prime sentence after it: n = p gives p > p, which is false | school arithmetic (irreflexivity of <)
exr-predicates-and-quantifiers-a1 (solution): (a)(i)-(iv): x + 1 > x; x + 1 = 0 only at -1; y = x - 1 < x; 2x = 1 only at 1/2; (v): x * x >= x for all integers; (1/2)^2 = 1/4 < 1/2 | school arithmetic; checked by verify/ch04/exr-predicates-and-quantifiers-a1.py
exr-predicates-and-quantifiers-b1 (solution): y * y >= 0 for real y; 2 + y >= 2 for y in N; x = 0, 1 have witnesses y = 1, 0 | school arithmetic; checked by verify/ch04/exr-predicates-and-quantifiers-b1.py
exr-predicates-and-quantifiers-b2 (solution): x + 1 > x; y > y is false; y != x and y >= x also work (partners x + 1 and x, failures at x = y and x = y + 1); y >= 1 fails because y = 1 is a partner of every x | school arithmetic; checked by verify/ch04/exr-predicates-and-quantifiers-b2.py
exr-predicates-and-quantifiers-c1 (solution): 0 < x/2 < x for 0 < x | school arithmetic; checked by verify/ch04/exr-predicates-and-quantifiers-c1.py
exr-predicates-and-quantifiers-c2 (solution): 0 is not > 0; 1 > 0; -1 < 0; 0 is not in {1} and not in {-1} | school arithmetic; checked by verify/ch04/exr-predicates-and-quantifiers-c2.py
-->
