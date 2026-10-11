"""lem-field-fraction-rules (a)-(d): the fraction identities, checked in Q on a grid of non-zero samples.

Each identity is an equation between rational functions of degree at most 2 in each variable;
agreement on a grid with more than 2 points per variable implies the identity.
"""
from fractions import Fraction as Fr
import itertools

QUOTED = {"sum_numerator": "ad + bc", "product_numerator": "{ac}{bd}", "reciprocal_difference": "{d - b}{bd}"}

vals = [Fr(-3, 2), Fr(-1), Fr(1, 3), Fr(2), Fr(5, 7)]
for A, B, C, D in itertools.product(vals, repeat=4):
    assert A / B + C / D == (A * D + B * C) / (B * D)
    assert (A / B) * (C / D) == (A * C) / (B * D)
    assert 1 / B - 1 / D == (D - B) / (B * D)
    assert B * D != 0 and 1 / (B * D) == (1 / B) * (1 / D) and 1 / (1 / B) == B
print("ok")
