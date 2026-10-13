"""exm-search-distribute (Ch 2 s06): the 14-line derivation checks; "nine of the fourteen lines" were
written by goal-directed steps and four (3, 4, 5, 10) by premise-directed steps."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"lines": 14, "premise_directed": [3, 4, 5, 10]}
d = r"""
  \hypo {1} {P \to \neg Q}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {Q} \ae{2}
  \have {5} {\neg Q} \ie{1,3}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg (P \wedge Q)} \ni{2-6}
  \open
  \hypo {8} {Q}
  \open
  \hypo {9} {P}
  \have {10} {\neg Q} \ie{1,9}
  \have {11} {\bot} \ne{8,10}
  \close
  \have {12} {\neg P} \ni{9-11}
  \close
  \have {13} {Q \to \neg P} \ii{8-12}
  \have {14} {\neg (P \wedge Q) \wedge (Q \to \neg P)} \ai{7,13}
"""
errs, n = check_derivation(d)
assert errs == [] and n == QUOTED["lines"]
# lines present in the second snapshot (written by step 2): the box assumptions, the current goals, the closings
snapshot2 = {1, 2, 6, 7, 8, 9, 11, 12, 13, 14}
goal_directed = snapshot2 - {1}                   # line 1 is the premise
assert len(goal_directed) == 9
assert sorted(set(range(1, 15)) - snapshot2) == QUOTED["premise_directed"]
print("exm-search-distribute: ok")
