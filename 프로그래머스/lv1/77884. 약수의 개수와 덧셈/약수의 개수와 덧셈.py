def solution(left, right):
    answer = 0
    for nums in range(left, right + 1):
        eli_num = get_eliment(nums)
        if eli_num % 2 == 0:
            answer += nums
        else:
            answer -= nums
    return answer


def get_eliment(num):
    eliments = []
    sq_num = int(num ** (1 / 2))
    for i in range(1, sq_num + 1):
        if num % i == 0:
            eliments.append(i)
            eliments.append(num // i)
    eliments = set(eliments)
    return len(eliments)