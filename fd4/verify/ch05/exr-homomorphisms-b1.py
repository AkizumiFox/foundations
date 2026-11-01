"""exr-homomorphisms-b1: homomorphisms Z -> Z/6Z are k -> k.[c]; least positive k with 6 | kc for
c = 0..5 is 1, 6, 3, 2, 3, 6; kernels Z, 6Z, 3Z, 2Z, 3Z, 6Z."""
QUOTED = {"least": [1, 6, 3, 2, 3, 6]}
for c in range(6):
    d = min(k for k in range(1, 100) if (k * c) % 6 == 0)
    assert d == QUOTED["least"][c]
    ker = [k for k in range(-60, 61) if (k * c) % 6 == 0]
    assert ker == [k for k in range(-60, 61) if k % d == 0]
    # additivity of k -> kc mod 6
    assert all(((k + l) * c) % 6 == (k * c + l * c) % 6 for k in range(-10, 10) for l in range(-10, 10))
assert [4 * k % 6 for k in (1, 2, 3)] == [4, 2, 0]
assert [5 * k % 6 for k in range(1, 7)] == [5, 4, 3, 2, 1, 0]
print("ok")
