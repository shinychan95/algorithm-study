from itertools import permutations

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(start, end):
    print("start: ", start)
    print("end: ", end)
    paths = 0
    visited = [[0] * N for _ in range(N)]
    stack = [start]
    visited[start[0]][start[1]] = 1
    while stack:
        cur = len(stack)
        for c in range(cur):
            _x, _y = stack.pop(0)

            for d in range(4):
                n_x, n_y = _x + dx[d], _y + dy[d]
                if n_x < 0 or n_x == N or n_y < 0 or n_y == N or Matrix[n_x][n_y] == 1:
                    continue

                if n_x == end[0] and n_y == end[1]:
                    return paths + 1

                elif not visited[n_x][n_y]:
                    stack.append((n_x, n_y))
                    visited[n_x][n_y] = 1
        paths += 1


N, M, F = map(int, input().split())

Matrix = []

for _ in range(N):
    Matrix.append(list(map(int, input().split())))

x, y = map(int, input().split())
x -= 1
y -= 1

Person = []

for i in range(1, M + 1):
    Person.append(list(map(int, input().split())))

for i in range(M):
    for j in range(4):
        Person[i][j] -= 1

for m in Matrix:
    print(m)

print(Person)

combs = list(permutations([i for i in range(1, M + 1)], M))

fuel = F
for com in combs:
    success = 1
    for p in com:
        print("who: ", p)
        print("fuel: " , fuel)

        length = bfs((x, y), Person[p - 1][:2])
        print("length: ", length)
        if fuel <= length:
            print("Fail: ", com)
            success = 0
            break
        fuel -= length
        print("To Person: ", length)
        length = bfs(Person[p - 1][:2], Person[p - 1][2:])
        print("length: ", length)
        if fuel <= length:
            print("Fail: ", com)
            success = 0
            break

        x = Person[p - 1][2]
        y = Person[p - 1][3]
        print("To Target: ", length)
        fuel += length * 2

    fuel = F

    if success:
        break

if success:
    print(F)