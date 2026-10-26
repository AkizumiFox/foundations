"""exm-elimination-f5: over F_5, 2x + y = 3, 3x + 2y = 4: inverses 2^{-1} = 3, 3^{-1} = 2,
4^{-1} = 4; x + 3y = 4; (2 - 9)y = 4 - 12, 3y = 2; y = 4, x = 4 - 12 = -8 = 2; ad - bc = 1;
formula x = 2, y = -1 = 4; checks 8 = 3, 14 = 4.
Quick check after it: x^2 = 1 in F_11 iff x in {1, 10}; 100 = 9*11 + 1.
Warning after it: in Z/6Z, [2]x in {[0],[2],[4]}; [2]x = [1] none; [2]x = [4] for x = [2], [5]."""
p = 5
QUOTED = {"inv": {1: 1, 2: 3, 3: 2, 4: 4}, "sol": (2, 4), "det": 1}
for a, b in QUOTED["inv"].items():
    assert a * b % p == 1
assert [(3 * 2) % p, (3 * 1) % p, (3 * 3) % p] == [1, 3, 4]
assert (2 - 9, 4 - 12) == (-7, -8) and -7 % p == 3 and -8 % p == 2
assert 2 * 3 % p == 1 and 2 * 2 % p == 4  # y = 3^{-1} * 2 = 2 * 2 = 4
y = 4
assert (4 - 3 * y) == -8 and -8 % p == 2
a, b, c, d, e, f = 2, 1, 3, 2, 3, 4
assert a * d - b * c == QUOTED["det"]
assert (e * d - b * f, a * f - c * e) == (2, -1) and -1 % p == 4
x, y = QUOTED["sol"]
assert (2 * x + y, 3 * x + 2 * y) == (8, 14) and 8 % p == 3 and 14 % p == 4
sols = [(u, v) for u in range(p) for v in range(p)
        if (2 * u + v - 3) % p == 0 and (3 * u + 2 * v - 4) % p == 0]
assert sols == [QUOTED["sol"]]
assert [x for x in range(11) if x * x % 11 == 1] == [1, 10] and 100 == 9 * 11 + 1
assert sorted({2 * x % 6 for x in range(6)}) == [0, 2, 4]
assert [x for x in range(6) if 2 * x % 6 == 1] == []
assert [x for x in range(6) if 2 * x % 6 == 4] == [2, 5] and 10 - 4 == 6
print("ok")
