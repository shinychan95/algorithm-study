def matching(n, s):
    stack = []
    stack.extend(Graph[n])
    # print("n: ", n)
    while stack:
        # print("stack: ", stack)
        m = stack.pop()
        # print("seen: ", s)
        # print("matched: ", matched)
        if s[m] == -1:
            s[m] = 1
            if matched[m] == -1 or matching(matched[m], s):
                matched[m] = n
                return 1
    return 0


T = int(input())

for t in range(T):

    N, M, E = map(int, input().split())

    Graph = {}

    for i in range(N):
        Graph[i] = []
    for i in range(M):
        Graph[i] = []
    for _ in range(E):
        _n, _m = map(int, input().split())
        Graph[_n].append(_m)

    paths = 0
    matched = [-1] * M
    # print(matched)
    for i in range(N):
        seen = [-1] * M
        # print("**********")
        # print("paths: ", paths)
        if matching(i, seen):
            paths += 1
    # print("Last matched: ", matched)
    print(paths)
    # print("")
    # print("")

    #   정답이 아니다. 왜냐하면, 모르겠다. 감각으로 하지 말자.
