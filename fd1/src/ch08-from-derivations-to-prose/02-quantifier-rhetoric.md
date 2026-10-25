# The Quantifier Rules in Prose

Section 8.1 read the connective rules in the sentences of written proofs. The statements of analysis, though, are made of "for every" and "there exists", and most of the words in an analysis proof carry a quantifier rule: "let", "fix", "choose", "take", "will do". This section completes the dictionary with the rows for the quantifiers, equality and unique existence, for definitions, "the" and double inclusion, and for the patterns that are not single rules but are written as if they were: the lemma ("it suffices to show") and its two "stronger" cases, induction, and symmetry ("without loss of generality"). It also makes exact one habit of analysis prose, the parenthesis "(depending on \( \varepsilon \))".

## Three sentences, three rules

Section 6.1 derived "if \( a_n \to L \), then \( 2a_n \to 2L \)" in sixteen lines. Written the way a mathematician writes it, the same argument takes three sentences:

> Let \( \varepsilon > 0 \). Since \( a_n \to L \) and \( \varepsilon/2 > 0 \), we may choose \( N \in \nN \) (depending on \( \varepsilon \)) such that \( \abs{a_n - L} < \varepsilon/2 \) for every \( n \ge N \). Then for every \( n \ge N \), \( \abs{2a_n - 2L} = 2\abs{a_n - L} < \varepsilon \).

Here is the derivation of Section 6.1 again, with the same line numbers. To keep its lines short, write \( A(n, \varepsilon) \) for \( \abs{a_n - L} < \varepsilon \) and \( B(n, \varepsilon) \) for \( \abs{2a_n - 2L} < \varepsilon \).

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to A(n, \varepsilon))}
  \open[\varepsilon_0]
  \hypo {2} {\varepsilon_0 > 0}
  \have {3} {\varepsilon_0 / 2 > 0} \by{arith}{2}
  \have {4} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to A(n, \varepsilon_0 / 2))} \Ae{1,3}
  \open[N_0]
  \hypo {5} {N_0 \in \nN}
  \hypo {6} {\forall n \in \nN \; (n \ge N_0 \to A(n, \varepsilon_0 / 2))}
  \open[n_0]
  \hypo {7} {n_0 \in \nN}
  \have {8} {n_0 \ge N_0 \to A(n_0, \varepsilon_0 / 2)} \Ae{6,7}
  \open
  \hypo {9} {n_0 \ge N_0}
  \have {10} {A(n_0, \varepsilon_0 / 2)} \ie{8,9}
  \have {11} {B(n_0, \varepsilon_0)} \by{arith}{10}
  \close
  \have {12} {n_0 \ge N_0 \to B(n_0, \varepsilon_0)} \ii{9-11}
  \close
  \have {13} {\forall n \in \nN \; (n \ge N_0 \to B(n, \varepsilon_0))} \Ai{7-12}
  \have {14} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to B(n, \varepsilon_0))} \Ei{5,13}
  \close
  \have {15} {\exists N \in \nN \; \forall n \in \nN \; (n \ge N \to B(n, \varepsilon_0))} \Ee{4,5-14}
  \close
  \have {16} {\forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to B(n, \varepsilon))} \Ai{2-15}
\end{nd}$
\end{center}
```

| Sentence | Lines |
|---|---|
| "Let \( \varepsilon > 0 \)." | opens the box 2–15; its closing line 16 is not written |
| "Since \( a_n \to L \) and \( \varepsilon/2 > 0 \), we may choose \( N \) …" | 3 and 4, then opens the box 5–14 |
| "Then for every \( n \ge N \), \( \abs{2a_n - 2L} = 2\abs{a_n - L} < \varepsilon \)." | 7–13 |
| (the paragraph ends) | 14, 15, 16 |

Each sentence opens a box, and the boxes are nested in the order of the sentences.

- "Let \( \varepsilon > 0 \)" opens the bounded \( \rulename{\forall I} \) box of lines 2–15 in the derivation above, with the fresh name \( \varepsilon_0 \). Its closing line, line 16, is not written: the paragraph simply ends, and a reader who heard "let" knows that the box closes there.
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

In the paragraph that opened this section, \( N \) was chosen "(depending on \( \varepsilon \))". Section 6.4 read off a derivation the rule behind the parenthesis:

*A constant chosen in a box may depend on the names of the boxes open around that box, and it does depend only on the names in the line it comes from.*

In the derivation of Section 6.1, the witness \( N_0 \) is obtained at line 5 from line 4, which mentions \( \varepsilon_0 \), inside the box of \( \varepsilon_0 \) only. So \( N_0 \) may depend on \( \varepsilon_0 \), and it does. In the derivation of @exm-uniform-implies-continuous, the witness \( \delta_0 \) is obtained inside the boxes of \( x_0 \) and \( \varepsilon_0 \), so it **may** depend on both; but it comes from a line that mentions \( \varepsilon_0 \) alone, so it **does** depend only on \( \varepsilon_0 \), and that is uniformity.

```{=latex}
\begin{center}
\begin{tikzpicture}[>=Stealth]
  \node[font=\small] at (2.6,3.75) {(a) continuity at every point};
  \draw[rounded corners] (0,0) rectangle (5.2,3.35);
  \node[anchor=north west, font=\small] (xa) at (0.1,3.3) {let $x \in A$};
  \draw[rounded corners] (0.3,0.25) rectangle (4.9,2.75);
  \node[anchor=north west, font=\small] (ea) at (0.4,2.7) {let $\varepsilon > 0$};
  \draw[rounded corners] (0.6,0.5) rectangle (4.6,2.1);
  \node[anchor=north west, font=\small] (da) at (0.7,2.05) {choose $\delta$};
  \node[draw, font=\scriptsize, align=center] at (2.6,1.0) {the line $\delta$ comes from:\\mentions $x$ and $\varepsilon$};
  \draw[->] (da.east) to[out=0, in=0, looseness=1.6] (ea.east);
  \draw[->] (da.east) to[out=10, in=0, looseness=1.4] (xa.east);
  \begin{scope}[xshift=6cm]
    \node[font=\small] at (2.6,3.75) {(b) uniform continuity};
    \draw[rounded corners] (0,0) rectangle (5.2,3.35);
    \node[anchor=north west, font=\small] (xb) at (0.1,3.3) {let $x \in A$};
    \draw[rounded corners] (0.3,0.25) rectangle (4.9,2.75);
    \node[anchor=north west, font=\small] (eb) at (0.4,2.7) {let $\varepsilon > 0$};
    \draw[rounded corners] (0.6,0.5) rectangle (4.6,2.1);
    \node[anchor=north west, font=\small] (db) at (0.7,2.05) {choose $\delta$};
    \node[draw, font=\scriptsize, align=center] at (2.6,1.0) {the line $\delta$ comes from:\\mentions $\varepsilon$ only};
    \draw[->] (db.east) to[out=0, in=0, looseness=1.6] (eb.east);
    \draw[->, dashed] (db.east) to[out=10, in=0, looseness=1.4] node[pos=0.55, right, font=\scriptsize] {may, but does not} (xb.east);
  \end{scope}
