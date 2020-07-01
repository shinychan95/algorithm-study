import sys
sys.setrecursionlimit(1000000000)


def find_path(before, visited):
    if visited == finish:
        return Graph[before][0] if Graph[before][0] != -1 else float('inf')

    if paths[before][visited] != -1:
        return paths[before][visited]

    dist = float('inf')
    for adj in range(N):
        if visited & (1 << adj) == 0 and Graph[before][adj] != -1:
            dist = min(dist, find_path(adj, visited | (1 << adj)) + Graph[before][adj])

    paths[before][visited] = dist

    return dist


T = int(input())

for _ in range(T):
    N, E = map(int, input().split())

    Graph = {}

    for _i in range(N):
        Graph[_i] = {}
        for _j in range(N):
            Graph[_i][_j] = -1

    for _ in range(E):
        x, y, w = map(int, input().split())
        Graph[x][y] = w
        Graph[y][x] = w
    # print("*******************")
    finish = (1 << N) - 1
    paths = [[-1] * (1 << N) for _ in range(N)]

    result = find_path(0, 1 << 0)

    if result == float('inf'):
        print("-1")
    else:
        print(result)