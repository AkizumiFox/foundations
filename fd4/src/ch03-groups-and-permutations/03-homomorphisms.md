# Homomorphisms and Isomorphisms

Section 3.1 named the pattern shared by \( (\nZ, +) \), the units of a ring and the bijections of a set, and Section 3.2 looked inside one group at a time, at its subgroups. This section compares two groups. A map between groups that respects the two operations is a homomorphism; a bijective one is an isomorphism, and it says that two groups differ only in the names of their elements. The elements a homomorphism sends to the identity form its kernel, a subgroup that measures how much the map forgets.

## Maps that respect the operation

Write out the addition table of \( \nZ/2\nZ \) (@fd3:def-integers-mod-n-ring) and the multiplication table of \( \{1, -1\} \subseteq \nZ \), the group \( \nZ^{\times} \) of @prp-units-form-group:

| \( + \) | \( [0] \) | \( [1] \) |
|---|---|---|
| \( [0] \) | \( [0] \) | \( [1] \) |
| \( [1] \) | \( [1] \) | \( [0] \) |

| \( \cdot \) | \( 1 \) | \( -1 \) |
|---|---|---|
| \( 1 \) | \( 1 \) | \( -1 \) |
| \( -1 \) | \( -1 \) | \( 1 \) |

Rename \( [0] \) as \( 1 \) and \( [1] \) as \( -1 \), and the first table becomes the second, entry for entry. The two groups are the same table with different names. The renaming is a function \( \varphi \) with \( \varphi([0]) = 1 \) and \( \varphi([1]) = -1 \), and "entry for entry" says that the entry for \( a, b \) is sent to the entry for \( \varphi(a), \varphi(b) \): \( \varphi(a + b) = \varphi(a)\varphi(b) \). Maps with this property are worth having even when they are not bijections. The map \( \nZ \to \nZ/2\nZ \), \( a \mapsto [a] \), keeps only the parity of an integer, and it still turns sums into sums.

*A homomorphism is a map between groups that sends products to products; an isomorphism is a bijective one, a renaming of the elements.*

