<!-- S2a (v3) evidence for authoring/blueprints/ch01.md: every schema (with the metavariables replaced by letters so the rule shape is checked) and every derivation the blueprint claims, tagged by section. Check with: python3 tools/check_fitch.py authoring/reviews/ch01v3-S2-derivations.md. Blocks titled "X ..." are marked expect-invalid. Each heading lists the rules used; the generator (scratch) confirmed that no block of §0n uses a rule introduced after §0n and that no block before §05 has a box. -->

# Chapter 1 (v3 blueprint) S2a: derivations checked

## Schemas, metavariables replaced by letters (φ := P, ψ := Q, χ := R)

### Tr (toy, §02): shape is \by, not checked; only structure

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {A}
  \have {j} {B}
  \have {k} {C} \by{Tr}{i,j}
\end{nd}$
\end{center}
```

### and-I, and-E (proposed layout: one new line per schema)

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {P}
  \have {j} {Q}
  \have {k} {P \wedge Q} \ai{i,j}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {P \wedge Q}
  \have {k} {P} \ae{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {P \wedge Q}
  \have {k} {Q} \ae{i}
\end{nd}$
\end{center}
```

### imp-E

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {P \to Q}
  \have {j} {P}
  \have {k} {Q} \ie{i,j}
\end{nd}$
\end{center}
```

### imp-I

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \open
  \hypo {i} {P}
  \have {} {\vdots}
  \have {j} {Q}
  \close
  \have {k} {P \to Q} \ii{i-j}
\end{nd}$
\end{center}
```

### R (general form proposed: no box needed)

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {P}
  \have {} {\vdots}
  \have {k} {P} \r{i}
\end{nd}$
\end{center}
```

### R as printed in the blueprint (into a box)

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {P}
  \have {} {\vdots}
  \open
  \hypo {j} {Q}
  \have {} {\vdots}
  \have {k} {P} \r{i}
  \close
\end{nd}$
\end{center}
```

### or-I (proposed layout: one new line per schema)

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {P}
  \have {k} {P \vee Q} \oi{i}
\end{nd}$
\qquad
$\begin{nd}[schema]
  \have {i} {P}
  \have {k} {Q \vee P} \oi{i}
\end{nd}$
\end{center}
```

### or-E

```{=latex}
% schema
\begin{center}
$\begin{nd}[schema]
  \have {i} {P \vee Q}
  \open
  \hypo {j} {P}
  \have {} {\vdots}
  \have {k} {R}
  \close
  \open
  \hypo {l} {Q}
  \have {} {\vdots}
  \have {m} {R}
  \close
  \have {n} {R} \oe{i,j-k,l-m}
\end{nd}$
\end{center}
```

### X schema shape test: a wrong or-I instance must be caught

```{=latex}
% schema
% expect-invalid
\begin{center}
$\begin{nd}[schema]
  \have {i} {P}
  \have {k} {Q \wedge P} \oi{i}
\end{nd}$
\end{center}
```

## Derivations (by section)

### S03 exm-conjunction-warm-ups (a) P, Q |- Q and P (§03, 3 lines; rules: ai)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {Q}
  \have {3} {Q \wedge P} \ai{2,1}
\end{nd}$
\end{center}
```

### S03 exm-conjunction-warm-ups (b) P |- P and P (§03, 2 lines; rules: ai)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have {2} {P \wedge P} \ai{1,1}
\end{nd}$
\end{center}
```

### S03 exm-conjunction-warm-ups (c) P and Q |- Q (§03, 2 lines; rules: ae)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {Q} \ae{1}
\end{nd}$
\end{center}
```

### S03 prp-and-commutes (§03, 4 lines; rules: ae ai)

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

### S03 prp-and-associative (§03, 7 lines; rules: ae ai)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \wedge R}
  \have {2} {P \wedge Q} \ae{1}
  \have {3} {R} \ae{1}
  \have {4} {P} \ae{2}
  \have {5} {Q} \ae{2}
  \have {6} {Q \wedge R} \ai{5,3}
  \have {7} {P \wedge (Q \wedge R)} \ai{4,6}
