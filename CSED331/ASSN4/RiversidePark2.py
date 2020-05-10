T = int(input())

for t in range(T):
    # print("-----Test Case-----")
    N, W = [int(i) for i in input().split(" ")]

    stack = []
    optimal = 0
    for n in range(N):
        low_hull = [int(i) for i in input().split(" ")]
        # print(low_hull)
        while stack and stack[-1][2] > low_hull[2]:
            _low_hull = stack.pop()
            size = (low_hull[0] - (stack and stack[-1][1] or 0)) * _low_hull[2]
            if optimal < size:
                optimal = size
        if stack and stack[-1][2] == low_hull[2]:
            stack[-1][1] = low_hull[1]
        else:
            stack.append(low_hull)
        # print("stack: ", stack)
        # print("optimal: ", optimal)

    # print("Final Stack: ", stack)
    while stack:
        _low_hull = stack.pop()
        size = (W - (stack and stack[-1][1] or 0)) * _low_hull[2]
        # print(optimal, size)
        if optimal < size:
            optimal = size

    print(optimal)



