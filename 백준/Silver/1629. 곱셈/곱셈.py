import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())

def dac(x, y):
    if y == 1:
        return x % c
    
    temp = dac(x, y // 2)
    if y % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c

print(dac(a, b))