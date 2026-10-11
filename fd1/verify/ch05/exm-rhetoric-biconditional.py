"""exm-rhetoric-biconditional (Ch 5, Section 5.1): for x >= 0, x <= 1 iff x^2 <= x;
x = -1 shows the hypothesis x >= 0 is needed for (=>);
without it (<=) still holds, since x < 0 gives x^2 >= 0 > x."""
from fractions import Fraction as Fr

QUOTED = {"counter_x": -1, "counter_sq": 1}

for k in range(0, 301):
    x = Fr(k, 100)
    assert (x <= 1) == (x * x <= x)
# (<=) without the hypothesis: negative x never has x^2 <= x
for k in range(1, 301):
    x = Fr(-k, 100)
    assert x * x >= 0 > x and not (x * x <= x)
    assert (not (x * x <= x)) or x <= 1
x = Fr(QUOTED["counter_x"])
assert x * x == QUOTED["counter_sq"] and x * x > x and x <= 1
print("exm-rhetoric-biconditional: all quoted values check")
