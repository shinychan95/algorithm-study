import sys

sys.setrecursionlimit(100000)

ctrl = [[1, 0], [0, -1], [0, 1]]


def find_path(x, y, before, _matrix, _n, _m):
    print("x: ", x, "y: ", y, "before: ", before)

    if x == _n - 1 and y == _m - 1:
        return _matrix[x][y]

    if Optimal[x][y][before]:
        return Optimal[x][y][before]

    result = []

    direction = [1, 1, 1]   # 아래, 좌, 우

    if before:
        direction[before] = 0
    if x == _n - 1:
        direction[0] = 0
        direction[1] = 0
    if y == 0:
        direction[1] = 0
    if y == _m - 1:
        direction[2] = 0

    print("direction: ", direction)
    print("Optimal: ", Optimal)
    # 0 -> 0, 1 -> 2, 2 -> 1
    for i, v in enumerate(direction):
        if v:
            result.append(_matrix[x][y] + find_path(x + ctrl[i][0], y + ctrl[i][1], (3 - i) % 3, _matrix, _n, _m))

    Optimal[x][y][before] = max(result)

    return Optimal[x][y][before]


T = int(input())

for t in range(T):

    N, M = [int(i) for i in input().split(" ")]
    Optimal = []
    Matrix = []
    for n in range(N):
        Matrix.append([int(i) for i in input().split(" ")])
        Optimal.append([])
        for m in range(M):
            Optimal[n].append([0] * 3)

    print("**************")
    print("N: :", N, "M: ", M)
    print(find_path(0, 0, 1, Matrix, N, M))
    # Optimal[0][0][0] = 1
    # print("Optimal: ", Optimal)

