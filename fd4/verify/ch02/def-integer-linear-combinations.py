"""def-integer-linear-combinations examples (02-gcd-and-bezout), the coin hook and the
coprime instances after def-coprime-integers / cor-coprime-iff-combination:
6 = 12*(-3) + 42*1 = 42 - 3*12, 30 = 42 - 12, 1 = 2*(-1) + 3*1; non-zero N-combinations of 12, 42 are >= 12."""
QUOTED = {"six": (-3, 1), "thirty": (-1, 1), "one": (-1, 1)}
x, y = QUOTED["six"]; assert 12 * x + 42 * y == 6 == 42 - 3 * 12
x, y = QUOTED["thirty"]; assert 12 * x + 42 * y == 30
x, y = QUOTED["one"]; assert 2 * x + 3 * y == 1
# every integer combination of 12, 42 is a multiple of 6, and every multiple of 6 in a range is reached
combos = {12 * x + 42 * y for x in range(-40, 41) for y in range(-40, 41)}
assert all(c % 6 == 0 for c in combos)
assert all(m in combos for m in range(-300, 301, 6))
nat = {12 * x + 42 * y for x in range(0, 30) for y in range(0, 30)}
assert min(c for c in nat if c != 0) == 12 and 6 not in nat and min(nat) == 0
print("ok")
