n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
sum_num = arr[0]
count = 0
while end < n:
    if sum_num < m:
        end += 1
        if end == n:
            break
        sum_num += arr[end]
    elif sum_num > m:
        sum_num -= arr[start]
        start += 1
    elif sum_num == m:
        count += 1
        end += 1
        if end == n:
            break
        sum_num += arr[end]
print(count)