\end{tikzpicture}
\end{center}
```

*A chosen constant **may** depend on the names of the boxes it sits in, and **does** depend only on the names in the line it comes from (the solid arrows).*

Numbers show why the arrows matter. Take \( f(x) = x^2 \) and \( \varepsilon = 1 \). At the point \( a \ge 0 \), the largest \( \delta \) with \( \abs{x^2 - a^2} < 1 \) for every \( x \) with \( \abs{x - a} < \delta \) is \( \sqrt{a^2 + 1} - a \): about \( 0.41 \) at \( a = 1 \), and about \( 0.005 \) at \( a = 100 \). No single \( \delta \) serves every point, so \( \delta \) must depend on the point as well as on \( \varepsilon \): panel (a). For \( f(x) = 3x + 1 \), \( \abs{f(x) - f(a)} = 3\abs{x - a} \), so \( \delta = \varepsilon/3 \) works at every point at once: \( \delta \) depends on \( \varepsilon \) only, panel (b).

The parenthesis is the prose record of this. "Choose \( N \) (depending on \( \varepsilon \))" says: the boxes open here are those of \( \varepsilon \) (besides the data of the theorem, such as the sequence), and the line from which \( N \) comes mentions \( \varepsilon \). "Choose \( \delta \) (depending on \( \varepsilon \) and on \( x \))" says that \( \delta \) came from a line mentioning both, inside both boxes. A witness that came from a line mentioning neither is a constant, and the proof may say "(depending on neither)" or simply "a fixed \( \delta \)". This is why proofs in analysis say what each chosen constant depends on. A missing parenthesis is not a wrong step, but it hides the one fact a reader most needs in order to check the quantifier order, and many false proofs in analysis go wrong exactly there.

::: {.check}
For \( f(x) = x^2 \) and \( \varepsilon = 1 \), does \( \delta = 0.1 \) work at the point \( a = 2 \)? At \( a = 10 \)?
:::

::: {.solution}
At \( a = 2 \), yes, since \( 0.1 < \sqrt 5 - 2 \approx 0.236 \). At \( a = 10 \), no: \( x = 10.06 \) has \( \abs{x - 10} = 0.06 < 0.1 \) and \( x^2 - 100 = 1.2036 \ge 1 \).
:::

::: {#exm-rhetoric-existential}
[The reciprocals tend to zero]

Prove that \( 1/n \to 0 \), for the sequence \( (1/n)_{n \ge 1} \). Annotate each phrase with its rule, and state what the chosen constant depends on.
:::

::: {.solution}
The sequence starts at \( n = 1 \), so in the definition of Section 6.1 the numbers \( N \) and \( n \) range over the positive integers \( \nZ_{>0} \). We use one school fact about the real numbers: for every real number \( u \) there is an integer greater than \( u \). (It follows from the axioms for the real numbers; here we take it as known.)

Let \( \varepsilon > 0 \) [\( \rulename{\forall I} \), opening]. It suffices to find \( N \in \nZ_{>0} \) with
\[
\frac{1}{N} < \varepsilon , \tag{$\ast$}
\]
since then every \( n \in \nZ_{>0} \) with \( n \ge N \) has \( 0 < 1/n \le 1/N < \varepsilon \), so \( \abs{1/n - 0} < \varepsilon \) [it suffices: the claim (\( \ast \)) displayed, then used].

By the school fact, applied to \( u = 1/\varepsilon \) [\( \rulename{\forall E} \)], there is an integer greater than \( 1/\varepsilon \); choose such an integer \( N \) [\( \rulename{\exists E} \)], which depends on \( \varepsilon \). Since \( \varepsilon > 0 \), we have \( 1/\varepsilon > 0 \), so \( N > 0 \) and \( N \in \nZ_{>0} \). From \( N > 1/\varepsilon > 0 \), taking reciprocals reverses the inequality: \( 1/N < \varepsilon \), which is (\( \ast \)). So this \( N \) will do [\( \rulename{\exists I} \)], and \( 1/n \to 0 \).

Read the proof as a skeleton. The first sentence opens the box of \( \varepsilon \). The second is an "it suffices to show", in the sense of the row below: it states a simpler claim (\( \ast \)), shows on the spot that (\( \ast \)) is enough, and leaves (\( \ast \)) to be proved. The next paragraph proves (\( \ast \)). It contains two different quantifier steps that both concern \( N \): "choose" is the \( \rulename{\exists E} \) on the school fact, which hands over some integer beyond \( 1/\varepsilon \) and calls it \( N \); "will do" is the \( \rulename{\exists I} \) that offers this \( N \) as the witness the definition asks for. Between them, the clause "so \( N > 0 \) and \( N \in \nZ_{>0} \)" checks the bound \( N \in \nZ_{>0} \) of the witness, which the bounded \( \rulename{\exists I} \) needs as a line.

The constant \( N \) depends on \( \varepsilon \) only: it came from the school fact at \( 1/\varepsilon \), inside the box of \( \varepsilon \). For instance, \( \varepsilon = 0.03 \) has \( 1/\varepsilon = 33.3\ldots \), and \( N = 34 \) is a choice that works; so is any larger integer.
:::

::: {.check}
"For every \( \varepsilon > 0 \), \( \abs{a_n - L} < \varepsilon \) for all large \( n \)." Where is the hidden \( \exists N \), and between which two quantifiers does it stand?
:::

::: {.solution}
"For all large \( n \)" is "there is an \( N \) such that for every \( n \ge N \)" (Section 6.1): the hidden \( \exists N \) stands after \( \forall \varepsilon > 0 \) and before \( \forall n \ge N \). Written out, the sentence is \( \forall \varepsilon > 0 \; \exists N \in \nN \; \forall n \in \nN \; (n \ge N \to \abs{a_n - L} < \varepsilon) \), the definition of \( a_n \to L \). Since \( \exists N \) comes after \( \forall \varepsilon \), the \( N \) may depend on \( \varepsilon \).
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
where each \( = \) link substitutes equals for equals and each inequality link applies one fact about order (Section 5.7). (Here \( \abs{x - 2} < 1 \) gives \( 1 < x < 3 \), so \( 3 < x + 2 < 5 \).) The \( \rulename{{=}I} \) lines \( t = t \) that such chains rest on are never written. Unique existence (@def-unique-existence) has two halves, which @prp-unique-existence-use separates: "\( 2x + 3 = 7 \) has exactly one real solution: \( x = 2 \) is one, and if \( 2y + 3 = 7 \), then \( y = 2 \)". The first clause is existence, by \( \rulename{\exists I} \); the second is uniqueness, a \( \rulename{\forall I} \) and \( \rulename{{\to}I} \) box on a second candidate. Neither half implies the other, so neither may be silent.

The uniqueness half often stands alone, when existence is not claimed or is proved elsewhere. Uniqueness of limits is a case of this kind.

::: {#exm-rhetoric-equality}
[A sequence has at most one limit]

Let \( (a_n) \) be a sequence of real numbers with \( a_n \to L \) and \( a_n \to M \). Prove that \( L = M \), and annotate each phrase with its rule.
:::

::: {.solution}
Let \( \varepsilon > 0 \) [\( \rulename{\forall I} \), opening]. Then \( \varepsilon/2 > 0 \), so, applying the definition of \( a_n \to L \) with \( \varepsilon/2 \) in place of \( \varepsilon \) [\( \rulename{\forall E} \)], we may choose \( N_1 \in \nN \) (depending on \( \varepsilon \)) such that \( \abs{a_n - L} < \varepsilon/2 \) for every \( n \ge N_1 \) [\( \rulename{\exists E} \), fresh name \( N_1 \)]. Likewise, from \( a_n \to M \), choose \( N_2 \in \nN \) (depending on \( \varepsilon \)) such that \( \abs{a_n - M} < \varepsilon/2 \) for every \( n \ge N_2 \) [\( \rulename{\forall E} \), \( \rulename{\exists E} \), fresh name \( N_2 \)]. Let \( n \coloneqq \max\{N_1, N_2\} \). Then \( n \in \nN \), \( n \ge N_1 \) and \( n \ge N_2 \), so both bounds apply at \( n \) [\( \rulename{\forall E} \) at \( n \), twice, with \( \rulename{{\to}E} \)], and
\[
\begin{aligned}
\abs{L - M} &= \abs{(L - a_n) + (a_n - M)} \\
&\le \abs{a_n - L} + \abs{a_n - M} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon ,
\end{aligned}
\]
where the inequality is the triangle inequality of @exm-triangle-inequality-cases, with \( \abs{L - a_n} = \abs{a_n - L} \). Since \( \varepsilon > 0 \) was arbitrary, \( \abs{L - M} < \varepsilon \) for every \( \varepsilon > 0 \) [\( \rulename{\forall I} \), closing], and @prp-arbitrarily-close-equal gives \( L = M \) [\( \rulename{{\to}E} \), citing it].

Four things in this proof are never silent, and each is visible. The instance \( \varepsilon/2 \) is named twice, because it is not the obvious instance. The two witnesses get two names, \( N_1 \) and \( N_2 \): the hypotheses promise a threshold for \( L \) and a threshold for \( M \), and nothing says they are the same number, so calling both \( N \) would assert an equality nobody proved (Section 8.6 catalogues the error). The point \( n = \max\{N_1, N_2\} \) is named, since the bounds are applied at it. And the closing result is cited by name.
:::

::: {.second-reading title="The bookkeeping of the two choices"}
What is silent is the bookkeeping of the two \( \rulename{\exists E} \) boxes. The line \( \abs{L - M} < \varepsilon \) mentions neither \( N_1 \), \( N_2 \) nor \( n \), so the side condition of \( \rulename{\exists E} \) lets it leave both boxes, and then the box of \( \varepsilon \) closes on it. The calculation chain hides its \( \rulename{{=}E} \) steps, as the row allows. The proof shows that a sequence has **at most one** limit: the uniqueness half of \( \exists! \). Whether a given sequence has a limit at all is a separate question, which this proof does not touch.
:::

## Definitions, descriptions and sets

Three more phrases do logical work in almost every chapter of analysis: "we define", "the", and "the two sets are equal".

| Pattern | Phrases | Silent in plain prose? |
|---|---|---|
| a definition (a definitional extension, @prp-definitional-extension) | "we define \( f(x) \coloneqq \dots \)"; "call \( n \) *perfect* if …"; "write \( d \) for …" | never the definition; its uses (\( \rulename{{\leftrightarrow}E} \) or \( \rulename{{=}E} \) with it) yes |
| "the" (a definite description, @def-definite-description) | "let \( L \) be the limit of \( (a_n) \)"; "the least element of \( A \)"; "\( \lim a_n \)" | never the existence and uniqueness behind "the": proved or cited before the name is used |
| double inclusion | "we show \( A \subseteq B \) and \( B \subseteq A \)"; element chasing: "let \( x \in A \); … so \( x \in B \)"; "so \( A = B \)" | never either inclusion, nor the opening "let \( x \in \dots \)" of each, nor the appeal to extensionality that turns "the same elements" into \( A = B \) |

"The", as in "the limit", names an object. It may be used only once there is exactly one such object (Section 5.8): for a limit, existence is the hypothesis that \( (a_n) \) converges, and uniqueness is @exm-rhetoric-equality. Chapter 5 read \( A \subseteq B \) as \( \forall x\, (x \in A \to x \in B) \). Two inclusions give \( \forall x\, (x \in A \leftrightarrow x \in B) \), by \( \rulename{{\leftrightarrow}I} \) inside \( \rulename{\forall I} \): the two sets have the same elements. Each inclusion is an **element chase**: "let \( x \in A \)" opens a bounded \( \rulename{\forall I} \) box whose last line is \( x \in B \). The last step, from "the same elements" to \( A = B \), is not logic. Logic gives only the converse, that equal sets have the same elements (@exm-extensionality-logical-half). The step itself is the **axiom of extensionality**, an axiom about sets (Section 5.7), and a proof cites it, as a premise or with the words "by extensionality"; it is never silent.

::: {.second-reading title="What a definition adds"}
A definition adds a word and proves nothing new about the old words (@prp-definitional-extension, Section 5.8). So "we define" writes an abbreviation, and every later use of it is \( \rulename{{\leftrightarrow}E} \) or \( \rulename{{=}E} \) with the definition.
:::

::: {#exm-rhetoric-double-inclusion}
[Two inclusions]

Let \( A \coloneqq \{ x \in \nR : x^2 \le 2x \} \) and \( B \coloneqq \{ x \in \nR : 0 \le x \le 2 \} \). Prove that \( A = B \), and tag the steps that carry the logic.
:::

::: {.solution}
- \( (\subseteq) \) Let \( x \in A \) [assumption for \( \rulename{\forall I} \)]; so \( x^2 \le 2x \), that is, \( x(x - 2) \le 0 \).
  - If \( x < 0 \), then \( x - 2 < 0 \) too, and a product of two negative numbers is positive: \( x(x - 2) > 0 \). This clashes with \( x(x - 2) \le 0 \) [\( \rulename{\neg E} \)], so \( x < 0 \) is impossible [\( \rulename{\neg I} \)], and \( x \ge 0 \) by trichotomy.
  - If \( x > 2 \), then both factors are positive and the same clash follows. So \( x \le 2 \).
  - Hence \( 0 \le x \le 2 \) [\( \rulename{\wedge I} \)], and \( x \in B \).
- \( (\supseteq) \) Let \( x \in B \) [assumption for \( \rulename{\forall I} \)]; so \( x \ge 0 \) and \( x - 2 \le 0 \) [\( \rulename{\wedge E} \)]. A product of a non-negative and a non-positive number is at most \( 0 \), so \( x(x - 2) \le 0 \), that is, \( x^2 \le 2x \), and \( x \in A \).
- So \( A \subseteq B \) and \( B \subseteq A \): every real \( x \) has \( x \in A \leftrightarrow x \in B \) [\( \rulename{{\leftrightarrow}I} \) inside \( \rulename{\forall I} \)]. By extensionality, \( A = B \) [\( \rulename{\forall E} \), \( \rulename{{\to}E} \) with the axiom].

The words "that is" unwind the two sets' definitions (\( \rulename{{\leftrightarrow}E} \), silent at level 3).
:::

::: {.check}
To prove \( \{ n \in \nZ : n^2 \text{ is even} \} = \{ n \in \nZ : n \text{ is even} \} \) by double inclusion, which inclusion is a theorem of Chapter 2, and which takes one line?
:::

::: {.solution}
\( \subseteq \) is @thm-square-even-implies-even. \( \supseteq \) is one line: \( n = 2k \) gives \( n^2 = 2(2k^2) \).
:::

## Induction, lemmas and symmetry

The rows of this table are not rules of the calculus. Each is a pattern of rules that proofs announce with a phrase of its own.

| Pattern | Phrases | Silent in plain prose? |
|---|---|---|
| it suffices to show; a lemma (a cut, @lem-weakening-cut) | "we first show (Claim)"; "it suffices to show"; "we claim" | never the claim itself; "it suffices" may be dropped if the claim is displayed and then used |
| it suffices to prove something stronger | "it suffices to prove the stronger …"; "in fact more is true: …" | never the stronger claim; the step from it to the goal may be silent when it is one \( \rulename{\wedge E} \), \( \rulename{\vee I} \) or chain link |
| a stronger hypothesis gives a weaker theorem | "in particular, for \( x \in (0, 1) \)"; "since every such \( x \) has \( \abs{x} < 1 \), the result applies" | the narrowing of the hypothesis, never |
| induction (@ax-induction, @thm-strong-induction) | "we argue by induction on \( n \)"; "base case"; "suppose the claim holds for \( n \)" | never either the base case or the step; the induction hypothesis is stated |
| symmetry | "without loss of generality"; "similarly"; "by symmetry" | allowed only when the swap turns the statement and the hypotheses into themselves, up to identities such as \( \abs{b - a} = \abs{a - b} \) |

### It suffices to show

"It suffices to show \( \varphi \)" does two things. It shows on the spot that \( \varphi \) gives the goal, and it leaves \( \varphi \) to be proved: the goal is replaced by \( \varphi \). As Section 1.3 observed, to show \( \psi \) it suffices to show \( \varphi \) when \( \varphi \to \psi \) is in hand. A lemma is the same move in the other order: prove \( \varphi \) first, then use it as if it were a premise. (Logicians call both a **cut**; @lem-weakening-cut (b) is the precise statement.) In analysis, "it suffices to show \( \abs{a_n - L} < \varepsilon \) for \( n \ge N \)" reduces a limit to one estimate; @exm-rhetoric-existential made one with the claim (\( \ast \)).

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc step] (g) {the goal};
  \node[fc step, below=of g] (c) {the claim $\varphi$};
  \node[fc step, below=of c] (h) {the hypotheses};
  \draw[fc arrow] (c) -- node[right, font=\scriptsize] {shown at once} (g);
  \draw[fc arrow, dashed] (h) -- node[right, font=\scriptsize] {proved next} (c);
\end{tikzpicture}
\end{center}
```

