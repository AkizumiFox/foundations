"""exm-characteristics: char Z/pZ = p for primes p < 200 (least positive n with n.[1] = [0]);
for composite n, Z/nZ has characteristic n as a ring. Quick check: char F7 = 7,
7.[3] = [21] = [1] in F5, and 7.[3] = 2.[3] = [6] = [1]. Quick check after
cor-finite-field-prime-characteristic: 2 != 3."""
QUOTED = {"charF7": 7, "check_mod": 5, "check_val": 1, "check_21": 21}


def char(mod):
    s, n = 0, 0
    while True:
        n += 1
        s = (s + 1) % mod
        if s == 0:
            return n


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, n))


for n in range(2, 200):
    assert char(n) == n
    if is_prime(n):
        # char p is the least positive multiple of p
        assert min(k for k in range(1, 3 * n) if k % n == 0) == n
assert char(7) == QUOTED["charF7"]
m = QUOTED["check_mod"]
assert (7 * 3) == QUOTED["check_21"] and 21 % m == QUOTED["check_val"]
assert (2 * 3) % m == QUOTED["check_val"] and (21 - 1) == 4 * 5
print("ok")
