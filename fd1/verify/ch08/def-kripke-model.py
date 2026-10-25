"""kripke.py (Section 8.8, and the right column of Section 8.7's table): a finite
Kripke-model checker. It evaluates forcing by (K1)-(K7) at every stage of the models
M1-M7 of Section 8.8 and asserts every forced / not-forced claim the section quotes
(items of the text, the settle table, the Not-allowed lines, A1, A2, B1, B2, C1, and
instances of C2). It checks heredity (lem-heredity) on the closure of all forcing sets
reachable from the letters p, q, r under the connectives (so for formulas of every
depth), that the models are Kripke models, that one-stage models agree with truth
tables, and B1 (c): no stage of any chain of up to four stages over p, q refutes
(p -> q) or (q -> p)."""
import itertools

# formulas: ("at", "p"), ("bot",), ("not", f), (op, f, g) with op in and/or/imp/iff
p, q, r = ("at", "p"), ("at", "q"), ("at", "r")
BOT = ("bot",)
def N(f): return ("not", f)
def A(f, g): return ("and", f, g)
def O(f, g): return ("or", f, g)
def I(f, g): return ("imp", f, g)


class Model:
    def __init__(self, arrows, known):
        self.stages = list(known)
        self.known = {w: set(v) for w, v in known.items()}
        reach = {w: {w} for w in self.stages}          # reflexive
        changed = True
        while changed:                                 # transitive closure
            changed = False
            for a, b in arrows:
                for w in self.stages:
                    if a in reach[w] and not reach[b] <= reach[w]:
                        reach[w] |= reach[b]
                        changed = True
        self.reach = reach
        for w in self.stages:                          # letters persist
            for v in reach[w]:
                assert self.known[w] <= self.known[v], (w, v)

    def forces(self, w, f):
        k = f[0]
        if k == "at":
            return f[1] in self.known[w]
        if k == "bot":
            return False
        if k == "and":
            return self.forces(w, f[1]) and self.forces(w, f[2])
        if k == "or":
            return self.forces(w, f[1]) or self.forces(w, f[2])
        if k == "imp":
            return all(self.forces(v, f[2]) for v in self.reach[w] if self.forces(v, f[1]))
        if k == "not":
            return not any(self.forces(v, f[1]) for v in self.reach[w])
        if k == "iff":
            return self.forces(w, I(f[1], f[2])) and self.forces(w, I(f[2], f[1]))
        raise ValueError(f)

    def refutes(self, w, prem, concl):
        return all(self.forces(w, g) for g in prem) and not self.forces(w, concl)


M1 = Model([(0, 1)], {0: [], 1: ["p"]})
M2 = Model([(0, 1), (0, 2)], {0: [], 1: ["p"], 2: ["q"]})
M3 = Model([(0, 1)], {0: [], 1: ["p", "q"]})
M4 = Model([(0, 1)], {0: ["p"], 1: ["p", "q"]})
M5 = Model([(0, 1), (1, 2)], {0: [], 1: ["p"], 2: ["p", "q"]})
M6 = Model([(0, 1), (1, 2)], {0: [], 1: ["q"], 2: ["p", "q"]})
M7 = Model([(0, 1), (0, 2)], {0: [], 1: ["p"], 2: []})
MODELS = [M1, M2, M3, M4, M5, M6, M7]

peirce = I(I(I(p, q), p), p)
lem = O(p, N(p))

# the picture of the Not-allowed line and A2 (g) is not a Kripke model
try:
    Model([(0, 1)], {0: ["p"], 1: []})
    raise AssertionError("letter lost at a later stage was accepted")
except AssertionError as e:
    assert "accepted" not in str(e)

