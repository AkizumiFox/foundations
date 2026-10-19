"""exr-completeness-a2 (Section 4.8, drill): (a)-(f) R3's parts; (g), (h), (k) TAUT lines by
truth table; (i) the list is unsatisfiable."""
import sys
sys.path.insert(0, "verify/ch04")
import _logic as L

v = {"p": False, "q": True}
assert [L.val(L.parse(f), v) for f in ["p", "q", r"p \to q", r"q \to p"]] == [False, True, True, False]
assert not L.val(L.parse(r"\neg p \wedge q"), {"p": True, "q": True})
assert (2 ** 3, 2 ** 3 - 1) == (8, 7)
assert not L.val(L.parse("q"), {"p": False, "q": False})
assert not L.entails([r"p \vee q", r"\neg p"], "q")                      # (g)
assert (False, True) in [L.tv(r, "p", "q") for r in L.entails([r"p \to q"], r"q \to p")]   # (h)
assert not L.entails([r"p \vee q", r"\neg p", r"\neg q"], r"\bot")        # (i)
assert not L.entails([], r"\neg(p \wedge \neg p)")                          # (k)
print("exr-completeness-a2: all quoted values check")
