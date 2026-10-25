"""exm-maximal-not-greatest: in {2,...,6} under divisibility the strict divisibilities are 2|4, 2|6,
3|6; maximal elements 4, 5, 6; minimal 2, 3, 5; no greatest, no least. In {{1},{2}} under
inclusion both are maximal and neither is greatest. {1,...,6} has least element 1, no greatest."""

QUOTED = {"strict": {(2, 4), (2, 6), (3, 6)}, "maximal": {4, 5, 6}, "minimal": {2, 3, 5}}

def analyse(A, le):
    lt = lambda x, y: le(x, y) and x != y
    mx = {m for m in A if not any(lt(m, a) for a in A)}
    mn = {m for m in A if not any(lt(a, m) for a in A)}
    gr = {g for g in A if all(le(a, g) for a in A)}
    ls = {l for l in A if all(le(l, a) for a in A)}
    return lt, mx, mn, gr, ls

div = lambda a, b: b % a == 0
A = [2, 3, 4, 5, 6]
lt, mx, mn, gr, ls = analyse(A, div)
assert {(a, b) for a in A for b in A if lt(a, b)} == QUOTED["strict"]
assert mx == QUOTED["maximal"] and mn == QUOTED["minimal"] and not gr and not ls
_, _, _, gr6, ls6 = analyse(range(1, 7), div)
assert not gr6 and ls6 == {1}
B = [frozenset({1}), frozenset({2})]
_, mxB, _, grB, _ = analyse(B, lambda x, y: x <= y)
assert mxB == set(B) and not grB
print("exm-maximal-not-greatest: all quoted values check")
