import heapq
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start_node = int(input())

graph = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    if graph.get(a):
        graph[a].append((b, c))
    else:
        graph[a] = [(b, c)]

def dk(x):
    q = []
    distance = [1e9] * (v + 1)

    heapq.heappush(q, (0, x))
    distance[x] = 0

    while q:
        dist, now_place = heapq.heappop(q)

        if distance[now_place] < dist:
            continue

        if graph.get(now_place):
            for place, d in graph[now_place]:
                cost = dist + d
                if distance[place] > cost:
                    distance[place] = cost
                    heapq.heappush(q, (cost, place))
        else:
            continue

    return distance

result = dk(start_node)

for i in range(1, v+1):
    if result[i] > 1e8:
        print("INF", end="\n")
    else:
        print(result[i], end="\n")