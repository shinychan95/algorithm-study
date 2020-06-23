while 1:
    case = input()
    if case == "end":
        break
    # print("**********")
    # print(case)
    x = 0
    o = 0
    dot = 0
    n = []
    for s in case:
        if s == "X":
            x += 1
            n.append(1)
        elif s == "O":
            o += 1
            n.append(-1)
        else:
            dot += 1
            n.append(0)

    if o > x or abs(o - x) > 1:
        print("invalid")
        continue

    xs = 0
    os = 0
    for i in range(3):
        if n[i * 3] + n[i * 3 + 1] + n[i * 3 + 2] == 3:
            xs += 1
        elif n[i * 3] + n[i * 3 + 1] + n[i * 3 + 2] == -3:
            os += 1

    for i in range(3):
        if n[i] + n[i + 3] + n[i + 6] == 3:
            xs += 1
        elif n[i] + n[i + 3] + n[i + 6] == -3:
            os += 1

    diag = 0
    if n[0] + n[4] + n[8] == 3:
        xs += 1
        diag += 1

    elif n[0] + n[4] + n[8] == -3:
        os += 1
        diag += -1

    if n[2] + n[4] + n[6] == 3:
        xs += 1
        diag += 1

    elif n[2] + n[4] + n[6] == -3:
        os += 1
        diag += -1

    if x + o == 9:
        if xs + os == 0:
            print("valid")
            continue
        else:
            if os == 1:
                print("invalid")
                continue
            else:
                print("valid")

    else:
        if x > o:
            if xs != 1:
                print("invalid")
            else:
                print("valid")
        else:
            if os == 1:
                print("valid")
            else:
                print("invalid")