\end{nd}$
\end{center}
```

### S03 item 4: P and Q, R |- (P and R) and (Q and R) (§03, 7 lines; rules: ae ai)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {R}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ae{1}
  \have {5} {P \wedge R} \ai{3,2}
  \have {6} {Q \wedge R} \ai{4,2}
  \have {7} {(P \wedge R) \wedge (Q \wedge R)} \ai{5,6}
\end{nd}$
\end{center}
```

### S03 item 5 (stretch): (P and Q) and (R and S) |- (S and Q) and (P and R) (§03, 10 lines; rules: ae ai)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \wedge (R \wedge S)}
  \have {2} {P \wedge Q} \ae{1}
  \have {3} {R \wedge S} \ae{1}
  \have {4} {P} \ae{2}
  \have {5} {Q} \ae{2}
  \have {6} {R} \ae{3}
  \have {7} {S} \ae{3}
  \have {8} {S \wedge Q} \ai{7,5}
  \have {9} {P \wedge R} \ai{4,6}
  \have {10} {(S \wedge Q) \wedge (P \wedge R)} \ai{8,9}
\end{nd}$
\end{center}
```

### S03 exm-product-in-unit-interval skeleton (arithmetic as a non-logical rule; A: 0<x, B: x<1, C: 0<y, D: y<1, E: 0<xy, F: xy<1) (§03, 9 lines; rules: ae ai by:algebra)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A \wedge B}
  \hypo {2} {C \wedge D}
  \have {3} {A} \ae{1}
  \have {4} {B} \ae{1}
  \have {5} {C} \ae{2}
  \have {6} {D} \ae{2}
  \have {7} {E} \by{algebra}{3,5}
  \have {8} {F} \by{algebra}{3,4,6}
  \have {9} {E \wedge F} \ai{7,8}
\end{nd}$
\end{center}
```

### S03 A1(e): P and (Q and R) |- R and P (§03, 5 lines; rules: ae ai)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \wedge R} \ae{1}
  \have {4} {R} \ae{3}
  \have {5} {R \wedge P} \ai{4,2}
\end{nd}$
\end{center}
```

### S03 B1: P and (Q and R) |- (P and Q) and R (§03, 7 lines; rules: ae ai)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \wedge R} \ae{1}
  \have {4} {Q} \ae{3}
  \have {5} {R} \ae{3}
  \have {6} {P \wedge Q} \ai{2,4}
  \have {7} {(P \wedge Q) \wedge R} \ai{6,5}
\end{nd}$
\end{center}
```

### S03 C2 correct: P and (Q and R) |- Q and P (5 lines) (§03, 5 lines; rules: ae ai)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {P} \ae{1}
  \have {3} {Q \wedge R} \ae{1}
  \have {4} {Q} \ae{3}
  \have {5} {Q \wedge P} \ai{4,2}
\end{nd}$
\end{center}
```

### X S03 C2 student's shortcut (line 2 not an instance) (§03, 4 lines; rules: ae ai)

```{=latex}
\begin{center}
% expect-invalid
$\begin{nd}
  \hypo {1} {P \wedge (Q \wedge R)}
  \have {2} {Q} \ae{1}
  \have {3} {P} \ae{1}
  \have {4} {Q \wedge P} \ai{2,3}
\end{nd}$
\end{center}
```

### X S03 warning (2): and-E on an implication (§03, 2 lines; rules: ae)

```{=latex}
\begin{center}
% expect-invalid
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \have {2} {P} \ae{1}
\end{nd}$
\end{center}
```

### S04 (a) P -> Q, P |- Q (§04, 3 lines; rules: ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {P}
  \have {3} {Q} \ie{1,2}
\end{nd}$
\end{center}
```

### S04 (b) P, P -> Q, Q -> R |- R (§04, 5 lines; rules: ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \hypo {3} {Q \to R}
  \have {4} {Q} \ie{2,1}
  \have {5} {R} \ie{3,4}
\end{nd}$
\end{center}
```

### S04 (c) P and Q, P -> (Q -> R) |- R (§04, 6 lines; rules: ae ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \hypo {2} {P \to (Q \to R)}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ae{1}
  \have {5} {Q \to R} \ie{2,3}
  \have {6} {R} \ie{5,4}
\end{nd}$
\end{center}
```

