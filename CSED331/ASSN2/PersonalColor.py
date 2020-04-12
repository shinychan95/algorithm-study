def make_color(r, g, b):
    color = []
    same = 0
    if r[0] == r[1] == r[2]:
        color.append(r[0])
        same += 1
    else:
        color.append((r[0] + r[1] + r[2]) % 16)

    if g[0] == g[1] == g[2]:
        color.append(g[0])
        same += 1
    else:
        color.append((g[0] + g[1] + g[2]) % 16)

    if b[0] == b[1] == b[2]:
        color.append(b[0])
        same += 1
    else:
        color.append((b[0] + b[1] + b[2]) % 16)

    if same == 3:
        color[1] = 15
    return color


def personal_color(arr):
    n = len(arr)
    if n == 1:
        return arr[0]

    if n > 3:
        return make_color(personal_color(arr[:n // 3]),
                          personal_color(arr[n // 3:(n // 3)*2]),
                          personal_color(arr[(n // 3)*2:(n // 3)*3]))

    else:
        return make_color(arr[0], arr[1], arr[2])


T = int(input())

for t in range(T):
    N = int(input())
    Arr = [i for i in input().split(" ")]
    for idx, v in enumerate(Arr):
        Arr[idx] = [int(v[0], 16), int(v[1], 16), int(v[2], 16)]

    result = ""
    for i in personal_color(Arr):
        result += format(i, 'x').upper()
    print(result)