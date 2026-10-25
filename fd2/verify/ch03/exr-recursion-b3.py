QUOTED = {"first": [0, 1, 3, 7, 15]}
a = [0]
for _ in range(60):
    a.append(2 * a[-1] + 1)
assert a[:5] == QUOTED["first"] and all(a[n] == 2**n - 1 for n in range(61))
print("ok")
