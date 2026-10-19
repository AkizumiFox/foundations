"""exr-soundness-b4 (Section 4.7, Test the subgoal): the row refuting the subgoal q, and
the scaffold and its completion by tools/check_fitch.py on a capital-letter copy."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L
import _s0708_lib as H

ctx = [r"p \to (q \vee r)", r"\neg q", "p"]
row = {"p": True, "q": False, "r": True}
assert all(L.val(L.parse(f), row) for f in ctx) and not row["q"]
assert not L.entails(ctx, "r")           # the box's goal r does follow from its context
assert not L.entails([r"p \to (q \vee r)", r"\neg q"], r"p \to r")
c = H.check(H.block(H.S07, "exr-soundness-b4"), derivations=2)
assert c["schema"] == 1
print("exr-soundness-b4: all quoted values check")