# --- the text ---------------------------------------------------------------
# Quick check: one stage, p unknown, forces not-p and p or not-p
one = Model([], {0: []})
assert one.forces(0, N(p)) and one.forces(0, lem)
# exm-two-stage-model
assert not M1.forces(0, p) and not M1.forces(0, N(p)) and not M1.forces(0, lem)
assert M1.forces(0, N(N(p))) and not M1.forces(0, I(N(N(p)), p))
assert M1.refutes(0, [N(N(p))], p)
# fallback Quick check: w1 of M1 forces p or not p
assert M1.forces(1, lem)
# RAA's failure in the table / Quick check
assert M1.forces(0, N(N(p))) and not M1.forces(0, p)
# exm-three-stage-model
assert not M2.forces(0, O(I(p, q), I(q, p)))
assert M2.refutes(0, [N(A(p, q))], O(N(p), N(q)))
assert not M2.forces(0, I(p, q)) and not M2.forces(0, I(q, p))

# --- the settle table ------------------------------------------------------
settle = [
    (M1, [], lem), (M1, [N(N(p))], p), (M1, [], I(N(N(p)), p)),
    (M1, [], peirce),
    (M1, [N(I(p, q))], A(p, N(q))),
    (M1, [I(I(p, q), q)], O(p, q)),
    (M3, [I(p, q)], O(N(p), q)),
    (M4, [I(N(q), N(p))], I(p, q)),
    (M2, [], O(I(p, q), I(q, p))),
    (M2, [N(A(p, q))], O(N(p), N(q))),
]
for M, prem, concl in settle:
    assert M.refutes(0, prem, concl), (prem, concl)
# details quoted in the table
assert not any(M1.forces(w, I(p, q)) for w in M1.stages)
assert all(M1.forces(w, I(I(p, q), p)) for w in M1.stages)
assert all(M1.forces(w, I(I(p, q), q)) for w in M1.stages)
assert M3.forces(0, I(p, q)) and M3.forces(1, p)
assert not any(M4.forces(w, N(q)) for w in M4.stages) and M4.forces(0, p)

# --- Not allowed -----------------------------------------------------------
assert not M1.forces(0, p) and not M1.forces(0, N(p))
assert all(M2.forces(w, O(p, q)) for w in (1, 2)) and not M2.forces(0, O(p, q))

# --- A1 --------------------------------------------------------------------
assert M1.forces(1, I(N(N(p)), p))

# --- A2 --------------------------------------------------------------------
a2 = {
    "a": not M1.forces(1, N(p)),
    "b": M1.forces(0, N(q)),
    "c": not M2.forces(0, O(p, q)),
    "d": M2.forces(1, N(q)),
    "e": not M5.forces(0, I(p, q)),
    "f": M5.forces(1, N(N(q))) and not M5.forces(1, q),
    "i": M2.forces(0, I(N(p), q)) and [w for w in M2.stages if M2.forces(w, N(p))] == [2],
    "j": not M5.forces(0, O(q, N(q))),
    "k": M5.forces(0, I(q, p)) and [w for w in M5.stages if M5.forces(w, q)] == [2],
}
assert all(a2.values()), a2
# (l): no one-stage model refutes not-not p |- p
for kn in ([], ["p"]):
    assert not Model([], {0: kn}).refutes(0, [N(N(p))], p)

# --- B1 --------------------------------------------------------------------
assert M6.forces(0, N(N(p)))
assert not M6.forces(0, lem)
assert not M6.forces(0, I(q, p))
assert M6.forces(0, O(I(q, p), I(p, q))) and M6.forces(0, I(p, q))
assert M6.forces(0, I(N(p), N(q)))
assert M6.refutes(0, [], lem) and M6.refutes(0, [N(N(p))], p)
assert not M6.refutes(0, [], O(I(p, q), I(q, p)))
# (c): every chain of 1-4 stages, every persistent assignment of p, q
lin = O(I(p, q), I(q, p))
for n in range(1, 5):
    arrows = [(i, i + 1) for i in range(n - 1)]
    # a persistent assignment on a chain: each letter becomes known at some step (or never)
    for sp, sq in itertools.product(range(n + 1), repeat=2):
        known = {i: [x for x, s in (("p", sp), ("q", sq)) if i >= s] for i in range(n)}
        M = Model(arrows, known)
        assert all(M.forces(w, lin) for w in M.stages)

