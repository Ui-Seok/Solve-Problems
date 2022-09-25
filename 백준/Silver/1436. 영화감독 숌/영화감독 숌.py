n = int(input())

start_num = 666
cnt = 1

if n == 1:
    print(666)
else:
    while True:
        start_num += 1
        if '666' in str(start_num):
            cnt += 1

        if n == cnt:
            print(start_num)
            break