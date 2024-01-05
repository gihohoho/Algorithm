def solution(want, number, discount):
    answer = 0

    wishlist = []

    for i in range(len(want)):
        for j in range(number[i]):
            wishlist.append(want[i])

    for k in range(0, len(discount)):
        new_discount = discount[k : k + 10]
        if len(new_discount) == 10:
            if sorted(wishlist) == sorted(new_discount):
                answer += 1

    return(answer)