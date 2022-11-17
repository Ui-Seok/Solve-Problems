t = int(input())
for _ in range(t):
    td = list(input())
    ans = 'YES'

    if td[-1] == '(':
        ans = 'NO'
    else:
        cnt_l = 0
        cnt_r = 0
        for i in td:
            if i == '(':
                cnt_l += 1
            else:
                cnt_r += 1
            if cnt_r > cnt_l:
                ans = 'NO'
                break
        if cnt_l != cnt_r:
            ans = 'NO'
    print(ans)