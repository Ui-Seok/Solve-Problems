from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [ [] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque()
q.append(1)

visit = [False] * (n + 1)
visit[1] = True

answer = [0 for _ in range(n + 1)]

while q:
    x = q.popleft()
    for i in graph[x]:
        if not visit[i]:
            answer[i] += x
            visit[i] = True
            q.append(i)

for i in range(2, n + 1):
    print(answer[i])