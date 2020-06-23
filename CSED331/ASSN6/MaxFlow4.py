def bfs(s, e):
    # print("**********BFS*********")
    # print(Graph)
    # print(Node)

    q = [s]

    for idx in range(len(Level)):
        Level[idx] = -1

    Level[0] = 0
    # print(Level)
    while q:
        node = q.pop(0)
        if not Node[node]:
            continue
        for adj in Graph[node].keys():
            if Level[adj] < 0 and Graph[node][adj] and Node[adj]:
                Level[adj] = Level[node] + 1
                q.append(adj)

    # print(Level)
    return False if Level[e] < 0 else True


def max_flow(u, e, flow):
    # print("************* ", u, " *************")
    if u == e:
        flow = min(Node[u], flow)
        Node[u] -= flow
        return flow

    for adj in Graph[u].keys():
        if Level[adj] == Level[u] + 1 and Graph[u][adj] and Node[u]:
            now = min(flow, Graph[u][adj], Node[u])
            after = max_flow(adj, e, now)
            # print("*****************")
            # print(Graph)
            # print(Node)
            # print("u: ", u, "adj: ", adj)
            # print("now: ", now, "after: ", after)
            if after > 0:
                Graph[u][adj] -= after
                Node[u] -= after
                return after

    return 0


T = int(input())

for t in range(T):
    N, E = map(int, input().split())

    Graph = {}
    Node = {}
    for i, v in enumerate(map(int, input().split())):
        Node[i] = v
        Graph[i] = {}

    for _ in range(E):
        _u, _v, _w = map(int, input().split())
        Graph[_u][_v] = _w

    Level = [-1] * N

    total = 0
    while bfs(0, N - 1):
        total += max_flow(0, N - 1, 10000)

    # print("")
    # print("total: ", total)
    # print("")

    print(total)
