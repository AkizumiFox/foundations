<!-- S2a evidence for ch01: every derivation the review relied on. Check with: python3 tools/check_fitch.py authoring/reviews/ch01-S2-derivations.md (expect 0 errors; three blocks are marked expect-invalid). Generated from a compact spec; D-numbers are cited in ch01-S2.md. -->

# Chapter 1 S2a: derivations checked

### D1 and-commutes

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {Q} \ae{1}
  \have {4} {Q \wedge P} \ai{3,2}
\end{nd}$
\end{center}
```

<!-- D1 and-commutes: 4 lines -->

### D2 implication-transitive

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
\end{nd}$
\end{center}
```

<!-- D2 implication-transitive: 6 lines -->

### D3a curry =>

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {Q \to R} \ii{3-5}
  \close
  \have {7} {P \to (Q \to R)} \ii{2-6}
\end{nd}$
\end{center}
```

<!-- D3a curry =>: 7 lines -->

### D3b curry <=

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {Q \to R} \ie{1,3}
  \have {6} {R} \ie{5,4}
  \close
  \have {7} {(P \wedge Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```

<!-- D3b curry <=: 7 lines -->

### D4 K

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P}
  \open
  \hypo {2} {Q}
  \have {3} {P} \r{1}
  \close
  \have {4} {Q \to P} \ii{2-3}
  \close
  \have {5} {P \to (Q \to P)} \ii{1-4}
\end{nd}$
\end{center}
```

<!-- D4 K: 5 lines -->

### D5 identity one-line box

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P}
  \close
  \have {2} {P \to P} \ii{1-1}
\end{nd}$
\end{center}
```

<!-- D5 identity one-line box: 2 lines -->

### D6 swap antecedents

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q \to R} \ie{1,3}
  \have {5} {R} \ie{4,2}
  \close
  \have {6} {P \to R} \ii{3-5}
  \close
  \have {7} {Q \to (P \to R)} \ii{2-6}
\end{nd}$
\end{center}
```

<!-- D6 swap antecedents: 7 lines -->

### D7 one box

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {P \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,3}
  \have {6} {Q \wedge R} \ai{4,5}
  \close
  \have {7} {P \to (Q \wedge R)} \ii{3-6}
\end{nd}$
\end{center}
```

<!-- D7 one box: 7 lines -->

### D8 s02 C2

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to (P \to R)}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {P \to R} \ie{1,6}
  \have {8} {R} \ie{7,2}
  \close
  \have {9} {Q \to R} \ii{3-8}
  \close
  \have {10} {P \to (Q \to R)} \ii{2-9}
\end{nd}$
\end{center}
```

<!-- D8 s02 C2: 10 lines -->

### D9a distributivity =>

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \vee R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \vee R} \ae{1}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{2,4}
  \have {6} {(P \wedge Q) \vee (P \wedge R)} \oi{5}
  \close
  \open
  \hypo {7} {R}
  \have {8} {P \wedge R} \ai{2,7}
  \have {9} {(P \wedge Q) \vee (P \wedge R)} \oi{8}
  \close
  \have {10} {(P \wedge Q) \vee (P \wedge R)} \oe{3,4-6,7-9}
\end{nd}$
\end{center}
```

<!-- D9a distributivity =>: 10 lines -->

