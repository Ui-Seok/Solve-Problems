'''
시작시간: 11:01
종료시간: 포기
'''        

def solution(n):
    answer_r = ''
    # 3으로 나눴을때 나머지가 1이면 1, 2면 2, 0이면 4이다.
    # 3으로 나눴을때의 몫이 1이면 1, 2면 2, 3이면 4이다.
    while (n // 3 > 0):
        A = n // 3
        a = n % 3
        if a == 0:
            answer_r += '4'
            A -= 1
            n = A
        elif a == 1:
            answer_r += '1'
            n = A
        else: 
            answer_r += '2'
            n = A

    if n // 3 == 0:
        if n % 3 == 1:
            answer_r += '1'
        elif n % 3 == 2: 
            answer_r += '2'
            
    answer = answer_r[::-1]
    return answer