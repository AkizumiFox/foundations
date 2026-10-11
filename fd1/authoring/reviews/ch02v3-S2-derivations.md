<!-- S2a evidence for the rewritten Chapter 2 (ch02v3): derivations the review relied on, beyond the D-numbers of authoring/reviews/ch01-S2-derivations.md. Check with: python3 tools/check_fitch.py authoring/reviews/ch02v3-S2-derivations.md (expect 0 errors). Lines by derived rules (MT, DS, CP, LEM, VI = vacuous implication) are \by lines: their shape is not machine-checked; each rule is derived from primitives in the D-file (D15, D17a, D14, D27, D20). -->

# Chapter 2 (v3) S2a: derivations checked

### N4a exm-first-contradictions (a): bot |- P (2 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\bot}
  \have {2} {P} \be{1}
\end{nd}$
\end{center}
```

### N4b exm-first-contradictions (b) as drafted: P and not P |- Q (5 lines; H&R's ex falso example, replaced below)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge \neg P}
  \have {2} {P} \ae{1}
  \have {3} {\neg P} \ae{1}
  \have {4} {\bot} \ne{2,3}
  \have {5} {Q} \be{4}
\end{nd}$
\end{center}
```

### N4b' replacement: P and Q, not Q |- R (5 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {\neg Q}
  \have {3} {Q} \ae{1}
  \have {4} {\bot} \ne{3,2}
  \have {5} {R} \be{4}
\end{nd}$
\end{center}
```

### N1 exm-manufactured-clash: not(P or Q) |- P -> R (6 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
    \hypo {2} {P}
    \have {3} {P \vee Q} \oi{2}
    \have {4} {\bot} \ne{3,1}
    \have {5} {R} \be{4}
  \close
  \have {6} {P \to R} \ii{2-5}
\end{nd}$
\end{center}
```

### N2 exm-impossible-case: P or Q, P -> R, not R |- Q (9 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {P \to R}
  \hypo {3} {\neg R}
  \open
    \hypo {4} {P}
    \have {5} {R} \ie{2,4}
    \have {6} {\bot} \ne{5,3}
    \have {7} {Q} \be{6}
  \close
  \open
    \hypo {8} {Q}
  \close
  \have {9} {Q} \oe{1,4-7,8-8}
\end{nd}$
\end{center}
```

### N10 skeleton of thm-square-even-implies-even, no CP/DS/notI (12 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \vee O}
  \hypo {2} {\neg (S \wedge T)}
  \hypo {3} {O \to T}
  \open
    \hypo {4} {S}
    \open
      \hypo {5} {E}
    \close
    \open
      \hypo {6} {O}
      \have {7} {T} \ie{3,6}
      \have {8} {S \wedge T} \ai{4,7}
      \have {9} {\bot} \ne{8,2}
      \have {10} {E} \be{9}
    \close
    \have {11} {E} \oe{1,5-5,6-10}
  \close
  \have {12} {S \to E} \ii{4-11}
\end{nd}$
\end{center}
```

### N13a s01 B1(a): not(P or Q) |- Q -> R (6 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \vee Q)}
  \open
    \hypo {2} {Q}
    \have {3} {P \vee Q} \oi{2}
    \have {4} {\bot} \ne{3,1}
    \have {5} {R} \be{4}
  \close
  \have {6} {Q \to R} \ii{2-5}
\end{nd}$
\end{center}
```

### N13b' s01 B1(b) replacement: (P -> Q) and not Q, P |- not R (7 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge \neg Q}
  \hypo {2} {P}
  \have {3} {P \to Q} \ae{1}
  \have {4} {\neg Q} \ae{1}
  \have {5} {Q} \ie{3,2}
  \have {6} {\bot} \ne{5,4}
  \have {7} {\neg R} \be{6}
\end{nd}$
\end{center}
```

### N12 s01 C1(a): P or (Q and not Q) |- P (8 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee (Q \wedge \neg Q)}
  \open
    \hypo {2} {P}
  \close
  \open
    \hypo {3} {Q \wedge \neg Q}
    \have {4} {Q} \ae{3}
    \have {5} {\neg Q} \ae{3}
    \have {6} {\bot} \ne{4,5}
    \have {7} {P} \be{6}
  \close
  \have {8} {P} \oe{1,2-2,3-7}
