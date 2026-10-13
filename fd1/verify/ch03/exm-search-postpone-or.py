"""exm-search-postpone-or (Ch 2 s06): the two rows quoted, validity, the 14-line derivation, and the
22-line derivation by LEM on P mentioned at the end."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {
    "row1": {"P": True, "Q": True, "R": False, "premise": True, "P->R": False},
    "row2": {"P": True, "Q": False, "R": True, "premise": True, "P->Q": False},
    "lines_lem_on_Q": 14,
    "lines_lem_on_P": 22,
}
prem = Imp(P, Or(Q, R))
goal = Or(Imp(P, Q), Imp(P, R))
r = QUOTED["row1"]; v = {k: r[k] for k in "PQR"}
assert tv(prem, v) == r["premise"] and tv(Imp(P, R), v) == r["P->R"]
r = QUOTED["row2"]; v = {k: r[k] for k in "PQR"}
assert tv(prem, v) == r["premise"] and tv(Imp(P, Q), v) == r["P->Q"]
assert classically_valid([prem], goal)
assert kripke_refutation([prem], goal) is not None   # a classical step is used (not claimed as necessary)
d14 = r"""
  \hypo {1} {P \to (Q \vee R)}
  \have {2} {Q \vee \neg Q} \lem{}
  \open
  \hypo {3} {Q}
  \open
  \hypo {4} {P}
  \have {5} {Q} \r{3}
  \close
  \have {6} {P \to Q} \ii{4-5}
  \have {7} {(P \to Q) \vee (P \to R)} \oi{6}
  \close
  \open
  \hypo {8} {\neg Q}
  \open
  \hypo {9} {P}
  \have {10} {Q \vee R} \ie{1,9}
  \have {11} {R} \ds{10,8}
  \close
  \have {12} {P \to R} \ii{9-11}
  \have {13} {(P \to Q) \vee (P \to R)} \oi{12}
  \close
  \have {14} {(P \to Q) \vee (P \to R)} \oe{2,3-7,8-13}
"""
errs, n = check_derivation(d14)
assert errs == [] and n == QUOTED["lines_lem_on_Q"], errs
d22 = r"""
  \hypo {1} {P \to (Q \vee R)}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {Q \vee R} \ie{1,3}
  \open
  \hypo {5} {Q}
  \open
  \hypo {6} {P}
  \have {7} {Q} \r{5}
  \close
  \have {8} {P \to Q} \ii{6-7}
  \have {9} {(P \to Q) \vee (P \to R)} \oi{8}
  \close
  \open
  \hypo {10} {R}
  \open
  \hypo {11} {P}
  \have {12} {R} \r{10}
  \close
  \have {13} {P \to R} \ii{11-12}
  \have {14} {(P \to Q) \vee (P \to R)} \oi{13}
  \close
  \have {15} {(P \to Q) \vee (P \to R)} \oe{4,5-9,10-14}
  \close
  \open
  \hypo {16} {\neg P}
  \open
  \hypo {17} {P}
  \have {18} {\bot} \ne{17,16}
  \have {19} {Q} \be{18}
  \close
  \have {20} {P \to Q} \ii{17-19}
  \have {21} {(P \to Q) \vee (P \to R)} \oi{20}
  \close
  \have {22} {(P \to Q) \vee (P \to R)} \oe{2,3-15,16-21}
"""
errs, n = check_derivation(d22)
assert errs == [] and n == QUOTED["lines_lem_on_P"], errs
print("exm-search-postpone-or: ok")
