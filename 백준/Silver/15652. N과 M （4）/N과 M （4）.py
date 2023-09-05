from itertools import combinations_with_replacement
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n + 1)]

comb = combinations_with_replacement(arr ,m)

for c in comb:
    print(*c)