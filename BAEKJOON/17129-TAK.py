import sys
sys.setrecursionlimit(100000000)


def can_go(_x, _y):
    if _x < 0 or _x == N or _y < 0 or _y == M or Map[_x][_y] == "1":
        return False
    else:
        return True


N, M = map(int, input().split())

Map = []
Length = []
X = 0
Y = 0
for n in range(N):
    Map.append(input())
    Length.append([-1] * M)
    for i, s in enumerate(Map[-1]):
        if s == "2":
            X = n
            Y = i

Map[X] = Map[X][:Y] + "0" + Map[X][Y + 1:]

Length[X][Y] = 0

ctr = [(1, 0), (-1, 0), (0, 1), (0, -1)]

stack = [(X, Y)]
path = 0
result = 0
while stack:
    # print("stack: ", stack)
    x, y = stack.pop(0)
    # print("X:", x, "Y: ", y)

    if Map[x][y] != "0":
        result = Length[x][y]
        break

    for dx, dy in ctr:
        if can_go(x + dx, y + dy):
            Length[x + dx][y + dy] = Length[x][y] + 1
            stack.append((x + dx, y + dy))


if result:
    print("TAK")
    print(result)
else:
    print("NIE")
