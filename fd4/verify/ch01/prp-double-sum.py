"""prp-double-sum: exchange of finite double sums and the product form, on random integer arrays, including m = 0."""
import random
random.seed(4)
for _ in range(500):
    m, n = random.randint(0, 5), random.randint(0, 5)
    a = [[random.randint(-9, 9) for _ in range(n + 1)] for _ in range(m + 1)]
    assert sum(sum(a[i][j] for j in range(n + 1)) for i in range(m + 1)) == \
        sum(sum(a[i][j] for i in range(m + 1)) for j in range(n + 1))
    x = [random.randint(-9, 9) for _ in range(m + 1)]
    y = [random.randint(-9, 9) for _ in range(n + 1)]
    assert sum(x) * sum(y) == sum(sum(xi * yj for yj in y) for xi in x)
print("ok")
