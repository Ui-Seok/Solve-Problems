n = int(input())
box = {}
whole_map = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, n + 1):
    x1, y1, w, h = map(int, input().split())
    x2 = x1 + w - 1
    y2 = y1 + h - 1
    box[i] = [x1, y1, x2, y2]
    for x in range(w):
        for y in range(h):
            whole_map[x1 + x][y1 + y] = i

for i in range(1, n + 1):
    area = 0
    x1, y1, x2, y2 = box[i]
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if whole_map[x][y] == i:
                area += 1
    print(area)