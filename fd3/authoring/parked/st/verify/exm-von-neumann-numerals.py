"""exm-von-neumann-numerals and the Quick checks / worked move of ch09 s03 (finite sets as frozensets)."""
F = frozenset
E = F()

QUOTED = {
    "elements": {1: [0], 2: [0, 1], 3: [0, 1, 2], 4: [0, 1, 2, 3]},
    # the text says "eight pairs of braces around eight copies of the empty set" in words
    "4 needs eight pairs of braces and eight copies of emptyset": True,
    "not_inductive_witness": {"{0}": 0, "{0,1,2}": 2},   # x with S(x) missing
}

def S(x):
    return F(x | {x})

num = [E]
for _ in range(8):
    num.append(S(num[-1]))

# element lists
for n, els in QUOTED["elements"].items():
    assert num[n] == F(num[k] for k in els)
# the pattern n = {0, ..., n-1} for the first numerals
for n in range(len(num)):
    assert num[n] == F(num[:n])
# distinctness
assert len(set(num)) == len(num)

# counting braces and emptysets when written out
def braces(x):
    return 0 if x == E else 1 + sum(braces(y) for y in x)
def empties(x):
    return 1 if x == E else sum(empties(y) for y in x)
assert braces(num[4]) == 8
assert empties(num[4]) == 8

# Quick check: {emptyset} and {0,1,2} are not inductive, failing at the quoted x
for name, k in QUOTED["not_inductive_witness"].items():
    A = F([num[0]]) if name == "{0}" else F(num[:3])
    assert num[0] in A
    assert num[k] in A and S(num[k]) not in A
    # and the witness is the only failure
    assert [x for x in A if S(x) not in A] == [num[k]]

# warning: S({1}) = {1, {1}} does not contain 0, while numerals 1..7 do
x = F([num[1]])
assert S(x) == F([num[1], F([num[1]])])
assert num[0] not in S(x)
assert all(num[0] in num[n] for n in range(1, len(num)))

# worked move: every n is 0, 1, or has 1 as an element; first with 1 in n is 2
assert all(n == num[0] or n == num[1] or num[1] in n for n in num)
assert min(i for i, n in enumerate(num) if num[1] in n) == 2

# B1: S(x) != emptyset for these x; A1 (b): 2 subset of 3 and 2 in 3
assert all(S(n) != E for n in num)
assert num[2] <= num[3] and num[2] in num[3]
# C1: every numeral is 0, 1 or S(S(k)) with k a numeral
assert all(n in (num[0], num[1]) or any(n == S(S(k)) for k in num) for n in num)
print("ok")
