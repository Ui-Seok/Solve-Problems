k, n = map(int, input().split())
length = [int(input()) for i in range(k)]
start, end = 1, max(length)

while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for i in length:
        cnt += i // mid
    
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)