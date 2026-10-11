"""exr-reductio-and-classical-rules-c3 (Ch 2 s05, exit check): |- P or (P -> Q) is valid, classical
(internal Kripke witness), and the 9-line derivation with one RAA at line 9 checks."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}
goal = Or(P, Imp(P, Q))
assert classically_valid([], goal)
assert kripke_refutation([], goal) is not None
assert not classically_valid([], P) and not classically_valid([], Imp(P, Q))
d = r"""
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
"""
errs, n = check_derivation(d)
assert errs == [] and n == 9 and d.count("raa") == 1
print("exr-reductio-and-classical-rules-c3: ok")
