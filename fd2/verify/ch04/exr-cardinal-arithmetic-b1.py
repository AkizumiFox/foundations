"""exr-cardinal-arithmetic-b1: the encodings (a), (b) round-trip; (c) is in exm-pairing-bijection.py."""
import itertools
import runpy, pathlib

QUOTED = {"E101": 4}

# (a) (n, r) -> 3n + r
enc = lambda n, r: 3 * n + r
dec = lambda m: divmod(m, 3)
assert all(dec(enc(n, r)) == (n, r) for n in range(500) for r in range(3))
assert all(enc(*dec(m)) == m for m in range(1500))
# (b) on prefixes: c of length 2L <-> d of length L
L = 5
for c in itertools.product((0, 1), repeat=2 * L):
    d = tuple(2 * c[2 * n] + c[2 * n + 1] for n in range(L))
    assert all(v in (0, 1, 2, 3) for v in d)
    back = []
    for v in d:
        q, r = divmod(v, 2)
        back += [q, r]
    assert tuple(back) == c
assert len({tuple(2 * c[2 * n] + c[2 * n + 1] for n in range(L)) for c in itertools.product((0, 1), repeat=2 * L)}) == 4**L
# (c) checked with the pairing
runpy.run_path(str(pathlib.Path(__file__).with_name("exm-pairing-bijection.py")))
print("ok")
