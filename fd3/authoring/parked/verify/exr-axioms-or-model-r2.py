"""exr-axioms-or-model-r2: in Z/5Z, 5 * [1] = [0], every non-zero class has an inverse
(so it is a field, as 5 is prime), and n * 1 = 0 for n = 5 rules out any order:
n * 1 > 0 for n >= 1 in an ordered field. Also: no subset P of Z/5Z satisfies (P1)-(P2)."""
from itertools import combinations
QUOTED = {"n": 5}
n = QUOTED["n"]
assert sum(1 for _ in range(n)) % n == 0                      # 5 * [1] = [0]
for a in range(1, n):
    assert any(a * b % n == 1 for b in range(1, n))          # a field
# brute force: no positive set P (closed under + and *, trichotomy) exists
found = False
for k in range(n + 1):
    for P in combinations(range(n), k):
        P = set(P)
        if 0 in P:
            continue
        if any((a + b) % n not in P or a * b % n not in P for a in P for b in P):
            continue
        if all((x in P) != ((-x) % n in P) for x in range(1, n)):
            found = True
assert not found
print("ok")
