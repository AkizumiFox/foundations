"""def-prime-factorization: the opening's 60, the examples and non-examples, the twelve orderings,
and the Quick check (360) in 03-unique-factorization."""
from itertools import permutations
from math import prod


def is_prime(p):
    return p >= 2 and all(p % d for d in range(2, p))


def partial_products(lst):
    out = [1]
    for x in lst:
        out.append(out[-1] * x)
    return out


def is_factorization(lst, n):
    return (all(is_prime(x) for x in lst)
            and all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
            and prod(lst) == n)


QUOTED = {
    "opening_splits": [(2, 30), (6, 10), (4, 15)],
    "fact60": (2, 2, 3, 5),
    "products60": [1, 2, 4, 12, 60],
    "fact5": (5,),
    "products5": [1, 5],
    "nonex_order": (2, 3, 2, 5),
    "nonex_merge": (2, 2, 15),
    "orderings60": 12,
    "fact360": (2, 2, 2, 3, 3, 5),
    "products360": [1, 2, 4, 8, 24, 72, 360],
}

for a, b in QUOTED["opening_splits"]:
    assert a * b == 60
assert 4 == 2 * 2 and 15 == 3 * 5 and 30 == 2 * 3 * 5 and 10 == 2 * 5 and 6 == 2 * 3
assert is_factorization(QUOTED["fact60"], 60)
assert partial_products(QUOTED["fact60"]) == QUOTED["products60"]
assert is_factorization(QUOTED["fact5"], 5)
assert partial_products(QUOTED["fact5"]) == QUOTED["products5"]
assert is_factorization((), 1)
# non-examples: each fails exactly the named clause
lst = QUOTED["nonex_order"]
assert all(is_prime(x) for x in lst) and prod(lst) == 60 and lst[1] > lst[2]
lst = QUOTED["nonex_merge"]
assert sorted(lst) == list(lst) and prod(lst) == 60 and not is_prime(15) and 15 == 3 * 5
assert len(set(permutations(QUOTED["fact60"]))) == QUOTED["orderings60"]
assert is_factorization(QUOTED["fact360"], 360)
assert partial_products(QUOTED["fact360"]) == QUOTED["products360"]
# uniqueness, brute force for these two
def all_factorizations(n, least=2):
    if n == 1:
        return [()]
    out = []
    for p in range(least, n + 1):
        if n % p == 0 and is_prime(p):
            out += [(p,) + rest for rest in all_factorizations(n // p, p)]
    return out
assert all_factorizations(60) == [QUOTED["fact60"]]
assert all_factorizations(360) == [QUOTED["fact360"]]
print("def-prime-factorization: ok")
