T = int(input())

for i in range(T):
    N = int(input())

    sqrt = 5 ** (1 / 2)
    ans = int(1 / sqrt * (((1 + sqrt) / 2) ** N - ((1 - sqrt) / 2) ** N))

    print(ans % 2147483647)