### S04 (d) (P and Q) -> R, P, Q |- R (§04, 5 lines; rules: ai ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {P}
  \hypo {3} {Q}
  \have {4} {P \wedge Q} \ai{2,3}
  \have {5} {R} \ie{1,4}
\end{nd}$
\end{center}
```

### S04 (e) (P -> Q) and (R -> S), P and R |- Q and S (§04, 9 lines; rules: ae ai ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (R \to S)}
  \hypo {2} {P \wedge R}
  \have {3} {P \to Q} \ae{1}
  \have {4} {R \to S} \ae{1}
  \have {5} {P} \ae{2}
  \have {6} {R} \ae{2}
  \have {7} {Q} \ie{3,5}
  \have {8} {S} \ie{4,6}
  \have {9} {Q \wedge S} \ai{7,8}
\end{nd}$
\end{center}
```

### S04 B1 first: P, P -> Q, Q -> (R and S) |- S and Q (§04, 7 lines; rules: ae ai ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \hypo {2} {P \to Q}
  \hypo {3} {Q \to (R \wedge S)}
  \have {4} {Q} \ie{2,1}
  \have {5} {R \wedge S} \ie{3,4}
  \have {6} {S} \ae{5}
  \have {7} {S \wedge Q} \ai{6,4}
\end{nd}$
\end{center}
```

### S04 B1 second: (P and Q) -> R, Q and P |- R (§04, 6 lines; rules: ae ai ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \to R}
  \hypo {2} {Q \wedge P}
  \have {3} {Q} \ae{2}
  \have {4} {P} \ae{2}
  \have {5} {P \wedge Q} \ai{4,3}
  \have {6} {R} \ie{1,5}
\end{nd}$
\end{center}
```

### S04 B2 skeleton (A: 0<x, B: x<1, C: x^2<x, D: x^3<x^2) (§04, 5 lines; rules: ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(A \wedge B) \to C}
  \hypo {2} {C \to D}
  \hypo {3} {A \wedge B}
  \have {4} {C} \ie{1,3}
  \have {5} {D} \ie{2,4}
\end{nd}$
\end{center}
```

### X S04 C1 affirming the consequent (line 3 not an instance) (§04, 3 lines; rules: ie)

```{=latex}
\begin{center}
% expect-invalid
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q}
  \have {3} {P} \ie{1,2}
\end{nd}$
\end{center}
```

### S04 C2: P -> (Q -> R), S -> P, S and Q |- R and S (§04, 9 lines; rules: ae ai ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {S \to P}
  \hypo {3} {S \wedge Q}
  \have {4} {S} \ae{3}
  \have {5} {Q} \ae{3}
  \have {6} {P} \ie{2,4}
  \have {7} {Q \to R} \ie{1,6}
  \have {8} {R} \ie{7,5}
  \have {9} {R \wedge S} \ai{8,4}
\end{nd}$
\end{center}
```

### S04 math example (A: x>2, B: x^2>4, C: x^2+1>5) (§04, 5 lines; rules: ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A \to B}
  \hypo {2} {B \to C}
  \hypo {3} {A}
  \have {4} {B} \ie{1,3}
  \have {5} {C} \ie{2,4}
\end{nd}$
\end{center}
```

### S05 prp-implication-transitive (D2) (§05, 6 lines, 1 box(es); rules: ie ii)

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

### S05 remark: (P -> Q) and (Q -> R) |- P -> R (book.yaml must-prove) (§05, 7 lines, 1 box(es); rules: ae ie ii)

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

### X S05 exm-illegal-citation (§05, 7 lines, 1 box(es); rules: ie ii r)

```{=latex}
\begin{center}
% expect-invalid
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {P \to R} \ii{3-5}
  \have {7} {R} \r{5}
