n = int(input())
arr = list(map(int, input().split()))
m = int(input())
check_arr = list(map(int, input().split()))

arr.sort()

def binary_search(arr, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return target
    elif arr[mid] > target:
        return binary_search(arr, start, mid-1, target)
    else:
        return binary_search(arr, mid+1, end, target)

for i in check_arr:
    target = binary_search(arr, 0, n-1, i)
    if target == i:
        print(1)
    else:
        print(0)