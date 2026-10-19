"""exr-soundness-c4 (Section 4.7, bot read as a letter): letter valuations w, with w(bot)
free and w(not phi) = T iff w(phi) = F or w(bot) = T. Every primitive rule other than bot-E
and RAA preserves |=_l, checked exhaustively over all value combinations in the form the
proof uses (m: the context is true); bot-E and RAA fail; the countervaluation of (b); and
the RAA derivation of bot |- p by tools/check_fitch.py on a capital-letter copy."""
import itertools
import sys
sys.path.insert(0, "verify/ch04")
import _s0708_lib as H

B = (True, False)
imp = lambda a, b: (not a) or b
for m, x, y, z, bot in itertools.product(B, repeat=5):
    neg = lambda a: (not a) or bot
    # and-I, and-E, or-I, ->E, <->E
    if m and x and y: assert x and y
    if m and (x and y): assert x and y
    if m and x: assert x or y
    if m and imp(x, y) and x: assert y
    if m and (x == y) and x: assert y
    # not-E: line k is bot
    if m and x and neg(x): assert bot
    # ->I, <->I, or-E (boxes: m and assumption -> last line)
    if m and imp(m and x, y): assert imp(x, y)
    if m and imp(m and x, y) and imp(m and y, x): assert x == y
    if m and (x or y) and imp(m and x, z) and imp(m and y, z): assert z
    # not-I: box from phi to bot
    if m and imp(m and x, bot): assert neg(x)
# bot-E fails: w(bot) = T, w(p) = F
assert any(m and bot and not z for m, bot, z in itertools.product(B, repeat=3))
# RAA fails: box from not p to bot holds (every negation true when bot is T), p false
bot, x, m = True, False, True
neg = lambda a: (not a) or bot
assert m and imp(m and neg(x), bot) and not x
# (b): w(bot) = T, w(p) = F makes bot true and p false
H.check(H.block(H.S07, "exr-soundness-c4"), derivations=1)
print("exr-soundness-c4: all quoted values check")
