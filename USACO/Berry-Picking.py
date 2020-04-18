import functools
import math


f = open("berries.in", "r")
line = f.readline()
N, K = [int(i) for i in line.split(" ")]
line = f.readline()
A = [int(i) for i in line.split(" ")]

mod = 0

M = max(A)

best = 0
for b in range(1, M+1):
    full = 0
    for j in range(N):
        full = math.floor(full + A[j] / b)
    if full < K/2:
        break
    if full >= K:
        best = max(best, b*(K/2))
        continue
    mod = b
    A = sorted(A, key=lambda x: x % mod, reverse=True)
    cur = b*(full - K/2)
    for i in range(N):
        if i < K - full:
            cur += A[i] % b
    best = max(best, cur)

f = open("berries.out", 'w')
f.write(str(int(best)))
f.close()





