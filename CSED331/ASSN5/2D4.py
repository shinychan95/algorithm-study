T = int(input())

for t in range(T):

    N, M, D = [int(i) for i in input().split(" ")]

    cnv = []
    result = [[] for _ in range(N - D + 1)]
    # print(result)
    for _ in range(N):
        cnv.append([int(i) for i in input().split(" ")])

    row = [0] * N
    for n in range(N):
        row[n] = sum(cnv[n][:D])

    # print(row)
    # print(cnv)
    for i in range(M - D + 1):
        value = sum(row[:D - 1])
        minus = 0
        for j in range(N - D + 1):
            value = value - minus + row[D + j - 1]
            minus = row[j]
            result[j].append(value)
        if i == M - D:
            break
        for n in range(N):
            row[n] = row[n] - cnv[n][i] + cnv[n][i + D]
        #     print(n)
        # print(result)

    for r in result:
        print(" ".join([str(x) for x in r]))


