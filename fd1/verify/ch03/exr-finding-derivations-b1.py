"""exr-finding-derivations-b1 (Ch 2 s06): (a) 7 lines; (b) 12 lines with VI, 15 with primitive rules
only, and P is the conjunct obtained by RAA; (c) 8 lines."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {"lines_b": 12, "lines_b_primitive": 15, "lines_c": 8}
assert classically_valid([And(P, Imp(Q, R))], Imp(Imp(P, Q), R))
prem = Not(Imp(P, Q))
assert classically_valid([prem], And(P, Not(Q)))
assert kripke_refutation([prem], P) is not None       # "no derivation of P avoids RAA": stated, not proved
assert kripke_refutation([prem], Not(Q)) is None
assert classically_valid([Imp(Not(P), Q)], Or(P, Q))
b15 = r"""
  \hypo {1} {\neg (P \to Q)}
  \open
  \hypo {2} {\neg P}
  \open
  \hypo {3} {P}
  \have {4} {\bot} \ne{3,2}
  \have {5} {Q} \be{4}
  \close
  \have {6} {P \to Q} \ii{3-5}
  \have {7} {\bot} \ne{6,1}
  \close
  \have {8} {P} \raa{2-7}
  \open
  \hypo {9} {Q}
  \open
  \hypo {10} {P}
  \have {11} {Q} \r{9}
  \close
  \have {12} {P \to Q} \ii{10-11}
  \have {13} {\bot} \ne{12,1}
  \close
  \have {14} {\neg Q} \ni{9-13}
  \have {15} {P \wedge \neg Q} \ai{8,14}
"""
errs, n = check_derivation(b15)
assert errs == [] and n == QUOTED["lines_b_primitive"]
assert n - 3 == QUOTED["lines_b"]         # the four lines 3-6 become the one line "VI 2"
c = r"""
  \hypo {1} {\neg P \to Q}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \have {4} {P \vee Q} \oi{3}
  \close
  \open
  \hypo {5} {\neg P}
  \have {6} {Q} \ie{1,5}
  \have {7} {P \vee Q} \oi{6}
  \close
  \have {8} {P \vee Q} \oe{2,3-4,5-7}
"""
errs, n = check_derivation(c)
assert errs == [] and n == QUOTED["lines_c"]
print("exr-finding-derivations-b1: ok")
