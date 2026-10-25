"""exm-uniform-four-levels (Section 5.3): level 0 is the 11-line derivation of
exm-uniform-implies-continuous, copied with the same lines (in the fold "Levels 0 and 2");
level 1 (in the solution) has 10 lines, merging lines 7 and 8; the level-3 text has three
sentences; level 1's closing lines are 8 (exists-E), 9 and 10 (forall-I)."""
import re
from pathlib import Path

QUOTED = {"level 0 lines": 11, "level 1 lines": 10, "level 3 sentences": 3}
ROOT = Path(__file__).resolve().parents[2]
SEC = (ROOT / "src/ch08-from-derivations-to-prose/03-levels-of-abbreviation.md").read_text()
CH4 = (ROOT / "src/ch06-working-with-quantifiers/04-uniform-continuity-rule-by-rule.md").read_text()


def blocks(text, marker):
    return re.findall(r"\\begin\{nd\}(.*?)\\end\{nd\}", text[text.index(marker):], re.S)


def norm(b):
    return [re.sub(r"\s+", " ", l.strip()) for l in b.strip().splitlines() if l.strip()]


lv1, lv0 = blocks(SEC, "{#exm-uniform-four-levels}")[:2]   # level 1 in the solution, level 0 in the fold
orig = blocks(CH4, "{#exm-uniform-implies-continuous}")[0]
assert norm(lv0) == norm(orig)                      # copied verbatim
n0 = re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", lv0)
n1 = re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", lv1)
assert len(n0) == QUOTED["level 0 lines"] and len(n1) == QUOTED["level 1 lines"]
for num, rule in [("8", r"\Ee"), ("9", r"\Ai"), ("10", r"\Ai")]:
    line = [l for l in lv1.splitlines() if re.search(r"\\have\s*\{%s\}" % num, l)][0]
    assert rule in line, (num, line)
# level 3: count the sentences of the quoted paragraph after "**Level 3.**"
part = SEC[SEC.index("{#exm-uniform-four-levels}"):]
part = part[part.index("**Level 3.**"):]
para = part.split("\n\n")[1]
assert para.startswith(">")
plain = re.sub(r"\\\(.*?\\\)", "M", para)
assert plain.count(". ") + plain.rstrip().endswith(".") == QUOTED["level 3 sentences"], plain
print("exm-uniform-four-levels: all quoted values check")
