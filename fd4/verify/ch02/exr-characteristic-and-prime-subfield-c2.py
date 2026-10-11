"""exr-characteristic-and-prime-subfield-c2: in F3, 4.1 = 1 = 1.1 and 4.1 != 0;
7.1 = 1 = 1.1 gives m - k = 6, while char F3 = 3."""
QUOTED = {"m": 4, "k": 1, "m2": 7, "diff": 6, "char": 3}
p = 3
assert QUOTED["m"] % p == QUOTED["k"] % p == 1 and QUOTED["m"] % p != 0
assert QUOTED["m2"] % p == 1 and QUOTED["m2"] - 1 == QUOTED["diff"]
assert min(n for n in range(1, 10) if n % p == 0) == QUOTED["char"]
print("ok")
