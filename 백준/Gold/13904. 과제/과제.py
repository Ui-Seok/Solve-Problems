n = int(input())

score = []

for _ in range(n):
    a, b = map(int, input().split())
    score.append((a, b))

score = sorted(score, key=lambda x: -x[1])
max_days = max(score)[0]
day = [0] * (max_days + 1)

for d, s in score:
    if not day[d]:
        day[d] = s
    else:
        while d > 1:
            d -= 1
            if not day[d]:
                day[d] = s
                break

print(sum(day))