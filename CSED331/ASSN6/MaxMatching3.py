def matching(n):
    stack = [n]
    parent = {}
    while stack:
        # print("stack: ", stack)
        node = stack.pop()
        if not matched[node]:
            matched[node] = 1
            reverse = [node]
            while reverse:

                down = reverse.pop()
                up = parent[down]

                Graph[up].remove(down)
                Graph[down].append(up)
                if up == n:
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

    Graph = {}

    for i in range(N):
        Graph[i] = []
    for i in range(N, N + M):
        Graph[i] = []
    for _ in range(E):
        _n, _m = map(int, input().split())
        Graph[_n].append(_m + N)

    paths = 0
    matched = [1] * M + [0] * N
    # print(matched)
    for i in range(N):
        if matching(i):
            paths += 1

    print(paths)

    #   정답이 아니다. 왜냐하면, 모르겠다. 감각으로 하지 말자.
