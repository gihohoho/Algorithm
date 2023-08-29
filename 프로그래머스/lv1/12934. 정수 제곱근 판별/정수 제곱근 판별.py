def solution(n):
    if n < 1:
        return -1

    x = 1
    while x * x < n:
        x += 1

    if x * x == n:
        return (x + 1) ** 2
    else:
        return -1