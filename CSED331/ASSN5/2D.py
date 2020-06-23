T = int(input())

for t in range(T):

    N, M, D = [int(i) for i in input().split(" ")]

    cnv = []

    for _ in range(N):
        cnv.append([int(i) for i in input().split(" ")])

    result = []

    num = 0
    for i in range(N - D + 1):
        result.append([])
        for j in range(M - D + 1):
            for d in range(D):
                num += sum(cnv[i + d][j:j + D])
            result[i].append(num)
            num = 0

    for r in result:
        print(" ".join([str(x) for x in r]))
