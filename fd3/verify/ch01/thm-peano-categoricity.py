"""thm-peano-categoricity: the Quick check (phi for (omega \\ {0}, 1, S)), the aftermath list
(phi on the two finite structures), the remark (phi(n) = (n, 0) in omega x 3), and the
warning (the swap of 1 and 2 is a bijection that does not respect S). Von Neumann numerals
are frozensets; phi is computed from its two recursion equations only."""
E = frozenset()
def S(x): return x | frozenset([x])
def num(k):
    x = E
    for _ in range(k): x = S(x)
    return x
def pair(a, b): return frozenset([frozenset([a]), frozenset([a, b])])

def phi(n_index, e, s):
    """phi(0) = e, phi(S(n)) = s(phi(n)), unwound n_index times."""
    v = e
    for _ in range(n_index): v = s(v)
    return v

QUOTED = {"check_phi": {0: 1, 1: 2, 2: 3, 3: 4},
          "p3_fail_phi1_eq_phi0": True, "p4_fail_phi1_eq_phi2": True,
          "remark_phi": "(n,0)", "warning_tau": (0, 2, 1)}

# Quick check: (omega \ {0}, 1, S); phi(n) = S(n)
for n, val in QUOTED["check_phi"].items():
    assert phi(n, num(1), S) == num(val) == S(num(n))
# aftermath: M = {0}, s(0) = 0 ; M = {0,1}, s(0) = s(1) = 1
s1 = {0: 0}
assert (phi(1, 0, s1.get) == phi(0, 0, s1.get)) == QUOTED["p3_fail_phi1_eq_phi0"]
s2 = {0: 1, 1: 1}
assert (phi(1, 0, s2.get) == phi(2, 0, s2.get) == 1) == QUOTED["p4_fail_phi1_eq_phi2"]
# remark: omega x 3, e = (0,0), s(n,0) = (S(n),0); phi(n) = (n,0) for n < 6, and (0,1) is missed
def s3(p):
    for n in range(10):
        for layer in range(3):
            if p == pair(num(n), num(layer)):
                if layer in (0, 1): return pair(num(n + 1), num(layer))
                return pair(num(0), num(1)) if n == 0 else pair(num(n - 1), num(2))
    raise ValueError
img = set()
for n in range(6):
    v = phi(n, pair(num(0), num(0)), s3)
    assert v == pair(num(n), num(0)); img.add(v)
assert pair(num(0), num(1)) not in img
# warning: tau swaps 1 and 2
def tau(k): return {1: 2, 2: 1}.get(k, k)
t0, tS0, Stau0 = tau(0), tau(1), tau(0) + 1
assert (t0, tS0, Stau0) == QUOTED["warning_tau"] and tS0 != Stau0
assert sorted(tau(k) for k in range(10)) == list(range(10))
print("ok")
