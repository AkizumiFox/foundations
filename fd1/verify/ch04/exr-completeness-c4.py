"""exr-completeness-c4 (Section 4.8, strike out or-I): with or read as and, every primitive
rule other than or-I preserves truth, checked exhaustively in the form the proof of
thm-soundness uses (m: the context is true); or-I fails; the two countervaluations of (c)."""
import itertools

B = (True, False)
imp = lambda a, b: (not a) or b
OR = lambda a, b: a and b          # the new reading
for m, x, y, z in itertools.product(B, repeat=4):
    if m and x and y: assert x and y                                  # and-I
    if m and (x and y): assert x and y                                # and-E
    if m and imp(x, y) and x: assert y                                # ->E
    if m and (x == y) and x: assert y                                 # <->E
    if m and x and (not x): assert False                              # not-E (vacuous)
    if m and imp(m and x, y): assert imp(x, y)                        # ->I
    if m and imp(m and x, False): assert not x                        # not-I
    if m and imp(m and (not x), False): assert x                      # RAA
    if m and imp(m and x, y) and imp(m and y, x): assert x == y       # <->I
    if m and OR(x, y) and imp(m and x, z) and imp(m and y, z): assert z   # or-E, new reading
assert any(x and not OR(x, y) for x, y in itertools.product(B, repeat=2))   # or-I fails
assert not OR(True, False)                         # p true, q false: p or q false
assert all(not OR(x, not x) for x in B)            # p or not p false under every valuation
print("exr-completeness-c4: all quoted values check")
