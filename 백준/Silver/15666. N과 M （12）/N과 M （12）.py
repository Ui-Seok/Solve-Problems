import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = sorted(set(list(map(int, input().split()))))
temp = []

def dfs(start):
    if len(temp) == m:
        print(*temp)
        return

    for i in range(start, len(arr)):
        temp.append(arr[i])
        dfs(i)
        temp.pop()

dfs(0)