def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = 0
        for i2 in range(1, i+1):
            if i % i2 == 0:
                count += 1
        if count % 2==0:
            answer += i
        else:
            answer -= i
    return(answer)