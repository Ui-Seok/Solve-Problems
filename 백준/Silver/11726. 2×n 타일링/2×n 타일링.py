n = int(input())

box_list = [0 for _ in range(1001)]

box_list[1] = 1
box_list[2] = 2

if n > 2:
    for num in range(3, n+1):
        box_list[num] = box_list[num-2] + box_list[num-1]

print(box_list[n] % 10007)