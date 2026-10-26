"""exr-peano-properties-b2: (N, 0, S o S) satisfies (P3), (P4), not (P5) (truncated check).
Natural numbers modelled by ints, S(n) = n + 1, so S(0) = 1."""
QUOTED = {"missing": 1}   # the element S(0) of the hint
N = 50
d = lambda n: n + 2
assert all(d(n) != 0 for n in range(N))
assert len({d(n) for n in range(N)}) == N
A = {n for n in range(N + 2) if n != QUOTED["missing"]}
assert 0 in A and all(d(n) in A for n in A if n < N)
assert QUOTED["missing"] not in A
# the d-closure of {0} is every second number: 0, S(S(0)), S^4(0), ...
C, x = set(), 0
while x < N:
    C.add(x); x = d(x)
assert C == set(range(0, N, 2))
print("ok")
