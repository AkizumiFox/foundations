"""exm-reductio-and-classical-rules-instances (Ch 2 s05), its Not-allowed block: the WRONG half fails
at line 7 only and the RIGHT half checks; the claim (P or R) -> Q, not Q |- P breaks with
P: x > 2, R: x < -2, Q: x^2 > 4 (first premise true for every real x; at x = 0 the second premise
holds and P fails); RIGHT's sequent is classically valid."""
import sys
from fractions import Fraction
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R = V("P"), V("Q"), V("R")

QUOTED = {"x": 0}
p = lambda x: x > 2
r = lambda x: x < -2
q = lambda x: x * x > 4
for k in range(-4000, 4001):
    x = Fraction(k, 400)
    assert (not (p(x) or r(x))) or q(x)          # first premise at every sampled x
x = QUOTED["x"]
assert (not q(x)) and (not p(x))                 # second premise true, P false
assert not classically_valid([Imp(Or(P, R), Q), Not(Q)], P)
assert classically_valid([Imp(Or(P, R), Q), Not(Q)], Not(P))
head = r"""
  \hypo {1} {(P \vee R) \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {P \vee R} \oi{3}
  \have {5} {Q} \ie{1,4}
  \have {6} {\bot} \ne{5,2}
  \close
"""
errs, _ = check_derivation(head + r"  \have {7} {P} \raa{3-6}")
assert len(errs) == 1 and "line 7" in errs[0][1], errs
errs, _ = check_derivation(head + r"  \have {7} {\neg P} \ni{3-6}")
assert errs == [], errs
print("exm-reductio-and-classical-rules-instances: ok")
