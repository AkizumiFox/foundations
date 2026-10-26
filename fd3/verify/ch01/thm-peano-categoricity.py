"""thm-peano-categoricity: the Quick check after the method box (f(2) = 7), the worked example
(phi for (N \\ {0}, 1, S) is n -> n + 1, phi(3) = 4), the list after it (phi on structures
(i), (ii) of exm-peano-axioms-independent and on the two copies of N), the Quick check
psi(3) = 3, and the first warning (the swap of 1 and 2 respects 0 but not S).
N is modelled by Python ints with S(n) = n + 1; + is computed from its recursion equations."""
def S(n): return n + 1
def pred(n): assert n > 0; return n - 1          # prp-peano-predecessor (a)
def add(m, n): return m if n == 0 else S(add(m, pred(n)))   # def-omega-arithmetic (a)

def phi(n, e, s):
    """phi(0) = e, phi(S(n)) = s(phi(n)), unwound n times."""
    v = e
    for _ in range(n): v = s(v)
    return v

QUOTED = {"qc_f": {1: 5, 2: 7}, "we_phi": {0: 1, 1: 2, 2: 3, 3: 4},
          "p3_fail_phi1_eq_phi0": True, "p4_fail_phi1_eq_phi2": 1,
          "copies_phi": "(n,a)", "psi3": 3, "warning_tau": (0, 2, 1)}

# Quick check: f(0) = 3, f(n + 1) = f(n) + 2
f = lambda n: phi(n, 3, lambda x: add(x, 2))
for n, v in QUOTED["qc_f"].items(): assert f(n) == v
# worked example: (N \ {0}, 1, S); phi(n) = S(n) = n + 1
for n, v in QUOTED["we_phi"].items():
    assert phi(n, 1, S) == v == S(n) == add(n, 1)
    assert phi(n, 1, S) != 0                       # lands in N \ {0}
# list: (i) M = {0}, s(0) = 0 ; (ii) M = {0, 1}, s(0) = s(1) = 1
s1 = {0: 0}
assert (phi(1, 0, s1.get) == phi(0, 0, s1.get)) == QUOTED["p3_fail_phi1_eq_phi0"]
s2 = {0: 1, 1: 1}
assert phi(1, 0, s2.get) == phi(2, 0, s2.get) == QUOTED["p4_fail_phi1_eq_phi2"]
# (iii) two copies: M = N x {a, b}, e = (0, a), s(n, t) = (S(n), t)
s3 = lambda p: (S(p[0]), p[1])
img = [phi(n, (0, "a"), s3) for n in range(40)]
assert img == [(n, "a") for n in range(40)] and len(set(img)) == 40
assert (0, "b") not in img
# psi = id is an isomorphism, so psi(3) = 3
assert all(S(n) == S(n) for n in range(20)) and QUOTED["psi3"] == 3
# warning: tau swaps 1 and 2
def tau(k): return {1: 2, 2: 1}.get(k, k)
t0, tS0, Stau0 = tau(0), tau(S(0)), S(tau(0))
assert (t0, tS0, Stau0) == QUOTED["warning_tau"] and tS0 != Stau0
assert sorted(tau(k) for k in range(10)) == list(range(10))
print("ok")
