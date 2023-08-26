import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
answer = 0

arr = arr[::-1]
for i in arr:
    if i <= k:
        answer += k // i
        k = k % i

print(answer)