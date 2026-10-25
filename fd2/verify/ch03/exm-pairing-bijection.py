"""exm-pairing-bijection: the diagonal pairing pi(m, n) = tau_(m+n) + n and its decoder delta.

Also covers Quick check 3 and the example in exr-cardinal-arithmetic-b1 (c)."""

QUOTED = {
    "table": {(0, 0): 0, (1, 0): 1, (0, 1): 2, (2, 0): 3, (1, 1): 4, (0, 2): 5},
    "tau4": 10, "tau5": 15, "delta11": (3, 1),
    "pi32": 17, "tau9": 45, "tau10": 55, "delta47": (7, 2),
    "E101": 4,
}


def tau(s):
    # recursion of def-sum-product: tau_0 = 0, tau_(s+1) = tau_s + s + 1
    t = 0
    for i in range(1, s + 1):
        t += i
    return t


def pi(m, n):
    return tau(m + n) + n


def delta(k):
    # find the unique (s, n) with n <= s and k = tau_s + n, by search
    found, s, t = [], 0, 0
    while t <= k:  # t = tau_s
        if 0 <= k - t <= s:
            found.append((s, k - t))
        s, t = s + 1, t + s + 1
    assert len(found) == 1, (k, found)
    s, n = found[0]
    return (s - n, n)


for s in range(200):
    assert tau(s + 1) == tau(s) + s + 1 and tau(s) == s * (s + 1) // 2
for (m, n), v in QUOTED["table"].items():
    assert pi(m, n) == v
assert tau(4) == QUOTED["tau4"] and tau(5) == QUOTED["tau5"]
assert delta(11) == QUOTED["delta11"]
assert pi(3, 2) == QUOTED["pi32"]
assert tau(9) == QUOTED["tau9"] and tau(10) == QUOTED["tau10"]
assert delta(47) == QUOTED["delta47"] and pi(7, 2) == 47
# both round trips on a range
N = 60
assert all(delta(pi(m, n)) == (m, n) for m in range(N) for n in range(N))
assert all(pi(*delta(k)) == k for k in range(3000))
# pi restricted to the triangle m + n < N hits exactly 0 .. tau_N - 1
vals = sorted(pi(m, n) for m in range(N) for n in range(N) if m + n < N)
assert vals == list(range(tau(N)))
# B1 (c): E(m, n, k) = pi(pi(m, n), k)
E = lambda m, n, k: pi(pi(m, n), k)
assert E(1, 0, 1) == QUOTED["E101"]
def dec3(k):
    j, kk = delta(k)
    m, n = delta(j)
    return (m, n, kk)
assert all(dec3(E(m, n, k)) == (m, n, k) for m in range(8) for n in range(8) for k in range(8))
assert all(E(*dec3(k)) == k for k in range(2000))
print("ok")
