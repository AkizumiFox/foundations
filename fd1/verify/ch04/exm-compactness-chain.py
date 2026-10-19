"""exm-compactness-chain (Section 4.10): on p_1..p_200, (b)'s valuation makes every member
but p_50 -> p_51 true and p_100 false; (a)'s hundred formulas entail p_100 (forward
chaining is forced); the aftermath: each p_k -> p_(k+1), k < 100, and p_1 are needed."""
N = 200
def members(skip=None):
    out = [("atom", 1)] + [("imp", n) for n in range(1, N)]
    return [m for m in out if m != skip]
def true_in(m, v):
    return v[1] if m[0] == "atom" else (not v[m[1]]) or v[m[1] + 1]
def val_upto(k):
    return {n: n <= k for n in range(1, N + 1)}
v = val_upto(50)
assert [m for m in members() if not true_in(m, v)] == [("imp", 50)]
assert v[100] is False
# (a): any valuation making p_1 and p_1->p_2 .. p_99->p_100 true makes p_100 true
lst = [("atom", 1)] + [("imp", n) for n in range(1, 100)]
for k in range(0, 101):        # the only candidate refuters: true up to k, then false
    w = val_upto(k)
    if all(true_in(m, w) for m in lst):
        assert w[100]
# aftermath
for k in range(1, 100):
    w = val_upto(k)
    assert [m for m in members() if not true_in(m, w)] == [("imp", k)] and not w[100]
w = val_upto(0)
assert [m for m in members() if not true_in(m, w)] == [("atom", 1)] and not w[100]
print("exm-compactness-chain: all quoted values check")
