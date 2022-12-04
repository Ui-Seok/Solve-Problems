from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    a = int(input())
    if a == 0:
        if arr:
            max_num = heappop(arr)
            print(-max_num)
        else:
            print(0)
    else:
        heappush(arr, -a)