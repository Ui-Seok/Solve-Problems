'''
start: 23:37
end: 00:30
'''


def solution(participant, completion):
    answer = ''
    temp = {}
    
    for p in participant:
        if temp.get(p):
            temp[p] += 1
        else:
            temp[p] = 1
    
    for c in completion:
        temp[c] -= 1
    
    items = temp.items()
    for item in items:
        if item[1] == 1:
            answer += item[0]    
            
    return answer