::: {#def-group-homomorphism}
[Group Homomorphism]

Let \( G \) and \( H \) be groups. A function \( \varphi \colon G \to H \) is a **homomorphism** if \( \varphi(ab) = \varphi(a)\varphi(b) \) **for all** \( a, b \in G \). A **bijective** homomorphism is an **isomorphism**. The groups \( G \) and \( H \) are **isomorphic**, written \( G \cong H \), if **there exists** an isomorphism \( G \to H \). The **kernel** of \( \varphi \) is
\[
\ker \varphi \coloneqq \{ g \in G : \varphi(g) = e_H \} ,
\]
where \( e_H \) is the identity of \( H \).
:::

In words: the product \( ab \) on the left is taken in \( G \), and the product \( \varphi(a)\varphi(b) \) on the right is taken in \( H \). So "\( \varphi \) respects the operation" compares two different operations, and either group may be written additively. For \( \varphi \colon (\nZ/2\nZ, +) \to (\{1, -1\}, \cdot) \) above, the condition reads \( \varphi(a + b) = \varphi(a)\varphi(b) \). The kernel is a subset of the **source** \( G \); the identity it is measured against is that of the **target** \( H \). We write \( e_G \) and \( e_H \) whenever both groups are in play.

The definition asks for one equation and nothing else. It does not ask that \( \varphi(e_G) = e_H \) or that \( \varphi \) respect inverses: both follow, by @thm-homomorphism-basic-properties below. This differs from the field homomorphisms of Chapter 2, which must send \( 1 \) to \( 1 \) by a clause of their own: the map sending every element of a field to \( 0 \) respects \( + \) and \( \cdot \), yet \( 1 \mapsto 0 \). In a group, every element can be canceled, and that is what makes the clause redundant.

Two homomorphisms exist between any two groups, or from any group to itself:

- the **trivial homomorphism** \( G \to H \), \( g \mapsto e_H \): since \( e_H e_H = e_H \) by (G2), \( \varphi(ab) = e_H = \varphi(a)\varphi(b) \). Its kernel is all of \( G \). It forgets everything.
- the **identity** \( \id_G \colon G \to G \): \( \id_G(ab) = ab = \id_G(a)\id_G(b) \). It is bijective (@fd2:thm-bijection-iff-inverse, with inverse \( \id_G \)), so it is an isomorphism, and its kernel is \( \{e_G\} \). It forgets nothing.

These two extremes are why we say that the kernel measures what \( \varphi \) forgets: the larger \( \ker \varphi \), the more elements \( \varphi \) sends to the same place. @prp-homomorphism-injective-iff-kernel-trivial below makes the slogan exact at the end where nothing is forgotten.

**The product of two groups.** Several examples below have a pair of groups as their target. For groups \( G \) and \( H \), take the set \( G \times H \) of pairs (@fd2:def-cartesian-product) with the operation in each coordinate:
\[
(g, h)(g', h') \coloneqq (gg', hh') .
\]
This is a binary operation on \( G \times H \), since \( gg' \in G \) and \( hh' \in H \). It makes \( G \times H \) a group, the **product** of \( G \) and \( H \):

- (G1) For \( (g, h), (g', h'), (g'', h'') \in G \times H \), both bracketings give \( (gg'g'', hh'h'') \), because (G1) holds in \( G \) in the first coordinate and in \( H \) in the second.
- (G2) \( (e_G, e_H)(g, h) = (e_G g, e_H h) = (g, h) \), and \( (g, h)(e_G, e_H) = (g, h) \) in the same way.
- (G3) \( (g, h)(g^{-1}, h^{-1}) = (gg^{-1}, hh^{-1}) = (e_G, e_H) \), and \( (g^{-1}, h^{-1})(g, h) = (e_G, e_H) \) in the same way.

If \( G \) and \( H \) are abelian, so is \( G \times H \), coordinate by coordinate. For abelian groups written additively, the product is written additively too, \( (g, h) + (g', h') = (g + g', h + h') \); this is the componentwise sum on \( \nZ/m\nZ \times \nZ/n\nZ \) of @fd3:thm-chinese-remainder-two (b).

::: {#exm-group-homomorphisms}
[Homomorphisms]

Check that each map is a homomorphism, and find its kernel.

::: {.enumerate options="label=(\alph*)"}
1. For \( n \in \nZ_{>0} \), the map \( (\nZ, +) \to (\nZ/n\nZ, +) \), \( a \mapsto [a] \).
2. For a group \( G \) and \( g \in G \), the map \( (\nZ, +) \to G \), \( k \mapsto g^k \). Find its image as well.
3. For a group \( G \) and \( g \in G \), **conjugation by \( g \)**, \( c_g \colon G \to G \), \( c_g(x) \coloneqq gxg^{-1} \). Show that it is an isomorphism, and that it is the identity map exactly when \( g \) commutes with every element of \( G \).
4. For an **abelian** group \( G \), the map \( G \to G \), \( x \mapsto x^2 \).
5. For \( m, n \in \nZ_{>0} \) with \( \gcd(m, n) = 1 \), the map \( \nZ/mn\nZ \to \nZ/m\nZ \times \nZ/n\nZ \), \( [x]_{mn} \mapsto ([x]_m, [x]_n) \), of additive groups. Show that it is an isomorphism.
6. The modulus \( (\nC \setminus \{0\}, \cdot) \to (\nR_{>0}, \cdot) \), \( z \mapsto \abs{z} \), where \( \nR_{>0} \coloneqq \{ x \in \nR : x > 0 \} \).
:::

Then show that \( x \mapsto x + 1 \) is **not** a homomorphism \( (\nZ, +) \to (\nZ, +) \).
:::

::: {.solution}
(a) \( (\nZ/n\nZ, +) \) is a group by @exm-groups (a). By @fd3:thm-quotient-ring-by-ideal (c), applied to the ideal \( n\nZ \) of \( \nZ \) (@fd3:def-integers-mod-n-ring), \( [a + b] = [a] + [b] \): a homomorphism. By @fd3:thm-quotient-ring-by-ideal (d), \( [a] = [0] \) exactly when \( a \in n\nZ \), so the kernel is \( n\nZ \). Every element of \( \nZ/n\nZ \) is a class \( [a] \), so the map is surjective.

(b) By @prp-group-power-laws (a), \( g^{k + l} = g^k g^l \) for all \( k, l \in \nZ \), which is the homomorphism property with \( + \) in the source and the product of \( G \) in the target. The kernel is \( \{ k \in \nZ : g^k = e_G \} \). The image is \( \{ g^k : k \in \nZ \} = \langle g \rangle \), by @def-subgroup-generated-by-element. For instance, for the group \( G = (\nZ/7\nZ)^{\times} \) (@prp-units-form-group) and \( g = [3] \), the image is all of \( (\nZ/7\nZ)^{\times} \): the powers \( [3]^0, \dots, [3]^5 \) are \( [1], [3], [2], [6], [4], [5] \), and \( [3]^6 = [1] \), so \( 6 \) lies in the kernel.

(c) For \( x, y \in G \), inserting \( e = g^{-1}g \) between \( x \) and \( y \) and dropping brackets (@prp-group-list-product-laws (b)),
\[
c_g(x)c_g(y) = gxg^{-1}gyg^{-1} = gxeyg^{-1} = gxyg^{-1} = c_g(xy) .
\]
So \( c_g \) is a homomorphism. Next, since \( (g^{-1})^{-1} = g \) (@thm-group-basic-properties (3)),
\[
c_{g^{-1}}(c_g(x)) = g^{-1}gxg^{-1}g = x ,
\]
and in the same way \( c_g(c_{g^{-1}}(x)) = gg^{-1}xgg^{-1} = x \). So \( c_{g^{-1}} \) is a two-sided inverse of \( c_g \) (@fd2:def-inverse-function), and \( c_g \) is bijective (@fd2:thm-bijection-iff-inverse): an isomorphism. Finally, \( c_g = \id_G \) means \( gxg^{-1} = x \) for every \( x \) (@fd2:prp-function-equality). Multiplying on the right by \( g \) turns \( gxg^{-1} = x \) into \( gx = xg \), and multiplying \( gx = xg \) on the right by \( g^{-1} \) turns it back. So \( c_g = \id_G \) exactly when \( gx = xg \) for every \( x \in G \). In an abelian group every conjugation is the identity. The kernel of \( c_g \) is \( \{e\} \): if \( gxg^{-1} = e \), then \( x = c_{g^{-1}}(e) = g^{-1}eg = e \).

(d) Since \( G \) is abelian, \( xy = yx \), and @prp-group-power-laws (d) gives \( (xy)^2 = x^2y^2 \). The kernel is \( \{ x \in G : x^2 = e \} \). In \( (\nZ/7\nZ)^{\times} \) the squares of \( [1], \dots, [6] \) are \( [1], [4], [2], [2], [4], [1] \), so the kernel is \( \{[1], [6]\} \). In \( (\nZ/8\nZ)^{\times} = \{[1], [3], [5], [7]\} \) the squares are \( [1], [9], [25], [49] \), all equal to \( [1] \), so the kernel is the whole group.

(e) The target is the product of the groups \( (\nZ/m\nZ, +) \) and \( (\nZ/n\nZ, +) \), written additively. The rule is the map \( \Phi \) of @fd3:thm-chinese-remainder-two (b), a well-defined bijection, and it satisfies \( \Phi([x]_{mn} + [y]_{mn}) = \Phi([x]_{mn}) + \Phi([y]_{mn}) \) with the componentwise sum, which is the product operation above. So it is an isomorphism of additive groups, and its kernel is \( \{[0]_{mn}\} \). For example, \( \nZ/12\nZ \cong \nZ/3\nZ \times \nZ/4\nZ \), since \( 1 = 4 - 3 \) shows \( \gcd(3, 4) = 1 \) (@fd3:cor-coprime-iff-combination).

(f) \( \nC \) is a field (@thm-complex-numbers-field), so \( (\nC \setminus \{0\}, \cdot) \) is a group by @exm-groups (b). \( (\nR_{>0}, \cdot) \) is a group by the rules of the ordered field \( \nR \) (@fd3:thm-reals-ordered-field): a product of positive reals is positive by (O4), associativity and the identity law are (F5)–(F7), and \( 1 > 0 \) (@fd3:prp-ordered-ring-rules (e)). For \( x > 0 \) we have \( x \ne 0 \) by (O1), so \( x^{-1} \) exists by (F8), and it is positive by @fd3:prp-reciprocal-order (a). For \( z \ne 0 \), \( \abs{z} \ge 0 \) by its definition as a non-negative square root (@def-conjugate-modulus) and \( \abs{z} \ne 0 \) by @thm-conjugate-properties (e), so \( \abs{z} \in \nR_{>0} \). The homomorphism property is \( \abs{zw} = \abs{z}\abs{w} \), @thm-conjugate-properties (d). The kernel is \( \{ z \in \nC : \abs{z} = 1 \} = \nT \), the unit circle of @prp-unit-circle.

*The non-example.* Let \( \varphi(x) \coloneqq x + 1 \). Then \( \varphi(0 + 0) = 1 \), while \( \varphi(0) + \varphi(0) = 2 \). So \( \varphi(0 + 0) \ne \varphi(0) + \varphi(0) \), and \( \varphi \) is not a homomorphism. It is a minimal change of the identity map \( x \mapsto x \), which is one: the shift keeps the map bijective and destroys only the equation.
:::

Part (b) says that every element \( g \) of every group is the image of \( 1 \) under a homomorphism out of \( \nZ \). Part (c) gives the first isomorphisms of a group with itself that can differ from the identity: \( c_g \ne \id_G \) exactly when \( g \) fails to commute with some element of \( G \), as for the two swaps of the fold after @exm-groups (c), there called \( f, g \): writing \( h \) for the second, \( c_f(h) = f \circ h \circ f^{-1} \ne h \) because \( f \circ h \ne h \circ f \). Part (f) shows a kernel that is not a set of integers.

## Basic properties of homomorphisms

The definition asks only for products. Identities, inverses and powers come with them, and kernels and images are subgroups.

::: {#thm-homomorphism-basic-properties}
[Basic Properties of Homomorphisms]

Let \( \varphi \colon G \to H \) be a homomorphism of groups, and let \( a \in G \).

::: {.enumerate options="label=(\alph*)"}
1. \( \varphi(e_G) = e_H \).
2. \( \varphi(a^{-1}) = \varphi(a)^{-1} \).
3. \( \ker \varphi \) is a subgroup of \( G \).
4. \( \varphi(a^n) = \varphi(a)^n \) for every \( n \in \nZ \).
5. The image \( \varphi(G) \) is a subgroup of \( H \).
:::
:::

::: {.idea}
For (a), apply \( \varphi \) to \( e_G e_G = e_G \): the equation \( \varphi(e_G)\varphi(e_G) = \varphi(e_G) \) has the shape \( gg = g \), and **multiply by the inverse** of \( \varphi(e_G) \) leaves \( \varphi(e_G) = e_H \). For (b), \( \varphi(a^{-1}) \) undoes \( \varphi(a) \), and inverses are unique. Then (c) and (e) are the subgroup test, and (d) is induction along the definition of powers.
:::

::: {.proof}
(a) Since \( e_G e_G = e_G \) by (G2) in \( G \), and \( \varphi(e_G) = \varphi(e_G) e_H \) by (G2) in \( H \),
\[
\varphi(e_G)\varphi(e_G) = \varphi(e_G e_G) = \varphi(e_G) = \varphi(e_G)e_H .
\]
Canceling \( \varphi(e_G) \) on the left (@thm-group-basic-properties (4)) gives \( \varphi(e_G) = e_H \).

(b) By the homomorphism property, (G3) in \( G \) and (a),
\[
\varphi(a)\varphi(a^{-1}) = \varphi(aa^{-1}) = \varphi(e_G) = e_H ,
\]
and in the same way \( \varphi(a^{-1})\varphi(a) = \varphi(a^{-1}a) = e_H \). So \( \varphi(a^{-1}) \) is an inverse of \( \varphi(a) \), and since inverses are unique (@thm-group-basic-properties (2)), \( \varphi(a^{-1}) = \varphi(a)^{-1} \).

(c) By (a), \( e_G \in \ker \varphi \), so \( \ker \varphi \ne \emptyset \). Let \( x, y \in \ker \varphi \). By the homomorphism property and (b),
\[
\varphi(xy^{-1}) = \varphi(x)\varphi(y)^{-1} = e_H e_H^{-1} = e_H ,
\]
where \( e_H^{-1} = e_H \) because \( e_H e_H = e_H \) and inverses are unique. So \( xy^{-1} \in \ker \varphi \), and \( \ker \varphi \) is a subgroup by the subgroup test (@thm-subgroup-test).

(d) First let \( n \in \nN \); we use induction on \( n \) (@fd1:ax-induction). For \( n = 0 \), \( \varphi(a^0) = \varphi(e_G) = e_H = \varphi(a)^0 \) by @def-group-integer-power and (a). If \( \varphi(a^n) = \varphi(a)^n \), then by the recursion \( a^{n+1} = a^n a \) of @def-group-integer-power, in \( G \) and in \( H \),
\[
\varphi(a^{n+1}) = \varphi(a^n a) = \varphi(a^n)\varphi(a) = \varphi(a)^n\varphi(a) = \varphi(a)^{n+1} .
\]
Now let \( n < 0 \), and write \( n = -m \) with \( m \in \nN \). By @def-group-integer-power, \( a^n = (a^{-1})^m \) and \( \varphi(a)^n = (\varphi(a)^{-1})^m \). By the case just proved, applied to \( a^{-1} \), and by (b),
\[
\varphi(a^n) = \varphi\bigl((a^{-1})^m\bigr) = \varphi(a^{-1})^m = \bigl(\varphi(a)^{-1}\bigr)^m = \varphi(a)^n .
\]

(e) By @fd2:def-image, \( \varphi(G) = \{ \varphi(x) : x \in G \} \subseteq H \). It contains \( \varphi(e_G) \), so it is non-empty. For two of its elements \( \varphi(x) \) and \( \varphi(y) \), with \( x, y \in G \), the homomorphism property and (b) give
\[
\varphi(x)\varphi(y)^{-1} = \varphi(x)\varphi(y^{-1}) = \varphi(xy^{-1}) \in \varphi(G) .
\]
So \( \varphi(G) \) is a subgroup by @thm-subgroup-test. This proves the theorem.
:::

So a homomorphism carries the whole structure of Section 3.1, identity, inverses and powers, and not just the products it was defined by. In additive notation, (a), (b) and (d) read \( \varphi(0) = 0 \), \( \varphi(-a) = -\varphi(a) \) and \( \varphi(n \cdot a) = n \cdot \varphi(a) \). Conversely to @exm-group-homomorphisms (b), every homomorphism \( \varphi \colon (\nZ, +) \to G \) is \( k \mapsto \varphi(1)^k \): \( k = k \cdot 1 \) (@prp-group-power-laws (e)), so \( \varphi(k) = \varphi(1)^k \) by (d). Part (c) gives a supply of subgroups: the unit circle \( \nT \) is a subgroup of \( \nC \setminus \{0\} \) because it is the kernel of the modulus (@exm-group-homomorphisms (f)), and \( n\nZ \) is a subgroup of \( \nZ \) because it is the kernel of \( a \mapsto [a] \).

::: {.check}
Is \( a \mapsto 3a \) a homomorphism \( (\nZ, +) \to (\nZ, +) \)? What is its kernel? Is it an isomorphism?
:::

::: {.solution}
Yes: \( 3(a + b) = 3a + 3b \) by distributivity in \( \nZ \) (@fd3:thm-integers-commutative-ring). The kernel is \( \{0\} \), since \( 3a = 0 \) with \( 3 \ne 0 \) forces \( a = 0 \) (@fd3:prp-ordered-ring-rules (f)). It is injective, since \( 3a = 3b \) gives \( 3(a - b) = 0 \) and so \( a = b \) by the same rule, but **not** surjective: \( 1 \) is not of the form \( 3a \), since \( 3 \nmid 1 \) (@fd3:prp-divisibility-rules-integers (g)). So it is not an isomorphism.
:::

Homomorphisms compose, and the inverse of an isomorphism is again one. These are the facts that let "isomorphic" behave like "equal up to renaming".

::: {#prp-homomorphism-composition-inverse}
[Composites and Inverses of Homomorphisms]

Let \( G \), \( H \) and \( K \) be groups.

::: {.enumerate options="label=(\alph*)"}
1. If \( \varphi \colon G \to H \) and \( \psi \colon H \to K \) are homomorphisms, then so is \( \psi \circ \varphi \colon G \to K \).
2. If \( \varphi \colon G \to H \) is an isomorphism, then its inverse function \( \varphi^{-1} \colon H \to G \) is an isomorphism.
3. \( \id_G \) is an isomorphism. Consequently \( G \cong G \); if \( G \cong H \), then \( H \cong G \); and if \( G \cong H \) and \( H \cong K \), then \( G \cong K \).
:::
:::

::: {.idea}
Part (a) is the homomorphism property applied twice. For (b), we cannot compute \( \varphi^{-1} \) directly, but we can compare \( \varphi^{-1}(xy) \) with \( \varphi^{-1}(x)\varphi^{-1}(y) \) after applying \( \varphi \), which is injective.
:::

::: {.proof}
(a) For \( a, b \in G \), by @fd2:def-composition and the homomorphism property of \( \varphi \) and then of \( \psi \),
\[
(\psi \circ \varphi)(ab) = \psi\bigl(\varphi(a)\varphi(b)\bigr) = \psi(\varphi(a))\,\psi(\varphi(b)) = (\psi \circ \varphi)(a)\,(\psi \circ \varphi)(b) .
\]

(b) Since \( \varphi \) is bijective, it has a two-sided inverse \( \varphi^{-1} \) (@fd2:thm-bijection-iff-inverse), which is bijective by the same theorem, with inverse \( \varphi \). Let \( x, y \in H \). Then, since \( \varphi \) is a homomorphism and \( \varphi \circ \varphi^{-1} = \id_H \),
\[
\varphi\bigl(\varphi^{-1}(x)\,\varphi^{-1}(y)\bigr) = \varphi(\varphi^{-1}(x))\,\varphi(\varphi^{-1}(y)) = xy = \varphi\bigl(\varphi^{-1}(xy)\bigr) .
\]
Since \( \varphi \) is injective, \( \varphi^{-1}(x)\varphi^{-1}(y) = \varphi^{-1}(xy) \). So \( \varphi^{-1} \) is a homomorphism, and being bijective, an isomorphism.

(c) \( \id_G \) is an isomorphism (the second of the two homomorphisms listed after @def-group-homomorphism), so \( G \cong G \). If \( \varphi \colon G \to H \) is an isomorphism, so is \( \varphi^{-1} \colon H \to G \) by (b). If \( \varphi \colon G \to H \) and \( \psi \colon H \to K \) are isomorphisms, then \( \psi \circ \varphi \) is a homomorphism by (a) and bijective by @fd2:thm-composition-injective-surjective (c). This proves the proposition.
:::

The kernel was introduced to measure what a homomorphism forgets. At the end where it forgets nothing, the measurement is exact:

::: {#prp-homomorphism-injective-iff-kernel-trivial}
[Injective Exactly When the Kernel Is Trivial]

A homomorphism \( \varphi \colon G \to H \) is injective **if and only if** \( \ker \varphi = \{e_G\} \).
:::

::: {.idea}
Injectivity compares two elements \( a, b \) with the same image; the kernel looks at one element with the image \( e_H \). The quotient \( ab^{-1} \) turns the first question into the second: \( \varphi(a) = \varphi(b) \) says exactly that \( ab^{-1} \) lies in the kernel.
:::

::: {.proof}
\( (\Rightarrow) \) Suppose \( \varphi \) is injective. By @thm-homomorphism-basic-properties (a), \( e_G \in \ker \varphi \). If \( g \in \ker \varphi \), then \( \varphi(g) = e_H = \varphi(e_G) \), so \( g = e_G \) by injectivity. Hence \( \ker \varphi = \{e_G\} \).

\( (\Leftarrow) \) Suppose \( \ker \varphi = \{e_G\} \), and let \( a, b \in G \) with \( \varphi(a) = \varphi(b) \). By the homomorphism property and @thm-homomorphism-basic-properties (b),
\[
\varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1} = \varphi(b)\varphi(b)^{-1} = e_H .
\]
So \( ab^{-1} \in \ker \varphi \), that is, \( ab^{-1} = e_G \). **Multiply by the inverse:** multiplying on the right by \( b \) and using (G1)–(G3), \( a = ab^{-1}b = e_G b = b \). So \( \varphi \) is injective. This proves the proposition.
:::

To decide injectivity we now check one equation, \( \varphi(g) = e_H \), instead of all pairs \( a, b \). Linear maps in linear algebra satisfy the same statement, with the same proof read additively: *Spaces and Maps*, the chapter "Linear Maps", proves that a linear map is injective exactly when its kernel is \( \{0\} \).

::: {.check}
Use the proposition to show that \( k \mapsto [3]^k \), from \( (\nZ, +) \) to \( (\nZ/7\nZ)^{\times} \), is not injective.
:::

::: {.solution}
It is a homomorphism by @exm-group-homomorphisms (b). Its kernel contains \( 6 \), since \( [3]^6 = [729] = [1] \) (\( 729 = 104 \cdot 7 + 1 \)). So the kernel is not \( \{0\} \), and by @prp-homomorphism-injective-iff-kernel-trivial the map is not injective; indeed \( [3]^0 = [3]^6 \).
:::

## Isomorphic and non-isomorphic groups

An isomorphism is a renaming, so we expect two isomorphic groups to agree on every property that is stated with the operation alone. For the three properties used here this is a one-line check; let \( \varphi \colon G \to H \) be an isomorphism. A bijection preserves the number of elements. If \( G \) is abelian, then any two elements of \( H \) are \( \varphi(a), \varphi(b) \), and \( \varphi(a)\varphi(b) = \varphi(ab) = \varphi(ba) = \varphi(b)\varphi(a) \). And \( x^2 = e_G \) exactly when \( \varphi(x)^2 = e_H \), by the homomorphism property, @thm-homomorphism-basic-properties (a) and injectivity, so \( \varphi \) maps the solutions of \( x^2 = e \) in \( G \) bijectively onto those in \( H \). This gives a method in both directions. To show \( G \cong H \), write down a bijection and check the homomorphism property. To show \( G \not\cong H \), find such a property that one group has and the other lacks.

::: {#exm-isomorphic-small-groups}
[Isomorphic and Non-Isomorphic Small Groups]

::: {.enumerate options="label=(\alph*)"}
1. Show that \( (\nZ/2\nZ, +) \cong (\{1, -1\}, \cdot) \).
2. Show that \( (\nZ/4\nZ, +) \cong ((\nZ/5\nZ)^{\times}, \cdot) \), by \( [k] \mapsto [2]^k \).
3. Show that \( (\nZ/4\nZ, +) \) and \( ((\nZ/8\nZ)^{\times}, \cdot) \) are **not** isomorphic.
4. Show that \( (\nZ, +) \cong (2\nZ, +) \), by \( x \mapsto 2x \).
:::
:::

::: {.solution}
(a) By @fd3:thm-integers-mod-n-ring (b), each element of \( \nZ/2\nZ \) is \( [r] \) for exactly one \( r \in \{0, 1\} \), so \( \varphi([0]) \coloneqq 1 \), \( \varphi([1]) \coloneqq -1 \) defines a function. It is bijective, since it pairs off the two elements. The homomorphism property is the comparison of the two tables at the start of the section, four equations:
\[
\begin{aligned}
\varphi([0] + [0]) &= \varphi([0]) = 1 = 1 \cdot 1 , &
\varphi([0] + [1]) &= \varphi([1]) = -1 = 1 \cdot (-1) , \\
\varphi([1] + [0]) &= \varphi([1]) = -1 = (-1) \cdot 1 , &
\varphi([1] + [1]) &= \varphi([0]) = 1 = (-1)(-1) ,
\end{aligned}
\]
using \( [1] + [1] = [2] = [0] \) and \( (-1)(-1) = 1 \) (@fd3:prp-ring-algebra (c)).

(b) The target is a group by @prp-units-form-group. Its elements are the four non-zero classes \( [1], [2], [3], [4] \) (@fd3:thm-integers-mod-n-ring (b), (c)): each is a unit, since \( [1][1] = [1] \), \( [2][3] = [6] = [1] \) and \( [4][4] = [16] = [1] \), while \( [0] \) is not, since \( [0][v] = [0] \ne [1] \).

*Well defined.* The rule must not depend on the representative \( k \). The powers \( [2]^0, [2]^1, [2]^2, [2]^3, [2]^4 \) are \( [1], [2], [4], [8] = [3], [16] = [1] \). If \( [k] = [k'] \) in \( \nZ/4\nZ \), then \( k' - k \in 4\nZ \) (@fd3:thm-quotient-ring-by-ideal (a)), so \( k' = k + 4q \) for some \( q \in \nZ \), and by @prp-group-power-laws (a) and (c),
\[
[2]^{k'} = [2]^k \bigl([2]^4\bigr)^q = [2]^k [1]^q = [2]^k ,
\]
where \( [1]^q = \bigl([2]^0\bigr)^q = [2]^{0 \cdot q} = [1] \), again by (c).

*Homomorphism.* \( [k] + [l] = [k + l] \mapsto [2]^{k + l} = [2]^k [2]^l \), by @prp-group-power-laws (a).

*Bijective.* The four distinct classes \( [0], [1], [2], [3] \), which are all of \( \nZ/4\nZ \) (@fd3:thm-integers-mod-n-ring (b)), go to \( [1], [2], [4], [3] \): four different elements, which are all of \( (\nZ/5\nZ)^{\times} \). So the map is injective and surjective.

(c) Both groups have four elements (@fd3:thm-integers-mod-n-ring (b)). In \( (\nZ/8\nZ)^{\times} = \{[1], [3], [5], [7]\} \) (the even classes are not units: \( [0] \), and \( [2][4] = [4][2] = [6][4] = [0] \) with \( [4], [2] \ne [0] \), and a unit is not a zero divisor, the paragraph after @fd3:def-ring-unit), every element \( y \) has \( y^2 = [1] \): the squares are \( [1] \), \( [9] = [1] \), \( [25] = [1] \), \( [49] = [1] \). Suppose \( \varphi \colon \nZ/4\nZ \to (\nZ/8\nZ)^{\times} \) were an isomorphism. Then, by the homomorphism property and @thm-homomorphism-basic-properties (a),
\[
\varphi([2]) = \varphi([1] + [1]) = \varphi([1])^2 = [1] = \varphi([0]) .
\]
Since \( [2] \ne [0] \) in \( \nZ/4\nZ \), this contradicts injectivity. So no isomorphism exists.

(d) \( 2\nZ \) is a subgroup of \( \nZ \) (@exm-subgroups (b)), so a group. The map \( x \mapsto 2x \) is a homomorphism by distributivity, \( 2(x + y) = 2x + 2y \) (@fd3:thm-integers-commutative-ring). It is surjective onto \( 2\nZ \) by the definition of \( 2\nZ \), and injective because its kernel is \( \{0\} \): \( 2x = 0 \) forces \( x = 0 \) (@fd3:prp-ordered-ring-rules (f)), and @prp-homomorphism-injective-iff-kernel-trivial applies. So \( \nZ \cong 2\nZ \): a group can be isomorphic to a subgroup of itself other than itself.
:::

The square of Section 3.1, turned by quarter turns, gives another group with four elements; once its rotations are written as permutations, Exercise B3 of Section 3.4 matches them with \( \nZ/4\nZ \).

::: {.warning}
Two groups with the same number of elements need not be isomorphic. \( \nZ/4\nZ \) and \( (\nZ/8\nZ)^{\times} \) both have four elements, yet part (c) shows that no isomorphism exists between them. Equal counts decide nothing by themselves: different counts prove \( G \not\cong H \), but equal counts never prove \( G \cong H \). To prove \( G \not\cong H \), find a property that an isomorphism would carry over and that one group has and the other lacks; in (c) it was "some element \( x \) has \( x^2 \ne e \)", which holds in \( \nZ/4\nZ \) (in additive form, \( [1] + [1] \ne [0] \)) and fails in \( (\nZ/8\nZ)^{\times} \).
:::

::: {.remark}
[Where homomorphisms go next]

In linear algebra, a linear map is in particular a homomorphism of the additive groups, and its kernel is the kernel of this section (*Spaces and Maps*, the chapter "Linear Maps"). The determinant will be a homomorphism from the invertible matrices to \( F^{\times} \) (*Determinants and the Structure of Operators*, the chapter "Determinants"). Quotient groups and the isomorphism theorems are in *Groups*, the chapter "Normal Subgroups, Quotient Groups, and the Isomorphism Theorems".
:::

::: {.remark}
[Field homomorphisms as group homomorphisms]

In the terms of Chapter 2 (no proof in this chapter rests on this remark): a field homomorphism \( \varphi \colon F \to L \) (@def-field-homomorphism) is a homomorphism of the additive groups \( (F, +) \to (L, +) \); it sends \( F^{\times} \) into \( L^{\times} \), and is a homomorphism of these multiplicative groups (@prp-field-homomorphism-properties (a)–(c)). The automorphisms of \( F \) form a group under composition (@prp-field-homomorphism-properties (e)), a subgroup of the group of bijections of \( F \) (@exm-groups (c)). And the multiplicative group \( \nF_p^{\times} \) of the field with \( p \) elements is the group \( (\nZ/p\nZ)^{\times} \) of @prp-units-form-group.
:::

## Exercises

### A. Check your understanding

::: {#exr-homomorphisms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. In the proof of \( (\Leftarrow) \) of @prp-homomorphism-injective-iff-kernel-trivial, where is it used that \( \varphi \) is a homomorphism?
2. The map \( \nZ \to \nZ/6\nZ \times \nZ/4\nZ \), \( a \mapsto ([a], [a]) \), is a homomorphism of additive groups. Find its kernel.
3. True or false: a homomorphism \( \varphi \colon G \to H \) sends every subgroup \( K \) of \( G \) onto a subgroup \( \varphi(K) \) of \( H \). Justify your answer.
4. The map \( x \mapsto x + 1 \) on \( (\nZ, +) \) sends \( 0 \) to \( 1 \). Could it become a homomorphism \( (\nZ,+) \to (\nZ,+) \) if \( 1 \) were declared the identity of the target, keeping its operation \( + \)? Explain.
:::
:::

::: {.solution}
(a) In the first displayed step, \( \varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1} \): the homomorphism property gives \( \varphi(ab^{-1}) = \varphi(a)\varphi(b^{-1}) \), and @thm-homomorphism-basic-properties (b), itself a consequence of the homomorphism property, gives \( \varphi(b^{-1}) = \varphi(b)^{-1} \). Without it, \( \varphi(a) = \varphi(b) \) says nothing about \( ab^{-1} \).

(b) The map is a homomorphism into the product group, coordinate by coordinate (@exm-group-homomorphisms (a) in each coordinate). Its kernel is \( \{ a : [a]_6 = [0]_6 \text{ and } [a]_4 = [0]_4 \} = 6\nZ \cap 4\nZ \), by @fd3:thm-quotient-ring-by-ideal (d). This is a subgroup of \( \nZ \) (@prp-subgroup-intersection), so it is \( d\nZ \) with \( d \) its least positive element (@thm-subgroups-of-integers). The positive multiples of \( 6 \) are \( 6, 12, \dots \), and \( 4 \nmid 6 \), \( 4 \mid 12 \); so \( d = 12 \) and the kernel is \( 12\nZ \).

(c) True. A subgroup \( K \) is a group with the operation of \( G \) (the paragraph after @def-subgroup), and the restriction of \( \varphi \) to \( K \) is a homomorphism \( K \to H \), since the homomorphism property for \( a, b \in K \) is a special case of that for \( a, b \in G \). Its image is \( \varphi(K) \), a subgroup of \( H \) by @thm-homomorphism-basic-properties (e).

(d) No. The identity of a group is not chosen; it is the element with (G2), and it is unique (@thm-group-basic-properties (1)). In \( (\nZ, +) \) it is \( 0 \), since \( 1 + 1 \ne 1 \). Every homomorphism into \( (\nZ, +) \) must send \( 0 \) to \( 0 \) (@thm-homomorphism-basic-properties (a)), and \( x \mapsto x + 1 \) does not. Changing the operation does change the identity: with \( a \ast b \coloneqq a + b - 1 \), whose identity is \( 1 \), the map is an isomorphism \( (\nZ,+) \to (\nZ,\ast) \); compare @exr-groups-a1 (b). But that is a different group.
:::

### B. Practice

::: {#exr-homomorphisms-b1}
[B1]

Find all homomorphisms \( (\nZ, +) \to (\nZ/6\nZ, +) \), and the kernel of each.

*Hint: @thm-homomorphism-basic-properties (d), applied to \( k = k \cdot 1 \).*
:::

::: {.solution}
Let \( \varphi \) be a homomorphism and write \( \varphi(1) = [c] \) with \( c \in \{0, \dots, 5\} \) (@fd3:thm-integers-mod-n-ring (b)). For \( k \in \nZ \), \( k = k \cdot 1 \) in \( (\nZ, +) \) (@prp-group-power-laws (e)), so @thm-homomorphism-basic-properties (d), in additive notation, gives
\[
\varphi(k) = \varphi(k \cdot 1) = k \cdot \varphi(1) = k \cdot [c] .
\]
So \( \varphi \) is determined by \( c \). Conversely, for each \( c \), the map \( k \mapsto k \cdot [c] \) is a homomorphism by @exm-group-homomorphisms (b) with \( g = [c] \). So there are exactly six homomorphisms, one for each class \( [c] \).

*Kernels.* The quotient map \( a \mapsto [a] \) is a homomorphism (@exm-group-homomorphisms (a)), so @thm-homomorphism-basic-properties (d) and @prp-group-power-laws (e) give \( k \cdot [c] = [k \cdot c] = [kc] \). Hence, since \( [kc] = [0] \) exactly when \( kc \in 6\nZ \) (@fd3:thm-quotient-ring-by-ideal (d)), the kernel is \( \{ k \in \nZ : 6 \mid kc \} \), a subgroup of \( \nZ \), so it is \( d\nZ \) with \( d \) the least positive \( k \) with \( 6 \mid kc \) (@thm-subgroups-of-integers). Running through \( k = 1, 2, \dots \):

| \( c \) | \( 0 \) | \( 1 \) | \( 2 \) | \( 3 \) | \( 4 \) | \( 5 \) |
|---|---|---|---|---|---|---|
| least \( k \) with \( 6 \mid kc \) | \( 1 \) | \( 6 \) | \( 3 \) | \( 2 \) | \( 3 \) | \( 6 \) |
| kernel | \( \nZ \) | \( 6\nZ \) | \( 3\nZ \) | \( 2\nZ \) | \( 3\nZ \) | \( 6\nZ \) |

For instance, for \( c = 4 \): \( 4 \), \( 8 \) are not multiples of \( 6 \), and \( 12 \) is. For \( c = 5 \): \( 5, 10, 15, 20, 25 \) are not, and \( 30 \) is.
:::

::: {#exr-homomorphisms-b2}
[B2]

::: {.enumerate options="label=(\alph*)"}
1. Let \( G \) and \( H \) be groups. Show that \( G \to G \times H \), \( g \mapsto (g, e_H) \), is an injective homomorphism into the product group.
2. Show that \( \nZ/2\nZ \times \nZ/2\nZ \) and \( \nZ/4\nZ \) (additive groups) are not isomorphic.
:::
:::

::: {.solution}
(a) For \( g, g' \in G \), \( (gg', e_H) = (gg', e_He_H) = (g, e_H)(g', e_H) \), by (G2) in \( H \) and the definition of the product operation. The kernel is \( \{ g : (g, e_H) = (e_G, e_H) \} = \{e_G\} \), since two pairs are equal exactly when their coordinates are. By @prp-homomorphism-injective-iff-kernel-trivial the map is injective.

(b) The invariant is that of @exm-isomorphic-small-groups (c). In \( \nZ/2\nZ \times \nZ/2\nZ \), every element satisfies \( x + x = 0 \): \( ([a], [b]) + ([a], [b]) = ([2a], [2b]) = ([0], [0]) \). Suppose \( \varphi \colon \nZ/4\nZ \to \nZ/2\nZ \times \nZ/2\nZ \) were an isomorphism. Then
\[
\varphi([2]) = \varphi([1] + [1]) = \varphi([1]) + \varphi([1]) = ([0], [0]) = \varphi([0])
\]
by @thm-homomorphism-basic-properties (a), against injectivity, since \( [2] \ne [0] \) in \( \nZ/4\nZ \). An isomorphism in the other direction would have an inverse that is an isomorphism (@prp-homomorphism-composition-inverse (b)), so it cannot exist either.
:::

::: {#exr-homomorphisms-b3}
[B3]

Give an example of a homomorphism from \( (\nQ \setminus \{0\}, \cdot) \) **onto** \( (\{1, -1\}, \cdot) \), and find its kernel.
:::

::: {.solution}
*What any answer must have.* A function \( \varphi \colon \nQ \setminus \{0\} \to \{1, -1\} \) with \( \varphi(xy) = \varphi(x)\varphi(y) \) for all non-zero \( x, y \), taking **both** values \( 1 \) and \( -1 \). Its kernel is then a subgroup (@thm-homomorphism-basic-properties (c)) that is not the whole group.

*One answer: the sign.* Let \( \varphi(x) \coloneqq 1 \) if \( x > 0 \) and \( \varphi(x) \coloneqq -1 \) if \( x < 0 \). This defines a function on \( \nQ \setminus \{0\} \), since the order of \( \nQ \) is total (@fd3:thm-rationals-ordered-field; @fd3:prp-ordered-ring-rules (i)). By the rules of the ordered field \( \nQ \) (@fd3:prp-ordered-ring-rules (c), (d)), the product of two positives is positive, of a positive and a negative is negative, and of two negatives is positive. In each of the four cases \( \varphi(xy) = \varphi(x)\varphi(y) \): for example, if \( x > 0 > y \), then \( xy < 0 \) and \( \varphi(xy) = -1 = 1 \cdot (-1) \). Both values are taken, at \( 1 \) and \( -1 \). The kernel is \( \nQ_{>0} \).

Other answers exist. For instance, writing a non-zero rational as \( \pm 2^k a/b \) with \( a, b \) odd, the parity of \( k \) gives another one; we do not prove that this is well defined here.
:::

### C. Going deeper

::: {#exr-homomorphisms-c1}
[C1]

::: {.enumerate options="label=(\alph*)"}
1. Let \( \varphi \colon G \to H \) be a homomorphism, with \( G \) abelian. Prove that the subgroup \( \varphi(G) \) of \( H \) is abelian.
2. Deduce that there is no homomorphism from \( \nZ/6\nZ \) **onto** the group of bijections of \( \{1, 2, 3\} \).
:::
:::

::: {.solution}
(a) Let \( u, v \in \varphi(G) \), say \( u = \varphi(a) \) and \( v = \varphi(b) \) with \( a, b \in G \) (@fd2:def-image). Then
\[
uv = \varphi(a)\varphi(b) = \varphi(ab) = \varphi(ba) = \varphi(b)\varphi(a) = vu ,
\]
using that \( G \) is abelian in the middle step.

(b) \( \nZ/6\nZ \) is abelian (@exm-groups (a)). If \( \varphi \) were a homomorphism from it onto the group of bijections of \( \{1, 2, 3\} \), then that group would be \( \varphi(\nZ/6\nZ) \), abelian by (a). It is not: the bijections \( f \) swapping \( 1, 2 \) and \( g \) swapping \( 2, 3 \) satisfy \( (f \circ g)(1) = f(1) = 2 \) and \( (g \circ f)(1) = g(2) = 3 \), as in the fold after @exm-groups (c). So no such homomorphism exists. (Size alone could not decide this: Section 3.4 shows that both groups have six elements.)

**Marking scheme.** (10 points)
- 2: (a) writes arbitrary \( u, v \in \varphi(G) \) as \( \varphi(a), \varphi(b) \).
- 3: (a) the chain \( uv = \varphi(ab) = \varphi(ba) = vu \), with the homomorphism property and commutativity of \( G \) named.
- 1: (b) notes that \( \nZ/6\nZ \) is abelian.
- 1: (b) "onto" makes the target equal to \( \varphi(\nZ/6\nZ) \), so (a) applies.
- 3: (b) exhibits two bijections of \( \{1, 2, 3\} \) that do not commute, with a point where the two composites differ.
Fatal errors (0 for the step): (a) takes \( u, v \) in all of \( H \) rather than in the image; (b) argues from the number of elements alone.
:::

::: {#exr-homomorphisms-c2}
[C2]

Let \( \varphi \colon G \to H \) be a homomorphism and \( a, b \in G \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that the following are equivalent: (i) \( \varphi(a) = \varphi(b) \); (ii) \( ab^{-1} \in \ker \varphi \); (iii) \( a^{-1}b \in \ker \varphi \).
2. Deduce that the set of elements with the same image as \( a \), the **fiber** \( \varphi^{-1}(\{\varphi(a)\}) \), equals \( \{ ak : k \in \ker \varphi \} \).
3. For the quotient map \( \nZ \to \nZ/5\nZ \), \( x \mapsto [x] \), write out the fiber of \( 7 \).
:::
:::

::: {.solution}
(a) (i) \( \Rightarrow \) (ii): as in the proof of @prp-homomorphism-injective-iff-kernel-trivial, \( \varphi(ab^{-1}) = \varphi(a)\varphi(b)^{-1} = \varphi(b)\varphi(b)^{-1} = e_H \).

(ii) \( \Rightarrow \) (i): if \( \varphi(ab^{-1}) = e_H \), then \( \varphi(a)\varphi(b)^{-1} = e_H \); multiplying on the right by \( \varphi(b) \), \( \varphi(a) = \varphi(b) \).

(i) \( \Leftrightarrow \) (iii): the same two arguments with \( a^{-1}b \): \( \varphi(a^{-1}b) = \varphi(a)^{-1}\varphi(b) \) (@thm-homomorphism-basic-properties (b)), which is \( e_H \) exactly when \( \varphi(b) = \varphi(a) \), multiplying on the left by \( \varphi(a) \) or by \( \varphi(a)^{-1} \).

(b) \( (\subseteq) \) Let \( b \) lie in the fiber, so \( \varphi(b) = \varphi(a) \). By (a), \( k \coloneqq a^{-1}b \in \ker \varphi \), and \( b = a(a^{-1}b) = ak \). \( (\supseteq) \) If \( k \in \ker \varphi \), then \( \varphi(ak) = \varphi(a)e_H = \varphi(a) \).

(c) The kernel is \( 5\nZ \) (@exm-group-homomorphisms (a)), so by (b) the fiber of \( 7 \) is \( \{ 7 + 5j : j \in \nZ \} = \{ \dots, -3, 2, 7, 12, \dots \} \), the class \( [7] = [2] \) itself. The sets \( \{ ak : k \in \ker \varphi \} \) are the **cosets** of the kernel, which *Groups*, the chapter "Cosets and Lagrange's Theorem", studies for every subgroup.

**Marking scheme.** (10 points)
- 2: (a) (i) \( \Rightarrow \) (ii), using \( \varphi(b^{-1}) = \varphi(b)^{-1} \), cited.
- 2: (a) (ii) \( \Rightarrow \) (i), multiplying by \( \varphi(b) \) on the right.
- 2: (a) (i) \( \Leftrightarrow \) (iii), both directions, by the mirror argument.
- 2: (b) both inclusions, with \( k \coloneqq a^{-1}b \) for \( (\subseteq) \).
- 2: (c) kernel \( 5\nZ \), and the fiber \( \{ 7 + 5j : j \in \nZ \} \).
Fatal errors (0 for the step): (a) "divides" by \( \varphi(b) \), or uses commutativity of \( H \); (b) proves one inclusion and calls it equality.
:::

<!-- dependency ledger
def-group-homomorphism (claim): (paragraph after the definition) the map F -> F, x -> 0 respects + and . of a field but sends 1 to 0 | prp-ring-algebra (b) of fd3 (0 = 0 + 0, 0 . 0 = 0), inline; Chapter 2 named in prose only, nothing depends on it
def-group-homomorphism (claim): trivial homomorphism and id_G; id_G bijective | (G2); fd2:thm-bijection-iff-inverse, cited
def-group-homomorphism (claim): product group G x H satisfies (G1)-(G3) coordinatewise; abelian if G, H are | fd2:def-cartesian-product, equality of pairs coordinatewise; inline
exm-group-homomorphisms (example): (a) Z/nZ a group; [a + b] = [a] + [b]; kernel nZ; surjective | exm-groups (a), fd3:thm-quotient-ring-by-ideal (c), (d), fd3:def-integers-mod-n-ring, fd2:def-quotient-set (every element a class), cited
exm-group-homomorphisms (example): (b) powers of [3] in (Z/7Z)^x: [1],[3],[2],[6],[4],[5], [3]^6 = [1] | inline arithmetic; verify/ch03/exm-group-homomorphisms.py
exm-group-homomorphisms (example): (c) c_g(x)c_g(y) = c_g(xy); inverse c_{g^-1} | prp-group-list-product-laws (b), thm-group-basic-properties (3), fd2:def-inverse-function, fd2:thm-bijection-iff-inverse, fd2:prp-function-equality, cited
exm-group-homomorphisms (example): (d) squares in (Z/7Z)^x and (Z/8Z)^x | inline arithmetic; verify/ch03/exm-group-homomorphisms.py
exm-group-homomorphisms (example): (e) gcd(3, 4) = 1 from 1 = 4 - 3 | fd3:cor-coprime-iff-combination, cited; fd3:thm-chinese-remainder-two (b), cited
exm-group-homomorphisms (example): (f) (R_{>0}, .) a group: positives closed under . (O4), (F5)-(F7), 1 > 0, x^{-1} exists (O1), (F8), x^{-1} > 0 | fd3:thm-reals-ordered-field (ordered field axioms), fd3:def-ordered-ring-and-field (O1), (O4), fd3:def-commutative-ring-and-field (F5)-(F8), fd3:prp-ordered-ring-rules (e) (1 > 0), fd3:prp-reciprocal-order (a); F3.10 used in an example only
exm-group-homomorphisms (claim): (paragraph after it) c_g != id_G when g fails to commute, e.g. the swaps f, g | exm-groups (c) and its fold, cited
thm-homomorphism-basic-properties (claim): (paragraph after it) every homomorphism Z -> G is k -> phi(1)^k, the converse of exm-group-homomorphisms (b) | prp-group-power-laws (e), thm-homomorphism-basic-properties (d), exm-group-homomorphisms (b), cited
exm-group-homomorphisms (example): (f) C a field, |z| >= 0, |z| != 0 for z != 0, |zw| = |z||w|, kernel the unit circle | F4.1: thm-complex-numbers-field, def-conjugate-modulus, thm-conjugate-properties (d), (e), prp-unit-circle (labels from the frozen blueprint ch01.md); example only, no proof rests on it
thm-homomorphism-basic-properties (proof): (d) induction on n in N | fd1:ax-induction read on omega (fd3 cor-omega-identification, F3.1 citing rule)
thm-homomorphism-basic-properties (proof): e_H^{-1} = e_H | thm-group-basic-properties (2), inline
thm-homomorphism-basic-properties (claim): (check after it) 3(a + b) = 3a + 3b; 3a = 0 => a = 0; 3 does not divide 1 | fd3:thm-integers-commutative-ring, fd3:prp-ordered-ring-rules (f), fd3:prp-divisibility-rules-integers (g), cited
prp-homomorphism-injective-iff-kernel-trivial (claim): (check after it) [3]^6 = [729] = [1], 729 = 104 * 7 + 1 | inline arithmetic; verify/ch03/prp-homomorphism-injective-iff-kernel-trivial.py
prp-homomorphism-injective-iff-kernel-trivial (claim): (aftermath) linear maps: injective iff kernel {0} | Spaces and Maps (LA1.2), prose pointer, nothing depends on it
exm-isomorphic-small-groups (example): (a) four sums in Z/2Z, (-1)(-1) = 1 | fd3:thm-integers-mod-n-ring (b), fd3:prp-ring-algebra (c), cited; verify/ch03/exm-isomorphic-small-groups.py
exm-isomorphic-small-groups (example): (b) (Z/5Z)^x = {[1],[2],[3],[4]}; [2]^k for k = 0..4; well defined via [2]^4 = [1]; images [1],[2],[4],[3] | prp-units-form-group, prp-group-power-laws (a), (c), fd3:thm-integers-mod-n-ring (b), (c), fd3:thm-quotient-ring-by-ideal (a), cited; inline arithmetic; verify/ch03/exm-isomorphic-small-groups.py
exm-isomorphic-small-groups (example): (c) (Z/8Z)^x = {[1],[3],[5],[7]}, even classes zero divisors, squares all [1] | fd3:thm-integers-mod-n-ring (b) (four elements each), fd3:def-ring-unit and the paragraph after it (a unit is not a zero divisor), cited; inline arithmetic; verify/ch03/exm-isomorphic-small-groups.py
exm-isomorphic-small-groups (example): (d) 2(x + y) = 2x + 2y; 2x = 0 => x = 0 | fd3:thm-integers-commutative-ring, fd3:prp-ordered-ring-rules (f), exm-subgroups (b), cited
exm-isomorphic-small-groups (claim): (paragraph after it) the rotations of the square are matched with Z/4Z in Section 3.4, Exercise B3 | forward pointer within the chapter (F4.3 §04 B3), nothing depends on it
exm-isomorphic-small-groups (claim): (paragraph before it) isomorphisms carry over the number of elements, being abelian, and the solutions of x^2 = e | bijectivity, homomorphism property, thm-homomorphism-basic-properties (a), injectivity; inline
exm-isomorphic-small-groups (claim): (warning) isomorphisms carry "some x has x^2 != e" | thm-homomorphism-basic-properties (a) and the homomorphism property, as in (c); inline
def-group-homomorphism (claim): (remark) linear maps, determinant, quotient groups; field homomorphisms as group homomorphisms, automorphisms a group, F_p^x = (Z/pZ)^x | Spaces and Maps, Determinants and the Structure of Operators, Groups (prose pointers); F4.2 def-field-homomorphism, prp-field-homomorphism-properties (a)-(c), (e) (labels from the frozen blueprint ch02.md), prp-units-form-group; remark only, nothing depends on it
exr-homomorphisms-a1 (solution): (b) 6Z cap 4Z = 12Z, 4 does not divide 6, 4 | 12 | prp-subgroup-intersection, thm-subgroups-of-integers, fd3:thm-quotient-ring-by-ideal (d), cited; verify/ch03/exr-homomorphisms-a1.py
exr-homomorphisms-a1 (solution): (c) restriction of a homomorphism to a subgroup is a homomorphism | def-subgroup and the paragraph after it; inline
exr-homomorphisms-b1 (solution): the six kernels; k . [c] = [kc] | thm-homomorphism-basic-properties (d), prp-group-power-laws (e), thm-subgroups-of-integers, fd3:thm-integers-mod-n-ring (b), fd3:thm-quotient-ring-by-ideal (d), exm-group-homomorphisms (a), (b), cited; verify/ch03/exr-homomorphisms-b1.py
exr-homomorphisms-b2 (solution): ([a],[b]) + ([a],[b]) = ([0],[0]) in Z/2Z x Z/2Z | inline arithmetic; verify/ch03/exr-homomorphisms-b2.py
exr-homomorphisms-b3 (solution): sign rules for products in Q; total order | fd3:thm-rationals-ordered-field, fd3:prp-ordered-ring-rules (c), (d), (i), cited; the 2-adic alternative stated, not proved, not used
exr-homomorphisms-c1 (solution): the bijections of {1, 2, 3} do not commute; both groups have six elements (aside) | exm-groups (c) and its fold, cited, recomputed inline; the six-element aside is a prose pointer to Section 3.4 (F4.3 §04), no @ref, the argument does not use it
exr-homomorphisms-a1 (solution): (d) a * b := a + b - 1 has identity 1 and x -> x + 1 is an isomorphism (Z,+) -> (Z,*) | inline; exr-groups-a1 (b) for comparison, an exercise cited from an exercise solution (STYLE, section 6); nothing depends on it
exr-homomorphisms-c2 (solution): fiber of 7 under Z -> Z/5Z | exm-group-homomorphisms (a), inline; cosets: Groups (AL1.4), prose pointer
-->
