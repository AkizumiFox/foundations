# Order by Inclusion, and Least Upper Bounds by Unions

This section belongs to the optional Chapter 7; nothing outside the chapter depends on it. Section 7.1 defined a cut as a set of rationals that is non-empty and not all of \( \nQ \), closed downward, and without a largest element (@def-dedekind-cut), and it called the set of all cuts \( \nR_{\mathrm D} \). Before cuts can be added or multiplied, they can already be compared, and the comparison costs nothing: one cut is below another when it is contained in it. This section shows that this order is total, and then proves the property that the Cauchy road of Chapter 5 reached only at its end. Every non-empty set of cuts that is bounded above has a least upper bound, and that least upper bound is simply the union of the set.

## Comparing cuts

For two rationals \( p \) and \( q \), "\( p \) is at most \( q \)" says the same as "every rational below \( p \) is below \( q \)". In the language of Section 7.1, \( p \le q \) holds exactly when \( D_p \subseteq D_q \): if \( p \le q \) and \( r < p \), then \( r < q \); and if \( q < p \), then \( q \in D_p \setminus D_q \). So on rational cuts, inclusion is the order of \( \nQ \) in disguise. We take it as the order of all cuts.

*One cut is below another when every rational in the first is also in the second.*

::: {#def-cut-order}
[Order of Cuts]

For cuts \( \alpha \) and \( \beta \), we write \( \alpha \le \beta \) if \( \alpha \subseteq \beta \), and \( \alpha < \beta \) if \( \alpha \subsetneq \beta \), that is, if \( \alpha \subseteq \beta \) **and** \( \alpha \ne \beta \). As usual, \( \beta \ge \alpha \) means \( \alpha \le \beta \), and \( \beta > \alpha \) means \( \alpha < \beta \).
:::

The relation \( \le \) is a partial order on \( \nR_{\mathrm D} \) (@fd2:def-partial-order): it is reflexive, since \( \alpha \subseteq \alpha \); antisymmetric, since \( \alpha \subseteq \beta \) and \( \beta \subseteq \alpha \) give \( \alpha = \beta \) (@fd2:prp-subset-antisymmetric); and transitive (@fd2:prp-subset-transitive). Its strict part, \( \alpha \le \beta \) and \( \alpha \ne \beta \), is exactly \( < \). These are the facts that make inclusion a partial order on all of \( \powerset{\nQ} \) (@fd2:exm-subset-order-not-total), restricted to the cuts.

**Two translations.** First, the order of \( \nQ \) is recovered on rational cuts: for \( p, q \in \nQ \),
\[
p < q \iff D_p < D_q , \qquad p = q \iff D_p = D_q .
\]
Indeed, @prp-rational-in-cut (a) with \( \alpha = D_q \) says \( p \in D_q \iff D_p \subsetneq D_q \), and \( p \in D_q \) means \( p < q \). For the second equivalence, if \( p \ne q \), then \( p < q \) or \( q < p \), and either way \( D_p \ne D_q \) by the first. Second, @prp-rational-in-cut now reads, for a cut \( \alpha \) and \( q \in \nQ \),
\[
q \in \alpha \iff D_q < \alpha , \qquad q \notin \alpha \iff \alpha \le D_q .
\]
So "the rational \( q \) lies in the cut \( \alpha \)" and "the rational cut of \( q \) is strictly below \( \alpha \)" are the same statement. This is the precise sense in which a cut is the set of rationals below it.

::: {.check}
Show that \( D_1 < \sigma < D_{3/2} \), where \( \sigma \) is the cut of @exm-cut-sqrt2.
:::

::: {.solution}
By the second translation, \( D_1 < \sigma \) because \( 1 \in \sigma \) (\( 1^2 = 1 < 2 \)), and \( \sigma \le D_{3/2} \) because \( 3/2 \notin \sigma \) (\( 3/2 > 0 \) and \( (3/2)^2 = 9/4 > 2 \)). The inclusion \( \sigma \subseteq D_{3/2} \) is proper: \( 29/20 \) lies in \( D_{3/2} \), since \( 29 \cdot 2 = 58 < 60 = 3 \cdot 20 \), but not in \( \sigma \), since \( 29/20 > 0 \) and \( (29/20)^2 = 841/400 > 2 \) (as \( 841 > 800 \)). So \( \sigma < D_{3/2} \).
:::

Inclusion is rarely a total order: in \( \powerset{\nQ} \), neither of \( \{0\} \) and \( \{1\} \) contains the other. Among cuts it is total, and the reason is separation.

::: {#thm-cut-order-total}
[Cuts Are Totally Ordered]

For all cuts \( \alpha \) and \( \beta \), \( \alpha \le \beta \) or \( \beta \le \alpha \). Hence exactly one of \( \alpha < \beta \), \( \alpha = \beta \), \( \beta < \alpha \) holds.
:::

::: {.idea}
If \( \alpha \) is not inside \( \beta \), then \( \alpha \) has a point \( p \) outside \( \beta \). Everything in \( \beta \) lies below every outside point of \( \beta \), so below \( p \); and \( \alpha \), being closed downward, contains everything below its point \( p \). So \( \alpha \) contains all of \( \beta \).
:::

::: {.proof}
Let \( \alpha, \beta \) be cuts. If \( \alpha \subseteq \beta \), then \( \alpha \le \beta \) and we are done; so suppose \( \alpha \not\subseteq \beta \). Then some \( p \in \alpha \) has \( p \notin \beta \). Let \( q \in \beta \) be arbitrary. Since \( q \in \beta \) and \( p \notin \beta \), @lem-cut-separation gives \( q < p \). Since \( p \in \alpha \) and \( q < p \), (C2) for \( \alpha \) gives \( q \in \alpha \). As \( q \) was arbitrary, \( \beta \subseteq \alpha \), that is, \( \beta \le \alpha \).

For the second statement: if \( \alpha \le \beta \), then \( \alpha = \beta \) or \( \alpha < \beta \); otherwise \( \beta \le \alpha \) and \( \beta \ne \alpha \), that is, \( \beta < \alpha \). So at least one of the three holds. No two hold together: \( \alpha < \beta \) and \( \beta < \alpha \) would give \( \alpha = \beta \) by antisymmetry, against \( \alpha \ne \beta \); and \( \alpha < \beta \) excludes \( \alpha = \beta \) by definition, as \( \beta < \alpha \) does.
:::

The proof used (C2), directly and through @lem-cut-separation, whose proof uses only (C2) and trichotomy in \( \nQ \); it never used (C1) or (C3). So any two subsets of \( \nQ \) that are closed downward are comparable by inclusion. The pair \( \{0\} \), \( \{1\} \) fails (C2), and that is why it could be incomparable.

With @thm-cut-order-total, \( (\nR_{\mathrm D}, \le) \) is a totally ordered set, and the vocabulary of *Sets and Functions*, Section 5.3 applies to it: a set \( A \subseteq \nR_{\mathrm D} \) is **bounded above** if some cut \( \beta \) has \( \alpha \le \beta \) for every \( \alpha \in A \) (@fd2:def-order-bounds), and a cut \( \gamma \) is its **supremum** if it is an upper bound of \( A \), clause (S1), and \( \gamma \le \delta \) for every upper bound \( \delta \) of \( A \), clause (S2) (@fd2:def-order-supremum). A supremum is unique when it exists (@fd2:prp-greatest-unique, applied to the set of upper bounds).

## Least upper bounds are unions

In \( \nQ \), the set \( \{ x \in \nQ : x^2 < 2 \} \) is non-empty and bounded above, and has no supremum (@thm-rationals-gap-sqrt2). The cuts were built so that no such gap remains, and here is the theorem that says so.

::: {#thm-dedekind-lub}
[Least Upper Bounds of Cuts]

Let \( A \subseteq \nR_{\mathrm D} \) be **non-empty** and **bounded above**: some cut \( \beta \) has \( \alpha \le \beta \) for every \( \alpha \in A \). Then
\[
\gamma \coloneqq \bigcup A = \{ p \in \nQ : p \in \alpha \text{ for some } \alpha \in A \}
\]
(@fd2:def-family-union-intersection, the family indexed by \( A \) itself) is a cut, and \( \gamma \) is the supremum of \( A \) in \( (\nR_{\mathrm D}, \le) \).
:::

*Try it first (ten minutes): which cut would you propose as the supremum of a set of cuts? Check your proposal against (C1)–(C3), and then against (S1) and (S2).*

::: {.idea}
The word "bounds" invites a first guess: the intersection \( \bigcap A \), the rationals common to all members. It sits on the wrong side. The intersection lies **inside** every member, so it is a candidate for a lower bound, the infimum's job, and it can even fail to be a cut (try it in Exercise C1). An upper bound must **contain** every member, and the smallest set that does is the union. In \( \powerset{\nQ} \) the union is the supremum: it contains every member, and any set that contains every member contains the union ((S1) and (S2) in the proof below check this for cuts). So everything comes down to one question: is the union a cut? Conditions (C2) and (C3) pass from the members to the union one element at a time, and (C1) needs both hypotheses, one for each half. *Before reading on: which of the three conditions will use "bounded above"?*
:::

::: {.proof}
Let \( \beta \) be an upper bound of \( A \). The set \( \gamma \) is a subset of \( \nQ \), since every member of \( A \) is.

*(C1).* Since \( A \) is non-empty, fix \( \alpha_0 \in A \); since \( \alpha_0 \ne \emptyset \) by (C1) for \( \alpha_0 \), fix \( p_0 \in \alpha_0 \). Then \( p_0 \in \gamma \), so \( \gamma \ne \emptyset \). Next, \( \gamma \subseteq \beta \): if \( p \in \gamma \), then \( p \in \alpha \) for some \( \alpha \in A \) \( [\rulename{\exists E}] \), and \( \alpha \subseteq \beta \) because \( \beta \) is an upper bound, so \( p \in \beta \). By (C1) for \( \beta \), some \( b \in \nQ \) has \( b \notin \beta \); then \( b \notin \gamma \), so \( \gamma \ne \nQ \).

*(C2).* Let \( p \in \gamma \) and \( q \in \nQ \) with \( q < p \). Then \( p \in \alpha \) for some \( \alpha \in A \) \( [\rulename{\exists E}] \). By (C2) for \( \alpha \), \( q \in \alpha \), so \( q \in \gamma \).

*(C3).* Let \( p \in \gamma \), say \( p \in \alpha \) with \( \alpha \in A \) \( [\rulename{\exists E}] \). By (C3) for \( \alpha \), some \( p' \in \alpha \) has \( p' > p \), and \( p' \in \gamma \).

So \( \gamma \) is a cut. *(S1).* For each \( \alpha \in A \), every element of \( \alpha \) lies in \( \gamma \), so \( \alpha \subseteq \gamma \), that is, \( \alpha \le \gamma \). *(S2).* Let \( \delta \) be an upper bound of \( A \). If \( p \in \gamma \), then \( p \in \alpha \) for some \( \alpha \in A \) \( [\rulename{\exists E}] \), and \( \alpha \subseteq \delta \), so \( p \in \delta \). Thus \( \gamma \subseteq \delta \), that is, \( \gamma \le \delta \). Hence \( \gamma \) is the supremum of \( A \).
:::

The answer to the prompt: "bounded above" is used once, in the second half of (C1), to show \( \gamma \ne \nQ \). "Non-empty" is used once too, in the first half of (C1). Conditions (C2) and (C3) of \( \gamma \), and the clauses (S1) and (S2), hold for **every** set of cuts; it is only being a cut at all that needs the hypotheses.

Compare the Cauchy road. There, completeness took two sections: Section 5.5 proved that every Cauchy sequence of real numbers converges, by building rational approximants, and Section 5.6 bisected intervals, with one line that needed the Archimedean property, to reach least upper bounds. Here it took one union and five short checks, (C1)–(C3) and (S1)–(S2). The proof above uses no arithmetic of \( \nQ \) at all, only its order, through (C2) and (C3) of the members; in particular it does not use the Archimedean property. The price is paid elsewhere: cuts have no sum or product yet, and Sections 7.3 and 7.4 build them, multiplication with some effort.

::: {.warning}
Both hypotheses of @thm-dedekind-lub are needed for the union to be a cut. Drop "bounded above": the rational cuts \( D_n \), \( n \in \nN \), have union \( \nQ \), since every rational \( r \) lies below some \( n \in \nN \) (@thm-rationals-archimedean) and so in \( D_n \); and \( \nQ \) fails (C1). Drop "non-empty": \( \bigcup \emptyset = \emptyset \), which fails (C1) too.
:::

::: {.second-reading title="The empty set and unbounded sets have no supremum among cuts"}
The warning shows that the **proof** breaks without each hypothesis. In fact the **conclusion** fails too: without either hypothesis, there is no supremum at all.

*The empty set.* Every cut is an upper bound of \( \emptyset \), vacuously, so a supremum of \( \emptyset \) would be a least cut. There is none: for a cut \( \alpha \), pick \( a \in \alpha \) (C1); then \( D_a < \alpha \) by @prp-rational-in-cut (a), and \( D_a \) is a cut, so \( \alpha \) is not least.

*An unbounded set.* A set with no upper bound has no supremum, since a supremum is an upper bound by (S1). For example \( \{ D_n : n \in \nN \} \) has none: if \( \beta \) bounded it, then \( \nQ = \bigcup_{n \in \nN} D_n \subseteq \beta \), against (C1) for \( \beta \).
:::

::: {.check}
Find \( \sup \{ D_{1 - 1/n} : n \in \nZ_{>0} \} \) in \( (\nR_{\mathrm D}, \le) \). Is it an element of the set?
:::

::: {.solution}
The set is non-empty and bounded above by \( D_1 \), since \( 1/n > 0 \) (@prp-reciprocal-order (a)), so \( 1 - 1/n < 1 \) and \( D_{1 - 1/n} \subseteq D_1 \). By @thm-dedekind-lub its supremum is the union \( U \coloneqq \bigcup_{n \ge 1} D_{1 - 1/n} \). We show \( U = D_1 \). \( (\subseteq) \): if \( r < 1 - 1/n \) for some \( n \), then \( r < 1 \). \( (\supseteq) \): let \( r < 1 \). Then \( 1 - r > 0 \), and @cor-rationals-archimedean-epsilon gives \( n \in \nZ_{>0} \) with \( 1/n < 1 - r \), that is, \( r < 1 - 1/n \), so \( r \in U \). Hence the supremum is \( D_1 \). It is not in the set: \( D_{1 - 1/n} = D_1 \) would force \( 1 - 1/n = 1 \) by the first translation, and \( 1/n \ne 0 \).
:::

So \( (\nR_{\mathrm D}, \le) \) is a totally ordered set in which every non-empty subset that is bounded above has a supremum. Once Sections 7.3 and 7.4 have made \( \nR_{\mathrm D} \) an ordered field with this order, Section 7.5 reads @thm-dedekind-lub as the statement that it is a **complete** ordered field (@def-complete-ordered-field).

## Exercises

### A. Check your understanding

::: {#exr-order-and-completeness-a1}
[A1]

These questions are about @thm-dedekind-lub and its proof.

::: {.enumerate options="label=(\alph*)"}
1. Let \( A \coloneqq \{ D_q : q \in \sigma \} \), with \( \sigma \) the cut of @exm-cut-sqrt2. Check that \( A \) satisfies the hypotheses, and find the cut \( \gamma \) of the proof, arguing directly from (C2) and (C3) of \( \sigma \).
2. State the idea of the proof in two sentences.
3. Which line of the proof fails if \( A = \emptyset \), and what is \( \gamma \) then?
4. In the check of (C3) for \( \gamma \), which cut's condition (C3) is used?
:::
:::

::: {.solution}
(a) \( A \) is non-empty, since \( 0 \in \sigma \) gives \( D_0 \in A \). It is bounded above by \( \sigma \): for \( q \in \sigma \), \( D_q < \sigma \) by @prp-rational-in-cut (a). The proof's cut is \( \gamma = \bigcup_{q \in \sigma} D_q \), and \( \gamma = \sigma \). \( (\subseteq) \): each \( D_q \) with \( q \in \sigma \) is contained in \( \sigma \), by (C2) of \( \sigma \). \( (\supseteq) \): let \( q \in \sigma \); by (C3) of \( \sigma \) there is \( q' \in \sigma \) with \( q' > q \), so \( q \in D_{q'} \subseteq \gamma \). So \( \sup A = \sigma \): the cut of the gap is the supremum of the rational cuts below it.

(b) The union of the cuts contains each of them, and lies inside every upper bound, so it is the least upper bound once it is known to be a cut. It is one because (C2) and (C3) pass from the members to the union element by element, while (C1) comes from \( A \ne \emptyset \) (some element) and from an upper bound \( \beta \ne \nQ \) (some non-element).

(c) The first line of (C1): with \( A = \emptyset \) there is no \( \alpha_0 \in A \) to fix. Then \( \gamma = \bigcup \emptyset = \emptyset \), which is not a cut.

(d) Condition (C3) of the member \( \alpha \in A \) that contains the given \( p \in \gamma \). Different points of \( \gamma \) may use different members.
:::

### B. Practice

::: {#exr-order-and-completeness-b1}
[B1]

Let \( q, r \in \nQ \). Prove that \( \sup \{ D_q, D_r \} = D_{\max(q, r)} \) in \( (\nR_{\mathrm D}, \le) \).
:::

::: {.solution}
Let \( m \coloneqq \max(q, r) \). Since \( q \le m \) and \( r \le m \), \( D_q \subseteq D_m \) and \( D_r \subseteq D_m \) (if \( s < q \le m \), then \( s < m \)); so \( \{ D_q, D_r \} \) is non-empty and bounded above by \( D_m \). By @thm-dedekind-lub its supremum is \( D_q \cup D_r \). This union contains \( D_m \), because \( D_m \) is one of \( D_q \), \( D_r \); and it is contained in \( D_m \), by the two inclusions above. Hence \( \sup \{ D_q, D_r \} = D_q \cup D_r = D_m \).
:::

::: {#exr-order-and-completeness-b2}
[B2: Put the proof in order]

Here are lines of a proof that for cuts \( \alpha \) and \( \beta \), \( \alpha \le \beta \) or \( \beta \le \alpha \), shuffled, together with two lines that do not belong. Without looking back, write the lines of a correct proof in a correct order, and say what is wrong with each line you leave out.

(i) Let \( q \in \beta \) be arbitrary.

(ii) Since \( q < p \) and \( p \in \alpha \), \( q \in \beta \).

(iii) As \( q \) was arbitrary, \( \beta \subseteq \alpha \).

(iv) Let \( \alpha \), \( \beta \) be cuts with \( \alpha \not\subseteq \beta \) (if \( \alpha \subseteq \beta \), there is nothing to prove).

(v) Since \( p \in \alpha \) and \( q < p \), \( q \in \alpha \), because \( \alpha \) is closed downward.

(vi) Since \( q \in \beta \) and \( p \notin \beta \), \( p < q \).

(vii) Then some \( p \in \alpha \) has \( p \notin \beta \).

(viii) Since \( q \in \beta \) and \( p \notin \beta \), \( q < p \), by separation.
:::

::: {.solution}
An admissible order is
\[
\text{(iv)}, \ \text{(vii)}, \ \text{(i)}, \ \text{(viii)}, \ \text{(v)}, \ \text{(iii)} .
\]
Line (i) may also come before (vii), since it only introduces a name for an arbitrary element of \( \beta \), and (vii) does not mention \( q \). Otherwise the order is forced: (vii) unwinds the assumption of (iv); (viii) needs \( p \) from (vii) and \( q \) from (i); (v) needs \( q < p \) from (viii); and (iii) closes the argument about the arbitrary \( q \).

*Line (vi) reads separation backwards.* @lem-cut-separation puts a point **inside** a cut below a point **outside** it. Here \( q \) is inside \( \beta \) and \( p \) is outside, so separation gives \( q < p \), as in (viii); line (vi) asserts the opposite, and the two together contradict (O1).

*Line (ii) applies closure to the wrong cut.* Closure downward of \( \alpha \) turns "\( p \in \alpha \) and \( q < p \)" into \( q \in \alpha \), not into \( q \in \beta \); the fact that \( p \in \alpha \) says nothing about \( \beta \). (Its conclusion \( q \in \beta \) is true, but only because it was assumed in (i).)
:::

### C. Going deeper

::: {#exr-order-and-completeness-c1}
[C1: Infima]

Let \( A \subseteq \nR_{\mathrm D} \) be non-empty and bounded below.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \bigcap A \) need not be a cut, by computing \( \bigcap A_0 \) for \( A_0 \coloneqq \{ D_{1/n} : n \in \nZ_{>0} \} \).
2. Prove that \( A \) nevertheless has an infimum in \( (\nR_{\mathrm D}, \le) \): it is the supremum of the set of lower bounds of \( A \).
3. Find \( \inf A_0 \).
:::
:::

::: {.solution}
[Hint 1]

For (b), the set \( L \) of lower bounds of \( A \) is non-empty by hypothesis. Find an upper bound for \( L \) among the elements of \( A \).
:::

::: {.solution}
[Hint 2]

Let \( \lambda_0 \coloneqq \sup L \), which exists by @thm-dedekind-lub; the claim is that \( \lambda_0 = \inf A \).
:::

::: {.solution}
(a) Here \( \bigcap A_0 = \{ r \in \nQ : r < 1/n \text{ for every } n \in \nZ_{>0} \} \), the intersection taken in \( \nQ \). We claim it is \( \{ r \in \nQ : r \le 0 \} \). If \( r \le 0 \), then \( r \le 0 < 1/n \) for every \( n \) (@prp-reciprocal-order (a)). If \( r > 0 \), @cor-rationals-archimedean-epsilon gives \( n \) with \( 1/n < r \), so \( r \notin D_{1/n} \) and \( r \notin \bigcap A_0 \). The set \( \{ r : r \le 0 \} \) has the largest element \( 0 \), so it fails (C3) and is not a cut. (The set \( A_0 \) is non-empty and bounded below, by \( D_0 \), for instance.)

(b) Let \( L \coloneqq \{ \lambda \in \nR_{\mathrm D} : \lambda \le \alpha \text{ for every } \alpha \in A \} \), the set of lower bounds of \( A \). It is non-empty, since \( A \) is bounded below. It is bounded above: fix \( \alpha_0 \in A \) (\( A \ne \emptyset \)); every \( \lambda \in L \) has \( \lambda \le \alpha_0 \). By @thm-dedekind-lub, \( L \) has a supremum \( \lambda_0 \).

*\( \lambda_0 \) is a lower bound of \( A \).* Let \( \alpha \in A \). Every \( \lambda \in L \) has \( \lambda \le \alpha \), so \( \alpha \) is an upper bound of \( L \), and (S2) for \( \lambda_0 = \sup L \) gives \( \lambda_0 \le \alpha \).

*\( \lambda_0 \) is the greatest lower bound.* We just showed \( \lambda_0 \in L \). If \( \lambda \) is any lower bound of \( A \), then \( \lambda \in L \), so \( \lambda \le \lambda_0 \) by (S1) for \( \lambda_0 \). Hence \( \lambda_0 = \inf A \).

(c) \( \inf A_0 = D_0 \). It is a lower bound: \( D_0 \subseteq D_{1/n} \) since \( 0 < 1/n \). Let \( \lambda \) be any lower bound. Then \( \lambda \subseteq \bigcap A_0 = \{ r : r \le 0 \} \) by (a). And \( 0 \notin \lambda \): otherwise (C3) for \( \lambda \) gives \( p' \in \lambda \) with \( p' > 0 \), but \( \lambda \) contains no positive rational. So every element of \( \lambda \) is negative, \( \lambda \subseteq D_0 \), and \( \lambda \le D_0 \). So the infimum is the intersection with its largest element removed.

**Marking scheme.** (10 points)
- 2: (a) computes \( \bigcap A_0 = \{ r : r \le 0 \} \), using the Archimedean property for the positive rationals, and names (C3) as the failing condition.
- 2: (b) shows that the set of lower bounds is non-empty and bounded above by a member of \( A \).
- 2: (b) shows that its supremum is a lower bound of \( A \), through (S2).
- 2: (b) shows that it is the greatest lower bound, through (S1).
- 2: (c) identifies \( D_0 \), with both inequalities.
Fatal errors (0 for the step): asserting that \( \bigcap A \) is the infimum without checking (C3); using a supremum of \( L \) without checking that \( L \) is non-empty and bounded above.
:::

::: {#exr-order-and-completeness-c2}
[C2: Find the error]

Here is a proof. Its conclusion is the first half of @thm-dedekind-lub.

> **Claim.** Let \( A \subseteq \nR_{\mathrm D} \) be non-empty and bounded above. Then \( \gamma \coloneqq \bigcup A \) is a cut.
>
> (1) Since \( A \) is non-empty, pick \( \alpha_0 \in A \); since \( \alpha_0 \ne \emptyset \), pick \( p_0 \in \alpha_0 \). Then \( p_0 \in \gamma \), so \( \gamma \ne \emptyset \). (2) Each \( \alpha \in A \) is a cut, so \( \alpha \ne \nQ \). Hence \( \gamma \ne \nQ \). (3) Let \( p \in \gamma \) and \( q < p \). Then \( p \in \alpha \) for some \( \alpha \in A \), so \( q \in \alpha \) by (C2), and \( q \in \gamma \). (4) Let \( p \in \gamma \). Then \( p \in \alpha \) for some \( \alpha \in A \); by (C3) there is \( p' \in \alpha \) with \( p' > p \), and \( p' \in \gamma \). (5) So \( \gamma \) satisfies (C1)–(C3).

Is the conclusion true? Does the argument prove it? If not, name the line that fails, say what is illegal about it, and give a counterexample to that step.
:::

::: {.solution}
The conclusion is true: it is proved in @thm-dedekind-lub. The argument does not prove it, because line (2) fails.

*What is illegal.* Line (2) passes from "for every \( \alpha \in A \) there is a rational outside \( \alpha \)" to "there is a rational outside every \( \alpha \in A \)", which is what \( \gamma \ne \nQ \) means. The rational outside \( \alpha \) depends on \( \alpha \), and the line uses it as if one rational served every member at once. This is the move (N2) of @fd1:exm-not-allowed-catalogue: a witness found inside the box of one \( \alpha \) is treated as uniform in \( \alpha \). A union of proper subsets of \( \nQ \) can be all of \( \nQ \).

*Counterexample to the step.* Let \( A' \coloneqq \{ D_n : n \in \nN \} \). Each \( D_n \) is a cut, so \( D_n \ne \nQ \), and the premise of the step holds; but \( \bigcup A' = \nQ \), since every rational lies below some natural number (@thm-rationals-archimedean). So the step leads from a true premise to a false conclusion. (This \( A' \) is not bounded above, so it is not a counterexample to the claim, which is true.)

*The tell.* The hypothesis "bounded above" is never used. A correct proof must use it, since the warning after @thm-dedekind-lub shows that the claim fails without it.

*Repair.* Let \( \beta \) be an upper bound of \( A \). Every \( \alpha \in A \) satisfies \( \alpha \subseteq \beta \), so \( \gamma \subseteq \beta \); and \( \beta \ne \nQ \), so some \( b \notin \beta \), hence \( b \notin \gamma \) and \( \gamma \ne \nQ \).
:::

::: {#exr-order-and-completeness-c3}
[C3: Exit check: least upper bounds of cuts]

Let \( A \) be a non-empty set of cuts, bounded above in \( (\nR_{\mathrm D}, \subseteq) \). Prove that \( \bigcup A \) is a cut and that it is the supremum of \( A \).
:::

::: {.solution}
Let \( \gamma \coloneqq \bigcup A \) and let \( \beta \) be an upper bound of \( A \).

*(C1).* Pick \( \alpha_0 \in A \) and \( p_0 \in \alpha_0 \), possible since \( A \ne \emptyset \) and \( \alpha_0 \ne \emptyset \); then \( p_0 \in \gamma \). Every element of \( \gamma \) lies in some \( \alpha \in A \), and \( \alpha \subseteq \beta \), so \( \gamma \subseteq \beta \). Pick \( b \in \nQ \setminus \beta \) (C1 for \( \beta \)); then \( b \notin \gamma \). So \( \emptyset \ne \gamma \ne \nQ \).

*(C2).* If \( q < p \) with \( p \in \gamma \), then \( p \in \alpha \) for some \( \alpha \in A \), so \( q \in \alpha \subseteq \gamma \).

*(C3).* If \( p \in \gamma \), then \( p \in \alpha \) for some \( \alpha \in A \), and (C3) for \( \alpha \) gives \( p' \in \alpha \subseteq \gamma \) with \( p' > p \).

*Upper bound.* Each \( \alpha \in A \) satisfies \( \alpha \subseteq \gamma \).

*Least.* If \( \delta \) is a cut with \( \alpha \subseteq \delta \) for every \( \alpha \in A \), then every \( p \in \gamma \) lies in some \( \alpha \in A \), hence in \( \delta \); so \( \gamma \subseteq \delta \).

So \( \gamma \) is a cut, an upper bound of \( A \), and below every upper bound: \( \gamma = \sup A \).

**Marking scheme.** (10 points)
- 2: \( \gamma \ne \emptyset \) from \( A \ne \emptyset \), and \( \gamma \ne \nQ \) from the upper bound \( \beta \ne \nQ \).
- 2: \( \gamma \) closed downward.
- 2: \( \gamma \) has no largest element.
- 2: \( \gamma \) is an upper bound of \( A \).
- 2: \( \gamma \) is below every upper bound of \( A \).
Fatal errors (0 for the step): "\( \gamma \ne \nQ \) because each \( \alpha \ne \nQ \)" (the error of Exercise C2); comparing cuts with "\( \le \)" as if they were rationals, instead of by inclusion.
:::

<!-- dependency ledger
def-cut-order (claim): p <= q iff D_p subset D_q (hook); r < p <= q gives r < q | (O2); inline
def-cut-order (claim): p < q iff D_p < D_q; p = q iff D_p = D_q | prp-rational-in-cut (a), trichotomy (O1); inline
def-cut-order (claim): Quick check: 9/4 > 2, 58 < 60, 841 > 800 | Q ordered field, F3.2 (comparison formula, thm-rationals-ordered-field (a)); verify/ch07/def-cut-order.py
thm-cut-order-total (proof): the three-way split from totality and antisymmetry | def-cut-order, fd2:prp-subset-antisymmetric; inline
thm-cut-order-total (claim): the proof uses only (C2) and trichotomy in Q | meta-claim about the proof above and lem-cut-separation's proof; checkable on the page
def-cut-order (claim): {0}, {1} incomparable in P(Q) | fd2:exm-subset-order-not-total, cited
thm-dedekind-lub (idea): in P(Q) the union is the supremum | inline; (S1)/(S2) of the proof
thm-dedekind-lub (claim): supremum unique | fd2:prp-greatest-unique, cited
thm-dedekind-lub (claim): Cauchy road comparison: Sections 5.5 and 5.6, the Archimedean line | thm-constructed-reals-cauchy-complete, thm-cauchy-archimedean-lub (prose only; nothing here depends on them)
thm-dedekind-lub (claim): "the proof uses no arithmetic of Q, only its order" | meta-claim about the proof above; checkable on the page
thm-dedekind-lub (claim): warning: every rational lies below some n in N | thm-rationals-archimedean, cited
thm-dedekind-lub (claim): Quick check: 1/n > 0, so 1 - 1/n < 1 and 1/n != 0; r < 1 - 1/n < 1 gives r < 1 | prp-reciprocal-order (a), cited; (O3), (O2); inline
thm-dedekind-lub (claim): Quick check: r < 1 gives n with 1/n < 1 - r | cor-rationals-archimedean-epsilon, cited; (O3)
thm-dedekind-lub (claim): closing paragraph: Section 7.5 reads the theorem as completeness | def-complete-ordered-field (prose pointer to Section 7.5)
exr-order-and-completeness-a1 (solution): D_q < sigma for q in sigma | prp-rational-in-cut (a), cited
exr-order-and-completeness-b1 (solution): D_q subset D_m for q <= m | (O2); inline
exr-order-and-completeness-c1 (solution): 0 < 1/n; n with 1/n < r | prp-reciprocal-order (a), cor-rationals-archimedean-epsilon, cited
exr-order-and-completeness-c2 (solution): (N2) witness-uniformity error | fd1:exm-not-allowed-catalogue, cited
-->
