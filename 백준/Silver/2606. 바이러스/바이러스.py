from collections import deque
import sys
input = sys.stdin.readline

computers = int(input())
nodes = int(input())

graph = dict()
for _ in range(nodes):
    a, b = map(int, input().split())

    if graph.get(a):
        graph[a].append(b)
    else:
        graph[a] = [b]
    
    if graph.get(b):
        graph[b].append(a)
    else:
        graph[b] = [a]

if graph.get(1):
    check_list = [False for _ in range(computers + 1)]
    q = deque()
    q.append(1)
    answer = 0

    while q:
        x = q.popleft()
        for i in graph[x]:
            if check_list[i] == False:
                check_list[i] = True
                q.append(i)
                answer += 1
            else:
                continue
        
    print(answer - 1)

else:
    print(0)