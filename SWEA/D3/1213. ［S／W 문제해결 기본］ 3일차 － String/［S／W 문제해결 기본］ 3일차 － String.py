for _ in range(10):
    tmp = input()
    target = input()
    arr = input()
    target_len = len(target)
    arr_len = len(arr)
    answer = idx = 0
    while idx != arr_len:
        if target == arr[idx:idx + target_len]:
            answer += 1
            idx += target_len
        else:
            idx += 1
    print(f'#{tmp} {answer}')