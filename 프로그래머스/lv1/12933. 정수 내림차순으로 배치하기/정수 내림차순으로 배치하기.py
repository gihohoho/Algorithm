def solution(n):
    x = list(str(n))
    y = []
    for i in x:
        y.append(i)
    y.sort(reverse=True)

    z = int("".join(y))
    return(z)