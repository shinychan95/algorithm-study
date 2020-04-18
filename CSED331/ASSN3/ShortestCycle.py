def explore(_edges, _passed, _u, _v, _k):
    # print("u: ", _u, "v: ", _v, "k: ", _k)
    # print(_passed)
    if _u == _v:
        if _k > 2:
            return [_k]
        else:
            return []

    r = []
    if len(_edges[_u]) == 1:
        _passed[_u] = 1
    else:
        for i in _edges[_u]:
            if _passed[i]:
                pass
            else:
                _passed[_u] = 1
                r += explore(_edges, _passed, i, _v, _k + 1)
                _passed[_u] = 0
        _passed[_u] = 1

    return r


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

    result = []
    # print("")
    for v in range(V):
        # print("********")
        # print("v: ", v)
        if len(edges[v]) == 1 or passed[v]:
            pass
        else:
            for u in edges[v]:
                result += explore(edges, passed, u, v, 1)
        passed[v] = 1
        # print("result: ", result)

    if result:
        print(min(result))
    else:
        print(-1)




