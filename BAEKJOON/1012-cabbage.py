import sys
sys.setrecursionlimit(10000)


def spread(_x, _y):
    if matrix[_x][_y] == 1:
        matrix[_x][_y] = 0
        spread(_x + 1, _y)
        spread(_x - 1, _y)
        spread(_x, _y + 1)
        spread(_x, _y - 1)
        return 1

    else:
        return 0


T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())

    matrix = []
    for _ in range(M + 2):
        matrix.append([0] * (N + 2))

    cabbage = []
    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1
        cabbage.append([x, y])

    result = 0
    for x, y in cabbage:
        result += spread(x, y)

    print(result)
