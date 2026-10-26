"""exr-peano-properties-c2: N x {a, b, c} with the two-sided chain on rows b, c.
Checked on rows truncated at 30 (natural numbers as ints, S(n) = n + 1)."""
QUOTED = {"no_arrow_in": [(0, "a")], "witness_missed": (0, "b"),
          "predecessor_conclusions_hold": ("a", "b")}
R = 30
M = [(n, t) for n in range(R) for t in "abc"]
e = (0, "a")

def s(x):
    n, t = x
    if t in "ab":
        return (n + 1, t)
    return (0, "b") if n == 0 else (n - 1, "c")

# (a) one value each, inside M (allowing first coordinate R at the truncation edge)
vals = {x: s(x) for x in M}
# (b) (P3) and (P4)
assert all(v != e for v in vals.values())
assert len(set(vals.values())) == len(vals)
# (c) every x != e is a value; the truncation loses only the preimages of row c at the edge
targets = set(vals.values())
missing = [x for x in M if x not in targets]
assert missing == [e] + [(R - 1, "c")]   # (R-1, c) = s(R, c), outside the truncation
assert [x for x in missing if x[1] != "c"] == QUOTED["no_arrow_in"]
# (d) N x {a} contains e, closed, misses (0, b)
A = {(n, "a") for n in range(R + 1)}
assert e in A and all(s(x) in A for x in A if x[0] < R)
assert QUOTED["witness_missed"] not in A
# (e) s(x) != x everywhere; predecessors unique where they exist
assert all(vals[x] != x for x in M)
# chain reading: (n, b) as n, (k, c) as -(k + 1); s adds one on rows b, c
val = lambda x: x[0] if x[1] == "b" else -(x[0] + 1)
assert all(val(s(x)) == val(x) + 1 for x in M if x[1] in "bc")
print("ok")
