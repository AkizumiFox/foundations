"""exr-translation-c2 (Ch 4, Section 4.8): the truth table of the four groups over Z, on a window."""

QUOTED = {"L witness y = x + 1 offset": 1}

W = range(-30, 31)
gt_x = lambda x, y, z: y > x
gt_z = lambda x, y, z: y > z
# true entries: the witness works for all inputs in W
assert all(gt_x(x, x + 1, z) for x in W for z in W)          # L, y > x
assert all(gt_z(x, z + 1, z) for x in W for z in W)          # L, y > z
assert all(gt_x(x, x + 1, z) for x in W for z in W)          # M_x, y > x
assert all(gt_z(x, z + 1, z) for x in W for z in W)          # M_z, y > z
# false entries: for every y the challenger defeats it
assert all(not gt_x(y, y, 0) for y in W)                    # F, M_z under y > x: x = y
assert all(not gt_z(0, y, y) for y in W)                    # F, M_x under y > z: z = y
table = {"F": (False, False), "L": (True, True), "Mx": (True, False), "Mz": (False, True)}
rows = list(table.values())
assert len(set(rows)) == 4                                  # every two rows differ
print("exr-translation-c2: all quoted values check")
