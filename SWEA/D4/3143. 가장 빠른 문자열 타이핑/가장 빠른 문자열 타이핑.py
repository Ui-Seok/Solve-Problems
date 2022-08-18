'''
시작시간: 00시 39분
종료시간: 00시 41분
'''

t = int(input())
for tc in range(1, t + 1):
    a, b = input().split()
    a = a.replace(b, 'a')
    print('#{} {}'.format(tc, len(a)))