"""exr-polynomial-ring-c2 (Section 4.2): (1 - x)(1, 1, 1, ...) = 1, checked in positions 0..199."""
QUOTED = {"one_minus_x": [1, -1]}
K = 200
s = [1] * K
p = QUOTED["one_minus_x"] + [0] * (K - 2)
prod = [sum(p[i] * s[k - i] for i in range(k + 1)) for k in range(K)]
assert prod == [1] + [0] * (K - 1)
print("exr-polynomial-ring-c2: ok")
