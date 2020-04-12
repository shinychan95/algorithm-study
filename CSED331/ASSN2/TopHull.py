T = int(input())

for t in range(T):
    N = int(input())
    Arr = []
    for n in range(N):
        arr = [int(v) for v in input().split(" ")]
        if arr[2] == 0:
            continue
        Arr.append([arr[0], arr[1], arr[2]])
        Arr.append([arr[1], arr[0], 0])

    Arr = [i for i in sorted(Arr, key=lambda k: [k[0], k[2]])]

    result = []
    xh_dict = {}
    best = 0
    for x, p, h in Arr:
        if best < h:
            result.append([x, h])
            xh_dict[str(x) + str(p)] = h
            best = h
        elif best > h > 0:
            xh_dict[str(x) + str(p)] = h
        else:
            del xh_dict[str(p) + str(x)]
            if xh_dict:
                _best = max(xh_dict.values())
            else:
                _best = 0
            if _best == 0:
                result.append([x, _best])
                best = 0
            elif best == _best:
                pass
            else:
                result.append([x, _best])
                best = _best

    d = []
    for i, p in enumerate(result[1:]):
        if result[i-1][0] == result[i][0]:
            d.append(i-1)
    tmp = 0
    for i in d:
        del result[i - tmp]
        del result[i - tmp]
        tmp += 2

    point = result[0]
    for p in result[1:]:
        if point[1] == 0:
            point = p
            continue
        print(point[0], p[0], point[1])
        point = p

