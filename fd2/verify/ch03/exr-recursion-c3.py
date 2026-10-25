"""exr-recursion-c3: Fibonacci identities (re-indexed form) for n <= 25 and the small cases."""
QUOTED = {"first": [0, 1, 1, 2, 3, 5, 8]}
F = [0, 1]
for n in range(80):
    F.append(F[n + 1] + F[n])
assert F[:7] == QUOTED["first"]
for n in range(26):
    assert F[2 * n + 1] == F[n] ** 2 + F[n + 1] ** 2
    assert F[2 * n + 2] == F[n + 1] * (F[n] + F[n + 2])
# quoted small cases
assert F[2] == 1 * (0 + 1) and F[4] == 3 == 1 * (1 + 2) and F[6] == 8 == 2 * (1 + 3)
assert F[1] == 0 + 1 and F[3] == 2 == 1 + 1 and F[5] == 5 == 1 + 4
# marking scheme, alternative route: F_{k+2} = 3F_k - F_{k-2} (k >= 2); G_n = F_n^2 + F_{n+1}^2
# obeys G_{n+1} = 3G_n - G_{n-1}; second identity from F_{2n+3} - F_{2n+1} = F_{n+2}^2 - F_n^2
for k in range(2, 70):
    assert F[k + 2] == 3 * F[k] - F[k - 2]
G = [F[n] ** 2 + F[n + 1] ** 2 for n in range(40)]
for n in range(1, 39):
    assert G[n + 1] == 3 * G[n] - G[n - 1]
for n in range(30):
    assert F[2 * n + 2] == F[2 * n + 3] - F[2 * n + 1] == F[n + 2] ** 2 - F[n] ** 2 == F[n + 1] * (F[n] + F[n + 2])
print("ok")