### D9b distributivity <=

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \vee (P \wedge R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {Q \vee R} \oi{4}
  \have {6} {P \wedge (Q \vee R)} \ai{3,5}
  \close
  \open
  \hypo {7} {P \wedge R}
  \have {8} {P} \ae{7}
  \have {9} {R} \ae{7}
  \have {10} {Q \vee R} \oi{9}
  \have {11} {P \wedge (Q \vee R)} \ai{8,10}
  \close
  \have {12} {P \wedge (Q \vee R)} \oe{1,2-6,7-11}
\end{nd}$
\end{center}
```

<!-- D9b distributivity <=: 12 lines -->

### D10 or commutes

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P}
  \have {3} {Q \vee P} \oi{2}
  \close
  \open
  \hypo {4} {Q}
  \have {5} {Q \vee P} \oi{4}
  \close
  \have {6} {Q \vee P} \oe{1,2-3,4-5}
\end{nd}$
\end{center}
```

<!-- D10 or commutes: 6 lines -->

### D11 or assoc

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \vee R)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {(P \vee Q) \vee R} \oi{3}
  \close
  \open
  \hypo {5} {Q \vee R}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {(P \vee Q) \vee R} \oi{7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {(P \vee Q) \vee R} \oi{9}
  \close
  \have {11} {(P \vee Q) \vee R} \oe{5,6-8,9-10}
  \close
  \have {12} {(P \vee Q) \vee R} \oe{1,2-4,5-11}
\end{nd}$
\end{center}
```

<!-- D11 or assoc: 12 lines -->

### D12a cases on hypothesis

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to R) \wedge (Q \to R)}
  \open
  \hypo {2} {P \vee Q}
  \open
  \hypo {3} {P}
  \have {4} {P \to R} \ae{1}
  \have {5} {R} \ie{4,3}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {Q \to R} \ae{1}
  \have {8} {R} \ie{7,6}
  \close
  \have {9} {R} \oe{2,3-5,6-8}
  \close
  \have {10} {(P \vee Q) \to R} \ii{2-9}
\end{nd}$
\end{center}
```

<!-- D12a cases on hypothesis: 10 lines -->

### D12b converse

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {R} \ie{1,3}
  \close
  \have {5} {P \to R} \ii{2-4}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {R} \ie{1,7}
  \close
  \have {9} {Q \to R} \ii{6-8}
  \have {10} {(P \to R) \wedge (Q \to R)} \ai{5,9}
\end{nd}$
\end{center}
```

<!-- D12b converse: 10 lines -->

### D13 s03 B3

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to S}
  \open
  \hypo {4} {P}
  \have {5} {R} \ie{2,4}
  \have {6} {R \vee S} \oi{5}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {S} \ie{3,7}
  \have {9} {R \vee S} \oi{8}
  \close
  \have {10} {R \vee S} \oe{1,4-6,7-9}
\end{nd}$
\end{center}
```

<!-- D13 s03 B3: 10 lines -->

### D14 contrapositive no RAA

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
  \close
  \have {7} {\neg Q \to \neg P} \ii{2-6}
\end{nd}$
\end{center}
```

<!-- D14 contrapositive no RAA: 7 lines -->

### D15 MT direct

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
\end{nd}$
\end{center}
```

<!-- D15 MT direct: 6 lines -->

### D15b MT via CP (derived rule)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \have {3} {\neg Q \to \neg P} \by{CP}{1}
  \have {4} {\neg P} \ie{3,2}
\end{nd}$
\end{center}
```

<!-- D15b MT via CP (derived rule): 4 lines -->

### D16 nni

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \close
  \have {4} {\neg\neg P} \ni{2-3}
\end{nd}$
\end{center}
```

<!-- D16 nni: 4 lines -->

### D17a DS

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \open
  \hypo {6} {Q}
  \close
  \have {7} {Q} \oe{1,3-5,6-6}
\end{nd}$
\end{center}
```

<!-- D17a DS: 7 lines -->

### D17b DS other

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \close
  \open
  \hypo {4} {Q}
  \have {5} {\bot} \ne{4,2}
  \have {6} {P} \be{5}
  \close
  \have {7} {P} \oe{1,3-3,4-6}
\end{nd}$
\end{center}
```

<!-- D17b DS other: 7 lines -->

### D18 not-or gives not-left

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
\end{nd}$
\end{center}
```

<!-- D18 not-or gives not-left: 5 lines -->

### D19 H&R p22 (to be replaced)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg P}
  \open
  \hypo {2} {P}
  \have {3} {\neg P} \ie{1,2}
  \have {4} {\bot} \ne{2,3}
  \close
  \have {5} {\neg P} \ni{2-4}
\end{nd}$
\end{center}
```

<!-- D19 H&R p22 (to be replaced): 5 lines -->

### D19' replacement (P or Q) -> not P

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to \neg P}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\neg P} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {\neg P} \ni{2-5}
\end{nd}$
\end{center}
```

<!-- D19' replacement (P or Q) -> not P: 6 lines -->

### D20 vacuous implication

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P}
  \have {3} {\bot} \ne{2,1}
  \have {4} {Q} \be{3}
  \close
  \have {5} {P \to Q} \ii{2-4}
\end{nd}$
\end{center}
```

