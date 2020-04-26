
T = int(input())

for t in range(T):
    Y, X = [int(i) for i in input().split(" ")]

    matrix = []
    visited = []
    matrix.append([-1] * (X + 2))
    visited.append([-1] * (X + 2))
    for y in range(Y):
        matrix.append([-1] + [int(i) for i in input().split(" ")] + [-1])
        visited.append([-1] + [0] * X + [-1])
    matrix.append([-1] * (X + 2))
    visited.append([-1] * (X + 2))

    print("*************")
    for y in range(Y + 2):
        print(matrix[y])
    for y in range(Y + 2):
        print(visited[y])

    x = 1
    y = 1
    l_m_x = 0
    l_m_y = 0
    less_most = 0
    most = matrix[1][1]
    while not visited[X - 1][Y - 1]:
        for _x, _y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
            if visited[_x][_y] == 0:
                if most <= matrix[_x][_y]:
                    visited[_x][_y] = 1
                elif less_most <= matrix[_x][_y]:
                    l_m_x = _x
                    l_m_y = _y
                    less_most = matrix[_x][_y]

        x = l_m_x
        y = l_m_y
        most = less_most
        less_most = 0

    print()

