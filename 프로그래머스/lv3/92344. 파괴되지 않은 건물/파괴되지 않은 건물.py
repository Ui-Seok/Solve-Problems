def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    sum_graph = [[0] * (M + 1) for _ in range(N + 1)]
    
    for tp, r1, c1, r2, c2, degree in skill:
        if tp == 1:
            degree = -degree
            
        sum_graph[r1][c1] += degree
        sum_graph[r2 + 1][c1] -= degree
        sum_graph[r1][c2 + 1] -= degree
        sum_graph[r2 + 1][c2 + 1] += degree
        
    for i in range(N):
        for j in range(1, M):
            sum_graph[i][j] += sum_graph[i][j - 1]
            
    for j in range(M):
        for i in range(1, N):
            sum_graph[i][j] += sum_graph[i - 1][j]
            
    for x in range(N):
        for y in range(M):
            if board[x][y] + sum_graph[x][y] > 0:
                answer += 1
    
    return answer