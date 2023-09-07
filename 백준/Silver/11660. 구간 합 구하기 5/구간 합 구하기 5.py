import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
arr = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        arr[i + 1][j + 1] = graph[i][j] + arr[i][j + 1] + arr[i + 1][j] - arr[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1]
    print(answer)