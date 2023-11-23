from collections import deque

def solution(places):
    answer = []
    
    for place in places:
        seat_info = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    seat_info.append((i, j))
        
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        tmp = True
        for a, b in seat_info:
            q = deque()
            q.append((a, b))
            visited = [[0] * 5 for _ in range(5)]
            visited[a][b] = 1

            cnt = 0
            
            while q:
                x, y = q.popleft()
                cnt += 1
                
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < 5 and 0 <= ny < 5 and place[nx][ny] != "X" and visited[nx][ny] == 0:
                        if place[nx][ny] == "P":
                            tmp = False
                        elif cnt == 1:
                            q.append((nx, ny))
                            visited[nx][ny] = 1

        if tmp:
            answer.append(1)
        else:
            answer.append(0)
                
        
    return answer