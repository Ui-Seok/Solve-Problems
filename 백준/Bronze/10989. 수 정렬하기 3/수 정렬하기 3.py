import sys
input = sys.stdin.readline

n = int(input())
arr = [0 for _ in range(10001)]

for _ in range(n):
    arr[int(input())] += 1

for idx, j in enumerate(arr):
    if j == 0:
        continue
    else:
        for _ in range(j):
            print(idx)