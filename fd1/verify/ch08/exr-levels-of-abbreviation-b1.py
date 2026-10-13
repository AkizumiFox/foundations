"""exr-levels-of-abbreviation-b1: over N with R(x, y) as x <= y, the premise
exists x forall y (x <= y) holds with witness 0, and y <= y gives the one-line proof."""
QUOTED = {"witness": 0}
W = range(0, 500)
assert all(QUOTED["witness"] <= y for y in W)
assert all(y <= y for y in W)
# the witness from the premise does not depend on y: one x serves every y in the window
assert any(all(x <= y for y in W) for x in W)
print("exr-levels-of-abbreviation-b1: all quoted values check")
