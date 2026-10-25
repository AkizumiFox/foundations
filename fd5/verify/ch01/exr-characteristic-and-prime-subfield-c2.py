"""exr-characteristic-and-prime-subfield-c2: in F3, 7.1 = 1 = 1.1 gives m - k = 6,
while char F3 = 3."""
QUOTED = {"m": 7, "k": 1, "diff": 6, "char": 3}
p = 3
assert QUOTED["m"] % p == QUOTED["k"] % p == 1
assert QUOTED["m"] - QUOTED["k"] == QUOTED["diff"] and QUOTED["diff"] % p == 0
assert min(n for n in range(1, 10) if n % p == 0) == QUOTED["char"] < QUOTED["diff"]
print("ok")
