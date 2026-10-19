"""exr-finding-derivations-b4 (Ch 3 s01): the 11-line derivation with detours checks; the 6-line
rewrite checks; the claim is valid. Also A2 (h): the breaking choice makes every resource true and R false."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S = V("P"), V("Q"), V("R"), V("S")
assert classically_valid([And(P, Q), Imp(Q, R)], And(R, P))
long = r"""
  \hypo {1} {P \wedge Q}
  \hypo {2} {Q \to R}
  \have {3} {Q} \ae{1}
  \open
  \hypo {4} {Q}
  \have {5} {R} \ie{2,4}
  \close
  \have {6} {Q \to R} \ii{4-5}
  \have {7} {R} \ie{6,3}
  \have {8} {P} \ae{1}
  \have {9} {R \wedge P} \ai{7,8}
  \have {10} {R} \ae{9}
  \have {11} {R \wedge P} \ai{10,8}
"""
errs, n = check_derivation(long)
assert errs == [] and n == 11, errs
short = r"""
  \hypo {1} {P \wedge Q}
  \hypo {2} {Q \to R}
  \have {3} {Q} \ae{1}
  \have {4} {R} \ie{2,3}
  \have {5} {P} \ae{1}
  \have {6} {R \wedge P} \ai{4,5}
"""
errs, n = check_derivation(short)
assert errs == [] and n == 6, errs
# A2 (h): P false, Q true, R false, S true
v = {"P": False, "Q": True, "R": False, "S": True}
assert tv(Or(P, Q), v) and tv(Imp(P, R), v) and tv(Imp(Q, S), v) and not tv(R, v)
print("exr-finding-derivations-b4: ok")
