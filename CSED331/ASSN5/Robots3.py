T = int(input())

for t in range(T):

    N, M = [int(i) for i in input().split(" ")]
    Optimal = []
    Matrix = []
    for n in range(N):
        Matrix.append([int(i) for i in input().split(" ")])
        Optimal.append([0] * M)

    if N == 1:
        print(sum(Matrix[0]))
    else:
        Optimal[0][0] = Matrix[0][0]
        for m in range(1, M):
            Optimal[0][m] = Optimal[0][m - 1] + Matrix[0][m]

        for n in range(1, N - 1):
            Optimal[n][0] = Optimal[n - 1][0] + Matrix[n][0]
            tmp = Optimal[n - 1][M - 1] + Matrix[n][M - 1]
            for m in range(1, M):
                if Optimal[n - 1][m] > Optimal[n][m - 1]:
                    Optimal[n][m] = Optimal[n - 1][m] + Matrix[n][m]
                else:
                    Optimal[n][m] = Optimal[n][m - 1] + Matrix[n][m]
            # print(tmp)
            # print(Optimal)
            for m in range(1, M):
                Optimal[n][M - m - 1] = max(Optimal[n][M - m - 1], tmp + Matrix[n][M - m - 1])
                # tmp = tmp + Matrix[n][M - m - 1]
                tmp = max(tmp + Matrix[n][M - m - 1], Matrix[n][M - m - 1] + Optimal[n - 1][M - m - 1])

        Optimal[N - 1][0] = Optimal[N - 2][0] + Matrix[N - 1][0]
        for m in range(1, M):
            if Optimal[N - 2][m] > Optimal[N - 1][m - 1]:
                Optimal[N - 1][m] = Optimal[N - 2][m] + Matrix[N - 1][m]
            else:
                Optimal[N - 1][m] = Optimal[N - 1][m - 1] + Matrix[N - 1][m]

        # print("**************")
        # print("N: :", N, "M: ", M)
        print(Optimal[N - 1][M - 1])
        # print("Result: ", Optimal[N - 1][M - 1])
        # print(find_path(1, 0, 2, N, M))
        # print(Optimal)


