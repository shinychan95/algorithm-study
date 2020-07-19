dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def draw_continent(x, y, _n):
    s = [(x, y)]
    while s:
        _x, _y = s.pop(0)

        if Continent[_x][_y] != -1:
            continue

        else:
            if Matrix[_x][_y] == "1":
                Continent[_x][_y] = _n
                for d in range(4):
                    n_x, n_y = _x + dx[d], _y + dy[d]
                    if n_x < 0 or n_x == N or n_y < 0 or n_y == N:
                        continue
                    else:
                        s.append((n_x, n_y))
            else:
                Continent[_x][_y] = 0


def find_continent(cnt):
    paths = 0
    visited = [[0] * N for _ in range(N)]     # visited 이자 distance
    s = []

    for _i in range(N):
        for _j in range(N):
            if Continent[_i][_j] == cnt:
                s.append((_i, _j))
                visited[_i][_j] = 1

    while s:
        cur = len(s)
        for c in range(cur):
            _x, _y = s.pop(0)

            for d in range(4):
                n_x, n_y = _x + dx[d], _y + dy[d]
                if n_x < 0 or n_x == N or n_y < 0 or n_y == N:
                    continue

                if Continent[n_x][n_y] and Continent[n_x][n_y] != cnt:
                    return paths

                elif not Continent[n_x][n_y] and not visited[n_x][n_y]:
                    s.append((n_x, n_y))
                    visited[n_x][n_y] = 1

        paths += 1


N = int(input())

Matrix = []
Continent = []
for _ in range(N):
    Matrix.append(input().split())
    Continent.append([-1] * N)

name = 1

for i in range(N):
    for j in range(N):
        if Continent[i][j] == -1:
            if Matrix[i][j] == "1":
                draw_continent(i, j, name)
                name += 1
            else:
                Continent[i][j] = 0


result = float("inf")
for cont in range(1, name):
    temp = find_continent(cont)
    if result > temp:
        result = temp

print(result)

