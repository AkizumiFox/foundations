# Predicates and Quantifiers

Chapters 1–4 treated an atomic statement as a closed box, and the statements of analysis keep their whole content inside the box: "for every \( \varepsilon > 0 \) there is an \( N \) such that …" lives in the words "for every" and "there is" and in the letters they govern. This section opens the box: it introduces predicates, variables, domains and the two quantifiers \( \forall \) and \( \exists \), and teaches how to **read** a quantified sentence, first in a small picture and then over the numbers; the rules come one per section, in Sections 5.3 to 5.6.

## An argument the truth table rejects

Here is an argument that nobody would doubt.

> Every positive real number has a square root. The number \( 2 \) is positive. Therefore \( 2 \) has a square root.

It is correct in the plainest sense: if the two premises are true, the conclusion must be. Now try to check it with the tools of Chapters 1–4. The three sentences contain no connective at all, so each is atomic. Give them atoms:

- \( p \): "every positive real number has a square root";
- \( q \): "\( 2 \) is positive";
- \( r \): "\( 2 \) has a square root".

The argument has the form \( p, q \therefore r \). Three different atoms, and nothing connects them. The valuation that makes \( p \) and \( q \) true and \( r \) false makes both premises true and the conclusion false. So by @cor-refuting-row,
\[
p, \ q \nvdash r .
\]
No derivation, with any rule of Chapters 1 and 2, leads from \( p \) and \( q \) to \( r \).

::: {.second-reading title="Why the truth table is not wrong"}
There is no contradiction here, and it is worth seeing exactly why. @cor-refuting-row is about the **form** \( p, q \therefore r \): it says that no derivation leads from two arbitrary statements to a third, unrelated one. That is true. Our argument is correct for a reason that the form cannot see. The first premise speaks about **every** positive real number. The second says that \( 2 \) is **one** of the things the first premise speaks about. The conclusion says of \( 2 \) what the first premise said of all of them. The three statements share parts: a property ("is positive"), another property ("has a square root"), an object (\( 2 \)), and the word "every". Chopped into atoms, the shared parts disappear.
:::

This is the warning of Section 4.4 come true: a truth table sees only the connectives, and everything inside an atom is invisible to it. Section 4.4 closed with the remark that this chapter looks inside atoms. We now do. The first job is a vocabulary for the parts inside: the properties, the objects, and the words "every" and "some". Section 5.3 then gives the rule that makes the argument above a derivation, four lines long.

## Predicates: statements with holes

Chapter 1 met the sentence "\( x > 2 \)" and called it an **open sentence** (item (e) of @exm-statements). It is not a statement, because its truth depends on what \( x \) is: it is true when \( x \) is \( 3 \) and false when \( x \) is \( 0 \). Put a number in for \( x \) and it becomes a statement.

The argument of the last subsection is built from two open sentences of this kind: "\( x \) is positive" and "\( x \) has a square root". Each has one hole, marked by \( x \). The premise "\( 2 \) is positive" is the first open sentence with \( 2 \) put into the hole; the conclusion is the second, with \( 2 \) put into its hole. The first premise does something else with the holes, which we come to in the next subsection. Open sentences are the missing parts, and they deserve a name.

*A predicate is a statement with holes in it; filling every hole with a name of an object gives a statement.*

A **predicate** is an open sentence with one or more marked holes. The number of holes is its **arity**: a predicate with one hole is **one-place** (or unary), with two holes **two-place** (binary), and so on. We write a predicate as a capital letter followed by its holes in parentheses: \( P(x) \) for "\( x \) is positive", \( S(x) \) for "\( x \) has a square root", \( D(x, y) \) for "\( x \) divides \( y \)". The letters that mark the holes are **variables**: \( x, y, z, u \), and in analysis also \( \varepsilon, \delta, N, n \). A **constant** is a name of one particular object: \( 0 \), \( 1 \), \( 2 \), or a letter \( a, b, c \) that has been given a fixed meaning.

In words: a predicate says something **about** objects without saying which objects. The variables are placeholders, not objects. "\( x \) is positive" is about whatever will be put in for \( x \), and until something is, it is neither true nor false.

Many predicates of mathematics are written with a symbol between their two holes rather than a letter in front: \( x < y \), \( x \le y \), \( x = y \), \( x \mid y \). These are two-place predicates like any other; only the way of writing them differs. Membership \( x \in A \), for a fixed set \( A \), is a one-place predicate of \( x \): "\( x \) is an element of \( A \)". Here a set is understood informally, as a collection of objects (usually numbers), and nothing in this section uses more about a set \( A \) than whether a given object is an element of it. For sets \( A \) and \( B \), \( A \subseteq B \) means that every element of \( A \) is an element of \( B \); so \( A \subseteq \nR \) says that \( A \) is a set of real numbers.

Objects can also be built from other objects: \( x + 1 \), \( x^2 \), \( \abs{x} \), \( 2 \cdot y \). The symbols that build them (\( + \), squaring, \( \abs{\cdot} \), \( \cdot \)) are **function symbols**, and an expression such as \( x^2 + 1 \) names an object as soon as \( x \) does. A function symbol may also be a letter, \( f(x) \). Here a function symbol is simply a way of naming one object in terms of others. Section 5.2 makes all of this exact, under the name **term**. For now, a term is any expression that names an object: a variable, a constant, or a function symbol applied to terms.

