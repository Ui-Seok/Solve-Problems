a, b = map(int, input().split())
c = int(input())

minute_sum = (b + c) // 60
if minute_sum >= 1:
    b = b + c - minute_sum * 60
    a = a + minute_sum

    if a > 23:
        a = a - 24

else:
    b = b + c

print(a, b)