"""def-field-fp and the quick check after it: 3 * 5 = 15 = 2*7 + 1, so 3^{-1} = 5 in F_7;
the products 3x for x = 1..5 are 3, 6, 9, 12, 15 with remainders 3, 6, 2, 5, 1 mod 7;
-1 = p - 1 in F_p; 1 + (p - 1) = 0 in F_p; F_2, F_3, F_5, F_7, F_11 fields, Z/4Z, Z/6Z, Z/9Z not."""
QUOTED = {"products": [3, 6, 9, 12, 15], "rems": [3, 6, 2, 5, 1], "inv": 5}
assert [3 * x for x in range(1, 6)] == QUOTED["products"]
assert [v % 7 for v in QUOTED["products"]] == QUOTED["rems"]
assert 15 == 2 * 7 + 1 and 3 * QUOTED["inv"] % 7 == 1
assert [x for x in range(7) if 3 * x % 7 == 1] == [QUOTED["inv"]]
def is_field(n):
    return n >= 2 and all(any(a * x % n == 1 for x in range(n)) for a in range(1, n))
assert all(is_field(p) for p in (2, 3, 5, 7, 11)) and not any(is_field(n) for n in (4, 6, 9))
for p in (2, 3, 5, 7, 11, 13):
    assert (-1) % p == p - 1 and (1 + (p - 1)) % p == 0
    assert [x for x in range(p) if x * x % p == 1] == sorted({1, p - 1})
print("ok")