<!-- D20 vacuous implication: 5 lines -->

### D21' s04 B4 replacement

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to \neg P}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg P} \ie{2,4}
  \have {6} {\bot} \ne{3,5}
  \close
  \have {7} {\neg P} \ni{3-6}
\end{nd}$
\end{center}
```

<!-- D21' s04 B4 replacement: 7 lines -->

### D22 iff negations, no RAA

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {Q}
  \have {4} {P} \bie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg Q} \ni{3-5}
  \close
  \open
  \hypo {7} {\neg Q}
  \open
  \hypo {8} {P}
  \have {9} {Q} \bie{1,8}
  \have {10} {\bot} \ne{9,7}
  \close
  \have {11} {\neg P} \ni{8-10}
  \close
  \have {12} {\neg P \leftrightarrow \neg Q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

<!-- D22 iff negations, no RAA: 12 lines -->

### D23 converse, RAA

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \leftrightarrow \neg Q}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {\neg P} \bie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \open
  \hypo {7} {Q}
  \open
  \hypo {8} {\neg P}
  \have {9} {\neg Q} \bie{1,8}
  \have {10} {\bot} \ne{7,9}
  \close
  \have {11} {P} \raa{8-10}
  \close
  \have {12} {P \leftrightarrow Q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

<!-- D23 converse, RAA: 12 lines -->

### D24 iff transitive

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \hypo {2} {Q \leftrightarrow R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \bie{1,3}
  \have {5} {R} \bie{2,4}
  \close
  \open
  \hypo {6} {R}
  \have {7} {Q} \bie{2,6}
  \have {8} {P} \bie{1,7}
  \close
  \have {9} {P \leftrightarrow R} \bi{3-5,6-8}
\end{nd}$
\end{center}
```

<!-- D24 iff transitive: 9 lines -->

### D25 nne

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg P}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{2,1}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

<!-- D25 nne: 4 lines -->

### D26 contrapositive converse

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg Q \to \neg P}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {\neg P} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {Q} \raa{3-5}
  \close
  \have {7} {P \to Q} \ii{2-6}
\end{nd}$
\end{center}
```

<!-- D26 contrapositive converse: 7 lines -->

### D27 LEM

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {\neg (P \vee \neg P)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee \neg P} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
  \have {6} {P \vee \neg P} \oi{5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {P \vee \neg P} \raa{1-7}
\end{nd}$
\end{center}
```

<!-- D27 LEM: 8 lines -->

