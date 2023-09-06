import heapq
import sys
input = sys.stdin.readline

n = int(input())
graph = {}
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    if graph.get(a):
        graph[a].append((b, c))
    else:
        graph[a] = [(b, c)]
    if graph.get(b):
        graph[b].append((a, c))
    else:
        graph[b] = [(a, c)]

def dk(x):
    q = []
    distance = [int(1e9)] * (n + 1)

    heapq.heappush(q, (0, x))
    distance[x] = 0

    while q:
        dist, place = heapq.heappop(q)
        if distance[place] < dist:
            continue
        
        if graph.get(place):
            for node, d in graph[place]:
                cost = dist + d
                if distance[node] > cost:
                    distance[node] = cost
                    heapq.heappush(q, (cost, node))
        else:
            continue
    
    return distance

first_distance = dk(1)
new_start_id = first_distance.index(max(first_distance[1:]))

result_distance = dk(new_start_id)
result_value = max(result_distance[1:])

print(result_value)