Filling holes is the first way to turn a predicate into a statement.

- \( P(2) \): "\( 2 \) is positive". A statement, and true.
- \( P(-3) \): "\( -3 \) is positive". A statement, and false.
- \( D(3, 12) \): "\( 3 \) divides \( 12 \)". True.
- \( D(3, y) \): "\( 3 \) divides \( y \)". Still open: one hole is filled and one is not. It is a one-place predicate of \( y \).
- \( P(x^2 + 1) \): "\( x^2 + 1 \) is positive". Still open, in \( x \). (It happens to be true whatever real number \( x \) is, but that is a fact about the numbers, and the sentence still has a hole.)

The last two items show that filling holes is not all or nothing. A predicate with some holes filled is a predicate with fewer holes. Only when **every** hole is filled, or closed in the way described next, do we have a statement.

Some letters change their job in this chapter:

| Letter | In Chapters 1–4 | In this chapter | How to tell |
|---|---|---|---|
| \( P, Q, R \) | a whole statement (Chapters 1–2); an atom or any formula (Chapter 4) | a predicate symbol | followed by its holes: \( P(x) \), \( R(x, y) \); a bare \( P \) is a statement letter from earlier chapters |
| \( p, q, r \) | atoms of a truth table | atoms still, only where a truth table reads a formula (the argument above; review exercises) | never a variable or a symbol of a first-order formula in this chapter |
| \( x, y, n, \varepsilon \) | one fixed number in an example ("let \( x \) be a real number") | variables: holes of predicates, closed by quantifiers | a quantifier in front of them, or a hole still open |

A property \( P(n) \) of natural numbers, as in the principle of induction (@ax-induction), was already a one-place predicate in this sense.

## Quantifiers and the domain

There is a second way to turn "\( x \) is positive" into a statement, and the first premise of our argument uses it. The premise does not put a particular number into the hole of "\( x \) has a square root". It says that the open sentence "if \( x \) is positive, then \( x \) has a square root" is true **whatever** real number is put in. The word "every" closes the hole without filling it.

Two questions have to be answered before "whatever is put in" makes sense. What may be put in? And how many of those things must make the sentence true?

The first question is answered by a **domain of discourse**, or **domain**: the collection of objects that the variables range over. For the argument above, the domain is the real numbers, \( \nR \). In number theory it is often \( \nZ \) or \( \nN \) (in this book \( \nN = \{0, 1, 2, \dots\} \), with \( 0 \)). A domain always has at least one element; an empty collection is handled by bounded quantifiers, as below.

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
"for every \( x \), if \( x \) is positive, then \( x \) has a square root". The second premise is \( P(2) \) and the conclusion is \( S(2) \). Now the shared parts are visible: \( P \) occurs in both premises, \( S \) in the first premise and the conclusion, and \( 2 \) in the second premise and the conclusion. The rule of Section 5.3 uses the first premise with \( x \) replaced by \( 2 \), giving \( P(2) \to S(2) \), and \( \rulename{{\to}E} \) finishes.

Notice the \( \to \) inside the quantifier. The premise does not say that every real number is positive and has a square root; it says that every real number which is positive has one. The subsection on bounded quantifiers below explains why a "for every" restricted to part of the domain always comes with an implication.

::: {.remark}
"True" here means what it means in ordinary mathematics: look at the domain and ask whether every element, or some element, makes the sentence true. A claim that a sentence can be **derived** is always proved by a derivation, never by this reading.
:::

### Quantifiers in a small world

Before the numbers, a picture. A **world** here is a few dots, the objects of the domain, with some dots labeled \( P \) or \( Q \) (the dots the one-place predicates hold of) and arrows between dots (the pairs a two-place predicate \( R \) holds of: an arrow from \( u \) to \( v \) means \( R(u, v) \)).

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=left:$a$, label=above:{$P$}] (a) at (0,1.8) {};
  \node[elt, label=right:$b$, label=above:{$P, Q$}] (b) at (2.4,1.8) {};
  \node[elt, label=below:$c$, label=left:{$Q$}] (c) at (2.4,0) {};
  \node[elt, label=below:$d$] (d) at (0,0) {};
  \draw[rel] (a) -- (b);
  \draw[rel] (b) -- (c);
  \draw[rel] (c) to[loop right] (c);
  \draw[rel] (d) -- (a);
