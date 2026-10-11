"""exm-square-even-via-contrapositive (Ch 2, Section 2.3): (E3) (2k+1)^2 = 2(2k^2+2k)+1;
n^2 even implies n even. The comparison paragraph after the example: Section 2.1's derivation
after thm-square-even-implies-even has twelve lines, its odd case is the box 6-10 (line 7 gets T
from (E3), lines 8-9 build S and T and clash with (E2)), and line 11 is the case split over 5-11."""
import re, pathlib

QUOTED = {}

for k in range(-500, 501):
    assert (2 * k + 1) ** 2 == 2 * (2 * k * k + 2 * k) + 1
for n in range(-1000, 1001):
    if (n * n) % 2 == 0:
        assert n % 2 == 0

s01 = pathlib.Path("src/ch02-negation-and-classical-logic/01-contradiction-and-vacuous-truth.md").read_text()
blk = s01.split("{#thm-square-even-implies-even}")[1].split("\\end{nd}")[0].split("\\begin{nd}")[1]
lines = dict(re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}\s*\{([^}]*(?:\{[^}]*\}[^}]*)*)\}", blk))
assert len(lines) == 12, lines
assert lines["6"].strip() == "O" and lines["7"].strip() == "T"
assert "S \\wedge T" in lines["8"] and "\\bot" in lines["9"] and lines["10"].strip() == "E"
assert re.search(r"\{11\}\s*\{E\}\s*\\oe\{1,5-5,6-10\}", blk)

s03 = pathlib.Path("src/ch02-negation-and-classical-logic/03-derived-rules.md").read_text()
blk3 = s03.split("{#exm-square-even-via-contrapositive}")[1].split("\\end{nd}")[0]
assert len(re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", blk3)) == 13
print("exm-square-even-via-contrapositive: all quoted values check")
