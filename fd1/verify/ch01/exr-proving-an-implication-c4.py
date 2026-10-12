"""exr-proving-an-implication-c4 (Section 1.4): the dependency sets of the first derivation of
prp-curry (lines 1-7; premise 1; boxes 2-6 and 3-5), computed from the boxes; the two sequents
of (b) valid by truth table; and (c)'s claim on this derivation: each cited line's set is
contained in the citing line's set, and a ->I line's set is its box's last line's set minus the
box's assumption."""
import itertools

PREMISES = {1}
BOXES = [(2, 6), (3, 5)]
QUOTED = {1: {1}, 2: {1, 2}, 3: {1, 2, 3}, 4: {1, 2, 3}, 5: {1, 2, 3}, 6: {1, 2}, 7: {1}}


def depends(k):
    return PREMISES | {a for a, b in BOXES if a <= k <= b}


for k, s in QUOTED.items():
    assert depends(k) == s, (k, depends(k), s)
CITES = {4: [2, 3], 5: [1, 4]}          # and-I 2,3; ->E 1,4
for k, cited in CITES.items():
    for i in cited:
        assert depends(i) <= depends(k)
ARROW_I = {6: (3, 5), 7: (2, 6)}         # ->I lines and the boxes they cite
for k, (a, b) in ARROW_I.items():
    assert depends(k) == depends(b) - {a}

imp = lambda x, y: (not x) or y
for P, Q, R in itertools.product((False, True), repeat=3):
    if imp(P and Q, R) and P and Q:
        assert R                          # line 5's sequent
    if imp(P and Q, R) and P:
        assert imp(Q, R)                  # line 6's sequent
print("exr-proving-an-implication-c4: checks")
