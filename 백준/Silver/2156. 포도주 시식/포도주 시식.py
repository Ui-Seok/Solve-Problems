'''
시작시간: 01시 15분
종료시간: 01시 54분
'''

n = int(input())
glass = [int(input()) for _ in range(n)]
dp = [0] * n

if n > 3:
    dp[0] = glass[0]
    dp[1] = glass[0] + glass[1]
    dp[2] = max(glass[0] + glass[2], glass[1] + glass[2], dp[1])

    for i in range(3, n):
        dp[i] = max(dp[i - 1], dp[i - 2] + glass[i], dp[i - 3] + glass[i - 1] + glass[i])
    print(max(dp))
elif n == 3:
    print(max(glass[0] + glass[2], glass[1] + glass[2], glass[0] + glass[1]))
elif n == 2:
    print(glass[0] + glass[1])
elif n == 1:
    print(glass[0])