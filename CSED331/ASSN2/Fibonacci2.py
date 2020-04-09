T = int(input())

for i in range(T):
    N = int(input())
    if N == 1:
        print(1)
        continue

    A = 0
    B = 1
    for j in range(N - 1):
        A, B = B, A+B

    print(B % 2147483647)

