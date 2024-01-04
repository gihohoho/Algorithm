def solution(k, m, score):
    answer = 0
    sorted_score = sorted(score, reverse=True)
    for i in range(0, len(sorted_score), m):
        box = sorted_score[i : i + m]
        if len(box) == m:
            answer += box[-1] * m

    return(answer)