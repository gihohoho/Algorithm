def solution(n):
    answer = []
    a=str(n)[::-1]
    for i in a:
        answer.append(int(i))
    
    return answer

print(solution(12345))