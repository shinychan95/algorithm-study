import sys


def sum_of_distances(town_list):
    best_case = 0
    temp_case = 0
    for i in town_list:
        for j in town_list:
            if int(i) == int(j):
                pass
            else:
                temp_case += abs(int(i) - int(j))

        if best_case > temp_case:
            best_case = temp_case
            temp_case = 0
        elif best_case == 0:
            best_case = temp_case
            temp_case = 0
        else:
            temp_case = 0
        print(best_case)

    return best_case


def quadratic_func(y_shift, x):
    return (x - y_shift)*(x - y_shift)


def quadratic_method(town):
    middle_point = (int(town[0]) + int(town[len(town) - 1])) / 2
    best_case = quadratic_func(middle_point, int(town[0]))
    best_spot = int(town[0])
    for v in range(1, len(town)):
        temp_case = quadratic_func(middle_point, int(town[v]))
        if best_case > temp_case:
            best_case = temp_case
            best_spot = int(town[v])
            temp_case = 0
        else:
            temp_case = 0

    result = 0
    for i in town:
        if int(i) == best_spot:
            pass
        else:
            result += abs(best_spot - int(i))

    print(result)


def find_middle_spot(town_list):
    if len(town_list) % 2 == 1:
        middle_spot = town_list[len(town_list) // 2 + 1]
    else:
        first = int(town_list[len(town_list) // 2 - 1])
        second = int(town_list[len(town_list) // 2])
        first_value = 0
        second_value = 0
        for i in town:
            if int(i) == first:
                pass
            else:
                first_value += abs(first - int(i))

        for i in town:
            if int(i) == second:
                pass
            else:
                second_value += abs(second - int(i))

        if first_value > second_value:
            middle_spot = first
        else:
            middle_spot = second
    result = 0
    for i in town:
        if int(i) == middle_spot:
            pass
        else:
            result += abs(middle_spot - int(i))
    return result



#stdin = ["2", "10", "1 2 3 4 5 6 7 8 9 10", "10", "0 0 0 0 0 0 0 0 0 10000"]
stdin = []

for line in sys.stdin:
    stdin.append(line)

cases = int(stdin[0])



for c in range(cases):
    town = stdin[2+2*c].split(" ")
    print(find_middle_spot(town))

