"""exm-negation-and-contradiction-instances (Ch 2, Section 2.2): the gallery of not-I and the
Not-allowed block after the rule card.

(1) Each gallery row's new line is the negation of the whole assumption phi; the look-alike
P and R is not of the form not(...).
(2) The WRONG/RIGHT pair: WRONG fails tools/check_fitch.py at line 6 only; RIGHT checks clean.
(3) The WRONG list "not(Q or R) |- not P" breaks at x = 1 with P: x > 0, Q: x > 5, R: x < -5:
the premise is true and not P is false; the RIGHT sequent is classically valid."""
from fractions import Fraction
from _s05s06_logic import V, Not, And, Or, Imp, classically_valid, check_derivation

P, Q, R = V("P"), V("Q"), V("R")
QUOTED = {"x": 1}

# (1) gallery rows: (phi, new line)
ROWS = [(Or(P, Not(Q)), Not(Or(P, Not(Q)))),
        (Imp(Q, R), Not(Imp(Q, R))),
        (Not(And(P, R)), Not(Not(And(P, R))))]
for phi, new in ROWS:
    assert new == Not(phi)
assert And(P, R)[0] != "not"

# (2)
COMMON = r"""
  \hypo {1} {\neg(Q \vee R)}
  \open
  \hypo {2} {P \wedge Q}
  \have {3} {Q} \ae{2}
  \have {4} {Q \vee R} \oi{3}
  \have {5} {\bot} \ne{4,1}
  \close
"""
err, n = check_derivation(COMMON + r"  \have {6} {\neg P} \ni{2-5}")
assert len(err) == 1 and "line 6" in err[0][1], err
err, n = check_derivation(COMMON + r"  \have {6} {\neg(P \wedge Q)} \ni{2-5}")
assert err == [] and n == 6, err
assert classically_valid([Not(Or(Q, R))], Not(And(P, Q)))
assert not classically_valid([Not(Or(Q, R))], Not(P))

# (3)
x = Fraction(QUOTED["x"])
p, q, r = x > 0, x > 5, x < -5
assert (not (q or r)) and p          # premise true, not P false
print("exm-negation-and-contradiction-instances: checks")