\end{nd}$
\end{center}
```

### S05 exm-first-boxes (a) |- P -> P (§05, 2 lines, 1 box(es); rules: ii)

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

### S05 exm-first-boxes (b) |- P -> (Q -> P): 5 lines, not 4 (§05, 5 lines, 2 box(es); rules: ii r)

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

### S05 prp-curry => (D3a) (§05, 7 lines, 2 box(es); rules: ai ie ii)

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

### S05 prp-curry <= (D3b) (§05, 7 lines, 1 box(es); rules: ae ie ii)

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

### S05 exm-first-boxes (c) = B4's derivation (D6) (§05, 7 lines, 2 box(es); rules: ie ii)

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

### X S05 B4 distractor 1: R by R 5 after the inner box closed (§05, 8 lines, 2 box(es); rules: ie ii r)

```{=latex}
\begin{center}
% expect-invalid
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
  \have {7} {R} \r{5}
  \close
  \have {8} {Q \to R} \ii{2-7}
\end{nd}$
\end{center}
```

### S05 quick check (replacement, not H&R 1.2.1(r)): Q and R |- (P -> Q) and (S -> R): two boxes (§05, 8 lines, 2 box(es); rules: ae ai ii)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q \wedge R}
  \open
  \hypo {2} {P}
  \have {3} {Q} \ae{1}
  \close
  \have {4} {P \to Q} \ii{2-3}
  \open
  \hypo {5} {S}
  \have {6} {R} \ae{1}
  \close
  \have {7} {S \to R} \ii{5-6}
  \have {8} {(P \to Q) \wedge (S \to R)} \ai{4,7}
\end{nd}$
\end{center}
```

### S05 B1: |- (P and Q) -> (Q and P) (§05, 5 lines, 1 box(es); rules: ae ai ii)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {Q} \ae{1}
  \have {4} {Q \wedge P} \ai{3,2}
  \close
  \have {5} {(P \wedge Q) \to (Q \wedge P)} \ii{1-4}
\end{nd}$
\end{center}
```

### S05 B2 (a): Q |- P -> Q (§05, 4 lines, 1 box(es); rules: ii r)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \r{1}
  \close
  \have {4} {P \to Q} \ii{2-3}
\end{nd}$
\end{center}
```

### S05 B2 (b): |- (P and Q) -> (R -> Q) (§05, 6 lines, 2 box(es); rules: ae ii r)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge Q}
  \have {2} {Q} \ae{1}
  \open
  \hypo {3} {R}
  \have {4} {Q} \r{2}
  \close
  \have {5} {R \to Q} \ii{3-4}
  \close
  \have {6} {(P \wedge Q) \to (R \to Q)} \ii{1-5}
\end{nd}$
\end{center}
```

### S05 B3 (D7) (§05, 7 lines, 1 box(es); rules: ai ie ii)

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

### S05 C2 (D8) (§05, 10 lines, 3 box(es); rules: ie ii r)

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

### S05 C1 repaired (exit check 3) (§05, 14 lines, 4 box(es); rules: ai ie ii)

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
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {P \wedge Q} \ai{9,8}
  \have {11} {R} \ie{1,10}
  \close
  \have {12} {P \to R} \ii{9-11}
  \close
  \have {13} {Q \to (P \to R)} \ii{8-12}
  \have {14} {(P \to (Q \to R)) \wedge (Q \to (P \to R))} \ai{7,13}
\end{nd}$
\end{center}
```

### S05 C3 NEW exit check: P -> Q, (Q -> R) and (R -> S) |- P -> S (§05, 9 lines, 1 box(es); rules: ae ie ii)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {(Q \to R) \wedge (R \to S)}
  \have {3} {Q \to R} \ae{2}
  \have {4} {R \to S} \ae{2}
  \open
  \hypo {5} {P}
  \have {6} {Q} \ie{1,5}
  \have {7} {R} \ie{3,6}
  \have {8} {S} \ie{4,7}
  \close
  \have {9} {P \to S} \ii{5-8}
\end{nd}$
\end{center}
```

### S06 (a) P |- P or Q (§06, 2 lines; rules: oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have {2} {P \vee Q} \oi{1}
\end{nd}$
\end{center}
```

