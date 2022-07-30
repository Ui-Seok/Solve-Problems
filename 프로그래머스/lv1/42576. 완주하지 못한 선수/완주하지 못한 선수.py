'''
start: 23:37
end: 00:30
'''


def solution(participant, completion):
    answer = ''
    part = {}
    for i in participant:
        part[i] = 0
    for i in participant:
        part[i] += 1
    
    for i in completion:
        part[i] -= 1
    
    items = part.items()
    for item in items:
        if item[1] == 1:
            answer += item[0]
    
    return answer