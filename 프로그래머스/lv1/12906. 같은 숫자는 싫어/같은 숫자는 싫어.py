'''
시작시간: 17시 55분
종료시간: 17시 56분
'''

def solution(arr):
    answer = []
    # answer에 원소 하나 추가해주기
    answer.append(arr[0])
    # answer의 마지막 원소와 arr의 원소가 같은 값이 아닐경우에만 answer에 추가
    for i in arr:
        if answer[-1] != i:
            answer.append(i)
    return answer