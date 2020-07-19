#   첫 줄에는 N(격자), M(자연수 번호, 상어 수), K(총 이동 수)
#   1, 2, 3, 4 위 아래 왼쪽 오른쪽

#   보고 있는 방향과 이동 방향 우선 순위

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M, K = map(int, input().split())

Matrix = []

Shark = {}
for i in range(N):
    Matrix.append(list(map(int, input().split())))
    for j, s in enumerate(Matrix[-1]):
        if s != 0:
            Shark[s] = {}
            Shark[s]["position"] = (i, j)
        Matrix[-1][j] = [0, 0, 0]   # 향, 상어, 향 주인

for i, v in enumerate(input().split()):
    Shark[i + 1]["direction"] = int(v)
    Shark[i + 1]["priority"] = []
    Shark[i + 1]["path"] = []
    Shark[i + 1]["live"] = 1


for i in range(1, M + 1):
    for _ in range(4):
        Shark[i]["priority"].append(list(map(int, input().split())))

alive = M
count = 0
will_move = []
for i in range(1, M + 1):
    x = Shark[i]["position"][0]
    y = Shark[i]["position"][1]
    Matrix[x][y] = [K, i, i]
    Shark[i]["path"].append((x, y))

while alive > 1 and count <= 1000:
    for i in range(1, M + 1):
        if not Shark[i]["live"]:
            continue

        d = Shark[i]["direction"]
        x = Shark[i]["position"][0]
        y = Shark[i]["position"][1]
        for j in Shark[i]["priority"][d - 1]:
            m_x = x + dx[j - 1]
            m_y = y + dy[j - 1]
            if m_x == -1 or m_x == N or m_y == -1 or m_y == N:
                continue
            if Matrix[m_x][m_y][0] == 0:
                Shark[i]["position"] = (m_x, m_y)
                Shark[i]["path"].append((m_x, m_y))
                Shark[i]["direction"] = j
                will_move.append((i, m_x, m_y))
                Matrix[x][y][1] = 0
                break
        if len(will_move) == 0 or will_move[-1][0] != i:
            for j in Shark[i]["priority"][d - 1]:
                m_x = x + dx[j - 1]
                m_y = y + dy[j - 1]
                if m_x == -1 or m_x == N or m_y == -1 or m_y == N:
                    continue
                if Matrix[m_x][m_y][2] == i:
                    Shark[i]["position"] = (m_x, m_y)
                    Shark[i]["direction"] = j
                    will_move.append((i, m_x, m_y))
                    Matrix[x][y][1] = 0
                    break

    for i, x, y in will_move:
        if Matrix[x][y][1] != 0:
            alive -= 1
            Shark[i]["live"] = 0
        else:
            Matrix[x][y] = [K + 1, i, i]

    will_move = []
    count += 1

    for i in range(N):
        for j in range(N):
            if Matrix[i][j][0] == 0:
                pass
            else:
                Matrix[i][j][0] -= 1


if count > 1000:
    print(-1)
else:
    print(count)


