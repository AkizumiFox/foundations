# Normal Forms and Adequate Connectives

The proof of completeness wrote each row of a truth table as a list of signed atoms \( p_1^{v}, \dots, p_n^{v} \) (Section 4.8). Join the signed atoms of one row by \( \wedge \), and you get a formula that is true in that row and in no other. Join those formulas, one for each row where a given formula \( \varphi \) is true, by \( \vee \), and you get a formula with the same truth table as \( \varphi \). This section turns that observation into two standard shapes for formulas, the disjunctive and the conjunctive normal form. It then reads validity off the conjunctive shape at a glance, and asks how few connectives are really needed.

*On a first reading this section may wait: it is a second-pass section, and nothing in Chapters 5–8 uses it.*

## Conjunctions and disjunctions of many formulas

Normal forms are long conjunctions and disjunctions. Section 4.5 fixed how to write them, in the paragraph on long conjunctions after @prp-standard-equivalences. For formulas \( \chi_1, \dots, \chi_k \) with \( k \ge 1 \), \( \chi_1 \wedge \chi_2 \wedge \dots \wedge \chi_k \) is the conjunction **grouped to the right**, \( \chi_1 \wedge (\chi_2 \wedge (\cdots \wedge \chi_k)) \), and likewise for \( \vee \); for \( k = 1 \) it is \( \chi_1 \) itself. That paragraph proved, by induction on the number of terms, how such formulas are evaluated: for every valuation \( v \),
\[
\begin{aligned}
v(\chi_1 \wedge \dots \wedge \chi_k) = \mathrm{T} &\iff v(\chi_i) = \mathrm{T} \text{ for every } i = 1, \dots, k, \\
v(\chi_1 \vee \dots \vee \chi_k) = \mathrm{T} &\iff v(\chi_i) = \mathrm{T} \text{ for some } i = 1, \dots, k.
\end{aligned}
\]{#eq-many-term-values}
We use these two lines constantly below, and we cite them by this display.

So a long conjunction is true when **all** its parts are, and a long disjunction when **at least one** is, just as the words say.

## Literals, clauses and the two normal forms

The building blocks are the smallest formulas that still carry a sign.

::: {#def-literal}
[Literal]

A **literal** is an atom or the negation of an atom.
:::

So \( p \), \( \neg p \), \( q_7 \) and \( \neg q_7 \) are literals. The signed atom \( p^{v} \) of Section 4.8 is always a literal. The formulas \( \neg\neg p \), \( \neg(p \wedge q) \) and \( \bot \) are not: in the first two, \( \neg \) is applied to something other than an atom, and \( \bot \) is neither an atom nor a negation. The **opposite** of a literal is \( \neg p \) if the literal is \( p \), and \( p \) if it is \( \neg p \). By the clause for \( \neg \) in @def-truth-value, a literal and its opposite take opposite values under every valuation.

From literals we build two kinds of blocks and two kinds of formulas.

- A **clause** joins one or more literals by \( \vee \), such as \( p \vee \neg q \vee r \), or \( \neg q \) alone.
- A **conjunctive clause** joins one or more literals by \( \wedge \), such as \( p \wedge \neg q \wedge r \), or \( \neg q \) alone. (We do not shorten it to "conjunct", which keeps its ordinary meaning, one side of a conjunction.)

*A normal form is a formula whose connectives come in fixed layers: negations only on atoms, then one layer of one connective, then one layer of the other.*

::: {#def-dnf}
[Disjunctive Normal Form]

A formula **has disjunctive normal form** (DNF), or is **in DNF**, when it has the shape \( C_1 \vee \dots \vee C_k \), with \( k \ge 1 \), where every \( C_i \) joins **one or more literals** by \( \wedge \).
:::

::: {#def-cnf}
[Conjunctive Normal Form]

A formula **has conjunctive normal form** (CNF), or is **in CNF**, when it has the shape \( K_1 \wedge \dots \wedge K_k \), with \( k \ge 1 \), where every \( K_i \) joins **one or more literals** by \( \vee \).
:::

In words: a DNF is an "or of ands" and a CNF an "and of ors", and in both the only negations sit directly on atoms. Read a DNF as a list of situations, any one of which makes it true; read a CNF as a list of requirements, all of which must be met.

Check some formulas against the definitions, clause by clause.

1. \( (p \wedge \neg q) \vee (\neg p \wedge q) \) is in DNF: two conjunctive clauses, each a conjunction of literals. It is not in CNF: as a conjunction of clauses it would have to be a single clause (it is not a conjunction), and a clause cannot contain \( \wedge \).
2. \( (p \vee q) \wedge (\neg p \vee \neg q) \) is in CNF, with two clauses, and not in DNF.
3. \( p \wedge \neg q \) is in both: in DNF with one conjunctive clause, and in CNF with two clauses of one literal each. Likewise \( p \vee \neg q \) is in both.
4. A single literal, \( \neg r \), is in both forms: one conjunctive clause of one literal, and one clause of one literal. This degenerate case matters, because a formula such as \( \neg r \) must count as already normal.

A nonexample by a minimal change: \( (p \wedge \neg q) \vee r \) is in DNF, but \( \neg(p \wedge q) \vee r \) is not in either form. Only one symbol moved, and the literal condition fails: \( \neg \) now stands on the conjunction \( p \wedge q \), not on an atom. The formula \( p \to q \) is in neither form either, since \( \to \) is not allowed at all.

Why these layers? Because they are the shapes that the truth table hands us, as the next theorem shows, and because in these shapes some questions become easy: the subsection "Reading validity off a CNF" below decides validity of a CNF without a table.

::: {.warning}
A literal is an atom with **at most one** \( \neg \), and nothing else. \( \neg\neg p \) is equivalent to the literal \( p \) but is not a literal, so \( \neg\neg p \vee q \) is not in CNF as written. Likewise \( \bot \) is not a literal, so a "normal form" containing \( \bot \) is not one; that is why the constructions below never use it.
:::

::: {.check}
Which of the following are in CNF, and which are in DNF? (i) \( (p \vee \neg q) \wedge r \); (ii) \( \neg(p \vee q) \); (iii) \( p \vee (\neg q \wedge r) \).
:::

::: {.solution}
*(i)* CNF, with clauses \( p \vee \neg q \) and \( r \); not DNF, since the conjunctive clause would have to be the whole formula and \( p \vee \neg q \) is not a literal. (ii) Neither: \( \neg \) stands on a disjunction. (iii) DNF, with conjunctive clauses \( p \) and \( \neg q \wedge r \); not CNF, since the one clause would contain \( \wedge \).
:::

## Reading a DNF off the truth table

Take a valuation \( v \) and atoms \( p_1, \dots, p_n \) with \( n \ge 1 \), and form the **minterm** of the row of \( v \), the conjunctive clause of its signed atoms,
\[
C_v \coloneqq p_1^{v} \wedge \dots \wedge p_n^{v} .
\]
For every valuation \( w \), each \( p_i^{v} \) is true under \( w \) exactly when \( w(p_i) = v(p_i) \): if \( v(p_i) = \mathrm{T} \), then \( p_i^{v} = p_i \); if \( v(p_i) = \mathrm{F} \), then \( p_i^{v} = \neg p_i \), which is true under \( w \) exactly when \( w(p_i) = \mathrm{F} \). By @eq-many-term-values,
\[
w(C_v) = \mathrm{T} \iff w(p_i) = v(p_i) \text{ for every } i = 1, \dots, n .
\]{#eq-row-conjunct}
So \( C_v \) is true in the row of \( v \) and in no other row. It is a formula that "names" one row.

::: {#exm-dnf-exclusive-or}
[Exactly one of two]

Find a formula in DNF that is true exactly when exactly one of \( p \), \( q \) is true, and check it.
:::

::: {.solution}
The rows with exactly one of \( p \), \( q \) true are \( (p, q) = (\mathrm{T}, \mathrm{F}) \) and \( (\mathrm{F}, \mathrm{T}) \). Their minterms are \( p \wedge \neg q \) and \( \neg p \wedge q \), so the answer is
\[
(p \wedge \neg q) \vee (\neg p \wedge q).
\]
Check against the table: in the row T, F the first minterm is true; in F, T the second is; in T, T each minterm has a false literal (\( \neg q \), \( \neg p \)); in F, F likewise (\( p \), \( q \)). So the formula is true in exactly the two rows wanted.
:::

The same recipe works for any formula.

::: {#thm-dnf}
[Disjunctive Normal Form]

Every formula \( \varphi \) is equivalent to a formula in DNF. If \( \varphi \) has at least one atom, the DNF can be chosen so that every atom in it is an atom of \( \varphi \).
:::

::: {.idea}
List the rows where \( \varphi \) is true and disjoin their minterms \( C_v \). A valuation makes the disjunction true exactly when it agrees with one of those rows, which by @lem-coincidence is exactly when it makes \( \varphi \) true. Two degenerate cases need a convention: a formula with no T-row, whose disjunction would be empty, and a formula with no atoms, which has no rows to speak of.
:::

::: {.proof}
By the paraphrase of @def-semantic-equivalence, two formulas \( \varphi \) and \( \psi \) are equivalent exactly when \( v(\varphi) = v(\psi) \) for every valuation \( v \).

*Case 1: \( \varphi \) has at least one atom.* Let \( p_1, \dots, p_n \) (\( n \ge 1 \)) be the atoms of \( \varphi \). A **row** is a choice of a value for each \( p_i \); there are \( 2^n \) rows, and for each we fix a valuation that takes those values at \( p_1, \dots, p_n \) (and, say, T at every other atom). By @lem-coincidence, \( v(\varphi) \) depends only on the row of \( v \). Let \( v_1, \dots, v_k \) be the fixed valuations of the rows in which \( \varphi \) is T.

If \( k \ge 1 \), let \( D \coloneqq C_{v_1} \vee \dots \vee C_{v_k} \), which is in DNF by @def-dnf, with atoms among \( p_1, \dots, p_n \). Let \( w \) be any valuation. By @eq-many-term-values and @eq-row-conjunct, \( w(D) = \mathrm{T} \) exactly when \( w \) agrees with some \( v_j \) on \( p_1, \dots, p_n \). If it does, then \( w(\varphi) = v_j(\varphi) = \mathrm{T} \) by @lem-coincidence. Conversely, if \( w(\varphi) = \mathrm{T} \), then the row of \( w \) is one where \( \varphi \) is T, so \( w \) agrees on \( p_1, \dots, p_n \) with the valuation \( v_j \) fixed for that row. Hence \( w(D) = w(\varphi) \) for every \( w \), and \( \varphi \equiv D \).

If \( k = 0 \), then \( \varphi \) is F in every row, hence under every valuation. The formula \( p_1 \wedge \neg p_1 \) is in DNF (one conjunctive clause of two literals) and is F under every valuation by @def-truth-value. So \( \varphi \equiv p_1 \wedge \neg p_1 \).

*Case 2: \( \varphi \) has no atoms.* Any two valuations agree on all the atoms of \( \varphi \) (there are none), so by @lem-coincidence \( v(\varphi) \) is the same for every \( v \). Let \( p \) be an atom. If that value is T, then \( \varphi \equiv p \vee \neg p \), which is true under every valuation and is in DNF (two conjunctive clauses of one literal); if it is F, then \( \varphi \equiv p \wedge \neg p \). This proves the theorem.
:::

The minterms of different rows are never true together, and in each row exactly one of the \( 2^n \) minterms is true: they divide the rows like the pieces of a partition, and a full disjunctive normal form collects the pieces in which the formula is true.

The minterms \( C_v \) are the signed atoms of Section 4.8 joined by \( \wedge \). There the signed atoms of a row were premises from which \( \varphi^{v} \) was derived; here they are joined into a formula that is true in that row only. The proof is the proof of completeness with the derivations taken out.

::: {.second-reading title="Why not the constant for contradiction"}
For \( p \wedge \neg p \) we could have written \( \bot \), which is also F under every valuation. We did not, because \( \bot \) is not a literal, and because the adequacy theorem at the end of this section reuses the construction in a language without \( \bot \).
:::

## Conjunctive normal form

A DNF lists the rows where a formula is true. A CNF does the opposite: it lists the rows where the formula is **false**, one clause per row, each clause being false in its row and true in every other.

::: {#thm-cnf}
[Conjunctive Normal Form]

Every formula \( \varphi \) is equivalent to a formula in CNF. If \( \varphi \) has at least one atom, the CNF can be chosen so that every atom in it is an atom of \( \varphi \).
:::

::: {.idea}
Apply @thm-dnf to \( \neg\varphi \) and negate the result: \( \varphi \equiv \neg\neg\varphi \equiv \neg(C_1 \vee \dots \vee C_k) \). Now push the \( \neg \) inwards with De Morgan's laws and double negation (@prp-standard-equivalences): \( \neg(C_1 \vee \dots \vee C_k) \) becomes \( \neg C_1 \wedge \dots \wedge \neg C_k \), and each \( \neg C_i \), the negation of a conjunction of literals, becomes the disjunction of the opposite literals. The proof checks the outcome directly with @eq-many-term-values, which avoids De Morgan's laws for many terms.
:::

::: {.proof}
By @thm-dnf, \( \neg\varphi \equiv C_1 \vee \dots \vee C_k \) for some conjunctive clauses \( C_1, \dots, C_k \) (with atoms among those of \( \varphi \) if it has any, since \( \neg\varphi \) has the same atoms). For each \( i \), let \( K_i \) be the disjunction of the opposites of the literals of \( C_i \), in the same order, and let \( K \coloneqq K_1 \wedge \dots \wedge K_k \). Then \( K \) is in CNF, with the same atoms as \( C_1 \vee \dots \vee C_k \).

Let \( w \) be a valuation. Each literal of \( K_i \) is true under \( w \) exactly when the corresponding literal of \( C_i \) is false. By @eq-many-term-values, used at each step:
\[
\begin{aligned}
w(K) = \mathrm{T}
&\iff \text{for every } i, \ w(K_i) = \mathrm{T} \\
&\iff \text{for every } i, \text{ some literal of } C_i \text{ is false under } w \\
&\iff \text{for every } i, \ w(C_i) = \mathrm{F} \\
&\iff w(C_1 \vee \dots \vee C_k) = \mathrm{F} .
\end{aligned}
\]
Since \( C_1 \vee \dots \vee C_k \equiv \neg\varphi \), the last line holds exactly when \( w(\neg\varphi) = \mathrm{F} \), that is, when \( w(\varphi) = \mathrm{T} \). So \( w(K) = w(\varphi) \) for every \( w \), and \( \varphi \equiv K \).
:::

Unwinding the construction: the conjunctive clauses \( C_i \) of the DNF of \( \neg\varphi \) are the rows where \( \varphi \) is **false**, and \( K_i \) is the clause that is false exactly in the row of \( C_i \). So the CNF can be read straight off the table: **one clause per F-row**, built from the opposites of that row's signed atoms. In the row \( p = \mathrm{T} \), \( q = \mathrm{F} \), for instance, the clause is \( \neg p \vee q \). A formula with no F-row gets, by the proof, the clause of a contradiction's DNF negated, \( \neg p \vee p \) (from \( C_1 = p \wedge \neg p \)), which is true in every row.

::: {.check}
On the atoms \( p \), \( q \), \( r \), write the CNF clause for the F-row \( p = \mathrm{F} \), \( q = \mathrm{T} \), \( r = \mathrm{F} \).
:::

::: {.solution}
The row's signed atoms are \( \neg p \), \( q \), \( \neg r \); their opposites give \( p \vee \neg q \vee r \). It is false exactly when \( p \) is F, \( q \) is T and \( r \) is F, that is, in that row only.
:::

Alternatively, a CNF can be reached by **rewriting**. First replace each \( \bot \), which is not a literal, by \( p \wedge \neg p \) for an atom \( p \); both are false in every row. Replace \( \alpha \leftrightarrow \beta \) by \( (\alpha \to \beta) \wedge (\beta \to \alpha) \) and \( \alpha \to \beta \) by \( \neg\alpha \vee \beta \); push each \( \neg \) inwards by De Morgan's laws, and remove \( \neg\neg \); finally distribute \( \vee \) over \( \wedge \), replacing \( \alpha \vee (\beta \wedge \gamma) \) by \( (\alpha \vee \beta) \wedge (\alpha \vee \gamma) \). Each step replaces a part of the formula by an equivalent one: the equivalences are \( \bot \equiv p \wedge \neg p \) and those of @prp-standard-equivalences, which hold for arbitrary formulas, and @lem-replacement says the whole formula stays equivalent; since \( \equiv \) is transitive (Section 4.5), the steps chain. Stopping before the distribution step, and distributing \( \wedge \) over \( \vee \) instead, gives a DNF. The rewriting route is often much shorter than the table, as the next example shows, but it can also explode, as the warning after it shows.

::: {#exm-normal-forms-two-routes}
[Two routes to a normal form]

Put \( \varphi = (p \to q) \to (\neg q \to r) \) into DNF and into CNF, first from its truth table and then by rewriting.
:::

::: {.solution}
*The table route.* Work backwards from F (Section 4.4): \( \varphi \) is false exactly when \( p \to q \) is T and \( \neg q \to r \) is F. The latter needs \( \neg q \) true and \( r \) false, so \( q = r = \mathrm{F} \); then \( p \to q \) true needs \( p = \mathrm{F} \). So \( \varphi \) has exactly one F-row, \( p = q = r = \mathrm{F} \), as the table confirms:
\[
\begin{array}{ccc|c|c|c}
p & q & r & p \to q & \neg q \to r & (p \to q) \to (\neg q \to r) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F}
\end{array}
\]
The DNF of @thm-dnf has one minterm for each of the seven T-rows:
\[
\begin{aligned}
&(p \wedge q \wedge r) \vee (p \wedge q \wedge \neg r) \vee (p \wedge \neg q \wedge r) \vee (p \wedge \neg q \wedge \neg r) \\
&\quad \vee (\neg p \wedge q \wedge r) \vee (\neg p \wedge q \wedge \neg r) \vee (\neg p \wedge \neg q \wedge r).
\end{aligned}
\]
The CNF of @thm-cnf has one clause for the single F-row, built from the opposites of \( \neg p, \neg q, \neg r \): it is the single clause \( p \vee q \vee r \).

*The rewriting route.* Eliminate the three implications, then push the negation in:
\[
\begin{aligned}
\varphi &\equiv \neg(\neg p \vee q) \vee (\neg\neg q \vee r) \\
&\equiv (\neg\neg p \wedge \neg q) \vee (q \vee r) \\
&\equiv (p \wedge \neg q) \vee q \vee r ,
\end{aligned}
\]
using (c) of @prp-standard-equivalences three times, then De Morgan's law (b) for \( \neg(\alpha \vee \beta) \), then double negation (d) twice. This is already a DNF, with three conjunctive clauses. For a CNF, distribute, by (g) together with commutativity (f) and associativity (h): \( (p \wedge \neg q) \vee (q \vee r) \equiv (p \vee q \vee r) \wedge (\neg q \vee q \vee r) \). The second clause contains \( q \) and \( \neg q \), so it is true in every row, and a conjunction with a part that is true in every row is equivalent to its other part. So \( \varphi \equiv p \vee q \vee r \): one clause, as the table route found.

The formula \( p \vee q \vee r \) is also a DNF, with three conjunctive clauses of one literal each. So the table's seven minterms and the rewriting's three conjunctive clauses can both be replaced by three one-literal conjunctive clauses. Both routes are correct; they differ in length, and neither is guaranteed to give the shortest normal form.
:::

::: {.warning}
A formula has **many** equivalent CNFs and DNFs; "normal form" does not mean "unique form". \( p \vee q \vee r \) and \( (p \vee q \vee r) \wedge (\neg q \vee q \vee r) \) are both CNFs of the formula above. And the two routes have opposite weaknesses. The table route needs all \( 2^n \) rows for \( n \) atoms. The rewriting route can explode at the distribution step: distributing \( (p_1 \wedge q_1) \vee (p_2 \wedge q_2) \vee (p_3 \wedge q_3) \) gives 8 clauses, one for each way of picking \( p_i \) or \( q_i \) from every conjunctive clause, and \( m \) such conjunctive clauses give \( 2^m \) clauses.
:::

## Reading validity off a CNF

A CNF is a list of requirements, all of which must hold. That makes one question easy.

::: {#prp-cnf-validity}
[Validity of a CNF]

::: {.enumerate options="label=(\alph*)"}
1. A formula in CNF is a tautology exactly when **every** clause contains some atom together with its negation.
2. A formula in DNF is satisfiable exactly when **some** conjunctive clause contains no atom together with its negation.
:::
:::

*Try it first (ten minutes): take a clause in which no atom occurs both with and without \( \neg \), such as \( p \vee \neg q \vee r \). Can you find a row that makes it false? What does that row do to a CNF containing this clause?*

::: {.idea}
The direction "every clause has a pair \( \Rightarrow \) tautology" is the easy one: \( p \vee \neg p \) is true in every row, so a clause containing both is too, and a conjunction of clauses true in every row is true in every row. The attempt above is the other direction. To make a CNF false, it is enough to make **one** clause false, and a clause is false only when **all** its literals are. So set every atom of the clause against its literal: F for a plain atom, T for a negated one. The one thing that could stop us is an atom that appears both plain and negated, since it would have to be both F and T. That is exactly the pair the proposition talks about.
:::

::: {.proof}
*(a)* Let \( K = K_1 \wedge \dots \wedge K_k \) be in CNF.

\( (\Leftarrow) \) Suppose every clause \( K_i \) contains some atom \( p \) and its negation \( \neg p \). Let \( v \) be a valuation. One of \( p \), \( \neg p \) is true under \( v \), by @def-truth-value, so \( v(K_i) = \mathrm{T} \) by @eq-many-term-values. This holds for every \( i \), so \( v(K) = \mathrm{T} \) by @eq-many-term-values. As \( v \) was arbitrary, \( K \) is a tautology (@def-tautology).

\( (\Rightarrow) \) We prove the contrapositive. Suppose some clause \( K_i \) contains no atom together with its negation. Define a valuation \( v \) by: \( v(p) \coloneqq \mathrm{F} \) if the literal \( p \) occurs in \( K_i \); \( v(p) \coloneqq \mathrm{T} \) if the literal \( \neg p \) occurs in \( K_i \); \( v(p) \coloneqq \mathrm{T} \) for every other atom. This is well defined, because no atom occurs in \( K_i \) both as \( p \) and as \( \neg p \). Every literal of \( K_i \) is false under \( v \), so \( v(K_i) = \mathrm{F} \) by @eq-many-term-values, and hence \( v(K) = \mathrm{F} \), again by @eq-many-term-values. So \( K \) is not a tautology.

*(b)* Let \( D = C_1 \vee \dots \vee C_k \) be in DNF.

\( (\Leftarrow) \) Suppose \( C_i \) contains no atom together with its negation. Define \( v \) by \( v(p) \coloneqq \mathrm{T} \) if \( p \) occurs in \( C_i \), \( v(p) \coloneqq \mathrm{F} \) if \( \neg p \) occurs in \( C_i \), and \( v(p) \coloneqq \mathrm{T} \) otherwise; this is well defined as in (a). Every literal of \( C_i \) is true under \( v \), so \( v(C_i) = \mathrm{T} \) and \( v(D) = \mathrm{T} \) by @eq-many-term-values. So \( D \) is satisfiable (@def-satisfiable).

\( (\Rightarrow) \) If every conjunctive clause contains some \( p \) and \( \neg p \), then under every valuation one of these two literals is false, so every conjunctive clause is false and so is \( D \), by @eq-many-term-values. So \( D \) is not satisfiable. This proves the proposition.
:::

::: {.second-reading title="Two faces of one fact"}
The two parts are two faces of one fact. Section 4.5 showed that a formula is a tautology exactly when its negation is unsatisfiable (after @def-satisfiable). Let \( D \) be in DNF, and let \( K \) be the CNF whose clauses are the conjunctive clauses of \( D \) with every literal replaced by its opposite. The proof of @thm-cnf, applied to \( \varphi = \neg D \) with \( D \) itself as the DNF of \( \neg\varphi \equiv D \), shows \( K \equiv \neg D \). A clause of \( K \) has an atom together with its negation exactly when the corresponding conjunctive clause of \( D \) has. So \( D \) is unsatisfiable exactly when \( \neg D \), and so \( K \), is a tautology, which by (a) happens exactly when every conjunctive clause of \( D \) has such a pair. That is (b) again.
:::

The proposition trades one kind of work for another. Checking a CNF for validity is now a glance, but getting the CNF in the first place may take the \( 2^n \) rows of the table route or the explosion of the rewriting route. Nothing is free: the work has moved, not vanished.

::: {#exm-cnf-validity-glance}
[Validity at a glance]

Decide whether each formula is a tautology, without a table.

::: {.enumerate options="label=(\alph*)"}
1. \( (\neg p \vee q \vee p) \wedge (r \vee \neg q \vee s \vee q) \wedge (\neg s \vee \neg r \vee s) \wedge (p \vee \neg r \vee r \vee q) \).
2. The same formula with the third clause changed to \( \neg s \vee \neg r \vee q \).
:::
:::

::: {.solution}
*(a)* Each clause has a pair: \( \neg p, p \) in the first; \( \neg q, q \) in the second; \( \neg s, s \) in the third; \( \neg r, r \) in the fourth. By @prp-cnf-validity (a), it is a tautology. A table would have needed 16 rows.

*(b)* The new third clause \( \neg s \vee \neg r \vee q \) has the atoms \( s \), \( r \), \( q \), each once, so it has no pair, and the formula is not a tautology. The proof of @prp-cnf-validity names a refuting row: \( s = \mathrm{T} \), \( r = \mathrm{T} \), \( q = \mathrm{F} \), and \( p = \mathrm{T} \), like every atom not in the clause; in fact either value of \( p \) works. In that row the third clause is F, so the conjunction is F.
:::

## Calculating with equivalences

Section 4.5 replaced a part of a formula by an equivalent part (@lem-replacement) and chained such steps, since \( \equiv \) is transitive. Normal forms can be reached in this way, as the rewriting route did, and so can shorter formulas. Each step cites a law, as each line of a derivation cites a rule. A few more laws make the calculations run; in them, \( \neg\bot \) serves as a formula that is true in every row.

::: {#prp-more-equivalences}
[Laws of the Constants, Idempotence and Absorption]

For all formulas \( \varphi \) and \( \psi \):

::: {.enumerate options="label=(\alph*)"}
1. \( \varphi \wedge \neg\bot \equiv \varphi \) and \( \varphi \vee \bot \equiv \varphi \);
2. \( \varphi \wedge \bot \equiv \bot \) and \( \varphi \vee \neg\bot \equiv \neg\bot \);
3. \( \varphi \wedge \neg\varphi \equiv \bot \) and \( \varphi \vee \neg\varphi \equiv \neg\bot \);
4. \( \varphi \wedge \varphi \equiv \varphi \) and \( \varphi \vee \varphi \equiv \varphi \);
5. \( \varphi \wedge (\varphi \vee \psi) \equiv \varphi \) and \( \varphi \vee (\varphi \wedge \psi) \equiv \varphi \).
:::
:::

::: {.second-reading title="The tables for the further laws"}
::: {.proof}
As for @prp-standard-equivalences: fix a valuation \( v \), and let \( a = v(\varphi) \) and \( b = v(\psi) \). By (V1) and (V2) of @def-truth-value, \( v(\bot) = \mathrm{F} \) and \( v(\neg\bot) = \mathrm{T} \), so the value of each side under \( v \) is computed from \( a \) (and \( b \)) by the clauses of its connectives. The first table covers (a)–(d), with one row for each value of \( a \); the second covers (e), with one row for each pair \( (a, b) \).
\[
\begin{array}{c|cc|cc|cc|cc}
a & \varphi \wedge \neg\bot & \varphi \vee \bot & \varphi \wedge \bot & \varphi \vee \neg\bot & \varphi \wedge \neg\varphi & \varphi \vee \neg\varphi & \varphi \wedge \varphi & \varphi \vee \varphi \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F}
\end{array}
\qquad
\begin{array}{cc|cc}
a & b & \varphi \wedge (\varphi \vee \psi) & \varphi \vee (\varphi \wedge \psi) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F}
\end{array}
\]
In (a), (d) and (e) both columns agree with \( a \); in (b) and (c) the columns are constant, F where the right side is \( \bot \) and T where it is \( \neg\bot \). So both sides of each law have the same value under \( v \), and as \( v \) was arbitrary they are equivalent, by the paraphrase of @def-semantic-equivalence.
:::
:::

::: {#exm-simplify-by-calculation}
[Simplifying by a chain]

Simplify \( (p \to q) \wedge (p \to \neg q) \), citing a law at each step.
:::

::: {.solution}
\[
\begin{aligned}
(p \to q) \wedge (p \to \neg q) &\equiv (\neg p \vee q) \wedge (\neg p \vee \neg q) \\
&\equiv \neg p \vee (q \wedge \neg q) \\
&\equiv \neg p \vee \bot \\
&\equiv \neg p .
\end{aligned}
\]
Step 1 is (c) of @prp-standard-equivalences, used twice, each time applied inside the formula by @lem-replacement. Step 2 is (g), second form, read from right to left with \( \varphi = \neg p \), \( \psi = q \), \( \chi = \neg q \). Step 3 is (c) of @prp-more-equivalences, applied inside. Step 4 is (a).

Read the result: if \( p \) gives both \( q \) and not \( q \), then not \( p \). This is the table's face of \( \rulename{\neg I} \).
:::

::: {.check}
Simplify \( (p \vee q) \wedge (p \vee \neg q) \), citing a law at each step.
:::

::: {.solution}
\( (p \vee q) \wedge (p \vee \neg q) \equiv p \vee (q \wedge \neg q) \equiv p \vee \bot \equiv p \): (g) of @prp-standard-equivalences, second form, read from right to left; then (c) of @prp-more-equivalences, first form, applied inside by @lem-replacement; then its (a), second form.
:::

## Stronger and weaker parts

*Replacing a part by an equivalent part keeps the value of the whole (@lem-replacement). Replacing it by a stronger or a weaker part moves the value in one direction, and which direction depends on where the part sits.*

::: {#def-occurrence-polarity}
[Positive and Negative Occurrences]

Each node of the parse tree of a formula \( \chi \) (an **occurrence** of a subformula, Section 4.5) is **positive**, **negative**, or **unsigned**, by the path from the root: the root is positive; the part of a node \( \neg\theta \), and the left part of a node \( \theta_1 \to \theta_2 \), have the sign opposite to that node; the parts of a node \( \theta_1 \wedge \theta_2 \) or \( \theta_1 \vee \theta_2 \), and the right part of \( \theta_1 \to \theta_2 \), have the same sign as that node; the parts of a node \( \theta_1 \leftrightarrow \theta_2 \), and every node below them, are unsigned.
:::

In words: walk down from the root; the sign flips at each negation and at each hypothesis of an implication, and stays at every other step. A biconditional uses each part in both directions, as hypothesis and as conclusion, so below it nothing is signed. The sign is well defined because a formula has only one parse tree (Section 4.3).

```{=latex}
\begin{center}
\begin{tikzpicture}[level distance=11mm, every node/.style={font=\normalsize},
  level 1/.style={sibling distance=34mm}, level 2/.style={sibling distance=18mm}]
  \node[label=right:{$+$}] {$\wedge$}
    child { node[label=right:{$+$}] {$\to$}
      child { node[label=right:{$-$}] {$\neg$}
        child { node[label=right:{$+$}] {$p$} }
      }
      child { node[label=right:{$+$}] {$q$} }
    }
    child { node[label=right:{$+$}] {$\neg$}
      child { node[label=right:{$-$}] {$r$} }
    };
\end{tikzpicture}
\end{center}
```

*The parse tree of \( (\neg p \to q) \wedge \neg r \), each node with its sign. Signs flip at each \( \neg \) and on the left of each \( \to \): here \( p \) is positive (two flips), \( q \) positive, \( r \) negative.*

::: {#thm-monotonicity}
[Monotonicity]

Let \( \alpha \models \beta \), and let \( \chi' \) be obtained from \( \chi \) by replacing one occurrence of \( \alpha \) by \( \beta \). If the occurrence is positive, then \( \chi \models \chi' \); if it is negative, then \( \chi' \models \chi \).
:::

In words: a stronger part in a positive place makes the whole stronger; in a negative place, weaker. Two readings are used daily. **A stronger hypothesis gives a weaker theorem**: the hypothesis of \( \alpha \to \theta \) is negative, so from \( \alpha \models \beta \) we get \( (\beta \to \theta) \models (\alpha \to \theta) \). **It suffices to prove something stronger**: the conclusion is positive, so from \( \alpha \models \beta \) we get \( (\theta \to \alpha) \models (\theta \to \beta) \). For example, from \( p \wedge q \models p \) the theorem gives \( (r \to (p \wedge q)) \models (r \to p) \) and \( (p \to r) \models ((p \wedge q) \to r) \).

::: {.idea}
Induct on \( \chi \), as for @lem-replacement. There the replaced part kept its value, and so did the whole. Here truth passes one way only: from the old part to the new one, and up through \( \wedge \), \( \vee \) and the right of \( \to \) unchanged; at a \( \neg \) and at the left of a \( \to \) the direction turns round, exactly where the sign flips.
:::

::: {.second-reading title="The proof of monotonicity"}
::: {.proof}
We apply @thm-structural-induction to the property \( M(\chi) \): *for every positive or negative occurrence of \( \alpha \) in \( \chi \), with \( \chi' \) the result of replacing it by \( \beta \), and every valuation \( v \): if the occurrence is positive, \( v(\chi) = \mathrm{T} \) implies \( v(\chi') = \mathrm{T} \); if it is negative, \( v(\chi') = \mathrm{T} \) implies \( v(\chi) = \mathrm{T} \).* By @def-valid-argument, these say \( \chi \models \chi' \) and \( \chi' \models \chi \).

*Signs inside a part.* Let \( \theta \) be an immediate part of \( \chi \). The parse tree of \( \theta \) is a subtree of that of \( \chi \) (@def-parse-tree), and the path from the root of \( \chi \) to a node of \( \theta \) is the path from the root of \( \theta \) with one step on top. So the node's sign in \( \chi \) is its sign in \( \theta \) if \( \theta \) is positive in \( \chi \), the opposite sign if \( \theta \) is negative, and none if \( \theta \) is unsigned.

If the occurrence is the root, it is positive, \( \chi = \alpha \) and \( \chi' = \beta \), and \( v(\alpha) = \mathrm{T} \) implies \( v(\beta) = \mathrm{T} \) because \( \alpha \models \beta \). An atom or \( \bot \) has no other node. Otherwise the occurrence lies in one immediate part, and \( \chi' \) is \( \chi \) with that part \( \theta \) replaced by the result \( \theta' \) of the replacement inside it.

*\( \chi = \neg\theta \).* The part is negative, so the occurrence has opposite signs in \( \chi \) and in \( \theta \). If it is positive in \( \chi \), it is negative in \( \theta \), and \( M(\theta) \) gives: \( v(\theta') = \mathrm{T} \) implies \( v(\theta) = \mathrm{T} \). So if \( v(\neg\theta) = \mathrm{T} \), then \( v(\theta) = \mathrm{F} \), hence \( v(\theta') = \mathrm{F} \), and \( v(\neg\theta') = \mathrm{T} \) by (V2). If it is negative in \( \chi \), the same argument runs with \( \theta \) and \( \theta' \) exchanged.

*\( \chi = \theta_1 \wedge \theta_2 \) or \( \theta_1 \vee \theta_2 \).* Both parts are positive, so the signs in \( \chi \) and in the part agree. Clauses (V3) and (V4) are monotone in each part: if a part is replaced by one that is true whenever it was, a true conjunction or disjunction stays true. With \( M \) of the part, this gives the claim in both cases.

*\( \chi = \theta_1 \to \theta_2 \).* In \( \theta_2 \) the signs agree, and (V5) is monotone in the conclusion: if \( v(\theta_2) = \mathrm{T} \) implies \( v(\theta_2') = \mathrm{T} \), then \( v(\theta_1 \to \theta_2) = \mathrm{T} \) implies \( v(\theta_1 \to \theta_2') = \mathrm{T} \). In \( \theta_1 \) the signs are opposite, and (V5) is antitone in the hypothesis: if \( v(\theta_1') = \mathrm{T} \) implies \( v(\theta_1) = \mathrm{T} \), then \( v(\theta_1 \to \theta_2) = \mathrm{T} \) implies \( v(\theta_1' \to \theta_2) = \mathrm{T} \), since a false \( \theta_1 \) leaves \( \theta_1' \) false. An occurrence positive in \( \chi \) is negative in \( \theta_1 \), so \( M(\theta_1) \) supplies exactly this premise; a negative one is positive in \( \theta_1 \), and the argument runs with \( \theta_1 \) and \( \theta_1' \) exchanged.

*\( \chi = \theta_1 \leftrightarrow \theta_2 \).* Every node below the root is unsigned, so there is no occurrence to treat.

By @thm-structural-induction, \( M(\chi) \) holds for every formula \( \chi \). This proves the theorem.
:::
:::

::: {.check}
Give the sign of each atom occurrence in \( \neg(p \to q) \vee r \).
:::

::: {.solution}
\( p \) is positive: flipped by the \( \neg \), and again as the hypothesis of \( \to \). \( q \) is negative: flipped by the \( \neg \) only. \( r \) is positive.
:::

::: {.warning}
Below a \( \leftrightarrow \) nothing may be strengthened. \( p \wedge q \models p \), but \( (p \wedge q) \leftrightarrow r \) and \( p \leftrightarrow r \) entail each other in neither direction: the row \( p = \mathrm{T} \), \( q = r = \mathrm{F} \) makes the first true and the second false, and the row \( p = r = \mathrm{T} \), \( q = \mathrm{F} \) does the reverse.
:::

## Adequate sets of connectives

Our formulas use five connectives and \( \bot \). Chapter 2 already showed that some of them can be traded for others: an implication for a disjunction (@prp-implication-as-disjunction), a biconditional for two implications (@prp-iff-two-implications). How far can this go? Before we can answer, we need to say what a set of connectives must be able to "say".

Every formula whose atoms are among \( p_1, \dots, p_n \) has a truth table: a value for each of the \( 2^n \) rows. Turn this around, and ask whether **every** table is the table of some formula.

Section 4.4 called such a table a **truth function** (@def-truth-function): a value for each list of inputs, with no formula attached; a formula **expresses** it when it has that table.

There are \( 2^n \) lists of inputs and two choices of output for each, so there are \( 2^{2^n} \) truth functions with \( n \) inputs: \( 4 \) with one input and \( 16 \) with two. Examples: the **negation** function with one input, \( \mathrm{T} \mapsto \mathrm{F} \), \( \mathrm{F} \mapsto \mathrm{T} \), expressed by \( \neg p_1 \); the two-input function that is T only at \( (\mathrm{T}, \mathrm{T}) \), expressed by \( p_1 \wedge p_2 \); the three-input **majority** function, T when at least two inputs are T, expressed by \( (p_1 \wedge p_2) \vee (p_1 \wedge p_3) \vee (p_2 \wedge p_3) \). A degenerate case: the one-input function that is always T is expressed by \( p_1 \vee \neg p_1 \), and also by \( p_2 \to p_2 \), which does not mention \( p_1 \) at all. The definition allows that.

We say a formula is **in** a set \( S \) of connectives if every connective occurring in it belongs to \( S \), and \( \bot \) occurs in it only if \( \bot \) belongs to \( S \) (for this purpose \( \bot \) counts as a connective with no inputs).

::: {#def-adequate}
[Adequate Set of Connectives]

A set \( S \) of connectives is **adequate** if **every** truth function, with **any** number \( n \ge 1 \) of inputs, is expressed by some formula in \( S \).
:::

A set containing an adequate set is adequate, since a formula in the smaller set is also in the larger one. The theorem below shows that \( \{\neg, \wedge, \vee\} \) is adequate, so the full set \( \{\neg, \wedge, \vee, \to, \leftrightarrow, \bot\} \) is too. The question is which smaller sets are.

**Rewriting "or" with "not" and "and".** The DNF of a truth table uses \( \neg \), \( \wedge \) and \( \vee \). To do without \( \vee \), rewrite each disjunction by De Morgan's law: \( \alpha \vee \beta \) has the same table as \( \neg(\neg\alpha \wedge \neg\beta) \). Done everywhere, from the leaves up, this is a translation \( t_1 \) of the formulas built from atoms with \( \neg \), \( \wedge \), \( \vee \) (the proof below gives the clauses for \( \bot \), \( \to \), \( \leftrightarrow \)): \( t_1(p) = p \), \( t_1(\neg\alpha) = \neg t_1(\alpha) \), \( t_1(\alpha \wedge \beta) = t_1(\alpha) \wedge t_1(\beta) \), \( t_1(\alpha \vee \beta) = \neg(\neg t_1(\alpha) \wedge \neg t_1(\beta)) \). For instance
\[
t_1\bigl( (p \vee q) \wedge \neg r \bigr) = \neg(\neg p \wedge \neg q) \wedge \neg r .
\]
In the row \( p = \mathrm{F} \), \( q = \mathrm{T} \), \( r = \mathrm{F} \) both sides are T: on the left \( p \vee q \) and \( \neg r \) are T; on the right \( \neg p \wedge \neg q \) is F, so its negation is T, and \( \neg r \) is T. Two more translations do the same for the other sets of the theorem below:

| | \( t_1 \), into \( \{\neg, \wedge\} \) | \( t_2 \), into \( \{\neg, \vee\} \) | \( t_3 \), into \( \{\to, \bot\} \) |
|---|---|---|---|
| \( \neg\alpha \) | \( \neg t_1(\alpha) \) | \( \neg t_2(\alpha) \) | \( t_3(\alpha) \to \bot \) |
| \( \alpha \wedge \beta \) | \( t_1(\alpha) \wedge t_1(\beta) \) | \( \neg(\neg t_2(\alpha) \vee \neg t_2(\beta)) \) | \( (t_3(\alpha) \to (t_3(\beta) \to \bot)) \to \bot \) |
| \( \alpha \vee \beta \) | \( \neg(\neg t_1(\alpha) \wedge \neg t_1(\beta)) \) | \( t_2(\alpha) \vee t_2(\beta) \) | \( (t_3(\alpha) \to \bot) \to t_3(\beta) \) |

::: {.check}
Use the translation \( t_3 \) to express \( p \wedge q \) with \( \to \) and \( \bot \) only, and check your formula in the row \( p = \mathrm{T} \), \( q = \mathrm{F} \).
:::

::: {.solution}
\( t_3(p \wedge q) = (p \to (q \to \bot)) \to \bot \). In the row \( p = \mathrm{T} \), \( q = \mathrm{F} \): \( q \to \bot \) is \( \mathrm{F} \to \mathrm{F} \), so T; then \( p \to (q \to \bot) \) is T; then the whole is \( \mathrm{T} \to \bot \), so F, which agrees with \( p \wedge q \).
:::

::: {#thm-adequate-connectives}
[Adequate Sets]

::: {.enumerate options="label=(\alph*)"}
1. The sets \( \{\neg, \wedge, \vee\} \), \( \{\neg, \wedge\} \), \( \{\neg, \vee\} \) and \( \{\to, \bot\} \) are adequate.
2. The set \( \{\wedge, \vee, \to\} \) is not adequate: no formula in it expresses the negation function.
:::
:::

::: {.idea}
For (a), the construction of @thm-dnf works for any table, not only for the table of a formula, and its output uses only \( \neg \), \( \wedge \), \( \vee \). To shrink the set further, rewrite each missing connective in terms of the others, for instance \( \alpha \vee \beta \) as \( \neg(\neg\alpha \wedge \neg\beta) \), recursively through the formula. For (b), look at the row where every atom is true: \( \wedge \), \( \vee \) and \( \to \) all give T on T inputs, so every formula in them is T there, while negation must give F.
:::

::: {.proof}
*(a)* *The set \( \{\neg, \wedge, \vee\} \).* Let \( f \) be a truth function with \( n \ge 1 \) inputs. For each of the \( 2^n \) lists of inputs, fix a valuation taking those values at \( p_1, \dots, p_n \), and let \( v_1, \dots, v_k \) be those fixed for the lists where \( f \) is T. If \( k \ge 1 \), let \( D \coloneqq C_{v_1} \vee \dots \vee C_{v_k} \), with the minterms \( C_{v} \) formed from \( p_1, \dots, p_n \); if \( k = 0 \), let \( D \coloneqq p_1 \wedge \neg p_1 \). By @eq-many-term-values and @eq-row-conjunct, a valuation \( w \) makes \( D \) true exactly when \( (w(p_1), \dots, w(p_n)) \) is a list where \( f \) is T, that is, when \( f(w(p_1), \dots, w(p_n)) = \mathrm{T} \). So \( D \) expresses \( f \), and \( D \) is in \( \{\neg, \wedge, \vee\} \).

*The other three sets.* By @thm-structural-recursion, the following clauses define three functions \( t_1, t_2, t_3 \) on all formulas. Each has \( t_i(p) \coloneqq p \) for every atom \( p \), and \( t_i(\bot) \coloneqq \bot \), \( t_i(\alpha \to \beta) \coloneqq t_i(\alpha) \to t_i(\beta) \) and \( t_i(\alpha \leftrightarrow \beta) \coloneqq t_i(\alpha) \leftrightarrow t_i(\beta) \) (these last clauses are never used below). The other clauses rewrite the connectives \( \neg \), \( \wedge \), \( \vee \):

- \( t_1 \), into \( \{\neg, \wedge\} \): \( t_1(\neg\alpha) \coloneqq \neg t_1(\alpha) \), \( t_1(\alpha \wedge \beta) \coloneqq t_1(\alpha) \wedge t_1(\beta) \), and \( t_1(\alpha \vee \beta) \coloneqq \neg(\neg t_1(\alpha) \wedge \neg t_1(\beta)) \);
- \( t_2 \), into \( \{\neg, \vee\} \): \( t_2(\neg\alpha) \coloneqq \neg t_2(\alpha) \), \( t_2(\alpha \wedge \beta) \coloneqq \neg(\neg t_2(\alpha) \vee \neg t_2(\beta)) \), and \( t_2(\alpha \vee \beta) \coloneqq t_2(\alpha) \vee t_2(\beta) \);
- \( t_3 \), into \( \{\to, \bot\} \): \( t_3(\neg\alpha) \coloneqq t_3(\alpha) \to \bot \), \( t_3(\alpha \wedge \beta) \coloneqq (t_3(\alpha) \to (t_3(\beta) \to \bot)) \to \bot \), and \( t_3(\alpha \vee \beta) \coloneqq (t_3(\alpha) \to \bot) \to t_3(\beta) \).

::: {.claim}
Let \( S_1 = \{\neg, \wedge\} \), \( S_2 = \{\neg, \vee\} \), \( S_3 = \{\to, \bot\} \). For every formula \( \varphi \) in \( \{\neg, \wedge, \vee\} \) and each \( i \), the formula \( t_i(\varphi) \) is in \( S_i \), and \( v(t_i(\varphi)) = v(\varphi) \) for every valuation \( v \).
:::

::: {.proofofclaim}
By structural induction (@thm-structural-induction) on \( \varphi \), with the property "if \( \varphi \) is in \( \{\neg, \wedge, \vee\} \), then for each \( i \), \( t_i(\varphi) \) is in \( S_i \) and has the same value as \( \varphi \) under every valuation". The immediate parts of a formula in \( \{\neg, \wedge, \vee\} \) are in \( \{\neg, \wedge, \vee\} \), so the induction hypothesis applies to them. For \( \bot \), \( \alpha \to \beta \) and \( \alpha \leftrightarrow \beta \) the property holds vacuously, since these formulas are not in \( \{\neg, \wedge, \vee\} \). For an atom, \( t_i(p) = p \). In the other cases, write \( a = v(t_i(\alpha)) = v(\alpha) \) and \( b = v(t_i(\beta)) = v(\beta) \), by the induction hypothesis. Each clause for \( t_i \) above uses only the connectives of \( S_i \), applied to formulas in \( S_i \), so \( t_i(\varphi) \) is in \( S_i \). For the values, use @def-truth-value, and that \( \chi \to \bot \) is true exactly when \( \chi \) is false (\( \bot \) is always F):

- \( \neg t_i(\alpha) \) and \( t_3(\alpha) \to \bot \) are true exactly when \( a = \mathrm{F} \), as is \( \neg\alpha \).
- \( \neg(\neg t_2(\alpha) \vee \neg t_2(\beta)) \) is true exactly when neither \( \neg t_2(\alpha) \) nor \( \neg t_2(\beta) \) is, that is, when \( a = b = \mathrm{T} \). And \( (t_3(\alpha) \to (t_3(\beta) \to \bot)) \to \bot \) is true exactly when \( t_3(\alpha) \to (t_3(\beta) \to \bot) \) is false, that is, when \( a = \mathrm{T} \) and \( t_3(\beta) \to \bot \) is false, that is, when \( a = b = \mathrm{T} \). Both agree with \( \alpha \wedge \beta \).
- \( \neg(\neg t_1(\alpha) \wedge \neg t_1(\beta)) \) is true exactly when \( a \) and \( b \) are not both F. And \( (t_3(\alpha) \to \bot) \to t_3(\beta) \) is true exactly when \( t_3(\alpha) \to \bot \) is false or \( b = \mathrm{T} \), that is, when \( a = \mathrm{T} \) or \( b = \mathrm{T} \). Both agree with \( \alpha \vee \beta \).

The remaining clauses, for \( t_1(\alpha \wedge \beta) \) and \( t_2(\alpha \vee \beta) \), keep the connective and have the right value by the induction hypothesis.
:::

Now let \( f \) be any truth function, and \( D \) the formula in \( \{\neg, \wedge, \vee\} \) that expresses it. By the Claim, \( t_i(D) \) is in \( S_i \) and \( v(t_i(D)) = v(D) = f(v(p_1), \dots, v(p_n)) \) for every valuation \( v \). So each \( S_i \) is adequate.

*(b)* Let \( v_{\mathrm{T}} \) be the valuation with \( v_{\mathrm{T}}(p) = \mathrm{T} \) for every atom \( p \). We show by structural induction that every formula in \( \{\wedge, \vee, \to\} \) is true under \( v_{\mathrm{T}} \); the property is "if \( \varphi \) is in \( \{\wedge, \vee, \to\} \), then \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \)". For an atom, \( v_{\mathrm{T}}(p) = \mathrm{T} \). The formulas \( \bot \), \( \neg\alpha \) and \( \alpha \leftrightarrow \beta \) are not in the set, so for them the property holds vacuously. If \( \varphi \) is \( \alpha \wedge \beta \), \( \alpha \vee \beta \) or \( \alpha \to \beta \) and is in the set, then so are \( \alpha \) and \( \beta \), and by the induction hypothesis \( v_{\mathrm{T}}(\alpha) = v_{\mathrm{T}}(\beta) = \mathrm{T} \). By @def-truth-value, \( v_{\mathrm{T}}(\alpha \wedge \beta) = \mathrm{T} \) and \( v_{\mathrm{T}}(\alpha \vee \beta) = \mathrm{T} \); and \( v_{\mathrm{T}}(\alpha \to \beta) = \mathrm{T} \) because its conclusion \( \beta \) is true. By @thm-structural-induction, every formula in the set is true under \( v_{\mathrm{T}} \).

Now suppose some \( \varphi \) in \( \{\wedge, \vee, \to\} \) expressed the negation function \( f \). Then \( v_{\mathrm{T}}(\varphi) = f(v_{\mathrm{T}}(p_1)) = f(\mathrm{T}) = \mathrm{F} \), contradicting \( v_{\mathrm{T}}(\varphi) = \mathrm{T} \). So no such \( \varphi \) exists, and the set is not adequate. This proves the theorem.
:::

In the implication case of (b), the reason is that the **conclusion** \( \beta \) is true. That is where a careless argument goes wrong, and @exr-valuations-and-truth-tables-c2 asked you to find a "proof" that goes wrong there.

The five connectives were chosen because each matches a word mathematicians use, not because they are needed: two suffice, and @exr-normal-forms-c1 shows that one well-chosen connective suffices.

::: {.warning}
The \( \bot \) in \( \{\to, \bot\} \) is essential. Without it, \( \{\to\} \) is not adequate: every formula in \( \{\to\} \) is also in \( \{\wedge, \vee, \to\} \), so by (b) of @thm-adequate-connectives none expresses negation. Implication alone cannot say "false"; implication together with a formula that is always false can.
:::

## Exercises

### A. Check your understanding

::: {#exr-normal-forms-a1}
[A1]

::: {.enumerate options="label=(\alph*)"}
1. Which of \( \neg p \), \( \neg\neg q \), \( \bot \), \( r \) and \( \neg(p \vee q) \) are literals?
2. Classify each as a clause, a conjunctive clause, both, or neither: \( p \vee \neg q \); \( \neg r \); \( p \wedge (q \vee r) \).
3. Is \( (p \vee q) \wedge (\neg p \vee p \vee r) \) a tautology? Is \( (q \vee \neg q) \wedge (\neg r \vee p \vee r) \)? Give a refuting row where the answer is no.
4. Give a formula in DNF that is not satisfiable.
5. True or false: every formula in CNF with only one clause is also in DNF.
:::
:::

::: {.solution}
*(a)* \( \neg p \) and \( r \). \( \neg\neg q \) has two negations, \( \bot \) is not an atom, and \( \neg(p \vee q) \) negates a disjunction.

*(b)* \( p \vee \neg q \) is a clause. \( \neg r \) is both (one literal). \( p \wedge (q \vee r) \) is neither: its part \( q \vee r \) is not a literal.

*(c)* The first is not a tautology: its first clause \( p \vee q \) has no pair, and the row \( p = q = \mathrm{F} \) (any \( r \)) makes it false, hence the whole conjunction. The second is: each clause has a pair (\( q, \neg q \) and \( r, \neg r \)), by @prp-cnf-validity (a).

*(d)* \( p \wedge \neg p \): its one conjunctive clause contains a pair, so by @prp-cnf-validity (b) it is not satisfiable.

*(e)* True. A single clause \( \ell_1 \vee \dots \vee \ell_m \) is a disjunction of \( m \) conjunctive clauses of one literal each.
:::

::: {#exr-normal-forms-a2}
[A2: Drill]

The parts run from one step of a calculation, through signs and what monotonicity gives, to normal forms and an adequate set.

::: {.enumerate options="label=(\alph*)"}
1. Simplify \( p \wedge (p \vee q) \).
2. Simplify \( \neg(p \to q) \).
3. Simplify \( (p \vee q) \wedge \neg p \).
4. Simplify \( (p \wedge q) \vee (p \wedge \neg q) \).
5. What is the sign of \( p \) in \( \neg(p \to q) \)?
6. What is the sign of \( q \) in \( (p \to \neg q) \wedge r \)?
7. What is the sign of \( p \) in \( p \leftrightarrow q \)?
8. From \( p \wedge q \models p \), what does @thm-monotonicity give for \( r \to (p \wedge q) \)?
9. Give a DNF of \( p \leftrightarrow q \).
10. Give a CNF of \( p \leftrightarrow q \).
11. How many minterms has the DNF of @thm-dnf for a tautology whose atoms are \( p \), \( q \), \( r \)?
12. Is \( \{\neg, \to\} \) adequate?
:::
:::

::: {.solution}
(a) \( p \), by @prp-more-equivalences (e).

(b) \( p \wedge \neg q \): (c), then (b), then (d) of @prp-standard-equivalences give \( \neg(\neg p \vee q) \), \( \neg\neg p \wedge \neg q \), \( p \wedge \neg q \).

(c) \( \neg p \wedge q \): distributivity and commutativity give \( (p \wedge \neg p) \vee (q \wedge \neg p) \); then (c) of @prp-more-equivalences gives \( \bot \vee (q \wedge \neg p) \), and (a) with commutativity gives \( \neg p \wedge q \).

(d) \( p \): (g) read from right to left gives \( p \wedge (q \vee \neg q) \), then (c) and (a) of @prp-more-equivalences.

(e) Positive: the \( \neg \) flips it, and so does the hypothesis place of \( \to \).

(f) Negative: the right side of \( \to \) keeps the sign, the \( \neg \) flips it.

(g) Unsigned: it is a part of a biconditional.

(h) \( (r \to (p \wedge q)) \models (r \to p) \): \( p \wedge q \) sits in the conclusion, a positive place.

(i) \( (p \wedge q) \vee (\neg p \wedge \neg q) \), one minterm per T-row.

(j) \( (\neg p \vee q) \wedge (p \vee \neg q) \), one clause per F-row.

(k) \( 8 \): one for each of the eight rows, since all are T-rows.

(l) Yes: \( \alpha \vee \beta \equiv \neg\alpha \to \beta \), so a formula in \( \{\neg, \vee\} \), adequate by @thm-adequate-connectives, can be rewritten into \( \{\neg, \to\} \), from the leaves up.
:::

### B. Practice

::: {#exr-normal-forms-b1}
[B1: Normal forms of three formulas]

Find a DNF and a CNF of each formula, by either route, and check one of them in two rows.

::: {.enumerate options="label=(\alph*)"}
1. \( p \leftrightarrow \neg q \).
2. \( (p \wedge q) \to r \).
3. \( \neg(p \vee (q \to r)) \).
:::
:::

::: {.solution}
*(a)* By the table: \( p \leftrightarrow \neg q \) is true when \( p \) and \( q \) have opposite values, so its T-rows are T, F and F, T, and its F-rows are T, T and F, F. DNF: \( (p \wedge \neg q) \vee (\neg p \wedge q) \), as in @exm-dnf-exclusive-or. CNF, one clause per F-row from the opposite literals: the row T, T gives \( \neg p \vee \neg q \) and the row F, F gives \( p \vee q \), so \( (\neg p \vee \neg q) \wedge (p \vee q) \). Check the CNF: in the row T, F both clauses are true, and so is \( p \leftrightarrow \neg q \); in the row T, T the first clause is false, and so is \( p \leftrightarrow \neg q \).

*(b)* By rewriting: \( (p \wedge q) \to r \equiv \neg(p \wedge q) \vee r \equiv \neg p \vee \neg q \vee r \). This is a single clause, so it is a CNF, and it is also a DNF with three one-literal conjunctive clauses. Check: in the row T, T, F it is false (every literal false), as is \( (p \wedge q) \to r \); in the row F, T, F it is true, as is the original (its hypothesis is false).

*(c)* By rewriting: \( \neg(p \vee (q \to r)) \equiv \neg p \wedge \neg(q \to r) \equiv \neg p \wedge \neg(\neg q \vee r) \equiv \neg p \wedge q \wedge \neg r \). This single conjunctive clause is a DNF, and it is also a CNF with three one-literal clauses. Check: in the row F, T, F it is true, and so is the original (\( q \to r \) is false and \( p \) is false); in the row F, T, T it is false, and so is the original (\( q \to r \) is true).
:::

::: {#exr-normal-forms-b2}
[B2: Two connectives from two]

Find formulas in \( \{\neg, \wedge\} \), with atoms \( p \) and \( q \), equivalent to \( p \vee q \) and to \( p \leftrightarrow q \). Check the second by a truth table.
:::

::: {.solution}
\( p \vee q \equiv \neg(\neg p \wedge \neg q) \): this is the translation \( t_1 \) in the proof of @thm-adequate-connectives, and the right side is F exactly when \( \neg p \) and \( \neg q \) are both true, that is, when \( p \vee q \) is F.

For the biconditional, \( p \leftrightarrow q \) says \( p \to q \) and \( q \to p \), and \( p \to q \) says "not \( p \) without \( q \)", that is, \( \neg(p \wedge \neg q) \). So \( p \leftrightarrow q \equiv \neg(p \wedge \neg q) \wedge \neg(\neg p \wedge q) \). The table:
\[
\begin{array}{cc|c|c|c|c}
p & q & \neg(p \wedge \neg q) & \neg(\neg p \wedge q) & \neg(p \wedge \neg q) \wedge \neg(\neg p \wedge q) & p \leftrightarrow q \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T}
\end{array}
\]
The last two columns agree in every row.
:::

::: {#exr-normal-forms-b3}
[B3: Odd parity]

Give an example of a formula in DNF, with atoms \( p \), \( q \), \( r \), that is true in exactly the rows where an **odd** number of \( p \), \( q \), \( r \) are true. List the properties your answer must have, and check it against them.
:::

::: {.solution}
The rows with an odd number of T's are those with three T's, T T T, and those with one, T F F, F T F, and F F T. One minterm per row, as in @thm-dnf:
\[
(p \wedge q \wedge r) \vee (p \wedge \neg q \wedge \neg r) \vee (\neg p \wedge q \wedge \neg r) \vee (\neg p \wedge \neg q \wedge r).
\]
The properties an answer must have: (i) it is in DNF (a disjunction of conjunctions of literals); (ii) its atoms are among \( p \), \( q \), \( r \); (iii) it is T in the four rows T T T, T F F, F T F, F F T; (iv) it is F in the other four, T T F, T F T, F T T, F F F. Check: (i) and (ii) hold by inspection. By @eq-row-conjunct, each minterm is T in its own row only, so the disjunction is T exactly in the four rows listed, which gives (iii) and (iv).

A different correct answer, for instance the same minterms in another order, or with the literals of a minterm reordered, passes the same checks. No DNF with fewer conjunctive clauses works. A conjunctive clause containing an atom and its negation is T in no row and contributes nothing. Any other conjunctive clause omitting an atom, say \( p \wedge q \), is T in two rows that differ at that atom, and changing one atom always changes the parity, so one of those rows has even parity. So every conjunctive clause that is T somewhere mentions all three atoms and is T in exactly one row, and four T-rows need at least four conjunctive clauses.
:::

### C. Going deeper

::: {#exr-normal-forms-c1}
[C1: One connective is enough]

Add to the language two binary connectives: \( \alpha \mathbin{|} \beta \) ("not both", NAND), which is F exactly when \( \alpha \) and \( \beta \) are both T, and \( \alpha \downarrow \beta \) ("neither", NOR), which is T exactly when \( \alpha \) and \( \beta \) are both F.

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \{\mathbin{|}\} \) is adequate.
2. Prove that \( \{\downarrow\} \) is adequate.
:::
:::

::: {.solution}
*(a)* First, two equivalences, checked from the table of \( \mathbin{|} \): \( \alpha \mathbin{|} \alpha \) is F exactly when \( \alpha \) is T, so \( \alpha \mathbin{|} \alpha \equiv \neg\alpha \); and \( (\alpha \mathbin{|} \beta) \mathbin{|} (\alpha \mathbin{|} \beta) \equiv \neg(\alpha \mathbin{|} \beta) \), which is T exactly when \( \alpha \) and \( \beta \) are both T, so it is equivalent to \( \alpha \wedge \beta \). Now define, by recursion on formulas as in @thm-structural-recursion, \( s(p) \coloneqq p \), \( s(\neg\alpha) \coloneqq s(\alpha) \mathbin{|} s(\alpha) \), \( s(\alpha \wedge \beta) \coloneqq (s(\alpha) \mathbin{|} s(\beta)) \mathbin{|} (s(\alpha) \mathbin{|} s(\beta)) \) (the other clauses do not matter). By structural induction, exactly as in the Claim in the proof of @thm-adequate-connectives, every formula \( \varphi \) in \( \{\neg, \wedge\} \) has \( s(\varphi) \) in \( \{\mathbin{|}\} \) and \( v(s(\varphi)) = v(\varphi) \) for every \( v \): the atom case is immediate, and the two equivalences above give the \( \neg \) and \( \wedge \) cases from the induction hypothesis. Given a truth function \( f \), @thm-adequate-connectives (a) gives a formula \( \varphi \) in \( \{\neg, \wedge\} \) expressing it, and then \( s(\varphi) \) expresses \( f \) and is in \( \{\mathbin{|}\} \).

*(b)* The same, with \( \{\neg, \vee\} \): \( \alpha \downarrow \alpha \) is T exactly when \( \alpha \) is F, so \( \alpha \downarrow \alpha \equiv \neg\alpha \); and \( (\alpha \downarrow \beta) \downarrow (\alpha \downarrow \beta) \equiv \neg(\alpha \downarrow \beta) \equiv \alpha \vee \beta \). The recursive translation \( s(\neg\alpha) \coloneqq s(\alpha) \downarrow s(\alpha) \), \( s(\alpha \vee \beta) \coloneqq (s(\alpha) \downarrow s(\beta)) \downarrow (s(\alpha) \downarrow s(\beta)) \) turns a formula in \( \{\neg, \vee\} \) expressing \( f \) into one in \( \{\downarrow\} \).

(Recursion and structural induction for the language with the new connectives hold by the same proofs as @thm-structural-recursion and @thm-structural-induction, with one more formation clause.)

**Marking scheme.** (10 points)

- 3: (a) two equivalences expressing the connectives of an adequate set from @thm-adequate-connectives (a) in terms of \( \mathbin{|} \), read off its table (for instance \( \alpha \mathbin{|} \alpha \equiv \neg\alpha \) and \( (\alpha \mathbin{|} \beta) \mathbin{|} (\alpha \mathbin{|} \beta) \equiv \alpha \wedge \beta \)).
- 3: (a) the recursive translation and the structural induction showing that it keeps the value under every valuation.
- 1: (a) the conclusion, via @thm-adequate-connectives (a).
- 3: (b) the same for \( \downarrow \), with \( \{\neg, \vee\} \).

Fatal errors (0 for the step): checking the translation on examples only, with no induction.
:::

::: {#exr-normal-forms-c2}
[C2: Two sets that are not adequate]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \{\wedge, \vee, \to, \leftrightarrow\} \) is not adequate.
2. Add to the language a three-place connective \( \mathsf{M}(\alpha, \beta, \gamma) \), **majority**, which is T exactly when at least two of \( \alpha \), \( \beta \), \( \gamma \) are T. Prove that \( \{\neg, \mathsf{M}\} \) is not adequate.
:::
:::

::: {.solution}
[Hint 1]

For (b): compare each row with the row in which every atom's value is flipped.
:::

::: {.solution}
[Hint 2]

For (b): show that every formula in \( \neg \) and \( \mathsf{M} \) takes opposite values in a row and in its flipped row.
:::

::: {.solution}
*(a)* Let \( v_{\mathrm{T}} \) make every atom true. Every formula in \( \{\wedge, \vee, \to, \leftrightarrow\} \) is true under \( v_{\mathrm{T}} \), by the structural induction in the proof of @thm-adequate-connectives (b) with one more case: if \( v_{\mathrm{T}}(\alpha) = v_{\mathrm{T}}(\beta) = \mathrm{T} \), then \( v_{\mathrm{T}}(\alpha \leftrightarrow \beta) = \mathrm{T} \), since the two values are equal. As there, no such formula expresses negation, which must give F at the input T.

*(b)* For a valuation \( v \), let \( \bar v \) be the **flipped** valuation: \( \bar v(p) \) is the opposite of \( v(p) \), for every atom \( p \). We show by structural induction that every formula \( \varphi \) in \( \{\neg, \mathsf{M}\} \) satisfies: for every valuation \( v \), \( \bar v(\varphi) \) is the opposite of \( v(\varphi) \). For an atom this is the definition of \( \bar v \). If \( \bar v(\alpha) \) is the opposite of \( v(\alpha) \), then \( \bar v(\neg\alpha) \), the opposite of \( \bar v(\alpha) \), is \( v(\alpha) \), which is the opposite of \( v(\neg\alpha) \). If the property holds for \( \alpha \), \( \beta \), \( \gamma \), then flipping \( v \) flips all three values; at least two of them are T after the flip exactly when at least two were F before, that is, exactly when at most one was T, that is, exactly when \( \mathsf{M}(\alpha, \beta, \gamma) \) was F. So \( \bar v(\mathsf{M}(\alpha, \beta, \gamma)) \) is the opposite of \( v(\mathsf{M}(\alpha, \beta, \gamma)) \). The other connectives and \( \bot \) do not occur in formulas of \( \{\neg, \mathsf{M}\} \), so those cases are vacuous. (Structural induction for the extended language holds by the proof of @thm-structural-induction, with one more formation clause.)

Now the two-input function of \( p_1 \wedge p_2 \) is F at \( (\mathrm{T}, \mathrm{F}) \) and at the flipped input \( (\mathrm{F}, \mathrm{T}) \). If a formula \( \varphi \) in \( \{\neg, \mathsf{M}\} \) expressed it, then for a valuation \( v \) with \( v(p_1) = \mathrm{T} \), \( v(p_2) = \mathrm{F} \) we would have \( v(\varphi) = \mathrm{F} \) and \( \bar v(\varphi) = \mathrm{F} \), since \( \bar v(p_1) = \mathrm{F} \) and \( \bar v(p_2) = \mathrm{T} \). But these values must be opposite. So no formula in \( \{\neg, \mathsf{M}\} \) expresses it, and the set is not adequate.

**Marking scheme.** (10 points)

- 3: (a) states the all-T valuation and runs the induction, with the \( \leftrightarrow \) case and the vacuous cases (\( \neg \), \( \bot \)) named.
- 1: (a) names a truth function that is not expressed (negation), with the reason.
- 4: (b) states the flipped-row property for **every** formula in \( \{\neg, \mathsf{M}\} \) and proves it by structural induction, including the \( \mathsf{M} \) case.
- 2: (b) exhibits a truth function that takes the same value on some row and on its flipped row, and concludes.

Fatal errors (0 for the step): in (b), checking the flipped-row property on a few formulas instead of proving it for all; in (a), an implication case justified by the hypothesis being true rather than by the conclusion.
:::

::: {#exr-normal-forms-c4}
[C3: Exit check: normal forms]

Put \( (p \to q) \to (q \wedge r) \) into DNF and into CNF, by either route, and check one of your answers against the truth table.
:::

::: {.solution}
*By rewriting.* Eliminate the outer implication and then the inner one, and push the negation in:
\[
\begin{aligned}
(p \to q) \to (q \wedge r) &\equiv \neg(p \to q) \vee (q \wedge r) \\
&\equiv \neg(\neg p \vee q) \vee (q \wedge r) \\
&\equiv (p \wedge \neg q) \vee (q \wedge r) .
\end{aligned}
\]
The last line is a DNF. Here \( \neg(p \to q) \equiv p \wedge \neg q \), since an implication is false exactly when its hypothesis is true and its conclusion false. For a CNF, distribute:
\[
(p \wedge \neg q) \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r) \wedge (\neg q \vee q) \wedge (\neg q \vee r) ,
\]
and drop the clause \( \neg q \vee q \), which is true in every row: the CNF is \( (p \vee q) \wedge (p \vee r) \wedge (\neg q \vee r) \). (The clause \( p \vee r \) is redundant too: \( (p \vee q) \wedge (\neg q \vee r) \) is an equivalent CNF, as splitting on \( q \) shows. Either is correct.)

*The check.* The formula is false exactly when \( p \to q \) holds and \( q \wedge r \) fails. Its table:
\[
\begin{array}{ccc|c|c|c}
p & q & r & p \to q & q \wedge r & (p \to q) \to (q \wedge r) \\
\hline
\mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{T} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} & \mathrm{T} \\
\mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{T} & \mathrm{F} & \mathrm{F} \\
\mathrm{F} & \mathrm{F} & \mathrm{F} & \mathrm{T} & \mathrm{F} & \mathrm{F}
\end{array}
\]
The T-rows are T T T, T F T, T F F, and F T T. The DNF \( (p \wedge \neg q) \vee (q \wedge r) \) is true in exactly these: \( p \wedge \neg q \) in T F T and T F F, and \( q \wedge r \) in T T T and F T T. In each of the four F-rows the CNF has a false clause: \( \neg q \vee r \) in T T F and F T F, \( p \vee q \) in F F T and F F F.

*By the table route*, the DNF has four minterms, one per T-row, and the CNF four clauses, one per F-row, for instance \( \neg p \vee \neg q \vee r \) for the row T T F. Any correct DNF and CNF earns full marks; a CNF is not unique.

**Marking scheme.** (10 points)

- 2: the route carried out correctly: \( \to \) eliminated, with \( \neg(p \to q) \equiv p \wedge \neg q \) and its reason, or the T-rows and F-rows read off a correct table.
- 3: a correct DNF.
- 3: a correct CNF, by distribution carried out in full or by one clause per F-row.
- 2: the check against the table, covering at least the four F-rows (or the four T-rows).

Fatal errors (0 for the step): \( \neg(p \to q) \) rewritten as \( \neg p \to \neg q \); a "CNF" with a conjunction inside a clause.
:::

::: {#exr-normal-forms-c5}
[C4: From connectives to sets]

Let \( U \) be a collection, and \( A \), \( B \), \( E \) collections of members of \( U \), in the everyday sense; \( U \setminus A \) is the collection of members of \( U \) not in \( A \). For a member \( x \) of \( U \), write \( a \), \( b \), \( e \) for the statements \( x \in A \), \( x \in B \), \( x \in E \).

::: {.enumerate options="label=(\alph*)"}
1. Write "\( x \in U \setminus (A \cap B) \)" and "\( x \in (U \setminus A) \cup (U \setminus B) \)" as formulas in \( a \), \( b \), and deduce from a standard equivalence that the two collections have the same members.
2. Show in the same way that \( A \cap (B \cup E) \) and \( (A \cap B) \cup (A \cap E) \) have the same members.
3. Show that \( (a \to b) \to ((a \wedge e) \to (b \wedge e)) \) is a tautology, and deduce: if every member of \( A \) is in \( B \), then every member of \( A \cap E \) is in \( B \cap E \).
:::
:::

::: {.solution}
*(a)* The formulas are \( \neg(a \wedge b) \) and \( \neg a \vee \neg b \). They are equivalent by @prp-standard-equivalences (b). Each member \( x \) of \( U \) gives a valuation of \( a \) and \( b \), by whether it lies in \( A \) and in \( B \), and under that valuation the two formulas have the same value. So \( x \) is in one collection exactly when it is in the other.

*(b)* The formulas are \( a \wedge (b \vee e) \) and \( (a \wedge b) \vee (a \wedge e) \), equivalent by @prp-standard-equivalences (g); conclude as in (a).

*(c)* Work backwards from F. Falsity needs \( a \to b \) true and \( (a \wedge e) \to (b \wedge e) \) false, so \( a \) and \( e \) true and \( b \wedge e \) false. Then \( b \) is true, by \( a \to b \), so \( b \wedge e \) is true: no row makes the formula false, and it is a tautology. For each \( x \), its memberships give a valuation making the formula true: so if "\( x \in A \) implies \( x \in B \)" holds, then "\( x \in A \cap E \) implies \( x \in B \cap E \)" holds. If every member of \( A \) is in \( B \), the first holds for every \( x \), hence so does the second.

**Marking scheme.** (8 points)

- 3: (a), with the step from an equivalence to equal membership argued (each \( x \) gives a valuation).
- 2: (b).
- 3: (c): the tautology, and the step to collections.

Fatal errors (0 for the step): checking the set equality on one example collection only.
:::

::: {#exr-normal-forms-c6}
[C5: Counting rows]

For a formula \( \varphi \) whose atoms are among \( p_1, \dots, p_n \), let \( \#\varphi \) be the number of rows of the table on \( p_1, \dots, p_n \) in which \( \varphi \) is true.

::: {.enumerate options="label=(\alph*)"}
1. Show that \( \varphi \models \psi \) implies \( \#\varphi \le \#\psi \), and that the converse fails.
2. Show that \( \#(\varphi \vee \psi) = \#\varphi + \#\psi - \#(\varphi \wedge \psi) \).
3. Show that the minterms of two different rows are never true together, and that the disjunction of all \( 2^n \) minterms is a tautology. Deduce that, for satisfiable \( \varphi \), the full DNF of \( \varphi \) over \( p_1, \dots, p_n \) (one minterm on \( p_1, \dots, p_n \) for each row on them in which \( \varphi \) is true) has exactly \( \#\varphi \) minterms.
:::
:::

::: {.solution}
*(a)* If \( \varphi \models \psi \), every row in which \( \varphi \) is true is one in which \( \psi \) is true, so there are at least as many of the second. The converse fails: on the atoms \( p \), \( q \), the formulas \( p \) and \( q \) are each true in two rows, so \( \#p \le \#q \), but \( p \not\models q \) (the row \( p = \mathrm{T} \), \( q = \mathrm{F} \)).

*(b)* By (V4), the rows of \( \varphi \vee \psi \) are those of \( \varphi \) together with those of \( \psi \). By (V3), the rows in both are the rows of \( \varphi \wedge \psi \). The sum \( \#\varphi + \#\psi \) counts those twice and every other row of \( \varphi \vee \psi \) once.

*(c)* Two different rows differ at some \( p_i \); one minterm contains \( p_i \) and the other \( \neg p_i \), and no valuation makes both literals true. Each row makes its own minterm true (@eq-row-conjunct), so the disjunction of all \( 2^n \) is true in every row (@eq-many-term-values). The full DNF over \( p_1, \dots, p_n \) has one minterm for each row on them in which \( \varphi \) is true, and different rows give different minterms, so it has \( \#\varphi \) of them. (It is not always the DNF that the proof of @thm-dnf builds. That proof uses only the atoms of \( \varphi \), so when \( \varphi \) is satisfiable and has at least one atom, and \( j \) of the \( p_i \) do not occur in \( \varphi \), it gives \( \#\varphi / 2^j \) minterms on the remaining atoms. When \( \varphi \) has no atoms it gives \( p \vee \neg p \) or \( p \wedge \neg p \). When \( \#\varphi = 0 \) it gives a contradiction \( q \wedge \neg q \) for some atom \( q \), which is a conjunctive clause but no minterm. Hence the restriction to satisfiable \( \varphi \).)

**Marking scheme.** (8 points)

- 2: (a) the inequality; 1: a counterexample to the converse, checked.
- 2: (b), with the rows counted twice named.
- 3: (c): different rows give minterms never true together; the disjunction of all is a tautology; the count.

Fatal errors (0 for the step): in (a), a "converse" argued from one pair of formulas that happen to entail each other.
:::

::: {#exr-normal-forms-c7}
[C6: Challenge: Interpolation]

::: {.enumerate options="label=(\alph*)"}
1. For \( \varphi = p \wedge q \) and \( \psi = q \vee r \), find a formula \( \theta \) whose only atom is \( q \), with \( \varphi \models \theta \) and \( \theta \models \psi \).
2. Prove: if \( \varphi \models \psi \), \( \varphi \) is satisfiable and \( \psi \) is not a tautology, then there is a formula \( \theta \), all of whose atoms occur both in \( \varphi \) and in \( \psi \), with \( \varphi \models \theta \) and \( \theta \models \psi \).
3. Show that under the hypotheses of (b), \( \varphi \) and \( \psi \) have at least one atom in common.
:::
:::

::: {.solution}
[Hint 1]

Let \( \theta \) say: the shared atoms take values that some row making \( \varphi \) true also gives them.
:::

::: {.solution}
[Hint 2]

To show \( \theta \models \psi \), build one row that agrees with a row of \( \varphi \) on the atoms of \( \varphi \) and with the given row on the other atoms of \( \psi \).
:::

::: {.solution}
*(a)* \( \theta = q \): \( p \wedge q \models q \) and \( q \models q \vee r \).

*(c)* (Proved first, since (b) uses it.) Suppose no atom is shared. Take a row \( u \) making \( \varphi \) true, and any row \( w \). The row that agrees with \( u \) on the atoms of \( \varphi \) and with \( w \) on every other atom makes \( \varphi \) true (@lem-coincidence), hence \( \psi \); it agrees with \( w \) on the atoms of \( \psi \), none of which is an atom of \( \varphi \), so \( w \) makes \( \psi \) true (@lem-coincidence again). As \( w \) was any row, \( \psi \) would be a tautology.

*(b)* Let \( q_1, \dots, q_k \) be the shared atoms (\( k \ge 1 \) by (c)). Call a row \( s \) on \( q_1, \dots, q_k \) *good* if some valuation making \( \varphi \) true gives the \( q_i \) the values of \( s \); there is at least one, since \( \varphi \) is satisfiable. Let \( \theta \) be the disjunction of the minterms, on \( q_1, \dots, q_k \), of the good rows. Its atoms are shared.

\( \varphi \models \theta \): a valuation making \( \varphi \) true gives the \( q_i \) the values of a good row \( s \), so it makes the minterm of \( s \) true (@eq-row-conjunct), hence \( \theta \).

\( \theta \models \psi \): let \( w \) make \( \theta \) true. Then \( w \) makes the minterm of some good row \( s \) true, so \( w \) gives the \( q_i \) the values of \( s \); and some \( u \) making \( \varphi \) true does the same. Let \( u' \) agree with \( u \) on the atoms of \( \varphi \) and with \( w \) on every other atom. By @lem-coincidence, \( u' \) makes \( \varphi \) true, so it makes \( \psi \) true, since \( \varphi \models \psi \). Now \( u' \) agrees with \( w \) on every atom of \( \psi \): on the shared atoms both give the values of \( s \), and the other atoms of \( \psi \) are not atoms of \( \varphi \). By @lem-coincidence, \( w \) makes \( \psi \) true.

**Marking scheme.** (12 points)

- 1: (a).
- 2: the definition of \( \theta \) from the good rows, with its existence (satisfiable \( \varphi \)).
- 2: \( \varphi \models \theta \).
- 5: \( \theta \models \psi \), with the glued row and both uses of @lem-coincidence.
- 2: (c).

Fatal errors (0 for the step): a \( \theta \) with an atom of \( \varphi \) alone; a glued row that is not shown to agree with \( w \) on every atom of \( \psi \).
:::

<!-- dependency ledger
prp-cnf-validity (claim): the duality remark: psi is a tautology iff not-psi is unsatisfiable | F1.3 §05, the display after def-satisfiable (unlabeled), recalled in prose
eq-many-term-values (claim): values of right-grouped long conjunctions and disjunctions | recalled from F1.3 §05 (paragraph after prp-standard-equivalences, proved there by ax-induction); not re-proved
thm-dnf (proof): phi equiv psi iff v(phi) = v(psi) for every v | the paraphrase after def-semantic-equivalence (F1.3 §05)
thm-dnf (proof): 2^n rows for n atoms; a valuation with prescribed values at p_1..p_n exists | def-valuation, def-truth-table (F1.3 §04)
thm-dnf (proof): the atoms of not-phi are those of phi | the recursive definition of the set of atoms (F1.3 §03)
thm-cnf (proof): a literal and its opposite take opposite values | def-truth-value (argued inline after def-literal)
thm-cnf (claim): the rewriting route; the equivalences used, applied inside a formula, chained | prp-standard-equivalences, lem-replacement (cited); transitivity of equivalence, F1.3 §05 (paraphrase of def-semantic-equivalence)
exm-normal-forms-two-routes (example): a conjunction with a part true in every row is equivalent to its other part | inline (eq-many-term-values)
thm-adequate-connectives (proof): chi -> bot is true exactly when chi is false | def-truth-value (argued inline)
thm-adequate-connectives (proof): the immediate parts of a formula in a set S of connectives are in S | inline (their symbols occur in the formula)
thm-adequate-connectives (claim): exr-valuations-and-truth-tables-c2 is F1.3 §04's find-the-error item on the all-T valuation | prose pointer only; the proof is written in full here
exr-normal-forms-b3 (solution): no DNF with fewer conjunctive clauses works | inline (a conjunctive clause missing an atom is true on two rows of different parity)
exr-normal-forms-c1 (solution): structural recursion and induction for the language extended by new connectives | the proofs of thm-structural-recursion and thm-structural-induction with one more clause; flagged in the solution
exr-normal-forms-c2 (solution): same extension for the majority connective | as above, flagged in the solution
prp-more-equivalences (proof): v(bot) = F and v(not bot) = T; both sides computed from v(phi), v(psi) | def-truth-value (V1), (V2); the method of prp-standard-equivalences (F1.3 §05)
exm-simplify-by-calculation (example): each law applied inside a formula; the steps chain | lem-replacement and transitivity of equivalence (F1.3 §05)
def-occurrence-polarity (claim): the sign is fixed by the path | defined along the parse tree, which is unique (thm-unique-readability)
thm-monotonicity (proof): the sign of a node in chi is its sign in an immediate part, kept or flipped by the part's sign | inline from def-occurrence-polarity and def-parse-tree
thm-monotonicity (proof): (V3), (V4) monotone in each part; (V5) monotone in the conclusion, antitone in the hypothesis | def-truth-value (argued inline)
exr-normal-forms-a2 (solution): {not, ->} adequate by rewriting alpha or beta as not-alpha -> beta from the leaves up | thm-adequate-connectives (a), as its t-translations do; one line
exr-normal-forms-c5 (solution): collections, set difference, intersection, union in the everyday sense | F2.1 (promised: def-set-operations)
exr-normal-forms-c6 (solution): counting rows; minterms of different rows exclude each other | eq-row-conjunct, eq-many-term-values (cited)
exr-normal-forms-c7 (solution): gluing two valuations that agree on the shared atoms | lem-coincidence (cited twice)
-->
