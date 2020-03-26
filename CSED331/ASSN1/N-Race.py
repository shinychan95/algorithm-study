import sys
import time

start_time = time.time()

# stdin = ["5", "2 3", "7 3 5 7 3 5", "2 2", "11 2 2 11", "3 4", "3 2 1 3 3 2 4 2 1 4 4 1", "3 5",
#          "1 2 1 5 1 2 2 3 5 5 4 3 4 3 4", "4 4", "1 2 1 2 3 4 3 4 1 3 2 4 1 2 3 4"]
stdin = []

for line in sys.stdin:
    stdin.append(line)

cases = int(stdin[0])

# for i in range(, 0, -1):
#     print(i)

for c in range(cases):
    laps, drivers = [int(i) for i in stdin[1 + 2 * c].split(" ")]
    records = stdin[2 + 2 * c].split(" ")

    ranking = []
    index = {}

    stop = 0
    for r in records:
        if r in index:
            for idx in range(index[r] - 1, -1, -1):
                if ranking[idx] == ranking[index[r]]:
                    print("YES")
                    stop = 1
                    break
                else:
                    break
            if stop:
                break
            else:
                ranking[index[r]] += 1
        else:
            index[r] = len(ranking)
            ranking.append(1)

    if stop:
        continue
    else:
        print("NO")

# print("--- %s seconds ---" % (time.time() - start_time))