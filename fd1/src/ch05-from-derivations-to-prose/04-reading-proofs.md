# Reading a Proof: Self-Explanation

Section 5.3 showed that a level-3 proof leaves steps unsaid by a fixed convention, and that any doubtful stretch can be expanded and checked. That presupposes a reader who notices the doubtful stretch. This section is about becoming that reader. It teaches one habit, **self-explanation**: for each line of a proof, say what makes it true. The habit is taught here once, on one short proof, and the rest of the book relies on it. When a later proof ends its Idea with "*Before reading on: …*" or "*Self-explain lines 3–5*", this is the passage it means.

## Two readers of one proof

Two people read the same proof, line by line, to the end. Both say they understood it. Asked afterwards whether it was correct, one can answer and point to the reason each line holds; the other can only repeat the proof in other words. What separates them is not intelligence or background. It is what each did at every line.

The first asked, at each line, *what makes this true?* and answered by pointing: to earlier lines, to a definition, to a named result, and to the rule that combines them. The second asked *what does this say?* and answered by restating it. Only the first answer can come out wrong, and that is exactly why it is useful. A restatement always succeeds, so it tests nothing.

*To self-explain a line is to name its warrant: the earlier lines, definitions and results it comes from, and the rule that gets it from them.*

The answer has the shape of a justification column in a derivation. In the derivations of Chapters 1–4 that column was printed beside every line. In level-3 prose it is gone, and self-explanation is the reader writing it back in, at level 1 or 2 of @def-levels-of-proof, one line at a time.

## The training passage

Here is a short proof. Read it once, then read the two explanations that follow.

