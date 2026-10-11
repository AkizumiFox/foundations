"""exr-frobenius-and-fermat-b1: in F13, 5^12 = 1, 38 = 3*12 + 2, 5^38 = 25 = 12; 5^2 = -1,
5^10 = -1, 5^11 = -5 = 8; 5*8 = 40 = 3*13 + 1; 13 prime."""
QUOTED = {"pow38": 12, "inv": 8}
assert all(13 % d for d in range(2, 13))
assert pow(5, 12, 13) == 1 and 38 == 3 * 12 + 2 and 25 % 13 == 12
assert pow(5, 38, 13) == QUOTED["pow38"]
assert pow(5, 2, 13) == 12 and pow(5, 10, 13) == 12 and pow(5, 11, 13) == QUOTED["inv"] == (-5) % 13
assert 5 * 8 == 40 == 3 * 13 + 1
print("ok")
