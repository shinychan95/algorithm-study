def mss(arr):
    if len(arr) // 2:
        left = sum(mss(arr[:len(arr) // 2]))
        right = sum(mss(arr[len(arr) // 2:]))
    else:
        return arr

    return [max(left, right, left+right)]


T = int(input())

for i in range(T):

    N = int(input())
    Array = [int(i) for i in input().split(" ")]

    new = 0
    best = -2**31
    for e in Array:
        new += e
        if best < new:
            best = new

        if new < 0:
            new = 0

    print(best)



