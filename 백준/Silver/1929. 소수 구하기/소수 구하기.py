m, n = map(int, input().split())

# 소수 판별 코드
def check_prime(num):
    root = int(num ** (1/2))
    for i in range(2, root + 1):
        if num % i == 0:
            return False
    return True

for i in range(m, n+1):
    if i == 1:
        continue
    if check_prime(i):
        print(i)