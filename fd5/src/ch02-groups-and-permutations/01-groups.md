# Groups

Several structures met so far behave alike: the integers under addition, the non-zero rationals under multiplication, the units of \( \nZ/n\nZ \) (*Number Systems: From \(\nN\) to \(\nR\)*, Section 3.5), and the bijections of a set under composition (*Sets, Relations, and Cardinality*, Chapter 1). This section names their common structure, a group, and proves its basic laws once, from three axioms, so that they hold in all of these at once. It then makes two habits honest: dropping brackets from a product of many factors, and writing powers \( g^n \) with \( n \in \nZ \).

Throughout the chapter \( \nN \) is \( \omega \), and \( \nZ \), \( \nQ \) are the integers and rationals built in *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 2. Induction and recursion on \( \nN \) are @fd1:ax-induction and @fd2:thm-recursion, read on \( \omega \) through @fd3:cor-omega-identification (b). Strong induction, @fd1:thm-strong-induction, holds on \( \omega \) too, since its proof uses only @fd1:ax-induction and the order facts @fd3:thm-omega-order (a), (b), (d).

## Four situations side by side

Look at four situations in which two things are combined into a third.

- In \( (\nZ, +) \) we add integers. The integer \( 0 \) does nothing, \( a + 0 = a \), and \( -a \) undoes \( a \), \( a + (-a) = 0 \).
- In \( \nQ \setminus \{0\} \) we multiply. The rational \( 1 \) does nothing, and \( a^{-1} \) undoes \( a \).
- Among the units of \( \nZ/12\nZ \), which are \( [1], [5], [7], [11] \) by @fd3:thm-units-mod-n (the classes of the integers coprime to \( 12 \)), we multiply classes. The class \( [1] \) does nothing, and each unit undoes itself: \( [5][5] = [25] = [1] \), \( [7][7] = [49] = [1] \) and \( [11][11] = [121] = [1] \), since \( 25 = 2 \cdot 12 + 1 \), \( 49 = 4 \cdot 12 + 1 \) and \( 121 = 10 \cdot 12 + 1 \).
- Among the bijections \( X \to X \) of a set we compose. The identity map \( \id_X \) does nothing, and each bijection \( f \) is undone by its inverse \( f^{-1} \) (@fd2:def-inverse-function).

The objects differ, and so do the ways of combining them, but the rules used are the same three: the combining is associative, one element changes nothing, and every element can be undone. So we give the pattern a name.

*A group is a set with one way of combining two elements into a third, in which combining is associative, some element does nothing, and every element can be undone.*

