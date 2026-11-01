"""exr-polynomials-as-sequences-a1 (Section 4.1): coefficient sequences and admissible N."""
QUOTED = {
    "a_first": [0, -2, 0, 1],      # x^3 - 2x over Z
    "a_second": [0, 0, 2],         # [2]x^2 + [4]x over Z/4Z, since [4] = [0]
    "d_least_N": 2,                # 3x^2 - x + 2
}
p = {3: 1, 1: -2}
assert [p.get(k, 0) for k in range(4)] == QUOTED["a_first"]
q = {2: 2, 1: 4}
assert [q.get(k, 0) % 4 for k in range(3)] == QUOTED["a_second"]
r = {2: 3, 1: -1, 0: 2}
admissible = [N for N in range(10) if all(r.get(k, 0) == 0 for k in range(N + 1, 20))]
assert admissible[0] == QUOTED["d_least_N"] and admissible == list(range(2, 10))
print("exr-polynomials-as-sequences-a1: ok")
