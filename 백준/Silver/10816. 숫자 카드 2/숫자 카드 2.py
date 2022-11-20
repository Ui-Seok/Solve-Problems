import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
check_arr = list(map(int, input().split()))

hashmap = {}
for i in arr:
    if hashmap.get(i) == None:
        hashmap[i] = 1
    else:
        hashmap[i] += 1

for j in check_arr:
    if hashmap.get(j) == None:
        print(0, end=' ')
    else:
        print(hashmap[j], end=' ')