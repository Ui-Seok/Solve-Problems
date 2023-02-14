n = int(input())
arr = dict()

for _ in range(n):
    a = input()
    arr[a] = len(a)

arr = sorted(arr.items(), key=lambda x: (x[1], x[0]))

for k in arr:
    print(k[0])