### S06 (a') P |- Q or P (§06, 2 lines; rules: oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have {2} {Q \vee P} \oi{1}
\end{nd}$
\end{center}
```

### S06 (b) P and Q |- P or Q (§06, 3 lines; rules: ae oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge Q}
  \have {2} {P} \ae{1}
  \have {3} {P \vee Q} \oi{2}
\end{nd}$
\end{center}
```

### S06 (c) P -> Q |- P -> (Q or R) (§06, 5 lines, 1 box(es); rules: ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {P}
  \have {3} {Q} \ie{1,2}
  \have {4} {Q \vee R} \oi{3}
  \close
  \have {5} {P \to (Q \vee R)} \ii{2-4}
\end{nd}$
\end{center}
```

### S06 (d) (P and Q) -> R |- P -> (Q -> (R or S)) (§06, 8 lines, 2 box(es); rules: ai ie ii oi)

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
  \have {6} {R \vee S} \oi{5}
  \close
  \have {7} {Q \to (R \vee S)} \ii{3-6}
  \close
  \have {8} {P \to (Q \to (R \vee S))} \ii{2-7}
\end{nd}$
\end{center}
```

### S06 exm-or-hypothesis-split (D12b): 10 lines, not 9 (§06, 10 lines, 2 box(es); rules: ai ie ii oi)

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

### S06 exm-product-zero (A: a=0, B: b=0, C: ab=0) (§06, 5 lines, 1 box(es); rules: ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(A \vee B) \to C}
  \open
  \hypo {2} {A}
  \have {3} {A \vee B} \oi{2}
  \have {4} {C} \ie{1,3}
  \close
  \have {5} {A \to C} \ii{2-4}
\end{nd}$
\end{center}
```

### S06 B1 old (H&R Ex 1.15 variant; replaced): P -> Q |- (P and R) -> (Q or S) (§06, 6 lines, 1 box(es); rules: ae ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \open
  \hypo {2} {P \wedge R}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ie{1,3}
  \have {5} {Q \vee S} \oi{4}
  \close
  \have {6} {(P \wedge R) \to (Q \vee S)} \ii{2-5}
\end{nd}$
\end{center}
```

### S06 B1 NEW: P and (Q -> R) |- Q -> (R or S) (§06, 6 lines, 1 box(es); rules: ae ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \wedge (Q \to R)}
  \open
  \hypo {2} {Q}
  \have {3} {Q \to R} \ae{1}
  \have {4} {R} \ie{3,2}
  \have {5} {R \vee S} \oi{4}
  \close
  \have {6} {Q \to (R \vee S)} \ii{2-5}
\end{nd}$
\end{center}
```

### S06 B1 second: P |- (Q or P) or R (§06, 3 lines; rules: oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P}
  \have {2} {Q \vee P} \oi{1}
  \have {3} {(Q \vee P) \vee R} \oi{2}
\end{nd}$
\end{center}
```

### S06 B2 old (near H&R 1.2.1(o)/(l); replaced): P -> R, Q -> S |- (P and Q) -> (R or S) (§06, 7 lines, 1 box(es); rules: ae ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to R}
  \hypo {2} {Q \to S}
  \open
  \hypo {3} {P \wedge Q}
  \have {4} {P} \ae{3}
  \have {5} {R} \ie{1,4}
  \have {6} {R \vee S} \oi{5}
  \close
  \have {7} {(P \wedge Q) \to (R \vee S)} \ii{3-6}
\end{nd}$
\end{center}
```

### S06 B2 NEW (faded, line 7 blank): P -> Q, Q -> R |- P -> (S or R) (§06, 7 lines, 1 box(es); rules: ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to Q}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {R} \ie{2,4}
  \have {6} {S \vee R} \oi{5}
  \close
  \have {7} {P \to (S \vee R)} \ii{3-6}
\end{nd}$
\end{center}
```

### S06 B3 skeleton (A: x>1, B: x=1, C: x^2>=x) (§06, 5 lines, 1 box(es); rules: ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(A \vee B) \to C}
  \open
  \hypo {2} {A}
  \have {3} {A \vee B} \oi{2}
  \have {4} {C} \ie{1,3}
  \close
  \have {5} {A \to C} \ii{2-4}
