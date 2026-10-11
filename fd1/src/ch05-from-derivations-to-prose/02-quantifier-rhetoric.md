# The Quantifier Rules in Prose

Section 5.1 read the connective rules in the sentences of written proofs. The statements of analysis, though, are made of "for every" and "there exists", and most of the words in an analysis proof carry a quantifier rule: "let", "fix", "choose", "take", "will do". This section completes the dictionary with the rows for the quantifiers, equality and unique existence, and for the three patterns that are not single rules but are written as if they were: induction, the lemma ("it suffices to show"), and symmetry ("without loss of generality"). It also makes exact one habit of analysis prose, the parenthesis "(depending on \( \varepsilon \))".

## Three sentences, three rules

Section 4.8 derived "if \( a_n \to L \), then \( 2a_n \to 2L \)" in sixteen lines. In a proof in Part I the same argument takes three sentences:

> Let \( \varepsilon > 0 \). Since \( a_n \to L \) and \( \varepsilon/2 > 0 \), we may choose \( N \in \nN \) (depending on \( \varepsilon \)) such that \( \abs{a_n - L} < \varepsilon/2 \) for every \( n \ge N \). Then for every \( n \ge N \), \( \abs{2a_n - 2L} = 2\abs{a_n - L} < \varepsilon \).

Each sentence opens a box, and the boxes are nested in the order of the sentences.

- "Let \( \varepsilon > 0 \)" opens the bounded \( \rulename{\forall I} \) box of lines 2–15 in the derivation of Section 4.8, with the fresh name \( \varepsilon_0 \). Its closing line, line 16, is not written: the paragraph simply ends, and a reader who heard "let" knows that the box closes there.
- "Choose \( N \) …" is two rules. The words "since \( a_n \to L \) and \( \varepsilon/2 > 0 \)" are the \( \rulename{\forall E} \) of line 4, at the term \( \varepsilon_0/2 \), with its bound from line 3. The word "choose" opens the \( \rulename{\exists E} \) box of lines 5–14, with the fresh name \( N_0 \).
- "Then for every \( n \ge N \)" opens the \( \rulename{\forall I} \) box of \( n_0 \) and the \( \rulename{{\to}I} \) box of \( n_0 \ge N_0 \) (lines 7 and 9), and the computation is lines 8, 10 and 11. The words "for every \( n \ge N \)" also announce the lines that close these two boxes, 12 and 13.
- The \( \rulename{\exists I} \) of line 14, which writes "some \( N \) works" from "this \( N \) works", and the closing line 15 of the \( \rulename{\exists E} \) box, are silent. They are the end of the paragraph.

The one word in the paragraph that no rule asks for is the parenthesis "(depending on \( \varepsilon \))". It is the subject of a subsection below. First, the rows.

## The quantifier rows

| Rule | Phrases | Silent in plain prose? |
|---|---|---|
| \( \rulename{\forall I} \) | "let \( x \in A \)"; "fix \( \varepsilon > 0 \)"; "let \( \varepsilon > 0 \) be given"; "since \( x \) was arbitrary" | never the introduction; "since \( x \) was arbitrary" may be silent |
| \( \rulename{\forall E} \) | "in particular, for \( x = \dots \)"; "applying … with \( \varepsilon/2 \) in place of \( \varepsilon \)" | the instance must be named when it is not the obvious one |
| \( \rulename{\exists I} \) | "take \( N = \dots \)"; "let \( \delta \coloneqq \dots \); then …"; "… will do" | never; its dependencies are stated |
| \( \rulename{\exists E} \) | "choose \( N \) such that"; "by hypothesis there is \( k \) with \( n = 2k \)"; "let \( x_0 \) be such a point" | never; the name must be fresh |

The phrases in the table are mostly the bounded forms of the rules (@prp-bounded-quantifier-rules): "let \( x \in A \)" opens a \( \rulename{\forall I} \) box whose assumption is \( x \in A \), and "choose \( N \in \nN \) such that …" opens an \( \rulename{\exists E} \) box with the two assumptions \( N \in \nN \) and "…". A bound is part of the phrase: "let \( \varepsilon > 0 \)" is one step, not "let \( \varepsilon \)" followed by "suppose \( \varepsilon > 0 \)".

In analysis, \( \rulename{\forall I} \) is the first sentence of every limit proof: "Let \( \varepsilon > 0 \)." \( \rulename{\forall E} \) is "apply the definition of \( a_n \to L \) with \( \varepsilon/2 \)": the instance \( \varepsilon/2 \) is not the obvious one, so it is named. \( \rulename{\exists I} \) is the line that places a constant, "let \( \delta \coloneqq \min\{1, \varepsilon/10\} \)", written before the computation that shows it works. \( \rulename{\exists E} \) is "choose \( N \) (depending on \( \varepsilon \)) such that …", in which the name \( N \) has not been used before in the proof.

