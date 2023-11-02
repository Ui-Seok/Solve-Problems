def solution(clothes):
    cloth_type = {}
    
    for a, b in clothes:
        if cloth_type.get(b):
            cloth_type[b] += 1
        else:
            cloth_type[b] = 2
    
    cnt = 1
    for ct in cloth_type:
        cnt *= cloth_type[ct]
    
    answer = cnt - 1
    return answer