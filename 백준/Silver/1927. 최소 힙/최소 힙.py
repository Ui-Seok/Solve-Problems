import heapq
import sys

input = sys.stdin.readline
n = int(input())

arr = list()
for _ in range(n):
    a = int(input())
    if a == 0:
        if not arr:
            print(0)
        else:
            item = heapq.heappop(arr)
            print(item)
    else:
        heapq.heappush(arr, a)