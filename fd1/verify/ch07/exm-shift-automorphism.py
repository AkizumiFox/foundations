"""exm-shift-automorphism (Section 7.5): the four-cycle's automorphisms are exactly the four
rotations (all 24 permutations tested); they move any element to any other; the Quick check
on {a,c} and {b,d}; with the loop (a,a) added only the identity remains (three of four removed)
and R(x,x) defines {a}. Also the finite isomorphism of Figure 7.5-I and the shift on Z (window)."""
import itertools

D = "abcd"
R = {("a", "b"), ("b", "c"), ("c", "d"), ("d", "a")}
def autos(D, R):
    out = []
    for p in itertools.permutations(D):
        h = dict(zip(D, p))
        if all(((x, y) in R) == ((h[x], h[y]) in R) for x in D for y in D):
            out.append(h)
    return out
A = autos(D, R)
QUOTED = {"autos": 4, "with_loop": 1}
assert len(A) == QUOTED["autos"]
rot = {"a": "b", "b": "c", "c": "d", "d": "a"}
assert rot in A
assert all(any(h[x] == y for h in A) for x in D for y in D)
assert {rot["a"], rot["c"]} == {"b", "d"} and {rot["b"], rot["d"]} == {"c", "a"}
R2 = R | {("a", "a")}
assert len(autos(D, R2)) == QUOTED["with_loop"]
assert [x for x in D if (x, x) in R2] == ["a"]
# Figure 7.5-I: a->1, b->2, c->3 is an isomorphism onto ({1,2,3}, <)
M = {("a", "b"), ("b", "c"), ("a", "c")}
h = {"a": 1, "b": 2, "c": 3}
assert all(((x, y) in M) == (h[x] < h[y]) for x in "abc" for y in "abc")
# shift on Z preserves < both ways (window); d -> d+1 on N misses 0
W = range(-50, 51)
assert all((d < e) == (d + 1 < e + 1) for d in W for e in W)
assert 0 not in {d + 1 for d in range(0, 100)}
print("exm-shift-automorphism: all quoted values check")
