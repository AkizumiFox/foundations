"""exr-excluded-middle-r3 (Ch 5, Section 5.7): the truth table of (P -> Q) -> Q and P or Q
(rows T before F, last atom fastest), the only row with P or Q false is P = Q = F, where the
premise is T -> F = F; so the entailment holds. The derivation has 11 lines and one RAA, at
line 11; replacing it by not-I gives not-not(P or Q)."""
import pathlib
import re

imp = lambda x, y: (not x) or y
rows = [(True, True), (True, False), (False, True), (False, False)]
table = [(p, q, imp(p, q), imp(imp(p, q), q), p or q) for p, q in rows]
QUOTED = {"table": [
    (True, True, True, True, True),
    (True, False, False, True, True),
    (False, True, True, True, True),
    (False, False, True, False, False),
], "lines": 11, "raa_line": 11}
assert table == QUOTED["table"]
assert [r[:2] for r in table if not r[4]] == [(False, False)]
assert all(r[4] for r in table if r[3])  # valid

src = pathlib.Path("src/ch05-from-derivations-to-prose/07-excluded-middle.md").read_text()
part = src.split("{#exr-excluded-middle-r3}")[1].split("{#exr-excluded-middle-r4}")[0]
arr = part.split("\\begin{array}")[1].split("\\end{array}")[0]
body = [ln for ln in arr.split("\\\\")[1:] if "mathrm" in ln]
tv = lambda c: c.strip().replace("\\hline", "").strip() == "\\mathrm{T}"
parsed = [tuple(tv(c) for c in ln.split("&")) for ln in body]
assert parsed == QUOTED["table"], parsed
blk = part.split("\\begin{nd}")[1].split("\\end{nd}")[0]
nums = re.findall(r"\\(?:hypo|have)\s*\{(\d+)\}", blk)
assert len(nums) == QUOTED["lines"]
assert len(re.findall(r"\\raa\{", blk)) == 1 and re.search(r"\{11\}\s*\{P \\vee Q\}\s*\\raa\{2-10\}", blk)
print("exr-excluded-middle-r3: all quoted values check")
