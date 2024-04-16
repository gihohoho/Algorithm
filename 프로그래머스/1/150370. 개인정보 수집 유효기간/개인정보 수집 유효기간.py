def to_days(date):
    year, month, day = map(int, date.split("."))
    return year * 28 * 12 + month * 28 + day


def solution(today, terms, privacies):
    months = {}
    for v in terms:
        key = v[0]
        value = int(v[2:]) * 28
        months[key] = value

    today = to_days(today)
    expire = []
    for i, privacy in enumerate(privacies, start=1):
        if to_days(privacy[:-2]) + months[privacy[-1]] <= today:
            expire.append(i)
    return expire