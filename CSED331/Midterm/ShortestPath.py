import heapq

T = int(input())

for t in range(T):
    V, E = [int(i) for i in input().split(" ")]
    edges = {}

    # edge, key: vertex, value: [[adj, w], ...]
    for v in range(V):
        edges[v] = []

    for i in range(V):
        edges[i] = {}

    for e in range(E):
        u, v, w = [int(i) for i in input().split(" ")]
        try:
            edges[u][v] = min(edges[u][v], w)
        except:
            edges[u][v] = w

    distance = [float("inf")] * V
    visited = [0] * V
    result = {}
    # stack = [(distance, index, parent), ...]
    stack = []

    heapq.heappush(stack, (0, 0, None))
    distance[0] = [0, None]
    while stack:
        s = heapq.heappop(stack)
        for adj in edges[s[1]].keys():
            if visited[adj]:
                if s[2] != adj and s[0] + edges[s[1]][adj] < distance[adj]:
                    distance[adj] = s[0] + edges[s[1]][adj]
                    result[adj] = s[1]
                    heapq.heappush(stack, (distance[adj], adj, s[1]))
            else:
                visited[adj] = 1
                distance[adj] = s[0] + edges[s[1]][adj]
                result[adj] = s[1]
                heapq.heappush(stack, (distance[adj], adj, s[1]))

    # print(result)
    # print(distance)
    try:
        r = result[V - 1]
        answer = [V - 1]
        while r:
            answer = [r] + answer
            r = result[r]
        answer = [0] + answer
        answer = list(map(str, answer))
        print(" ".join(answer))

    except:
        print("NO")