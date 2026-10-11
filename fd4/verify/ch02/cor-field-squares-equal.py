"""cor-field-squares-equal (remark): in Z/8Z, [3]^2 = [9] = [1]; [3] != [1], [3] != [-1] = [7],
since 8 divides neither 3 - 1 = 2 nor 3 - 7 = -4. Also: the squares-equal property holds in F_p
for small primes p (x^2 = y^2 iff x = y or x = -y)."""
QUOTED = {"n": 8, "a": 3, "sq": 9, "minus_one": 7, "diffs": (2, -4)}
n, a = QUOTED["n"], QUOTED["a"]
assert a * a == QUOTED["sq"] and QUOTED["sq"] % n == 1
assert (-1) % n == QUOTED["minus_one"]
assert (a - 1, a - 7) == QUOTED["diffs"]
assert all(d % n != 0 for d in QUOTED["diffs"])
# the units of Z/8Z all square to 1 (four square roots of 1)
assert [x for x in range(8) if x * x % 8 == 1] == [1, 3, 5, 7]
for p in [2, 3, 5, 7, 11, 13]:
    for x in range(p):
        for y in range(p):
            assert ((x * x - y * y) % p == 0) == ((x - y) % p == 0 or (x + y) % p == 0)
print("ok")
