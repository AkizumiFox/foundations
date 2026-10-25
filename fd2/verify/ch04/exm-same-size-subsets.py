"""exm-same-size-subsets: the eight subsets of {1, 2, 3}, grouped by number of elements
(bijections exist exactly between subsets of equal size), give four classes of sizes 1, 3, 3, 1:
{emptyset}, the singletons, the pairs, {1, 2, 3}."""
from itertools import combinations, product

QUOTED = {"class_sizes": [1, 3, 3, 1]}

X = (1, 2, 3)
subsets = [frozenset(c) for r in range(4) for c in combinations(X, r)]
assert len(subsets) == 8

def equinumerous(A, B):
    """Whether some map A -> B is a bijection (brute force over all maps)."""
    A, B = sorted(A), sorted(B)
    for img in product(B, repeat=len(A)):
        if len(set(img)) == len(A) and set(img) == set(B):
            return True
    return False

classes = []
for S in subsets:
    for C in classes:
        if equinumerous(S, C[0]):
            C.append(S); break
    else:
        classes.append([S])
assert [len(C) for C in classes] == QUOTED["class_sizes"]
assert [sorted(len(S) for S in C) for C in classes] == [[0], [1] * 3, [2] * 3, [3]]
print("exm-same-size-subsets: all quoted values check")
