def solution(answers):
    answer = []
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    
    for i, ans in enumerate(answers):
        cnt_1 = get_rank(ans, person_1[i%5], cnt_1)
        cnt_2 = get_rank(ans, person_2[i%8], cnt_2)
        cnt_3 = get_rank(ans, person_3[i%10], cnt_3)
        
        
    max_num = max(cnt_1, cnt_2, cnt_3)
    if max_num == cnt_1:
        answer.append(1)
    if max_num == cnt_2:
        answer.append(2)
    if max_num == cnt_3:
        answer.append(3)    
    return answer

def get_rank(answer, check, cnt):
    if answer == check:
        cnt += 1
    return cnt