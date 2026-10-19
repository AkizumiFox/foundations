"""exr-negation-and-contradiction-a2 (Ch 2, Section 2.2): the drill bank.
(g) the filled justification column derives  not Q, P -> (Q and R) |- not P  (7 lines);
(j) the illegal line is line 7 only; (l) the identity x^2 + 4 - 2x = (x - 1)^2 + 3 and
(x - 1)^2 = -3 under the supposition; (m)-(o) the three derivations check, with the line
counts quoted; each derived sequent is classically valid."""
from fractions import Fraction as F
from _s05s06_logic import V, Not, And, Or, Imp, classically_valid, check_derivation

P, Q, R = V("P"), V("Q"), V("R")
QUOTED = {"(g) lines": 7, "(m) lines": 5, "(n) lines": 5, "(o) lines": 7, "(l) constant": 3}

G = r"""
  \hypo {1} {\neg Q}
  \hypo {2} {P \to (Q \wedge R)}
  \open
  \hypo {3} {P}
  \have {4} {Q \wedge R} \ie{2,3}
  \have {5} {Q} \ae{4}
  \have {6} {\bot} \ne{5,1}
  \close
  \have {7} {\neg P} \ni{3-6}
"""
err, n = check_derivation(G)
assert err == [] and n == QUOTED["(g) lines"], err
assert classically_valid([Not(Q), Imp(P, And(Q, R))], Not(P))

J = r"""
  \hypo {1} {P \to Q}
  \hypo {2} {\neg Q}
  \open
  \hypo {3} {P}
  \have {4} {Q} \ie{1,3}
  \have {5} {\bot} \ne{4,2}
  \close
  \have {6} {\neg P} \ni{3-5}
  \have {7} {Q} \ie{1,3}
"""
err, n = check_derivation(J)
assert len(err) == 1 and "line 7" in err[0][1], err

c = QUOTED["(l) constant"]
for k in range(-400, 401):
    for d in (1, 2, 3, 7):
        x = F(k, d)
        assert x * x + 4 - 2 * x == (x - 1) ** 2 + c
        if x * x + 4 == 2 * x:            # never happens, but the step is the identity
            assert (x - 1) ** 2 == -c
assert -c < 0

M = r"""
  \hypo {1} {\neg P}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {P} \ae{2}
  \have {4} {\bot} \ne{3,1}
  \close
  \have {5} {\neg(P \wedge Q)} \ni{2-4}
"""
N = r"""
  \hypo {1} {P \to \neg P}
  \open
  \hypo {2} {P}
  \have {3} {\neg P} \ie{1,2}
  \have {4} {\bot} \ne{2,3}
  \close
  \have {5} {\neg P} \ni{2-4}
"""
O = r"""
  \hypo {1} {P \wedge \neg Q}
  \open
  \hypo {2} {P \to Q}
  \have {3} {P} \ae{1}
  \have {4} {Q} \ie{2,3}
  \have {5} {\neg Q} \ae{1}
  \have {6} {\bot} \ne{4,5}
  \close
  \have {7} {\neg(P \to Q)} \ni{2-6}
"""
for body, key in ((M, "(m) lines"), (N, "(n) lines"), (O, "(o) lines")):
    err, n = check_derivation(body)
    assert err == [] and n == QUOTED[key], (key, err)
print("exr-negation-and-contradiction-a2: all quoted values check")
