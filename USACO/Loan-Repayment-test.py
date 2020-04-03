import math


f = open("loan.in", "r")
line = f.readline()
Number, Day, Minimum = [int(i) for i in line.split(" ")]

print("Problem Parameters: ", Number, Day, Minimum)
Best = 0
Finish = 0
X = 10000
Y = 0
Given = 0
for d in range(Day):
    Y = math.floor((Number - Given) / X)
    if Y < Minimum:
        Y = Minimum
    Given += Y
    if Number - Given < 0:
        print("Day: ", d)
        break

print("Result:   ", Number - Given)
