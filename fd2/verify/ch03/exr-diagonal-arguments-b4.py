"""exr-diagonal-arguments-b4: (a) on {0, ..., 23}, a p-periodic sequence is determined by its
first p values, so P_p has 2^p members there, and the periodic extension of every pattern
is p-periodic; (b) the interleaving map lands in "no two consecutive 1s" and is injective
(on length-8 inputs); (e) restriction to N is onto (extension by 0, on a window)."""
import itertools

M = 24
for p in range(1, 7):
    Pp = set()
    for w in itertools.product((0, 1), repeat=p):
        a = tuple(w[n % p] for n in range(M))
        assert all(a[n + p] == a[n] for n in range(M - p))
        Pp.add(a)
    # every p-periodic sequence on the window is an extension of its first p values
    count = 0
    for a in itertools.product((0, 1), repeat=12):
        if all(a[n + p] == a[n] for n in range(12 - p)):
            count += 1
            assert a == tuple(a[n % p] for n in range(12))
    assert count == 2 ** p and len(Pp) == 2 ** p
# (b)
seen = set()
for b in itertools.product((0, 1), repeat=8):
    a = []
    for x in b:
        a += [x, 0]
    assert not any(a[i] == a[i + 1] == 1 for i in range(len(a) - 1))
    seen.add(tuple(a))
assert len(seen) == 2 ** 8
# (e) window -5..9: extension by 0 restricts back to b
for b in itertools.product((0, 1), repeat=10):
    ext = {z: (b[z] if z >= 0 else 0) for z in range(-5, 10)}
    assert tuple(ext[n] for n in range(10)) == b
print("exr-diagonal-arguments-b4: all quoted values check")
