"""exr-models-b1 (Section 4.11): the three counter-models, on D = {a, b}; (iii) needs l(x) = b,
and l(x) = a is not a counter-model."""
import sys
sys.path.insert(0, "verify/ch04")
from _fo_models import structure, sat, is_counter_model, P, ALL, EX, IMP

QUOTED = {}
Px, Qx = P("P", "x"), P("Q", "x")
M = structure(["a", "b"], pred={"P": {("a",)}})
assert is_counter_model([EX("x", Px)], ALL("x", Px), M)
M2 = structure(["a", "b"], pred={"P": {("a",)}, "Q": {("a",)}})
assert is_counter_model([ALL("x", IMP(Px, Qx))], IMP(EX("x", Px), ALL("x", Qx)), M2)
f = IMP(EX("x", Px), Px)
assert is_counter_model([], f, M, {"x": "b"})
assert sat(f, M, {"x": "a"})
print("exr-models-b1: all quoted values check")
