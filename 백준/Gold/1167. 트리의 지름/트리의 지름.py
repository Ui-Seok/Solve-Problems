import sys
input = sys.stdin.readline

v = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(v):
    arr = list(map(int, input().split()))
    n = len(arr)
    for i in range(1, n-1, 2):
        graph[arr[0]].append((arr[i], arr[i + 1]))

def dfs(x, temp):
    for node, distance in graph[x]:
        if visit[node] == -1:
            visit[node] = temp + distance
            dfs(node, temp + distance)

visit = [-1] * (v + 1)
visit[1] = 0
dfs(1, 0)

new_start = visit.index(max(visit))
visit = [-1] * (v + 1)
visit[new_start] = 0
dfs(new_start, 0)

print(max(visit))