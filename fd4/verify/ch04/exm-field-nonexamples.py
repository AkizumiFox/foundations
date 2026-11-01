"""exm-field-nonexamples: (i)/(ii) 2x = 1 has no integer solution (2x even); (iv) in Z/6Z,
[2][3] = [6] = [0], 6 divides neither 2 nor 3, and [2] has no inverse."""
QUOTED = {"prod": 6}
assert all(2 * x != 1 for x in range(-1000, 1001))
assert 2 * 3 == QUOTED["prod"] and QUOTED["prod"] % 6 == 0
assert 2 % 6 != 0 and 3 % 6 != 0
assert all(2 * u % 6 != 1 for u in range(6))
# Z/6Z satisfies the ring clauses: spot-check distributivity and associativity on all triples
for a in range(6):
    for b in range(6):
        for c in range(6):
            assert a * (b + c) % 6 == (a * b + a * c) % 6
            assert (a * b) * c % 6 == a * (b * c) % 6
print("ok")
