"""The Quick check after def-sequent (Section 1.1): the witness n = 2 for P -> Q, Q |- P."""
QUOTED = {"witness n": 2}
n = QUOTED["witness n"]
# first premise "if n is divisible by 4 then n is even" holds for every integer (sampled)
assert all((m % 4 != 0) or (m % 2 == 0) for m in range(-1000, 1001))
assert n % 2 == 0          # second premise: n is even
assert n % 4 != 0          # conclusion fails: n is not divisible by 4
# the correct form: divisible by 6 implies divisible by 3
assert all((m % 6 != 0) or (m % 3 == 0) for m in range(-1000, 1001))
print("def-sequent: witness checks")
