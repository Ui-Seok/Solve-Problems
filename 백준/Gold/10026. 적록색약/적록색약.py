import sys
sys.setrecursionlimit(10**6)

n = int(input())
graph = [list(input()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

color_cnt = 0
weakness_cnt = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y):
    visited[x][y] = True
    now_color = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False:
                if graph[nx][ny] == now_color:
                    dfs(nx, ny)

# 적록색약이 아닌 사람이 봤을 때의 구역의 수 찾기
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            color_cnt += 1

# 적록색약을 위한 Green to Red
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

# 방문체크 다시 선언
visited = [[False] * n for _ in range(n)]

# 적록색약인 사람이 봤을 때의 구역의 수 찾기
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            weakness_cnt += 1

print(color_cnt, weakness_cnt)
