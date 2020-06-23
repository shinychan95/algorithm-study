import heapq

T = int(input())

# m이 훨씬 크다.
for t in range(T):
    n, m, k = [int(i) for i in input().split(" ")]
    A = sorted([int(i) for i in input().split(" ")])
    B = sorted([int(i) for i in input().split(" ")])

    A_len = len(A)
    B_len = len(B) - 1
    stack = []
    for i, a in enumerate(A):
        heapq.heappush(stack, (a * B[0], i, 0))

    # print(stack)
    r = 0
    for i in range(k):
        r = heapq.heappop(stack)
        if r[2] == B_len:
            pass
        else:
            heapq.heappush(stack, (A[r[1]] * B[r[2] + 1], r[1], r[2] + 1))

    print(r[0])