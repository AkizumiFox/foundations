# The Field Axioms and the First Examples

*Number Systems: From \( \nN \) to \( \nR \)* defined fields (@fd3:def-commutative-ring-and-field) and built \( \nQ \), \( \nR \) and, for each prime \( p \), the field \( \nZ/p\nZ \). Chapter 1 added \( \nC \). This chapter looks at fields as a kind of object in their own right. Its first section restates the definition under the name that the linear-algebra volumes use, collects the rules that hold in every field, solves one and two linear equations in any field, and sorts the standard examples from the standard non-examples, naming in each case the clause that fails.

## What solving equations needs

Here is a small system of equations, solved the way it is solved at school:
\[
\begin{aligned}
2x + 3y &= 7, \\
x - y &= 1.
\end{aligned}
\]
Subtract twice the second equation from the first: \( 5y = 5 \). Divide by \( 5 \): \( y = 1 \). Then \( x = 1 + y = 2 \). Check: \( 2 \cdot 2 + 3 \cdot 1 = 7 \) and \( 2 - 1 = 1 \).

List the moves. Equations were combined by sums and differences, one equation was scaled by a number, and one was divided by a number that is **not zero**. Silently, terms were also reordered, regrouped, and brackets were multiplied out. Elimination, the method the linear-algebra volumes run on systems of any size, uses these moves and nothing else.

Now stay inside \( \nZ \). The equation \( 2x = 1 \) has integer coefficients and no integer solution: \( 2x \) is even and \( 1 = 2 \cdot 0 + 1 \) is odd, and no integer is both (@fd3:cor-integers-even-odd (a)). The move "divide by \( 2 \)" leads out of \( \nZ \). So the dividing line between \( \nZ \) and \( \nQ \) is division, and division by every non-zero element is what the definition must ask for.

*A field is a number system where you can add, subtract, multiply, and divide by anything non-zero, with the usual rules.*

## The definition

The definition lists the rules once, as clauses that can be checked and cited. The numbering is the one *Number Systems* used for commutative rings, and the one the linear-algebra volumes cite.

