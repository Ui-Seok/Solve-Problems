'''
시작시간: 02시 15분
종료시간: 02시 31분
'''
# 다시 풀기
def solution(n):
    answer = 0
    result = convert(n)
    for i in range(len(result)):
        answer += (3 ** (len(result) - (i + 1))) * int(result[i])
    return answer

def convert(n):
    result = ''
    while n > 0:
        n, convt = divmod(n, 3)
        print(n, convt)
        result += str(convt)
    return result