\end{nd}$
\end{center}
```

### S06 C2 first: (P or Q) -> (R and S) |- P -> S (§06, 6 lines, 1 box(es); rules: ae ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to (R \wedge S)}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {R \wedge S} \ie{1,3}
  \have {5} {S} \ae{4}
  \close
  \have {6} {P \to S} \ii{2-5}
\end{nd}$
\end{center}
```

### S06 C2 second: (P or Q) -> R |- (P and Q) -> R (§06, 6 lines, 1 box(es); rules: ae ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \vee Q) \to R}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {P \vee Q} \oi{3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {(P \wedge Q) \to R} \ii{2-5}
\end{nd}$
\end{center}
```

### S07 exm-disjunction-first-derivations (a) (D10) (§07, 6 lines, 2 box(es); rules: oe oi)

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

### S07 exm-disjunction-first-derivations (b) P or P |- P (§07, 4 lines, 2 box(es); rules: oe)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \vee P}
  \open
  \hypo {2} {P}
  \close
  \open
  \hypo {3} {P}
  \close
  \have {4} {P} \oe{1,2-2,3-3}
\end{nd}$
\end{center}
```

### S07 exm-cases-on-hypothesis (D12a) (§07, 10 lines, 3 box(es); rules: ae ie ii oe)

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

### S07 prp-distributivity => (D9a) (§07, 10 lines, 2 box(es); rules: ae ai oe oi)

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

### S07 prp-distributivity <= (D9b) (§07, 12 lines, 2 box(es); rules: ae ai oe oi)

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

### S07 exm-disjunction-regroup (D11): 12 lines, not 13 (§07, 12 lines, 4 box(es); rules: oe oi)

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

### S07 item 5: P or Q, P -> R, Q -> R |- R (§07, 8 lines, 2 box(es); rules: ie oe)

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

### S07 exm-abs-at-least-x skeleton (A: x>=0, B: x<0, C: |x|=x, D: |x|>x; goal D or C unfolds |x|>=x) (§07, 10 lines, 2 box(es); rules: ie oe oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {A \vee B}
  \hypo {2} {A \to C}
  \hypo {3} {B \to D}
  \open
  \hypo {4} {A}
  \have {5} {C} \ie{2,4}
  \have {6} {D \vee C} \oi{5}
  \close
  \open
  \hypo {7} {B}
  \have {8} {D} \ie{3,7}
  \have {9} {D \vee C} \oi{8}
  \close
  \have {10} {D \vee C} \oe{1,4-6,7-9}
\end{nd}$
\end{center}
```

### S07 B1 (E1) (§07, 13 lines, 4 box(es); rules: ae ai oe oi)

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

### S07 B3 (a): P or Q, P -> R, Q -> S |- R or S (§07, 10 lines, 2 box(es); rules: ie oe oi)

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

### S07 C3 exit check: (P and Q) or (R and Q) |- (P or R) and Q (§07, 12 lines, 2 box(es); rules: ae ai oe oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \vee (R \wedge Q)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {P \vee R} \oi{3}
  \have {6} {(P \vee R) \wedge Q} \ai{5,4}
  \close
  \open
  \hypo {7} {R \wedge Q}
  \have {8} {R} \ae{7}
  \have {9} {Q} \ae{7}
  \have {10} {P \vee R} \oi{8}
  \have {11} {(P \vee R) \wedge Q} \ai{10,9}
  \close
  \have {12} {(P \vee R) \wedge Q} \oe{1,2-6,7-11}
\end{nd}$
\end{center}
```

### S07 C3 second route (two or-E, then and-I): must score under the scheme (§07, 14 lines, 4 box(es); rules: ae ai oe oi)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \wedge Q) \vee (R \wedge Q)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {P \vee R} \oi{3}
  \close
  \open
  \hypo {5} {R \wedge Q}
  \have {6} {R} \ae{5}
  \have {7} {P \vee R} \oi{6}
  \close
  \have {8} {P \vee R} \oe{1,2-4,5-7}
  \open
  \hypo {9} {P \wedge Q}
  \have {10} {Q} \ae{9}
  \close
  \open
  \hypo {11} {R \wedge Q}
  \have {12} {Q} \ae{11}
  \close
  \have {13} {Q} \oe{1,9-10,11-12}
  \have {14} {(P \vee R) \wedge Q} \ai{8,13}
