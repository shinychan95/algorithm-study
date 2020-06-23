#   TIMELIMIT
#   DFS를 이용했는데, BFS로도 작성해보자.


def max_flow(s, e):
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
# start = time.time()  # 시작 시간 저장
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
        visited = [0] * N
        temp = max_flow(0, N - 1)
        if not temp:
            break
        paths += temp

    print(paths)

# print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
