"""exm-group-homomorphisms: (b) powers of [3] in (Z/7Z)^x are [1],[3],[2],[6],[4],[5], [3]^6 = [1];
(d) squares in (Z/7Z)^x: [1],[4],[2],[2],[4],[1], kernel {[1],[6]}; squares in (Z/8Z)^x all [1];
(e) Z/12Z -> Z/3Z x Z/4Z bijective and additive, 1 = 4 - 3; (f) kernel of |.| contains 1, i, -1, -i
(spot check of |zw| = |z||w| on Gaussian integers); the non-example x -> x + 1."""
QUOTED = {
    "pow3": [1, 3, 2, 6, 4, 5],
    "sq7": [1, 4, 2, 2, 4, 1],
    "ker7": [1, 6],
    "units8": [1, 3, 5, 7],
}
assert [pow(3, k, 7) for k in range(6)] == QUOTED["pow3"] and pow(3, 6, 7) == 1
assert [x * x % 7 for x in range(1, 7)] == QUOTED["sq7"]
assert [x for x in range(1, 7) if x * x % 7 == 1] == QUOTED["ker7"]
assert [x for x in range(8) if any(x * y % 8 == 1 for y in range(8))] == QUOTED["units8"]
assert all(x * x % 8 == 1 for x in QUOTED["units8"])
# (e)
phi = {x: (x % 3, x % 4) for x in range(12)}
assert len(set(phi.values())) == 12 and 4 - 3 == 1
for x in range(12):
    for y in range(12):
        a, b = phi[x], phi[y]
        assert phi[(x + y) % 12] == ((a[0] + b[0]) % 3, (a[1] + b[1]) % 4)
# (f) modulus multiplicative: |zw|^2 = |z|^2 |w|^2 on a grid
for a in range(-3, 4):
    for b in range(-3, 4):
        for c in range(-3, 4):
            for d in range(-3, 4):
                re, im = a * c - b * d, a * d + b * c
                assert re * re + im * im == (a * a + b * b) * (c * c + d * d)
# non-example
f = lambda x: x + 1
assert f(0 + 0) == 1 and f(0) + f(0) == 2
print("ok")
