"""exr-peano-properties-b2: (omega, 0, S o S) satisfies (P3), (P4), not (P5) (truncated check)."""
QUOTED = {"missing": 1}
N = 50
d = lambda n: n + 2
assert all(d(n) != 0 for n in range(N))
assert len({d(n) for n in range(N)}) == N
A = {n for n in range(N + 2) if n != QUOTED["missing"]}
assert 0 in A and all(d(n) in A for n in A if n < N)
assert QUOTED["missing"] not in A
# the d-closure of {0} is the even numbers
C, x = set(), 0
while x < N:
    C.add(x); x = d(x)
assert C == {n for n in range(N) if n % 2 == 0}
print("ok")
