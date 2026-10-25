# Theories and Their Models

Section 7.2 called a structure in which three sentences are true a model of them. Mathematics works this way all the time: a list of axioms describes a kind of structure, and a theorem about that kind is whatever follows from the axioms. This section makes that precise, and answers the chapter's first question: the axioms of a partial order do not prove that any two elements are comparable.

The plan has five steps. First, theories and their models are defined. A gallery follows: equivalence relations, orders, groups and fields, each written as axioms, each with a model and a non-model. Then one theorem is derived from the group axioms, to show what a theorem of a theory is. Then comes consistency, which a single model proves. Last comes independence, which two models prove.

## Theories and their models

Fix the symbols (constants, function and predicate symbols) that the axioms will use, as in @def-structure.

*A theory is a collection of sentences taken as axioms; its theorems are what can be derived from finitely many of them.*

::: {#def-theory}
[Theory]

A **theory** \( T \) is a set of sentences in the chosen symbols, called its **axioms**; the set may be finite or infinite. A sentence \( \sigma \) is **derivable from** \( T \), written \( T \vdash \sigma \), if \( \varphi_1, \dots, \varphi_n \vdash \sigma \) for some finite list \( \varphi_1, \dots, \varphi_n \) of axioms of \( T \) (\( n \ge 0 \)); such a \( \sigma \) is a **theorem** of \( T \).
:::

In words: a derivation is finite, so it uses finitely many axioms, even when \( T \) has infinitely many. So "\( T \vdash \sigma \)" reads @def-derivable through a finite list, and needs nothing new. The case \( n = 0 \) says that a sentence derivable from no premises at all is a theorem of every theory. At the other end, each axiom is a theorem of its own theory: the derivation whose only line is the axiom, as a premise, has it as its last line. The theorems are everything in between: what the axioms, used finitely often, force.

*A model of a theory is a structure in which every axiom is true.*

::: {#def-model-of-theory}
[Model of a Theory]

A structure \( \fM \) for the symbols of \( T \) is a **model of** \( T \), written \( \fM \models T \), if every axiom of \( T \) is true in \( \fM \). A sentence \( \sigma \) is a **semantic consequence** of \( T \), written \( T \models \sigma \), if \( \sigma \) is true in every model of \( T \).
:::

The axioms are sentences, so no assignment is needed: by @lem-free-coincidence each axiom is true or false in \( \fM \) outright. And "every model of \( T \)" is the theory's version of "every structure satisfying \( \Gamma \)" in @def-first-order-entailment.

::: {.check}
Let \( T \) be the three sentences of the strict order with no largest element (Section 7.2). Is \( (\{ 0 \}, <) \) a model of \( T \)? Is the set \( \nQ_{>0} \) of positive rationals with \( < \)?
:::

::: {.solution}
Not the first: \( \forall x\, \neg(x < x) \) and transitivity hold, but \( \forall x\, \exists y\, (x < y) \) fails at \( 0 \), since nothing is above it. The second is a model: no rational is below itself, \( < \) is transitive, and for each positive \( d \) the witness \( d + 1 \) is again positive and above \( d \).
:::

## A gallery of theories

Each theory below is given by its axioms, written as sentences and named, with a model and a non-model. A non-model is checked by naming the axiom that fails and where. The names in parentheses are local to this chapter, except the field clauses (F1)–(F9), which keep their series-wide numbering; none of them is one of the clauses (S1)–(S7) of @def-satisfaction.

::: {#exm-axioms-and-models}
[Axioms, Models and Non-models]

*Equivalence relations.* One two-place predicate symbol \( R \), and three axioms:
\[
\begin{aligned}
&\text{(Refl)} && \forall x\, R(x, x), \\
&\text{(Sym)} && \forall x\, \forall y\, (R(x, y) \to R(y, x)), \\
&\text{(Trans)} && \forall x\, \forall y\, \forall z\, \bigl( (R(x, y) \wedge R(y, z)) \to R(x, z) \bigr).
\end{aligned}
\]
A model: \( D = \{ a, b, c \} \), with \( R^{\fM} \) relating \( a \) and \( b \) both ways and every element to itself (Figure A, left). Each loop gives (Refl); the only pairs of different elements are \( (a, b) \) and \( (b, a) \), which give (Sym); and every chain of two arrows ends where a loop or one of these pairs already is, which gives (Trans). In numbers: "\( x \) and \( y \) have the same parity" on \( \nZ \). A non-model: on \( \nZ \), read \( R(x, y) \) as \( \abs{x - y} \le 1 \). It is reflexive and symmetric, and (Trans) fails at \( 0, 1, 2 \): \( \abs{0 - 1} \le 1 \) and \( \abs{1 - 2} \le 1 \), but \( \abs{0 - 2} = 2 \).

*Partial and linear orders.* One two-place symbol \( \le \). The axioms (Refl) and (Trans), written with \( \le \), together with
\[
\text{(Antisym)} \quad \forall x\, \forall y\, \bigl( (x \le y \wedge y \le x) \to x = y \bigr),
\]
make the theory of a **partial order**. Adding
\[
\text{(Conn)} \quad \forall x\, \forall y\, (x \le y \vee y \le x)
\]
gives the theory of a **linear order**. A model of the first and not the second: divisibility on \( \{ 1, 2, 3, 6 \} \) (the right panel of Figure F in Section 7.1), where \( 2 \) and \( 3 \) are incomparable, so (Conn) fails at \( (2, 3) \). A model of both: \( (\nN, \le) \). Smallest of all, the **antichain** \( D = \{ a, b \} \) with \( \le^{\fM} = \{ (a, a), (b, b) \} \) (Figure A, right) is a partial order: the loops give (Refl), and (Antisym) and (Trans) only ever meet pairs \( (d, d) \). (Conn) fails at \( (a, b) \).

*Strict and dense orders.* One two-place symbol \( < \). The axioms
\[
\begin{aligned}
&\text{(Irrefl)} && \forall x\, \neg(x < x), \\
&\text{(Trans)} && \forall x\, \forall y\, \forall z\, \bigl( (x < y \wedge y < z) \to x < z \bigr)
\end{aligned}
\]
make a **strict order**; with
\[
\text{(Tri)} \quad \forall x\, \forall y\, (x < y \vee x = y \vee y < x)
\]
a **strict linear order**; and with
\[
\text{(Dense)} \quad \forall x\, \forall y\, \bigl( x < y \to \exists z\, (x < z \wedge z < y) \bigr)
\]
a **dense** one. A model of all four: \( (\nQ, <) \), where \( (p + q)/2 \) lies between \( p < q \). A non-model of (Dense): \( (\nZ, <) \), at \( 0 < 1 \), since no integer lies strictly between.

*Groups.* A two-place function symbol \( \cdot \) and a constant \( e \), with
\[
\begin{aligned}
&\text{(Assoc)} && \forall x\, \forall y\, \forall z\, \bigl( (x \cdot y) \cdot z = x \cdot (y \cdot z) \bigr), \\
&\text{(Id)} && \forall x\, (x \cdot e = x \wedge e \cdot x = x), \\
&\text{(Inv)} && \forall x\, \exists y\, (x \cdot y = e \wedge y \cdot x = e).
\end{aligned}
\]
A model: \( (\nZ; +, 0) \), with \( \cdot \) read as \( + \) and \( e \) as \( 0 \); the inverse of \( d \) is \( -d \). A non-model: \( (\nN; +, 0) \), where (Inv) fails at \( 1 \), since no natural number added to \( 1 \) gives \( 0 \). Commutativity,
\[
\text{(Comm)} \quad \forall x\, \forall y\, (x \cdot y = y \cdot x),
\]
is **not** an axiom; the next example shows why.

*Fields.* Constants \( 0 \), \( 1 \) and two-place function symbols \( + \), \( \cdot \), with ten axioms, the nine (F1)–(F9), numbered as in the field axioms used throughout this series, and \( (1 \ne 0) \):
\[
\begin{aligned}
&\text{(F1)} && \forall x\, \forall y\, (x + y = y + x), &&\text{(F2)} && \forall x\, \forall y\, \forall z\, \bigl( (x + y) + z = x + (y + z) \bigr), \\
&\text{(F3)} && \forall x\, (x + 0 = x), &&\text{(F4)} && \forall x\, \exists y\, (x + y = 0), \\
&\text{(F5)} && \forall x\, \forall y\, \forall z\, \bigl( (x \cdot y) \cdot z = x \cdot (y \cdot z) \bigr), &&\text{(F6)} && \forall x\, \forall y\, (x \cdot y = y \cdot x), \\
&\text{(F7)} && \forall x\, (x \cdot 1 = x), &&\text{(F8)} && \forall x\, \bigl( \neg(x = 0) \to \exists y\, (x \cdot y = 1) \bigr), \\
&\text{(F9)} && \forall x\, \forall y\, \forall z\, \bigl( x \cdot (y + z) = x \cdot y + x \cdot z \bigr), &&(1 \ne 0) && \neg(0 = 1).
\end{aligned}
\]
Models: \( \nQ \) and \( \nR \), with the usual operations, and the **two-element field**, with domain \( \{ 0, 1 \} \) and the tables
\[
\begin{array}{c|cc}
+ & 0 & 1 \\ \hline
0 & 0 & 1 \\
1 & 1 & 0
\end{array}
\qquad\qquad
\begin{array}{c|cc}
\cdot & 0 & 1 \\ \hline
0 & 0 & 0 \\
1 & 0 & 1
\end{array}
\]
(the sum of two equal elements is \( 0 \); the products are the usual ones). A non-model: \( \nZ \), where (F8) fails at \( 2 \): no integer \( y \) has \( 2y = 1 \).
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \begin{scope}
    \node[elt, label=below:$a$] (a) at (0,0) {};
    \node[elt, label=below:$b$] (b) at (1.6,0) {};
    \node[elt, label=below:$c$] (c) at (3.2,0) {};
    \draw[rel] (a) to[loop above] (a);
    \draw[rel] (b) to[loop above] (b);
    \draw[rel] (c) to[loop above] (c);
    \draw[rel] (a) to[bend left] (b);
    \draw[rel] (b) to[bend left] (a);
    \node at (1.6,-1) {\small an equivalence relation};
  \end{scope}
  \begin{scope}[xshift=5.2cm]
    \node[elt, label=below:$a$] (p) at (0,0) {};
    \node[elt, label=below:$b$] (q) at (1.6,0) {};
    \draw[rel] (p) to[loop above] (p);
    \draw[rel] (q) to[loop above] (q);
    \node at (0.8,-1) {\small the antichain: a partial order, not linear};
  \end{scope}
\end{tikzpicture}
\end{center}
```

**Figure A.** Left: an equivalence relation on \( \{ a, b, c \} \), whose classes are \( \{ a, b \} \) and \( \{ c \} \). Right: the antichain on \( \{ a, b \} \).

The non-models are as instructive as the models: a non-model with every axiom but one true shows exactly what that one axiom adds.

::: {.check}
In the two-element field, which element is the additive inverse of \( 1 \), and which is the reciprocal of \( 1 \)? Why does the field axiom for reciprocals ask nothing of \( 0 \)?
:::

::: {.solution}
\( 1 \) in both cases: \( 1 + 1 = 0 \) and \( 1 \cdot 1 = 1 \). The axiom (F8) reads \( \forall x\, \bigl( \neg(x = 0) \to \exists y\, (x \cdot y = 1) \bigr) \), and at \( 0 \) its hypothesis fails, so the implication holds by (S5).
:::

The groups part promised a model of the group axioms in which (Comm) is false. Every group of numbers under addition or multiplication is commutative, so the model comes from geometry.

::: {#exm-triangle-group}
[The Six Symmetries of a Triangle]

Label the corners of an equilateral triangle \( 1 \), \( 2 \), \( 3 \) (Figure T). A **symmetry** is a motion that puts the triangle back on itself, recorded by where it sends each corner. There are six:

- \( e \): nothing moves;
- \( r \): a turn by a third, \( 1 \mapsto 2 \), \( 2 \mapsto 3 \), \( 3 \mapsto 1 \);
- \( q \): a turn by two thirds, \( 1 \mapsto 3 \), \( 2 \mapsto 1 \), \( 3 \mapsto 2 \);
- the flips \( a \) (fixing \( 1 \), swapping \( 2 \) and \( 3 \)), \( b \) (fixing \( 2 \)) and \( c \) (fixing \( 3 \)).

Read \( x \cdot y \) as "**first** \( x \), **then** \( y \)". For instance \( a \cdot r \) sends \( 1 \) to \( 1 \) and then to \( 2 \); \( 2 \) to \( 3 \) and then to \( 1 \); \( 3 \) to \( 2 \) and then to \( 3 \). It fixes \( 3 \) and swaps \( 1 \), \( 2 \), so \( a \cdot r = c \). Computed in the same way, the whole table, with row \( x \), column \( y \) and entry \( x \cdot y \), is
\[
\begin{array}{c|cccccc}
\cdot & e & r & q & a & b & c \\ \hline
e & e & r & q & a & b & c \\
r & r & q & e & b & c & a \\
q & q & e & r & c & a & b \\
a & a & c & b & e & q & r \\
b & b & a & c & r & e & q \\
c & c & b & a & q & r & e
\end{array}
\]
Take the domain \( \{ e, r, q, a, b, c \} \), the table as the meaning of \( \cdot \), and \( e \) as the meaning of the constant \( e \). Check the group axioms.

- (Id): the \( e \) row and the \( e \) column repeat the column and row heads.
- (Inv): each row contains \( e \), and in the same place as its column does. So \( r \cdot q = e = q \cdot r \), and each flip undoes itself: \( a \cdot a = b \cdot b = c \cdot c = e \).
- (Assoc): "first \( x \), then \( y \), then \( z \)" is one sequence of motions, however it is bracketed. The fold below says this once more, carefully.

Now \( a \cdot r = c \) and \( r \cdot a = b \), so (Comm) fails at \( (a, r) \). So this is a model of the group axioms in which (Comm) is false.

Two elements would not do: in a group \( \{ e, g \} \), every product with \( e \) is fixed by (Id), and \( g \cdot g \) commutes with itself, so (Comm) holds.
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[scale=1.1]
  \coordinate (A) at (0,0);
  \coordinate (B) at (3,0);
  \coordinate (C) at (1.5,2.598);
  \draw (A) -- (B) -- (C) -- cycle;
  \node[below left] at (A) {$1$};
  \node[below right] at (B) {$2$};
  \node[above] at (C) {$3$};
  \draw[dashed] (-0.35,-0.2) -- (2.6,1.5);
  \node[right] at (2.6,1.5) {$a$};
  \draw[->] (1.5,0.866) ++(-60:0.45) arc (-60:220:0.45);
  \node at (1.5,0.866) {$r$};
\end{tikzpicture}
\end{center}
```

**Figure T.** The corners \( 1 \), \( 2 \), \( 3 \); the turn \( r \) about the center, carrying \( 1 \) to \( 2 \), \( 2 \) to \( 3 \) and \( 3 \) to \( 1 \); and the line of the flip \( a \), through corner \( 1 \) and the midpoint of the opposite side.

::: {.second-reading title="Why the table is associative without 216 checks"}
Checking (Assoc) entry by entry would mean \( 6 \cdot 6 \cdot 6 = 216 \) triples \( (x, y, z) \), each needing four look-ups in the table. There is a shorter way. A symmetry is a rearrangement of the corners, and \( x \cdot y \) is the rearrangement that applies \( x \) and then \( y \) to each corner. Follow one corner \( i \) through \( (x \cdot y) \cdot z \): first \( x \cdot y \) sends it to where \( y \) sends the place \( x \) sent it, and then \( z \) moves it on. Through \( x \cdot (y \cdot z) \): first \( x \) moves it, and then \( y \cdot z \) applies \( y \) and then \( z \). Either way, corner \( i \) goes through \( x \), then \( y \), then \( z \), and lands in the same place. The two products send every corner to the same corner, so they are the same symmetry. The table only records the results, so it is associative because composing rearrangements is.
:::

::: {.check}
From the table, what is \( a \cdot a \)? What is \( r \cdot r \cdot r \), bracketed either way?
:::

::: {.solution}
\( a \cdot a = e \). And \( (r \cdot r) \cdot r = q \cdot r = e \), while \( r \cdot (r \cdot r) = r \cdot q = e \): three turns by a third bring every corner home.
:::

## A theorem of a theory

A theorem of a theory is derived from finitely many of its axioms with the rules of Chapters 1, 2 and 5; nothing else is used. Section 5.4 has already derived one, in @exr-universal-introduction-b5 (c): from (Irrefl) and (Trans), a strict order is asymmetric. Here is a theorem of the group axioms.

::: {#prp-group-identity-unique}
[A Group Has Only One Identity]

From (Id), the sentence
\[
\forall x\, \bigl( \forall y\, (y \cdot x = y \wedge x \cdot y = y) \to x = e \bigr)
\]
is derivable: an element that acts as an identity on every element is \( e \).
:::

::: {.proof}
The plan: fix \( x_0 \) and assume that it acts as an identity; apply that assumption at \( e \), and (Id) at \( x_0 \). The two give two values of the one product \( x_0 \cdot e \), and \( \rulename{{=}E} \) equates them.

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, (x \cdot e = x \wedge e \cdot x = x)}
  \open[x_0]
  \open
  \hypo {2} {\forall y\, (y \cdot x_0 = y \wedge x_0 \cdot y = y)}
  \have {3} {e \cdot x_0 = e \wedge x_0 \cdot e = e} \Ae{2}
  \have {4} {x_0 \cdot e = e} \ae{3}
  \have {5} {x_0 \cdot e = x_0 \wedge e \cdot x_0 = x_0} \Ae{1}
  \have {6} {x_0 \cdot e = x_0} \ae{5}
  \have {7} {x_0 = e} \eqe{6,4}
  \close
  \have {8} {\forall y\, (y \cdot x_0 = y \wedge x_0 \cdot y = y) \to x_0 = e} \ii{2-7}
  \close
  \have {9} {\forall x\, (\forall y\, (y \cdot x = y \wedge x \cdot y = y) \to x = e)} \Ai{2-8}
\end{nd}$
\end{center}
```

Line 7 is \( \rulename{{=}E} \) with \( \varphi \) the formula \( z = e \): line 4 is \( \varphi[x_0 \cdot e / z] \), and line 6 says \( x_0 \cdot e = x_0 \), so the rule gives \( \varphi[x_0 / z] \). At line 9, \( x_0 \) appears in no premise, in no open assumption, and not in line 9.
:::

So in **every** group the identity is the only element that acts as one, by the soundness statement of [Section 7.2](#from-counter-models-to-non-derivability), without checking any group. In \( (\nZ; +, 0) \), \( 0 \) is the only integer \( x \) with \( d + x = d \) and \( x + d = d \) for every \( d \); in the triangle group, only the \( e \) row and the \( e \) column repeat the heads. Only (Id) was used. A theorem of a theory says something about all its models at once; that is what a theory is for.

## Consistency

Section 3.2 called a list of formulas inconsistent when it derives \( \bot \) (@def-inconsistent-set). A theory may be infinite, so its version goes through finite lists.

::: {#def-inconsistent-theory}
[Inconsistent Theory]

A theory \( T \) is **inconsistent** if \( T \vdash \bot \), that is, if \( \varphi_1, \dots, \varphi_n \vdash \bot \) for some finite list of axioms of \( T \); otherwise \( T \) is **consistent**.
:::

An inconsistent theory derives every sentence, since \( \rulename{\bot E} \) turns \( \bot \) into anything. So it says nothing, and consistency is the least one asks of axioms. Deriving \( \bot \) shows inconsistency: one derivation is enough. Consistency is harder to show by derivations, since it says that **no** derivation from the axioms ends with \( \bot \), and there are infinitely many derivations to rule out. Section 7.2 met the same difficulty with non-derivability, and solved it with a counter-model. A model does the same here: it rules out every derivation of \( \bot \) at once.

::: {#prp-model-shows-consistency}
[A Theory with a Model Is Consistent]

If some structure is a model of \( T \), then \( T \) is consistent.
:::

::: {.proof}
Let \( \fM \models T \), and suppose \( \varphi_1, \dots, \varphi_n \vdash \bot \) for axioms \( \varphi_i \) of \( T \). By the soundness statement of [Section 7.2](#from-counter-models-to-non-derivability) (proved in the optional Section 7.3), \( \varphi_1, \dots, \varphi_n \models \bot \). Each \( \varphi_i \) is true in \( \fM \), so \( \fM, \ell \models \bot \) for any assignment \( \ell \), which (S3) forbids. So no such list exists.
:::

So each model in the gallery proves its theory consistent. The converse, that every consistent theory has a model, is also true; it is the completeness theorem for predicate logic, stated without proof in the optional Section 7.6. *Consistent* is a word about derivations, and *has a model* (satisfiable) is one about structures. The two are never swapped, and where they agree the text says which theorem makes them agree.

The same reasoning shows that a sentence is **not** a theorem. To show \( T \nvdash \sigma \), make the counterexample set \( T, \neg\sigma \) true (@def-counterexample-set): find a model of \( T \) in which \( \sigma \) is false.

::: {.warning}
A model in which \( \sigma \) is **true** shows nothing about \( T \vdash \sigma \). Comparability, (Conn), is true in \( (\nN, \le) \), a model of the partial order axioms, and it is not a theorem of them, as the next subsection shows.
:::

::: {.check}
Is the theory \( \{ \exists x\, P(x), \ \forall x\, \neg P(x) \} \) consistent?
:::

::: {.solution}
No. Open an \( \rulename{\exists E} \) box on the first axiom, with witness \( x_0 \) and assumption \( P(x_0) \); \( \rulename{\forall E} \) on the second gives \( \neg P(x_0) \), and \( \rulename{\neg E} \) gives \( \bot \), which \( \rulename{\exists E} \) carries out of the box, since \( x_0 \) is not in \( \bot \), in the first axiom or in a premise. (Equally, no structure is a model; but that alone would not show inconsistency without the completeness theorem.)
:::

## Independence

One model with \( \sigma \) false shows that \( \sigma \) is not a theorem. Two models, one each way, show more.

::: {#prp-model-shows-independence}
[Independence by Models]

Let \( T \) be a theory and \( \sigma \) a sentence.

::: {.enumerate options="label=(\alph*)"}
1. If some model of \( T \) makes \( \sigma \) false, then \( T \nvdash \sigma \).
2. If, besides, some model of \( T \) makes \( \sigma \) true, then \( T \nvdash \neg\sigma \) as well; \( \sigma \) is then **independent** of \( T \): neither it nor its negation is a theorem.
:::
:::

::: {.proof}
(a) If \( \varphi_1, \dots, \varphi_n \vdash \sigma \) for axioms of \( T \), then \( \varphi_1, \dots, \varphi_n \models \sigma \) by the soundness statement of [Section 7.2](#from-counter-models-to-non-derivability) (proved in the optional Section 7.3). The model satisfies every \( \varphi_i \), so it satisfies \( \sigma \), against the hypothesis. (b) Apply (a) to \( \neg\sigma \), which the second model makes false, by (S4).
:::

Now the chapter's question. The antichain of Figure A is a model of the partial order axioms in which (Conn) is false, and \( (\nN, \le) \) is one in which it is true. So comparability is independent of the axioms of a partial order: they neither prove nor refute it. That is why "linear order" needs (Conn) as an axiom of its own.

The same goes for groups. \( (\nZ; +, 0) \) and the triangle group are models of the group axioms; (Comm) is true in the first and false in the second. So commutativity is independent of the group axioms. Mathematicians call the groups that satisfy it **abelian**, and study the others too.

*Finding the two models.* The model in which \( \sigma \) is true is usually the one the axioms were written for, such as \( (\nN, \le) \) or \( (\nZ; +, 0) \). The model in which \( \sigma \) is false is a counter-model in the sense of Section 7.2, and it is found by the same backward reading: write down what \( \neg\sigma \) demands, then what each axiom demands, and build the smallest structure meeting both. For (Conn) the demand is two incomparable elements, and the axioms of a partial order then ask only for a loop at each; that is the antichain.

Independence also tells whether an axiom list has a spare member: an axiom that follows from the others could be dropped from the list without changing the theorems. The three axioms of an equivalence relation have none.

::: {#exm-independence-rst}
[Reflexive, Symmetric, Transitive: Each Independent of the Other Two]

Three structures for one two-place symbol \( R \) (Figure I). The first two are the counter-readings (d) and (f) of @exr-universal-introduction-b5, now as models, with \( a \), \( b \) in place of \( 0 \), \( 1 \).

- *Not reflexive*: \( D = \{ a, b \} \), \( R^{\fM} = \{ (a, a) \} \). Symmetric and transitive, since the only pair is \( (a, a) \); (Refl) fails at \( b \).
- *Not symmetric*: \( D = \{ a, b \} \), \( R^{\fM} = \{ (a, a), (b, b), (a, b) \} \). Reflexive; transitive, since every chain of two arrows has a loop as one of them; (Sym) fails at \( (a, b) \), since \( (b, a) \) is missing.
- *Not transitive*: \( D = \{ a, b, c \} \), \( R^{\fM} \) the loops at \( a \), \( b \), \( c \) together with \( (a, b) \), \( (b, a) \), \( (b, c) \), \( (c, b) \). Reflexive; symmetric, since the arrows between different elements come in pairs; (Trans) fails at \( a, b, c \), since \( (a, b) \) and \( (b, c) \) are in \( R^{\fM} \) and \( (a, c) \) is not.

By @prp-model-shows-independence (a), no one of the three axioms follows from the other two.
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \begin{scope}
    \node[elt, label=below:$a$] (a1) at (0,0) {};
    \node[elt, label=below:$b$] (b1) at (1.6,0) {};
    \draw[rel] (a1) to[loop above] (a1);
    \node at (0.8,-1) {\small not reflexive};
  \end{scope}
  \begin{scope}[xshift=3.2cm]
    \node[elt, label=below:$a$] (a2) at (0,0) {};
    \node[elt, label=below:$b$] (b2) at (1.6,0) {};
    \draw[rel] (a2) to[loop above] (a2);
    \draw[rel] (b2) to[loop above] (b2);
    \draw[rel] (a2) -- (b2);
    \node at (0.8,-1) {\small not symmetric};
  \end{scope}
  \begin{scope}[xshift=6.4cm]
    \node[elt, label=below:$a$] (a3) at (0,0) {};
    \node[elt, label=below:$b$] (b3) at (1.6,0) {};
    \node[elt, label=below:$c$] (c3) at (3.2,0) {};
    \draw[rel] (a3) to[loop above] (a3);
    \draw[rel] (b3) to[loop above] (b3);
    \draw[rel] (c3) to[loop above] (c3);
    \draw[rel] (a3) to[bend left] (b3);
    \draw[rel] (b3) to[bend left] (a3);
    \draw[rel] (b3) to[bend left] (c3);
    \draw[rel] (c3) to[bend left] (b3);
    \node at (1.6,-1) {\small not transitive};
  \end{scope}
\end{tikzpicture}
\end{center}
```

**Figure I.** Three relations, each with exactly two of the three properties of an equivalence relation.

::: {.warning}
A tempting "proof" that a symmetric and transitive relation is reflexive: "\( R(x, y) \) gives \( R(y, x) \) by symmetry, and the two give \( R(x, x) \) by transitivity." The step from nothing to \( R(x, y) \) is the error: it needs some \( y \) related to \( x \). In the first structure above, \( b \) is related to nothing, and \( R(b, b) \) fails. Section 5.4 broke the claim with this reading, @exr-universal-introduction-b5 (d), and here it is a model of (Sym) and (Trans) in which (Refl) is false.
:::

::: {.check}
Show that (Dense) is independent of the strict linear order axioms.
:::

::: {.solution}
\( (\nQ, <) \) is a strict linear order in which (Dense) holds; \( (\nZ, <) \) is one in which it fails, at \( 0 < 1 \). Apply @prp-model-shows-independence.
:::

::: {.remark}
[Looking ahead]

*Sets and Functions*, Chapter 5 studies equivalence relations and partial orders as relations on a set, with their maximal and greatest elements; *Algebraic Preliminaries*, Chapters 1 and 2 take fields and groups as theories and study their models.
:::

## Exercises

### A. Check your understanding

::: {#exr-theories-and-models-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Define a theory, a model of a theory, and \( T \vdash \sigma \).
2. Why does @def-inconsistent-theory say "finite list of axioms"?
3. In the proof of @prp-model-shows-independence (a), where is the soundness statement used? Why does a model in which \( \sigma \) is true not show \( T \vdash \sigma \)?
4. What two models show \( \sigma \) independent of \( T \)?
5. True or false: every theory with a finite model is consistent.
:::
:::

::: {.solution}
*(a)* A theory is a set of sentences, its axioms (@def-theory). A model of \( T \) is a structure in which every axiom of \( T \) is true (@def-model-of-theory). \( T \vdash \sigma \) means \( \varphi_1, \dots, \varphi_n \vdash \sigma \) for some finite list of axioms of \( T \).

*(b)* A derivation has finitely many lines, so it uses finitely many premises, and a theory may be infinite.

*(c)* To pass from \( \varphi_1, \dots, \varphi_n \vdash \sigma \) to \( \varphi_1, \dots, \varphi_n \models \sigma \). A model in which \( \sigma \) is true is compatible with \( T \vdash \sigma \) and with \( T \nvdash \sigma \) alike: comparability is true in \( (\nN, \le) \) and is not a theorem of the partial order axioms.

*(d)* A model of \( T \) in which \( \sigma \) is false, and one in which it is true.

*(e)* True, by @prp-model-shows-consistency: a finite model is a model.
:::

::: {#exr-theories-and-models-a2}
[A2: Drill]

Each part takes a line or two. The parts run from reading an axiom, through deciding axioms in a given structure, to judging claims about theories and building a model.

::: {.enumerate options="label=(\alph*)"}
1. Write "\( R \) is symmetric" as a sentence.
2. Which axiom of a partial order fails in \( (\nZ, <) \), with \( \le \) read as \( < \)?
3. In the triangle table, what are \( q \cdot a \) and \( a \cdot q \)?
4. Is \( D = \{ a, b \} \), \( R^{\fM} = \{ (a, b), (b, a) \} \) a model of the equivalence relation axioms? Which of the three hold?
5. Is \( (\nQ \setminus \{ 0 \}; \cdot, 1) \), with the group's \( \cdot \) read as multiplication and \( e \) as \( 1 \), a model of the group axioms?
6. On \( D = \{ a \} \), which relations make a model of the strict order axioms? Of the partial order axioms?
7. On \( D = \{ a, b \} \) with \( (a, b) \in R^{\fM} \), add the fewest pairs that make \( R^{\fM} \) an equivalence relation.
8. Give a model of the dense strict linear order axioms other than \( (\nQ, <) \).
9. True or false: if \( \sigma \) is false in some structure, then \( T \nvdash \sigma \).
10. Is the empty theory consistent?
11. Is the theory with the two axioms \( \forall x\, \neg R(x, x) \) and \( \forall x\, \forall y\, R(x, y) \) consistent?
12. Give a model of the partial order axioms with three elements in which exactly one pair of different elements is comparable.
:::
:::

::: {.solution}
(a) \( \forall x\, \forall y\, (R(x, y) \to R(y, x)) \): whenever \( x \) is related to \( y \), \( y \) is related to \( x \).

(b) (Refl): \( 0 < 0 \) is false.

(c) \( q \cdot a = c \) and \( a \cdot q = b \).

(d) No. (Sym) holds; (Refl) fails, since there are no loops; (Trans) fails, since \( (a, b) \) and \( (b, a) \) are in \( R^{\fM} \) and \( (a, a) \) is not.

(e) Yes: multiplication is associative, \( 1 \) is an identity, and each \( d \) has the inverse \( 1/d \), again a non-zero rational.

(f) Strict order: exactly \( <^{\fM} = \emptyset \). The loop \( (a, a) \) breaks (Irrefl), and with no pairs (Trans) has no chain to check. Partial order: exactly \( \le^{\fM} = \{ (a, a) \} \); with \( \emptyset \), (Refl) fails at \( a \).

(g) \( (a, a) \), \( (b, b) \) and \( (b, a) \).

(h) \( (\nR, <) \), or the rationals strictly between \( 0 \) and \( 1 \) with \( < \).

(i) False: the structure must be a **model of \( T \)**. With \( T = \{ \forall x\, R(x, x) \} \) and \( \sigma \) the same sentence, \( \sigma \) is false in every structure with \( R^{\fM} = \emptyset \), yet \( T \vdash \sigma \) in one line.

(j) Yes: every structure is a model of it, so @prp-model-shows-consistency applies.

(k) No: \( \rulename{\forall E} \) twice on the second axiom gives \( R(x_0, x_0) \), \( \rulename{\forall E} \) on the first gives \( \neg R(x_0, x_0) \), and \( \rulename{\neg E} \) gives \( \bot \). (Any variable or constant may be the term.)

(l) \( D = \{ a, b, c \} \), \( \le^{\fM} \) the three loops and \( (a, b) \).
:::

### B. Practice

::: {#exr-theories-and-models-b1}
[B1: Construct a relation, or show none exists, used later]

On \( D = \{ 1, 2, 3, 4 \} \), give a relation that is:

::: {.enumerate options="label=(\roman*)"}
1. reflexive and transitive, but neither symmetric nor antisymmetric;
2. symmetric and transitive, not reflexive, with \( 1 \), \( 2 \) and \( 3 \) each related to something;
3. irreflexive, symmetric, transitive and non-empty; or show that no domain has one.
4. Which of your answers refutes the "proof" in the last warning of this section, and at which element?
:::
:::

::: {.solution}
(i) \( R \) = the four loops together with \( (1, 2) \), \( (2, 1) \), \( (1, 3) \), \( (2, 3) \). Reflexive: the loops. Transitive: the chains \( (x, y), (y, z) \) of two non-loop pairs (\( x \ne y \) and \( y \ne z \)) are \( (1, 2), (2, 1) \), giving \( (1, 1) \); \( (2, 1), (1, 2) \), giving \( (2, 2) \); \( (1, 2), (2, 3) \), giving \( (1, 3) \); and \( (2, 1), (1, 3) \), giving \( (2, 3) \); all in \( R \), and a chain through a loop gives back its other pair. Not symmetric: \( (1, 3) \) without \( (3, 1) \). Not antisymmetric: \( (1, 2) \) and \( (2, 1) \) with \( 1 \ne 2 \).

(ii) \( R = \{ (1, 1), (1, 2), (2, 1), (2, 2), (3, 3) \} \): symmetric and transitive (the classes \( \{ 1, 2 \} \) and \( \{ 3 \} \)), not reflexive at \( 4 \).

(iii) None, on any domain. If \( (d, e) \in R \), symmetry gives \( (e, d) \), and transitivity applied to \( (d, e), (e, d) \) gives \( (d, d) \), against irreflexivity.

(iv) (ii), at \( 4 \), which is related to nothing, so the "proof" has no \( y \) to start from.

*Used later:* Section 7.5 comes back to the relation of (ii).

**Marking scheme.** (10 points)
- 3: (i), a relation with all four properties checked, transitivity by listing the chains.
- 2: (ii).
- 3: (iii), the argument from an arbitrary pair.
- 2: (iv).
Fatal error (0 for (iii)): an argument that assumes every element is related to something.
:::

::: {#exr-theories-and-models-b2}
[B2: A sentence true in one structure and false in the other]

For each pair, find a sentence true in the first structure and false in the second, and read it back in words.

::: {.enumerate options="label=(\alph*)"}
1. \( (\nZ; +, 0) \) and \( (\nN; +, 0) \).
2. \( (\nQ; \cdot, 0, 1) \) and \( (\nZ; \cdot, 0, 1) \).
3. \( \fM_1 \): \( D = \{ a, b, c \} \), \( R^{\fM_1} = \{ (a, b), (b, c) \} \); and \( \fM_2 \): \( D = \{ a, b, c \} \), \( R^{\fM_2} = \{ (a, b), (a, c) \} \) (drawn below).
4. \( \fM_2 \) and \( \fM_1 \), in that order.
:::

```{=latex}
\begin{center}
\begin{tikzpicture}[structure]
  \begin{scope}
    \node at (1.6,1) {$\mathfrak{M}_1$};
    \node[elt, label=below:$a$] (a) at (0,0) {};
    \node[elt, label=below:$b$] (b) at (1.6,0) {};
    \node[elt, label=below:$c$] (c) at (3.2,0) {};
    \draw[rel] (a) -- (b);
    \draw[rel] (b) -- (c);
  \end{scope}
  \begin{scope}[xshift=5cm]
    \node at (1.6,1) {$\mathfrak{M}_2$};
    \node[elt, label=below:$a$] (a2) at (0,0) {};
    \node[elt, label=below:$b$] (b2) at (1.6,0) {};
    \node[elt, label=below:$c$] (c2) at (3.2,0) {};
    \draw[rel] (a2) -- (b2);
    \draw[rel] (a2) to[bend right] (c2);
  \end{scope}
\end{tikzpicture}
\end{center}
```
:::

::: {.solution}
*(a)* \( \forall x\, \exists y\, (x + y = 0) \), "every element has an additive inverse": true in \( \nZ \), with \( y = -x \); false in \( \nN \) at \( 1 \).

*(b)* \( \forall x\, \bigl( \neg(x = 0) \to \exists y\, (x \cdot y = 1) \bigr) \), "every non-zero element has a reciprocal": true in \( \nQ \), with \( y = 1/x \); false in \( \nZ \) at \( 2 \).

*(c)* \( \exists x\, \exists y\, \exists z\, (R(x, y) \wedge R(y, z)) \), "there is a path of two arrows": in \( \fM_1 \), \( a \), \( b \), \( c \); in \( \fM_2 \) no arrow leaves \( b \) or \( c \), so no path of two arrows exists.

*(d)* \( \exists x\, \exists y\, \exists z\, (R(x, y) \wedge R(x, z) \wedge \neg(y = z)) \), "some element has arrows to two different elements": in \( \fM_2 \), \( a \), \( b \), \( c \); in \( \fM_1 \) each element has at most one outgoing arrow.

Any other correct sentence earns full marks.

**Marking scheme.** (10 points)
- 2.5 per part: 1 for a sentence true in the first structure (checked), 1 for false in the second (with the failing element), 0.5 for the reading back.
Fatal error (0 for the part): a formula with a free variable.
:::

::: {#exr-theories-and-models-b3}
[B3: Derive a theorem of a theory]

From the three group axioms, derive \( \forall x\, (x \cdot x = x \to x = e) \): the only element equal to its own square is the identity. Which axioms did you use? Show by a model that (Inv) cannot be left out.
:::

::: {.solution}
*Plan.* Fix \( x_0 \) and assume \( x_0 \cdot x_0 = x_0 \). Take an inverse \( y_0 \) by \( \rulename{\exists E} \), multiply the assumption by \( y_0 \) on the left, and regroup: in words, \( e = y_0 \cdot x_0 = y_0 \cdot (x_0 \cdot x_0) = (y_0 \cdot x_0) \cdot x_0 = e \cdot x_0 = x_0 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \forall y\, \forall z\, ((x \cdot y) \cdot z = x \cdot (y \cdot z))}
  \hypo {2} {\forall x\, (x \cdot e = x \wedge e \cdot x = x)}
  \hypo {3} {\forall x\, \exists y\, (x \cdot y = e \wedge y \cdot x = e)}
  \open[x_0]
  \open
  \hypo {4} {x_0 \cdot x_0 = x_0}
  \have {5} {\exists y\, (x_0 \cdot y = e \wedge y \cdot x_0 = e)} \Ae{3}
  \open[y_0]
  \hypo {6} {x_0 \cdot y_0 = e \wedge y_0 \cdot x_0 = e}
  \have {7} {y_0 \cdot x_0 = e} \ae{6}
  \have {8} {\forall y\, \forall z\, ((y_0 \cdot y) \cdot z = y_0 \cdot (y \cdot z))} \Ae{1}
  \have {9} {\forall z\, ((y_0 \cdot x_0) \cdot z = y_0 \cdot (x_0 \cdot z))} \Ae{8}
  \have {10} {(y_0 \cdot x_0) \cdot x_0 = y_0 \cdot (x_0 \cdot x_0)} \Ae{9}
  \have {11} {(y_0 \cdot x_0) \cdot x_0 = y_0 \cdot x_0} \eqe{4,10}
  \have {12} {e \cdot x_0 = y_0 \cdot x_0} \eqe{7,11}
  \have {13} {e \cdot x_0 = e} \eqe{7,12}
  \have {14} {x_0 \cdot e = x_0 \wedge e \cdot x_0 = x_0} \Ae{2}
  \have {15} {e \cdot x_0 = x_0} \ae{14}
  \have {16} {x_0 = e} \eqe{15,13}
  \close
  \have {17} {x_0 = e} \Ee{5,6-16}
  \close
  \have {18} {x_0 \cdot x_0 = x_0 \to x_0 = e} \ii{4-17}
  \close
  \have {19} {\forall x\, (x \cdot x = x \to x = e)} \Ai{4-18}
\end{nd}$
\end{center}
```

The four \( \rulename{{=}E} \) steps, each with its \( \varphi \): line 11 with \( \varphi \) the formula \( (y_0 \cdot x_0) \cdot x_0 = y_0 \cdot w \), line 10 being \( \varphi[x_0 \cdot x_0 / w] \); line 12 with \( w \cdot x_0 = y_0 \cdot x_0 \), line 11 being \( \varphi[y_0 \cdot x_0 / w] \); line 13 with \( e \cdot x_0 = w \), line 12 being \( \varphi[y_0 \cdot x_0 / w] \); line 16 with \( w = e \), line 13 being \( \varphi[e \cdot x_0 / w] \). At line 17, \( y_0 \) is not in \( x_0 = e \), not in line 5, in no premise and in no open assumption. At line 19, \( x_0 \) is in no premise, in no assumption open outside its box, and not in line 19.

All three axioms are used. (Inv) cannot be left out: \( (\{ 0, 1 \}; \cdot, 1) \), with the usual product and \( e \) read as \( 1 \), satisfies (Assoc), since multiplication of numbers is associative, and (Id), since \( 0 \cdot 1 = 1 \cdot 0 = 0 \) and \( 1 \cdot 1 = 1 \). But \( 0 \cdot 0 = 0 \) and \( 0 \ne 1 \), so the theorem fails at \( 0 \). By @prp-model-shows-independence (a), it does not follow from (Assoc) and (Id) alone.

**Marking scheme.** (10 points)
- 2: the plan (fix \( x_0 \), assume \( x_0 \cdot x_0 = x_0 \), take an inverse by \( \rulename{\exists E} \)).
- 3: the chain of equations, with each \( \rulename{{=}E} \) naming its \( \varphi \).
- 2: the \( \rulename{\exists E} \) and \( \rulename{\forall I} \) side conditions checked: \( \rulename{\exists E} \), \( y_0 \) not in \( x_0 = e \), not in \( \exists y\, (x_0 \cdot y = e \wedge y \cdot x_0 = e) \), in no premise and in no open assumption; \( \rulename{\forall I} \), \( x_0 \) in no premise, in no assumption open outside its box, and not in \( \forall x\, (x \cdot x = x \to x = e) \).
- 1: the axioms named.
- 2: the model without (Inv), with (Assoc) and (Id) checked and the theorem failing at \( 0 \).
Fatal errors (0 for the derivation): an \( \rulename{{=}E} \) step that replaces a term the line does not contain; using \( y_0 \) outside its \( \rulename{\exists E} \) box.
:::

### C. Going deeper

::: {#exr-theories-and-models-c1}
[C1: Describe every model]

Describe every model of each sentence, and prove your description.

::: {.enumerate options="label=(\alph*)"}
1. \( \forall x\, \forall y\, (x = y) \).
2. \( \exists x\, \exists y\, \neg(x = y) \wedge \forall x\, \forall y\, \forall z\, (x = y \vee x = z \vee y = z) \).
3. \( \forall x\, \forall y\, R(x, y) \).
4. \( \forall x\, \exists y\, \bigl( R(x, y) \wedge \forall z\, (R(x, z) \to z = y) \bigr) \).
:::
:::

::: {.solution}
*(a)* "Any two elements are equal": exactly the structures with one element. If \( D \) has \( d \ne e \), then (S6) at \( d \) and \( e \) meets the equation \( x = y \) with different values, which (S2) rejects. With one element, every equation between its values holds. Domains are non-empty, so "at most one element" is "exactly one".

*(b)* "There are two different elements, and among any three, two are equal": exactly the structures with two elements. The first conjunct gives two different elements \( d \ne e \). If a third \( f \) differed from both, then \( x, y, z \) at \( d, e, f \) would make all three equations false. Conversely, in a two-element domain the two elements witness the first conjunct, and any three values repeat one of them.

*(c)* "Everything is related to everything": exactly the structures with \( R^{\fM} = D \times D \), on any non-empty \( D \). By (S6) twice, every pair \( (d, e) \) must be in \( R^{\fM} \), and if every pair is, the sentence holds.

*(d)* "Each element is related to exactly one element": exactly the structures in which \( R^{\fM} \) is the graph of a function from \( D \) to \( D \), that is, each \( d \) has exactly one \( e \) with \( (d, e) \in R^{\fM} \). For each \( d \), (S7) gives an \( e \) with \( (d, e) \in R^{\fM} \), and the inner \( \forall z \) says that any \( f \) with \( (d, f) \in R^{\fM} \) is \( e \). Conversely, if each \( d \) has exactly one such \( e \), that \( e \) is the witness, and the inner clause holds by uniqueness.

**Marking scheme.** (10 points)
- 2.5 per part: 1 for the description, 1.5 for both directions (every model is of this kind; every structure of this kind is a model).
Fatal error (0 for (a)): forgetting that domains are non-empty, so that "at most one" is "exactly one".
:::

::: {#exr-theories-and-models-c2}
[C2: The partial order axioms are independent]

Show that each of (Refl), (Antisym) and (Trans), for \( \le \), is independent of the other two.
:::

::: {.solution}
For (a) of @prp-model-shows-independence, three structures:

- *Not (Refl)*: \( D = \{ a, b \} \), \( \le^{\fM} = \{ (a, b) \} \). Antisymmetric and transitive, vacuously: there is no pair \( (b, a) \) and no chain of two arrows. No loops.
- *Not (Antisym)*: \( D = \{ a, b \} \), all four pairs. Reflexive and transitive; \( a \le b \) and \( b \le a \) with \( a \ne b \).
- *Not (Trans)*: \( D = \{ a, b, c \} \), the loops together with \( (a, b) \) and \( (b, c) \). Reflexive; antisymmetric, since no two different elements are related both ways; \( (a, c) \) is missing.

For (b), each axiom is also true in a model of the other two, for instance in \( (\nN, \le) \), where all three hold. So each axiom is independent of the other two.

**Marking scheme.** (10 points)
- 3 per axiom: the structure 1, the two other axioms checked 1, the failing pair 1.
- 1: independence cited correctly, including that each axiom is true in some model of the other two.
Fatal error (0 for the axiom): a structure in which one of the "other two" fails.
:::

::: {#exr-theories-and-models-c3}
[C3: Exit check: a theory checked three ways]

Let \( T \) be the theory of a strict linear order with a least element: (Irrefl), (Trans), (Tri), and
\[
\text{(Least)} \quad \exists x\, \forall y\, (x = y \vee x < y).
\]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( T \) is consistent.
2. Show that (Dense) is independent of \( T \).
3. Derive from \( T \) that the least element is unique: \( \forall x\, \forall y\, \bigl( (L(x) \wedge L(y)) \to x = y \bigr) \), where \( L(x) \) abbreviates \( \forall z\, (x = z \vee x < z) \). You may use \( \rulename{TAUT} \) on the propositional skeleton.
:::
:::

::: {.solution}
*(a)* \( (\nN, <) \) is a model: no number is below itself, \( < \) is transitive, any two numbers are equal or one is below the other, and \( 0 \) is a least element. By @prp-model-shows-consistency, \( T \) is consistent.

*(b)* In \( (\nN, <) \), (Dense) fails at \( 0 < 1 \). The non-negative rationals with \( < \) are a model of \( T \) (no rational is below itself, \( < \) is transitive, any two rationals are equal or one is below the other, and \( 0 \) is least, since no non-negative rational is below it), in which (Dense) holds: between \( p < q \) lies \( (p + q)/2 \). By @prp-model-shows-independence, (Dense) is independent of \( T \).

*(c)* Written out, \( L(x_0) \) is \( \forall z\, (x_0 = z \vee x_0 < z) \). The plan: fix \( x_0 \), \( y_0 \), assume both are least, instantiate each at the other, and let a TAUT step combine the two disjunctions with (Irrefl) and (Trans) at \( x_0 \), \( y_0 \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall x\, \neg(x < x)}
  \hypo {2} {\forall x\, \forall y\, \forall z\, ((x < y \wedge y < z) \to x < z)}
  \open[x_0]
  \open[y_0]
  \open
  \hypo {3} {\forall z\, (x_0 = z \vee x_0 < z) \wedge \forall z\, (y_0 = z \vee y_0 < z)}
  \have {4} {\forall z\, (x_0 = z \vee x_0 < z)} \ae{3}
  \have {5} {\forall z\, (y_0 = z \vee y_0 < z)} \ae{3}
  \have {6} {x_0 = y_0 \vee x_0 < y_0} \Ae{4}
  \have {7} {y_0 = x_0 \vee y_0 < x_0} \Ae{5}
  \have {8} {\neg(x_0 < x_0)} \Ae{1}
  \have {9} {\forall y\, \forall z\, ((x_0 < y \wedge y < z) \to x_0 < z)} \Ae{2}
  \have {10} {\forall z\, ((x_0 < y_0 \wedge y_0 < z) \to x_0 < z)} \Ae{9}
  \have {11} {(x_0 < y_0 \wedge y_0 < x_0) \to x_0 < x_0} \Ae{10}
  \open
  \hypo {12} {y_0 = x_0}
  \have {13} {y_0 = y_0} \eqi{}
  \have {14} {x_0 = y_0} \eqe{12,13}
  \close
  \have {15} {y_0 = x_0 \to x_0 = y_0} \ii{12-14}
  \have {16} {x_0 = y_0} \taut{6,7,8,11,15}
  \close
  \have {17} {(\forall z\, (x_0 = z \vee x_0 < z) \wedge \forall z\, (y_0 = z \vee y_0 < z)) \to x_0 = y_0} \ii{3-16}
  \close
  \have {18} {\forall y\, ((\forall z\, (x_0 = z \vee x_0 < z) \wedge \forall z\, (y = z \vee y < z)) \to x_0 = y)} \Ai{3-17}
  \close
  \have {19} {\forall x\, \forall y\, ((\forall z\, (x = z \vee x < z) \wedge \forall z\, (y = z \vee y < z)) \to x = y)} \Ai{3-18}
\end{nd}$
\end{center}
```

Line 14 is \( \rulename{{=}E} \) with \( \varphi \) the formula \( z = y_0 \): line 13 is \( \varphi[y_0 / z] \), and line 12 says \( y_0 = x_0 \), so the rule gives \( \varphi[x_0 / z] \). The TAUT step on line 16 reads the skeleton with the letters \( A \) for \( x_0 = y_0 \), \( B \) for \( x_0 < y_0 \), \( C \) for \( y_0 = x_0 \), \( D \) for \( y_0 < x_0 \) and \( E \) for \( x_0 < x_0 \). From \( A \vee B \), \( C \vee D \), \( \neg E \), \( (B \wedge D) \to E \) and \( C \to A \), the letter \( A \) follows in every row: if \( A \) is false, then \( B \) is true; \( C \to A \) makes \( C \) false, so \( D \) is true; then \( E \) is true, against \( \neg E \). At line 18, \( y_0 \) is in no premise, no assumption is open outside its box, and \( y_0 \) is not in line 18; at line 19 the same holds for \( x_0 \). Only (Irrefl) and (Trans) were used.

**Marking scheme.** (10 points)
- 2: (a), a model with every axiom checked.
- 3: (b), two models of \( T \) (the axioms checked for the new one), with (Dense) checked in each.
- 4: (c), the derivation: the case \( y_0 = x_0 \) closed, by symmetry of \( = \) via \( \rulename{{=}I} \) and \( \rulename{{=}E} \) or by \( \rulename{{=}E} \) into \( x_0 < y_0 \) (1), the instance of (Trans) at \( x_0 \), \( y_0 \), \( x_0 \), reached by three \( \rulename{\forall E} \) steps (1), the cases combined, by a TAUT step whose skeleton is a tautology or by an equivalent \( \rulename{\vee E} \) and \( \rulename{\bot E} \) case analysis (1), the \( \rulename{\forall I} \) side conditions (1).
- 1: names the axioms used.
Fatal error (0 for (c)): a TAUT step that needs \( y_0 = x_0 \) and \( x_0 = y_0 \) to be the same letter (they are not).
:::

<!-- dependency ledger
def-theory (claim): a derivation has finitely many lines, so it uses finitely many premises | def-derivable (cited; a derivation is a finite list of lines)
def-model-of-theory (claim): the truth of an axiom in a structure needs no assignment | lem-free-coincidence (cited)
exm-axioms-and-models (claim): "same parity" is an equivalence relation on Z; |x - y| <= 1 is reflexive and symmetric and fails transitivity at 0, 1, 2 | school arithmetic; checked by verify/ch07/exm-axioms-and-models.py on a window of Z
exm-axioms-and-models (claim): divisibility on {1, 2, 3, 6} is a partial order, 2 and 3 incomparable; (N, <=) a linear order; the antichain a partial order failing (Conn) | school arithmetic (divisibility); checked by verify/ch07/exm-axioms-and-models.py
exm-axioms-and-models (claim): (Q, <) is a dense strict linear order, (p + q)/2 between p < q; no integer strictly between 0 and 1 | school algebra; AN1.1 / F3.2 (promised, prose only, nothing rests on it)
exm-axioms-and-models (claim): (Z; +, 0) is a group; (N; +, 0) fails (Inv) at 1 | school arithmetic
exm-axioms-and-models (claim): Q and R are fields; Z fails (F8) at 2 | school algebra; F3.2 / AN1.1 (promised, prose only, nothing rests on it)
exm-axioms-and-models (claim): the two-element field tables satisfy (F1)-(F9) and (1 != 0) | inline tables; checked by verify/ch07/exm-axioms-and-models.py
def-model-of-theory (example): Quick check 1, in Q_{>0}, < is irreflexive and transitive, and d + 1 is positive and above d; nothing lies above 0 in ({0}, <) | school arithmetic
exm-triangle-group (claim): addition and multiplication of numbers are commutative, so every group of numbers under them satisfies (Comm) | school arithmetic
exm-triangle-group (claim): the table is computed from the six rearrangements; (Id), (Inv); a.r = c, r.a = b | inline computation; checked by verify/ch07/exm-triangle-group.py
exm-triangle-group (claim): associativity, composing rearrangements of the corners is associative | fold "Why the table is associative without 216 checks" (argued inline); all 216 triples checked by verify/ch07/exm-triangle-group.py
exm-triangle-group (claim): every two-element group is commutative | argued inline; checked by enumeration in verify/ch07/exm-triangle-group.py
prp-group-identity-unique (proof): the derivation | rules def-rule-universal-elimination, def-rules-universal, def-rules-equality, Chapters 1-2 (cited by rule name); checked by tools/check_fitch.py
prp-group-identity-unique (claim): the theorem holds in every group | the soundness statement of F1.6 §02 (#from-counter-models-to-non-derivability; proved in F1.6 §03, optional, never cited by label)
prp-model-shows-consistency (proof): derivable from axioms implies entailed by them | the soundness statement of F1.6 §02 (#from-counter-models-to-non-derivability; proved in F1.6 §03, optional, never cited by label)
prp-model-shows-consistency (claim): every consistent theory has a model | completeness, stated without proof in F1.6 §06 (optional; prose pointer, nothing rests on it)
prp-model-shows-independence (proof): derivable from axioms implies entailed by them | the soundness statement of F1.6 §02 (#from-counter-models-to-non-derivability; proved in F1.6 §03, optional, never cited by label)
def-inconsistent-theory (claim): an inconsistent theory derives every sentence | bot-E (Chapter 2 rule, cited by name)
exm-independence-rst (claim): each structure has exactly the two named properties | inline checks; checked by verify/ch07/exm-independence-rst.py, and the first two agree with verify/ch05/exr-universal-introduction-b5.py
exr-theories-and-models-a2 (solution): (e) Q without 0 is a group under multiplication; (h) R and the rationals in (0, 1) are dense linear orders | school algebra; checked on finite samples by verify/ch07/exr-theories-and-models-a2.py
exr-theories-and-models-b1 (solution): the four properties of each answer; (iii) impossible | inline; checked by enumeration (domains of size 1-4) in verify/ch07/exr-theories-and-models-b1.py
exr-theories-and-models-b2 (solution): the four sentences true in the first structure and false in the second | school arithmetic; checked by verify/ch07/exr-theories-and-models-b2.py
exr-theories-and-models-b3 (solution): the derivation; ({0, 1}; ., 1) satisfies (Assoc), (Id) and fails the theorem at 0 | checked by tools/check_fitch.py and verify/ch07/exr-theories-and-models-b3.py
exr-theories-and-models-c1 (solution): the four descriptions | argued inline; checked on all structures of sizes 1-3 by verify/ch07/exr-theories-and-models-c1.py
exr-theories-and-models-c2 (solution): the three structures | inline; checked by verify/ch07/exr-theories-and-models-c2.py
exr-theories-and-models-c3 (solution): (N, <) and the non-negative rationals are models of T; the TAUT skeleton | school arithmetic; prp-taut-skeleton and def-rule-taut (cited by the TAUT convention of F1.8 §03); checked by verify/ch07/exr-theories-and-models-c3.py and tools/check_fitch.py
-->
