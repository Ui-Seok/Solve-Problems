while True:
    length_list = list(map(int, input().split()))
    if sum(length_list) == 0:
        break
    else:
        max_length = max(length_list)
        length_list.remove(max_length)

        for i in range(len(length_list)):
            length_list[i] = length_list[i] ** 2

        if max_length ** 2 == sum(length_list):
            print('right')
        else:
            print('wrong')