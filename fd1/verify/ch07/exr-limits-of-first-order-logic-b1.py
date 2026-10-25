"""exr-limits-of-first-order-logic-b1 (Section 7.6): the pairing structures of sizes 2-8 (even)
satisfy (Refl), (Sym), (Trans) and the exactly-two-per-class sentence; odd sizes 1-7 fail it;
Z with floor(x/2) = floor(y/2) satisfies it on a window."""
import sys
sys.path.insert(0, "verify/ch07")
from _fo_models import structure, sat, P, ALL, EX, NOT, AND, OR, IMP

eq = lambda a, b: ("eq", a, b)
R = lambda a, b: P("R", a, b)
refl = ALL("x", R("x", "x"))
sym = ALL("x", ALL("y", IMP(R("x", "y"), R("y", "x"))))
trans = ALL("x", ALL("y", ALL("z", IMP(AND(R("x", "y"), R("y", "z")), R("x", "z")))))
pair = ALL("x", EX("y", AND(NOT(eq("x", "y")), AND(R("x", "y"),
        ALL("z", IMP(R("x", "z"), OR(eq("z", "x"), eq("z", "y"))))))))
for n in range(1, 9):
    D = list(range(n))
    rel = {(x, y) for x in D for y in D if x // 2 == y // 2}
    M = structure(D, pred={"R": rel})
    assert all(sat(f, M, {}) for f in (refl, sym, trans))
    assert sat(pair, M, {}) == (n % 2 == 0)
W = range(-20, 20)
for x in W:
    cls = [y for y in range(-25, 25) if x // 2 == y // 2]
    assert len(cls) == 2 and x in cls
print("exr-limits-of-first-order-logic-b1: all quoted values check")
