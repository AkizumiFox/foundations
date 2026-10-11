"""exr-derivations-b3 (Section 1.2): 0 < 1/4 < 1/3 < 1/2; forward chaining uses m - 1
applications of Tr; and (stated, not proved, in the text) no derivation uses fewer:
checked by breadth-first search over sets of derived lines for m <= 5."""
import pathlib
import sys
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import is_derivation

QUOTED = {"chain": (Fraction(0), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)),
          "links m": 3, "applications": 2}
ch = QUOTED["chain"]
assert all(ch[i] < ch[i + 1] for i in range(len(ch) - 1))
d = [("0 < 1/4", None, ()), ("1/4 < 1/3", None, ()), ("1/3 < 1/2", None, ()),
     ("0 < 1/3", "Tr", (1, 2)), ("0 < 1/2", "Tr", (4, 3))]
assert is_derivation(d, ("Tr",))
assert sum(1 for _, r, _ in d if r == "Tr") == QUOTED["applications"] == QUOTED["links m"] - 1


def min_steps(m):
    """Fewest Tr lines deriving (0, m) from links (i, i+1); lines are index pairs."""
    start = frozenset((i, i + 1) for i in range(m))
    if (0, m) in start:
        return 0
    frontier, seen, steps = {start}, {start}, 0
    while frontier:
        steps += 1
        nxt = set()
        for s in frontier:
            for (a, b) in s:
                for (b2, c) in s:
                    if b == b2 and (a, c) not in s:
                        t = s | {(a, c)}
                        if (0, m) in t:
                            return steps
                        if t not in seen:
                            seen.add(t)
                            nxt.add(t)
        frontier = nxt
    raise AssertionError


for m in range(1, 6):
    assert min_steps(m) == m - 1, m
print("exr-derivations-b3: all checks pass")
