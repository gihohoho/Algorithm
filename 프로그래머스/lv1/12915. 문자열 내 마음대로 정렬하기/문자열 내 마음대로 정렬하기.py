def solution(strings, n):
    a = []
    answer = []
    for i in range(len(strings)):
        strings[i] = strings[i][n]+strings[i]
        a.append(strings[i])
    sorted_ans = sorted(a)

    for j in range(len(sorted_ans)):
        answer.append(sorted_ans[j][1:])

    return(answer)