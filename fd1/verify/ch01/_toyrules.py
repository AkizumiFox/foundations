"""Shared helper for the Section 1.2 sidecars: the toy rules Tr and Sh, checked by matching.

A line is a string "L < R" (exactly one " < ", spaces around it). Matching is symbol for
symbol, as @def-rule-schema demands: expressions are compared as strings (whitespace
ignored), never evaluated. A derivation is a list of (statement, rule, cited) triples;
rule None marks a premise.
"""


def norm(e):
    return "".join(e.split())


def sides(line):
    parts = line.split(" < ")
    if len(parts) != 2:
        raise ValueError(f"not an inequality a < b: {line!r}")
    return norm(parts[0]), norm(parts[1])


def tr_instance(li, lj, lk):
    """Is (li as a < b, lj as b < c, lk as a < c) an instance of Tr?"""
    a, b = sides(li)
    b2, c = sides(lj)
    return b == b2 and sides(lk) == (a, c)


def sh_instance(li, lk):
    """Is (li as a < b, lk as a + c < b + c) an instance of Sh, for one expression c?"""
    a, b = sides(li)
    l, r = sides(lk)
    if not (l.startswith(a + "+") and r.startswith(b + "+")):
        return False
    return l[len(a) + 1:] == r[len(b) + 1:] != ""


def check_line(deriv, k, rules=("Tr", "Sh")):
    """The three questions of 'Reading a derivation' for line k (1-based).

    Returns (rule_ok, instance_ok, earlier_ok)."""
    stmt, rule, cited = deriv[k - 1]
    rule_ok = rule in rules
    earlier_ok = all(1 <= c < k for c in cited)
    try:
        got = [deriv[c - 1][0] for c in cited]
    except IndexError:
        return rule_ok, False, earlier_ok
    if rule == "Tr":
        inst = len(got) == 2 and tr_instance(got[0], got[1], stmt)
    elif rule == "Sh":
        inst = len(got) == 1 and sh_instance(got[0], stmt)
    elif rule == "Flip":
        inst = len(got) == 1 and sides(stmt) == tuple(reversed(sides(got[0])))
    else:
        inst = False
    return rule_ok, inst, earlier_ok


def is_derivation(deriv, rules=("Tr", "Sh")):
    """Box-free derivation: premises first, then every line passes all three questions."""
    seen_rule = False
    for k, (stmt, rule, cited) in enumerate(deriv, start=1):
        if rule is None:
            if seen_rule:
                return False
            continue
        seen_rule = True
        if not all(check_line(deriv, k, rules)):
            return False
    return len(deriv) >= 1
