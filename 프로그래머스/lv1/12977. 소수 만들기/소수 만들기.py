'''
시작시간: 16:56
종료시간: 
'''
from itertools import combinations

def solution(nums):
    answer = 0
    nums = sorted(nums)
    rand_list = list(combinations(nums, 3))
    for rand in rand_list:
        check = 0
        for i in range(2, sum(rand)):
            if sum(rand) % i == 0:
                check  += 1
        if check == 0:
            answer += 1

    return answer