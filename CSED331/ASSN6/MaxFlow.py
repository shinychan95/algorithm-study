import sys


def ff(s, e, v):
    stack = [s]
    minimum = sys.maxsize
    parent = {}
    while stack:
        node = stack.pop()
        if visited[node]:
            continue
        visited[node] = 1
        if node == e:

            while node != 0:

                if Graph[parent[node]][node] < minimum:
                    minimum = Graph[parent[node]][node]
                node = parent[node]

            node = e
            while node != 0:
                Graph[parent[node]][node] -= minimum
                if not Graph[parent[node]][node]:
                    del Graph[parent[node]][node]
                try:
                    Graph[node][parent[node]] += minimum
                except:
                    if abs(node - parent[node]) == 1:
                        pass
                    else:
                        Graph[node][parent[node]] = minimum

                node = parent[node]
            return minimum

        child = Graph[node].keys()
        for c in child:
            parent[c] = node

        stack.extend(child)

    return 0


T = int(input())

for t in range(T):
    N, E = map(int, input().split())

    Graph = {}
    for i, v in enumerate(map(int, input().split())):
        Graph[i * 2] = {i * 2 + 1: v}
        Graph[i * 2 + 1] = {}

    for _ in range(E):
        u, v, w = map(int, input().split())
        Graph[u * 2 + 1][v * 2] = w

    paths = 0
    while True:
        visited = [0] * (N * 2)
        temp = ff(0, N * 2 - 1, visited)
        if not temp:
            break
        paths += temp
    print(paths)

