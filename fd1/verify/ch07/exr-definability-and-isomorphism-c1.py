"""exr-definability-and-isomorphism-c1 (Section 7.5): shifts of Z preserve < (window);
x < y and nothing strictly between iff y = x + 1 (window)."""
Z = range(-25, 26)
for k in (-7, 1, 13):
    assert all((d < e) == (d + k < e + k) for d in Z for e in Z)
for x in Z:
    for y in Z:
        f = x < y and not any(x < z < y for z in range(-30, 31))
        assert f == (y == x + 1)
print("exr-definability-and-isomorphism-c1: all quoted values check")
