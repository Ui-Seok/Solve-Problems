from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = deque()
graph = []
visit = [[False] * m for _ in range(n)]
answer = [[-1] * m for _ in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))

    for j in range(m):
        if arr[j] == 2:
            q.append((i, j))
            visit[i][j] = True
            answer[i][j] = 0

        elif arr[j] == 0:
            answer[i][j] = 0

    graph.append(arr)

move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()

    for dx, dy in move:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                visit[nx][ny] = True
                answer[nx][ny] = answer[x][y] + 1

for row in answer:
    for i in row:
        print(i, end=" ")
    print()