"""exm-newton-rationals-sqrt2: x_0..x_3, e_0..e_3, the recurrence e_{n+1} = e_n^2/(4 x_n^2) <= e_n^2/8,
x_n - x_{n+1} = e_n/(2 x_n) > 0, the products 577^2, 408^2, 144*1156, the decimals of the table,
e_3 < 1/100000, and the Quick check (3/2, 17/12 bound A: 9 > 8, 289 > 288)."""
from fractions import Fraction as F
QUOTED = {"x": [F(2), F(3, 2), F(17, 12), F(577, 408)],
          "e": [F(2), F(1, 4), F(1, 144), F(1, 166464)],
          "decimals": ["2", "1.5", "1.41667", "1.414216"],
          "sq577": 332929, "sq408": 166464}
t = lambda s: (s*s + 2) / (2*s)
x = [F(2)]
for n in range(12):
    x.append(t(x[-1]))
e = [xi*xi - 2 for xi in x]
assert x[:4] == QUOTED["x"] and e[:4] == QUOTED["e"]
for n in range(11):
    assert x[n] > 0 and e[n] > 0
    assert e[n+1] == e[n]**2 / (4*x[n]**2) and e[n+1] < e[n]**2 / 8
    assert x[n] - x[n+1] == e[n] / (2*x[n]) > 0
assert 577**2 == QUOTED["sq577"] == 2*166464 + 1 and 408**2 == QUOTED["sq408"] and 144*1156 == 166464
assert x[1] == F(4 + 2, 4) and x[2] == (F(9, 4) + 2) / 3 and x[3] == (F(289, 144) + 2) / F(17, 6)
assert (F(1, 144))**2 / (4*F(289, 144)) == F(1, 166464)
assert e[3] < F(1, 100000)
for xi, d in zip(x[:4], QUOTED["decimals"]):
    digits = len(d.split(".")[1]) if "." in d else 0
    assert abs(F(xi) - F(d)) <= F(1, 2 * 10**digits)   # correctly rounded
assert 9 > 8 and 289 > 288 and F(9, 4) > 2 and F(289, 144) > 2
print("ok")
