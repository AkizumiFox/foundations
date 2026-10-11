"""exm-write-from-derivation (Ch 5, Section 5.5): the four premises (every integer even or odd;
an even factor makes a product even; odd plus one is even) and the conclusion n(n+1) even;
n = 2k gives n(n+1) = 2(k(n+1))."""
QUOTED = {}
for n in range(-2000, 2001):
    E, O = n % 2 == 0, n % 2 == 1
    G, Fv = (n * (n + 1)) % 2 == 0, (n + 1) % 2 == 0
    assert E or O
    assert (not E) or G          # premise 2
    assert (not O) or Fv         # premise 3
    assert (not Fv) or G         # premise 4
    if E:
        assert G
        k = n // 2
        assert n * (n + 1) == 2 * (k * (n + 1))
    if O:
        assert Fv and G
    assert G
print("exm-write-from-derivation: all quoted values check")
