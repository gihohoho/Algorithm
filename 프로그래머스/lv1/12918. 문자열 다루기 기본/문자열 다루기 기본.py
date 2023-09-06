def solution(s):
    try:
        int(s)
    except:
        return False
    
    if len(s) == 4 or len(s)== 6:
        return True
    else:
        return False
