x, n = map(int, input().split())
visitors = list(map(int, input().split()))

visit = []
sum_visitor = sum(visitors[:n])
visit.append(sum_visitor)

for i in range(x - n):
    sum_visitor = sum_visitor - visitors[i] + visitors[i + n]
    visit.append(sum_visitor)

max_visit = max(visit)
count = visit.count(max_visit)

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(count)