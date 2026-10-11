"""def-transitive-set examples and lem-omega-transitive on the first numerals (ch09 s04)."""
F = frozenset
E = F()
def S(x): return F(x | {x})
def transitive(x): return all(y <= x for y in x)
num = [E]
for _ in range(9):
    num.append(S(num[-1]))

TRANSITIVE = ["0", "1", "3", "{0,1,{1}}"]
NOT_TRANSITIVE = ["{0,2}", "{1}"]
QUOTED = {
    "0, 1, 3 and {0, 1, {1}} are transitive": True,
    "{0, 2} and {1} are not transitive": True,
}
named = {
    "0": num[0], "1": num[1], "3": num[3],
    "{0,1,{1}}": F([num[0], num[1], F([num[1]])]),
    "{0,2}": F([num[0], num[2]]),
    "{1}": F([num[1]]),
}
for k in TRANSITIVE:
    assert transitive(named[k]), k
for k in NOT_TRANSITIVE:
    assert not transitive(named[k]), k
# {0,2} fails exactly at 2 (missing 1); {1} fails at 1 (missing 0)
assert [y for y in named["{0,2}"] if not y <= named["{0,2}"]] == [num[2]]
assert num[1] not in named["{0,2}"]
assert num[0] not in named["{1}"]
# {0,1,{1}} is not a numeral, and {1} is not S(k) for any numeral k
assert named["{0,1,{1}}"] not in num and F([num[1]]) not in num
assert all(S(k) != F([num[1]]) for k in num)
# lemma (a), (c), (d), (e) on the numerals
for i, n in enumerate(num):
    assert transitive(n)
    assert n not in n
    assert all(m in num for m in n)            # (b) on these
    if i > 0:
        assert n == S(num[i - 1])              # (d)
        assert E in n                          # (e)
# P4 counterexample to cancelling union: {1} u {0} = {0} u {1}, 0 != 1
assert F([num[1]]) | F([num[0]]) == F([num[0]]) | F([num[1]]) and num[0] != num[1]
# S on the numerals is injective and never 0 (P3), (P4)
assert len({S(n) for n in num}) == len(num) and all(S(n) != E for n in num)
# A1 (c): S(omega) is neither omega nor in omega -- checked on a truncation:
# for every finite initial segment W = {0..N}, S(W) not in W u {W} and S(W) != W
for N in range(1, 8):
    W = F(num[:N])
    assert S(W) != W and S(W) not in W
print("ok")
