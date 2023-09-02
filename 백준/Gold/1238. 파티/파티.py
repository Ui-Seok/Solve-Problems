import heapq
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int,input().split())
    graph[s].append((e, t))

def dijkstra(start_point):
    q = []
    distance = [1e9] * (n + 1)

    heapq.heappush(q, (0, start_point))
    distance[start_point] = 0

    while q:
        now_distance, now_place = heapq.heappop(q)

        if distance[now_place] < now_distance:
            continue

        for start, cost in graph[now_place]:
            new_cost = now_distance + cost

            if distance[start] > new_cost:
                distance[start] = new_cost
                heapq.heappush(q, (new_cost, start))
    
    return distance

result = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(x)
    result = max(result, go[x] + back[i])

print(result)