*"It suffices to show \( \varphi \)": the solid step is written on the spot, the dashed one is the rest of the proof.*

::: {.check}
In @exm-rhetoric-existential, which sentence is the "it suffices" step, and what does it leave to prove?
:::

::: {.solution}
"It suffices to find \( N \in \nZ_{>0} \) with \( 1/N < \varepsilon \), since then …". It leaves (\( \ast \)), which the next paragraph proves.
:::

Two cases of the move have names of their own. To prove \( \psi \) it suffices to prove a **stronger** \( \varphi \) from which \( \psi \) follows at once: to show \( x^2 < 1 \) for \( 0 < x < 1 \), show \( x^2 < x \), and then \( x^2 < x < 1 \). And a theorem stays true when its hypothesis is narrowed: from "if \( \abs{x} < 1 \), then \( x^2 < 1 \)" and "every \( x \in (0, 1) \) has \( \abs{x} < 1 \)", the chain of @prp-implication-transitive gives "if \( x \in (0, 1) \), then \( x^2 < 1 \)": a stronger hypothesis, a weaker theorem.

::: {.second-reading title="Stronger and weaker, in general"}
Both moves are instances of one fact about where a part sits in a formula. Weakening a part in a positive place, such as the conclusion of an implication, weakens the whole; weakening a part in a negative place, such as the hypothesis, strengthens the whole. The second-pass Section 4.9 states and proves this as @thm-monotonicity; nothing on the main line uses it.
:::

