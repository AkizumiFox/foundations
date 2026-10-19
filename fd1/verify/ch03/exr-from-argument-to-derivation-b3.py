"""exr-from-argument-to-derivation-b3 (Ch 3 s03): every derive verdict valid; the breaks at n = 2, 15, 25."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403

QUOTED = {"breaks": {11: 2, 13: 15, 15: 25}}
P, Q, R = V("P"), V("Q"), V("R")
E, T, G = V("E"), V("T"), V("G")
F1, F2, F3 = Imp(And(P, E), Not(G)), Imp(And(P, T), Not(G)), Imp(And(E, T), Not(P))
derive = {
    1: ([Not(Or(P, Q))], Imp(P, R)),
    2: ([Or(P, Q), Imp(P, R), Not(R)], And(Q, Not(P))),
    3: ([Not(And(P, Not(Q)))], Imp(P, Q)),
    4: ([Imp(Or(P, Q), R)], Imp(Not(R), And(Not(P), Not(Q)))),
    5: ([Imp(Not(P), Q), Not(Q)], And(P, Or(Not(Q), R))),
    6: ([And(E, T), F3], And(Not(P), Not(And(P, G)))),
    7: ([Or(And(P, Not(G)), Not(E))], Imp(E, Not(G))),
    8: ([And(P, T), F2, F3], And(Not(G), Not(E))),
    9: ([P, Or(Not(T), Not(G)), T], Not(G)),
    10: ([F1], Imp(G, Not(And(P, E)))),
    12: ([And(P, E), F1], Not(G)),
    14: ([Not(E)], Not(And(P, E))),
}
for k, (prem, concl) in derive.items():
    assert classically_valid(prem, concl), k
assert classically_valid([Or(Not(T), Not(G)), T], Not(G))   # 9 without P


def prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def val(n):
    return {"E": n % 2 == 0, "P": prime(n), "T": n % 3 == 0, "G": n > 10}


breaks = {11: ([And(E, Not(T))], Not(P)), 13: ([And(Not(E), G)], P), 15: ([Not(P)], Or(E, T))}
for k, (prem, concl) in breaks.items():
    v = val(QUOTED["breaks"][k])
    for f in prem + [F1, F2, F3, Not(concl)]:
        assert tv(f, v) is True, (k, f)
print("exr-from-argument-to-derivation-b3: ok")
