import sys
sys.setrecursionlimit(1000000)


def solution(n):
    s = [0 for i in range(10)]
    point = 1
    while n != 0:
        while n % 10 != 9:
            for i in str(n):
                s[int(i)] += point
            n -= 1
        if n < 10:
            for i in range(n + 1):
                s[i] += point
            s[0] -= point
            break
        else:
            for i in range(10):
                s[i] += (n // 10 + 1) * point
        s[0] -= point
        point *= 10
        n //= 10
    return s


def full_count(length, c):
    # print("full_count: ", length, c)
    if length == 1:
        for i in range(1, 10):
            c[i] += 1
    else:
        for i in range(1, 10):
            c[i] += 10**(length - 1)
        # print("c: ", c)
        for i in range(10):
            c[i] += (9*(10**(length - 1))*(length - 1)) // 10
        length -= 1
        # print("c: ", c)
        full_count(length, c)


def count(n, length, c):
    # print("count: ", n, length, c)
    if length == 1:
        for i in range(1, int(n) + 1):
            c[i] += 1
    else:
        first = int(n[0])
        rest = int(n[1:])
        full_count(length - 1, c)
        # print("c: ", c)
        for i in range(1, first):
            c[i] += 10**(length - 1)
            for j in range(10):
                c[j] += (10**(length - 1)) * (length - 1) // 10
        # print("c: ", c)
        c[first] += rest + 1
        # print("c: ", c)
        for i in range(length - 1):
            c[0] += 10**i
        # print("c: ", c)
        count(n[1:], length - 1, c)
        # print("c: ", c)


for N in range(2, 1000000):

    Length = N

    if Length == 1:
        result = ["0"]
        result.extend(["1" for _ in range(N)])
        result.extend(["0" for _ in range(9 - N)])
        print(" ".join(result))

    else:
        C = [0] * 10
        count(str(N), Length, C)

        _C = solution(N)
        if C != _C:
            print(C)
            print(_C)


