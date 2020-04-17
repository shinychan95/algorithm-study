def solution(n, edge):
    vertex = {}
    passed = {}
    for i in range(n):
        vertex[i + 1] = []
        passed[i + 1] = 0

    for v in edge:
        vertex[v[0]].append(v[1])
        vertex[v[1]].append(v[0])

    result = [[1]]
    passed[1] = 1
    point = [1]
    length = 0

    while result[length]:
        length += 1
        result.append([])
        for i in point:
            for j in vertex[i]:
                if passed[j]:
                    pass
                else:
                    result[length].append(j)
                    passed[j] = 1

        point = result[length]

    print(result)

    answer = len(result[-2])

    return answer
