def bfs(s, e):
    q = [s]

    for idx in range(len(Level)):
        Level[idx] = -1

    Level[0] = 0

    while q:
        node = q.pop(0)
        for _v, _f, _c, _r in Adj[node]:
            if Level[_v] < 0 and _f < _c:
                Level[_v] = Level[node] + 1
                q.append(_v)
    print(Level)
    return False if Level[e] < 0 else True


def send_flow(_u, flow, _e):
    if _u == _e:
        return flow

    while Visited[u] < len(Adj[u]):
        print()
        _v, _f, _c, _r = Adj[u][Visited[u]]
        if Level[_v] == Level[u] + 1 and _f < _c:
            now = min(flow, _c - _f)
            temp = send_flow(_v, now, _e)
            print("sendflow: ", _u, now, temp)
            if temp > 0:
                Adj[u][Visited[u]][1] += temp

                Adj[_v][_r][1] -= temp
                return temp

    return 0


def dinic(s, e):
    if s == e:
        return -1

    total = 0
    while bfs(s, e):
        while True:
            flow = send_flow(s, 10000, t)
            if not flow:
                break
            total += flow
            print(total)

    return total


T = int(input())

for t in range(T):
    N, E = map(int, input().split())

    Adj = {}
    Node = {}

    for i, v in enumerate(map(int, input().split())):
        Node[i] = v
        Adj[i] = []

    # edge data = [vertex, flow, capacity, reverse]
    for _ in range(E):
        u, v, w = map(int, input().split())
        Adj[u].append([v, 0, w, len(Adj[v])])
        Adj[v].append([u, 0, 0, len(Adj[u])])

    Level = [-1] * N
    Visited = [0] * N

    print(dinic(0, N - 1))





