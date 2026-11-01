"""exm-integers-mod-six: the tables of Z/6Z and Z/5Z and the claims read from them;
also Z/2Z has the tables of exm-finite-ring-not-orderable."""
QUOTED = {
    "T6": [[0, 0, 0, 0, 0, 0],
           [0, 1, 2, 3, 4, 5],
           [0, 2, 4, 0, 2, 4],
           [0, 3, 0, 3, 0, 3],
           [0, 4, 2, 0, 4, 2],
           [0, 5, 4, 3, 2, 1]],
    "T5": [[0, 0, 0, 0, 0],
           [0, 1, 2, 3, 4],
           [0, 2, 4, 1, 3],
           [0, 3, 1, 4, 2],
           [0, 4, 3, 2, 1]],
    "ex20": (3, 2),
    "zero_div6": {(2, 3), (3, 2), (3, 4), (4, 3)},
    "inv6": {1, 5},
    "idem6": (4, 16),
    "inv5": {1: 1, 2: 3, 3: 2, 4: 4},
}
for n, T in ((6, QUOTED["T6"]), (5, QUOTED["T5"])):
    for a in range(n):
        for b in range(n):
            assert T[a][b] == (a * b) % n
q, r = QUOTED["ex20"]
assert 4 * 5 == 20 == q * 6 + r and 0 <= r < 6
T = QUOTED["T6"]
assert {(a, b) for a in range(1, 6) for b in range(1, 6) if T[a][b] == 0} == QUOTED["zero_div6"]
assert {a for a in range(6) if 1 in T[a]} == QUOTED["inv6"]
a, sq = QUOTED["idem6"]
assert a * a == sq and sq % 6 == a
assert 2 * 3 == 6 and 3 * 4 == 12 and 5 * 5 == 25 and 25 % 6 == 1
T = QUOTED["T5"]
assert all(T[a][b] != 0 for a in range(1, 5) for b in range(1, 5))
for a, b in QUOTED["inv5"].items():
    assert T[a][b] == 1
assert 5 % 5 == 0
# Z/2Z
assert [[(a + b) % 2 for b in range(2)] for a in range(2)] == [[0, 1], [1, 0]]
assert [[(a * b) % 2 for b in range(2)] for a in range(2)] == [[0, 0], [0, 1]]
print("exm-integers-mod-six: ok")
