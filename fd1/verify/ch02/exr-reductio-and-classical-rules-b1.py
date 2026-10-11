"""exr-reductio-and-classical-rules-b1 (Ch 2 s05): (a) holds without RAA (12 lines), and Q does not
follow without a classical step; (b) is valid and its derivation uses RAA."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {}
a = ([Not(Not(P)), Not(Not(Imp(P, Q)))], Not(Not(Q)))
assert classically_valid(*a)
assert kripke_refutation(*a) is None
assert kripke_refutation(a[0], Q) is not None       # removing the outer not-not is classical (not claimed)
d = r"""
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
"""
errs, n = check_derivation(d)
assert errs == [] and n == 12 and "raa" not in d
b = ([Imp(Not(P), Q), Imp(Not(P), Not(Q))], P)
assert classically_valid(*b)
assert kripke_refutation(*b) is not None
print("exr-reductio-and-classical-rules-b1: ok")
