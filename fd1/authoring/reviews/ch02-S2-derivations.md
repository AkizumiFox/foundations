<!-- S2a evidence for ch02: derivations the review relied on. Check with: python3 tools/check_fitch.py authoring/reviews/ch02-S2-derivations.md (expect 0 errors). Letters A, B stand for arbitrary formulas (the alpha, beta of lem-connective-rows); P, Q, R for atoms. Lines justified by \by{...} (LEM, DS, a row of lem-connective-rows, a pasted derivation) are not shape-checked. -->

# Chapter 2 S2a: derivations checked

### C1 row and TT: A, B |- A and B

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A}
  \hypo {2} {B}
  \have {3} {A \wedge B} \ai{1,2}
\end{nd}$
\end{center}
```

<!-- C1: 3 lines -->

### C2 row and F?: not A |- not(A and B)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg A}
  \open
    \hypo {2} {A \wedge B}
    \have {3} {A} \ae{2}
    \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg (A \wedge B)} \ni{2-4}
\end{nd}$
\end{center}
```

<!-- C2: 5 lines -->

### C3 row and ?F: not B |- not(A and B)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg B}
  \open
    \hypo {2} {A \wedge B}
    \have {3} {B} \ae{2}
    \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg (A \wedge B)} \ni{2-4}
\end{nd}$
\end{center}
```

<!-- C3: 5 lines -->

### C4 row or T?: A |- A or B

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A}
  \have {2} {A \vee B} \oi{1}
\end{nd}$
\end{center}
```

<!-- C4: 2 lines -->

### C5 row or ?T: B |- A or B

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {B}
  \have {2} {A \vee B} \oi{1}
\end{nd}$
\end{center}
```

<!-- C5: 2 lines -->

### C6 row or FF: not A, not B |- not(A or B)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg A}
  \hypo {2} {\neg B}
  \open
    \hypo {3} {A \vee B}
    \open
      \hypo {4} {A}
      \have {5} {\bot} \ne{4,1}
    \close
    \open
      \hypo {6} {B}
      \have {7} {\bot} \ne{6,2}
    \close
    \have {8} {\bot} \oe{3,4-5,6-7}
  \close
  \have {9} {\neg (A \vee B)} \ni{3-8}
\end{nd}$
\end{center}
```

<!-- C6: 9 lines -->

### C7 row imp F?: not A |- A -> B

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg A}
  \open
    \hypo {2} {A}
    \have {3} {\bot} \ne{2,1}
    \have {4} {B} \be{3}
  \close
  \have {5} {A \to B} \ii{2-4}
\end{nd}$
\end{center}
```

<!-- C7: 5 lines -->

### C8 row imp ?T: B |- A -> B

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {B}
  \open
    \hypo {2} {A}
    \have {3} {B} \r{1}
  \close
  \have {4} {A \to B} \ii{2-3}
\end{nd}$
\end{center}
```

<!-- C8: 4 lines -->

### C9 row imp TF: A, not B |- not(A -> B)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A}
  \hypo {2} {\neg B}
  \open
    \hypo {3} {A \to B}
    \have {4} {B} \ie{3,1}
    \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg (A \to B)} \ni{3-5}
\end{nd}$
\end{center}
```

<!-- C9: 6 lines -->

### C10 row iff TT: A, B |- A <-> B

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A}
  \hypo {2} {B}
  \open
    \hypo {3} {A}
    \have {4} {B} \r{2}
  \close
  \open
    \hypo {5} {B}
    \have {6} {A} \r{1}
  \close
  \have {7} {A \leftrightarrow B} \bi{3-4,5-6}
\end{nd}$
\end{center}
```

<!-- C10: 7 lines -->

### C11 row iff FF: not A, not B |- A <-> B

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg A}
  \hypo {2} {\neg B}
  \open
    \hypo {3} {A}
    \have {4} {\bot} \ne{3,1}
    \have {5} {B} \be{4}
  \close
  \open
    \hypo {6} {B}
    \have {7} {\bot} \ne{6,2}
    \have {8} {A} \be{7}
  \close
  \have {9} {A \leftrightarrow B} \bi{3-5,6-8}
