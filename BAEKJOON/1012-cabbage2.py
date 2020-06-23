#   맨 윗줄부터 아래로 흘러내릴 수 있으면 흘러내린다.


def count_row(arr):
    begin = 0
    cnt = 0
    for a in arr:
        if a == 1 and begin == 0:
            cnt += 1
            begin = a

        elif begin == 1 and a == 0:
            begin = 0
    print("cnt: ", cnt)
    return cnt


def make_zero(arr):


    return 0


T = int(input())

for t in range(T):
    M, N, K = map(int, input().split())

    matrix = []
    for _ in range(M):
        matrix.append([0] * N)

    for _ in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1
    print("")
    for m in matrix:
        print(m)

    adding = 0
    count = 0
    for i, m in enumerate(matrix):
        if i < M - 1:
            for _i, _m in enumerate(m[:-1]):
                make_one(i, _i)
            print("")
            for m in matrix:
                print(m)

        # print(m)
        count += count_row(m)

    print(count)
    # X = sorted(Arr, key=lambda k: k[0])
    # print(X)
    # Y = sorted(Arr, key=lambda k: k[1])
    # print(Y)
    #
    # begin = -1
    # temp = 0
    # for x, y in X:
    #     if begin != x and abs(temp - y) == 1:
    #         K -= 1
    #         begin = x
    #     temp = y
    #
    # begin = -1
    # temp = 0
    # for x, y in X:
    #     if begin != y and abs(temp - x) == 1:
    #         K -= 1
    #         begin = y
    #     temp = x
    #
    # print(K)


