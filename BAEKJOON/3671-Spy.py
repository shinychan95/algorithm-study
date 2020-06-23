from math import sqrt, ceil


def is_prime(n):
    sr = ceil(sqrt(n))

    if n < 4:
        if n <= 1:
            return 0
        else:
            return 1

    for i in range(2, sr + 1):
        if n % i == 0:
            return 0

    return 1


def combination(elements, length):
    for i in range(len(elements)):
        if length == 1:
            yield elements[i]
        else:
            for nxt in combination(elements[i + 1:len(elements)] + elements[:i], length - 1):
                yield elements[i] + nxt


T = int(input())

for _ in range(T):
    papers = input()

    numbers = [p for p in papers]

    check = {}
    # print("***************")
    result = 0
    for cipher in range(1, len(numbers) + 1):
        comb = list(combination(numbers, cipher))
        # print(comb)
        for c in comb:
            c = int(c)
            try:
                if check[c]:
                    pass
            except:
                check[c] = is_prime(c)
                result += check[c]

    print(result)



