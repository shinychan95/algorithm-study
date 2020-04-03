import re

def solution(files):
    answer = []
    HEAD = {}
    NUMBER = {}
    p = re.compile("[0-9]{1,5}")
    for i, file in enumerate(files):
        s = p.search(file)
        HEAD[i] = file[:s.start()].lower()
        NUMBER[i] = file[s.start():s.end()]
    
    max_HEAD_len = max([len(i) for i in HEAD.values()])
    max_NUMBER_len = max([len(i) for i in NUMBER.values()])
    
    result = {}
    for i in range(len(files)):
        result[i] = HEAD[i]
        for j in range(max_HEAD_len - len(HEAD[i])):
            result[i] += "!"
        result[i] = result[i].replace(" ", "#")
        
    for i in range(len(files)):
        for j in range(max_NUMBER_len - len(NUMBER[i])):
            result[i] += "0"
        result[i] += NUMBER[i]

    result = [ i[0] for i in sorted(result.items(), key=lambda t : t[1])]
    
    print(result)
    
    for i in result:
        answer.append(files[i])
    
    return answer