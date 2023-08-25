from collections import deque
import sys
input = sys.stdin.readline

m, n, h = map(int, input().split())
q = deque()

graph = []
for i in range(h):
    arrs = []
    for j in range(n):
        arr = list(map(int, input().split()))
        for k in range(m):
            if arr[k] == 1:
                q.append((i, j, k))
        arrs.append(arr)
    graph.append(arrs)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while q:
    x, y, z = q.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
            if graph[nx][ny][nz] == 0:
                q.append((nx, ny, nz))
                graph[nx][ny][nz] = graph[x][y][z] + 1

answer = 0
break_point = False
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                break_point = True
                
        answer = max(answer, max(j))

if break_point:
    print("-1")
else:
    print(answer - 1)
