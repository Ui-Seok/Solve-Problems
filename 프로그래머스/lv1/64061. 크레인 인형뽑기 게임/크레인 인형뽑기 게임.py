'''
시작시간: ---
종료시간: ---
다시풀기~
'''

def solution(board, moves):
    answer = 0
    
    basket=[]
    
    for i in range(len(moves)):
        crain=moves[i]-1
        for j in board:
            if j[crain]!=0:
                if len(basket)!=0 and basket[-1]==j[crain]:
                    basket.pop()
                    answer+=2          
                else:
                    basket.append(j[crain])
                j[crain]=0
                break
            else:
                pass
    return answer