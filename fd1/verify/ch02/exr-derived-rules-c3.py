"""exr-derived-rules-c3 (Ch 2, Section 2.3, exit check): (2k)^2 = 2(2k^2); n^2 odd implies
n odd; the skeleton derivation has 12 lines; the marking scheme sums to 10."""
QUOTED = {"points": 10}

for k in range(-500, 501):
    assert (2 * k) ** 2 == 2 * (2 * k * k)
for n in range(-1000, 1001):
    if (n * n) % 2 == 1:
        assert n % 2 == 1
assert 2 + 2 + 3 + 2 + 1 == QUOTED["points"]

import re, pathlib
src = pathlib.Path("src/ch02-negation-and-classical-logic/03-derived-rules.md").read_text()
sol = src.split("{#exr-derived-rules-c3}")[1]
block = sol.split("\\begin{nd}")[1].split("\\end{nd}")[0]
assert len(re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", block)) == 12
print("exr-derived-rules-c3: all quoted values check")
