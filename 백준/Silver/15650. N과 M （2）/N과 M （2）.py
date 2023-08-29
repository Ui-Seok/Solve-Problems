from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]

comb_arr = combinations(arr, m)

for c in comb_arr:
    print(*c)