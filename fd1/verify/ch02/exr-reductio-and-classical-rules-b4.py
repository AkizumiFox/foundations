"""exr-reductio-and-classical-rules-b4 (Ch 2 s05, the scaffold "Stuck at a letter"): the sequent
(not P -> Q) and (not P -> R), not(Q and R) |- P is classically valid, has no derivation without RAA
(a Kripke countermodel), and the 10-line completion checks with one RAA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R = V("P"), V("Q"), V("R")

QUOTED = {"lines": 10}
prem = [And(Imp(Not(P), Q), Imp(Not(P), R)), Not(And(Q, R))]
assert classically_valid(prem, P)
assert kripke_refutation(prem, P) is not None
body = r"""
  \hypo {1} {(\neg P \to Q) \wedge (\neg P \to R)}
  \hypo {2} {\neg (Q \wedge R)}
  \open
  \hypo {3} {\neg P}
  \have {4} {\neg P \to Q} \ae{1}
  \have {5} {Q} \ie{4,3}
  \have {6} {\neg P \to R} \ae{1}
  \have {7} {R} \ie{6,3}
  \have {8} {Q \wedge R} \ai{5,7}
  \have {9} {\bot} \ne{8,2}
  \close
  \have {10} {P} \raa{3-9}
"""
errs, n = check_derivation(body)
assert errs == [] and n == QUOTED["lines"], errs
print("exr-reductio-and-classical-rules-b4: ok")
