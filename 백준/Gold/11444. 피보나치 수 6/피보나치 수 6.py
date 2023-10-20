import sys
input = sys.stdin.readline

n = int(input())
p = 1000000007

def power(fi, n):
    if n == 1:
        return fi
    elif n % 2:
        return multi(power(fi, n - 1), fi)
    else:
        return power(multi(fi, fi), n // 2)

def multi(a, b):
    temp = [[0] * len(b[0]) for _ in range(2)]
    for i in range(2):
        for j in range(len(b[0])):
            sum = 0
            for k in range(2):
                sum += a[i][k] * b[k][j]
            temp[i][j] = sum % p

    return temp

fi = [[1, 1], [1, 0]]
start = [[1], [1]]

if n < 3:
    print(1)
else:
    print(multi(power(fi, n - 2), start)[0][0])