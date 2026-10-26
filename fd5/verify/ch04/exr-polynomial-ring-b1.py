"""exr-polynomial-ring-b1 (Section 4.2): (2x^3 - x + 4)(-2x^3 + x^2 + 3) over Z and F_2."""
QUOTED = {
    "p": [4, -1, 0, 2],
    "q": [3, 0, 1, -2],
    "Z": [12, -3, 4, -3, 2, 2, -4],     # constant term first
    "F2": [0, 1, 0, 1],                  # x^3 + x
}


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


prod = mul(QUOTED["p"], QUOTED["q"])
assert prod == QUOTED["Z"]
p2 = [c % 2 for c in QUOTED["p"]]
q2 = [c % 2 for c in QUOTED["q"]]
assert p2 == [0, 1, 0, 0] and q2 == [1, 0, 1, 0]          # x and x^2 + 1
prod2 = [c % 2 for c in mul(p2, q2)]
assert prod2[:4] == QUOTED["F2"] and not any(prod2[4:])
assert [c % 2 for c in prod][:4] == QUOTED["F2"] and not any(c % 2 for c in prod[4:])
print("exr-polynomial-ring-b1: ok")
