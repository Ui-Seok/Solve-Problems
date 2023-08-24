import sys 
input = sys.stdin.readline

n, m = map(int, input().split())
tree_height = list(map(int, input().split()))

end = max(tree_height)
start = 1

while start <= end:
    mid = (end + start) // 2
    cnt = 0

    for tree in tree_height:
        if tree > mid:
            cnt += tree - mid

    if cnt >= m:
        start = mid + 1
    elif cnt < m:
        end = mid - 1

print(end)
