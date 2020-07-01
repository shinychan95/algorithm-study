Ones = [0] * (1 << 20)

for i in range(1 << 20):
    Ones[i] = (i & 1) + Ones[i >> 1]


Town, Ship = map(int, input().split())

Left = [None] * Town

K = (Town + 19) // 20

for i in range(len(Left)):
    Left[i] = [0] * K

for _ in range(Ship):
    L, R = map(int, input().split())
    Left[L - 1][(R - 1) // 20] |= (1 << (R - 1) % 20)

result = 0
for i in range(Town):
    for j in range(i):
        for k in range(K):
            p = Ones[Left[i][k] & Left[j][k]]
            result += (p * p - 1) // 2

print(result)
