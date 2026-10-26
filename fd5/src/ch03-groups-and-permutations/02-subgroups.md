# Subgroups and the Subgroups of the Integers

Section 3.1 defined groups and proved their basic laws. After a structure comes the substructure. The even integers sit inside \( (\nZ, +) \) and form a group on their own, with the same addition; so do the multiples of \( 7 \), of \( 12 \), and of \( 0 \), which is just \( \{0\} \). Are there any other subgroups of \( \nZ \)? Section 1.3 answered the same question for ideals, which are closed under multiplication by every integer (@thm-integer-ideals-principal). Here the multiplication is gone, and the answer is the same: this section proves that the subgroups of \( (\nZ, +) \) are exactly the sets \( n\nZ \) with \( n \in \nN \).

## Subgroups

A subset of a group can fail to be a group with the inherited operation in three ways: a product can leave it, the identity can be missing, or an inverse can be missing. The definition rules out all three.

*A subgroup is a subset that contains the identity and is closed under products and inverses.*

::: {#def-subgroup}
[Subgroup]

Let \( G \) be a group. A subset \( H \subseteq G \) is a **subgroup** of \( G \) if \( e \in H \), and \( ab \in H \) and \( a^{-1} \in H \) **for all** \( a, b \in H \).
:::

In words: the identity of \( G \) is in \( H \); multiplying two elements of \( H \) never leaves \( H \); and the inverse in \( G \) of an element of \( H \) lies in \( H \). We say "\( H \) is a subgroup of \( G \)" in words and use no symbol for it; in this chapter \( \le \) always means the order of \( \nZ \).

Then the operation of \( G \) restricts to a binary operation \( H \times H \to H \), and \( H \) is a group with it: (G1) holds in \( H \) because it holds in \( G \), and (G2), (G3) hold because \( e \) and the inverses lie in \( H \). The identity of the group \( H \) is the identity \( e \) of \( G \), and the inverse of \( a \) in \( H \) is its inverse in \( G \), by the uniqueness in @thm-group-basic-properties (1) and (2). Three conditions are a lot to check; in practice one checks that \( H \) is non-empty and a single combined condition.

::: {#thm-subgroup-test}
[Subgroup Test]

Let \( G \) be a group and \( H \subseteq G \). Then \( H \) is a subgroup of \( G \) if and only if \( H \ne \emptyset \) and \( ab^{-1} \in H \) for all \( a, b \in H \).
:::

::: {.proof}
\( (\Rightarrow) \) If \( H \) is a subgroup, then \( e \in H \), so \( H \ne \emptyset \). For \( a, b \in H \) we have \( b^{-1} \in H \), and then \( ab^{-1} \in H \), since \( H \) is closed under products.

\( (\Leftarrow) \) Suppose \( H \ne \emptyset \) and \( ab^{-1} \in H \) for all \( a, b \in H \). Pick \( h \in H \). Taking \( a = b = h \) gives \( e = hh^{-1} \in H \). For \( b \in H \), taking \( a = e \) gives \( b^{-1} = eb^{-1} \in H \). For \( a, b \in H \), we now know \( b^{-1} \in H \), so \( ab = a(b^{-1})^{-1} \in H \) by @thm-group-basic-properties (3). Hence \( H \) is a subgroup. This proves the theorem.
:::

In additive notation the test reads: \( H \ne \emptyset \) and \( a - b \in H \) for all \( a, b \in H \), where \( a - b \coloneqq a + (-b) \).

::: {#exm-subgroups}
[Subgroups]

Check that each of the following is a subgroup.

::: {.enumerate options="label=(\alph*)"}
1. \( \{e\} \) and \( G \), in any group \( G \).
2. \( n\nZ \) in \( (\nZ, +) \), for \( n \in \nZ \); more generally \( a\nZ + b\nZ \), for \( a, b \in \nZ \) (@def-integer-linear-combinations).
3. \( \{1, -1\} \) and \( \nQ_{>0} \) in \( (\nQ \setminus \{0\}, \cdot) \).
4. \( \{[0], [2], [4]\} \) in \( (\nZ/6\nZ, +) \); \( \{[1], [3]\} \) in \( (\nZ/8\nZ)^{\times} \).
5. In the group of bijections of a set \( X \) (@exm-groups (c)), the bijections \( \sigma \) that fix a chosen point \( x_0 \in X \), that is, \( \sigma(x_0) = x_0 \).
6. \( \{1, i, -1, -i\} \), the unit circle \( \nT \), and, for \( n \ge 1 \), the set \( \mu_n \) of \( n \)-th roots of unity, in \( (\nC \setminus \{0\}, \cdot) \) (*Analytic Preliminaries*, Chapter 1).
:::
:::

::: {.solution}
In each case we use @thm-subgroup-test, or @def-subgroup directly.

*(a)* \( \{e\} \) is non-empty, and \( ee^{-1} = e \). \( G \) is non-empty, since \( e \in G \), and \( ab^{-1} \in G \) because the operation is a binary operation. The **trivial subgroup** \( \{e\} \) is the smallest subgroup of every group: by the definition, every subgroup contains \( e \).

*(b)* \( 0 = 0n \in n\nZ \) (@fd3:prp-ring-algebra (b), with (F6)). For \( kn, ln \in n\nZ \),
\[
kn - ln = kn + (-l)n = (k - l)n \in n\nZ ,
\]
by @fd3:prp-ring-algebra (c), then (F9) with (F6). In the same way \( 0 = a0 + b0 \in a\nZ + b\nZ \), and \( (ax + by) - (ax' + by') = a(x - x') + b(y - y') \). So both are subgroups, by the additive form of the test. For instance \( 2\nZ \) is the set of even integers, and \( 0\nZ = \{0\} \).

*(c)* For \( \{1, -1\} \): \( (-1)(-1) = 1 \) (@fd3:prp-ring-algebra (c)), so each of \( 1, -1 \) is its own inverse, and the products \( 1 \cdot 1 = 1 \), \( 1 \cdot (-1) = -1 \), \( (-1)(-1) = 1 \) lie in the set; so it is a subgroup by the definition. For \( \nQ_{>0} \): it contains \( 1 \), which is positive (@fd3:prp-ordered-ring-rules (e)). Let \( a, b > 0 \). Then \( b^{-1} > 0 \) by @fd3:prp-reciprocal-order (a). So \( ab^{-1} > 0 \) by (O4), \( \nQ \) being an ordered field (@fd3:thm-rationals-ordered-field).

*(d)* For classes, \( [a] - [b] = [a - b] \) (@thm-quotient-ring-by-ideal (b)). For \( a, b \in \{0, 2, 4\} \), the difference \( a - b \) is one of \( 0, \pm 2, \pm 4 \), and \( [-2] = [4] \), \( [-4] = [2] \) in \( \nZ/6\nZ \) (since \( 6 \mid -2 - 4 \) and \( 6 \mid -4 - 2 \)). So every difference lies in \( \{[0], [2], [4]\} \). For \( \{[1], [3]\} \): \( [3]^{-1} = [3] \), since \( [3][3] = [9] = [1] \), so the four quotients \( [1][1]^{-1} = [1] \), \( [1][3]^{-1} = [3] \), \( [3][1]^{-1} = [3] \), \( [3][3]^{-1} = [1] \) lie in the set.

*(e)* The identity map fixes \( x_0 \), so the set is non-empty. Let \( \sigma \) and \( \tau \) fix \( x_0 \). Applying \( \tau^{-1} \) to \( \tau(x_0) = x_0 \) gives \( x_0 = \tau^{-1}(x_0) \), so \( (\sigma \circ \tau^{-1})(x_0) = \sigma(x_0) = x_0 \). Section 3.4 uses this subgroup for \( X = \{1, \dots, n + 1\} \) and \( x_0 = n + 1 \).

*(f)* \( \nC \) is a field (@fd4:thm-complex-numbers-field), so \( (\nC \setminus \{0\}, \cdot) \) is a group by @exm-groups (b). Recall that \( i^2 = -1 \) (@fd4:prp-reals-embed-complex, with the identification of \( \nR \) inside \( \nC \) made after it).

For \( \{1, i, -1, -i\} \): products of two of \( \pm 1 \) are \( \pm 1 \), products of \( \pm 1 \) with \( \pm i \) are \( \pm i \), and products of two of \( \pm i \) are \( \pm i^2 = \mp 1 \) (signs by @fd3:prp-ring-algebra (c)). So the set is closed under products, and it contains \( 1 \). Each of \( 1 \), \( -1 \) is its own inverse, and \( i(-i) = -i^2 = 1 \), so \( i^{-1} = -i \) and \( (-i)^{-1} = i \). It is a subgroup by the definition.

For \( \nT = \{ u \in \nC : \abs{u} = 1 \} \): by @fd4:prp-unit-circle (a), which rests on the modulus rule \( \abs{zw} = \abs{z}\abs{w} \) of @fd4:thm-conjugate-properties (d), \( 1 \in \nT \), \( uv \in \nT \) for \( u, v \in \nT \), and each \( u \in \nT \) is non-zero with \( u^{-1} = \conj{u} \in \nT \). So \( \nT \subseteq \nC \setminus \{0\} \), and \( \nT \) is a subgroup by the definition.

For \( \mu_n \), the set of \( z \in \nC \) with \( z^n = 1 \) (*Analytic Preliminaries*, Chapter 1's notation, after @fd4:exm-roots-of-unity): \( 0 \notin \mu_n \), since \( 0^n = 0^{n-1} \cdot 0 = 0 \ne 1 \) for \( n \ge 1 \); so \( \mu_n \subseteq \nC \setminus \{0\} \), and there \( z^n \) is the power of @def-group-integer-power, defined by the same recursion. Also \( 1 \in \mu_n \). For \( \zeta, \eta \in \mu_n \), since \( \nC \setminus \{0\} \) is abelian,
\[
(\zeta \eta^{-1})^n = \zeta^n (\eta^{-1})^n = \zeta^n (\eta^n)^{-1} = 1 \cdot 1^{-1} = 1 ,
\]
by @prp-group-power-laws (d) and (b). So \( \zeta\eta^{-1} \in \mu_n \), and \( \mu_n \) is a subgroup by the test. *Analytic Preliminaries*, Chapter 1 also notes that \( \mu_n \subseteq \nT \). Its *Analytic Preliminaries*, Section 1.6, Exercise R2 builds a bijection \( \nZ/n\nZ \to \mu_n \) that sends sums to products; in the words of Section 3.3 this is an isomorphism of groups. That exercise rests on the facts about cosine and sine that *Analytic Preliminaries*, Chapter 1 borrows, and nothing in this chapter cites it.
:::

Now non-examples, each a minimal change of an example. The set \( \nN \subseteq \nZ \) contains \( 0 \) and is closed under \( + \), but \( 0 - 1 = -1 \notin \nN \): the inverses are missing. The odd integers fail more badly: they do not contain \( 0 \), which is even (\( 0 = 2 \cdot 0 \)) and so not odd (@fd3:cor-integers-even-odd (a)). And \( \nZ_{>0} \subseteq \nQ_{>0} \) is non-empty and closed under multiplication, but \( 2^{-1} = 1/2 \notin \nZ \): an integer \( m \) with \( 2m = 1 \) would make \( 1 \) even, and \( 1 = 2 \cdot 0 + 1 \) is odd. Each fails the test at one clause, and each is an infinite set; for a **finite** non-empty subset, closure under products alone suffices (Exercise C1).

Subgroups can be combined. If two subgroups are given, the elements they share form a subgroup again, and so do the elements shared by any family of subgroups:

::: {#prp-subgroup-intersection}
[Intersections of Subgroups]

Let \( G \) be a group and \( (H_i)_{i \in I} \) a family of subgroups of \( G \). Then \( \bigcap_{i \in I} H_i \), taken inside \( G \) (@fd2:def-family-union-intersection (b)), is a subgroup of \( G \).
:::

::: {.proof}
Write \( H \coloneqq \bigcap_{i \in I} H_i \). Since \( e \in G \) and \( e \in H_i \) for every \( i \in I \), \( e \in H \), so \( H \ne \emptyset \). Let \( a, b \in H \). Then \( ab^{-1} \in G \), and for each \( i \in I \), \( a, b \in H_i \), so \( ab^{-1} \in H_i \) by @thm-subgroup-test applied to the subgroup \( H_i \). Hence \( ab^{-1} \in H \), and \( H \) is a subgroup by @thm-subgroup-test. This proves the proposition.
:::

For the empty family the intersection is \( G \) itself, which is a subgroup.

::: {.warning}
A union of two subgroups need not be a subgroup. \( 2\nZ \cup 3\nZ \) contains \( 3 \) and \( 2 \), but not \( 3 - 2 = 1 \): \( 1 \notin 2\nZ \) and \( 1 \notin 3\nZ \), since neither \( 2 \) nor \( 3 \) divides \( 1 \) (@fd3:prp-divisibility-rules-integers (g)). Intersections are safe; unions are not.
:::

## The subgroup generated by one element

Fix \( g \in G \). Which subgroups contain \( g \)? Each of them contains \( gg \), \( ggg \), …, and their inverses, so it contains every power \( g^n \). The powers themselves form a subgroup, and so they are the smallest possible answer.

::: {#def-subgroup-generated-by-element}
[Subgroup Generated by an Element]

Let \( G \) be a group and \( g \in G \). The **subgroup generated by \( g \)** is
\[
\langle g \rangle \coloneqq \{ g^n : n \in \nZ \} ,
\]
with the powers of @def-group-integer-power. In additive notation, \( \langle a \rangle = \{ n \cdot a : n \in \nZ \} \).
:::

In \( (\nZ, +) \), \( \langle n \rangle = \{ k \cdot n : k \in \nZ \} = \{ kn : k \in \nZ \} = n\nZ \), since the group multiple \( k \cdot n \) is the product \( kn \) (@prp-group-power-laws (e)). The name is justified by the next result.

::: {#prp-subgroup-generated-by-element}
[The Subgroup Generated by an Element]

Let \( G \) be a group and \( g \in G \). Then \( \langle g \rangle \) is an abelian subgroup of \( G \) that contains \( g \), and every subgroup of \( G \) that contains \( g \) contains \( \langle g \rangle \).
:::

::: {.idea}
Both halves are the power laws at work. The test asks for \( g^m (g^n)^{-1} \), which the laws turn into the single power \( g^{m-n} \). Conversely, a subgroup containing \( g \) is closed under products and inverses, and every power is built from \( g \) by those two operations.
:::

::: {.proof}
First, \( g = g^1 \in \langle g \rangle \), so \( \langle g \rangle \ne \emptyset \). For \( g^m, g^n \in \langle g \rangle \),
\[
g^m (g^n)^{-1} = g^m g^{-n} = g^{m-n} \in \langle g \rangle ,
\]
by @prp-group-power-laws (b) and (a); so \( \langle g \rangle \) is a subgroup by @thm-subgroup-test. It is abelian: \( g^m g^n = g^{m+n} = g^{n+m} = g^n g^m \), by @prp-group-power-laws (a) and (F1) in \( \nZ \).

Now let \( H \) be a subgroup of \( G \) with \( g \in H \). By @fd1:ax-induction, \( g^n \in H \) for every \( n \in \nN \): \( g^0 = e \in H \), and if \( g^n \in H \), then \( g^{n+1} = g^n g \in H \), since \( H \) is closed under products. For \( n \in \nN \), also \( g^{-n} = (g^n)^{-1} \in H \) (@prp-group-power-laws (b)), since \( H \) is closed under inverses. Every integer is \( n \) or \( -n \) for some \( n \in \nN \) (@fd3:prp-naturals-embed-integers (c)), so \( \langle g \rangle \subseteq H \). This proves the proposition.
:::

So \( \langle g \rangle \) is the smallest subgroup containing \( g \). A group that equals \( \langle g \rangle \) for one of its elements \( g \) is called cyclic; *Groups*, the chapter "Cyclic Groups", studies these groups and the least \( m \ge 1 \) with \( g^m = e \).

**Examples.** If \( g^m = e \) for some \( m \ge 1 \), the subgroup \( \langle g \rangle \) is finite and easy to list. Indeed, divide any \( n \in \nZ \) by \( m \): \( n = qm + r \) with \( 0 \le r < m \) (@fd3:thm-integers-division-remainder (a)). Then
\[
g^n = g^{mq} g^r = (g^m)^q g^r = e^q g^r = g^r ,
\]
by @prp-group-power-laws (a) and (c), and \( e^q = (g^0)^q = g^0 = e \) by (c) again. So \( \langle g \rangle = \{ g^0, g^1, \dots, g^{m-1} \} \).

- In \( (\nZ/6\nZ, +) \), \( k \cdot [2] = [2k] \) for \( k \in \nN \), by @prp-group-power-laws (c) and (e) and @thm-integers-mod-n-ring (d), where (e) identifies the group multiples with the ring multiples to which (d) applies: \( k \cdot (2 \cdot [1]) = (2k) \cdot [1] = [2k] \). So the multiples are \( [0], [2], [4] \), and \( 3 \cdot [2] = [6] = [0] \). By the paragraph above (with \( m = 3 \)), \( \langle [2] \rangle = \{[0], [2], [4]\} \), the subgroup of @exm-subgroups (d).
- In \( (\nZ/7\nZ)^{\times} \), the powers of \( [2] \) are \( [1], [2], [4] \), and \( [2]^3 = [8] = [1] \). So \( \langle [2] \rangle = \{[1], [2], [4]\} \).
- In \( (\nZ/7\nZ)^{\times} \), the powers \( [3]^1, \dots, [3]^6 \) are \( [3], [2], [6], [4], [5], [1] \), each obtained from the one before by multiplying by \( [3] \) (for instance \( [6][3] = [18] = [4] \)). Since \( \nZ/7\nZ \) is a field (@thm-integers-mod-prime-field), \( (\nZ/7\nZ)^{\times} = (\nZ/7\nZ) \setminus \{[0]\} \), as in any field (the paragraph "Why this definition" after @def-ring-unit), so it has the six elements \( [1], \dots, [6] \) (@thm-integers-mod-n-ring (b)), and all of them are powers of \( [3] \): \( \langle [3] \rangle = (\nZ/7\nZ)^{\times} \).

## The subgroups of the integers

Every set \( n\nZ = \langle n \rangle \) is a subgroup of \( (\nZ, +) \). The theorem says that there are no others, and that \( n \) is determined by the subgroup.

::: {#thm-subgroups-of-integers}
[Subgroups of the Integers]

Let \( H \) be a subgroup of \( (\nZ, +) \). Then \( H = n\nZ \) for **exactly one** \( n \in \nN \): \( n = 0 \) if \( H = \{0\} \), and otherwise \( n \) is the least positive element of \( H \).
:::

*Try it first (ten minutes): find the smallest subgroup of \( \nZ \) containing \( 6 \) and \( 15 \). List a few of its elements, guess what it is, and say why its least positive element should divide \( 6 \).*

::: {.idea}
The attempt finds elements by subtracting: \( 15 - 6 = 9 \), \( 9 - 6 = 3 \), and then every multiple of \( 3 \). That suggests "the multiples of \( 3 \)", but listing gives no reason why nothing else can be in the subgroup. The guess also points at the right candidate for \( n \): the **least positive** element, \( 3 \) here. Why should every element be a multiple of it? Divide an element \( a \) by \( n \). The remainder is \( a \) minus a multiple of \( n \), so it lies in the subgroup, and it is smaller than \( n \). It cannot be positive, so it is \( 0 \). This is the move of Section 1.1, **least positive element, then divide**, now with nothing but subtraction available.

*Before reading on: where is \( H \ne \{0\} \) used, and why is the least **positive** element taken, not the least element?*
:::

::: {.proof}
If \( H = \{0\} \), then \( H = 0\nZ \). Suppose \( H \ne \{0\} \), and pick \( a \in H \) with \( a \ne 0 \). Then \( -a \in H \), and one of \( a \), \( -a \) is positive (@fd3:prp-divisibility-rules-integers (h)). So \( H \cap \nZ_{>0} \) is non-empty, and it has the lower bound \( 0 \); by @fd3:prp-integer-least-element it has a least element \( n \), the least positive element of \( H \).

\( (\supseteq) \) Since \( n \in H \) and \( n\nZ = \langle n \rangle \) (@prp-group-power-laws (e)), @prp-subgroup-generated-by-element gives \( n\nZ \subseteq H \).

\( (\subseteq) \) Let \( a \in H \). Since \( n > 0 \), @fd3:thm-integers-division-remainder (a) gives \( q, r \in \nZ \) with \( a = qn + r \) and \( 0 \le r < n \). Here \( qn \in n\nZ \subseteq H \), so \( r = a - qn \in H \), since \( H \) is a subgroup. If \( r > 0 \), then \( r \) is a positive element of \( H \) smaller than \( n \), against the choice of \( n \). So \( r = 0 \), and \( a = qn \in n\nZ \).

Hence \( H = n\nZ \). For uniqueness, let \( n\nZ = m\nZ \) with \( n, m \in \nN \). Then \( n = 1 \cdot n \in m\nZ \), so \( m \mid n \), and in the same way \( n \mid m \); hence \( n = m \) by @fd3:prp-divisibility-rules-integers (f). This proves the theorem.
:::

The answer to the prompt. The hypothesis \( H \ne \{0\} \) is used once, in the first paragraph: it supplies a non-zero element, hence a positive one, so that the set of positive elements of \( H \) is non-empty and has a least element. The least element of \( H \) itself does not exist when \( H \ne \{0\} \): if \( m \) were least, then \( m - n \in H \) and \( m - n < m \). And \( 0 \in H \) is useless as a divisor, since division with remainder needs a positive divisor; the minimality of \( n \) among the **positive** elements is exactly what forces \( r = 0 \).

::: {.remark}
This is the statement of @exr-quotient-rings-c2, an exercise in Section 1.3, promoted to a theorem, and it is the additive half of @thm-integer-ideals-principal (b). In \( \nZ \), being an ideal comes free: every subgroup \( H = n\nZ \) of \( \nZ \) is an ideal (@def-ideal-commutative-ring), since for \( jn \in H \) and \( k \in \nZ \), \( k(jn) = (kj)n \in n\nZ \) by (F5).
:::

The theorem turns questions about subgroups of \( \nZ \) into questions about one number: the least positive element.

::: {.check}
Which \( n \in \nN \) has \( n\nZ = 6\nZ \cap 15\nZ \)?
:::

::: {.solution}
\( n = 30 \). The intersection is a subgroup (@prp-subgroup-intersection), and it contains \( 30 = 5 \cdot 6 = 2 \cdot 15 \ne 0 \), so by @thm-subgroups-of-integers it is \( n\nZ \) with \( n \) its least positive element, the least positive common multiple of \( 6 \) and \( 15 \). The positive multiples of \( 15 \) below \( 30 \) are \( 15 \) alone, and \( 15 = 2 \cdot 6 + 3 \) is not a multiple of \( 6 \) (by the uniqueness of the remainder in @fd3:thm-integers-division-remainder (a)), while \( 30 \) is. So \( n = 30 \).
:::

## Exercises

### A. Check your understanding

::: {#exr-subgroups-a1}
[A1]

These parts are about the proof of @thm-subgroups-of-integers.

::: {.enumerate options="label=(\alph*)"}
1. Where is the minimality of \( n \) used?
2. Run the proof on \( H = 4\nZ + 6\nZ \): find \( n \), and the division of \( 6 \) by \( n \).
3. The conclusion fails for the subset \( \nN \) of \( \nZ \). Which condition of @def-subgroup does \( \nN \) lack, and which step of the proof breaks?
4. State the idea of the proof in two sentences.
:::
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. In the step \( (\subseteq) \): the remainder \( r \) lies in \( H \) and \( 0 \le r < n \), and minimality forbids \( r > 0 \), so \( r = 0 \).
2. \( H \) is a subgroup (@exm-subgroups (b)). Its least positive element is \( n = 2 \): \( 2 = 6 - 4 \in H \), and \( 1 \notin H \), since every element \( 4x + 6y = 2(2x + 3y) \) is even and \( 1 \) is odd (@fd3:cor-integers-even-odd (a)). Dividing \( 6 \) by \( 2 \) gives \( 6 = 3 \cdot 2 + 0 \), with remainder \( 0 \), as the proof predicts. So \( H = 2\nZ \).
3. \( \nN \) lacks inverses: \( 1 \in \nN \), but \( -1 \notin \nN \). The step \( (\supseteq) \) breaks: there \( n = 1 \), and \( n\nZ \subseteq H \) went through \( n\nZ = \langle n \rangle \) and @prp-subgroup-generated-by-element, which needs a subgroup; indeed \( -1 = (-1) \cdot 1 \notin \nN \). The first paragraph's step \( -a \in H \) also fails for \( \nN \) (take \( a = 1 \)), but harmlessly: a non-zero \( a \in \nN \) is already positive, so \( n = 1 \) still exists. The step whose failure breaks the conclusion is \( (\supseteq) \). The other inclusion still holds for \( \nN \): each \( a \in \nN \) is \( a = a \cdot 1 + 0 \), so \( \nN \subseteq 1\nZ = \nZ \).
4. The least positive element \( n \) of \( H \) is the only candidate. Division by \( n \) leaves a remainder in \( H \) smaller than \( n \), so the remainder is \( 0 \) and every element is a multiple of \( n \).
:::
:::

### B. Practice

::: {#exr-subgroups-b1}
[B1: Put the proof in order]

The following lines contain the proof of the direction \( (\Leftarrow) \) of @thm-subgroup-test, shuffled, together with two lines that do not belong. Write the seven correct lines in an order that makes a proof, say which other orders are also admissible, and say why each of the other two lines fails.

(i) For \( a, b \in H \), we know \( b^{-1} \in H \).

(ii) Hence \( H \) is a subgroup of \( G \).

(iii) Choose \( h \in H \).

(iv) Taking \( a = e \) and \( b = h \): \( h^{-1} = eh^{-1} \in H \); so \( e = hh^{-1} \in H \).

(v) Suppose \( H \ne \emptyset \) and \( ab^{-1} \in H \) for all \( a, b \in H \).

(vi) So \( ab = a(b^{-1})^{-1} \in H \), by @thm-group-basic-properties (3).

(vii) For \( b \in H \), taking \( a = e \): \( b^{-1} = eb^{-1} \in H \).

(viii) \( ab \in H \), because \( H \) is closed under products.

(ix) Taking \( a = b = h \): \( e = hh^{-1} \in H \).
:::

::: {.solution}
The admissible order is (v), (iii), (ix), (vii), (i), (vi), (ii). Each line uses the one before it: (iii) uses \( H \ne \emptyset \) from (v); (ix) uses the \( h \) of (iii); (vii) takes \( a = e \), which needs \( e \in H \) from (ix); (i) is (vii) applied to an arbitrary \( b \); (vi) needs \( b^{-1} \in H \) from (i); and (ii) collects \( e \in H \), inverses and products. So no other order is admissible: the dependencies form a single chain.

The distractor (iv) is circular. It takes \( a = e \) in the hypothesis, which is allowed only once \( e \in H \) is known, and then concludes \( e \in H \). Placed before (ix), it uses what it is meant to prove; placed after (ix), its first half is a special case of (vii) and its second half repeats (ix).

The distractor (viii) assumes what is being proved: closure under products is one of the three conditions of @def-subgroup that the direction \( (\Leftarrow) \) must establish, and the hypothesis (v) does not state it.
:::

::: {#exr-subgroups-b2}
[B2: Subgroups of the integers modulo twelve]

Determine which of the following subsets of \( (\nZ/12\nZ, +) \) are subgroups. Justify your answer.

::: {.enumerate options="label=(\alph*)"}
1. \( \{[0], [4], [8]\} \).
2. \( \{[0], [3], [6], [9]\} \).
3. \( \{[0], [5]\} \).
4. \( \{[0], [6]\} \).
:::

Then show that every subgroup of \( \nZ/12\nZ \) that contains \( [5] \) is all of \( \nZ/12\nZ \).
:::

::: {.solution}
We use the additive form of @thm-subgroup-test, with \( [a] - [b] = [a - b] \) (@thm-quotient-ring-by-ideal (b)).

::: {.enumerate options="label=(\alph*)"}
1. A subgroup. For \( a, b \in \{0, 4, 8\} \), \( a - b \in \{0, \pm 4, \pm 8\} \), and \( [-4] = [8] \), \( [-8] = [4] \), since \( 12 \) divides \( -4 - 8 \) and \( -8 - 4 \).
2. A subgroup. For \( a, b \in \{0, 3, 6, 9\} \), \( a - b \in \{0, \pm 3, \pm 6, \pm 9\} \), and \( [-3] = [9] \), \( [-6] = [6] \), \( [-9] = [3] \).
3. Not a subgroup: \( [0] - [5] = [-5] = [7] \), which is not in the set (the remainders \( 7 \), \( 0 \), \( 5 \) are distinct, @thm-integers-mod-n-ring (b)). Equally, \( [5] + [5] = [10] \) is not in the set.
4. A subgroup: \( [6] - [6] = [0] \), \( [0] - [6] = [-6] = [6] \), and the other differences are \( [0] \) and \( [6] \).
:::

Now let \( H \) be a subgroup with \( [5] \in H \). By @prp-subgroup-generated-by-element, \( \langle [5] \rangle \subseteq H \), so \( 5 \cdot [5] \in H \). By @prp-group-power-laws (c) and (e) and @thm-integers-mod-n-ring (d), \( 5 \cdot [5] = 5 \cdot (5 \cdot [1]) = 25 \cdot [1] = [25] = [1] \), since \( 25 = 2 \cdot 12 + 1 \). So \( [1] \in H \), and then \( k \cdot [1] = [k] \in H \) for every \( k \in \nN \) (@prp-subgroup-generated-by-element, @prp-group-power-laws (e) and @thm-integers-mod-n-ring (d) again). Taking \( k = 0, 1, \dots, 11 \) gives every class of \( \nZ/12\nZ \) (@thm-integers-mod-n-ring (b)). Hence \( H = \nZ/12\nZ \).
:::

::: {#exr-subgroups-b3}
[B3: Integer combinations, once more]

Let \( a, b \in \nZ \), not both \( 0 \). Use @thm-subgroups-of-integers to prove that \( a\nZ + b\nZ = d\nZ \), where \( d \) is the least positive element of \( a\nZ + b\nZ \). Compare the proof with the one in Section 1.1.
:::

::: {.solution}
\( a\nZ + b\nZ \) is a subgroup of \( (\nZ, +) \) (@exm-subgroups (b)). It is not \( \{0\} \): it contains \( a = a \cdot 1 + b \cdot 0 \) and \( b = a \cdot 0 + b \cdot 1 \), and one of them is non-zero. So by @thm-subgroups-of-integers, \( a\nZ + b\nZ = n\nZ \) with \( n \) its least positive element, which is \( d \).

This is @thm-integers-bezout (e), whose \( d \) is the same least positive combination. The two proofs are one argument. *Number Systems: From \(\nN\) to \(\nR\)* divided \( a \) and \( b \) by \( d \) and used that the remainder is again a combination; the proof of @thm-subgroups-of-integers divides an arbitrary element of the subgroup by \( n \) and uses only that a subgroup is closed under subtraction. The second form applies to every subgroup of \( \nZ \), not only to sets of combinations.
:::

### C. Going deeper

::: {#exr-subgroups-c1}
[C1: Finite subsets closed under products]

Let \( G \) be a group, and let \( H \subseteq G \) be finite, non-empty and closed under products (\( ab \in H \) for all \( a, b \in H \)). Prove that \( H \) is a subgroup of \( G \). Then explain why \( \nN \subseteq \nZ \), which is non-empty and closed under \( + \) but not a subgroup, does not contradict this.

The first half of a proof is given.

> Let \( h \in H \), and let \( k \coloneqq \card{H} \) (@fd2:def-finite). The powers \( h, h^2, \dots, h^{k+1} \) all lie in \( H \), by induction on the exponent, since \( h^{j+1} = h^j h \).

The last half is blank. *Name the move, then complete it.*
:::

::: {.solution}
The move is **multiply by the inverse**: two equal powers \( h^i = h^j \) become \( e = h^{j-i} \) once \( h^i \) is removed from both sides.

Completion. The map \( \{1, \dots, k+1\} \to H \), \( j \mapsto h^j \), goes from a set with \( k + 1 \) elements to a set with \( k \) elements, so it is not injective (@fd2:cor-pigeonhole-finite-sets (a)): \( h^i = h^j \) for some \( 1 \le i < j \le k + 1 \). Multiplying both sides on the left by \( (h^i)^{-1} = h^{-i} \) gives
\[
e = h^{-i} h^i = h^{-i} h^j = h^{j-i}
\]
(@prp-group-power-laws (b), (a)). Since \( 1 \le j - i \le k \), \( h^{j-i} \) is one of the listed powers, so \( e \in H \). Next, if \( j - i \ge 2 \), then \( h\, h^{j-i-1} = h^{j-i-1} h = h^{j-i} = e \) (@prp-group-power-laws (a)), so \( h^{-1} = h^{j-i-1} \) by @thm-group-basic-properties (2), and \( h^{j-i-1} \in H \) since \( 1 \le j - i - 1 \le k \). If \( j - i = 1 \), then \( h = h^1 = e \), and \( h^{-1} = e \in H \). As \( h \in H \) was arbitrary, \( H \) is closed under inverses; it contains \( e \) and is closed under products, so it is a subgroup by @def-subgroup.

The set \( \nN \) is not finite, so the result does not apply to it. Read backwards, the result even proves this: if \( \nN \) were finite, it would be a subgroup of \( \nZ \), and it is not, since \( -1 \notin \nN \).

**Marking scheme.** (10 points)
- 1: names the move (multiply by the inverse, or cancel \( h^i \)).
- 2: gets \( h^i = h^j \) with \( 1 \le i < j \le k + 1 \) from the pigeonhole principle, cited.
- 2: derives \( h^{j-i} = e \) with the power laws named, and concludes \( e \in H \) from \( 1 \le j - i \le k \).
- 3: shows \( h^{-1} \in H \): \( h^{-1} = h^{j-i-1} \) when \( j - i \ge 2 \), and \( h = e \) when \( j - i = 1 \).
- 1: concludes that \( H \) is a subgroup, by @def-subgroup or @thm-subgroup-test.
- 1: explains that \( \nN \) is infinite, so the result does not apply.
Fatal errors (0 for the step): \( h^0 = e \) taken as one of the listed powers (the list starts at \( h^1 \)); \( h^{-1} \in H \) asserted without exhibiting it as a positive power; the case \( j - i = 1 \) mishandled so that \( h^0 \) is claimed to lie in the list.
:::

::: {#exr-subgroups-c2}
[C2: Exit check: subgroups of the integers]

State and prove @thm-subgroups-of-integers.
:::

::: {.solution}
[Hint 1]

Look at the positive elements of \( H \), and take the least one.
:::

::: {.solution}
[Hint 2]

To show that an element \( a \in H \) is a multiple of that least positive element \( n \), divide \( a \) by \( n \).
:::

::: {.solution}
The statement and proof of @thm-subgroups-of-integers are a complete answer. In outline: \( H = \{0\} = 0\nZ \), or \( H \) has a non-zero element \( a \), and then \( a \) or \( -a \), both in \( H \), is positive; the least positive element \( n \) exists by @fd3:prp-integer-least-element; \( n\nZ \subseteq H \) because \( H \) is a subgroup containing \( n \) (all multiples \( kn \), negative \( k \) included); for \( a \in H \), \( a = qn + r \) with \( 0 \le r < n \) and \( r = a - qn \in H \), so \( r = 0 \) by minimality; and \( n\nZ = m\nZ \) with \( n, m \in \nN \) forces \( n = m \).

**Marking scheme.** (10 points)
- 3: the case \( H = \{0\} \); otherwise the existence of a positive element, with the reason when the chosen element is negative (its inverse lies in \( H \)).
- 1: the least positive element, by a cited well-ordering result for sets of integers bounded below.
- 2: \( n\nZ \subseteq H \) by closure, with the negative multiples included.
- 2: division of \( a \in H \) by \( n \), with the remainder shown to lie in \( H \).
- 1: minimality of \( n \) forces \( r = 0 \).
- 1: uniqueness of \( n \in \nN \).
Fatal errors (0 for the step): assuming that \( H \) is an ideal, or citing @thm-integer-ideals-principal for \( H \) (closure under multiplication by integers is not given; that it comes free is a consequence of the theorem); "the least element of \( H \)" without positivity. A proof by induction showing \( kn \in H \) for \( k \in \nN \), followed by inverses for \( k < 0 \), earns the 2 points for \( n\nZ \subseteq H \). A descent proof (for \( a \in H \) with \( a \ge 0 \), strong induction on \( a \): if \( a \ge n \), then \( a - n \in H \) and \( 0 \le a - n < a \); negative \( a \) handled through \( -a \in H \)) earns the 2 points for division when it shows \( a - n \in H \) and treats negative \( a \), and the 1 point for minimality when it rules out \( 0 < a < n \).
:::

::: {#exr-subgroups-c3}
[C3: Inclusions and intersections]

Let \( m, n \in \nZ_{>0} \).

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( m\nZ \subseteq n\nZ \) if and only if \( n \mid m \).
2. Prove that \( m\nZ \cap n\nZ = L\nZ \), where \( L \) is the least positive common multiple of \( m \) and \( n \). Deduce that \( L \) divides every common multiple of \( m \) and \( n \).
:::
:::

::: {.solution}
[Hint 1]

For (a), ask where \( m \) itself lies. For (b), ask what kind of set the intersection is.
:::

::: {.solution}
[Hint 2]

For (b): \( m\nZ \cap n\nZ \) is a subgroup of \( \nZ \) by @prp-subgroup-intersection, and \( mn \) lies in it.
:::

::: {.solution}
::: {.enumerate options="label=(\alph*)"}
1. \( (\Rightarrow) \) \( m = 1 \cdot m \in m\nZ \subseteq n\nZ \), so \( m = kn \) for some \( k \in \nZ \), that is, \( n \mid m \). \( (\Leftarrow) \) If \( m = kn \), then every \( jm = (jk)n \) lies in \( n\nZ \), by (F5).
2. By @prp-subgroup-intersection, \( m\nZ \cap n\nZ \) is a subgroup of \( (\nZ, +) \). It contains \( mn = n \cdot m = m \cdot n \), which is positive by (O4), so it is not \( \{0\} \). By @thm-subgroups-of-integers it equals \( L\nZ \), with \( L \) its least positive element. Its elements are exactly the common multiples of \( m \) and \( n \), so \( L \) is the least positive common multiple. A common multiple \( c \) lies in \( m\nZ \cap n\nZ = L\nZ \), so \( L \mid c \).
:::

This is @exr-unique-factorization-b2, there proved by dividing \( c \) by \( L \) directly; here the division is done once and for all inside @thm-subgroups-of-integers.

**Marking scheme.** (10 points)
- 2: (a) \( (\Rightarrow) \) uses \( m \in m\nZ \) to get \( m = kn \).
- 1: (a) \( (\Leftarrow) \) shows \( jm = (jk)n \in n\nZ \).
- 2: (b) the intersection is a subgroup of \( (\nZ, +) \), by @prp-subgroup-intersection.
- 2: (b) it is not \( \{0\} \) (\( mn \) is a positive element), so @thm-subgroups-of-integers gives \( L\nZ \) with \( L \) its least positive element.
- 2: (b) identifies the intersection with the set of common multiples, so \( L \) is the least positive common multiple.
- 1: (b) deduces \( L \mid c \) for every common multiple \( c \).
Fatal errors (0 for the step): (b) applies @thm-subgroups-of-integers without checking that the intersection is a subgroup; (b) assumes \( L = mn \) or \( L = mn/\gcd(m, n) \) without proof.
:::

<!-- dependency ledger
def-subgroup (claim): (opening) F5.1 answered the question for ideals | thm-integer-ideals-principal (cited)
def-subgroup (claim): H is a group with the restricted operation; its identity and inverses are those of G | inline (G1)-(G3) restricted; thm-group-basic-properties (1), (2) (cited)
exm-subgroups (solution): (a) G is non-empty and closed under a b^{-1} | def-group (cited implicitly through "binary operation"), used silently
exm-subgroups (solution): (d) 6 | -2 - 4, 6 | -4 - 2; [3][3] = [9] = [1] in Z/8Z | numerals; verify/ch03/exm-subgroups.py; class test of F5.1 §04 (thm-quotient-ring-by-ideal (a), (d)), used silently
exm-subgroups (solution): (f) i^2 = -1; signs of products of +-1, +-i | def-complex-numbers, prp-reals-embed-complex (F4.1, cited; example only); fd3:prp-ring-algebra (c) in the field C; verify/ch03/exm-subgroups.py
exm-subgroups (solution): (f) z^n in C (*Analytic Preliminaries*, Chapter 1's ring power) is the group power of def-group-integer-power on C \ {0} | same recursion z^0 = 1, z^{k+1} = z^k z; uniqueness in fd2:thm-recursion, used silently; 0^n = 0 for n >= 1 by the recursion and fd3:prp-ring-algebra (b)
exm-subgroups (claim): (f) mu_n subset of T; *Analytic Preliminaries*, Section 1.6 Exercise R2 is an isomorphism | F4.1 blueprint ch01.md (F4.1 §06 B3, R2; prose, no claim rests on them)
exm-subgroups (claim): (e) reused in Section 3.4 | F5.3 §04 lem-permutations-fixing-last-point (prose pointer within the chapter)
exm-subgroups (claim): (non-examples) 0 - 1 = -1 not in N; 1/2 not in Z | fd3:thm-integers-ordered-ring (b) (N = {x >= 0}) and -1 < 0, used silently; 2m = 1 in Q gives 2m = 1 in Z by the identification of F3.11 §01 (fd3:prp-integers-embed-rationals), used silently; fd3:cor-integers-even-odd (a) (cited)
exm-subgroups (solution): (c) b > 0 gives b^{-1} > 0 | fd3:prp-reciprocal-order (a) (cited), Q an ordered field by fd3:thm-rationals-ordered-field
exm-subgroups (claim): (non-examples) Z_{>0} non-empty and closed under multiplication | (O4) of fd3:thm-integers-ordered-ring, used silently; 1 > 0 by fd3:prp-ordered-ring-rules (e)
exm-subgroups (claim): (non-examples) finite non-empty subsets closed under products are subgroups | exr-subgroups-c1 (pointer to an exercise; nothing rests on it)
prp-subgroup-intersection (claim): the intersection over the empty family, taken inside G, is G | fd2:def-family-union-intersection (b) (cited), vacuous quantifier
prp-subgroup-intersection (proof): e in G, ab^{-1} in G for membership in the intersection taken inside G | def-group (binary operation, (G2)), used silently
def-subgroup-generated-by-element (claim): <n> = nZ in Z | prp-group-power-laws (e) (cited) with def-integer-linear-combinations
prp-subgroup-generated-by-element (claim): (remark) cyclic groups in Groups, the chapter "Cyclic Groups" | AL1.2 (prose pointer); nothing depends on it
prp-subgroup-generated-by-element (claim): (examples) powers of [2] in Z/6Z and of [2], [3] in (Z/7Z)^x; 18 = 2*7 + 4 | numerals; verify/ch03/prp-subgroup-generated-by-element.py
prp-subgroup-generated-by-element (claim): (examples) k . [2] = [2k] and 5 . [5] = [1]: group multiples equal ring multiples | prp-group-power-laws (e) (cited) with thm-integers-mod-n-ring (d) (cited); also in exr-subgroups-b2
prp-subgroup-generated-by-element (claim): (examples) (Z/7Z)^x = (Z/7Z) \ {[0]} | thm-integers-mod-prime-field (cited); def-ring-unit and its paragraph 'Why this definition' (cited; 0 is never a unit when 1 != 0, fd3:prp-ring-algebra (b))
prp-subgroup-generated-by-element (claim): (examples) n = qm + r gives mq + r and g^{mq} = (g^m)^q | prp-group-power-laws (a), (c) (cited); ring arithmetic in Z
thm-subgroups-of-integers (proof): -a in H; r = a - qn in H; 1 . n = n; n Z = m Z gives n | m | subgroup axioms in additive notation; fd2:def-divides read on the constructed Z (as in fd3 Ch 3), used silently
thm-subgroups-of-integers (claim): (try it first, idea) 15 - 6 = 9, 9 - 6 = 3; the smallest subgroup containing 6 and 15 is 3Z | numerals; verify/ch03/thm-subgroups-of-integers.py
thm-subgroups-of-integers (claim): (answer to prompt) m - n < m for n > 0 | fd3:prp-ordered-ring-rules (a), used silently
thm-subgroups-of-integers (claim): (remark) statement of exr-quotient-rings-c2; additive half of thm-integer-ideals-principal (b); every subgroup of Z is an ideal | meta-claim checked against F5.1 §03 C2 (same statement) and the theorem's (b); k(jn) = (kj)n by (F5)
thm-subgroups-of-integers (claim): (check) 30 = 5*6 = 2*15, 15 = 2*6 + 3; only 15 is a positive multiple of 15 below 30 | numerals; discreteness fd3:thm-integers-ordered-ring (c), used silently; verify/ch03/thm-subgroups-of-integers.py
exr-subgroups-a1 (solution): 4x + 6y = 2(2x + 3y); 6 = 3*2 + 0 | ring arithmetic; verify/ch03/exr-subgroups-a1.py
exr-subgroups-a1 (solution): (c) a non-zero a in N is positive | fd3:thm-integers-ordered-ring (b) (N = {x >= 0}), used silently
exr-subgroups-b1 (solution): the dependency chain of the seven lines | the solution's own analysis
exr-subgroups-b2 (solution): differences mod 12; 25 = 2*12 + 1 | numerals; verify/ch03/exr-subgroups-b2.py
exr-subgroups-b3 (solution): comparison with the proof of thm-integers-bezout | meta-claim checked against F5.1 §01 (proof of (b) divides a and b by d; (e) from (b))
exr-subgroups-c1 (solution): {1, ..., k + 1} has k + 1 elements | fd2:def-finite with the identity bijection, read on omega (F3.1 §04 citing rule, group (i))
exr-subgroups-c3 (solution): mn > 0 by (O4); comparison with exr-unique-factorization-b2 | fd3:thm-integers-ordered-ring (cited through (O4)); meta-claim checked against F5.1 §02 B2 (divides c by L)
-->
