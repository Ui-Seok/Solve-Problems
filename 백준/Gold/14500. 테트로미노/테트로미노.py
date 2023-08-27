import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

maxValue = -1

# ㅓ, ㅏ, ㅗ, ㅜ 제외 모양
def dfs(x, y, check, cnt):
    global maxValue
    if cnt == 4:
        maxValue = max(maxValue, check)
        return
    
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
            visit[nx][ny] = True
            dfs(nx, ny, check + graph[nx][ny], cnt + 1)
            visit[nx][ny] = False

# ㅓ, ㅏ, ㅗ, ㅜ 모양
def symbol(x, y):
    global maxValue
    for i in range(4):
        tmp = graph[x][y]
        for j in range(3):
            k = (i + j) % 4
            dx, dy = move[k]
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < m:
                tmp += graph[nx][ny]
            else:
                tmp = 0
                break

        maxValue = max(maxValue, tmp)

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visit[i][j] = False

        symbol(i, j)

print(maxValue)