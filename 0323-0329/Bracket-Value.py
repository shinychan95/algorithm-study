# BAEKJOON 2504. 괄호의 값

Problem = input()

Plus = []  # 닫혔을 때
P_I = -1
Stack = []  # 열릴 때
S_I = -1
Inside = []  # 내부 원소 수
I_I = -1
Iter = 1

Answer = 0

for i, b in enumerate(Problem):
    if b == "(" or b == "[":
        if Iter == 1:
            Stack.append(b)
            S_I += 1
            Inside.append(0)
            I_I += 1
        else:
            Plus.append(Iter)
            P_I += 1
            Stack.append(b)
            S_I += 1
            Inside.append(0)
            I_I += 1
            Iter = 1

    elif b == ")" and S_I >= 0:
        if Stack[S_I] == "(":
            if Inside[I_I] <= 1:
                Iter *= 2
                del Stack[S_I]
                S_I -= 1
                del Inside[I_I]
                I_I -= 1
                if I_I >= 0:
                    Inside[I_I] += 1
            else:
                Plus.append(Iter)
                Iter = (sum(Plus[-Inside[I_I]:])) * 2
                for j in range(len(Plus) - 1, len(Plus) - 1 - Inside[I_I], -1):
                    del Plus[j]
                    P_I -= 1
                del Stack[S_I]
                S_I -= 1
                del Inside[I_I]
                I_I -= 1
                if I_I >= 0:
                    Inside[I_I] += 1
        else:
            Answer = -1
            break
    elif b == "]" and S_I >= 0:
        if Stack[S_I] == "[":
            if Inside[I_I] <= 1:
                Iter *= 3
                del Stack[S_I]
                S_I -= 1
                del Inside[I_I]
                I_I -= 1
                if I_I >= 0:
                    Inside[I_I] += 1
            else:
                Plus.append(Iter)
                Iter = (sum(Plus[-Inside[I_I]:])) * 3
                for j in range(len(Plus) - 1, len(Plus) - 1 - Inside[I_I], -1):
                    del Plus[j]
                    P_I -= 1
                del Stack[S_I]
                S_I -= 1
                del Inside[I_I]
                I_I -= 1
                if I_I >= 0:
                    Inside[I_I] += 1
        else:
            Answer = -1
            break
    else:
        Answer = -1
        break


if S_I >= 0 or Answer == -1:
    print(0)
else:
    print(sum(Plus) + Iter)



