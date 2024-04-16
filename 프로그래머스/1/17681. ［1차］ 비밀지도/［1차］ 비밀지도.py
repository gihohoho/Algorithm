def bin_arr(n, num_list):
    arr = [bin(i)[2:] for i in num_list]
    
    new_arr = []
    for i in arr:
        while len(i) != n:
            i = "0"+i
        new_arr.append(i)
    return new_arr

def solution(n, arr1, arr2):
    two_arr1 = bin_arr(n, arr1)
    two_arr2 = bin_arr(n, arr2)
    print(two_arr1)
    print(two_arr2)
    
    result = ["#"*n]*n
    for i in range(0,n):
        for j in range(0,n):
            if two_arr1[i][j]=="0" and two_arr2[i][j]=="0":
                result_list = list(result[i])
                result_list[j]=" "
                result[i] = "".join(result_list)
    return(result)