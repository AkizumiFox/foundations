"""exr-negation-and-contradiction-c1 (Ch 2, Section 2.2): p^2 = 6q^2 = 2(3q^2); p = 2m gives
4m^2 = 6q^2, i.e. 3q^2 = 2m^2; q = 2j'+1 odd gives q^2 = 2j+1 and 3q^2 = 6j+3 = 2(3j+1)+1 odd;
no p^2 = 6q^2 in a range."""
QUOTED = {"3(2j+1)": "2(3j+1)+1"}

for m in range(-100, 101):
    for q in range(-100, 101):
        assert ((2 * m) ** 2 == 6 * q * q) == (3 * q * q == 2 * m * m)
        assert 6 * q * q == 2 * (3 * q * q)
for j in range(-500, 501):
    assert 3 * (2 * j + 1) == 6 * j + 3 == 2 * (3 * j + 1) + 1
for q in range(-500, 501):
    if q % 2 == 1:
        assert (q * q) % 2 == 1 and (3 * q * q) % 2 == 1
for q in range(1, 1500):
    for p in range(0, 3 * q):
        assert p * p != 6 * q * q
print("exr-negation-and-contradiction-c1: all quoted values check")
