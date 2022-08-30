from collections import deque

n, m = map(int, input().split())

maps = [list(map(int, input())) for _ in range(n)]
distance = [[[1, 1] for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y, z):
    queue = deque()
    queue.append((x, y, z))

    while queue:
        x, y, z = queue.popleft()

        if z == 0:
            can_break_wall = True
        else:
            can_break_wall = False

        if x == n - 1 and y == m - 1:
            return distance[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < n) and (0 <= ny < m):
                if maps[nx][ny] == 1 and can_break_wall:
                    distance[nx][ny][1] = distance[x][y][0] + 1
                    queue.append((nx, ny, 1))
                elif maps[nx][ny] == 0 and distance[nx][ny][z] == 1:
                    distance[nx][ny][z] = distance[x][y][z] + 1
                    queue.append((nx, ny, z))
    return -1

print(bfs(0, 0, 0))
