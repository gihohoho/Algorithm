def solution(survey, choices):
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(survey)):
        if choices[i] == 1:
            dic[survey[i][0]] += 3
        elif choices[i] == 2:
            dic[survey[i][0]] += 2
        elif choices[i] == 3:
            dic[survey[i][0]] += 1
        elif choices[i] == 5:
            dic[survey[i][1]] += 1
        elif choices[i] == 6:
            dic[survey[i][1]] += 2
        elif choices[i] == 7:
            dic[survey[i][1]] += 3
    print(list(dic.values()))

    answer = ""

    for j in range(0, len(dic), 2):
        if list(dic.values())[j] >= list(dic.values())[j + 1]:
            answer += list(dic.keys())[j]
        elif list(dic.values())[j] < list(dic.values())[j + 1]:
            answer += list(dic.keys())[j + 1]
    
    return(answer)