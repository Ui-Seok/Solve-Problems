from collections import deque

n = int(input())
arr = deque([i for i in range(1, n+1)])

while len(arr) > 1:
    del arr[0]

    if len(arr) == 1:
        break
    else:
        pops = arr.popleft()
        arr.append(pops)

print(*arr)