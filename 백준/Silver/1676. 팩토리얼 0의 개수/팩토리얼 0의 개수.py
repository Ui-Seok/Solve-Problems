n = int(input())

num_list = [i for i in range(1, n+1)]
cnt_5 = 0

for num in num_list:
    if num % 125 == 0:
        cnt_5 += 3
    elif num % 25 == 0:
        cnt_5 += 2
    elif num % 5 == 0:
        cnt_5 += 1

print(cnt_5)