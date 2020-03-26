import sys
import time
import math


#stdin = ["3", "4", "1 0", "1 3", "7 1", "0 11", "4", "1 1", "-1 1", "-1 -1", "1 -1", "4", "1 1", "-1 1", "-1 -1", "1 -1"]
stdin = ["1000", "12", "1 0", "1 3", "7 1", "0 11", "1 1", "-1 1", "-1 -1", "1 -1", "-8 -7", "-1 -2", "-1 10", "-3 5"]
temp = ["12", "1 0", "1 3", "7 1", "0 11", "1 1", "-1 1", "-1 -1", "1 -1", "-8 -7", "-1 -2", "-1 10", "-3 5"]

for i in range(999):
    stdin += temp

# stdin = []
# for line in sys.stdin:
#     stdin.append(line)

start_time = time.time()

n_of_c = int(stdin[0])
index = 1

for c in range(n_of_c):
    n_of_p = int(stdin[index])
    index += 1
    space_one = []
    space_two = []
    space_three = []
    space_four = []
    point_one = []
    point_two = []
    point_three = []
    point_four = []

    for idx in range(index, index + n_of_p):
        x, y = [int(p) for p in stdin[idx].split(" ")]
        length = math.sqrt(x*x + y*y)
        sin = 0
        if y > 0 and x >= 0:  # Space One
            sin = x / length
            if space_one:
                for i, v in enumerate(space_one):
                    if v > sin:
                        space_one.insert(i, sin)
                        point_one.insert(i, stdin[idx])
                        break
                    elif v == sin:
                        x_, y_ = [int(p) for p in point_one[i].split(" ")]
                        length_ = math.sqrt(x_ * x_ + y_ * y_)
                        if length < length_:
                            space_one.insert(i, sin)
                            point_one.insert(i, stdin[idx])
                        else:
                            space_one.insert(i + 1, sin)
                            point_one.insert(i + 1, stdin[idx])
                        break
                    elif i == len(space_one) - 1:
                        space_one.append(sin)
                        point_one.append(stdin[idx])
                        break
            else:
                space_one.append(sin)
                point_one.append(stdin[idx])

        elif y <= 0 < x:  # Space Two
            sin = y / length
            if space_two:
                for i, v in enumerate(space_two):
                    if v > sin:
                        space_two.insert(i, sin)
                        point_two.insert(i, stdin[idx])
                        break
                    elif v == sin:
                        x_, y_ = [int(p) for p in point_two[i].split(" ")]
                        length_ = math.sqrt(x_ * x_ + y_ * y_)
                        if length < length_:
                            space_two.insert(i, sin)
                            point_two.insert(i, stdin[idx])
                        else:
                            space_two.insert(i + 1, sin)
                            point_two.insert(i + 1, stdin[idx])
                        break
                    elif i == len(space_two) - 1:
                        space_two.append(sin)
                        point_two.append(stdin[idx])
                        break
            else:
                space_two.append(sin)
                point_two.append(stdin[idx])

        elif y < 0 and x <= 0:  # Space Three
            sin = (x * -1) / length
            if space_three:
                for i, v in enumerate(space_three):
                    if v > sin:
                        space_three.insert(i, sin)
                        point_three.insert(i, stdin[idx])
                        break
                    elif v == sin:
                        x_, y_ = [int(p) for p in point_three[i].split(" ")]
                        length_ = math.sqrt(x_ * x_ + y_ * y_)
                        if length < length_:
                            space_three.insert(i, sin)
                            point_three.insert(i, stdin[idx])
                        else:
                            space_three.insert(i + 1, sin)
                            point_three.insert(i + 1, stdin[idx])
                        break
                    elif i == len(space_three) - 1:
                        space_three.append(sin)
                        point_three.append(stdin[idx])
                        break
            else:
                space_three.append(sin)
                point_three.append(stdin[idx])

        else:  # Space Four
            sin = (y * -1) / length
            if space_four:
                for i, v in enumerate(space_four):
                    if v > sin:
                        space_four.insert(i, sin)
                        point_four.insert(i, stdin[idx])
                        break
                    elif v == sin:
                        x_, y_ = [int(p) for p in point_four[i].split(" ")]
                        length_ = math.sqrt(x_ * x_ + y_ * y_)
                        if length < length_:
                            space_four.insert(i, sin)
                            point_four.insert(i, stdin[idx])
                        else:
                            space_four.insert(i + 1, sin)
                            point_four.insert(i + 1, stdin[idx])
                        break
                    elif i == len(space_four) - 1:
                        space_four.append(sin)
                        point_four.append(stdin[idx])
                        break
            else:
                space_four.append(sin)
                point_four.append(stdin[idx])

    #print(space_one)
    #print(point_one)
    #print(space_two)
    #print(point_two)
    #print(space_three)
    #print(point_three)
    #print(space_four)
    #print(point_four)

    for v in point_one:
        print(v)
    for v in point_two:
        print(v)
    for v in point_three:
        print(v)
    for v in point_four:
        print(v)

    print("")
    index += n_of_p
print("time elapsed: {:.2f}s".format(time.time() - start_time))