\end{nd}$
\end{center}
```

<!-- C11: 9 lines -->

### C12 row iff TF: A, not B |- not(A <-> B)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A}
  \hypo {2} {\neg B}
  \open
    \hypo {3} {A \leftrightarrow B}
    \have {4} {B} \bie{3,1}
    \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg (A \leftrightarrow B)} \ni{3-5}
\end{nd}$
\end{center}
```

<!-- C12: 6 lines -->

### C13 row iff FT: not A, B |- not(A <-> B)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg A}
  \hypo {2} {B}
  \open
    \hypo {3} {A \leftrightarrow B}
    \have {4} {A} \bie{3,2}
    \have {5} {\bot} \ne{4,1}
  \close
  \have {6} {\neg (A \leftrightarrow B)} \ni{3-5}
\end{nd}$
\end{center}
```

<!-- C13: 6 lines -->

### C14 row not T: A |- not not A

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A}
  \open
    \hypo {2} {\neg A}
    \have {3} {\bot} \ne{1,2}
  \close
  \have {4} {\neg \neg A} \ni{2-3}
\end{nd}$
\end{center}
```

<!-- C14: 4 lines -->

### C15 row bot: |- not bot

```{=latex}
\begin{center}
$\begin{nd}
  \open
    \hypo {1} {\bot}
  \close
  \have {2} {\neg \bot} \ni{1-1}
\end{nd}$
\end{center}
```

<!-- C15: 2 lines -->

### K1 completeness Claim, false premise: G, not G |- C

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {G}
  \hypo {2} {\neg G}
  \have {3} {\bot} \ne{1,2}
  \have {4} {C} \be{3}
\end{nd}$
\end{center}
```

<!-- K1: 4 lines -->

### K2 atom splitting, instance shape (Delta = D; the two given derivations stand as vdots)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {D}
  \have {2} {P \vee \neg P} \by{LEM}{}
  \open
    \hypo {3} {P}
    \have {4} {C} \by{pasted derivation of D, P ⊢ C}{1,3}
  \close
  \open
    \hypo {5} {\neg P}
    \have {6} {C} \by{pasted derivation of D, not P ⊢ C}{1,5}
  \close
  \have {7} {C} \oe{2,3-4,5-6}
\end{nd}$
\end{center}
```

<!-- K2: 7 lines -->

### S6B3a not(P<->Q) |- not P <-> Q, primitive rules (22 lines, over the limit)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
    \hypo {2} {\neg P}
    \open
      \hypo {3} {\neg Q}
      \open
        \hypo {4} {P}
        \have {5} {\bot} \ne{4,2}
        \have {6} {Q} \be{5}
      \close
      \open
        \hypo {7} {Q}
        \have {8} {\bot} \ne{7,3}
        \have {9} {P} \be{8}
      \close
      \have {10} {P \leftrightarrow Q} \bi{4-6,7-9}
      \have {11} {\bot} \ne{10,1}
    \close
    \have {12} {Q} \raa{3-11}
  \close
  \open
    \hypo {13} {Q}
    \open
      \hypo {14} {P}
      \open
        \hypo {15} {P}
        \have {16} {Q} \r{13}
      \close
      \open
        \hypo {17} {Q}
        \have {18} {P} \r{14}
      \close
      \have {19} {P \leftrightarrow Q} \bi{15-16,17-18}
      \have {20} {\bot} \ne{19,1}
    \close
    \have {21} {\neg P} \ni{14-20}
  \close
  \have {22} {\neg P \leftrightarrow Q} \bi{2-12,13-21}
\end{nd}$
\end{center}
```

<!-- S6B3a: 22 lines -->

### S6B3b not(P<->Q) |- not P <-> Q, citing rows of lem-connective-rows (12 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
    \hypo {2} {\neg P}
    \open
      \hypo {3} {\neg Q}
      \have {4} {P \leftrightarrow Q} \by{rows (C11)}{2,3}
      \have {5} {\bot} \ne{4,1}
    \close
    \have {6} {Q} \raa{3-5}
  \close
  \open
    \hypo {7} {Q}
    \open
      \hypo {8} {P}
      \have {9} {P \leftrightarrow Q} \by{rows (C10)}{8,7}
      \have {10} {\bot} \ne{9,1}
    \close
    \have {11} {\neg P} \ni{8-10}
  \close
  \have {12} {\neg P \leftrightarrow Q} \bi{2-6,7-11}
\end{nd}$
\end{center}
```

