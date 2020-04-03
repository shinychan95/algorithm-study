import sys
import time
import math


#stdin = ["3", "4", "1 0", "1 3", "7 1", "0 11", "4", "1 1", "-1 1", "-1 -1", "1 -1", "4", "1 1", "-1 1", "-1 -1", "1 -1"]
stdin = ["30 6", "97 4 58 9 97 3 26 167 154 86 44 160 110 138 174 140 118 785 57 24 62 89 175 184 929 56 69 171 48 103"]

# stdin = []
# for line in sys.stdin:
#     stdin.append(line)

start_time = time.time()


def separate(s, n):
    result = []
    for i in range(s, 0, -1):
        result.append(n // i)
        n -= n // i
    return result


# baskets = even number
trees, baskets = [int(i) for i in stdin[0].split(" ")]
berries = sorted([int(i) for i in stdin[1].split(" ")])[-baskets:]
print("berries: ", berries)

best = 0

for num in range(baskets, baskets // 2, -1):
    temp = berries[-num:]
    yes_or_no = 1
    while 1:
        print(temp)
        if yes_or_no:
            if len(temp) - baskets // 2 >= 3 and sum(temp[-(baskets // 2 + 3):-(baskets // 2)]) < temp[-1]:
                del temp[0]
                del temp[1]
                temp = separate(3, temp[-1]) + temp
                del temp[-1]
                temp = sorted(temp)
            elif len(temp) - baskets // 2 >= 2 and sum(temp[-(baskets // 2 + 2):-(baskets // 2)]) < temp[-1]:
                del temp[0]
                temp = separate(2, temp[-1]) + temp
                del temp[-1]
                temp = sorted(temp)
            else:
                yes_or_no = 0
        else:
            break

    if sum(temp[:-(baskets // 2)]) > best:
        best = sum(temp[:num // 2])

print(best)



print("time elapsed: {:.2f}s".format(time.time() - start_time))