### D28a DM not-or => and-nots

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg P} \ni{2-4}
  \open
  \hypo {6} {Q}
  \have {7} {P \vee Q} \oi{6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {\neg Q} \ni{6-8}
  \have {10} {\neg P \wedge \neg Q} \ai{5,9}
\end{nd}$
\end{center}
```

<!-- D28a DM not-or => and-nots: 10 lines -->

### D28b DM and-nots => not-or

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \wedge \neg Q}
  \open
  \hypo {2} {P \vee Q}
  \open
  \hypo {3} {P}
  \have {4} {\neg P} \ae{1}
  \have {5} {\bot} \ne{3,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {\neg Q} \ae{1}
  \have {8} {\bot} \ne{6,7}
  \close
  \have {9} {\bot} \oe{2,3-5,6-8}
  \close
  \have {10} {\neg (P \vee Q)} \ni{2-9}
\end{nd}$
\end{center}
```

<!-- D28b DM and-nots => not-or: 10 lines -->

### D28c DM or-nots => not-and

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \vee \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \open
  \hypo {3} {\neg P}
  \have {4} {P} \ae{2}
  \have {5} {\bot} \ne{4,3}
  \close
  \open
  \hypo {6} {\neg Q}
  \have {7} {Q} \ae{2}
  \have {8} {\bot} \ne{7,6}
  \close
  \have {9} {\bot} \oe{1,3-5,6-8}
  \close
  \have {10} {\neg (P \wedge Q)} \ni{2-9}
\end{nd}$
\end{center}
```

<!-- D28c DM or-nots => not-and: 10 lines -->

### D28d DM not-and => or-nots (RAA)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \open
  \hypo {2} {\neg (\neg P \vee \neg Q)}
  \open
  \hypo {3} {\neg P}
  \have {4} {\neg P \vee \neg Q} \oi{3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {P} \raa{3-5}
  \open
  \hypo {7} {\neg Q}
  \have {8} {\neg P \vee \neg Q} \oi{7}
  \have {9} {\bot} \ne{8,2}
  \close
  \have {10} {Q} \raa{7-9}
  \have {11} {P \wedge Q} \ai{6,10}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {\neg P \vee \neg Q} \raa{2-12}
\end{nd}$
\end{center}
```

<!-- D28d DM not-and => or-nots (RAA): 13 lines -->

### D28d' via LEM on P

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{3,4}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg Q} \ni{4-6}
  \have {8} {\neg P \vee \neg Q} \oi{7}
  \close
  \open
  \hypo {9} {\neg P}
  \have {10} {\neg P \vee \neg Q} \oi{9}
  \close
  \have {11} {\neg P \vee \neg Q} \oe{2,3-8,9-10}
\end{nd}$
\end{center}
```

<!-- D28d' via LEM on P: 11 lines -->

### D29a impl as disj, no RAA

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \vee Q}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \close
  \open
  \hypo {7} {Q}
  \open
  \hypo {8} {P}
  \have {9} {Q} \r{7}
  \close
  \have {10} {P \to Q} \ii{8-9}
  \close
  \have {11} {P \to Q} \oe{1,2-6,7-10}
\end{nd}$
\end{center}
```

<!-- D29a impl as disj, no RAA: 11 lines -->

### D29b with LEM

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg P \vee Q} \oi{4}
  \close
  \open
  \hypo {6} {\neg P}
  \have {7} {\neg P \vee Q} \oi{6}
  \close
  \have {8} {\neg P \vee Q} \oe{2,3-5,6-7}
\end{nd}$
\end{center}
```

<!-- D29b with LEM: 8 lines -->

### D30ii nne derives RAA (instance: box from premise)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to \bot}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \ie{1,2}
  \close
  \have {4} {\neg\neg P} \ni{2-3}
  \have {5} {P} \by{$\neg\neg$E}{4}
\end{nd}$
\end{center}
```

<!-- D30ii nne derives RAA (instance: box from premise): 5 lines -->

### D30iii LEM derives nne

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg P}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \close
  \open
  \hypo {4} {\neg P}
  \have {5} {\bot} \ne{4,1}
  \have {6} {P} \be{5}
  \close
  \have {7} {P} \oe{2,3-3,4-6}
\end{nd}$
\end{center}
```

<!-- D30iii LEM derives nne: 7 lines -->

### D30i' LEM derives RAA directly (s06 C1)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to \bot}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \close
  \open
  \hypo {4} {\neg P}
  \have {5} {\bot} \ie{1,4}
  \have {6} {P} \be{5}
  \close
  \have {7} {P} \oe{2,3-3,4-6}
\end{nd}$
\end{center}
```

<!-- D30i' LEM derives RAA directly (s06 C1): 7 lines -->

### D31a triple negation

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg\neg P}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {\neg P}
  \have {4} {\bot} \ne{2,3}
  \close
  \have {5} {\neg\neg P} \ni{3-4}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg P} \ni{2-6}