<!-- S6B3b: 12 lines -->

### S5B1 new trap: P -> (Q or R) |- (P -> Q) or (P -> R) (exm-search-postpone-or; LEM on Q, DS)

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

<!-- S5B1: 14 lines -->

### R1x rejected candidate (too close to H&R 1.2.1(e)): P -> (Q -> R), not R |- P -> not Q

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {\neg R}
  \open
    \hypo {3} {P}
    \open
      \hypo {4} {Q}
      \have {5} {Q \to R} \ie{1,3}
      \have {6} {R} \ie{5,4}
      \have {7} {\bot} \ne{6,2}
    \close
    \have {8} {\neg Q} \ni{4-7}
  \close
  \have {9} {P \to \neg Q} \ii{3-8}
\end{nd}$
\end{center}
```

<!-- R1x: 9 lines -->

### R3 |- ((P -> Q) and (Q -> R)) -> (P -> R) without RAA

```{=latex}
\begin{center}
$\begin{nd}
  \open
    \hypo {1} {(P \to Q) \wedge (Q \to R)}
    \have {2} {P \to Q} \ae{1}
    \have {3} {Q \to R} \ae{1}
    \open
      \hypo {4} {P}
      \have {5} {Q} \ie{2,4}
      \have {6} {R} \ie{3,5}
    \close
    \have {7} {P \to R} \ii{4-6}
  \close
  \have {8} {((P \to Q) \wedge (Q \to R)) \to (P \to R)} \ii{1-7}
\end{nd}$
\end{center}
```

<!-- R3: 8 lines -->

### S6B2 method on P, P -> Q |= Q: the four signed-atom sequents collapse; one row shown: P, not Q, P, P->Q |- Q

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \hypo {3} {P}
  \hypo {4} {\neg Q}
  \have {5} {Q} \ie{2,3}
\end{nd}$
\end{center}
```

<!-- S6B2: 5 lines -->

### S6 worked example row: P, not Q |- (P -> Q) or (Q -> P) (row Q->P true via C8)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {\neg Q}
  \open
    \hypo {3} {Q}
    \have {4} {P} \r{1}
  \close
  \have {5} {Q \to P} \ii{3-4}
  \have {6} {(P \to Q) \vee (Q \to P)} \oi{5}
\end{nd}$
\end{center}
```

<!-- S6: 6 lines -->

### R1b new R1: P -> (Q -> R) |- (P and not R) -> not Q (no RAA)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \open
    \hypo {2} {P \wedge \neg R}
    \have {3} {P} \ae{2}
    \have {4} {\neg R} \ae{2}
    \open
      \hypo {5} {Q}
      \have {6} {Q \to R} \ie{1,3}
      \have {7} {R} \ie{6,5}
      \have {8} {\bot} \ne{7,4}
    \close
    \have {9} {\neg Q} \ni{5-8}
  \close
  \have {10} {(P \wedge \neg R) \to \neg Q} \ii{2-9}
\end{nd}$
\end{center}
```

<!-- R1b: 10 lines -->

### X3a exit check (a): (P -> Q) or (P -> R) |- P -> (Q or R)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \vee (P \to R)}
  \open
    \hypo {2} {P}
    \open
      \hypo {3} {P \to Q}
      \have {4} {Q} \ie{3,2}
      \have {5} {Q \vee R} \oi{4}
    \close
    \open
      \hypo {6} {P \to R}
      \have {7} {R} \ie{6,2}
      \have {8} {Q \vee R} \oi{7}
    \close
    \have {9} {Q \vee R} \oe{1,3-5,6-8}
  \close
  \have {10} {P \to (Q \vee R)} \ii{2-9}
\end{nd}$
\end{center}
```

<!-- X3a: 10 lines -->

### X3d exit check (d): P and (Q -> R) |- (P -> Q) -> R

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \to R)}
  \open
    \hypo {2} {P \to Q}
    \have {3} {P} \ae{1}
    \have {4} {Q} \ie{2,3}
    \have {5} {Q \to R} \ae{1}
    \have {6} {R} \ie{5,4}
  \close
  \have {7} {(P \to Q) \to R} \ii{2-6}
\end{nd}$
\end{center}
```

<!-- X3d: 7 lines -->
