import heapq

T = int(input())

for t in range(T):
    # print("-----Test Case-----")
    I, P, B = [int(i) for i in input().split(" ")]
    initials = [int(i) for i in input().split(" ")]

    visited = [0] * I
    for i, j in enumerate(initials):
        visited[j] = i + 1

    edges = {}
    bridge = []
    for i in range(I):
        edges[i] = []
    for b in range(B):
        s, e, w = [int(i) for i in input().split(" ")]
        edges[s].append([w, s, e])
        edges[e].append([w, e, s])
        bridge.append([-w, s, e])

    # 색칠하는 부분
    # stack value: [weight, start(key), end]
    stack = []
    for i in initials:
        for j in edges[i]:
            if not visited[j[2]]:
                heapq.heappush(stack, j)

    while stack: # 인접한 것들을 stack에 넣는다.
        value = heapq.heappop(stack) # 제일 weight가 작은 놈부터 텔레포트 생성
        if not visited[value[2]]:
            visited[value[2]] = visited[value[1]]
            for e in edges[value[2]]:
                if not visited[e[2]]:
                    heapq.heappush(stack, e)

    # 영역끼리 최대 연결 다리 찾는 부분
    connected = [0] * P
    for b in bridge:
        if visited[b[1]] != visited[b[2]]:
            heapq.heappush(stack, b)

    maximum = 0
    count = 0
    while count != P:
        value = heapq.heappop(stack)
        if not connected[visited[value[1]] - 1] and not connected[visited[value[2]] - 1]:
            connected[visited[value[1]] - 1] = 1
            connected[visited[value[2]] - 1] = 1
            maximum += -value[0]
            count += 2
        elif not connected[visited[value[1]] - 1]:
            connected[visited[value[1]] - 1] = 1
            maximum += -value[0]
            count += 1
        elif not connected[visited[value[2]] - 1]:
            connected[visited[value[2]] - 1] = 1
            maximum += -value[0]
            count += 1

    print(maximum)



