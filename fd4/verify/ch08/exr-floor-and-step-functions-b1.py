"""B1: (a) floor 2x = floor x + floor(x + 1/2) (true); (b) false at 0; (c) floor sqrt floor x =
floor sqrt x for x >= 0 (true; checked with exact integer square roots); (d) false at 1/2."""
import sys, os, math; sys.path.insert(0, os.path.dirname(__file__))
from _floorlib import F, floor, ceil, rationals
h = F(1, 2)


def floor_sqrt(x):
    """floor(sqrt(x)) for rational x >= 0, exactly: largest j >= 0 with j*j <= x."""
    j = math.isqrt(floor(x))
    assert j * j <= x < (j + 1) ** 2
    return j


for x in rationals():
    assert floor(2 * x) == floor(x) + floor(x + h)
    assert (ceil(x) - floor(x) == 1) == (x.denominator != 1)
    assert (floor(x) + floor(-x) == 0) == (x.denominator == 1)
    if x >= 0:
        assert floor_sqrt(floor(x)) == floor_sqrt(x)
assert ceil(0) - floor(0) == 0 and floor(h) + floor(-h) == -1
print("exr-floor-and-step-functions-b1: OK")
