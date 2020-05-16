import heapq

T = int(input())

for t in range(T):

    N, M, K = [int(i) for i in input().split(" ")]

    visited = [0] * N

    edges = {}
    for i in range(N):
        edges[i] = []

    for b in range(M):
        s, e, w = [int(i) for i in input().split(" ")]
        edges[s].append([w, s, e])
        edges[e].append([w, e, s])

    # stack value: [weight, start(key), end]
    stack = []
    visited[0] = 1
    for adj in edges[0]:
        heapq.heappush(stack, adj)

    interval = [0] * 1000000

    result = 0
    count = 1
    # print("****************")
    while stack:  # 인접한 것들을 stack에 넣는다.
        v = heapq.heappop(stack)  # 제일 weight가 작은 놈부터 텔레포트 생성
        if not visited[v[2]] and not sum(interval[v[0] - K + 1:v[0] + K]):
            visited[v[2]] = 1
            interval[v[0]] = 1
            result += v[0]
            count += 1
            # print("adding: ", v)
            for e in edges[v[2]]:
                if not visited[e[2]]:
                    heapq.heappush(stack, e)

    # print("result: ", result)
    # print("interval: ", interval[0:10])
    if count < N:
        print("NO")
    else:
        print(result)