\end{nd}$
\end{center}
```

### S07 C4 old (= H&R Exercise 1.2.1(x) verbatim; replaced) (§07, 11 lines, 3 box(es); rules: ie ii oe)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {P \to (Q \vee R)}
  \hypo {2} {Q \to S}
  \hypo {3} {R \to S}
  \open
  \hypo {4} {P}
  \have {5} {Q \vee R} \ie{1,4}
  \open
  \hypo {6} {Q}
  \have {7} {S} \ie{2,6}
  \close
  \open
  \hypo {8} {R}
  \have {9} {S} \ie{3,8}
  \close
  \have {10} {S} \oe{5,6-7,8-9}
  \close
  \have {11} {P \to S} \ii{4-10}
\end{nd}$
\end{center}
```

### S07 C4 NEW (faded, lines 1-4 given): Q or R, Q -> (P -> S), R -> S |- P -> S (§07, 11 lines, 3 box(es); rules: ie ii oe)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {Q \vee R}
  \hypo {2} {Q \to (P \to S)}
  \hypo {3} {R \to S}
  \open
  \hypo {4} {P}
  \open
  \hypo {5} {Q}
  \have {6} {P \to S} \ie{2,5}
  \have {7} {S} \ie{6,4}
  \close
  \open
  \hypo {8} {R}
  \have {9} {S} \ie{3,8}
  \close
  \have {10} {S} \oe{1,5-7,8-9}
  \close
  \have {11} {P \to S} \ii{4-10}
\end{nd}$
\end{center}
```

### S07 R1: (C and B) -> I, B, C |- I and B (§07, 6 lines; rules: ai ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(C \wedge B) \to I}
  \hypo {2} {B}
  \hypo {3} {C}
  \have {4} {C \wedge B} \ai{3,2}
  \have {5} {I} \ie{1,4}
  \have {6} {I \wedge B} \ai{5,2}
\end{nd}$
\end{center}
```

### S07 R2: (P -> Q) and (Q -> R), P and S |- R and S (§07, 9 lines; rules: ae ai ie)

```{=latex}
\begin{center}
$\begin{nd}
  \hypo {1} {(P \to Q) \wedge (Q \to R)}
  \hypo {2} {P \wedge S}
  \have {3} {P \to Q} \ae{1}
  \have {4} {Q \to R} \ae{1}
  \have {5} {P} \ae{2}
  \have {6} {S} \ae{2}
  \have {7} {Q} \ie{3,5}
  \have {8} {R} \ie{4,7}
  \have {9} {R \wedge S} \ai{8,6}
\end{nd}$
\end{center}
```

### S07 R3 old (= H&R 1.2.1(s) closed by ->I; replaced) (§07, 9 lines, 2 box(es); rules: ae ai ie ii)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {(P \to Q) \wedge (P \to R)}
  \open
  \hypo {2} {P}
  \have {3} {P \to Q} \ae{1}
  \have {4} {P \to R} \ae{1}
  \have {5} {Q} \ie{3,2}
  \have {6} {R} \ie{4,2}
  \have {7} {Q \wedge R} \ai{5,6}
  \close
  \have {8} {P \to (Q \wedge R)} \ii{2-7}
  \close
  \have {9} {((P \to Q) \wedge (P \to R)) \to (P \to (Q \wedge R))} \ii{1-8}
\end{nd}$
\end{center}
```

### S07 R3 NEW: |- (P and (P -> Q)) -> (Q or R) (§07, 6 lines, 1 box(es); rules: ae ie ii oi)

```{=latex}
\begin{center}
$\begin{nd}
  \open
  \hypo {1} {P \wedge (P \to Q)}
  \have {2} {P} \ae{1}
  \have {3} {P \to Q} \ae{1}
  \have {4} {Q} \ie{3,2}
  \have {5} {Q \vee R} \oi{4}
  \close
  \have {6} {(P \wedge (P \to Q)) \to (Q \vee R)} \ii{1-5}
\end{nd}$
\end{center}
```
