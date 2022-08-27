'''
시작시간: 10:30
종료시간: 10:47
'''

def solution(record):
    answer = []
    call = ['Enter', 'Leave', 'Change']
    ID = {}
    
    for i in record:
        I = i.split()
        if I[0] == 'Enter':
            ID[I[1]] = I[2]
        elif I[0] == 'Change':
            ID[I[1]] = I[2]
            
    for j in record:
        J = j.split()
        if J[0] == 'Enter':
            answer.append(f"{ID[J[1]]}님이 들어왔습니다.")
        elif J[0] == 'Leave':
            answer.append(f"{ID[J[1]]}님이 나갔습니다.")
    return answer