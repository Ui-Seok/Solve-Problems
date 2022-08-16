'''
시작시간: 00시 46분
종료시간: 02시 01분
'''
# 다시 풀기

def solution(w,h): 
    w_list = []
    h_list = []
    for i in range(1, int(w ** (1 / 2)) + 1):
        if w % i == 0:
            w_list.append(i)
            w_list.append(w // i)
    for j in range(1, int(h ** (1 / 2)) + 1):
        if h % j == 0:
            h_list.append(j)
            h_list.append(h // j)
    w_list.sort(reverse = True)
    for i in w_list:
        if i in h_list:
            common_factor = i
            break
    return (w * h) - (w + h - common_factor)