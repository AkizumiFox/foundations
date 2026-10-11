"""exm-function-set-small (Ch 6 Section 6.4): {0,1}^{1,2} has four elements, each an indicator."""
import sys
sys.path.insert(0, "verify/ch06")
from _sets import functions, subsets

QUOTED = {"number of functions": 4}

fs = functions({1, 2}, {0, 1})
assert len(fs) == QUOTED["number of functions"]
inds = [{x: (1 if x in A else 0) for x in (1, 2)} for A in subsets({1, 2})]
assert sorted(map(lambda d: tuple(sorted(d.items())), fs)) == sorted(map(lambda d: tuple(sorted(d.items())), inds))
print("exm-function-set-small: all quoted values check")