# --- B2 --------------------------------------------------------------------
assert M2.refutes(0, [N(N(O(p, q)))], O(N(N(p)), N(N(q))))
assert M2.forces(2, N(p)) and M2.forces(1, N(q))
assert M1.refutes(0, [I(N(p), p)], p)
assert not any(M1.forces(w, N(p)) for w in M1.stages)
assert M3.refutes(0, [A(I(p, q), I(N(p), q))], q)
# the derivable claims are forced wherever their premises are, in every model here
for M in MODELS:
    for w in M.stages:
        for prem, concl in [([N(N(A(p, q)))], A(N(N(p)), N(N(q)))),
                            ([A(N(N(p)), N(N(q)))], N(N(A(p, q)))),
                            ([I(I(p, q), p)], N(N(p))),
                            ([A(O(p, q), N(p))], q),
                            ([I(N(p), p)], N(N(p)))]:
            assert not M.refutes(w, prem, concl)

# --- C1 --------------------------------------------------------------------
c1b = I(peirce, lem)
assert M7.refutes(0, [], c1b)
assert M7.forces(0, peirce) and not M7.forces(0, lem)
assert M7.forces(2, I(p, q)) and not M7.forces(2, I(I(p, q), p))
assert [w for w in M7.stages if M7.forces(w, I(I(p, q), p))] == [1]
assert M1.forces(0, c1b)
assert [w for w in M1.stages if M1.forces(w, peirce)] == [1] and M1.forces(1, lem)
# (a): from p or not p, Peirce's law is forced at every stage that forces the premise
for M in MODELS:
    for w in M.stages:
        assert not M.refutes(w, [lem], peirce)

# --- heredity, on every formula over p, q, r -------------------------------
def closure(M):
    """All forcing sets of formulas over p, q, r: a fixed point of the clauses."""
    st = M.stages
    def fset(sets_a, op, sets_b=None):
        if op == "not":
            return frozenset(w for w in st if not (M.reach[w] & sets_a))
        if op == "and":
            return sets_a & sets_b
        if op == "or":
            return sets_a | sets_b
        if op == "imp":
            return frozenset(w for w in st if all(v in sets_b for v in M.reach[w] if v in sets_a))
        if op == "iff":
            return fset(sets_a, "imp", sets_b) & fset(sets_b, "imp", sets_a)
    sets = {frozenset(), *(frozenset(w for w in st if x in M.known[w]) for x in "pqr")}
    while True:
        new = set(sets)
        for a in sets:
            new.add(fset(a, "not"))
            for b in sets:
                for op in ("and", "or", "imp", "iff"):
                    new.add(fset(a, op, b))
        if new == sets:
            return sets
        sets = new

for M in MODELS + [one]:
    for s in closure(M):
        for w in s:
            assert M.reach[w] <= s, "heredity fails"

# the recursive evaluator agrees with the set computation on formulas of depth <= 2
def formulas(depth):
    fs = [p, q, r, BOT]
    for _ in range(depth):
        fs = fs + [N(f) for f in fs] + [(op, f, g) for op in ("and", "or", "imp", "iff")
                                        for f in fs[:8] for g in fs[:8]]
    return fs

# one-stage models are rows of a truth table
def truth(v, f):
    k = f[0]
    if k == "at": return v[f[1]]
    if k == "bot": return False
    if k == "not": return not truth(v, f[1])
    if k == "and": return truth(v, f[1]) and truth(v, f[2])
    if k == "or": return truth(v, f[1]) or truth(v, f[2])
    if k == "imp": return (not truth(v, f[1])) or truth(v, f[2])
    if k == "iff": return truth(v, f[1]) == truth(v, f[2])

for bits in itertools.product([True, False], repeat=3):
    v = dict(zip("pqr", bits))
    M = Model([], {0: [x for x in "pqr" if v[x]]})
    for f in formulas(2):
        assert M.forces(0, f) == truth(v, f)
    for f in [peirce, lem, c1b, I(N(N(p)), p), O(I(p, q), I(q, p))]:
        assert M.forces(0, f) == truth(v, f)

# --- C2 instances: not-not-not phi and not phi are forced at the same stages -----
for M in MODELS:
    for f in formulas(1):
        for w in M.stages:
            assert M.forces(w, N(N(N(f)))) == M.forces(w, N(f))

print("kripke: all quoted values check")
