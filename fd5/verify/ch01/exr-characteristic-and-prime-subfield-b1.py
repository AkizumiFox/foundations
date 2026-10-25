"""exr-characteristic-and-prime-subfield-b1: in F7, 100.[3] = [300] = [6]; 300 = 42*7 + 6;
100 = 14*7 + 2 and 2.[3] = [6]. (a), (b) checked in F_p for small p by brute force."""
QUOTED = {"300": (42, 6), "100": (14, 2), "answer": 6}
q, r = QUOTED["300"]
assert 300 == q * 7 + r and 0 <= r < 7
q2, r2 = QUOTED["100"]
assert 100 == q2 * 7 + r2 and 0 <= r2 < 7
assert (100 * 3) % 7 == QUOTED["answer"] == (2 * 3) % 7
for p in (2, 3, 5, 7, 11, 13):
    for a in range(p):
        assert ((p - 1) * a) % p == (-a) % p
        for k in range(-5, 6):
            for rr in range(-5, 6):
                assert ((k * p + rr) * a) % p == (rr * a) % p
print("ok")
