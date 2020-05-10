import heapq

T = int(input())

for t in range(T):
    Y, X = [int(i) for i in input().split(" ")]
    matrix = []
    # print("*****************")
    for y in range(Y):
        matrix.append([int(i) for i in input().split(" ")])

    edges = {}

    for i in range(X * Y + 1):
        edges[i] = {}

    edges[0][1] = matrix[0][0]
    edges[1][0] = matrix[0][0]

    for i in range(Y):
        for j in range(X - 1):
            edges[X * i + j + 1][X * i + j + 2] = matrix[i][j + 1]
            edges[X * i + j + 2][X * i + j + 1] = matrix[i][j + 1]

    for i in range(X):
        for j in range(Y - 1):
            edges[X * j + i + 1][X * (j + 1) + i + 1] = matrix[j + 1][i]
            edges[X * (j + 1) + i + 1][X * j + i + 1] = matrix[j + 1][i]

    stack = []
    # (weight, v)
    heapq.heappush(stack, (0, 0))
    parent = {0: 0}
    distance = [float('-inf')] * (X * Y + 1)
    distance[0] = float('inf')
    while stack:
        v = heapq.heappop(stack)[1]
        for j in list(edges[v].keys()):
            if distance[j] < min(distance[v], edges[v][j]) and parent[v] != j:
                parent[j] = v
                distance[j] = min(distance[v], edges[v][j])
                heapq.heappush(stack, (edges[v][j], j))

    if matrix[Y - 1][X - 1] < distance[-1]:
        print(matrix[Y - 1][X - 1])
    else:
        print(distance[-1])

