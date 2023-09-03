import heapq
import sys
input = sys.stdin.readline

n, e = map(int, input().split())
graph = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    if graph.get(a):
        graph[a].append((b, c))
    else:
        graph[a] = [(b, c)]
    
    if graph.get(b):
        graph[b].append((a, c))
    else:
        graph[b] = [(a, c)]

v1, v2 = map(int, input().split())

def dk(x):
    q = []
    distance = [1e9] * (n + 1)

    heapq.heappush(q, (0, x))
    distance[x] = 0

    while q:
        dist, place = heapq.heappop(q)

        if distance[place] < dist:
            continue

        for start, d in graph[place]:
            cost = dist + d

            if distance[start] > cost:
                distance[start] = cost
                heapq.heappush(q, (cost, start))

    return distance

if graph.get(v1) and graph.get(v2):
    root_a = dk(1)[v1] + dk(v1)[v2] + dk(v2)[n]
    root_b = dk(1)[v2] + dk(v2)[v1] + dk(v1)[n]
    result = min(root_a, root_b)
else:
    result = -1
    
if result > 1e7:
    print(-1)
else:
    print(result)