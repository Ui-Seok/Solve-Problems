n = int(input())
answer_list = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

answer_list.sort()

def binary_search(data, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return target
    elif data[mid] > target:
        return binary_search(data, start, mid-1, target)
    else:
        return binary_search(data, mid+1, end, target)

for i in check_list:
    ch = binary_search(answer_list, 0, n-1, i)
    if ch == i:
        print(1)
    else:
        print(0)