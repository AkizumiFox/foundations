"""exr-equivalence-relations-b3, on representatives 0..29: [a]_n -> [a^2]_n well defined
(n = 1..12); [a]_5 -> [a]_10 not ([0]_5 = [5]_5, [0]_10 != [5]_10); [a]_10 -> [a]_5 well defined."""

QUOTED = {"bad_pair": (0, 5)}

reps = range(30)
def well_defined(m_in, m_out, g=lambda a: a):
    return all((g(a) - g(b)) % m_out == 0 for a in reps for b in reps if (a - b) % m_in == 0)

assert all(well_defined(n, n, lambda a: a * a) for n in range(1, 13))
a, b = QUOTED["bad_pair"]
assert (a - b) % 5 == 0 and (a - b) % 10 != 0
assert not well_defined(5, 10)
assert well_defined(10, 5)
print("exr-equivalence-relations-b3: all quoted values check")
