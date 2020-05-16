import heapq


def connected(_edges, _v):
    _stack = [0]
    _visited = [0] * _v
    _count = 0

    for _i in _stack:
        if _visited[_i]:
            continue
        else:
            _visited[_i] = 1
            _count += 1
            for _w, _s, _e in _edges[_i]:
                if _visited[_e]:
                    continue
                else:
                    _stack.append(_e)

    if _count == _v:
        return 1
    else:
        return 0



T = int(input())

for t in range(T):

    N, M, K = [int(i) for i in input().split(" ")]

    visited = [0] * N

    edges = {}
    for i in range(N):
        edges[i] = []

    # stack value: [weight, start(key), end]
    stack = []
    for b in range(M):
        s, e, w = [int(i) for i in input().split(" ")]
        edges[s].append([w, s, e])
        edges[e].append([w, e, s])
        heapq.heappush(stack, [w, s, e])

    interval = [0] * 1000000
    edges_num = []



    result = 0
    count = 1
    # print("****************")
    if connected(edges, N):
        while stack:  # 인접한 것들을 stack에 넣는다.
            v = heapq.heappop(stack)  # 제일 weight가 작은 놈부터 텔레포트 생성
            if not sum(interval[v[0] - K + 1:v[0] + K]):
                if not visited[v[1]] and not visited[v[2]]:
                    visited[v[1]] = 1
                    visited[v[2]] = 1
                    interval[v[0]] = 1
                    result += v[0]
                    count += 2
                    if count == N:
                        break
                elif not visited[v[1]] or not visited[v[2]]:
                    visited[v[1]] = 1
                    visited[v[2]] = 1
                    interval[v[0]] = 1
                    result += v[0]
                    count += 1
                    if count == N:
                        break

        print(result)
    else:
        print("NO")




