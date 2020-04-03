import math
import time

start_time = time.time()

f = open("loan.in", "r")
line = f.readline()
Number, Day, Minimum = [int(i) for i in line.split(" ")]

End = 1
Finish = 0
while 1:
    Given = 0
    print(End)
    for d in range(Day):
        Y = math.floor((Number - Given) / End)
        if Y < Minimum:
            Y = Minimum
        Given += Y
        if Number - Given < 0:
            End = End*10
            break
        elif d == Day - 1:
            Finish = 1
            break
    if Finish:
        break

Best = 0
Finish = 0
Start = 1
Y = 0
while 1:
    Given = 0
    X = (End + Start) // 2
    print(X, Day)
    for d in range(Day):
        Y = math.floor((Number - Given) / X)
        if Y < Minimum:
            Y = Minimum
        Given += Y
        if Number - Given < 0 and Best < d:
            if abs(Best - d) <= 2:
                Finish = 1
            Start = X
            Best = d
            break
        elif d == Day - 1:
            End = X
            break
    if Finish:
        break

f = open("loan.out", 'w')
f.write(str(int(X)))
f.close()

print("X:  ", X)

print("time elapsed: {:.2f}s".format(time.time() - start_time))