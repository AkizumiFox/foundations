"""def-polynomial (Section 4.1): the hook over F_2 (x^2 + x, x^3 + x, x^4 + x^2 all give
the zero rule on F_2, while their coefficient sequences are non-zero) and the warning
(p = x^2 + 1 in Z[x]: p_2 = 1, value at 2 is 5)."""
QUOTED = {
    "hook_values": (0, 0),          # 0*0 + 0 = 0, 1*1 + 1 = 0 in F_2
    "warning_coef": 1,              # p_2 for p = x^2 + 1
    "warning_value": 5,             # 2*2 + 1
}


def rule(coeffs, c, n):
    """sum_k coeffs[k] c^k computed in Z/nZ, with c^k by repeated multiplication."""
    total, power = 0, 1
    for a in coeffs:
        total = (total + a * power) % n
        power = (power * c) % n
    return total


# x^2 + x, x^3 + x, x^4 + x^2 over F_2: non-zero sequences, zero rule
for coeffs in ([0, 1, 1], [0, 1, 0, 1], [0, 0, 1, 0, 1]):
    assert any(a % 2 for a in coeffs)
    assert tuple(rule(coeffs, c, 2) for c in (0, 1)) == QUOTED["hook_values"]
assert (0 * 0 + 0) % 2 == 0 and (1 * 1 + 1) % 2 == 0
# x(x + 1) = x^2 + x: coefficients of the product (convolution) over Z
p, q = [0, 1], [1, 1]
prod = [sum(p[i] * q[k - i] for i in range(k + 1) if i < len(p) and k - i < len(q)) for k in range(3)]
assert prod == [0, 1, 1]
# warning
p = [1, 0, 1]
assert p[2] == QUOTED["warning_coef"]
assert rule(p, 2, 10**9) == QUOTED["warning_value"] == 2 * 2 + 1
print("def-polynomial: ok")