### Induction

An induction is \( \rulename{{\to}E} \) applied to @ax-induction, whose hypothesis is a conjunction: the base case \( P(0) \), and the step "**for every** \( n \in \nN \), if \( P(n) \) then \( P(n + 1) \)". So the step is a \( \rulename{\forall I} \) box with a \( \rulename{{\to}I} \) box inside it, and the phrase "suppose the claim holds for \( n \)" opens the inner box; its assumption is the **induction hypothesis**, and it must be stated, because the step uses it.

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc step] (b) {base case:\\$P(0)$};
  \node[fc step, right=of b] (s) {step: let $n \in \nN$;\\suppose $P(n)$; \dots; $P(n + 1)$};
  \coordinate (m) at ($(b.south)!0.5!(s.south)$);
  \node[fc start, below=10mm of m] (c) {$\forall n \in \nN\; P(n)$};
  \draw[fc arrow] (b.south) -- (c);
  \draw[fc arrow] (s.south) -- (c);
  \node[font=\scriptsize, right=3mm of c] {$\to$E on the induction axiom};
\end{tikzpicture}
\end{center}
```

*An induction: two inputs to one implication, the induction axiom (@ax-induction). The step is two boxes, the box of \( n \) and, inside it, the box of the induction hypothesis \( P(n) \).*

### Without loss of generality

Symmetry is a case split \( \rulename{\vee E} \) whose second box is the first with two letters exchanged. "Without loss of generality \( x \le y \)" writes the first box and leaves the second to the reader, who must be able to get it by swapping the letters; that works when the statement and the hypotheses come back unchanged under the swap, up to identities such as \( \abs{b - a} = \abs{a - b} \).

```{=latex}
\begin{center}
\begin{tikzpicture}[flowchart]
  \node[fc step] (l) {case $a \le b$:\\\dots\ $\Longrightarrow$ claim};
  \node[fc step, dashed, right=of l] (r) {case $b \le a$: the same lines\\with $a$, $b$ swapped $\Longrightarrow$ claim};
  \draw[fc arrow] (l) -- node[above, font=\scriptsize] {swap $a \leftrightarrow b$} (r);
  \coordinate (m) at ($(l.south)!0.5!(r.south)$);
  \node[fc start, below=10mm of m] (e) {$\vee$E on ``$a \le b$ or $b \le a$''};
  \draw[fc arrow] (l.south) -- (e);
  \draw[fc arrow] (r.south) -- (e);
