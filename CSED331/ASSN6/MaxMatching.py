T = int(input())

for t in range(T):

    N, M, E = map(int, input().split())

    Ns = [0] * N
    Ms = [0] * M

    N_num = 0
    M_num = 0
    for _ in range(E):
        n, m = map(int, input().split())
        if not Ns[n]:
            Ns[n] = 1
            N_num += 1
        if not Ms[m]:
            Ms[m] = 1
            M_num += 1

    print(N_num if N_num < M_num else M_num)

    #   정답이 아니다. 왜냐하면,
    #   N, M, E = 4 4 4
    #   (1 0), (1 1), (2 2), (3 2)
