"""Section 1.4: the gallery exm-proving-an-implication-instances and the Not-allowed block
after the rule card.

(1) The three gallery rows are instances of ->I: each box is written out below as a
derivation and checked by the book's derivation checker (tools/check_fitch.py, imported),
and each new line is a tautology (truth table).
(2) The WRONG/RIGHT pair: WRONG fails at line 6 only; RIGHT checks clean.
(3) The break of the WRONG list at x = 1, with P: x > 5, R: x > 0, Q: x > 3: the first
premise (x > 5 and x > 0) -> x > 3 holds for every real x, and at x = 1 the premises are true
and Q is false."""
import sys, pathlib, itertools
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parents[2]))          # the repository root, for tools/
from _grid import grid
from tools.check_fitch import check_text

QUOTED = {"x": 1}

ROWS = r"""
```{=latex}
$\begin{nd}
  \open
  \hypo {1} {P \wedge \neg Q}
  \have {2} {P} \ae{1}
  \have {3} {P \wedge (P \wedge \neg Q)} \ai{2,1}
  \close
  \have {4} {(P \wedge \neg Q) \to (P \wedge (P \wedge \neg Q))} \ii{1-3}
\end{nd}$
```

```{=latex}
$\begin{nd}
  \open
  \hypo {1} {Q \to R}
  \open
  \hypo {2} {P \to Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{2,3}
  \have {5} {R} \ie{1,4}
  \close
  \have {6} {P \to R} \ii{3-5}
  \close
  \have {7} {(P \to Q) \to (P \to R)} \ii{2-6}
  \close
  \have {8} {(Q \to R) \to ((P \to Q) \to (P \to R))} \ii{1-7}
\end{nd}$
```

```{=latex}
$\begin{nd}
  \open
  \hypo {1} {(P \vee Q) \wedge R}
  \close
  \have {2} {((P \vee Q) \wedge R) \to ((P \vee Q) \wedge R)} \ii{1-1}
\end{nd}$
```

```{=latex}
$\begin{nd}
  \hypo {1} {(P \wedge R) \to Q}
  \hypo {2} {R}
  \open
  \hypo {3} {P}
  \have {4} {P \wedge R} \ai{3,2}
  \have {5} {Q} \ie{1,4}
  \close
  \have {6} {P \to Q} \ii{3-5}
\end{nd}$
```
"""
errors, notes, counts = check_text(ROWS)
assert errors == [], errors
assert counts["derivations"] == 4, counts

WRONG = r"""
```{=latex}
$\begin{nd}
  \hypo {1} {(P \wedge R) \to Q}
  \hypo {2} {R}
  \open
  \hypo {3} {P} \purpose{\ii}
  \have {4} {P \wedge R} \ai{3,2}
  \have {5} {Q} \ie{1,4}
  \close
  \have {6} {Q} \r{5}
\end{nd}$
```
"""
errors, notes, counts = check_text(WRONG)
assert len(errors) == 1 and errors[0][1].startswith("line 6 "), errors

imp = lambda a, b: (not a) or b
for P, Q, R in itertools.product((False, True), repeat=3):
    assert imp(P and not Q, P and (P and not Q))
    assert imp(imp(Q, R), imp(imp(P, Q), imp(P, R)))
# (3)
for x in grid():
    assert imp(x > 5 and x > 0, x > 3)
x = QUOTED["x"]
assert x > 0 and not x > 3 and imp(x > 5 and x > 0, x > 3)
print("exm-proving-an-implication-instances: checks")
