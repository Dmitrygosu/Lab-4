
import numpy as np


def is_prime(k):
    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True


foo = np.vectorize(is_prime)
k, n = 4, 6
a = np.random.randint(-10, 10, (n, n))
print(a)
print()

f = a.copy()
tmp = a[n // 2:, :n // 2].copy().astype(np.float64)
tmp[1:-1, 1:-1] = np.nan
t1 = np.nanprod(tmp)
t2 = foo(a[:n // 2, n // 2::2]).sum()
print(t1)
print(t2)
print()
if t2 > t1:
    f[:, :n // 2] = np.flip(f[:, :n // 2], 0)
else:
    f[:n // 2, n // 2:] = a[n // 2:, :n // 2].copy()
    f[n // 2:, :n // 2] = a[:n // 2, n // 2:].copy()
print(f)
print()

ft = f.T
print(ft)
print()

at = a.T
print(at)
print()

kat = at * k
print(kat)
print()

fa = f + a
print(fa)
print()

katfa = kat * fa
print(katfa)
print()

kft = ft * k
print(kft)
print()

res = katfa - kft
print(res)
