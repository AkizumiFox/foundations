"""thm-irrational-power-rational (Ch 5, Section 5.7): Case 2 computes
(sqrt2^sqrt2)^sqrt2 = sqrt2^(sqrt2*sqrt2) = sqrt2^2 = 2; s = sqrt2^sqrt2 is a positive real.
Also the meta-claim after the proof: LEM is the first line and the only classical tag."""
import pathlib
import re
from decimal import Decimal, getcontext

QUOTED = {"case2_value": 2, "exponent_product": 2}

getcontext().prec = 80
r2 = Decimal(2).sqrt()
s = r2 ** r2
assert s > 0
assert abs(r2 * r2 - QUOTED["exponent_product"]) < Decimal(10) ** -70
assert abs(s ** r2 - QUOTED["case2_value"]) < Decimal(10) ** -60
assert abs(r2 ** (r2 * r2) - 2) < Decimal(10) ** -60
assert 1 < s < 2  # s is not an integer; not a proof of irrationality, only a sanity check

src = pathlib.Path("src/ch05-from-derivations-to-prose/07-excluded-middle.md").read_text()
blk = src.split("{#thm-irrational-power-rational .optional}")[1]
proof = blk.split("::: {.proof}")[1].split("\n:::\n")[0]
tags = re.findall(r"\[\\\( \\rulename\{([^}]*)\} \\\)\]", proof)
assert tags[0] == "LEM", tags
assert tags.count("LEM") == 1 and "RAA" not in tags, tags
print("thm-irrational-power-rational: all quoted values check")
