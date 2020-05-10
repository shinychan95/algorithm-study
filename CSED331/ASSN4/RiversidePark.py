T = int(input())

for t in range(T):
    print("-----Test Case-----")
    N, W = [int(i) for i in input().split(" ")]

    low_hull = []
    finished = []
    low_hull.append([int(i) for i in input().split(" ")])

    for n in range(N - 1):
        l_m, r_m, y = [int(i) for i in input().split(" ")]

        plus = []
        delete = []
        print(l_m, r_m, y)
        print(low_hull)
        print(finished)
        for i, before in enumerate(low_hull):
            if y < before[2]:
                delete = [i] + delete
                finished.append(before)
                plus.append([l_m, r_m, y])
            elif y == before[2]:
                print("SHOT")
                low_hull[i][1] = r_m
            else:
                low_hull[i][1] = r_m
                plus.append([l_m, r_m, y])
        low_hull += plus
        for i in delete:
            del low_hull[i]


    optimal = 0
    for l_h in low_hull + finished:
        size = (l_h[1] - l_h[0]) * l_h[2]
        if size > optimal:
            optimal = size

    print(optimal)
    #
    # print("max_size: ", max_size)
    # print("optimal: ", optimal)

