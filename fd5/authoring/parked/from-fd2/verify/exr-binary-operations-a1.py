"""exr-binary-operations-a1: Z/3 addition table, inverses; x*y := y left/right identities."""
QUOTED = {"table": [[0, 1, 2], [1, 2, 0], [2, 0, 1]], "neg": {0: 0, 1: 2, 2: 1}}
assert [[(a + b) % 3 for b in range(3)] for a in range(3)] == QUOTED["table"]
assert all((a + QUOTED["neg"][a]) % 3 == 0 for a in range(3))
assert [a for a in range(3) if all((a + x) % 3 == x for x in range(3))] == [0]
assert 2 - 3 < 0 and (1 / 2) != int(1 / 2)
X = [1, 2]
op = lambda x, y: y
assert [e for e in X if all(op(e, y) == y for y in X)] == X
assert [e for e in X if all(op(x, e) == x for x in X)] == []
print("exr-binary-operations-a1: all quoted values check")
