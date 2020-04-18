def shortest_cycle(_edges, n):
    minimum = n + 1

    for i in range(n):
        # print("*******")
        # print("i: ", i)
        if len(_edges[i]) <= 1:
            continue
        if minimum == 3:
            break

        distance = [n + 1] * n
        parent = [-1] * n

        distance[i] = 0

        queue = [i]

        while queue:
            # print("distance: ", distance)
            # print("parent: ", parent)
            # print("queue: ", queue)
            # print("minimum: ", minimum)

            pop = queue[0]
            del queue[0]

            for neighbor in _edges[pop]:
                if distance[neighbor] == n + 1:
                    distance[neighbor] = distance[pop] + 1
                    parent[neighbor] = pop
                    queue.append(neighbor)
                elif parent[pop] != neighbor and parent[neighbor] != pop and parent[neighbor] != -1:
                    # print("pop: ", pop, "neighbor: ", neighbor)
                    minimum = min(minimum, distance[pop] + distance[neighbor] + 1)

        # print("So, minimum: ", minimum)



    if minimum == n + 1:
        return -1

    return minimum


T = int(input())

for t in range(T):
    V, E = [int(i) for i in input().split(" ")]

    edges = []

    for i in range(V):
        edges.append([])

    for e in range(E):
        v = [int(i) for i in input().split(" ")]
        edges[v[0]].append(v[1])
        edges[v[1]].append(v[0])
    # print(edges)
    print(shortest_cycle(edges, V))
