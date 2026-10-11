# Statements, Connectives and the Form of an Argument

This is where the book starts, and it starts with a question every reader of mathematics eventually asks: when is an argument a proof? A proof is not a list of true sentences, and it is not an argument that merely sounds convincing. This section takes the first steps towards a precise answer. It says what the sentences of a proof are, how they are built from smaller ones, and what it means for two arguments to have the same **form**, which is the thing logic studies.

## Two arguments about squares

Recall that an integer \( n \) is **even** when \( n = 2k \) for some integer \( k \), and **odd** when \( n = 2k + 1 \) for some integer \( k \). (The word "some" has rules of its own, which come in Chapter 4; here we use it as school algebra does.) Here is a fact about integers that Chapter 2 proves properly, once the rules for "not" are in place.

> For every integer \( n \), if \( n^2 \) is even, then \( n \) is even.

Read the following two arguments for it. Each is written in the style of a textbook proof, and each sentence in each of them is true.

**Argument A.** Suppose \( n \) is odd, say \( n = 2k + 1 \) for an integer \( k \). Then \( n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1 \), so \( n^2 \) is odd, and therefore \( n^2 \) is not even. So an odd \( n \) never has an even square. Since every integer is even or odd, an integer with an even square must be even.

**Argument B.** Suppose \( n \) is even, say \( n = 2k \) for an integer \( k \). Then \( n^2 = 4k^2 = 2(2k^2) \), and \( 2k^2 \) is an integer, so \( n^2 \) is even. Hence if \( n^2 \) is even, then \( n \) is even.

Argument A is a correct proof. Argument B is not, although none of its sentences is false. It starts from "\( n \) is even" and arrives at "\( n^2 \) is even". That is a perfectly good proof of a different statement: "if \( n \) is even, then \( n^2 \) is even". The claim asks for the journey in the opposite direction, from the square back to the number, and the last sentence of B announces a conclusion that the argument never reached.

Seeing this is easy once it is pointed out. Saying in general what went wrong is harder, and that is what this chapter and the next are for. To name the error we need to know what the rules of proof are, and before that, what they act on. So we start with the smallest pieces: the sentences a proof is made of.

## Statements

A proof is written in sentences, but not every sentence can appear in one. "Is 91 prime?" cannot be a step of an argument, because it asserts nothing; neither can "Let us now turn to the case \( n = 0 \)." The sentences that can serve as steps are the ones that make a claim.

*A statement is a sentence that is either true or false.*

