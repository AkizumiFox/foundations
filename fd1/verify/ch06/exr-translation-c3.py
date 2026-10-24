"""exr-translation-c3 (Section 6.1): the witness N0 + M0 and the parity counter-reading."""

QUOTED = {"even witness": "2M", "odd witness": "2N + 1"}

R = range(0, 51)
for N0 in R:
    for M0 in R:
        t = N0 + M0
        assert t >= 0 and t >= N0 and t >= M0
even = lambda n: n % 2 == 0
B = range(0, 200)
# (b): premise of the converse true (2M >= M is even), conclusion false (2N + 1 >= N is odd)
assert all(2 * M >= M and even(2 * M) for M in B)
assert all(2 * N + 1 >= N and not even(2 * N + 1) for N in B)
# the premise of (a) is true under some reading, e.g. P(n): n >= 5, and then so is its conclusion
P = lambda n: n >= 5
assert all(any(n >= M and P(n) for n in range(M, M + 10)) for M in B)
print("exr-translation-c3: all quoted values check")
