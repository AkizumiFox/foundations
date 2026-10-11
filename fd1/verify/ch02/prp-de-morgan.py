"""prp-de-morgan (Ch 2 s05): the rows in the Idea, the four laws, which derivations use RAA,
and the 11-line LEM route to (d) described after the proof."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403
P, Q, R, S, N, G = V("P"), V("Q"), V("R"), V("S"), V("N"), V("G")

QUOTED = {
    "row_P_true_Q_false": {"premise": True, "notP": False},
    "row_P_false_Q_true": {"premise": True, "notQ": False},
    "raa_free": ["a", "b", "c"],
    "lem_route_lines": 11,
}
prem = Not(And(P, Q))
v = {"P": True, "Q": False}
assert tv(prem, v) == QUOTED["row_P_true_Q_false"]["premise"]
assert tv(Not(P), v) == QUOTED["row_P_true_Q_false"]["notP"]
v = {"P": False, "Q": True}
assert tv(prem, v) == QUOTED["row_P_false_Q_true"]["premise"]
assert tv(Not(Q), v) == QUOTED["row_P_false_Q_true"]["notQ"]
laws = {
    "a": ([Not(Or(P, Q))], And(Not(P), Not(Q))),
    "b": ([And(Not(P), Not(Q))], Not(Or(P, Q))),
    "c": ([Or(Not(P), Not(Q))], Not(And(P, Q))),
    "d": ([Not(And(P, Q))], Or(Not(P), Not(Q))),
}
for k, (pr, c) in laws.items():
    assert classically_valid(pr, c), k
    km = kripke_refutation(pr, c)
    if k in QUOTED["raa_free"]:
        assert km is None, (k, km)      # consistent with the RAA-free derivations
    else:
        assert km is not None           # (d): "no derivation avoids a classical rule" (stated, not proved)
assert not classically_valid([prem], Not(P)) and not classically_valid([prem], Not(Q))
# The LEM route to (d), as the paragraph after the proof describes it.
lem_route = r"""
  \hypo {1} {\neg (P \wedge Q)}
  \have {2} {P \vee \neg P} \lem{}
  \open
  \hypo {3} {P}
  \open
  \hypo {4} {Q}
  \have {5} {P \wedge Q} \ai{3,4}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg Q} \ni{4-6}
  \have {8} {\neg P \vee \neg Q} \oi{7}
  \close
  \open
  \hypo {9} {\neg P}
  \have {10} {\neg P \vee \neg Q} \oi{9}
  \close
  \have {11} {\neg P \vee \neg Q} \oe{2,3-8,9-10}
"""
errs, n = check_derivation(lem_route)
assert errs == [] and n == QUOTED["lem_route_lines"], (errs, n)
print("prp-de-morgan: ok")
