"""exm-angles-computed, the Quick checks of the cosine subsection and the warning: exact cosines.
A cosine c = <x,y>/sqrt(N) is checked through its sign and c^2 = <x,y>^2/N."""
from fractions import Fraction as Fr
QUOTED = {
    "a": ("1/sqrt2", 1, Fr(1, 2)),          # (label, sign, square)
    "b": (Fr(4, 9), 1, Fr(16, 81)),
    "body_edge": ("1/sqrt3", 1, Fr(1, 3)),
    "body_body": (Fr(1, 3), 1, Fr(1, 9)),
    "body_face": ("sqrt6/3", 1, Fr(6, 9)),
    "weird": (1, -1, 0),
    "check": -1,
}
dot = lambda a, b: sum(Fr(i) * Fr(j) for i, j in zip(a, b))
def cos_sq(x, y):
    d = dot(x, y); s = (d > 0) - (d < 0)
    return s, d * d / (dot(x, x) * dot(y, y))
assert cos_sq((1, 0), (1, 1)) == QUOTED["a"][1:]
assert cos_sq((1, 2, 2), (2, -1, 2)) == QUOTED["b"][1:] and dot((1, 2, 2), (2, -1, 2)) / 9 == QUOTED["b"][0]
assert cos_sq((1, 1, 1), (1, 0, 0)) == QUOTED["body_edge"][1:]
assert cos_sq((1, 1, 1), (1, 1, -1)) == QUOTED["body_body"][1:] and dot((1, 1, 1), (1, 1, -1)) / 3 == QUOTED["body_body"][0]
assert cos_sq((1, 1, 1), (1, 1, 0)) == QUOTED["body_face"][1:]
assert Fr(2) ** 2 / 6 == Fr(6, 9)               # (2/sqrt6)^2 = (sqrt6/3)^2
assert tuple(a - b for a, b in zip((1, 1, 0), (0, 0, 1))) == (1, 1, -1)
x = (1, 1, 0)
vals = []
for y in (x, (-1, -1, 0), (1, -1, 0)):
    s, sq = cos_sq(x, y); vals.append(s if sq in (0, 1) else None)
assert tuple(vals) == QUOTED["weird"]
assert cos_sq((1, 1), (-1, -1)) == (QUOTED["check"], 1)
# warning: 4/sqrt2 = 2 sqrt2 (square 8), and -2 sqrt2 for (-1,-1)
assert dot((3, 1), (1, 1)) ** 2 / 2 == 8 and dot((3, 1), (-1, -1)) == -4
print("ok")
