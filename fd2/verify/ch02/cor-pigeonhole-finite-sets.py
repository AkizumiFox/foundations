"""cor-pigeonhole-finite-sets: among any three integers two have an even sum (brute force)."""
from itertools import combinations
QUOTED = {"set_size": 3}
for trip in combinations(range(-15, 16), QUOTED["set_size"]):
    assert any((a + b) % 2 == 0 for a, b in combinations(trip, 2))
print("ok")
