def solution(food):
    answer = ""
    answer1 = ""
    answer2 = ""
    for i in range(1, len(food)):
        if food[i] % 2 == 0:
            answer1 += str(i) * int(food[i] / 2)
        else:
            food[i] == food[i] - 1
            answer1 += str(i) * int(food[i] / 2)
    answer1 = answer1 + "0"

    for i in reversed(range(len(food))):
        if food[i] % 2 == 0:
            answer2 += str(i) * int(food[i] / 2)
        else:
            food[i] == food[i] - 1
            answer2 += str(i) * int(food[i] / 2)
    answer = answer1 + answer2
    return(answer)