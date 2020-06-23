T = int(input())

for t in range(T):
    N, M = [int(i) for i in input().split(" ")]

    stairs = [1, 2, 4]
    arr = [1, 2, 4]
    for n in range(3, N, 3):
        arr.append((arr[-1] + arr[-2] + arr[-3]) % M)
        arr.append((arr[-1] + arr[-2] + arr[-3]) % M)
        arr.append((arr[-1] + arr[-2] + arr[-3]) % M)
        arr = arr[3:]
    print(arr[N % 3 - 1] % M)


