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
        length = len(b) // 2 if len(b) % 2 == 0 else len(b) // 2 + 1

        for i in range(length):
            _b.append(b[i])
            del b[i]

        prev = cartesian(a, _b, (_k + 1) // 2)

        for i, v in enumerate(prev):
            prev[i][2] *= 2

        _k -= (_k + 1) // 2

        arr = [[a[0] * v, 0, i + 1 + i] for i, v in enumerate(b)]

        arr += prev

        arr = [i for i in sorted(arr, key=lambda p: [p[0], p[2]])]

        for i, v in enumerate(_b):
            b.insert(i*2, v)

        for i in range(_k):
            if arr[0][1] == len(A) - 1:
                del arr[0]
                _k -= 1
                continue

            temp = [a[arr[0][1] + 1] * b[arr[0][2]], arr[0][1] + 1, arr[0][2]]

            del arr[0]
            _k -= 1
            arr = interpolation_insert(arr, temp)

        return arr


T = int(input())

for t in range(T):
    n, m, k = [int(i) for i in input().split(" ")]
    A = sorted([int(i) for i in input().split(" ")])
    B = sorted([int(i) for i in input().split(" ")])

    result = cartesian(A, B, k - 1)

    print(result[0][0])



