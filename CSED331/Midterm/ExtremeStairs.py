T = int(input())

for t in range(T):
    N, M = [int(i) for i in input().split(" ")]
    print("****************")
    print("N: ", N, "M: ", M)
    if N < 3:
        if N == 1:
            print(1)
            continue
        else:
            print(2)
            continue

    share = N // 3
    rest = N % 3

    result = 1

    for i in range(share):
        result = (result * 4)

    if rest == 1:
        result = result * (share + 1) - 1 - share
    elif rest == 2:
        result = result * (share + 1) - 1 + (share - 1)
        result = result * (share + 1) + share - share

    if N % 2 == 0:
        result += 1
    print(result % M)
