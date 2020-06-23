def get_one_row(r, c, m, d):
    o_r = [sum(r)]
    for i in range(m - d):
        r = [r[_d] - cnv[c + _d][i] + cnv[c + _d][i + d] for _d in range(d)]
        o_r.append(sum(r))

    return o_r


T = int(input())

for t in range(T):

    N, M, D = [int(i) for i in input().split(" ")]

    cnv = []

    for _ in range(N):
        cnv.append([int(i) for i in input().split(" ")])

    row = [0] * N
    count = 0
    for n in range(N):
        row[n] = sum(cnv[n][:D])

    next_row = row

    result = []
    for _ in range(N - D + 1):
        result.append(get_one_row(row[count:count + D], count, M, D))
        count += 1

    for r in result:
        print(" ".join([str(x) for x in r]))


