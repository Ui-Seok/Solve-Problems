def solution(numbers):
    answer = 0
    nums = []
    for i in range(10):
        nums.append(i)
    for j in nums:
        if j not in numbers: 
            answer += j
    return answer