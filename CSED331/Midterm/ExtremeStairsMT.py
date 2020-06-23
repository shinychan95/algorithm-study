def multiply(m1, m2, k):
    return [[(m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0] + m1[0][2] * m2[2][0]) % k,
             (m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1] + m1[0][2] * m2[2][1]) % k,
             (m1[0][0] * m2[0][2] + m1[0][1] * m2[1][2] + m1[0][2] * m2[2][2]) % k],
            [(m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0] + m1[1][2] * m2[2][0]) % k,
             (m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1] + m1[1][2] * m2[2][1]) % k,
             (m1[1][0] * m2[0][2] + m1[1][1] * m2[1][2] + m1[1][2] * m2[2][2]) % k],
            [(m1[2][0] * m2[0][0] + m1[2][1] * m2[1][0] + m1[2][2] * m2[2][0]) % k,
             (m1[2][0] * m2[0][1] + m1[2][1] * m2[1][1] + m1[2][2] * m2[2][1]) % k,
             (m1[2][0] * m2[0][2] + m1[2][1] * m2[1][2] + m1[2][2] * m2[2][2]) % k]]


def get_extreme_stairs(n, k):
    m = [[1, 1, 1], [1, 0, 0], [0, 1, 0]]
    result = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    while 1:
        if n == 0:
            break
        if n % 2:   # 나머지가 1이면,
            result = multiply(result, m, k)
            n = n // 2
            m = multiply(m, m, k)
        else:   # 나머지가 0이면,
            n = n // 2
            m = multiply(m, m, k)

    return result


T = int(input())

for i in range(T):
    N, M = [int(i) for i in input().split(" ")]

    if N < 3:
        if N == 1:
            print(1)
            continue
        else:
            print(2)
            continue
    # print("*******************")
    # print("N: ", N, "M: ", M)
    print(get_extreme_stairs(N, M)[0][0])


