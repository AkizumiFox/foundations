"""exm-frobenius-computations: (i) 3^100 = 4 in F7 (100 = 16*6 + 4, 81 = 11*7 + 4);
(ii) 101 prime, remainders of 101 mod 2..10, 2^100 = 1 in F101; (iii) 31 prime (remainders mod
2..5), 7^2 = 18, 7^4 = 14, 7^8 = 10, 7^16 = 7, 70 = 8, 98 = 5, 40 = 9, 7^29 = 9; Euclid
31 = 4*7 + 3, 7 = 2*3 + 1, 1 = 9*7 - 2*31; 7*9 = 63 = 2*31 + 1."""
QUOTED = {
    "i": 4, "100": (16, 4), "81": (11, 4),
    "rem101": [1, 2, 1, 1, 5, 3, 5, 2, 1], "rem31": [1, 1, 3, 1],
    "sq": {2: 18, 4: 14, 8: 10, 16: 7}, "partial": (70, 8, 98, 5, 40), "inv": 9,
}
assert pow(3, 100, 7) == QUOTED["i"] and pow(3, 6, 7) == 1
q, r = QUOTED["100"]
assert 100 == q * 6 + r and 3 ** 4 == 81
q, r = QUOTED["81"]
assert 81 == q * 7 + r == 11 * 7 + 4
assert [101 % d for d in range(2, 11)] == QUOTED["rem101"] and 10 * 10 <= 101 < 11 * 11
assert all(101 % d for d in range(2, 101)) and pow(2, 100, 101) == 1
assert [31 % d for d in range(2, 6)] == QUOTED["rem31"] and all(31 % d for d in range(2, 31))
for e, v in QUOTED["sq"].items():
    assert pow(7, e, 31) == v
a, b, c, d, e = QUOTED["partial"]
assert 7 * 10 == a and a % 31 == b and 14 * 7 == c and c % 31 == d and b * d == e and e % 31 == QUOTED["inv"]
assert 16 + 8 + 4 + 1 == 29 and pow(7, 29, 31) == QUOTED["inv"]
assert 31 == 4 * 7 + 3 and 7 == 2 * 3 + 1 and 9 * 7 - 2 * 31 == 1
assert 7 * 9 == 63 == 2 * 31 + 1
print("ok")
