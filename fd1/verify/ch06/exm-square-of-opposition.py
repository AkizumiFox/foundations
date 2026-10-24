"""exm-square-of-opposition (Section 6.2) and its Quick check: the four corners over N
(checked on 0..100), with S = multiple of 4 and P = perfect square; then S = odd multiple
of 4, which is empty, so A and E are true and I and O false."""
N = range(0, 101)
squares = {k * k for k in range(0, 11)}
def corners(S, P):
    A = all(P(n) for n in N if S(n))
    E = all(not P(n) for n in N if S(n))
    I = any(S(n) and P(n) for n in N)
    O = any(S(n) and not P(n) for n in N)
    return A, E, I, O
S = lambda n: n % 4 == 0
P = lambda n: n in squares
assert corners(S, P) == (False, False, True, True)
assert S(8) and not P(8)            # A false at 8, O true at 8
assert S(4) and P(4) and 4 == 2 ** 2  # E false at 4, I true at 4
assert S(16) and 16 == 4 * 4 == 4 ** 2  # Quick check: I true at 16
# each diagonal joins a true corner to a false one
A, E, I, O = corners(S, P)
assert A != O and E != I
S_odd = lambda n: n % 4 == 0 and n % 2 == 1
assert not any(S_odd(n) for n in N)
assert corners(S_odd, P) == (True, True, False, False)
print("exm-square-of-opposition: ok")
