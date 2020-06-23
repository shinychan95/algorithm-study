import heapq


def find_p(p, n):
    count = 0
    _n = n
    while 1:
        if p[n] == n:
            if count >= 2:
                p[_n] = n
            return n
        else:
            n = p[n]
            count += 1


T = int(input())

for t in range(T):

    N, M, K = [int(i) for i in input().split(" ")]

    # stack value: [weight, start(key), end]
    stack = []
    for b in range(M):
        s, e, w = [int(i) for i in input().split(" ")]
        heapq.heappush(stack, [w, s, e])

    # print(edges)
    parents = [i for i in range(N)]
    ranks = [0] * N

    result = 0
    count = 0
    interval = [0] * 1000000
    # print("****************")
    while stack:
        v = heapq.heappop(stack)
        # print("interval: ", interval[:20])
        if sum(interval[max(v[0] - K + 1, 0):min(v[0] + K, 999999)]):
            pass
        else:
            p_v_one = find_p(parents, v[1])
            p_v_two = find_p(parents, v[2])
            if p_v_one == p_v_two:
                pass
            else:
                # print(v)
                result += v[0]
                count += 1
                interval[v[0]] = 1
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

