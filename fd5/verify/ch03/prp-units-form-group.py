"""prp-units-form-group: the units of Z/8Z are [1], [3], [5], [7], each its own inverse;
the Quick check in (Z/7Z)^x: [3]^{-1} = [5], [3]^{-2} = [4]."""
QUOTED = {
    "units8": {1, 3, 5, 7},
    "inv3_mod7": 5,
    "inv3_sq_mod7": 4,
    "check_arith": [(15, 2, 1), (25, 3, 4), (36, 5, 1)],  # x = q*7 + r
}
units8 = {a for a in range(8) if any(a * b % 8 == 1 for b in range(8))}
assert units8 == QUOTED["units8"]
assert all(a * a % 8 == 1 for a in units8)
assert 9 % 8 == 1 and 25 % 8 == 1 and 49 % 8 == 1
inv = QUOTED["inv3_mod7"]
assert 3 * inv % 7 == 1
assert inv * inv % 7 == QUOTED["inv3_sq_mod7"]
assert (3 * 3) * QUOTED["inv3_sq_mod7"] % 7 == 1
for x, q, r in QUOTED["check_arith"]:
    assert x == q * 7 + r
assert 3 * 5 == 15 and 5 * 5 == 25 and 9 * 4 == 36
# zero divisors in Z/8Z for the non-units
for a in (0, 2, 4, 6):
    assert a not in units8
print("prp-units-form-group: ok")
