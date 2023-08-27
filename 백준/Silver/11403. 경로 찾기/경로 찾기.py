import sys
input = sys.stdin.readline

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

visit = [False] * n

def dfs(x):
    for i in range(n):
        if graph[x][i] == 1 and not visit[i]:
            visit[i] = True
            dfs(i)

for i in range(n):
    dfs(i)
    for j in range(n):
        if visit[j]:
            print(1, end = " ")
        else:
            print(0, end = " ")
    print()
    visit = [False] * n