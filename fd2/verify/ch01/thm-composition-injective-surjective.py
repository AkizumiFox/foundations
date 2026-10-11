"""thm-composition-injective-surjective, and exercises B2, C1, C2 of Ch 6 Section 6.4:
brute force over all functions between sets of sizes 0..3."""
import sys
sys.path.insert(0, "verify/ch06")
from _sets import functions, injective, surjective

QUOTED = {"statements checked": True}

sets = [set(range(n)) for n in range(4)]
for X in sets:
    for Y in sets:
        for Z in sets:
            for f in functions(X, Y):
                for g in functions(Y, Z):
                    gf = {x: g[f[x]] for x in X}
                    if injective(f) and injective(g):
                        assert injective(gf)
                    if surjective(f, Y) and surjective(g, Z):
                        assert surjective(gf, Z)
                    if injective(gf):          # C1 (a)
                        assert injective(f)
                    if surjective(gf, Z):      # B2
                        assert surjective(g, Z)
# the C1/C2 example
f = {1: 1}
g = {1: 1, 2: 1}
gf = {x: g[f[x]] for x in f}
assert injective(gf) and surjective(gf, {1}) and not injective(g) and not surjective(f, {1, 2})
print("thm-composition-injective-surjective: all statements check")
