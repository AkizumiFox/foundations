"""prp-subgroup-generated-by-element (examples): <[2]> = {[0],[2],[4]} in Z/6Z with 3.[2] = [0];
<[2]> = {[1],[2],[4]} and <[3]> = (Z/7Z)^x in (Z/7Z)^x, with the listed powers;
the reduction g^n = g^r for n = qm + r when g^m = e."""
QUOTED = {"z6": {0, 2, 4}, "two7": {1, 2, 4}, "three7_powers": [3, 2, 6, 4, 5, 1]}
mult6 = {(k * 2) % 6 for k in range(-30, 31)}
assert mult6 == QUOTED["z6"] and (3 * 2) % 6 == 0
assert [(k * 2) % 6 for k in range(3)] == [0, 2, 4]

def pw(a, n, p=7):
    return pow(a, n, p) if n >= 0 else pow(pow(a, -1, p), -n, p)

assert {pw(2, n) for n in range(-20, 21)} == QUOTED["two7"] and pow(2, 3) == 8 and 8 % 7 == 1
assert [pow(3, k, 7) for k in range(1, 7)] == QUOTED["three7_powers"]
assert 6 * 3 == 18 and 18 % 7 == 4
assert {pw(3, n) for n in range(-20, 21)} == set(range(1, 7))
# reduction: if g^m = e then g^n = g^(n mod m)
for a in range(1, 7):
    m = next(k for k in range(1, 7) if pow(a, k, 7) == 1)
    for n in range(-30, 31):
        assert pw(a, n) == pow(a, n % m, 7)
print("prp-subgroup-generated-by-element: ok")
