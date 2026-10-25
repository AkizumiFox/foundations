"""prp-divides-partial-order: antisymmetry on N (0..80), failure on Z at 2, -2."""
QUOTED = {}
d = lambda a, b: (b == 0) if a == 0 else (b % a == 0)
N = range(0, 81)
assert all(a == b for a in N for b in N if d(a, b) and d(b, a))
assert d(2, -2) and d(-2, 2)
assert all(d(a, 0) and d(1, a) for a in N)
assert not any(d(0, b) for b in range(1, 81))
print("ok")
