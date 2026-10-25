"""exr-contrapositive-and-contradiction-b4 (F2.2 §04): (a) false at n = 2; (b) true, its look-alike false at 2;
(c) false at sqrt 2; (e) a^2 - b^2 != 10; (f) false, 89 is the smallest counterexample; 91 = 7*13, 93 = 3*31, 95 = 5*19."""
def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, int(p ** 0.5) + 1))
assert (2 * 2 - 1) % 5 != 0 and 2 % 5 != 0
for n in range(-2000, 2000):
    if (n * n) % 4:
        assert n % 2 == 1
assert (2 * 2) % 4 == 0 and 2 % 4 != 0
for a in range(1, 300):
    for b in range(1, 300):
        assert a * a - b * b != 10
assert 10 % 4 == 2
assert 91 == 7 * 13 and 93 == 3 * 31 and 95 == 5 * 19
assert not any(is_prime(k) for k in range(90, 96))
bad = [n for n in range(0, 200) if not any(is_prime(p) for p in range(n + 1, n + 7))]
assert bad[0] == 89
print("exr-contrapositive-and-contradiction-b4: all quoted values check")
