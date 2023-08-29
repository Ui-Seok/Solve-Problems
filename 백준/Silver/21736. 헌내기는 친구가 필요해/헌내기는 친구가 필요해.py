from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, (input().split()))
q = deque()

graph = []
for i in range(n):
    arr = list(input())
    n_arr = []
    for j in range(m):
        if arr[j] == "O":
            n_arr.append(0)
        elif arr[j] == "I":
            n_arr.append(2)
            q.append((i, j))
        elif arr[j] == "X":
            n_arr.append(-1)
        else:
            n_arr.append(1)
    graph.append(n_arr)

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visit = [[False] * m for _ in range(n)]
answer = 0

while q:
    x, y = q.popleft()
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            if graph[nx][ny] == 1:
                visit[nx][ny] = True
                q.append((nx, ny))
                answer += 1
            elif graph[nx][ny] == 0:
                visit[nx][ny] = True
                q.append((nx, ny))
            elif graph[nx][ny] == -1:
                continue

if answer:
    print(answer)
else:
    print("TT")