"""exr-quantifier-laws-a1: (d) the instance x * x = 2 has a real solution (so line 9 of the
derivation is true over R, though no line names it); (e) over R, forall e > 0 (e > 0) is true
and exists e <= 0 not(e > 0) is true with the witness e = 0."""
import math

QUOTED = {"square in (d)": 2, "witness in (e)": 0}
r = math.sqrt(QUOTED["square in (d)"])
assert abs(r * r - 2) < 1e-12
e = QUOTED["witness in (e)"]
assert e <= 0 and not (e > 0)
assert all(t > 0 for t in [1e-9, 0.5, 3.0])     # forall e > 0 (e > 0): each instance holds
print("exr-quantifier-laws-a1: all quoted values check")
