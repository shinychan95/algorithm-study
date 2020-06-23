def dfs(start, end):
    stack = [start]
    parent = {}
    while stack:
        node = stack.pop()
        if node == end:
            reverse = [node]
            while reverse:

                down = reverse.pop()
                up = parent[down]

                Graph[up].remove(down)
                Graph[down].append(up)
                if up == 0:
                    break
                reverse.append(up)
            return 1

        child = Graph[node]
        for c in child:
            parent[c] = node
        stack.extend(child)

    return 0


T = int(input())

for t in range(T):

    N, M, E = map(int, input().split())

    Graph = {0: list(range(1, N + 1))}

    for idx in range(1, N + 1):
        Graph[idx] = []
    for idx in range(N + 1, N + 1 + M):
        Graph[idx] = [N + 1 + M]

    for _ in range(E):
        n, m = map(int, input().split())
        Graph[n + 1].append(m + N + 1)

    Graph[M + N + 1] = []

    paths = 0
    while dfs(0, N + 1 + M):
        paths += 1

    print(paths)

    #   정답이지만, 시간 초과
