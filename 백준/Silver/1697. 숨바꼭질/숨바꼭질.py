from collections import deque

n, k = map(int, input().split())

visited = [0 for _ in range(100001)]
visited[n] = 1

q = deque()
q.append(n)

while True:
    start = q.popleft()
    if start == k:
        print(visited[start] - 1)
        break

    if start > 0:
        if visited[start-1] == 0:
            visited[start-1] += visited[start] + 1
            q.append(start-1)

    if start < 100000:
        if visited[start+1] == 0:
            visited[start+1] += visited[start] + 1
            q.append(start+1)

    if start <= 50000:
        if visited[2*start] == 0:
            visited[2*start] += visited[start] + 1
            q.append(2*start)