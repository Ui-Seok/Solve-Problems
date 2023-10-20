import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))
visited = [False] * n
temp = []

def backtracking():
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(n):
        if not visited[i] and remember_me != arr[i]:
            visited[i] = True
            temp.append(arr[i])
            remember_me = arr[i]
            backtracking()
            visited[i] = False
            temp.pop()

backtracking()