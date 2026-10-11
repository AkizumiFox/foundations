"""exr-polynomial-ring-a1 (Section 4.2): (2x)(3x^2)(x) in Z[x], both groupings give 6x^4."""
QUOTED = {"coefficient": 6, "exponent": 4, "inner_left": 3, "inner_right": 3}


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


two_x, three_x2, x = [0, 2], [0, 0, 3], [0, 1]
left = mul(mul(two_x, three_x2), x)
right = mul(two_x, mul(three_x2, x))
expected = [0] * QUOTED["exponent"] + [QUOTED["coefficient"]]
assert left == right == expected
assert 1 + 2 == QUOTED["inner_left"] and 2 + 1 == QUOTED["inner_right"]
print("exr-polynomial-ring-a1: ok")
