# Formulas as Objects

Chapter 2 ended on a question that no derivation can answer. We show that a sequent holds by writing a derivation of it; but how could we show that one does **not** hold, that no derivation of \( Q \to P \) from \( P \to Q \) exists, however long and however clever? This chapter answers the question, and the answer is a theorem about **every** derivation of **every** formula. A theorem about every formula needs, first of all, an exact description of what a formula is. This section gives it. It defines formulas, draws them as trees, names their parts, and says how the shorthand of Chapters 1 and 2 fits in. Nothing is yet proved about all formulas at once; the tool for that is the next section's.

## Why formulas must become objects

Here is the theorem that Section 3.5 proves, stated loosely:

> If \( \psi \) can be derived from premises \( \Gamma \), then \( \psi \) is true in every situation in which all the premises are true.

Read it as a mathematician reads a statement about all integers. "For every integer \( n \), \( n^2 - n \) is even" can be proved only by someone who knows what an integer is: every integer is even or odd, and each kind can be handled. A proof needs a way to take hold of an arbitrary object of the kind the statement is about. The loose theorem above is about arbitrary derivations, and a derivation is a list of formulas, so the proof will need a way to take hold of an arbitrary formula.

Chapters 1 and 2 never needed one. There we read statements by eye: we found the main connective of \( \neg(P \wedge Q) \to R \) (@def-main-connective) by looking, and we drew its tree by hand. That is fine for one statement at a time. It is useless for a claim about all statements, because "all the strings we would recognize as statements" is not a description anyone can reason from. So we now do for formulas what Chapter 11 will do for the real numbers: say exactly which objects we mean, in a form that later proofs can use.

The description has three parts. First, the **alphabet**, the symbols formulas are written with. Second, the **formation rules**, which say how formulas are built. Third, a closing clause saying that **nothing else** is a formula. The third is the one that is easy to forget and that makes everything else work.

## The alphabet

Formulas are strings of symbols. A **string** is a finite list of symbols written one after another, and its **length** is the number of symbols in it. The symbols are these.

- **Atoms:** \( p, q, r, p_1, p_2, p_3, \dots \), infinitely many of them. Each atom is **one** symbol: \( p_1 \) is a single symbol whose name happens to carry a subscript, not the two symbols \( p \) and \( 1 \).
- **The constant** \( \bot \), read "contradiction", as in Chapter 1.
- **The connectives:** \( \neg \) (the only one that takes one part) and \( \wedge, \vee, \to, \leftrightarrow \) (the **binary** connectives, which take two).
- **The parentheses** \( ( \) and \( ) \).

An atom plays the part that a letter played in Chapters 1 and 2: a statement whose inner structure we ignore. In those chapters the letters were capitals, \( P, Q, R \), and they stood for **arbitrary** statements, atomic or compound. From now on we keep two kinds of letter apart, because the theorems of this chapter need the difference.

- An **atom** \( p, q, r, \dots \) is a symbol of the language. It occurs in formulas.
- A **metavariable** \( \varphi, \psi, \chi \) (phi, psi, chi) is a name we use when talking **about** formulas: "let \( \varphi \) be a formula". It never occurs in a formula. Chapter 1 already used these three letters in exactly this way, in the schemas of its rules (@def-rule-schema).

We write \( \Gamma \) and \( \Delta \) (capital gamma and delta) for finite lists of formulas, as in the sequents of Chapter 1 (@def-derivable). The capitals \( P, Q, R \) of Chapters 1 and 2 were stand-ins for arbitrary formulas; the last part of this section says exactly what that means.

We use \( \circ \) as a metavariable for a binary connective: "\( (\varphi \circ \psi) \)" means any one of \( (\varphi \wedge \psi) \), \( (\varphi \vee \psi) \), \( (\varphi \to \psi) \), \( (\varphi \leftrightarrow \psi) \). This saves writing four clauses where one will do.

## Formulas

Chapter 1 described a statement as something "built from smaller ones by a connective". The definition below says exactly how the building goes. It is an **inductive definition**: it names the starting pieces, names the ways of building new formulas from old, and then closes the door on everything else.

*A formula is a string built from atoms and \( \bot \) by the connectives, one step at a time, with a pair of parentheses around every binary step.*

