import math


f = open("socdist.in", "r")
line = f.readline()
Number, Mutual = [int(i) for i in line.split(" ")]
Array = []
for i in range(Mutual):
    line = f.readline()
    Array.append([int(i) for i in line.split(" ")])

Most = Array[-1][1]

interval = []
for i, v in enumerate(Array):
    if v[1] - v[0] > 0:
        interval.append([v[1] - v[0], 1])

for i in range(len(Array) - 1):
    interval.insert(1 + i * 2, [Array[i + 1][0] - Array[i][1], 0])

Best = 0

for i in range(1, math.floor(Most / (Number-1)) + 1):
    Sum = 0
    Count = 0
    for j in interval:
        if j[1]:
            Count += j[0] // i
            Sum += j[0] % i
        else:
            Sum += j[0]
        if Sum >= i:
            Count += 1
            Sum = 0
        if Count >= Number - 1:
            Best = i
            break

    if Best == i:
        continue
    else:
        break

f = open("socdist.out", 'w')
f.write(str(int(Best)))
f.close()