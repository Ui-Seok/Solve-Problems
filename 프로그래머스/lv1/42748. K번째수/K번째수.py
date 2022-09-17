def solution(array, commands):
    answer = []
    for command in commands:
        a, b, c = command
        new_arr = sorted(array[a - 1 : b])
        answer.append(new_arr[c - 1])
    return answer