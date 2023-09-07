import sys
input = sys.stdin.readline

a_arr = input().strip()
b_arr = input().strip()
a_len = len(a_arr)
b_len = len(b_arr)

cache = [0] * b_len

for i in range(a_len):
    cnt = 0
    for j in range(b_len):
        if cnt < cache[j]:
            cnt = cache[j]
        elif a_arr[i] == b_arr[j]:
            cache[j] = cnt + 1

print(max(cache))