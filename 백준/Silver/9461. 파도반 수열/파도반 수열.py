import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    
    arr = [1, 1, 1, 2, 2]
    if n > 5:
        for i in range(6, n + 1):
            arr.append(arr[i - 6] + arr[i - 2])
        answer = arr[n - 1]
    else:
        answer = arr[n - 1]

    print(answer)
