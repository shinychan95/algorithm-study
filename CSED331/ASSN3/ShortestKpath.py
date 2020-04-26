def connected(_edges, _v):
    _s = [0]
    _n_s = []
    _visited = [0] * _v
    # print("*********")
    while 1:
        if not _s:
            return 0
        for _i in _s:
            for _j in _edges[_i].keys():
                # print("i: ", _i, "j: ", _j)
                if _j == _v - 1:
                    return 1
                if _visited[_j]:
                    pass
                else:
                    _visited[_j] = 1
                    _n_s.append(_j)
            _s = _n_s
            _n_s = []


T = int(input())

for t in range(T):
    V, E, k = [int(i) for i in input().split(" ")]
    edges = {}

    for i in range(V):
        edges[i] = {}

    for e in range(E):
        u, v, w = [int(i) for i in input().split(" ")]
        if v in edges[u]:
            if edges[u][v] > w:
                edges[u][v] = w
        else:
            edges[u][v] = w

    visited = [0] * V
    distance = [0] * V
    distance[V - 1] = 2**32
    stack = [0]
    next_stack = []
    # print("**********")
    if connected(edges, V):
        for n in range(k):
            if not stack:
                break
            for i in stack:
                for j in edges[i].keys():
                    # print("i: ", i, "j: ", j)
                    if visited[j]:
                        if j == V - 1:
                            if distance[j] > distance[i] + edges[i][j]:
                                distance[j] = distance[i] + edges[i][j]
                        else:
                            next_stack.append(j)
                            if distance[j] > distance[i] + edges[i][j]:
                                distance[j] = distance[i] + edges[i][j]
                    else:
                        visited[j] = 1
                        next_stack.append(j)
                        distance[j] = distance[i] + edges[i][j]

            # print("stack: ", stack)
            # print("distance: ", distance)
            stack = next_stack
            next_stack = []
        print(distance[V - 1])
    else:
        print("NO")