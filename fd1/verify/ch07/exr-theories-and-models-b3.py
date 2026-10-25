"""exr-theories-and-models-b3 (Section 7.4): the theorem forall x (x.x = x -> x = e) holds in
the triangle group and in addition modulo n for n <= 6; ({0,1}; ., 1) satisfies (Assoc) and
(Id) and fails the theorem at 0. (The derivation is checked by tools/check_fitch.py.)"""
import itertools
import runpy
import sys

QUOTED = {"fail_at": 0, "identity": 1}
sys.argv = ["x"]
tg = runpy.run_path("verify/ch07/exm-triangle-group.py")
mul, NAMES = tg["mul"], tg["NAMES"]
assert all(mul(x, x) != x or x == "e" for x in NAMES)
for n in range(1, 7):
    assert all((x + x) % n != x or x == 0 for x in range(n))
D = [0, 1]
for x, y, z in itertools.product(D, repeat=3):
    assert (x * y) * z == x * (y * z)
assert all(x * QUOTED["identity"] == x == QUOTED["identity"] * x for x in D)
x0 = QUOTED["fail_at"]
assert x0 * x0 == x0 and x0 != QUOTED["identity"]
print("exr-theories-and-models-b3: all quoted values check")
