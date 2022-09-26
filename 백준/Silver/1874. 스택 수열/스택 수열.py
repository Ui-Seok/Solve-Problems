n = int(input())
answer_list = [int(input()) for _ in range(n)]
numbers = [i for i in range(1, n+1)]
stack = list()

pop_cnt = 0
push_pop_list = list()

cnt = 0
while cnt <= 200001:
    if stack and stack[-1] == answer_list[0]:
        pop_cnt += 1
        push_pop_list.append(1) # pop
        del answer_list[0]
        del stack[-1]
        
    else:    
        if numbers and numbers[0] == answer_list[0]:
            pop_cnt += 1    # count pop
            push_pop_list.append(0) # push
            push_pop_list.append(1) # pop
            del numbers[0]
            del answer_list[0]
        elif numbers:
            push_pop_list.append(0) # push
            stack.append(numbers[0])
            del numbers[0]

    cnt += 1

if pop_cnt != n:
    print('NO')
else:
    for i in push_pop_list:
        if not i: print('+')
        else: print('-')