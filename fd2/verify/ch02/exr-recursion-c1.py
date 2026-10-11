"""exr-recursion-c1: every n >= 1 is 2^k q with q odd; 0 is not."""
QUOTED = {}
for n in range(1, 2001):
    k, q = 0, n
    while q % 2 == 0:
        q //= 2
        k += 1
    assert n == 2**k * q and q % 2 == 1
# 0 = 2^k q forces q = 0, which is even
assert all(0 % (2**k) == 0 for k in range(10))
print("ok")
