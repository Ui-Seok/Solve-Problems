n = int(input())

dp = [0 for _ in range(int(1e+6 + 1))]

dp[1] = 0
dp[2] = 1
dp[3] = 1

if n > 3:
    for num in range(4, n+1):
        if num % 3 == 0 and num % 2 == 0:
            dp[num] = min(dp[num-1], dp[num//2], dp[num//3]) + 1
        elif num % 3 == 0:
            dp[num] = min(dp[num-1], dp[num//3]) + 1
        elif num % 2 == 0:
            dp[num] = min(dp[num-1], dp[num//2]) + 1
        else:
            dp[num] = dp[num-1] + 1
    print(dp[n])
else:
    print(dp[n])