::: {#def-field}
[Field]

A **field** is a set \( F \) together with two functions, **addition** \( + \colon F \times F \to F \), \( (a, b) \mapsto a + b \), and **multiplication** \( \cdot \colon F \times F \to F \), \( (a, b) \mapsto a \cdot b = ab \), satisfying the following clauses.

::: {.enumerate options="label=(F\arabic*)"}
1. \( a + b = b + a \) **for all** \( a, b \in F \).
2. \( (a + b) + c = a + (b + c) \) **for all** \( a, b, c \in F \).
3. **There is** an element \( 0 \in F \) such that \( a + 0 = a \) **for every** \( a \in F \).
4. **For every** \( a \in F \) there is an element \( -a \in F \) such that \( a + (-a) = 0 \).
5. \( (ab)c = a(bc) \) **for all** \( a, b, c \in F \).
6. \( ab = ba \) **for all** \( a, b \in F \).
7. **There is** an element \( 1 \in F \) with **\( 1 \ne 0 \)** such that \( a \cdot 1 = a \) **for every** \( a \in F \).
8. **For every non-zero** \( a \in F \) there is an element \( a^{-1} \in F \) such that \( a a^{-1} = 1 \).
9. \( a(b + c) = ab + ac \) **for all** \( a, b, c \in F \).
:::

We write \( a - b \coloneqq a + (-b) \), and \( a / b \coloneqq a b^{-1} \) for \( b \ne 0 \).
:::

Read the clauses in three groups.

- **(F1)–(F4)** speak only of addition. The order and the grouping of a sum do not matter, \( 0 \) changes nothing when added, and each element can be undone by its negative. Subtraction is built from these.
- **(F5)–(F8)** repeat those four statements for multiplication, with one change: an inverse is demanded only of a **non-zero** element. So division is defined only by non-zero elements, and no clause ever calls for division by \( 0 \). Clause (F7) also demands that the two neutral elements differ.
- **(F9)**, the distributive law, is the single bridge between the two operations: it alone mentions both, and multiplying out brackets rests on it, with (F6) for a bracket on the left.

Mind the order of the quantifiers in (F3): there is **one** element \( 0 \) that works **for every** \( a \). The weaker reading, "each \( a \) has its own \( z \) with \( a + z = a \)", would let \( z \) change with \( a \), and it is not what (F3) says. In (F4) the order is the other way round, as it has to be: the negative \( -a \) depends on \( a \).

Both operations are functions **into** \( F \): a sum or product of two elements of \( F \) is again in \( F \). For a candidate field cut out of a larger number system, that closure is where checking starts. We say "\( F \) is a field" when the two operations are understood, and write \( (F, +, \cdot) \) when they must be named.

::: {.remark}
[The same definition in *Number Systems*]

@fd3:def-commutative-ring-and-field calls a set with two operations a **commutative ring** when (F1)–(F7) and (F9) hold, its (F7) asking only for an element \( 1 \) with \( a \cdot 1 = a \); it calls a commutative ring a **field** when, in addition, \( 1 \ne 0 \) and (F8) hold. Clause by clause, these are the conditions of @def-field: the nine clauses are worded alike, and the only difference is where the condition \( 1 \ne 0 \) is filed, inside (F7) here and as a separate clause there. So \( F \) is a field in the sense of @def-field **if and only if** it is a field in the sense of @fd3:def-commutative-ring-and-field. Every result that *Number Systems* proves for fields, or for commutative rings, therefore applies to every field of this chapter, and conversely. The separate filing there has a purpose: it lets the one-element set \( \{0\} \) count as a commutative ring (the zero ring) while keeping it out of the fields.
:::

::: {.check}
Is \( \nQ_{>0} \), the set of positive rationals with the usual \( + \) and \( \cdot \) of \( \nQ \), a field?
:::

::: {.solution}
No. Addition and multiplication do map \( \nQ_{>0} \times \nQ_{>0} \) into \( \nQ_{>0} \) (@fd3:thm-rationals-ordered-field, with (P1) of @fd3:prp-order-from-positives). But (F3) fails. An element \( z \in \nQ_{>0} \) with \( 1 + z = 1 \) would satisfy \( z = 0 + z = ((-1) + 1) + z = (-1) + (1 + z) = (-1) + 1 = 0 \) in the field \( \nQ \), by (F1), (F3), (F4) and (F2), and \( 0 \notin \nQ_{>0} \). (Once (F3) fails, (F4) cannot even be stated.)
:::

## Rules that hold in every field

The definition's notation takes something for granted. The symbols \( 0 \), \( -a \) and \( a^{-1} \) are written as names of single elements, while (F3), (F4), (F7) and (F8) assert only that suitable elements **exist**. Were there two different zeros in some field, the symbols \( 0 \), \( a - b \) and \( a / b \) would be ambiguous. The next theorem removes the worry and collects the rules of school algebra that every field obeys. Most of it was proved in *Number Systems* for every commutative ring; we collect it under one name, citing the proofs there, and add the rules for fractions as part (g).

::: {#thm-field-basic-properties}
[Basic Properties of Fields]

Let \( F \) be a field and let \( a, b, c, d \in F \).

::: {.enumerate options="label=(\alph*)"}
1. The element \( 0 \) in (F3) is unique, and the element \( 1 \) in (F7) is unique.
2. (Cancellation) If \( a + b = a + c \), then \( b = c \). If \( ab = ac \) and \( a \ne 0 \), then \( b = c \).
3. The negative \( -a \) in (F4) is unique, and for \( a \ne 0 \) the inverse \( a^{-1} \) in (F8) is unique.
4. \( 0 \cdot a = 0 \).
5. \( (-1)a = -a \).
6. If \( ab = 0 \), then \( a = 0 \) or \( b = 0 \).
7. If \( b \ne 0 \) and \( d \ne 0 \), then \( bd \ne 0 \), \( (bd)^{-1} = b^{-1} d^{-1} \), \( (b^{-1})^{-1} = b \), and
\[
\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}, \qquad \frac{a}{b} \cdot \frac{c}{d} = \frac{ac}{bd}.
\]
:::
:::

::: {.idea}
Work backwards from each goal to the clause that could produce it; each part then takes a few lines. For uniqueness, take two candidates and prove them equal. No clause says anything about \( 0 \cdot a \), so for (d) we manufacture a place where (F9) can act: \( 0 = 0 + 0 \), distribute, cancel. In (f) the hypothesis \( a \ne 0 \) has exactly one use, which is to unlock (F8). The fraction rules in (g) come from one move: an element is identified by showing that it satisfies the defining equation of the element we want, and uniqueness finishes.
:::

::: {.proof}
By the remark after @def-field, \( F \) is a commutative ring in the sense of @fd3:def-commutative-ring-and-field, so @fd3:prp-ring-algebra applies to it.

(a) This is @fd3:prp-ring-algebra (a).

(b) Suppose \( a + b = a + c \). Put \( -a \) in front of each side and regroup with (F2): this gives \( ((-a) + a) + b = ((-a) + a) + c \). By (F1) and (F4), \( (-a) + a = a + (-a) = 0 \), so \( 0 + b = 0 + c \), and by (F1) and (F3) this says \( b = c \).

Now suppose \( ab = ac \) and \( a \ne 0 \). By (F8), \( a^{-1} \) exists. Using (F7), (F8), (F6) and (F5),
\[
\begin{aligned}
b &= b \cdot 1 = b(a a^{-1}) = (ba) a^{-1} = (ab) a^{-1} \\
&= (ac) a^{-1} = (ca) a^{-1} = c (a a^{-1}) = c \cdot 1 = c.
\end{aligned}
\]

(c) The negative is unique by @fd3:prp-ring-algebra (a). For \( a \ne 0 \), clause (F8) says that \( a \) is a unit of \( F \) in the sense of @fd3:def-ring-unit, and the inverse of a unit is unique (the well-definedness paragraph after @fd3:def-ring-unit).

(d) By @fd3:prp-ring-algebra (b), \( a \cdot 0 = 0 \), and \( 0 \cdot a = a \cdot 0 \) by (F6).

(e) By @fd3:prp-ring-algebra (c) with \( a = 1 \), \( (-1)b = -(1 \cdot b) \) for every \( b \in F \); and \( 1 \cdot b = b \cdot 1 = b \) by (F6) and (F7). Applied to \( b = a \), this gives \( (-1)a = -a \).

(f) Suppose \( ab = 0 \). If \( a = 0 \) there is nothing to prove, so suppose \( a \ne 0 \). By (F8), \( a \) is a unit of \( F \) (@fd3:def-ring-unit), and a unit is not a zero divisor (the paragraph after @fd3:def-ring-unit): from \( ab = 0 \) it follows that \( b = 0 \). So \( a = 0 \) or \( b = 0 \).

(g) Let \( b \ne 0 \) and \( d \ne 0 \). If \( bd = 0 \), then (f) would give \( b = 0 \) or \( d = 0 \); so \( bd \ne 0 \). By (F8), \( b \) and \( d \) are units of \( F \). A product of units is a unit, with \( (bd)^{-1} = b^{-1} d^{-1} \), and the inverse of a unit is a unit, with \( (b^{-1})^{-1} = b \) (the closure paragraph after @fd3:def-ring-unit). Here \( b^{-1} \ne 0 \), since \( 1 \ne 0 \) by (F7) and so \( 0 \) is not a unit (the paragraph "Why this definition" after @fd3:def-ring-unit); thus \( (b^{-1})^{-1} \) is also the inverse that (F8) supplies, by (c).

For the sum, multiply out with (F9) and reorder with (F5) and (F6):
\[
\begin{aligned}
(a b^{-1} + c d^{-1})(bd)
&= a (b^{-1} b) d + c (d^{-1} d) b \\
&= ad + cb = ad + bc,
\end{aligned}
\]
by (F8) and (F7) and then (F6). Multiplying both ends by \( (bd)^{-1} \), and using \( (bd)(bd)^{-1} = 1 \) with (F5) and (F7) on the left, gives \( a b^{-1} + c d^{-1} = (ad + bc)(bd)^{-1} \), which is the first displayed rule. For the product, (F5) and (F6) give \( (a b^{-1})(c d^{-1}) = (ac)(b^{-1} d^{-1}) = (ac)(bd)^{-1} \), by the formula for \( (bd)^{-1} \) just proved. This proves the theorem.
:::

From now on we use \( 0 + a = a \) and \( 1 \cdot a = a \) silently; they follow from (F1), (F3), (F6) and (F7). The larger gain is that any school identity whose proof uses only (F1)–(F9) is true in every field: for instance \( (a + b)^2 = a^2 + 2ab + b^2 \), where \( a^2 \coloneqq aa \) and \( 2 \coloneqq 1 + 1 \) (@fd3:prp-ring-algebra (d)), and \( (-a)(-b) = ab \) (@fd3:prp-ring-algebra (c)). Part (f) is the rule we will lean on most: a product of non-zero elements is non-zero.

::: {.remark}
Part (g), with the uniqueness of inverses in (c), is the content of @fd3:lem-field-fraction-rules (a) and (b), which *Number Systems* proved for every field when it studied ordered fields. Part (f) and the inverse identities of (g) come from the paragraphs on units after @fd3:def-ring-unit; the two fraction formulas are proved here rather than cited from @fd3:lem-field-fraction-rules, so that no theorem of this section rests on that chapter; only the examples \( \nR \) and \( \nC \) below lean on it.
:::

::: {.check}
In a field, does \( a^2 = 0 \) imply \( a = 0 \)?
:::

::: {.solution}
Yes. \( a^2 = aa = 0 \), so by @thm-field-basic-properties (f) with \( b = a \), \( a = 0 \) or \( a = 0 \).
:::

::: {.warning}
Cancellation needs its hypothesis. "If \( ab = ac \), then \( b = c \)" is **false** without \( a \ne 0 \): in \( \nQ \), \( 0 \cdot 1 = 0 \cdot 2 \), yet \( 1 \ne 2 \). Every time a factor is canceled, say why it is not \( 0 \).
:::

Part (f) has a consequence that school algebra uses all the time without naming it: an element has at most two square roots, and they are negatives of each other.

::: {#cor-field-squares-equal}
[Equal Squares]

Let \( F \) be a field and \( x, y \in F \). Then \( x^2 = y^2 \) if and only if \( x = y \) or \( x = -y \). In particular, \( x^2 = 1 \) if and only if \( x = 1 \) or \( x = -1 \).
:::

::: {.idea}
Move everything to one side and factor: \( x^2 - y^2 = (x - y)(x + y) \), the school identity, which holds in every field. A product is zero only when a factor is, by part (f), and the two factors give the two cases.
:::

::: {.proof}
First, \( (x - y)(x + y) = x^2 - y^2 \). Indeed, by (F9) and (F6), \( (x + (-y))(x + y) = xx + xy + (-y)x + (-y)y \), and @fd3:prp-ring-algebra (c) turns the last two terms into \( -(yx) \) and \( -(yy) \). Since \( yx = xy \) by (F6), the terms \( xy \) and \( -(xy) \) add to \( 0 \) by (F4), and what is left is \( x^2 - y^2 \).

\( (\Rightarrow) \) If \( x^2 = y^2 \), then \( x^2 - y^2 = y^2 + (-y^2) = 0 \) by (F4), so \( (x - y)(x + y) = 0 \). By @thm-field-basic-properties (f), \( x - y = 0 \) or \( x + y = 0 \). In the first case, adding \( y \) to both sides gives \( x = y \), by (F2), (F1), (F4) and (F3). In the second, \( y \) satisfies the defining equation of \( -x \), so \( y = -x \) by @thm-field-basic-properties (c), and then \( x = -(-x) = -y \) by @fd3:prp-ring-algebra (a).

\( (\Leftarrow) \) If \( x = y \), there is nothing to prove. If \( x = -y \), then \( x^2 = (-y)(-y) = yy = y^2 \) by @fd3:prp-ring-algebra (c).

For the last sentence take \( y = 1 \), with \( 1^2 = 1 \) by (F7).
:::

::: {.remark}
The two square roots \( y \) and \( -y \) can coincide even when \( y \ne 0 \): in the field with two elements of the next section, \( 1 + 1 = 0 \), so \( -1 = 1 \). And the corollary needs (f), so it can fail in a commutative ring with zero divisors. In \( \nZ/8\nZ \) we have \( [3]^2 = [9] = [1] \), yet \( [3] \ne [1] \) and \( [3] \ne [-1] = [7] \), since \( 8 \) divides neither \( 3 - 1 = 2 \) nor \( 3 - 7 = -4 \). For \( \nC \), Chapter 1 proved the same fact directly from real and imaginary parts (@prp-complex-square-roots (b)); the corollary gives it in every field at once.
:::

## Solving linear equations in a field

The opening slogan promised that a field is where elimination works. Here is that promise kept for one equation in one unknown and for two equations in two unknowns.

::: {#prp-field-linear-equation}
[Linear Equations in a Field]

Let \( F \) be a field and let \( a, b, c, d, e, f \in F \).

::: {.enumerate options="label=(\alph*)"}
1. If \( a \ne 0 \), the equation \( ax = b \) has **exactly one** solution \( x \in F \), namely \( x = a^{-1} b \).
2. If \( ad - bc \ne 0 \), the system
\[
\begin{aligned}
ax + by &= e, \\
cx + dy &= f
\end{aligned}
\]
has **exactly one** solution \( (x, y) \in F \times F \), namely
\[
x = \frac{ed - bf}{ad - bc}, \qquad y = \frac{af - ce}{ad - bc}.
\]
:::
:::

::: {.idea}
Uniqueness and existence are separate jobs. For uniqueness, assume a solution and run the school elimination on it: one combination of the two equations kills \( y \), another kills \( x \), and each leaves an equation of the form (a). For existence, substitute the candidate and multiply out. The quantity \( ad - bc \) is exactly the coefficient elimination produces, and the hypothesis lets us divide by it.
:::

::: {.proof}
(a) By (F5), (F8) and (F7), \( a(a^{-1} b) = (a a^{-1}) b = 1 \cdot b = b \), so \( x = a^{-1} b \) is a solution. If \( ax = b \) and \( ax' = b \), then \( ax = ax' \) with \( a \ne 0 \), so \( x = x' \) by cancellation (@thm-field-basic-properties (b)).

(b) Write \( D \coloneqq ad - bc \), so \( D \ne 0 \).

*Uniqueness.* Let \( (x, y) \) be a solution. Multiply the first equation by \( d \), the second by \( b \), and subtract. Multiplying out with (F9), reordering with (F5) and (F6), and using @fd3:prp-ring-algebra (c) for the signs,
\[
\begin{aligned}
d(ax + by) - b(cx + dy)
&= (ad)x + (bd)y - (bc)x - (bd)y \\
&= (ad - bc)x = Dx,
\end{aligned}
\]
while the right-hand sides give \( de - bf = ed - bf \). So \( Dx = ed - bf \). In the same way, \( a(cx + dy) - c(ax + by) = (ad - bc)y = Dy \) and the right-hand sides give \( af - ce \), so \( Dy = af - ce \). By (a), applied twice with the non-zero coefficient \( D \), \( x = D^{-1}(ed - bf) \) and \( y = D^{-1}(af - ce) \). These are the displayed values, since \( D^{-1} u = u D^{-1} = u / D \) by (F6).

*Existence.* Put \( x_0 \coloneqq (ed - bf) D^{-1} \) and \( y_0 \coloneqq (af - ce) D^{-1} \). By (F5), (F6) and (F9), multiplying out and reordering with (F5) and (F6), and using @fd3:prp-ring-algebra (c) for the signs,
\[
\begin{aligned}
a x_0 + b y_0
&= \big(a(ed - bf) + b(af - ce)\big) D^{-1} \\
&= (ade - abf + abf - bce) D^{-1} \\
&= e(ad - bc) D^{-1} = e D D^{-1} = e,
\end{aligned}
\]
by (F8) and (F7) at the end. Likewise
\[
\begin{aligned}
c x_0 + d y_0
&= \big(c(ed - bf) + d(af - ce)\big) D^{-1} \\
&= (cde - bcf + adf - cde) D^{-1} \\
&= f(ad - bc) D^{-1} = f.
\end{aligned}
\]
So \( (x_0, y_0) \) is a solution, and by uniqueness it is the only one.
:::

Both hypotheses have a job. Over \( \nZ \), part (a) fails: \( 2 \ne 0 \), and \( 2x = 1 \) has no integer solution, because the inverse \( 2^{-1} \) of (F8) is missing. And if \( ad - bc = 0 \), part (b) fails in every field: the system \( x + y = 1 \), \( x + y = 0 \) has no solution, since it would give \( 1 = 0 \), while \( x + y = 0 \), \( 2x + 2y = 0 \) has the solutions \( (t, -t) \) for every \( t \in F \), at least two of them (\( t = 0 \) and \( t = 1 \)). The linear-algebra volumes treat \( n \) equations in \( n \) unknowns by the same elimination.

## Examples

Three fields are already at hand. Each was proved a field in the sense of @fd3:def-commutative-ring-and-field, and the remark after @def-field translates.

::: {#exm-fields}
[The Fields \( \nQ \), \( \nR \) and \( \nC \)]

Explain why \( \nQ \), \( \nR \) and \( \nC \), with their usual addition and multiplication, are fields.
:::

::: {.solution}
For \( \nQ \), built as classes of pairs of integers, @fd3:thm-rationals-field proves that it is a field in the sense of @fd3:def-commutative-ring-and-field. For \( \nR \), built as classes of Cauchy sequences of rationals, @fd3:thm-reals-field does the same; there \( 1 \ne 0 \) is part of the field clause. For \( \nC \coloneqq \nR \times \nR \), @thm-complex-numbers-field proves it, resting on the arithmetic laws @prp-complex-arithmetic-laws and the inverse @prp-complex-inverse. In each case the remark after @def-field turns "field in the sense of *Number Systems*" into "field in the sense of @def-field", with the same zero, one, negatives and inverses.
:::

These three are infinite: each contains an injective image of the infinite set \( \nN \) (@fd2:exm-hilbert-hotel), through @fd3:prp-naturals-embed-integers (a), @fd3:prp-integers-embed-rationals, @fd3:thm-rational-embedding (b) and @prp-reals-embed-complex. A finite set has only finite subsets (@fd2:prp-subset-finite). The next section produces finite fields, and Section 2.3 produces fields strictly between \( \nQ \) and \( \nR \).

Changing an operation on a familiar set can give a new field; deciding means checking every clause.

::: {#exm-field-negated-product}
[A New Multiplication on \( \nQ \)]

Show that \( \nQ \), with the usual addition and the new multiplication \( a \odot b \coloneqq -(ab) \), is a field, and find its one.
:::

::: {.solution}
Addition is that of \( \nQ \), so (F1)–(F4) hold with the usual \( 0 \) and negatives. The new product is a function \( \nQ \times \nQ \to \nQ \). Each identity below is computed in the field \( \nQ \) (@exm-fields), the signs by @fd3:prp-ring-algebra (a) and (c). For all \( a, b, c \in \nQ \):

- (F5): \( (a \odot b) \odot c = -\big((-(ab))c\big) = abc = -\big(a(-(bc))\big) = a \odot (b \odot c) \).
- (F6): \( -(ab) = -(ba) \).
- (F9): \( a \odot (b + c) = -(ab + ac) = -(ab) + (-(ac)) = a \odot b + a \odot c \), since \( -(u + v) = (-1)(u + v) = -u + (-v) \) by @thm-field-basic-properties (e).
- (F7): the one is \( -1 \), since \( a \odot (-1) = -(a(-1)) = -(-a) = a \), and \( -1 \ne 0 \) (otherwise \( 1 = -(-1) = -0 = 0 \), where \( -0 = 0 \) by @thm-field-basic-properties (c), since \( 0 + 0 = 0 \)).
- (F8): a non-zero \( a \) has the inverse \( a^{-1} \), the usual one, since \( a \odot a^{-1} = -(aa^{-1}) = -1 \), the one of this field.

The one of a field need not be the number \( 1 \).
:::

## Non-examples {#non-examples}

Each system below falls short of the slogan somewhere. For each, find the precise clause that breaks; a vague "it is not like \( \nQ \)" teaches nothing.

::: {#exm-field-nonexamples}
[Four Systems That Are Not Fields]

For each of the following, with its usual operations, name the clauses of @def-field that fail, with a witness: (i) \( \nN \); (ii) \( \nZ \); (iii) the zero ring \( \{0\} \), with \( 0 + 0 \coloneqq 0 \) and \( 0 \cdot 0 \coloneqq 0 \); (iv) \( \nZ/6\nZ \).
:::

::: {.solution}
(i) *Number Systems* checked the minimal change from \( \nN \) to \( \nZ \): \( \nN \) satisfies (F1)–(F3), (F5)–(F7) and (F9), and (F4) fails at \( a = 1 \), since \( 1 + x \ne 0 \) for every \( x \in \nN \) (the non-example after @fd3:def-commutative-ring-and-field). The condition \( 1 \ne 0 \) holds, since it holds in \( \nZ \) (@fd3:thm-integers-commutative-ring), and \( \nN \subseteq \nZ \) with \( \iota \) injective (@fd3:prp-naturals-embed-integers (a)). Clause (F8) fails too, at \( a = 2 \): a natural number \( x \) with \( 2x = 1 \) would be an integer with \( 2x = 1 \) (\( \iota \) preserves products, @fd3:prp-naturals-embed-integers (a)), and there is none (@fd3:cor-integers-even-odd (a)).

(ii) \( \nZ \) is a commutative ring with \( 1 \ne 0 \) (@fd3:thm-integers-commutative-ring), so (F1)–(F7) and (F9) hold. Only (F8) fails, at \( a = 2 \), by the same parity argument.

(iii) Every clause other than (F7) and (F8) is an equation between elements of \( \{0\} \), and each such equation reads \( 0 = 0 \); (F8) holds because there is no non-zero element to invert. The only candidate for the element \( 1 \) of (F7) is \( 0 \), and (F7) demands \( 1 \ne 0 \). So exactly the condition \( 1 \ne 0 \) inside (F7) fails. This is the reason the condition is there: without it, a one-element "field" would make every statement of the form "a field has a non-zero element" false.

(iv) \( \nZ/6\nZ \) is a commutative ring with \( [1] \ne [0] \) (@fd3:thm-integers-mod-n-ring (a), (c)), so (F1)–(F7) and (F9) hold. But \( [2][3] = [6] = [0] \) (@fd3:exm-integers-mod-six), while \( [2] \ne [0] \) and \( [3] \ne [0] \), since \( 6 \) divides neither \( 2 \) nor \( 3 \). If \( [2] \) had an inverse \( u \), then \( [3] = (u[2])[3] = u([2][3]) = u[0] = [0] \), by (F7), (F8), (F6), (F5) and @fd3:prp-ring-algebra (b), which is false. So (F8) fails at \( [2] \). Had \( \nZ/6\nZ \) been a field, @thm-field-basic-properties (f) would have forbidden the product \( [2][3] = [0] \) outright.
:::

The first linear-algebra volume meets one more kind of non-example, the square matrices, where (F6) fails: two matrices can give different products in the two orders.

## Why these axioms

Drop a clause and something we use breaks.

- **Without (F8)**, elimination halts at the first coefficient that cannot be inverted, as \( 2x = 1 \) over \( \nZ \) showed.
- **Without (F6)**, numbers would not commute with each other. Linear algebra swaps scalars constantly (in the first linear-algebra volume, when a vector is multiplied by two numbers in turn), so commutativity is kept.
- **Without \( 1 \ne 0 \)**, the zero ring of @exm-field-nonexamples (iii) would count as a field.

The word "field" is a historical label; nothing in it is meant literally.

::: {.warning}
Order is not part of a field. Clauses (F1)–(F9) say nothing about \( < \), so "squares are \( \ge 0 \)" has no meaning in a general field, and read in \( \nC \) it is false, since \( i^2 = -1 \) (Chapter 1). Likewise "\( 1 + 1 \ne 0 \)" is not a clause, and it fails in the field with two elements of the next section. In a general field, never use an inequality.
:::

## Exercises

### A. Check your understanding

::: {#exr-field-axioms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the definition of a field.
2. Which clauses of @def-field does each of \( \nN \), \( \nZ \) and the zero ring \( \{0\} \) fail?
3. True or false: in every field, \( ab = ac \) implies \( b = c \). Justify your answer.
4. Which parts of @thm-field-basic-properties fail in the commutative ring \( \nZ/6\nZ \)? Give a witness for each.
5. Use @prp-field-linear-equation to solve \( 3x + 2y = 1 \), \( x - y = 2 \) in \( \nQ \).
:::
:::

::: {.solution}
(a) A field is a set \( F \) with two functions \( + , \cdot \colon F \times F \to F \) satisfying (F1)–(F9) of @def-field, where (F7) includes \( 1 \ne 0 \) and (F8) asks for inverses of non-zero elements only.

(b) \( \nN \): (F4), at \( a = 1 \), and (F8), at \( a = 2 \). \( \nZ \): only (F8), at \( a = 2 \). \( \{0\} \): only the condition \( 1 \ne 0 \) in (F7). (See @exm-field-nonexamples.)

(c) False. With \( a = 0 \), \( b = 1 \), \( c = 2 \) in \( \nQ \): \( 0 \cdot 1 = 0 = 0 \cdot 2 \), but \( 1 \ne 2 \). Cancellation needs \( a \ne 0 \) (@thm-field-basic-properties (b)).

(d) Multiplicative cancellation in (b) fails: \( [2][1] = [2] \) and \( [2][4] = [8] = [2] \), but \( [1] \ne [4] \), since \( 6 \) does not divide \( 4 - 1 = 3 \). Part (f) fails: \( [2][3] = [0] \) with \( [2], [3] \ne [0] \). The first clause of (g) fails for the same pair: \( [2] \ne [0] \), \( [3] \ne [0] \), but \( [2][3] = [0] \). The uniqueness of inverses in (c) is not violated, but for \( [2] \) it says nothing, since \( [2] \) has no inverse (@exm-field-nonexamples (iv)). Parts (a), (d) and (e) hold in every commutative ring (@fd3:prp-ring-algebra (a)–(c), with (F6), (F7)), and so does additive cancellation, whose proof in (b) uses only (F1)–(F4).

(e) Here \( a = 3 \), \( b = 2 \), \( c = 1 \), \( d = -1 \), \( e = 1 \), \( f = 2 \), and \( ad - bc = -3 - 2 = -5 \ne 0 \). So
\[
x = \frac{1 \cdot (-1) - 2 \cdot 2}{-5} = \frac{-5}{-5} = 1, \qquad y = \frac{3 \cdot 2 - 1 \cdot 1}{-5} = \frac{5}{-5} = -1.
\]
Check: \( 3 \cdot 1 + 2 \cdot (-1) = 1 \) and \( 1 - (-1) = 2 \).
:::

### B. Practice

::: {#exr-field-axioms-b1}
[B1]

Let \( F \) be a field and \( a, b, x \in F \). Prove:

::: {.enumerate options="label=(\alph*)"}
1. \( -(a - b) = b - a \);
2. if \( a \ne 0 \), then \( -a \ne 0 \) and \( (-a)^{-1} = -(a^{-1}) \);
3. \( x^2 = x \) if and only if \( x = 0 \) or \( x = 1 \);
4. \( x^2 + x = 0 \) if and only if \( x = 0 \) or \( x = -1 \).
:::
:::

::: {.solution}
(a) By (F1) and (F2), \( (a - b) + (b - a) = \big(a + (-a)\big) + \big(b + (-b)\big) = 0 + 0 = 0 \), using (F4) and (F3). So \( b - a \) satisfies the defining equation of \( -(a - b) \), and \( -(a - b) = b - a \) by the uniqueness of negatives (@thm-field-basic-properties (c)).

(b) If \( -a = 0 \), then \( a = -(-a) = -0 = 0 \), by @fd3:prp-ring-algebra (a) and \( 0 + 0 = 0 \); so \( -a \ne 0 \). By @fd3:prp-ring-algebra (c) and (F8), \( (-a)\big(-(a^{-1})\big) = a a^{-1} = 1 \). So \( -(a^{-1}) \) satisfies the defining equation of \( (-a)^{-1} \), and the two are equal by @thm-field-basic-properties (c).

(c) By (F7), (F9) and @fd3:prp-ring-algebra (c), \( x(x - 1) = xx + x(-1) = x^2 - x \). So \( x^2 = x \) if and only if \( x(x - 1) = 0 \), adding \( -x \) or \( x \) to both sides. By @thm-field-basic-properties (f), \( x(x - 1) = 0 \) gives \( x = 0 \) or \( x - 1 = 0 \), that is, \( x = 1 \). Conversely, \( 0^2 = 0 \) by @thm-field-basic-properties (d), and \( 1^2 = 1 \) by (F7).

(d) By (F7) and (F9), \( x(x + 1) = x^2 + x \). So \( x^2 + x = 0 \) means \( x(x + 1) = 0 \), which by @thm-field-basic-properties (f) gives \( x = 0 \) or \( x + 1 = 0 \), and the latter means \( x = -1 \) by the uniqueness of negatives (@thm-field-basic-properties (c)). Conversely, \( 0^2 + 0 = 0 \) by @thm-field-basic-properties (d) and (F3), and \( (-1)^2 + (-1) = 1 + (-1) = 0 \), since \( (-1)(-1) = 1 \cdot 1 = 1 \) by @fd3:prp-ring-algebra (c).
:::

::: {#exr-field-axioms-b2}
[B2]

Let \( F \) be a field and \( a, b, c, d \in F \) with \( b \ne 0 \) and \( d \ne 0 \). Prove that \( a/b = c/d \) if and only if \( ad = bc \).
:::

::: {.solution}
\( (\Rightarrow) \) Multiply both sides of \( a b^{-1} = c d^{-1} \) by \( bd \). Reordering with (F5) and (F6), and using (F8) and (F7), the left side becomes \( a (b^{-1} b) d = ad \) and the right side \( c (d^{-1} d) b = cb = bc \). So \( ad = bc \).

\( (\Leftarrow) \) By @thm-field-basic-properties (g), \( bd \ne 0 \) and \( (bd)^{-1} = b^{-1} d^{-1} \). Multiply both sides of \( ad = bc \) by \( b^{-1} d^{-1} \): reordering as before, the left side becomes \( a b^{-1} (d d^{-1}) = a b^{-1} \) and the right side \( (b b^{-1}) c d^{-1} = c d^{-1} \). So \( a / b = c / d \).
:::

::: {#exr-field-axioms-b3}
[B3: Which Are Fields?]

Determine which of the following are fields. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nQ \), with the usual addition and the new multiplication \( a \odot b \coloneqq 2ab \).
2. \( \nQ \), with the usual addition and the new multiplication \( a \odot b \coloneqq ab + 1 \).
3. The set \( \{0, 1\} \subseteq \nQ \), with the addition and multiplication of \( \nQ \).
:::
:::

::: {.solution}
(a) **A field.** Addition is that of \( \nQ \), so (F1)–(F4) hold with the usual \( 0 \) and negatives. The new product is a function \( \nQ \times \nQ \to \nQ \). For all \( a, b, c \in \nQ \): (F5) \( (a \odot b) \odot c = 2(2ab)c = 4abc = 2a(2bc) = a \odot (b \odot c) \); (F6) \( 2ab = 2ba \); (F9) \( a \odot (b + c) = 2a(b + c) = 2ab + 2ac = a \odot b + a \odot c \). For (F7) the one is \( \tfrac12 \): \( a \odot \tfrac12 = 2a \cdot \tfrac12 = a \), and \( \tfrac12 \ne 0 \). For (F8), a non-zero \( a \) has the inverse \( \tfrac{1}{4a} \), since \( a \odot \tfrac{1}{4a} = \tfrac{2a}{4a} = \tfrac12 \), the one of this field. Each identity is computed in the field \( \nQ \) (@exm-fields). The one of a field need not be the number \( 1 \); Exercise B3 of Section 2.4 shows that this field is \( \nQ \) in disguise.

(b) **Not a field:** (F9) fails. For all \( a, b, c \), \( a \odot (b + c) = ab + ac + 1 \), while \( a \odot b + a \odot c = ab + ac + 2 \), and \( 1 \ne 2 \). For instance \( a = b = c = 0 \) gives \( 1 \ne 2 \).

(c) **Not a field:** addition is not a function \( \{0, 1\} \times \{0, 1\} \to \{0, 1\} \), since \( 1 + 1 = 2 \notin \{0, 1\} \). (The next section puts a different addition on a two-element set and obtains a field.)
:::

### C. Going deeper

::: {#exr-field-axioms-c1}
[C1: Exit check: rules from the axioms]

Let \( F \) be a field and \( a, b, x, y \in F \). Prove the following from (F1)–(F9), using of @thm-field-basic-properties only part (c) (uniqueness of negatives and inverses) and part (e) (\( (-1)a = -a \)), and citing no result of *Number Systems*.

::: {.enumerate options="label=(\alph*)"}
1. \( 0 \cdot a = 0 \).
2. If \( ab = 0 \), then \( a = 0 \) or \( b = 0 \).
3. \( x^2 = y^2 \) if and only if \( x = y \) or \( x = -y \).
:::
:::

::: {.solution}
(a) By (F3), \( 0 + 0 = 0 \), so by (F9), \( a \cdot 0 = a(0 + 0) = a \cdot 0 + a \cdot 0 \). Add \( -(a \cdot 0) \), which exists by (F4), to both sides. On the left this gives \( 0 \). On the right, by (F2), (F4) and (F3), \( (a \cdot 0 + a \cdot 0) + (-(a \cdot 0)) = a \cdot 0 + \big(a \cdot 0 + (-(a \cdot 0))\big) = a \cdot 0 + 0 = a \cdot 0 \). So \( 0 = a \cdot 0 \), and \( 0 \cdot a = a \cdot 0 = 0 \) by (F6).

(b) Suppose \( ab = 0 \). If \( a = 0 \), we are done. Otherwise \( a^{-1} \) exists by (F8), and by (F7), (F8), (F5) and (F6),
\[
b = b \cdot 1 = b (a a^{-1}) = (ba) a^{-1} = (ab) a^{-1} = 0 \cdot a^{-1} = 0,
\]
the last step by (a).

(c) *Two sign rules.* For \( u, v \in F \), part (e), (F5) and (F6) give \( (-u)v = ((-1)u)v = (-1)(uv) = -(uv) \). Hence \( (-1)(-1) = -(1 \cdot (-1)) = -(-1) = 1 \), where \( 1 \cdot (-1) = -1 \) by (F6), (F7), and \( -(-1) = 1 \) by part (c), since \( (-1) + 1 = 0 \) by (F1), (F4). So \( (-y)(-y) = ((-1)y)((-1)y) = ((-1)(-1))(yy) = yy \), by (F5) and (F6).

*The factorization.* By (F9), (F6) and the first sign rule,
\[
\begin{aligned}
(x + (-y))(x + y) &= xx + xy + (-y)x + (-y)y \\
&= xx + xy + (-(xy)) + (-(yy)),
\end{aligned}
\]
using \( yx = xy \) by (F6). By (F2), (F4) and (F3) the middle terms cancel, so \( (x - y)(x + y) = x^2 - y^2 \).

\( (\Rightarrow) \) If \( x^2 = y^2 \), then \( x^2 - y^2 = 0 \) by (F4), so \( (x - y)(x + y) = 0 \), and (b) gives \( x - y = 0 \) or \( x + y = 0 \). From \( x - y = 0 \), adding \( y \) and using (F2), (F1), (F4), (F3) gives \( x = y \). From \( x + y = 0 \), \( x \) satisfies the defining equation of \( -y \) (with (F1)), so \( x = -y \) by part (c).

\( (\Leftarrow) \) If \( x = y \) there is nothing to prove; if \( x = -y \), then \( x^2 = (-y)(-y) = y^2 \) by the sign rules.

**Marking scheme.** (10 points)

- 2: for (a), writes \( 0 = 0 + 0 \) and multiplies out \( a(0 + 0) \) by (F9).
- 2: cancels \( a \cdot 0 \) by adding its negative, naming (F2), (F4) and (F3).
- 1: obtains \( 0 \cdot a \) from \( a \cdot 0 \) by (F6).
- 2: for (b), treats the case \( a = 0 \) separately and spends \( a \ne 0 \) on (F8).
- 1: writes the chain \( b = b \cdot 1 = \dots = 0 \) with each clause named.
- 1: proves \( (x - y)(x + y) = x^2 - y^2 \), justifying the cancellation of \( xy \) against \( -(yx) \), and concludes by (b).
- 1: proves the converse, deriving \( (-y)(-y) = yy \) from part (e), (F5) and (F6).

Fatal errors (0 for the step): dividing by \( a \) without \( a \ne 0 \); "\( 0 \cdot a = 0 \) is obvious"; citing (b) of the exercise inside the proof of (a). A proof of (c) that factors as \( (x + y)(x - y) \) or that cites (b) as "no zero divisors" earns the same points.
:::

::: {#exr-field-axioms-c2}
[C2: Find the error]

Here is a claim with a proof.

> **Claim.** In a field \( F \), if \( x \in F \) and \( x^2 = x \), then \( x = 0 \) or \( x = 1 \).
>
> **Proof.** (1) Let \( x^2 = x \). (2) Dividing both sides by \( x \) gives \( x = 1 \). (3) So \( x = 0 \) or \( x = 1 \).

Is the claim true? Does the proof prove it? If not, name the line that fails, the error, and give a counterexample to the step.
:::

::: {.solution}
The **claim is true**: it is @exr-field-axioms-b1 (c).

The **proof is wrong**, at line (2). Dividing by \( x \) means multiplying by \( x^{-1} \), which (F8) supplies only when \( x \ne 0 \). No line provides \( x \ne 0 \), so the step cites an unavailable "fact", cancellation of \( x \) without \( x \ne 0 \): entry (N9) of @fd1:exm-not-allowed-catalogue. Line (3) is a correct weakening of (2) by \( \rulename{\vee I} \); the proof fails only at (2).

A counterexample to the step: \( x = 0 \) satisfies \( x^2 = x \), and "\( x = 1 \)" is false for it, in every field. The step's conclusion fails, although the claim's does not.

A repair: \( x^2 = x \) gives \( x(x - 1) = 0 \), and @thm-field-basic-properties (f) gives \( x = 0 \) or \( x - 1 = 0 \), which treats both cases at once.
:::

<!-- dependency ledger
def-field (claim): (hook before it) 2 = 1 + 1 and 5y = 5 arithmetic in Q | inline school arithmetic, an illustration before any definition
def-field (claim): (hook before it) 2x = 1 has no integer solution | fd3:cor-integers-even-odd (a), with 1 = 2 * 0 + 1, cited
def-field (claim): (remark after it) the clauses of def-field and fd3:def-commutative-ring-and-field correspond one to one, 1 != 0 filed in (F7) here | inline comparison of the two clause lists (restatement; atlas label-triage records def-field as same as fd3:def-commutative-ring-and-field)
def-field (claim): (quick check after it) Q_{>0} closed under +, * | fd3:thm-rationals-ordered-field, (P1) of fd3:prp-order-from-positives, cited
def-field (claim): (quick check after it) 1 + z = 1 forces z = 0 | (F1)-(F4) in Q (fd3:thm-rationals-field), inline
thm-field-basic-properties (proof): parts (a), (c) negatives, (d), (e) from the commutative-ring algebra | fd3:prp-ring-algebra (a)-(c), cited, via the remark after def-field
thm-field-basic-properties (proof): uniqueness of inverses of units | fd3:def-ring-unit and its well-definedness paragraph, cited
thm-field-basic-properties (proof): (f) a unit is not a zero divisor; (g) bd != 0, (bd)^{-1} = b^{-1}d^{-1}, (b^{-1})^{-1} = b, b^{-1} != 0 | (f) of this theorem; fd3:def-ring-unit, its closure paragraph, the paragraph 'A unit is not a zero divisor' and 'Why this definition' (0 is not a unit when 1 != 0), cited
thm-field-basic-properties (claim): (aftermath) 0 + a = a, 1 * a = a; (a + b)^2, (-a)(-b) = ab | (F1), (F3), (F6), (F7); fd3:prp-ring-algebra (c), (d), cited
thm-field-basic-properties (claim): (remark after it) (g) is fd3:lem-field-fraction-rules (a), (b) | comparison only (F3.9 soft citation); nothing rests on it
cor-field-squares-equal (proof): (x - y)(x + y) = x^2 - y^2 | (F9), (F6), (F4), fd3:prp-ring-algebra (c), inline
cor-field-squares-equal (claim): (remark after it) -1 = 1 in the two-element field | exm-finite-fields (next section), prose pointer within the chapter; nothing rests on it
cor-field-squares-equal (claim): (remark after it) [3]^2 = [1] in Z/8Z, [3] != [1], [7] | fd3:thm-quotient-ring-by-ideal (b), (d) on representatives, inline; verify/ch02/cor-field-squares-equal.py
cor-field-squares-equal (claim): (remark after it) the case of C | prp-complex-square-roots (b) (F4.1, see edge; comparison only)
prp-field-linear-equation (proof): expanding d(ax + by) - b(cx + dy) and the existence identities | (F5), (F6), (F9), fd3:prp-ring-algebra (c), inline; verify/ch02/prp-field-linear-equation.py (identity checked on a grid of rationals)
prp-field-linear-equation (claim): (aftermath) x + y = 1, x + y = 0 inconsistent; (t, -t) solutions, t = 0, 1 distinct | inline, (F7)
exm-fields (solution): Q, R, C are fields | fd3:thm-rationals-field, fd3:thm-reals-field (F3.10 soft citation, example), thm-complex-numbers-field, prp-complex-arithmetic-laws, prp-complex-inverse (F4.1 see edge, example only), cited
exm-fields (claim): (after it) Q, R, C infinite | fd3:prp-naturals-embed-integers (a), fd3:prp-integers-embed-rationals, fd3:thm-rational-embedding (b) (F3.10 soft; reported), prp-reals-embed-complex, fd2:exm-hilbert-hotel, fd2:prp-subset-finite, cited
exm-field-negated-product (solution): (F1)-(F9) for a o b = -(ab) | in Q (exm-fields), fd3:prp-ring-algebra (a), (c), thm-field-basic-properties (c), (e); verify/ch02/exm-field-negated-product.py
exm-field-nonexamples (solution): N inside Z | fd3:prp-naturals-embed-integers (a), cited (blueprint names (c); reported)
exm-field-nonexamples (solution): N satisfies (F1)-(F3), (F5)-(F7), (F9), fails (F4) at 1 | the non-example paragraph after fd3:def-commutative-ring-and-field (F3.2), quoted, not reproved
exm-field-nonexamples (solution): Z is a commutative ring with 1 != 0 | fd3:thm-integers-commutative-ring (F3.2; not in the blueprint's allowed list, which names F3.2's def-commutative-ring-and-field and prp-ring-algebra; reported)
exm-field-nonexamples (solution): Z/6Z commutative ring, [1] != [0], [2][3] = [0], 6 does not divide 2, 3 | fd3:thm-integers-mod-n-ring (a), (c), fd3:exm-integers-mod-six, cited; fd3:prp-divisibility-rules-integers (e); verify/ch02/exm-field-nonexamples.py
exm-field-nonexamples (claim): (paragraph after it; why these axioms) square matrices fail (F6); n equations in n unknowns | the linear-algebra volumes, prose pointers; nothing rests on them
exm-field-nonexamples (claim): (warning on order after it) i^2 = -1 in C | def-complex-numbers (F4.1), prose
exr-field-axioms-a1 (solution): witnesses in Z/6Z; the system 3x + 2y = 1, x - y = 2 | verify/ch02/exr-field-axioms-a1.py
exr-field-axioms-b1 (solution): -0 = 0 | (F3) with uniqueness of negatives, inline
exr-field-axioms-b3 (solution): the axioms for (Q, +, odot), inverse 1/(4a); (F9) failing for ab + 1 | computed in the field Q (exm-fields); verify/ch02/exr-field-axioms-b3.py
exr-field-axioms-b3 (solution): Section 2.4 B3 shows (Q, +, odot) is isomorphic to Q | prose pointer within the chapter (exr-field-homomorphisms-b3); nothing rests on it
exr-field-axioms-c2 (solution): (N9) | fd1:exm-not-allowed-catalogue, cited
-->
