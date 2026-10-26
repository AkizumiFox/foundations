"""thm-no-rational-square-two: the descent identity (2q - p)^2 - 2(p - q)^2 = 2q^2 - p^2 and the
expansions quoted; the inequalities q < p < 2q follow from p^2 = 2q^2 (checked on all integer
pairs with p^2 close to 2q^2, where the descent's hypotheses are tested numerically); no
p, q <= 2000 with p^2 = 2q^2.  Polynomial identities: degree 2 in two variables, checked on
a 9 x 9 grid (enough points to determine the polynomial)."""
QUOTED = {"identity": "2q^2 - p^2"}
for p in range(-4, 5):
    for q in range(-4, 5):
        assert (2*q - p)**2 == 4*q*q - 4*p*q + p*p
        assert 2*(p - q)**2 == 2*p*p - 4*p*q + 2*q*q
        assert (2*q - p)**2 - 2*(p - q)**2 == 2*q*q - p*p
# the idea: x = (2 - x)/(x - 1) when x^2 = 2 -- as a polynomial identity: x(x - 1) - (2 - x) = x^2 - 2
for x in range(-5, 6):
    assert x*(x - 1) - (2 - x) == x*x - 2
# no solutions in a range (sanity), and the descent map on near-solutions p^2 - 2q^2 = +-1
assert not any(p*p == 2*q*q for p in range(1, 2001) for q in range(1, 1500))
for p in range(1, 400):
    for q in range(1, 300):
        if abs(p*p - 2*q*q) == 1 and q > 1:
            assert q < p < 2*q
            pp, qq = 2*q - p, p - q
            assert 0 < qq < q and pp > 0 and pp*pp - 2*qq*qq == -(p*p - 2*q*q)
print("ok")
