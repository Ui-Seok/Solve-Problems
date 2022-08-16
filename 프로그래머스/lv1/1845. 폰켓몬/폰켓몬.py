'''
시작시간: 18시 43분
종료시간: 18시 54분
'''

def solution(nums):
    answer = 0
    # 중복 제거하기
    arr = set(nums)
    # 중복제거 후 리스트가 nums의 1/2보다 크면 nums의 1/2, 작으면 중복이 제거된 리스트의 길이
    if len(arr) > (len(nums) // 2):
        answer = len(nums) // 2
    else:
        answer = len(arr)
    return answer