n = int(input())
check_arr = [int(input()) for _ in range(n)]
stack_arr = [0]
answer = list()

idx = 0
st_num = 1
while idx < n and st_num <= n+1:
    if stack_arr[-1] != check_arr[idx]:
        stack_arr.append(st_num)
        st_num += 1
        answer.append('+')
    else:
        stack_arr.pop()
        idx += 1
        answer.append('-')

if stack_arr != [0]:
    print('NO')
else:
    for i in answer:
        print(*i)