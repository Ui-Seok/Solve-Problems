def solution(array, commands):
    answer = []
    for command in commands:
        a = command[0] - 1
        b = command[1]
        c = command[2] - 1
        new_arr = array[a : b]
        new_arr.sort()
        answer.append(new_arr[c])
        
    return answer