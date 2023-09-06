def solution(price, money, count):
    sum = 0
    for i in range(1, count+1):
        p = i*price
        sum += p
    answer = sum-money
    if answer>0 :
        return(answer)
    else :
        return(0)
