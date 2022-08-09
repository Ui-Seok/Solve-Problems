def solution(s):
    answer = ''
    num = [str(i) for i in range(10)]
    alpha = {'zer':0, 'one':1, 'two':2, 'thr':3, 'fou':4, 'fiv':5, 'six':6, 'sev':7, 'eig':8, 'nin':9}
    
    for i in range(len(s)):
        if s[i] in num:
            answer += s[i]
        elif s[i:i+3] in alpha:
            answer += str(alpha[s[i:i+3]])
        else: continue
    
    return int(answer)