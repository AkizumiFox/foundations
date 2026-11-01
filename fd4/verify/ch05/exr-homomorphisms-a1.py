"""exr-homomorphisms-a1 (b): kernel of a -> ([a]_6, [a]_4) is 12Z; 4 does not divide 6, 4 | 12."""
QUOTED = {"d": 12}
ker = [a for a in range(-100, 101) if a % 6 == 0 and a % 4 == 0]
assert ker == [a for a in range(-100, 101) if a % QUOTED["d"] == 0]
assert 6 % 4 != 0 and 12 % 4 == 0
print("ok")
