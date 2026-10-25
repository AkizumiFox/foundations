"""exr-set-operations-b4: Prove or disprove (verdicts on all small sets, and the counterexamples)."""
import os, sys
from itertools import product
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _sets import subsets

QUOTED = {"(b)": ({1}, {1}), "(d)": ({1}, set(), {1})}
S = subsets([1, 2, 3])
T = list(product(S, repeat=3))
laws = {
    "a": lambda A, B, C: A - (A - B) == A & B,
    "b": lambda A, B, C: (A | B) - B == A,
    "c": lambda A, B, C: (A | B) - B == A - B,
    "d": lambda A, B, C: A | (B - C) == (A | B) - C,
    "e": lambda A, B, C: A & (B - C) == (A & B) - C,
}
verdict = {k: all(f(*t) for t in T) for k, f in laws.items()}
assert verdict == {"a": True, "b": False, "c": True, "d": False, "e": True}
A, B = QUOTED["(b)"]
assert (A | B) - B == set() and A == {1}
A, B, C = QUOTED["(d)"]
assert A | (B - C) == {1} and (A | B) - C == set()
print("exr-set-operations-b4: all quoted values check")
