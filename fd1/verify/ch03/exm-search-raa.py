"""exm-search-raa (Ch 2 s06): not(P iff Q) |- P or Q is valid; the 13-line derivation checks; the
search's claims: no side is in hand, and after LEM on P the case not-P is stuck again."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"lines": 13}
prem = Not(Iff(P, Q))
assert classically_valid([prem], Or(P, Q))
assert not classically_valid([prem], P) and not classically_valid([prem], Q)
assert kripke_refutation([prem], Or(P, Q)) is not None      # internal: RAA-free derivation impossible
# in the case not-P the goal Q is not reachable without a classical step (internal witness)
assert classically_valid([prem, Not(P)], Q) and kripke_refutation([prem, Not(P)], Q) is not None
d = r"""
  \hypo {1} {\neg (P \leftrightarrow Q)}
  \open
  \hypo {2} {\neg (P \vee Q)}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \have {5} {\bot} \ne{4,2}
  \have {6} {Q} \be{5}
  \close
  \open
  \hypo {7} {Q}
  \have {8} {P \vee Q} \oi{7}
  \have {9} {\bot} \ne{8,2}
  \have {10} {P} \be{9}
  \close
  \have {11} {P \leftrightarrow Q} \bi{3-6,7-10}
  \have {12} {\bot} \ne{11,1}
  \close
  \have {13} {P \vee Q} \raa{2-12}
"""
errs, n = check_derivation(d)
assert errs == [] and n == QUOTED["lines"], errs
print("exm-search-raa: ok")
