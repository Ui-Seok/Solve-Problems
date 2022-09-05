import sys
input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

rev_board = [k[:] for k in board] 
ans = n**2

for i in range(n):
    for j in range(n):
        if rev_board[i][j] == 'T':
            rev_board[i][j] = 'H'
        else:
            rev_board[i][j] = 'T'
                    
for b in range(1<<n):
    tmp_board = []
    for i in range(n):
        if b & (1<<i):
            tmp_board.append(rev_board[i][:])
        else:
            tmp_board.append(board[i][:])
    
    cnt = 0
    for i in range(n):
        tmp = 0
        for j in range(n):
            if tmp_board[j][i] == 'T':
                tmp+=1
        cnt += min(tmp,n-tmp)
    ans = min(ans,cnt)
print(ans)