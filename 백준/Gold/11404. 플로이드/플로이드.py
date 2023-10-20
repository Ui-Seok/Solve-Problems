import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 1e9

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for x in range(1, n + 1):
    for y in range(1, n + 1):
        if x == y:
            graph[x][y] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end = " ")
        else:
            print(graph[a][b], end = " ")

    print()
