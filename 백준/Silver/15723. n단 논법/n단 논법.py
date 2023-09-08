import sys
input = sys.stdin.readline

n = int(input())

graph = [[0] * 26 for _ in range(26)]
for _ in range(n):
    a, b = input().strip().split(" is ")
    a_ord = ord(a) - ord("a")
    b_ord = ord(b) - ord("a")

    graph[a_ord][b_ord] = 1

for k in range(26):
    for i in range(26):
        for j in range(26):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1


m = int(input())
for _ in range(m):
    x, y = input().strip().split(" is ")
    x_ord = ord(x) - ord("a")
    y_ord = ord(y) - ord("a")

    if graph[x_ord][y_ord] == 1:
        print("T")
    else:
        print("F")