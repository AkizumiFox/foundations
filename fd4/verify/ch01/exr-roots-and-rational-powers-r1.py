"""exr-roots-and-rational-powers-r1 (05): 1/(sqrt k + sqrt(k+1)) = sqrt(k+1) - sqrt k; sum = sqrt(n+1) - 1.
Exact check of the identity (x - y)(x + y) = x^2 - y^2 = 1 with x^2 = k + 1, y^2 = k, and a float check of the sum."""
import math

QUOTED = {}
for k in range(1, 1000):
    assert (k + 1) - k == 1
for n in range(1, 200):
    s = sum(1 / (math.sqrt(j) + math.sqrt(j + 1)) for j in range(1, n + 1))
    assert abs(s - (math.sqrt(n + 1) - 1)) < 1e-9
print("ok")
