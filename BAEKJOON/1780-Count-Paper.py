# BAEKJOON 1780. 종이의 개수

N = int(input())
Array = []

for i in range(N):
    Array.append([int(v) for v in input().split(" ")])


def count_paper(n, x, y):
    diff = 0
    first = Array[y][x]
    count = [0, 0, 0]
    if n > 1:
        for i in range(3):
            for j in range(3):
                count_ = count_paper(n // 3, x + (i*(n // 3)), y + (j*(n // 3)))
                count = [a+b for a, b in zip(count, count_)]

        if 9 in count and sum(count) == 9:
            for i, v in enumerate(count):
                if v == 9:
                    count[i] = 1
    else:
        count[first + 1] += 1

    return count


Result = count_paper(N, 0, 0)

for i in Result:
    print(i)

