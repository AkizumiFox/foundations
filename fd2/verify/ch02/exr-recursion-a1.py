"""exr-recursion-a1 (c): the partial solutions of thm-recursion for a = 1, g(n, x) = (n + 1)x."""
from math import factorial

QUOTED = {
    "G0": {(0, 1)},
    "G1": {(0, 1), (1, 1)},
    "G2": {(0, 1), (1, 1), (2, 2)},
}


def partial(n, a=1, g=lambda k, x: (k + 1) * x):
    graph, val = {(0, a)}, a
    for k in range(n):
        val = g(k, val)
        graph.add((k + 1, val))
    return graph


for n in range(3):
    assert partial(n) == QUOTED[f"G{n}"], n
# the graphs extend one another, and f(n) = n!
for n in range(30):
    assert partial(n) <= partial(n + 1)
    assert dict(partial(n))[n] == factorial(n)
print("ok")