::: {#def-group}
[Group]

A **group** is a set \( G \) together with a **binary operation** on \( G \), that is, a function \( G \times G \to G \), \( (a, b) \mapsto ab \) (@fd2:def-function, with \( G \times G \) the Cartesian product of @fd2:def-cartesian-product), such that:

::: {.enumerate options="label=(G\arabic*)"}
1. **(Associativity)** \( (ab)c = a(bc) \) **for all** \( a, b, c \in G \);
2. **(Identity)** **there is** an element \( e \in G \) with \( ea = ae = a \) **for every** \( a \in G \);
3. **(Inverses)** **for every** \( a \in G \) **there is** \( b \in G \) with \( ab = ba = e \), where \( e \) is the element of (G2).
:::

The group is **abelian** if moreover \( ab = ba \) **for all** \( a, b \in G \).
:::

In words: the operation is a function on pairs, so the combination of two elements of \( G \) **lies in \( G \)** again. This "closure" is not a fourth axiom; it is built into the phrase "binary operation \( G \times G \to G \)". (G1) says that the two ways of combining three elements in a fixed order agree. (G2) asks for an element that changes nothing, from **both** sides. (G3) asks that each element can be undone, again from both sides, back to that same \( e \).

We write a group as \( (G, \cdot) \), or simply \( G \) when the operation is clear, and call \( ab \) the **product** of \( a \) and \( b \), whatever the operation is. When the operation is an addition we write \( a + b \), \( 0 \) and \( -a \) in place of \( ab \), \( e \) and the inverse of \( a \). This **additive notation** is used only for abelian groups.

::: {#exm-groups}
[Groups]

Check that each of (a)–(d) is a group, and decide which are abelian.

::: {.enumerate options="label=(\alph*)"}
1. \( (R, +) \) for a commutative ring \( R \) (@fd3:def-commutative-ring-and-field); in particular \( (\nZ, +) \), \( (\nQ, +) \), \( (\nR, +) \) and \( (\nZ/n\nZ, +) \) for \( n \in \nZ_{>0} \).
2. \( (\nQ \setminus \{0\}, \cdot) \), and \( (F \setminus \{0\}, \cdot) \) for any field \( F \); in particular \( (\nZ/p\nZ \setminus \{[0]\}, \cdot) \) for a prime \( p \).
3. The set of bijections \( X \to X \) of a set \( X \), under composition \( \circ \).
4. A one-element set \( \{e\} \) with \( ee \coloneqq e \).
5. (A fifth situation, described here and checked in Section 2.4.) The four rotations of a square about its center, by no turn, a quarter turn, a half turn and three quarter turns. Label the corners \( 1, 2, 3, 4 \) in order around the square; the quarter turn moves each label to the next corner, which is the bijection \( i \mapsto i + 1 \) for \( i < 4 \), \( 4 \mapsto 1 \) of \( \{1, 2, 3, 4\} \). Two rotations in a row make a rotation, the rotation by no turn changes nothing, and each rotation is undone by turning back.
:::
:::

::: {.solution}
*(a)* Recall the clauses (F1)–(F4) of @fd3:def-commutative-ring-and-field: addition is commutative (F1) and associative (F2), \( a + 0 = a \) (F3), and \( a + (-a) = 0 \) (F4). Addition is a function \( R \times R \to R \) by the definition, so it is a binary operation. (G1) is (F2). For (G2), \( a + 0 = a \) is (F3), and \( 0 + a = a + 0 = a \) by (F1). For (G3), \( a + (-a) = 0 \) is (F4), and \( (-a) + a = 0 \) by (F1). The group is abelian by (F1). The instances: \( \nZ \) is a commutative ring by @fd3:thm-integers-commutative-ring, \( \nQ \) by @fd3:thm-rationals-field, \( \nR \) by @fd3:thm-reals-ordered-field, and \( \nZ/n\nZ \) by @fd3:thm-integers-mod-n-ring (a).

*(b)* Let \( F \) be a field (in the form of @fd3:def-commutative-ring-and-field; Chapter 1 restates the definition as @def-field), for instance \( F = \nQ \) (@fd3:thm-rationals-field). The first thing to check is that multiplication lands in \( F \setminus \{0\} \). If \( x \ne 0 \) and \( y \ne 0 \), then \( x \) is a unit by (F8), and a unit is not a zero divisor (the paragraph after @fd3:def-ring-unit), so \( xy \ne 0 \). So a product of two non-zero elements is non-zero, and multiplication restricts to a binary operation on \( F \setminus \{0\} \). (G1) is (F5). For (G2), \( 1 \ne 0 \) in a field, so \( 1 \in F \setminus \{0\} \), and \( a \cdot 1 = 1 \cdot a = a \) by (F7) and (F6). For (G3), let \( a \ne 0 \); then \( aa^{-1} = a^{-1}a = 1 \) by (F8) and (F6), and \( a^{-1} \ne 0 \), since \( a^{-1} = 0 \) would give \( 1 = a \cdot 0 = 0 \) (@fd3:prp-ring-algebra (b)). The group is abelian by (F6). For a prime \( p \), \( \nZ/p\nZ \) is a field by @fd3:thm-integers-mod-prime-field, so \( \nZ/p\nZ \setminus \{[0]\} \) is a group under multiplication.

*(c)* Composition of two bijections \( X \to X \) is a bijection \( X \to X \) by @fd2:thm-composition-injective-surjective (c), so \( \circ \) is a binary operation on the set of bijections. (G1) holds by @fd2:prp-composition-associative, and the same result gives \( f \circ \id_X = f = \id_X \circ f \), so \( \id_X \), a bijection, satisfies (G2). For (G3), a bijection \( f \) has a two-sided inverse \( f^{-1} \) by @fd2:thm-bijection-iff-inverse, with \( f^{-1} \circ f = \id_X \) and \( f \circ f^{-1} = \id_X \) (@fd2:def-inverse-function). These two equations also say that \( f \) is a two-sided inverse of \( f^{-1} \), so \( f^{-1} \) is a bijection, again by @fd2:thm-bijection-iff-inverse.

Whether it is abelian depends on \( X \); the fold below decides it.

::: {.second-reading title="When is the group of bijections abelian?"}
If \( X \) has three distinct elements \( x, y, z \), let \( f \) swap \( x \) and \( y \) and fix every other point, and let \( g \) swap \( y \) and \( z \) and fix every other point. Each is its own inverse (\( f \circ f = \id_X \)), so each is a bijection. Then \( (f \circ g)(x) = f(x) = y \), while \( (g \circ f)(x) = g(y) = z \ne y \). So \( f \circ g \ne g \circ f \), and the group is **not** abelian. If \( X \) has at most two elements, there are at most two bijections, \( \id_X \) and the swap, and any two of them commute, since each commutes with \( \id_X \) and with itself. Section 2.4 meets this group again for \( X = \{1, \dots, n\} \) and computes in it.
:::

*(d)* All three axioms reduce to \( ee = e \): \( (ee)e = e = e(ee) \), \( e \) is an identity, and \( e \) is its own inverse. This **trivial group** is the degenerate case. It is abelian, and it reappears in Section 2.2 as the smallest subgroup of every group.

*(e)* is not checked here. Section 2.4 writes the four rotations as permutations of \( \{1, 2, 3, 4\} \), and its Exercise B3 shows that they behave exactly like \( \nZ/4\nZ \) under addition.
:::

::: {.remark}
The invertible \( n \times n \) matrices over a field form a group under matrix multiplication; *Spaces and Maps*, the chapter "Matrices", proves it. Nothing in this volume uses it.
:::

Now non-examples, each a minimal change of an example above.

::: {#exm-group-nonexamples}
[Not Groups]

For each of the following, say which of (G1)–(G3), or the binary operation itself, fails: \( (\nZ, \cdot) \); \( (\nN, +) \); \( \nZ \) with \( a \ast b \coloneqq a - b \); \( \nZ/6\nZ \setminus \{[0]\} \) under multiplication.
:::

::: {.solution}
*\( (\nZ, \cdot) \).* Replace addition by multiplication in (a). Multiplication is a binary operation on \( \nZ \), it is associative by (F5), and \( 1 \) is an identity by (F7) and (F6) (@fd3:thm-integers-commutative-ring). But (G3) fails at \( a = 2 \): if \( 2b = 1 \) for some \( b \in \nZ \), then \( 2 \mid 1 \), and @fd3:prp-divisibility-rules-integers (g) gives \( 2 = 1 \) or \( 2 = -1 \), which is false.

*\( (\nN, +) \).* Keep addition but shrink \( \nZ \) to \( \nN \). Addition still lands in \( \nN \) (@fd3:prp-naturals-embed-integers (a)), it is associative, and \( 0 \) is an identity, by (F1)–(F3) in \( \nZ \). But (G3) fails at \( a = 1 \): in \( \nZ \) the only \( b \) with \( 1 + b = 0 \) is \( -1 \) (uniqueness of negatives, @fd3:prp-ring-algebra (a)), and \( -1 < 0 \), so \( -1 \notin \nN \) by @fd3:thm-integers-ordered-ring (b).

*\( a \ast b \coloneqq a - b \) on \( \nZ \).* It is a binary operation, but (G1) fails: \( (1 \ast 1) \ast 1 = 0 - 1 = -1 \), while \( 1 \ast (1 \ast 1) = 1 - 0 = 1 \).

*\( \nZ/6\nZ \setminus \{[0]\} \) under multiplication.* Replace the prime \( p \) of (b) by \( 6 \). Here the operation itself fails: \( [2] \) and \( [3] \) lie in the set, but \( [2][3] = [6] = [0] \) does not (@fd3:exm-integers-mod-six), so (G1)–(G3) are not even in question.
:::

::: {.warning}
**Check closure first.** "\( \nZ_{>0} \) under subtraction" is not a group, and not because an axiom fails: \( 1 \) and \( 2 \) are positive integers, but \( 1 - 2 = -1 \) is not, so subtraction is not a binary operation on \( \nZ_{>0} \) at all. Before checking (G1)–(G3), check that combining two elements of the set gives an element of the set.
:::

## The basic laws, proved once

The rules we proved separately for functions (uniqueness of inverses) and for rings (uniqueness of \( 0 \), of \( -a \), of \( u^{-1} \)) follow from the three axioms alone. We prove them once:

::: {#thm-group-basic-properties}
[Basic Properties of Groups]

Let \( G \) be a group and \( a, b, c \in G \).

::: {.enumerate options="label=(\arabic*)"}
1. The identity element of \( G \) is unique.
2. The inverse of \( a \) is unique. We denote it by \( a^{-1} \).
3. \( (a^{-1})^{-1} = a \) and \( (ab)^{-1} = b^{-1}a^{-1} \).
4. **(Cancellation)** If \( ab = ac \), then \( b = c \). If \( ba = ca \), then \( b = c \).
5. The equations \( ax = b \) and \( ya = b \) have **exactly one** solution \( x \in G \) and **exactly one** solution \( y \in G \): \( x = a^{-1}b \) and \( y = ba^{-1} \).
:::
:::

::: {.idea}
Uniqueness is proved by taking two candidates and showing they are equal. For the identity, play the two identity properties against each other. For inverses, the only tools are (G1)–(G3), so insert \( e \) in a clever form and regroup. The candidate \( b^{-1}a^{-1} \) for the inverse of \( ab \) is found by undoing the last step first, as with putting on socks and then shoes.
:::

::: {.proof}
For (1), suppose \( e \) and \( e' \) both satisfy (G2). Then \( e = ee' \), using that \( e' \) is an identity, and \( ee' = e' \), using that \( e \) is one. Hence \( e = e' \).

For (2), suppose \( b \) and \( b' \) both satisfy (G3) for \( a \): \( ab = ba = e \) and \( ab' = b'a = e \). Multiply the equation \( ab' = e \) on the left by \( b \), and regroup by (G1):
\[
b = be = b(ab') = (ba)b' = eb' = b' ,
\]
where the first and last equalities are (G2), and \( ba = e \) is used in the fourth.

For (3), the equations \( aa^{-1} = a^{-1}a = e \) say that \( a \) is an inverse of \( a^{-1} \), so \( (a^{-1})^{-1} = a \) by (2). Next, by (G1) twice, then (G3), (G2) and (G3),
\[
(ab)(b^{-1}a^{-1}) = \bigl((ab)b^{-1}\bigr)a^{-1} = \bigl(a(bb^{-1})\bigr)a^{-1} = (ae)a^{-1} = aa^{-1} = e ,
\]
and in the same way \( (b^{-1}a^{-1})(ab) = \bigl((b^{-1}a^{-1})a\bigr)b = \bigl(b^{-1}(a^{-1}a)\bigr)b = (b^{-1}e)b = b^{-1}b = e \). By (2), \( (ab)^{-1} = b^{-1}a^{-1} \).

For (4), suppose \( ab = ac \). Multiplying on the left by \( a^{-1} \) and using (G1),
\[
b = eb = (a^{-1}a)b = a^{-1}(ab) = a^{-1}(ac) = (a^{-1}a)c = ec = c .
\]
The second statement follows by multiplying on the right by \( a^{-1} \).

For (5), \( x = a^{-1}b \) is a solution, since \( a(a^{-1}b) = (aa^{-1})b = eb = b \) by (G1), (G3) and (G2). If \( ax = b \) and \( ax' = b \), then \( ax = ax' \), so \( x = x' \) by (4). In the same way \( y = ba^{-1} \) solves \( ya = b \), since \( (ba^{-1})a = b(a^{-1}a) = b \), and it is the only solution by the second half of (4). This proves the theorem.
:::

Parts (2) and (4) use one move, and we give it a name: **multiply by the inverse**. To remove a factor from one side of an equation in a group, multiply both sides **on the same side** by its inverse, then regroup with (G1). The side matters, since a group need not be abelian; there is no "dividing by \( a \)".

Part (2) is the argument of @fd2:prp-inverse-unique, that a left inverse and a right inverse of a function agree, with functions erased; the uniqueness of the inverse of a unit in @fd3:def-ring-unit is the same argument once more. Part (1) is the argument for the uniqueness of \( 0 \) and \( 1 \) in @fd3:prp-ring-algebra (a). That is the point of the definition: a proof that uses only (G1)–(G3) holds in every group at once.

## Products of many factors

Part (3) had to write every bracket out. To write \( g_1 g_2 \cdots g_r \) with no brackets at all, we must say which product it means, and then check that the brackets do not matter. The definition uses the recursion that defined finite sums and products of reals.

::: {#def-group-list-product}
[Product of a List]

Let \( G \) be a group and \( r \in \nN \). A **list** of length \( r \) in \( G \) is a function \( \{1, \dots, r\} \to G \), written \( (g_1, \dots, g_r) \); for \( r = 0 \) it is the **empty list**. Its **product** \( g_1 g_2 \cdots g_r \in G \) is given by recursion: the product of the empty list is \( e \), and
\[
g_1 \cdots g_{j+1} \coloneqq (g_1 \cdots g_j)\, g_{j+1} \quad \text{for } 0 \le j < r ,
\]
where \( g_1 \cdots g_j \) is the product of the shortened list \( (g_1, \dots, g_j) \).
:::

In words: start with \( e \), and multiply on the right by one more entry at each stage. The product of a list of length \( 1 \) is \( eg_1 = g_1 \), the product of \( (g_1, g_2) \) is \( g_1g_2 \), and \( g_1g_2g_3 \) means \( (g_1g_2)g_3 \): **the brackets are nested to the left** by definition.

This is the recursion of @fd2:def-sum-product, stated there for products of real numbers and used here as a pattern with the group \( G \) in place of \( \nR \) and \( e \) in place of \( 1 \), as *Number Systems: From \(\nN\) to \(\nR\)*, Section 3.3 used it for products of integers (@fd3:def-prime-factorization). The recursion runs on \( \nN \) by @fd2:thm-recursion, after extending the list by \( g_k \coloneqq e \) for \( k > r \); the "Finite lists" remark after @fd2:def-sum-product shows that the products up to \( r \) do not depend on the extension. That remark only multiplies on the right; it never reorders factors, so it holds in a group that is not abelian.

::: {#prp-group-list-product-laws}
[Laws for Products of Lists]

Let \( G \) be a group, and let \( (g_1, \dots, g_r) \) and \( (h_1, \dots, h_s) \) be lists in \( G \).

::: {.enumerate options="label=(\alph*)"}
1. **(Concatenation)** \( (g_1 \cdots g_r)(h_1 \cdots h_s) = g_1 \cdots g_r h_1 \cdots h_s \), the product of the list \( (g_1, \dots, g_r, h_1, \dots, h_s) \) of length \( r + s \).
2. **(Brackets)** If \( r \ge 1 \), every bracketing of \( g_1, \dots, g_r \), in this order, has the value \( g_1 \cdots g_r \).
3. **(Inverses)** \( (g_1 \cdots g_r)^{-1} = g_r^{-1} \cdots g_1^{-1} \).
:::
:::

Here a **bracketing** of a list of length \( r \ge 1 \) is a way of inserting brackets, built by one rule: a single entry \( g_1 \) is a bracketing of \( (g_1) \), with value \( g_1 \); and for \( r \ge 2 \), a bracketing is \( (B)(B') \), where \( B \) is a bracketing of a first part \( (g_1, \dots, g_k) \) with \( 1 \le k < r \) and \( B' \) is a bracketing of the rest \( (g_{k+1}, \dots, g_r) \), with value the product of their values. For instance, \( (g_1g_2)(g_3g_4) \) and \( g_1(g_2(g_3g_4)) \) are bracketings of a list of length \( 4 \).

::: {.idea}
Each part is an induction that follows the recursion. For (a), induct on the length \( s \) of the second list: adding one entry to it multiplies both sides on the right by that entry, and (G1) moves the bracket. For (b), the outermost product of a bracketing joins two shorter bracketings, which the induction hypothesis turns into list products, and (a) joins those. For (c), part (3) of @thm-group-basic-properties reverses two factors at a time.
:::

::: {.proof}
(a) Fix the list \( (g_1, \dots, g_r) \) and write \( P \coloneqq g_1 \cdots g_r \). We prove the statement for every list \( (h_1, \dots, h_s) \) by @fd1:ax-induction on \( s \). For \( s = 0 \), the right side is the product of \( (g_1, \dots, g_r) \) itself, and the left side is \( Pe = P \) by (G2). Suppose the statement holds for lists of length \( s \), and let \( (h_1, \dots, h_{s+1}) \) be a list. Then
\[
\begin{aligned}
P\,(h_1 \cdots h_{s+1}) &= P\bigl((h_1 \cdots h_s)h_{s+1}\bigr) = \bigl(P\,(h_1 \cdots h_s)\bigr)h_{s+1} \\
&= (g_1 \cdots g_r h_1 \cdots h_s)\,h_{s+1} = g_1 \cdots g_r h_1 \cdots h_{s+1} ,
\end{aligned}
\]
by the recursion of @def-group-list-product, then (G1), then the induction hypothesis for the shortened list \( (h_1, \dots, h_s) \), and finally the recursion for the concatenated list at its last entry, \( h_{s+1} \).

Parts (b) and (c) are proved in the fold below. This proves (a).
:::

::: {.second-reading title="Proofs of (b) and (c): brackets and inverses"}
::: {.proof of="prp-group-list-product-laws"}
(b) We use @fd1:thm-strong-induction on \( r \), for the property "if \( r \ge 1 \), every bracketing of every list of length \( r \) has the value \( g_1 \cdots g_r \)"; for \( r = 0 \) there is nothing to prove. Let \( r \ge 1 \), and suppose the property holds for every smaller length. If \( r = 1 \), the only bracketing is \( g_1 \), and \( g_1 = eg_1 \) is the product of \( (g_1) \) by (G2) and the recursion. If \( r \ge 2 \), a bracketing is \( (B)(B') \) with \( B \) a bracketing of \( (g_1, \dots, g_k) \) and \( B' \) a bracketing of \( (g_{k+1}, \dots, g_r) \), where \( 1 \le k < r \). Both lengths, \( k \) and \( r - k \), are at least \( 1 \) and smaller than \( r \), so by the hypothesis the value of \( B \) is \( g_1 \cdots g_k \) and the value of \( B' \) is \( g_{k+1} \cdots g_r \). By (a), their product is the product of the concatenated list, which is \( (g_1, \dots, g_r) \). So the value of \( (B)(B') \) is \( g_1 \cdots g_r \). This completes the induction.

(c) By @fd1:ax-induction on \( r \). For \( r = 0 \), both sides are \( e \), since \( ee = e \) makes \( e \) its own inverse (@thm-group-basic-properties (2)). Suppose the statement holds for lists of length \( r \), and let \( (g_1, \dots, g_{r+1}) \) be a list. Then
\[
\begin{aligned}
(g_1 \cdots g_{r+1})^{-1} &= \bigl((g_1 \cdots g_r)\,g_{r+1}\bigr)^{-1} = g_{r+1}^{-1}\,(g_1 \cdots g_r)^{-1} \\
&= g_{r+1}^{-1}\,(g_r^{-1} \cdots g_1^{-1}) = g_{r+1}^{-1} g_r^{-1} \cdots g_1^{-1} ,
\end{aligned}
\]
by the recursion, @thm-group-basic-properties (3), the induction hypothesis, and (a) with the list \( (g_{r+1}^{-1}) \) of length \( 1 \), whose product is \( g_{r+1}^{-1} \). This proves the proposition.
:::
:::

By part (b), **from now on we drop brackets** from products in a group, regrouping in any way that keeps the order of the factors. The order itself may not change, unless the group is abelian (Exercise C3).

## Integer powers

The commonest list is a constant one. A product of \( n \) copies of \( g \) is the power \( g^n \), and the inverse of \( g^n \) deserves to be a power too.

::: {#def-group-integer-power}
[Integer Powers]

Let \( G \) be a group and \( g \in G \). For \( n \in \nN \), the **power** \( g^n \) is the product of the constant list \( (g, \dots, g) \) of length \( n \); so
\[
g^0 = e , \qquad g^{n+1} = g^n g \quad \text{for } n \in \nN .
\]
For \( n \in \nZ \) with \( n < 0 \), write \( n = -m \) with \( m \in \nN \) (@fd3:prp-naturals-embed-integers (c)), and set \( g^n \coloneqq (g^{-1})^m \). In additive notation the power is the **multiple** \( n \cdot g \): \( 0 \cdot g = 0 \), \( (n + 1) \cdot g = n \cdot g + g \), and \( (-m) \cdot g = m \cdot (-g) \).
:::

The two clauses do not overlap, since \( n < 0 \) and \( n \in \nN \) exclude each other (@fd3:thm-integers-ordered-ring (b)), and for \( n < 0 \) the \( m \) is \( -n \), so \( g^n \) is well defined. The new notation agrees with the old one: \( g^1 = eg = g \), and \( g^{-1} = (g^{-1})^1 \) is the inverse of \( g \). So \( g^2 = gg \) and \( g^{-2} = g^{-1}g^{-1} \).

The power laws look like school algebra, but the school proofs commute factors; here only (d) may, and it says so:

::: {#prp-group-power-laws}
[Power Laws in a Group]

Let \( G \) be a group, \( g, h \in G \) and \( m, n \in \nZ \).

::: {.enumerate options="label=(\alph*)"}
1. \( g^m g^n = g^{m+n} \).
2. \( (g^m)^{-1} = g^{-m} = (g^{-1})^m \).
3. \( (g^m)^n = g^{mn} \).
4. If \( gh = hg \), then \( (gh)^n = g^n h^n \).
5. Let \( R \) be a commutative ring. In the group \( (R, +) \), for \( a \in R \) and \( n \in \nN \), the multiple \( n \cdot a \) of @def-group-integer-power is the multiple \( n \cdot a \) of *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.3. In \( (\nZ, +) \), \( n \cdot a = na \), the product in the ring \( \nZ \), for all \( n, a \in \nZ \).
:::
:::

::: {.idea}
For exponents in \( \nN \), a power is a list product, and (a) is concatenation. Negative exponents are reduced to natural ones by one fact: \( g^m \) and \( (g^{-1})^m \) are inverse to each other, because the factors cancel in pairs from the middle out, \( g \cdots g\, g^{-1} \cdots g^{-1} = e \). With that, each sign case of (a) is a natural-number case for \( g \) or for \( g^{-1} \). Parts (c) and (d) are inductions on \( n \in \nN \), extended to \( n < 0 \) by (b).
:::

::: {.second-reading title="Proof of the power laws"}
::: {.proof of="prp-group-power-laws"}
*(a) for \( m, n \in \nN \).* The left side is the product of the constant list of length \( m \) times that of length \( n \). By @prp-group-list-product-laws (a) it is the product of the concatenated list, the constant list of length \( m + n \), which is \( g^{m+n} \).

*(b).* First let \( m \in \nN \). We show \( g^m (g^{-1})^m = e \) by @fd1:ax-induction on \( m \). For \( m = 0 \), \( ee = e \). For the step, \( g^{m+1} = g^1 g^m = g g^m \) by (a) on \( \nN \), and \( (g^{-1})^{m+1} = (g^{-1})^m g^{-1} \) by the definition, so, dropping brackets (@prp-group-list-product-laws (b)),
\[
g^{m+1} (g^{-1})^{m+1} = g \bigl(g^m (g^{-1})^m\bigr) g^{-1} = g e g^{-1} = e .
\]
So \( x = (g^{-1})^m \) solves \( g^m x = e \). By @thm-group-basic-properties (5) the only solution is \( (g^m)^{-1}e = (g^m)^{-1} \); hence \( (g^m)^{-1} = (g^{-1})^m \). This is also \( g^{-m} \): for \( m > 0 \) by the definition of negative powers, and for \( m = 0 \) because \( g^0 = e = (g^{-1})^0 \).

Now let \( m < 0 \), and write \( m = -k \) with \( k \in \nN \). By the definition, \( g^m = (g^{-1})^k \). The case just proved, applied to the element \( g^{-1} \) and the exponent \( k \), gives \( \bigl((g^{-1})^k\bigr)^{-1} = \bigl((g^{-1})^{-1}\bigr)^k = g^k \), by @thm-group-basic-properties (3). So \( (g^m)^{-1} = g^k = g^{-m} \). Finally \( (g^{-1})^m = \bigl((g^{-1})^{-1}\bigr)^k = g^k \) by the definition of negative powers, applied to the element \( g^{-1} \). This proves (b). In particular,
\[
(g^{-1})^p = g^{-p} \quad \text{for every } p \in \nZ . \tag{$\ast$}
\]

*(a) in general.* We first show, for \( m, k \in \nN \),
\[
g^m g^{-k} = g^{m-k} . \tag{$\ast\ast$}
\]
By (b), \( g^{-k} = (g^{-1})^k \), and \( g^k (g^{-1})^k = e \) (shown in (b)). If \( m \ge k \), then \( m - k \in \nN \) and \( g^m = g^{m-k} g^k \) by (a) on \( \nN \), so \( g^m (g^{-1})^k = g^{m-k} g^k (g^{-1})^k = g^{m-k} \). If \( m < k \), then \( k - m \in \nN \), and \( (g^{-1})^k = (g^{-1})^m (g^{-1})^{k-m} \) by (a) on \( \nN \) for the element \( g^{-1} \); since \( g^m (g^{-1})^m = e \), we get \( g^m (g^{-1})^k = (g^{-1})^{k-m} = g^{-(k-m)} = g^{m-k} \), by (\( \ast \)).

Now let \( m, n \in \nZ \), and write \( u \coloneqq g^{-1} \), so that \( g^p = u^{-p} \) for every \( p \in \nZ \) by (\( \ast \)) and \( (g^{-1})^{-1} = g \). There are four cases. If \( m, n \ge 0 \), this is (a) on \( \nN \). If \( m \ge 0 > n \), write \( n = -k \); this is (\( \ast\ast \)). If \( m < 0 \le n \), write \( m = -j \); then \( g^m g^n = u^j u^{-n} = u^{j-n} = g^{n-j} = g^{m+n} \), by (\( \ast\ast \)) for \( u \) and then (\( \ast \)). If \( m, n < 0 \), write \( m = -j \), \( n = -k \); then \( g^m g^n = u^j u^k = u^{j+k} = g^{-(j+k)} = g^{m+n} \), by (a) on \( \nN \) for \( u \) and (\( \ast \)). The identities between exponents used here, such as \( n - j = m + n \), are ring arithmetic in \( \nZ \) (@fd3:thm-integers-commutative-ring).

*(c).* For \( n \in \nN \), by @fd1:ax-induction on \( n \): \( (g^m)^0 = e = g^0 \), and \( (g^m)^{n+1} = (g^m)^n g^m = g^{mn} g^m = g^{mn + m} = g^{m(n+1)} \), by the definition, the hypothesis, (a), and (F9) in \( \nZ \). For \( n < 0 \), write \( n = -k \); then
\[
(g^m)^n = \bigl((g^m)^{-1}\bigr)^k = (g^{-m})^k = g^{(-m)k} = g^{m(-k)} = g^{mn} ,
\]
by the definition, (b), the case \( k \in \nN \) for the exponent \( -m \), and @fd3:prp-ring-algebra (c).

*(d).* Suppose \( gh = hg \). First, \( g h^n = h^n g \) for \( n \in \nN \), by @fd1:ax-induction: for \( n = 0 \) both sides are \( g \), and \( g h^{n+1} = (g h^n) h = h^n g h = h^n h g = h^{n+1} g \). Next, \( (gh)^n = g^n h^n \) for \( n \in \nN \), again by induction: for \( n = 0 \) both sides are \( e \), and
\[
(gh)^{n+1} = (gh)^n\, gh = g^n h^n g h = g^n g h^n h = g^{n+1} h^{n+1} ,
\]
using \( h^n g = g h^n \) and (a). For \( n < 0 \), write \( n = -k \). Taking inverses in \( gh = hg \) gives \( h^{-1} g^{-1} = g^{-1} h^{-1} \) (@thm-group-basic-properties (3)), so \( g^{-1} \) and \( h^{-1} \) commute too. Hence
\[
(gh)^n = \bigl((gh)^{-1}\bigr)^k = (h^{-1} g^{-1})^k = (g^{-1} h^{-1})^k = (g^{-1})^k (h^{-1})^k = g^n h^n ,
\]
by the definition, @thm-group-basic-properties (3), the commuting just shown, the case \( k \in \nN \) for the commuting pair \( g^{-1}, h^{-1} \), and the definition again.

*(e).* For \( n \in \nN \), both multiples are given by the same two clauses, \( 0 \cdot a = 0 \) and \( (n + 1) \cdot a = n \cdot a + a \), so they are the same function \( \nN \to R \) by the uniqueness in @fd2:thm-recursion. In \( \nZ \), *Number Systems: From \(\nN\) to \(\nR\)*, Section 2.3 shows \( n \cdot a = na \) for \( n \in \nN \) (the paragraph "Multiples", before @fd3:prp-ordered-ring-rules). For \( n = -m \) with \( m \in \nN \), \( (-m) \cdot a = m \cdot (-a) = m(-a) = (-m)a \), by @def-group-integer-power, the case \( n \in \nN \), and @fd3:prp-ring-algebra (c). This proves the proposition.
:::
:::

Part (d) needs \( gh = hg \): without it the law fails, and Section 2.4 exhibits a failure with two permutations of \( \{1, 2, 3\} \).

::: {.second-reading title="Multiples in Chapters 1 and 2 agree"}
::: {.remark}
For \( n = -m < 0 \), part (b) in additive notation reads \( m \cdot (-a) = -(m \cdot a) \), so the multiple \( (-m) \cdot a = m \cdot (-a) \) of @def-group-integer-power equals \( -(m \cdot a) \). That is how Section 1.5 defines \( n \cdot a \) for \( n < 0 \) in a commutative ring. So "\( n \cdot a \)" means the same thing in Chapters 1 and 2 for every \( n \in \nZ \), and the identities of @lem-integer-multiples apply to the multiples of the group \( (R, +) \). No proof in this chapter rests on this comparison; Exercise R1 of Section 2.5 needs only part (e).
:::
:::

## The units of a commutative ring form a group

*Number Systems: From \(\nN\) to \(\nR\)*, Section 3.5 found the units of a commutative ring \( R \), the elements \( u \) with \( uv = 1 \) for some \( v \in R \) (@fd3:def-ring-unit), and showed in the paragraph after the definition that \( 1 \) is a unit, that products and inverses of units are units, and that the inverse \( u^{-1} \) is unique. In the language of this section:

::: {#prp-units-form-group}
[The Units Form a Group]

Let \( R \) be a commutative ring. Then \( R^{\times} \), the set of units of \( R \), is an abelian group under the multiplication of \( R \), with identity \( 1 \), and the inverse of \( u \) in this group is \( u^{-1} \).
:::

::: {.proof}
By the paragraph after @fd3:def-ring-unit, a product of two units is a unit, so multiplication restricts to a binary operation on \( R^{\times} \). (G1) holds by (F5) of @fd3:def-commutative-ring-and-field. For (G2), \( 1 \) is a unit since \( 1 \cdot 1 = 1 \), and \( u \cdot 1 = 1 \cdot u = u \) by (F7) and (F6). For (G3), let \( u \in R^{\times} \). Then \( uu^{-1} = u^{-1}u = 1 \) by @fd3:def-ring-unit and (F6), and \( u^{-1} \) is itself a unit, by the same paragraph. The group is abelian by (F6). This proves the proposition.
:::

So the third situation at the start of the section was the group \( (\nZ/12\nZ)^{\times} \). More examples:

- \( \nZ^{\times} = \{1, -1\} \) (the examples after @fd3:def-ring-unit), a group with two elements.
- \( (\nZ/n\nZ)^{\times} = \{ [a] : \gcd(a, n) = 1 \} \) for \( n \in \nZ_{>0} \), by @fd3:thm-units-mod-n. For \( n = 8 \) it is \( \{[1], [3], [5], [7]\} \), and every element is its own inverse: \( [3][3] = [9] = [1] \), \( [5][5] = [25] = [1] \), \( [7][7] = [49] = [1] \).
- \( F^{\times} = F \setminus \{0\} \) for a field \( F \): every non-zero element is a unit by (F8), and \( 0 \) is not, since \( 0 \cdot v = 0 \ne 1 \) (@fd3:prp-ring-algebra (b)). So the group of @exm-groups (b) is \( F^{\times} \).

::: {.check}
In \( (\nZ/7\nZ)^{\times} \), find \( [3]^{-1} \) and \( [3]^{-2} \).
:::

::: {.solution}
\( [3]^{-1} = [5] \), since \( 3 \cdot 5 = 15 = 2 \cdot 7 + 1 \), so \( [3][5] = [1] \). By @def-group-integer-power, \( [3]^{-2} = ([3]^{-1})^2 = [5][5] = [25] = [4] \), since \( 25 = 3 \cdot 7 + 4 \). Check: \( [3]^2 [4] = [9][4] = [36] = [1] \), as \( 36 = 5 \cdot 7 + 1 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-groups-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State the axioms (G1)–(G3), and say where in the definition of a group closure is required.
2. Is \( \nZ \) with \( a \ast b \coloneqq a + b + 1 \) a group? Justify your answer.
3. True or false: in every group, \( (ab)^{-1} = a^{-1}b^{-1} \). Justify your answer.
4. Compute \( 3 \cdot [5] \) and \( (-2) \cdot [5] \) in the group \( (\nZ/7\nZ, +) \).
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. (G1) \( (ab)c = a(bc) \) for all \( a, b, c \in G \); (G2) there is \( e \in G \) with \( ea = ae = a \) for every \( a \in G \); (G3) for every \( a \in G \) there is \( b \in G \) with \( ab = ba = e \). Closure is not an axiom of its own: it is required by "binary operation", a function \( G \times G \to G \), whose values lie in \( G \).
2. Yes. The rule is a function \( \nZ \times \nZ \to \nZ \). (G1): both \( (a \ast b) \ast c = (a + b + 1) + c + 1 \) and \( a \ast (b \ast c) = a + (b + c + 1) + 1 \) equal \( a + b + c + 2 \), by (F1) and (F2). (G2): \( e = -1 \) works, since \( a \ast (-1) = a + (-1) + 1 = a \) and \( (-1) \ast a = a \) likewise. (G3): the inverse of \( a \) is \( -a - 2 \), since \( a \ast (-a - 2) = a - a - 2 + 1 = -1 \), and the other order gives the same by (F1). It is abelian, since \( a + b + 1 = b + a + 1 \).
3. False. Let \( f \) and \( g \) be the bijections of \( \{1, 2, 3\} \) with \( f \) swapping \( 1, 2 \) and \( g \) swapping \( 2, 3 \), each fixing the third point; each is its own inverse. Then \( f \circ g \) sends \( 1 \mapsto 2 \), \( 2 \mapsto 3 \), \( 3 \mapsto 1 \) (for instance \( (f \circ g)(2) = f(3) = 3 \)), so its inverse sends \( 1 \mapsto 3 \). But \( f^{-1} \circ g^{-1} = f \circ g \) sends \( 1 \mapsto 2 \). So \( (f \circ g)^{-1} \ne f^{-1} \circ g^{-1} \). The correct rule is \( (ab)^{-1} = b^{-1}a^{-1} \) (@thm-group-basic-properties (3)); in an abelian group \( b^{-1}a^{-1} = a^{-1}b^{-1} \), so there the statement is true.
4. By @def-group-integer-power, \( 3 \cdot [5] = [5] + [5] + [5] = [15] = [1] \), since \( 15 = 2 \cdot 7 + 1 \). Next \( -[5] = [-5] = [2] \), so \( (-2) \cdot [5] = 2 \cdot [2] = [4] \).
:::
:::

### B. Practice

::: {#exr-groups-b1}
[B1: Groups or not]

Determine which of the following are groups. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \nQ_{>0} \) under multiplication.
2. \( \{1, -1\} \subseteq \nZ \) under multiplication.
3. The odd integers under addition.
4. \( \{[1], [3], [5], [7]\} \subseteq \nZ/8\nZ \) under multiplication.
5. \( \nZ/6\nZ \setminus \{[0]\} \) under multiplication.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. A group. \( \nQ \) is an ordered field (@fd3:thm-rationals-ordered-field), so a product of positive rationals is positive by (O4), and multiplication is a binary operation on \( \nQ_{>0} \). Associativity is (F5), and \( 1 > 0 \) (@fd3:prp-ordered-ring-rules (e)) is an identity. For \( x > 0 \), \( x^{-1} \) exists since \( x \ne 0 \), and \( x^{-1} > 0 \) by @fd3:prp-reciprocal-order (a). So the inverse stays in \( \nQ_{>0} \).
2. A group: it is \( \nZ^{\times} \), a group by @prp-units-form-group.
3. Not a group: addition is not a binary operation on the odd integers, since \( 1 + 1 = 2 \) is even and so not odd (@fd3:cor-integers-even-odd (a)).
4. A group: it is \( (\nZ/8\nZ)^{\times} \) (the examples after @prp-units-form-group), and every element is its own inverse.
5. Not a group: \( [2][3] = [0] \), so multiplication is not a binary operation on the set (@exm-group-nonexamples).
:::
:::

::: {#exr-groups-b2}
[B2: An element equal to its square]

Let \( G \) be a group and \( g \in G \) with \( gg = g \). Prove that \( g = e \).

The first step is given: by (G2), \( gg = g = ge \).

The last step is blank. *Name the move, then complete it.*
:::

::: {.solution}
The move is **multiply by the inverse**: \( g \) appears on the left of both sides, so multiply both sides on the left by \( g^{-1} \) and regroup.

Completion: from \( gg = ge \), cancellation (@thm-group-basic-properties (4)) gives \( g = e \). Written out, \( g = (g^{-1}g)g = g^{-1}(gg) = g^{-1}(ge) = (g^{-1}g)e = e \).
:::

::: {#exr-groups-b3}
[B3: Powers of a conjugate]

Let \( G \) be a group and \( g, h \in G \). Prove that \( (ghg^{-1})^n = gh^ng^{-1} \) for every \( n \in \nZ \).
:::

::: {.solution}
*For \( n \in \nN \),* by @fd1:ax-induction on \( n \). For \( n = 0 \), both sides are \( e \), since \( geg^{-1} = gg^{-1} = e \). Suppose \( (ghg^{-1})^n = gh^ng^{-1} \). Then, dropping brackets (@prp-group-list-product-laws (b)),
\[
(ghg^{-1})^{n+1} = (ghg^{-1})^n\, ghg^{-1} = gh^n g^{-1} g h g^{-1} = gh^n h g^{-1} = g h^{n+1} g^{-1} ,
\]
by @def-group-integer-power, the hypothesis, \( g^{-1}g = e \), and @def-group-integer-power again.

*For \( n < 0 \),* write \( n = -k \) with \( k \in \nN \). By @prp-group-power-laws (b), the case just proved, and @prp-group-list-product-laws (c),
\[
(ghg^{-1})^{n} = \bigl((ghg^{-1})^k\bigr)^{-1} = (gh^kg^{-1})^{-1} = (g^{-1})^{-1}(h^k)^{-1}g^{-1} = g h^{-k} g^{-1} ,
\]
where the last step uses @thm-group-basic-properties (3) and @prp-group-power-laws (b). This proves the identity for every \( n \in \nZ \).
:::

### C. Going deeper

::: {#exr-groups-c1}
[C1: Exit check: the basic laws of a group]

Prove parts (1)–(3) of @thm-group-basic-properties from (G1)–(G3) only: the identity is unique; the inverse of each element is unique; and \( (a^{-1})^{-1} = a \), \( (ab)^{-1} = b^{-1}a^{-1} \).
:::

::: {.solution}
[Hint 1]

For uniqueness, take two candidates and compute one expression in two ways.
:::

::: {.solution}
[Hint 2]

For inverses, let \( b \) and \( b' \) both be inverses of \( a \), and start from \( b = be \).
:::

::: {.solution}
The proof of (1)–(3) in @thm-group-basic-properties is a complete answer. In outline: two identities \( e, e' \) give \( e = ee' = e' \); two inverses \( b, b' \) of \( a \) give \( b = be = b(ab') = (ba)b' = eb' = b' \); \( a \) is an inverse of \( a^{-1} \), so \( (a^{-1})^{-1} = a \) by uniqueness; and \( (ab)(b^{-1}a^{-1}) = \bigl((ab)b^{-1}\bigr)a^{-1} = \bigl(a(bb^{-1})\bigr)a^{-1} = e \) and \( (b^{-1}a^{-1})(ab) = \bigl((b^{-1}a^{-1})a\bigr)b = \bigl(b^{-1}(a^{-1}a)\bigr)b = e \), so \( (ab)^{-1} = b^{-1}a^{-1} \) by uniqueness.

**Marking scheme.** (10 points)
- 2: uniqueness of the identity, with each of the two identity properties named where it is used.
- 3: uniqueness of inverses, by inserting \( e = ab' \) (or an equivalent use of (G2) and (G3)) and regrouping, with each step named.
- 1: \( (a^{-1})^{-1} = a \), by reading \( aa^{-1} = a^{-1}a = e \) as "\( a \) is an inverse of \( a^{-1} \)" and citing uniqueness.
- 3: \( (ab)(b^{-1}a^{-1}) = e \), with (G1) named, **and** \( (b^{-1}a^{-1})(ab) = e \).
- 1: the conclusion \( (ab)^{-1} = b^{-1}a^{-1} \), citing uniqueness of inverses.
Fatal errors (0 for the step): using commutativity; "dividing" by an element. Checking only one product earns 1 of those 3 points (not fatal), or all 4 points for \( (ab)^{-1} \) with a proof from (G1)–(G3) that a one-sided inverse is the inverse (\( xy = e \) or \( yx = e \) implies \( y = x^{-1} \)). A proof of uniqueness of inverses through cancellation earns the 3 points only if cancellation is itself proved from (G1)–(G3).
:::

::: {#exr-groups-c2}
[C2: Find the error]

Here is a statement and an argument for it.

> **Claim.** In every group, \( (ab)^{-1} = b^{-1}a^{-1} \).
>
> **Argument.** (1) By (G1)–(G3), \( (b^{-1}a^{-1})(ab) = b^{-1}(a^{-1}a)b = b^{-1}eb = b^{-1}b = e \). (2) Since \( xy = yx \) for all \( x, y \) in a group, also \( (ab)(b^{-1}a^{-1}) = (b^{-1}a^{-1})(ab) = e \). (3) So \( b^{-1}a^{-1} \) is a two-sided inverse of \( ab \), and \( (ab)^{-1} = b^{-1}a^{-1} \) by uniqueness of inverses.

Is the claim true? Does the argument prove it? If not, name the line that fails, explain why, and give a counterexample to the step.
:::

::: {.solution}
The claim is **true**: it is @thm-group-basic-properties (3). The argument does **not** prove it.

Lines (1) and (3) are correct. The failing line is (2), and only (2). It rests on the general "fact" that any two elements of a group commute. That is not an axiom, it has not been proved, and it is false, so the line cites nothing: entry (N9) of @fd1:exm-not-allowed-catalogue. A counterexample to the step: the bijections \( f \), \( g \) of \( \{1, 2, 3\} \) in A1 (c), with \( (f \circ g)(1) = 2 \) and \( (g \circ f)(1) = g(2) = 3 \), so \( f \circ g \ne g \circ f \). There is no counterexample to the conclusion, which is true.

The repair is to compute the second product as the first one was computed, with (G1): \( (ab)(b^{-1}a^{-1}) = a(bb^{-1})a^{-1} = aea^{-1} = aa^{-1} = e \). Alternatively, line (1) alone suffices: it says that \( b^{-1}a^{-1} \) solves \( y(ab) = e \), whose only solution is \( e(ab)^{-1} = (ab)^{-1} \) by @thm-group-basic-properties (5).
:::

::: {#exr-groups-c3}
[C3: Rearranging in an abelian group]

Let \( G \) be an abelian group and \( (g_1, \dots, g_r) \) a list in \( G \) with \( r \ge 2 \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that swapping two adjacent entries \( g_i, g_{i+1} \) (\( 1 \le i < r \)) does not change the product of the list.
2. Deduce that the product does not change under any rearrangement obtained by finitely many such adjacent swaps.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. By @prp-group-list-product-laws (a) and (b), the product of the list is the bracketing
\[
(g_1 \cdots g_{i-1})(g_i g_{i+1})(g_{i+2} \cdots g_r) ,
\]
where an empty product is \( e \). The list with \( g_i \) and \( g_{i+1} \) swapped has, in the same way, the product \( (g_1 \cdots g_{i-1})(g_{i+1} g_i)(g_{i+2} \cdots g_r) \). Since \( G \) is abelian, \( g_i g_{i+1} = g_{i+1} g_i \), so the two products are equal.
2. By @fd1:ax-induction on the number \( k \) of swaps: for \( k = 0 \) the list is unchanged, and a rearrangement by \( k + 1 \) swaps is one swap applied to a rearrangement by \( k \) swaps, whose product equals the original product by the hypothesis; the last swap does not change the product, by (a).
:::

Section 2.5 proves that every permutation of \( \{1, \dots, r\} \) is a product of adjacent transpositions; read for lists, every rearrangement is obtained by adjacent swaps, and so the product of a list in an abelian group does not depend on the order of the factors.

**Marking scheme.** (10 points)
- 3: (a) brackets both products as \( (g_1 \cdots g_{i-1})(\,\cdot\,)(g_{i+2} \cdots g_r) \), citing @prp-group-list-product-laws, with the empty product read as \( e \) when \( i = 1 \) or \( i + 1 = r \).
- 2: (a) uses \( g_i g_{i+1} = g_{i+1} g_i \) (abelian) to conclude that the products agree.
- 1: (b) names the induction and its variable, the number of swaps.
- 2: (b) base case: zero swaps leave the list unchanged.
- 2: (b) step: writes a rearrangement by \( k + 1 \) swaps as one swap after \( k \) swaps and applies (a) to the intermediate list.
Fatal errors (0 for the step): (a) swaps the two entries inside a product written without brackets, with no appeal to the list-product laws; (b) "and so on" in place of an induction.
:::

<!-- dependency ledger
def-group (claim): (hook) the units of Z/12Z are [1], [5], [7], [11]; 25 = 2*12 + 1, 49 = 4*12 + 1, 121 = 10*12 + 1 | fd3:thm-units-mod-n (cited); gcd(a, 12) = 1 exactly for a in {1, 5, 7, 11} among 0..11 computed; verify/ch02/exm-groups.py
def-group (claim): (opening) N is omega, Z and Q are fd3's; induction, strong induction and recursion read on omega | fd3:cor-omega-identification (b) (cited); strong induction: its fd1 proof uses only fd1:ax-induction and fd3:thm-omega-order (a), (b), (d) (cited)
exm-groups (solution): (a) 0 + a = a and (-a) + a = 0 from (F3), (F4) with (F1) | fd3:def-commutative-ring-and-field, named in the solution
exm-groups (solution): (b) a product of non-zero elements is non-zero; 1 != 0 in a field; a^{-1} != 0 via a . 0 = 0 | (F8) makes x a unit (fd3:def-ring-unit), and a unit is not a zero divisor (the paragraph after fd3:def-ring-unit, cited); the field clause 1 != 0 of fd3:def-commutative-ring-and-field; fd3:prp-ring-algebra (b) for a . 0 = 0 (cited)
exm-groups (solution): (c) a swap of two points is its own inverse, hence a bijection; at most two bijections of a set with at most two elements | direct from the definitions (fd2:def-composition, fd2:thm-bijection-iff-inverse); the count of bijections of a set with at most two elements is by listing, used silently
exm-groups (solution): (e) rotations of a square, and Section 2.4 B3 matching them with Z/4Z | F5.3 §04 (prose pointer within the chapter, blueprint 04 B3); nothing here depends on it
exm-groups (claim): (remark) GL_n(F) is a group | Spaces and Maps, the chapter "Matrices" (LA1.0, prose pointer); nothing here depends on it
exm-group-nonexamples (solution): 2 != 1 and 2 != -1 | order of Z (fd3:thm-integers-ordered-ring), used silently
exm-group-nonexamples (solution): -1 < 0 | fd3:prp-ordered-ring-rules (a), (e) with 1 != 0 (fd3:thm-integers-commutative-ring), used silently
exm-group-nonexamples (solution): (N, +) associative with identity 0 | (F1)-(F3) in Z (fd3:thm-integers-commutative-ring)
exm-group-nonexamples (solution): (1 - 1) - 1 = -1, 1 - (1 - 1) = 1 | ring arithmetic in Z; verify/ch02/exm-group-nonexamples.py
thm-group-basic-properties (claim): (remark) (2) is the argument of fd2:prp-inverse-unique and of the uniqueness paragraph after fd3:def-ring-unit; (1) that of fd3:prp-ring-algebra (a) | meta-claim, checked against F2.1 §05, F3.5 §05, F3.2 §03
def-group-list-product (claim): recursion on N for a list extended by e; independence of the extension; the remark never reorders factors | fd2:def-sum-product and its "Finite lists" remark used as a template (F3.1 §07 citing rule, group (iii)), fd2:thm-recursion read on omega; checked: the remark's induction only compares the added terms a_{n+1}
prp-group-list-product-laws (proof): (b) concatenating (g_1..g_k) with the re-indexed rest (g_{k+1}..g_r) gives (g_1..g_r) | definition of the concatenated list (entry r + i is h_i), inline
prp-group-list-product-laws (proof): strong induction with the property "r >= 1 implies ..." | fd1:thm-strong-induction read on omega (opening line above)
prp-group-power-laws (proof): exponent arithmetic in Z (m - k + k = m, n - j = m + n, (-m)k = m(-k), mn + m = m(n + 1)); m - k in N for m >= k, k - m in N for m < k | fd3:thm-integers-commutative-ring and fd3:prp-ring-algebra (cited); fd3:thm-integers-ordered-ring (b) for membership in N, used silently
prp-group-power-laws (proof): (e) n . a = na in Z for n in N | F3.2 §03 paragraph "Multiples" (cited by position, as the blueprint allows)
prp-group-power-laws (claim): (sentence after) Section 2.4 exhibits (st)^2 != s^2 t^2 | F5.3 §04 warning (prose pointer within the chapter); nothing here depends on it
prp-group-power-laws (claim): (remark) F5.2 Section 1.5 defines n . a := -((-n) . a) for n < 0; lem-integer-multiples applies | F5.2 blueprint, its section 5 (lem-integer-multiples (d)); comparison only, no proof rests on it
prp-units-form-group (claim): Z^x = {1, -1}; [3]^2 = [5]^2 = [7]^2 = [1] in Z/8Z; F^x = F \ {0} | fd3:def-ring-unit examples (cited), fd3:thm-units-mod-n (cited); verify/ch02/prp-units-form-group.py; (F8) and fd3:prp-ring-algebra (b) (cited)
prp-units-form-group (claim): (check) 15 = 2*7 + 1, 25 = 3*7 + 4, 36 = 5*7 + 1 | numerals; verify/ch02/prp-units-form-group.py
exr-groups-a1 (solution): (b) identity -1, inverse -a - 2, both bracketings a + b + c + 2; (c) values of f o g; (d) 15 = 2*7 + 1, -5 = 2 mod 7 | ring arithmetic; verify/ch02/exr-groups-a1.py
exr-groups-b1 (solution): (a) x > 0 gives x^{-1} > 0 | fd3:prp-reciprocal-order (a) (cited)
exr-groups-b1 (solution): (c) 2 = 2*1 is even, hence not odd | fd3:cor-integers-even-odd (a) (cited)
exr-groups-c3 (solution): every rearrangement is a product of adjacent swaps (Section 2.5) | F5.3 §05 cor-adjacent-transpositions-generate (prose pointer in a solution); nothing in (a), (b) depends on it
-->
