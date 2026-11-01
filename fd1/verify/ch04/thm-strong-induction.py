"""thm-strong-induction (Ch 4, Section 4.2): the instance before the theorem (14 from 11, three steps back)."""
QUOTED = {"11": "3 \\cdot 2 + 5", "14": "3 \\cdot 3 + 5"}

assert 11 == 3 * 2 + 5 and 14 == 3 * 3 + 5 and 14 - 3 == 11
print("thm-strong-induction: all quoted values check")
