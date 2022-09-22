arr = list(map(int, input().split()))
new_arr = list()

for i in arr:
    new_arr.append(i**2)

sum_num = sum(new_arr)
print(sum_num % 10)