n = int(input())
persons = [list(map(int, input().split())) for _ in range(n)]
answer = [1 for _ in range(n)]

for i in range(n):
    weight, height = persons[i]
    rank = answer[i]

    for j in range(n):
        if weight < persons[j][0] and height < persons[j][1]:
            rank += 1

    answer[i] = rank

print(*answer)