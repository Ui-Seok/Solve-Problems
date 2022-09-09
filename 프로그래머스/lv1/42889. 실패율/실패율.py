'''
시작시간: 10:35
종료시간: 11:12
'''


# def solution(N, stages):
#     answer = []
#     fail_percent = {}
#     num_of_people = len(stages)
    
#     for i in range(1, N+1):
#         count = stages.count(i)
#         if num_of_people == 0:
#             fail_percent[i] = 0
#         else:
#             fail_percent[i] = count / num_of_people
#         num_of_people = num_of_people - count
        
#     answer = [stage[0] for stage in sorted(fail_percent.items(), key = lambda x: (-x[1], x[0]))]
#     return answer

def solution(N, stages):
    answer = []
    fail_p = {}
    total_num = len(stages)
    
    for i in range(1, N + 1):
        fail_num = stages.count(i)
        if fail_num == 0:
            fail_p[i] = 0
            continue
        fail_p[i] = fail_num / total_num
        total_num -= fail_num

    fail_p = sorted(fail_p.items(), key = lambda x: -x[1])

    for f in fail_p:
        answer.append(f[0])
        
    return answer