# BAEKJOON 11278. 2-SAT-2

global ID
ID = 0


def dfs(x):
    # print("X: ", x, "id: ", _id)
    # print("stack: ", stack)
    stack.append(x)
    global ID
    ID += 1
    Parent[x] = ID
    parent = Parent[x]
    for adj in Graph[x]:
        if Parent[adj] == 0:
            parent = min(parent, dfs(adj))
        elif not visited[adj]:
            parent = min(parent, Parent[adj])

    if parent == Parent[x]:
        _scc = []
        while True:
            t = stack.pop()
            Parent[t] = parent
            _scc.append(t)
            ans[t] = len(scc)
            visited[t] = 1
            if t == x:
                break
        scc.append(_scc)
    # print("scc: ", scc)
    return parent


# Boolean variables, Number of Clauses
N, M = map(int, input().split())

Graph = {}
Parent = {}
Variable = []
visited = [0] * (N * 2 + 1)
ans = [0] * (N * 2 + 1)
for n in range(1, N + 1):
    Graph[n] = []
    Graph[-n] = []
    Parent[n] = 0
    Parent[-n] = 0
    Variable.extend([n, -n])


for m in range(1, M + 1):
    p, q = map(int, input().split())
    if p == q:
        Graph[p * -1].append(q)
    else:
        Graph[p * -1].append(q)
        Graph[q * -1].append(p)

print("Graph: ", Graph)
print("Variable: ", Variable)
scc = []
stack = []

for v in Variable:
    if Parent[v] == 0:
        dfs(v)

print("scc: ", scc)
print("parent: ", Parent)
answer = 1
for s in scc:
    count = [0] * N
    for _s in s:
        count[abs(_s) - 1] += 1

    if 2 in count:
        answer = 0
        break
print(answer)


print("ans: ", ans)

result = []
for i in range(1, N + 1):
    result.append("1" if ans[i] < ans[-i] else "0")

print(" ".join(result))

# https://blog.qwaz.io/problem-solving/scc%EC%99%80-2-sat