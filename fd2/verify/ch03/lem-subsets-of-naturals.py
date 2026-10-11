"""lem-subsets-of-naturals: the increasing listing s_0 = min S, s_{n+1} = min{s in S : s > s_n}
is strictly increasing, s_n >= n, and reaches every t in S (sample infinite S, truncated)."""
QUOTED = {}
LIMIT = 20000
samples = [lambda k: k * k, lambda k: 3 * k + 2, lambda k: 2**k]
for gen in samples:
    S = sorted({gen(k) for k in range(200) if gen(k) < LIMIT})
    Sset = set(S)
    s = [min(S)]
    while True:
        bigger = [x for x in S if x > s[-1]]
        if not bigger:
            break
        s.append(min(bigger))
    assert all(s[i] < s[i + 1] for i in range(len(s) - 1))
    assert all(s[n] >= n for n in range(len(s)))
    for t in S:
        n = min(i for i in range(len(s)) if s[i] >= t)
        assert s[n] == t
print("ok")
