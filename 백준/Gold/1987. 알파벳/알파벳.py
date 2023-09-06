import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input().rstrip()) for _ in range(r)]

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

visit = set()
visit.add(graph[0][0])
cnt = 1
answer = 0

def dfs(x, y, cnt):
    global answer
    answer = max(cnt, answer)

    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < r and 0 <= ny < c:
            if not graph[nx][ny] in visit:
                visit.add(graph[nx][ny])
                dfs(nx, ny, cnt + 1)
                visit.remove(graph[nx][ny])

dfs(0, 0, cnt)
print(answer)