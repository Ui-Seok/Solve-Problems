import sys
input = sys.stdin.readline

n = int(input())

stack = list()
for _ in range(n):
    a = list(input().split())

    if a[0] == 'push':
        x = a[1]
        stack.append(x)

    elif a[0] == 'pop':
        if stack:
            pop_ = stack.pop()
            print(pop_)
        else:
            print(-1)

    elif a[0] == 'size':
        print(len(stack))

    elif a[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif a[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)