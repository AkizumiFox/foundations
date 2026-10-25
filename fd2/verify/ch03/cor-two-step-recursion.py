"""cor-two-step-recursion example: a0 = 2, a1 = 3, a_{n+2} = 3 a_{n+1} - 2 a_n."""
QUOTED = {"first": [2, 3, 5, 9, 17]}

a = [2, 3]
for n in range(60):
    a.append(3 * a[n + 1] - 2 * a[n])
assert a[:5] == QUOTED["first"]
assert all(a[n] == 2**n + 1 for n in range(len(a)))
# the step algebra: 3(2^(n+1)+1) - 2(2^n+1) = 2^(n+2)+1
assert all(3 * (2**(n + 1) + 1) - 2 * (2**n + 1) == 2**(n + 2) + 1 for n in range(60))
# quick check: a0 = a1 = 1, a_{n+2} = a_{n+1} a_n is constantly 1
_a = [1, 1]
for _n in range(50):
    _a.append(_a[-1] * _a[-2])
assert all(v == 1 for v in _a)
print("ok")
