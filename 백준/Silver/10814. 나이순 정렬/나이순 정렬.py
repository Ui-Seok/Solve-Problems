n = int(input())
arr = list()
for _ in range(n):
    a, b = input().split()
    arr.append((int(a), b))

arr = sorted(arr, key=lambda x: x[0])

for i in arr:
    print(*i)