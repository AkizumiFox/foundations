"""exr-refuting-row-search-b3: the completed tree for p v (q & r) |= p v q closes."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _logic as L  # noqa: E402
from _s06_trees import N, check  # noqa: E402

QUOTED = {"verdict": "valid"}
t = N([r"p \vee (q \wedge r)", r"\neg(p \vee q)"], r"\neg(p \vee q)", [
    N([r"\neg p", r"\neg q"], r"p \vee (q \wedge r)", [
        N("p", end="x"),
        N(r"q \wedge r", r"q \wedge r", [N(["q", "r"], end="x")])])])
assert check(t, "B3")[0] and not L.entails([r"p \vee (q \wedge r)"], r"p \vee q")
print("exr-refuting-row-search-b3: all quoted values check")
