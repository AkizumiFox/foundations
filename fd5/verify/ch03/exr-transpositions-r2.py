"""exr-transpositions-r2: powers of [3] mod 7: [1],[3],[2],[6],[4],[5]; [3]^6 = [1]; [k] -> [3]^k
is a well-defined bijective homomorphism Z/6Z -> (Z/7Z)^x; [x]_6 -> ([x]_2, [x]_3) bijective, additive;
1 = 3*1 + 2*(-1)."""
QUOTED = {"powers": [1, 3, 2, 6, 4, 5]}
assert [pow(3, k, 7) for k in range(6)] == QUOTED["powers"] and pow(3, 6, 7) == 1
assert [9 - 7, 6, 18 - 14, 12 - 7, 15 - 14] == [2, 6, 4, 5, 1]
assert sorted(QUOTED["powers"]) == [1, 2, 3, 4, 5, 6]
for k in range(-30, 30):
    assert pow(3, k % 6, 7) == (pow(3, k, 7) if k >= 0 else pow(pow(3, -1, 7), -k, 7))
for k in range(6):
    for l in range(6):
        assert pow(3, (k + l) % 6, 7) == pow(3, k, 7) * pow(3, l, 7) % 7
crt = {x: (x % 2, x % 3) for x in range(6)}
assert len(set(crt.values())) == 6
for x in range(6):
    for y in range(6):
        assert crt[(x + y) % 6] == ((crt[x][0] + crt[y][0]) % 2, (crt[x][1] + crt[y][1]) % 3)
assert 3 * 1 + 2 * (-1) == 1
print("ok")
