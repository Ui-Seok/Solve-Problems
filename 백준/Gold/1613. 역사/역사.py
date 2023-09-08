from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = {}
for _ in range(k):
    a, b = map(int, input().split())
    if graph.get(a):
        graph[a].append(b)
    else:
        graph[a] = [b]

s = int(input())
for _ in range(s):
    c, d = map(int, input().split())
    answer = 0

    q = deque()
    q.append(c)
    
    visit = [False] * (n + 1)
    visit[c] = True

    while q:
        x = q.popleft()
        if x == d:
            answer = -1
            break
        
        if graph.get(x):
            for i in graph[x]:
                if not visit[i]:
                    visit[i] = True
                    q.append(i)

    else:
        q = deque()
        q.append(d)

        visit = [False] * (n + 1)
        visit[d] = True

        while q:
            x = q.popleft()
            if x == c:
                answer = 1
                break

            if graph.get(x):
                for i in graph[x]:
                    if not visit[i]:
                        visit[i] = True
                        q.append(i)

    print(answer)