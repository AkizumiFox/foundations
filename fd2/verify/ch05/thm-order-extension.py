"""5.2 worked schedule before lem-one-step-order-extension: tasks S, F, D, P, B with
S->D, F->D, D->B, F->P. The generated order (reflexive-transitive closure) has 11
pairs, is a partial order; both schedules S,F,D,P,B and F,P,S,D,B contain it and
arise from 'pick a task with no unfinished prerequisite'."""
X = "SFDPB"
base = {("S", "D"), ("F", "D"), ("D", "B"), ("F", "P")}
R = {(x, x) for x in X} | base
while True:
    new = {(x, z) for (x, y) in R for (w, z) in R if y == w} - R
    if not new:
        break
    R |= new
assert len(R) == 11 and R - base - {(x, x) for x in X} == {("S", "B"), ("F", "B")}
assert all(not ((x, y) in R and (y, x) in R) for x in X for y in X if x != y)


def valid(sched):
    pos = {t: i for i, t in enumerate(sched)}
    return all(pos[x] <= pos[y] for x, y in R)


def greedy_possible(sched):
    done = set()
    for t in sched:
        if any((u, t) in base and u not in done for u in X):
            return False
        done.add(t)
    return True


for s in ["SFDPB", "FPSDB"]:
    assert valid(s) and greedy_possible(s)
from itertools import permutations
print("thm-order-extension: ok;", sum(valid(p) for p in permutations(X)), "schedules in all")