::: {#exm-self-explanation}
[Explaining a proof, well and badly]

**Claim.** For every real number \( x > 0 \), \( x + 1/x \ge 2 \).

**Proof.** Let \( x > 0 \).

1. \( (x - 1)^2 \ge 0 \).
2. So \( x^2 - 2x + 1 \ge 0 \).
3. Dividing by \( x \), \( x - 2 + 1/x \ge 0 \).
4. Hence \( x + 1/x \ge 2 \).

Self-explain each line of the proof.
:::

::: {.solution}
**Explained well.**

- *The opening.* "Let \( x > 0 \)" opens a box for an arbitrary \( x \) with the assumption \( x > 0 \): the claim is \( \forall x > 0 \; (x + 1/x \ge 2) \), and this is its bounded \( \rulename{\forall I} \). Everything below may use \( x > 0 \); so far nothing has.
- *Line 1* is an instance of the school fact that the square of every real number is at least \( 0 \), at the term \( x - 1 \) (a \( \rulename{\forall E} \)). It uses no earlier line, and in particular not \( x > 0 \): it holds for every real \( x \).
- *Line 2* follows from line 1 because \( (x - 1)^2 \) and \( x^2 - 2x + 1 \) are the same number, by expanding the square; one is replaced by the other (\( \rulename{{=}E} \)).
- *Line 3* follows from line 2 by dividing both sides by \( x \). Two things need \( x > 0 \) here. Dividing by \( x \) needs \( x \ne 0 \), and dividing both sides of an inequality by a number is guaranteed to keep its direction only when that number is positive. Both come from the assumption \( x > 0 \), and this is the **only** place in the proof where the assumption is used. The left side becomes \( (x^2 - 2x + 1)/x = x - 2 + 1/x \), and the right side \( 0/x = 0 \).
- *Line 4* follows from line 3 by adding \( 2 \) to both sides, which keeps any inequality. It is the claim for this \( x \); since \( x \) was arbitrary, the claim holds for every \( x > 0 \) (the closing \( \rulename{\forall I} \), silent in the proof as written).

**Explained badly.**

- *Line 1:* we start with a square, which is positive.
- *Line 2:* multiply it out.
- *Line 3:* now we divide by \( x \) and it still works.
- *Line 4:* rearranging gives the answer.
:::

Both explanations follow the order of the proof, and the second is not even wrong everywhere; it is shorter, and every sentence after the first describes what happened (the first we return to below). But compare what each one did with line 3. The first says *why* the inequality survives the division, and in saying it, finds the one place where the hypothesis \( x > 0 \) earns its keep. The second says "it still works", which is a description of the outcome, not a reason.

The difference shows as soon as the proof is wrong. Change the claim to "for every real \( x \ne 0 \), \( x + 1/x \ge 2 \)", and keep all four lines. The bad explanation reads the new proof exactly as happily as the old one: we start with a square, multiply out, divide by \( x \) and it still works, rearrange. The good explanation stops at line 3. It needs "the inequality keeps its direction because \( x > 0 \)", and the hypothesis now says only \( x \ne 0 \); for negative \( x \), division by \( x \) reverses the inequality, and line 3 does not follow. The claim is in fact false: at \( x = -1 \), \( x + 1/x = -2 < 2 \). A reader who explains warrants finds the gap; a reader who paraphrases cannot, because a paraphrase of a wrong step reads exactly like a paraphrase of a right one.

The bad explanation also slipped in its first line. A square is not always positive, only at least \( 0 \): \( (x - 1)^2 = 0 \) at \( x = 1 \), where the claim holds with equality. Restating invites such slips, because nothing is being checked. Explaining a warrant forces the exact fact, "every square is at least \( 0 \)", because the explanation has to cite it.

So the first kind of reading does three things the second does not. It **checks** each step, since a warrant can fail to exist. It **locates the hypotheses**, since every use of a hypothesis is a warrant. And it **prepares the reader to reuse the proof**, since the warrants, not the restatements, are what transfer to the next problem.

## How to explain a line

For each line, ask four questions, in this order.

1. **What kind of line is it?** An assumption that opens a box ("let", "suppose", "choose … such that"), a line derived from earlier ones, or the closing of a box ("hence", "so", "since \( x \) was arbitrary").
2. **Where does it come from?** Name the earlier lines, the definitions and the results it uses. "Line 2", "the definition of even", "@thm-square-even-implies-even", "the hypothesis \( x > 0 \)". A result is named, not paraphrased.
3. **By which step?** A rule of Chapters 1–4, or a piece of arithmetic that you can say in one clause ("divide both sides by \( x \)", "expand the square").
4. **Is it legitimate here?** Is every cited line still available, inside the boxes that are open (@def-derivation)? Is a chosen name fresh? Does a division have a non-zero divisor, and does an inequality keep its direction?

You do not need to write out a derivation; a phrase per line is enough, at the level of the "explained well" column above. When you cannot answer one of the four questions, you have found what to look at: either a step you do not yet understand, or a gap in the proof. Section 5.3 says what to do next: expand that stretch to level 1.

::: {.warning}
**Self-explanation is not re-reading, and not summarizing.** Reading a proof twice more makes it familiar, not checked: familiarity is what makes the bad explanation of @exm-self-explanation feel adequate. A summary ("the proof expands a square and divides by \( x \)") is useful afterwards, but it skips exactly the warrants that matter, such as why the division by \( x \) is allowed and keeps the inequality's direction. Self-explanation is local and backward-looking: each line, against what came before it.
:::

::: {.check}
Here is a six-line proof that for real numbers \( x \) and \( y \), if \( x + y > 2 \), then \( x > 1 \) or \( y > 1 \).

1. We prove the contrapositive: if it is not the case that \( x > 1 \) or \( y > 1 \), then \( x + y > 2 \) fails.
2. Suppose it is not the case that \( x > 1 \) or \( y > 1 \).
3. Then \( x \le 1 \) and \( y \le 1 \).
4. Adding these, \( x + y \le 2 \).
5. So \( x + y > 2 \) fails.
6. This proves the contrapositive, and hence the claim.

Self-explain lines 2–4.
:::

::: {.solution}
*Line 2* is an assumption: it opens the \( \rulename{{\to}I} \) box for the contrapositive announced in line 1, whose hypothesis is \( \neg(x > 1 \vee y > 1) \).

*Line 3* comes from line 2 in two steps. First @prp-de-morgan (a), \( \neg(P \vee Q) \vdash \neg P \wedge \neg Q \), gives "not \( x > 1 \), and not \( y > 1 \)". Then the order fact that \( \neg(u > 1) \) means \( u \le 1 \), for every real \( u \), turns each conjunct into the form written.

*Line 4* uses both conjuncts of line 3 (\( \rulename{\wedge E} \), twice) and the order fact that inequalities may be added: \( x \le 1 \) and \( y \le 1 \) give \( x + y \le 1 + y \le 1 + 1 = 2 \).

(For the record: line 5 is the order fact \( x + y \le 2 \) means \( \neg(x + y > 2) \); line 6 closes the box by \( \rulename{{\to}I} \) and then passes from the contrapositive to the claim by @prp-contrapositive-converse, a classical step.)
:::

## Strategies of good readers

Self-explanation is the habit for single lines. Readers who are good at proofs also do a few things with a proof as a whole. Here are five, shown on one short proof.

**Claim.** For real numbers \( x > 0 \) and \( y > 0 \), \( \sqrt{xy} \le (x + y)/2 \).

**Proof.** Let \( x > 0 \) and \( y > 0 \). Since \( x = (\sqrt x)^2 \), \( y = (\sqrt y)^2 \) and \( \sqrt{xy} = \sqrt x \, \sqrt y \),
\[
x + y - 2\sqrt{xy} = (\sqrt x - \sqrt y)^2 \ge 0 .
\]
Hence \( 2\sqrt{xy} \le x + y \), and dividing by \( 2 \) gives the claim.

1. **Try it first.** Before reading the proof, spend a few minutes on the claim yourself. A natural attempt squares both sides: \( xy \le (x + y)^2/4 \) is \( 4xy \le x^2 + 2xy + y^2 \), that is, \( 0 \le (x - y)^2 \), which is true. Already you know what the difficulty is (the square root) and what your attempt rests on (that a square is at least \( 0 \)).
2. **Identify the framework.** Find the skeleton, level 1 of @def-levels-of-proof. Here: a bounded \( \rulename{\forall I} \) on \( x \) and \( y \) (opened by "Let", closed silently) with the bounds \( x > 0 \), \( y > 0 \), then a direct chain. There is no case split, no contradiction, and no chosen witness. Knowing that tells you where to look: every line is a computation, so every warrant is an algebraic fact.
3. **Break it into sub-proofs.** The proof has one claim inside it, the displayed identity, and then a short finish. A claim inside a proof is a cut (the cut row of Section 5.2's dictionary): it is proved once and then used. Here the claim is proved inside the box on \( x \) and \( y \), so it is simply a line that later lines of the box may cite (@def-derivation); @lem-weakening-cut (b) is the same move for sequents proved outside every box. Read the claim on its own: it needs \( \sqrt{xy} = \sqrt x \sqrt y \) (true for \( x, y \ge 0 \)) and \( (\sqrt x)^2 = x \).
4. **Illustrate a hard line with an example.** If the identity is not clear, try numbers. With \( x = 1 \) and \( y = 4 \): the left side is \( 1 + 4 - 2 \cdot 2 = 1 \), the right side \( (1 - 2)^2 = 1 \). An example checks nothing in general, but it shows what the line claims.
5. **Compare with your own attempt.** Your squaring route proves the claim too, and it hides a warrant the given proof avoids: passing back from \( xy \le (x + y)^2/4 \) to \( \sqrt{xy} \le (x + y)/2 \) uses the converse of "squaring preserves order": from \( a^2 \le b^2 \) conclude \( a \le b \). This holds when \( b \ge 0 \), because then \( \abs{a} \le b \); here \( b = (x + y)/2 > 0 \). Without that hypothesis it fails: \( a = 1 \), \( b = -2 \). Comparing the two routes shows why the given proof introduces \( \sqrt x \) and \( \sqrt y \): it never has to undo a squaring. The comparison also links this claim to @exm-self-explanation: put \( y = 1/x \), and \( \sqrt{xy} = 1 \), so the claim becomes \( x + 1/x \ge 2 \).

The five strategies work at the level of the whole proof and self-explanation at the level of the line, and they support each other. Trying first tells you which line will be the hard one; the framework tells you which boxes are open at each line, which is what the fourth question of self-explanation needs.

## Exercises

### A. Check your understanding

::: {#exr-reading-proofs-a1}
[A1]

Here is a proof that if \( a > 0 \), \( b > 0 \) and \( a^2 = b^2 \), then \( a = b \).

(1) \( a^2 - b^2 = 0 \). (2) \( (a - b)(a + b) = 0 \). (3) \( a + b > 0 \). (4) Hence \( a - b = 0 \), that is, \( a = b \).

Classify each explanation as one that **justifies** its line or one that **paraphrases** it.

::: {.enumerate options="label=(\alph*)"}
1. "Line 1 follows from the hypothesis \( a^2 = b^2 \) by subtracting \( b^2 \) from both sides."
2. "Line 2: then the factored form is zero as well."
3. "Line 2 is line 1 rewritten with the identity \( u^2 - v^2 = (u - v)(u + v) \), at \( u = a \) and \( v = b \)."
4. "Line 3: now we know that \( a + b \) is positive."
5. "Line 3 holds because \( a > 0 \) and \( b > 0 \) are hypotheses, and a sum of two positive numbers is positive."
6. "Line 4: so \( a - b \) is zero, which is what we wanted."
:::
:::

::: {.solution}
(a) Justifies: it names the source (the hypothesis) and the step (subtracting \( b^2 \)).

(b) Paraphrases: "is zero as well" restates line 2 without saying why the product equals the left side of line 1.

(c) Justifies: it names the identity and the instance.

(d) Paraphrases: it restates line 3 and gives no reason.

(e) Justifies: it names both hypotheses and the fact that combines them.

(f) Paraphrases: it gives no warrant. A justification would say: by line 2 a product is zero, so one of its factors is zero; line 3 says the factor \( a + b \) is not zero, being positive; so \( a - b = 0 \) (@prp-disjunctive-syllogism, applied to "\( a + b = 0 \) or \( a - b = 0 \)" and \( a + b \ne 0 \)).
:::

### B. Practice

::: {#exr-reading-proofs-b1}
[B1: Self-explain a counterexample]

Here, with its lines numbered, is the half of @exm-square-not-uniform that shows \( f(x) = x^2 \) is **not** uniformly continuous on \( \nR \).

(1) By the negation of uniform continuity, with the bounds \( x \in \nR \) and \( y \in \nR \) dropped because they always hold, we must show
\[
\exists \varepsilon > 0 \; \forall \delta > 0 \; \exists x \; \exists y \; \bigl( \abs{x - y} < \delta \wedge \abs{x^2 - y^2} \ge \varepsilon \bigr).
\]
(2) Take \( \varepsilon = 1 \). (3) Let \( \delta > 0 \) be arbitrary, and take \( x \coloneqq 1/\delta \) and \( y \coloneqq 1/\delta + \delta/2 \), which depend on \( \delta \). (4) Then \( \abs{x - y} = \delta/2 < \delta \), (5) and, since \( y > x > 0 \),
\[
\abs{x^2 - y^2} = (y - x)(y + x) = \frac{\delta}{2} \Bigl( \frac{2}{\delta} + \frac{\delta}{2} \Bigr) = 1 + \frac{\delta^2}{4} \ge 1 .
\]
(6) Since \( \delta \) was arbitrary, uniform continuity fails.

Self-explain each line, citing labels where a line uses an earlier result. Say at which lines \( \delta > 0 \) is used.
:::

::: {.solution}
*(1)* A cut: the goal "\( f \) is not uniformly continuous" is replaced by the displayed formula, and the proof then proves the formula. The formula is the positive form of the negation of uniform continuity, @exm-negating-definitions (c), read with \( A = \nR \); there the two are shown interderivable, by @prp-bounded-quantifier-negation, @prp-negated-implication and the order fact \( \neg(u < \varepsilon) \) iff \( u \ge \varepsilon \). The direction used here is from the displayed formula to the negation. The bounds can be dropped because a bounded quantifier \( \exists x \in \nR \) abbreviates \( \exists x\, (x \in \nR \wedge \dots) \) (@def-bounded-quantifier), and over the domain \( \nR \) the conjunct \( x \in \nR \) always holds.

*(2)* The witness for \( \exists \varepsilon > 0 \): a bounded \( \rulename{\exists I} \) at the term \( 1 \), with its bound \( 1 > 0 \). It is written first, but as a rule it is applied last: the instance it needs, the formula after \( \exists \varepsilon > 0 \) with \( 1 \) for \( \varepsilon \), is what lines (3)–(6) prove.

*(3)* "Let \( \delta > 0 \) be arbitrary" opens a bounded \( \rulename{\forall I} \) box flagged \( \delta_0 \) with the assumption \( \delta_0 > 0 \). As in Section 4.4, the prose uses the letter \( \delta \) both for the flag and for the bound variable; below, \( \delta \) in the arithmetic is the flag \( \delta_0 \). The terms \( 1/\delta \) and \( 1/\delta + \delta/2 \) are the witnesses for \( \exists x \) and \( \exists y \) (two \( \rulename{\exists I} \), applied at the end of the box). They may mention \( \delta \) because \( \delta \)'s box is open; the clause "which depend on \( \delta \)" records this. The term \( 1/\delta \) exists because \( \delta \ne 0 \), from \( \delta > 0 \).

*(4)* Arithmetic: \( y - x = \delta/2 \), which is positive since \( \delta > 0 \), so \( \abs{x - y} = \delta/2 \); and \( \delta/2 < \delta \) since \( \delta > 0 \). This is the first conjunct.

*(5)* Arithmetic. Since \( \delta > 0 \), \( x = 1/\delta > 0 \) and \( y = x + \delta/2 > x \). Then \( x^2 < y^2 \), so \( \abs{x^2 - y^2} = y^2 - x^2 = (y - x)(y + x) \), with \( y - x = \delta/2 \) and \( y + x = 2/\delta + \delta/2 \); multiplying out gives \( 1 + \delta^2/4 \), which is at least \( 1 \) because \( \delta^2/4 \ge 0 \). This is the second conjunct; with (4) it gives the conjunction (\( \rulename{\wedge I} \)), and the two \( \rulename{\exists I} \) of (3) then give \( \exists x\, \exists y\, (\dots) \).

*(6)* The closing line of the bounded \( \rulename{\forall I} \) box flagged \( \delta_0 \) (@prp-bounded-quantifier-rules). The side condition holds: the proof has no premises; the only assumption mentioning \( \delta_0 \) is \( \delta_0 > 0 \), the assumption of the box this line closes, and no outer box is open; and \( \delta_0 \) does not appear in the conclusion \( \forall \delta > 0\, \exists x\, \exists y\, (\dots) \), whose \( \delta \) is a bound variable different from the flag. With (2) this proves the displayed formula, and by the cut (1) uniform continuity fails.

\( \delta > 0 \) is used in (3) (so that \( 1/\delta \) exists), in (4) (twice) and in (5) (for \( y > x > 0 \)).
:::

::: {#exr-reading-proofs-b2}
[B2: The unjustified line]

Here is a proof that for real numbers \( x < y \), \( x^3 < y^3 \).

(1) Let \( x < y \). (2) Then \( y^3 - x^3 = (y - x)(y^2 + xy + x^2) \). (3) Since \( x < y \), \( y - x > 0 \). (4) Also \( y^2 + xy + x^2 > 0 \). (5) So \( y^3 - x^3 > 0 \), as a product of two positive numbers. (6) Hence \( x^3 < y^3 \).

Every line is true. Line 1 opens the box; of the rest, all but one are instances of a routine algebra or order fact, cited or not; one line is not an instance of any fact stated so far, and it needs an argument of its own. Self-explain the proof line by line to find it, and supply that argument as its warrant.
:::

::: {.solution}
Line 1 opens the box, with the assumption \( x < y \). Line 2 is the identity \( (y - x)(y^2 + xy + x^2) = y^3 - x^3 \), checked by multiplying out. Line 3 cites line 1 and the order fact \( u < v \) iff \( v - u > 0 \). Line 5 cites lines 2, 3 and 4 and the fact that a product of two positive numbers is positive. Line 6 is line 5 rearranged by the same order fact.

Line 4 is the one without a warrant: it cites nothing, and it is not an instance of any fact stated so far. It is not obvious either, since \( xy \) can be negative. A warrant: complete the square,
\[
y^2 + xy + x^2 = \Bigl( y + \frac{x}{2} \Bigr)^2 + \frac{3x^2}{4} \ge 0 ,
\]
with equality only if \( x = 0 \) and \( y + x/2 = 0 \), that is, only if \( x = y = 0 \). Line 1 rules that out, since \( x < y \) gives \( x \ne y \). So \( y^2 + xy + x^2 > 0 \). The repaired line 4 uses the hypothesis \( x < y \) a second time, which the proof as printed hides; a reader who explains only "the bracket is positive" has paraphrased line 4 and missed this.
:::

### C. Going deeper

::: {#exr-reading-proofs-c1}
[C1: A longer proof]

Self-explain the proof of @lem-atom-splitting in Section 3.6: for each of its five numbered steps, and for each claim in the paragraph that follows them, say what it uses and why that is legitimate. Then state the idea of the proof in two sentences.
:::

::: {.solution}
[Hint 1]

Keep @def-derivation open beside you: the paragraph after the five steps checks, in turn, the premises, the scope rule for the transplanted citations, the rule schemas, the last line of each box, and the availability of what the last line cites.
:::

::: {.solution}
[Hint 2]

Start with step 2. Which result supplies \( p \vee \neg p \), what is substituted for its letter, and why may that line cite nothing?
:::

::: {.solution}
*Step 1.* The premises of the new list are the members of \( \Delta \) that \( D \) or \( E \) uses. Clause (D1) of @def-derivation places premises first, above every box, and puts no restriction on which statements they are. The conclusion will be \( \Delta \vdash \psi \), so only members of \( \Delta \) are taken. The premises \( p \), \( \neg p \) of \( D \) and \( E \) are therefore left out, unless they also belong to \( \Delta \), which does no harm.

*Step 2.* The line \( p \vee \neg p \) is @prp-excluded-middle with the atom \( p \) for the letter \( P \), used as a derived rule (@def-derived-rule) with no premises, so it cites nothing. This is the one classical step, through \( \rulename{LEM} \).

*Step 3.* The box opened by \( p \) contains the non-premise lines of \( D \) with their own boxes; every citation of the premise \( p \) is redirected to the assumption, and every citation of a premise in \( \Delta \) to the premise line of step 1. The two degenerate cases (the last line of \( D \) is a premise) are handled separately so that the box still ends in \( \psi \), by repetition (\( \rulename{R} \), clause (D3)) where needed.

*Step 4.* The same, for \( E \) with the assumption \( \neg p \).

*Step 5.* The last line \( \psi \) is \( \rulename{\vee E} \) (@def-rules-disjunction), citing the disjunction of step 2 and the two boxes, each opened by one disjunct and ending in \( \psi \).

*The verification paragraph.* It checks that the list is a derivation. (i) Premises are first and in no box, so they are available everywhere. (ii) Inside each new box, a line of \( D \) cites the same lines and boxes as before, renumbered, or a premise line, or the assumption, and each of those is available by the scope rule of @def-derivation: the old boxes have simply been placed inside one new box, which contains both the citing line and the cited one. (iii) Each line is still an instance of its rule's schema, since its statement and the statements it cites are unchanged, as in the proof of @lem-weakening-cut. (iv) The last line of each new box is \( \psi \), as a line of that box itself, which \( \rulename{\vee E} \) requires. (v) The disjunction and the two boxes are available at the last line, which lies in no box. So the last line is a correct \( \rulename{\vee E} \), and \( \Delta \vdash \psi \).

*The idea in two sentences.* The lemma is proof by cases on \( p \vee \neg p \): excluded middle supplies the disjunction, and the two given derivations, with their premise \( p \) or \( \neg p \) turned into the assumption of a box, are the two cases of \( \rulename{\vee E} \). All the work is in checking that the transplanted lines still cite only available lines.

**Marking scheme.** (10 points)
- 2: step 2 explained: @prp-excluded-middle as a derived rule at the atom \( p \), citing nothing, and identified as the classical step.
- 2: steps 3 and 4 explained: the redirection of citations of \( p \) (or \( \neg p \)) to the assumption and of members of \( \Delta \) to the premise lines, and the degenerate cases.
- 1: step 5 named as \( \rulename{\vee E} \) with its three citations.
- 3: the verification paragraph explained against @def-derivation: availability by the scope rule, schemas unchanged, each box ending in \( \psi \) as its own line.
- 2: an idea in two sentences that names both the case split on \( p \vee \neg p \) and the transplanting of \( D \) and \( E \) into the two boxes.
Fatal errors (0 for the step): explanations that restate the steps without naming what they use; calling the case split \( \rulename{\neg I} \) or \( \rulename{RAA} \).
:::

<!-- dependency ledger
exm-self-explanation (example): u^2 >= 0 for every real u; (x - 1)^2 = x^2 - 2x + 1; dividing by x > 0 keeps the direction; dividing by x < 0 reverses it (so line 3 fails for negative x); 0/x = 0; (x^2 - 2x + 1)/x = x - 2 + 1/x; adding 2 keeps an inequality | school algebra and order facts (ch11 proves them from the axioms); checked by verify/ch05/exm-self-explanation.py
exm-self-explanation (claim): x = -1 gives x + 1/x = -2 < 2; equality at x = 1 | arithmetic; checked by verify/ch05/exm-self-explanation.py
exm-self-explanation (claim): "this is the only place the hypothesis is used" (line 3) | read off the four lines on the page
exm-self-explanation (claim): [the Quick check after it] de Morgan (a); not (u > 1) iff u <= 1; inequalities add; line 6 by prp-contrapositive-converse | prp-de-morgan, prp-contrapositive-converse (cited); order facts (school)
exm-self-explanation (claim): [the strategies passage after it] sqrt(xy) = sqrt(x) sqrt(y) and (sqrt x)^2 = x for x, y >= 0; x + y - 2 sqrt(xy) = (sqrt x - sqrt y)^2; (x + y)^2 = x^2 + 2xy + y^2; 4xy <= x^2 + 2xy + y^2 iff 0 <= (x - y)^2 (the try-it-first route); a^2 <= b^2 and b >= 0 imply a <= b (via |a| <= b), failing at a = 1, b = -2; the instance x = 1, y = 4 | school facts about square roots (NOTATION: a school fact before ch11, then thm-nth-root); checked by verify/ch05/exm-self-explanation.py
exm-self-explanation (claim): [the strategies passage after it] a claim inside a proof is a cut; inside a box it is a line later lines may cite | Section 5.2's dictionary (prose pointer); def-derivation, lem-weakening-cut (b) (cited)
exr-reading-proofs-a1 (solution): u^2 - v^2 = (u - v)(u + v); a product is zero only if a factor is; a sum of positives is positive | school algebra; prp-disjunctive-syllogism (cited); checked by verify/ch05/exr-reading-proofs-a1.py
exr-reading-proofs-b1 (solution): |x - y| = delta/2 < delta; (delta/2)(2/delta + delta/2) = 1 + delta^2/4 >= 1; |u| = u for u >= 0 (bars dropped, y - x > 0 and y^2 - x^2 > 0); 0 < x < y implies x^2 < y^2; delta^2/4 >= 0; delta > 0 gives delta != 0, 1/delta > 0, delta/2 < delta | school algebra and order facts (ch11 proves them from the axioms); checked by verify/ch05/exr-reading-proofs-b1.py
exr-reading-proofs-b1 (solution): the displayed formula yields the negation of uniform continuity | exm-negating-definitions (c), prp-bounded-quantifier-negation, prp-negated-implication, def-bounded-quantifier (cited)
exr-reading-proofs-b1 (solution): the flag delta_0 meets the side condition of the bounded forall-I; the prose uses one letter for flag and bound variable | prp-bounded-quantifier-rules (cited); Section 4.4 (prose pointer)
exr-reading-proofs-b2 (solution): y^3 - x^3 = (y - x)(y^2 + xy + x^2); y^2 + xy + x^2 = (y + x/2)^2 + 3x^2/4; zero only at x = y = 0 | school algebra; checked by verify/ch05/exr-reading-proofs-b2.py
exr-reading-proofs-c1 (solution): reading of the proof of lem-atom-splitting | lem-atom-splitting, def-derivation, prp-excluded-middle, def-derived-rule, def-rules-disjunction, lem-weakening-cut (cited)
-->
