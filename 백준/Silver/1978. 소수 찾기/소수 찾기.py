n = int(input())
arr = list(map(int, input().split()))

def check_prime(num):
    sqrt_num = num ** (1/2)
    for i in range(2, int(sqrt_num+1)):
        if num % i == 0:
            return False
    return True

cnt = 0
for i in arr:
    if i > 1 and check_prime(i):
        cnt += 1

print(cnt)