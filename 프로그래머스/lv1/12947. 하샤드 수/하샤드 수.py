def solution(n):

    sum = 0
    a = str(n)
    for i in a:
        sum += int(i)

    if n % sum == 0:
        return True
    else:
        return False