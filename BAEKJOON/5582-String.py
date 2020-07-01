A = input()
B = input()

English = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

A_dict = {}
B_dict = {}

for e in English:
    A_dict[e] = []
    B_dict[e] = []


for i, a in enumerate(A):
    A_dict[a].append(i)

for i, b in enumerate(B):
    B_dict[b].append(i)


maximum = 0
for i_a, a in range(len(A)):
    for i_b in B_dict[a]:
        temp = 1
        _i_a = i_a + 1
        _i_b = i_b + 1
        while _i_b < len(B) and _i_a < len(A) and B[_i_b] == A[_i_a]:
            temp += 1
            _i_a += 1
            _i_b += 1

        if temp > maximum:
            maximum = temp

print(maximum)


