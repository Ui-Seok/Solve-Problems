n, m = map(int, input().split())
chess = [list(input()) for _ in range(n)]
change_value = 64
start_x, start_y = 0, 0

for i in range(n-8+1):
    for j in range(m-8+1):
        cnt = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if x % 2 == 0 and y % 2 == 1:
                    if chess[x][y] == 'W':
                        cnt += 1
                elif x % 2 == 0 and y % 2 == 0:
                    if chess[x][y] == 'B':
                        cnt += 1
                elif x % 2 == 1 and y % 2 == 1:
                    if chess[x][y] == 'B':
                        cnt += 1
                elif x % 2 == 1 and y % 2 == 0:
                    if chess[x][y] == 'W':
                        cnt += 1
        if min(cnt, 64-cnt) < change_value:
            change_value = min(cnt, 64-cnt)

print(change_value)