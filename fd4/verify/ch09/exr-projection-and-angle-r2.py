"""exr-projection-and-angle-r2: the kernel witnesses a2 e1 - a1 e2 (a1 != 0) and e1 (a1 = 0)."""
import random
random.seed(4)
QUOTED = {"witness": True}
dot = lambda a, b: sum(i * j for i, j in zip(a, b))
for _ in range(500):
    n = random.randint(2, 5)
    a = [random.randint(-5, 5) for _ in range(n)]
    if all(c == 0 for c in a):
        continue
    v = [a[1], -a[0]] + [0] * (n - 2) if a[0] != 0 else [1] + [0] * (n - 1)
    assert dot(a, v) == 0 and any(v)
print("ok")
