"""exr-gaps-in-the-rationals-r5: f(a, b) = (a, b) if b <= a, else (b, a), respects
(a, b) ~ (c, d) iff a + d = b + c, checked on N x N with entries <= 20; the case match
b <= a iff d <= c; the induced map is the absolute value (the class of (a, b) is a - b)."""
QUOTED = {"bound": 20}
N = range(QUOTED["bound"] + 1)
f = lambda a, b: (a, b) if b <= a else (b, a)
sim = lambda x, y: x[0] + y[1] == x[1] + y[0]
pairs = [(a, b) for a in N for b in N]
for x in pairs:
    for y in pairs:
        if sim(x, y):
            assert (x[1] <= x[0]) == (y[1] <= y[0])
            assert sim(f(*x), f(*y))
for a, b in pairs:
    fa, fb = f(a, b)
    assert fa - fb == abs(a - b)
print("ok")
