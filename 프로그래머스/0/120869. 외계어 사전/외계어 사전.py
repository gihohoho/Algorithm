def solution(spell, dic):
    s=""
    for j in spell:
        s += j
    
    for i in dic:
        if sorted(i) == sorted(s):
            return 1
    return 2