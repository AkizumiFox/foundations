"""exr-equality-and-uniqueness-c1 (Section 4.7): exists!x exists!y R(x,y) and
exists!y exists!x R(x,y) agree on every relation on a 1- or 2-element domain
(2 + 16 = 18 relations), and are separated by R = {(1,2),(2,0),(2,1)} on {0,1,2}."""
import itertools

QUOTED = {
    "small_relations": 18,
    "separating_small": 0,
    "single_count": 1,
    "cosingle_count": 3,
    "example_first": True,
    "example_second": False,
    "smallest_domain": 3,
}


def unique(D, pred):
    return sum(1 for d in D if pred(d)) == 1


def first(D, R):  # exists! x exists! y R(x, y)
    return unique(D, lambda x: unique(D, lambda y: (x, y) in R))


def second(D, R):  # exists! y exists! x R(x, y)
    return unique(D, lambda y: unique(D, lambda x: (x, y) in R))


def relations(n):
    D = range(n)
    pairs = [(x, y) for x in D for y in D]
    for bits in itertools.product([False, True], repeat=len(pairs)):
        yield D, {p for p, b in zip(pairs, bits) if b}


small = 0
separating = 0
for n in (1, 2):
    for D, R in relations(n):
        small += 1
        if first(D, R) != second(D, R):
            separating += 1
assert small == QUOTED["small_relations"]
assert separating == QUOTED["separating_small"]

smallest = None
for n in range(1, 4):
    if any(first(D, R) != second(D, R) for D, R in relations(n)):
        smallest = n
        break
assert smallest == QUOTED["smallest_domain"]

D = range(3)
R = {(1, 2), (2, 0), (2, 1)}
singles = [x for x in D if unique(D, lambda y: (x, y) in R)]
cosingles = [y for y in D if unique(D, lambda x: (x, y) in R)]
assert len(singles) == QUOTED["single_count"] and singles == [1]
assert len(cosingles) == QUOTED["cosingle_count"]
assert first(D, R) is QUOTED["example_first"]
assert second(D, R) is QUOTED["example_second"]
print("exr-equality-and-uniqueness-c1: all quoted values check")
