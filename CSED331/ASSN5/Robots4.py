import sys

sys.setrecursionlimit(100000)


# 아래, 좌, 우
# 0 -> 0, 1 -> 2, 2 -> 1
def find_path(x, y, _n, _m):
    if x == _n - 1 and y == _m - 1:
        return max(Down[x - 1][y] + Matrix[x][y]

    if x == _n - 1:
        return find_path(x, y + 1, value, 2, _n, _m)

    if y == 0:
        if before == 1:
            return find_path(x + 1, y, value, 0, _n, _m)
        else:
            return max(find_path(x + 1, y, value, 0, _n, _m), find_path(x, y + 1, value, 2, _n, _m))

    if y == _m - 1:
        if before == 2:
            return find_path(x + 1, y, value, 0, _n, _m)
        else:
            return max(find_path(x + 1, y, value, 0, _n, _m), find_path(x, y - 1, value, 1, _n, _m))

    if before:
        if before == 1:
            return max(find_path(x + 1, y, value, 0, _n, _m), find_path(x, y - 1, value, 1, _n, _m))
        else:
            return max(find_path(x + 1, y, value, 0, _n, _m), find_path(x, y + 1, value, 2, _n, _m))

    return max(find_path(x + 1, y, value, 0, _n, _m), find_path(x, y - 1, value, 1, _n, _m),
               find_path(x, y + 1, value, 2, _n, _m))


T = int(input())

for t in range(T):

    N, M = [int(i) for i in input().split(" ")]

    Matrix = []
    Left = []
    Right = []
    Down = []
    for n in range(N):
        Matrix.append([int(i) for i in input().split(" ")])
        Left.append([0] * M)
        Right.append([0] * M)
        Down.append([0] * M)
    if N == 1:
        print(sum(Matrix[0]))
    else:
        Left[0][0] = Matrix[0][0]
        for m in range(1, M):
            Left[0][m] = Left[0][m - 1] + Matrix[0][m]
        for m in range(M):
            Down[0][m] = Left[0][m]
        Right[1][-1] = Down[0][-1] + Matrix[1][-1]

        # print("**************")
        # print("N: :", N, "M: ", M)
        print(find_path(N - 1, M - 1, N, M))
        # print(Optimal)


