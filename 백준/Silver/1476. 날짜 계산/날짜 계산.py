import sys
input = sys.stdin.readline

e, s, m = map(int, input().split())

cnt = 0
x, y, z = 0, 0, 0
while True:
    if x == e and y == s and z == m:
        print(cnt)
        break

    x += 1
    y += 1
    z += 1
    cnt += 1
    if x > 15:
        x = 1
    
    if y > 28:
        y = 1
    
    if z > 19:
        z = 1