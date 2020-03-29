f = open("cereal.in", "r")
line = f.readline()
Number, Cereal = [int(i) for i in line.split(" ")]
Cereals = [1 for i in range(Cereal)]
Cows = []
Likes = []
for i in range(Number):
    line = f.readline()
    Cows.append([int(i) for i in line.split(" ")])

print(Cows)
print(Cereals)

f = open("cereal.out", 'w')
for i in range(Number):
    Count = 0
    Cereals = [1 for i in range(Cereal)]
    for j in range(i, Number):
        if Cereals[Cows[j][0] - 1] == 1:
            Count += 1
            Cereals[Cows[j][0] - 1] -= 1
        elif Cereals[Cows[j][1] - 1] == 1:
            Count += 1
            Cereals[Cows[j][1] - 1] -= 1
        else:
            continue
    f.write(str(int(Count))+"\n")

f.close()