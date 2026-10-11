"""exr-reductio-and-classical-rules-c2 (Ch 2 s05): the sequent is derivable (true conclusion);
the illegal step proves P or Q |- P, refuted by the row P false, Q true; the corrected derivation."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"row": {"P": False, "Q": True}}
assert classically_valid([Not(And(Not(P), Not(Q)))], Or(P, Q))
v = QUOTED["row"]
assert tv(Or(P, Q), v) is True and tv(P, v) is False
flawed = r"""
  \hypo {1} {\neg (\neg P \wedge \neg Q)}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {\bot} \ne{3,5}
  \have {7} {Q} \be{6}
  \have {8} {P \vee Q} \oi{7}
  \close
  \have {9} {P \vee Q} \oe{2,3-4,5-8}
"""
errs, _ = check_derivation(flawed)
assert len(errs) == 1 and "line 6" in errs[0][1], errs     # fails exactly at line 6
print("exr-reductio-and-classical-rules-c2: ok")