\end{tikzpicture}
\end{center}
```

*"Without loss of generality \( a \le b \)": the solid case is written, the dashed one is left to the reader, who gets it by the swap.*

::: {.check}
May a proof that \( x^2 + y^2 \ge 2xy \) for all real \( x \), \( y \) begin "Without loss of generality \( x \le y \)"?
:::

::: {.solution}
Yes: swapping \( x \) and \( y \) leaves the statement unchanged, and there are no hypotheses. The case split is legitimate, though not needed, since \( x^2 + y^2 - 2xy = (x - y)^2 \ge 0 \).
:::

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

**The hidden universal closure.** A theorem stated as "if \( n \) is even, then \( n^2 \) is even" means "for every integer \( n \), if \( n \) is even, then \( n^2 \) is even". Section 5.1 introduced this convention: *a letter that is not introduced anywhere, in the statement of a theorem, is read with a "for every" in front of the whole statement.* It applies to the statement of a theorem, lemma or exercise, not to a line inside a proof: inside a proof every letter has been introduced by a "let" or a "choose", and its box tells the reader which. The proof of such a theorem begins by opening the hidden box: "let \( n \) be an integer".

**"For all large \( n \)"** hides an \( \exists N \) and a bound, as the Quick check above found. "Eventually" means the same. The negation of "\( P(n) \) for all large \( n \)" is "for every \( N \) there is an \( n \ge N \) for which \( P(n) \) fails", usually said "\( P(n) \) fails for infinitely many \( n \)".

**"Any"** can mean "every" or "some", and only the rest of the sentence decides (Section 5.1). "Any \( x \in A \) is positive" means every element of \( A \) is positive. "If any \( x \in A \) is positive, then \( A \) is non-empty" means: if **some** element of \( A \) is positive. When "any" appears, rewrite the sentence once with "every" and once with "some", and keep the one that was meant.

**Quantifiers at the end of a sentence.** English lets a writer put "for some \( x \)" or "for all \( y \)" after the formula they govern, and then the order of two such phrases is unclear. "\( x^2 > y \) for some \( x \) for all \( y \)", over \( \nR \), has two readings:
\[
\forall y\, \exists x\; (x^2 > y) \qquad \text{and} \qquad \exists x\, \forall y\; (x^2 > y) .
\]
The first is true (for \( y \ge 0 \) take \( x = y + 1 \), since \( (y + 1)^2 = y^2 + 2y + 1 > y \); for \( y < 0 \) take \( x = 0 \)). The second is false (whatever \( x \) is proposed, \( y = x^2 \) refutes it). The remedy is to write the quantifiers of such a statement **in front**, in the order in which they apply. A trailing phrase such as "for every \( n \ge N \)" is safe only when it is the last quantifier of the sentence, as in the definition of \( a_n \to L \).

::: {.warning}
Moving "for all \( x \)" to the end of a sentence can change continuity into uniform continuity. "\( \abs{f(x) - f(y)} < \varepsilon \) whenever \( \abs{x - y} < \delta \), for all \( x \)", written after "for every \( \varepsilon > 0 \) there is \( \delta > 0 \) such that", does not say whether \( \forall x \) comes before \( \exists \delta \) (continuity at every point) or after it (uniform continuity). The two formulas of Section 6.4 differ exactly there, and @exm-square-not-uniform shows that the difference is real: \( f(x) = x^2 \) on \( \nR \) satisfies the first and not the second. Write the quantifiers in front.
:::

::: {.warning}
[Not allowed: quantifier steps in prose]

Each sentence below might appear in a proof, and each is wrong. The tag names the entry of the catalogue in Section 8.6, or the item of the convention on silent steps in Section 8.3, that it breaks.

- "Let \( \varepsilon > 0 \) and choose \( N \) with \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N \). This \( N \) works for every \( \varepsilon > 0 \)." The \( N \) was chosen inside the box of one \( \varepsilon \): (N2).
- "Some \( x \in A \) has \( f(x) > 0 \). Let \( x \in A \); then \( f(x) > 0 \)." The witness of an existential is *chosen* ("choose \( x \in A \) with \( f(x) > 0 \)", \( \rulename{\exists E} \) with a fresh name). Written with "let", the second sentence claims \( f(x) > 0 \) for every \( x \in A \): (N3).
- "Choose \( N \) with \( \abs{a_n - L} < \varepsilon/2 \) for \( n \ge N \), and \( N \) with \( \abs{b_n - M} < \varepsilon/2 \) for \( n \ge N \)." One name for two witnesses: (N4).
- "Let \( L \) be the limit of \( (a_n) \)", in a proof that has not shown that \( (a_n) \) converges: (N14).
- "Let \( \varepsilon > 0 \). Then \( \abs{a_n - L} < \varepsilon \) for every \( n \ge N \), as required", where no sentence says what \( N \) is. The witness of \( \rulename{\exists I} \), with what it depends on, is never silent (@def-silent-steps, Section 8.3).
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

::: {#exr-quantifier-rhetoric-a2}
[A2: Drill]

Each part takes a line or two. Most parts ask which rule a phrase carries, whether it may be silent, or for a judgment or a sentence.

::: {.enumerate options="label=(\alph*)"}
1. "Fix \( \varepsilon > 0 \)." Which rule, and may it be silent?
2. "Applying the hypothesis with \( \varepsilon/3 \) in place of \( \varepsilon \)." Which rule, and may the term go unnamed?
3. "Take \( \delta \coloneqq \varepsilon/5 \)." Which rule, may it be silent, and what does \( \delta \) depend on?
4. "By hypothesis there is \( k \) with \( m = 2k + 1 \); choose such a \( k \)." Which rule, and what does it require of the name?
5. In "Let \( \varepsilon > 0 \). Choose \( N \) such that … . Let \( n \ge N \).", may \( N \) depend on \( n \)?
6. In "Let \( x \in A \). Let \( \varepsilon > 0 \). Choose \( \delta > 0 \) such that …", may \( \delta \) depend on \( x \)?
7. Write "\( x^2 > 0 \) for all \( x \ne 0 \)" with the quantifier in front.
8. Negate "\( a_n > 0 \) for all large \( n \)" with no \( \neg \) in front of a quantifier.
9. A proof of "\( \max\{a, b\} \ge a \)" begins "Without loss of generality \( a \le b \)." Is that legitimate?
10. In an induction, which sentence opens the box of the induction hypothesis?
11. To prove \( A = B \), a proof shows \( A \subseteq B \) and \( B \subseteq A \). Which rules does that pattern use, and how does each inclusion open?
12. A proof begins "Let \( m \) be the least element of \( A \)". What must already be on the page?
:::
:::

::: {.solution}
(a) Bounded \( \rulename{\forall I} \), opening; never silent.

(b) \( \rulename{\forall E} \) at a term that is not the obvious one; the term must be named.

(c) \( \rulename{\exists I} \)'s witness, written before the work; never silent; it depends on \( \varepsilon \).

(d) \( \rulename{\exists E} \), with a fresh name.

(e) No: the box of \( n \) opens after \( N \) is chosen.

(f) It may, since both boxes are open; whether it does depends on the line it comes from.

(g) \( \forall x\, (x \ne 0 \to x^2 > 0) \).

(h) For every \( N \) there is \( n \ge N \) with \( a_n \le 0 \).

(i) No: the swap turns the claim into \( \max\{b, a\} \ge b \), a different claim; each case needs its own line (both are one line long).

(j) "Suppose \( P(n) \) holds", inside "Let \( n \in \nN \)".

(k) \( \rulename{{\leftrightarrow}I} \) inside \( \rulename{\forall I} \), for \( \forall x\, (x \in A \leftrightarrow x \in B) \); then \( A = B \) by \( \rulename{\forall E} \) and \( \rulename{{\to}E} \) with the axiom of extensionality, cited. Each inclusion is a bounded \( \rulename{\forall I} \) that opens with "let \( x \in A \)" (or "let \( x \in B \)").

(l) That such an element exists and that there is only one (\( \exists! \), a definite description). Uniqueness is one line, since two least elements are each at most the other; existence is the part that needs a reason.
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

::: {#exr-quantifier-rhetoric-b3}
[B3: Six, two and three, used later]

Let \( A \coloneqq \{ n \in \nZ : 6 \mid n \} \) and \( B \coloneqq \{ n \in \nZ : 2 \mid n \text{ and } 3 \mid n \} \). Prove \( A = B \) by double inclusion. Name each "let", each "choose" with its fresh name, and each witness.
:::

::: {.solution}
- \( (\subseteq) \) Let \( n \in A \) [\( \rulename{\forall I} \)], and choose \( k \) with \( n = 6k \) [\( \rulename{\exists E} \), \( k \) fresh]. Then \( n = 2(3k) \) and \( n = 3(2k) \), so \( 2 \mid n \) and \( 3 \mid n \), with the witnesses \( 3k \) and \( 2k \) [\( \rulename{\exists I} \) twice, \( \rulename{\wedge I} \)]; so \( n \in B \).
- \( (\supseteq) \) Let \( n \in B \) [\( \rulename{\forall I} \)]. Choose \( a \) with \( n = 2a \) and \( b \) with \( n = 3b \) [\( \rulename{\exists E} \) twice, two fresh names: one name for both would be (N4)]. Then \( b = 3b - 2b = n - 2b = 2a - 2b = 2(a - b) \), so \( n = 3b = 6(a - b) \), and \( 6 \mid n \) with the witness \( a - b \) [\( \rulename{\exists I} \)]; so \( n \in A \).
- So every integer \( n \) has \( n \in A \leftrightarrow n \in B \) [\( \rulename{{\leftrightarrow}I} \) inside \( \rulename{\forall I} \)], and by extensionality \( A = B \).

The two \( \rulename{\exists E} \) boxes of \( (\supseteq) \) close on "\( n \in A \)", which mentions neither \( a \) nor \( b \).

**Marking scheme.** (10 points)
- 2: \( (\subseteq) \), with \( k \) chosen and both witnesses written.
- 4: \( (\supseteq) \): two choices with distinct names (1); the computation \( b = 2(a - b) \), or another valid route to an integer \( c \) with \( n = 6c \) (2); the witness named (1).
- 2: the double-inclusion frame: both inclusions, each opened by "let \( n \in \dots \)", and the conclusion \( A = B \) by extensionality, cited.
- 2: the tags: \( \rulename{\forall I} \), \( \rulename{\exists E} \) with fresh names, \( \rulename{\exists I} \).

Fatal errors (0 for the step): one name for both witnesses; "\( 2 \mid n \) and \( 3 \mid n \), so \( 6 \mid n \)" asserted without an argument (N9).
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
quantifier-rhetoric-reprint (example): the derivation of Section 6.1 reprinted line for line, with A(n, eps), B(n, eps) abbreviating |a_n - L| < eps and |2a_n - 2L| < eps; the bracket table's line ranges | F1.8 §01's derivation (06-translation.md, the 16-line block after the outline; abbreviations only)
quantifier-rhetoric-dependency (claim): a chosen constant may depend on the names of the open boxes and does depend only on the names in its line; the picture's panels | F1.8 §04's reading of dependence (prose pointer); exm-uniform-implies-continuous (cited)
quantifier-rhetoric-dependency (claim): for f(x) = x^2, eps = 1, a >= 0 the largest delta is sqrt(a^2 + 1) - a, about 0.41 at a = 1, 0.005 at a = 100, 0.236 at a = 2; delta = 0.1 fails at a = 10 (x = 10.06, x^2 - 100 = 1.2036); for 3x + 1, delta = eps/3 | school algebra; verify/ch08/exm-rhetoric-existential.py
exm-rhetoric-universal (solution): |c - c| = 0 < eps | arithmetic
exm-rhetoric-existential (solution): for every real u there is an integer N > u | school fact stated in the solution (follows from the axioms for the real numbers; AN1.1 thm-naturals-unbounded, no volume named)
exm-rhetoric-existential (solution): 1/eps > 0; N > 1/eps > 0 gives 1/N < eps; n >= N gives 0 < 1/n <= 1/N; eps = 0.03, N = 34 | school algebra; verify/ch08/exm-rhetoric-existential.py
exm-rhetoric-existential (claim): the definition read with N, n in Z_{>0} | exm-translate-limit (a) (Section 6.1's definition; named in the solution)
exm-rhetoric-equality (solution): |u + v| <= |u| + |v|; |-u| = |u|; max{N1, N2} in N; max{N1, N2} >= N1, N2 | exm-triangle-inequality-cases (cited); school facts
exm-rhetoric-equality (solution): |L - M| < eps for all eps > 0 gives L = M | prp-arbitrarily-close-equal (cited)
exm-rhetoric-equality (claim): |x - 2| < 1 gives 3 < x + 2 < 5, |x^2 - 4| <= 5|x - 2|; 2x + 3 = 7 iff x = 2 | school algebra; exm-abs-product-cases; verify/ch08/exm-rhetoric-equality.py
quantifier-rhetoric-definitions (claim): a definition proves nothing new (fold F8.2-c); "the" needs existence and uniqueness; uniqueness of limits is exm-rhetoric-equality | prp-definitional-extension, def-definite-description (F1.4 §08, cited); exm-rhetoric-equality (cited)
quantifier-rhetoric-definitions (claim): A subset B read as forall x (x in A -> x in B); two inclusions give forall x (x in A <-> x in B) by iff-I inside forall-I | F1.4 §01's gloss of subset (prose, "Chapter 5")
quantifier-rhetoric-definitions (claim): the step from the same elements to A = B is the axiom of extensionality, cited, never silent; logic gives only the converse | exm-extensionality-logical-half (F1.4 §07, cited, with its paragraph "For sets, the converse is taken as an axiom"); agrees with F1.4 §08's B4 and F1.6 §02's "Extensionality: an axiom, not a law of logic"
exm-rhetoric-double-inclusion (solution): x^2 <= 2x iff x(x - 2) <= 0; x < 0 or x > 2 gives x(x - 2) > 0; 0 <= x <= 2 gives x(x - 2) <= 0; trichotomy | school order facts (signs of products), trichotomy; the axiom of extensionality (cited); verify/ch08/exm-rhetoric-double-inclusion.py
quantifier-rhetoric-double-inclusion-check (solution): subset is thm-square-even-implies-even; n = 2k gives n^2 = 2(2k^2) | thm-square-even-implies-even (cited); school algebra
quantifier-rhetoric-suffices (claim): "to show psi it suffices to show phi" as Section 1.3 observed; a lemma is a cut | F1.1 §04 (prose); lem-weakening-cut (cited)
quantifier-rhetoric-stronger (claim): 0 < x < 1 gives x^2 < x < 1; the narrowed hypothesis by prp-implication-transitive; |x| < 1 gives x^2 < 1 | prp-implication-transitive (cited); school algebra (the x^2 < x of exm-rhetoric-conjunction, within the chapter)
quantifier-rhetoric-stronger (claim): fold F8.2-a: weakening in a positive place weakens the whole, in a negative place strengthens it | thm-monotonicity (F1.3 §09, second pass; prose pointer in a fold, nothing rests on it)
exm-rhetoric-induction (solution): a^0 = 1, a^(n+1) = a^n a | powers, school meaning; F2.2 (promised): def-power
exm-rhetoric-induction (solution): products of positives; a^n a <= a^n <= 1; a^0 <= a fails for a < 1; |a - b| = max - min | school algebra; trichotomy; verify/ch08/exm-rhetoric-induction.py
exm-rhetoric-induction (claim): the warning's max{2, 1} = 2; the subsection after it: x = y + 1 or x = 0 gives x^2 > y, and y = x^2 refutes exists x forall y | arithmetic; verify/ch08/exm-rhetoric-induction.py
exm-rhetoric-induction (claim): the WLOG check: x^2 + y^2 is symmetric in x, y; x^2 + y^2 - 2xy = (x - y)^2 >= 0 | school algebra; verify/ch08/exm-rhetoric-induction.py
quantifier-rhetoric-not-allowed (claim): the five lines and their tags (N2), (N3), (N4), (N14), and the never-silent exists-I witness | entries of exm-not-allowed-catalogue and def-silent-steps (F1.5 §06, §03; tags within the chapter, not reasons)
exr-quantifier-rhetoric-a1 (solution): -u <= |u|; L - L/2 = L/2 > 0 | exm-triangle-inequality-cases (its lemma); verify/ch08/exr-quantifier-rhetoric-a1.py
exr-quantifier-rhetoric-a2 (solution): (i) the swap of a, b changes max{a, b} >= a into max{a, b} >= b; (k) extensionality cited; (l) two least elements are each at most the other | school facts; exm-extensionality-logical-half (F1.4 §07); def-definite-description (F1.4 §08)
exr-quantifier-rhetoric-b1 (solution): the witnesses M + 1, -y, 1 - y, |x - y|; 1 + delta^2/4 | exm-square-not-uniform (cited); school algebra; verify/ch08/exr-quantifier-rhetoric-b1.py
exr-quantifier-rhetoric-b2 (solution): 5^0 = 1, 5^(n+1) = 5 * 5^n | powers, school meaning; F2.2 (promised): def-power
exr-quantifier-rhetoric-b2 (solution): 5^(n+1) - 1 = 5(5^n - 1) + 4 = 4(5k + 1); integers closed under + and * | school algebra; F2.2 (promised): prp-integers-closed; verify/ch08/exr-quantifier-rhetoric-b2.py
exr-quantifier-rhetoric-b3 (solution): n = 6k gives n = 2(3k) = 3(2k); 2a = 3b gives b = 2(a - b) and n = 6(a - b); A = B | school algebra; F2.2 (promised): prp-integers-closed; verify/ch08/exr-quantifier-rhetoric-b3.py
exr-quantifier-rhetoric-c1 (solution): max, min of two reals; x >= y, x >= 0 give x^2 >= xy; x = -1, y = -2 | school algebra; trichotomy; verify/ch08/exr-quantifier-rhetoric-c1.py
exr-quantifier-rhetoric-c2 (solution): an integer beyond 1/x | school fact of exm-rhetoric-existential; verify/ch08/exr-quantifier-rhetoric-c2.py
exr-quantifier-rhetoric-c2 (solution): the other answer, x^2 continuous but not uniformly continuous on R | exm-square-not-uniform (cited)
-->
