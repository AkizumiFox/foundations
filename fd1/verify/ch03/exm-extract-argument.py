"""exm-extract-argument (Ch 3 s03): the key's facts F1-F3 hold for every integer (checked for |n| <= 500),
with their reasons; the sequent of the example (and of exm-two-columns and its Quick check) is valid."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _s05s06_logic import *  # noqa: E402,F401,F403

QUOTED = {"bound": 500, "only_even_prime": 2, "only_prime_multiple_of_3": 3, "lines": 16}


def prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


rng = range(-QUOTED["bound"], QUOTED["bound"] + 1)
for n in rng:
    E, Pr, T, G = n % 2 == 0, prime(n), n % 3 == 0, n > 10
    assert not (Pr and E) or not G          # F1
    assert not (Pr and T) or not G          # F2
    assert not (E and T) or not Pr          # F3
assert [n for n in rng if prime(n) and n % 2 == 0] == [QUOTED["only_even_prime"]]
assert [n for n in rng if prime(n) and n % 3 == 0] == [QUOTED["only_prime_multiple_of_3"]]
# F3's reason: a positive multiple of 6 has divisor 2 and exceeds 2
assert all(n % 2 == 0 and n > 2 for n in rng if n > 0 and n % 6 == 0)

E, P, T, G = V("E"), V("P"), V("T"), V("G")
F1, F2, F3 = Imp(And(P, E), Not(G)), Imp(And(P, T), Not(G)), Imp(And(E, T), Not(P))
assert classically_valid([And(P, G), F1, F2], And(Not(E), Not(T)))
assert classically_valid([F1, F2], Imp(And(P, G), And(Not(E), Not(T))))      # the aftermath
assert classically_valid([F3], Imp(And(E, P), Not(T)))                        # exm-two-columns
assert classically_valid([F1], Imp(And(E, P), Not(G)))                        # its Quick check
# the Quick check of the key: "an odd prime greater than 10"
assert any(not (n % 2 == 0) and prime(n) and n > 10 for n in rng)
print("exm-extract-argument: ok")
