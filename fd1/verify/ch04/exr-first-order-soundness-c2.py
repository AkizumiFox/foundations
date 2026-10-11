"""exr-first-order-soundness-c2 (Section 4.12), and the (Z, <=) facts of B1: in (Z, <=), for every x
the integer x + 1 is not <= x (premise true); <= is reflexive (conclusion false); forall y (y <= y)
true and 'there is a least integer' false (window)."""
QUOTED = {}
Z = range(-300, 301)
assert all(not (x + 1 <= x) for x in Z)
assert all(y <= y for y in Z)
# no least integer: every candidate m has m - 1 < m
assert all(m - 1 < m for m in Z)
# after renaming: not forall z (z <= y) true under every assignment (witness y + 1)
assert all(not ((y + 1) <= y) for y in Z)
print("exr-first-order-soundness-c2: all quoted values check")
