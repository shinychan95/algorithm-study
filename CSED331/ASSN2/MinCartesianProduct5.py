import heapq


def cartesian(a, b, _k):
    if len(b) == 1:
        return [[a[_k] * b[0], _k, 0]]
    elif len(a) == 1:
        arr = [[a[0] * v, 0, i + 1 + i] for i, v in enumerate(b)]
        arr = [i for i in sorted(arr, key=lambda p: [p[0], p[2]])]
        return [arr[_k]]
    else:
        _b = []
        length = (len(b) + 1) // 2

        for i in range(length):
            _b.append(b[i])
            del b[i]

        prev = cartesian(a, _b, (_k + 1) // 2)
        print("prev: ", prev)
        for i, v in enumerate(prev):
            prev[i][2] *= 2

        _k -= (_k + 1) // 2

        arr = [[a[0] * v, 0, i + 1 + i] for i, v in enumerate(b)]
        print("arr: ", arr)
        print("prev: ", prev)
        stack = []
        for a in arr:
            heapq.heappush(stack, a)
        for p in prev:
            heapq.heappush(stack, p)

        for i, v in enumerate(_b):
            b.insert(i*2, v)
        print("k: ", _k)
        print("stack: ", stack)
        for i in range(_k):
            r = heapq.heappop(stack)
            if r[2] == len(b) - 1:
                pass
            else:
                heapq.heappush(stack, [a[r[1] + 1] * b[r[2] + 1], r[1] + 1, r[2]])
        print("So: ", [r])
        return [r]


T = int(input())

for t in range(T):
    n, m, k = [int(i) for i in input().split(" ")]
    A = sorted([int(i) for i in input().split(" ")])
    B = sorted([int(i) for i in input().split(" ")])

    print("result: ", cartesian(A, B, k - 1))