\end{nd}$
\end{center}
```

<!-- D31a triple negation: 7 lines -->

### D31b not P -> P gives P (H&R 3a)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to P}
  \open
  \hypo {2} {\neg P}
  \have {3} {P} \ie{1,2}
  \have {4} {\bot} \ne{3,2}
  \close
  \have {5} {P} \raa{2-4}
\end{nd}$
\end{center}
```

<!-- D31b not P -> P gives P (H&R 3a): 5 lines -->

### D31b' replacement

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to Q}
  \hypo {2} {\neg P \to \neg Q}
  \open
  \hypo {3} {\neg P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg Q} \ie{2,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {P} \raa{3-6}
\end{nd}$
\end{center}
```

<!-- D31b' replacement: 7 lines -->

### D32 botE from RAA and R

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\bot}
  \open
  \hypo {2} {\neg P}
  \have {3} {\bot} \r{1}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

<!-- D32 botE from RAA and R: 4 lines -->

### D33 (P->Q)v(Q->P) by LEM on Q

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {Q \vee \neg Q} \by{LEM}{}
  \open
  \hypo {2} {Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \r{2}
  \close
  \have {5} {P \to Q} \ii{3-4}
  \have {6} {(P \to Q) \vee (Q \to P)} \oi{5}
  \close
  \open
  \hypo {7} {\neg Q}
  \open
  \hypo {8} {Q}
  \have {9} {\bot} \ne{8,7}
  \have {10} {P} \be{9}
  \close
  \have {11} {Q \to P} \ii{8-10}
  \have {12} {(P \to Q) \vee (Q \to P)} \oi{11}
  \close
  \have {13} {(P \to Q) \vee (Q \to P)} \oe{1,2-6,7-12}
\end{nd}$
\end{center}
```

<!-- D33 (P->Q)v(Q->P) by LEM on Q: 13 lines -->

### D33alt LEM on P also works

```{=latex}
\begin{center}
$\begin{nd}
  \have {1} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P} \r{2}
  \close
  \have {5} {Q \to P} \ii{3-4}
  \have {6} {(P \to Q) \vee (Q \to P)} \oi{5}
  \close
  \open
  \hypo {7} {\neg P}
  \open
  \hypo {8} {P}
  \have {9} {\bot} \ne{8,7}
  \have {10} {Q} \be{9}
  \close
  \have {11} {P \to Q} \ii{8-10}
  \have {12} {(P \to Q) \vee (Q \to P)} \oi{11}
  \close
  \have {13} {(P \to Q) \vee (Q \to P)} \oe{1,2-6,7-12}
\end{nd}$
\end{center}
```

<!-- D33alt LEM on P also works: 13 lines -->

### X D33flaw2 genuine sibling error

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \have {1} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P} \r{2}
  \close
  \have {5} {Q \to P} \ii{3-4}
  \have {6} {(P \to Q) \vee (Q \to P)} \oi{5}
  \close
  \open
  \hypo {7} {\neg P}
  \open
  \hypo {8} {Q}
  \have {9} {P} \r{2}
  \close
  \have {10} {Q \to P} \ii{8-9}
  \have {11} {(P \to Q) \vee (Q \to P)} \oi{10}
  \close
  \have {12} {(P \to Q) \vee (Q \to P)} \oe{1,2-6,7-11}
\end{nd}$
\end{center}
```

<!-- X D33flaw2 genuine sibling error: 12 lines -->

### D34' new exm-search-distribute

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {\neg Q} \ie{1,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg (P \wedge Q)} \ni{2-6}
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {\neg Q} \ie{1,9}
  \have {11} {\bot} \ne{8,10}
  \close
  \have {12} {\neg P} \ni{9-11}
  \close
  \have {13} {Q \to \neg P} \ii{8-12}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
\end{nd}$
\end{center}
```

<!-- D34' new exm-search-distribute: 14 lines -->

### D34 old (H&R 1r) premise-directed steps needed

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \wedge R)}
  \open
  \hypo {2} {P}
  \have {3} {Q \wedge R} \ie{1,2}
  \have {4} {Q} \ae{3}
  \close
  \have {5} {P \to Q} \ii{2-4}
  \open
  \hypo {6} {P}
  \have {7} {Q \wedge R} \ie{1,6}
  \have {8} {R} \ae{7}
  \close
  \have {9} {P \to R} \ii{6-8}
  \have {10} {(P \to Q) \wedge (P \to R)} \ai{5,9}
