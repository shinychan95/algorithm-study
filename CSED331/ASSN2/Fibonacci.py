def multiply(m1, m2):
    return [[m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0], m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]],
            [m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0], m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]]]


def square(m, n):
    if n <= 1:
        return m
    else:
        return multiply(square(m, n // 2), square(m, n - n // 2))


T = int(input())

for i in range(T):
    N = int(input())

    if N == 1:
        print(1)
        continue
    elif N == 2:
        print(1)
        continue

    M = [[1, 1], [1, 0]]

    print(square(M, N)[0][1] % 2147483647)








