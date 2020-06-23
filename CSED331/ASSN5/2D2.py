T = int(input())

for t in range(T):

    N, M, D = [int(i) for i in input().split(" ")]

    cnv = []
    net = []

    for _ in range(N):
        cnv.append([int(i) for i in input().split(" ")])
        net.append([sum(cnv[-1][d:d + D]) for d in range(M - D + 1)])

    result = []
    # print("**************")
    # print(cnv)
    # print(net)

    for i in range(N - D + 1):
        result.append([])
        for j in range(M - D + 1):
            result[i].append(sum([net[i + d][j] for d in range(D)]))

    for r in result:
        print(" ".join([str(x) for x in r]))