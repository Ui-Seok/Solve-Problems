def solution(clothes):
    from collections import Counter
    
    cloth = []
    part = []
    for a, b in clothes:
        cloth.append(a)
        part.append(b)
    
    wear_cnt = Counter(part)
    cnt = 1
    
    for key in wear_cnt:
        cnt *= wear_cnt[key] + 1
    
    answer = cnt - 1
    return answer