"""exr-compactness-c1 (Section 4.10): the collection Gamma of the three kinds, built for a
finite graph; a satisfying valuation is a 3-colouring and conversely. The 5-cycle is
3-colourable and its Gamma_0 satisfiable; K_4 is not, and its Gamma_0 unsatisfiable."""
import itertools
def gamma(vertices, edges):
    out = []
    for n in vertices:
        out.append(("one", n))
        for i, j in itertools.combinations((1, 2, 3), 2):
            out.append(("two", n, i, j))
    for m, n in edges:
        for i in (1, 2, 3):
            out.append(("edge", m, n, i))
    return out
def true_in(f, v):
    if f[0] == "one":
        return any(v[(f[1], i)] for i in (1, 2, 3))
    if f[0] == "two":
        return not (v[(f[1], f[2])] and v[(f[1], f[3])])
    return not (v[(f[1], f[3])] and v[(f[2], f[3])])
def satisfiable(vertices, edges):
    G = gamma(vertices, edges)
    keys = [(n, i) for n in vertices for i in (1, 2, 3)]
    found = []
    for bits in itertools.product([False, True], repeat=len(keys)):
        v = dict(zip(keys, bits))
        if all(true_in(f, v) for f in G):
            col = {n: [i for i in (1, 2, 3) if v[(n, i)]] for n in vertices}
            assert all(len(c) == 1 for c in col.values())
            assert all(col[m] != col[n] for m, n in edges)
            found.append(col)
    return found
def colourable(vertices, edges):
    return any(all(c[a] != c[b] for a, b in edges)
               for c in (dict(zip(vertices, cs)) for cs in itertools.product((1, 2, 3), repeat=len(vertices))))
C5 = ([1, 2, 3, 4, 5], [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])
K4 = ([1, 2, 3, 4], list(itertools.combinations([1, 2, 3, 4], 2)))
assert colourable(*C5) and satisfiable(*C5)
assert not colourable(*K4) and not satisfiable(*K4)
print("exr-compactness-c1: all quoted values check")
