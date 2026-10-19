"""exm-search-free-lines (Ch 3 s01): P and (P -> Q), Q -> R |- (S -> R) and (T -> (Q and R)) is valid;
the 13-line derivation checks; the boxes-first version (lines 3-6 repeated in each box) has 16 lines."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, T = V("P"), V("Q"), V("R"), V("S"), V("T")
prem = [And(P, Imp(P, Q)), Imp(Q, R)]
concl = And(Imp(S, R), Imp(T, And(Q, R)))
assert classically_valid(prem, concl)
d = r"""
  \hypo {1} {P \wedge (P \to Q)}
  \hypo {2} {Q \to R}
  \have {3} {P} \ae{1}
  \have {4} {P \to Q} \ae{1}
  \have {5} {Q} \ie{4,3}
  \have {6} {R} \ie{2,5}
  \open
  \hypo {7} {S}
  \have {8} {R} \r{6}
  \close
  \have {9} {S \to R} \ii{7-8}
  \open
  \hypo {10} {T}
  \have {11} {Q \wedge R} \ai{5,6}
  \close
  \have {12} {T \to (Q \wedge R)} \ii{10-11}
  \have {13} {(S \to R) \wedge (T \to (Q \wedge R))} \ai{9,12}
"""
errs, n = check_derivation(d)
assert errs == [] and n == 13, errs
boxes_first = r"""
  \hypo {1} {P \wedge (P \to Q)}
  \hypo {2} {Q \to R}
  \open
  \hypo {3} {S}
  \have {4} {P} \ae{1}
  \have {5} {P \to Q} \ae{1}
  \have {6} {Q} \ie{5,4}
  \have {7} {R} \ie{2,6}
  \close
  \have {8} {S \to R} \ii{3-7}
  \open
  \hypo {9} {T}
  \have {10} {P} \ae{1}
  \have {11} {P \to Q} \ae{1}
  \have {12} {Q} \ie{11,10}
  \have {13} {R} \ie{2,12}
  \have {14} {Q \wedge R} \ai{12,13}
  \close
  \have {15} {T \to (Q \wedge R)} \ii{9-14}
  \have {16} {(S \to R) \wedge (T \to (Q \wedge R))} \ai{8,15}
"""
errs, n = check_derivation(boxes_first)
assert errs == [] and n == 16, errs
print("exm-search-free-lines: ok")
