for _ in range(4):
    box_list = list(map(int, input().split()))
    box_1 = box_list[:4]
    box_2 = box_list[4:]
    
    if (box_1[2] < box_2[0]) or (box_2[2] < box_1[0]) or (box_1[3] < box_2[1]) or (box_1[1] > box_2[3]):
        print('d')
    elif box_1[0] == box_2[2] or box_1[2] == box_2[0] :
        if box_1[1] == box_2[3] or box_1[3] == box_2[1]:
            print('c')
        else:
            print('b')
    elif box_1[1] == box_2[3] or box_1[3] == box_2[1]:
        print('b')
    else:
        print('a')