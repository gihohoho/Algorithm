def solution(dots):
    x = max(dots)[0] - min(dots)[0]
    y = max(dots)[1] - min(dots)[1]
    return x*y