"""exm-subgroups: {[0],[2],[4]} in Z/6Z and {[1],[3]} in (Z/8Z)^x pass the subgroup test;
{1, i, -1, -i} is closed under products and inverses (Gaussian integers as pairs);
non-examples: 0 - 1 not in N, 2m = 1 has no integer solution."""
QUOTED = {"z6": {0, 2, 4}, "u8": {1, 3}, "four": {(1, 0), (0, 1), (-1, 0), (0, -1)}}
H = QUOTED["z6"]
assert all((a - b) % 6 in H for a in H for b in H)
assert (-2) % 6 == 4 and (-4) % 6 == 2
K = QUOTED["u8"]
inv8 = {a: next(b for b in range(8) if a * b % 8 == 1) for a in K}
assert inv8[3] == 3 and 3 * 3 == 9 and 9 % 8 == 1
assert all(a * inv8[b] % 8 in K for a in K for b in K)

def cmul(z, w):
    a, b = z
    c, d = w
    return (a * c - b * d, a * d + b * c)

F = QUOTED["four"]
assert cmul((0, 1), (0, 1)) == (-1, 0)  # i^2 = -1
assert all(cmul(z, w) in F for z in F for w in F)
assert all(any(cmul(z, w) == (1, 0) for w in F) for z in F)
assert cmul((0, 1), (0, -1)) == (1, 0)
assert 0 - 1 < 0
assert all(2 * m != 1 for m in range(-50, 51))
print("exm-subgroups: ok")
