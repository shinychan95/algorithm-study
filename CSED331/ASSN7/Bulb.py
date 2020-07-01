from copy import deepcopy
from itertools import product


def turn(n):
    return states[n] if n > 0 else -states[abs(n)]


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    # checked = [-1, -1]
    # for _ in range(N - 1):
    #     temp = deepcopy(checked)
    #     checked = [temp, checked]

    checked = {}
    for i in product((-1, 1), repeat=N):
        checked[i] = 0

    states = [1] * (N + 1)
    clauses = []
    for _ in range(K):
        clauses.append(list(map(int, input().split())))

    checked[tuple(states[1:])] = 1

    count = 0
    while count == 0:
        for c in clauses:
            if turn(c[0]) == 1 or turn(c[1]) == 1 or turn(c[2]) == 1:
                count += 1
                continue

            else:
                possible = 0
                for b in c:
                    states[abs(b)] *= -1
                    if not checked[tuple(states[1:])]:
                        checked[tuple(states[1:])] = 1
                        possible = 1
                        break
                    else:
                        states[abs(b)] *= -1

                if not possible:
                    count = -1
                    break

        if count == len(clauses):
            break

        elif count == -1:
            break

        else:
            count = 0

    if count == -1:
        print("NO")
    else:
        print("Yes")







