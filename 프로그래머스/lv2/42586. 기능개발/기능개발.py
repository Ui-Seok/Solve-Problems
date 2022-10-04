'''
시작시간: 11:35
종료시간: 
'''

def solution(progresses, speeds):
    answer = []
    _, _, answer = plus_sp(progresses, speeds, answer)
    
    return answer

def plus_sp(progresses, speeds, answer):
    N = len(progresses)
    cnt = 0
    for i in range(N):
        progresses[i] += speeds[i]
    if progresses[0] >= 100:
        if N >= 2:
            for j in range(1, N):
                if progresses[j] >= 100:
                    cnt += 1
                else: 
                    break
        cnt += 1
        if cnt == N:
            answer.append(cnt)
            return progresses, speeds, answer
        elif cnt < N:
            for _ in range(cnt):
                progresses.pop(0)
                speeds.pop(0)
            answer.append(cnt)
            plus_sp(progresses, speeds, answer)
    else:
        plus_sp(progresses, speeds, answer)
    return progresses, speeds, answer