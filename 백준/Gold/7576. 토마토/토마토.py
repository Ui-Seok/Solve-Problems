from collections import deque

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append([i, j])

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
day = 0

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append([nx, ny])

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
        if box[i][j] > day:
            day = box[i][j]

print(day - 1)