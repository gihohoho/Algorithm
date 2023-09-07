def solution(n, m):    
    for i in range(min(n, m), 0, -1):
        if n % i == 0 and m % i == 0:
            break

    for i2 in range(max(n, m), n*m+1):
        if i2 % n == 0 and i2 % m == 0:
            break
    
    answer=[i,i2]
    
    return answer