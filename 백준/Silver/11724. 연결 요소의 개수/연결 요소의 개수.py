from collections import deque

n, m = map(int, input().split())

# graph 불러오기(양방향)
graph = dict()

for _ in range(m):
    a, b = map(int, input().split())
    # a에 대해 선 연결
    if graph.get(a) == None:
        graph[a] = [b]
    else:
        graph[a].append(b)

    # b에 대해 선 연결
    if graph.get(b) == None:
        graph[b] = [a]
    else:
        graph[b].append(a)

# 각 정점마다 방문 확인
visited = [False for _ in range(n+1)]

# 큐 생성 및 연결요소(roop) 정의
q = deque()
roop = 0

# visited를 하나씩 확인하며 루프가 끊어진 지점부터 다시 연결 확인
for start in range(1, n+1):
    # 만약 정점에 대한 간선 정보가 없을경우 자기 자신 추가
    if graph.get(start) == None:
        graph[start] = [start]

    # 방문이 안된 정점의 경우
    if visited[start] == False:
        # 시작점 생성 및 방문 체크
        visited[start] = True
        q.append(start)

        # BFS 시작
        while q:
            x = q.popleft()
            for a in graph[x]:
                if visited[a] == False:
                    visited[a] = True
                    q.append(a)
        
        # BFS가 끝나면 연결이 끝나므로 연결요소 +1
        roop += 1

# 결과 확인
print(roop)