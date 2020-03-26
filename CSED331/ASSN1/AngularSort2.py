import sys
import time
import math


# input_list = [[sin, point], ...]
def quick_sort(input_list):
    if len(input_list) <= 1:
        return input_list
    pivot = input_list[len(input_list) // 2]
    l_list = []
    e_list = []
    b_list = []
    for v in input_list:
        if v[0] < pivot[0]:
            l_list.append(v)
        elif v[0] > pivot[0]:
            b_list.append(v)
        else:
            x_v, y_v = [int(i) for i in v[1].split(" ")]
            x_p, y_p = [int(i) for i in pivot[1].split(" ")]
            length_v = x_v * x_v + y_v * y_v
            length_p = x_p * x_p + y_p * y_p
            if length_v < length_p:
                l_list.append(v)
            elif length_v > length_p:
                b_list.append(v)
            else:
                e_list.append(v)

    return quick_sort(l_list) + e_list + quick_sort(b_list)


#stdin = ["3", "4", "1 0", "1 3", "7 1", "0 11", "4", "1 1", "-1 1", "-1 -1", "1 -1", "4", "1 1", "-1 1", "-1 -1", "1 -1"]

stdin = []
for line in sys.stdin:
    stdin.append(line)

start_time = time.time()

n_of_c = int(stdin[0])
index = 1

for c in range(n_of_c):
    n_of_p = int(stdin[index])
    index += 1
    sins = []

    for idx in range(index, index + n_of_p):
        x, y = [int(p) for p in stdin[idx].split(" ")]
        length = math.sqrt(x*x + y*y)
        sin = 0
        if x >= 0:  # Space Right
            sins.append([-y / length, stdin[idx]])
        else:  # Space Left
            sins.append([y / length + 2, stdin[idx]])

    sins = quick_sort(sins)

    for v in sins:
        print(v[1])

    index += n_of_p

#print("time elapsed: {:.2f}s".format(time.time() - start_time))
