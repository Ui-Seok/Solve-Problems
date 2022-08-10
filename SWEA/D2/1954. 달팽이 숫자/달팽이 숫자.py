t = int(input())

for tmp in range(t):
    n = int(input())

    bounds = n // 2 + n % 2
    array = [[0] * n for _ in range(n)]
    wid = [1, 0, -1, 0]
    hei = [0, 1, 0, -1]
    cnt, pl_cnt = 0, 0
    if n == 1:
        print(f'#{tmp + 1}')
        print(1)
    else:
        for bound in range(bounds):
            x, y = bound, bound
            i = 0
            while array[y][x] == False:
                cnt += 1
                array[y][x] += cnt
                x += wid[i]
                y += hei[i]
                pl_cnt += 1
                if pl_cnt == (n - 1):
                    pl_cnt = 0
                    i += 1
            n -= 2
        print(f'#{tmp + 1}')
        for arr in array:
            print(*arr)