\end{nd}$
\end{center}
```

### N3 s01 C2 flawed: not P |- P -> Q, line 4 cites a closed box (expect-invalid; fails at 4 only)

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
    \hypo {2} {P}
    \have {3} {\bot} \ne{2,1}
  \close
  \have {4} {Q} \be{3}
  \open
    \hypo {5} {P}
    \have {6} {Q} \r{4}
  \close
  \have {7} {P \to Q} \ii{5-6}
\end{nd}$
\end{center}
```

### N3b the same move proves too much: not P |- Q (expect-invalid)

```{=latex}
% expect-invalid
\begin{center}
$\begin{nd}
  \hypo {1} {\neg P}
  \open
    \hypo {2} {P}
    \have {3} {\bot} \ne{2,1}
  \close
  \have {4} {Q} \be{3}
\end{nd}$
\end{center}
```

### N5 s02 B1: P -> not Q |- Q -> not P (7 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to \neg Q}
  \open
    \hypo {2} {Q}
    \open
      \hypo {3} {P}
      \have {4} {\neg Q} \ie{1,3}
      \have {5} {\bot} \ne{2,4}
    \close
    \have {6} {\neg P} \ni{3-5}
  \close
  \have {7} {Q \to \neg P} \ii{2-6}
\end{nd}$
\end{center}
```

### N6a exm-derived-rules-in-use (a): P -> Q, Q -> R, not R |- not P by MT twice (5 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {\neg R}
  \have {4} {\neg Q} \mt{2,3}
  \have {5} {\neg P} \mt{1,4}
\end{nd}$
\end{center}
```

### N6a-expanded: the same with each MT line replaced by its four-line box (11 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \hypo {3} {\neg R}
  \open
    \hypo {4} {Q}
    \have {5} {R} \ie{2,4}
    \have {6} {\bot} \ne{5,3}
  \close
  \have {7} {\neg Q} \ni{4-6}
  \open
    \hypo {8} {P}
    \have {9} {Q} \ie{1,8}
    \have {10} {\bot} \ne{9,7}
  \close
  \have {11} {\neg P} \ni{8-10}
\end{nd}$
\end{center}
```

### N7 exm-derived-rules-in-use (b): P or Q, not P, Q -> R |- R (5 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee Q}
  \hypo {2} {\neg P}
  \hypo {3} {Q \to R}
  \have {4} {Q} \ds{1,2}
  \have {5} {R} \ie{3,4}
\end{nd}$
\end{center}
```

### N16 s03 B3: (P or Q) -> R, not R |- not P and not Q (12 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \hypo {2} {\neg R}
  \have {3} {\neg (P \vee Q)} \mt{1,2}
  \open
    \hypo {4} {P}
    \have {5} {P \vee Q} \oi{4}
    \have {6} {\bot} \ne{5,3}
  \close
  \have {7} {\neg P} \ni{4-6}
  \open
    \hypo {8} {Q}
    \have {9} {P \vee Q} \oi{8}
    \have {10} {\bot} \ne{9,3}
  \close
  \have {11} {\neg Q} \ni{8-10}
  \have {12} {\neg P \wedge \neg Q} \ai{7,11}
\end{nd}$
\end{center}
```

### N14 s03 C1(a) as drafted: P -> Q, not P -> Q, not Q |- bot (6 lines; close to H&R 1.2.5(d), replaced below)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg P \to Q}
  \hypo {3} {\neg Q}
  \have {4} {\neg P} \mt{1,3}
  \have {5} {\neg\neg P} \mt{2,3}
  \have {6} {\bot} \ne{4,5}
\end{nd}$
\end{center}
```

### N15 s03 C1(b) as drafted: P -> Q, not P -> Q |- not not Q (7 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg P \to Q}
  \open
    \hypo {3} {\neg Q}
    \have {4} {\neg P} \mt{1,3}
    \have {5} {\neg\neg P} \mt{2,3}
    \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg\neg Q} \ni{3-6}
\end{nd}$
\end{center}
```

### N14' s03 C1(a) replacement: P -> Q, not P -> R, not Q, not R |- bot (7 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg P \to R}
  \hypo {3} {\neg Q}
  \hypo {4} {\neg R}
  \have {5} {\neg P} \mt{1,3}
  \have {6} {\neg\neg P} \mt{2,4}
  \have {7} {\bot} \ne{5,6}
\end{nd}$
\end{center}
```

