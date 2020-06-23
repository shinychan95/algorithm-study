# BAEKJOON 11278. 2-SAT-2

N, M = map(int, input().split())

# in_clauses = {}
cla_TF = [0] * (M + 1)
ltr_Where = {}
ltr_TF = {}
ltr_Assign = [0] * (N + 1)

for n in range(1, N + 1):
    ltr_Where[n] = []
    ltr_Where[-n] = []

stack = []
for m in range(1, M + 1):
    i, j = map(int, input().split())
    ltr_Where[i].append(m)
    ltr_Where[j].append(m)
    stack.append([m, i])
    stack.append([m, j])

front = []
back = []
front.extend(stack)
front.extend(back)
count = 0
while stack:
    if count == M:
        break

    m, x = stack.pop(0)
    # print(count, m, x)
    if cla_TF[m]:
        continue

    if ltr_Assign[abs(x)]:
        continue

    else:
        if x > 0:
            ltr_TF[abs(x)] = 1
            ltr_Assign[abs(x)] = 1
            for _m in ltr_Where[x]:
                if not cla_TF[_m]:
                    cla_TF[_m] = 1
                    count += 1
        else:
            ltr_TF[abs(x)] = 0
            ltr_Assign[abs(x)] = 1
            for _m in ltr_Where[x]:
                if not cla_TF[_m]:
                    cla_TF[_m] = 1
                    count += 1


if count == M:
    print(1)
    result = [str(ltr_TF[n]) for n in range(1, N + 1)]
    print(" ".join(result))
else:
    print(0)
