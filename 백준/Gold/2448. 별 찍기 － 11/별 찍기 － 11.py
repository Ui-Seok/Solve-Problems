import sys
ipnut = sys.stdin.readline

n = int(input())
star_map = [[" "] * 2 * n for _ in range(n)]

def star(x, y, m):
    global star_map
    if m == 3:
        for i in range(3):
            for j in range(i + 1):
                star_map[x + i][y + j] = star_map[x + i][y - j] = "*"
        star_map[x + 1][y] = " "
        return

    h = m // 2
    star(x, y, h)
    star(x + h, y - h, h)
    star(x + h, y + h, h)

star(0, n - 1, n)

for i in range(n):
    print("".join(star_map[i]))
