n = int(input())
cnt = 0

def check_num(nums):
    if n % 3 == 0:
        answer = n // 3
        if answer >= 5:
            cnt = answer // 5
            answer = cnt * 3 + answer % 5
    elif n % 5 == 0:
        answer = n // 5
    else:
        answer = False
        
    return answer

while n > 0:
    if check_num(n) == False:
        n -= 5
        cnt += 1
    else:
        answer = check_num(n)
        cnt += answer
        break
    
if n < 0:
    print('-1')
else:
    print(cnt)