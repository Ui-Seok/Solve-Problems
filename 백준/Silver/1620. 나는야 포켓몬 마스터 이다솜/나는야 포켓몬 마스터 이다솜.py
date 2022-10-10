import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pocketmon_list = [input().strip() for _ in range(n)]
problem = [input().strip() for _ in range(m)]

for pr in problem:
    if pr.isdigit():
        print(pocketmon_list[int(pr)-1])
    else:
        print(pocketmon_list.index(pr) + 1)