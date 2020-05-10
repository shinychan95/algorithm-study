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

    # print("*************")
    # print("Matrix")
    # for y in range(Y + 2):
    #     print(matrix[y])
    # print("Visited")
    # for y in range(Y + 2):
    #     print(visited[y])

    stack = [[1, 1, matrix[1][1]]]
    next_stack = []
    less_most = 0

    while 1:
        # print("*************")
        # print("stack: ", stack)
        # print("next_stack: ", next_stack)
        # print("less_most: ", less_most)
        # print("Visited")
        # for y in range(Y + 2):
        #     print(visited[y])

        for x, y, most in stack:
            visited[y][x] = 1
            # print("stack: ", stack)
            for _x, _y in [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]]:
                if visited[_y][_x] == 0:
                    if most <= matrix[_y][_x]:
                        visited[_y][_x] = 1
                        stack.append([_x, _y, most])

                    elif less_most <= matrix[_y][_x]:
                        if [_x, _y, matrix[_y][_x]] in next_stack:
                            pass
                        else:
                            next_stack.insert(0, [_x, _y, matrix[_y][_x]])
                            less_most = matrix[_y][_x]

            if visited[Y][X] == 1:
                break
        if visited[Y][X] == 1:
            break
        stack = next_stack
        most = less_most
        less_most = 0
        next_stack = []

    # print("############")
    # print("Most: ", most)

    print(most)