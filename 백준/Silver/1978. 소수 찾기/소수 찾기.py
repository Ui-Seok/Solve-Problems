n = int(input())
arr = list(map(int, input().split()))
cnt = 0

def is_Prime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        else:
            return True

for num in arr:
    if is_Prime(num):
        cnt += 1

print(cnt)