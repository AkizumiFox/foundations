"""exr-predicates-and-quantifiers-b2 (Ch 4, Section 4.1): a predicate R(x, y) on N with forall-exists true and exists-forall false."""

QUOTED = {"partner of x for y > x": "x + 1", "defeating x for y > x": "y",
          "partner of x for y != x": "x + 1", "partner of x for y >= x": "x",
          "defeating x for y >= x": "y + 1", "y >= 1: partner of every x": 1}

N = range(0, 200)


def forall_exists(R, partner):
    return all(R(x, partner(x)) for x in N)


def no_universal_partner(R, defeat):
    return all(not R(defeat(y), y) for y in N)


# y > x: partner x + 1, defeated at x = y
gt = lambda x, y: y > x
assert forall_exists(gt, lambda x: x + 1) and no_universal_partner(gt, lambda y: y)
# y != x: partner x + 1, defeated at x = y
ne = lambda x, y: y != x
assert forall_exists(ne, lambda x: x + 1) and no_universal_partner(ne, lambda y: y)
# y >= x: partner x, defeated at x = y + 1
ge = lambda x, y: y >= x
assert forall_exists(ge, lambda x: x) and no_universal_partner(ge, lambda y: y + 1)
# y >= 1: property 1 holds, but y = 1 is a partner of every x
ge1 = lambda x, y: y >= 1
assert forall_exists(ge1, lambda x: 1) and all(ge1(x, 1) for x in N)
print("exr-predicates-and-quantifiers-b2: all quoted values check")
