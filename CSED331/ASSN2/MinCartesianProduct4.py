def interpolation_insert(arr, val):
    low = 0
    high = len(arr) - 1
    while 1:
        if high == -1:
            arr.append(val)
            break
        if high == low:
            if arr[high][0] < val[0] or (arr[high][0] == val[0] and arr[high][1] < val[1]):
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


T = int(input())

for t in range(T):
    n, m, k = [int(i) for i in input().split(" ")]
    A = sorted([int(i) for i in input().split(" ")])
    B = sorted([int(i) for i in input().split(" ")])

    Arr = [[v * B[0], i, 0] for i, v in enumerate(A)]
    _k = k

    _k -= 1
    for i in range(_k):
        if Arr[0][2] == len(B) - 1:
            del Arr[0]
            _k -= 1
            continue

        temp = [A[Arr[0][1]] * B[Arr[0][2] + 1], Arr[0][1], Arr[0][2] + 1]
        del Arr[0]
        Arr = interpolation_insert(Arr, temp)

    print(Arr[0][0])


