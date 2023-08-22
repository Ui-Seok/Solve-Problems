import sys
input = sys.stdin.readline

n = int(input())

def check_round(number):
    if number - int(number) >= 0.5:
        return int(number) + 1
    else:
        return int(number)

if n == 0:
    print("0")

else:
    nums = sorted([int(input()) for _ in range(n)])
    r_num = check_round(n * 0.15)
    filterd = nums[r_num : (n - r_num)]
    answer = check_round(sum(filterd) / (n - 2 * r_num))

    print(answer)
