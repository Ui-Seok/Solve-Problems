import sys
input = sys.stdin.readline

n = int(input())
num = int(input())

graph = [[0] * n for _ in range(n)]
tmp = n ** 2
graph[0][0] = tmp

x, y = 0, 0
answer = (0, 0)
for _ in range(n ** 2):
    if tmp == 1:
        break

    if 0 <= (x + 1) < n and graph[x + 1][y] == 0:
        while True:
            if x + 1 >= n or graph[x + 1][y] != 0: break
            if tmp == num:
                answer = (x, y)
            x += 1
            tmp -= 1
            graph[x][y] = tmp

    elif 0 <= (y + 1) < n and graph[x][y + 1] == 0:
        while True:
            if y + 1 >= n or graph[x][y + 1] != 0: break
            if tmp == num:
                answer = (x, y)
            y += 1
            tmp -= 1
            graph[x][y] = tmp

    elif 0 <= (x - 1) < n and graph[x - 1][y] == 0:
        while True:
            if x <= 0 or graph[x - 1][y] != 0: break
            if tmp == num:
                answer = (x, y)
            x -= 1
            tmp -= 1
            graph[x][y] = tmp

    elif 0 <= (y - 1) < n and graph[x][y - 1] == 0:
        while True:
            if y <= 0 or graph[x][y - 1] != 0: break
            if tmp == num:
                answer = (x, y)
            y -= 1
            tmp -= 1
            graph[x][y] = tmp


for g in graph:
    print(*g)

if num == 1:
    print(n // 2 + 1, n // 2 + 1)
else:
    for a in answer:
        print(a + 1, end = " ")