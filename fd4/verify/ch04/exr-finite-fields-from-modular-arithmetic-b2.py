"""exr-finite-fields-from-modular-arithmetic-b2: [3][3] = [0] in Z/9Z; 5 prime; [1] = [0] in Z/1Z;
91 = 7 * 13, [7][13] = [0] in Z/91Z."""
QUOTED = {"[3][3] = [9] = [0]": (3, 9), "prime": 5, "91 = 7 * 13": (91, 7, 13),
          "fields among Z/9Z, F_5, Z/1Z, Z/91Z": (False, True, False, False)}
assert 3 * 3 % 9 == 0 and 3 % 9
assert all(5 % d for d in range(2, 5))
assert 1 % 1 == 0
assert 91 == 7 * 13 and 7 * 13 % 91 == 0
def is_field(n):
    return n >= 2 and all(any(a * x % n == 1 for x in range(n)) for a in range(1, n))
assert [is_field(n) for n in (9, 5, 1, 91)] == [False, True, False, False]
assert 3 * 3 == 9 and 9 % 9 == 0
n, r, s = QUOTED["91 = 7 * 13"]
assert n == r * s and 1 < r < n and r * s % n == 0
assert tuple(is_field(m) for m in (9, QUOTED["prime"], 1, 91)) == QUOTED["fields among Z/9Z, F_5, Z/1Z, Z/91Z"]
print("ok")
