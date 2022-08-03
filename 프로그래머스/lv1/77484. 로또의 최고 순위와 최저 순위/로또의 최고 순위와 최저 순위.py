def solution(lottos, win_nums):
    answer = []
    check = []
    lottos.sort()
    win_nums.sort()
    
    for i in win_nums:
        if i in lottos:
            check.append(i)
    if len(check) >= 2:
        rank = 7 - len(check)
    else: 
        rank = 6

    answer.append(rank)
    
    while (0 in lottos):            
        if lottos[0] == 0:
            rank -= 1
            lottos.pop(0)
            if rank == 0:
                rank += 1
        else:
            return rank
    answer.append(rank)
    answer.sort()
    return answer