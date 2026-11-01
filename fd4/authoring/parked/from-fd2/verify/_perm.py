"""Shared helpers for the 5.4 sidecars (not a check itself)."""


def orbits(f, X):
    """Orbits of a permutation f (dict) on X, each as the list x, f(x), ..."""
    seen, out = set(), []
    for x in X:
        if x in seen:
            continue
        orb, y = [x], f[x]
        while y != x:
            orb.append(y)
            y = f[y]
        seen.update(orb)
        out.append(orb)
    return out


def compose(f, g):
    """f o g (g first)."""
    return {x: f[g[x]] for x in g}


def power(f, n):
    h = {x: x for x in f}
    for _ in range(n):
        h = compose(f, h)
    return h


def least_identity_power(f):
    n, h = 1, dict(f)
    while any(h[x] != x for x in h):
        h = compose(f, h)
        n += 1
    return n


def tail_and_period(f, x, n):
    """m, p for the forward orbit of x (n = number of elements); first repeat."""
    seq = [x]
    for _ in range(n):
        seq.append(f[seq[-1]])
    for j in range(len(seq)):
        for i in range(j):
            if seq[i] == seq[j]:
                return i, j - i, seq
    raise AssertionError("no repeat")
