import heapq
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if graph.get(a):
        graph[a].append((b, c))
    else:
        graph[a] = [(b, c)]
    
start, end = map(int, input().split())

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
            for cur, d in graph[place]:
                cost = dist + d
                if distance[cur] > cost:
                    distance[cur] = cost
                    heapq.heappush(q, (cost, cur))
        else:
            continue

    return distance

print(dk(start)[end])