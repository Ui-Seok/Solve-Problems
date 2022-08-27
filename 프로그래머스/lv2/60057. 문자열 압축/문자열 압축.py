'''
시작시간: 11:35
종료시간: 
'''

def solution(s):
    answer = len(s)
    if len(s) == 1:
        return 1
    for i in range(1, len(s)//2 + 1):
        cnt = 1
        st = ''
        check = s[:i]
        
        for j in range(i, len(s), i):
            if check == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    st += check
                else:
                    st += str(cnt) + check
                cnt = 1
                check = s[j:j+i]
                
        if cnt == 1:
            st += check
        else:
            st += str(cnt) + check
            
        answer = min(answer, len(st))
    return answer