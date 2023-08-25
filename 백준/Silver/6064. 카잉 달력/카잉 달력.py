import sys
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    m, n, x, y = map(int, input().split())
    
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            print(k)
            break
        k += m
    else:
        print("-1")