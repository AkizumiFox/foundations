"""exm-sqrt2-four-levels (Section 5.3): the irrationality of sqrt 2 at four levels.
Arithmetic lines 11, 12, 15 of level 0; the remark that q = 0 forces p = 0; and the line
counts the text quotes (level 0: 24 lines, level 1: 15 lines; the derivation after
thm-sqrt2-irrational in Section 2.2: 13 lines; exm-uniform-implies-continuous: 11 lines)."""
import re
import sys
from fractions import Fraction as Fr
from pathlib import Path

QUOTED = {"level 0 lines": 24, "level 1 lines": 15, "ch02 derivation lines": 13,
          "ch04 uniform derivation lines": 11, "silent lines": [5, 10, 13, 16, 19, 21, 22, 24],
          "level 3 sentences": 4}

ROOT = Path(__file__).resolve().parents[2]


def nd_blocks(path):
    text = (ROOT / path).read_text()
    return re.findall(r"\\begin\{nd\}(.*?)\\end\{nd\}", text, re.S)


def numbered_lines(block):
    return [int(m) for m in re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", block)]


def block_after(path, marker, k=0):
    text = (ROOT / path).read_text()
    rest = text[text.index(marker):]
    return re.findall(r"\\begin\{nd\}(.*?)\\end\{nd\}", rest, re.S)[k]


SEC = "src/ch05-from-derivations-to-prose/03-levels-of-abbreviation.md"
lv0 = numbered_lines(block_after(SEC, "{#exm-sqrt2-four-levels}", 0))
lv1 = numbered_lines(block_after(SEC, "{#exm-sqrt2-four-levels}", 1))
assert lv0 == list(range(1, QUOTED["level 0 lines"] + 1)), lv0
assert lv1 == list(range(1, QUOTED["level 1 lines"] + 1)), lv1
ch2 = numbered_lines(block_after("src/ch02-negation-and-classical-logic/02-negation-and-contradiction.md",
                                 "{#thm-sqrt2-irrational}", 0))
assert ch2 == list(range(1, QUOTED["ch02 derivation lines"] + 1))
ch4 = numbered_lines(block_after("src/ch04-predicate-logic/10-uniform-continuity-rule-by-rule.md",
                                 "{#exm-uniform-implies-continuous}", 0))
assert ch4 == list(range(1, QUOTED["ch04 uniform derivation lines"] + 1))

# the silent lines: those whose justification is forall-E at the obvious term, and-E,
# or a closing exists-E / forall-I (read off the level-0 block)
b0 = block_after(SEC, "{#exm-sqrt2-four-levels}", 0)
just = {}
for line in b0.splitlines():
    m = re.search(r"\\(?:hypo|have)\s*\{(\d+)\}", line)
    if m:
        js = re.findall(r"(\\(?:ae|Ae|Ee|Ai|ai|ie|ne|ni|Ei|by))\{", line)
        just[int(m.group(1))] = js[-1] if js and "\\hypo" not in line else None
silent = sorted(n for n, j in just.items() if j in (r"\ae", r"\Ee", r"\Ai")) + [5, 13, 16]
assert sorted(silent) == QUOTED["silent lines"], sorted(silent)
assert just[5] == just[13] == just[16] == r"\Ae"

# arithmetic: p = r q and r^2 = 2 give p^2 = 2 q^2 (p^2 = r^2 q^2 identically)
for r in [Fr(a, b) for a in range(-6, 7) for b in range(1, 6)]:
    for q in range(-5, 6):
        p = r * q
        assert p * p == (r * r) * (q * q)
# p even, p = 2m, p^2 = 2 q^2 gives q^2 = 2 m^2; and p^2 = 2 q^2 has no integer solution but 0
for m in range(-20, 21):
    for q in range(-30, 31):
        if (2 * m) ** 2 == 2 * q * q:
            assert q * q == 2 * m * m
sols = [(p, q) for p in range(-60, 61) for q in range(-60, 61) if p * p == 2 * q * q]
assert sols == [(0, 0)]          # only the pair with both even, as the clash requires
# q = 0 forces p = r q = 0, and 0 is even
assert all(Fr(a, b) * 0 == 0 for a in range(-3, 4) for b in range(1, 4))
print("exm-sqrt2-four-levels: all quoted values check")

# the level-3 text has four sentences, the second beginning "By (L), write"
text = (ROOT / SEC).read_text()
part = text[text.index("{#exm-sqrt2-four-levels}"):]
part = part[part.index("**Level 3.**"):]
para = re.sub(r"\\\(.*?\\\)", "M", part.split("\n\n")[1].lstrip("> "))
sentences = [t for t in re.split(r"(?<=\.)\s+", para.strip()) if t]
assert len(sentences) == QUOTED["level 3 sentences"], sentences
assert sentences[1].startswith("By (L), write")
print("exm-sqrt2-four-levels: level-3 sentence count checks")