\end{nd}$
\end{center}
```

<!-- D34 old (H&R 1r) premise-directed steps needed: 10 lines -->

### D35 exm-search-cases (three premises)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {Q \to R}
  \open
  \hypo {4} {P}
  \have {5} {R} \ie{2,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {R} \ie{3,6}
  \close
  \have {8} {R} \oe{1,4-5,6-7}
\end{nd}$
\end{center}
```

<!-- D35 exm-search-cases (three premises): 8 lines -->

### D36 postpone-or, LEM on Q with DS

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \have {2} {Q \vee \neg Q} \by{LEM}{}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {(P \to Q) \vee (P \to R)} \oi{6}
  \close
  \open
  \hypo {8} {\neg Q}
  \open
  \hypo {9} {P}
  \have {10} {Q \vee R} \ie{1,9}
  \have {11} {R} \by{DS}{10,8}
  \close
  \have {12} {P \to R} \ii{9-11}
  \have {13} {(P \to Q) \vee (P \to R)} \oi{12}
  \close
  \have {14} {(P \to Q) \vee (P \to R)} \oe{2,3-7,8-13}
\end{nd}$
\end{center}
```

<!-- D36 postpone-or, LEM on Q with DS: 14 lines -->

### D36b postpone-or, LEM on P (blueprint's route)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \have {4} {Q \vee R} \ie{1,3}
  \open
  \hypo {5} {Q}
  \open
  \hypo {6} {P}
  \have {7} {Q} \r{5}
  \close
  \have {8} {P \to Q} \ii{6-7}
  \have {9} {(P \to Q) \vee (P \to R)} \oi{8}
  \close
  \open
  \hypo {10} {R}
  \open
  \hypo {11} {P}
  \have {12} {R} \r{10}
  \close
  \have {13} {P \to R} \ii{11-12}
  \have {14} {(P \to Q) \vee (P \to R)} \oi{13}
  \close
  \have {15} {(P \to Q) \vee (P \to R)} \oe{4,5-9,10-14}
  \close
  \open
  \hypo {16} {\neg P}
  \open
  \hypo {17} {P}
  \have {18} {\bot} \ne{17,16}
  \have {19} {Q} \be{18}
  \close
  \have {20} {P \to Q} \ii{17-19}
  \have {21} {(P \to Q) \vee (P \to R)} \oi{20}
  \close
  \have {22} {(P \to Q) \vee (P \to R)} \oe{2,3-15,16-21}
\end{nd}$
\end{center}
```

