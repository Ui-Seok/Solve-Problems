from itertools import permutations

n, m = map(int, input().split())
arr = list(i for i in range(1, n+1))

nums = permutations(arr, m)

for i in nums:
    for j in i:
        print(j, end=' ')
    print()