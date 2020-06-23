def matching(n, m, s):
    s[m] = 1
    stack = []
    stack.extend(Graph[m])
    while stack:
        node = stack.pop()
        if not s[node] and not matching(n, node, s):
            Graph[m].remove(node)
            Graph[node].append(m)
            if m == n:
                return 1
            return 0
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
    # print(matched)
    for i in range(N):
        seen = [0] * (M + N)
        # print("**********")
        # print("paths: ", paths)
        if matching(i, i, seen):
            paths += 1
    print("Last Graph: ", Graph)
    print(paths)

    #   정답이 아니다. 왜냐하면, 모르겠다. 감각으로 하지 말자.
