n = int(input())

maps = []
white, blue = 0, 0
for i in range(n):
    maps.append(list(map(int, input().split())))

def cutting(box):
    global white, blue
    if len(box) == 1:
        if box == 1:
            blue += 1
            return None
        elif box == 0:
            white += 1
            return None
    # elif len(box) == n:
    #     if box == 1:
    #         blue += 1
    #         return None
    #     elif box == 0:
    #         white += 1
    #         return None

    cut_num = len(box) // 2
    box_L = box[:cut_num]
    box_R = box[cut_num:]
    box_1, box_2, box_3, box_4 = [], [], [], []
    for i in box_L:
        box_1.append(i[:cut_num])
        box_2.append(i[cut_num:])
    for i in box_R:
        box_3.append(i[:cut_num])
        box_4.append(i[cut_num:])

    for i in box_1, box_2, box_3, box_4:
        if sum_list(i) == cut_num ** 2:
            blue += 1
            continue
        elif sum_list(i) == 0:
            white += 1
            continue
        else:
            cutting(i)

def sum_list(ls):
    sum = 0
    for i in ls:
        for j in i:
            sum += j
    return sum

if sum_list(maps) == n ** 2:
    blue +=1
elif sum_list(maps) == 0:
    white += 1
else:
    cutting(maps)
print(white, blue)