n, r, c = map(int, input().split())

def get_nums(dims, location, answer):
    if dims == 1:
        x, y = location
        answer += 2*x + y
        return answer
    else:
        repeat_num = 4 ** (dims-1)
        x, y = location
        lc_x = x // 2 ** (dims-1)
        lc_y = y // 2 ** (dims-1)
        # 좌측상단
        if lc_x == 0 and lc_y == 0:
            init_num = repeat_num * 0
            answer += init_num
            return get_nums(dims-1, (x, y), answer)
        # 좌측하단
        elif lc_x == 1 and lc_y == 0:
            init_num = repeat_num * 2
            x -= 2 ** (dims-1)
            answer += init_num
            return get_nums(dims-1, (x, y), answer)
        # 우측상단
        elif lc_x == 0 and lc_y == 1:
            init_num = repeat_num * 1
            y -= 2 ** (dims-1)
            answer += init_num
            return get_nums(dims-1, (x, y), answer)
        # 우측하단
        elif lc_x == 1 and lc_y == 1:
            init_num = repeat_num * 3
            x -= 2 ** (dims-1)
            y -= 2 ** (dims-1)
            answer += init_num
            return get_nums(dims-1, (x, y), answer)

answer = get_nums(n, (r, c), 0)
print(answer)