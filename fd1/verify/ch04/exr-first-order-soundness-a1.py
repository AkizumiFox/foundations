"""exr-first-order-soundness-a1 (Section 4.12): in D = {a, b}, P = {a}, l(x0) = b the premise
exists x P(x) holds and P(x0) fails; R(x0, y0) on Z with R read as < under (1, 2) and (2, 1)."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, is_counter_model, P, EX

QUOTED = {}
M = structure(["a", "b"], pred={"P": {("a",)}})
assert is_counter_model([EX("x", P("P", "x"))], P("P", "x0"), M, {"x0": "b"})
assert sat(P("P", "x0"), M, {"x0": "a"})
assert (1 < 2) and not (2 < 1)
print("exr-first-order-soundness-a1: all quoted values check")
