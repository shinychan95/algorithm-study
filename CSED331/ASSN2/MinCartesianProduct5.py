def interpolation_insert(arr, val):
    low = 0
    high = len(arr) - 1
    while 1:
        if high == -1:
            arr.append(val)
            break
        if high == low:
            if arr[high][0] < val[0] or (arr[high][0] == val[0] and arr[high][2] < val[2]):
                arr.append(val)
            else:
                arr.insert(high, val)
            break
        if arr[high][0] - arr[low][0] == 0:
            s = high
        else:
            s = int((val[0] - arr[low][0]) / (arr[high][0] - arr[low][0]) * (high - low) + low)
        if arr[s][0] < val[0]:
            low = s
        elif arr[s][0] == val[0]:
            low = s
            high = s
        else:
            high = s
    return arr


def cartesian(a, b, _k):
    if len(b) == 1:
        return [[a[_k] * b[0], _k, 0]]
    elif len(a) == 1:
        arr = [[a[0] * v, 0, i + 1 + i] for i, v in enumerate(b)]
        arr = [i for i in sorted(arr, key=lambda p: [p[0], p[2]])]
        return [arr[_k]]
    else:
        _b = []
        if len(b) % 2 == 0:
            length = len(b) // 2
        else:
            length = len(b) // 2 + 1

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

    print(cartesian(A, B, k - 1)[0][0])



