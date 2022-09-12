n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n
answer = []

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
print(max_dp)
for j in range(n-1, -1, -1):
    if dp[j] == max_dp:
        answer.append(arr[j])
        max_dp -= 1

answer = answer[::-1]
print(*answer)