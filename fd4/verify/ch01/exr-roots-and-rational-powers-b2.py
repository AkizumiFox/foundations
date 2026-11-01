"""exr-roots-and-rational-powers-b2 (05): 3^10 = 59049, 2^15 = 32768, 5^6 = 15625; order 5^(1/5) < 2^(1/2) < 3^(1/3)."""
QUOTED = {"3^10": 59049, "2^15": 32768, "5^6": 15625}
assert 3 ** 10 == QUOTED["3^10"] and 2 ** 15 == QUOTED["2^15"] and 5 ** 6 == QUOTED["5^6"]
assert QUOTED["5^6"] < QUOTED["2^15"] < QUOTED["3^10"]
assert 5 ** 0.2 < 2 ** 0.5 < 3 ** (1 / 3)
print("ok")
