def multiply(m1, m2):
    return [[(m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]) % 2147483647,
             (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]) % 2147483647],
            [(m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]) % 2147483647,
             (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]) % 2147483647]]


def square(m):
    x = (m[0][0] * m[0][0] + m[0][1] * m[1][0]) % 2147483647
    y = (m[0][0] * m[0][1] + m[0][1] * m[1][1]) % 2147483647
    z = (m[1][0] * m[0][1] + m[1][1] * m[1][1]) % 2147483647
    return [[x, y], [y, z]]


def binary_fibonacci(n):
    m = [[1, 1], [1, 0]]
    sqr = 0
    result = [[1, 0], [0, 1]]
    while 1:
        if n == 0:
            break
        if n % 2:
            result = multiply(result, m)
            n = n // 2
            m = square(m)
        else:
            n = n // 2
            m = square(m)
    return result


T = int(input())

for i in range(T):
    N = int(input())

    print(binary_fibonacci(N)[0][1])








