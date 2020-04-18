base = "0123456789ABCDEF"


def get_string(i, n):
    s = ""
    while 1:
        remain = i % n
        s = base[remain] + s
        i = i // n
        if i == 0:
            break
    return s


def solution(n, t, m, p):
    element = base[0:n]
    number = (t - 1) * m + p
    index = 1
    count = 1
    answer = ""
    while 1:
        if number < n ** index:
            count += number // index + 1
            break
        else:
            count += n ** index - n ** (index - 1)
            number -= index * (n ** index - n ** (index - 1))
            index += 1

    for i in range(count):
        answer += get_string(i, n)

    result = ""
    for i in range(p - 1, t * m, m):
        result += answer[i]

    return result


print(solution(16, 100, 10, 2))