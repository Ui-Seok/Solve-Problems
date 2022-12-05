import sys
input = sys.stdin.readline

k = int(input())
arr = list()

for _ in range(k):
    a = int(input())
    if a == 0:
        del arr[-1]
    else:
        arr.append(a)

print(sum(arr))