::: {#exm-rhetoric-universal}
[A constant sequence]

Let \( c \) be a real number and let \( a_n \coloneqq c \) for every \( n \in \nN \). Prove that \( a_n \to c \), and annotate each phrase with its rule.
:::

::: {.solution}
Let \( \varepsilon > 0 \) [\( \rulename{\forall I} \), opening]. Take \( N \coloneqq 0 \) [\( \rulename{\exists I} \)]. Let \( n \in \nN \) with \( n \ge N \) [\( \rulename{\forall I} \), \( \rulename{{\to}I} \), opening]. Then
\[
\abs{a_n - c} = \abs{c - c} = 0 < \varepsilon ,
\]
where the first equality substitutes \( a_n = c \) [\( \rulename{{=}E} \)] and the last step uses \( \varepsilon > 0 \), the assumption of the first box. This proves \( a_n \to c \).

The last sentence stands for three closing lines, all silent: the \( \rulename{{\to}I} \) and \( \rulename{\forall I} \) for \( n \) ("for every \( n \ge N \)"), and the \( \rulename{\forall I} \) for \( \varepsilon \) ("since \( \varepsilon \) was arbitrary"). The witness "take \( N \coloneqq 0 \)" is placed before the work that justifies it.

Two things here are degenerate, and both are worth seeing once. The witness \( N \) depends on nothing: any \( N \in \nN \) works. And the assumption \( n \ge N \) is never used. The box is still opened, because the goal \( \forall n \in \nN\; (n \ge N \to \dots) \) asks for it; without "let \( n \ge N \)", the line "\( \abs{a_n - c} = 0 \)" would not say which \( n \) it is about.
:::

## The dependency parenthesis

In the paragraph that opened this section, \( N \) was chosen "(depending on \( \varepsilon \))". Section 4.10 read off a derivation the rule behind the parenthesis:

*A constant chosen in a box may depend on the names of the boxes open around that box, and it does depend only on the names in the line it comes from.*

In the derivation of Section 4.8, the witness \( N_0 \) is obtained at line 5 from line 4, which mentions \( \varepsilon_0 \), inside the box of \( \varepsilon_0 \) only. So \( N_0 \) may depend on \( \varepsilon_0 \), and it does. In the derivation of @exm-uniform-implies-continuous, the witness \( \delta_0 \) is obtained inside the boxes of \( x_0 \) and \( \varepsilon_0 \), so it **may** depend on both; but it comes from a line that mentions \( \varepsilon_0 \) alone, so it **does** depend only on \( \varepsilon_0 \), and that is uniformity.

The parenthesis is the prose record of this. "Choose \( N \) (depending on \( \varepsilon \))" says: the boxes open here are those of \( \varepsilon \) (besides the data of the theorem, such as the sequence), and the line from which \( N \) comes mentions \( \varepsilon \). "Choose \( \delta \) (depending on \( \varepsilon \) and on \( x \))" says that \( \delta \) came from a line mentioning both, inside both boxes. A witness that came from a line mentioning neither is a constant, and the proof may say "(depending on neither)" or simply "a fixed \( \delta \)". This is why proofs in analysis say what each chosen constant depends on. A missing parenthesis is not a wrong step, but it hides the one fact a reader most needs in order to check the quantifier order, and many false proofs in analysis go wrong exactly there.

::: {#exm-rhetoric-existential}
[The reciprocals tend to zero]

Prove that \( 1/n \to 0 \), for the sequence \( (1/n)_{n \ge 1} \). Annotate each phrase with its rule, and state what the chosen constant depends on.
:::

::: {.solution}
The sequence starts at \( n = 1 \), so the definition of Section 4.8 is read with \( N \) and \( n \) in \( \nZ_{>0} \) instead of \( \nN \): for every \( \varepsilon > 0 \) there is \( N \in \nZ_{>0} \) such that \( \abs{1/n - 0} < \varepsilon \) for every \( n \in \nZ_{>0} \) with \( n \ge N \). We use one school fact about the real numbers: for every real number \( u \) there is an integer greater than \( u \). (Chapter 11 proves it from the axioms of \( \nR \).)

Let \( \varepsilon > 0 \) [\( \rulename{\forall I} \), opening]. It suffices to find \( N \in \nZ_{>0} \) with
\[
\frac{1}{N} < \varepsilon , \tag{$\ast$}
\]
since then every \( n \in \nZ_{>0} \) with \( n \ge N \) has \( 0 < 1/n \le 1/N < \varepsilon \), so \( \abs{1/n - 0} < \varepsilon \) [cut: the claim (\( \ast \)) displayed, then used].

By the school fact, applied to \( u = 1/\varepsilon \) [\( \rulename{\forall E} \)], there is an integer greater than \( 1/\varepsilon \); choose such an integer \( N \) [\( \rulename{\exists E} \)], which depends on \( \varepsilon \). Since \( \varepsilon > 0 \), we have \( 1/\varepsilon > 0 \), so \( N > 0 \) and \( N \in \nZ_{>0} \). From \( N > 1/\varepsilon > 0 \), taking reciprocals reverses the inequality: \( 1/N < \varepsilon \), which is (\( \ast \)). So this \( N \) will do [\( \rulename{\exists I} \)], and \( 1/n \to 0 \).

Read the proof as a skeleton. The first sentence opens the box of \( \varepsilon \). The second is a cut, in the sense of the row below: it states a simpler claim (\( \ast \)), shows on the spot that (\( \ast \)) is enough, and leaves (\( \ast \)) to be proved. The next paragraph proves (\( \ast \)). It contains two different quantifier steps that both concern \( N \): "choose" is the \( \rulename{\exists E} \) on the school fact, which hands over some integer beyond \( 1/\varepsilon \) and calls it \( N \); "will do" is the \( \rulename{\exists I} \) that offers this \( N \) as the witness the definition asks for. Between them, the clause "so \( N > 0 \) and \( N \in \nZ_{>0} \)" checks the bound \( N \in \nZ_{>0} \) of the witness, which the bounded \( \rulename{\exists I} \) needs as a line.

The constant \( N \) depends on \( \varepsilon \) only: it came from the school fact at \( 1/\varepsilon \), inside the box of \( \varepsilon \). For instance, \( \varepsilon = 0.03 \) has \( 1/\varepsilon = 33.3\ldots \), and \( N = 34 \) is a choice that works; so is any larger integer.
:::

::: {.check}
"For every \( \varepsilon > 0 \), \( \abs{a_n - L} < \varepsilon \) for all large \( n \)." Where is the hidden \( \exists N \), and between which two quantifiers does it stand?
:::

::: {.solution}
"For all large \( n \)" is "there is an \( N \) such that for every \( n \ge N \)" (Section 4.8): the hidden \( \exists N \) stands after \( \forall \varepsilon > 0 \) and before \( \forall n \ge N \). Written out, the sentence is \( \forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{a_n - L} < \varepsilon) \), the definition of \( a_n \to L \). Since \( \exists N \) comes after \( \forall \varepsilon \), the \( N \) may depend on \( \varepsilon \).
:::

## Equality and unique existence

| Rule | Phrases | Silent in plain prose? |
|---|---|---|
| \( \rulename{{=}I} \), \( \rulename{{=}E} \) | "substituting"; chains "\( \dots = \dots = \dots \)"; "by (1)" | yes, inside chains |
| \( \exists! \) | "there is exactly one"; "existence … uniqueness …"; "suppose \( y \) also …" | never either half |

In analysis, \( \rulename{{=}E} \) is at work in every chain of equalities and inequalities, such as
\[
\abs{x^2 - 4} = \abs{x - 2}\, \abs{x + 2} \le 5 \abs{x - 2} \quad \text{for } \abs{x - 2} < 1 ,
\]
where each \( = \) link substitutes equals for equals and each inequality link applies one fact about order (Section 4.7). (Here \( \abs{x - 2} < 1 \) gives \( 1 < x < 3 \), so \( 3 < x + 2 < 5 \).) The \( \rulename{{=}I} \) lines \( t = t \) that such chains rest on are never written. Unique existence (@def-unique-existence) has two halves, which @prp-unique-existence-use separates: "\( 2x + 3 = 7 \) has exactly one real solution: \( x = 2 \) is one, and if \( 2y + 3 = 7 \), then \( y = 2 \)". The first clause is existence, by \( \rulename{\exists I} \); the second is uniqueness, a \( \rulename{\forall I} \) and \( \rulename{{\to}I} \) box on a second candidate. Neither half implies the other, so neither may be silent.

The uniqueness half often stands alone, when existence is not claimed or is proved elsewhere. Uniqueness of limits is a case of this kind.

::: {#exm-rhetoric-equality}
[A sequence has at most one limit]

Let \( (a_n) \) be a sequence of real numbers with \( a_n \to L \) and \( a_n \to M \). Prove that \( L = M \), and annotate each phrase with its rule.
:::

::: {.solution}
Let \( \varepsilon > 0 \) [\( \rulename{\forall I} \), opening]. Then \( \varepsilon/2 > 0 \), so, applying the definition of \( a_n \to L \) with \( \varepsilon/2 \) in place of \( \varepsilon \) [\( \rulename{\forall E} \)], we may choose \( N_1 \in \nN \) (depending on \( \varepsilon \)) such that \( \abs{a_n - L} < \varepsilon/2 \) for every \( n \ge N_1 \) [\( \rulename{\exists E} \), fresh name \( N_1 \)]. Likewise, from \( a_n \to M \), choose \( N_2 \in \nN \) (depending on \( \varepsilon \)) such that \( \abs{a_n - M} < \varepsilon/2 \) for every \( n \ge N_2 \) [\( \rulename{\forall E} \), \( \rulename{\exists E} \), fresh name \( N_2 \)]. Let \( n \coloneqq \max\{N_1, N_2\} \). Then \( n \ge N_1 \) and \( n \ge N_2 \), so both bounds apply at \( n \) [\( \rulename{\forall E} \) at \( n \), twice, with \( \rulename{{\to}E} \)], and
\[
\begin{aligned}
\abs{L - M} &= \abs{(L - a_n) + (a_n - M)} \\
&\le \abs{a_n - L} + \abs{a_n - M} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon ,
\end{aligned}
\]
where the inequality is the triangle inequality of @exm-triangle-inequality-cases, with \( \abs{L - a_n} = \abs{a_n - L} \). Since \( \varepsilon > 0 \) was arbitrary, \( \abs{L - M} < \varepsilon \) for every \( \varepsilon > 0 \) [\( \rulename{\forall I} \), closing], and @prp-arbitrarily-close-equal gives \( L = M \) [\( \rulename{{\to}E} \), citing it].

Four things in this proof are never silent, and each is visible. The instance \( \varepsilon/2 \) is named twice, because it is not the obvious instance. The two witnesses get two names, \( N_1 \) and \( N_2 \): the hypotheses promise a threshold for \( L \) and a threshold for \( M \), and nothing says they are the same number, so calling both \( N \) would assert an equality nobody proved (Section 5.6 catalogues the error). The point \( n = \max\{N_1, N_2\} \) is named, since the bounds are applied at it. And the closing result is cited by name.

What is silent is the bookkeeping of the two \( \rulename{\exists E} \) boxes. The line \( \abs{L - M} < \varepsilon \) mentions neither \( N_1 \), \( N_2 \) nor \( n \), so the side condition of \( \rulename{\exists E} \) lets it leave both boxes, and then the box of \( \varepsilon \) closes on it. The calculation chain hides its \( \rulename{{=}E} \) steps, as the row allows. The proof shows that a sequence has **at most one** limit: the uniqueness half of \( \exists! \). Whether a given sequence has a limit at all is a separate question, which this proof does not touch.
:::

## Induction, lemmas and symmetry

The last three rows are not rules of the calculus. Each is a pattern of rules that proofs announce with a phrase of its own.

| Pattern | Phrases | Silent in plain prose? |
|---|---|---|
| induction (@ax-induction, @thm-strong-induction) | "we argue by induction on \( n \)"; "base case"; "suppose the claim holds for \( n \)" | never either the base case or the step; the induction hypothesis is stated |
| cut, lemma (@lem-weakening-cut) | "we first show (Claim)"; "it suffices to show"; "we claim" | never the claim itself; "it suffices" may be dropped if the claim is displayed and then used |
| symmetry | "without loss of generality"; "similarly"; "by symmetry" | allowed only when the swap turns the statement and the hypotheses into themselves, up to identities such as \( \abs{b - a} = \abs{a - b} \) |

An induction is \( \rulename{{\to}E} \) applied to @ax-induction, whose hypothesis is a conjunction: the base case \( P(0) \), and the step "**for every** \( n \in \nN \), if \( P(n) \) then \( P(n + 1) \)". So the step is a \( \rulename{\forall I} \) box with a \( \rulename{{\to}I} \) box inside it, and the phrase "suppose the claim holds for \( n \)" opens the inner box; its assumption is the **induction hypothesis**, and it must be stated, because the step uses it. A lemma is a cut: @lem-weakening-cut (b) says that once \( \varphi \) is derived, it may be used as a premise. "It suffices to show \( \varphi \)" is the same cut seen from the goal, as Section 1.4 observed: it promises a derivation of the goal from \( \varphi \) and leaves \( \varphi \) to be proved. In analysis, "it suffices to show \( \abs{a_n - L} < \varepsilon \) for \( n \ge N \)" is the cut that reduces a limit to a single estimate; @exm-rhetoric-existential made one with the claim (\( \ast \)). Symmetry is a case split \( \rulename{\vee E} \) whose second box is the first with two letters exchanged, up to identities such as \( \abs{b - a} = \abs{a - b} \); "without loss of generality \( x \le y \)" writes the first box and leaves that check to the reader.

::: {#exm-rhetoric-induction}
[An induction, and a legitimate symmetry]

(a) Let \( a \) be a real number with \( 0 < a \le 1 \). Prove that \( 0 < a^n \le 1 \) for every \( n \in \nN \), and annotate each phrase with its rule.

(b) Let \( a \) and \( b \) be real numbers. Prove that \( \abs{a - b} = \max\{a, b\} - \min\{a, b\} \), with a "without loss of generality", and write out the case split it abbreviates.
:::

::: {.solution}
*(a)* For \( n \in \nN \), let \( P(n) \) be the statement "\( 0 < a^n \) and \( a^n \le 1 \)". We argue by induction on \( n \), using @ax-induction.

*Base case.* \( a^0 = 1 \), and \( 0 < 1 \) and \( 1 \le 1 \), so \( P(0) \) holds [\( \rulename{\wedge I} \)].

*Step.* Let \( n \in \nN \) [\( \rulename{\forall I} \), opening], and suppose \( P(n) \) holds, that is, \( 0 < a^n \) and \( a^n \le 1 \) [\( \rulename{{\to}I} \), opening: the induction hypothesis]. Then \( a^{n+1} = a^n a \). Since \( a^n > 0 \) [\( \rulename{\wedge E} \)] and \( a > 0 \), the product \( a^n a \) is positive, so \( 0 < a^{n+1} \). Since \( a \le 1 \) and \( a^n > 0 \), multiplying gives \( a^n a \le a^n \), and \( a^n \le 1 \) [\( \rulename{\wedge E} \)], so \( a^{n+1} \le 1 \). Hence \( P(n + 1) \) holds [\( \rulename{\wedge I} \)].

By induction, \( P(n) \) holds for every \( n \in \nN \) [\( \rulename{{\to}E} \) on @ax-induction].

The base case is the first hypothesis of @ax-induction, written as its own paragraph. The step is the second: "let \( n \in \nN \)" and "suppose \( P(n) \) holds" open its two boxes, and "hence \( P(n + 1) \)" is the last line of the inner one; the closing lines "so \( P(n) \to P(n + 1) \), for every \( n \)" are silent. The induction hypothesis is stated in full, and each of its halves is taken out by \( \rulename{\wedge E} \) and used: \( a^n > 0 \) twice (for the sign of \( a^{n+1} \), and to multiply \( a \le 1 \) by \( a^n \) without reversing it), and \( a^n \le 1 \) once, at the end. The statement was chosen with care: the tempting "\( a^n \le a \)" fails at \( n = 0 \) whenever \( a < 1 \), since \( a^0 = 1 \), and an induction for it would have to start at \( n = 1 \).

*(b)* Without loss of generality, \( a \le b \). Then \( \max\{a, b\} = b \) and \( \min\{a, b\} = a \), and since \( b - a \ge 0 \),
\[
\abs{a - b} = \abs{b - a} = b - a = \max\{a, b\} - \min\{a, b\} .
\]

The phrase abbreviates a \( \rulename{\vee E} \) on "\( a \le b \) or \( b \le a \)", which holds for all real \( a, b \) by trichotomy. The first box is the paragraph above. The second box, on \( b \le a \), reads: then \( \max\{a, b\} = a \) and \( \min\{a, b\} = b \), and since \( a - b \ge 0 \), \( \abs{a - b} = a - b = \max\{a, b\} - \min\{a, b\} \). That is the first box with \( a \) and \( b \) exchanged throughout, read through three identities: \( \abs{b - a} = \abs{a - b} \), \( \max\{b, a\} = \max\{a, b\} \), and \( \min\{b, a\} = \min\{a, b\} \). These say that the **statement** is unchanged when \( a \) and \( b \) are exchanged, and there are no hypotheses to check. This is what makes the swap exact, and so what licenses "without loss of generality".
:::

::: {.warning}
"Without loss of generality" needs a statement and hypotheses that are unchanged by the swap. Here is a false "proof" that \( \max\{a, b\} = b \) for all real \( a, b \): "Without loss of generality \( a \le b \); then \( \max\{a, b\} = b \)." Exchanging \( a \) and \( b \) turns the claim into \( \max\{b, a\} = a \), which is a different claim, so the second case is not the first one in disguise; and indeed \( a = 2 \), \( b = 1 \) gives \( \max\{a, b\} = 2 \ne 1 \). Before writing "without loss of generality", swap the letters in the statement and the hypotheses, and check that each comes back unchanged, up to identities such as \( \abs{b - a} = \abs{a - b} \).
:::

## What the sentence does not say {#what-the-sentence-does-not-say}

Some quantifiers in mathematical English are not written at all, and some are written where they do not apply. Four habits of mathematical English cover most of them.

**The hidden universal closure.** A theorem stated as "if \( n \) is even, then \( n^2 \) is even" means "for every integer \( n \), if \( n \) is even, then \( n^2 \) is even". Section 4.1 introduced this convention: *a letter that is not introduced anywhere, in the statement of a theorem, is read with a "for every" in front of the whole statement.* It applies to the statement of a theorem, lemma or exercise, not to a line inside a proof: inside a proof every letter has been introduced by a "let" or a "choose", and its box tells the reader which. The proof of such a theorem begins by opening the hidden box: "let \( n \) be an integer".

**"For all large \( n \)"** hides an \( \exists N \) and a bound, as the Quick check above found. "Eventually" means the same. The negation of "\( P(n) \) for all large \( n \)" is "for every \( N \) there is an \( n \ge N \) for which \( P(n) \) fails", usually said "\( P(n) \) fails for infinitely many \( n \)".

**"Any"** can mean "every" or "some", and only the rest of the sentence decides (Section 4.1). "Any \( x \in A \) is positive" means every element of \( A \) is positive. "If any \( x \in A \) is positive, then \( A \) is non-empty" means: if **some** element of \( A \) is positive. When "any" appears, rewrite the sentence once with "every" and once with "some", and keep the one that was meant.

**Quantifiers at the end of a sentence.** English lets a writer put "for some \( x \)" or "for all \( y \)" after the formula they govern, and then the order of two such phrases is unclear. "\( x^2 > y \) for some \( x \) for all \( y \)", over \( \nR \), has two readings:
\[
\forall y\, \exists x\; (x^2 > y) \qquad \text{and} \qquad \exists x\, \forall y\; (x^2 > y) .
\]
The first is true (for \( y \ge 0 \) take \( x = y + 1 \), since \( (y + 1)^2 = y^2 + 2y + 1 > y \); for \( y < 0 \) take \( x = 0 \)). The second is false (whatever \( x \) is proposed, \( y = x^2 \) refutes it). The remedy is to write the quantifiers of such a statement **in front**, in the order in which they apply. A trailing phrase such as "for every \( n \ge N \)" is safe only when it is the last quantifier of the sentence, as in the definition of \( a_n \to L \).

::: {.warning}
Moving "for all \( x \)" to the end of a sentence can change continuity into uniform continuity. "\( \abs{f(x) - f(y)} < \varepsilon \) whenever \( \abs{x - y} < \delta \), for all \( x \)", written after "for every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that", does not say whether \( \forall x \) comes before \( \exists \delta \) (continuity at every point) or after it (uniform continuity). The two formulas of Section 4.10 differ exactly there, and @exm-square-not-uniform shows that the difference is real: \( f(x) = x^2 \) on \( \nR \) satisfies the first and not the second. Write the quantifiers in front.
:::

## Exercises

### A. Check your understanding

::: {#exr-quantifier-rhetoric-a1}
[A1]

Let \( (a_n) \) be a sequence of real numbers and \( L \) a real number. Here is a proof that if \( a_n \to L \) and \( L > 0 \), then \( a_n > 0 \) for all large \( n \). Its sentences are numbered.

> (1) Suppose \( a_n \to L \) and \( L > 0 \). (2) Then \( L/2 > 0 \). (3) Choose \( N \in \nN \) such that \( \abs{a_n - L} < L/2 \) for every \( n \ge N \). (4) Let \( n \in \nN \) with \( n \ge N \). (5) Then \( L - a_n \le \abs{a_n - L} < L/2 \), so \( a_n > L/2 > 0 \). (6) Hence \( a_n > 0 \) for every \( n \ge N \), that is, \( a_n > 0 \) for all large \( n \).

::: {.enumerate options="label=(\alph*)"}
1. Name the rule or rules carried by each sentence.
2. Sentence (3) has no dependency parenthesis. What should it say, and why does \( N \) not depend on \( n \)?
3. Which instance of \( \rulename{\forall E} \) in the proof is not the obvious one?
4. Which closing lines are silent?
:::
:::

::: {.solution}
*(a)* (1) \( \rulename{{\to}I} \), opening: the hypothesis of the theorem is assumed (its two conjuncts are then available by \( \rulename{\wedge E} \)). (2) An arithmetic step from \( L > 0 \). (3) \( \rulename{\forall E} \) on the definition of \( a_n \to L \) at \( L/2 \), with its bound from (2), then \( \rulename{\exists E} \), opening a box with the fresh name \( N \). (4) \( \rulename{\forall I} \) and \( \rulename{{\to}I} \), opening the boxes of \( n \) and of \( n \ge N \). (5) \( \rulename{\forall E} \) at \( n \) and \( \rulename{{\to}E} \) on the line from (3), giving \( \abs{a_n - L} < L/2 \); then the school fact \( -u \le \abs{u} \) with \( u = a_n - L \), and arithmetic. (6) \( \rulename{{\to}I} \) and \( \rulename{\forall I} \), closing ("for every \( n \ge N \)"), then \( \rulename{\exists I} \) with the witness \( N \) ("for all large \( n \)" is \( \exists N\, \forall n \ge N \)), and the \( \rulename{\exists E} \) box of (3) closes, since the conclusion does not mention \( N \).

*(b)* "Choose \( N \in \nN \) (depending on \( L \)) such that …". \( N \) is obtained at line (3), from the definition instantiated at \( L/2 \), a term that mentions \( L \) (and the sequence, which is data). The box of \( n \) is opened only at (4), after \( N \) is chosen, so \( N \) cannot depend on \( n \).

*(c)* The instance \( \varepsilon = L/2 \) in (3). It is the instance the proof is built around: any \( \varepsilon \) with \( 0 < \varepsilon \le L \) would do, and \( L/2 \) leaves the margin \( a_n > L/2 \).

*(d)* The closing lines of the \( \rulename{\exists E} \) box (3) and of the \( \rulename{{\to}I} \) box (1), "hence, if \( a_n \to L \) and \( L > 0 \), then …". Sentence (6) writes the closings of the boxes of (4) in words, and the \( \rulename{\exists I} \) through "that is".
:::

### B. Practice

::: {#exr-quantifier-rhetoric-b1}
[B1: Ambiguous English]

Each sentence has a quantifier phrase at its end. Write both readings in symbols, with the quantifiers in front, and decide whether each reading is true for the function given.

::: {.enumerate options="label=(\alph*)"}
1. "\( f(x) \le M \) for every real \( x \), for some real \( M \)", for \( f(x) = x \).
2. "\( x + y = 0 \) for some real \( y \), for every real \( x \)."
3. "\( \abs{x - y} < \delta \) implies \( \abs{f(x) - f(y)} < 1 \) for all real \( x, y \), for some \( \delta > 0 \)", for \( f(x) = x^2 \).
:::
:::

::: {.solution}
*(a)* \( \exists M\, \forall x\; (f(x) \le M) \), "\( f \) is bounded above", and \( \forall x\, \exists M\; (f(x) \le M) \). For \( f(x) = x \) the first is false: whatever \( M \) is proposed, \( x = M + 1 \) has \( f(x) = M + 1 > M \). The second is true for every function: given \( x \), take \( M = f(x) \).

*(b)* \( \forall x\, \exists y\; (x + y = 0) \) and \( \exists y\, \forall x\; (x + y = 0) \). The first is true: given \( x \), take \( y = -x \). The second is false: for any \( y \), the two values \( x = -y \) and \( x = 1 - y \) give \( x + y = 0 \) and \( x + y = 1 \), so not every \( x \) works.

*(c)* \( \exists \delta > 0\; \forall x\, \forall y\; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < 1) \) and \( \forall x\, \forall y\; \exists \delta > 0\; (\abs{x - y} < \delta \to \abs{f(x) - f(y)} < 1) \). For \( f(x) = x^2 \) the first is false: it is the uniform continuity condition at \( \varepsilon = 1 \), and @exm-square-not-uniform refutes it with \( x = 1/\delta \), \( y = 1/\delta + \delta/2 \), for which \( \abs{x - y} < \delta \) and \( \abs{x^2 - y^2} = 1 + \delta^2/4 \ge 1 \). The second is true for every function: given \( x \) and \( y \), if \( x = y \) then \( \abs{f(x) - f(y)} = 0 < 1 \) for any \( \delta \), say \( \delta = 1 \); if \( x \ne y \), take \( \delta = \abs{x - y} \), so that \( \abs{x - y} < \delta \) is false and the implication holds vacuously.

In (a) and (c), the reading with \( \exists \) in front is the one a writer means; the other is true of every function, so it says nothing about \( f \). In (b), the intended reading is \( \forall x\, \exists y \). Written with the quantifiers in front, the sentences say what they mean: "there is \( M \) such that \( f(x) \le M \) for every \( x \)", "for every \( x \) there is \( y \) with \( x + y = 0 \)", "there is \( \delta > 0 \) such that for all \( x, y \), …".
:::

::: {#exr-quantifier-rhetoric-b2}
[B2: An induction, annotated]

Prove that \( 5^n - 1 \) is divisible by \( 4 \) for every \( n \in \nN \). Annotate each phrase of your proof with its rule, and say which hypothesis of @ax-induction each part of the proof establishes.
:::

::: {.solution}
For \( n \in \nN \), let \( P(n) \) be "\( 4 \mid 5^n - 1 \)", that is, "there is an integer \( k \) with \( 5^n - 1 = 4k \)". We argue by induction on \( n \).

*Base case.* \( 5^0 - 1 = 0 = 4 \cdot 0 \), so \( P(0) \) holds, with the witness \( k = 0 \) [\( \rulename{\exists I} \)]. This is hypothesis (i) of @ax-induction.

*Step.* Let \( n \in \nN \) [\( \rulename{\forall I} \), opening], and suppose \( P(n) \) holds [\( \rulename{{\to}I} \), opening: the induction hypothesis]. By the induction hypothesis there is an integer \( k \) with \( 5^n - 1 = 4k \); choose such a \( k \) (depending on \( n \)) [\( \rulename{\exists E} \), fresh name \( k \)]. Then
\[
5^{n+1} - 1 = 5 \cdot 5^n - 1 = 5(5^n - 1) + 4 = 5 \cdot 4k + 4 = 4(5k + 1) ,
\]
where the third equality substitutes \( 5^n - 1 = 4k \) [\( \rulename{{=}E} \)]. Since \( 5k + 1 \) is an integer, \( P(n + 1) \) holds, with the witness \( 5k + 1 \) [\( \rulename{\exists I} \)]. The step is hypothesis (ii) of @ax-induction: the \( \rulename{\forall I} \) on \( n \) and the \( \rulename{{\to}I} \) on \( P(n) \).

By induction, \( 4 \mid 5^n - 1 \) for every \( n \in \nN \) [\( \rulename{{\to}E} \) on @ax-induction].

The \( \rulename{\exists E} \) box of \( k \) closes on "\( P(n + 1) \)", which does not mention \( k \), as its side condition requires; its closing line, and those of the two boxes of the step, are silent.
:::

### C. Going deeper

::: {#exr-quantifier-rhetoric-c1}
[C1: When "similarly" is honest]

::: {.enumerate options="label=(\alph*)"}
1. Prove that \( \max\{x, y\} + \min\{x, y\} = x + y \) for all real \( x \) and \( y \), with a "without loss of generality". Then write out the \( \rulename{\vee E} \) it abbreviates, and check that its second box is the first with the letters exchanged.
2. Let \( x \ge 0 \) and \( y \) be real numbers. A student proves \( x \max\{x, y\} \ge xy \) as follows: "Without loss of generality \( x \le y \). Then \( \max\{x, y\} = y \), and \( xy \ge xy \)." Explain why "without loss of generality" is not legitimate here, prove the case the student skipped, and show by an example that the hypothesis \( x \ge 0 \) cannot be dropped from the statement.
:::
:::

::: {.solution}
[Hint 1]

In (b), exchange \( x \) and \( y \) in the statement and in the hypothesis, and compare with the original.
:::

::: {.solution}
[Hint 2]

In the case \( y \le x \), \( \max\{x, y\} = x \), and the claim becomes \( x^2 \ge xy \).
:::

::: {.solution}
*(a)* Without loss of generality \( x \le y \). Then \( \max\{x, y\} = y \) and \( \min\{x, y\} = x \), so \( \max\{x, y\} + \min\{x, y\} = y + x = x + y \).

The phrase abbreviates \( \rulename{\vee E} \) on "\( x \le y \) or \( y \le x \)", true for all real \( x, y \) by trichotomy. Box 1, on \( x \le y \), is the paragraph above. Box 2, on \( y \le x \): then \( \max\{x, y\} = x \) and \( \min\{x, y\} = y \), so \( \max\{x, y\} + \min\{x, y\} = x + y \). Exchanging \( x \) and \( y \) in box 1 gives "\( y \le x \); \( \max\{y, x\} = x \), \( \min\{y, x\} = y \); \( \max\{y, x\} + \min\{y, x\} = x + y = y + x \)", which is box 2 read through \( \max\{y, x\} = \max\{x, y\} \), \( \min\{y, x\} = \min\{x, y\} \) and \( y + x = x + y \). These identities say that the statement is unchanged by the exchange, and there are no hypotheses, so the swap is exact.

*(b)* Exchanging \( x \) and \( y \) changes both the hypothesis and the claim: it gives "\( y \ge 0 \), and \( y \max\{y, x\} \ge yx \)", which is not the original statement. So the case \( y \le x \) is not the case \( x \le y \) in disguise, and it needs its own argument.

*Case \( y \le x \).* Then \( \max\{x, y\} = x \), and multiplying \( x \ge y \) by \( x \ge 0 \) gives \( x \max\{x, y\} = x^2 \ge xy \).

With the student's case (\( x \le y \): \( x \max\{x, y\} = xy \ge xy \)), this proves the claim in either case. The hypothesis \( x \ge 0 \) is used only in the skipped case. It cannot be dropped: \( x = -1 \), \( y = -2 \) has \( \max\{x, y\} = -1 \), so \( x \max\{x, y\} = 1 \), while \( xy = 2 \), and \( 1 \ge 2 \) is false.

**Marking scheme.** (10 points)
- 2: (a) a correct computation in the case \( x \le y \).
- 3: (a) the \( \rulename{\vee E} \) written out, with its disjunction justified, and the exchange checked against the statement.
- 2: (b) the reason: the exchange changes the hypothesis and the claim.
- 2: (b) the case \( y \le x \) proved, using \( x \ge 0 \).
- 1: (b) a counterexample without \( x \ge 0 \), checked.
Fatal errors (0 for the step): in (b), "the other case is similar" without computing it; a counterexample that satisfies \( x \ge 0 \).
:::

::: {#exr-quantifier-rhetoric-c2}
[C2: Moving a quantifier changes the meaning]

Give an example of a sentence of analysis, in English, that begins "for every \( x \) …", whose meaning changes when the phrase "for every \( x \)" is moved to the end of the sentence. Write both readings in symbols and show that one is true and the other false.
:::

::: {.solution}
*An example.* "For every real \( x > 0 \), there is \( n \in \nZ_{>0} \) with \( 1/n < x \)." Moved: "There is \( n \in \nZ_{>0} \) with \( 1/n < x \), for every real \( x > 0 \)." The readings are
\[
\forall x > 0\; \exists n \in \nZ_{>0}\; (1/n < x) \qquad \text{and} \qquad \exists n \in \nZ_{>0}\; \forall x > 0\; (1/n < x) .
\]
The first is true: given \( x > 0 \), there is an integer \( n > 1/x \) (the school fact of @exm-rhetoric-existential), and \( n > 1/x > 0 \) gives \( n \in \nZ_{>0} \) and \( 1/n < x \). The second is false: whatever \( n \in \nZ_{>0} \) is proposed, \( x = 1/n \) is positive and \( 1/n < x \) fails. (It is natural to read the moved sentence as the second formula, since its "for every \( x \)" now comes after "there is \( n \)"; whichever reading a reader picks, the sentence no longer says one thing.)

*What a different answer must have,* so that it can be checked against this one:
- the sentence contains "for every \( x \)" and at least one existential quantifier ("there is", "for some") whose scope contains a formula mentioning \( x \);
- moved to the end, "for every \( x \)" can be read as coming after the existential quantifier, so that the witness may no longer depend on \( x \);
- both readings are written in symbols with all quantifiers in front, and there is a specific interpretation (here \( \nR \) with its usual order) in which one reading is true and the other false, each claim checked;
- the false reading is refuted by naming, for each candidate witness, a value of \( x \) that defeats it.
Another correct answer, for \( f(x) = x^2 \) on \( \nR \), is "for every \( x \), for every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that \( \abs{f(x) - f(y)} < \varepsilon \) whenever \( \abs{x - y} < \delta \)" (continuity, true); with "for every \( x \)" moved to the end, it becomes the sentence of the warning, whose uniform-continuity reading @exm-square-not-uniform refutes.
:::

<!-- dependency ledger
exm-rhetoric-universal (solution): |c - c| = 0 < eps | arithmetic
exm-rhetoric-existential (solution): for every real u there is an integer N > u | school fact stated in the solution; Ch 11 thm-naturals-unbounded (prose pointer)
exm-rhetoric-existential (solution): 1/eps > 0; N > 1/eps > 0 gives 1/N < eps; n >= N gives 0 < 1/n <= 1/N; eps = 0.03, N = 34 | school algebra; verify/ch05/exm-rhetoric-existential.py
exm-rhetoric-existential (claim): the definition read with N, n in Z_{>0} | exm-translate-limit (a), restated in the solution
exm-rhetoric-equality (solution): |u + v| <= |u| + |v|; |-u| = |u|; max{N1, N2} >= N1, N2 | exm-triangle-inequality-cases (cited); school facts
exm-rhetoric-equality (solution): |L - M| < eps for all eps > 0 gives L = M | prp-arbitrarily-close-equal (cited)
exm-rhetoric-equality (claim): |x - 2| < 1 gives 3 < x + 2 < 5, |x^2 - 4| <= 5|x - 2|; 2x + 3 = 7 iff x = 2 | school algebra; exm-abs-product-cases; verify/ch05/exm-rhetoric-equality.py
exm-rhetoric-induction (solution): a^0 = 1, a^(n+1) = a^n a | powers, school meaning; ch07 (promised): def-power
exm-rhetoric-induction (solution): products of positives; a^n a <= a^n <= 1; a^0 <= a fails for a < 1; |a - b| = max - min | school algebra; trichotomy; verify/ch05/exm-rhetoric-induction.py
exm-rhetoric-induction (claim): the warning's max{2, 1} = 2; the subsection after it: x = y + 1 or x = 0 gives x^2 > y, and y = x^2 refutes exists x forall y | arithmetic; verify/ch05/exm-rhetoric-induction.py
exr-quantifier-rhetoric-a1 (solution): -u <= |u|; L - L/2 = L/2 > 0 | exm-triangle-inequality-cases (its lemma); verify/ch05/exr-quantifier-rhetoric-a1.py
exr-quantifier-rhetoric-b1 (solution): the witnesses M + 1, -y, 1 - y, |x - y|; 1 + delta^2/4 | exm-square-not-uniform (cited); school algebra; verify/ch05/exr-quantifier-rhetoric-b1.py
exr-quantifier-rhetoric-b2 (solution): 5^0 = 1, 5^(n+1) = 5 * 5^n | powers, school meaning; ch07 (promised): def-power
exr-quantifier-rhetoric-b2 (solution): 5^(n+1) - 1 = 5(5^n - 1) + 4 = 4(5k + 1); integers closed under + and * | school algebra; ch07 (promised): prp-integers-closed; verify/ch05/exr-quantifier-rhetoric-b2.py
exr-quantifier-rhetoric-c1 (solution): max, min of two reals; x >= y, x >= 0 give x^2 >= xy; x = -1, y = -2 | school algebra; trichotomy; verify/ch05/exr-quantifier-rhetoric-c1.py
exr-quantifier-rhetoric-c2 (solution): an integer beyond 1/x | school fact of exm-rhetoric-existential; verify/ch05/exr-quantifier-rhetoric-c2.py
exr-quantifier-rhetoric-c2 (solution): the other answer, x^2 continuous but not uniformly continuous on R | exm-square-not-uniform (cited)
-->
