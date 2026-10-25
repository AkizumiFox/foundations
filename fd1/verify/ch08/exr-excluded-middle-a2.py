"""exr-excluded-middle-a2 (Section 8.7, drill): part (f) hands over the witness 8 for
exists n in N (n^2 > 50), with 8^2 = 64 > 50; 8 is also the least such natural number."""
QUOTED = {"witness": 8, "square": 64, "bound": 50}

n = QUOTED["witness"]
assert n * n == QUOTED["square"] and QUOTED["square"] > QUOTED["bound"]
assert min(k for k in range(100) if k * k > QUOTED["bound"]) == n
print("exr-excluded-middle-a2: all quoted values check")
