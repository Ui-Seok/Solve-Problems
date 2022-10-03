from collections import deque

tc = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(ground, a, b):
    q = deque()
    q.append((a, b))
    ground[a][b] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if ground[nx][ny] == 1:
                    ground[nx][ny] = 0
                    q.append((nx, ny))

for _ in range(tc):
    m, n, k = map(int, input().split())
    ground = [([0] * m) for _ in range(n)]
    cnt = 0
    
    for _ in range(k):
        i, j = map(int, input().split())
        ground[j][i] = 1
    
    for b in range(m):
        for a in range(n):
            if ground[a][b] == 1:
                bfs(ground, a, b)
                cnt += 1
        
    print(cnt)