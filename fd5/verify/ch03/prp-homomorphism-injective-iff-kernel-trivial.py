"""prp-homomorphism-injective-iff-kernel-trivial, check after it: [3]^6 = [729] = [1], 729 = 104*7 + 1."""
QUOTED = {"p": 729, "q": 104}
assert 3 ** 6 == QUOTED["p"] == QUOTED["q"] * 7 + 1
assert pow(3, 0, 7) == pow(3, 6, 7) == 1
print("ok")
