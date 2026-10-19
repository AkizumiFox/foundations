"""exr-derivations-a2 (Section 1.2, drill bank of fifteen parts): parts (a), (f), (g), (h), (k)
with the toy rule Tr, checked by matching; parts (b)-(e), (i), (j), (l)-(o) with a small
and-I/and-E matcher (and-I in either order)."""
import pathlib
import sys
from fractions import Fraction
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from _toyrules import check_line, is_derivation, tr_instance

QUOTED = {
    "(a) new line": "2 < z",
    "(k) chain": (Fraction(0), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2)),
    "(h) failing question": 2,
    "(h) clashing middles": (2, 0),
}

# (a) Tr 1, 2 on 2 < y, y < z writes 2 < z
assert tr_instance("2 < y", "y < z", QUOTED["(a) new line"])
# (f) middles 3 and 4 differ: no instance, though u < v follows since 3 < 4
assert not tr_instance("u < 3", "4 < v", "u < v") and 3 < 4
# (g) premises 0 < x, x < 3, 3 < y: "0 < y, Tr 1, 3" fails the instance question only
prem = [("0 < x", None, ()), ("x < 3", None, ()), ("3 < y", None, ())]
assert check_line(prem + [("0 < y", "Tr", (1, 3))], 4, ("Tr",)) == (True, False, True)
# (k) the chain and its derivation
ch = QUOTED["(k) chain"]
assert all(ch[i] < ch[i + 1] for i in range(3))
d = [("0 < 1/4", None, ()), ("1/4 < 1/3", None, ()), ("1/3 < 1/2", None, ()),
     ("0 < 1/3", "Tr", (1, 2)), ("0 < 1/2", "Tr", (4, 3))]
assert is_derivation(d, ("Tr",))
# (h) "0 < 2, Tr 2, 1": rule named, lines earlier, no instance (b would be 2 and 0)
e = [("0 < 1", None, ()), ("1 < 2", None, ()), ("0 < 2", "Tr", (2, 1))]
assert check_line(e, 3, ("Tr",)) == (True, False, True)
assert QUOTED["(h) failing question"] == 2
b_from_line2 = "1 < 2".split(" < ")[1]
b_from_line1 = "0 < 1".split(" < ")[0]
assert (int(b_from_line2), int(b_from_line1)) == QUOTED["(h) clashing middles"]

# --- a tiny matcher for and-I / and-E on formulas as nested tuples ('and', l, r)
def andE(src, new):
    return isinstance(src, tuple) and src[0] == "and" and new in (src[1], src[2])

def andI(x, y, new):
    return new in (("and", x, y), ("and", y, x))

P, Q, R, S = "P", "Q", "R", "S"
A = lambda l, r: ("and", l, r)
# (i) not P and Q: main connective and (not binds tightest)
negP = ("not", P)
assert andE(A(negP, Q), negP) and andE(A(negP, Q), Q)
# (j) lines 1 P&(Q&R), 2 S, 3 Q&R
l1, l2, l3 = A(P, A(Q, R)), S, A(Q, R)
assert andI(l3, l2, A(A(Q, R), S))          # (i) yes
assert not andI(l3, l2, A(Q, S))            # (ii) no
assert not andE(l1, R)                      # (iii) no
assert andE(l3, R)                          # (iv) yes
# (l) P&Q, R |- R&P
assert andE(A(P, Q), P) and andI(R, P, A(R, P))
# (m) (P&Q)&R |- Q
assert andE(A(A(P, Q), R), A(P, Q)) and andE(A(P, Q), Q)
# (n) P&Q, R&S |- S&P
assert andE(A(P, Q), P) and andE(A(R, S), S) and andI(S, P, A(S, P))
# (o) P&(Q&R) |- R in two rounds of and-E
assert andE(l1, A(Q, R)) and andE(A(Q, R), R) and not andE(l1, R)
# (b) exactly two statements from ((P&Q)&R)&S
top = A(A(A(P, Q), R), S)
cands = [P, Q, R, S, A(P, Q), A(A(P, Q), R), top]
assert [c for c in cands if andE(top, c)] == [S, A(A(P, Q), R)]
assert not any(andE(top, c) for c in [A(P, Q), P, Q, R])
# (c) (P or Q) & (Q -> R): and-E gives exactly the two conjuncts
PvQ, QtoR = ("or", P, Q), ("imp", Q, R)
c3 = A(PvQ, QtoR)
assert [c for c in [P, Q, R, PvQ, QtoR, c3] if andE(c3, c)] == [PvQ, QtoR]
# (d) line 6 (R -> S) & P by and-I 2, 4 with line 4 = P: line 2 is R -> S (and only that)
RtoS = ("imp", R, S)
cands2 = [RtoS, P, R, S, A(RtoS, P)]
assert [x for x in cands2 if andI(x, P, A(RtoS, P))] == [RtoS]
# (e) fill the justifications: (P&Q)&R; P&Q; R; Q; R&Q; (R&Q)&(P&Q)
e1, e2, e3, e4 = A(A(P, Q), R), A(P, Q), R, Q
e5, e6 = A(R, Q), A(A(R, Q), A(P, Q))
assert andE(e1, e2) and andE(e1, e3) and andE(e2, e4)
assert andI(e3, e4, e5) and andI(e4, e3, e5) and andI(e5, e2, e6)
cites = {2: (1,), 3: (1,), 4: (2,), 5: (3, 4), 6: (5, 2)}
assert sum(c.count(2) for c in cites.values()) == 2      # line 2 is cited twice
print("exr-derivations-a2: all checks pass")
