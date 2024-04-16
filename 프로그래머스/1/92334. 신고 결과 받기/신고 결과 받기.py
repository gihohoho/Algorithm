def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ban_count = {i: 0 for i in id_list}

    for j in set(report):
        from_to = j.split(" ")
        ban_count[from_to[1]] += 1

    for r in set(report):
        f_t = r.split(" ")
        if ban_count[f_t[1]] >= k:
            answer[id_list.index(f_t[0])] += 1

    return answer