\end{tikzpicture}
\end{center}
```

**Figure W.** World W: domain \( \{a, b, c, d\} \); \( P \) holds of \( a, b \); \( Q \) of \( b, c \); \( R \) is the four arrows.

Six readings, each checked dot by dot:

- \( \exists x\, P(x) \): true; the witness \( a \).
- \( \forall x\, P(x) \): false; the counterexample \( c \) (or \( d \)).
- \( \forall x\, (P(x) \vee Q(x)) \): false at \( d \), which has neither label.
- \( \exists x\, (P(x) \wedge Q(x)) \): true at \( b \).
- \( \forall x\, \exists y\, R(x, y) \): true; every dot has an arrow leaving it (\( a \to b \), \( b \to c \), \( c \to c \), \( d \to a \)).
- \( \exists y\, \forall x\, R(x, y) \): false; no dot receives an arrow from all four (\( c \) receives from \( b \) and \( c \) only).

In a finite world every quantifier can be checked dot by dot. Over \( \nN \) or \( \nR \) it cannot, and the reading needs an argument, as the next subsection shows.

::: {.check}
In world W, is \( \forall x\, (Q(x) \to R(x, c)) \) true? Is \( \exists x\, \forall y\, \neg R(y, x) \) true?
:::

::: {.solution}
The first is true: \( Q \) holds of \( b \) and \( c \), and both have an arrow to \( c \); at \( a \) and \( d \) the hypothesis \( Q(x) \) is false, so the implication holds. The second is true, with the witness \( d \): no arrow ends at \( d \).
:::

**A long "and", a long "or".** When the dots of a world can be listed, a quantifier is a connective repeated. In world W, \( \forall x\, P(x) \) says the same as \( P(a) \wedge P(b) \wedge P(c) \wedge P(d) \), and \( \exists x\, P(x) \) the same as \( P(a) \vee P(b) \vee P(c) \vee P(d) \). A counterexample to the first is a false conjunct (\( c \)); a witness for the second is a true disjunct (\( a \)). De Morgan's law (@prp-de-morgan), used three times, then says that "not every dot has \( P \)" is "some dot lacks \( P \)": \( \neg(P(a) \wedge \dots \wedge P(d)) \) and \( \neg P(a) \vee \dots \vee \neg P(d) \). Over \( \nN \) the conjunction would never end, and no formula can write it down; that is why the quantifiers get rules of their own.

::: {.check}
In world W, write \( \forall x\, (P(x) \to Q(x)) \) as a conjunction of four statements, one per dot. Which conjunct is false?
:::

::: {.solution}
\( (P(a) \to Q(a)) \wedge (P(b) \to Q(b)) \wedge (P(c) \to Q(c)) \wedge (P(d) \to Q(d)) \). The first conjunct is false, since \( a \) has \( P \) and not \( Q \). The other three are true: \( b \) has both labels, and \( c \) and \( d \) lack \( P \).
:::

### The same sentence over different domains

A quantified sentence is a claim about its domain, so changing the domain can change its truth value. Two examples show how.

Take \( \forall x\, (x \ge 0) \), "every \( x \) is at least \( 0 \)".

- Over \( \nN \) it is **true**: every natural number is at least \( 0 \).
- Over \( \nZ \) it is **false**: the integer \( -1 \) is in the domain, and \( -1 \ge 0 \) is false.

One element of the domain that makes \( \varphi \) false is enough to make \( \forall x\, \varphi \) false. Such an element is a **counterexample**. To show that the sentence is true over \( \nN \), on the other hand, we had to say something about every natural number at once.

Take \( \exists x\, (x^2 = 2) \), "some \( x \) has square \( 2 \)".

- Over \( \nR \) it is **true**: the real number \( \sqrt{2} \) has square \( 2 \). (Its existence is a school fact here.)
- Over \( \nQ \) it is **false**: that no rational number has square \( 2 \) is exactly @thm-sqrt2-irrational.

One element that makes \( \varphi \) true is enough to make \( \exists x\, \varphi \) true. Such an element is a **witness**. To show that the sentence is false over \( \nQ \), on the other hand, a theorem about every rational number was needed, and Chapter 2 proved it by contradiction.

The two quantifiers are mirror images. For \( \forall \), a single counterexample refutes and a general argument confirms. For \( \exists \), a single witness confirms and a general argument refutes.

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
3. \( \neg\exists m\, \bigl( \mathrm{Prime}(m) \wedge \forall n\, (\mathrm{Prime}(n) \to n \le m) \bigr) \), over \( \nN \), where \( \mathrm{Prime}(m) \) is the one-place predicate "\( m \) is prime".
:::
:::

::: {.solution}
*(a)* "For every \( x \), \( x^2 \) is at least \( 0 \)." The claim is about every real number, and it is true: the square of a real number is never negative (a school fact about signs: \( x \cdot x \) is a product of two numbers of the same sign, or \( 0 \)).

*(b)* "There is an \( x \) such that for every \( y \), \( x \le y \)." Unpack from the outside. The outer quantifier \( \exists x \) asks for one natural number \( x \). What must be true of it is the inside, \( \forall y\, (x \le y) \): every natural number \( y \) is at least \( x \). So the sentence says that \( \nN \) has a **least element**. It is true, with the witness \( x = 0 \): every natural number is at least \( 0 \).

*(c)* The outer symbol is \( \neg \), so the sentence denies what follows. What follows is \( \exists m\, (\dots) \): there is an \( m \) that is prime and such that every prime \( n \) is at most \( m \). Such an \( m \) would be a **largest prime**. So the sentence says "there is no largest prime". It is true: this is the ancient theorem that there are infinitely many primes. Nothing in this book depends on that theorem; here it is only something to read.

Notice the shape inside (c): \( \forall n\, (\mathrm{Prime}(n) \to n \le m) \), "every prime is at most \( m \)", has an implication under the \( \forall \). It speaks about primes only, and the implication is how a "for every" is restricted to them. The next subsection makes this a rule of writing.
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

::: {.second-reading title="The induction display, read again"}
The display after @ax-induction, in Section 4.2, used \( \forall n \in \nN \) as an abbreviation of the words "for every natural number \( n \)". It was already this bounded form: \( \forall n \in \nN\; \bigl( P(n) \to P(n + 1) \bigr) \) stands for \( \forall n\, \bigl( n \in \nN \to (P(n) \to P(n + 1)) \bigr) \).
:::

**Why \( \to \) under \( \forall \), and \( \wedge \) under \( \exists \).** Try the other choices and see what they say. Take the domain \( \nR \), the set \( A = \{1, 2\} \), and the open sentence \( x > 5 \).

- "Every element of \( A \) is greater than \( 5 \)" is false: \( 1 \) is not. The correct form \( \forall x\, (x \in A \to x > 5) \) is false too, with the counterexample \( x = 1 \), which is in \( A \) and not greater than \( 5 \). The wrong form \( \forall x\, (x \in A \wedge x > 5) \) says that **every real number** is in \( A \) and greater than \( 5 \). It is false as well, but for a reason that has nothing to do with \( A \)'s elements: \( x = 0 \) is not in \( A \). Change \( A \) to \( \{6, 7\} \) and the correct form becomes true while the wrong one stays false.
- "Some element of \( A \) is greater than \( 5 \)" is false for \( A = \{1, 2\} \). The correct form \( \exists x\, (x \in A \wedge x > 5) \) is false too: no real number is both in \( A \) and greater than \( 5 \). The wrong form \( \exists x\, (x \in A \to x > 5) \) is **true**, with the witness \( x = 0 \): since \( 0 \notin A \), the implication "if \( 0 \in A \) then \( 0 > 5 \)" has a false hypothesis and is true (vacuous truth, the phenomenon behind @prp-vacuous-implication).

So a \( \forall \) with \( \wedge \) inside claims too much: it says the whole domain lies in \( A \). An \( \exists \) with \( \to \) inside claims too little: anything outside \( A \) is a witness. Neither says what was meant.

::: {.warning}
An existential quantifier with an implication directly inside, \( \exists x\, (\alpha \to \beta) \), is almost always a mistranslation. Over \( \nR \), "some element of \( \{1, 2\} \) exceeds \( 5 \)" is false, but \( \exists x\, (x \in \{1, 2\} \to x > 5) \) is true, because \( x = 0 \) makes the hypothesis false. When you write \( \exists \) and then \( \to \), check whether you meant \( \wedge \).
:::

**Mixing kinds of number.** A sentence of analysis often mixes real numbers and natural numbers; the convention is to take the larger kind as the domain and let the smaller kind enter as a bound, as in \( \forall \varepsilon > 0\; \exists N \in \nN \), with a sequence \( (a_n) \) read as a function symbol \( a \), \( a_n = a(n) \).

**The empty set.** Bounded quantifiers make sense even when the bound is never satisfied. Let \( \emptyset \) be the **empty set**, the set with no elements, so that \( x \in \emptyset \) is false for every \( x \).

- \( \forall x \in \emptyset \; \varphi \) stands for \( \forall x\, (x \in \emptyset \to \varphi) \). For every \( x \), the hypothesis \( x \in \emptyset \) is false, so the implication is true. The sentence is **true**, whatever \( \varphi \) says. For example, "every element of \( \emptyset \) is greater than \( 5 \)" and "every element of \( \emptyset \) is less than \( 5 \)" are both true.
- \( \exists x \in \emptyset \; \varphi \) stands for \( \exists x\, (x \in \emptyset \wedge \varphi) \). No \( x \) makes the first conjunct true, so the sentence is **false**, whatever \( \varphi \) says.

Section 2.1 met this phenomenon for implications: a statement whose hypothesis never holds is true, and says nothing. A universal statement about the elements of an empty set is true for the same reason, because there is nothing to test. This is the reading; Section 5.4 derives the universal half with the rules.

::: {.warning}
**Existential import.** "Every element of \( A \) has property \( \varphi \)" does **not** imply "some element of \( A \) has property \( \varphi \)". A "for every" over a bound has no *existential import*: it does not say that anything satisfies the bound. It fails when \( A \) is empty: "every element of \( \emptyset \) is greater than \( 5 \)" is true, and "some element of \( \emptyset \) is greater than \( 5 \)" is false. The step from "every" to "some" needs an element, and the bound can remove all of them.
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
:::

::: {.second-reading title="What makes the pair work"}
What makes the pair work as an example? Two properties, and any other pair with the same shape would do as well. First, for each \( x \) separately there is a suitable \( y \). Second, no one \( y \) is suitable for all \( x \) together, because each \( y \) serves only one \( x \) (here, only \( x = -y \)).
:::

**Quantifiers as a game.** Read a sentence as a game between two players, the challenger, who tries to make it false, and the defender, who tries to make it true.

- Each \( \forall \) is a move of the challenger, who picks a value; each \( \exists \) is a move of the defender.
- The moves are made in the order the quantifiers are written, left to right, and each player sees every move made so far.
- When every variable has a value, the inside is checked. The sentence is true exactly when the defender can win whatever the challenger does.

Here are the two sentences of @exm-quantifier-order-sum, played.

| | (i) \( \forall x\, \exists y\, (x + y = 0) \) | (ii) \( \exists y\, \forall x\, (x + y = 0) \) |
|---|---|---|
| first move | challenger picks \( x \), say \( x = 5 \) | defender picks \( y \) without knowing \( x \), say \( y = 3 \) |
| second move | defender answers \( y = -x = -5 \) | challenger answers \( x = 1 - y = -2 \) |
| check | \( 5 + (-5) = 0 \): defender wins | \( -2 + 3 = 1 \ne 0 \): challenger wins |
| who always wins | the defender, with \( y = -x \) | the challenger, with \( x = 1 - y \) |

::: {.remark}
The game reads sentences whose quantifiers all stand at the front, unnegated, before an inside with no quantifiers. A bounded quantifier such as \( \forall \varepsilon > 0 \) counts, its bound checked with the inside. Under a \( \neg \), or in the hypothesis of an implication, a quantifier changes sides.
:::

*Read the dependency off the order: a variable may depend on the variables quantified to its left, and only on them.* In (i), \( y \) is to the right of \( x \), so the choice of \( y \) may use \( x \). In (ii), \( y \) is to the left, so it may not. Sections 5.4 to 5.6 will show this same dependence as a fact about the boxes of a derivation.

::: {.check}
Over the domain \( \nN \), swap the two quantifiers in "for every \( n \) there is a prime larger than \( n \)", that is, in \( \forall n\, \exists m\, \bigl( \mathrm{Prime}(m) \wedge m > n \bigr) \). Read the result aloud. Is it true?
:::

::: {.solution}
The swapped sentence is \( \exists m\, \forall n\, \bigl( \mathrm{Prime}(m) \wedge m > n \bigr) \): "there is a prime that is larger than every natural number". It is **false**. Whatever \( m \) is proposed, take \( n = m \): then \( m > n \) is false, so the inside fails. (The original sentence is true; it is another form of the theorem that there are infinitely many primes, which we do not use.) As in @exm-quantifier-order-sum, the original lets the prime depend on \( n \), and the swapped sentence demands one prime for all \( n \) at once.
:::

::: {.second-reading title="When swapping is harmless"}
**When swapping is harmless.** Two quantifiers of the **same** kind may be swapped. \( \forall x\, \forall y\, \varphi \) and \( \forall y\, \forall x\, \varphi \) both say that \( \varphi \) holds for every choice of the pair; in the game, the challenger makes both moves, and the order of the challenger's own moves gives nothing away. Likewise \( \exists x\, \exists y\, \varphi \) and \( \exists y\, \exists x\, \varphi \) both say that some pair works. Section 5.4 derives the first swap with the rules. For quantifiers of **different** kinds, one direction is always safe: if one \( y \) works for every \( x \), then for every \( x \) some \( y \) works (the same one). Section 5.6 derives this, \( \exists y\, \forall x\, \varphi \) to \( \forall x\, \exists y\, \varphi \), and @exm-quantifier-order-sum shows that the other direction fails.
:::

## Words that hide quantifiers

English marks quantifiers loosely, and mathematical English has habits that hide them altogether. Two traps are worth naming now, before they cause trouble.

::: {.warning}
The word **"any"** can mean "every" or "some", and only the sentence around it decides. "Any \( x \) in \( A \) is positive" means every element of \( A \) is positive: \( \forall x \in A\; (x > 0) \). "If any \( x \) in \( A \) is positive, then \( A \) is non-empty" means if **some** element is positive: \( \exists x \in A\; (x > 0) \to \dots \). When you meet "any", rewrite the sentence with "every" and with "some", and keep the one that says what was meant.
:::

**Hidden universal quantifiers.** A theorem stated as "if \( n \) is even, then \( n^2 \) is even" has no quantifier word in it, and yet it is not about one number. It means: for every integer \( n \), if \( n \) is even, then \( n^2 \) is even. A letter that is not introduced anywhere, in the statement of a theorem, is read with a "for every" in front. When translating, put the hidden quantifier back first.

## Keys and locks

A domain with no numbers in it makes the shapes easy to see: the objects of a building, with \( \mathrm{Key}(x) \): "\( x \) is a key", \( \mathrm{Lock}(x) \): "\( x \) is a lock", and \( \mathrm{Opens}(x, y) \): "\( x \) opens \( y \)". The table reads in either direction; \( c \) is a constant, "the front lock".

| English | Formula | Note |
|---|---|---|
| every key opens lock \( c \) | \( \forall x\, (\mathrm{Key}(x) \to \mathrm{Opens}(x, c)) \) | \( \to \) under \( \forall \) |
| some key opens lock \( c \) | \( \exists x\, (\mathrm{Key}(x) \wedge \mathrm{Opens}(x, c)) \) | \( \wedge \) under \( \exists \) |
| no key opens lock \( c \) | \( \forall x\, (\mathrm{Key}(x) \to \neg\mathrm{Opens}(x, c)) \), or \( \neg\exists x\, (\mathrm{Key}(x) \wedge \mathrm{Opens}(x, c)) \) | two equally good forms |
| only keys open lock \( c \) | \( \forall x\, (\mathrm{Opens}(x, c) \to \mathrm{Key}(x)) \) | "only" turns the arrow round |
| every lock has a key that opens it | \( \forall y\, (\mathrm{Lock}(y) \to \exists x\, (\mathrm{Key}(x) \wedge \mathrm{Opens}(x, y))) \) | every … some |
| some key opens every lock | \( \exists x\, (\mathrm{Key}(x) \wedge \forall y\, (\mathrm{Lock}(y) \to \mathrm{Opens}(x, y))) \) | some … every |

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \node[elt, label=left:{$k_1$ (key)}] (k1) at (0,1.4) {};
  \node[elt, label=left:{$k_2$ (key)}] (k2) at (0,0) {};
  \node[elt, label=right:{$\ell_1$ (lock)}] (l1) at (3,1.4) {};
  \node[elt, label=right:{$\ell_2$ (lock)}] (l2) at (3,0) {};
  \draw[rel] (k1) -- (l1);
  \draw[rel] (k2) -- (l2);
\end{tikzpicture}
\end{center}
```