<!-- D36b postpone-or, LEM on P (blueprint's route): 22 lines -->

### D37 Peirce

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {(P \to Q) \to P}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \have {7} {P} \ie{1,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {P} \raa{2-8}
  \close
  \have {10} {((P \to Q) \to P) \to P} \ii{1-9}
\end{nd}$
\end{center}
```

<!-- D37 Peirce: 10 lines -->

### D38a

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \to R)}
  \open
  \hypo {2} {Q}
  \have {3} {P} \ae{1}
  \have {4} {Q \to R} \ae{1}
  \have {5} {R} \ie{4,2}
  \have {6} {P \wedge R} \ai{3,5}
  \close
  \have {7} {Q \to (P \wedge R)} \ii{2-6}
\end{nd}$
\end{center}
```

<!-- D38a: 7 lines -->

### D38b not(P->Q) |- P and not Q

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \to Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {P} \raa{2-7}
  \open
  \hypo {9} {Q}
  \open
  \hypo {10} {P}
  \have {11} {Q} \r{9}
  \close
  \have {12} {P \to Q} \ii{10-11}
  \have {13} {\bot} \ne{12,1}
  \close
  \have {14} {\neg Q} \ni{9-13}
  \have {15} {P \wedge \neg Q} \ai{8,14}
\end{nd}$
\end{center}
```

<!-- D38b not(P->Q) |- P and not Q: 15 lines -->

### D38c old (H&R 5a) RAA route

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to Q}
  \open
  \hypo {2} {Q \to P}
  \open
  \hypo {3} {\neg P}
  \open
  \hypo {4} {P}
  \have {5} {\bot} \ne{4,3}
  \have {6} {Q} \be{5}
  \close
  \have {7} {P \to Q} \ii{4-6}
  \have {8} {Q} \ie{1,7}
  \have {9} {P} \ie{2,8}
  \have {10} {\bot} \ne{9,3}
  \close
  \have {11} {P} \raa{3-10}
  \close
  \have {12} {(Q \to P) \to P} \ii{2-11}
\end{nd}$
\end{center}
```

<!-- D38c old (H&R 5a) RAA route: 12 lines -->

### D38c' new: not P -> Q |- P or Q

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to Q}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {Q} \ie{1,5}
  \have {7} {P \vee Q} \oi{6}
  \close
  \have {8} {P \vee Q} \oe{2,3-4,5-7}
\end{nd}$
\end{center}
```

<!-- D38c' new: not P -> Q |- P or Q: 8 lines -->

### D39' B2 new

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {R \to \neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \open
  \hypo {5} {R}
  \have {6} {\neg Q} \ie{2,5}
  \have {7} {\bot} \ne{4,6}
  \close
  \have {8} {\neg R} \ni{5-7}
  \close
  \have {9} {P \to \neg R} \ii{3-8}
\end{nd}$
\end{center}
```

<!-- D39' B2 new: 9 lines -->

### D40' C1 new

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \wedge R)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {P \vee R} \oi{2}
  \have {5} {(P \vee Q) \wedge (P \vee R)} \ai{3,4}
  \close
  \open
  \hypo {6} {Q \wedge R}
  \have {7} {Q} \ae{6}
  \have {8} {R} \ae{6}
  \have {9} {P \vee Q} \oi{7}
  \have {10} {P \vee R} \oi{8}
  \have {11} {(P \vee Q) \wedge (P \vee R)} \ai{9,10}
  \close
  \have {12} {(P \vee Q) \wedge (P \vee R)} \oe{1,2-5,6-11}
\end{nd}$
\end{center}
```

<!-- D40' C1 new: 12 lines -->

### D41' C2 new

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to Q}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \open
  \hypo {6} {P}
  \have {7} {\bot} \ne{6,5}
  \have {8} {Q} \be{7}
  \close
  \have {9} {P \to Q} \ii{6-8}
  \have {10} {Q} \ie{1,9}
  \have {11} {P \vee Q} \oi{10}
  \close
  \have {12} {P \vee Q} \oe{2,3-4,5-11}
\end{nd}$
\end{center}
```

<!-- D41' C2 new: 12 lines -->

### D42a

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to R)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {Q \to R} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{2,4}
  \have {6} {R} \ie{3,5}
  \close
  \have {7} {P \to R} \ii{4-6}
\end{nd}$
\end{center}
```

<!-- D42a: 7 lines -->

### D42b

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge Q)}
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg Q} \ni{3-5}
\end{nd}$
\end{center}
```

<!-- D42b: 6 lines -->

### D42c' new

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \wedge \neg Q)}
  \hypo {2} {P}
  \open
  \hypo {3} {\neg Q}
  \have {4} {P \wedge \neg Q} \ai{2,3}
  \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {Q} \raa{3-5}
\end{nd}$
\end{center}
```

<!-- D42c' new: 6 lines -->

### D42c old (H&R Ex 1.8)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {\neg P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {P} \raa{3-5}
\end{nd}$
\end{center}
```

<!-- D42c old (H&R Ex 1.8): 6 lines -->