::: {#def-formula}
[Formula]

The **formulas** are the strings given by the following clauses.

::: {.enumerate options="label=(F\arabic*)"}
1. Every atom is a formula, and \( \bot \) is a formula.
2. If \( \varphi \) is a formula, then \( \neg\varphi \) is a formula.
3. If \( \varphi \) and \( \psi \) are formulas, then \( (\varphi \wedge \psi) \), \( (\varphi \vee \psi) \), \( (\varphi \to \psi) \) and \( (\varphi \leftrightarrow \psi) \) are formulas.
4. **Nothing else** is a formula: a string is a formula **only if** it is the last entry of a **formation sequence**. A formation sequence is a finite list of strings \( \chi_1, \dots, \chi_m \), with \( m \ge 1 \), in which **every** entry \( \chi_i \) is an atom or \( \bot \), or is \( \neg\chi_j \) for some **earlier** entry \( \chi_j \) (so \( j < i \)), or is \( (\chi_j \circ \chi_l) \) for some earlier entries \( \chi_j \) and \( \chi_l \) (so \( j, l < i \); \( j = l \) is allowed) and some binary connective \( \circ \).
:::
:::

In words, clause by clause.

- *(F1), the starting pieces.* A single atom is a formula, and so is \( \bot \). These are the only formulas of length one.
- *(F2), negation.* Writing \( \neg \) in front of a formula gives a formula. No parentheses are added: \( \neg p \) and \( \neg\neg p \) are formulas, and \( \neg\neg p \) is \( \neg \) in front of the formula \( \neg p \).
- *(F3), the binary connectives.* Writing a binary connective between two formulas **and** wrapping the result in one pair of parentheses gives a formula. The two formulas may be the same: \( (p \wedge p) \) is a formula.
- *(F4), nothing else.* Clauses (F1)–(F3) say which strings **are** formulas. They do not say that other strings are **not**. Clause (F4) does: a formula is exactly something we can reach from atoms and \( \bot \) by finitely many uses of (F2) and (F3), and the formation sequence is the written record of such a reaching.

Two facts about formation sequences are used constantly, and both are immediate from the definition.

First, **every entry of a formation sequence is a formula.** The first \( i \) entries \( \chi_1, \dots, \chi_i \) of a formation sequence are themselves a formation sequence (each entry was built from entries earlier still), and it ends in \( \chi_i \).

Second, **every formula was made by one of the clauses from formulas.** Take a formula \( \chi \) and a formation sequence ending in it. Its last entry \( \chi \) is an atom or \( \bot \), or it is \( \neg\chi_j \), or it is \( (\chi_j \circ \chi_l) \), where the earlier entries \( \chi_j, \chi_l \) are formulas by the first fact. So every formula is an atom, or \( \bot \), or \( \neg\varphi \) for a formula \( \varphi \), or \( (\varphi \circ \psi) \) for formulas \( \varphi, \psi \). We will call this **looking at the last step** of a formula.

Looking at the last step already tells us something about the first symbol. A formula of the form \( \neg\varphi \) begins with \( \neg \), and one of the form \( (\varphi \circ \psi) \) begins with \( ( \) and ends with \( ) \). So:

> **The first-symbol test.** A formula of length one is an atom or \( \bot \). A longer formula begins with \( \neg \) or with \( ( \), and if it begins with \( ( \), it is \( (\varphi \circ \psi) \) for formulas \( \varphi, \psi \) and ends with \( ) \).

(A formula of the form \( \neg\varphi \) has length at least \( 2 \), and one of the form \( (\varphi \circ \psi) \) has length at least \( 5 \), since \( \varphi \) and \( \psi \) each have at least one symbol. So a formula of length one is made by (F1).)

::: {#exm-formation-sequences}
[Formation sequences]

Write down a formation sequence for each of the strings \( p \), \( \bot \), \( \neg\neg q \) and \( ((p \wedge \neg q) \to p) \), which shows that each is a formula.
:::

::: {.solution}
For \( p \), the one-entry list \( p \) is a formation sequence: its only entry is an atom. Likewise the list \( \bot \). These are the degenerate cases, and they matter: a formula need not have been built at all. Every structural argument in the next section has to deal with them.

For \( \neg\neg q \):
\[
q, \quad \neg q, \quad \neg\neg q .
\]
The first entry is an atom; the second is \( \neg \) in front of the first; the third is \( \neg \) in front of the second.

For \( ((p \wedge \neg q) \to p) \):
\[
p, \quad q, \quad \neg q, \quad (p \wedge \neg q), \quad ((p \wedge \neg q) \to p) .
\]
Entries 1 and 2 are atoms. Entry 3 is \( \neg \) in front of entry 2. Entry 4 is \( (\chi_1 \wedge \chi_3) \). Entry 5 is \( (\chi_4 \to \chi_1) \): the atom \( p \) is used twice, and it need be listed only once.

A formula has many formation sequences. We could have listed \( q \) before \( p \), or added entries that are never used, such as \( r \) or \( \neg r \). The definition asks only that **some** formation sequence ends in the string, and nothing in this chapter depends on which one we take.
:::

To show that a string **is** a formula, we exhibit a formation sequence, just as we show that a sequent holds by exhibiting a derivation. To show that a string is **not** a formula, exhibiting is not enough; we need a property that every formula has and the string lacks. The first-symbol test supplies such properties.

::: {#exm-not-formulas}
[Strings that are not formulas]

Show that none of the strings \( p \wedge \to q \), \( (p \wedge q \), \( (\neg p) \) and \( p \wedge q \) is a formula.
:::

::: {.solution}
\( p \wedge \to q \): it has length \( 4 \), so by the first-symbol test a formula would begin with \( \neg \) or \( ( \). It begins with \( p \). Not a formula.

\( (p \wedge q \): it begins with \( ( \), so by the first-symbol test a formula would end with \( ) \). It ends with \( q \). Not a formula. (The missing parenthesis is the whole problem: \( (p \wedge q) \) is a formula.)

\( (\neg p) \): it begins with \( ( \), so a formula would have to be \( (\varphi \circ \psi) \), with the two symbols \( \neg p \) between the parentheses equal to \( \varphi \circ \psi \), and so containing a binary connective. The string \( \neg p \) contains none. Not a formula. The official language puts no parentheses around a negation; (F2) adds none.

\( p \wedge q \): it has length \( 3 \) and begins with \( p \). Not a formula. This one is a surprise at first, since we have written \( p \wedge q \) all along. It is **shorthand** for the formula \( (p \wedge q) \), in the way explained later in this section.
:::

The last two strings are ones Chapter 1 wrote freely, and that is no mistake in Chapter 1. Chapter 1 used a convenient shorthand; the official formulas carry every parenthesis that (F3) puts in and none that it does not. We come back to the shorthand below.

::: {.check}
Which of the following strings are formulas? For each, give a formation sequence or name the test it fails.

::: {.enumerate options="label=(\alph*)"}
1. \( \neg(p \to \bot) \)
2. \( (p \to \neg) \)
3. \( \bot\bot \)
:::
:::

::: {.solution}
*(a)* A formula: \( p, \ \bot, \ (p \to \bot), \ \neg(p \to \bot) \) is a formation sequence.

*(b)* Not a formula. It begins with \( ( \), so it would be \( (\varphi \to \psi) \) with \( \varphi \) the string \( p \) and \( \psi \) the string \( \neg \) (the only binary connective is the \( \to \)). But \( \neg \) is a string of length one that is neither an atom nor \( \bot \), so by the first-symbol test it is not a formula.

*(c)* Not a formula. It has length \( 2 \), so it would begin with \( \neg \) or \( ( \); it begins with \( \bot \).
:::

## Why this definition

Each feature of the definition is there because something breaks without it.

**Without (F4),** clauses (F1)–(F3) would be satisfied by far too many collections of strings. The collection of **all** strings contains every atom and \( \bot \), and is closed under writing \( \neg \) in front and under wrapping two strings with a connective in parentheses; so (F1)–(F3) alone cannot tell us that \( p \wedge \to q \) is excluded. Clause (F4) says the formulas are only those strings that the building steps reach. In the language of sets, which Chapter 6 introduces properly, the formulas are the **smallest** collection of strings closed under (F1)–(F3).

**Without the parentheses in (F3),** a string could be read in two ways. Take \( p \wedge q \vee r \). Built one way, it is "\( p \wedge q \)" joined to \( r \) by \( \vee \); built the other way, it is \( p \) joined to "\( q \vee r \)" by \( \wedge \). The two constructions have different parse trees (defined below), and they say different things: if \( p \) is false and \( r \) is true, then "\( p \) and \( q \), or \( r \)" is true, because \( r \) is, while "\( p \), and \( q \) or \( r \)" is false, because \( p \) is. (Section 3.3 makes "true under an assignment of values" exact; the everyday reading of Chapter 1 is enough here.) With the parentheses of (F3) the two constructions give two **different** strings,
\[
((p \wedge q) \vee r) \qquad \text{and} \qquad (p \wedge (q \vee r)) ,
\]
and the ambiguity disappears. The next section proves that it disappears for every formula: a formula can be built in only one way (the unique readability theorem of Section 3.2).

**Why not parentheses around a negation too?** Nothing would break, but nothing would be gained. The symbol \( \neg \) always stands in front of what it negates, so \( \neg\varphi \) can be read in only one way without help. Keeping the official language as lean as possible makes the proofs about it shorter.

**Why atoms, and not sentences like "\( x > 0 \)"?** Because the theorems of this chapter are about **forms**, and the form of an argument is what remains when the content of its atomic statements is forgotten (Chapter 1's slogan: logic studies the forms of arguments). An atom is a statement reduced to a name.

::: {.warning}
A formula is a string of symbols, and questions about formulas are questions about strings. "Is \( (p \wedge p) \) the same formula as \( p \)?" has the answer **no**: the first has length \( 5 \) and the second length \( 1 \), even though they always have the same truth value (Section 3.3 gives the means to check this). Sameness of formulas is letter-for-letter identity; sameness of meaning is a different relation, which Section 3.4 names.
:::

## Parse trees

A formation sequence records how a formula was built, but it is a list, and a list hides the shape of the building. Chapter 1 drew the shape as a tree, with the main connective at the top (the tree after @def-main-connective). We now make that drawing official.

*A parse tree is a formula's construction drawn upside down: the last step at the root, the atoms at the leaves.*

::: {#def-parse-tree}
[Parse Tree]

A **parse tree for** a formula is defined along the clauses of @def-formula.

::: {.enumerate options="label=(T\arabic*)"}
1. For an atom or \( \bot \): a single node, labeled by that atom or by \( \bot \).
2. If \( T \) is a parse tree for \( \varphi \), then the tree whose **root** is labeled \( \neg \) and has \( T \) hanging below it as its only subtree is a parse tree for \( \neg\varphi \).
3. If \( T \) and \( T' \) are parse trees for \( \varphi \) and \( \psi \), then the tree whose root is labeled \( \circ \), with \( T \) hanging below it on the **left** and \( T' \) on the **right**, is a parse tree for \( (\varphi \circ \psi) \).
:::

The **leaves** are the nodes with nothing below them; a **branch** is a path from the root down to a leaf.
:::

In words: (T1) is the tree of a formula that was not built at all, a single node. (T2) puts a new root \( \neg \) on top of an existing tree. (T3) joins two existing trees under a new root carrying the connective, keeping left and right apart, because \( (p \to q) \) and \( (q \to p) \) are different formulas. Parentheses do not appear in a parse tree: their only job in the string was to show the grouping, and the tree shows the grouping by its shape.

**Every formula has a parse tree.** Take a formation sequence of the formula and build a tree for each entry in turn: an atom or \( \bot \) gets (T1), and an entry \( \neg\chi_j \) or \( (\chi_j \circ \chi_l) \) gets (T2) or (T3) from the trees already built for the earlier entries. The tree built for the last entry is a parse tree for the formula.

Could a formula have **two** different parse trees? That would happen if one string could be built in two different ways, as \( p \wedge q \vee r \) could if parentheses were not written. Section 3.2 proves that it never happens (the unique readability theorem); until then we say "**a** parse tree". After that section, every formula has exactly one, and we speak of **the** parse tree.

::: {#exm-parse-trees}
[Three parse trees]

Draw a parse tree for each formula: (a) \( p \); (b) \( \neg(p \wedge \neg q) \); (c) \( ((p \leftrightarrow \neg q) \vee (r \wedge (\bot \to p))) \), which uses every connective and \( \bot \).
:::

::: {.solution}
*(a)* A single node labeled \( p \), by (T1). This is the degenerate tree: its root is also its only leaf, and its only branch has one node.

*(b)* By (T1) the atoms \( p \) and \( q \) get one-node trees; (T2) puts \( \neg \) above \( q \); (T3) joins \( p \) and \( \neg q \) under \( \wedge \); (T2) puts \( \neg \) on top.

\begin{center}
\begin{tikzpicture}[level distance=10mm, sibling distance=16mm, every node/.style={font=\normalsize}]
  \node {$\neg$}
    child { node {$\wedge$}
      child { node {$p$} }
      child { node {$\neg$}
        child { node {$q$} }
      }
    };
\end{tikzpicture}
\end{center}

*(c)* The main connective is the \( \vee \): it is the last step, joining \( (p \leftrightarrow \neg q) \) on the left to \( (r \wedge (\bot \to p)) \) on the right. Each side is taken apart in the same way.

\begin{center}
\begin{tikzpicture}[level distance=10mm, every node/.style={font=\normalsize},
  level 1/.style={sibling distance=36mm}, level 2/.style={sibling distance=18mm},
  level 3/.style={sibling distance=12mm}]
  \node {$\vee$}
    child { node {$\leftrightarrow$}
      child { node {$p$} }
      child { node {$\neg$}
        child { node {$q$} }
      }
    }
    child { node {$\wedge$}
      child { node {$r$} }
      child { node {$\to$}
        child { node {$\bot$} }
        child { node {$p$} }
      }
    };
\end{tikzpicture}
\end{center}

The leaves are \( p \), \( q \), \( r \), \( \bot \) and \( p \) again: the atom \( p \) occurs twice in the formula, and each occurrence is its own leaf.
:::

To draw a parse tree from a string, find the last step, draw it as the root, and repeat on the parts. For a formula \( (\varphi \circ \psi) \), the last step is the binary connective that sits inside **exactly one** pair of parentheses; in (c), it is the \( \vee \), and every other binary connective sits inside at least two pairs. Section 3.2 proves that this recipe always finds the main connective, and only it.

## Subformulas and height

Each node of a parse tree is the root of the part of the tree below it, and that part is itself a parse tree, built by the same clauses, for a formula. The formulas that arise in this way are the pieces a formula is built from.

::: {#def-subformula}
[Subformula]

The **subformulas** of a formula \( \varphi \) are the formulas whose parse trees hang from the nodes of a parse tree for \( \varphi \): for each node, the formula of which the part of the tree from that node downwards is a parse tree. The formulas at the children of the root are the **immediate subformulas** of \( \varphi \).
:::

So the subformulas of \( \varphi \) include \( \varphi \) itself (at the root) and each atom that occurs in \( \varphi \) (at the leaves). A formula of the form \( \neg\varphi \) has one immediate subformula, \( \varphi \); a formula \( (\varphi \circ \psi) \) has the two immediate subformulas \( \varphi \) and \( \psi \) (one, if \( \varphi \) and \( \psi \) are the same formula); an atom or \( \bot \) has none. When we list the subformulas, a formula that sits at several nodes is listed once.

For the formula (c) of @exm-parse-trees, the subformulas are
\[
\begin{gathered}
((p \leftrightarrow \neg q) \vee (r \wedge (\bot \to p))), \quad
(p \leftrightarrow \neg q), \quad (r \wedge (\bot \to p)), \\
\neg q, \quad (\bot \to p), \quad p, \quad q, \quad r, \quad \bot ,
\end{gathered}
\]
nine in all. The tree has ten nodes, \( \vee \), \( \leftrightarrow \), \( p \), \( \neg \), \( q \), \( \wedge \), \( r \), \( \to \), \( \bot \) and \( p \) again, and only \( p \) sits at two of them; so ten nodes give nine distinct subformulas. Counting by eye is easy to get wrong, and the safe method is to walk the tree level by level, as we just did.

A string that merely **appears inside** a formula need not be a subformula. The formula \( ((p \wedge q) \vee r) \) contains the string \( q) \vee r \), which is not a formula at all, and it contains the string \( p \wedge q \), which is only the shorthand of a formula. Its subformulas are the formulas at the nodes: \( ((p \wedge q) \vee r) \), \( (p \wedge q) \), \( p \), \( q \) and \( r \).

The second measurement of a tree is how deep it goes.

::: {#def-height}
[Height]

The **height** of a formula \( \varphi \), written \( \hgt(\varphi) \), is the number of nodes on a **longest** branch of its parse tree.
:::

Atoms and \( \bot \) have height \( 1 \): their tree is one node, and its only branch has one node. (Some books count edges instead of nodes and give atoms height \( 0 \); with nodes, every formula has height at least \( 1 \).) In @exm-parse-trees, (b) has height \( 4 \), along the branch \( \neg, \wedge, \neg, q \), and (c) has height \( 4 \) too, along \( \vee, \leftrightarrow, \neg, q \) or along \( \vee, \wedge, \to, \bot \).

The definition speaks of "its parse tree", and so it depends on the fact, proved only in Section 3.2, that a formula has one parse tree. Until then the height is a promise, not a number: nothing in Section 3.2 uses it before that fact is proved, and Section 3.2 then obtains the height a second way, by a recursive definition that needs no trees at all.

::: {.check}
Draw the parse tree of \( (\neg p \vee q) \leftrightarrow \neg(r \wedge p) \) (in official form, \( ((\neg p \vee q) \leftrightarrow \neg(r \wedge p)) \)), list its subformulas, and give its height.
:::

::: {.solution}
The root is \( \leftrightarrow \). Its left subtree is \( \vee \) over \( \neg p \) and \( q \), where \( \neg p \) is \( \neg \) over the leaf \( p \). Its right subtree is \( \neg \) over \( \wedge \), and \( \wedge \) has the leaves \( r \) and \( p \).

The subformulas are the formula itself, \( (\neg p \vee q) \), \( \neg(r \wedge p) \), \( \neg p \), \( q \), \( (r \wedge p) \), \( p \) and \( r \): **eight**, with \( p \) listed once although it sits at two leaves.

The height is \( 4 \): the branches \( \leftrightarrow, \vee, \neg, p \) and \( \leftrightarrow, \neg, \wedge, r \) (and \( \leftrightarrow, \neg, \wedge, p \)) have four nodes, and no branch has more.
:::

::: {.warning}
The height counts the nodes on the longest **branch**, not the symbols of the formula. The formula \( \neg(p \wedge \neg q) \) has seven symbols, \( \neg \), \( ( \), \( p \), \( \wedge \), \( \neg \), \( q \), \( ) \), and height \( 4 \); the formula \( ((p \wedge q) \wedge (r \wedge p)) \) has thirteen symbols and height only \( 3 \). Parentheses never count towards the height, and a wide tree can be shallow.
:::

::: {.warning}
A parse tree is not a truth table. The tree records how a formula is **built**, and it is the same whatever the atoms stand for; nothing in it is true or false. Values come in Section 3.3, where they are computed **along** the tree, from the leaves up. Mixing the two, for instance writing "T" beside a node while drawing the tree, is a habit worth not forming: the same tree carries different values under different assignments.
:::

## Shorthand and official formulas

Nobody wants to write \( (((p \wedge q) \to r) \leftrightarrow (p \to (q \to r))) \). Chapter 1 used conventions that let us drop parentheses (Section 1.1, the four conventions before @def-main-connective), and we keep using them. What changes is their status: they are **not** part of the definition of a formula. A string written with the conventions is **shorthand**, and it stands for exactly one official formula, the one obtained by putting the dropped parentheses back.

The translation, from shorthand to official form, goes as follows.

1. Put back the outer pair of parentheses of a formula whose main connective is binary: \( p \wedge q \) stands for \( (p \wedge q) \).
2. \( \neg \) binds most tightly: it applies to the smallest formula that follows it. So \( \neg p \wedge q \) stands for \( (\neg p \wedge q) \), not for \( \neg(p \wedge q) \).
3. \( \wedge \) and \( \vee \) bind more tightly than \( \to \) and \( \leftrightarrow \): \( p \wedge q \to r \) stands for \( ((p \wedge q) \to r) \).
4. \( \to \) groups to the right: \( p \to q \to r \) stands for \( (p \to (q \to r)) \).
5. Chapter 1 sometimes wrote a negation in parentheses for emphasis, as in \( (\neg P) \to Q \); such parentheses are simply removed.

In a mixture of \( \wedge \) with \( \vee \), or of \( \to \) with \( \leftrightarrow \), the shorthand keeps the parentheses (Chapter 1's fourth convention), so no rule is needed for those.

::: {#exm-shorthand-translation}
[Two groupings of three implications]

Write the official formula for the shorthand \( p \to q \to r \), draw its parse tree beside that of \( ((p \to q) \to r) \), and find a situation in which the two formulas say different things.
:::

::: {.solution}
By rule 4, \( p \to q \to r \) stands for \( (p \to (q \to r)) \): the first \( \to \) is the main connective, and its conclusion is \( (q \to r) \). The other grouping, \( ((p \to q) \to r) \), has the second \( \to \) as main connective, and its hypothesis is \( (p \to q) \). Left, \( (p \to (q \to r)) \); right, \( ((p \to q) \to r) \).

\begin{center}
\begin{tikzpicture}[level distance=10mm, sibling distance=14mm, every node/.style={font=\normalsize}]
  \node {$\to$}
    child { node {$p$} }
    child { node {$\to$}
      child { node {$q$} }
      child { node {$r$} }
    };
\end{tikzpicture}
\qquad\qquad
\begin{tikzpicture}[level distance=10mm, sibling distance=14mm, every node/.style={font=\normalsize}]
  \node {$\to$}
    child { node {$\to$}
      child { node {$p$} }
      child { node {$q$} }
    }
    child { node {$r$} };
\end{tikzpicture}
\end{center}

The two trees are mirror images in shape, and they say different things. Suppose \( p \), \( q \) and \( r \) are all false. The left formula is an implication whose hypothesis \( p \) is false, so it is true (vacuous truth, @prp-vacuous-implication). The right formula has the true hypothesis \( p \to q \) (again vacuous, since \( p \) is false) and the false conclusion \( r \), so it is false. The everyday reading of Chapters 1 and 2 is enough to see this; Section 3.3 makes it a computation.

This is why the grouping convention matters. Chapter 1 chose to group to the right because statements of the form "if \( P \), then if \( Q \), then \( R \)" are common and \( (P \to Q) \to R \) is rare.
:::

Going the other way, from official to shorthand, we drop every pair of parentheses the rules would put back. \( (\neg(p \vee q) \leftrightarrow (\neg p \wedge \neg q)) \) becomes \( \neg(p \vee q) \leftrightarrow \neg p \wedge \neg q \): the outer pair goes by rule 1, the pair around \( \neg p \wedge \neg q \) by rule 3, and the pair after the first \( \neg \) must stay, since without it rule 2 would read \( \neg p \vee q \).

From now on we write formulas in shorthand whenever that is clearer, and every statement about "the formula \( p \wedge q \)" is about the official formula \( (p \wedge q) \). Where the official form matters, as in counting parentheses or symbols, we write it out.

## Letters, metavariables and substitution

We can now say exactly what the letters of Chapters 1 and 2 were.

Every rule was stated as a schema (@def-rule-schema), with metavariables: \( \rulename{\wedge I} \) writes \( \varphi \wedge \psi \) from \( \varphi \) and \( \psi \), **for any** formulas \( \varphi \) and \( \psi \). The derivations of those chapters were written with capital letters, as in the derivation of @prp-implication-transitive:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
\end{nd}$
\end{center}
```

In the language of this chapter, read the letters \( P, Q, R \) as three atoms. Then this is a derivation of \( p \to q, \ q \to r \vdash p \to r \) in the official sense, written in shorthand. But Chapter 1 meant more: the derivation was a **pattern**, good for any statements put in for the letters. Here is that promise made exact.

**Substitution.** Replace each atom of a derivation by a formula, **the same formula at every occurrence of the same atom**, and all such replacements at once. The result is again a derivation.

Here is why. First, each line becomes a formula. Replacing atoms by formulas in a formula \( \chi \) gives a formula: take a formation sequence of \( \chi \), write in front of it a formation sequence of each formula put in for an atom, and replace the atoms inside the old entries. Each old entry that was an atom has become the last entry of one of the sequences written in front; each old entry built by (F2) or (F3) is now built by the same clause from the replaced versions of the same earlier entries. So the new list is a formation sequence, and its last entry is the replaced \( \chi \).

Second, each line is still justified. Each line of the old derivation was a premise, an assumption, a repetition, or an instance of a rule's schema (@def-derivation, clauses (D1)–(D4)). Being an instance means: the line and the lines it cites are the schema with its metavariables replaced by certain formulas. The schema's own symbols are connectives, \( \bot \) and parentheses, never atoms, so replacing atoms in the lines is the same as replacing atoms inside those certain formulas. The new lines are therefore the same schema with its metavariables replaced by the new formulas: an instance of the same rule.

Third, nothing about citations changes. The line numbers, the boxes, and which line cites which are untouched, and whether a line or a box is available depends on nothing else (@def-derivation, the scope rule). So the result is a derivation, with the replaced premises and the replaced last line.

For instance, put \( (p_1 \wedge p_2) \) for \( P \), \( \neg p_1 \) for \( Q \), and \( (p_2 \vee p_1) \) for \( R \) in the derivation above:

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(p_1 \wedge p_2) \to \neg p_1}
  \hypo {2} {\neg p_1 \to (p_2 \vee p_1)}
  \open
  \hypo {3} {p_1 \wedge p_2}
  \have {4} {\neg p_1} \ie{1,3}
  \have {5} {p_2 \vee p_1} \ie{2,4}
  \close
  \have {6} {(p_1 \wedge p_2) \to (p_2 \vee p_1)} \ii{3-5}
\end{nd}$
\end{center}
```

Line 4 is still \( \rulename{{\to}E} \): lines 1 and 3 are \( \varphi \to \psi \) and \( \varphi \) with \( \varphi \) the formula \( p_1 \wedge p_2 \) and \( \psi \) the formula \( \neg p_1 \). Line 6 is still \( \rulename{{\to}I} \) with the same box.

The fact is immediate rule by rule, because every rule was stated for arbitrary formulas from the start. It is what the phrase "the letters stand for arbitrary statements" (Chapter 1, Section 1.2) and the clause "replace each letter … the same statement for every occurrence" of @def-derived-rule were relying on. We use it in two places later in the chapter: the soundness proof of Section 3.5 reads a derived rule as its pasted derivation, and the completeness proof of Section 3.6 uses the sequents of Chapters 1 and 2 with their letters replaced by formulas. Its counterpart for truth values is a lemma of Section 3.4.

::: {.remark}
The replacement must be **uniform**. Replacing only the first \( P \) of the derivation above by \( p_1 \wedge p_2 \), and leaving the \( P \) on line 3 alone, would break line 4, which needs the hypothesis of line 1 to be literally the formula on line 3.
:::

## Exercises

### A. Check your understanding

::: {#exr-formulas-and-parse-trees-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Decide which of the following strings are formulas. Give a formation sequence for each formula, and for each nonformula name the test or clause it fails: (i) \( (p \vee \bot) \); (ii) \( \neg\neg p \); (iii) \( (p \neg q) \); (iv) \( ((p \to q)) \); (v) \( (p \wedge q \wedge r) \).
2. List the subformulas of \( (\neg(p \to q) \vee q) \) and give its height.
3. True or false, with a reason: every subformula of \( \varphi \) other than \( \varphi \) itself has smaller height than \( \varphi \).
4. Why does clause (F3) of @def-formula put parentheses around its result, while (F2) does not?
5. Explain why clauses (F1)–(F3) alone do not show that \( \to p \) is not a formula, and which clause does.
:::
:::

::: {.solution}
*(a)* (i) A formula: \( p, \ \bot, \ (p \vee \bot) \).

(ii) A formula: \( p, \ \neg p, \ \neg\neg p \).

(iii) Not a formula. It begins with \( ( \), so by the first-symbol test it would be \( (\varphi \circ \psi) \), and the string \( p \neg q \) between the parentheses would contain a binary connective. It contains none.

(iv) Not a formula. It begins with \( ( \), so it would be \( (\varphi \circ \psi) \) with \( \varphi \circ \psi \) the string \( (p \to q) \). The only binary connective in that string is the \( \to \), so \( \varphi \) would be the string \( (p \), of length \( 2 \). A formula of length \( 2 \) begins with \( \neg \), by the first-symbol test (one beginning with \( ( \) has length at least \( 5 \)). So \( (p \) is not a formula, and neither is the string. Doubled parentheses are never part of an official formula.

*(v)* Not a formula. It would be \( (\varphi \wedge \psi) \) with the \( \wedge \) one of the two. If it is the first, \( \psi \) is the string \( q \wedge r \); if the second, \( \varphi \) is \( p \wedge q \). Each has length \( 3 \) and begins with an atom, so by the first-symbol test neither is a formula. (Chapter 1's conventions give no reading of the shorthand \( p \wedge q \wedge r \); Section 3.4 introduces it for the right-grouped \( (p \wedge (q \wedge r)) \) and explains why either grouping would do.)

*(b)* The formula is \( (\neg(p \to q) \vee q) \). Its subformulas are \( (\neg(p \to q) \vee q) \), \( \neg(p \to q) \), \( (p \to q) \), \( p \) and \( q \): five, with \( q \) listed once although it sits at two leaves. The longest branch is \( \vee, \neg, \to, p \) (or \( \vee, \neg, \to, q \)), so the height is \( 4 \).

*(c)* True. A subformula other than \( \varphi \) sits at a node below the root, and the part of the tree below that node is its parse tree. A longest branch of that part, with the path from the root of \( \varphi \)'s tree down to the node added in front, is a branch of \( \varphi \)'s tree with at least one more node. So \( \varphi \)'s tree has a branch longer than every branch of the subformula's tree.

*(d)* A binary connective joins two formulas, and without parentheses a string such as \( p \wedge q \vee r \) could be built in two ways, with different meanings (see "Why this definition"). A negation stands in front of the one formula it negates, so there is nothing to group.

*(e)* Clauses (F1)–(F3) say which strings are formulas and never which are not: the collection of all strings satisfies them. Clause (F4) says a formula is the last entry of a formation sequence, and from it follows the first-symbol test: \( \to p \) has length \( 2 \) and does not begin with \( \neg \) or \( ( \).
:::

### B. Practice

::: {#exr-formulas-and-parse-trees-b1}
[B1: Trees from Chapter 1]

Each formula below appears, with capital letters, in a result of Chapter 1 (@prp-curry and @prp-distributivity); here the letters are atoms. For each, write the official formula, draw its parse tree, list its subformulas, and give its height.

::: {.enumerate options="label=(\alph*)"}
1. \( (p \wedge q) \to r \)
2. \( p \to (q \to r) \)
3. \( (p \wedge q) \vee (p \wedge r) \)
:::
:::

::: {.solution}
*(a)* Official form \( ((p \wedge q) \to r) \). Root \( \to \); left subtree \( \wedge \) with leaves \( p \), \( q \); right subtree the leaf \( r \). Subformulas: \( ((p \wedge q) \to r) \), \( (p \wedge q) \), \( p \), \( q \), \( r \). Height \( 3 \), along \( \to, \wedge, p \).

*(b)* Official form \( (p \to (q \to r)) \). Root \( \to \); left the leaf \( p \); right subtree \( \to \) with leaves \( q \), \( r \). Subformulas: \( (p \to (q \to r)) \), \( (q \to r) \), \( p \), \( q \), \( r \). Height \( 3 \), along \( \to, \to, q \). (This is the left tree of @exm-shorthand-translation. The formulas of (a) and (b) have different trees; @prp-curry says that each can be derived from the other.)

*(c)* Official form \( ((p \wedge q) \vee (p \wedge r)) \). Root \( \vee \); left subtree \( \wedge \) with leaves \( p \), \( q \); right subtree \( \wedge \) with leaves \( p \), \( r \).

\begin{center}
\begin{tikzpicture}[level distance=10mm, every node/.style={font=\normalsize},
  level 1/.style={sibling distance=26mm}, level 2/.style={sibling distance=12mm}]
  \node {$\vee$}
    child { node {$\wedge$}
      child { node {$p$} }
      child { node {$q$} }
    }
    child { node {$\wedge$}
      child { node {$p$} }
      child { node {$r$} }
    };
\end{tikzpicture}
\end{center}

Subformulas: \( ((p \wedge q) \vee (p \wedge r)) \), \( (p \wedge q) \), \( (p \wedge r) \), \( p \), \( q \), \( r \): six, with \( p \) listed once although it sits at two leaves. Height \( 3 \).
:::

::: {#exr-formulas-and-parse-trees-b2}
[B2: Shorthand and back]

::: {.enumerate options="label=(\alph*)"}
1. Write in shorthand, dropping every pair of parentheses the conventions allow: \( ((p \wedge q) \to (r \to p)) \) and \( (\neg(p \vee q) \to (\neg p \wedge \neg q)) \).
2. Write the official formula for: \( p \to q \vee r \to \neg p \) and \( \neg p \wedge q \leftrightarrow r \).
:::
:::

::: {.solution}
*(a)* \( p \wedge q \to r \to p \). The outer pair goes by rule 1; \( (p \wedge q) \) loses its pair because \( \wedge \) binds more tightly than \( \to \) (rule 3); \( (r \to p) \) loses its pair because \( \to \) groups to the right (rule 4).

\( \neg(p \vee q) \to \neg p \wedge \neg q \). The outer pair goes; the pair around \( \neg p \wedge \neg q \) goes by rule 3. The pair after the first \( \neg \) stays: without it, rule 2 would make the \( \neg \) apply to \( p \) alone.

*(b)* \( (p \to ((q \vee r) \to \neg p)) \). Rule 3 groups \( q \vee r \) first; rule 4 then makes the first \( \to \) the main connective, with conclusion \( ((q \vee r) \to \neg p) \).

\( ((\neg p \wedge q) \leftrightarrow r) \). Rule 2 makes \( \neg \) apply to \( p \) alone; rule 3 groups \( \neg p \wedge q \) before \( \leftrightarrow \).
:::

### C. Going deeper

::: {#exr-formulas-and-parse-trees-c1}
[C1: Forgetting the grouping convention]

Suppose we forgot rule 4 of the shorthand, so that \( p \to q \to r \to s \) could stand for any official formula obtained by inserting parentheses into it.

::: {.enumerate options="label=(\alph*)"}
1. List every official formula it could stand for, and draw the shape of each parse tree.
2. How many are there? Say how the count is found, by splitting at the main connective.
3. Which of them is the one rule 4 chooses?
:::
:::

::: {.solution}
[Hint 1]

The main connective is one of the three arrows. Choose it first.
:::

::: {.solution}
[Hint 2]

Write \( c_n \) for the number of groupings of a chain of \( n \) atoms, and find \( c_1 \), \( c_2 \) and \( c_3 \) first.
:::

::: {.solution}
*(a)* The main connective is one of the three arrows; what lies on each side is then grouped in every possible way.

- Main connective the **first** arrow: \( p \) on the left, and \( q \to r \to s \) on the right, grouped in one of two ways. This gives \( (p \to (q \to (r \to s))) \) and \( (p \to ((q \to r) \to s)) \).
- Main connective the **second** arrow: \( (p \to q) \) on the left and \( (r \to s) \) on the right, each grouped in one way. This gives \( ((p \to q) \to (r \to s)) \).
- Main connective the **third** arrow: \( p \to q \to r \) on the left, grouped in one of two ways, and \( s \) on the right. This gives \( ((p \to (q \to r)) \to s) \) and \( (((p \to q) \to r) \to s) \).

Their parse trees have the root \( \to \) in each case: in the first two, the leaf \( p \) on the left and a tree of height \( 3 \) on the right (a right-leaning chain, or a left-leaning one); in the third, two trees of height \( 2 \) side by side; in the last two, a tree of height \( 3 \) on the left and the leaf \( s \) on the right.

*(b)* There are \( 5 \). Write \( c_n \) for the number of groupings of a chain of \( n \) atoms joined by one binary connective. A chain of one or two atoms has one grouping: \( c_1 = c_2 = 1 \). For three atoms the main connective is the first or the second arrow, and the side with two atoms has one grouping: \( c_3 = c_1 c_2 + c_2 c_1 = 2 \). For four atoms, choosing the main connective splits the chain into a left part of \( k \) atoms and a right part of \( 4 - k \) atoms, for \( k = 1, 2, 3 \), and the two parts are grouped independently:
\[
c_4 = c_1 c_3 + c_2 c_2 + c_3 c_1 = 2 + 1 + 2 = 5 .
\]
The three terms are the three bullets of (a).

*(c)* Rule 4 groups to the right, so the main connective is the first arrow and its right side is grouped to the right again: \( (p \to (q \to (r \to s))) \), the first formula of the list.

The numbers \( 1, 1, 2, 5, 14, 42, \dots \) produced by this splitting are the **Catalan numbers**; they grow quickly: a chain of eleven atoms joined by ten connectives already has \( 16{,}796 \) readings. Parentheses, or a fixed convention, are not pedantry.
:::

<!-- dependency ledger
def-formula (claim): every formula of the form neg(phi) has length at least 2, and (phi o psi) length at least 5, since every formula has at least one symbol | inline (from (F1)-(F4): every formation-sequence entry is non-empty)
def-parse-tree (claim): every formula has a parse tree, built along a formation sequence | inline
def-height (claim): "the" parse tree, hence the height, is well defined | thm-unique-readability (Section 3.2), stated as such in the text; nothing here uses the height before then except examples of drawing
exm-shorthand-translation (example): with p, q, r false, p -> (q -> r) is true and (p -> q) -> r is false | informal reading of Chapters 1-2 (prp-vacuous-implication cited); made exact in Section 3.3
def-formula (example): ("Why this definition") with p false and r true, (p and q) or r is true and p and (q or r) false | informal reading of Chapter 1; made exact in Section 3.3 (prose pointer)
def-formula (claim): (substitution paragraph, last subsection) replacing atoms uniformly in a derivation gives a derivation | inline (formation sequences; def-rule-schema; def-derivation (D1)-(D4) and the scope rule)
exr-formulas-and-parse-trees-a1 (solution): (c) a subtree's branch extended by the path from the root is a branch of the whole tree | inline
exr-formulas-and-parse-trees-c1 (solution): counts c_1..c_4 = 1, 1, 2, 5 by splitting at the main connective; Catalan growth ~4^n (remark only) | inline; checked by verify/ch03/exr-formulas-and-parse-trees-c1.py; the growth remark is not used
-->
