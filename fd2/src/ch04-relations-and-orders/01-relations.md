# Properties of Relations

Chapter 1 made relations into sets: a relation on a set \( X \) is a subset \( R \subseteq X \times X \), and \( x \mathrel{R} y \) means \( (x, y) \in R \) (@def-relation). It named the properties that make a relation an order or an equivalence and left them to this chapter. Equality, \( \le \), inclusion \( \subseteq \), divisibility \( \mid \), and "leaves the same remainder on division by \( 3 \)" are all relations, and they behave alike in some ways and differently in others. This section names four properties that sort them, proves the ones that divisibility has, and collects witnesses for every failure. Each property is decided by the same method: a proof for all elements when it holds, one witness when it fails. Sections 4.2 and 4.3 then study the two combinations that matter most.

## Four properties

Start from equality. Every \( x \) equals itself; if \( x = y \), then \( y = x \); and if \( x = y \) and \( y = z \), then \( x = z \). The relation \( \le \) on \( \nR \) keeps the first and third of these and loses the second, but it has a substitute: \( x \le y \) and \( y \le x \) together force \( x = y \). Each of these is a property a relation may or may not have.

*Each property is one rule for what the relation must contain, given what it already contains.*

::: {#def-relation-properties}
[Properties of a Relation]

Let \( X \) be a set and \( R \) a relation on \( X \). Then \( R \) is

- **reflexive on \( X \)** if \( x \mathrel{R} x \) for **every** \( x \in X \):
\[
\forall x \in X \ \ x \mathrel{R} x ;
\]
- **symmetric** if \( x \mathrel{R} y \) implies \( y \mathrel{R} x \), for all \( x, y \in X \):
\[
\forall x \in X \ \forall y \in X \ \ \bigl( x \mathrel{R} y \to y \mathrel{R} x \bigr) ;
\]
- **antisymmetric** if \( x \mathrel{R} y \) and \( y \mathrel{R} x \) together imply \( x = y \), for all \( x, y \in X \):
\[
\forall x \in X \ \forall y \in X \ \ \bigl( (x \mathrel{R} y \wedge y \mathrel{R} x) \to x = y \bigr) ;
\]
- **transitive** if \( x \mathrel{R} y \) and \( y \mathrel{R} z \) together imply \( x \mathrel{R} z \), for all \( x, y, z \in X \):
\[
\forall x \in X \ \forall y \in X \ \forall z \in X \ \ \bigl( (x \mathrel{R} y \wedge y \mathrel{R} z) \to x \mathrel{R} z \bigr) .
\]
:::

In words: reflexive says every element is related to itself. Symmetric says the relation can be read backwards: whenever it relates \( x \) to \( y \), it also relates \( y \) to \( x \). Antisymmetric says it can be read both ways only between an element and itself. Transitive says two steps can always be replaced by one.

Three of the four are implications, so a relation has them unless some related pair (or triple) makes the conclusion false: for symmetry and transitivity a pair is missing from \( R \), and for antisymmetry two different elements are related both ways. Negating with @fd1:prp-bounded-quantifier-negation and @fd1:prp-negated-implication turns each failure into a **witness**:
\[
\begin{aligned}
\text{not reflexive:} \quad & \exists x \in X \ \ \neg (x \mathrel{R} x) , \\
\text{not symmetric:} \quad & \exists x \in X \ \exists y \in X \ \ \bigl( x \mathrel{R} y \wedge \neg (y \mathrel{R} x) \bigr) , \\
\text{not antisymmetric:} \quad & \exists x \in X \ \exists y \in X \ \ \bigl( (x \mathrel{R} y \wedge y \mathrel{R} x) \wedge x \ne y \bigr) , \\
\text{not transitive:} \quad & \exists x \in X \ \exists y \in X \ \exists z \in X \ \ \bigl( (x \mathrel{R} y \wedge y \mathrel{R} z) \wedge \neg (x \mathrel{R} z) \bigr) .
\end{aligned}
\]
So "not symmetric" is shown by **one** pair related in one direction only, and "not transitive" by one triple. A single witness settles a failure; a success needs an argument for all elements.

**Reading a relation as a picture.** Draw the elements of \( X \) as points and an arrow from \( x \) to \( y \) whenever \( x \mathrel{R} y \). The relation \( \le \) on \( \{1, 2, 3\} \) is \( \{ (1, 1), (2, 2), (3, 3), (1, 2), (1, 3), (2, 3) \} \):

\begin{center}
\begin{tikzpicture}[scale=1.0, every node/.style={circle, draw, inner sep=2pt, minimum size=16pt}]
  \node (a) at (0,0) {$1$};
  \node (b) at (2.4,0) {$2$};
  \node (c) at (4.8,0) {$3$};
  \draw[->, thick] (a) to[loop above] (a);
  \draw[->, thick] (b) to[loop above] (b);
  \draw[->, thick] (c) to[loop above] (c);
  \draw[->, thick] (a) -- (b);
  \draw[->, thick] (b) -- (c);
  \draw[->, thick] (a) to[bend right=35] (c);
\end{tikzpicture}
\end{center}

Reflexive means a loop at every point. Symmetric means every arrow has a return arrow. Antisymmetric means no two **different** points are joined in both directions. Transitive means every path of two arrows has a direct arrow from its start to its end. In the picture there are loops everywhere, no return arrows, and the two-arrow path \( 1 \to 2 \to 3 \) has its shortcut \( 1 \to 3 \); so \( \le \) on \( \{1, 2, 3\} \) is reflexive, antisymmetric and transitive, and not symmetric, with witness the pair \( (1, 2) \). A path may also return to its start: \( x \to y \to x \). Transitivity then demands the loop at \( x \). That case is the source of the warning below.

**Why "reflexive on \( X \)".** The other three properties mention elements only when they are related, so they depend on the set \( R \) alone. Reflexivity depends on \( X \) too. The relation \( \{(0, 0)\} \) is reflexive on \( \{0\} \), and the same set of pairs, viewed as a relation on \( \{0, 1\} \), is not reflexive on \( \{0, 1\} \), with witness \( 1 \). That is why the definition names the set.

## Prove or disprove, property by property

A relation given by a formula has each property or not, and nothing tells us in advance which. So the first step is to test small elements and guess; the second is a proof if the guess is "yes", and a witness, checked clause by clause, if it is "no".

::: {#exm-checking-a-relation}
[Deciding four properties]

On \( \nZ \), let \( x \mathrel{R} y \) mean \( 7 \mid 3x + 4y \). Decide which of the four properties of @def-relation-properties \( R \) has.
:::

::: {.idea}
[Scratch work]

Test small elements first. \( 1 \mathrel{R} 1 \), since \( 3 + 4 = 7 \). Also \( 0 \mathrel{R} 7 \) (\( 0 + 28 = 28 \)) and \( 7 \mathrel{R} 0 \) (\( 21 + 0 = 21 \)), with \( 0 \ne 7 \): antisymmetry fails, and the pair \( 0, 7 \) is the witness. Reflexivity looks true in general: \( 3x + 4x = 7x \). Symmetry is the one to plan, since the coefficients swap places.

| Givens | Goal |
|---|---|
| \( x \mathrel{R} y \) | \( y \mathrel{R} x \) |
| \( 3x + 4y = 7k \), with \( k \in \nZ \) | \( 3y + 4x = 7m \) for some \( m \in \nZ \): find \( m \) |
| \( 3x + 4y = 7k \) | \( (3y + 4x) + (3x + 4y) = 7x + 7y \), so \( 3y + 4x = 7(x + y - k) \): try \( m = x + y - k \) |

The last row closes the gap: the two expressions add up to a multiple of \( 7 \), because \( 3 + 4 = 7 \). Transitivity goes the same way: adding the givens \( 3x + 4y = 7k \) and \( 3y + 4z = 7l \) gives \( 3x + 7y + 4z \), and the middle term is a multiple of \( 7 \).
:::

::: {.solution}
*Reflexive.* For \( x \in \nZ \), \( 3x + 4x = 7x \) with \( x \in \nZ \), so \( 7 \mid 3x + 4x \).

*Symmetric.* Let \( x \mathrel{R} y \), say \( 3x + 4y = 7k \) with \( k \in \nZ \). Then \( 3y + 4x = 7(x + y) - (3x + 4y) = 7(x + y - k) \), and \( x + y - k \in \nZ \) by @prp-integers-closed (a), so \( y \mathrel{R} x \).

*Transitive.* Let \( x \mathrel{R} y \) and \( y \mathrel{R} z \), say \( 3x + 4y = 7k \) and \( 3y + 4z = 7l \) with \( k, l \in \nZ \). Adding, \( 3x + 7y + 4z = 7(k + l) \), so \( 3x + 4z = 7(k + l - y) \), with \( k + l - y \in \nZ \) (@prp-integers-closed (a)), and \( x \mathrel{R} z \).

*Not antisymmetric.* \( 3 \cdot 0 + 4 \cdot 7 = 28 = 7 \cdot 4 \) and \( 3 \cdot 7 + 4 \cdot 0 = 21 = 7 \cdot 3 \), so \( 0 \mathrel{R} 7 \) and \( 7 \mathrel{R} 0 \), while \( 0 \ne 7 \).

| reflexive | symmetric | antisymmetric | transitive |
|---|---|---|---|
| yes | yes | no: \( 0, 7 \) | yes |
:::

Three verdicts needed a proof about all integers, and one needed a single pair: that asymmetry of effort is the method.

::: {#exm-method-relation-properties}
[Method: proving or disproving a property of a relation]

**Template.** To prove a property, write it as the "for all" it is (@def-relation-properties), take arbitrary elements satisfying its hypothesis, unwind the relation's definition and rewind the conclusion (@exm-method-direct-proof). To disprove it, exhibit one witness of the negated form and check each clause (@exm-method-counterexample). Record the verdicts in a table, each "no" with its witness.

**When to use it.** A relation is given by a formula, a list or a picture, and the question is which properties it has: whether it is an equivalence relation, or a partial order.

**The usual failure.** "Proving" a property from one example; refuting antisymmetry with a pair related one way only, which refutes symmetry instead; a witness for "not reflexive" that is not in \( X \).
:::

::: {.check}
On \( \nZ \), let \( x \mathrel{S} y \) mean \( 7 \mid 3x + 5y \). Is \( S \) reflexive? Is it symmetric?
:::

::: {.solution}
Neither. Not reflexive: \( 1 \mathrel{S} 1 \) would need \( 7 \mid 8 \), and \( 8 = 7k \) fails for every integer \( k \): if \( k \le 1 \), then \( 7k \le 7 \); if \( k > 1 \), then \( k \ge 2 \) by @prp-integers-closed (c), and \( 7k \ge 14 \). Not symmetric: \( 1 \mathrel{S} 5 \), since \( 3 + 25 = 28 = 7 \cdot 4 \), but \( 5 \mathrel{S} 1 \) fails, since \( 15 + 5 = 20 \) and \( 14 < 20 < 21 \), and no multiple of \( 7 \) lies strictly between \( 7 \cdot 2 \) and \( 7 \cdot 3 \), as no integer lies strictly between \( 2 \) and \( 3 \) (@prp-integers-closed (c)). With \( 3 + 5 = 8 \), the coefficients no longer add up to a multiple of \( 7 \), and the trick of the scratch work is gone.
:::

## Divisibility

Divisibility shows that the same rule can give an antisymmetric relation on one set and not on a larger one, because the larger set brings in more pairs: \( \mid \) on \( \nZ \) contains both \( (2, -2) \) and \( (-2, 2) \), which \( \mid \) on \( \nN \) does not. Recall @def-divides: for integers \( a, b \), \( a \mid b \) means \( b = ka \) for some \( k \in \nZ \).

::: {#prp-divides-partial-order}
[Divisibility on the Natural Numbers]

The relation \( \mid \) is reflexive, antisymmetric and transitive on \( \nN \). On \( \nZ \) it is reflexive and transitive, and **not** antisymmetric.
:::

::: {.idea}
Reflexivity and transitivity are one line each from @def-divides. For antisymmetry, \( b = ka \) and \( a = lb \) give \( a = lka \). If \( a \ne 0 \), this forces \( kl = 1 \), and for **positive** integers that means \( k = l = 1 \). On \( \nN \) the multipliers are positive, so \( b = a \); on \( \nZ \) they may both be \( -1 \). (The method of @exm-method-relation-properties: three proofs for \( \nN \) and one witness for \( \nZ \).)
:::

::: {.proof}
*Reflexive.* For every integer \( a \), \( a = 1 \cdot a \), so \( a \mid a \).

*Transitive.* This is @prp-divides-transitive.

These two arguments work for all integers, so on \( \nN \) and on \( \nZ \).

*Antisymmetric on \( \nN \).* Let \( a, b \in \nN \) with \( a \mid b \) and \( b \mid a \), say \( b = ka \) and \( a = lb \) with \( k, l \in \nZ \).

*Case 1:* \( a = 0 \) or \( b = 0 \). If \( a = 0 \), then \( b = k \cdot 0 = 0 \); if \( b = 0 \), then \( a = l \cdot 0 = 0 \). Either way \( a = b \).

*Case 2:* \( a \ne 0 \) and \( b \ne 0 \). By @lem-naturals-arithmetic (a), \( a \ge 1 \) and \( b \ge 1 \), so both are positive. Since \( ka = b > 0 \) and \( a > 0 \), we have \( k > 0 \) (if \( k \le 0 \), then \( ka \le 0 \)); likewise \( l > 0 \). By @prp-integers-closed (b), \( k, l \in \nZ_{>0} = \{ n \in \nN : n \ge 1 \} \), so \( k \ge 1 \) and \( l \ge 1 \). Now \( a = lb = lka \), and \( a \ne 0 \), so \( kl = 1 \). If \( k > 1 \), then multiplying by \( l > 0 \) gives \( kl > l \ge 1 \), contradicting \( kl = 1 \). So \( k \le 1 \), hence \( k = 1 \), and \( b = a \).

*Not antisymmetric on \( \nZ \).* \( -2 = (-1) \cdot 2 \) and \( 2 = (-1) \cdot (-2) \), so \( 2 \mid -2 \) and \( -2 \mid 2 \), but \( 2 \ne -2 \).
:::

The failure on \( \nZ \) is a non-example by minimal change: enlarging the set from \( \nN \) to \( \nZ \) keeps reflexivity and transitivity, and antisymmetry fails exactly because an integer and its negative divide each other. Two facts about \( (\nN, \mid) \) will matter in Section 4.3: every \( a \in \nN \) divides \( 0 \), since \( 0 = 0 \cdot a \), and \( 1 \) divides every \( a \), since \( a = a \cdot 1 \). In the divisibility relation, \( 0 \) sits above everything and \( 1 \) below everything.

## A table of examples

Here are eight relations checked against the four properties. Each "no" comes with its witness, which is how a failure is proved; each "yes" is a one-line argument given after the table. The table is the method of @exm-method-relation-properties run eight times: thirty-two verdicts, nine of them refuted by a witness.

::: {#exm-relation-table}
[Eight relations, four properties]

Decide which of the four properties each relation has: \( = \), \( \le \) and \( < \) on \( \nR \); \( \subseteq \) on \( \powerset{X} \) for a set \( X \) with at least one element; \( \mid \) on \( \nN \) and on \( \nZ \); "\( x - y \in \nZ \)" on \( \nR \); and the empty relation \( \emptyset \) on a set \( X \) with at least one element.
:::

::: {.solution}
| Relation | reflexive | symmetric | antisymmetric | transitive |
|---|---|---|---|---|
| \( = \) on \( \nR \) | yes | yes | yes | yes |
| \( \le \) on \( \nR \) | yes | no: \( 0, 1 \) | yes | yes |
| \( < \) on \( \nR \) | no: \( 0 \) | no: \( 0, 1 \) | yes | yes |
| \( \subseteq \) on \( \powerset{X} \) | yes | no: \( \emptyset, X \) | yes | yes |
| \( \mid \) on \( \nN \) | yes | no: \( 1, 2 \) | yes | yes |
| \( \mid \) on \( \nZ \) | yes | no: \( 1, 2 \) | no: \( 2, -2 \) | yes |
| \( x - y \in \nZ \) on \( \nR \) | yes | yes | no: \( 0, 1 \) | yes |
| \( \emptyset \) on \( X \) | no: any \( x \) | yes | yes | yes |

The witnesses. \( 0 \le 1 \) and not \( 1 \le 0 \); \( 0 < 1 \) and not \( 1 < 0 \); not \( 0 < 0 \). \( \emptyset \subseteq X \), since the empty set is a subset of every set (Section 1.2, after @prp-empty-set-unique), and \( X \not\subseteq \emptyset \), since \( X \) has an element and \( \emptyset \) has none. \( 1 \mid 2 \), and \( 2 \nmid 1 \): \( 1 = 2k \) would give \( 0 < k < 1 \), and no integer lies there (@prp-integers-closed (c)). The pair \( 2, -2 \) is from @prp-divides-partial-order. For \( x - y \in \nZ \): \( 0 - 1 = -1 \) and \( 1 - 0 = 1 \) are integers, and \( 0 \ne 1 \). For \( \emptyset \): no \( x \) has \( (x, x) \in \emptyset \).

The "yes" entries. Equality is reflexive by \( \rulename{{=}I} \) (@fd1:def-rules-equality), symmetric and transitive by @fd1:prp-equality-symmetric-transitive, and antisymmetric because its conclusion \( x = y \) is one of its hypotheses. For \( \le \) and \( < \), antisymmetry and transitivity are order facts about \( \nR \), and \( \le \) is reflexive because \( x = x \) gives \( x \le x \); for \( < \), antisymmetry holds **vacuously**, since \( x < y \) and \( y < x \) never hold together. For \( \subseteq \), reflexivity is immediate from @def-subset, transitivity is @prp-subset-transitive, and antisymmetry is @prp-subset-antisymmetric. For \( \mid \), see @prp-divides-partial-order. For \( x - y \in \nZ \): \( x - x = 0 \in \nZ \); \( y - x = -(x - y) \); and \( x - z = (x - y) + (y - z) \); these are integers by @prp-integers-closed (a). The empty relation is symmetric, antisymmetric and transitive vacuously: each property is an implication whose hypothesis requires a pair in \( \emptyset \).
:::

Three degenerate cases are worth a sentence each, because each shows a property holding for a reason other than the one we expect.

- The **empty relation** on a non-empty \( X \) has every property except reflexivity, all vacuously. It is the standard witness that the three implication properties do not imply reflexivity.
- The **full relation** \( X \times X \) relates everything to everything. It is reflexive, symmetric and transitive; it is antisymmetric only if \( X \) has at most one element.
- If \( X = \emptyset \), then \( \powerset{X} = \{\emptyset\} \), and \( \subseteq \) on it is \( \{(\emptyset, \emptyset)\} \): with only one element, it is **symmetric**. The non-emptiness of \( X \) in the table is what the witness \( \emptyset, X \) needs.

::: {.check}
On the set \( \{2, 3, 4, \dots\} \) of integers \( \ge 2 \), let \( x \mathrel{C} y \) mean "\( x \) and \( y \) have a common prime factor", that is, some prime \( p \) divides both. Which of the four properties does \( C \) have?
:::

::: {.solution}
Reflexive: every integer \( x \ge 2 \) has a prime factor \( p \) (@thm-prime-factor), and \( p \) divides \( x \) and \( x \). Symmetric: the condition "\( p \mid x \) and \( p \mid y \)" does not depend on the order of \( x \) and \( y \). Not antisymmetric: \( 2 \mathrel{C} 4 \) and \( 4 \mathrel{C} 2 \) (both divisible by \( 2 \)), and \( 2 \ne 4 \). Not transitive: \( 2 \mathrel{C} 6 \) (common factor \( 2 \)) and \( 6 \mathrel{C} 3 \) (common factor \( 3 \)), but \( 2 \) and \( 3 \) have no common prime factor, since \( 2 \) is prime (Section 1.1, after @def-prime), so a prime dividing \( 2 \), being a positive divisor of \( 2 \) other than \( 1 \), is \( 2 \); and \( 2 \nmid 3 \): \( 3 = 2k \) would give \( 1 < k < 2 \), and no integer lies there (@prp-integers-closed (c)). Sharing a factor with a middle element does not pass along, because the shared factor may change.
:::

::: {.warning}
**A false theorem: "symmetric and transitive imply reflexive."** The "proof": let \( x \in X \), and take \( y \) with \( x \mathrel{R} y \); by symmetry \( y \mathrel{R} x \), and by transitivity \( x \mathrel{R} x \). The conclusion is false: the empty relation on \( \{1\} \) is symmetric and transitive (vacuously) and not reflexive, with witness \( 1 \). The illegal step, "take \( y \) with \( x \mathrel{R} y \)", is an \( \rulename{\exists E} \) (@fd1:def-rules-existential) on \( \exists y \in X \ x \mathrel{R} y \), which was never derived and need not be true: (N9) of @fd1:exm-not-allowed-catalogue (Exercise C2 gives the correct version).
:::

::: {.remark}
"Antisymmetric" is not "not symmetric". Equality is both symmetric and antisymmetric. And \( \{ (1, 2), (2, 1), (2, 3) \} \) on \( \{1, 2, 3\} \) is neither: it is not symmetric, since \( 2 \mathrel{R} 3 \) and not \( 3 \mathrel{R} 2 \); and it is not antisymmetric, since \( 1 \mathrel{R} 2 \), \( 2 \mathrel{R} 1 \) and \( 1 \ne 2 \).
:::

Two combinations of the properties organize the rest of the chapter. A relation that is reflexive, symmetric and transitive behaves like equality; Section 4.2 calls it an **equivalence relation** and shows that it cuts \( X \) into classes. A relation that is reflexive, antisymmetric and transitive behaves like \( \le \); Section 4.3 calls it a **partial order**; inclusion on \( \powerset{X} \) and divisibility on \( \nN \) are examples that are not comparisons of sizes.

## Exercises

### A. Check your understanding

::: {#exr-relations-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. State in symbols what it means for a relation \( R \) on \( X \) to be antisymmetric, and write its negation in symbols.
2. True or false, with a witness: every antisymmetric relation fails to be symmetric.
3. Which of the four properties does the relation "\( \abs{x - y} \le 1 \)" have on \( \nR \)?
4. Let \( X = \{p, q\} \) with \( p \ne q \). How many relations on \( X \) are reflexive on \( X \)?
5. To show that a relation is **not** transitive, what must you produce? To show that it **is**, what do you assume?
:::
:::

::: {.solution}
(a) \( \forall x \in X \ \forall y \in X \ ((x \mathrel{R} y \wedge y \mathrel{R} x) \to x = y) \). Its negation, by @fd1:prp-bounded-quantifier-negation and @fd1:prp-negated-implication: \( \exists x \in X \ \exists y \in X \ ((x \mathrel{R} y \wedge y \mathrel{R} x) \wedge x \ne y) \).

(b) False. Equality on any set is antisymmetric and symmetric. So is the empty relation (vacuously).

(c) Reflexive: \( \abs{x - x} = 0 \le 1 \). Symmetric: \( \abs{y - x} = \abs{x - y} \). Not antisymmetric: \( \abs{0 - 1} \le 1 \) both ways and \( 0 \ne 1 \). Not transitive: \( \abs{0 - 1} \le 1 \) and \( \abs{1 - 2} \le 1 \), but \( \abs{0 - 2} = 2 > 1 \). "Close to" does not pass along a chain, because small differences add up.

(d) Four. A reflexive relation must contain \( (p, p) \) and \( (q, q) \). The other two pairs of \( X \times X \), \( (p, q) \) and \( (q, p) \), may each be in or out, independently, which gives \( 2 \cdot 2 = 4 \) relations: \( \{(p, p), (q, q)\} \) together with one of \( \emptyset \), \( \{(p, q)\} \), \( \{(q, p)\} \), \( \{(p, q), (q, p)\} \).

(e) Elements \( x, y, z \) (not necessarily distinct) with \( x \mathrel{R} y \), \( y \mathrel{R} z \) and not \( x \mathrel{R} z \) (the witness form of @def-relation-properties). To show transitivity, assume arbitrary \( x, y, z \in X \) with \( x \mathrel{R} y \) and \( y \mathrel{R} z \), and derive \( x \mathrel{R} z \) (@exm-method-relation-properties).
:::

### B. Practice

::: {#exr-relations-b1}
[B1: Five relations]

For each relation, determine which of the four properties it has. Justify your answer, with a witness for each failure.

::: {.enumerate options="label=(\alph*)"}
1. On \( \nN \times \nN \): \( (a, b) \mathrel{E} (c, d) \) if and only if \( a + d = b + c \).
2. On \( \nR \): \( x \mathrel{S} y \) if and only if \( x^2 = y^2 \).
3. On the set \( \nR^{\nR} \) of functions \( \nR \to \nR \): \( f \mathrel{L} g \) if and only if \( f(x) \le g(x) \) for every \( x \in \nR \).
4. On \( \nR \): \( x \mathrel{P} y \) if and only if \( xy > 0 \).
5. On \( \nZ \): \( x \mathrel{N} y \) if and only if \( y = x + 1 \).
:::
:::

::: {.solution}
(a) Reflexive: \( a + b = b + a \). Symmetric: \( a + d = b + c \) gives \( c + b = d + a \). Transitive: from \( a + d = b + c \) and \( c + f = d + e \), adding gives \( a + d + c + f = b + c + d + e \), and canceling \( c + d \) gives \( a + f = b + e \). Not antisymmetric: \( (0, 0) \mathrel{E} (1, 1) \) both ways, and \( (0, 0) \ne (1, 1) \). (The pairs \( (a, b) \) and \( (c, d) \) are related exactly when \( a - b = c - d \); *Number Systems: From \(\nN\) to \(\nR\)*, Chapter 2 builds \( \nZ \) from the classes of this relation.)

(b) Reflexive, symmetric and transitive, because "\( x^2 = y^2 \)" is equality of the values \( x^2 \) and \( y^2 \), and equality has those three properties. Not antisymmetric: \( 1^2 = (-1)^2 \) and \( 1 \ne -1 \).

(c) Reflexive: \( f(x) \le f(x) \). Transitive: \( f(x) \le g(x) \le h(x) \) at each \( x \). Antisymmetric: if \( f \mathrel{L} g \) and \( g \mathrel{L} f \), then \( f(x) = g(x) \) for every \( x \), and \( f = g \) by @prp-function-equality (same domain and codomain). Not symmetric: the constant functions \( 0 \) and \( 1 \) satisfy \( 0 \mathrel{L} 1 \) and not \( 1 \mathrel{L} 0 \). In addition, two functions need not be comparable: for \( f(x) = x \) and the constant \( 0 \), neither \( f \mathrel{L} 0 \) (fails at \( x = 1 \)) nor \( 0 \mathrel{L} f \) (fails at \( x = -1 \)).

(d) Symmetric: \( xy = yx \). Transitive: if \( xy > 0 \) and \( yz > 0 \), then \( (xy)(yz) = xz \, y^2 > 0 \), and \( y^2 > 0 \) (since \( y \ne 0 \), as \( xy \ne 0 \)), so \( xz > 0 \). **Not reflexive:** \( 0 \cdot 0 = 0 \), so \( 0 \) is not related to itself. Not antisymmetric: \( 1 \mathrel{P} 2 \) and \( 2 \mathrel{P} 1 \) (both products are \( 2 > 0 \)), and \( 1 \ne 2 \). This is the planted case: \( P \) is symmetric and transitive, yet not reflexive on \( \nR \), exactly at the one element related to nothing. On \( \nR \setminus \{0\} \) it is reflexive. Compare the warning before these exercises.

(e) Not reflexive: \( 0 \ne 0 + 1 \). Not symmetric: \( 0 \mathrel{N} 1 \) and not \( 1 \mathrel{N} 0 \) (\( 0 \ne 2 \)). Not transitive: \( 0 \mathrel{N} 1 \) and \( 1 \mathrel{N} 2 \), and not \( 0 \mathrel{N} 2 \). Antisymmetric, vacuously: \( x \mathrel{N} y \) and \( y \mathrel{N} x \) would give \( y = x + 1 \) and \( x = y + 1 = x + 2 \), which is impossible, so no pair satisfies the hypothesis.
:::

::: {#exr-relations-b2}
[B2: Example generation]

Give an example of a relation on \( \{1, 2, 3\} \) that is reflexive and transitive, but neither symmetric nor antisymmetric. Check each property. Then list the properties that every correct answer must have.
:::

::: {.solution}
One answer:
\[
R = \{ (1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (1, 3), (2, 3) \} .
\]
Reflexive: the three loops are in \( R \). Not symmetric: \( 1 \mathrel{R} 3 \) and not \( 3 \mathrel{R} 1 \). Not antisymmetric: \( 1 \mathrel{R} 2 \), \( 2 \mathrel{R} 1 \) and \( 1 \ne 2 \). Transitive: we check every two-step path \( x \mathrel{R} y \mathrel{R} z \) with \( x \ne y \) and \( y \ne z \) (a step along a loop changes nothing). They are \( 1 \to 2 \to 1 \), \( 1 \to 2 \to 3 \), \( 2 \to 1 \to 2 \) and \( 2 \to 1 \to 3 \), and their shortcuts \( (1, 1) \), \( (1, 3) \), \( (2, 2) \), \( (2, 3) \) are all in \( R \). Element \( 3 \) has no arrow out except its loop, so no other path exists.

Every correct answer must:
- contain the three pairs \( (1, 1) \), \( (2, 2) \), \( (3, 3) \);
- contain two different elements related **both** ways (to fail antisymmetry);
- contain a pair related **one** way only (to fail symmetry);
- contain the shortcut of every two-arrow path.

The second and fourth items together force more: if \( a \mathrel{R} b \), \( b \mathrel{R} a \) and \( b \mathrel{R} c \), transitivity puts \( a \mathrel{R} c \) in. First, there is only one two-way pair: two of them, say \( \{a, b\} \) and \( \{b, c\} \), give \( a \mathrel{R} c \) and \( c \mathrel{R} a \) by transitivity, so \( R \) is the full relation, which is symmetric. Call the two-way pair \( \{a, b\} \) and the third element \( c \). Every arrow between \( a \) and \( b \) is two-way, so a one-way arrow must have \( c \) at one end, and one such arrow is never enough: transitivity relates \( c \) to the other element of the pair too, in the same direction. For example, \( \{(1, 1), (2, 2), (3, 3), (1, 2), (2, 1), (3, 1)\} \) fails transitivity, since \( 3 \mathrel{R} 1 \mathrel{R} 2 \) and not \( 3 \mathrel{R} 2 \). If \( c \mathrel{R} a \), then \( c \mathrel{R} a \mathrel{R} b \) gives \( c \mathrel{R} b \), and neither \( a \mathrel{R} c \) nor \( b \mathrel{R} c \) can hold, since that would make a second two-way pair; so both arrows point out of \( c \). Likewise \( a \mathrel{R} c \) forces \( b \mathrel{R} c \), and both arrows point into \( c \). Conversely, each of these six relations is a correct answer. Those with \( c \) above the pair are the answer above with the elements renamed. Those with \( c \) below are obtained from them by reversing every arrow, which keeps the loops, the two-way pair and the one-way arrows, and keeps transitivity: a path \( z \to y \to x \) of the reversed relation is the reverse of a path \( x \to y \to z \), and the reverse of its shortcut \( (x, z) \) is \( (z, x) \). So \( \{1, 2, 3\} \) carries exactly six correct answers: one for each choice of the two-way pair (three choices) and of whether the third element lies above the pair or below it (two choices); the answer above has \( 3 \) above the pair \( \{1, 2\} \).
:::

::: {#exr-relations-b3}
[B3: Intersections and unions]

Let \( R \) and \( S \) be transitive relations on a set \( X \). Prove that \( R \cap S \) is transitive. Show by an example on \( \{1, 2, 3\} \) that \( R \cup S \) need not be transitive.
:::

::: {.solution}
Let \( x, y, z \in X \) with \( (x, y) \in R \cap S \) and \( (y, z) \in R \cap S \). Then \( (x, y), (y, z) \in R \), so \( (x, z) \in R \) because \( R \) is transitive; likewise \( (x, z) \in S \). Hence \( (x, z) \in R \cap S \).

For the union, let \( R = \{(1, 2)\} \) and \( S = \{(2, 3)\} \). Each is transitive, vacuously: in \( R \) a two-step path would need a pair starting at \( 2 \), and there is none; in \( S \) one would need a pair ending at \( 2 \). But \( R \cup S = \{ (1, 2), (2, 3) \} \) contains \( (1, 2) \) and \( (2, 3) \) and not \( (1, 3) \), so it is not transitive. The intersection keeps both relations' shortcuts; the union creates paths that neither relation contains, so neither supplies their shortcuts.
:::

::: {#exr-relations-b4}
[B4: Prove or disprove]

Prove or disprove each statement. Here \( R \) and \( S \) are relations on a set \( X \), and \( R^{-1} \) is the inverse relation (@def-relation).

::: {.enumerate options="label=(\alph*)"}
1. If \( R \) is reflexive on \( X \) and transitive, then \( R \cap R^{-1} \) is an equivalence relation on \( X \) (reflexive on \( X \), symmetric and transitive).
2. If \( R \) and \( S \) are symmetric, then \( R \cup S \) is symmetric.
3. If \( R \) and \( S \) are antisymmetric, then \( R \cup S \) is antisymmetric.
4. If \( R \) is transitive, then \( R^{-1} \) is transitive.
5. On \( \nN \), the relation "\( x + y \) is a multiple of \( 3 \)" is transitive.
:::
:::

::: {.solution}
(a) True. Write \( E \coloneqq R \cap R^{-1} \); so \( (x, y) \in E \) means \( x \mathrel{R} y \) and \( y \mathrel{R} x \). *Reflexive.* For \( x \in X \), \( x \mathrel{R} x \) by reflexivity, so \( (x, x) \in E \). *Symmetric.* The definition of \( E \) is symmetric in \( x \) and \( y \). *Transitive.* Let \( (x, y), (y, z) \in E \). From \( x \mathrel{R} y \) and \( y \mathrel{R} z \), transitivity gives \( x \mathrel{R} z \); from \( z \mathrel{R} y \) and \( y \mathrel{R} x \), it gives \( z \mathrel{R} x \). So \( (x, z) \in E \).

(b) True. If \( (x, y) \in R \cup S \), say \( (x, y) \in R \), then \( (y, x) \in R \) by symmetry of \( R \), so \( (y, x) \in R \cup S \); likewise if \( (x, y) \in S \).

(c) False. On \( X = \{1, 2\} \), \( R = \{(1, 2)\} \) and \( S = \{(2, 1)\} \) are antisymmetric (vacuously: neither relates two elements both ways), but \( R \cup S \) contains \( (1, 2) \) and \( (2, 1) \), and \( 1 \ne 2 \).

(d) True. Let \( x \mathrel{R^{-1}} y \) and \( y \mathrel{R^{-1}} z \), that is, \( y \mathrel{R} x \) and \( z \mathrel{R} y \). By transitivity of \( R \), from \( z \mathrel{R} y \) and \( y \mathrel{R} x \), \( z \mathrel{R} x \), that is, \( x \mathrel{R^{-1}} z \).

(e) False. Take \( x = 1 \), \( y = 2 \), \( z = 1 \): \( 1 + 2 = 3 \) and \( 2 + 1 = 3 \) are multiples of \( 3 \), but \( 1 + 1 = 2 \) is not: \( 2 = 3k \) fails for every integer \( k \), since \( k \le 0 \) gives \( 3k \le 0 \), and \( k > 0 \) gives \( k \ge 1 \) by @prp-integers-closed (c), hence \( 3k \ge 3 \). (A triple with \( x = z \) is allowed: transitivity quantifies over all \( x, y, z \).)
:::

### C. Going deeper

::: {#exr-relations-c1}
[C1: Properties as equations between sets]

Let \( R \) be a relation on \( X \), let \( R^{-1} \) be its inverse relation (@def-relation), and let \( \Delta_X \coloneqq \{ (x, x) : x \in X \} \) be the diagonal.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( R \) is symmetric if and only if \( R = R^{-1} \), and that \( R \) is antisymmetric if and only if \( R \cap R^{-1} \subseteq \Delta_X \).
2. Deduce that a relation that is both symmetric and antisymmetric satisfies \( R \subseteq \Delta_X \). Is every subset of \( \Delta_X \) both symmetric and antisymmetric?
:::
:::

::: {.solution}
Recall that \( (x, y) \in R^{-1} \) if and only if \( (y, x) \in R \).

(a) *Symmetric.* \( (\Rightarrow) \) Let \( R \) be symmetric. If \( (x, y) \in R \), then \( (y, x) \in R \), that is, \( (x, y) \in R^{-1} \); so \( R \subseteq R^{-1} \). If \( (x, y) \in R^{-1} \), then \( (y, x) \in R \), so \( (x, y) \in R \) by symmetry; so \( R^{-1} \subseteq R \). By @prp-subset-antisymmetric, \( R = R^{-1} \). \( (\Leftarrow) \) If \( R = R^{-1} \) and \( x \mathrel{R} y \), then \( (x, y) \in R^{-1} \), so \( (y, x) \in R \).

*Antisymmetric.* A pair \( (x, y) \) lies in \( R \cap R^{-1} \) exactly when \( x \mathrel{R} y \) and \( y \mathrel{R} x \), and it lies in \( \Delta_X \) exactly when \( x = y \) (by the characteristic property of pairs, @def-ordered-pair). So "\( R \cap R^{-1} \subseteq \Delta_X \)" says: for all \( x, y \in X \), if \( x \mathrel{R} y \) and \( y \mathrel{R} x \), then \( x = y \). That is antisymmetry, word for word.

(b) If \( R \) is symmetric and antisymmetric, then by (a), \( R = R \cap R = R \cap R^{-1} \subseteq \Delta_X \). Conversely, every \( R \subseteq \Delta_X \) is symmetric (each of its pairs is \( (x, x) \), which is its own reverse) and antisymmetric (\( x \mathrel{R} y \) already forces \( x = y \)). So the relations with both properties are exactly the subsets of the diagonal; equality, \( \Delta_X \) itself, is the largest of them, and \( \emptyset \) the smallest.
:::

::: {#exr-relations-c2}
[C2: What symmetry and transitivity do give]

Let \( R \) be a symmetric and transitive relation on \( X \), and let \( D \coloneqq \{ x \in X : \exists y \in X \ \ x \mathrel{R} y \} \) be its domain. Prove that \( R \subseteq D \times D \) and that \( R \), as a relation on \( D \), is reflexive on \( D \), symmetric and transitive.
:::

::: {.solution}
*\( R \subseteq D \times D \).* Let \( (x, y) \in R \). Then \( x \in D \), with witness \( y \). By symmetry \( y \mathrel{R} x \), so \( y \in D \), with witness \( x \). Hence \( (x, y) \in D \times D \).

*Reflexive on \( D \).* Let \( x \in D \). By the definition of \( D \) there is \( y \in X \) with \( x \mathrel{R} y \); fix one (an \( \rulename{\exists E} \), legitimate now, because \( x \in D \) is exactly the statement \( \exists y \in X \ x \mathrel{R} y \)). By symmetry \( y \mathrel{R} x \), and by transitivity, from \( x \mathrel{R} y \) and \( y \mathrel{R} x \), \( x \mathrel{R} x \).

*Symmetric and transitive on \( D \).* These are implications about related elements, and every related pair lies in \( D \times D \); so they hold on \( D \) because they hold on \( X \).

This is the correct version of the false theorem in the warning: its argument proves reflexivity exactly on the set of elements for which "take \( y \) with \( x \mathrel{R} y \)" is available. Elements outside \( D \) are related to nothing, and there reflexivity fails. In the language of Section 4.2, \( R \) is an equivalence relation on \( D \).

**Marking scheme.** (10 points)
- 2: shows \( R \subseteq D \times D \), using symmetry to put the second coordinate in \( D \).
- 4: for reflexivity on \( D \), obtains \( y \) with \( x \mathrel{R} y \) **from \( x \in D \)**, and says why this step is now legitimate.
- 2: applies symmetry and then transitivity, in that order, to get \( x \mathrel{R} x \).
- 2: explains why symmetry and transitivity restrict to \( D \).
Fatal errors (0 for the step): taking \( y \) with \( x \mathrel{R} y \) for an arbitrary \( x \in X \) rather than \( x \in D \) (the error of the warning); applying transitivity to \( x \mathrel{R} y \) and \( x \mathrel{R} y \).
:::

<!-- dependency ledger
def-relation-properties (claim): (the paragraph "Why reflexive on X") symmetric, antisymmetric, transitive depend only on the set R, since x R y forces x, y in X | def-relation (cited)
prp-divides-partial-order (proof): if k <= 0 and a > 0 then ka <= 0; multiplying k > 1 by l > 0 | R order, school fact; axioms in AN1.1
prp-divides-partial-order (proof): cancelling a != 0 from a = lka | R arithmetic, school fact
exm-checking-a-relation (solution): 28 = 7*4, 21 = 7*3; the symmetry and transitivity identities | inline arithmetic; sidecar verify/ch04/exm-checking-a-relation.py
exm-checking-a-relation (claim): (the Quick check after the box) 8 and 20 are not multiples of 7 | prp-integers-closed (c) (cited); sidecar verify/ch04/exm-checking-a-relation.py
exr-relations-b4 (solution): (e) 2 is not a multiple of 3 | prp-integers-closed (c) (cited); (a) R^{-1} as in def-relation (cited); sidecar verify/ch04/exr-relations-b4.py
exm-relation-table (solution): reflexivity of <= (x = x); antisymmetry and transitivity of <= and < on R; not 0 < 0; not 1 <= 0 | R order, school fact; axioms in AN1.1
exm-relation-table (solution): reflexivity and transitivity of subset | def-subset (cited); prp-subset-transitive (cited)
exm-relation-table (solution): 2 does not divide 1 (no integer strictly between 0 and 1) | prp-integers-closed (c) (cited)
exm-relation-table (claim): (the degenerate cases) the full relation X x X is antisymmetric only if X has at most one element | inline (two different elements are related both ways)
exm-relation-table (solution): (the Quick check on common prime factors) the only prime dividing 2 is 2; 3 = 2k gives 1 < k < 2 | def-prime (cited), 2 prime as in the example after def-prime (fd2 1.1); prp-integers-closed (c) (cited)
exr-relations-b1 (solution): cancellation in R; y^2 > 0 for y != 0; product of positives is positive | R arithmetic and order, school fact
exr-relations-b1 (solution): x = x + 2 is impossible | R arithmetic, school fact
exr-relations-b2 (solution): the list of two-step paths in R is complete | inline, by listing the pairs of R
exr-relations-b2 (solution): exactly six correct answers | inline (one two-way pair; the third element above or below it; each candidate is a renaming of R or the reverse of one)
exr-relations-c1 (solution): (x, y) in Delta_X iff x = y | def-ordered-pair (cited)
-->
