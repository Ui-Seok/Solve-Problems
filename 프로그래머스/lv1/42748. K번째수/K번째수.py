def solution(array, commands):
    answer = []
    for command in commands:
        a, b, c = command
        new_arr = array[a - 1 : b]
        new_arr.sort()
        answer.append(new_arr[c - 1])
        
    return answer