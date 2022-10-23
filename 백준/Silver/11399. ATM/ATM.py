n = int(input())
times = list(map(int, input().split()))

times.sort()

answer = list()
answer.append(times[0])

for i in range(1, n):
    answer.append(answer[-1]+times[i])

print(sum(answer))