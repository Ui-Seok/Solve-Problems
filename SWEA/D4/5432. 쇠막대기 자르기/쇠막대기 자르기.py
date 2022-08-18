'''
시작시간: 10시 39분
종료시간: 11시 05분
'''
t = int(input())
for tc in range(1, t + 1):
    parts = list(input())
    stack = []
    count = 0
    last_pop = 0
    for i in parts:
        if i == '(':
            stack.append(i)
            last_pop = 0
        elif i == ')':
            if last_pop == 1:
                count += 1
                del stack[-1]
                last_pop = 1
            elif last_pop == 0:
                del stack[-1]
                count += len(stack)
                last_pop = 1

    print('#{} {}'.format(tc, count))