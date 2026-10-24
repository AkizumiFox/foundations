"""exr-existential-elimination-c3 (Section 5.6, the diagonal of a list): for both lists of (b),
on 0 <= n <= 200, the diagonal set D and the differences between D and A_0, A_1, A_2 at 0, 1, 2;
and, for every m in the window, that D and A_m differ at m (the proof's prediction)."""
N = 200
lists = {
    "k > n": lambda n, k: k > n,
    "multiple of n + 1": lambda n, k: k % (n + 1) == 0,
}
for name, member in lists.items():
    D = {n for n in range(N + 1) if not member(n, n)}
    for m in range(N + 1):
        assert (m in D) != member(m, m)             # D and A_m differ at m
    if name == "k > n":
        assert D == set(range(N + 1))               # D = N
        assert all(m in D and not member(m, m) for m in (0, 1, 2))
    else:
        assert D == set(range(1, N + 1))            # D = {1, 2, 3, ...}
        assert member(0, 0) and 0 not in D          # A_0 = N contains 0, D does not
        assert not member(1, 1) and 1 in D          # A_1 = evens lacks 1
        assert not member(2, 2) and 2 in D          # A_2 = multiples of 3 lacks 2
        assert [k for k in range(7) if member(1, k)] == [0, 2, 4, 6]
        assert [k for k in range(7) if member(2, k)] == [0, 3, 6]
print("exr-existential-elimination-c3: both lists and all differences check")
