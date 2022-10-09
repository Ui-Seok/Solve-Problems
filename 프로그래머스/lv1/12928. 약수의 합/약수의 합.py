def solution(n):
    ele = list()
    if n == 1:
        return 1
    for i in range(1, int(n ** 0.5)+1):
        if n % i == 0:
            ele.append(i)
            ele.append(n // i)
    answer = sum(set(ele))
    return answer