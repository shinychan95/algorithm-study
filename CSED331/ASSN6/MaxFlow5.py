def max_flow_dn(s, e):
    q = [s]

    parent = {}
    level = [-1] * (e + 1)
    level[0] = 0
    flow = 0
    minimum = 10000

    while q:
        node = q.pop(0)
        if Node[node] == 0:
            continue
        if node == e:
            stack = []
            while node != 0:
                p_node = parent[node].pop(0)
                stack.append((p_node, node))
                minimum = min(minimum, Node[node], Graph[p_node][node])
                node = p_node

            minimum = min(minimum, Node[node])

            for p_n, n in stack:
                Node[n] -= minimum
                Graph[p_n][n] -= minimum

            Node[0] -= minimum
            flow += minimum
            node = e
            minimum = 10000

        for c in Graph[node].keys():
            if level[c] < 0:
                parent[c] = [node]
                level[c] = level[node] + 1
                q.append(c)
            elif Graph[node][c] and level[c] > level[node]:
                parent[c].append(node)
                q.append(c)

    return flow


def max_flow_ff(s, e):
    stack = []
    parent = {}

    stack.extend(Graph[s])
    for n in stack:
        parent[n] = s

    minimum = 10000
    while stack:
        node = stack.pop()
        if visited[node] or Node[node] == 0:
            continue
        visited[node] = 1
        if node == e:
            while node != 0:
                minimum = min([minimum, Node[node], Graph[parent[node]][node]])
                node = parent[node]
            minimum = min([minimum, Node[node]])
            node = e
            while node != 0:
                Node[node] -= minimum
                Graph[parent[node]][node] -= minimum
                node = parent[node]
            Node[node] -= minimum
            return minimum

        for c in Graph[node].keys():
            if Graph[node][c]:
                parent[c] = node
                stack.append(c)

    return 0


T = int(input())

for t in range(T):
    N, E = map(int, input().split())

    if N < E:
        Graph = {}
        Node = {}
        for i, v in enumerate(map(int, input().split())):
            Node[i] = v
            Graph[i] = {}

        for _ in range(E):
            u, v, w = map(int, input().split())
            Graph[u][v] = w

        paths = 0
        while True:
            temp = max_flow_dn(0, N - 1)
            if not temp:
                break
            paths += temp

        print(paths)

    else:
        Graph = {}
        Node = {}
        for i, v in enumerate(map(int, input().split())):
            Node[i] = v
            Graph[i] = {}

        for _ in range(E):
            u, v, w = map(int, input().split())
            Graph[u][v] = w

        paths = 0
        while True:
            visited = [0] * N
            temp = max_flow_ff(0, N - 1)
            if not temp:
                break
            paths += temp

        print(paths)



