T = int(input())

for i in range(T):

    n, m = [int(i) for i in input().split(" ")]
    sorted_list = [int(i) for i in input().split(" ")]
    query_list = [int(i) for i in input().split(" ")]

    result = ""
    for v in query_list:
        start = 0
        end = len(sorted_list) - 1
        while 1:
            middle = (end + start) // 2
            if sorted_list[middle] < v:
                start = middle
            elif sorted_list[middle] == v:
                break
            else:
                end = middle
            if end - start <= 1:
                if abs(sorted_list[end] - v) < abs(sorted_list[start] - v):
                    middle = end
                else:
                    middle = start
                break
        result += str(sorted_list[middle]) + " "

    print(result.rstrip())

