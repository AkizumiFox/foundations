"""Shared exact helpers for the ch08 section 4 sidecars (floor, ceiling, distance)."""
from fractions import Fraction as F
import math, random


def floor(x):
    return math.floor(F(x))


def ceil(x):
    return -floor(-F(x))


def dist(x):
    """Distance to Z by brute force over integers near x (independent of the min formula)."""
    x = F(x)
    c = math.floor(x)
    return min(abs(x - n) for n in range(c - 3, c + 4))


def rationals(count=4000, seed=8):
    rnd = random.Random(seed)
    out = [F(0), F(1, 2), F(-1, 2), F(3), F(-3)]
    for _ in range(count):
        out.append(F(rnd.randint(-400, 400), rnd.randint(1, 37)))
    return out