### D43 C4

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
  \hypo {2} {P \to Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{2,3}
  \have {5} {Q \to R} \ie{1,3}
  \have {6} {R} \ie{5,4}
  \close
  \have {7} {P \to R} \ii{3-6}
  \close
  \have {8} {(P \to Q) \to (P \to R)} \ii{2-7}
\end{nd}$
\end{center}
```

<!-- D43 C4: 8 lines -->

### D44 R3

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \to R}
  \open
  \hypo {2} {P}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {R} \ie{1,6}
  \close
  \have {8} {Q \to R} \ii{3-7}
  \close
  \have {9} {P \to (Q \to R)} \ii{2-8}
\end{nd}$
\end{center}
```

<!-- D44 R3: 9 lines -->

### D46a iff to two implications

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \bie{1,2}
  \close
  \have {4} {P \to Q} \ii{2-3}
  \open
  \hypo {5} {Q}
  \have {6} {P} \bie{1,5}
  \close
  \have {7} {Q \to P} \ii{5-6}
  \have {8} {(P \to Q) \wedge (Q \to P)} \ai{4,7}
\end{nd}$
\end{center}
```

<!-- D46a iff to two implications: 8 lines -->

### D46b two implications to iff

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to P)}
  \have {2} {P \to Q} \ae{1}
  \have {3} {Q \to P} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {Q} \ie{2,4}
  \close
  \open
  \hypo {6} {Q}
  \have {7} {P} \ie{3,6}
  \close
  \have {8} {P \leftrightarrow Q} \bi{4-5,6-7}
\end{nd}$
\end{center}
```

<!-- D46b two implications to iff: 8 lines -->

### D48 ex falso

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {\neg P}
  \have {3} {\bot} \ne{1,2}
  \have {4} {Q} \be{3}
\end{nd}$
\end{center}
```

<!-- D48 ex falso: 4 lines -->

### E1 s03 B1 new: (PvQ)^(PvR) |- Pv(Q^R)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \wedge (P \vee R)}
  \have {2} {P \vee Q} \ae{1}
  \have {3} {P \vee R} \ae{1}
  \open
  \hypo {4} {P}
  \have {5} {P \vee (Q \wedge R)} \oi{4}
  \close
  \open
  \hypo {6} {Q}
  \open
  \hypo {7} {P}
  \have {8} {P \vee (Q \wedge R)} \oi{7}
  \close
  \open
  \hypo {9} {R}
  \have {10} {Q \wedge R} \ai{6,9}
  \have {11} {P \vee (Q \wedge R)} \oi{10}
  \close
  \have {12} {P \vee (Q \wedge R)} \oe{3,7-8,9-11}
  \close
  \have {13} {P \vee (Q \wedge R)} \oe{2,4-5,6-12}
\end{nd}$
\end{center}
```

<!-- E1 s03 B1 new: (PvQ)^(PvR) |- Pv(Q^R): 13 lines -->

### E2 s06 C2 new, correct: not(notP and notQ) |- P or Q

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge \neg Q)}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \open
  \hypo {6} {\neg Q}
  \have {7} {\neg P \wedge \neg Q} \ai{5,6}
  \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {Q} \raa{6-8}
  \have {10} {P \vee Q} \oi{9}
  \close
  \have {11} {P \vee Q} \oe{2,3-4,5-10}
\end{nd}$
\end{center}
```

<!-- E2 s06 C2 new, correct: not(notP and notQ) |- P or Q: 11 lines -->

### X E3 s06 C2 new, flawed (sibling box)

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge \neg Q)}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {\bot} \ne{3,5}
  \have {7} {Q} \be{6}
  \have {8} {P \vee Q} \oi{7}
  \close
  \have {9} {P \vee Q} \oe{2,3-4,5-8}
\end{nd}$
\end{center}
```

<!-- X E3 s06 C2 new, flawed (sibling box): 9 lines -->

### X E4 illegal step proves too much: P or Q |- P

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \open
  \hypo {2} {P}
  \close
  \open
  \hypo {3} {Q}
  \have {4} {P} \r{2}
  \close
  \have {5} {P} \oe{1,2-2,3-4}
\end{nd}$
\end{center}
```

<!-- X E4 illegal step proves too much: P or Q |- P: 5 lines -->

