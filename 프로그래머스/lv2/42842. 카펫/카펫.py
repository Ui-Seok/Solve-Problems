def solution(brown, yellow):
    answer = []
    ms_list = get_measure(yellow)
    if len(ms_list):
        for i in range(len(ms_list) // 2):
            a = ms_list[2 * i + 1]
            b = ms_list[2 * i]
            box_num = get_box(a, b)
            if box_num == brown:
                answer.append(a + 2)
                answer.append(b + 2)            
    else:
        answer.append(yellow + 2)
        answer.append(3)
    return answer

def get_measure(nums):
    ms_list = []
    mid = int(nums ** (1 / 2))
    for i in range(2, mid + 1):
        if nums % i == 0:
            k = nums // i
            ms_list.append(i)
            ms_list.append(k)
    return ms_list
    
def get_box(a, b):
    return (a + b) * 2 + 4