import re

def solution(files):
    # 1
    temp = [re.split(r"([0-9]+)", s) for s in files]
    
    # 2
    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    # 3
    return ["".join(s) for s in sort]
