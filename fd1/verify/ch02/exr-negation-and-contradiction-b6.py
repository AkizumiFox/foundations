"""exr-negation-and-contradiction-b6 (Ch 2, Section 2.2): derive or break.
Each verdict by truth table (derive: valid; break: invalid). Each derivation is written out
and checked by tools/check_fitch.py, with the line count the solution prints, and uses only
the rules of Chapter 1 and Sections 2.1-2.2 (no RAA line); each derived sequent also has no
G3 or Kripke refutation, as a derivation without RAA requires. Each break at its stated
number makes the counterexample set true; for (e) the implication holds at every grid point."""
import sys, pathlib
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "ch01"))
from _grid import grid
from _s05s06_logic import (V, Not, And, Or, Imp, classically_valid, g3_refutation,
                           kripke_refutation, check_derivation)

P, Q, R = V("P"), V("Q"), V("R")
CLAIMS = {
    "a": ([P], Not(And(Not(P), Q)), "derive"),
    "b": ([Not(And(P, Q))], Not(P), "break"),
    "c": ([Imp(Or(P, Q), Not(P))], Not(P), "derive"),
    "d": ([Imp(P, Imp(Q, R)), Not(R)], Not(And(P, Q)), "derive"),
    "e": ([Not(Q)], Not(Imp(P, Q)), "break"),
    "f": ([Imp(P, Q), Imp(P, Not(Q))], Not(P), "derive"),
    "g": ([Not(Not(And(P, Q)))], Not(Not(P)), "derive"),
    "h": ([Not(Not(P))], Not(Not(And(P, Q))), "break"),
}
QUOTED = {"b": 1, "e": 0, "h": 1, "lines": {"a": 5, "c": 6, "d": 9, "f": 7, "g": 8}}
for k, (prem, concl, verdict) in CLAIMS.items():
    assert classically_valid(prem, concl) == (verdict == "derive"), k
    if verdict == "derive":
        assert g3_refutation(prem, concl) is None, k
        assert kripke_refutation(prem, concl) is None, k

D = {
"a": r"""
  \hypo {1} {P}
  \open
  \hypo {2} {\neg P \wedge Q}
  \have {3} {\neg P} \ae{2}
  \have {4} {\bot} \ne{1,3}
  \close
  \have {5} {\neg(\neg P \wedge Q)} \ni{2-4}
""",
"c": r"""
  \hypo {1} {(P \vee Q) \to \neg P}
  \open
  \hypo {2} {P}
  \have {3} {P \vee Q} \oi{2}
  \have {4} {\neg P} \ie{1,3}
  \have {5} {\bot} \ne{2,4}
  \close
  \have {6} {\neg P} \ni{2-5}
""",
"d": r"""
  \hypo {1} {P \to (Q \to R)}
  \hypo {2} {\neg R}
  \open
  \hypo {3} {P \wedge Q}
  \have {4} {P} \ae{3}
  \have {5} {Q \to R} \ie{1,4}
  \have {6} {Q} \ae{3}
  \have {7} {R} \ie{5,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {\neg(P \wedge Q)} \ni{3-8}
""",
"f": r"""
  \hypo {1} {P \to Q}
  \hypo {2} {P \to \neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\neg Q} \ie{2,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg P} \ni{3-6}
""",
"g": r"""
  \hypo {1} {\neg\neg(P \wedge Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P \wedge Q}
  \have {4} {P} \ae{3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg(P \wedge Q)} \ni{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {\neg\neg P} \ni{2-7}
""",
}
for k, body in D.items():
    err, n = check_derivation(body)
    assert err == [] and n == QUOTED["lines"][k], (k, err)
    assert "\\raa" not in body and "\\nne" not in body and "\\lem" not in body

imp = lambda a, b: (not a) or b
# (b) P: x > 0, Q: x > 5 at x = 1: not(P and Q) true, not not P (that is, P) true
x = Fraction(QUOTED["b"]); assert (not (x > 0 and x > 5)) and x > 0
# (e) P: x > 5, Q: x > 3; P -> Q everywhere; at 0: not Q true, P -> Q true
assert all(imp(t > 5, t > 3) for t in grid())
x = Fraction(QUOTED["e"]); assert (not x > 3) and imp(x > 5, x > 3)
# (h) P: x > 0, Q: x > 5 at x = 1: P true, P and Q false
x = Fraction(QUOTED["h"]); assert x > 0 and not (x > 0 and x > 5)
print("exr-negation-and-contradiction-b6: all verdicts and witnesses check")
