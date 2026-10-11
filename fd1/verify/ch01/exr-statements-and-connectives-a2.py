"""Values quoted in the solution of exr-statements-and-connectives-a2 (Section 1.1, drill)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _grid import grid

QUOTED = {"(f),(g) x": -2, "(h) n": 2, "(i) x": 0}
x = QUOTED["(f),(g) x"]
assert not x > 1                         # (f): hypothesis false, nothing promised
assert x**2 > 1 and x**2 == 4 and not x > 1   # (g): broken
n = QUOTED["(h) n"]
assert all(n % d for d in range(2, n)) and n >= 2 and n % 2 == 0   # 2 is prime and not odd
x = QUOTED["(i) x"]
assert (x >= 0 or x <= 0) and x >= 0 and x <= 0   # both premises true, not-Q false
# (j): 7 is odd, so the premise "7 is even" is false; 49 is odd, so the conclusion is false
assert 7 % 2 == 1 and 49 % 2 == 1
# (d),(e) are translations; nothing numeric
print("exr-statements-and-connectives-a2: checks")
