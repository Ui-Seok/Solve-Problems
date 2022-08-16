'''
시작시간: 17시 58분
종료시간: 18시 07분
'''

def solution(sizes):
    answer = 0
    width = []
    height = []
    # sizes안의 1차원 리스트들을 크기순으로 정렬
    for i in sizes:
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]
    # 리스트의 첫번째 원소를 width에 저장, 두번째 원소를 height에 저장
    for size in sizes:
        width.append(size[0])
        height.append(size[1])
    # 각각의 max값을 받아와 곱하기
    answer = max(width) * max(height)
    return answer