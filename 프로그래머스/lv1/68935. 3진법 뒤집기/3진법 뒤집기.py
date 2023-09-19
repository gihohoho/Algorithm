def solution(n):
    result = ''
    while n > 0:
        result += str(n % 3)
        n = n // 3

    return int(result, 3) # 10진법 > n진법 변환 (걍 외우자..ㅋㅋ)