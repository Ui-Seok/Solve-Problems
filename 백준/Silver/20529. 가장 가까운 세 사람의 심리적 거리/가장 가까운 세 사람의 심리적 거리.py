import heapq
import sys
from itertools import combinations

input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    mbti_list = list(input().split())

    if n >= 48:
        print(0)
        continue

    answer = 0
    diff_list = []

    comb_list = combinations(mbti_list, 3)
    for c_mbti in comb_list:
        diff = 0
        for i in range(4):
            if c_mbti[0][i] != c_mbti[1][i]:
                diff += 1
            if c_mbti[1][i] != c_mbti[2][i]:
                diff += 1
            if c_mbti[2][i] != c_mbti[0][i]:
                diff += 1
        heapq.heappush(diff_list, diff)

    print(heapq.heappop(diff_list))