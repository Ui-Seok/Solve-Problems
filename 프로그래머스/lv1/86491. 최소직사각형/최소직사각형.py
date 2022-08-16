'''
시작시간: 17시 58분
종료시간: 
'''

def solution(sizes):
    answer = 0
    for i in sizes:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]
    width = []
    height = []
    for size in sizes:
        width.append(size[0])
        height.append(size[1])
    answer = max(width) * max(height)
    return answer