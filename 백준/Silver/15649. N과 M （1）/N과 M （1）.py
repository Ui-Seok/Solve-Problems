n, m = map(int, input().split())
answer = list()
visited = [False] * (n+1)

def DFS(num):
    if num == m:
        print(' '.join(map(str, answer)))
        return
    else:
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                answer.append(i)
                DFS(num+1)
                answer.pop()
                visited[i] = False

DFS(0)