T = int(input())

for t in range(T):
    n, m, k = [int(i) for i in input().split(" ")]
    A = sorted([int(i) for i in input().split(" ")])
    B = sorted([int(i) for i in input().split(" ")])

    _max = min(n, m)
    _time = abs(n - m) + 1
    _max_time = 0
    _k = k
    accumulate = 0
    count = 0
    subtract = 1
    reverse = 0
    while 1:
        if _k <= 0:
            break
        _k -= subtract
        accumulate += subtract
        count += 1
        if subtract < _max and not reverse:
            subtract += 1
        elif reverse:
            subtract -= 1
        elif subtract == _max:
            _max_time += 1
            if _max_time == _time:
                reverse = 1

    diagonal = []
    print("********")
    print("subtract: ", subtract)
    print("count: ", count)
    print("_k: ", _k)
    print("accumulate: ", accumulate)

    x = count - 1
    y = 0
    if len(A) > len(B):
        for i in range(subtract):
            diagonal.append(A[x] * B[y])
            x -= 1
            y += 1
    else:
        for i in range(subtract):
            diagonal.append(B[x] * A[y])
            x -= 1
            y += 1

    print(sorted(diagonal)[k - (accumulate - subtract) - 1])
