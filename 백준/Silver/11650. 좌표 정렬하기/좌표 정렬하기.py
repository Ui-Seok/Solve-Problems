import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))

arr = sorted(arr, key=lambda x: (x[0], x[1]))

for ar in arr:
    print(*ar)