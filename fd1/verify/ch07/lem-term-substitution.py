"""lem-term-substitution (Section 4.12): the capture example in (Z, >) (window) and the Quick
check: phi = forall z (x < z -> y < z), t = y + 1, l(x) = 3, l(y) = 5, a = 6; both sides true;
phi false under l itself, at z = 4. The instance before the lemma: phi = y < x, t = y + 1,
l(y) = 3; value of t is 4, and both 3 < 4 sides hold."""
QUOTED = {"a": 6, "failing z": 4, "instance value": 4}
Z = range(-300, 301)
# capture: exists y (y > y + 1) false; exists y (y > a) true for every a (witness a + 1)
assert not any(y > y + 1 for y in Z)
assert all(a + 1 > a for a in range(-200, 201))
lx, ly = 3, 5
a = ly + 1
assert a == QUOTED["a"]
rhs = all((not (a < z)) or (ly < z) for z in Z)          # l[x -> 6] |= phi
lhs = all((not (ly + 1 < z)) or (ly < z) for z in Z)     # l |= phi[t/x]
assert rhs and lhs
bad = [z for z in Z if (lx < z) and not (ly < z)]
assert bad == [4, 5] and QUOTED["failing z"] in bad
# instance before the lemma: phi = (y < x), t = y + 1, l(y) = 3
iy = 3
tval = iy + 1
assert tval == QUOTED["instance value"]
assert iy < iy + 1                 # l |= phi[t/x], i.e. y < y + 1
assert iy < tval                   # l[x -> 4] |= y < x
# renaming instance: exists y (y > x) and exists z (z > x) hold at every x (witness x + 1)
assert all(any(w > x for w in range(x, x + 2)) for x in range(-200, 201))
print("lem-term-substitution: all quoted values check")
