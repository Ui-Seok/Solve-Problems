def solution(numbers, target):
    answer = 0
    def dfs(i, number):
        nonlocal answer
        if i == len(numbers):
            if number == target:
                answer += 1
            return

        number_1 = number + numbers[i]
        number_2 = number - numbers[i]
        i += 1

        dfs(i, number_1)
        dfs(i, number_2)
        
    dfs(0, 0)
    
    return answer

