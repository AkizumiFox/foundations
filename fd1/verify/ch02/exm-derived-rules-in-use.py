"""exm-derived-rules-in-use (Ch 2, Section 2.3): part (a) is 5 lines with MT twice, and its
natural expansion (each MT line replaced by a four-line box) has eleven lines
(the snapshots before the finished derivations are skipped)."""
import re, pathlib

QUOTED = {}
SHORT, EXPANDED = 5, 11  # the text says "eleven lines"

src = pathlib.Path("src/ch02-negation-and-classical-logic/03-derived-rules.md").read_text()
sol = src.split("{#exm-derived-rules-in-use}")[1].split("::: {.check}")[0]
# finished derivations only: the snapshot blocks are marked "% schema"
raws = [r for r in sol.split("```{=latex}")[1:] if not r.lstrip().startswith("% schema")]
blocks = [r.split("\\begin{nd}")[1] for r in raws]
counts = [len(re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", b.split("\\end{nd}")[0])) for b in blocks]
assert counts[0] == SHORT and counts[1] == EXPANDED, counts
# the expansion: 3 premises + 2 MT lines, each MT line becoming 4 lines
assert 3 + 2 * 4 == EXPANDED
print("exm-derived-rules-in-use: all quoted values check")
