def topology_sort(_edges, _visited, _stack, _v):
    if _visited[_v] == 1:
        return 0
    else:
        _visited[_v] = 1
        # recur = 0
        if _edges[_v]:
            for i, j in _edges[_v]:
                topology_sort(_edges, _visited, _stack, i)
                # recur += topology_sort(_edges, _visited, _stack, i)
            _stack.insert(0, _v)

        else:
            _stack.insert(0, _v)


T = int(input())

for t in range(T):
    V, E = [int(i) for i in input().split(" ")]
    edges = {}

    for i in range(V):
        edges[i] = []

    for e in range(E):
        u, v, w = [int(i) for i in input().split(" ")]
        edges[u].append([v, w])

    visited = [0] * V
    stack = []
    for i in range(V):
        topology_sort(edges, visited, stack, i)

    distance = [0] * V
    for i in stack:
        for j, k in edges[i]:
            if distance[j] < distance[i] + k:
                distance[j] = distance[i] + k

    print(max(distance))



