"""exr-valuations-and-truth-tables-c1 (Section 3.3): of the 16 possible tables t for ->,
exactly one passes the four instances used in the solution, and it is the table of (V5).
Instances: (E) at v(p)=T, v(q)=F; (I) with Gamma empty, phi = psi = p; (I) with Gamma = q,
phi = p, psi = q. None of these formulas contains ->, so the hypothesis of (I) is
checked with the clauses of the other connectives only."""
import itertools

QUOTED = {"tables passing": 1}
pairs = [(a, b) for a in (True, False) for b in (True, False)]
passing = []
for vals in itertools.product((True, False), repeat=4):
    t = dict(zip(pairs, vals))
    ok = True
    # (E): v(p)=T, v(q)=F: if t(T,F) then v(q) would have to be T
    if t[(True, False)]:
        ok = False
    # (I), Gamma empty, phi = psi = p: every valuation makes p -> p true
    if not (t[(True, True)] and t[(False, False)]):
        ok = False
    # (I), Gamma = q, phi = p, psi = q: every v with v(q) = T makes p -> q true
    if not (t[(True, True)] and t[(False, True)]):
        ok = False
    if ok:
        passing.append(t)
assert len(passing) == QUOTED["tables passing"]
t = passing[0]
assert t == {(True, True): True, (True, False): False, (False, True): True, (False, False): True}
print("exr-valuations-and-truth-tables-c1: all quoted values check")
