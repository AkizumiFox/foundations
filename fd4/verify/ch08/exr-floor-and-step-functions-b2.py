"""B2: the number of multiples of k in {1..N} is floor(N/k)."""
import sys, os; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor
for N in range(1, 120):
    for k in range(1, 130):
        assert sum(1 for i in range(1, N + 1) if i % k == 0) == floor(F(N, k))
print("exr-floor-and-step-functions-b2: OK")
