import heapq

T = int(input())

for t in range(T):
    N = int(input())

    bids = {}

    for n in range(N):
        f, d = [int(i) for i in input().split(" ")]
        try:
            bids[d].append(f)
        except:
            bids[d] = [f]

    result = [i for i in sorted(bids.items(), key=lambda b: b[0], reverse=True)]

    # print(result)
    possible = []
    answer = 0
    interval = result[0][0]
    for i in result:
        for j in range(interval - i[0]):
            if possible:
                answer += -heapq.heappop(possible)
        for k in i[1]:
            heapq.heappush(possible, -k)

        answer += -heapq.heappop(possible)

        interval = i[0] - 1
        # print(answer)

    for j in range(interval):
        if possible:
            answer += -heapq.heappop(possible)

    # print("answer: ", answer)
    print(answer)


# h = []
#
# heapq.heappush(h, -1)
# heapq.heappush(h, [-3, -4])
# heapq.heappush(h, -5)
# heapq.heappush(h, -2)
# heapq.heappush(h, -10)
# heapq.heappush(h, -4)
#
# print(heapq.heappop(h))
# print(heapq.heappop(h))
# print(heapq.heappop(h))
#
# print(h)