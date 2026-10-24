"""exr-equality-and-uniqueness-b5 (Section 5.7, [B3: Derive or break]): the counter-readings
of (b), (e), (h) on {0, 1}, each with every premise true and the conclusion false; and, as a
sanity check, the 'derive' claims (a), (c), (d), (f), (g) true in every structure on 1-3
elements (every f, every value of the constants)."""
import itertools

QUOTED = {"break": "beh", "derive": True, "domain": 2}


def claims(f, a, b, c, D):
    """premises -> conclusion, as (list of premise truth values, conclusion truth value)."""
    return {
        "a": ([f[a] == b, a == c], f[c] == b),
        "b": ([f[a] == f[b]], a == b),
        "c": ([all(f[x] == x for x in D)], f[f[c]] == c),
        "d": ([all(f[x] != f[y] or x == y for x in D for y in D), f[a] == f[b]], a == b),
        "e": ([a != b, b != c], a != c),
        "f": ([a == b, b != c], a != c),
        "g": ([f[a] == a], f[f[a]] == a),
        "h": ([f[f[a]] == a], f[a] == a),
    }


broken = set()
for n in (1, 2, 3):
    D = range(n)
    for fv in itertools.product(D, repeat=n):
        for a, b, c in itertools.product(D, repeat=3):
            for k, (prem, concl) in claims(list(fv), a, b, c, D).items():
                if all(prem) and not concl:
                    broken.add(k)
assert set("abcdefgh") - broken == set("acdfg")   # the derive claims never break
assert broken == set(QUOTED["break"])          # exactly (b), (e), (h) can break

# the readings given in the solution
D = range(QUOTED["domain"])
cb = claims([0, 0], 0, 1, 0, D)["b"]                 # f sends both to 0, a = 0, b = 1
ce = claims([0, 1], 0, 1, 0, D)["e"]                 # a, c name 0, b names 1
ch = claims([1, 0], 0, 0, 0, D)["h"]                 # f exchanges 0 and 1, a = 0
for prem, concl in (cb, ce, ch):
    assert all(prem) and not concl
print("exr-equality-and-uniqueness-b5: all quoted values check")
