def solution(arr1, arr2):
    answer = arr1

    for i in range(len(arr1)):
        for i2 in range(len(arr1[i])):
            answer[i][i2] = arr1[i][i2]+arr2[i][i2]
    return(answer)