"""Quick check after prp-injection-gives-surjection (Section 4.4).

The inclusion iota: N -> Z; the left inverse g of the proof of
thm-left-inverse-iff-injective (b) with default value 0: g(n) = n for n >= 0,
g(n) = 0 for n < 0. Checked on a window of Z.
"""
import sys

QUOTED = {"default": 0}

def g(n):
    return n if n >= 0 else QUOTED["default"]

def iota(n):
    return n

W = range(-200, 201)
N = range(0, 201)
ok = True
# g o iota = id_N
ok &= all(g(iota(n)) == n for n in N)
# values of g lie in N
ok &= all(g(z) >= 0 for z in W)
# onto N (on the window): every n in N is a value
vals = {g(z) for z in W}
ok &= all(n in vals for n in N)
# g agrees with iota^{-1} on the image, default off it
ok &= all(g(z) == 0 for z in W if z < 0)
assert ok
print("ok")
sys.exit(0)
