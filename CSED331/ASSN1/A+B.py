import sys

stdin = ["4", "1 2", "3 4", "5 6", "7 8"]

# In Python 3, this question doesn't apply. The plain int type is unbounded.

for line in sys.stdin:
    temp = line.split(" ")
    if len(temp) < 2:
        continue
    print(int(temp[0]) + int(temp[1]))