### N15' s03 C1(b) replacement: P -> Q, not P -> R |- not(not Q and not R) (9 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {\neg P \to R}
  \open
    \hypo {3} {\neg Q \wedge \neg R}
    \have {4} {\neg Q} \ae{3}
    \have {5} {\neg R} \ae{3}
    \have {6} {\neg P} \mt{1,4}
    \have {7} {\neg\neg P} \mt{2,5}
    \have {8} {\bot} \ne{6,7}
  \close
  \have {9} {\neg (\neg Q \wedge \neg R)} \ni{3-8}
\end{nd}$
\end{center}
```

### N17 s03 C3 exit check skeleton: E or O, E -> S, not(S and T) |- T -> O (12 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {E \vee O}
  \hypo {2} {E \to S}
  \hypo {3} {\neg (S \wedge T)}
  \open
    \hypo {4} {T}
    \open
      \hypo {5} {S}
      \have {6} {S \wedge T} \ai{5,4}
      \have {7} {\bot} \ne{6,3}
    \close
    \have {8} {\neg S} \ni{5-7}
    \have {9} {\neg S \to \neg E} \ctp{2}
    \have {10} {\neg E} \ie{9,8}
    \have {11} {O} \ds{1,10}
  \close
  \have {12} {T \to O} \ii{4-11}
\end{nd}$
\end{center}
```

### N8 exm-iff-symmetric: P iff Q |- Q iff P (6 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \open
    \hypo {2} {Q}
    \have {3} {P} \bie{1,2}
  \close
  \open
    \hypo {4} {P}
    \have {5} {Q} \bie{1,4}
  \close
  \have {6} {Q \leftrightarrow P} \bi{2-3,4-5}
\end{nd}$
\end{center}
```

### N11 s05 B1(a) as drafted: |- not not (P or not P) without RAA (8 lines; = Chapter 5's key proof prp-not-not-excluded-middle, replaced below)

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
  \have {8} {\neg\neg (P \vee \neg P)} \ni{1-7}
\end{nd}$
\end{center}
```

### N11' s05 B1(a) replacement: not not P, not not (P -> Q) |- not not Q without RAA (12 lines). (The first candidate, |- not not (not not P -> P), is Chapter 5's B1, so it was not used.)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg\neg P}
  \hypo {2} {\neg\neg (P \to Q)}
  \open
    \hypo {3} {\neg Q}
    \open
      \hypo {4} {P}
      \open
        \hypo {5} {P \to Q}
        \have {6} {Q} \ie{5,4}
        \have {7} {\bot} \ne{6,3}
      \close
      \have {8} {\neg (P \to Q)} \ni{5-7}
      \have {9} {\bot} \ne{8,2}
    \close
    \have {10} {\neg P} \ni{4-9}
    \have {11} {\bot} \ne{10,1}
  \close
  \have {12} {\neg\neg Q} \ni{3-11}
\end{nd}$
\end{center}
```

### N18 s05 C3 exit check replacement: |- P or (P -> Q) from the primitive rules (9 lines, one RAA)

```{=latex}
\begin{center}
$\begin{nd}
  \open
    \hypo {1} {\neg (P \vee (P \to Q))}
    \open
      \hypo {2} {P}
      \have {3} {P \vee (P \to Q)} \oi{2}
      \have {4} {\bot} \ne{3,1}
      \have {5} {Q} \be{4}
    \close
    \have {6} {P \to Q} \ii{2-5}
    \have {7} {P \vee (P \to Q)} \oi{6}
    \have {8} {\bot} \ne{7,1}
  \close
  \have {9} {P \vee (P \to Q)} \raa{1-8}
\end{nd}$
\end{center}
```

### N19 s06 C3 exit check replacement: not(not P and Q) |- P or not Q, RAA route (13 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge Q)}
  \open
    \hypo {2} {\neg (P \vee \neg Q)}
    \open
      \hypo {3} {Q}
      \open
        \hypo {4} {P}
        \have {5} {P \vee \neg Q} \oi{4}
        \have {6} {\bot} \ne{5,2}
      \close
      \have {7} {\neg P} \ni{4-6}
      \have {8} {\neg P \wedge Q} \ai{7,3}
      \have {9} {\bot} \ne{8,1}
    \close
    \have {10} {\neg Q} \ni{3-9}
    \have {11} {P \vee \neg Q} \oi{10}
    \have {12} {\bot} \ne{11,2}
  \close
  \have {13} {P \vee \neg Q} \raa{2-12}
\end{nd}$
\end{center}
```