**Figure K.** A building where every lock has a key that opens it, and no key opens every lock.

In this building the fifth sentence of the table is true (\( \ell_1 \) has \( k_1 \), \( \ell_2 \) has \( k_2 \)) and the sixth is false (\( k_1 \) fails at \( \ell_2 \), \( k_2 \) at \( \ell_1 \)). The sixth implies the fifth, since a master key opens each lock, so the order "some … every" says more, exactly as in @exm-quantifier-order-sum.

::: {.check}
Translate "no key opens every lock". Is it true in the building of Figure K?
:::

::: {.solution}
\( \neg\exists x\, (\mathrm{Key}(x) \wedge \forall y\, (\mathrm{Lock}(y) \to \mathrm{Opens}(x, y))) \), or \( \forall x\, (\mathrm{Key}(x) \to \neg\forall y\, (\mathrm{Lock}(y) \to \mathrm{Opens}(x, y))) \). It is true in the building of Figure K, since \( k_1 \) does not open \( \ell_2 \) and \( k_2 \) does not open \( \ell_1 \).
:::

::: {.second-reading title="Two slips with an implication inside \"there is\""}
"Some key opens lock \( c \)" is **not** \( \exists x\, (\mathrm{Key}(x) \to \mathrm{Opens}(x, c)) \): that formula is true in every building, since the lock \( c \) is not a key, so \( c \) itself makes the hypothesis \( \mathrm{Key}(c) \) false. It is the warning after @def-bounded-quantifier again.

