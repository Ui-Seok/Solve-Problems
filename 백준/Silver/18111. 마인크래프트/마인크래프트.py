import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(n)]

height = 0
answer = 10000000000000000000000

for i in range(257):
    use_block = 0
    remove_block = 0

    for x in range(n):
        for y in range(m):
            if ground[x][y] < i:
                use_block += i - ground[x][y]
            else:
                remove_block += ground[x][y] - i

    if b + remove_block < use_block:
        continue

    time = 2 * remove_block + use_block

    if time <= answer:
        answer = time
        height = i

print(answer, height)