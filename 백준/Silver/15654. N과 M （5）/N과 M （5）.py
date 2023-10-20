from itertools import permutations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

comb_arr = permutations(arr, m)

for i in comb_arr:
    print(*i)