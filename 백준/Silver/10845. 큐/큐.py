from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

q = deque()
for _ in range(n):
    a = list(input().split())
    if a[0] == 'push':
        q.append(int(a[1]))

    elif a[0] == 'pop':
        if q:
            x = q.popleft()
            print(x)
        else:
            print(-1)

    elif a[0] == 'size':
        print(len(q))

    elif a[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

    elif a[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    elif a[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)