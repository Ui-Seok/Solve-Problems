from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

time = [-1 for _ in range(100001)]
time[n] = 0

q = deque()
q.append(n)

answer = 0
while q:
    x = q.popleft()
    if x == k:
        print(time[x])
        break

    if 0 <= x - 1 < 100001 and time[x - 1] == -1:
        time[x - 1] = time[x] + 1
        q.append(x - 1)
    
    if 0 <= 2 * x < 100001 and time[2 * x] == -1:
        time[2 * x] = time[x]
        q.append(2 * x)
        
    if 0 <= x + 1 < 100001 and time[x + 1] == -1:
        time[x + 1] = time[x] + 1
        q.append(x + 1)
