"""exr-finding-derivations-c3 (Ch 2 s06, exit check): valid; classical (internal witness); the 13-line
RAA route and the 11-line LEM-on-P route check; LEM on Q needs a second classical step in the case Q."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"lines_lem_route": 11}
prem = Not(And(Not(P), Q))
goal = Or(P, Not(Q))
assert classically_valid([prem], goal)
assert kripke_refutation([prem], goal) is not None
assert not classically_valid([prem], P) and not classically_valid([prem], Not(Q))   # no side in hand
# case Q of a split on Q: P is needed, and it is not intuitionistically available there
assert classically_valid([prem, Q], P) and kripke_refutation([prem, Q], P) is not None
raa = r"""
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
"""
errs, n = check_derivation(raa)
assert errs == [] and n == 13
lem = r"""
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
"""
errs, n = check_derivation(lem)
assert errs == [] and n == QUOTED["lines_lem_route"]
print("exr-finding-derivations-c3: ok")
