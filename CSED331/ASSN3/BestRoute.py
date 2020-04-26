T = int(input())

for t in range(T):
    V, E = [int(i) for i in input().split(" ")]

    edges = {}
    passed = {}
    for v in range(V):
        edges[v] = []
        passed[v] = 0

    for e in range(E):
        v = [int(i) for i in input().split(" ")]
        edges[v[0]].append(v[1])
        edges[v[1]].append(v[0])
