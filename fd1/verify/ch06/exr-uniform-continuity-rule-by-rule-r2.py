"""exr-uniform-continuity-rule-by-rule-r2 (Section 6.4): P <-> not Q, Q <-> not R, R <-> not P
have no satisfying row; the R3 skeleton p and (q or r) |= (p and q) or (p and r)."""
from _tt import entails, satisfiable
assert not satisfiable("PQR", [lambda v: v["P"] == (not v["Q"]), lambda v: v["Q"] == (not v["R"]),
                               lambda v: v["R"] == (not v["P"])])
assert entails("pqr", [lambda v: v["p"] and (v["q"] or v["r"])],
               lambda v: (v["p"] and v["q"]) or (v["p"] and v["r"]))
print("exr-uniform-continuity-rule-by-rule-r2: all quoted values check")
