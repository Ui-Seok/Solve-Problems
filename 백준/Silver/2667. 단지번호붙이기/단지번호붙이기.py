from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()

graph = []
for _ in range(n):
    arr = list(input().rstrip())
    arr_ = []
    for i in arr:
        arr_.append(int(i))

    graph.append(arr_)

move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(graph, x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in move:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx, ny))
                    cnt += 1
    return cnt
    
answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            answer.append(bfs(graph, i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)