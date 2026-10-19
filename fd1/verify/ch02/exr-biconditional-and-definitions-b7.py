"""exr-biconditional-and-definitions-b7 (Ch 2, Section 2.4): the eight verdicts by truth table
(derive = no assignment makes the counterexample set true), and the three breaks at x = 1."""
import itertools

QUOTED = {"x": 1}
VERDICTS = "DBDBDDBD"  # (a)-(h): D derive, B break; the solution states each in words

imp = lambda a, b: (not a) or b
iff = lambda a, b: a == b
claims = {
    "a": ([lambda P, Q, R: iff(P, Q)], lambda P, Q, R: iff(P or R, Q or R)),
    "b": ([lambda P, Q, R: iff(P or R, Q or R)], lambda P, Q, R: iff(P, Q)),
    "c": ([lambda P, Q, R: iff(P, Q and R)], lambda P, Q, R: imp(P, Q)),
    "d": ([lambda P, Q, R: iff(P, Q and R)], lambda P, Q, R: imp(Q, P)),
    "e": ([lambda P, Q, R: iff(P, Q), lambda P, Q, R: iff(Q, not R)], lambda P, Q, R: not (P and R)),
    "f": ([lambda P, Q, R: iff(P, Q)], lambda P, Q, R: not (P and not Q)),
    "g": ([lambda P, Q, R: not (P and not Q)], lambda P, Q, R: iff(P, Q)),
    "h": ([lambda P, Q, R: iff(P, Q), lambda P, Q, R: P or Q], lambda P, Q, R: P and Q),
}
verdict = ""
for key in "abcdefgh":
    prem, concl = claims[key]
    broken = any(all(p(*v) for p in prem) and not concl(*v)
                 for v in itertools.product([True, False], repeat=3))
    verdict += "B" if broken else "D"
assert verdict == VERDICTS, verdict

x = QUOTED["x"]
def holds(key, P, Q, R):
    prem, concl = claims[key]
    return all(p(P, Q, R) for p in prem) and not concl(P, Q, R)
assert holds("b", x > 0, x > 5, x > -1)      # (b)
assert holds("d", x > 5, x > 0, x > 3)       # (d)
assert holds("g", x > 5, x > 0, False)       # (g); R does not occur
print("exr-biconditional-and-definitions-b7: all quoted values check")
