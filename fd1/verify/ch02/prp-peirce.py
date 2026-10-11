"""prp-peirce (Ch 2 s05): valid; its RAA cannot be avoided (stated without proof in the text);
the 10-line derivation; assuming not-Q at the stalled gap gives no clash."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"lines": 10}
law = Imp(Imp(Imp(P, Q), P), P)
assert classically_valid([], law)
assert kripke_refutation([], law) is not None        # internal witness, not in the text
d = r"""
  \open
  \hypo {1} {(P \to Q) \to P}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \have {7} {P} \ie{1,6}
  \have {8} {\bot} \ne{7,2}
  \close
  \have {9} {P} \raa{2-8}
  \close
  \have {10} {((P \to Q) \to P) \to P} \ii{1-9}
"""
errs, n = check_derivation(d)
assert errs == [] and n == QUOTED["lines"]
# At the stalled gap the resources are (P->Q)->P, P and the would-be assumption not-Q:
# they are jointly satisfiable, so no clash (bot) can be derived from them.
assert not classically_valid([Imp(Imp(P, Q), P), P, Not(Q)], BOT)
print("prp-peirce: ok")
