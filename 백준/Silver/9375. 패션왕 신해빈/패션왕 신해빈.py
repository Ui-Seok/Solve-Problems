from collections import Counter
import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    answer = n

    cloth, part = [], []
    for _ in range(n):
        a, b = input().split()
        cloth.append(a)
        part.append(b)

    wear_cnt = Counter(part)
    cnt = 1

    for key in wear_cnt:
        cnt *= wear_cnt[key] + 1

    print(cnt - 1)