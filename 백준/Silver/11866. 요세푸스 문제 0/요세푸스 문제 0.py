n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]

idx = -1
answer_list = list()
while arr:
    idx += k
    if idx >= len(arr):
        idx %= len(arr)

    a = arr.pop(idx)
    idx -= 1
    answer_list.append(a)

print('<', end='')
for i in range(n-1):
    print(f'{answer_list[i]}', end=', ')
print(f'{answer_list[-1]}>')