::: {#def-statement}
[Statement]

A **statement** is a declarative sentence that is **either true or false**, and not both.
:::

In words: a statement makes a claim, and the claim is either correct or incorrect. The definition asks that one of the two is the case. It does **not** ask that we know which one. A statement whose truth nobody has settled is still a statement.

::: {#exm-statements}
[Statements and nonstatements]

Decide which of the following are statements.

::: {.enumerate options="label=(\alph*)"}
1. \( 7 \) is a prime number.
2. \( 0.999 > 1 \).
3. There are infinitely many primes \( p \) for which \( p + 2 \) is also prime.
4. Is \( 2^{11} - 1 \) prime?
5. \( x > 2 \).
6. \( 3 > 2 \).
:::
:::

::: {.solution}
(a) This is a statement, and it is true.

(b) This is a statement, and it is false. A false sentence is as much a statement as a true one.

(c) This is a statement. It is the twin prime conjecture, and at the time of writing nobody knows whether it is true. It is certainly true or false, which is all the definition asks.

(d) This is a question, so it is not a statement. The sentence "\( 2^{11} - 1 \) is prime" is a statement, and a false one, since \( 2^{11} - 1 = 2047 = 23 \cdot 89 \).

(e) This is not a statement. Whether it is true depends on what \( x \) is: it is true when \( x = 3 \) and false when \( x = 0 \), and as written nothing says which. Such a sentence is called an **open sentence**.

(f) This is the sentence of (e) with \( x \) replaced by \( 3 \), and it is a true statement.
:::

Items (e) and (f) differ by one symbol, and the difference is the whole point. The open sentence \( x > 2 \) becomes a statement in two ways. We can put a number in for \( x \), as in (f). Or we can say which \( x \) we mean in some other way, as in "for every real number \( x \), \( x > 2 \)" (a false statement) or "for some real number \( x \), \( x > 2 \)" (a true one). The words "for every" and "for some" are the **quantifiers**, and they are the subject of Chapter 4.

Mathematics is full of open sentences, and we cannot wait until Chapter 4 to use them. So this chapter adopts a convention. When an example says "let \( x \) be a real number" and then talks about \( x \), the letter \( x \) names **one fixed** number, not further specified. Every sentence about that \( x \) is then a statement, true or false according to which number \( x \) is. "Let \( x \) be a real number with \( x > 2 \); then \( x^2 > 4 \)" is an argument about one number, which happens to work whatever the number is. Chapter 4 explains why an argument of that kind proves a statement about every \( x \) at once.

::: {.remark}
The book reserves the words "proposition" and "theorem" for proved results, so it calls the sentences of logic **statements**. Other books call them propositions, which is where the name **propositional logic**, for what this chapter and the next study, comes from.
:::

## The connectives

Most statements in mathematics are built from smaller ones. "\( 0 < x \) and \( x < 1 \)" is built from "\( 0 < x \)" and "\( x < 1 \)" with the word "and". "If \( n^2 \) is even, then \( n \) is even" is built from two statements with "if … then". The words that do the building are the **connectives**. A statement built from smaller statements by a connective is **compound**; one that is not is **atomic**. For this chapter, "\( x > 0 \)" is atomic: it has an inner structure, a number and an order, but no connective joins parts of it.

We write \( P \), \( Q \), \( R \), \( S \) for statements whose inner structure we are ignoring. They stand for **arbitrary** statements, atomic or compound. There are five connectives. In the last column of the table, \( x \) is a real number, \( P \) is "\( x > 0 \)", and \( Q \) is "\( x < 1 \)".

| Symbol | Name | Read | Example |
|--------|------------|---------------------|--------------------------------|
| \( P \wedge Q \) | conjunction | \( P \) and \( Q \) | \( x > 0 \) and \( x < 1 \), that is, \( 0 < x < 1 \) |
| \( P \vee Q \) | disjunction | \( P \) or \( Q \) | \( x > 0 \) or \( x < 1 \) |
| \( P \to Q \) | implication | if \( P \), then \( Q \) | if \( x > 0 \), then \( x < 1 \) |
| \( P \leftrightarrow Q \) | biconditional | \( P \) if and only if \( Q \) | \( x > 0 \) if and only if \( x < 1 \) |
| \( \neg P \) | negation | not \( P \) | \( x \) is not positive, that is, \( x \le 0 \) |

To the five connectives we add one statement with no parts at all, written \( \bot \) and read "contradiction". It stands for a statement that is false however things stand: \( 0 = 1 \) will do. A proof that reaches \( \bot \) has shown that the situation it was working in cannot occur. That is the heart of proof by contradiction, and Chapter 2 gives \( \bot \) its rules.

In \( P \to Q \), the statement \( P \) is the **hypothesis** (or antecedent) and \( Q \) the **conclusion** (or consequent). English has many ways of saying \( P \to Q \): "\( P \) implies \( Q \)", "\( Q \) if \( P \)", "\( Q \) whenever \( P \)", "\( P \) only if \( Q \)", "\( P \) is sufficient for \( Q \)", and "\( Q \) is necessary for \( P \)" all say the same thing, and the exercises ask you to see why. "If and only if" is often shortened to **iff**.

Several English words become \( \wedge \): "but", "although", and "while" all assert both parts, and add a tone of contrast that logic ignores. "\( 2 \) is prime but not odd" is a conjunction. So is "neither … nor", in disguise: "\( 9 \) is neither even nor prime" asserts that \( 9 \) is not even **and** that \( 9 \) is not prime, which is \( \neg P \wedge \neg Q \) with \( P \): "\( 9 \) is even" and \( Q \): "\( 9 \) is prime".

Chained inequalities are conjunctions in disguise too. \( 0 < x < 1 \) abbreviates \( (0 < x) \wedge (x < 1) \), and \( a \le b \le c \) abbreviates \( (a \le b) \wedge (b \le c) \). The symbol \( \le \) itself hides a disjunction: \( a \le b \) means \( (a < b) \vee (a = b) \). And \( a \ne b \) is the negation \( \neg(a = b) \). All three facts are used often in the sections that follow.

In theorem statements the book writes \( \Rightarrow \) and \( \iff \), as mathematicians usually do, and in running prose it says "implies" and "if and only if". The arrows \( \to \) and \( \leftrightarrow \) are kept for the formal derivations that start in the next section. Nothing but typography separates the two pairs.

::: {.warning}
In everyday English, "or" is often exclusive: "soup or salad" on a menu means one but not both. In mathematics, \( P \vee Q \) is **inclusive**: it is true when \( P \) is true, when \( Q \) is true, and when both are. For a real number \( x \), "\( x \ge 0 \) or \( x \le 0 \)" is true whatever \( x \) is; at \( x = 0 \) both parts are true, and that does not spoil it. An exclusive "or" must be said in full: "\( P \) or \( Q \), but not both", which is \( (P \vee Q) \wedge \neg (P \wedge Q) \).
:::

::: {.warning}
The word "if" means different things in a theorem and in a definition. In a theorem, "if \( P \), then \( Q \)" is one direction only: "if \( n \) is divisible by \( 4 \), then \( n \) is even" is true, and its converse is false at \( n = 2 \). In a definition, "a number is **even** if it is twice an integer" is meant as "if and only if": a number that is not twice an integer is not called even. Section 2.4 explains this convention of language.
:::

## Translating a sentence

Translating into symbols is a skill of its own, best learned slowly, in three steps. Find the atomic statements, the smallest pieces that make a claim, and give each a letter. Find the connectives, whatever English words carry them. Then decide how the pieces group.

Take "if \( 12 \) is divisible by \( 3 \) and by \( 4 \), then \( 12 \) is divisible by \( 6 \)". The atomic statements are \( P \): "\( 12 \) is divisible by \( 3 \)", \( Q \): "\( 12 \) is divisible by \( 4 \)" and \( R \): "\( 12 \) is divisible by \( 6 \)". English lets "\( 12 \) is divisible by" be said once and shared; logic writes each piece in full. The words "if … then" carry \( \to \), and "and" carries \( \wedge \). The hypothesis is everything between "if" and "then", so the statement is \( (P \wedge Q) \to R \), not \( P \wedge (Q \to R) \). The second reading would claim \( P \) outright, and the English sentence claims nothing outright: it only says what follows from what.

A second example shows a connective hidden inside a word. Let \( x \) be a real number, and read "\( x \) is nonzero, and if \( x \) is positive, then so is \( x^3 \)". With \( Z \): "\( x = 0 \)", \( P \): "\( x > 0 \)" and \( C \): "\( x^3 > 0 \)", "nonzero" is \( \neg Z \), and the whole sentence is \( \neg Z \wedge (P \to C) \). Letters that recall their statements, as here, often help; a letter is only a name.

In both examples the English word order is a poor guide to the grouping. When in doubt, ask of each connective: which two statements does it join?

## Reading a statement: precedence and the main connective

Connectives can be combined without limit, and a string of symbols is only useful if it can be read in one way. Consider \( \neg P \wedge Q \). Does it deny \( P \) and then assert \( Q \), or does it deny the whole of \( P \wedge Q \)? These are different claims. With \( P \): "\( n \) is even" and \( Q \): "\( n > 0 \)", the first says that \( n \) is odd and positive, while the second says only that \( n \) is not a positive even number, which \( n = -4 \) satisfies.

Parentheses settle every such question, and a few conventions let us drop the ones that would only add clutter.

::: {.enumerate options="label=(\arabic*)"}
1. \( \neg \) binds most tightly: it applies to the smallest complete statement that follows it. So \( \neg P \wedge Q \) means \( (\neg P) \wedge Q \), and to deny \( P \wedge Q \) we write \( \neg(P \wedge Q) \).
2. \( \wedge \) and \( \vee \) bind more tightly than \( \to \) and \( \leftrightarrow \). So \( P \wedge Q \to R \) means \( (P \wedge Q) \to R \).
3. \( \to \) groups to the right: \( P \to Q \to R \) means \( P \to (Q \to R) \). The book usually writes these parentheses anyway.
4. In a mixture of \( \wedge \) and \( \vee \), or of \( \to \) and \( \leftrightarrow \), the parentheses are always written. We never write \( P \wedge Q \vee R \).
:::

Convention (3) is the natural one: a statement "if \( P \), then if \( Q \), then \( R \)" is common, and \( (P \to Q) \to R \), whose hypothesis is itself an implication, is rare. Chapter 3 turns "a statement built from letters by connectives" into an exact definition (@def-formula) and proves that every such statement can be read in only one way (@thm-unique-readability). In this chapter we parse by eye.

The conventions only decide where parentheses may be dropped. The next definition names the one piece of information that reading a statement is for.

::: {#def-main-connective}
[Main Connective]

The **main connective** of a compound statement is the connective applied **last** when the statement is built up from its parts. An atomic statement has no main connective.
:::

The main connective is found by undoing the construction from the outside. Take
\[
\neg(P \wedge Q) \to R .
\]
By convention (1), the \( \neg \) applies only to the parenthesized \( P \wedge Q \); by convention (2), the \( \to \) takes everything to its left as its hypothesis. So the last step joined \( \neg(P \wedge Q) \) and \( R \) with \( \to \), and \( \to \) is the main connective. Its hypothesis \( \neg(P \wedge Q) \) has main connective \( \neg \), applied to \( P \wedge Q \), whose main connective is \( \wedge \). The construction can be drawn as a tree, with the main connective at the root and the letters at the leaves.

\begin{center}
\begin{tikzpicture}[level distance=11mm, sibling distance=26mm, every node/.style={font=\normalsize}]
  \node {$\to$}
    child { node {$\neg$}
      child { node {$\wedge$}
        child { node {$P$} }
        child { node {$Q$} }
      }
    }
    child { node {$R$} };
\end{tikzpicture}
\end{center}

Reading the tree from the top: the statement is an implication; its hypothesis is a negation; what is negated is a conjunction. Reading from the bottom retraces how the statement was built. A one-symbol change moves the root: in \( \neg(P \wedge Q \to R) \) the parentheses make the whole implication the thing denied, and the main connective is \( \neg \).

Here is a second statement taken apart the same way, this time with every step said aloud:
\[
P \vee Q \to R \wedge S .
\]
There is no \( \neg \), so convention (1) does nothing. By convention (2), \( \vee \) and \( \wedge \) bind before \( \to \), so the statement is \( (P \vee Q) \to (R \wedge S) \), and its main connective is \( \to \). The hypothesis \( P \vee Q \) has main connective \( \vee \) and the conclusion \( R \wedge S \) has main connective \( \wedge \). With \( x \) a real number, \( P \): "\( x > 1 \)", \( Q \): "\( x < -1 \)", \( R \): "\( x^2 > 1 \)" and \( S \): "\( x^4 > 1 \)", it reads: if \( x > 1 \) or \( x < -1 \), then \( x^2 > 1 \) and \( x^4 > 1 \).

The main connective is not grammar for its own sake. It is the first thing to find when a proof has to be written, because it decides how the proof begins. To prove "if \( 0 < x < 1 \), then \( x^2 < x \)", whose main connective is \( \to \), a proof starts "Suppose \( 0 < x < 1 \)." To prove "\( x^2 + 1 > 0 \) and \( x^2 + 1 \ne 0 \)", whose main connective is \( \wedge \), a proof has two parts, one for each side. Section 1.3 gives this habit a name, each later section of this chapter adds to it, and Section 2.6 turns it into a method for finding proofs.

::: {.check}
Find the main connective of each statement.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg P \vee Q \)
2. \( \neg (P \vee Q) \)
3. \( (P \to Q) \wedge (Q \to P) \)
:::
:::

::: {.solution}
(a) \( \vee \): by convention (1) the \( \neg \) applies only to \( P \), so the statement is the disjunction of \( \neg P \) and \( Q \).

(b) \( \neg \): the parentheses make the whole disjunction the thing denied.

(c) \( \wedge \): each parenthesized implication is complete, and the last step joins them with "and".
:::

## The form of an argument

Here are two short arguments, one about integers and one about real numbers.

> If \( n \) is odd, then \( n^2 \) is odd. And \( n \) is odd. So \( n^2 \) is odd.

> If \( x > 2 \), then \( x^2 > 4 \). And \( x > 2 \). So \( x^2 > 4 \).

They are about different things, and yet they are the same argument. Write \( P \) for "\( n \) is odd" and \( Q \) for "\( n^2 \) is odd" in the first, and \( P \) for "\( x > 2 \)" and \( Q \) for "\( x^2 > 4 \)" in the second. Both then read: from \( P \to Q \) and \( P \), conclude \( Q \). What makes the step correct has nothing to do with odd numbers or squares. It depends only on the shape of the premises, on the fact that one of them is an implication and the other is its hypothesis. That shape is the argument's **form**, and the part of the argument that lives in the letters is its **content**.

*Logic studies the forms of arguments, not their content.*

Separating the two has a payoff. Once a form has been shown to be correct, every argument of that form is correct, whatever its content; we check the form once and use it forever. The notation for a claim about forms is the following.

::: {#def-sequent}
[Sequent]

Let \( P_1, \dots, P_n \) and \( Q \) be statements, where \( n \ge 0 \). The **sequent**
\[
P_1, \dots, P_n \vdash Q
\]
is the **claim** that \( Q \) can be derived from \( P_1, \dots, P_n \) by the rules of logic. The statements \( P_1, \dots, P_n \) are its **premises** and \( Q \) is its **conclusion**. When \( n = 0 \) we write \( \vdash Q \).
:::

The symbol \( \vdash \) is called the turnstile, and \( P_1, \dots, P_n \vdash Q \) is read "\( P_1 \) to \( P_n \) prove \( Q \)". A sequent is not an argument, and it is not true merely because its conclusion is true: it claims that a certain kind of object, a derivation from those premises to that conclusion, exists. The next section says what a derivation is, and so exactly when the claim holds. It is proved the way any existence claim is proved, by exhibiting one. The two arguments above both have the form
\[
P \to Q, \ P \vdash Q ,
\]
and the rule \( \rulename{{\to}E} \) of Section 1.4 says that this sequent holds.

The case \( n = 0 \) is the degenerate one, and it matters. \( \vdash Q \) claims that \( Q \) can be derived from **no** premises at all: that the rules alone produce it. Such statements exist, and Section 1.5 derives the first of them.

::: {.check}
Which of the following arguments has the same form as "If \( n \) is divisible by \( 6 \), then \( n \) is divisible by \( 3 \). And \( n \) is divisible by \( 6 \). So \( n \) is divisible by \( 3 \)"?

::: {.enumerate options="label=(\roman*)"}
1. If \( n \) is divisible by \( 4 \), then \( n \) is even. And \( n \) is even. So \( n \) is divisible by \( 4 \).
2. If \( x > 0 \) and \( y > 0 \), then \( xy > 0 \). And \( x > 0 \) and \( y > 0 \). So \( xy > 0 \).
:::
:::

::: {.solution}
The given argument has the form \( P \to Q, \ P \vdash Q \).

(i) does not. With \( P \): "\( n \) is divisible by \( 4 \)" and \( Q \): "\( n \) is even", it has the form \( P \to Q, \ Q \vdash P \): the second premise is the conclusion of the implication, not its hypothesis. This form is not correct, and \( n = 2 \) shows it. The first premise is true for every integer, since a multiple of \( 4 \) is \( 4k = 2(2k) \); the second is true, since \( 2 \) is even; yet \( 2 \) is not divisible by \( 4 \).

(ii) has the same form, with \( P \) the compound statement "\( x > 0 \) and \( y > 0 \)" and \( Q \) the statement "\( xy > 0 \)". A letter may stand for a compound statement.
:::

## Each connective, two rules

We now come to the idea that organizes this chapter and the next. Think about what a mathematician does with the word "and". There are exactly two things to do with it.

- To **prove** a statement of the form \( P \wedge Q \), prove \( P \) and prove \( Q \).
- To **use** a statement of the form \( P \wedge Q \) that is already known, take either half.

Nobody needs to be taught these two moves. They are also, and this is the point, **all** there is to know about "and" for the purpose of writing proofs. Every other fact about \( \wedge \), such as that \( P \wedge Q \) and \( Q \wedge P \) say the same thing, follows from the two moves, as Section 1.3 shows. The first move is called the **introduction rule** for \( \wedge \), written \( \rulename{\wedge I} \), because it is how a \( \wedge \) gets into a proof. The second is the **elimination rule**, \( \rulename{\wedge E} \), because it is how a \( \wedge \) is taken apart.

The table below is an informal preview. Section 1.3 states these two rules exactly, as patterns of lines.

| Rule | What it allows | You write |
|------|---------------------------|--------------------------------------|
| \( \rulename{\wedge I} \) | from \( P \) and \( Q \), conclude \( P \wedge Q \) | "We have shown \( x > 0 \) and \( x < 1 \). Hence \( 0 < x < 1 \)." |
| \( \rulename{\wedge E} \) | from \( P \wedge Q \), conclude \( P \); also \( Q \) | "Since \( 0 < x < 1 \), in particular \( x > 0 \)." |

Every connective works the same way. Each comes with introduction rules, saying how to prove a statement with that main connective, and elimination rules, saying what a statement with that main connective lets us conclude. The rules for \( \wedge \) come in Section 1.3, those for \( \to \) in Sections 1.4 and 1.5, and those for \( \vee \) in Sections 1.6 and 1.7. The rules for \( \neg \), \( \bot \), and \( \leftrightarrow \), and one more rule for proof by contradiction, which stands apart from the others, are the subject of Chapter 2. Two slogans summarize the plan.

*Each connective comes with a way to prove it and a way to use it.*

*A proof is a chain in which every line is a premise, an assumption, or one application of a rule.*

The rules are chosen so that they never lead from true statements to a false one. For \( \wedge \) this is plain: if \( P \) and \( Q \) are both true, so is \( P \wedge Q \), and if \( P \wedge Q \) is true, so is \( P \). Chapter 3 proves it for every rule at once (@thm-soundness); the theorem is called soundness.

The second slogan is what makes a proof possible to check. Finding a proof may need an idea. Checking one needs none: go through it line by line and ask of each line which rule produced it and whether that rule was applied to lines that really are there. A reader who has lost the thread of a long argument can always fall back on that question, and it is the question to ask of Argument B. In Part 0 we ask it out loud; Chapter 5 shows how the same rules run silently underneath ordinary written proofs.

The order of these chapters differs from that of many logic books, which begin with truth tables: tables listing, for instance, when \( P \to Q \) is true. There, the row "if \( P \) is false, then \( P \to Q \) is true" has to be accepted as a convention, and it looks arbitrary. Here, that fact comes out of how proofs work (Section 2.1), and the tables arrive in Chapter 3, which proves that the rules and the tables agree (@cor-derivable-iff-valid).

We can now say what we will make of Argument B. Its claim has the form \( Q \to P \), with \( Q \): "\( n^2 \) is even" and \( P \): "\( n \) is even", and B's reasoning runs from \( P \) to \( Q \). Section 1.5 names the error as a misuse of the rule for proving an implication: B began from the conclusion \( P \) where the rule asks it to begin from the hypothesis \( Q \). And to repair B without new ideas, one would have to pass from "if \( n \) is even, then \( n^2 \) is even" and "\( n^2 \) is even" to "\( n \) is even", the form \( P \to Q, \ Q \vdash P \) of the Quick check above. Chapter 3 proves that this pattern cannot be derived from the rules at all: no derivation leads from \( P \to Q \) and \( Q \) to \( P \) (@cor-refuting-row).

## What comes next

The rest of this chapter is built to a pattern, and knowing the pattern in advance makes the sections easier to read.

Section 1.2 says what a derivation looks like and how to read one. It uses no logic at all. Its only rules are two facts about inequalities, borrowed for practice, so that the **format** can be seen on its own: numbered lines, premises at the top, and a justification on every line.

Each of Sections 1.3 to 1.7 then introduces **one** rule, except that Section 1.3 introduces the pair of rules for "and", which are so simple that the two are one idea. The rule is defined by its **pattern**, a small picture of the lines it needs and the line it writes. The pattern is read clause by clause, since each clause is there for a reason and each is broken by some tempting mistake. Then come several derivations with the new rule, from the smallest possible to a few lines longer, and each is preceded by an *Idea* that says why each rule was chosen. Each section also shows its rule at work in a proof about numbers, where the rule is usually invisible.

The Ideas ask two questions, again and again, and it is worth learning them now.

- *What does the goal's main connective ask for?* The statement we are trying to reach decides the last step of the derivation, and so its overall shape.
- *What does an available line's main connective let me do?* A statement we already have decides what we can get out of it.

The first question works backwards, from the bottom of a derivation; the second works forwards, from the top. Section 1.3 gives the two directions their names, and every later section adds its rule to one of them: an introduction rule answers the first question, an elimination rule the second.

## Exercises

### A. Check your understanding

::: {#exr-statements-and-connectives-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of a statement. Is "\( 10^{100} + 1 \) is prime" a statement? For a real number \( x \), is "\( x^2 - 1 = 0 \)" a statement? Is "\( 0^2 - 1 = 0 \)"?
2. With \( P \): "\( n \) is even" and \( Q \): "\( n \) is prime", write "\( n \) is prime but not even" in symbols.
3. Find the main connective of \( P \wedge Q \to \neg R \), and write the statement with all its parentheses.
4. True or false, with a reason: if \( P \) and \( Q \) are both true, then \( P \vee Q \) is false.
5. Let \( x \) and \( y \) be real numbers. Write the form of the argument "\( x > 0 \) and \( y > 0 \); so \( y > 0 \) and \( x > 0 \)" as a sequent, saying what each letter stands for.
6. Which of \( \wedge \), \( \vee \), \( \to \) is the main connective of \( (P \vee Q) \wedge (Q \to R) \)? Using the preview table of "Each connective, two rules", say what a proof of this statement must do, and name the rule that Section 1.3 will state for it.
:::
:::

::: {.solution}
(a) A statement is a declarative sentence that is either true or false, and not both (@def-statement). Yes: \( 10^{100} + 1 \) is a definite integer, so it either is prime or is not. The definition does not ask us to know which. With \( x \) fixed, as in this chapter's convention, "\( x^2 - 1 = 0 \)" is a statement about that one number: true if \( x \) is \( 1 \) or \( -1 \), false otherwise. Without the convention it would be an open sentence. The sentence "\( 0^2 - 1 = 0 \)" is a statement outright, and it is false, since \( 0^2 - 1 = -1 \).

(b) \( Q \wedge \neg P \). The word "but" is a conjunction.

(c) Convention (2) groups \( P \wedge Q \) before \( \to \) acts, and convention (1) lets \( \neg \) take only \( R \). So the statement is \( (P \wedge Q) \to (\neg R) \), and its main connective is \( \to \) (@def-main-connective).

(d) False. The mathematical "or" is inclusive, so \( P \vee Q \) is true when both parts are true.

(e) With \( P \): "\( x > 0 \)" and \( Q \): "\( y > 0 \)", the form is \( P \wedge Q \vdash Q \wedge P \) (@def-sequent). Section 1.3 derives it.

(f) \( \wedge \): each parenthesized part is complete, and the last step joins them with "and". So a proof of it has two parts: it proves \( P \vee Q \), and it proves \( Q \to R \). The rule that puts the two parts together is \( \rulename{\wedge I} \). This is the first question of "What comes next", asked before any rule has been stated exactly: the goal's main connective decides the last step.
:::

### B. Practice

::: {#exr-statements-and-connectives-b1}
[B1: Translating analysis]

Translate each sentence into symbols, using the atomic statements given. You do not need to know what the words mean; only the grammar matters.

::: {.enumerate options="label=(\alph*)"}
1. "\( f \) is continuous at \( a \) but not differentiable there", with \( C \): "\( f \) is continuous at \( a \)" and \( D \): "\( f \) is differentiable at \( a \)".
2. "If the sequence \( (a_n) \) converges, it is bounded", with \( V \): "\( (a_n) \) converges" and \( B \): "\( (a_n) \) is bounded".
3. "\( x \) is rational or irrational", with \( R \): "\( x \) is rational". (A real number is irrational when it is not rational.)
4. "The set \( F \) is closed if and only if its complement is open", with \( K \): "\( F \) is closed" and \( U \): "the complement of \( F \) is open".
:::
:::

::: {.solution}
(a) \( C \wedge \neg D \). "But" asserts both parts, and "not differentiable there" is the negation of \( D \).

(b) \( V \to B \). The pronoun "it" refers to \( (a_n) \), so the conclusion is the statement \( B \).

(c) \( R \vee \neg R \). "Irrational" means "not rational", so the second part is \( \neg R \), not a new atomic statement.

(d) \( K \leftrightarrow U \).
:::

::: {#exr-statements-and-connectives-b2}
[B2: Parsing]

For each statement, insert all the parentheses that the conventions allow us to omit, and name the main connective.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg P \to Q \)
2. \( P \vee \neg Q \leftrightarrow \neg R \)
3. \( \neg\neg P \wedge (Q \to R) \)
4. \( P \to Q \to \neg R \)
:::

Then let \( x \) and \( y \) be real numbers, with \( P \): "\( x > 0 \)", \( Q \): "\( y > 0 \)" and \( R \): "\( xy > 0 \)". Write \( P \wedge Q \to R \) as an English sentence, and say whether it is true whatever the numbers \( x \) and \( y \) are.
:::

::: {.solution}
(a) \( (\neg P) \to Q \), main connective \( \to \).

(b) \( (P \vee (\neg Q)) \leftrightarrow (\neg R) \), main connective \( \leftrightarrow \). Each \( \neg \) applies to the single letter after it, and \( \vee \) binds more tightly than \( \leftrightarrow \).

(c) \( (\neg(\neg P)) \wedge (Q \to R) \), main connective \( \wedge \). The first \( \neg \) applies to the statement \( \neg P \), which is the smallest complete statement following it.

(d) \( P \to (Q \to (\neg R)) \), main connective the first \( \to \). By convention (3), \( \to \) groups to the right.

The statement \( P \wedge Q \to R \) is \( (P \wedge Q) \to R \): "if \( x > 0 \) and \( y > 0 \), then \( xy > 0 \)". It is true for all real \( x \) and \( y \), since the product of two positive numbers is positive.
:::

### C. Going deeper

::: {#exr-statements-and-connectives-c1}
[C1: "Only if" and "unless"]

Let \( P \) and \( Q \) be statements.

::: {.enumerate options="label=(\alph*)"}
1. Explain why "\( P \) only if \( Q \)" means \( P \to Q \), and not \( Q \to P \). *(Ask: which situation would make "\( P \) only if \( Q \)" false?)*
2. Explain why "\( P \) unless \( Q \)" means \( \neg Q \to P \).
3. Let \( x \) be a real number. Decide whether each sentence is true for every real \( x \). Justify your answer, giving a value of \( x \) that makes it false where there is one.
    - "\( x^2 = 4 \) if \( x = 2 \)."
    - "\( x^2 = 4 \) only if \( x = 2 \)."
    - "\( x^2 > 0 \) unless \( x = 0 \)."
:::
:::

::: {.solution}
(a) "\( P \) only if \( Q \)" says that \( P \) does not happen without \( Q \). It is broken exactly when \( P \) holds and \( Q \) fails. That is also exactly when \( P \to Q \) is broken: an implication promises \( Q \) whenever \( P \), and the promise fails only when \( P \) holds without \( Q \). So the two say the same thing. By contrast, \( Q \to P \) is broken when \( Q \) holds and \( P \) fails, a different situation. For example, "a number is divisible by \( 4 \) only if it is even" is true, while "a number is even only if it is divisible by \( 4 \)" is false (take \( 2 \)).

(b) "\( P \) unless \( Q \)" says that \( P \) holds in every situation except possibly those where \( Q \) holds. So once we know that \( Q \) fails, we may conclude \( P \), which is \( \neg Q \to P \). For instance, "the equation \( ax = 1 \) has a solution unless \( a = 0 \)" says: if \( a \ne 0 \), then \( ax = 1 \) has a solution.

(c) The first sentence is \( (x = 2) \to (x^2 = 4) \). It is true for every \( x \): when \( x = 2 \), \( x^2 = 4 \), and when \( x \ne 2 \) it promises nothing.

The second is \( (x^2 = 4) \to (x = 2) \), the same two parts in the opposite direction. It is false for \( x = -2 \), where \( x^2 = 4 \) but \( x \ne 2 \).

The third is \( \neg(x = 0) \to (x^2 > 0) \), by (b). It is true for every \( x \): a nonzero real number is positive or negative, and in both cases its square is positive.

The first two sentences differ by one word, and they are implications in opposite directions. Confusing them is exactly the mistake of Argument B at the start of this section.
:::

::: {#exr-statements-and-connectives-c2}
[C2: Necessary and sufficient]

Let \( x \) be a real number.

::: {.enumerate options="label=(\alph*)"}
1. Write "\( x > 1 \) is sufficient for \( x^2 > 1 \)" and "\( x > 1 \) is necessary for \( x^2 > 1 \)" as implications.
2. Decide which of the two is true for every real \( x \), and give a value of \( x \) that makes the other false.
3. Find a condition on \( x \), written with \( \vee \), that is both necessary and sufficient for \( x^2 > 1 \). You may use that \( x^2 > 1 \) exactly when \( \abs{x} > 1 \), where \( \abs{x} \) is \( x \) if \( x \ge 0 \) and \( -x \) if \( x < 0 \).
:::
:::

::: {.solution}
(a) "\( P \) is sufficient for \( Q \)" means that \( P \) is enough to guarantee \( Q \), that is, \( P \to Q \). "\( P \) is necessary for \( Q \)" means that \( Q \) cannot hold without \( P \), that is, \( Q \to P \). So the two sentences are \( (x > 1) \to (x^2 > 1) \) and \( (x^2 > 1) \to (x > 1) \).

(b) The first is true for every \( x \): if \( x > 1 \), then \( x > 0 \), so \( x^2 = x \cdot x > 1 \cdot x = x > 1 \), where multiplying \( x > 1 \) by the positive number \( x \) keeps the inequality. The second is false for \( x = -2 \): then \( x^2 = 4 > 1 \), but \( x < 1 \).

(c) \( (x > 1) \vee (x < -1) \). It is sufficient: if \( x > 1 \), then \( \abs{x} = x > 1 \), and if \( x < -1 \), then \( \abs{x} = -x > 1 \); either way \( x^2 > 1 \). It is necessary: if \( x^2 > 1 \), then \( \abs{x} > 1 \), and \( \abs{x} \) is \( x \) or \( -x \), so \( x > 1 \) or \( -x > 1 \), the latter meaning \( x < -1 \).
:::

<!-- dependency ledger
exm-statements (example): 2^11 - 1 = 2047 = 23 * 89, and 0.999 < 1 | inline arithmetic (checked by verify/ch01/exm-statements.py)
exm-statements (example): the twin prime conjecture is open | status of an open problem at the time of writing; not used in any argument
def-statement (example): the opening's Argument A uses that every integer is even or odd, and that no integer is both | school algebra, allowed as a fact in examples by the Chapter 1 blueprint (Allowed prerequisites); ch07 (promised); the hook is an illustration, and no proof here uses it
def-main-connective (example): the connective table before it: every real number is positive or less than 1; 0 < 1/2 < 1; 2 > 1 | school algebra (Allowed prerequisites); ch11 (promised)
def-sequent (example): the Quick check's witness n = 2 (2 is even and not divisible by 4; a multiple of 4 is even) | inline arithmetic (checked by verify/ch01/def-sequent.py)
exr-statements-and-connectives-a1 (solution): x^2 - 1 = 0 exactly when x = 1 or x = -1; 0^2 - 1 = -1 | school algebra (Allowed prerequisites); ch11 (promised)
exr-statements-and-connectives-b2 (solution): a product of two positive reals is positive | school algebra (Allowed prerequisites); ch11 (promised)
exr-statements-and-connectives-c1 (solution): the square of a non-zero real is positive; (-2)^2 = 4 | school algebra (Allowed prerequisites); ch11 (promised); checked by verify/ch01/exr-statements-and-connectives-c1.py
exr-statements-and-connectives-c2 (solution): multiplying an inequality by a positive number keeps it; x^2 > 1 iff |x| > 1 (given in the item) | school algebra (Allowed prerequisites); ch11 (promised); checked by verify/ch01/exr-statements-and-connectives-c2.py
-->