**An implication inside \( \exists \).** This is the warning after @def-bounded-quantifier once more, and it comes up in analysis: "there is an \( N \) such that, if \( n \ge N \), then …" is not the shape of "for every \( \varepsilon > 0 \) there is \( N \in \nN \) such that for every \( n \ge N \), …", where the implication \( n \ge N \to \dots \) sits under \( \forall n \in \nN \). The implication belongs under a \( \forall \).
:::

## What comes next

We can read quantified sentences, and translate into them. We cannot yet reason with them. Section 5.2 makes the language exact, because every rule will put a term in for a variable; Sections 5.3–5.6 give the four rules.

::: {.remark}
[Looking ahead]

Chapter 7 turns "true in a domain" into a definition, and proves that a reading in which the premises are true and the conclusion false rules out every derivation.
:::

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

::: {#exr-predicates-and-quantifiers-a2}
[A2: Drill]

Answer each part in a line or two. Parts (a)–(d) are about world W of Figure W, parts (e)–(i) about the building with \( \mathrm{Key} \), \( \mathrm{Lock} \) and \( \mathrm{Opens} \), and parts (j)–(l) about numbers.

::: {.enumerate options="label=(\alph*)"}
1. In W, is \( \forall x\, (P(x) \to \exists y\, R(x, y)) \) true?
2. In W, is \( \exists x\, (Q(x) \wedge \neg P(x)) \) true?
3. In W, is \( \forall x\, \exists y\, R(y, x) \) true?
4. In W, write \( \exists x\, R(x, x) \) as a disjunction of four statements, one per dot, and decide it.
5. Translate "every key opens some lock".
6. Translate "no lock is a key".
7. Translate "only keys open locks".
8. Translate "some lock is opened by every key".
9. Is (h) true in the building of Figure K?
10. Over \( \nZ \), translate "every integer has a larger one", and say whether it is true.
11. Swap the quantifiers of (j) and read the result.
12. Over \( \nR \), translate with bounded quantifiers "some positive number is smaller than every positive number", and say whether it is true.
:::
:::

::: {.solution}
(a) Yes: \( P \) holds of \( a \) and \( b \), and \( a \to b \), \( b \to c \).

(b) Yes, at \( c \).

(c) No: no arrow ends at \( d \).

(d) \( R(a, a) \vee R(b, b) \vee R(c, c) \vee R(d, d) \); true, by the third disjunct (the loop at \( c \)).

(e) \( \forall x\, (\mathrm{Key}(x) \to \exists y\, (\mathrm{Lock}(y) \wedge \mathrm{Opens}(x, y))) \).

(f) \( \forall x\, (\mathrm{Lock}(x) \to \neg\mathrm{Key}(x)) \), or \( \neg\exists x\, (\mathrm{Lock}(x) \wedge \mathrm{Key}(x)) \).

(g) \( \forall x\, \forall y\, ((\mathrm{Lock}(y) \wedge \mathrm{Opens}(x, y)) \to \mathrm{Key}(x)) \).

(h) \( \exists y\, (\mathrm{Lock}(y) \wedge \forall x\, (\mathrm{Key}(x) \to \mathrm{Opens}(x, y))) \).

(i) No: \( \ell_1 \) is not opened by \( k_2 \), and \( \ell_2 \) not by \( k_1 \).

(j) \( \forall x\, \exists y\, (y > x) \); true, with \( y = x + 1 \).

(k) \( \exists y\, \forall x\, (y > x) \), "some integer is larger than every integer"; false: \( x = y \) defeats every \( y \).

(l) \( \exists x > 0\; \forall y > 0\; (x < y) \); false: for any proposed \( x > 0 \), \( y = x \) gives \( x < x \).
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

::: {#exr-predicates-and-quantifiers-b3}
[B3: Every and some on three numbers]

Let the domain be \( D = \{0, 1, 2\} \), with \( \le \) and \( < \) as usual, and with the constants \( 0, 1, 2 \) naming its elements.

::: {.enumerate options="label=(\alph*)"}
1. Write \( \exists x\, \forall y\, (x \le y) \) without quantifiers, as a disjunction of conjunctions, and decide it.
2. Write \( \neg\forall x\, (x < 2) \) without quantifiers, as a disjunction, using De Morgan's law, and say which disjunct is true.
3. Let \( A \) be the set of elements of \( D \) greater than \( 2 \). Decide \( \forall x \in A\; (x < 0) \) and \( \exists x \in A\; (x < 0) \).
4. Give an example, or explain why there is none: a domain and a one-place predicate \( P \) for which \( \forall x\, P(x) \) is true and \( \exists x\, P(x) \) is false.
:::
:::

::: {.solution}
*(a)* The sentence is
\[
\begin{aligned}
& (0 \le 0 \wedge 0 \le 1 \wedge 0 \le 2) \vee (1 \le 0 \wedge 1 \le 1 \wedge 1 \le 2) \\
& \qquad {} \vee (2 \le 0 \wedge 2 \le 1 \wedge 2 \le 2).
\end{aligned}
\]
It is true, by the first disjunct: \( 0 \) is a least element.

*(b)* \( \neg(0 < 2 \wedge 1 < 2 \wedge 2 < 2) \) is, by De Morgan's law (@prp-de-morgan), \( \neg(0 < 2) \vee \neg(1 < 2) \vee \neg(2 < 2) \). The third disjunct is true, since \( 2 < 2 \) is false: "some element is not below \( 2 \)", with the witness \( 2 \).

*(c)* \( A \) is empty. The first is true: for every \( x \), the hypothesis \( x \in A \) is false. The second is false: no \( x \) is in \( A \).

*(d)* There is none. A domain has at least one element (the convention of "Quantifiers and the domain"), say \( d \); if \( \forall x\, P(x) \) is true, then \( P \) holds of \( d \), so \( d \) is a witness and \( \exists x\, P(x) \) is true. The emptiness in (c) is the emptiness of a bound, not of the domain.

Worked examples of these types: the long "and" of world W; "The empty set" in "Bounded quantifiers".

**Marking scheme.** (10 points)

- 3: (a), all nine atoms in the right places and the verdict with its witness.
- 2: (b), De Morgan applied to a three-term conjunction and the true disjunct named.
- 2: (c), both verdicts, each with the reason (hypothesis false; no element).
- 3: (d), "none", with the argument from a non-empty domain; 1 of the 3 for an answer that separates the empty bound of (c) from the domain.

Fatal error (0 for the part): an empty domain offered as the example in (d).
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

The last two domains differ by a single point, \( 0 \), and that point is exactly the least element of \( [0, 1] \). Removing it leaves a set with no least element, although every element of \( (0, 1] \) is still at least \( 0 \). *Analysis on the Real Line*, Chapter 1 returns to this distinction between a least element and a greatest lower bound.
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
predicates-and-quantifiers-world-w (example): the six readings of world W, its Quick check, and the long "and"/"or" expansions over the four dots (c a false conjunct of forall x P(x); a a true disjunct; P(a) -> Q(a) the false conjunct of the second Quick check) | informal truth in a finite world, read dot by dot; checked by verify/ch05/exr-predicates-and-quantifiers-a2.py
predicates-and-quantifiers-world-w (claim): "not every dot has P" is "some dot lacks P" over the four dots | prp-de-morgan (c), (d) (F1.2 §05, cited), applied three times to a four-term conjunction
predicates-and-quantifiers-keys (example): the verdicts in the building of Figure K (fifth sentence true, sixth false), its Quick check; "some ... every" implies "every ... some" there | informal truth in a finite world; checked by verify/ch05/exr-predicates-and-quantifiers-a2.py; the implication is the reading of exm-quantifier-order-sum's pattern (a master key opens each lock), stated informally; derived in general in F1.4 §06 (prp-exists-forall-swap)
predicates-and-quantifiers-keys (claim): fold "Two slips": exists x (Key(x) -> Opens(x, c)) is true in every building | vacuous truth at x = c (c is a lock, locks are not keys), informal reading as def-bounded-quantifier's demonstration
exm-reading-quantified-sentences (claim): in the subsection "The same sentence over different domains" before it, sqrt 2 exists in R, so exists x (x^2 = 2) is true over R | school fact here, stated as such; AN1.1 (index, Where this goes)
exm-reading-quantified-sentences (claim): in the subsection "The same sentence over different domains" before it, every natural number is at least 0, so forall x (x >= 0) holds over N | convention N = {0, 1, 2, ...} (NOTATION); school fact
exm-reading-quantified-sentences (solution): the check "exists x (x + x = x)" before it: x + x = x iff x = 0; 0 is in Z, R and N, not in Z_{>0}; n + n > n for n in Z_{>0} | school arithmetic
exm-reading-quantified-sentences (example): x^2 >= 0 for every real x | school fact (signs), stated as such
exm-reading-quantified-sentences (example): there is no largest prime | school fact (infinitude of primes), stated in the text as not used; nothing depends on it
def-bounded-quantifier (claim): an implication with a false hypothesis is true (vacuous truth), used to read the wrong bounded forms and the empty-set cases | informal reading of F1.2 (prp-vacuous-implication cited); the universal empty-set case is derived in F1.4 §04
def-bounded-quantifier (claim): the existential-import warning: a "for every" over a bound does not say that anything satisfies the bound | informal truth, as the empty-set bullets before it
exm-quantifier-order-sum (example): x + (-x) = 0 and (1 - y) + y = 1 in R; the move table (5 + (-5) = 0; -2 + 3 = 1) | school arithmetic
exm-quantifier-order-sum (claim): the game reading after it; a quantifier under a negation or in a hypothesis changes sides | informal reading only, stated as such; nothing here rests on it
exm-quantifier-order-sum (claim): fold "When swapping is harmless": swapping two quantifiers of the same kind is harmless; exists y forall x implies forall x exists y | informal reading only, stated as such; derived in F1.4 §04 and F1.4 §06; the failure of the converse is exm-quantifier-order-sum
exm-quantifier-order-sum (solution): the check on the swapped prime sentence after it: n = m gives m > m, which is false | school arithmetic (irreflexivity of <)
exr-predicates-and-quantifiers-a1 (solution): (a)(i)-(iv): x + 1 > x; x + 1 = 0 only at -1; y = x - 1 < x; 2x = 1 only at 1/2; (v): x * x >= x for all integers; (1/2)^2 = 1/4 < 1/2 | school arithmetic; checked by verify/ch05/exr-predicates-and-quantifiers-a1.py
exr-predicates-and-quantifiers-a2 (solution): (a)-(d), (i) read off world W and Figure K; (j)-(l): x + 1 > x, y > y false, x < x false | informal truth in a finite world and school arithmetic; checked by verify/ch05/exr-predicates-and-quantifiers-a2.py
exr-predicates-and-quantifiers-b1 (solution): y * y >= 0 for real y; 2 + y >= 2 for y in N; x = 0, 1 have witnesses y = 1, 0 | school arithmetic; checked by verify/ch05/exr-predicates-and-quantifiers-b1.py
exr-predicates-and-quantifiers-b2 (solution): x + 1 > x; y > y is false; y != x and y >= x also work (partners x + 1 and x, failures at x = y and x = y + 1); y >= 1 fails because y = 1 is a partner of every x | school arithmetic; checked by verify/ch05/exr-predicates-and-quantifiers-b2.py
exr-predicates-and-quantifiers-b3 (solution): the order on {0, 1, 2}: the nine atoms of (a), the three of (b); A empty in (c); (d) from non-empty domains | school order; prp-de-morgan (cited); the convention "a domain always has at least one element" of this section; checked by verify/ch05/exr-predicates-and-quantifiers-b3.py
exr-predicates-and-quantifiers-c1 (solution): 0 < x/2 < x for 0 < x | school arithmetic; checked by verify/ch05/exr-predicates-and-quantifiers-c1.py
exr-predicates-and-quantifiers-c2 (solution): 0 is not > 0; 1 > 0; -1 < 0; 0 is not in {1} and not in {-1} | school arithmetic; checked by verify/ch05/exr-predicates-and-quantifiers-c2.py
-->
