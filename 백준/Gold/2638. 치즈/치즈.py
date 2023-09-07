from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visit = [[False] * m for _ in range(n)]
melt = [[0] * m for _ in range(n)]

q = deque()
q.append((0, 0))
visit[0][0] = True
answer = 0

while True:
    if q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if graph[nx][ny] == 1:
                    melt[nx][ny] += 1
                else:
                    visit[nx][ny] = True
                    q.append((nx, ny))
    else:
        for i in range(n):
            for j in range(m):
                if melt[i][j] >= 2:
                    graph[i][j] = 0

        answer += 1
        if not 1 in max(graph):
            break

        visit = [[False] * m for _ in range(n)]
        melt = [[0] * m for _ in range(n)]
        q.append((0, 0))

print(answer)