### N19' the same, LEM route on P (11 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (\neg P \wedge Q)}
  \have {2} {P \vee \neg P} \lem{}
  \open
    \hypo {3} {P}
    \have {4} {P \vee \neg Q} \oi{3}
  \close
  \open
    \hypo {5} {\neg P}
    \open
      \hypo {6} {Q}
      \have {7} {\neg P \wedge Q} \ai{5,6}
      \have {8} {\bot} \ne{7,1}
    \close
    \have {9} {\neg Q} \ni{6-8}
    \have {10} {P \vee \neg Q} \oi{9}
  \close
  \have {11} {P \vee \neg Q} \oe{2,3-4,5-10}
\end{nd}$
\end{center}
```

### N20 s06 B1(b) with vacuous implication as one line: not(P -> Q) |- P and not Q (12 lines, one RAA)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (P \to Q)}
  \open
    \hypo {2} {\neg P}
    \have {3} {P \to Q} \by{VI}{2}
    \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {P} \raa{2-4}
  \open
    \hypo {6} {Q}
    \open
      \hypo {7} {P}
      \have {8} {Q} \r{6}
    \close
    \have {9} {P \to Q} \ii{7-8}
    \have {10} {\bot} \ne{9,1}
  \close
  \have {11} {\neg Q} \ni{6-10}
  \have {12} {P \wedge \neg Q} \ai{5,11}
\end{nd}$
\end{center}
```

### N21 s06 R3: not(N or G) |- not N and (G -> S) (11 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg (N \vee G)}
  \open
    \hypo {2} {N}
    \have {3} {N \vee G} \oi{2}
    \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg N} \ni{2-4}
  \open
    \hypo {6} {G}
    \have {7} {N \vee G} \oi{6}
    \have {8} {\bot} \ne{7,1}
    \have {9} {S} \be{8}
  \close
  \have {10} {G \to S} \ii{6-9}
  \have {11} {\neg N \wedge (G \to S)} \ai{5,10}
\end{nd}$
\end{center}
```

### N22 degenerate RAA: P |- P (4 lines)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \open
    \hypo {2} {\neg P}
    \have {3} {\bot} \ne{1,2}
  \close
  \have {4} {P} \raa{2-3}
\end{nd}$
\end{center}
```

### S1 schema instances with P, Q (shape check of the blueprint's schemas): notE, botE

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

### S2 schema instances: notI

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {\neg Q}
  \open
    \hypo {2} {Q}
    \have {3} {\bot} \ne{2,1}
  \close
  \have {4} {\neg Q} \ni{2-3}
\end{nd}$
\end{center}
```

### S3 schema instances: iffE both directions, RAA

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \leftrightarrow Q}
  \hypo {2} {P}
  \hypo {3} {\neg\neg Q}
  \have {4} {Q} \bie{1,2}
  \have {5} {P} \bie{1,4}
  \open
    \hypo {6} {\neg Q}
    \have {7} {\bot} \ne{6,3}
  \close
  \have {8} {Q} \raa{6-7}
\end{nd}$
\end{center}
```

### N23 s06 B3 replacement: P -> (Q -> R), P -> (R -> S) |- P -> (Q -> S) (10 lines; replaces D43 = H&R 1.2.1(k) curried)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {P \to (R \to S)}
  \open
    \hypo {3} {P}
    \have {4} {Q \to R} \ie{1,3}
    \have {5} {R \to S} \ie{2,3}
    \open
      \hypo {6} {Q}
      \have {7} {R} \ie{4,6}
      \have {8} {S} \ie{5,7}
    \close
    \have {9} {Q \to S} \ii{6-8}
  \close
  \have {10} {P \to (Q \to S)} \ii{3-9}
\end{nd}$
\end{center}
```

### N24 s06 B1(a) replacement: P and (Q -> R) |- (P -> Q) -> R (7 lines)

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
