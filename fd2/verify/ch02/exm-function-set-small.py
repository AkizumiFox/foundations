"""exm-function-set-small (Ch 6 Section 6.4): {0,1}^{1,2} has four elements, each an indicator.
Also the five-string game and the Quick check after it (moved from exm-fraction-map.py with
the re-cut): the indicator of {1, 4} in {1,...,5} is 10010, the value of 01100 at 2 is 1,
and there are 32 strings of length 5."""
import itertools
import sys
sys.path.insert(0, "verify/ch01")
from _sets import functions, subsets

QUOTED = {"number of functions": 4, "indicator_14": "10010", "value_01100_at_2": 1, "strings": 32}

fs = functions({1, 2}, {0, 1})
assert len(fs) == QUOTED["number of functions"]
inds = [{x: (1 if x in A else 0) for x in (1, 2)} for A in subsets({1, 2})]
assert sorted(map(lambda d: tuple(sorted(d.items())), fs)) == sorted(map(lambda d: tuple(sorted(d.items())), inds))
# Quick check after the game, and the game's count
ind = "".join("1" if k in (1, 4) else "0" for k in range(1, 6))
assert ind == QUOTED["indicator_14"]
assert int("01100"[2 - 1]) == QUOTED["value_01100_at_2"]
assert len(list(itertools.product("01", repeat=5))) == QUOTED["strings"]
assert ind not in ("01001", "10110")   # not the game's diagonal or its flip
lst = ["00000", "11111", "01010", "10101", "00111"]
diag = "".join(lst[k][k] for k in range(5))
assert diag == "01001" and "".join("1" if c == "0" else "0" for c in diag) == "10110"
print("exm-function-set-small: all quoted values check")
