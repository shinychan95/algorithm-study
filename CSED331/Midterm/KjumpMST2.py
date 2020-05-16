import heapq


def find_p(p, n):
    while 1:
        if p[n] == n:
            return n
        else:
            n = p[n]


T = int(input())

for t in range(T):

    N, M, K = [int(i) for i in input().split(" ")]

    visited = [0] * N
    length = [0] * N
    edges = []

    # edges value: [weight, start(key), end]
    for m in range(M):
        s, e, w = [int(i) for i in input().split(" ")]
        edges.append([w, s, e])
        edges.append([w, e, s])
        length[s] += 1
        length[e] += 1

    for i, e in enumerate(edges):
        edges[i] = [length[e[1]]] + e

    edges = [i for i in sorted(edges, key=lambda k: [k[0], k[1]], reverse=True)]

    # print(edges)
    parents = [i for i in range(N)]
    ranks = [0] * N

    result = 0
    count = 0
    interval = [0] * 1000000
    # print("****************")
    while edges:
        v = edges.pop()
        # print("interval: ", interval[:20])
        if sum(interval[max(v[1] - K + 1, 0):min(v[1] + K, 999999)]):
            pass
        else:
            p_v_one = find_p(parents, v[2])
            p_v_two = find_p(parents, v[3])
            if p_v_one == p_v_two:
                pass
            else:
                # print(v)
                result += v[1]
                count += 1
                interval[v[1]] = 1
                if ranks[p_v_one] > ranks[p_v_two]:
                    parents[p_v_two] = p_v_one
                elif ranks[p_v_one] == ranks[p_v_two]:
                    ranks[p_v_one] += 1
                    parents[p_v_two] = p_v_one
                else:
                    parents[p_v_one] = p_v_two

        if count == N - 1:
            break

    if count < N - 1:
        print("NO")
    else:
        print(result)

