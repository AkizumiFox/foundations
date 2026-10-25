"""exr-equivalence-relations-b2: in Z/7, [3]+[5] = [1], [3][5] = [1]; 729 = 104*7 + 1,
81 = 11*7 + 4, 100 = 6*16 + 4, 3^100 mod 7 = 4."""

QUOTED = {"sum": 1, "prod": 1, "729": (104, 1), "81": (11, 4), "answer": 4}

assert (3 + 5) % 7 == QUOTED["sum"] and (3 * 5) % 7 == QUOTED["prod"]
assert 3 ** 6 == 729 and divmod(729, 7) == QUOTED["729"]
assert 3 ** 4 == 81 and divmod(81, 7) == QUOTED["81"]
assert 6 * 16 + 4 == 100 and (3 ** 6) ** 16 * 3 ** 4 == 3 ** 100
assert pow(3, 100, 7) == QUOTED["answer"] == (3 ** 100) % 7
print("exr-equivalence-relations-b2: all quoted values check")
