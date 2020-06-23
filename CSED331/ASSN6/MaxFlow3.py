import queue


def ff(s, e):
    q = queue.Queue()
    q.put(s)

    parent = {}
    level = [-1] * (e + 1)
    flow = 0

    minimum = 10000
    while q.qsize():
        node = q.get()
        if Node[node] == 0:
            continue
        if node == e:
            stack = []
            while node != 0:
                p_node = parent[node].get()
                stack.append((p_node, node))
                minimum = min([minimum, Node[node], Graph[p_node][node]])
                node = p_node

            minimum = min([minimum, Node[node]])

            for p_n, n in stack:
                Node[n] -= minimum
                Graph[p_n][n] -= minimum

            Node[0] -= minimum
            flow += minimum
            node = e

        child = Graph[node].keys()
        for c in child:
            if level[c] < 0:
                parent[c] = queue.Queue()
                parent[c].put(node)
                level[c] = level[node] + 1
                q.put(c)
            elif level[c] > level[node]:
                parent[c].put(node)
                q.put(c)

    return flow


T = int(input())

for t in range(T):
    N, E = map(int, input().split())

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
        temp = ff(0, N - 1)
        if not temp:
            break
        paths += temp

    print(paths)


# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

