"""exr-normal-forms-r2 (Section 3.7): e -> ((a and b) or (not a and not b)), a and not b |= not e."""
from _s0607_lib import entails
QUOTED = {}
assert entails(["e \\to ((a \\wedge b) \\vee (\\neg a \\wedge \\neg b))", "a \\wedge \\neg b"], "\\neg e")
print("exr-normal-forms-r2: all quoted values check")
