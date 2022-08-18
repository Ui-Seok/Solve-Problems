for tc in range(1, 11):
    t = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    end_line = ladder[-1]
    end = end_line.index(2)
    x, y = 98, end

    before = 'up'

    while x != 0:
        if before == 'left':
            if ladder[x - 1][y] == 1:
                x -= 1
                before = 'up'
            else:
                y -= 1
        elif before == 'right':
            if ladder[x - 1][y] == 1:
                x -= 1
                before = 'up'
            else:
                y += 1
        else:
            if (y > 0) and (ladder[x][y - 1] == 1):
                y -= 1
                before = 'left'
            elif (y < 99) and (ladder[x][y + 1] == 1):
                y += 1
                before = 'right'
            else:
                x -= 1
    print('#{} {}'.format(tc, y))