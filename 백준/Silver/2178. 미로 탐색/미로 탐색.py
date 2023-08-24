from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
q = deque()

graph = []
for _ in range(n):
    arr = list(input().rstrip())
    arr_ = []
    for i in arr:
        arr_.append(int(i))
    graph.append(arr_)

visit = [[False] * m for _ in range(n)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
q.append((0, 0))

while q:
    x, y = q.popleft()
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                visit[nx][ny] = True
                graph[nx][ny] = graph[x][y] + 1

print(graph[n - 1][m - 1])