n = int(input())
arr = [int(input()) for _ in range(n)]
max_num = 0

for i in arr:
    if i > max_num:
        max_num = i

dp = [[0, 0] for _ in range(41)]

dp[0] = [1, 0]
dp[1] = [0, 1]

if max_num > 1:
    for j in range(2, max_num+1):
        dp[j][0] = dp[j-1][0] + dp[j-2][0]
        dp[j][1] = dp[j-1][1] + dp[j-2][1]

for num in arr:
    print(*dp[num])