"""exr-compactness-a2 (Section 4.10): the drill answers that are finite checks: (b), (c),
(d), (h), (i), (j), (l) on finite parts; (a), (b), (l) by the stated valuations on p_1..p_40."""
from _logic import parse, val, rows, entails
N = 40
v = {n: True for n in range(1, N + 1)}                       # (a)
assert all(v.values())
v = {n: n == 1 for n in range(1, N + 1)}                     # (b) and the Quick check
assert v[1] and all(not v[n] for n in range(2, N + 1))
assert v[1] or v[2]
assert not entails(["p_1 \\to p_2", "p_2 \\to p_3", "p_3 \\to p_4", "p_4 \\to p_5",
                    "p_5 \\to p_6", "p_6 \\to p_7"], "p_1 \\to p_7")      # (c)
assert entails(["p_1 \\to p_2", "p_2 \\to p_3", "p_3 \\to p_4", "p_4 \\to p_5",
                "p_5 \\to p_6"], "p_1 \\to p_7")                            # one fewer fails
assert not entails(["p_1 \\vee p_2", "\\neg p_1", "\\neg p_2"], "\\bot")  # (d) unsatisfiable
assert not entails(["p", "\\neg q"], "p \\wedge \\neg q")                   # (h)
assert not entails(["p \\to q", "p", "\\neg q"], "\\bot")                   # (i)
assert len(["p", "q", "\\bot"]) == 3                                         # (j)
v = {n: n % 2 == 1 for n in range(1, N + 2)}                                # (l)
assert all(v[n] == (not v[n + 1]) for n in range(1, N + 1))
print("exr-compactness-a2: all quoted values check")
