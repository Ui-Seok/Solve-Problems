from collections import deque

n, m, v = map(int, input().split())
graph = {i: [i] for i in range(n+1)}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    graph[i].sort()

# dfs
visited = [False for _ in range(n+1)]
answer_dfs = list()
def dfs(graph, start, visited):
    answer_dfs.append(start)
    visited[start] = True
    for i in graph[start]:
        if visited[i]:
            continue
        else:
            dfs(graph, i, visited)

dfs(graph, v, visited)
print(*answer_dfs)

# bfs
visited = [False for _ in range(n+1)]
visited[v] = True
q = deque()
q.append(v)
answer_bfs = list()

while q:
    start = q.popleft()
    answer_bfs.append(start)
    for i in graph[start]:
        if visited[i]:
            continue
        else:
            visited[i] = True
            q.append(i)

print(*answer_bfs)