import sys
input = sys.stdin.readline

n = int(input())
arr = list()
for _ in range(n):
    start, end = map(int, input().split())
    arr.append((start, end))

arr = sorted(arr, key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0

for start, end in arr:
    if end_time <= start:
        cnt += 1
        end_time = end

print(cnt)