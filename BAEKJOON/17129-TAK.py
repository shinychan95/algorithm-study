from sys import stdin

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    paths = 0
    stack = [(x, y)]
    visited[x][y] = 1
    while stack:
        for _ in range(len(stack)):
            _x, _y = stack.pop(0)

            for _d in range(4):
                n_x, n_y = _x + dx[_d], _y + dy[_d]

                if n_x < 0 or n_x == N or n_y < 0 or n_y == M or visited[n_x][n_y] or Map[n_x][n_y] == "1":
                    continue

                if Map[n_x][n_y] == "0":
                    visited[n_x][n_y] = 1
                    stack.append((n_x, n_y))
                else:
                    return paths + 1

        paths += 1

    return False


N, M = map(int, input().split())

Map = [stdin.readline().rstrip() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
X = 0
Y = 0

stop = False
for i, m in enumerate(Map):
    for j, s in enumerate(m):
        if s == "2":
            X = i
            Y = j
            stop = True
            break
    if stop:
        break


result = bfs(X, Y)


if result:
    print("TAK")
    print(result)
else:
    print("NIE")
