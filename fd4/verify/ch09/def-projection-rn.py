"""def-projection-rn: the opening completed square, the examples after the definition, the 'why ||y||^2' remark, and the Quick check."""
from fractions import Fraction as Fr
import random

QUOTED = {
    "opening_poly": (2, -8, 10),          # (3-t)^2 + (1-t)^2 = 2t^2 - 8t + 10 = 2(t-2)^2 + 2
    "opening_proj": (2, 2),
    "e3_proj_of_(3,-1,2)": (0, 0, 2),
    "wrong_division_dot": (4, -4),        # 4 - 4*sqrt(2), as (rational, coefficient of sqrt 2)
    "check_(1,0)": (2, 0),
    "check_(2,0)": (2, 0),
}
dot = lambda a, b: sum(Fr(i) * Fr(j) for i, j in zip(a, b))
proj = lambda x, y: tuple(dot(x, y) / dot(y, y) * b for b in y)
for t in [Fr(k, 3) for k in range(-9, 10)]:
    a, b, c = QUOTED["opening_poly"]
    v = (3 - t) ** 2 + (1 - t) ** 2
    assert v == a * t * t + b * t + c == 2 * (t - 2) ** 2 + 2
assert proj((3, 1), (1, 1)) == QUOTED["opening_proj"]
assert dot((1, -1), (1, 1)) == 0
assert proj((3, -1, 2), (0, 0, 1)) == QUOTED["e3_proj_of_(3,-1,2)"]
# dividing by ||y|| = sqrt 2: coefficient c = 4/sqrt 2 = 2 sqrt 2; error (3 - c, 1 - c); <err, y> = 4 - 2c = 4 - 4 sqrt 2
r, s = QUOTED["wrong_division_dot"]
assert (r, s) == (3 + 1, -2 * 2) and s != 0          # 4 - 2*(2 sqrt 2), nonzero since sqrt 2 is irrational
assert Fr(4) ** 2 / 2 == 8                          # (4/sqrt 2)^2 = 8 = (2 sqrt 2)^2
assert proj((2, 3), (1, 0)) == QUOTED["check_(1,0)"]
assert proj((2, 3), (2, 0)) == QUOTED["check_(2,0)"]
random.seed(6)
for _ in range(300):
    x = tuple(random.randint(-9, 9) for _ in range(4)); y = tuple(random.randint(-9, 9) for _ in range(4))
    if dot(y, y) == 0:
        continue
    c = random.choice([-3, -1, 2, Fr(5, 2)])
    assert proj(x, y) == proj(x, tuple(c * b for b in y))
print("ok")
