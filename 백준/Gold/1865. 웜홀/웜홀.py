import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph.append((s, e, t))
        graph.append((e, s, t))
    
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph.append((s, e, -t))

    def bf(x):
        distance[x] = 0
        for i in range(n):
            for start, end, cost in graph:
                new_cost = distance[start] + cost
                if distance[end] > new_cost:
                    distance[end] = new_cost
                    if i == n - 1:
                        return True
        return False

    distance = [1e9] * (n + 1)

    if bf(1):
        print("YES")
    else:
        print("NO")